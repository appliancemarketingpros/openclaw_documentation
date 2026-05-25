---
title: StepFun
source_url: https://docs.openclaw.ai/pt-BR/providers/stepfun
scraped_at: 2026-05-25
---

OpenClaw inclui um Plugin de provedor StepFun integrado com dois IDs de provedor:

  * `stepfun` para o endpoint padrão
  * `stepfun-plan` para o endpoint Step Plan


## Visão geral de região e endpoint

Endpoint | China (`.com`) | Global (`.ai`)  
---|---|---  
Standard | `https://api.stepfun.com/v1` | `https://api.stepfun.ai/v1`  
Step Plan | `https://api.stepfun.com/step_plan/v1` | `https://api.stepfun.ai/step_plan/v1`  
  
Variável de ambiente de autenticação: `STEPFUN_API_KEY`

## Catálogo integrado

Standard (`stepfun`):

Ref do modelo | Contexto | Saída máx. | Observações  
---|---|---|---  
`stepfun/step-3.5-flash` | 262,144 | 65,536 | Modelo padrão Standard  
  
Step Plan (`stepfun-plan`):

Ref do modelo | Contexto | Saída máx. | Observações  
---|---|---|---  
`stepfun-plan/step-3.5-flash` | 262,144 | 65,536 | Modelo padrão Step Plan  
`stepfun-plan/step-3.5-flash-2603` | 262,144 | 65,536 | Modelo Step Plan adicional  
  
## Primeiros passos

Escolha a superfície do provedor e siga as etapas de configuração.

### Standard

**Ideal para:** uso de propósito geral pelo endpoint Standard da StepFun.

* ### Escolha a região do endpoint

Opção de autenticação | Endpoint | Região  
---|---|---  
`stepfun-standard-api-key-intl` | `https://api.stepfun.ai/v1` | Internacional  
`stepfun-standard-api-key-cn` | `https://api.stepfun.com/v1` | China  
* ### Execute o onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl
[/code]

Ou para o endpoint da China:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-cn
[/code]

* ### Alternativa não interativa

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Verifique se os modelos estão disponíveis

bashCopy code
[code]
    openclaw models list --provider stepfun
[/code]

### Refs de modelo

  * Modelo padrão: `stepfun/step-3.5-flash`


### Step Plan

**Ideal para:** endpoint de raciocínio Step Plan.

* ### Escolha a região do endpoint

Opção de autenticação | Endpoint | Região  
---|---|---  
`stepfun-plan-api-key-intl` | `https://api.stepfun.ai/step_plan/v1` | Internacional  
`stepfun-plan-api-key-cn` | `https://api.stepfun.com/step_plan/v1` | China  
* ### Execute o onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl
[/code]

Ou para o endpoint da China:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-cn
[/code]

* ### Alternativa não interativa

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Verifique se os modelos estão disponíveis

bashCopy code
[code]
    openclaw models list --provider stepfun-plan
[/code]

### Refs de modelo

  * Modelo padrão: `stepfun-plan/step-3.5-flash`
  * Modelo alternativo: `stepfun-plan/step-3.5-flash-2603`


## Configuração avançada

Configuração completa: provedor Standard json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      stepfun: {        baseUrl: "https://api.stepfun.ai/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Configuração completa: provedor Step Plan json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun-plan/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      "stepfun-plan": {        baseUrl: "https://api.stepfun.ai/step_plan/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },          {            id: "step-3.5-flash-2603",            name: "Step 3.5 Flash 2603",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Observações

  * O provedor é integrado ao OpenClaw, portanto não há uma etapa separada de instalação de Plugin.
  * `step-3.5-flash-2603` atualmente é exposto apenas em `stepfun-plan`.
  * Um único fluxo de autenticação grava perfis correspondentes à região para `stepfun` e `stepfun-plan`, portanto as duas superfícies podem ser descobertas juntas.
  * Use `openclaw models list` e `openclaw models set <provider/model>` para inspecionar ou trocar modelos.


## Relacionados

[**Seleção de modelo** Visão geral de todos os provedores, refs de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Referência de configuração** Esquema completo de configuração para provedores, modelos e plugins. ](</pt-BR/gateway/configuration-reference>) [**Seleção de modelo** Como escolher e configurar modelos. ](</pt-BR/concepts/models>) [**Plataforma StepFun** Gerenciamento de chaves de API e documentação da StepFun. ](<https://platform.stepfun.com>)

Was this useful?YesNo