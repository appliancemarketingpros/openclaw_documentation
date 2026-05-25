---
title: Arcee AI
source_url: https://docs.openclaw.ai/fr/providers/arcee
scraped_at: 2026-05-25
---

[Arcee AI](<https://arcee.ai>) donne accès à la famille Trinity de modèles à mélange d’experts via une API compatible avec OpenAI. Tous les modèles Trinity sont sous licence Apache 2.0.

Les modèles Arcee AI sont accessibles directement via la plateforme Arcee ou via [OpenRouter](</fr/providers/openrouter>).

Propriété | Valeur  
---|---  
Fournisseur | `arcee`  
Authentification | `ARCEEAI_API_KEY` (direct) ou `OPENROUTER_API_KEY` (via OpenRouter)  
API | Compatible avec OpenAI  
URL de base | `https://api.arcee.ai/api/v1` (direct) ou `https://openrouter.ai/api/v1` (OpenRouter)  
  
## Premiers pas

### Direct (Arcee platform)

* ### Obtenir une clé API

Créez une clé API sur [Arcee AI](<https://chat.arcee.ai/>).

* ### Exécuter l’intégration

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-api-key
[/code]

* ### Définir un modèle par défaut

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

### Via OpenRouter

* ### Obtenir une clé API

Créez une clé API sur [OpenRouter](<https://openrouter.ai/keys>).

* ### Exécuter l’intégration

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-openrouter
[/code]

* ### Définir un modèle par défaut

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

Les mêmes références de modèle fonctionnent pour les configurations directes et OpenRouter (par exemple `arcee/trinity-large-thinking`).

## Configuration non interactive

### Direct (Arcee platform)

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-api-key \  --arceeai-api-key "$ARCEEAI_API_KEY"
[/code]

### Via OpenRouter

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-openrouter \  --openrouter-api-key "$OPENROUTER_API_KEY"
[/code]

## Catalogue intégré

OpenClaw inclut actuellement ce catalogue Arcee intégré :

Référence du modèle | Nom | Entrée | Contexte | Coût (entrée/sortie par million) | Notes  
---|---|---|---|---|---  
`arcee/trinity-large-thinking` | Trinity Large Thinking | texte | 256K | $0.25 / $0.90 | Modèle par défaut ; raisonnement activé  
`arcee/trinity-large-preview` | Trinity Large Preview | texte | 128K | $0.25 / $1.00 | Généraliste ; 400B paramètres, 13B actifs  
`arcee/trinity-mini` | Trinity Mini 26B | texte | 128K | $0.045 / $0.15 | Rapide et économique ; appel de fonctions  
  
## Fonctionnalités prises en charge

Fonctionnalité | Pris en charge  
---|---  
Streaming | Oui  
Utilisation d’outils / appel de fonctions | Oui (Trinity Mini, Trinity Large Preview)  
Sortie structurée (mode JSON et schéma JSON) | Oui  
Réflexion étendue | Oui (Trinity Large Thinking ; outils désactivés)  
  
Note sur l’environnement

Si le Gateway s’exécute comme daemon (launchd/systemd), assurez-vous que `ARCEEAI_API_KEY` (ou `OPENROUTER_API_KEY`) est disponible pour ce processus (par exemple, dans `~/.openclaw/.env` ou via `env.shellEnv`).

Routage OpenRouter

Lorsque vous utilisez des modèles Arcee via OpenRouter, les mêmes références de modèle `arcee/*` s’appliquent. OpenClaw gère le routage de manière transparente en fonction de votre choix d’authentification. Consultez la [documentation du fournisseur OpenRouter](</fr/providers/openrouter>) pour les détails de configuration propres à OpenRouter.

## Articles connexes

[**OpenRouter** Accédez aux modèles Arcee et à beaucoup d’autres avec une seule clé API. ](</fr/providers/openrouter>) [**Sélection de modèle** Choisir les fournisseurs, les références de modèle et le comportement de basculement. ](</fr/concepts/model-providers>)

Was this useful?YesNo