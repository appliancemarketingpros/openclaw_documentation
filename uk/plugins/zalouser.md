---
title: Особистий Plugin Zalo
source_url: https://docs.openclaw.ai/uk/plugins/zalouser
scraped_at: 2026-05-25
---

Підтримка Zalo Personal для OpenClaw через плагін із використанням нативного `zca-js` для автоматизації звичайного облікового запису користувача Zalo.

## Іменування

Ідентифікатор каналу — `zalouser`, щоб явно вказати, що це автоматизує **особистий обліковий запис користувача Zalo** (неофіційно). Ми залишаємо `zalo` зарезервованим для потенційної майбутньої офіційної інтеграції з Zalo API.

## Де це працює

Цей плагін працює **всередині процесу Gateway**.

Якщо ви використовуєте віддалений Gateway, установіть/налаштуйте його на **машині, де запущено Gateway** , а потім перезапустіть Gateway.

Зовнішній CLI-бінарник `zca`/`openzca` не потрібен.

## Установлення

### Варіант A: установлення з npm

bashCopy code
[code]
    openclaw plugins install @openclaw/zalouser
[/code]

Використовуйте пакет без префіксів, щоб стежити за поточним офіційним тегом релізу. Закріплюйте точну версію лише тоді, коли потрібне відтворюване встановлення.

Після цього перезапустіть Gateway.

### Варіант B: установлення з локальної папки (dev)

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/zalouser-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

Після цього перезапустіть Gateway.

## Конфігурація

Конфігурація каналу розміщується в `channels.zalouser` (а не в `plugins.entries.*`):

json5Copy code
[code]
    {  channels: {    zalouser: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

## CLI

bashCopy code
[code]
    openclaw channels login --channel zalouseropenclaw channels logout --channel zalouseropenclaw channels status --probeopenclaw message send --channel zalouser --target <threadId> --message "Hello from OpenClaw"openclaw directory peers list --channel zalouser --query "name"
[/code]

## Інструмент агента

Назва інструмента: `zalouser`

Дії: `send`, `image`, `link`, `friends`, `groups`, `me`, `status`

Дії повідомлень каналу також підтримують `react` для реакцій на повідомлення.

## Пов’язане

  * [Створення плагінів](</uk/plugins/building-plugins>)
  * [ClawHub](</uk/clawhub>)


Was this useful?YesNo