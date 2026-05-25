---
title: StepFun
source_url: https://docs.openclaw.ai/it/providers/stepfun
scraped_at: 2026-05-25
---

OpenClaw include un plugin provider StepFun integrato con due ID provider:

  * `stepfun` per l'endpoint standard
  * `stepfun-plan` per l'endpoint Step Plan


## Panoramica di area geografica ed endpoint

Endpoint | Cina (`.com`) | Globale (`.ai`)  
---|---|---  
Standard | `https://api.stepfun.com/v1` | `https://api.stepfun.ai/v1`  
Step Plan | `https://api.stepfun.com/step_plan/v1` | `https://api.stepfun.ai/step_plan/v1`  
  
Variabile d'ambiente di autenticazione: `STEPFUN_API_KEY`

## Catalogo integrato

Standard (`stepfun`):

Riferimento modello | Contesto | Output massimo | Note  
---|---|---|---  
`stepfun/step-3.5-flash` | 262,144 | 65,536 | Modello standard predefinito  
  
Step Plan (`stepfun-plan`):

Riferimento modello | Contesto | Output massimo | Note  
---|---|---|---  
`stepfun-plan/step-3.5-flash` | 262,144 | 65,536 | Modello Step Plan predefinito  
`stepfun-plan/step-3.5-flash-2603` | 262,144 | 65,536 | Modello Step Plan aggiuntivo  
  
## Primi passi

Scegli la superficie del provider e segui i passaggi di configurazione.

### Standard

**Ideale per:** uso generico tramite l'endpoint StepFun standard.

* ### Scegli l'area geografica del tuo endpoint

Scelta di autenticazione | Endpoint | Area geografica  
---|---|---  
`stepfun-standard-api-key-intl` | `https://api.stepfun.ai/v1` | Internazionale  
`stepfun-standard-api-key-cn` | `https://api.stepfun.com/v1` | Cina  
* ### Esegui l'onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl
[/code]

Oppure per l'endpoint Cina:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-cn
[/code]

* ### Alternativa non interattiva

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Verifica che i modelli siano disponibili

bashCopy code
[code]
    openclaw models list --provider stepfun
[/code]

### Riferimenti modello

  * Modello predefinito: `stepfun/step-3.5-flash`


### Step Plan

**Ideale per:** endpoint di ragionamento Step Plan.

* ### Scegli l'area geografica del tuo endpoint

Scelta di autenticazione | Endpoint | Area geografica  
---|---|---  
`stepfun-plan-api-key-intl` | `https://api.stepfun.ai/step_plan/v1` | Internazionale  
`stepfun-plan-api-key-cn` | `https://api.stepfun.com/step_plan/v1` | Cina  
* ### Esegui l'onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl
[/code]

Oppure per l'endpoint Cina:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-cn
[/code]

* ### Alternativa non interattiva

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Verifica che i modelli siano disponibili

bashCopy code
[code]
    openclaw models list --provider stepfun-plan
[/code]

### Riferimenti modello

  * Modello predefinito: `stepfun-plan/step-3.5-flash`
  * Modello alternativo: `stepfun-plan/step-3.5-flash-2603`


## Configurazione avanzata

Configurazione completa: provider Standard json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      stepfun: {        baseUrl: "https://api.stepfun.ai/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Configurazione completa: provider Step Plan json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun-plan/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      "stepfun-plan": {        baseUrl: "https://api.stepfun.ai/step_plan/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },          {            id: "step-3.5-flash-2603",            name: "Step 3.5 Flash 2603",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Note

  * Il provider è integrato in OpenClaw, quindi non è necessario un passaggio separato di installazione del plugin.
  * `step-3.5-flash-2603` è attualmente esposto solo su `stepfun-plan`.
  * Un singolo flusso di autenticazione scrive profili corrispondenti all'area geografica per sia `stepfun` sia `stepfun-plan`, così entrambe le superfici possono essere scoperte insieme.
  * Usa `openclaw models list` e `openclaw models set <provider/model>` per ispezionare o cambiare modelli.


## Correlati

[**Selezione del modello** Panoramica di tutti i provider, riferimenti modello e comportamento di failover. ](</it/concepts/model-providers>) [**Riferimento di configurazione** Schema di configurazione completo per provider, modelli e plugin. ](</it/gateway/configuration-reference>) [**Selezione del modello** Come scegliere e configurare i modelli. ](</it/concepts/models>) [**Piattaforma StepFun** Gestione e documentazione delle chiavi API StepFun. ](<https://platform.stepfun.com>)

Was this useful?YesNo