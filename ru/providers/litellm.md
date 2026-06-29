---
title: LiteLLM
source_url: https://docs.openclaw.ai/ru/providers/litellm
scraped_at: 2026-06-29
---

ModelsProviders

[LiteLLM](<https://litellm.ai>) — это open-source LLM-шлюз, который предоставляет единый API для более чем 100 провайдеров моделей. Направляйте OpenClaw через LiteLLM, чтобы получить централизованное отслеживание расходов, журналирование и гибкость переключения бэкендов без изменения конфигурации OpenClaw.

## Быстрый старт

### Onboarding (recommended)

**Лучше всего подходит для:** самого быстрого пути к рабочей настройке LiteLLM.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice litellm-api-key
[/code]

Для неинтерактивной настройки с удаленным прокси явно передайте URL прокси:

bashCopy code
[code]
    openclaw onboard --non-interactive --auth-choice litellm-api-key --litellm-api-key "$LITELLM_API_KEY" --custom-base-url "https://litellm.example/v1"
[/code]

### Manual setup

**Лучше всего подходит для:** полного контроля над установкой и конфигурацией.

* ### Start LiteLLM Proxy

bashCopy code
[code]
    pip install 'litellm[proxy]'litellm --model claude-opus-4-6
[/code]

* ### Point OpenClaw to LiteLLM

bashCopy code
[code]
    export LITELLM_API_KEY="your-litellm-key" openclaw
[/code]

Готово. Теперь OpenClaw направляет запросы через LiteLLM.

## Конфигурация

### Переменные окружения

bashCopy code
[code]
    export LITELLM_API_KEY="sk-litellm-key"
[/code]

### Файл конфигурации

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",        api: "openai-completions",        models: [          {            id: "claude-opus-4-6",            name: "Claude Opus 4.6",            reasoning: true,            input: ["text", "image"],            contextWindow: 200000,            maxTokens: 64000,          },          {            id: "gpt-4o",            name: "GPT-4o",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "litellm/claude-opus-4-6" },    },  },}
[/code]

## Расширенная конфигурация

### Генерация изображений

LiteLLM также может обеспечивать работу инструмента `image_generate` через OpenAI-совместимые маршруты `/images/generations` и `/images/edits`. Настройте модель изображений LiteLLM в `agents.defaults.imageGenerationModel`:

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",      },    },  },  agents: {    defaults: {      imageGenerationModel: {        primary: "litellm/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

Loopback-URL LiteLLM, такие как `http://localhost:4000`, работают без глобального переопределения частной сети. Для прокси, размещенного в LAN, задайте `models.providers.litellm.request.allowPrivateNetwork: true`, потому что API-ключ будет отправлен на настроенный хост прокси.

Virtual keys

Создайте выделенный ключ для OpenClaw с лимитами расходов:

bashCopy code
[code]
    curl -X POST "http://localhost:4000/key/generate" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \  -H "Content-Type: application/json" \  -d '{    "key_alias": "openclaw",    "max_budget": 50.00,    "budget_duration": "monthly"  }'
[/code]

Используйте сгенерированный ключ как `LITELLM_API_KEY`.

Model routing

LiteLLM может направлять запросы моделей к разным бэкендам. Настройте это в LiteLLM `config.yaml`:

yamlCopy code
[code]
    model_list:  - model_name: claude-opus-4-6    litellm_params:      model: claude-opus-4-6      api_key: os.environ/ANTHROPIC_API_KEY   - model_name: gpt-4o    litellm_params:      model: gpt-4o      api_key: os.environ/OPENAI_API_KEY
[/code]

OpenClaw продолжает запрашивать `claude-opus-4-6` — LiteLLM обрабатывает маршрутизацию.

Viewing usage

Проверьте панель управления или API LiteLLM:

bashCopy code
[code]
    # Key infocurl "http://localhost:4000/key/info" \  -H "Authorization: Bearer sk-litellm-key" # Spend logscurl "http://localhost:4000/spend/logs" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY"
[/code]

Proxy behavior notes

  * По умолчанию LiteLLM работает на `http://localhost:4000`
  * OpenClaw подключается через прокси-стиль OpenAI-совместимой конечной точки LiteLLM `/v1`
  * Формирование запросов, предназначенное только для нативного OpenAI, не применяется через LiteLLM: нет `service_tier`, нет Responses `store`, нет подсказок для prompt cache и нет формирования payload для совместимости с reasoning OpenAI
  * Скрытые заголовки атрибуции OpenClaw (`originator`, `version`, `User-Agent`) не внедряются для пользовательских базовых URL LiteLLM


## Связанные материалы

[**LiteLLM Docs** Официальная документация LiteLLM и справочник API. ](<https://docs.litellm.ai>) [**Model selection** Обзор всех провайдеров, ссылок на модели и поведения failover. ](</ru/concepts/model-providers>) [**Configuration** Полный справочник конфигурации. ](</ru/gateway/configuration>) [**Model selection** Как выбирать и настраивать модели. ](</ru/concepts/models>)

Was this useful?YesNo

Open issue