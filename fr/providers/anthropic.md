---
title: Anthropic
source_url: https://docs.openclaw.ai/fr/providers/anthropic
scraped_at: 2026-05-25
---

Anthropic développe la famille de modèles **Claude**. OpenClaw prend en charge deux modes d’authentification :

  * **Clé API** — accès direct à l’API Anthropic avec facturation à l’usage (modèles `anthropic/*`)
  * **Claude CLI** — réutilise une connexion Claude CLI existante sur le même hôte


## Bien démarrer

### Clé API

**Idéal pour :** l’accès API standard et la facturation à l’usage.

* ### Obtenir votre clé API

Créez une clé API dans l’[Anthropic Console](<https://console.anthropic.com/>).

* ### Exécuter l’intégration

bashCopy code
[code]
    openclaw onboard# choose: Anthropic API key
[/code]

Ou transmettez la clé directement :

bashCopy code
[code]
    openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
[/code]

* ### Vérifier que le modèle est disponible

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Exemple de configuration

json5Copy code
[code]
    {  env: { ANTHROPIC_API_KEY: "sk-ant-..." },  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

### Claude CLI

**Idéal pour :** réutiliser une connexion Claude CLI existante sans clé API séparée.

* ### Vérifier que Claude CLI est installé et connecté

Vérifiez avec :

bashCopy code
[code]
    claude --version
[/code]

* ### Exécuter l’intégration

bashCopy code
[code]
    openclaw onboard# choose: Claude CLI
[/code]

OpenClaw détecte et réutilise les identifiants Claude CLI existants.

* ### Vérifier que le modèle est disponible

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Exemple de configuration

Préférez la référence de modèle Anthropic canonique avec une substitution d’exécution CLI :

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-7" },      models: {        "anthropic/claude-opus-4-7": {          agentRuntime: { id: "claude-cli" },        },      },    },  },}
[/code]

Les anciennes références de modèle `claude-cli/claude-opus-4-7` fonctionnent encore pour la compatibilité, mais les nouvelles configurations doivent conserver la sélection fournisseur/modèle sous la forme `anthropic/*` et placer le backend d’exécution dans la politique d’exécution fournisseur/modèle.

## Valeurs par défaut de raisonnement (Claude 4.6)

Les modèles Claude 4.6 utilisent par défaut le raisonnement `adaptive` dans OpenClaw lorsqu’aucun niveau de raisonnement explicite n’est défini.

Remplacez-le par message avec `/think:<level>` ou dans les paramètres du modèle :

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { thinking: "adaptive" },        },      },    },  },}
[/code]

## Mise en cache des prompts

OpenClaw prend en charge la fonctionnalité de mise en cache des prompts d’Anthropic pour l’authentification par clé API.

Valeur | Durée du cache | Description  
---|---|---  
`"short"` (défaut) | 5 minutes | Appliqué automatiquement pour l’authentification par clé API  
`"long"` | 1 heure | Cache étendu  
`"none"` | Aucune mise en cache | Désactive la mise en cache des prompts  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },  },}
[/code]

Substitutions de cache par agent

Utilisez les paramètres au niveau du modèle comme base, puis remplacez des agents spécifiques via `agents.list[].params` :

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-6" },      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },    list: [      { id: "research", default: true },      { id: "alerts", params: { cacheRetention: "none" } },    ],  },}
[/code]

Ordre de fusion de la configuration :

  1. `agents.defaults.models["provider/model"].params`
  2. `agents.list[].params` (`id` correspondant, remplace par clé)


Cela permet à un agent de conserver un cache de longue durée tandis qu’un autre agent utilisant le même modèle désactive la mise en cache pour un trafic en rafales ou à faible réutilisation.

Notes sur Claude avec Bedrock

  * Les modèles Anthropic Claude sur Bedrock (`amazon-bedrock/*anthropic.claude*`) acceptent le transfert de `cacheRetention` lorsqu’il est configuré.
  * Les modèles Bedrock non Anthropic sont forcés à `cacheRetention: "none"` à l’exécution.
  * Les valeurs par défaut intelligentes pour clé API renseignent aussi `cacheRetention: "short"` pour les références Claude sur Bedrock lorsqu’aucune valeur explicite n’est définie.


## Configuration avancée

Mode rapide

Le bouton partagé `/fast` d’OpenClaw prend en charge le trafic Anthropic direct (clé API et OAuth vers `api.anthropic.com`).

Commande | Correspond à  
---|---  
`/fast on` | `service_tier: "auto"`  
`/fast off` | `service_tier: "standard_only"`  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-sonnet-4-6": {          params: { fastMode: true },        },      },    },  },}
[/code]

Compréhension des médias (image et PDF)

Le Plugin Anthropic intégré enregistre la compréhension des images et des PDF. OpenClaw résout automatiquement les capacités multimédias à partir de l’authentification Anthropic configurée ; aucune configuration supplémentaire n’est nécessaire.

Propriété | Valeur  
---|---  
Modèle par défaut | `claude-opus-4-7`  
Entrée prise en charge | Images, documents PDF  
  
Lorsqu’une image ou un PDF est joint à une conversation, OpenClaw l’achemine automatiquement via le fournisseur de compréhension multimédia Anthropic.

Fenêtre de contexte 1M (bêta)

La fenêtre de contexte 1M d’Anthropic est soumise à un accès bêta. Activez-la par modèle :

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { context1m: true },        },      },    },  },}
[/code]

OpenClaw mappe cela à `anthropic-beta: context-1m-2025-08-07` sur les requêtes.

`params.context1m: true` s’applique aussi au backend Claude CLI (`claude-cli/*`) pour les modèles Opus et Sonnet éligibles, en étendant la fenêtre de contexte d’exécution de ces sessions CLI afin de correspondre au comportement de l’API directe.

Contexte 1M de Claude Opus 4.7

`anthropic/claude-opus-4.7` et sa variante `claude-cli` disposent par défaut d’une fenêtre de contexte 1M — aucun `params.context1m: true` n’est nécessaire.

## Dépannage

Erreurs 401 / jeton soudainement invalide

L’authentification par jeton Anthropic expire et peut être révoquée. Pour les nouvelles configurations, utilisez plutôt une clé API Anthropic.

Aucune clé API trouvée pour le fournisseur "anthropic"

L’authentification Anthropic est **par agent** : les nouveaux agents n’héritent pas des clés de l’agent principal. Relancez l’intégration pour cet agent (ou configurez une clé API sur l’hôte Gateway), puis vérifiez avec `openclaw models status`.

Aucun identifiant trouvé pour le profil "anthropic:default"

Exécutez `openclaw models status` pour voir quel profil d’authentification est actif. Relancez l’intégration, ou configurez une clé API pour ce chemin de profil.

Aucun profil d’authentification disponible (tous en cooldown)

Consultez `openclaw models status --json` pour `auth.unusableProfiles`. Les cooldowns de limite de débit Anthropic peuvent être limités à un modèle ; un modèle Anthropic voisin peut donc encore être utilisable. Ajoutez un autre profil Anthropic ou attendez la fin du cooldown.

## Liens associés

[**Sélection de modèle** Choisir des fournisseurs, des références de modèle et un comportement de basculement. ](</fr/concepts/model-providers>) [**Backends CLI** Détails de configuration et d’exécution du backend Claude CLI. ](</fr/gateway/cli-backends>) [**Mise en cache des prompts** Fonctionnement de la mise en cache des prompts entre fournisseurs. ](</fr/reference/prompt-caching>) [**OAuth et authentification** Détails d’authentification et règles de réutilisation des identifiants. ](</fr/gateway/authentication>)

Was this useful?YesNo