---
title: IPC macOS
source_url: https://docs.openclaw.ai/uk/platforms/mac/xpc
scraped_at: 2026-05-25
---

# Архітектура IPC macOS OpenClaw

**Поточна модель:** локальний Unix socket з’єднує **службу хоста node** із **застосунком macOS** для погоджень exec і `system.run`. Для перевірок виявлення/підключення існує CLI налагодження `openclaw-mac`; дії агента, як і раніше, проходять через Gateway WebSocket і `node.invoke`. Автоматизація UI використовує PeekabooBridge.

## Цілі

  * Єдиний екземпляр GUI-застосунку, який володіє всією роботою, пов’язаною з TCC (сповіщення, screen recording, мікрофон, мовлення, AppleScript).
  * Невелика поверхня для автоматизації: команди Gateway + node, а також PeekabooBridge для автоматизації UI.
  * Передбачувані дозволи: завжди той самий підписаний bundle ID, запущений через launchd, щоб дозволи TCC зберігалися.


## Як це працює

### Gateway + транспорт node

  * Застосунок запускає Gateway (локальний режим) і підключається до нього як node.
  * Дії агента виконуються через `node.invoke` (наприклад, `system.run`, `system.notify`, `canvas.*`).


### Служба node + IPC застосунку

  * Безголова служба хоста node підключається до Gateway WebSocket.
  * Запити `system.run` переспрямовуються до застосунку macOS через локальний Unix socket.
  * Застосунок виконує exec у контексті UI, за потреби показує запит і повертає вивід.


Діаграма (SCI):

CodeCopy code
[code]
    Agent -> Gateway -> Node Service (WS)                      |  IPC (UDS + token + HMAC + TTL)                      v                  Mac App (UI + TCC + system.run)
[/code]

### PeekabooBridge (автоматизація UI)

  * Автоматизація UI використовує окремий UNIX socket з назвою `bridge.sock` і JSON-протокол PeekabooBridge.
  * Порядок пріоритету хоста (на боці клієнта): Peekaboo.app → Claude.app → OpenClaw.app → локальне виконання.
  * Безпека: хости bridge вимагають дозволеного TeamID; захисний обхід same-UID лише для DEBUG контролюється через `PEEKABOO_ALLOW_UNSIGNED_SOCKET_CLIENTS=1` (угода Peekaboo).
  * Докладніше див.: [Використання PeekabooBridge](</uk/platforms/mac/peekaboo>).


## Операційні потоки

  * Перезапуск/перезбірка: `SIGN_IDENTITY="Apple Development: &lt;Developer Name&gt; (&lt;TEAMID&gt;)" scripts/restart-mac.sh`
    * Завершує наявні екземпляри
    * Виконує збірку та пакування Swift
    * Записує/ініціалізує/перезапускає LaunchAgent
  * Єдиний екземпляр: застосунок завершується раніше, якщо вже працює інший екземпляр із тим самим bundle ID.


## Примітки щодо захисту

  * Надавайте перевагу вимозі збігу TeamID для всіх привілейованих поверхонь.
  * PeekabooBridge: `PEEKABOO_ALLOW_UNSIGNED_SOCKET_CLIENTS=1` (лише DEBUG) може дозволяти виклики від того самого UID для локальної розробки.
  * Усі комунікації залишаються лише локальними; мережеві sockets не відкриваються.
  * Запити TCC надходять лише від bundle GUI-застосунку; зберігайте підписаний bundle ID стабільним між перезбірками.
  * Захист IPC: режим socket `0600`, token, перевірки peer-UID, challenge/response HMAC, короткий TTL.


## Пов’язане

  * [Застосунок macOS](</uk/platforms/macos>)
  * [Потік IPC macOS (погодження Exec)](</uk/tools/exec-approvals-advanced#macos-ipc-flow>)


Was this useful?YesNo