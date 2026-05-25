---
title: Tavily
source_url: https://docs.openclaw.ai/fr/tools/tavily
scraped_at: 2026-05-25
---

[Tavily](<https://tavily.com>) est une API de recherche conçue pour les applications d’IA. OpenClaw l’expose de deux manières :

  * comme fournisseur `web_search` pour l’outil de recherche générique
  * comme outils de plugin explicites : `tavily_search` et `tavily_extract`


Tavily renvoie des résultats structurés optimisés pour la consommation par les LLM, avec une profondeur de recherche configurable, un filtrage par sujet, des filtres de domaine, des résumés de réponse générés par l’IA et l’extraction de contenu depuis des URL (y compris les pages rendues par JavaScript).

Propriété | Valeur  
---|---  
ID du Plugin | `tavily`  
Authentification | `TAVILY_API_KEY` or config `apiKey`  
URL de base | `https://api.tavily.com` (par défaut)  
Outils groupés | `tavily_search`, `tavily_extract`  
  
## Premiers pas

* ### Obtenir une clé API

Créez un compte Tavily sur [tavily.com](<https://tavily.com>), puis générez une clé API dans le tableau de bord.

* ### Configurer le plugin et le fournisseur

json5Copy code
[code]
    {  plugins: {    entries: {      tavily: {        enabled: true,        config: {          webSearch: {            apiKey: "tvly-...", // optional if TAVILY_API_KEY is set            baseUrl: "https://api.tavily.com",          },        },      },    },  },  tools: {    web: {      search: {        provider: "tavily",      },    },  },}
[/code]

* ### Vérifier que la recherche s’exécute

Déclenchez un `web_search` depuis n’importe quel agent, ou appelez directement `tavily_search`.

## Référence des outils

### `tavily_search`

Utilisez ceci lorsque vous voulez des contrôles de recherche propres à Tavily au lieu de `web_search` générique.

Paramètre | Type | Contraintes / valeur par défaut | Description  
---|---|---|---  
`query` | string | requis | Chaîne de requête de recherche. Gardez-la sous 400 caractères.  
`search_depth` | enum | `basic` (par défaut), `advanced` | `advanced` est plus lent mais plus pertinent.  
`topic` | enum | `general` (par défaut), `news`, `finance` | Filtrer par famille de sujets.  
`max_results` | integer | 1-20 | Nombre de résultats.  
`include_answer` | boolean | par défaut `false` | Inclure un résumé de réponse généré par l’IA de Tavily.  
`time_range` | enum | `day`, `week`, `month`, `year` | Filtrer les résultats par récence.  
`include_domains` | string array | (aucun) | Inclure uniquement les résultats de ces domaines.  
`exclude_domains` | string array | (aucun) | Exclure les résultats de ces domaines.  
  
Compromis de profondeur de recherche :

Profondeur | Vitesse | Pertinence | Idéal pour  
---|---|---|---  
`basic` | Plus rapide | Élevée | Requêtes polyvalentes (par défaut).  
`advanced` | Plus lent | Maximale | Recherche précise et vérification des faits.  
  
### `tavily_extract`

Utilisez ceci pour extraire du contenu propre depuis une ou plusieurs URL. Gère les pages rendues par JavaScript et prend en charge le découpage ciblé par requête pour une extraction ciblée.

Paramètre | Type | Contraintes / valeur par défaut | Description  
---|---|---|---  
`urls` | string array | requis, 1-20 | URL depuis lesquelles extraire le contenu.  
`query` | string | (facultatif) | Reclasser les fragments extraits selon leur pertinence pour cette requête.  
`extract_depth` | enum | `basic` (par défaut), `advanced` | Utilisez `advanced` pour les pages riches en JS, les SPA ou les tableaux dynamiques.  
`chunks_per_source` | integer | 1-5 ; **nécessite`query`** | Fragments renvoyés par URL. Génère une erreur si défini sans `query`.  
`include_images` | boolean | par défaut `false` | Inclure les URL d’images dans les résultats.  
  
Compromis de profondeur d’extraction :

Profondeur | Quand l’utiliser  
---|---  
`basic` | Pages simples. Essayez ceci en premier.  
`advanced` | SPA rendues par JS, contenu dynamique, tableaux.  
  
## Choisir le bon outil

Besoin | Outil  
---|---  
Recherche web rapide, sans options particulières | `web_search`  
Recherche avec profondeur, sujet, réponses IA | `tavily_search`  
Extraire du contenu depuis des URL spécifiques | `tavily_extract`  
  
## Configuration avancée

Ordre de résolution de la clé API

Le client Tavily recherche sa clé API dans cet ordre :

  1. `plugins.entries.tavily.config.webSearch.apiKey` (résolu via SecretRefs).
  2. `TAVILY_API_KEY` depuis l’environnement du gateway.


`tavily_extract` génère une erreur de configuration si aucun des deux n’est présent.

URL de base personnalisée

Remplacez `plugins.entries.tavily.config.webSearch.baseUrl` si vous faites passer Tavily par un proxy. La valeur par défaut est `https://api.tavily.com`.

`chunks_per_source` nécessite `query`

`tavily_extract` rejette les appels qui passent `chunks_per_source` sans `query`. Tavily classe les fragments selon leur pertinence pour la requête, donc le paramètre n’a aucun sens sans requête.

## Connexe

[**Vue d’ensemble de Web Search** Tous les fournisseurs et règles de détection automatique. ](</fr/tools/web>) [**Firecrawl** Recherche avec scraping et extraction de contenu. ](</fr/tools/firecrawl>) [**Exa Search** Recherche neuronale avec extraction de contenu. ](</fr/tools/exa-search>) [**Configuration** Schéma de configuration complet pour les entrées de plugin et le routage des outils. ](</fr/gateway/configuration>)

Was this useful?YesNo