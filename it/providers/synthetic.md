---
title: Synthetic
source_url: https://docs.openclaw.ai/it/providers/synthetic
scraped_at: 2026-05-25
---

[Synthetic](<https://synthetic.new>) espone endpoint compatibili Anthropic. OpenClaw lo registra come provider `synthetic` e usa l'API Anthropic Messages.

Proprietà | Valore  
---|---  
Provider | `synthetic`  
Auth | `SYNTHETIC_API_KEY`  
API | Anthropic Messages  
URL base | `https://api.synthetic.new/anthropic`  
  
## Per iniziare

* ### Ottieni una API key

Ottieni una `SYNTHETIC_API_KEY` dal tuo account Synthetic, oppure lascia che la procedura guidata di onboarding te ne richieda una.

* ### Esegui l'onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice synthetic-api-key
[/code]

* ### Verifica il modello predefinito

Dopo l'onboarding il modello predefinito viene impostato su:

CodeCopy code
[code]
    synthetic/hf:MiniMaxAI/MiniMax-M2.5
[/code]

## Esempio di configurazione

json5Copy code
[code]
    {  env: { SYNTHETIC_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.5" },      models: { "synthetic/hf:MiniMaxAI/MiniMax-M2.5": { alias: "MiniMax M2.5" } },    },  },  models: {    mode: "merge",    providers: {      synthetic: {        baseUrl: "https://api.synthetic.new/anthropic",        apiKey: "${SYNTHETIC_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "hf:MiniMaxAI/MiniMax-M2.5",            name: "MiniMax M2.5",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 192000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## Catalogo integrato

Tutti i modelli Synthetic usano costo `0` (input/output/cache).

ID modello | Finestra di contesto | Token max | Reasoning | Input  
---|---|---|---|---  
`hf:MiniMaxAI/MiniMax-M2.5` | 192,000 | 65,536 | no | text  
`hf:moonshotai/Kimi-K2-Thinking` | 256,000 | 8,192 | sì | text  
`hf:zai-org/GLM-4.7` | 198,000 | 128,000 | no | text  
`hf:deepseek-ai/DeepSeek-R1-0528` | 128,000 | 8,192 | no | text  
`hf:deepseek-ai/DeepSeek-V3-0324` | 128,000 | 8,192 | no | text  
`hf:deepseek-ai/DeepSeek-V3.1` | 128,000 | 8,192 | no | text  
`hf:deepseek-ai/DeepSeek-V3.1-Terminus` | 128,000 | 8,192 | no | text  
`hf:deepseek-ai/DeepSeek-V3.2` | 159,000 | 8,192 | no | text  
`hf:meta-llama/Llama-3.3-70B-Instruct` | 128,000 | 8,192 | no | text  
`hf:meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | 524,000 | 8,192 | no | text  
`hf:moonshotai/Kimi-K2-Instruct-0905` | 256,000 | 8,192 | no | text  
`hf:moonshotai/Kimi-K2.5` | 256,000 | 8,192 | sì | text + image  
`hf:openai/gpt-oss-120b` | 128,000 | 8,192 | no | text  
`hf:Qwen/Qwen3-235B-A22B-Instruct-2507` | 256,000 | 8,192 | no | text  
`hf:Qwen/Qwen3-Coder-480B-A35B-Instruct` | 256,000 | 8,192 | no | text  
`hf:Qwen/Qwen3-VL-235B-A22B-Instruct` | 250,000 | 8,192 | no | text + image  
`hf:zai-org/GLM-4.5` | 128,000 | 128,000 | no | text  
`hf:zai-org/GLM-4.6` | 198,000 | 128,000 | no | text  
`hf:zai-org/GLM-5` | 256,000 | 128,000 | sì | text + image  
`hf:deepseek-ai/DeepSeek-V3` | 128,000 | 8,192 | no | text  
`hf:Qwen/Qwen3-235B-A22B-Thinking-2507` | 256,000 | 8,192 | sì | text  
  
Allowlist dei modelli

Se abiliti una allowlist dei modelli (`agents.defaults.models`), aggiungi ogni modello Synthetic che intendi usare. I modelli non presenti nell'allowlist verranno nascosti all'agente.

Override dell'URL base

Se Synthetic cambia il proprio endpoint API, sovrascrivi l'URL base nella tua configurazione:

json5Copy code
[code]
    {  models: {    providers: {      synthetic: {        baseUrl: "https://new-api.synthetic.new/anthropic",      },    },  },}
[/code]

Ricorda che OpenClaw aggiunge automaticamente `/v1`.

## Correlati

[**Selezione del modello** Regole dei provider, riferimenti dei modelli e comportamento di failover. ](</it/concepts/model-providers>) [**Configuration reference** Schema completo di configurazione, incluse le impostazioni del provider. ](</it/gateway/configuration-reference>) [**Synthetic** Dashboard Synthetic e documentazione API. ](<https://synthetic.new>)

Was this useful?YesNo