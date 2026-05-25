---
title: Cerebras
source_url: https://docs.openclaw.ai/fr/providers/cerebras
scraped_at: 2026-05-25
---

[Cerebras](<https://www.cerebras.ai>) fournit une inférence haute vitesse compatible avec OpenAI sur du matériel d’inférence personnalisé. OpenClaw inclut un Plugin fournisseur Cerebras intégré avec un catalogue statique de quatre modèles.

Propriété | Valeur  
---|---  
ID du fournisseur | `cerebras`  
Plugin | intégré, `enabledByDefault: true`  
Variable d’env. d’auth. | `CEREBRAS_API_KEY`  
Option d’intégration | `--auth-choice cerebras-api-key`  
Option CLI directe | `--cerebras-api-key <key>`  
API | compatible OpenAI (`openai-completions`)  
URL de base | `https://api.cerebras.ai/v1`  
Modèle par défaut | `cerebras/zai-glm-4.7`  
  
## Premiers pas

* ### Obtenir une clé API

Créez une clé API dans la [console cloud Cerebras](<https://cloud.cerebras.ai>).

* ### Lancer l’intégration initiale

Intégration initialeCopy code
[code]
    openclaw onboard --auth-choice cerebras-api-key
[/code]

Option directeCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice cerebras-api-key \--cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

Env uniquementCopy code
[code]
    export CEREBRAS_API_KEY=csk-...
[/code]

* ### Vérifier que les modèles sont disponibles

bashCopy code
[code]
    openclaw models list --provider cerebras
[/code]

La liste doit inclure les quatre modèles intégrés. Si `CEREBRAS_API_KEY` n’est pas résolu, `openclaw models status --json` signale l’identifiant manquant sous `auth.unusableProfiles`.

## Configuration non interactive

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cerebras-api-key \  --cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

## Catalogue intégré

OpenClaw fournit un catalogue Cerebras statique qui reflète le point de terminaison public compatible avec OpenAI. Les quatre modèles partagent un contexte de 128k et 8 192 tokens de sortie maximum.

Référence du modèle | Nom | Raisonnement | Notes  
---|---|---|---  
`cerebras/zai-glm-4.7` | [Z.ai](<http://Z.ai>) GLM 4.7 | oui | Modèle par défaut ; modèle de raisonnement en aperçu  
`cerebras/gpt-oss-120b` | GPT OSS 120B | oui | Modèle de raisonnement de production  
`cerebras/qwen-3-235b-a22b-instruct-2507` | Qwen 3 235B Instruct | non | Modèle sans raisonnement en aperçu  
`cerebras/llama3.1-8b` | Llama 3.1 8B | non | Modèle de production axé sur la vitesse  
  
## Configuration manuelle

Le Plugin intégré signifie généralement que vous n’avez besoin que de la clé API. Utilisez une configuration `models.providers.cerebras` explicite lorsque vous voulez remplacer les métadonnées de modèle ou exécuter en `mode: "merge"` avec le catalogue statique :

json5Copy code
[code]
    {  env: { CEREBRAS_API_KEY: "csk-..." },  agents: {    defaults: {      model: { primary: "cerebras/zai-glm-4.7" },    },  },  models: {    mode: "merge",    providers: {      cerebras: {        baseUrl: "https://api.cerebras.ai/v1",        apiKey: "${CEREBRAS_API_KEY}",        api: "openai-completions",        models: [          { id: "zai-glm-4.7", name: "Z.ai GLM 4.7" },          { id: "gpt-oss-120b", name: "GPT OSS 120B" },        ],      },    },  },}
[/code]

## Connexe

[**Fournisseurs de modèles** Choisir des fournisseurs, des références de modèles et le comportement de basculement. ](</fr/concepts/model-providers>) [**Modes de réflexion** Niveaux d’effort de raisonnement pour les deux modèles Cerebras capables de raisonnement. ](</fr/tools/thinking>) [**Référence de configuration** Valeurs par défaut des agents et configuration des modèles. ](</fr/gateway/config-agents#agent-defaults>) [**FAQ sur les modèles** Profils d’authentification, changement de modèles et résolution des erreurs « no profile ». ](</fr/help/faq-models>)

Was this useful?YesNo