---
title: LiteLLM
source_url: https://docs.openclaw.ai/uk/providers/litellm
scraped_at: 2026-05-25
---

[LiteLLM](<https://litellm.ai>) — це шлюз LLM з відкритим кодом, який надає уніфікований API до понад 100 постачальників моделей. Спрямуйте OpenClaw через LiteLLM, щоб отримати централізоване відстеження витрат, журналювання та гнучкість перемикання бекендів без змін у конфігурації OpenClaw.

## Швидкий початок

### Початкове налаштування (рекомендовано)

**Найкраще для:** найшвидшого способу отримати робоче налаштування LiteLLM.

* ### Запустіть початкове налаштування

bashCopy code
[code]
    openclaw onboard --auth-choice litellm-api-key
[/code]

Для неінтерактивного налаштування з віддаленим проксі явно передайте URL проксі:

bashCopy code
[code]
    openclaw onboard --non-interactive --auth-choice litellm-api-key --litellm-api-key "$LITELLM_API_KEY" --custom-base-url "https://litellm.example/v1"
[/code]

### Ручне налаштування

**Найкраще для:** повного контролю над встановленням і конфігурацією.

* ### Запустіть LiteLLM Proxy

bashCopy code
[code]
    pip install 'litellm[proxy]'litellm --model claude-opus-4-6
[/code]

* ### Спрямуйте OpenClaw до LiteLLM

bashCopy code
[code]
    export LITELLM_API_KEY="your-litellm-key" openclaw
[/code]

Ось і все. Тепер OpenClaw спрямовує запити через LiteLLM.

## Конфігурація

### Змінні середовища

bashCopy code
[code]
    export LITELLM_API_KEY="sk-litellm-key"
[/code]

### Файл конфігурації

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",        api: "openai-completions",        models: [          {            id: "claude-opus-4-6",            name: "Claude Opus 4.6",            reasoning: true,            input: ["text", "image"],            contextWindow: 200000,            maxTokens: 64000,          },          {            id: "gpt-4o",            name: "GPT-4o",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "litellm/claude-opus-4-6" },    },  },}
[/code]

## Розширена конфігурація

### Генерація зображень

LiteLLM також може обслуговувати інструмент `image_generate` через OpenAI-сумісні маршрути `/images/generations` і `/images/edits`. Налаштуйте модель зображень LiteLLM у `agents.defaults.imageGenerationModel`:

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",      },    },  },  agents: {    defaults: {      imageGenerationModel: {        primary: "litellm/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

URL LiteLLM із local loopback, наприклад `http://localhost:4000`, працюють без глобального перевизначення приватної мережі. Для проксі, розміщеного в LAN, установіть `models.providers.litellm.request.allowPrivateNetwork: true`, оскільки API-ключ буде надіслано налаштованому хосту проксі.

Віртуальні ключі

Створіть окремий ключ для OpenClaw з лімітами витрат:

bashCopy code
[code]
    curl -X POST "http://localhost:4000/key/generate" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \  -H "Content-Type: application/json" \  -d '{    "key_alias": "openclaw",    "max_budget": 50.00,    "budget_duration": "monthly"  }'
[/code]

Використовуйте згенерований ключ як `LITELLM_API_KEY`.

Маршрутизація моделей

LiteLLM може спрямовувати запити до моделей на різні бекенди. Налаштуйте це у вашому `config.yaml` LiteLLM:

yamlCopy code
[code]
    model_list:  - model_name: claude-opus-4-6    litellm_params:      model: claude-opus-4-6      api_key: os.environ/ANTHROPIC_API_KEY   - model_name: gpt-4o    litellm_params:      model: gpt-4o      api_key: os.environ/OPENAI_API_KEY
[/code]

OpenClaw і далі запитуватиме `claude-opus-4-6` — маршрутизацією керує LiteLLM.

Перегляд використання

Перевіряйте панель керування або API LiteLLM:

bashCopy code
[code]
    # Інформація про ключcurl "http://localhost:4000/key/info" \  -H "Authorization: Bearer sk-litellm-key" # Журнали витратcurl "http://localhost:4000/spend/logs" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY"
[/code]

Примітки щодо поведінки проксі

  * LiteLLM за замовчуванням працює на `http://localhost:4000`
  * OpenClaw підключається через OpenAI-сумісну кінцеву точку `/v1` у стилі проксі LiteLLM
  * Власне формування запитів лише для OpenAI не застосовується через LiteLLM: немає `service_tier`, немає `store` для Responses, немає підказок кешу промптів і немає формування payload для сумісності з reasoning OpenAI
  * Приховані заголовки атрибуції OpenClaw (`originator`, `version`, `User-Agent`) не додаються для користувацьких базових URL LiteLLM


## Пов’язане

[**Документація LiteLLM** Офіційна документація LiteLLM і довідник API. ](<https://docs.litellm.ai>) [**Вибір моделі** Огляд усіх постачальників, посилань на моделі та поведінки резервного перемикання. ](</uk/concepts/model-providers>) [**Конфігурація** Повний довідник із конфігурації. ](</uk/gateway/configuration>) [**Вибір моделі** Як вибирати та налаштовувати моделі. ](</uk/concepts/models>)

Was this useful?YesNo