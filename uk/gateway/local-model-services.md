---
title: Локальні сервіси моделей
source_url: https://docs.openclaw.ai/uk/gateway/local-model-services
scraped_at: 2026-05-25
---

`models.providers.<id>.localService` дозволяє OpenClaw запускати належний провайдеру локальний сервер моделей на вимогу. Це конфігурація на рівні провайдера: коли вибрана модель належить цьому провайдеру, OpenClaw перевіряє службу, запускає процес, якщо endpoint недоступний, чекає готовності, а потім надсилає запит до моделі.

Використовуйте це для локальних серверів, які дорого тримати запущеними цілий день, або для ручних налаштувань, де вибору моделі має бути достатньо, щоб підняти backend.

## Як це працює

  1. Запит до моделі зіставляється з налаштованим провайдером.
  2. Якщо цей провайдер має `localService`, OpenClaw перевіряє `healthUrl`.
  3. Якщо перевірка успішна, OpenClaw використовує наявний сервер.
  4. Якщо перевірка неуспішна, OpenClaw запускає `command` з `args`.
  5. OpenClaw опитує готовність, доки не сплине `readyTimeoutMs`.
  6. Запит до моделі надсилається через звичайний транспорт провайдера.
  7. Якщо OpenClaw запустив процес і `idleStopMs` додатний, процес зупиняється після того, як останній активний запит простоював так довго.


OpenClaw не встановлює для цього launchd, systemd, Docker або daemon. Сервер є дочірнім процесом процесу OpenClaw, якому він уперше знадобився.

## Форма конфігурації

json5Copy code
[code]
    {  models: {    providers: {      local: {        baseUrl: "http://127.0.0.1:8000/v1",        apiKey: "local-model",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/absolute/path/to/server",          args: ["--host", "127.0.0.1", "--port", "8000"],          cwd: "/absolute/path/to/working-dir",          env: { LOCAL_MODEL_CACHE: "/absolute/path/to/cache" },          healthUrl: "http://127.0.0.1:8000/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "my-local-model",            name: "My Local Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## Поля

  * `command`: абсолютний шлях до виконуваного файла. Пошук через shell не використовується.
  * `args`: аргументи процесу. Розгортання shell, pipes, globbing або правила quoting не застосовуються.
  * `cwd`: необов’язковий робочий каталог для процесу.
  * `env`: необов’язкові змінні середовища, об’єднані поверх середовища процесу OpenClaw.
  * `healthUrl`: URL готовності. Якщо пропущено, OpenClaw додає `/models` до `baseUrl`, тож `http://127.0.0.1:8000/v1` стає `http://127.0.0.1:8000/v1/models`.
  * `readyTimeoutMs`: граничний час очікування готовності під час запуску. Типово: `120000`.
  * `idleStopMs`: затримка вимкнення через простій для процесів, запущених OpenClaw. `0` або пропущене значення тримає процес активним, доки OpenClaw не завершиться.


## Приклад Inferrs

Inferrs — це кастомний backend `/v1`, сумісний з OpenAI, тому той самий API локальної служби працює із записом провайдера `inferrs`.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "inferrs/google/gemma-4-E2B-it" },    },  },  models: {    mode: "merge",    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/opt/homebrew/bin/inferrs",          args: [            "serve",            "google/gemma-4-E2B-it",            "--host",            "127.0.0.1",            "--port",            "8080",            "--device",            "metal",          ],          healthUrl: "http://127.0.0.1:8080/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

Замініть `command` на результат `which inferrs` на машині, де запущено OpenClaw.

## Приклад ds4

json5Copy code
[code]
    {  models: {    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/Users/you/Projects/oss/ds4/ds4-server",          args: [            "--model",            "/Users/you/Projects/oss/ds4/ds4flash.gguf",            "--host",            "127.0.0.1",            "--port",            "18000",            "--ctx",            "393216",          ],          cwd: "/Users/you/Projects/oss/ds4",          healthUrl: "http://127.0.0.1:18000/v1/models",          readyTimeoutMs: 300000,          idleStopMs: 0,        },        models: [],      },    },  },}
[/code]

## Операційні нотатки

  * Один процес OpenClaw керує дочірнім процесом, який він запустив. Інший процес OpenClaw, який бачить, що той самий URL перевірки вже активний, повторно використає його без переймання керування.
  * Запуск серіалізується для кожної команди провайдера та набору аргументів, тому паралельні запити не створюють дублікати серверів для тієї самої конфігурації.
  * Активні streaming-відповіді утримують lease; вимкнення через простій чекає, доки обробка тіла відповіді завершиться.
  * Використовуйте `timeoutSeconds` для повільних локальних провайдерів, щоб холодні запуски й довгі генерації не впиралися в типовий timeout запиту до моделі.
  * Використовуйте явний `healthUrl`, якщо ваш сервер надає готовність десь іще, крім `/v1/models`.


## Пов’язане

[**Локальні моделі** Налаштування локальних моделей, вибір провайдера та рекомендації з безпеки. ](</uk/gateway/local-models>) [**Inferrs** Запускайте OpenClaw через локальний сервер inferrs, сумісний з OpenAI. ](</uk/providers/inferrs>)

Was this useful?YesNo