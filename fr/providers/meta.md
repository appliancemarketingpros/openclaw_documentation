---
title: Méta
source_url: https://docs.openclaw.ai/fr/providers/meta
scraped_at: 2026-07-13
---

ModelsProviders

L’**API Meta** utilise l’**API Responses** compatible avec OpenAI (`POST /v1/responses`) pour le modèle de raisonnement `muse-spark-1.1`. Le fournisseur est distribué sous forme de plugin OpenClaw intégré.

Propriété | Valeur  
---|---  
Identifiant du fournisseur | `meta`  
Plugin | fournisseur intégré  
Variable d’environnement d’authentification | `MODEL_API_KEY`  
Option d’intégration | `--auth-choice meta-api-key`  
Option CLI directe | `--meta-api-key <key>`  
API | API Responses (`openai-responses`)  
URL de base | `https://api.meta.ai/v1`  
Modèle par défaut | `meta/muse-spark-1.1`  
Raisonnement par défaut | `high` (`reasoning.effort`)  
  
## Prise en main

* ### Définir la clé API

IntégrationCopy code
[code]
    openclaw onboard --auth-choice meta-api-key
[/code]

Option directeCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \--auth-choice meta-api-key \--meta-api-key "$MODEL_API_KEY"
[/code]

Variable d’environnement uniquementCopy code
[code]
    export MODEL_API_KEY=<key>
[/code]

* ### Vérifier que les modèles sont disponibles

bashCopy code
[code]
    openclaw models list --provider meta
[/code]

Répertorie l’entrée statique `muse-spark-1.1` du catalogue. Si `MODEL_API_KEY` n’est pas résolue, `openclaw models status --json` signale l’identifiant d’authentification manquant sous `auth.unusableProfiles`.

## Configuration non interactive

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --mode local \  --auth-choice meta-api-key \  --meta-api-key "$MODEL_API_KEY"
[/code]

## Catalogue intégré

Référence du modèle | Nom | Raisonnement | Fenêtre de contexte | Sortie maximale  
---|---|---|---|---  
`meta/muse-spark-1.1` | Muse Spark 1.1 | oui | 1 048 576 | 131 072  
  
Fonctionnalités :

  * Entrée texte et image
  * Appel d’outils et diffusion en continu
  * Effort de raisonnement : `minimal`, `low`, `medium`, `high`, `xhigh` (valeur par défaut : `high`)
  * Relecture chiffrée et sans état du raisonnement (`store: false`, `include: ["reasoning.encrypted_content"]`)


## Configuration manuelle

json5Copy code
[code]
    {  env: { MODEL_API_KEY: "<key>" },  agents: {    defaults: {      model: { primary: "meta/muse-spark-1.1" },      models: {        "meta/muse-spark-1.1": { alias: "Muse Spark 1.1" },      },    },  },}
[/code]

## Test rapide

bashCopy code
[code]
    export MODEL_API_KEY=<key>pnpm test:live -- extensions/meta/meta.live.test.ts
[/code]

Les tests en conditions réelles utilisent `muse-spark-1.1` avec `POST /v1/responses`.

## Voir aussi

[**Fournisseurs de modèles** Choix des fournisseurs, des références de modèles et du comportement de basculement. ](</fr/concepts/model-providers>) [**Modes de réflexion** Niveaux d’effort de raisonnement pour muse-spark-1.1. ](</fr/tools/thinking>) [**Référence de configuration** Valeurs par défaut des agents et configuration des modèles. ](</fr/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue