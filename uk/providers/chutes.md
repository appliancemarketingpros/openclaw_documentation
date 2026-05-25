---
title: Chutes
source_url: https://docs.openclaw.ai/uk/providers/chutes
scraped_at: 2026-05-25
---

[Chutes](<https://chutes.ai>) надає каталоги моделей із відкритим кодом через API, сумісний з OpenAI. OpenClaw підтримує як браузерний OAuth, так і пряму автентифікацію ключем API для вбудованого провайдера `chutes`.

Властивість | Значення  
---|---  
Провайдер | `chutes`  
API | сумісний з OpenAI  
Базовий URL | `https://llm.chutes.ai/v1`  
Автентифікація | OAuth або ключ API (див. нижче)  
  
## Початок роботи

### OAuth

* ### Запустіть процес онбордингу OAuth

bashCopy code
[code]
    openclaw onboard --auth-choice chutes
[/code]

OpenClaw запускає браузерний процес локально або показує URL + процес вставлення перенаправлення на віддалених/безголових хостах. Токени OAuth автоматично оновлюються через профілі автентифікації OpenClaw.

* ### Перевірте модель за замовчуванням

Після онбордингу модель за замовчуванням встановлюється на `chutes/zai-org/GLM-4.7-TEE`, а вбудований каталог Chutes реєструється.

### Ключ API

* ### Отримайте ключ API

Створіть ключ на сторінці [chutes.ai/settings/api-keys](<https://chutes.ai/settings/api-keys>).

* ### Запустіть процес онбордингу ключа API

bashCopy code
[code]
    openclaw onboard --auth-choice chutes-api-key
[/code]

* ### Перевірте модель за замовчуванням

Після онбордингу модель за замовчуванням встановлюється на `chutes/zai-org/GLM-4.7-TEE`, а вбудований каталог Chutes реєструється.

## Поведінка виявлення

Коли автентифікація Chutes доступна, OpenClaw запитує каталог Chutes із цими обліковими даними й використовує виявлені моделі. Якщо виявлення завершується невдало, OpenClaw повертається до вбудованого статичного каталогу, тож онбординг і запуск однаково працюють.

## Псевдоніми за замовчуванням

OpenClaw реєструє три зручні псевдоніми для вбудованого каталогу Chutes:

Псевдонім | Цільова модель  
---|---  
`chutes-fast` | `chutes/zai-org/GLM-4.7-FP8`  
`chutes-pro` | `chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes-vision` | `chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
  
## Вбудований стартовий каталог

Вбудований резервний каталог містить поточні refs Chutes:

Посилання на модель  
---  
`chutes/zai-org/GLM-4.7-TEE`  
`chutes/zai-org/GLM-5-TEE`  
`chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes/deepseek-ai/DeepSeek-R1-0528-TEE`  
`chutes/moonshotai/Kimi-K2.5-TEE`  
`chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
`chutes/Qwen/Qwen3-Coder-Next-TEE`  
`chutes/openai/gpt-oss-120b-TEE`  
  
## Приклад конфігурації

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "chutes/zai-org/GLM-4.7-TEE" },      models: {        "chutes/zai-org/GLM-4.7-TEE": { alias: "Chutes GLM 4.7" },        "chutes/deepseek-ai/DeepSeek-V3.2-TEE": { alias: "Chutes DeepSeek V3.2" },      },    },  },}
[/code]

Перевизначення OAuth

Ви можете налаштувати процес OAuth за допомогою необов’язкових змінних середовища:

Змінна | Призначення  
---|---  
`CHUTES_CLIENT_ID` | Власний ідентифікатор клієнта OAuth  
`CHUTES_CLIENT_SECRET` | Власний секрет клієнта OAuth  
`CHUTES_OAUTH_REDIRECT_URI` | Власний URI перенаправлення  
`CHUTES_OAUTH_SCOPES` | Власні області OAuth  
  
Див. [документацію Chutes OAuth](<https://chutes.ai/docs/sign-in-with-chutes/overview>) щодо вимог до застосунків перенаправлення та довідки.

Примітки

  * Виявлення за ключем API та OAuth використовують той самий id провайдера `chutes`.
  * Моделі Chutes реєструються як `chutes/<model-id>`.
  * Якщо виявлення під час запуску завершується невдало, автоматично використовується вбудований статичний каталог.


## Пов’язане

[**Вибір моделі** Правила провайдерів, refs моделей і поведінка відмовостійкого перемикання. ](</uk/concepts/model-providers>) [**Довідник із конфігурації** Повна схема конфігурації, включно з налаштуваннями провайдера. ](</uk/gateway/configuration-reference>) [**Chutes** Панель Chutes і документація API. ](<https://chutes.ai>) [**Ключі API Chutes** Створюйте ключі API Chutes і керуйте ними. ](<https://chutes.ai/settings/api-keys>)

Was this useful?YesNo