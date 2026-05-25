---
title: StepFun
source_url: https://docs.openclaw.ai/de/providers/stepfun
scraped_at: 2026-05-25
---

OpenClaw enthält ein gebündeltes StepFun-Provider-Plugin mit zwei Provider-IDs:

  * `stepfun` für den Standard-Endpunkt
  * `stepfun-plan` für den Step-Plan-Endpunkt


## Überblick über Region und Endpunkt

Endpunkt | China (`.com`) | Global (`.ai`)  
---|---|---  
Standard | `https://api.stepfun.com/v1` | `https://api.stepfun.ai/v1`  
Step Plan | `https://api.stepfun.com/step_plan/v1` | `https://api.stepfun.ai/step_plan/v1`  
  
Auth-Env-Var: `STEPFUN_API_KEY`

## Integrierter Katalog

Standard (`stepfun`):

Modellreferenz | Kontext | Max. Ausgabe | Hinweise  
---|---|---|---  
`stepfun/step-3.5-flash` | 262,144 | 65,536 | Standardmodell für Standard  
  
Step Plan (`stepfun-plan`):

Modellreferenz | Kontext | Max. Ausgabe | Hinweise  
---|---|---|---  
`stepfun-plan/step-3.5-flash` | 262,144 | 65,536 | Standardmodell für Step Plan  
`stepfun-plan/step-3.5-flash-2603` | 262,144 | 65,536 | Zusätzliches Step-Plan-Modell  
  
## Erste Schritte

Wählen Sie Ihre Provider-Oberfläche und folgen Sie den Einrichtungsschritten.

### Standard

**Am besten geeignet für:** allgemeine Nutzung über den Standard-Endpunkt von StepFun.

* ### Wählen Sie Ihre Endpunktregion

Authentifizierungsoption | Endpunkt | Region  
---|---|---  
`stepfun-standard-api-key-intl` | `https://api.stepfun.ai/v1` | International  
`stepfun-standard-api-key-cn` | `https://api.stepfun.com/v1` | China  
* ### Onboarding ausführen

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl
[/code]

Oder für den China-Endpunkt:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-cn
[/code]

* ### Nicht-interaktive Alternative

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Prüfen, ob Modelle verfügbar sind

bashCopy code
[code]
    openclaw models list --provider stepfun
[/code]

### Modellreferenzen

  * Standardmodell: `stepfun/step-3.5-flash`


### Step Plan

**Am besten geeignet für:** Step-Plan-Reasoning-Endpunkt.

* ### Wählen Sie Ihre Endpunktregion

Authentifizierungsoption | Endpunkt | Region  
---|---|---  
`stepfun-plan-api-key-intl` | `https://api.stepfun.ai/step_plan/v1` | International  
`stepfun-plan-api-key-cn` | `https://api.stepfun.com/step_plan/v1` | China  
* ### Onboarding ausführen

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl
[/code]

Oder für den China-Endpunkt:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-cn
[/code]

* ### Nicht-interaktive Alternative

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Prüfen, ob Modelle verfügbar sind

bashCopy code
[code]
    openclaw models list --provider stepfun-plan
[/code]

### Modellreferenzen

  * Standardmodell: `stepfun-plan/step-3.5-flash`
  * Alternatives Modell: `stepfun-plan/step-3.5-flash-2603`


## Erweiterte Konfiguration

Vollständige Konfiguration: Standard-Provider json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      stepfun: {        baseUrl: "https://api.stepfun.ai/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Vollständige Konfiguration: Step-Plan-Provider json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun-plan/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      "stepfun-plan": {        baseUrl: "https://api.stepfun.ai/step_plan/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },          {            id: "step-3.5-flash-2603",            name: "Step 3.5 Flash 2603",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Hinweise

  * Der Provider ist mit OpenClaw gebündelt, daher gibt es keinen separaten Installationsschritt für das Plugin.
  * `step-3.5-flash-2603` wird derzeit nur auf `stepfun-plan` bereitgestellt.
  * Ein einzelner Authentifizierungsablauf schreibt regionspassende Profile für `stepfun` und `stepfun-plan`, sodass beide Oberflächen gemeinsam erkannt werden können.
  * Verwenden Sie `openclaw models list` und `openclaw models set <provider/model>`, um Modelle zu prüfen oder zu wechseln.


## Verwandte Themen

[**Modellauswahl** Überblick über alle Provider, Modellreferenzen und Failover-Verhalten. ](</de/concepts/model-providers>) [**Konfigurationsreferenz** Vollständiges Konfigurationsschema für Provider, Modelle und Plugins. ](</de/gateway/configuration-reference>) [**Modellauswahl** So wählen und konfigurieren Sie Modelle. ](</de/concepts/models>) [**StepFun Platform** Verwaltung und Dokumentation von StepFun-API-Schlüsseln. ](<https://platform.stepfun.com>)

Was this useful?YesNo