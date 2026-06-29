---
title: Межпроцессное взаимодействие в macOS
source_url: https://docs.openclaw.ai/ru/platforms/mac/xpc
scraped_at: 2026-06-29
---

PlatformsmacOS companion app

# Архитектура IPC OpenClaw для macOS

**Текущая модель:** локальный Unix-сокет соединяет **хост-службу node** с **приложением macOS** для разрешений exec и `system.run`. Существует отладочный CLI `openclaw-mac` для проверок обнаружения и подключения; действия агента по-прежнему проходят через WebSocket Gateway и `node.invoke`. Автоматизация UI использует PeekabooBridge.

## Цели

  * Единый экземпляр GUI-приложения, которому принадлежат все работы, связанные с TCC (уведомления, запись экрана, микрофон, речь, AppleScript).
  * Небольшая поверхность для автоматизации: Gateway и команды node, плюс PeekabooBridge для автоматизации UI.
  * Предсказуемые разрешения: всегда один и тот же подписанный ID бандла, запущенный через launchd, чтобы разрешения TCC сохранялись.


## Как это работает

### Транспорт Gateway + node

  * Приложение запускает Gateway (локальный режим) и подключается к нему как node.
  * Действия агента выполняются через `node.invoke` (например, `system.run`, `system.notify`, `canvas.*`).
  * Распространенные команды Mac node включают `canvas.*`, `camera.snap`, `camera.clip`, `screen.snapshot`, `screen.record`, `system.run` и `system.notify`.
  * Node сообщает карту `permissions`, чтобы агенты могли видеть, доступен ли доступ к экрану, камере, микрофону, речи, автоматизации или функциям доступности.


### Служба node + IPC приложения

  * Безголовая хост-служба node подключается к WebSocket Gateway.
  * Запросы `system.run` перенаправляются в приложение macOS через локальный Unix-сокет.
  * Приложение выполняет exec в контексте UI, при необходимости запрашивает подтверждение и возвращает вывод.


Диаграмма (SCI):

CodeCopy code
[code]
    Agent -> Gateway -> Node Service (WS)                      |  IPC (UDS + token + HMAC + TTL)                      v                  Mac App (UI + TCC + system.run)
[/code]

### PeekabooBridge (автоматизация UI)

  * Автоматизация UI использует отдельный UNIX-сокет с именем `bridge.sock` и JSON-протокол PeekabooBridge.
  * Порядок предпочтения хостов (на стороне клиента): Peekaboo.app → Claude.app → OpenClaw.app → локальное выполнение.
  * Безопасность: хосты bridge требуют разрешенный TeamID; DEBUG-only аварийный выход для того же UID защищен `PEEKABOO_ALLOW_UNSIGNED_SOCKET_CLIENTS=1` (соглашение Peekaboo).
  * См. подробности: [использование PeekabooBridge](</ru/platforms/mac/peekaboo>).


## Операционные потоки

  * Перезапуск/пересборка: `SIGN_IDENTITY="Apple Development: &lt;Developer Name&gt; (&lt;TEAMID&gt;)" scripts/restart-mac.sh`
    * Завершает существующие экземпляры
    * Выполняет Swift build + package
    * Записывает/инициализирует/перезапускает LaunchAgent
  * Единый экземпляр: приложение завершает работу на раннем этапе, если уже запущен другой экземпляр с тем же ID бандла.


## Заметки по усилению безопасности

  * Предпочтительно требовать совпадение TeamID для всех привилегированных поверхностей.
  * PeekabooBridge: `PEEKABOO_ALLOW_UNSIGNED_SOCKET_CLIENTS=1` (только DEBUG) может разрешать вызовы с тем же UID для локальной разработки.
  * Вся коммуникация остается только локальной; сетевые сокеты не открываются.
  * Запросы TCC исходят только от бандла GUI-приложения; сохраняйте стабильный подписанный ID бандла между пересборками.
  * Усиление IPC: режим сокета `0600`, токен, проверки peer-UID, challenge/response через HMAC, короткий TTL.


## Связанные материалы

  * [Приложение macOS](</ru/platforms/macos>)
  * [Поток IPC macOS (разрешения exec)](</ru/tools/exec-approvals-advanced#macos-ipc-flow>)


Was this useful?YesNo

Open issue