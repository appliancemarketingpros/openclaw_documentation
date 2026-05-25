---
title: Venice AI
source_url: https://docs.openclaw.ai/uk/providers/venice
scraped_at: 2026-05-25
---

Venice AI надає **орієнтований на приватність AI inference** з підтримкою нецензурованих моделей і доступом до основних пропрієтарних моделей через їхній анонімізований проксі. Усі inference є приватними за замовчуванням — без навчання на ваших даних і без логування.

## Навіщо Venice в OpenClaw

  * **Приватний inference** для моделей із відкритим кодом (без логування).
  * **Нецензуровані моделі** , коли вони вам потрібні.
  * **Анонімізований доступ** до пропрієтарних моделей (Opus/GPT/Gemini), коли важлива якість.
  * OpenAI-сумісні endpoints `/v1`.


## Режими приватності

Venice пропонує два рівні приватності — розуміння цього є ключовим для вибору моделі:

Режим | Опис | Моделі  
---|---|---  
**Приватний** | Повністю приватний. Запити/відповіді **ніколи не зберігаються й не логуються**. Ефемерний. | Llama, Qwen, DeepSeek, Kimi, MiniMax, Venice Uncensored, etc.  
**Анонімізований** | Проксіюється через Venice із видаленими метаданими. Базовий провайдер (OpenAI, Anthropic, Google, xAI) бачить анонімізовані запити. | Claude, GPT, Gemini, Grok  
  
## Функції

  * **Орієнтованість на приватність** : обирайте між режимами "приватний" (повністю приватний) і "анонімізований" (проксійований)
  * **Нецензуровані моделі** : доступ до моделей без обмежень вмісту
  * **Доступ до основних моделей** : використовуйте Claude, GPT, Gemini і Grok через анонімізований проксі Venice
  * **OpenAI-сумісний API** : стандартні endpoints `/v1` для легкої інтеграції
  * **Streaming** : підтримується на всіх моделях
  * **Виклики функцій** : підтримуються на вибраних моделях (перевіряйте можливості моделі)
  * **Vision** : підтримується на моделях із можливістю vision
  * **Без жорстких лімітів частоти** : для надмірного використання може застосовуватися обмеження за принципом добросовісного використання


## Початок роботи

