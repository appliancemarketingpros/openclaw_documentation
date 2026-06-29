---
title: Создание plugins
source_url: https://docs.openclaw.ai/ru/plugins/building-plugins
scraped_at: 2026-06-29
---

CapabilitiesBuilding plugins

Plugins расширяют OpenClaw без изменения core. Plugin может добавить канал обмена сообщениями, поставщика моделей, локальный CLI-бэкенд, агентский инструмент, hook, поставщика медиа или другую возможность, принадлежащую Plugin.

Вам не нужно добавлять внешний Plugin в репозиторий OpenClaw. Опубликуйте пакет в [ClawHub](</ru/clawhub>), и пользователи установят его с помощью:

bashCopy code
[code]
    openclaw plugins install clawhub:<package-name>
[/code]

Спецификации пакетов без префикса по-прежнему устанавливаются из npm во время перехода при запуске. Используйте префикс `clawhub:`, когда вам нужно разрешение через ClawHub.

## Требования

  * Используйте Node 22.19 или новее и менеджер пакетов, например `npm` или `pnpm`.
  * Будьте знакомы с TypeScript ESM-модулями.
  * Для работы над встроенным Plugin внутри репозитория клонируйте репозиторий и выполните `pnpm install`. Разработка Plugin из исходного checkout поддерживает только pnpm, потому что OpenClaw загружает встроенные Plugins из workspace-пакетов `extensions/*`.


## Выберите форму Plugin

[**Plugin канала** Подключите OpenClaw к платформе обмена сообщениями. ](</ru/plugins/sdk-channel-plugins>) [**Plugin поставщика** Добавьте поставщика моделей, медиа, поиска, fetch, речи или realtime. ](</ru/plugins/sdk-provider-plugins>) [**Plugin CLI-бэкенда** Запускайте локальный AI CLI через fallback моделей OpenClaw. ](</ru/plugins/cli-backend-plugins>) [**Plugin инструментов** Регистрируйте агентские инструменты. ](</ru/plugins/tool-plugins>)

## Быстрый старт

Создайте минимальный Plugin инструментов, зарегистрировав один обязательный агентский инструмент. Это самая короткая полезная форма Plugin, которая показывает пакет, манифест, точку входа и локальное подтверждение.

* ### Создайте метаданные пакета

package.jsonCopy code
[code]
    {"name": "@myorg/openclaw-my-plugin","version": "1.0.0","type": "module","openclaw": {"extensions": ["./index.ts"],"compat": {"pluginApi": ">=2026.3.24-beta.2","minGatewayVersion": "2026.3.24-beta.2"},"build": {"openclawVersion": "2026.3.24-beta.2","pluginSdkVersion": "2026.3.24-beta.2"}}}
[/code]

openclaw.plugin.jsonCopy code
[code]
    {"id": "my-plugin","name": "My Plugin","description": "Adds a custom tool to OpenClaw","contracts": {"tools": ["my_tool"]},"activation": {"onStartup": true},"configSchema": {"type": "object","additionalProperties": false}}
[/code]

Опубликованные внешние Plugins должны указывать runtime-точки входа на собранные JavaScript-файлы. Полный контракт точки входа см. в [точках входа SDK](</ru/plugins/sdk-entrypoints>).

Каждому Plugin нужен манифест, даже если у него нет конфигурации. Runtime-инструменты должны быть указаны в `contracts.tools`, чтобы OpenClaw мог обнаруживать владельца без предварительной загрузки runtime каждого Plugin. Задавайте `activation.onStartup` осознанно. Этот пример запускается при запуске Gateway.

Поверхности Plugin, доверенные host, также ограничиваются манифестом и требуют явного включения для установленных Plugins. Если установленный Plugin регистрирует `api.registerAgentToolResultMiddleware(...)`, объявите каждый целевой runtime в `contracts.agentToolResultMiddleware`. Если он регистрирует `api.registerTrustedToolPolicy(...)`, объявите каждый id политики в `contracts.trustedToolPolicies`. Эти объявления синхронизируют проверку при установке и регистрацию runtime.

Все поля манифеста см. в [манифесте Plugin](</ru/plugins/manifest>).

* ### Зарегистрируйте инструмент

index.tsCopy code
[code]
    import { Type } from "typebox";import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry"; export default definePluginEntry({  id: "my-plugin",  name: "My Plugin",  description: "Adds a custom tool to OpenClaw",  register(api) {    api.registerTool({      name: "my_tool",      description: "Echo one input value",      parameters: Type.Object({ input: Type.String() }),      async execute(_id, params) {        return {          content: [{ type: "text", text: `Got: ${params.input}` }],        };      },    });  },});
[/code]

Используйте `definePluginEntry` для Plugins, не являющихся каналами. Plugins каналов используют `defineChannelPluginEntry`.

* ### Проверьте runtime

Для установленного или внешнего Plugin проверьте загруженный runtime:

bashCopy code
[code]
    openclaw plugins inspect my-plugin --runtime --json
[/code]

