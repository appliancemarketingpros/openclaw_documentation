---
title: Створення Plugin
source_url: https://docs.openclaw.ai/uk/plugins/building-plugins
scraped_at: 2026-05-25
---

Plugins розширюють OpenClaw новими можливостями: каналами, провайдерами моделей, мовленням, транскрипцією в реальному часі, голосом у реальному часі, розумінням медіа, генерацією зображень, генерацією відео, web fetch, web search, інструментами агентів або будь-якою комбінацією.

Вам не потрібно додавати свій plugin до репозиторію OpenClaw. Опублікуйте його в [ClawHub](</uk/clawhub>), і користувачі встановлять його за допомогою `openclaw plugins install clawhub:<package-name>`. Прості специфікації пакетів усе ще встановлюються з npm під час перехідного запуску.

## Передумови

  * Node >= 22 і менеджер пакетів (npm або pnpm)
  * Знайомство з TypeScript (ESM)
  * Для plugins у репозиторії: репозиторій клоновано, а `pnpm install` виконано. Розробка plugin з checkout вихідного коду підтримується лише через pnpm, оскільки OpenClaw завантажує bundled plugins з пакетів workspace `extensions/*`.


## Який тип plugin?

[**Channel plugin** Під’єднайте OpenClaw до платформи обміну повідомленнями (Discord, IRC тощо) ](</uk/plugins/sdk-channel-plugins>) [**Provider plugin** Додайте провайдера моделей (LLM, proxy або користувацький endpoint) ](</uk/plugins/sdk-provider-plugins>) [**CLI backend plugin** Зіставте локальний AI CLI з текстовим fallback runner OpenClaw ](</uk/plugins/cli-backend-plugins>) [**Tool / hook plugin** Зареєструйте інструменти агентів, event hooks або сервіси - продовжуйте нижче ](</uk/plugins/hooks>)

Для channel plugin, який не гарантовано буде встановлено під час onboarding/setup, використовуйте `createOptionalChannelSetupSurface(...)` з `openclaw/plugin-sdk/channel-setup`. Він створює пару setup adapter + wizard, яка повідомляє про вимогу встановлення і fail closed під час реальних записів конфігурації, доки plugin не буде встановлено.

## Швидкий старт: tool plugin

Цей покроковий посібник створює мінімальний plugin, який реєструє інструмент агента. Для channel і provider plugins є окремі посібники за посиланнями вище.

* ### Створіть пакет і manifest

package.jsonCopy code
[code]
    {"name": "@myorg/openclaw-my-plugin","version": "1.0.0","type": "module","openclaw": {  "extensions": ["./index.ts"],  "compat": {    "pluginApi": ">=2026.3.24-beta.2",    "minGatewayVersion": "2026.3.24-beta.2"  },  "build": {    "openclawVersion": "2026.3.24-beta.2",    "pluginSdkVersion": "2026.3.24-beta.2"  }}}
[/code]

openclaw.plugin.jsonCopy code
[code]
    {"id": "my-plugin","name": "My Plugin","description": "Adds a custom tool to OpenClaw","contracts": {  "tools": ["my_tool"]},"activation": {  "onStartup": true},"configSchema": {  "type": "object",  "additionalProperties": false}}
[/code]

Кожному plugin потрібен manifest, навіть без config. Інструменти, зареєстровані під час виконання, мають бути перелічені в `contracts.tools`, щоб OpenClaw міг виявити plugin-власник без завантаження runtime кожного plugin. Plugins також мають свідомо оголошувати `activation.onStartup`. У цьому прикладі для нього встановлено `true`. Повну схему див. у [Manifest](</uk/plugins/manifest>). Канонічні фрагменти публікації ClawHub розміщені в `docs/snippets/plugin-publish/`.

* ### Напишіть entry point

typescriptCopy code
[code]
    // index.tsimport { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";import { Type } from "@sinclair/typebox"; export default definePluginEntry({  id: "my-plugin",  name: "My Plugin",  description: "Adds a custom tool to OpenClaw",  register(api) {    api.registerTool({      name: "my_tool",      description: "Do a thing",      parameters: Type.Object({ input: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: `Got: ${params.input}` }] };      },    });  },});
