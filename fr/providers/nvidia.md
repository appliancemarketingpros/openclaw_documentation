---
title: NVIDIA
source_url: https://docs.openclaw.ai/fr/providers/nvidia
scraped_at: 2026-05-25
---

NVIDIA fournit une API compatible avec OpenAI à `https://integrate.api.nvidia.com/v1` pour les modèles ouverts, gratuitement. Authentifiez-vous avec une clé d’API depuis [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

## Bien démarrer

* ### Get your API key

Créez une clé d’API sur [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

* ### Export the key and run onboarding

bashCopy code
[code]
    export NVIDIA_API_KEY="nvapi-..."openclaw onboard --auth-choice nvidia-api-key
[/code]

* ### Set an NVIDIA model

bashCopy code
[code]
    openclaw models set nvidia/nvidia/nemotron-3-super-120b-a12b
[/code]

Pour une configuration non interactive, vous pouvez aussi passer la clé directement :

bashCopy code
[code]
    openclaw onboard --auth-choice nvidia-api-key --nvidia-api-key "nvapi-..."
[/code]

## Exemple de configuration

json5Copy code
[code]
    {  env: { NVIDIA_API_KEY: "nvapi-..." },  models: {    providers: {      nvidia: {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",      },    },  },  agents: {    defaults: {      model: { primary: "nvidia/nvidia/nemotron-3-super-120b-a12b" },    },  },}
[/code]

## Catalogue intégré

Référence de modèle | Nom | Contexte | Sortie maximale  
---|---|---|---  
`nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Nemotron 3 Super 120B | 262,144 | 8,192  
`nvidia/moonshotai/kimi-k2.5` | Kimi K2.5 | 262,144 | 8,192  
`nvidia/minimaxai/minimax-m2.5` | Minimax M2.5 | 196,608 | 8,192  
`nvidia/z-ai/glm5` | GLM 5 | 202,752 | 8,192  
  
## Configuration avancée

Auto-enable behavior

Le fournisseur s’active automatiquement lorsque la variable d’environnement `NVIDIA_API_KEY` est définie. Aucune configuration explicite du fournisseur n’est requise au-delà de la clé.

Catalog and pricing

Le catalogue fourni est statique. Les coûts sont définis par défaut sur `0` dans la source, car NVIDIA propose actuellement un accès API gratuit pour les modèles listés.

OpenAI-compatible endpoint

NVIDIA utilise le point de terminaison standard de complétions `/v1`. Tout outil compatible avec OpenAI devrait fonctionner directement avec l’URL de base NVIDIA.

Slow custom provider responses

Certains modèles personnalisés hébergés par NVIDIA peuvent prendre plus longtemps que le délai de surveillance d’inactivité par défaut du modèle avant d’émettre le premier fragment de réponse. Pour les entrées de fournisseur NVIDIA personnalisées, augmentez le délai d’expiration du fournisseur au lieu d’augmenter le délai d’expiration de tout l’environnement d’exécution de l’agent :

json5Copy code
[code]
    {  models: {    providers: {      "custom-integrate-api-nvidia-com": {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",        apiKey: "NVIDIA_API_KEY",        timeoutSeconds: 300,      },    },  },  agents: {    defaults: {      models: {        "custom-integrate-api-nvidia-com/meta/llama-3.1-70b-instruct": {          params: { thinking: "off" },        },      },    },  },}
[/code]

## Articles connexes

[**Model selection** Choisir les fournisseurs, les références de modèles et le comportement de basculement. ](</fr/concepts/model-providers>) [**Configuration reference** Référence complète de configuration pour les agents, les modèles et les fournisseurs. ](</fr/gateway/configuration-reference>)

Was this useful?YesNo