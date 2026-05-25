---
title: Recherche Exa
source_url: https://docs.openclaw.ai/fr/tools/exa-search
scraped_at: 2026-05-25
---

OpenClaw prend en charge [Exa AI](<https://exa.ai/>) comme fournisseur `web_search`. Exa propose des modes de recherche neuronale, par mots-clés et hybride avec une extraction de contenu intégrée (extraits, texte, résumés).

## Obtenir une clé d’API

* ### Créer un compte

Inscrivez-vous sur [exa.ai](<https://exa.ai/>) et générez une clé d’API depuis votre tableau de bord.

* ### Stocker la clé

Définissez `EXA_API_KEY` dans l’environnement Gateway, ou configurez-la via :

bashCopy code
[code]
    openclaw configure --section web
[/code]

## Configuration

json5Copy code
[code]
    {  plugins: {    entries: {      exa: {        config: {          webSearch: {            apiKey: "exa-...", // optional if EXA_API_KEY is set            baseUrl: "https://api.exa.ai", // optional; OpenClaw appends /search          },        },      },    },  },  tools: {    web: {      search: {        provider: "exa",      },    },  },}
[/code]

**Autre option d’environnement :** définissez `EXA_API_KEY` dans l’environnement Gateway. Pour une installation Gateway, placez-la dans `~/.openclaw/.env`.

## Remplacement de l’URL de base

Définissez `plugins.entries.exa.config.webSearch.baseUrl` lorsque les requêtes de recherche Exa doivent passer par un proxy compatible ou un autre point de terminaison Exa. OpenClaw normalise les hôtes nus en ajoutant `https://` au début et ajoute `/search`, sauf si le chemin se termine déjà ainsi. Le point de terminaison résolu est inclus dans la clé du cache de recherche, afin que les résultats provenant de différents points de terminaison Exa ne soient pas partagés.

## Paramètres de l’outil

Requête de recherche.

Résultats à renvoyer (1–100).

Mode de recherche.

Filtre temporel.

Résultats après cette date (`YYYY-MM-DD`).

Résultats avant cette date (`YYYY-MM-DD`).

Options d’extraction de contenu (voir ci-dessous).

### Extraction de contenu

Exa peut renvoyer du contenu extrait avec les résultats de recherche. Passez un objet `contents` pour l’activer :

javascriptCopy code
[code]
    await web_search({  query: "transformer architecture explained",  type: "neural",  contents: {    text: true, // full page text    highlights: { numSentences: 3 }, // key sentences    summary: true, // AI summary  },});
[/code]

Option de contenu | Type | Description  
---|---|---  
`text` | `boolean | { maxCharacters }` | Extraire le texte complet de la page  
`highlights` | `boolean | { maxCharacters, query, numSentences, highlightsPerUrl }` | Extraire les phrases clés  
`summary` | `boolean | { query }` | Résumé généré par l’IA  
  
### Modes de recherche

Mode | Description  
---|---  
`auto` | Exa choisit le meilleur mode (par défaut)  
`neural` | Recherche sémantique/fondée sur le sens  
`fast` | Recherche rapide par mots-clés  
`deep` | Recherche approfondie complète  
`deep-reasoning` | Recherche approfondie avec raisonnement  
`instant` | Résultats les plus rapides  
  
## Remarques

  * Si aucune option `contents` n’est fournie, Exa utilise par défaut `{ highlights: true }`, afin que les résultats incluent des extraits de phrases clés
  * Les résultats conservent les champs `highlightScores` et `summary` de la réponse de l’API Exa lorsqu’ils sont disponibles
  * Les descriptions des résultats sont résolues à partir des extraits d’abord, puis du résumé, puis du texte complet — selon ce qui est disponible
  * `freshness` et `date_after`/`date_before` ne peuvent pas être combinés — utilisez un seul mode de filtre temporel
  * Jusqu’à 100 résultats peuvent être renvoyés par requête (sous réserve des limites de type de recherche Exa)
  * Les résultats sont mis en cache pendant 15 minutes par défaut (configurable via `cacheTtlMinutes`)
  * Exa est une intégration d’API officielle avec des réponses JSON structurées


## Articles connexes

  * [Vue d’ensemble de Web Search](</fr/tools/web>) \-- tous les fournisseurs et la détection automatique
  * [Brave Search](</fr/tools/brave-search>) \-- résultats structurés avec filtres de pays/langue
  * [Perplexity Search](</fr/tools/perplexity-search>) \-- résultats structurés avec filtrage par domaine


Was this useful?YesNo