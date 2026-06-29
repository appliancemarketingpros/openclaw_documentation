---
title: Локальные сервисы моделей
source_url: https://docs.openclaw.ai/ru/gateway/local-model-services
scraped_at: 2026-06-29
---

Gateway & OpsGateway

`models.providers.<id>.localService` позволяет OpenClaw запускать принадлежащий провайдеру локальный сервер моделей по требованию. Это конфигурация уровня провайдера: когда выбранная модель принадлежит этому провайдеру, OpenClaw проверяет сервис, запускает процесс, если endpoint недоступен, дожидается готовности, а затем отправляет запрос к модели.

Используйте это для локальных серверов, которые дорого держать запущенными весь день, или для ручных настроек, где выбора модели должно быть достаточно, чтобы поднять backend.

## Как это работает

  1. Запрос к модели разрешается в настроенного провайдера.
  2. Если у этого провайдера есть `localService`, OpenClaw проверяет `healthUrl`.
  3. Если проверка успешна, OpenClaw использует существующий сервер.
  4. Если проверка завершается ошибкой, OpenClaw запускает `command` с `args`.
  5. OpenClaw опрашивает готовность до истечения `readyTimeoutMs`.
  6. Запрос к модели отправляется через обычный транспорт провайдера.
  7. Если OpenClaw запустил процесс и `idleStopMs` положителен, процесс останавливается после того, как последний выполняющийся запрос простаивал это время.


OpenClaw не устанавливает для этого launchd, systemd, Docker или daemon. Сервер является дочерним процессом процесса OpenClaw, которому он первым понадобился.

## Форма конфигурации

json5Copy code
[code]
    {  models: {    providers: {      local: {        baseUrl: "http://127.0.0.1:8000/v1",        apiKey: "local-model",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/absolute/path/to/server",          args: ["--host", "127.0.0.1", "--port", "8000"],          cwd: "/absolute/path/to/working-dir",          env: { LOCAL_MODEL_CACHE: "/absolute/path/to/cache" },          healthUrl: "http://127.0.0.1:8000/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "my-local-model",            name: "My Local Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## Поля

  * `command`: абсолютный путь к исполняемому файлу. Поиск через shell не используется.
  * `args`: аргументы процесса. Расширение shell, pipes, globbing или правила quoting не применяются.
  * `cwd`: необязательный рабочий каталог для процесса.
  * `env`: необязательные переменные окружения, объединяемые поверх окружения процесса OpenClaw.
  * `healthUrl`: URL готовности. Если он опущен, OpenClaw добавляет `/models` к `baseUrl`, поэтому `http://127.0.0.1:8000/v1` становится `http://127.0.0.1:8000/v1/models`.
  * `readyTimeoutMs`: крайний срок готовности при запуске. По умолчанию: `120000`.
  * `idleStopMs`: задержка остановки при простое для процессов, запущенных OpenClaw. `0` или пропуск оставляет процесс живым до выхода OpenClaw.


## Пример Inferrs

Inferrs — это пользовательский OpenAI-совместимый backend `/v1`, поэтому тот же API локального сервиса работает с записью провайдера `inferrs`.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "inferrs/google/gemma-4-E2B-it" },    },  },  models: {    mode: "merge",    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/opt/homebrew/bin/inferrs",          args: [            "serve",            "google/gemma-4-E2B-it",            "--host",            "127.0.0.1",            "--port",            "8080",            "--device",            "metal",          ],          healthUrl: "http://127.0.0.1:8080/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

Замените `command` результатом `which inferrs` на машине, где запущен OpenClaw.

## Пример ds4

Полную настройку, рекомендации по размеру контекста и команды проверки см. в [ds4](</ru/providers/ds4>).

json5Copy code
[code]
    {  models: {    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "&lt;DS4_DIR&gt;/ds4-server",          args: [            "--model",            "&lt;DS4_DIR&gt;/ds4flash.gguf",            "--host",            "127.0.0.1",            "--port",            "18000",            "--ctx",            "32768",            "--tokens",            "128",          ],          cwd: "&lt;DS4_DIR&gt;",          healthUrl: "http://127.0.0.1:18000/v1/models",          readyTimeoutMs: 300000,          idleStopMs: 0,        },        models: [],      },    },  },}
[/code]

## Операционные заметки

  * Один процесс OpenClaw управляет дочерним процессом, который он запустил. Другой процесс OpenClaw, увидев тот же уже работающий URL проверки, переиспользует его без принятия под управление.
  * Запуск сериализуется для каждого набора команды и аргументов провайдера, поэтому параллельные запросы не создают дублирующиеся серверы для одной конфигурации.
  * Активные потоковые ответы удерживают lease; остановка при простое ждет, пока обработка тела ответа завершится.
  * Используйте `timeoutSeconds` для медленных локальных провайдеров, чтобы холодные запуски и долгие генерации не упирались в стандартный timeout запроса к модели.
  * Используйте явный `healthUrl`, если ваш сервер публикует готовность где-то еще, кроме `/v1/models`.


## Связанные материалы

[**Локальные модели** Настройка локальных моделей, выбор провайдера и рекомендации по безопасности. ](</ru/gateway/local-models>) [**Inferrs** Запускайте OpenClaw через OpenAI-совместимый локальный сервер inferrs. ](</ru/providers/inferrs>)

Was this useful?YesNo

Open issue