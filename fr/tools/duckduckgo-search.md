---
title: Recherche DuckDuckGo
source_url: https://docs.openclaw.ai/fr/tools/duckduckgo-search
scraped_at: 2026-05-25
---

OpenClaw prend en charge DuckDuckGo comme fournisseur `web_search` **sans clé**. Aucune clé API ni aucun compte n’est requis.

## Configuration

Aucune clé API n’est nécessaire : définissez simplement DuckDuckGo comme fournisseur :

* ### Configure

bashCopy code
[code]
    openclaw configure --section web# Select "duckduckgo" as the provider
[/code]

## Configuration

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "duckduckgo",      },    },  },}
[/code]

Paramètres optionnels au niveau du Plugin pour la région et SafeSearch :

json5Copy code
[code]
    {  plugins: {    entries: {      duckduckgo: {        config: {          webSearch: {            region: "us-en", // DuckDuckGo region code            safeSearch: "moderate", // "strict", "moderate", or "off"          },        },      },    },  },}
[/code]

## Paramètres de l’outil

Requête de recherche.

Résultats à retourner (1-10).

Code de région DuckDuckGo (par exemple `us-en`, `uk-en`, `de-de`).

Niveau SafeSearch.

La région et SafeSearch peuvent aussi être définis dans la configuration du Plugin (voir ci-dessus) ; les paramètres de l’outil remplacent les valeurs de configuration pour chaque requête.

## Notes

  * **Aucune clé API** : fonctionne immédiatement, sans configuration
  * **Expérimental** : collecte les résultats depuis les pages de recherche HTML sans JavaScript de DuckDuckGo, et non depuis une API ou un SDK officiel
  * **Risque de défi anti-bot** : DuckDuckGo peut servir des CAPTCHA ou bloquer les requêtes en cas d’utilisation intensive ou automatisée
  * **Analyse HTML** : les résultats dépendent de la structure de la page, qui peut changer sans préavis
  * **Ordre de détection automatique** : DuckDuckGo est le premier recours sans clé (ordre 100) dans la détection automatique. Les fournisseurs avec API disposant de clés configurées s’exécutent d’abord, puis Ollama Web Search (ordre 110), puis SearXNG (ordre 200)
  * **SafeSearch utilise moderate par défaut** lorsqu’il n’est pas configuré


## Articles connexes

  * [Vue d’ensemble de Web Search](</fr/tools/web>) \-- tous les fournisseurs et la détection automatique
  * [Brave Search](</fr/tools/brave-search>) \-- résultats structurés avec offre gratuite
  * [Exa Search](</fr/tools/exa-search>) \-- recherche neuronale avec extraction de contenu


Was this useful?YesNo