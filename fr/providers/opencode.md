---
title: OpenCode
source_url: https://docs.openclaw.ai/fr/providers/opencode
scraped_at: 2026-05-25
---

OpenCode expose deux catalogues hébergés dans OpenClaw :

Catalogue | Préfixe | Fournisseur runtime  
---|---|---  
**Zen** | `opencode/...` | `opencode`  
**Go** | `opencode-go/...` | `opencode-go`  
  
Les deux catalogues utilisent la même clé API OpenCode. OpenClaw conserve des identifiants de fournisseur runtime distincts afin que le routage en amont par modèle reste correct, mais l’onboarding et la documentation les traitent comme une seule configuration OpenCode.

## Démarrage

### Catalogue Zen

**Idéal pour :** le proxy multi-modèles OpenCode sélectionné (Claude, GPT, Gemini).

* ### Exécuter l’onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zen
[/code]

Ou passez la clé directement :

bashCopy code
[code]
    openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
[/code]

* ### Définir un modèle Zen comme valeur par défaut

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode/claude-opus-4-6"
[/code]

* ### Vérifier que les modèles sont disponibles

bashCopy code
[code]
    openclaw models list --provider opencode
[/code]

### Catalogue Go

**Idéal pour :** la gamme Kimi, GLM et MiniMax hébergée par OpenCode.

* ### Exécuter l’onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

Ou passez la clé directement :

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Définir un modèle Go comme valeur par défaut

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### Vérifier que les modèles sont disponibles

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Exemple de configuration

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

## Catalogues intégrés

### Zen

Property | Value  
---|---  
Fournisseur runtime | `opencode`  
Exemples de modèles | `opencode/claude-opus-4-6`, `opencode/gpt-5.5`, `opencode/gemini-3-pro`  
  
### Go

Property | Value  
---|---  
Fournisseur runtime | `opencode-go`  
Exemples de modèles | `opencode-go/kimi-k2.6`, `opencode-go/glm-5`, `opencode-go/minimax-m2.5`  
  
## Configuration avancée

Alias de clé API

`OPENCODE_ZEN_API_KEY` est également pris en charge comme alias de `OPENCODE_API_KEY`.

Identifiants partagés

Saisir une clé OpenCode pendant la configuration stocke les identifiants pour les deux fournisseurs runtime. Vous n’avez pas besoin d’effectuer l’onboarding de chaque catalogue séparément.

Facturation et tableau de bord

Vous vous connectez à OpenCode, ajoutez les détails de facturation, puis copiez votre clé API. La facturation et la disponibilité du catalogue sont gérées depuis le tableau de bord OpenCode.

Comportement de relecture Gemini

Les références OpenCode adossées à Gemini restent sur le chemin proxy-Gemini, donc OpenClaw conserve l’assainissement des signatures de pensée Gemini sans activer la validation native de relecture Gemini ni les réécritures bootstrap.

Comportement de relecture non-Gemini

Les références OpenCode non-Gemini conservent la politique minimale de relecture compatible OpenAI.

## Liens associés

[**Sélection de modèle** Choisir les fournisseurs, les références de modèles et le comportement de failover. ](</fr/concepts/model-providers>) [**Référence de configuration** Référence complète de configuration pour agents, modèles et fournisseurs. ](</fr/gateway/configuration-reference>)

Was this useful?YesNo