---
title: Gateway на macOS
source_url: https://docs.openclaw.ai/ru/platforms/mac/bundled-gateway
scraped_at: 2026-06-29
---

PlatformsmacOS companion app

OpenClaw.app больше не включает в комплект Node/Bun или среду выполнения Gateway. Приложение macOS ожидает **внешнюю** установку CLI `openclaw`, не запускает Gateway как дочерний процесс и управляет пользовательской службой launchd, чтобы Gateway оставался запущенным (или подключается к существующему локальному Gateway, если он уже работает).

## Установка CLI (требуется для локального режима)

Node 24 — среда выполнения по умолчанию на Mac. Node 22 LTS, сейчас `22.19+`, по-прежнему работает для совместимости. Затем установите `openclaw` глобально:

bashCopy code
[code]
    npm install -g openclaw@<version>
[/code]

Кнопка **Установить CLI** в приложении macOS запускает тот же поток глобальной установки, который приложение использует внутренне: сначала предпочитается npm, затем pnpm, затем bun, если это единственный обнаруженный менеджер пакетов. Node остается рекомендуемой средой выполнения Gateway.

## Launchd (Gateway как LaunchAgent)

Метка:

  * `ai.openclaw.gateway` (или `ai.openclaw.<profile>`; устаревшие `com.openclaw.*` могут оставаться)


Расположение plist (для пользователя):

  * `~/Library/LaunchAgents/ai.openclaw.gateway.plist` (или `~/Library/LaunchAgents/ai.openclaw.<profile>.plist`)


Менеджер:

  * Приложение macOS управляет установкой/обновлением LaunchAgent в локальном режиме.
  * CLI также может установить его: `openclaw gateway install`.


Поведение:

  * «OpenClaw активен» включает/отключает LaunchAgent.
  * Выход из приложения **не** останавливает gateway (launchd поддерживает его работу).
  * Если Gateway уже работает на настроенном порту, приложение подключается к нему вместо запуска нового.


Журналирование:

  * stdout launchd: `~/Library/Logs/openclaw/gateway.log` (профили используют `gateway-<profile>.log`)
  * stderr launchd: подавляется


## Совместимость версий

Приложение macOS проверяет версию gateway относительно собственной версии. Если они несовместимы, обновите глобальный CLI до версии приложения.

## Каталог состояния в macOS

Храните состояние OpenClaw на локальном диске без синхронизации. Избегайте iCloud Drive и других папок с облачной синхронизацией, потому что задержки синхронизации и блокировки файлов могут влиять на сеансы, учетные данные и состояние Gateway.

Задавайте `OPENCLAW_STATE_DIR` локальным путем только когда нужно переопределение. `openclaw doctor` предупреждает о распространенных путях состояния с облачной синхронизацией и рекомендует вернуться к локальному хранилищу. См. [переменные среды](</ru/help/environment#path-related-env-vars>) и [Doctor](</ru/gateway/doctor>).

## Отладка подключения приложения

Используйте отладочный CLI macOS из исходного checkout, чтобы выполнить ту же логику WebSocket-рукопожатия и обнаружения Gateway, которую использует приложение:

bashCopy code
[code]
    cd apps/macosswift run openclaw-mac connect --jsonswift run openclaw-mac discover --timeout 3000 --json
[/code]

`connect` принимает `--url`, `--token`, `--timeout` и `--json`. `discover` принимает `--timeout`, `--json` и `--include-local`. Сравните вывод обнаружения с `openclaw gateway discover --json`, когда нужно отделить обнаружение CLI от проблем подключения на стороне приложения.

## Дымовая проверка

bashCopy code
[code]
    openclaw --version OPENCLAW_SKIP_CHANNELS=1 \OPENCLAW_SKIP_CANVAS_HOST=1 \openclaw gateway --port 18999 --bind loopback
[/code]

Затем:

bashCopy code
[code]
    openclaw gateway call health --url ws://127.0.0.1:18999 --timeout 3000
[/code]

## См. также

  * [приложение macOS](</ru/platforms/macos>)
  * [операционный справочник Gateway](</ru/gateway>)


Was this useful?YesNo

Open issue