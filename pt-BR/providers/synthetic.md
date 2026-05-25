---
title: Synthetic
source_url: https://docs.openclaw.ai/pt-BR/providers/synthetic
scraped_at: 2026-05-25
---

[Synthetic](<https://synthetic.new>) expõe endpoints compatíveis com Anthropic. O OpenClaw a registra como o provedor `synthetic` e usa a API Anthropic Messages.

Propriedade | Valor  
---|---  
Provedor | `synthetic`  
Autenticação | `SYNTHETIC_API_KEY`  
API | Anthropic Messages  
Base URL | `https://api.synthetic.new/anthropic`  
  
## Primeiros passos

* ### Obter uma chave de API

Obtenha uma `SYNTHETIC_API_KEY` na sua conta Synthetic ou deixe o assistente de onboarding solicitá-la para você.

* ### Executar o onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice synthetic-api-key
[/code]

* ### Verificar o modelo padrão

Após o onboarding, o modelo padrão é definido como:

CodeCopy code
[code]
    synthetic/hf:MiniMaxAI/MiniMax-M2.5
[/code]

## Exemplo de configuração

json5Copy code
[code]
    {  env: { SYNTHETIC_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.5" },      models: { "synthetic/hf:MiniMaxAI/MiniMax-M2.5": { alias: "MiniMax M2.5" } },    },  },  models: {    mode: "merge",    providers: {      synthetic: {        baseUrl: "https://api.synthetic.new/anthropic",        apiKey: "${SYNTHETIC_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "hf:MiniMaxAI/MiniMax-M2.5",            name: "MiniMax M2.5",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 192000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## Catálogo integrado

Todos os modelos Synthetic usam custo `0` (entrada/saída/cache).

ID do modelo | Janela de contexto | Máx. de tokens | Reasoning | Entrada  
---|---|---|---|---  
`hf:MiniMaxAI/MiniMax-M2.5` | 192,000 | 65,536 | não | text  
`hf:moonshotai/Kimi-K2-Thinking` | 256,000 | 8,192 | sim | text  
`hf:zai-org/GLM-4.7` | 198,000 | 128,000 | não | text  
`hf:deepseek-ai/DeepSeek-R1-0528` | 128,000 | 8,192 | não | text  
`hf:deepseek-ai/DeepSeek-V3-0324` | 128,000 | 8,192 | não | text  
`hf:deepseek-ai/DeepSeek-V3.1` | 128,000 | 8,192 | não | text  
`hf:deepseek-ai/DeepSeek-V3.1-Terminus` | 128,000 | 8,192 | não | text  
`hf:deepseek-ai/DeepSeek-V3.2` | 159,000 | 8,192 | não | text  
`hf:meta-llama/Llama-3.3-70B-Instruct` | 128,000 | 8,192 | não | text  
`hf:meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | 524,000 | 8,192 | não | text  
`hf:moonshotai/Kimi-K2-Instruct-0905` | 256,000 | 8,192 | não | text  
`hf:moonshotai/Kimi-K2.5` | 256,000 | 8,192 | sim | text + image  
`hf:openai/gpt-oss-120b` | 128,000 | 8,192 | não | text  
`hf:Qwen/Qwen3-235B-A22B-Instruct-2507` | 256,000 | 8,192 | não | text  
`hf:Qwen/Qwen3-Coder-480B-A35B-Instruct` | 256,000 | 8,192 | não | text  
`hf:Qwen/Qwen3-VL-235B-A22B-Instruct` | 250,000 | 8,192 | não | text + image  
`hf:zai-org/GLM-4.5` | 128,000 | 128,000 | não | text  
`hf:zai-org/GLM-4.6` | 198,000 | 128,000 | não | text  
`hf:zai-org/GLM-5` | 256,000 | 128,000 | sim | text + image  
`hf:deepseek-ai/DeepSeek-V3` | 128,000 | 8,192 | não | text  
`hf:Qwen/Qwen3-235B-A22B-Thinking-2507` | 256,000 | 8,192 | sim | text  
  
Allowlist de modelos

Se você habilitar uma allowlist de modelos (`agents.defaults.models`), adicione todos os modelos Synthetic que pretende usar. Modelos fora da allowlist ficarão ocultos para o agente.

Sobrescrita de base URL

Se a Synthetic alterar seu endpoint de API, sobrescreva a base URL na sua configuração:

json5Copy code
[code]
    {  models: {    providers: {      synthetic: {        baseUrl: "https://new-api.synthetic.new/anthropic",      },    },  },}
[/code]

Lembre-se de que o OpenClaw acrescenta `/v1` automaticamente.

## Relacionados

[**Seleção de modelo** Regras de provedor, referências de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Referência de configuração** Schema completo de configuração, incluindo definições de provedor. ](</pt-BR/gateway/configuration-reference>) [**Synthetic** Dashboard da Synthetic e documentação da API. ](<https://synthetic.new>)

Was this useful?YesNo