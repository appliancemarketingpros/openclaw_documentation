---
title: Kilo Gateway
source_url: https://docs.openclaw.ai/uk/providers/kilocode
scraped_at: 2026-05-25
---

Kilo Gateway надає **єдиний API** , який маршрутизує запити до багатьох моделей через одну кінцеву точку й API-ключ. Він сумісний з OpenAI, тому більшість OpenAI SDK працюють після зміни базової URL-адреси.

Властивість | Значення  
---|---  
Провайдер | `kilocode`  
Автентифікація | `KILOCODE_API_KEY`  
API | сумісний з OpenAI  
Базова URL-адреса | `https://api.kilo.ai/api/gateway/`  
  
## Початок роботи

* ### Create an account

Перейдіть на [app.kilo.ai](<https://app.kilo.ai>), увійдіть або створіть обліковий запис, потім перейдіть до API Keys і згенеруйте новий ключ.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice kilocode-api-key
[/code]

Або задайте змінну середовища безпосередньо:

bashCopy code
[code]
    export KILOCODE_API_KEY="<your-kilocode-api-key>" # pragma: allowlist secret
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider kilocode
[/code]

## Модель за замовчуванням

Модель за замовчуванням — `kilocode/kilo/auto`, модель розумної маршрутизації, якою керує провайдер Kilo Gateway.

## Вбудований каталог

OpenClaw динамічно виявляє доступні моделі з Kilo Gateway під час запуску. Використовуйте `/models kilocode`, щоб побачити повний список моделей, доступних для вашого облікового запису.

Будь-яку модель, доступну на Gateway, можна використовувати з префіксом `kilocode/`:

Посилання на модель | Примітки  
---|---  
`kilocode/kilo/auto` | За замовчуванням — розумна маршрутизація  
`kilocode/anthropic/claude-sonnet-4` | Anthropic через Kilo  
`kilocode/openai/gpt-5.5` | OpenAI через Kilo  
`kilocode/google/gemini-3.1-pro-preview` | Google через Kilo  
...і багато інших | Використовуйте `/models kilocode`, щоб перелічити всі  
  
## Приклад конфігурації

json5Copy code
[code]
    {  env: { KILOCODE_API_KEY: "<your-kilocode-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "kilocode/kilo/auto" },    },  },}
[/code]

Transport and compatibility

Kilo Gateway задокументовано в джерелі як сумісний з OpenRouter, тому він залишається на проксі-подібному шляху, сумісному з OpenAI, а не на нативному формуванні запитів OpenAI.

  * Kilo-посилання на базі Gemini залишаються на проксі-Gemini шляху, тому OpenClaw зберігає санітизацію thought-signature Gemini там, без увімкнення нативної перевірки відтворення Gemini або bootstrap-переписувань.
  * Kilo Gateway використовує Bearer token із вашим API-ключем під капотом.

Stream wrapper and reasoning

Спільна потокова обгортка Kilo додає заголовок застосунку провайдера й нормалізує проксі-навантаження reasoning для підтримуваних конкретних посилань на моделі.

Troubleshooting

  * Якщо виявлення моделей не вдається під час запуску, OpenClaw повертається до вбудованого статичного каталогу, що містить `kilocode/kilo/auto`.
  * Переконайтеся, що ваш API-ключ дійсний і що у вашому обліковому записі Kilo увімкнено потрібні моделі.
  * Коли Gateway працює як daemon, переконайтеся, що `KILOCODE_API_KEY` доступний цьому процесу (наприклад, у `~/.openclaw/.env` або через `env.shellEnv`).


## Пов’язане

[**Model selection** Вибір провайдерів, посилань на моделі та поведінки failover. ](</uk/concepts/model-providers>) [**Configuration reference** Повний довідник конфігурації OpenClaw. ](</uk/gateway/configuration-reference>) [**Kilo Gateway** Панель керування Kilo Gateway, API-ключі та керування обліковим записом. ](<https://app.kilo.ai>)

Was this useful?YesNo