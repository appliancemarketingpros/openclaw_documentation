---
title: Perplexity
source_url: https://docs.openclaw.ai/fr/providers/perplexity-provider
scraped_at: 2026-05-25
---

Le Plugin Perplexity fournit des fonctionnalités de recherche web via l’API Perplexity Search ou Perplexity Sonar via OpenRouter.

Propriété | Valeur  
---|---  
Type | Fournisseur de recherche web (pas un fournisseur de modèles)  
Auth | `PERPLEXITY_API_KEY` (direct) ou `OPENROUTER_API_KEY` (via OpenRouter)  
Chemin de configuration | `plugins.entries.perplexity.config.webSearch.apiKey`  
  
## Bien démarrer

* ### Définir la clé API

Exécutez le flux interactif de configuration de la recherche web :

bashCopy code
[code]
    openclaw configure --section web
[/code]

Ou définissez directement la clé :

bashCopy code
[code]
    openclaw config set plugins.entries.perplexity.config.webSearch.apiKey "pplx-xxxxxxxxxxxx"
[/code]

* ### Commencer la recherche

L’agent utilisera automatiquement Perplexity pour les recherches web une fois la clé configurée. Aucune étape supplémentaire n’est requise.

## Modes de recherche

Le Plugin sélectionne automatiquement le transport selon le préfixe de la clé API :

### API Perplexity native (pplx-)

Lorsque votre clé commence par `pplx-`, OpenClaw utilise l’API Perplexity Search native. Ce transport renvoie des résultats structurés et prend en charge les filtres de domaine, de langue et de date (voir les options de filtrage ci-dessous).

### OpenRouter / Sonar (sk-or-)

Lorsque votre clé commence par `sk-or-`, OpenClaw achemine les requêtes via OpenRouter en utilisant le modèle Perplexity Sonar. Ce transport renvoie des réponses synthétisées par IA avec des citations.

Préfixe de clé | Transport | Fonctionnalités  
---|---|---  
`pplx-` | API Perplexity Search native | Résultats structurés, filtres de domaine/langue/date  
`sk-or-` | OpenRouter (Sonar) | Réponses synthétisées par IA avec citations  
  
## Filtrage de l’API native

Lors de l’utilisation de l’API Perplexity native, les recherches prennent en charge les filtres suivants :

Filtre | Description | Exemple  
---|---|---  
Pays | Code pays à 2 lettres | `us`, `de`, `jp`  
Langue | Code de langue ISO 639-1 | `en`, `fr`, `zh`  
Plage de dates | Fenêtre de récence | `day`, `week`, `month`, `year`  
Filtres de domaine | Liste d’autorisation ou de refus (20 domaines max.) | `example.com`  
Budget de contenu | Limites de jetons par réponse / par page | `max_tokens`, `max_tokens_per_page`  
  
## Configuration avancée

Variable d’environnement pour les processus daemon

Si le Gateway OpenClaw s’exécute comme daemon (launchd/systemd), assurez-vous que `PERPLEXITY_API_KEY` est disponible pour ce processus.

Configuration du proxy OpenRouter

Si vous préférez acheminer les recherches Perplexity via OpenRouter, définissez une `OPENROUTER_API_KEY` (préfixe `sk-or-`) au lieu d’une clé Perplexity native. OpenClaw détectera le préfixe et basculera automatiquement vers le transport Sonar.

## Associé

[**Outil de recherche Perplexity** Comment l’agent invoque les recherches Perplexity et interprète les résultats. ](</fr/tools/perplexity-search>) [**Référence de configuration** Référence de configuration complète incluant les entrées de Plugin. ](</fr/gateway/configuration-reference>)

Was this useful?YesNo