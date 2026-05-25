---
title: Створення бекенд-Plugin для CLI
source_url: https://docs.openclaw.ai/uk/plugins/cli-backend-plugins
scraped_at: 2026-05-25
---

Плагіни бекенду CLI дають OpenClaw змогу викликати локальний AI CLI як бекенд текстового виведення. Бекенд відображається як префікс провайдера в посиланнях на моделі:

textCopy code
[code]
    acme-cli/acme-large
[/code]

Використовуйте бекенд CLI, коли upstream-інтеграція вже доступна як локальна команда, коли CLI володіє локальним станом входу, або коли CLI є корисним резервним варіантом, якщо API-провайдери недоступні.

## За що відповідає плагін

Плагін бекенду CLI має три контракти:

Контракт | Файл | Призначення  
---|---|---  
Точка входу пакета | `package.json` | Вказує OpenClaw на модуль середовища виконання плагіна  
Володіння маніфестом | `openclaw.plugin.json` | Оголошує ідентифікатор бекенду до завантаження runtime  
Реєстрація runtime | `index.ts` | Викликає `api.registerCliBackend(...)` з типовими командами  
  
Маніфест — це метадані виявлення. Він не виконує CLI і не реєструє поведінку runtime. Поведінка runtime починається, коли точка входу плагіна викликає `api.registerCliBackend(...)`.

## Мінімальний плагін бекенду

* ### Створіть метадані пакета

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-acme-cli",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./index.ts"],    "compat": {      "pluginApi": ">=2026.3.24-beta.2",      "minGatewayVersion": "2026.3.24-beta.2"    },    "build": {      "openclawVersion": "2026.3.24-beta.2",      "pluginSdkVersion": "2026.3.24-beta.2"    }  },  "dependencies": {    "openclaw": "^2026.3.24"  },  "devDependencies": {    "typescript": "^5.9.0"  }}
[/code]

Опубліковані пакети мають постачати зібрані файли JavaScript runtime. Якщо ваша вихідна точка входу — `./src/index.ts`, додайте `openclaw.runtimeExtensions`, що вказує на відповідний зібраний JavaScript-файл. Див. [Точки входу](</uk/plugins/sdk-entrypoints>).

* ### Оголосіть володіння бекендом

openclaw.plugin.jsonCopy code
[code]
    {  "id": "acme-cli",  "name": "Acme CLI",  "description": "Run Acme's local AI CLI through OpenClaw",  "cliBackends": ["acme-cli"],  "setup": {    "cliBackends": ["acme-cli"],    "requiresRuntime": false  },  "activation": {    "onStartup": false  },  "configSchema": {    "type": "object",    "additionalProperties": false  }}
[/code]

`cliBackends` — це список володіння runtime. Він дає OpenClaw змогу автоматично завантажувати плагін, коли конфігурація або вибір моделі згадує `acme-cli/...`.

`setup.cliBackends` — це поверхня налаштування за принципом descriptor-first. Додайте її, коли виявлення моделей, onboarding або статус мають розпізнавати бекенд без завантаження runtime плагіна. Використовуйте `requiresRuntime: false` лише тоді, коли цих статичних дескрипторів достатньо для налаштування.

* ### Зареєструйте бекенд

index.tsCopy code
[code]
    import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";import {  CLI_FRESH_WATCHDOG_DEFAULTS,  CLI_RESUME_WATCHDOG_DEFAULTS,  type CliBackendPlugin,} from "openclaw/plugin-sdk/cli-backend"; function buildAcmeCliBackend(): CliBackendPlugin {  return {    id: "acme-cli",    liveTest: {      defaultModelRef: "acme-cli/acme-large",      defaultImageProbe: false,      defaultMcpProbe: false,      docker: {        npmPackage: "@acme/acme-cli",        binaryName: "acme",      },    },    config: {      command: "acme",      args: ["chat", "--json"],      output: "json",      input: "stdin",      modelArg: "--model",      sessionArg: "--session",      sessionMode: "existing",      sessionIdFields: ["session_id", "conversation_id"],      systemPromptFileArg: "--system-file",      systemPromptWhen: "first",      imageArg: "--image",      imageMode: "repeat",      reliability: {        watchdog: {          fresh: { ...CLI_FRESH_WATCHDOG_DEFAULTS },          resume: { ...CLI_RESUME_WATCHDOG_DEFAULTS },        },      },      serialize: true,    },  };} export default definePluginEntry({  id: "acme-cli",  name: "Acme CLI",  description: "Run Acme's local AI CLI through OpenClaw",  register(api) {    api.registerCliBackend(buildAcmeCliBackend());  },});
[/code]

Ідентифікатор бекенду має збігатися із записом `cliBackends` у маніфесті. Зареєстрована `config` є лише типовою; користувацька конфігурація в `agents.defaults.cliBackends.acme-cli` об’єднується з нею під час виконання.

## Форма конфігурації

`CliBackendConfig` описує, як OpenClaw має запускати й розбирати CLI:

Поле | Використання  
---|---  
`command` | Ім’я бінарного файла або абсолютний шлях до команди  
`args` | Базовий argv для нових запусків  
`resumeArgs` | Альтернативний argv для відновлених сесій; підтримує `{sessionId}`  
`output` / `resumeOutput` | Парсер: `json`, `jsonl` або `text`  
`input` | Транспорт підказки: `arg` або `stdin`  
`modelArg` | Прапорець, що використовується перед ідентифікатором моделі  
`modelAliases` | Зіставляє ідентифікатори моделей OpenClaw з нативними ідентифікаторами CLI  
`sessionArg` / `sessionArgs` | Як передавати ідентифікатор сесії  
`sessionMode` | `always`, `existing` або `none`  
`sessionIdFields` | JSON-поля, які OpenClaw читає з виводу CLI  
`systemPromptArg` / `systemPromptFileArg` | Транспорт системної підказки  
`systemPromptWhen` | `first`, `always` або `never`  
`imageArg` / `imageMode` | Підтримка шляхів до зображень  
`serialize` | Зберігати порядок запусків того самого бекенду  
`reliability.watchdog` | Налаштування тайм-ауту без виводу  
  
Надавайте перевагу найменшій статичній конфігурації, що відповідає CLI. Додавайте callback-и плагіна лише для поведінки, яка справді належить бекенду.

## Розширені хуки бекенду

`CliBackendPlugin` також може визначати:

Хук | Використання  
---|---  
`normalizeConfig(config, context)` | Переписати застарілу користувацьку конфігурацію після об’єднання  
`resolveExecutionArgs(ctx)` | Додати прапорці в межах запиту, наприклад thinking effort  
`prepareExecution(ctx)` | Створити тимчасові мости auth або конфігурації перед запуском  
`transformSystemPrompt(ctx)` | Застосувати фінальне CLI-специфічне перетворення системної підказки  
`textTransforms` | Двонапрямні заміни підказок/виводу  
`defaultAuthProfileId` | Надавати перевагу конкретному профілю auth OpenClaw  
`authEpochMode` | Вирішувати, як зміни auth інвалідовують збережені сесії CLI  
`nativeToolMode` | Оголосити, чи CLI має завжди ввімкнені нативні інструменти  
`bundleMcp` / `bundleMcpMode` | Увімкнути міст інструментів loopback MCP OpenClaw  
  
Зберігайте ці хуки у власності провайдера. Не додавайте CLI-специфічні гілки до core, коли хук бекенду може виразити поведінку.

## Міст інструментів MCP

Бекенди CLI типово не отримують інструменти OpenClaw. Якщо CLI може споживати конфігурацію MCP, увімкніть це явно:

typescriptCopy code
[code]
    return {  id: "acme-cli",  bundleMcp: true,  bundleMcpMode: "codex-config-overrides",  config: {    command: "acme",    args: ["chat", "--json"],    output: "json",  },};
[/code]

Підтримувані режими мосту:

Режим | Використання  
---|---  
`claude-config-file` | CLI, що приймають файл конфігурації MCP  
`codex-config-overrides` | CLI, що приймають перевизначення конфігурації в argv  
`gemini-system-settings` | CLI, що читають налаштування MCP зі свого каталогу системних налаштувань  
  
Увімкніть міст лише тоді, коли CLI справді може його споживати. Якщо CLI має власний вбудований шар інструментів, який не можна вимкнути, встановіть `nativeToolMode: "always-on"`, щоб OpenClaw міг відмовляти закрито, коли викликач вимагає відсутності нативних інструментів.

## Користувацька конфігурація

Користувачі можуть перевизначити будь-яке типове значення бекенду:

json5Copy code
[code]
    {  agents: {    defaults: {      cliBackends: {        "acme-cli": {          command: "/opt/acme/bin/acme",          args: ["chat", "--json", "--profile", "work"],          modelAliases: {            large: "acme-large-2026",          },        },      },      model: {        primary: "openai/gpt-5.5",        fallbacks: ["acme-cli/large"],      },    },  },}
[/code]

Документуйте мінімальне перевизначення, яке, ймовірно, знадобиться користувачам. Зазвичай це лише `command`, коли бінарний файл розташований поза `PATH`.

## Перевірка

Для вбудованих плагінів додайте сфокусований тест для builder і реєстрації налаштування, а потім запустіть цільову тестову лінію плагіна:

bashCopy code
[code]
    pnpm test extensions/acme-cli
[/code]

Для локальних або встановлених плагінів перевірте виявлення й один реальний запуск моделі:

bashCopy code
[code]
    openclaw plugins inspect acme-cli --runtime --jsonopenclaw agent --message "reply exactly: backend ok" --model acme-cli/acme-large
[/code]

Якщо бекенд підтримує зображення або MCP, додайте live smoke, що доводить ці шляхи з реальним CLI. Не покладайтеся на статичну інспекцію для поведінки підказок, зображень, MCP або відновлення сесій.

## Контрольний список

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `package.json` має `openclaw.extensions` і зібрані runtime-точки входу для опублікованих пакетів OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `openclaw.plugin.json` оголошує `cliBackends` і навмисне `activation.onStartup` OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `setup.cliBackends` присутній, коли налаштування/виявлення моделей має бачити бекенд холодним OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `api.registerCliBackend(...)` використовує той самий ідентифікатор бекенду, що й маніфест OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Користувацькі перевизначення в `agents.defaults.cliBackends.<id>` усе ще мають пріоритет OPENCLAW_DOCS_MARKER:calloutClose:

Was this useful?YesNo