Если Plugin регистрирует CLI-команду, также запустите эту команду. Например, demo-команда должна иметь подтверждение выполнения, такое как `openclaw demo-plugin ping`.

Для встроенного Plugin в этом репозитории OpenClaw обнаруживает пакеты Plugin из исходного checkout в workspace `extensions/*`. Запустите ближайший целевой тест:

bashCopy code
[code]
    pnpm test -- extensions/my-plugin/pnpm check
[/code]

* ### Опубликуйте

Проверьте пакет перед публикацией:

bashCopy code
[code]
    clawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-plugin
[/code]

Канонические фрагменты ClawHub находятся в `docs/snippets/plugin-publish/`.

* ### Установите

Установите опубликованный пакет через ClawHub:

bashCopy code
[code]
    openclaw plugins install clawhub:your-org/your-plugin
[/code]

## Регистрация инструментов

Инструменты могут быть обязательными или опциональными. Обязательные инструменты всегда доступны, когда Plugin включен. Опциональные инструменты требуют явного согласия пользователя.

typescriptCopy code
[code]
    register(api) {  api.registerTool(    {      name: "workflow_tool",      description: "Run a workflow",      parameters: Type.Object({ pipeline: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: params.pipeline }] };      },    },    { optional: true },  );}
[/code]

Каждый инструмент, зарегистрированный через `api.registerTool(...)`, также должен быть объявлен в манифесте Plugin:

jsonCopy code
[code]
    {  "contracts": {    "tools": ["workflow_tool"]  },  "toolMetadata": {    "workflow_tool": {      "optional": true    }  }}
[/code]

Пользователи включают его через `tools.allow`:

json5Copy code
[code]
    {  tools: { allow: ["workflow_tool"] }, // or ["my-plugin"] for all tools from one plugin}
[/code]

Опциональные инструменты управляют тем, раскрывается ли инструмент модели. Используйте [запросы разрешений Plugin](</ru/plugins/plugin-permission-requests>), когда инструмент или hook должен запросить подтверждение после выбора моделью и до выполнения действия.

Используйте опциональные инструменты для побочных эффектов, необычных бинарных файлов или возможностей, которые не должны быть раскрыты по умолчанию. Имена инструментов не должны конфликтовать с core-инструментами; конфликты пропускаются и отображаются в диагностике Plugin. Некорректные регистрации, включая дескрипторы инструментов без `parameters`, пропускаются и отображаются так же. Зарегистрированные инструменты являются типизированными функциями, которые модель может вызывать после прохождения проверок политик и allowlist.

Фабрики инструментов получают объект контекста, предоставленный runtime. Используйте `ctx.activeModel`, когда инструменту нужно логировать, отображать или адаптироваться к активной модели для текущего хода. Объект может включать `provider`, `modelId` и `modelRef`. Рассматривайте его как информационные runtime-метаданные, а не как границу безопасности против локального оператора, кода установленного Plugin или измененного runtime OpenClaw. Чувствительные локальные инструменты всё равно должны требовать явного согласия Plugin или оператора и завершаться закрытым отказом, когда метаданные активной модели отсутствуют или неподходят.

Манифест объявляет владение и обнаружение; выполнение всё равно вызывает живую зарегистрированную реализацию инструмента. Держите `toolMetadata.<tool>.optional: true` согласованным с `api.registerTool(..., { optional: true })`, чтобы OpenClaw мог не загружать runtime этого Plugin, пока инструмент не будет явно добавлен в allowlist.

## Соглашения об импорте

Импортируйте из специализированных подпутей SDK:

typescriptCopy code
[code]
      
[/code]

Не импортируйте из устаревшего корневого barrel:

typescriptCopy code
[code]
     
[/code]

Внутри пакета вашего Plugin используйте локальные barrel-файлы, такие как `api.ts` и `runtime-api.ts`, для внутренних импортов. Не импортируйте собственный Plugin через путь SDK. Хелперы, специфичные для поставщика, должны оставаться в пакете поставщика, если граница не является действительно общей.

Пользовательские методы Gateway RPC являются продвинутой точкой входа. Держите их на префиксе, специфичном для Plugin; core-пространства имен администрирования, такие как `config.*`, `exec.approvals.*`, `operator.admin.*`, `wizard.*` и `update.*`, остаются зарезервированными и разрешаются в `operator.admin`. Мост `openclaw/plugin-sdk/gateway-method-runtime` зарезервирован для HTTP-маршрутов Plugin, которые объявляют `contracts.gatewayMethodDispatch: ["authenticated-request"]`.

Полную карту импортов см. в [обзоре Plugin SDK](</ru/plugins/sdk-overview>).

## Чеклист перед отправкой

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s **package.json** содержит корректные метаданные `openclaw` OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Манифест **openclaw.plugin.json** присутствует и валиден OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Точка входа использует `defineChannelPluginEntry` или `definePluginEntry` OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Все импорты используют специализированные пути `plugin-sdk/<subpath>` OPENCLAW_DOCS_MARKER:calloutClose:

Was this useful?YesNo

Open issue