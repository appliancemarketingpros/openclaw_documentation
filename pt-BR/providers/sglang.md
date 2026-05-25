---
title: SGLang
source_url: https://docs.openclaw.ai/pt-BR/providers/sglang
scraped_at: 2026-05-25
---

SGLang serve modelos de peso aberto por meio de uma API HTTP compatível com OpenAI. OpenClaw se conecta ao SGLang usando a família de provedores `openai-completions` com descoberta automática dos modelos disponíveis.

Propriedade | Valor  
---|---  
ID do provedor | `sglang`  
Plugin | incluído, `enabledByDefault: true`  
Variável de ambiente de auth | `SGLANG_API_KEY` (qualquer valor não vazio se o servidor não tiver auth)  
Flag de onboarding | `--auth-choice sglang`  
API | compatível com OpenAI (`openai-completions`)  
URL base padrão | `http://127.0.0.1:30000/v1`  
Placeholder de modelo padrão | `sglang/Qwen/Qwen3-8B`  
Uso de streaming | Sim (`supportsStreamingUsage: true`)  
Preços | Marcado como externo gratuito (`modelPricing.external: false`)  
  
OpenClaw também **descobre automaticamente** os modelos disponíveis do SGLang quando você opta por isso com `SGLANG_API_KEY`. Use `sglang/*` em `agents.defaults.models` para manter a descoberta dinâmica quando você também configura uma URL base personalizada do SGLang. Veja Descoberta de modelos (provedor implícito) abaixo.

## Primeiros passos

* ### Iniciar o SGLang

Inicie o SGLang com um servidor compatível com OpenAI. Sua URL base deve expor endpoints `/v1` (por exemplo, `/v1/models`, `/v1/chat/completions`). SGLang normalmente é executado em:

  * `http://127.0.0.1:30000/v1`


* ### Definir uma chave de API

Qualquer valor funciona se nenhuma auth estiver configurada no seu servidor:

bashCopy code
[code]
    export SGLANG_API_KEY="sglang-local"
[/code]

* ### Executar o onboarding ou definir um modelo diretamente

bashCopy code
[code]
    openclaw onboard
[/code]

Ou configure o modelo manualmente:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "sglang/your-model-id" },    },  },}
[/code]

## Descoberta de modelos (provedor implícito)

Quando `SGLANG_API_KEY` está definido (ou existe um perfil de auth) e você **não** define `models.providers.sglang`, o OpenClaw consultará:

  * `GET http://127.0.0.1:30000/v1/models`


e converterá os IDs retornados em entradas de modelo.

## Configuração explícita (modelos manuais)

Use configuração explícita quando:

  * O SGLang é executado em outro host/porta.
  * Você quer fixar valores de `contextWindow`/`maxTokens`.
  * Seu servidor exige uma chave de API real (ou você quer controlar headers).

json5Copy code
[code]
    {  models: {    providers: {      sglang: {        baseUrl: "http://127.0.0.1:30000/v1",        apiKey: "${SGLANG_API_KEY}",        api: "openai-completions",        models: [          {            id: "your-model-id",            name: "Local SGLang Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## Configuração avançada

Comportamento no estilo proxy

SGLang é tratado como um backend `/v1` compatível com OpenAI no estilo proxy, não como um endpoint nativo da OpenAI.

Comportamento | SGLang  
---|---  
Formatação de requisição exclusiva da OpenAI | Não aplicada  
`service_tier`, Responses `store`, dicas de cache de prompt | Não enviados  
Formatação de payload compatível com reasoning | Não aplicada  
Headers de atribuição ocultos (`originator`, `version`, `User-Agent`) | Não injetados em URLs base personalizadas do SGLang  
Solução de problemas

**Servidor inacessível**

Verifique se o servidor está em execução e respondendo:

bashCopy code
[code]
    curl http://127.0.0.1:30000/v1/models
[/code]

**Erros de auth**

Se as requisições falharem com erros de auth, defina um `SGLANG_API_KEY` real que corresponda à configuração do seu servidor, ou configure o provedor explicitamente em `models.providers.sglang`.

## Relacionado

[**Seleção de modelo** Escolha de provedores, referências de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Referência de configuração** Esquema completo de configuração, incluindo entradas de provedor. ](</pt-BR/gateway/configuration-reference>)

Was this useful?YesNo