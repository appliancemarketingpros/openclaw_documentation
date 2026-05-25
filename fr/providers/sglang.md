---
title: SGLang
source_url: https://docs.openclaw.ai/fr/providers/sglang
scraped_at: 2026-05-25
---

SGLang sert des modèles à pondérations ouvertes via une API HTTP compatible avec OpenAI. OpenClaw se connecte à SGLang avec la famille de fournisseurs `openai-completions`, avec découverte automatique des modèles disponibles.

Propriété | Valeur  
---|---  
ID du fournisseur | `sglang`  
Plugin | intégré, `enabledByDefault: true`  
Variable d'env d'authentification | `SGLANG_API_KEY` (toute valeur non vide si le serveur n'a pas d'authentification)  
Indicateur d'onboarding | `--auth-choice sglang`  
API | compatible avec OpenAI (`openai-completions`)  
URL de base par défaut | `http://127.0.0.1:30000/v1`  
Espace réservé du modèle par défaut | `sglang/Qwen/Qwen3-8B`  
Utilisation du streaming | Oui (`supportsStreamingUsage: true`)  
Tarification | Marquée comme externe gratuite (`modelPricing.external: false`)  
  
OpenClaw **découvre aussi automatiquement** les modèles disponibles depuis SGLang lorsque vous l'activez avec `SGLANG_API_KEY`. Utilisez `sglang/*` dans `agents.defaults.models` pour conserver une découverte dynamique lorsque vous configurez aussi une URL de base SGLang personnalisée. Consultez Découverte de modèles (fournisseur implicite) ci-dessous.

## Premiers pas

* ### Démarrer SGLang

Lancez SGLang avec un serveur compatible avec OpenAI. Votre URL de base doit exposer des points de terminaison `/v1` (par exemple `/v1/models`, `/v1/chat/completions`). SGLang s'exécute généralement sur :

  * `http://127.0.0.1:30000/v1`


* ### Définir une clé API

Toute valeur fonctionne si aucune authentification n'est configurée sur votre serveur :

bashCopy code
[code]
    export SGLANG_API_KEY="sglang-local"
[/code]

* ### Exécuter l'onboarding ou définir directement un modèle

bashCopy code
[code]
    openclaw onboard
[/code]

Ou configurez le modèle manuellement :

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "sglang/your-model-id" },    },  },}
[/code]

## Découverte de modèles (fournisseur implicite)

Lorsque `SGLANG_API_KEY` est défini (ou qu'un profil d'authentification existe) et que vous **ne** définissez pas `models.providers.sglang`, OpenClaw interroge :

  * `GET http://127.0.0.1:30000/v1/models`


et convertit les identifiants renvoyés en entrées de modèle.

## Configuration explicite (modèles manuels)

Utilisez une configuration explicite lorsque :

  * SGLang s'exécute sur un hôte ou un port différent.
  * Vous voulez épingler les valeurs `contextWindow`/`maxTokens`.
  * Votre serveur exige une vraie clé API (ou vous voulez contrôler les en-têtes).

json5Copy code
[code]
    {  models: {    providers: {      sglang: {        baseUrl: "http://127.0.0.1:30000/v1",        apiKey: "${SGLANG_API_KEY}",        api: "openai-completions",        models: [          {            id: "your-model-id",            name: "Local SGLang Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## Configuration avancée

Comportement de type proxy

SGLang est traité comme un backend `/v1` compatible avec OpenAI de type proxy, et non comme un point de terminaison OpenAI natif.

Comportement | SGLang  
---|---  
Mise en forme des requêtes uniquement pour OpenAI | Non appliquée  
`service_tier`, `store` de Responses, indications de cache de prompt | Non envoyés  
Mise en forme de payload compatible avec le raisonnement | Non appliquée  
En-têtes d'attribution masqués (`originator`, `version`, `User-Agent`) | Non injectés sur les URL de base SGLang personnalisées  
Dépannage

**Serveur inaccessible**

Vérifiez que le serveur est en cours d'exécution et répond :

bashCopy code
[code]
    curl http://127.0.0.1:30000/v1/models
[/code]

**Erreurs d'authentification**

Si les requêtes échouent avec des erreurs d'authentification, définissez une vraie `SGLANG_API_KEY` qui correspond à la configuration de votre serveur, ou configurez explicitement le fournisseur sous `models.providers.sglang`.

## Connexe

[**Sélection du modèle** Choisir les fournisseurs, les références de modèles et le comportement de basculement. ](</fr/concepts/model-providers>) [**Référence de configuration** Schéma de configuration complet, y compris les entrées de fournisseurs. ](</fr/gateway/configuration-reference>)

Was this useful?YesNo