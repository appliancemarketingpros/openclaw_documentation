---
title: Мета
source_url: https://docs.openclaw.ai/uk/providers/meta
scraped_at: 2026-07-13
---

ModelsProviders

**Meta API** використовує сумісний з OpenAI **Responses API** (`POST /v1/responses`) для моделі міркування `muse-spark-1.1`. Провайдер постачається як вбудований плагін OpenClaw.

Властивість | Значення  
---|---  
Ідентифікатор провайдера | `meta`  
Плагін | вбудований провайдер  
Змінна середовища автентифікації | `MODEL_API_KEY`  
Прапорець початкового налаштування | `--auth-choice meta-api-key`  
Прямий прапорець CLI | `--meta-api-key <key>`  
API | Responses API (`openai-responses`)  
Базова URL-адреса | `https://api.meta.ai/v1`  
Типова модель | `meta/muse-spark-1.1`  
Типовий рівень міркування | `high` (`reasoning.effort`)  
  
## Початок роботи

* ### Установіть ключ API

Початкове налаштуванняCopy code
[code]
    openclaw onboard --auth-choice meta-api-key
[/code]

Прямий прапорецьCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \--auth-choice meta-api-key \--meta-api-key "$MODEL_API_KEY"
[/code]

Лише змінна середовищаCopy code
[code]
    export MODEL_API_KEY=<key>
[/code]

* ### Перевірте доступність моделей

bashCopy code
[code]
    openclaw models list --provider meta
[/code]

Виводить статичний запис каталогу `muse-spark-1.1`. Якщо значення `MODEL_API_KEY` не визначено, `openclaw models status --json` повідомляє про відсутні облікові дані в `auth.unusableProfiles`.

## Неінтерактивне налаштування

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --mode local \  --auth-choice meta-api-key \  --meta-api-key "$MODEL_API_KEY"
[/code]

## Вбудований каталог

Посилання на модель | Назва | Міркування | Контекстне вікно | Максимальний обсяг виводу  
---|---|---|---|---  
`meta/muse-spark-1.1` | Muse Spark 1.1 | так | 1,048,576 | 131,072  
  
Можливості:

  * Введення тексту та зображень
  * Виклики інструментів і потокове передавання
  * Рівень міркування: `minimal`, `low`, `medium`, `high`, `xhigh` (типовий: `high`)
  * Відтворення зашифрованих міркувань без збереження стану (`store: false`, `include: ["reasoning.encrypted_content"]`)


## Ручна конфігурація

json5Copy code
[code]
    {  env: { MODEL_API_KEY: "<key>" },  agents: {    defaults: {      model: { primary: "meta/muse-spark-1.1" },      models: {        "meta/muse-spark-1.1": { alias: "Muse Spark 1.1" },      },    },  },}
[/code]

## Швидка перевірка

bashCopy code
[code]
    export MODEL_API_KEY=<key>pnpm test:live -- extensions/meta/meta.live.test.ts
[/code]

Тести в реальному середовищі використовують `muse-spark-1.1` із запитом до `POST /v1/responses`.

## Пов’язані матеріали

[**Провайдери моделей** Вибір провайдерів, посилань на моделі та поведінки резервного перемикання. ](</uk/concepts/model-providers>) [**Режими мислення** Рівні інтенсивності міркування для muse-spark-1.1. ](</uk/tools/thinking>) [**Довідник із конфігурації** Типові налаштування агентів і конфігурація моделей. ](</uk/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue