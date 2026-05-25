---
title: Anthropic
source_url: https://docs.openclaw.ai/uk/providers/anthropic
scraped_at: 2026-05-25
---

Anthropic створює сімейство моделей **Claude**. OpenClaw підтримує два способи автентифікації:

  * **API-ключ** — прямий доступ до Anthropic API з оплатою за використання (моделі `anthropic/*`)
  * **Claude CLI** — повторне використання наявного входу Claude CLI на тому самому хості


## Початок роботи

### API-ключ

**Найкраще для:** стандартного доступу до API та оплати за використання.

* ### Отримайте свій API-ключ

Створіть API-ключ у [Anthropic Console](<https://console.anthropic.com/>).

* ### Запустіть початкове налаштування

bashCopy code
[code]
    openclaw onboard# choose: Anthropic API key
[/code]

Або передайте ключ безпосередньо:

bashCopy code
[code]
    openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
[/code]

* ### Перевірте, що модель доступна

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Приклад конфігурації

json5Copy code
[code]
    {  env: { ANTHROPIC_API_KEY: "sk-ant-..." },  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

### Claude CLI

**Найкраще для:** повторного використання наявного входу Claude CLI без окремого API-ключа.

* ### Переконайтеся, що Claude CLI встановлено і ви ввійшли

Перевірте за допомогою:

bashCopy code
[code]
    claude --version
[/code]

* ### Запустіть початкове налаштування

bashCopy code
[code]
    openclaw onboard# choose: Claude CLI
[/code]

OpenClaw виявляє та повторно використовує наявні облікові дані Claude CLI.

* ### Перевірте, що модель доступна

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Приклад конфігурації

Надавайте перевагу канонічному посиланню на модель Anthropic плюс перевизначенню середовища виконання CLI:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-7" },      models: {        "anthropic/claude-opus-4-7": {          agentRuntime: { id: "claude-cli" },        },      },    },  },}
[/code]

Застарілі посилання на моделі `claude-cli/claude-opus-4-7` все ще працюють для сумісності, але нова конфігурація має зберігати вибір провайдера/моделі як `anthropic/*`, а бекенд виконання розміщувати в політиці середовища виконання провайдера/моделі.

## Стандартні налаштування мислення (Claude 4.6)

Моделі Claude 4.6 за замовчуванням використовують `adaptive` мислення в OpenClaw, якщо явний рівень мислення не задано.

Перевизначайте для окремого повідомлення за допомогою `/think:<level>` або в параметрах моделі:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { thinking: "adaptive" },        },      },    },  },}
[/code]

## Кешування промптів

OpenClaw підтримує функцію кешування промптів Anthropic для автентифікації через API-ключ.

Значення | Тривалість кешу | Опис  
---|---|---  
`"short"` (типово) | 5 хвилин | Застосовується автоматично для автентифікації через API-ключ  
`"long"` | 1 година | Розширений кеш  
`"none"` | Без кешування | Вимкнути кешування промптів  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },  },}
[/code]

Перевизначення кешу для окремого агента

Використовуйте параметри рівня моделі як базові, а потім перевизначайте конкретних агентів через `agents.list[].params`:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-6" },      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },    list: [      { id: "research", default: true },      { id: "alerts", params: { cacheRetention: "none" } },    ],  },}
[/code]

Порядок злиття конфігурації:

  1. `agents.defaults.models["provider/model"].params`
  2. `agents.list[].params` (відповідний `id`, перевизначення за ключем)


Це дає змогу одному агенту зберігати довготривалий кеш, тоді як інший агент на тій самій моделі вимикає кешування для сплескового трафіку або трафіку з низьким повторним використанням.

Примітки щодо Bedrock Claude

  * Моделі Anthropic Claude на Bedrock (`amazon-bedrock/*anthropic.claude*`) приймають наскрізний `cacheRetention`, якщо його налаштовано.
  * Для моделей Bedrock, що не належать Anthropic, під час виконання примусово встановлюється `cacheRetention: "none"`.
  * Розумні стандартні налаштування API-ключа також задають `cacheRetention: "short"` для посилань Claude-на-Bedrock, якщо явне значення не встановлено.


## Розширена конфігурація

Швидкий режим

Спільний перемикач `/fast` в OpenClaw підтримує прямий трафік Anthropic (API-ключ і OAuth до `api.anthropic.com`).

Команда | Відповідає  
---|---  
`/fast on` | `service_tier: "auto"`  
`/fast off` | `service_tier: "standard_only"`  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-sonnet-4-6": {          params: { fastMode: true },        },      },    },  },}
[/code]

Розуміння медіа (зображення і PDF)

Вбудований Plugin Anthropic реєструє розуміння зображень і PDF. OpenClaw автоматично визначає медіаможливості з налаштованої автентифікації Anthropic — додаткова конфігурація не потрібна.

Властивість | Значення  
---|---  
Типова модель | `claude-opus-4-7`  
Підтримуваний ввід | Зображення, PDF-документи  
  
Коли зображення або PDF додано до розмови, OpenClaw автоматично спрямовує його через провайдера розуміння медіа Anthropic.

Контекстне вікно 1M (бета)

Контекстне вікно 1M Anthropic доступне через бета-доступ. Увімкніть його для окремої моделі:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { context1m: true },        },      },    },  },}
[/code]

OpenClaw відображає це в `anthropic-beta: context-1m-2025-08-07` у запитах.

`params.context1m: true` також застосовується до бекенда Claude CLI (`claude-cli/*`) для відповідних моделей Opus і Sonnet, розширюючи контекстне вікно виконання для цих CLI-сеансів, щоб воно відповідало поведінці прямого API.

Контекст 1M для Claude Opus 4.7

`anthropic/claude-opus-4.7` і його варіант `claude-cli` мають контекстне вікно 1M за замовчуванням — `params.context1m: true` не потрібен.

## Усунення несправностей

Помилки 401 / токен раптово став недійсним

Токенна автентифікація Anthropic має строк дії і може бути відкликана. Для нових налаштувань натомість використовуйте Anthropic API-ключ.

API-ключ для провайдера "anthropic" не знайдено

Автентифікація Anthropic є **окремою для кожного агента** — нові агенти не успадковують ключі основного агента. Повторно запустіть початкове налаштування для цього агента (або налаштуйте API-ключ на хості gateway), а потім перевірте за допомогою `openclaw models status`.

Облікові дані для профілю "anthropic:default" не знайдено

Запустіть `openclaw models status`, щоб побачити, який профіль автентифікації активний. Повторно запустіть початкове налаштування або налаштуйте API-ключ для цього шляху профілю.

Немає доступного профілю автентифікації (усі в періоді очікування)

Перевірте `openclaw models status --json` для `auth.unusableProfiles`. Періоди очікування через обмеження частоти Anthropic можуть бути прив’язані до моделі, тому споріднена модель Anthropic все ще може бути придатною до використання. Додайте інший профіль Anthropic або дочекайтеся завершення періоду очікування.

## Пов’язане

[**Вибір моделі** Вибір провайдерів, посилань на моделі та поведінки відмовостійкості. ](</uk/concepts/model-providers>) [**Бекенди CLI** Налаштування бекенда Claude CLI та подробиці виконання. ](</uk/gateway/cli-backends>) [**Кешування промптів** Як кешування промптів працює між провайдерами. ](</uk/reference/prompt-caching>) [**OAuth і автентифікація** Подробиці автентифікації та правила повторного використання облікових даних. ](</uk/gateway/authentication>)

Was this useful?YesNo