---
title: Plugins для инструментов
source_url: https://docs.openclaw.ai/ru/plugins/tool-plugins
scraped_at: 2026-06-29
---

CapabilitiesBuilding plugins

Плагины инструментов добавляют в OpenClaw инструменты, вызываемые агентом, без добавления канала, поставщика модели, hook, сервиса или backend настройки. Используйте `defineToolPlugin`, когда плагин владеет фиксированным списком инструментов и вы хотите, чтобы OpenClaw сгенерировал метаданные манифеста, которые сохраняют эти инструменты доступными для обнаружения без загрузки runtime-кода.

Рекомендуемый процесс:

  1. Создайте каркас пакета с помощью `openclaw plugins init`.
  2. Напишите инструменты с `defineToolPlugin`.
  3. Соберите JavaScript.
  4. Сгенерируйте метаданные `openclaw.plugin.json` и `package.json` с помощью `openclaw plugins build`.
  5. Проверьте сгенерированные метаданные перед публикацией или установкой.


Для плагинов поставщиков, каналов, hook, сервисов или плагинов со смешанными возможностями начните с [Создание плагинов](</ru/plugins/building-plugins>), [Плагины каналов](</ru/plugins/sdk-channel-plugins>) или [Плагины поставщиков](</ru/plugins/sdk-provider-plugins>).

## Требования

  * Node >= 22.
  * Вывод пакета TypeScript ESM.
  * `typebox` для схем конфигурации и параметров инструментов.
  * `openclaw >=2026.5.17`, первая версия OpenClaw, которая экспортирует `openclaw/plugin-sdk/tool-plugin`.
  * Корень пакета, который может поставлять `dist/`, `openclaw.plugin.json` и `package.json`.


Сгенерированный плагин импортирует `typebox` во время выполнения, поэтому держите `typebox` в `dependencies`, а не только в `devDependencies`.

## Быстрый старт

Создайте новый пакет плагина:

bashCopy code
[code]
    openclaw plugins init stock-quotes --name "Stock Quotes"cd stock-quotesnpm installnpm run plugin:buildnpm run plugin:validatenpm test
[/code]

Каркас создает:

  * `src/index.ts`: entry `defineToolPlugin` с инструментом `echo`.
  * `src/index.test.ts`: небольшой тест метаданных.
  * `tsconfig.json`: вывод TypeScript NodeNext в `dist/`.
  * `package.json`: скрипты, runtime-зависимости и `openclaw.extensions: ["./dist/index.js"]`.
  * `openclaw.plugin.json`: сгенерированные метаданные манифеста для начального инструмента.


Ожидаемый вывод проверки:

textCopy code
[code]
    Plugin stock-quotes is valid.
[/code]

## Написание инструмента

`defineToolPlugin` принимает идентификацию плагина, необязательную схему конфигурации и статический список инструментов. Типы параметров и конфигурации выводятся из схем TypeBox.

typescriptCopy code
[code]
      export default defineToolPlugin({  id: "stock-quotes",  name: "Stock Quotes",  description: "Fetch stock quote snapshots.",  configSchema: Type.Object({    apiKey: Type.Optional(Type.String({ description: "Quote API key." })),    baseUrl: Type.Optional(Type.String({ description: "Quote API base URL." })),  }),  tools: (tool) => [    tool({      name: "stock_quote",      label: "Stock Quote",      description: "Fetch a stock quote snapshot.",      parameters: Type.Object({        symbol: Type.String({ description: "Ticker symbol, for example OPEN." }),      }),      async execute({ symbol }, config, context) {        context.signal?.throwIfAborted();        return {          symbol: symbol.toUpperCase(),          configured: Boolean(config.apiKey),          baseUrl: config.baseUrl ?? "https://api.example.com",        };      },    }),  ],});
[/code]

Имена инструментов являются стабильным API. Выбирайте имена, которые уникальны, написаны в нижнем регистре и достаточно конкретны, чтобы избежать конфликтов с инструментами core или другими плагинами.

## Необязательные и фабричные инструменты

Установите `optional: true`, когда пользователи должны явно добавить инструмент в allowlist, прежде чем он будет отправлен модели:

typescriptCopy code
[code]
    tool({  name: "workflow_run",  description: "Run an external workflow.",  parameters: Type.Object({ goal: Type.String() }),  optional: true,  execute: ({ goal }) => ({ queued: true, goal }),});
[/code]

`openclaw plugins build` записывает соответствующую запись манифеста `toolMetadata.<tool>.optional`, чтобы OpenClaw мог обнаружить инструмент без загрузки runtime-кода плагина.

