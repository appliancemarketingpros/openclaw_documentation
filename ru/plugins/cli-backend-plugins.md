---
title: Создание плагинов бэкенда CLI
source_url: https://docs.openclaw.ai/ru/plugins/cli-backend-plugins
scraped_at: 2026-06-29
---

CapabilitiesBuilding plugins

Плагины бэкендов CLI позволяют OpenClaw вызывать локальный AI CLI как бэкенд текстового инференса. Бэкенд отображается как префикс провайдера в ссылках на модели:

textCopy code
[code]
    acme-cli/acme-large
[/code]

Используйте бэкенд CLI, когда вышестоящая интеграция уже доступна как локальная команда, когда CLI владеет локальным состоянием входа или когда CLI является полезным резервным вариантом, если API-провайдеры недоступны.

## За что отвечает плагин

Плагин бэкенда CLI имеет три контракта:

Контракт | Файл | Назначение  
---|---|---  
Точка входа пакета | `package.json` | Указывает OpenClaw на модуль среды выполнения плагина  
Владение манифестом | `openclaw.plugin.json` | Объявляет id бэкенда до загрузки среды выполнения  
Регистрация runtime | `index.ts` | Вызывает `api.registerCliBackend(...)` с командами по умолчанию  
  
Манифест — это метаданные обнаружения. Он не выполняет CLI и не регистрирует поведение среды выполнения. Поведение среды выполнения начинается, когда точка входа плагина вызывает `api.registerCliBackend(...)`.

## Минимальный плагин бэкенда

* ### Создайте метаданные пакета

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-acme-cli",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./index.ts"],    "compat": {      "pluginApi": ">=2026.3.24-beta.2",      "minGatewayVersion": "2026.3.24-beta.2"    },    "build": {      "openclawVersion": "2026.3.24-beta.2",      "pluginSdkVersion": "2026.3.24-beta.2"    }  },  "dependencies": {    "openclaw": "^2026.3.24"  },  "devDependencies": {    "typescript": "^5.9.0"  }}
[/code]

Опубликованные пакеты должны поставлять собранные JavaScript-файлы среды выполнения. Если ваша исходная точка входа — `./src/index.ts`, добавьте `openclaw.runtimeExtensions`, указывающий на собранный JavaScript-аналог. См. [Точки входа](</ru/plugins/sdk-entrypoints>).

* ### Объявите владение бэкендом

openclaw.plugin.jsonCopy code
[code]
    {  "id": "acme-cli",  "name": "Acme CLI",  "description": "Run Acme's local AI CLI through OpenClaw",  "cliBackends": ["acme-cli"],  "setup": {    "cliBackends": ["acme-cli"],    "requiresRuntime": false  },  "activation": {    "onStartup": false  },  "configSchema": {    "type": "object",    "additionalProperties": false  }}
[/code]

`cliBackends` — это список владения runtime. Он позволяет OpenClaw автоматически загружать плагин, когда конфигурация или выбор модели упоминает `acme-cli/...`.

`setup.cliBackends` — это setup-поверхность, ориентированная сначала на дескрипторы. Добавьте ее, когда обнаружение моделей, онбординг или статус должны распознавать бэкенд без загрузки runtime плагина. Используйте `requiresRuntime: false` только когда этих статических дескрипторов достаточно для setup.

* ### Зарегистрируйте бэкенд

index.tsCopy code
[code]
    import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";import {  CLI_FRESH_WATCHDOG_DEFAULTS,  CLI_RESUME_WATCHDOG_DEFAULTS,  type CliBackendPlugin,} from "openclaw/plugin-sdk/cli-backend"; function buildAcmeCliBackend(): CliBackendPlugin {  return {    id: "acme-cli",    liveTest: {      defaultModelRef: "acme-cli/acme-large",      defaultImageProbe: false,      defaultMcpProbe: false,      docker: {        npmPackage: "@acme/acme-cli",        binaryName: "acme",      },    },    config: {      command: "acme",      args: ["chat", "--json"],      output: "json",      input: "stdin",      modelArg: "--model",      sessionArg: "--session",      sessionMode: "existing",      sessionIdFields: ["session_id", "conversation_id"],      systemPromptFileArg: "--system-file",      systemPromptWhen: "first",      imageArg: "--image",      imageMode: "repeat",      reliability: {        watchdog: {          fresh: { ...CLI_FRESH_WATCHDOG_DEFAULTS },          resume: { ...CLI_RESUME_WATCHDOG_DEFAULTS },        },      },      serialize: true,    },  };} export default definePluginEntry({  id: "acme-cli",  name: "Acme CLI",  description: "Run Acme's local AI CLI through OpenClaw",  register(api) {    api.registerCliBackend(buildAcmeCliBackend());  },});
