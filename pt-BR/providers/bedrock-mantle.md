---
title: Manto do Amazon Bedrock
source_url: https://docs.openclaw.ai/pt-BR/providers/bedrock-mantle
scraped_at: 2026-05-25
---

OpenClaw inclui um provedor **Amazon Bedrock Mantle** integrado que se conecta ao endpoint compatível com OpenAI da Mantle. A Mantle hospeda modelos de código aberto e de terceiros (GPT-OSS, Qwen, Kimi, GLM e similares) por meio de uma superfície padrão `/v1/chat/completions` apoiada pela infraestrutura da Bedrock.

Propriedade | Valor  
---|---  
ID do provedor | `amazon-bedrock-mantle`  
API | `openai-completions` (compatível com OpenAI) ou `anthropic-messages` (rota Anthropic Messages)  
Autenticação | `AWS_BEARER_TOKEN_BEDROCK` explícito ou geração de token bearer pela cadeia de credenciais do IAM  
Região padrão | `us-east-1` (substitua com `AWS_REGION` ou `AWS_DEFAULT_REGION`)  
  
## Primeiros passos

Escolha seu método de autenticação preferido e siga as etapas de configuração.

### Explicit bearer token

**Ideal para:** ambientes em que você já tem um token bearer da Mantle.

* ### Set the bearer token on the gateway host

bashCopy code
[code]
    export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

Opcionalmente, defina uma região (o padrão é `us-east-1`):

bashCopy code
[code]
    export AWS_REGION="us-west-2"
[/code]

* ### Verify models are discovered

bashCopy code
[code]
    openclaw models list
[/code]

Os modelos descobertos aparecem sob o provedor `amazon-bedrock-mantle`. Nenhuma configuração adicional é necessária, a menos que você queira substituir os padrões.

### IAM credentials

**Ideal para:** usar credenciais compatíveis com o AWS SDK (configuração compartilhada, SSO, identidade web, funções de instância ou de tarefa).

* ### Configure AWS credentials on the gateway host

Qualquer origem de autenticação compatível com o AWS SDK funciona:

bashCopy code
[code]
    export AWS_PROFILE="default"export AWS_REGION="us-west-2"
[/code]

* ### Verify models are discovered

bashCopy code
[code]
    openclaw models list
[/code]

O OpenClaw gera automaticamente um token bearer da Mantle a partir da cadeia de credenciais.

## Descoberta automática de modelos

Quando `AWS_BEARER_TOKEN_BEDROCK` está definido, o OpenClaw o usa diretamente. Caso contrário, o OpenClaw tenta gerar um token bearer da Mantle a partir da cadeia de credenciais padrão da AWS. Em seguida, ele descobre os modelos Mantle disponíveis consultando o endpoint `/v1/models` da região.

Comportamento | Detalhe  
---|---  
Cache de descoberta | Resultados em cache por 1 hora  
Atualização do token IAM | A cada hora  
  
Para manter o Plugin Mantle habilitado, mas suprimir a descoberta automática e a geração de token bearer do IAM pertencentes ao Plugin, desabilite a alternância de descoberta pertencente ao Plugin:

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock-mantle.config.discovery.enabled false
[/code]

### Regiões compatíveis

`us-east-1`, `us-east-2`, `us-west-2`, `ap-northeast-1`, `ap-south-1`, `ap-southeast-3`, `eu-central-1`, `eu-west-1`, `eu-west-2`, `eu-south-1`, `eu-north-1`, `sa-east-1`.

## Configuração manual

Se você preferir configuração explícita em vez de descoberta automática:

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        baseUrl: "https://bedrock-mantle.us-east-1.api.aws/v1",        api: "openai-completions",        auth: "api-key",        apiKey: "env:AWS_BEARER_TOKEN_BEDROCK",        models: [          {            id: "gpt-oss-120b",            name: "GPT-OSS 120B",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32000,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

## Configuração avançada

Reasoning support

O suporte a raciocínio é inferido a partir de IDs de modelo que contêm padrões como `thinking`, `reasoner` ou `gpt-oss-120b`. O OpenClaw define `reasoning: true` automaticamente para modelos correspondentes durante a descoberta.

Endpoint unavailability

Se o endpoint Mantle estiver indisponível ou não retornar modelos, o provedor será ignorado silenciosamente. O OpenClaw não gera erro; outros provedores configurados continuam funcionando normalmente.

Claude Opus 4.7 via the Anthropic Messages route

A Mantle também expõe uma rota Anthropic Messages que transporta modelos Claude pelo mesmo caminho de streaming autenticado por bearer. O Claude Opus 4.7 (`amazon-bedrock-mantle/claude-opus-4.7`) pode ser chamado por essa rota com streaming pertencente ao provedor, portanto os tokens bearer da AWS não são tratados como chaves de API da Anthropic.

Quando você fixa um modelo Anthropic Messages no provedor Mantle, o OpenClaw usa a superfície de API `anthropic-messages` em vez de `openai-completions` para esse modelo. A autenticação ainda vem de `AWS_BEARER_TOKEN_BEDROCK` (ou do token bearer IAM emitido).

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        models: [          {            id: "claude-opus-4.7",            name: "Claude Opus 4.7",            api: "anthropic-messages",            reasoning: true,            input: ["text", "image"],            contextWindow: 1000000,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Relationship to Amazon Bedrock provider

O Bedrock Mantle é um provedor separado do provedor [Amazon Bedrock](</pt-BR/providers/bedrock>) padrão. A Mantle usa uma superfície `/v1` compatível com OpenAI, enquanto o provedor Bedrock padrão usa a API nativa da Bedrock.

Ambos os provedores compartilham a mesma credencial `AWS_BEARER_TOKEN_BEDROCK` quando ela está presente.

## Relacionados

[**Amazon Bedrock** Provedor Bedrock nativo para Anthropic Claude, Titan e outros modelos. ](</pt-BR/providers/bedrock>) [**Model selection** Escolha de provedores, referências de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**OAuth and auth** Detalhes de autenticação e regras de reutilização de credenciais. ](</pt-BR/gateway/authentication>) [**Troubleshooting** Problemas comuns e como resolvê-los. ](</pt-BR/help/troubleshooting>)

Was this useful?YesNo