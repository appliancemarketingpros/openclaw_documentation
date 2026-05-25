---
title: Synthetic
source_url: https://docs.openclaw.ai/pl/providers/synthetic
scraped_at: 2026-05-25
---

[Synthetic](<https://synthetic.new>) udostępnia endpointy zgodne z Anthropic. OpenClaw rejestruje go jako dostawcę `synthetic` i używa API Anthropic Messages.

Właściwość | Wartość  
---|---  
Dostawca | `synthetic`  
Uwierzytelnianie | `SYNTHETIC_API_KEY`  
API | Anthropic Messages  
Base URL | `https://api.synthetic.new/anthropic`  
  
## Pierwsze kroki

* ### Pobierz klucz API

Uzyskaj `SYNTHETIC_API_KEY` ze swojego konta Synthetic albo pozwól, aby kreator onboardingu poprosił Cię o niego.

* ### Uruchom onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice synthetic-api-key
[/code]

* ### Sprawdź domyślny model

Po onboardingu domyślny model jest ustawiony na:

CodeCopy code
[code]
    synthetic/hf:MiniMaxAI/MiniMax-M2.5
[/code]

## Przykład konfiguracji

json5Copy code
[code]
    {  env: { SYNTHETIC_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.5" },      models: { "synthetic/hf:MiniMaxAI/MiniMax-M2.5": { alias: "MiniMax M2.5" } },    },  },  models: {    mode: "merge",    providers: {      synthetic: {        baseUrl: "https://api.synthetic.new/anthropic",        apiKey: "${SYNTHETIC_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "hf:MiniMaxAI/MiniMax-M2.5",            name: "MiniMax M2.5",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 192000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## Wbudowany katalog

Wszystkie modele Synthetic używają kosztu `0` (wejście/wyjście/cache).

ID modelu | Okno kontekstu | Maks. tokeny | Reasoning | Wejście  
---|---|---|---|---  
`hf:MiniMaxAI/MiniMax-M2.5` | 192,000 | 65,536 | nie | text  
`hf:moonshotai/Kimi-K2-Thinking` | 256,000 | 8,192 | tak | text  
`hf:zai-org/GLM-4.7` | 198,000 | 128,000 | nie | text  
`hf:deepseek-ai/DeepSeek-R1-0528` | 128,000 | 8,192 | nie | text  
`hf:deepseek-ai/DeepSeek-V3-0324` | 128,000 | 8,192 | nie | text  
`hf:deepseek-ai/DeepSeek-V3.1` | 128,000 | 8,192 | nie | text  
`hf:deepseek-ai/DeepSeek-V3.1-Terminus` | 128,000 | 8,192 | nie | text  
`hf:deepseek-ai/DeepSeek-V3.2` | 159,000 | 8,192 | nie | text  
`hf:meta-llama/Llama-3.3-70B-Instruct` | 128,000 | 8,192 | nie | text  
`hf:meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | 524,000 | 8,192 | nie | text  
`hf:moonshotai/Kimi-K2-Instruct-0905` | 256,000 | 8,192 | nie | text  
`hf:moonshotai/Kimi-K2.5` | 256,000 | 8,192 | tak | text + image  
`hf:openai/gpt-oss-120b` | 128,000 | 8,192 | nie | text  
`hf:Qwen/Qwen3-235B-A22B-Instruct-2507` | 256,000 | 8,192 | nie | text  
`hf:Qwen/Qwen3-Coder-480B-A35B-Instruct` | 256,000 | 8,192 | nie | text  
`hf:Qwen/Qwen3-VL-235B-A22B-Instruct` | 250,000 | 8,192 | nie | text + image  
`hf:zai-org/GLM-4.5` | 128,000 | 128,000 | nie | text  
`hf:zai-org/GLM-4.6` | 198,000 | 128,000 | nie | text  
`hf:zai-org/GLM-5` | 256,000 | 128,000 | tak | text + image  
`hf:deepseek-ai/DeepSeek-V3` | 128,000 | 8,192 | nie | text  
`hf:Qwen/Qwen3-235B-A22B-Thinking-2507` | 256,000 | 8,192 | tak | text  
  
Allowlist modeli

Jeśli włączysz allowlist modeli (`agents.defaults.models`), dodaj każdy model Synthetic, którego planujesz używać. Modele spoza allowlist będą ukryte przed agentem.

Nadpisanie base URL

Jeśli Synthetic zmieni endpoint API, nadpisz base URL w konfiguracji:

json5Copy code
[code]
    {  models: {    providers: {      synthetic: {        baseUrl: "https://new-api.synthetic.new/anthropic",      },    },  },}
[/code]

Pamiętaj, że OpenClaw automatycznie dopisuje `/v1`.

## Powiązane

[**Wybór modelu** Zasady dostawców, model ref i zachowanie failover. ](</pl/concepts/model-providers>) [**Dokumentacja konfiguracji** Pełny schemat konfiguracji, w tym ustawienia dostawców. ](</pl/gateway/configuration-reference>) [**Synthetic** Panel Synthetic i dokumentacja API. ](<https://synthetic.new>)

Was this useful?YesNo