Используйте `factory`, когда инструменту нужен runtime-контекст инструмента, прежде чем его можно будет создать. Фабрика сохраняет метаданные статическими, позволяя инструменту отказаться от конкретного запуска, проверить состояние sandbox или привязать runtime-помощники.

typescriptCopy code
[code]
    tool({  name: "local_workflow",  description: "Run a local workflow outside sandboxed sessions.",  parameters: Type.Object({ goal: Type.String() }),  optional: true,  factory({ api, toolContext }) {    if (toolContext.sandboxed) {      return null;    }    return createLocalWorkflowTool(api);  },});
[/code]

Фабрики по-прежнему предназначены для фиксированных имен инструментов. Используйте `definePluginEntry` напрямую, когда плагин вычисляет имена инструментов динамически или объединяет инструменты с hook, сервисами, поставщиками, командами или другими runtime-поверхностями.

## Возвращаемые значения

`defineToolPlugin` оборачивает простые возвращаемые значения в формат результата инструмента OpenClaw:

  * Верните строку, когда модель должна увидеть именно этот текст.
  * Верните JSON-совместимое значение, когда вы хотите, чтобы модель увидела форматированный JSON, а OpenClaw сохранил исходное значение в `details`.

typescriptCopy code
[code]
    tool({  name: "echo_text",  description: "Echo input text.",  parameters: Type.Object({    input: Type.String(),  }),  execute: ({ input }) => input,});
[/code]

typescriptCopy code
[code]
    tool({  name: "echo_json",  description: "Echo input as structured JSON.",  parameters: Type.Object({    input: Type.String(),  }),  execute: ({ input }) => ({ input, length: input.length }),});
[/code]

Используйте фабричный инструмент, когда нужно вернуть собственный `AgentToolResult` или повторно использовать существующую реализацию `api.registerTool`. Используйте `definePluginEntry` вместо `defineToolPlugin`, когда вам нужны полностью динамические инструменты или смешанные возможности плагина.

## Конфигурация

`configSchema` необязательна. Если вы ее опустите, OpenClaw использует строгую схему пустого объекта, и сгенерированный манифест все равно будет включать `configSchema`.

typescriptCopy code
[code]
    export default defineToolPlugin({  id: "no-config-tools",  name: "No Config Tools",  description: "Adds tools that do not need configuration.",  tools: () => [],});
[/code]

Когда вы включаете `configSchema`, второй аргумент `execute` типизируется на основе схемы:

typescriptCopy code
[code]
    const configSchema = Type.Object({  apiKey: Type.String(),}); export default defineToolPlugin({  id: "configured-tools",  name: "Configured Tools",  description: "Adds configured tools.",  configSchema,  tools: (tool) => [    tool({      name: "configured_ping",      description: "Check whether configuration is available.",      parameters: Type.Object({}),      execute: (_params, config) => ({ hasKey: config.apiKey.length > 0 }),    }),  ],});
[/code]

OpenClaw читает конфигурацию плагина из записи плагина в конфигурации Gateway. Не зашивайте секреты в исходный код или примеры в документации. Используйте конфигурацию, переменные окружения или SecretRefs согласно модели безопасности плагина.

## Сгенерированные метаданные

OpenClaw обнаруживает установленные плагины по холодным метаданным. Он должен уметь читать манифест плагина до импорта runtime-кода плагина. Поэтому `defineToolPlugin` предоставляет статические метаданные, а `openclaw plugins build` записывает эти метаданные в пакет.

Запускайте генератор после изменения id, имени, описания, схемы конфигурации, активации или имен инструментов плагина:

bashCopy code
[code]
    npm run buildopenclaw plugins build --entry ./dist/index.js
[/code]

Для плагина с одним инструментом сгенерированный манифест выглядит так:

jsonCopy code
[code]
    {  "id": "stock-quotes",  "name": "Stock Quotes",  "description": "Fetch stock quote snapshots.",  "version": "0.1.0",  "configSchema": {    "type": "object",    "additionalProperties": false,    "properties": {}  },  "activation": {    "onStartup": true  },  "contracts": {    "tools": ["stock_quote"]  }}
[/code]

`contracts.tools` — важный контракт обнаружения. Он сообщает OpenClaw, какой плагин владеет каждым инструментом, без загрузки runtime-кода каждого установленного плагина. Если манифест устарел, инструмент может отсутствовать при обнаружении или неправильный плагин может быть указан как причина ошибки регистрации.

## Метаданные пакета

Для простого процесса tool-plugin `openclaw plugins build` выравнивает `package.json` с выбранной единственной runtime-точкой входа:

