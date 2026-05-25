---
title: StepFun
source_url: https://docs.openclaw.ai/fr/providers/stepfun
scraped_at: 2026-05-25
---

OpenClaw inclut un plugin fournisseur StepFun intégré avec deux identifiants de fournisseur :

  * `stepfun` pour le point de terminaison standard
  * `stepfun-plan` pour le point de terminaison Step Plan


## Vue d’ensemble des régions et des points de terminaison

Point de terminaison | Chine (`.com`) | Global (`.ai`)  
---|---|---  
Standard | `https://api.stepfun.com/v1` | `https://api.stepfun.ai/v1`  
Step Plan | `https://api.stepfun.com/step_plan/v1` | `https://api.stepfun.ai/step_plan/v1`  
  
Variable d’environnement d’authentification : `STEPFUN_API_KEY`

## Catalogue intégré

Standard (`stepfun`) :

Référence de modèle | Contexte | Sortie max. | Notes  
---|---|---|---  
`stepfun/step-3.5-flash` | 262,144 | 65,536 | Modèle standard par défaut  
  
Step Plan (`stepfun-plan`) :

Référence de modèle | Contexte | Sortie max. | Notes  
---|---|---|---  
`stepfun-plan/step-3.5-flash` | 262,144 | 65,536 | Modèle Step Plan par défaut  
`stepfun-plan/step-3.5-flash-2603` | 262,144 | 65,536 | Modèle Step Plan supplémentaire  
  
## Prise en main

Choisissez votre surface de fournisseur et suivez les étapes de configuration.

### Standard

**Idéal pour :** une utilisation générale via le point de terminaison StepFun standard.

* ### Choisir votre région de point de terminaison

Choix d’authentification | Point de terminaison | Région  
---|---|---  
`stepfun-standard-api-key-intl` | `https://api.stepfun.ai/v1` | International  
`stepfun-standard-api-key-cn` | `https://api.stepfun.com/v1` | Chine  
* ### Exécuter l’onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl
[/code]

Ou pour le point de terminaison Chine :

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-cn
[/code]

* ### Alternative non interactive

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Vérifier que les modèles sont disponibles

bashCopy code
[code]
    openclaw models list --provider stepfun
[/code]

### Références de modèle

  * Modèle par défaut : `stepfun/step-3.5-flash`


### Step Plan

**Idéal pour :** le point de terminaison de raisonnement Step Plan.

* ### Choisir votre région de point de terminaison

Choix d’authentification | Point de terminaison | Région  
---|---|---  
`stepfun-plan-api-key-intl` | `https://api.stepfun.ai/step_plan/v1` | International  
`stepfun-plan-api-key-cn` | `https://api.stepfun.com/step_plan/v1` | Chine  
* ### Exécuter l’onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl
[/code]

Ou pour le point de terminaison Chine :

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-cn
[/code]

* ### Alternative non interactive

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Vérifier que les modèles sont disponibles

bashCopy code
[code]
    openclaw models list --provider stepfun-plan
[/code]

### Références de modèle

  * Modèle par défaut : `stepfun-plan/step-3.5-flash`
  * Modèle alternatif : `stepfun-plan/step-3.5-flash-2603`


## Configuration avancée

Configuration complète : fournisseur Standard json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      stepfun: {        baseUrl: "https://api.stepfun.ai/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Configuration complète : fournisseur Step Plan json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun-plan/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      "stepfun-plan": {        baseUrl: "https://api.stepfun.ai/step_plan/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },          {            id: "step-3.5-flash-2603",            name: "Step 3.5 Flash 2603",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Notes

  * Le fournisseur est intégré à OpenClaw ; il n’y a donc aucune étape distincte d’installation de plugin.
  * `step-3.5-flash-2603` est actuellement exposé uniquement sur `stepfun-plan`.
  * Un flux d’authentification unique écrit des profils correspondant à la région pour `stepfun` et `stepfun-plan`, ce qui permet de découvrir les deux surfaces ensemble.
  * Utilisez `openclaw models list` et `openclaw models set <provider/model>` pour inspecter ou changer de modèle.


## Connexe

[**Sélection de modèle** Vue d’ensemble de tous les fournisseurs, références de modèle et comportement de basculement. ](</fr/concepts/model-providers>) [**Référence de configuration** Schéma de configuration complet pour les fournisseurs, les modèles et les plugins. ](</fr/gateway/configuration-reference>) [**Sélection de modèle** Comment choisir et configurer les modèles. ](</fr/concepts/models>) [**Plateforme StepFun** Gestion des clés d’API StepFun et documentation. ](<https://platform.stepfun.com>)

Was this useful?YesNo