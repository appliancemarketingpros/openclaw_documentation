---
title: LiteLLM
source_url: https://docs.openclaw.ai/fr/providers/litellm
scraped_at: 2026-05-25
---

[LiteLLM](<https://litellm.ai>) est un Gateway LLM open source qui fournit une API unifiée pour plus de 100 fournisseurs de modèles. Faites passer OpenClaw par LiteLLM pour bénéficier d’un suivi centralisé des coûts, de la journalisation et de la flexibilité nécessaire pour changer de backend sans modifier votre configuration OpenClaw.

## Démarrage rapide

### Onboarding (recommended)

**Idéal pour :** le chemin le plus rapide vers une configuration LiteLLM fonctionnelle.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice litellm-api-key
[/code]

Pour une configuration non interactive avec un proxy distant, transmettez explicitement l’URL du proxy :

bashCopy code
[code]
    openclaw onboard --non-interactive --auth-choice litellm-api-key --litellm-api-key "$LITELLM_API_KEY" --custom-base-url "https://litellm.example/v1"
[/code]

### Manual setup

**Idéal pour :** un contrôle complet de l’installation et de la configuration.

* ### Start LiteLLM Proxy

bashCopy code
[code]
    pip install 'litellm[proxy]'litellm --model claude-opus-4-6
[/code]

* ### Point OpenClaw to LiteLLM

bashCopy code
[code]
    export LITELLM_API_KEY="your-litellm-key" openclaw
[/code]

C’est tout. OpenClaw passe désormais par LiteLLM.

## Configuration

### Variables d’environnement

bashCopy code
[code]
    export LITELLM_API_KEY="sk-litellm-key"
[/code]

### Fichier de configuration

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",        api: "openai-completions",        models: [          {            id: "claude-opus-4-6",            name: "Claude Opus 4.6",            reasoning: true,            input: ["text", "image"],            contextWindow: 200000,            maxTokens: 64000,          },          {            id: "gpt-4o",            name: "GPT-4o",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "litellm/claude-opus-4-6" },    },  },}
[/code]

## Configuration avancée

### Génération d’images

LiteLLM peut également prendre en charge l’outil `image_generate` via les routes `/images/generations` et `/images/edits` compatibles avec OpenAI. Configurez un modèle d’image LiteLLM sous `agents.defaults.imageGenerationModel` :

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",      },    },  },  agents: {    defaults: {      imageGenerationModel: {        primary: "litellm/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

Les URL LiteLLM en loopback comme `http://localhost:4000` fonctionnent sans dérogation globale pour le réseau privé. Pour un proxy hébergé sur le LAN, définissez `models.providers.litellm.request.allowPrivateNetwork: true`, car la clé API sera envoyée à l’hôte proxy configuré.

Virtual keys

Créez une clé dédiée pour OpenClaw avec des limites de dépenses :

bashCopy code
[code]
    curl -X POST "http://localhost:4000/key/generate" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \  -H "Content-Type: application/json" \  -d '{    "key_alias": "openclaw",    "max_budget": 50.00,    "budget_duration": "monthly"  }'
[/code]

Utilisez la clé générée comme `LITELLM_API_KEY`.

Model routing

LiteLLM peut acheminer les requêtes de modèles vers différents backends. Configurez-le dans votre `config.yaml` LiteLLM :

yamlCopy code
[code]
    model_list:  - model_name: claude-opus-4-6    litellm_params:      model: claude-opus-4-6      api_key: os.environ/ANTHROPIC_API_KEY   - model_name: gpt-4o    litellm_params:      model: gpt-4o      api_key: os.environ/OPENAI_API_KEY
[/code]

OpenClaw continue de demander `claude-opus-4-6` — LiteLLM gère le routage.

Viewing usage

Consultez le tableau de bord ou l’API de LiteLLM :

bashCopy code
[code]
    # Key infocurl "http://localhost:4000/key/info" \  -H "Authorization: Bearer sk-litellm-key" # Spend logscurl "http://localhost:4000/spend/logs" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY"
[/code]

Proxy behavior notes

  * LiteLLM s’exécute par défaut sur `http://localhost:4000`
  * OpenClaw se connecte via l’endpoint `/v1` compatible OpenAI de style proxy de LiteLLM
  * La mise en forme des requêtes propre à OpenAI ne s’applique pas via LiteLLM : pas de `service_tier`, pas de `store` Responses, pas d’indications de cache de prompt, et pas de mise en forme de charge utile compatible avec le raisonnement OpenAI
  * Les en-têtes d’attribution OpenClaw masqués (`originator`, `version`, `User-Agent`) ne sont pas injectés sur les URL de base LiteLLM personnalisées


## Connexe

[**LiteLLM Docs** Documentation officielle de LiteLLM et référence de l’API. ](<https://docs.litellm.ai>) [**Model selection** Vue d’ensemble de tous les fournisseurs, des références de modèles et du comportement de basculement. ](</fr/concepts/model-providers>) [**Configuration** Référence complète de la configuration. ](</fr/gateway/configuration>) [**Model selection** Comment choisir et configurer les modèles. ](</fr/concepts/models>)

Was this useful?YesNo