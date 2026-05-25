---
title: Synthetic
source_url: https://docs.openclaw.ai/uk/providers/synthetic
scraped_at: 2026-05-25
---

[Synthetic](<https://synthetic.new>) надає endpoint, сумісні з Anthropic. OpenClaw реєструє його як провайдера `synthetic` і використовує Anthropic Messages API.

Властивість | Значення  
---|---  
Провайдер | `synthetic`  
Auth | `SYNTHETIC_API_KEY`  
API | Anthropic Messages  
Base URL | `https://api.synthetic.new/anthropic`  
  
## Початок роботи

* ### Отримайте API key

Отримайте `SYNTHETIC_API_KEY` у своєму обліковому записі Synthetic або дозвольте майстру onboarding запросити його у вас.

* ### Запустіть onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice synthetic-api-key
[/code]

* ### Перевірте типову модель

Після onboarding типовою моделлю буде:

CodeCopy code
[code]
    synthetic/hf:MiniMaxAI/MiniMax-M2.5
[/code]

## Приклад config

json5Copy code
[code]
    {  env: { SYNTHETIC_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.5" },      models: { "synthetic/hf:MiniMaxAI/MiniMax-M2.5": { alias: "MiniMax M2.5" } },    },  },  models: {    mode: "merge",    providers: {      synthetic: {        baseUrl: "https://api.synthetic.new/anthropic",        apiKey: "${SYNTHETIC_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "hf:MiniMaxAI/MiniMax-M2.5",            name: "MiniMax M2.5",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 192000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## Вбудований catalog

Усі моделі Synthetic використовують вартість `0` (input/output/cache).

ID моделі | Контекстне вікно | Макс. токенів | Reasoning | Вхід  
---|---|---|---|---  
`hf:MiniMaxAI/MiniMax-M2.5` | 192,000 | 65,536 | ні | text  
`hf:moonshotai/Kimi-K2-Thinking` | 256,000 | 8,192 | так | text  
`hf:zai-org/GLM-4.7` | 198,000 | 128,000 | ні | text  
`hf:deepseek-ai/DeepSeek-R1-0528` | 128,000 | 8,192 | ні | text  
`hf:deepseek-ai/DeepSeek-V3-0324` | 128,000 | 8,192 | ні | text  
`hf:deepseek-ai/DeepSeek-V3.1` | 128,000 | 8,192 | ні | text  
`hf:deepseek-ai/DeepSeek-V3.1-Terminus` | 128,000 | 8,192 | ні | text  
`hf:deepseek-ai/DeepSeek-V3.2` | 159,000 | 8,192 | ні | text  
`hf:meta-llama/Llama-3.3-70B-Instruct` | 128,000 | 8,192 | ні | text  
`hf:meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | 524,000 | 8,192 | ні | text  
`hf:moonshotai/Kimi-K2-Instruct-0905` | 256,000 | 8,192 | ні | text  
`hf:moonshotai/Kimi-K2.5` | 256,000 | 8,192 | так | text + image  
`hf:openai/gpt-oss-120b` | 128,000 | 8,192 | ні | text  
`hf:Qwen/Qwen3-235B-A22B-Instruct-2507` | 256,000 | 8,192 | ні | text  
`hf:Qwen/Qwen3-Coder-480B-A35B-Instruct` | 256,000 | 8,192 | ні | text  
`hf:Qwen/Qwen3-VL-235B-A22B-Instruct` | 250,000 | 8,192 | ні | text + image  
`hf:zai-org/GLM-4.5` | 128,000 | 128,000 | ні | text  
`hf:zai-org/GLM-4.6` | 198,000 | 128,000 | ні | text  
`hf:zai-org/GLM-5` | 256,000 | 128,000 | так | text + image  
`hf:deepseek-ai/DeepSeek-V3` | 128,000 | 8,192 | ні | text  
`hf:Qwen/Qwen3-235B-A22B-Thinking-2507` | 256,000 | 8,192 | так | text  
  
Allowlist моделей

Якщо ви вмикаєте allowlist моделей (`agents.defaults.models`), додайте кожну модель Synthetic, яку плануєте використовувати. Моделі, яких немає в allowlist, будуть приховані від агента.

Перевизначення base URL

Якщо Synthetic змінить свій endpoint API, перевизначте base URL у config:

json5Copy code
[code]
    {  models: {    providers: {      synthetic: {        baseUrl: "https://new-api.synthetic.new/anthropic",      },    },  },}
[/code]

Пам’ятайте, що OpenClaw автоматично додає `/v1`.

## Пов’язане

[**Вибір моделі** Правила провайдера, посилання на моделі та поведінка failover. ](</uk/concepts/model-providers>) [**Довідник конфігурації** Повна schema config, включно з налаштуваннями провайдера. ](</uk/gateway/configuration-reference>) [**Synthetic** Dashboard Synthetic і документація API. ](<https://synthetic.new>)

Was this useful?YesNo