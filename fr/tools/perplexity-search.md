---
title: Recherche Perplexity
source_url: https://docs.openclaw.ai/fr/tools/perplexity-search
scraped_at: 2026-05-25
---

OpenClaw prend en charge Perplexity Search API comme fournisseur `web_search`. Elle renvoie des résultats structurés avec les champs `title`, `url` et `snippet`.

Pour des raisons de compatibilité, OpenClaw prend également en charge les configurations héritées Perplexity Sonar/OpenRouter. Si vous utilisez `OPENROUTER_API_KEY`, une clé `sk-or-...` dans `plugins.entries.perplexity.config.webSearch.apiKey`, ou si vous définissez `plugins.entries.perplexity.config.webSearch.baseUrl` / `model`, le fournisseur bascule vers le chemin des complétions de chat et renvoie des réponses synthétisées par l'IA avec citations au lieu de résultats structurés de la Search API.

## Obtenir une clé d'API Perplexity

  1. Créez un compte Perplexity sur [perplexity.ai/settings/api](<https://www.perplexity.ai/settings/api>)
  2. Générez une clé d'API dans le tableau de bord
  3. Stockez la clé dans la configuration ou définissez `PERPLEXITY_API_KEY` dans l'environnement du Gateway.


## Compatibilité OpenRouter

Si vous utilisiez déjà OpenRouter pour Perplexity Sonar, conservez `provider: "perplexity"` et définissez `OPENROUTER_API_KEY` dans l'environnement du Gateway, ou stockez une clé `sk-or-...` dans `plugins.entries.perplexity.config.webSearch.apiKey`.

Contrôles de compatibilité facultatifs :

  * `plugins.entries.perplexity.config.webSearch.baseUrl`
  * `plugins.entries.perplexity.config.webSearch.model`


## Exemples de configuration

### API Perplexity Search native

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "pplx-...",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

### Compatibilité OpenRouter / Sonar

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "<openrouter-api-key>",            baseUrl: "https://openrouter.ai/api/v1",            model: "perplexity/sonar-pro",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

## Où définir la clé

**Via la configuration :** exécutez `openclaw configure --section web`. La clé est stockée dans `~/.openclaw/openclaw.json` sous `plugins.entries.perplexity.config.webSearch.apiKey`. Ce champ accepte également les objets SecretRef.

**Via l'environnement :** définissez `PERPLEXITY_API_KEY` ou `OPENROUTER_API_KEY` dans l'environnement du processus Gateway. Pour une installation du gateway, placez-la dans `~/.openclaw/.env` (ou dans l'environnement de votre service). Consultez [Variables d'environnement](</fr/help/faq#env-vars-and-env-loading>).

Si `provider: "perplexity"` est configuré et que la SecretRef de la clé Perplexity n'est pas résolue sans solution de repli par variable d'environnement, le démarrage/rechargement échoue immédiatement.

## Paramètres de l'outil

Ces paramètres s'appliquent au chemin de l'API Perplexity Search native.

Requête de recherche.

Nombre de résultats à renvoyer (1-10).

Code pays ISO à 2 lettres (par exemple `US`, `DE`).

Code de langue ISO 639-1 (par exemple `en`, `de`, `fr`).

Filtre temporel - `day` correspond à 24 heures.

Uniquement les résultats publiés après cette date (`YYYY-MM-DD`).

Uniquement les résultats publiés avant cette date (`YYYY-MM-DD`).

Tableau de domaines en liste d'autorisation/liste de blocage (20 max).

Budget total de contenu (max 1000000).

Limite de tokens par page.

Pour le chemin de compatibilité hérité Sonar/OpenRouter :

  * `query`, `count` et `freshness` sont acceptés
  * `count` n'y sert qu'à la compatibilité ; la réponse reste une seule réponse synthétisée avec citations plutôt qu'une liste de N résultats
  * Les filtres réservés à la Search API, comme `country`, `language`, `date_after`, `date_before`, `domain_filter`, `max_tokens` et `max_tokens_per_page` renvoient des erreurs explicites


**Exemples :**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (allowlist)await web_search({  query: "climate research",  domain_filter: ["nature.com", "science.org", ".edu"],}); // Domain filtering (denylist - prefix with -)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],}); // More content extractionawait web_search({  query: "detailed AI research",  max_tokens: 50000,  max_tokens_per_page: 4096,});
[/code]

### Règles du filtre de domaine

  * Maximum 20 domaines par filtre
  * Impossible de mélanger liste d'autorisation et liste de blocage dans la même requête
  * Utilisez le préfixe `-` pour les entrées de liste de blocage (par exemple `["-reddit.com"]`)


## Notes

  * Perplexity Search API renvoie des résultats de recherche web structurés (`title`, `url`, `snippet`)
  * OpenRouter ou `plugins.entries.perplexity.config.webSearch.baseUrl` / `model` explicite fait rebascule Perplexity vers les complétions de chat Sonar pour la compatibilité
  * La compatibilité Sonar/OpenRouter renvoie une seule réponse synthétisée avec citations, et non des lignes de résultats structurés
  * Les résultats sont mis en cache pendant 15 minutes par défaut (configurable via `cacheTtlMinutes`)


## Connexe

[**Vue d'ensemble de la recherche web** Tous les fournisseurs et règles de détection automatique. ](</fr/tools/web>) [**Recherche Brave** Résultats structurés avec filtres de pays et de langue. ](</fr/tools/brave-search>) [**Recherche Exa** Recherche neuronale avec extraction de contenu. ](</fr/tools/exa-search>) [**Documentation de Perplexity Search API** Guide de démarrage rapide et référence officiels de Perplexity Search API. ](<https://docs.perplexity.ai/docs/search/quickstart>)

Was this useful?YesNo