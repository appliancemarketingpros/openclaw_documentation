---
title: Amazon Bedrock Mantle
source_url: https://docs.openclaw.ai/fr/providers/bedrock-mantle
scraped_at: 2026-05-25
---

OpenClaw inclut un fournisseur **Amazon Bedrock Mantle** intégré qui se connecte au point de terminaison Mantle compatible avec OpenAI. Mantle héberge des modèles open source et tiers (GPT-OSS, Qwen, Kimi, GLM, et similaires) via une surface `/v1/chat/completions` standard adossée à l’infrastructure Bedrock.

Propriété | Valeur  
---|---  
ID du fournisseur | `amazon-bedrock-mantle`  
API | `openai-completions` (compatible avec OpenAI) ou `anthropic-messages` (route Anthropic Messages)  
Authentification | `AWS_BEARER_TOKEN_BEDROCK` explicite ou génération de jeton porteur via la chaîne d’identifiants IAM  
Région par défaut | `us-east-1` (remplacer avec `AWS_REGION` ou `AWS_DEFAULT_REGION`)  
  
## Démarrage

Choisissez votre méthode d’authentification préférée et suivez les étapes de configuration.

### Explicit bearer token

**Idéal pour :** les environnements où vous disposez déjà d’un jeton porteur Mantle.

* ### Set the bearer token on the gateway host

bashCopy code
[code]
    export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

Définissez éventuellement une région (`us-east-1` par défaut) :

bashCopy code
[code]
    export AWS_REGION="us-west-2"
[/code]

* ### Verify models are discovered

bashCopy code
[code]
    openclaw models list
[/code]

Les modèles découverts apparaissent sous le fournisseur `amazon-bedrock-mantle`. Aucune configuration supplémentaire n’est requise, sauf si vous souhaitez remplacer les valeurs par défaut.

### IAM credentials

**Idéal pour :** utiliser des identifiants compatibles avec l’AWS SDK (configuration partagée, SSO, identité web, rôles d’instance ou de tâche).

* ### Configure AWS credentials on the gateway host

Toute source d’authentification compatible avec l’AWS SDK fonctionne :

bashCopy code
[code]
    export AWS_PROFILE="default"export AWS_REGION="us-west-2"
[/code]

* ### Verify models are discovered

bashCopy code
[code]
    openclaw models list
[/code]

OpenClaw génère automatiquement un jeton porteur Mantle à partir de la chaîne d’identifiants.

## Découverte automatique des modèles

Lorsque `AWS_BEARER_TOKEN_BEDROCK` est défini, OpenClaw l’utilise directement. Sinon, OpenClaw tente de générer un jeton porteur Mantle à partir de la chaîne d’identifiants AWS par défaut. Il découvre ensuite les modèles Mantle disponibles en interrogeant le point de terminaison `/v1/models` de la région.

Comportement | Détail  
---|---  
Cache de découverte | Résultats mis en cache 1 heure  
Actualisation du jeton IAM | Toutes les heures  
  
Pour conserver le Plugin Mantle activé tout en supprimant la découverte automatique et la génération de jeton porteur IAM, désactivez le bouton de découverte appartenant au Plugin :

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock-mantle.config.discovery.enabled false
[/code]

### Régions prises en charge

`us-east-1`, `us-east-2`, `us-west-2`, `ap-northeast-1`, `ap-south-1`, `ap-southeast-3`, `eu-central-1`, `eu-west-1`, `eu-west-2`, `eu-south-1`, `eu-north-1`, `sa-east-1`.

## Configuration manuelle

Si vous préférez une configuration explicite plutôt que la découverte automatique :

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        baseUrl: "https://bedrock-mantle.us-east-1.api.aws/v1",        api: "openai-completions",        auth: "api-key",        apiKey: "env:AWS_BEARER_TOKEN_BEDROCK",        models: [          {            id: "gpt-oss-120b",            name: "GPT-OSS 120B",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32000,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

## Configuration avancée

Reasoning support

La prise en charge du raisonnement est déduite des ID de modèles contenant des motifs comme `thinking`, `reasoner` ou `gpt-oss-120b`. OpenClaw définit automatiquement `reasoning: true` pour les modèles correspondants pendant la découverte.

Endpoint unavailability

Si le point de terminaison Mantle est indisponible ou ne renvoie aucun modèle, le fournisseur est ignoré silencieusement. OpenClaw ne renvoie pas d’erreur ; les autres fournisseurs configurés continuent de fonctionner normalement.

Claude Opus 4.7 via the Anthropic Messages route

Mantle expose également une route Anthropic Messages qui transporte les modèles Claude via le même chemin de streaming authentifié par jeton porteur. Claude Opus 4.7 (`amazon-bedrock-mantle/claude-opus-4.7`) peut être appelé via cette route avec un streaming appartenant au fournisseur, de sorte que les jetons porteurs AWS ne sont pas traités comme des clés API Anthropic.

Lorsque vous épinglez un modèle Anthropic Messages sur le fournisseur Mantle, OpenClaw utilise la surface API `anthropic-messages` au lieu de `openai-completions` pour ce modèle. L’authentification provient toujours de `AWS_BEARER_TOKEN_BEDROCK` (ou du jeton porteur IAM émis).

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        models: [          {            id: "claude-opus-4.7",            name: "Claude Opus 4.7",            api: "anthropic-messages",            reasoning: true,            input: ["text", "image"],            contextWindow: 1000000,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Relationship to Amazon Bedrock provider

Bedrock Mantle est un fournisseur distinct du fournisseur [Amazon Bedrock](</fr/providers/bedrock>) standard. Mantle utilise une surface `/v1` compatible avec OpenAI, tandis que le fournisseur Bedrock standard utilise l’API Bedrock native.

Les deux fournisseurs partagent le même identifiant `AWS_BEARER_TOKEN_BEDROCK` lorsqu’il est présent.

## Associé

[**Amazon Bedrock** Fournisseur Bedrock natif pour Anthropic Claude, Titan et d’autres modèles. ](</fr/providers/bedrock>) [**Model selection** Choix des fournisseurs, des références de modèles et du comportement de basculement. ](</fr/concepts/model-providers>) [**OAuth and auth** Détails d’authentification et règles de réutilisation des identifiants. ](</fr/gateway/authentication>) [**Troubleshooting** Problèmes courants et manière de les résoudre. ](</fr/help/troubleshooting>)

Was this useful?YesNo