[/code]

`definePluginEntry` призначений для plugins, які не є каналами. Для каналів використовуйте `defineChannelPluginEntry` \- див. [Channel Plugins](</uk/plugins/sdk-channel-plugins>). Повні параметри entry point див. у [Entry Points](</uk/plugins/sdk-entrypoints>).

* ### Перевірте й опублікуйте

**Зовнішні plugins:** перевірте й опублікуйте за допомогою ClawHub, потім установіть:

bashCopy code
[code]
    clawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginopenclaw plugins install clawhub:@myorg/openclaw-my-plugin
[/code]

Голі специфікації пакетів, як-от `@myorg/openclaw-my-plugin`, установлюються з npm під час переходу на запуск. Використовуйте `clawhub:`, коли потрібне розв’язання через ClawHub.

**Plugin у репозиторії:** розмістіть під деревом робочого простору bundled plugin - виявляється автоматично.

bashCopy code
[code]
    pnpm test -- <bundled-plugin-root>/my-plugin/
[/code]

## Можливості Plugin

Один plugin може зареєструвати будь-яку кількість можливостей через об’єкт `api`:

Можливість | Метод реєстрації | Докладний посібник  
---|---|---  
Текстовий інференс (LLM) | `api.registerProvider(...)` | [Provider Plugins](</uk/plugins/sdk-provider-plugins>)  
Бекенд інференсу CLI | `api.registerCliBackend(...)` | [CLI Backend Plugins](</uk/plugins/cli-backend-plugins>)  
Канал / обмін повідомленнями | `api.registerChannel(...)` | [Channel Plugins](</uk/plugins/sdk-channel-plugins>)  
Мовлення (TTS/STT) | `api.registerSpeechProvider(...)` | [Provider Plugins](</uk/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Транскрипція в реальному часі | `api.registerRealtimeTranscriptionProvider(...)` | [Provider Plugins](</uk/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Голос у реальному часі | `api.registerRealtimeVoiceProvider(...)` | [Provider Plugins](</uk/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Розуміння медіа | `api.registerMediaUnderstandingProvider(...)` | [Provider Plugins](</uk/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Генерація зображень | `api.registerImageGenerationProvider(...)` | [Provider Plugins](</uk/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Генерація музики | `api.registerMusicGenerationProvider(...)` | [Provider Plugins](</uk/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Генерація відео | `api.registerVideoGenerationProvider(...)` | [Provider Plugins](</uk/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Отримання даних з вебу | `api.registerWebFetchProvider(...)` | [Provider Plugins](</uk/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Вебпошук | `api.registerWebSearchProvider(...)` | [Provider Plugins](</uk/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Middleware для результатів інструментів | `api.registerAgentToolResultMiddleware(...)` | [Огляд SDK](</uk/plugins/sdk-overview#registration-api>)  
Інструменти агента | `api.registerTool(...)` | Нижче  
Користувацькі команди | `api.registerCommand(...)` | [Точки входу](</uk/plugins/sdk-entrypoints>)  
Хуки Plugin | `api.on(...)` | [Хуки Plugin](</uk/plugins/hooks>)  
Внутрішні хуки подій | `api.registerHook(...)` | [Точки входу](</uk/plugins/sdk-entrypoints>)  
HTTP-маршрути | `api.registerHttpRoute(...)` | [Внутрішні механізми](</uk/plugins/architecture-internals#gateway-http-routes>)  
Підкоманди CLI | `api.registerCli(...)` | [Точки входу](</uk/plugins/sdk-entrypoints>)  
  
Повний API реєстрації див. в [огляді SDK](</uk/plugins/sdk-overview#registration-api>).

Bundled plugins можуть використовувати `api.registerAgentToolResultMiddleware(...)`, коли їм потрібне асинхронне переписування результату інструмента до того, як модель побачить вивід. Оголосіть цільові середовища виконання в `contracts.agentToolResultMiddleware`, наприклад `["pi", "codex"]`. Це довірений seam для bundled plugin; зовнішнім plugins варто надавати перевагу звичайним хукам Plugin OpenClaw, якщо OpenClaw не додасть явну політику довіри для цієї можливості.

Якщо ваш plugin реєструє користувацькі RPC-методи Gateway, тримайте їх під префіксом, специфічним для plugin. Основні адміністративні простори імен (`config.*`, `exec.approvals.*`, `wizard.*`, `update.*`) залишаються зарезервованими й завжди розв’язуються в `operator.admin`, навіть якщо plugin просить вужчу область дії.

Семантика захисту хуків, яку слід мати на увазі:

  * `before_tool_call`: `{ block: true }` є термінальним і зупиняє обробники з нижчим пріоритетом.
  * `before_tool_call`: `{ block: false }` трактується як відсутність рішення.
  * `before_tool_call`: `{ requireApproval: true }` призупиняє виконання агента й запитує схвалення користувача через оверлей схвалення exec, кнопки Telegram, взаємодії Discord або команду `/approve` у будь-якому каналі.
  * `before_install`: `{ block: true }` є термінальним і зупиняє обробники з нижчим пріоритетом.
  * `before_install`: `{ block: false }` трактується як відсутність рішення.
  * `message_sending`: `{ cancel: true }` є термінальним і зупиняє обробники з нижчим пріоритетом.
  * `message_sending`: `{ cancel: false }` трактується як відсутність рішення.
  * `message_received`: надавайте перевагу типізованому полю `threadId`, коли потрібна маршрутизація вхідного ланцюжка/теми. Залишайте `metadata` для специфічних для каналу додаткових даних.
  * `message_sending`: надавайте перевагу типізованим полям маршрутизації `replyToId` / `threadId` замість специфічних для каналу ключів metadata.


Команда `/approve` обробляє як exec-схвалення, так і схвалення plugin з обмеженим резервним варіантом: коли id exec-схвалення не знайдено, OpenClaw повторює спробу з тим самим id через схвалення plugin. Пересилання схвалень plugin можна налаштувати незалежно через `approvals.plugin` у конфігурації.

Якщо користувацькі механізми схвалення мають виявляти той самий випадок обмеженого резервного варіанта, надавайте перевагу `isApprovalNotFoundError` з `openclaw/plugin-sdk/error-runtime` замість ручного зіставлення рядків про завершення строку дії схвалення.

Приклади та довідник хуків див. у [хуках Plugin](</uk/plugins/hooks>).

## Реєстрація інструментів агента

Інструменти - це типізовані функції, які може викликати LLM. Вони можуть бути обов’язковими (завжди доступні) або необов’язковими (користувач увімкне самостійно):

typescriptCopy code
[code]
    register(api) {  // Required tool - always available  api.registerTool({    name: "my_tool",    description: "Do a thing",    parameters: Type.Object({ input: Type.String() }),    async execute(_id, params) {      return { content: [{ type: "text", text: params.input }] };    },  });   // Optional tool - user must add to allowlist  api.registerTool(    {      name: "workflow_tool",      description: "Run a workflow",      parameters: Type.Object({ pipeline: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: params.pipeline }] };      },    },    { optional: true },  );}
[/code]

Фабрики інструментів отримують об’єкт контексту, наданий runtime. Використовуйте `ctx.activeModel`, коли інструменту потрібно журналювати, показувати або адаптуватися до активної моделі для поточного ходу. Об’єкт може містити `provider`, `modelId` і `modelRef`. Сприймайте його як інформаційні runtime-метадані, а не як межу безпеки проти локального оператора, встановленого коду plugin або модифікованого runtime OpenClaw. Для чутливих локальних інструментів зберігайте явне підтвердження від plugin або оператора та відмовляйте за замовчуванням, коли метадані активної моделі відсутні або невідповідні.

Кожен інструмент, зареєстрований через `api.registerTool(...)`, також має бути оголошений у маніфесті plugin:

jsonCopy code
[code]
    {  "contracts": {    "tools": ["my_tool", "workflow_tool"]  },  "toolMetadata": {    "workflow_tool": {      "optional": true    }  }}
[/code]

OpenClaw захоплює й кешує перевірений дескриптор із зареєстрованого інструмента, тому plugins не дублюють `description` або дані схеми в маніфесті. Контракт маніфесту лише оголошує власність і виявлення; виконання все одно викликає живу зареєстровану реалізацію інструмента. Установіть `toolMetadata.<tool>.optional: true` для інструментів, зареєстрованих через `api.registerTool(..., { optional: true })`, щоб OpenClaw міг не завантажувати runtime цього plugin, доки інструмент явно не буде внесено до списку дозволених.

Користувачі вмикають необов’язкові інструменти в конфігурації:

json5Copy code
[code]
    {  tools: { allow: ["workflow_tool"] },}
[/code]

  * Назви інструментів не мають конфліктувати з інструментами ядра (конфлікти пропускаються)
  * Інструменти з некоректно сформованими об’єктами реєстрації, зокрема без `parameters`, пропускаються й повідомляються в діагностиці plugin замість того, щоб зривати запуски агентів
  * Використовуйте `optional: true` для інструментів із побічними ефектами або додатковими вимогами до бінарних файлів
  * Користувачі можуть увімкнути всі інструменти з plugin, додавши id plugin до `tools.allow`


## Реєстрація команд CLI

Plugins можуть додавати кореневі групи команд `openclaw` за допомогою `api.registerCli`. Надайте `descriptors` для кожного кореня команди верхнього рівня, щоб OpenClaw міг показувати й маршрутизувати команду без завчасного завантаження runtime кожного plugin.

typescriptCopy code
[code]
    register(api) {  api.registerCli(    ({ program }) => {      const demo = program        .command("demo-plugin")        .description("Run demo plugin commands");       demo        .command("ping")        .description("Check that the plugin CLI is executable")        .action(() => {          console.log("demo-plugin:pong");        });    },    {      descriptors: [        {          name: "demo-plugin",          description: "Run demo plugin commands",          hasSubcommands: true,        },      ],    },  );}
[/code]

Після встановлення перевірте runtime-реєстрацію та виконайте команду:

bashCopy code
[code]
    openclaw plugins inspect demo-plugin --runtime --jsonopenclaw demo-plugin ping
[/code]

## Угоди щодо імпортів

Завжди імпортуйте зі сфокусованих шляхів `openclaw/plugin-sdk/<subpath>`:

typescriptCopy code
[code]
      // Wrong: monolithic root (deprecated, will be removed) 
[/code]

Повний довідник підшляхів див. у [Огляді SDK](</uk/plugins/sdk-overview>).

У межах вашого plugin використовуйте локальні barrel-файли (`api.ts`, `runtime-api.ts`) для внутрішніх імпортів - ніколи не імпортуйте власний plugin через його SDK-шлях.

Для provider plugins тримайте специфічні для провайдера helpers у цих barrel-файлах кореня пакета, якщо seam не є справді універсальним. Поточні вбудовані приклади:

  * Anthropic: обгортки Claude stream і helpers `service_tier` / beta
  * OpenAI: конструктори провайдера, helpers моделей за замовчуванням, realtime-провайдери
  * OpenRouter: конструктор провайдера та helpers onboarding/конфігурації


Якщо helper корисний лише всередині одного вбудованого пакета провайдера, тримайте його на цьому seam кореня пакета замість просування в `openclaw/plugin-sdk/*`.

Деякі згенеровані helper seams `openclaw/plugin-sdk/<bundled-id>` усе ще існують для обслуговування вбудованих plugins, коли вони мають відстежене використання власником. Вважайте їх зарезервованими поверхнями, а не типовим шаблоном для нових сторонніх plugins.

## Контрольний список перед поданням

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s **package.json** має коректні метадані `openclaw` OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Маніфест **openclaw.plugin.json** присутній і валідний OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Точка входу використовує `defineChannelPluginEntry` або `definePluginEntry` OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Усі імпорти використовують сфокусовані шляхи `plugin-sdk/<subpath>` OPENCLAW_DOCS_MARKER:calloutClose:

Was this useful?YesNo