jsonCopy code
[code]
    {  "type": "module",  "files": ["dist", "openclaw.plugin.json", "README.md"],  "dependencies": {    "typebox": "^1.1.38"  },  "peerDependencies": {    "openclaw": ">=2026.5.17"  },  "openclaw": {    "extensions": ["./dist/index.js"]  }}
[/code]

Используйте собранный JavaScript, например `./dist/index.js`, для установленных пакетов. Исходные entry полезны при разработке в workspace, но опубликованные пакеты не должны зависеть от runtime-загрузки TypeScript.

## Проверка в CI

Используйте `plugins build --check`, чтобы CI падал, когда сгенерированные метаданные устарели, без перезаписи файлов:

bashCopy code
[code]
    npm run buildopenclaw plugins build --entry ./dist/index.js --checkopenclaw plugins validate --entry ./dist/index.jsnpm test
[/code]

`plugins validate` проверяет, что:

  * `openclaw.plugin.json` существует и проходит обычный загрузчик манифеста.
  * Текущая entry экспортирует метаданные `defineToolPlugin`.
  * Сгенерированные поля манифеста соответствуют метаданным entry.
  * `contracts.tools` соответствует объявленным именам инструментов.
  * `package.json` указывает `openclaw.extensions` на выбранную runtime-entry.


## Локальная установка и проверка

Из отдельного checkout OpenClaw или установленного CLI установите путь пакета:

bashCopy code
[code]
    openclaw plugins install ./stock-quotesopenclaw plugins inspect stock-quotes --runtime
[/code]

Для пакетного smoke сначала упакуйте и установите tarball:

bashCopy code
[code]
    npm packopenclaw plugins install npm-pack:./openclaw-plugin-stock-quotes-0.1.0.tgzopenclaw plugins inspect stock-quotes --runtime --json
[/code]

После установки запустите или перезапустите Gateway и попросите агента использовать инструмент. Если вы отлаживаете видимость инструмента, проверьте runtime плагина и эффективный каталог инструментов перед изменением кода.

## Публикация

Публикуйте через ClawHub, когда пакет готов:

bashCopy code
[code]
    clawhub package publish your-org/stock-quotes --dry-runclawhub package publish your-org/stock-quotes
[/code]

Установите с явным локатором ClawHub:

bashCopy code
[code]
    openclaw plugins install clawhub:your-org/stock-quotes
[/code]

Простые npm package specs остаются поддерживаемыми во время перехода при запуске, но ClawHub является предпочтительной поверхностью обнаружения и распространения для плагинов OpenClaw.

## Устранение неполадок

### `plugin entry not found: ./dist/index.js`

Выбранный entry-файл не существует. Запустите `npm run build`, затем повторно выполните `openclaw plugins build --entry ./dist/index.js` или `openclaw plugins validate --entry ./dist/index.js`.

### `plugin entry does not expose defineToolPlugin metadata`

Entry не экспортировал значение, созданное `defineToolPlugin`. Проверьте, что default export модуля является результатом `defineToolPlugin(...)`, или передайте правильную entry с `--entry`.

### `openclaw.plugin.json generated metadata is stale`

Манифест больше не соответствует метаданным entry. Запустите:

bashCopy code
[code]
    npm run buildopenclaw plugins build --entry ./dist/index.js
[/code]

Закоммитьте изменения как `openclaw.plugin.json`, так и `package.json`.

### `package.json openclaw.extensions must include ./dist/index.js`

Метаданные пакета указывают на другую runtime-entry. Запустите `openclaw plugins build --entry ./dist/index.js`, чтобы генератор выровнял метаданные пакета с entry, которую вы собираетесь поставлять.

### `Cannot find package 'typebox'`

Собранный плагин импортирует `typebox` во время выполнения. Держите `typebox` в `dependencies`, переустановите зависимости пакета, пересоберите и повторно выполните проверку.

### Инструмент не появляется после установки

Проверьте следующее по порядку:

  1. `openclaw plugins inspect <plugin-id> --runtime`
  2. `openclaw plugins validate --root <plugin-root> --entry ./dist/index.js`
  3. В `openclaw.plugin.json` есть `contracts.tools` с ожидаемыми именами инструментов.
  4. В `package.json` есть `openclaw.extensions: ["./dist/index.js"]`.
  5. Gateway был перезапущен или перезагружен после установки плагина.


## См. также

  * [Создание плагинов](</ru/plugins/building-plugins>)
  * [Точки входа плагинов](</ru/plugins/sdk-entrypoints>)
  * [Подпути Plugin SDK](</ru/plugins/sdk-subpaths>)
  * [Манифест плагина](</ru/plugins/manifest>)
  * [CLI плагинов](</ru/cli/plugins>)
  * [Публикация ClawHub](</ru/clawhub/publishing>)


Was this useful?YesNo

Open issue