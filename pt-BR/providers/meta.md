---
title: Metadados
source_url: https://docs.openclaw.ai/pt-BR/providers/meta
scraped_at: 2026-07-13
---

ModelsProviders

A **API da Meta** usa a **Responses API** compatível com a OpenAI (`POST /v1/responses`) para o modelo de raciocínio `muse-spark-1.1`. O provedor é distribuído como um plugin incluído no OpenClaw.

Propriedade | Valor  
---|---  
ID do provedor | `meta`  
Plugin | provedor incluído  
Variável de ambiente de autenticação | `MODEL_API_KEY`  
Sinalizador de integração inicial | `--auth-choice meta-api-key`  
Sinalizador direto da CLI | `--meta-api-key <key>`  
API | Responses API (`openai-responses`)  
URL base | `https://api.meta.ai/v1`  
Modelo padrão | `meta/muse-spark-1.1`  
Raciocínio padrão | `high` (`reasoning.effort`)  
  
## Primeiros passos

* ### Defina a chave da API

Integração inicialCopy code
[code]
    openclaw onboard --auth-choice meta-api-key
[/code]

Sinalizador diretoCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \--auth-choice meta-api-key \--meta-api-key "$MODEL_API_KEY"
[/code]

Somente variável de ambienteCopy code
[code]
    export MODEL_API_KEY=<key>
[/code]

* ### Verifique se os modelos estão disponíveis

bashCopy code
[code]
    openclaw models list --provider meta
[/code]

Lista a entrada estática `muse-spark-1.1` do catálogo. Se `MODEL_API_KEY` não for resolvida, `openclaw models status --json` informará a credencial ausente em `auth.unusableProfiles`.

## Configuração não interativa

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --mode local \  --auth-choice meta-api-key \  --meta-api-key "$MODEL_API_KEY"
[/code]

## Catálogo integrado

Referência do modelo | Nome | Raciocínio | Janela de contexto | Saída máxima  
---|---|---|---|---  
`meta/muse-spark-1.1` | Muse Spark 1.1 | sim | 1,048,576 | 131,072  
  
Recursos:

  * Entrada de texto e imagem
  * Chamada de ferramentas e transmissão contínua
  * Esforço de raciocínio: `minimal`, `low`, `medium`, `high`, `xhigh` (padrão: `high`)
  * Reprodução de raciocínio criptografado sem estado (`store: false`, `include: ["reasoning.encrypted_content"]`)


## Configuração manual

json5Copy code
[code]
    {  env: { MODEL_API_KEY: "<key>" },  agents: {    defaults: {      model: { primary: "meta/muse-spark-1.1" },      models: {        "meta/muse-spark-1.1": { alias: "Muse Spark 1.1" },      },    },  },}
[/code]

## Teste de fumaça

bashCopy code
[code]
    export MODEL_API_KEY=<key>pnpm test:live -- extensions/meta/meta.live.test.ts
[/code]

Os testes em tempo real usam `muse-spark-1.1` com `POST /v1/responses`.

## Relacionado

[**Provedores de modelos** Escolha de provedores, referências de modelos e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Modos de pensamento** Níveis de esforço de raciocínio para o muse-spark-1.1. ](</pt-BR/tools/thinking>) [**Referência de configuração** Padrões dos agentes e configuração de modelos. ](</pt-BR/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue