---
title: Mistral
source_url: https://docs.openclaw.ai/pt-BR/providers/mistral
scraped_at: 2026-05-25
---

OpenClaw inclui um Plugin Mistral integrado que registra quatro contratos: preenchimentos de chat, compreensão de mídia (transcrição em lote Voxtral), STT em tempo real para Voice Call (Voxtral Realtime) e embeddings de memória (`mistral-embed`).

Propriedade | Valor  
---|---  
ID do provedor | `mistral`  
Plugin | integrado, `enabledByDefault: true`  
Variável de ambiente de autenticação | `MISTRAL_API_KEY`  
Flag de onboarding | `--auth-choice mistral-api-key`  
Flag direta da CLI | `--mistral-api-key <key>`  
API | compatível com OpenAI (`openai-completions`)  
URL base | `https://api.mistral.ai/v1`  
Modelo padrão | `mistral/mistral-large-latest`  
Modelo de embedding | `mistral-embed`  
Lote Voxtral | `voxtral-mini-latest` (transcrição de áudio)  
Voxtral em tempo real | `voxtral-mini-transcribe-realtime-2602`  
  
## Primeiros passos

* ### Get your API key

Crie uma chave de API no [Mistral Console](<https://console.mistral.ai/>).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice mistral-api-key
[/code]

Ou passe a chave diretamente:

bashCopy code
[code]
    openclaw onboard --mistral-api-key "$MISTRAL_API_KEY"
[/code]

* ### Set a default model

json5Copy code
[code]
    {  env: { MISTRAL_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "mistral/mistral-large-latest" } } },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider mistral
[/code]

## Catálogo de LLM integrado

[Mistral Medium 3.5](<https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04>) é o modelo Medium combinado atual no catálogo integrado: pesos densos de 128B, entrada de texto e imagem, contexto de 256K, chamada de função, saída estruturada, codificação e raciocínio ajustável por meio da API Chat Completions. Use `mistral/mistral-medium-3-5` quando quiser o modelo agentivo/de codificação unificado mais recente da Mistral em vez do padrão `mistral/mistral-large-latest`.

Atualmente, o OpenClaw distribui este catálogo Mistral integrado:

Ref. do modelo | Entrada | Contexto | Saída máx. | Observações  
---|---|---|---|---  
`mistral/mistral-large-latest` | texto, imagem | 262,144 | 16,384 | Modelo padrão  
`mistral/mistral-medium-2508` | texto, imagem | 262,144 | 8,192 | Mistral Medium 3.1  
`mistral/mistral-medium-3-5` | texto, imagem | 262,144 | 8,192 | Mistral Medium 3.5; raciocínio ajustável  
`mistral/mistral-small-latest` | texto, imagem | 128,000 | 16,384 | Mistral Small 4; raciocínio ajustável via API `reasoning_effort`  
`mistral/pixtral-large-latest` | texto, imagem | 128,000 | 32,768 | Pixtral  
`mistral/codestral-latest` | texto | 256,000 | 4,096 | Codificação  
`mistral/devstral-medium-latest` | texto | 262,144 | 32,768 | Devstral 2  
`mistral/magistral-small` | texto | 128,000 | 40,000 | Com raciocínio habilitado  
  
Após o onboarding, faça um teste rápido do Medium 3.5 sem iniciar o Gateway:

bashCopy code
[code]
    openclaw infer model run --local \  --model mistral/mistral-medium-3-5 \  --prompt "Reply with exactly: mistral-ok" \  --json
[/code]

Para navegar pela linha do catálogo integrado antes de alterar a configuração:

bashCopy code
[code]
    openclaw models list --all --provider mistral --plain
[/code]

## Transcrição de áudio (Voxtral)

Use o Voxtral para transcrição de áudio em lote por meio do pipeline de compreensão de mídia.

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "mistral", model: "voxtral-mini-latest" }],      },    },  },}
[/code]

## STT de streaming para Voice Call

O Plugin `mistral` integrado registra o Voxtral Realtime como um provedor de STT de streaming para Voice Call.

Configuração | Caminho de configuração | Padrão  
---|---|---  
Chave de API | `plugins.entries.voice-call.config.streaming.providers.mistral.apiKey` | Usa `MISTRAL_API_KEY` como fallback  
Modelo | `...mistral.model` | `voxtral-mini-transcribe-realtime-2602`  
Codificação | `...mistral.encoding` | `pcm_mulaw`  
Taxa de amostragem | `...mistral.sampleRate` | `8000`  
Atraso alvo | `...mistral.targetStreamingDelayMs` | `800`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "mistral",            providers: {              mistral: {                apiKey: "${MISTRAL_API_KEY}",                targetStreamingDelayMs: 800,              },            },          },        },      },    },  },}
[/code]

## Configuração avançada

Adjustable reasoning

`mistral/mistral-small-latest` (Mistral Small 4) e `mistral/mistral-medium-3-5` oferecem suporte a [raciocínio ajustável](<https://docs.mistral.ai/studio-api/conversations/reasoning/adjustable>) na API Chat Completions via `reasoning_effort` (`none` minimiza pensamento extra na saída; `high` expõe rastros completos de pensamento antes da resposta final). A Mistral recomenda `reasoning_effort="high"` para casos de uso agentivos e de código com Medium 3.5.

O OpenClaw mapeia o nível de **thinking** da sessão para a API da Mistral:

Nível de thinking do OpenClaw | `reasoning_effort` da Mistral  
---|---  
**off** / **minimal** | `none`  
**low** / **medium** / **high** / **xhigh** / **adaptive** / **max** | `high`  
  
Exemplo de configuração com escopo de modelo para raciocínio do Medium 3.5:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "mistral/mistral-medium-3-5" },      models: {        "mistral/mistral-medium-3-5": {          params: { thinking: "high" },        },      },    },  },}
[/code]

Memory embeddings

A Mistral pode fornecer embeddings de memória via `/v1/embeddings` (modelo padrão: `mistral-embed`).

json5Copy code
[code]
    {  memorySearch: { provider: "mistral" },}
[/code]

Auth and base URL

  * A autenticação da Mistral usa `MISTRAL_API_KEY` (cabeçalho Bearer).
  * A URL base do provedor usa `https://api.mistral.ai/v1` por padrão e aceita o formato padrão de solicitação de chat-completions compatível com OpenAI.
  * O modelo padrão de onboarding é `mistral/mistral-large-latest`.
  * Substitua a URL base em `models.providers.mistral.baseUrl` somente quando a Mistral publicar explicitamente um endpoint regional de que você precise.


## Relacionado

[**Model selection** Escolha de provedores, refs de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Media understanding** Configuração de transcrição de áudio e seleção de provedor. ](</pt-BR/nodes/media-understanding>)

Was this useful?YesNo