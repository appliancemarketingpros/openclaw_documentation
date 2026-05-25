---
title: Cerebras
source_url: https://docs.openclaw.ai/uk/providers/cerebras
scraped_at: 2026-05-25
---

[Cerebras](<https://www.cerebras.ai>) надає високошвидкісний OpenAI-сумісний інференс на спеціалізованому апаратному забезпеченні для інференсу. OpenClaw містить вбудований Plugin провайдера Cerebras зі статичним каталогом із чотирьох моделей.

Властивість | Значення  
---|---  
Ідентифікатор провайдера | `cerebras`  
Plugin | вбудований, `enabledByDefault: true`  
Змінна середовища автентифікації | `CEREBRAS_API_KEY`  
Прапорець початкового налаштування | `--auth-choice cerebras-api-key`  
Прямий прапорець CLI | `--cerebras-api-key <key>`  
API | OpenAI-сумісний (`openai-completions`)  
Базова URL-адреса | `https://api.cerebras.ai/v1`  
Модель за замовчуванням | `cerebras/zai-glm-4.7`  
  
## Початок роботи

* ### Отримайте API-ключ

Створіть API-ключ у [Cerebras Cloud Console](<https://cloud.cerebras.ai>).

* ### Запустіть початкове налаштування

Початкове налаштуванняCopy code
[code]
    openclaw onboard --auth-choice cerebras-api-key
[/code]

Прямий прапорецьCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice cerebras-api-key \--cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

Лише змінна середовищаCopy code
[code]
    export CEREBRAS_API_KEY=csk-...
[/code]

* ### Перевірте, що моделі доступні

bashCopy code
[code]
    openclaw models list --provider cerebras
[/code]

Список має містити всі чотири вбудовані моделі. Якщо `CEREBRAS_API_KEY` не розв’язано, `openclaw models status --json` повідомить про відсутні облікові дані в `auth.unusableProfiles`.

## Неінтерактивне налаштування

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cerebras-api-key \  --cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

## Вбудований каталог

OpenClaw постачається зі статичним каталогом Cerebras, який віддзеркалює публічну OpenAI-сумісну кінцеву точку. Усі чотири моделі мають контекст 128k і 8 192 максимальні вихідні токени.

Посилання на модель | Назва | Міркування | Примітки  
---|---|---|---  
`cerebras/zai-glm-4.7` | [Z.ai](<http://Z.ai>) GLM 4.7 | так | Модель за замовчуванням; попередня модель із міркуванням  
`cerebras/gpt-oss-120b` | GPT OSS 120B | так | Виробнича модель із міркуванням  
`cerebras/qwen-3-235b-a22b-instruct-2507` | Qwen 3 235B Instruct | ні | Попередня модель без міркування  
`cerebras/llama3.1-8b` | Llama 3.1 8B | ні | Виробнича модель, оптимізована для швидкості  
  
## Ручна конфігурація

Завдяки вбудованому Plugin зазвичай потрібен лише API-ключ. Використовуйте явну конфігурацію `models.providers.cerebras`, якщо хочете перевизначити метадані моделей або працювати в `mode: "merge"` зі статичним каталогом:

json5Copy code
[code]
    {  env: { CEREBRAS_API_KEY: "csk-..." },  agents: {    defaults: {      model: { primary: "cerebras/zai-glm-4.7" },    },  },  models: {    mode: "merge",    providers: {      cerebras: {        baseUrl: "https://api.cerebras.ai/v1",        apiKey: "${CEREBRAS_API_KEY}",        api: "openai-completions",        models: [          { id: "zai-glm-4.7", name: "Z.ai GLM 4.7" },          { id: "gpt-oss-120b", name: "GPT OSS 120B" },        ],      },    },  },}
[/code]

## Пов’язане

[**Провайдери моделей** Вибір провайдерів, посилань на моделі та поведінки аварійного перемикання. ](</uk/concepts/model-providers>) [**Режими мислення** Рівні інтенсивності міркування для двох моделей Cerebras із підтримкою міркування. ](</uk/tools/thinking>) [**Довідник із конфігурації** Типові параметри агентів і конфігурація моделей. ](</uk/gateway/config-agents#agent-defaults>) [**FAQ щодо моделей** Профілі автентифікації, перемикання моделей і усунення помилок "no profile". ](</uk/help/faq-models>)

Was this useful?YesNo