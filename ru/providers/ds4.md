---
title: ds4
source_url: https://docs.openclaw.ai/ru/providers/ds4
scraped_at: 2026-06-29
---

ModelsProviders

[ds4](<https://github.com/antirez/ds4>) обслуживает DeepSeek V4 Flash из локального бэкенда Metal с OpenAI-совместимым API `/v1`. OpenClaw подключается к ds4 через универсальное семейство провайдеров `openai-completions`.

ds4 не является встроенным Plugin провайдера OpenClaw. Настройте его в `models.providers.ds4`, затем выберите `ds4/deepseek-v4-flash`.

  * Идентификатор провайдера: `ds4`
  * Plugin: нет
  * API: OpenAI-совместимый Chat Completions (`openai-completions`)
  * Рекомендуемый базовый URL: `http://127.0.0.1:18000/v1`
  * Идентификатор модели: `deepseek-v4-flash`
  * Вызовы инструментов: поддерживаются через `tools` и `tool_calls` в стиле OpenAI
  * Рассуждение: `thinking` и `reasoning_effort` в стиле DeepSeek


## Требования

  * macOS с поддержкой Metal.
  * Рабочая копия ds4 с `ds4-server` и файлом GGUF DeepSeek V4 Flash.
  * Достаточно памяти для выбранного вами контекста. Большие значения `--ctx` выделяют больше KV-памяти при запуске сервера.


## Быстрый старт

* ### Start ds4-server

Замените `&lt;DS4_DIR&gt;` на путь к вашей рабочей копии ds4.

bashCopy code
[code]
    &lt;DS4_DIR&gt;/ds4-server \  --model &lt;DS4_DIR&gt;/ds4flash.gguf \  --host 127.0.0.1 \  --port 18000 \  --ctx 32768 \  --tokens 128
[/code]

* ### Verify the OpenAI-compatible endpoint

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

Ответ должен включать `deepseek-v4-flash`.

* ### Add the OpenClaw provider config

Добавьте конфигурацию из Полной конфигурации, затем выполните разовую проверку модели:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

## Полная конфигурация

Используйте эту конфигурацию, когда ds4 уже запущен на `127.0.0.1:18000`.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "ds4/deepseek-v4-flash" },      models: {        "ds4/deepseek-v4-flash": {          alias: "DS4 local",        },      },    },  },  models: {    mode: "merge",    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

Держите `contextWindow` согласованным со значением `ds4-server --ctx`. Держите `maxTokens` согласованным с `--tokens`, если вы намеренно не хотите, чтобы OpenClaw запрашивал меньше вывода, чем значение сервера по умолчанию.

## Запуск по требованию

OpenClaw может запускать ds4 только когда выбрана модель `ds4/...`. Добавьте `localService` в ту же запись провайдера:

json5Copy code
[code]
    {  models: {    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "&lt;DS4_DIR&gt;/ds4-server",          args: [            "--model",            "&lt;DS4_DIR&gt;/ds4flash.gguf",            "--host",            "127.0.0.1",            "--port",            "18000",            "--ctx",            "32768",            "--tokens",            "128",          ],          cwd: "&lt;DS4_DIR&gt;",          healthUrl: "http://127.0.0.1:18000/v1/models",          readyTimeoutMs: 300000,          idleStopMs: 0,        },        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

`command` должен быть абсолютным путем к исполняемому файлу. Поиск через оболочку и раскрытие `~` не используются. См. [Локальные сервисы моделей](</ru/gateway/local-model-services>) для всех полей `localService`.

## Think Max

ds4 применяет Think Max только когда оба условия истинны:

  * `ds4-server` запускается с `--ctx 393216` или выше.
  * Запрос использует `reasoning_effort: "max"` или эквивалентное поле усилия ds4.


Если вы запускаете такой большой контекст, обновите и флаги сервера, и метаданные модели OpenClaw:

json5Copy code
[code]
    {  contextWindow: 393216,  maxTokens: 384000,  compat: {    supportsUsageInStreaming: true,    supportsReasoningEffort: true,    maxTokensField: "max_tokens",    supportsStrictMode: false,    thinkingFormat: "deepseek",    supportedReasoningEfforts: ["low", "medium", "high", "xhigh", "max"],  },}
[/code]

## Тестирование

Начните с прямой HTTP-проверки:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"Reply with exactly: ds4-ok"}],"max_tokens":16,"stream":false,"thinking":{"type":"disabled"}}'
[/code]

Затем проверьте маршрутизацию модели OpenClaw:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

Для полного smoke-теста агента и вызова инструментов используйте контекст не меньше 32768:

bashCopy code
[code]
    openclaw agent \  --local \  --session-id ds4-tool-smoke \  --model ds4/deepseek-v4-flash \  --thinking off \  --message "Use the shell command pwd once, then reply exactly: tool-ok <output>" \  --json \  --timeout 240
[/code]

Ожидаемый результат:

  * `executionTrace.winnerProvider` равен `ds4`
  * `executionTrace.winnerModel` равен `deepseek-v4-flash`
  * `toolSummary.calls` не меньше `1`
  * `finalAssistantVisibleText` начинается с `tool-ok`


## Устранение неполадок

curl /v1/models cannot connect

ds4 не запущен или не привязан к хосту и порту из `baseUrl`. Запустите `ds4-server`, затем повторите попытку:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

500 prompt exceeds context

Настроенный `--ctx` слишком мал для хода OpenClaw. Увеличьте `ds4-server --ctx`, затем обновите `models.providers.ds4.models[].contextWindow`, чтобы значения совпадали. Полным ходам агента с инструментами требуется существенно больше контекста, чем прямому curl-запросу с одним сообщением.

Think Max does not activate

ds4 использует Think Max только когда `--ctx` не меньше `393216`, а запрос запрашивает `reasoning_effort: "max"`. Меньшие контексты откатываются к высокому уровню рассуждения.

The first request is slow

У ds4 есть фаза холодного размещения Metal и прогрева модели. Используйте `localService.readyTimeoutMs: 300000`, когда OpenClaw запускает сервер по требованию.

## Связанные материалы

[**Local model services** Запускайте локальные серверы моделей по требованию перед запросами к моделям. ](</ru/gateway/local-model-services>) [**Local models** Выбирайте и эксплуатируйте локальные бэкенды моделей. ](</ru/gateway/local-models>) [**Model providers** Настраивайте ссылки на провайдеров, аутентификацию и failover. ](</ru/concepts/model-providers>) [**DeepSeek** Нативное поведение провайдера DeepSeek и элементы управления thinking. ](</ru/providers/deepseek>)

Was this useful?YesNo

Open issue