[/code]

Id бэкенда должен совпадать с записью `cliBackends` в манифесте. Зарегистрированная `config` — только значение по умолчанию; пользовательская конфигурация в `agents.defaults.cliBackends.acme-cli` накладывается поверх нее во время выполнения.

## Форма конфигурации

`CliBackendConfig` описывает, как OpenClaw должен запускать и разбирать CLI:

Поле | Использование  
---|---  
`command` | Имя бинарного файла или абсолютный путь команды  
`args` | Базовый argv для новых запусков  
`resumeArgs` | Альтернативный argv для возобновленных сессий; поддерживает `{sessionId}`  
`output` / `resumeOutput` | Парсер: `json`, `jsonl` или `text`  
`input` | Транспорт промпта: `arg` или `stdin`  
`modelArg` | Флаг, используемый перед id модели  
`modelAliases` | Сопоставляет id моделей OpenClaw с нативными id CLI  
`sessionArg` / `sessionArgs` | Как передавать id сессии  
`sessionMode` | `always`, `existing` или `none`  
`sessionIdFields` | JSON-поля, которые OpenClaw читает из вывода CLI  
`systemPromptArg` / `systemPromptFileArg` | Транспорт системного промпта  
`systemPromptWhen` | `first`, `always` или `never`  
`imageArg` / `imageMode` | Поддержка пути к изображению  
`serialize` | Сохранять порядок запусков одного бэкенда  
`reliability.watchdog` | Настройка таймаута при отсутствии вывода  
  
Предпочитайте минимальную статическую конфигурацию, которая соответствует CLI. Добавляйте callbacks плагина только для поведения, которое действительно принадлежит бэкенду.

## Расширенные hooks бэкенда

`CliBackendPlugin` также может определять:

Hook | Использование  
---|---  
`normalizeConfig(config, context)` | Переписать устаревшую пользовательскую конфигурацию после merge  
`resolveExecutionArgs(ctx)` | Добавить флаги уровня запроса, например усилие рассуждения или изоляцию дополнительного вопроса  
`prepareExecution(ctx)` | Создать временные мосты auth или конфигурации перед запуском  
`transformSystemPrompt(ctx)` | Применить финальное CLI-специфичное преобразование системного промпта  
`textTransforms` | Двунаправленные замены промпта/вывода  
`defaultAuthProfileId` | Предпочитать конкретный профиль auth OpenClaw  
`authEpochMode` | Решить, как изменения auth инвалидируют сохраненные CLI-сессии  
`nativeToolMode` | Объявить, есть ли у CLI постоянно включенные нативные инструменты  
`sideQuestionToolMode` | Объявить отключенные нативные инструменты для дополнительных вопросов `/btw`  
`bundleMcp` / `bundleMcpMode` | Подключить loopback-мост MCP-инструментов OpenClaw  
`ownsNativeCompaction` | Бэкенд владеет собственной compaction — OpenClaw откладывает свою  
  
Держите эти hooks во владении провайдера. Не добавляйте CLI-специфичные ветки в core, когда hook бэкенда может выразить это поведение.

`ctx.executionMode` равен `"agent"` для обычных ходов и `"side-question"` для эфемерных вызовов `/btw`. Используйте его, когда CLI нужны другие одноразовые флаги, например отключение нативных инструментов, сохранения сессии или поведения возобновления для BTW. Если бэкенд обычно имеет `nativeToolMode: "always-on"`, но его argv для дополнительного вопроса надежно отключает эти инструменты, также задайте `sideQuestionToolMode: "disabled"`; иначе OpenClaw fail-closed, когда BTW требует запуск CLI без инструментов.

