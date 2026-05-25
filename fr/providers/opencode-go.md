---
title: OpenCode Go
source_url: https://docs.openclaw.ai/fr/providers/opencode-go
scraped_at: 2026-05-25
---

OpenCode Go est le catalogue Go au sein de [OpenCode](</fr/providers/opencode>). Il utilise la même `OPENCODE_API_KEY` que le catalogue Zen, mais conserve l’identifiant de fournisseur d’exécution `opencode-go` afin que le routage amont par modèle reste correct.

Property | Value  
---|---  
Fournisseur d’exécution | `opencode-go`  
Authentification | `OPENCODE_API_KEY`  
Configuration parente | [OpenCode](</fr/providers/opencode>)  
  
## Catalogue intégré

OpenClaw récupère la plupart des lignes du catalogue Go à partir du registre de modèles pi intégré et complète les lignes amont actuelles pendant que le registre se met à jour. Exécutez `openclaw models list --provider opencode-go` pour obtenir la liste actuelle des modèles.

Le fournisseur inclut :

Référence de modèle | Nom  
---|---  
`opencode-go/glm-5` | GLM-5  
`opencode-go/glm-5.1` | GLM-5.1  
`opencode-go/kimi-k2.5` | Kimi K2.5  
`opencode-go/kimi-k2.6` | Kimi K2.6 (limites x3)  
`opencode-go/deepseek-v4-pro` | DeepSeek V4 Pro  
`opencode-go/deepseek-v4-flash` | DeepSeek V4 Flash  
`opencode-go/mimo-v2-omni` | MiMo V2 Omni  
`opencode-go/mimo-v2-pro` | MiMo V2 Pro  
`opencode-go/minimax-m2.5` | MiniMax M2.5  
`opencode-go/minimax-m2.7` | MiniMax M2.7  
`opencode-go/qwen3.5-plus` | Qwen3.5 Plus  
`opencode-go/qwen3.6-plus` | Qwen3.6 Plus  
  
## Premiers pas

### Interactif

* ### Exécuter l’onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

* ### Définir un modèle Go par défaut

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### Vérifier que les modèles sont disponibles

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

### Non interactif

* ### Transmettre directement la clé

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Vérifier que les modèles sont disponibles

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Exemple de configuration

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "YOUR_API_KEY_HERE" }, // pragma: allowlist secret  agents: { defaults: { model: { primary: "opencode-go/kimi-k2.6" } } },}
[/code]

## Configuration avancée

Comportement du routage

OpenClaw gère automatiquement le routage par modèle lorsque la référence de modèle utilise `opencode-go/...`. Aucune configuration supplémentaire du fournisseur n’est requise.

Convention de référence d’exécution

Les références d’exécution restent explicites : `opencode/...` pour Zen, `opencode-go/...` pour Go. Cela permet de conserver un routage amont correct par modèle dans les deux catalogues.

Identifiants partagés

La même `OPENCODE_API_KEY` est utilisée par les catalogues Zen et Go. Saisir la clé pendant la configuration enregistre les identifiants pour les deux fournisseurs d’exécution.

## Liens associés

[**OpenCode (parent)** Onboarding partagé, vue d’ensemble du catalogue et notes avancées. ](</fr/providers/opencode>) [**Sélection du modèle** Choisir les fournisseurs, les références de modèle et le comportement de basculement. ](</fr/concepts/model-providers>)

Was this useful?YesNo