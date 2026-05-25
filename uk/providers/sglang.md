---
title: SGLang
source_url: https://docs.openclaw.ai/uk/providers/sglang
scraped_at: 2026-05-25
---

SGLang обслуговує моделі з відкритими вагами через HTTP API, сумісний з OpenAI. OpenClaw підключається до SGLang за допомогою сімейства провайдерів `openai-completions` з автоматичним виявленням доступних моделей.

Властивість | Значення  
---|---  
Ідентифікатор провайдера | `sglang`  
Plugin | вбудований, `enabledByDefault: true`  
Змінна середовища автентифікації | `SGLANG_API_KEY` (будь-яке непорожнє значення, якщо сервер не має автентифікації)  
Прапорець початкового налаштування | `--auth-choice sglang`  
API | сумісний з OpenAI (`openai-completions`)  
Базова URL-адреса за замовчуванням | `http://127.0.0.1:30000/v1`  
Заповнювач моделі за замовчуванням | `sglang/Qwen/Qwen3-8B`  
Використання потокової передачі | Так (`supportsStreamingUsage: true`)  
Ціноутворення | Позначено як зовнішньо безкоштовне (`modelPricing.external: false`)  
  
OpenClaw також **автоматично виявляє** доступні моделі з SGLang, коли ви вмикаєте це за допомогою `SGLANG_API_KEY`. Використовуйте `sglang/*` у `agents.defaults.models`, щоб зберегти динамічне виявлення, коли ви також налаштовуєте власну базову URL-адресу SGLang. Див. Виявлення моделей (неявний провайдер) нижче.

## Початок роботи

* ### Запустіть SGLang

Запустіть SGLang із сервером, сумісним з OpenAI. Ваша базова URL-адреса має надавати кінцеві точки `/v1` (наприклад, `/v1/models`, `/v1/chat/completions`). SGLang зазвичай працює на:

  * `http://127.0.0.1:30000/v1`


* ### Установіть API-ключ

Підійде будь-яке значення, якщо на вашому сервері не налаштовано автентифікацію:

bashCopy code
[code]
    export SGLANG_API_KEY="sglang-local"
[/code]

* ### Запустіть початкове налаштування або задайте модель напряму

bashCopy code
[code]
    openclaw onboard
[/code]

Або налаштуйте модель вручну:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "sglang/your-model-id" },    },  },}
[/code]

## Виявлення моделей (неявний провайдер)

Коли встановлено `SGLANG_API_KEY` (або існує профіль автентифікації), і ви **не** визначаєте `models.providers.sglang`, OpenClaw виконає запит:

  * `GET http://127.0.0.1:30000/v1/models`


і перетворить повернуті ідентифікатори на записи моделей.

## Явна конфігурація (моделі вручну)

Використовуйте явну конфігурацію, коли:

  * SGLang працює на іншому хості або порту.
  * Ви хочете закріпити значення `contextWindow`/`maxTokens`.
  * Ваш сервер потребує справжнього API-ключа (або ви хочете керувати заголовками).

json5Copy code
[code]
    {  models: {    providers: {      sglang: {        baseUrl: "http://127.0.0.1:30000/v1",        apiKey: "${SGLANG_API_KEY}",        api: "openai-completions",        models: [          {            id: "your-model-id",            name: "Local SGLang Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## Розширена конфігурація

Поведінка в стилі проксі

SGLang розглядається як проксі-бекенд `/v1`, сумісний з OpenAI, а не як нативна кінцева точка OpenAI.

Поведінка | SGLang  
---|---  
Формування запитів лише для OpenAI | Не застосовується  
`service_tier`, Responses `store`, підказки кешу промптів | Не надсилаються  
Формування корисного навантаження для сумісності reasoning | Не застосовується  
Приховані заголовки атрибуції (`originator`, `version`, `User-Agent`) | Не вставляються для власних базових URL-адрес SGLang  
Усунення несправностей

**Сервер недоступний**

Переконайтеся, що сервер запущений і відповідає:

bashCopy code
[code]
    curl http://127.0.0.1:30000/v1/models
[/code]

**Помилки автентифікації**

Якщо запити завершуються помилками автентифікації, установіть справжній `SGLANG_API_KEY`, який відповідає конфігурації вашого сервера, або явно налаштуйте провайдера в `models.providers.sglang`.

## Пов’язане

[**Вибір моделі** Вибір провайдерів, посилань на моделі та поведінки перемикання після збою. ](</uk/concepts/model-providers>) [**Довідник конфігурації** Повна схема конфігурації, включно із записами провайдерів. ](</uk/gateway/configuration-reference>)

Was this useful?YesNo