### `ownsNativeCompaction`: отказ от compaction OpenClaw

Если ваш бэкенд запускает агента, который сжимает свой **собственный** transcript, задайте `ownsNativeCompaction: true`, чтобы защитный summarizer OpenClaw никогда не запускался для его сессий — жизненный цикл compaction CLI возвращает no-op, и ход продолжается. `claude-cli` объявляет это, потому что Claude Code сжимает внутренне без endpoint harness. Сессии native-harness, такие как Codex, вместо этого продолжают маршрутизироваться к endpoint compaction своего harness.

**Объявляйте это только когда выполняются все следующие условия** , иначе отложенная сессия с превышенным бюджетом может остаться выше бюджета / устареть (OpenClaw больше ее не спасает):

  * бэкенд надежно сжимает или ограничивает собственный transcript по мере приближения к своему окну;
  * он сохраняет возобновляемую сессию, чтобы сжатое состояние переживало ходы (например, `--resume` / `--session-id`);
  * это не сессия compaction native-harness — сессии, соответствующие `agentHarnessId`, вместо этого маршрутизируются к endpoint harness.


## Мост MCP-инструментов

Бэкенды CLI по умолчанию не получают инструменты OpenClaw. Если CLI может потреблять конфигурацию MCP, явно включите это:

typescriptCopy code
[code]
    return {  id: "acme-cli",  bundleMcp: true,  bundleMcpMode: "codex-config-overrides",  config: {    command: "acme",    args: ["chat", "--json"],    output: "json",  },};
[/code]

Поддерживаемые режимы моста:

Режим | Использование  
---|---  
`claude-config-file` | CLI, которые принимают файл конфигурации MCP  
`codex-config-overrides` | CLI, которые принимают переопределения конфигурации в argv  
`gemini-system-settings` | CLI, которые читают настройки MCP из каталога системных настроек  
  
Включайте мост только когда CLI действительно может его потреблять. Если у CLI есть собственный встроенный слой инструментов, который нельзя отключить, задайте `nativeToolMode: "always-on"`, чтобы OpenClaw мог fail-closed, когда вызывающей стороне требуются отсутствие нативных инструментов.

## Пользовательская конфигурация

Пользователи могут переопределить любое значение бэкенда по умолчанию:

json5Copy code
[code]
    {  agents: {    defaults: {      cliBackends: {        "acme-cli": {          command: "/opt/acme/bin/acme",          args: ["chat", "--json", "--profile", "work"],          modelAliases: {            large: "acme-large-2026",          },        },      },      model: {        primary: "openai/gpt-5.5",        fallbacks: ["acme-cli/large"],      },    },  },}
[/code]

Документируйте минимальное переопределение, которое, вероятно, понадобится пользователям. Обычно это только `command`, когда бинарный файл находится вне `PATH`.

## Проверка

Для встроенных плагинов добавьте целевой тест для регистрации сборщика и настройки, затем запустите целевой тестовый путь плагина:

bashCopy code
[code]
    pnpm test extensions/acme-cli
[/code]

Для локальных или установленных плагинов проверьте обнаружение и один реальный запуск модели:

bashCopy code
[code]
    openclaw plugins inspect acme-cli --runtime --jsonopenclaw agent --message "reply exactly: backend ok" --model acme-cli/acme-large
[/code]

Если бэкенд поддерживает изображения или MCP, добавьте проверку работоспособности с реальным CLI, которая подтверждает эти пути. Не полагайтесь на статическую проверку для поведения prompt, изображений, MCP или возобновления сеанса.

## Контрольный список

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `package.json` содержит `openclaw.extensions` и собранные runtime-записи для опубликованных пакетов OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `openclaw.plugin.json` объявляет `cliBackends` и намеренное `activation.onStartup` OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `setup.cliBackends` присутствует, когда настройка или обнаружение моделей должны видеть бэкенд в холодном состоянии OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `api.registerCliBackend(...)` использует тот же идентификатор бэкенда, что и манифест OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Пользовательские переопределения в `agents.defaults.cliBackends.<id>` по-прежнему имеют приоритет OPENCLAW_DOCS_MARKER:calloutClose:

Was this useful?YesNo

Open issue