---
title: StepFun
source_url: https://docs.openclaw.ai/pl/providers/stepfun
scraped_at: 2026-05-25
---

OpenClaw zawiera wbudowany Plugin dostawcy StepFun z dwoma identyfikatorami dostawcy:

  * `stepfun` dla standardowego punktu końcowego
  * `stepfun-plan` dla punktu końcowego Step Plan


## Omówienie regionów i punktów końcowych

Punkt końcowy | Chiny (`.com`) | Globalny (`.ai`)  
---|---|---  
Standardowy | `https://api.stepfun.com/v1` | `https://api.stepfun.ai/v1`  
Step Plan | `https://api.stepfun.com/step_plan/v1` | `https://api.stepfun.ai/step_plan/v1`  
  
Zmienna env uwierzytelniania: `STEPFUN_API_KEY`

## Wbudowany katalog

Standardowy (`stepfun`):

Odwołanie do modelu | Kontekst | Maks. dane wyjściowe | Uwagi  
---|---|---|---  
`stepfun/step-3.5-flash` | 262,144 | 65,536 | Domyślny model standardowy  
  
Step Plan (`stepfun-plan`):

Odwołanie do modelu | Kontekst | Maks. dane wyjściowe | Uwagi  
---|---|---|---  
`stepfun-plan/step-3.5-flash` | 262,144 | 65,536 | Domyślny model Step Plan  
`stepfun-plan/step-3.5-flash-2603` | 262,144 | 65,536 | Dodatkowy model Step Plan  
  
## Pierwsze kroki

Wybierz powierzchnię dostawcy i wykonaj kroki konfiguracji.

### Standardowy

**Najlepsze do:** zastosowań ogólnych przez standardowy punkt końcowy StepFun.

* ### Wybierz region punktu końcowego

Wybór uwierzytelniania | Punkt końcowy | Region  
---|---|---  
`stepfun-standard-api-key-intl` | `https://api.stepfun.ai/v1` | Międzynarodowy  
`stepfun-standard-api-key-cn` | `https://api.stepfun.com/v1` | Chiny  
* ### Uruchom onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl
[/code]

Albo dla chińskiego punktu końcowego:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-cn
[/code]

* ### Alternatywa nieinteraktywna

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Sprawdź, czy modele są dostępne

bashCopy code
[code]
    openclaw models list --provider stepfun
[/code]

### Odwołania do modeli

  * Model domyślny: `stepfun/step-3.5-flash`


### Step Plan

**Najlepsze do:** punktu końcowego rozumowania Step Plan.

* ### Wybierz region punktu końcowego

Wybór uwierzytelniania | Punkt końcowy | Region  
---|---|---  
`stepfun-plan-api-key-intl` | `https://api.stepfun.ai/step_plan/v1` | Międzynarodowy  
`stepfun-plan-api-key-cn` | `https://api.stepfun.com/step_plan/v1` | Chiny  
* ### Uruchom onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl
[/code]

Albo dla chińskiego punktu końcowego:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-cn
[/code]

* ### Alternatywa nieinteraktywna

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Sprawdź, czy modele są dostępne

bashCopy code
[code]
    openclaw models list --provider stepfun-plan
[/code]

### Odwołania do modeli

  * Model domyślny: `stepfun-plan/step-3.5-flash`
  * Model alternatywny: `stepfun-plan/step-3.5-flash-2603`


## Konfiguracja zaawansowana

Pełna konfiguracja: dostawca standardowy json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      stepfun: {        baseUrl: "https://api.stepfun.ai/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Pełna konfiguracja: dostawca Step Plan json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun-plan/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      "stepfun-plan": {        baseUrl: "https://api.stepfun.ai/step_plan/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },          {            id: "step-3.5-flash-2603",            name: "Step 3.5 Flash 2603",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Uwagi

  * Dostawca jest dołączony do OpenClaw, więc nie ma oddzielnego kroku instalacji Plugin.
  * `step-3.5-flash-2603` jest obecnie udostępniony tylko w `stepfun-plan`.
  * Pojedynczy przepływ uwierzytelniania zapisuje profile dopasowane do regionu zarówno dla `stepfun`, jak i `stepfun-plan`, więc obie powierzchnie można wykrywać razem.
  * Użyj `openclaw models list` i `openclaw models set <provider/model>`, aby sprawdzać lub przełączać modele.


## Powiązane

[**Wybór modelu** Omówienie wszystkich dostawców, odwołań do modeli i zachowania przełączania awaryjnego. ](</pl/concepts/model-providers>) [**Informacje o konfiguracji** Pełny schemat konfiguracji dostawców, modeli i plugins. ](</pl/gateway/configuration-reference>) [**Wybór modelu** Jak wybierać i konfigurować modele. ](</pl/concepts/models>) [**Platforma StepFun** Zarządzanie kluczami API StepFun i dokumentacja. ](<https://platform.stepfun.com>)

Was this useful?YesNo