* ### Отримайте свій API key

  1. Зареєструйтеся на [venice.ai](<https://venice.ai>)
  2. Перейдіть до **Settings > API Keys > Create new key**
  3. Скопіюйте свій API key (формат: `vapi_xxxxxxxxxxxx`)


* ### Налаштуйте OpenClaw

Оберіть бажаний спосіб налаштування:

### Інтерактивно (рекомендовано)

bashCopy code
[code]
    openclaw onboard --auth-choice venice-api-key
[/code]

Це:

  1. Запитає ваш API key (або використає наявний `VENICE_API_KEY`)
  2. Покаже всі доступні моделі Venice
  3. Дозволить вибрати модель за замовчуванням
  4. Автоматично налаштує провайдера


### Змінна середовища

bashCopy code
[code]
    export VENICE_API_KEY="vapi_xxxxxxxxxxxx"
[/code]

### Неінтерактивно

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice venice-api-key \  --venice-api-key "vapi_xxxxxxxxxxxx"
[/code]

* ### Перевірте налаштування

bashCopy code
[code]
    openclaw agent --model venice/kimi-k2-5 --message "Hello, are you working?"
[/code]

## Вибір моделі

Після налаштування OpenClaw показує всі доступні моделі Venice. Обирайте відповідно до своїх потреб:

  * **Модель за замовчуванням** : `venice/kimi-k2-5` для сильного приватного reasoning плюс vision.
  * **Варіант із високими можливостями** : `venice/claude-opus-4-6` для найсильнішого анонімізованого шляху Venice.
  * **Приватність** : обирайте "приватні" моделі для повністю приватного inference.
  * **Можливості** : обирайте "анонімізовані" моделі для доступу до Claude, GPT, Gemini через проксі Venice.


Змініть модель за замовчуванням будь-коли:

bashCopy code
[code]
    openclaw models set venice/kimi-k2-5openclaw models set venice/claude-opus-4-6
[/code]

Перелічіть усі доступні моделі:

bashCopy code
[code]
    openclaw models list --all --provider venice
[/code]

Ви також можете запустити `openclaw configure`, вибрати **Model/auth** і обрати **Venice AI**.

## Поведінка повторного відтворення DeepSeek V4

Якщо Venice надає моделі DeepSeek V4, як-от `venice/deepseek-v4-pro` або `venice/deepseek-v4-flash`, OpenClaw заповнює потрібний для DeepSeek V4 placeholder повторного відтворення `reasoning_content` у повідомленнях assistant, коли проксі його пропускає. Venice відхиляє нативний top-level контроль `thinking` DeepSeek, тому OpenClaw тримає це специфічне для провайдера виправлення повторного відтворення окремо від нативних контролів thinking провайдера DeepSeek.

## Вбудований каталог (усього 41)

Приватні моделі (26) — повністю приватні, без логування ID моделі | Назва | Context | Функції  
---|---|---|---  
`kimi-k2-5` | Kimi K2.5 | 256k | За замовчуванням, reasoning, vision  
`kimi-k2-thinking` | Kimi K2 Thinking | 256k | Reasoning  
`llama-3.3-70b` | Llama 3.3 70B | 128k | Загальна  
`llama-3.2-3b` | Llama 3.2 3B | 128k | Загальна  
`hermes-3-llama-3.1-405b` | Hermes 3 Llama 3.1 405B | 128k | Загальна, tools вимкнено  
`qwen3-235b-a22b-thinking-2507` | Qwen3 235B Thinking | 128k | Reasoning  
`qwen3-235b-a22b-instruct-2507` | Qwen3 235B Instruct | 128k | Загальна  
`qwen3-coder-480b-a35b-instruct` | Qwen3 Coder 480B | 256k | Кодування  
`qwen3-coder-480b-a35b-instruct-turbo` | Qwen3 Coder 480B Turbo | 256k | Кодування  
`qwen3-5-35b-a3b` | Qwen3.5 35B A3B | 256k | Reasoning, vision  
`qwen3-next-80b` | Qwen3 Next 80B | 256k | Загальна  
`qwen3-vl-235b-a22b` | Qwen3 VL 235B (Vision) | 256k | Vision  
`qwen3-4b` | Venice Small (Qwen3 4B) | 32k | Швидка, reasoning  
`deepseek-v3.2` | DeepSeek V3.2 | 160k | Reasoning, tools вимкнено  
`venice-uncensored` | Venice Uncensored (Dolphin-Mistral) | 32k | Нецензурована, tools вимкнено  
`mistral-31-24b` | Venice Medium (Mistral) | 128k | Vision  
`google-gemma-3-27b-it` | Google Gemma 3 27B Instruct | 198k | Vision  
`openai-gpt-oss-120b` | OpenAI GPT OSS 120B | 128k | Загальна  
`nvidia-nemotron-3-nano-30b-a3b` | NVIDIA Nemotron 3 Nano 30B | 128k | Загальна  
`olafangensan-glm-4.7-flash-heretic` | GLM 4.7 Flash Heretic | 128k | Reasoning  
`zai-org-glm-4.6` | GLM 4.6 | 198k | Загальна  
`zai-org-glm-4.7` | GLM 4.7 | 198k | Reasoning  
`zai-org-glm-4.7-flash` | GLM 4.7 Flash | 128k | Reasoning  
`zai-org-glm-5` | GLM 5 | 198k | Reasoning  
`minimax-m21` | MiniMax M2.1 | 198k | Reasoning  
`minimax-m25` | MiniMax M2.5 | 198k | Reasoning  
Анонімізовані моделі (15) — через проксі Venice ID моделі | Назва | Context | Функції  
---|---|---|---  
`claude-opus-4-6` | Claude Opus 4.6 (через Venice) | 1M | Reasoning, vision  
`claude-opus-4-5` | Claude Opus 4.5 (через Venice) | 198k | Reasoning, vision  
`claude-sonnet-4-6` | Claude Sonnet 4.6 (через Venice) | 1M | Reasoning, vision  
`claude-sonnet-4-5` | Claude Sonnet 4.5 (через Venice) | 198k | Reasoning, vision  
`openai-gpt-54` | GPT-5.4 (через Venice) | 1M | Reasoning, vision  
`openai-gpt-53-codex` | GPT-5.3 Codex (через Venice) | 400k | Reasoning, vision, кодування  
`openai-gpt-52` | GPT-5.2 (через Venice) | 256k | Reasoning  
`openai-gpt-52-codex` | GPT-5.2 Codex (через Venice) | 256k | Reasoning, vision, кодування  
`openai-gpt-4o-2024-11-20` | GPT-4o (через Venice) | 128k | Vision  
`openai-gpt-4o-mini-2024-07-18` | GPT-4o Mini (через Venice) | 128k | Vision  
`gemini-3-1-pro-preview` | Gemini 3.1 Pro (через Venice) | 1M | Reasoning, vision  
`gemini-3-pro-preview` | Gemini 3 Pro (через Venice) | 198k | Reasoning, vision  
`gemini-3-flash-preview` | Gemini 3 Flash (через Venice) | 256k | Reasoning, vision  
`grok-41-fast` | Grok 4.1 Fast (через Venice) | 1M | Reasoning, vision  
`grok-code-fast-1` | Grok Code Fast 1 (через Venice) | 256k | Reasoning, кодування  
  
## Виявлення моделей

OpenClaw постачається з підкріпленим маніфестом початковим каталогом Venice для read-only списку моделей. Runtime refresh усе ще може виявляти моделі з Venice API і повертається до каталогу маніфесту, якщо API недоступний.

Endpoint `/models` є публічним (автентифікація не потрібна для списку), але inference потребує дійсний API key.

## Streaming і підтримка tools

Функція | Підтримка  
---|---  
**Стримінг** | Усі моделі  
**Виклик функцій** | Більшість моделей (перевірте `supportsFunctionCalling` в API)  
**Зір/зображення** | Моделі, позначені функцією "Vision"  
**Режим JSON** | Підтримується через `response_format`  
  
## Ціни

Venice використовує систему на основі кредитів. Перевірте [venice.ai/pricing](<https://venice.ai/pricing>), щоб дізнатися актуальні тарифи:

  * **Приватні моделі** : Зазвичай нижча вартість
  * **Анонімізовані моделі** : Подібно до прямого ціноутворення API + невелика комісія Venice


### Venice (анонімізовано) проти прямого API

Аспект | Venice (анонімізовано) | Прямий API  
---|---|---  
**Приватність** | Метадані видалено, анонімізовано | Ваш обліковий запис прив’язано  
**Затримка** | +10-50 мс (проксі) | Напряму  
**Функції** | Підтримується більшість функцій | Повний набір функцій  
**Оплата** | Кредити Venice | Оплата провайдеру  
  
## Приклади використання

bashCopy code
[code]
    # Use the default private modelopenclaw agent --model venice/kimi-k2-5 --message "Quick health check" # Use Claude Opus via Venice (anonymized)openclaw agent --model venice/claude-opus-4-6 --message "Summarize this task" # Use uncensored modelopenclaw agent --model venice/venice-uncensored --message "Draft options" # Use vision model with imageopenclaw agent --model venice/qwen3-vl-235b-a22b --message "Review attached image" # Use coding modelopenclaw agent --model venice/qwen3-coder-480b-a35b-instruct --message "Refactor this function"
[/code]

## Усунення несправностей

API key not recognized bashCopy code
[code]
    echo $VENICE_API_KEYopenclaw models list | grep venice
[/code]

Переконайтеся, що ключ починається з `vapi_`.

Model not available

Каталог моделей Venice оновлюється динамічно. Запустіть `openclaw models list`, щоб переглянути наразі доступні моделі. Деякі моделі можуть бути тимчасово офлайн.

Connection issues

API Venice розміщено за адресою `https://api.venice.ai/api/v1`. Переконайтеся, що ваша мережа дозволяє HTTPS-з’єднання.

## Розширена конфігурація

Config file example json5Copy code
[code]
    {  env: { VENICE_API_KEY: "vapi_..." },  agents: { defaults: { model: { primary: "venice/kimi-k2-5" } } },  models: {    mode: "merge",    providers: {      venice: {        baseUrl: "https://api.venice.ai/api/v1",        apiKey: "${VENICE_API_KEY}",        api: "openai-completions",        models: [          {            id: "kimi-k2-5",            name: "Kimi K2.5",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 256000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## Пов’язане

[**Model selection** Вибір провайдерів, посилань на моделі та поведінки відмовостійкого перемикання. ](</uk/concepts/model-providers>) [**Venice AI** Головна сторінка Venice AI і реєстрація облікового запису. ](<https://venice.ai>) [**API documentation** Довідник API Venice і документація для розробників. ](<https://docs.venice.ai>) [**Pricing** Поточні кредитні тарифи й плани Venice. ](<https://venice.ai/pricing>)

Was this useful?YesNo