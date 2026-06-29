---
title: ds4
source_url: https://docs.openclaw.ai/uk/providers/ds4
scraped_at: 2026-06-29
---

ModelsProviders

[ds4](<https://github.com/antirez/ds4>) обслуговує DeepSeek V4 Flash з локального бекенду Metal через OpenAI-сумісний API `/v1`. OpenClaw підключається до ds4 через загальну родину провайдерів `openai-completions`.

ds4 не є вбудованим Plugin провайдера OpenClaw. Налаштуйте його в `models.providers.ds4`, а потім виберіть `ds4/deepseek-v4-flash`.

  * Ідентифікатор провайдера: `ds4`
  * Plugin: немає
  * API: OpenAI-сумісні Chat Completions (`openai-completions`)
  * Рекомендована базова URL-адреса: `http://127.0.0.1:18000/v1`
  * Ідентифікатор моделі: `deepseek-v4-flash`
  * Виклики інструментів: підтримуються через OpenAI-стиль `tools` і `tool_calls`
  * Міркування: DeepSeek-стиль `thinking` і `reasoning_effort`


## Вимоги

  * macOS із підтримкою Metal.
  * Робоча копія ds4 з `ds4-server` і файлом DeepSeek V4 Flash GGUF.
  * Достатньо пам'яті для вибраного контексту. Більші значення `--ctx` виділяють більше пам'яті KV під час запуску сервера.


## Швидкий старт

* ### Запустіть ds4-server

Замініть `&lt;DS4_DIR&gt;` на шлях до вашої копії ds4.

bashCopy code
[code]
    &lt;DS4_DIR&gt;/ds4-server \  --model &lt;DS4_DIR&gt;/ds4flash.gguf \  --host 127.0.0.1 \  --port 18000 \  --ctx 32768 \  --tokens 128
[/code]

* ### Перевірте OpenAI-сумісну кінцеву точку

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

Відповідь має містити `deepseek-v4-flash`.

* ### Додайте конфігурацію провайдера OpenClaw

Додайте конфігурацію з розділу Повна конфігурація, а потім запустіть одноразову перевірку моделі:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

## Повна конфігурація

Використовуйте цю конфігурацію, коли ds4 уже працює на `127.0.0.1:18000`.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "ds4/deepseek-v4-flash" },      models: {        "ds4/deepseek-v4-flash": {          alias: "DS4 local",        },      },    },  },  models: {    mode: "merge",    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

Тримайте `contextWindow` узгодженим зі значенням `ds4-server --ctx`. Тримайте `maxTokens` узгодженим із `--tokens`, якщо ви навмисно не хочете, щоб OpenClaw запитував менше виводу, ніж стандартно задає сервер.

## Запуск на вимогу

OpenClaw може запускати ds4 лише тоді, коли вибрано модель `ds4/...`. Додайте `localService` до того самого запису провайдера:

json5Copy code
[code]
    {  models: {    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "&lt;DS4_DIR&gt;/ds4-server",          args: [            "--model",            "&lt;DS4_DIR&gt;/ds4flash.gguf",            "--host",            "127.0.0.1",            "--port",            "18000",            "--ctx",            "32768",            "--tokens",            "128",          ],          cwd: "&lt;DS4_DIR&gt;",          healthUrl: "http://127.0.0.1:18000/v1/models",          readyTimeoutMs: 300000,          idleStopMs: 0,        },        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

`command` має бути абсолютним шляхом до виконуваного файлу. Пошук через shell і розгортання `~` не використовуються. Усі поля `localService` дивіться в розділі [Локальні сервіси моделей](</uk/gateway/local-model-services>).

## Think Max

ds4 застосовує Think Max лише тоді, коли обидві умови істинні:

  * `ds4-server` запускається з `--ctx 393216` або більшим значенням.
  * Запит використовує `reasoning_effort: "max"` або еквівалентне поле зусилля ds4.


Якщо ви запускаєте такий великий контекст, оновіть і прапорці сервера, і метадані моделі OpenClaw:

json5Copy code
[code]
    {  contextWindow: 393216,  maxTokens: 384000,  compat: {    supportsUsageInStreaming: true,    supportsReasoningEffort: true,    maxTokensField: "max_tokens",    supportsStrictMode: false,    thinkingFormat: "deepseek",    supportedReasoningEfforts: ["low", "medium", "high", "xhigh", "max"],  },}
[/code]

## Тестування

Почніть із прямої перевірки HTTP:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"Reply with exactly: ds4-ok"}],"max_tokens":16,"stream":false,"thinking":{"type":"disabled"}}'
[/code]

Потім протестуйте маршрутизацію моделі OpenClaw:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

Для повного димового тесту агента й виклику інструментів використовуйте контекст щонайменше 32768:

bashCopy code
[code]
    openclaw agent \  --local \  --session-id ds4-tool-smoke \  --model ds4/deepseek-v4-flash \  --thinking off \  --message "Use the shell command pwd once, then reply exactly: tool-ok <output>" \  --json \  --timeout 240
[/code]

Очікуваний результат:

  * `executionTrace.winnerProvider` дорівнює `ds4`
  * `executionTrace.winnerModel` дорівнює `deepseek-v4-flash`
  * `toolSummary.calls` становить щонайменше `1`
  * `finalAssistantVisibleText` починається з `tool-ok`


## Усунення неполадок

curl /v1/models не може підключитися

ds4 не запущено або він не прив'язаний до хоста й порту в `baseUrl`. Запустіть `ds4-server`, а потім повторіть спробу:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

500 prompt exceeds context

Налаштоване значення `--ctx` замале для ходу OpenClaw. Збільште `ds4-server --ctx`, а потім оновіть `models.providers.ds4.models[].contextWindow`, щоб воно збігалося. Повним ходам агента з інструментами потрібно значно більше контексту, ніж прямому curl-запиту з одним повідомленням.

Think Max не активується

ds4 використовує Think Max лише тоді, коли `--ctx` становить щонайменше `393216`, а запит просить `reasoning_effort: "max"`. Менші контексти повертаються до високого міркування.

Перший запит повільний

ds4 має фазу холодного розміщення Metal і прогрівання моделі. Використовуйте `localService.readyTimeoutMs: 300000`, коли OpenClaw запускає сервер на вимогу.

## Пов'язане

[**Локальні сервіси моделей** Запускайте локальні сервери моделей на вимогу перед запитами до моделі. ](</uk/gateway/local-model-services>) [**Локальні моделі** Вибирайте й експлуатуйте локальні бекенди моделей. ](</uk/gateway/local-models>) [**Провайдери моделей** Налаштовуйте посилання на провайдерів, автентифікацію та failover. ](</uk/concepts/model-providers>) [**DeepSeek** Нативна поведінка провайдера DeepSeek і елементи керування мисленням. ](</uk/providers/deepseek>)

Was this useful?YesNo

Open issue