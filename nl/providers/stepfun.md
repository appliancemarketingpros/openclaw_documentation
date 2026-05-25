---
title: StepFun
source_url: https://docs.openclaw.ai/nl/providers/stepfun
scraped_at: 2026-05-25
---

OpenClaw bevat een gebundelde StepFun-provider-Plugin met twee provider-id's:

  * `stepfun` voor het standaardendpoint
  * `stepfun-plan` voor het Step Plan-endpoint


## Overzicht van regio's en endpoints

Endpoint | China (`.com`) | Globaal (`.ai`)  
---|---|---  
Standard | `https://api.stepfun.com/v1` | `https://api.stepfun.ai/v1`  
Step Plan | `https://api.stepfun.com/step_plan/v1` | `https://api.stepfun.ai/step_plan/v1`  
  
Auth-omgevingsvariabele: `STEPFUN_API_KEY`

## Ingebouwde catalogus

Standard (`stepfun`):

Modelverwijzing | Context | Maximale uitvoer | Opmerkingen  
---|---|---|---  
`stepfun/step-3.5-flash` | 262,144 | 65,536 | Standaardmodel voor Standard  
  
Step Plan (`stepfun-plan`):

Modelverwijzing | Context | Maximale uitvoer | Opmerkingen  
---|---|---|---  
`stepfun-plan/step-3.5-flash` | 262,144 | 65,536 | Standaardmodel voor Step Plan  
`stepfun-plan/step-3.5-flash-2603` | 262,144 | 65,536 | Extra model voor Step Plan  
  
## Aan de slag

Kies je provideroppervlak en volg de installatiestappen.

### Standard

**Meest geschikt voor:** algemeen gebruik via het standaardendpoint van StepFun.

* ### Kies je endpointregio

Auth-keuze | Endpoint | Regio  
---|---|---  
`stepfun-standard-api-key-intl` | `https://api.stepfun.ai/v1` | Internationaal  
`stepfun-standard-api-key-cn` | `https://api.stepfun.com/v1` | China  
* ### Voer onboarding uit

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl
[/code]

Of voor het China-endpoint:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-cn
[/code]

* ### Niet-interactief alternatief

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Controleer of modellen beschikbaar zijn

bashCopy code
[code]
    openclaw models list --provider stepfun
[/code]

### Modelverwijzingen

  * Standaardmodel: `stepfun/step-3.5-flash`


### Step Plan

**Meest geschikt voor:** reasoning-endpoint van Step Plan.

* ### Kies je endpointregio

Auth-keuze | Endpoint | Regio  
---|---|---  
`stepfun-plan-api-key-intl` | `https://api.stepfun.ai/step_plan/v1` | Internationaal  
`stepfun-plan-api-key-cn` | `https://api.stepfun.com/step_plan/v1` | China  
* ### Voer onboarding uit

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl
[/code]

Of voor het China-endpoint:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-cn
[/code]

* ### Niet-interactief alternatief

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Controleer of modellen beschikbaar zijn

bashCopy code
[code]
    openclaw models list --provider stepfun-plan
[/code]

### Modelverwijzingen

  * Standaardmodel: `stepfun-plan/step-3.5-flash`
  * Alternatief model: `stepfun-plan/step-3.5-flash-2603`


## Geavanceerde configuratie

Volledige configuratie: Standard-provider json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      stepfun: {        baseUrl: "https://api.stepfun.ai/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Volledige configuratie: Step Plan-provider json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun-plan/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      "stepfun-plan": {        baseUrl: "https://api.stepfun.ai/step_plan/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },          {            id: "step-3.5-flash-2603",            name: "Step 3.5 Flash 2603",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Opmerkingen

  * De provider is gebundeld met OpenClaw, dus er is geen afzonderlijke installatiestap voor de Plugin.
  * `step-3.5-flash-2603` wordt momenteel alleen beschikbaar gemaakt op `stepfun-plan`.
  * Eén auth-flow schrijft regiogekoppelde profielen voor zowel `stepfun` als `stepfun-plan`, zodat beide oppervlakken samen kunnen worden ontdekt.
  * Gebruik `openclaw models list` en `openclaw models set <provider/model>` om modellen te inspecteren of te wisselen.


## Gerelateerd

[**Modelselectie** Overzicht van alle providers, modelverwijzingen en failovergedrag. ](</nl/concepts/model-providers>) [**Configuratiereferentie** Volledig configuratieschema voor providers, modellen en plugins. ](</nl/gateway/configuration-reference>) [**Modelselectie** Modellen kiezen en configureren. ](</nl/concepts/models>) [**StepFun Platform** Beheer en documentatie voor StepFun API-sleutels. ](<https://platform.stepfun.com>)

Was this useful?YesNo