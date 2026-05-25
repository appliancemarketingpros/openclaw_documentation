---
title: Arcee AI
source_url: https://docs.openclaw.ai/uk/providers/arcee
scraped_at: 2026-05-25
---

[Arcee AI](<https://arcee.ai>) надає доступ до сімейства моделей Trinity типу mixture-of-experts через API, сумісний з OpenAI. Усі моделі Trinity ліцензовано за Apache 2.0.

До моделей Arcee AI можна отримати доступ безпосередньо через платформу Arcee або через [OpenRouter](</uk/providers/openrouter>).

Властивість | Значення  
---|---  
Провайдер | `arcee`  
Автентифікація | `ARCEEAI_API_KEY` (безпосередньо) або `OPENROUTER_API_KEY` (через OpenRouter)  
API | Сумісний з OpenAI  
Базова URL-адреса | `https://api.arcee.ai/api/v1` (безпосередньо) або `https://openrouter.ai/api/v1` (OpenRouter)  
  
## Початок роботи

### Direct (Arcee platform)

* ### Get an API key

Створіть API-ключ в [Arcee AI](<https://chat.arcee.ai/>).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-api-key
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

### Via OpenRouter

* ### Get an API key

Створіть API-ключ в [OpenRouter](<https://openrouter.ai/keys>).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-openrouter
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

Ті самі посилання на моделі працюють як для безпосереднього налаштування, так і для налаштування через OpenRouter (наприклад, `arcee/trinity-large-thinking`).

## Неінтерактивне налаштування

### Direct (Arcee platform)

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-api-key \  --arceeai-api-key "$ARCEEAI_API_KEY"
[/code]

### Via OpenRouter

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-openrouter \  --openrouter-api-key "$OPENROUTER_API_KEY"
[/code]

## Вбудований каталог

OpenClaw наразі постачається з цим вбудованим каталогом Arcee:

Посилання на модель | Назва | Вхід | Контекст | Вартість (вхід/вихід за 1 млн) | Примітки  
---|---|---|---|---|---  
`arcee/trinity-large-thinking` | Trinity Large Thinking | текст | 256K | $0.25 / $0.90 | Модель за замовчуванням; reasoning увімкнено  
`arcee/trinity-large-preview` | Trinity Large Preview | текст | 128K | $0.25 / $1.00 | Загального призначення; 400B параметрів, 13B активних  
`arcee/trinity-mini` | Trinity Mini 26B | текст | 128K | $0.045 / $0.15 | Швидка та економічна; виклик функцій  
  
## Підтримувані можливості

Можливість | Підтримується  
---|---  
Потокове передавання | Так  
Використання інструментів / виклик функцій | Так (Trinity Mini, Trinity Large Preview)  
Структурований вивід (режим JSON і схема JSON) | Так  
Розширене мислення | Так (Trinity Large Thinking; інструменти вимкнено)  
  
Environment note

Якщо Gateway працює як демон (launchd/systemd), переконайтеся, що `ARCEEAI_API_KEY` (або `OPENROUTER_API_KEY`) доступний цьому процесу (наприклад, у `~/.openclaw/.env` або через `env.shellEnv`).

OpenRouter routing

Під час використання моделей Arcee через OpenRouter застосовуються ті самі посилання на моделі `arcee/*`. OpenClaw прозоро обробляє маршрутизацію на основі вашого вибору автентифікації. Див. [документацію провайдера OpenRouter](</uk/providers/openrouter>), щоб дізнатися подробиці конфігурації, специфічні для OpenRouter.

## Пов’язане

[**OpenRouter** Отримуйте доступ до моделей Arcee та багатьох інших через один API-ключ. ](</uk/providers/openrouter>) [**Model selection** Вибір провайдерів, посилань на моделі та поведінки failover. ](</uk/concepts/model-providers>)

Was this useful?YesNo