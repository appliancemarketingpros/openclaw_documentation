---
title: NVIDIA
source_url: https://docs.openclaw.ai/uk/providers/nvidia
scraped_at: 2026-05-25
---

NVIDIA надає OpenAI-сумісний API за адресою `https://integrate.api.nvidia.com/v1` для відкритих моделей безкоштовно. Автентифікуйтеся за допомогою API-ключа з [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

## Початок роботи

* ### Отримайте свій API-ключ

Створіть API-ключ на [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

* ### Експортуйте ключ і запустіть онбординг

bashCopy code
[code]
    export NVIDIA_API_KEY="nvapi-..."openclaw onboard --auth-choice nvidia-api-key
[/code]

* ### Задайте модель NVIDIA

bashCopy code
[code]
    openclaw models set nvidia/nvidia/nemotron-3-super-120b-a12b
[/code]

Для неінтерактивного налаштування ключ також можна передати безпосередньо:

bashCopy code
[code]
    openclaw onboard --auth-choice nvidia-api-key --nvidia-api-key "nvapi-..."
[/code]

## Приклад конфігурації

json5Copy code
[code]
    {  env: { NVIDIA_API_KEY: "nvapi-..." },  models: {    providers: {      nvidia: {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",      },    },  },  agents: {    defaults: {      model: { primary: "nvidia/nvidia/nemotron-3-super-120b-a12b" },    },  },}
[/code]

## Вбудований каталог

Посилання на модель | Назва | Контекст | Макс. вивід  
---|---|---|---  
`nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Nemotron 3 Super 120B | 262,144 | 8,192  
`nvidia/moonshotai/kimi-k2.5` | Kimi K2.5 | 262,144 | 8,192  
`nvidia/minimaxai/minimax-m2.5` | Minimax M2.5 | 196,608 | 8,192  
`nvidia/z-ai/glm5` | GLM 5 | 202,752 | 8,192  
  
## Розширена конфігурація

Поведінка автоматичного ввімкнення

Провайдер автоматично вмикається, коли задано змінну середовища `NVIDIA_API_KEY`. Окрім ключа, явна конфігурація провайдера не потрібна.

Каталог і ціни

Вбудований каталог є статичним. Витрати в джерелі за замовчуванням дорівнюють `0`, оскільки NVIDIA наразі пропонує безкоштовний доступ до API для перелічених моделей.

OpenAI-сумісний endpoint

NVIDIA використовує стандартний endpoint completions `/v1`. Будь-які OpenAI-сумісні інструменти мають працювати одразу з базовим URL NVIDIA.

Повільні відповіді власного провайдера

Деякі власні моделі, розміщені NVIDIA, можуть потребувати більше часу, ніж стандартний idle watchdog моделі, перш ніж вони видадуть перший фрагмент відповіді. Для власних записів провайдера NVIDIA збільшуйте timeout провайдера, а не timeout усього runtime агента:

json5Copy code
[code]
    {  models: {    providers: {      "custom-integrate-api-nvidia-com": {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",        apiKey: "NVIDIA_API_KEY",        timeoutSeconds: 300,      },    },  },  agents: {    defaults: {      models: {        "custom-integrate-api-nvidia-com/meta/llama-3.1-70b-instruct": {          params: { thinking: "off" },        },      },    },  },}
[/code]

## Пов’язане

[**Вибір моделі** Вибір провайдерів, посилань на моделі та поведінки failover. ](</uk/concepts/model-providers>) [**Довідник із конфігурації** Повний довідник із конфігурації для агентів, моделей і провайдерів. ](</uk/gateway/configuration-reference>)

Was this useful?YesNo