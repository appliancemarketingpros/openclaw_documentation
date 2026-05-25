---
title: Виводить
source_url: https://docs.openclaw.ai/uk/providers/inferrs
scraped_at: 2026-05-25
---

[inferrs](<https://github.com/ericcurtin/inferrs>) може обслуговувати локальні моделі за OpenAI-сумісним API `/v1`. OpenClaw працює з `inferrs` через загальний шлях `openai-completions`.

Властивість | Значення  
---|---  
ID провайдера | `inferrs` (користувацький; налаштовується в `models.providers.inferrs`)  
Plugin | немає — `inferrs` не є вбудованим Plugin провайдера OpenClaw  
Змінна env для автентифікації | Необов’язкова. Будь-яке значення працює, якщо ваш сервер inferrs не має автентифікації  
API | OpenAI-сумісний (`openai-completions`)  
Пропонована базова URL-адреса | `http://127.0.0.1:8080/v1` (або там, де працює ваш сервер inferrs)  
  
## Початок роботи

* ### Запустіть inferrs із моделлю

bashCopy code
[code]
    inferrs serve google/gemma-4-E2B-it \  --host 127.0.0.1 \  --port 8080 \  --device metal
[/code]

* ### Перевірте, що сервер доступний

bashCopy code
[code]
    curl http://127.0.0.1:8080/healthcurl http://127.0.0.1:8080/v1/models
[/code]

* ### Додайте запис провайдера OpenClaw

Додайте явний запис провайдера та спрямуйте на нього вашу модель за замовчуванням. Повний приклад конфігурації наведено нижче.

## Повний приклад конфігурації

У цьому прикладі використовується Gemma 4 на локальному сервері `inferrs`.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "inferrs/google/gemma-4-E2B-it" },      models: {        "inferrs/google/gemma-4-E2B-it": {          alias: "Gemma 4 (inferrs)",        },      },    },  },  models: {    mode: "merge",    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

## Запуск на вимогу

Inferrs також може запускатися OpenClaw лише тоді, коли вибрано модель `inferrs/...`. Додайте `localService` до того самого запису провайдера:

json5Copy code
[code]
    {  models: {    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/opt/homebrew/bin/inferrs",          args: [            "serve",            "google/gemma-4-E2B-it",            "--host",            "127.0.0.1",            "--port",            "8080",            "--device",            "metal",          ],          healthUrl: "http://127.0.0.1:8080/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

`command` має бути абсолютним. Використайте `which inferrs` на хості Gateway і вкажіть цей шлях у конфігурації. Повний довідник полів див. у [Служби локальних моделей](</uk/gateway/local-model-services>).

## Розширена конфігурація

Чому requiresStringContent важливий

Деякі маршрути Chat Completions у `inferrs` приймають лише рядковий `messages[].content`, а не структуровані масиви частин вмісту.

json5Copy code
[code]
    compat: {  requiresStringContent: true}
[/code]

OpenClaw перетворить частини суто текстового вмісту на прості рядки перед надсиланням запиту.

Застереження щодо Gemma і схем інструментів

Деякі поточні комбінації `inferrs` \+ Gemma приймають невеликі прямі запити `/v1/chat/completions`, але все одно дають збій на повних ходах agent-runtime OpenClaw.

Якщо це трапляється, спершу спробуйте таке:

json5Copy code
[code]
    compat: {  requiresStringContent: true,  supportsTools: false}
[/code]

Це вимикає поверхню схем інструментів OpenClaw для моделі й може зменшити навантаження промпта на суворіші локальні бекенди.

Якщо крихітні прямі запити все ще працюють, але звичайні ходи агента OpenClaw продовжують аварійно завершуватися всередині `inferrs`, решта проблеми зазвичай пов’язана з поведінкою upstream-моделі або сервера, а не з транспортним шаром OpenClaw.

Ручний smoke-тест

Після налаштування перевірте обидва шари:

bashCopy code
[code]
    curl http://127.0.0.1:8080/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"google/gemma-4-E2B-it","messages":[{"role":"user","content":"What is 2 + 2?"}],"stream":false}'
[/code]

bashCopy code
[code]
    openclaw infer model run \  --model inferrs/google/gemma-4-E2B-it \  --prompt "What is 2 + 2? Reply with one short sentence." \  --json
[/code]

Якщо перша команда працює, а друга завершується помилкою, перегляньте розділ усунення несправностей нижче.

Поведінка у стилі проксі

`inferrs` розглядається як OpenAI-сумісний бекенд `/v1` у стилі проксі, а не як нативна кінцева точка OpenAI.

  * Формування запитів, призначене лише для нативного OpenAI, тут не застосовується
  * Немає `service_tier`, немає Responses `store`, немає підказок prompt-cache і немає формування payload для сумісності reasoning OpenAI
  * Приховані заголовки атрибуції OpenClaw (`originator`, `version`, `User-Agent`) не додаються до користувацьких базових URL-адрес `inferrs`


## Усунення несправностей

curl /v1/models завершується помилкою

`inferrs` не запущено, він недоступний або не прив’язаний до очікуваного хоста/порту. Переконайтеся, що сервер запущено й він прослуховує адресу, яку ви налаштували.

messages[].content очікує рядок

Задайте `compat.requiresStringContent: true` у записі моделі. Докладніше див. розділ `requiresStringContent` вище.

Прямі виклики /v1/chat/completions проходять, але openclaw infer model run завершується помилкою

Спробуйте задати `compat.supportsTools: false`, щоб вимкнути поверхню схем інструментів. Див. застереження щодо схем інструментів Gemma вище.

inferrs все ще аварійно завершується на більших ходах агента

Якщо OpenClaw більше не отримує помилок схеми, але `inferrs` усе ще аварійно завершується на більших ходах агента, розглядайте це як обмеження upstream `inferrs` або моделі. Зменште навантаження промпта або перейдіть на інший локальний бекенд чи модель.

## Пов’язане

[**Локальні моделі** Запуск OpenClaw із локальними серверами моделей. ](</uk/gateway/local-models>) [**Служби локальних моделей** Запуск локальних серверів моделей на вимогу для налаштованих провайдерів. ](</uk/gateway/local-model-services>) [**Усунення несправностей Gateway** Налагодження локальних OpenAI-сумісних бекендів, які проходять перевірки, але дають збій під час запусків агента. ](</uk/gateway/troubleshooting#local-openai-compatible-backend-passes-direct-probes-but-agent-runs-fail>) [**Вибір моделі** Огляд усіх провайдерів, посилань на моделі та поведінки failover. ](</uk/concepts/model-providers>)

Was this useful?YesNo