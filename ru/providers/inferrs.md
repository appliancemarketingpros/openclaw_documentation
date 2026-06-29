---
title: Выводит
source_url: https://docs.openclaw.ai/ru/providers/inferrs
scraped_at: 2026-06-29
---

ModelsProviders

[inferrs](<https://github.com/ericcurtin/inferrs>) может обслуживать локальные модели через OpenAI-совместимый API `/v1`. OpenClaw работает с `inferrs` через общий путь `openai-completions`.

Свойство | Значение  
---|---  
Идентификатор провайдера | `inferrs` (пользовательский; настраивается в `models.providers.inferrs`)  
Plugin | нет — `inferrs` не является встроенным Plugin провайдера OpenClaw  
Переменная окружения auth | Необязательно. Подойдет любое значение, если у вашего сервера inferrs нет auth  
API | OpenAI-совместимый (`openai-completions`)  
Предлагаемый базовый URL | `http://127.0.0.1:8080/v1` (или там, где находится ваш сервер inferrs)  
  
## Начало работы

* ### Запустите inferrs с моделью

bashCopy code
[code]
    inferrs serve google/gemma-4-E2B-it \  --host 127.0.0.1 \  --port 8080 \  --device metal
[/code]

* ### Проверьте, что сервер доступен

bashCopy code
[code]
    curl http://127.0.0.1:8080/healthcurl http://127.0.0.1:8080/v1/models
[/code]

* ### Добавьте запись провайдера OpenClaw

Добавьте явную запись провайдера и укажите ее для модели по умолчанию. Полный пример конфигурации см. ниже.

## Полный пример конфигурации

В этом примере используется Gemma 4 на локальном сервере `inferrs`.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "inferrs/google/gemma-4-E2B-it" },      models: {        "inferrs/google/gemma-4-E2B-it": {          alias: "Gemma 4 (inferrs)",        },      },    },  },  models: {    mode: "merge",    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

## Запуск по требованию

Inferrs также может запускаться OpenClaw только тогда, когда выбрана модель `inferrs/...`. Добавьте `localService` в ту же запись провайдера:

json5Copy code
[code]
    {  models: {    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/opt/homebrew/bin/inferrs",          args: [            "serve",            "google/gemma-4-E2B-it",            "--host",            "127.0.0.1",            "--port",            "8080",            "--device",            "metal",          ],          healthUrl: "http://127.0.0.1:8080/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

`command` должен быть абсолютным. Используйте `which inferrs` на хосте Gateway и поместите этот путь в конфигурацию. Полный справочник полей см. в разделе [Сервисы локальных моделей](</ru/gateway/local-model-services>).

## Расширенная конфигурация

Почему requiresStringContent важен

Некоторые маршруты Chat Completions в `inferrs` принимают только строковый `messages[].content`, а не структурированные массивы частей контента.

json5Copy code
[code]
    compat: {  requiresStringContent: true}
[/code]

OpenClaw преобразует части чисто текстового контента в обычные строки перед отправкой запроса.

Gemma и оговорка о схеме инструментов

Некоторые текущие сочетания `inferrs` \+ Gemma принимают небольшие прямые запросы `/v1/chat/completions`, но все равно завершаются ошибкой на полных ходах среды выполнения агента OpenClaw.

Если это происходит, сначала попробуйте следующее:

json5Copy code
[code]
    compat: {  requiresStringContent: true,  supportsTools: false}
[/code]

Это отключает поверхность схемы инструментов OpenClaw для модели и может снизить нагрузку промпта на более строгие локальные бэкенды.

Если крошечные прямые запросы по-прежнему работают, но обычные ходы агента OpenClaw продолжают падать внутри `inferrs`, оставшаяся проблема обычно связана с поведением вышестоящей модели или сервера, а не с транспортным уровнем OpenClaw.

Ручная smoke-проверка

После настройки протестируйте оба уровня:

bashCopy code
[code]
    curl http://127.0.0.1:8080/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"google/gemma-4-E2B-it","messages":[{"role":"user","content":"What is 2 + 2?"}],"stream":false}'
[/code]

bashCopy code
[code]
    openclaw infer model run \  --model inferrs/google/gemma-4-E2B-it \  --prompt "What is 2 + 2? Reply with one short sentence." \  --json
[/code]

Если первая команда работает, а вторая завершается ошибкой, проверьте раздел устранения неполадок ниже.

Поведение в стиле прокси

`inferrs` рассматривается как OpenAI-совместимый бэкенд `/v1` в стиле прокси, а не как нативная конечная точка OpenAI.

  * Формирование запросов, предназначенное только для нативного OpenAI, здесь не применяется
  * Нет `service_tier`, нет Responses `store`, нет подсказок prompt-cache и нет формирования полезной нагрузки совместимости reasoning OpenAI
  * Скрытые заголовки атрибуции OpenClaw (`originator`, `version`, `User-Agent`) не внедряются для пользовательских базовых URL `inferrs`


## Устранение неполадок

curl /v1/models завершается ошибкой

`inferrs` не запущен, недоступен или не привязан к ожидаемым хосту/порту. Убедитесь, что сервер запущен и слушает адрес, который вы настроили.

messages[].content expected a string

Задайте `compat.requiresStringContent: true` в записи модели. Подробнее см. раздел `requiresStringContent` выше.

Прямые вызовы /v1/chat/completions проходят, но openclaw infer model run завершается ошибкой

Попробуйте задать `compat.supportsTools: false`, чтобы отключить поверхность схемы инструментов. См. оговорку о схеме инструментов Gemma выше.

inferrs все еще падает на более крупных ходах агента

Если OpenClaw больше не получает ошибок схемы, но `inferrs` все еще падает на более крупных ходах агента, рассматривайте это как ограничение вышестоящего `inferrs` или модели. Снизьте нагрузку промпта или перейдите на другой локальный бэкенд либо модель.

## Связанные материалы

[**Локальные модели** Запуск OpenClaw с локальными серверами моделей. ](</ru/gateway/local-models>) [**Сервисы локальных моделей** Запуск локальных серверов моделей по требованию для настроенных провайдеров. ](</ru/gateway/local-model-services>) [**Устранение неполадок Gateway** Отладка локальных OpenAI-совместимых бэкендов, которые проходят пробы, но завершаются ошибкой при запусках агента. ](</ru/gateway/troubleshooting#local-openai-compatible-backend-passes-direct-probes-but-agent-runs-fail>) [**Выбор модели** Обзор всех провайдеров, ссылок на модели и поведения при отказе. ](</ru/concepts/model-providers>)

Was this useful?YesNo

Open issue