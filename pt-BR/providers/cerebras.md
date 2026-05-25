---
title: Cerebras
source_url: https://docs.openclaw.ai/pt-BR/providers/cerebras
scraped_at: 2026-05-25
---

[Cerebras](<https://www.cerebras.ai>) fornece inferência de alta velocidade compatível com OpenAI em hardware de inferência personalizado. OpenClaw inclui um plugin de provedor Cerebras incluído com um catálogo estático de quatro modelos.

Propriedade | Valor  
---|---  
ID do provedor | `cerebras`  
Plugin | incluído, `enabledByDefault: true`  
Var. de env de auth | `CEREBRAS_API_KEY`  
Flag de onboarding | `--auth-choice cerebras-api-key`  
Flag direta da CLI | `--cerebras-api-key <key>`  
API | compatível com OpenAI (`openai-completions`)  
URL base | `https://api.cerebras.ai/v1`  
Modelo padrão | `cerebras/zai-glm-4.7`  
  
## Primeiros passos

* ### Obtenha uma chave de API

Crie uma chave de API no [Cerebras Cloud Console](<https://cloud.cerebras.ai>).

* ### Execute o onboarding

OnboardingCopy code
[code]
    openclaw onboard --auth-choice cerebras-api-key
[/code]

Flag diretaCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice cerebras-api-key \--cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

Somente envCopy code
[code]
    export CEREBRAS_API_KEY=csk-...
[/code]

* ### Verifique se os modelos estão disponíveis

bashCopy code
[code]
    openclaw models list --provider cerebras
[/code]

A lista deve incluir todos os quatro modelos incluídos. Se `CEREBRAS_API_KEY` não for resolvida, `openclaw models status --json` relata a credencial ausente em `auth.unusableProfiles`.

## Configuração não interativa

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cerebras-api-key \  --cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

## Catálogo integrado

OpenClaw vem com um catálogo estático da Cerebras que espelha o endpoint público compatível com OpenAI. Todos os quatro modelos compartilham um contexto de 128k e 8.192 tokens de saída máximos.

Ref. do modelo | Nome | Raciocínio | Observações  
---|---|---|---  
`cerebras/zai-glm-4.7` | [Z.ai](<http://Z.ai>) GLM 4.7 | sim | Modelo padrão; modelo de raciocínio em prévia  
`cerebras/gpt-oss-120b` | GPT OSS 120B | sim | Modelo de raciocínio de produção  
`cerebras/qwen-3-235b-a22b-instruct-2507` | Qwen 3 235B Instruct | não | Modelo em prévia sem raciocínio  
`cerebras/llama3.1-8b` | Llama 3.1 8B | não | Modelo de produção focado em velocidade  
  
## Configuração manual

O plugin incluído geralmente significa que você só precisa da chave de API. Use a configuração explícita `models.providers.cerebras` quando quiser substituir metadados de modelo ou executar em `mode: "merge"` contra o catálogo estático:

json5Copy code
[code]
    {  env: { CEREBRAS_API_KEY: "csk-..." },  agents: {    defaults: {      model: { primary: "cerebras/zai-glm-4.7" },    },  },  models: {    mode: "merge",    providers: {      cerebras: {        baseUrl: "https://api.cerebras.ai/v1",        apiKey: "${CEREBRAS_API_KEY}",        api: "openai-completions",        models: [          { id: "zai-glm-4.7", name: "Z.ai GLM 4.7" },          { id: "gpt-oss-120b", name: "GPT OSS 120B" },        ],      },    },  },}
[/code]

## Relacionado

[**Provedores de modelos** Escolha de provedores, refs. de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Modos de pensamento** Níveis de esforço de raciocínio para os dois modelos Cerebras com capacidade de raciocínio. ](</pt-BR/tools/thinking>) [**Referência de configuração** Padrões de agente e configuração de modelo. ](</pt-BR/gateway/config-agents#agent-defaults>) [**FAQ de modelos** Perfis de autenticação, troca de modelos e resolução de erros de "no profile". ](</pt-BR/help/faq-models>)

Was this useful?YesNo