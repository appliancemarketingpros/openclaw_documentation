---
title: Синтетический
source_url: https://docs.openclaw.ai/ru/providers/synthetic
scraped_at: 2026-06-29
---

ModelsProviders

[Synthetic](<https://synthetic.new>) предоставляет Anthropic-совместимые конечные точки. OpenClaw регистрирует его как поставщика `synthetic` и использует Anthropic Messages API.

Свойство | Значение  
---|---  
Поставщик | `synthetic`  
Аутентификация | `SYNTHETIC_API_KEY`  
API | Anthropic Messages  
Базовый URL | `https://api.synthetic.new/anthropic`  
  
## Начало работы

* ### Get an API key

Получите `SYNTHETIC_API_KEY` в своей учетной записи Synthetic или дайте мастеру первоначальной настройки запросить его у вас.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice synthetic-api-key
[/code]

* ### Verify the default model

После первоначальной настройки модель по умолчанию задается как:

CodeCopy code
[code]
    synthetic/hf:MiniMaxAI/MiniMax-M2.5
[/code]

## Пример конфигурации

json5Copy code
[code]
    {  env: { SYNTHETIC_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.5" },      models: { "synthetic/hf:MiniMaxAI/MiniMax-M2.5": { alias: "MiniMax M2.5" } },    },  },  models: {    mode: "merge",    providers: {      synthetic: {        baseUrl: "https://api.synthetic.new/anthropic",        apiKey: "${SYNTHETIC_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "hf:MiniMaxAI/MiniMax-M2.5",            name: "MiniMax M2.5",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 192000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## Встроенный каталог

Все модели Synthetic используют стоимость `0` (ввод/вывод/кэш).

ID модели | Контекстное окно | Максимум токенов | Рассуждение | Ввод  
---|---|---|---|---  
`hf:MiniMaxAI/MiniMax-M2.5` | 192,000 | 65,536 | нет | текст  
`hf:moonshotai/Kimi-K2-Thinking` | 256,000 | 8,192 | да | текст  
`hf:zai-org/GLM-4.7` | 198,000 | 128,000 | нет | текст  
`hf:deepseek-ai/DeepSeek-R1-0528` | 128,000 | 8,192 | нет | текст  
`hf:deepseek-ai/DeepSeek-V3-0324` | 128,000 | 8,192 | нет | текст  
`hf:deepseek-ai/DeepSeek-V3.1` | 128,000 | 8,192 | нет | текст  
`hf:deepseek-ai/DeepSeek-V3.1-Terminus` | 128,000 | 8,192 | нет | текст  
`hf:deepseek-ai/DeepSeek-V3.2` | 159,000 | 8,192 | нет | текст  
`hf:meta-llama/Llama-3.3-70B-Instruct` | 128,000 | 8,192 | нет | текст  
`hf:meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | 524,000 | 8,192 | нет | текст  
`hf:moonshotai/Kimi-K2-Instruct-0905` | 256,000 | 8,192 | нет | текст  
`hf:moonshotai/Kimi-K2.5` | 256,000 | 8,192 | да | текст + изображение  
`hf:openai/gpt-oss-120b` | 128,000 | 8,192 | нет | текст  
`hf:Qwen/Qwen3-235B-A22B-Instruct-2507` | 256,000 | 8,192 | нет | текст  
`hf:Qwen/Qwen3-Coder-480B-A35B-Instruct` | 256,000 | 8,192 | нет | текст  
`hf:Qwen/Qwen3-VL-235B-A22B-Instruct` | 250,000 | 8,192 | нет | текст + изображение  
`hf:zai-org/GLM-4.5` | 128,000 | 128,000 | нет | текст  
`hf:zai-org/GLM-4.6` | 198,000 | 128,000 | нет | текст  
`hf:zai-org/GLM-5` | 256,000 | 128,000 | да | текст + изображение  
`hf:deepseek-ai/DeepSeek-V3` | 128,000 | 8,192 | нет | текст  
`hf:Qwen/Qwen3-235B-A22B-Thinking-2507` | 256,000 | 8,192 | да | текст  
  
Model allowlist

Если вы включаете список разрешенных моделей (`agents.defaults.models`), добавьте каждую модель Synthetic, которую планируете использовать. Модели не из списка разрешенных будут скрыты от агента.

Base URL override

Если Synthetic изменит свою конечную точку API, переопределите базовый URL в конфигурации:

json5Copy code
[code]
    {  models: {    providers: {      synthetic: {        baseUrl: "https://new-api.synthetic.new/anthropic",      },    },  },}
[/code]

Помните, что OpenClaw автоматически добавляет `/v1`.

## Связанные материалы

[**Model selection** Правила поставщиков, ссылки на модели и поведение при отказе. ](</ru/concepts/model-providers>) [**Configuration reference** Полная схема конфигурации, включая настройки поставщиков. ](</ru/gateway/configuration-reference>) [**Synthetic** Панель управления Synthetic и документация API. ](<https://synthetic.new>)

Was this useful?YesNo

Open issue