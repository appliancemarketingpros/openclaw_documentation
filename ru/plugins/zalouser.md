---
title: Персональный Plugin Zalo
source_url: https://docs.openclaw.ai/ru/plugins/zalouser
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

Поддержка Zalo Personal для OpenClaw через Plugin с использованием нативного `zca-js` для автоматизации обычной учетной записи пользователя Zalo.

## Именование

Идентификатор канала — `zalouser`, чтобы явно указать, что он автоматизирует **личную учетную запись пользователя Zalo** (неофициально). Мы оставляем `zalo` зарезервированным для возможной будущей официальной интеграции с API Zalo.

## Где он запускается

Этот Plugin запускается **внутри процесса Gateway**.

Если вы используете удаленный Gateway, установите и настройте его на **машине, где запущен Gateway** , затем перезапустите Gateway.

Внешний CLI-бинарник `zca`/`openzca` не требуется.

## Установка

### Вариант A: установка из npm

bashCopy code
[code]
    openclaw plugins install @openclaw/zalouser
[/code]

Используйте пакет без указания версии, чтобы следовать текущему официальному релизному тегу. Закрепляйте точную версию только тогда, когда вам нужна воспроизводимая установка.

После этого перезапустите Gateway.

### Вариант B: установка из локальной папки (разработка)

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/zalouser-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

После этого перезапустите Gateway.

## Конфигурация

Конфигурация канала находится в `channels.zalouser` (а не в `plugins.entries.*`):

json5Copy code
[code]
    {  channels: {    zalouser: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

## CLI

bashCopy code
[code]
    openclaw channels login --channel zalouseropenclaw channels logout --channel zalouseropenclaw channels status --probeopenclaw message send --channel zalouser --target <threadId> --message "Hello from OpenClaw"openclaw directory peers list --channel zalouser --query "name"
[/code]

## Инструмент агента

Имя инструмента: `zalouser`

Действия: `send`, `image`, `link`, `friends`, `groups`, `me`, `status`

Действия сообщений канала также поддерживают `react` для реакций на сообщения.

## Связанное

  * [Создание Plugin](</ru/plugins/building-plugins>)
  * [ClawHub](</ru/clawhub>)


Was this useful?YesNo

Open issue