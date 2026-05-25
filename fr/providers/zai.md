---
title: Z.AI
source_url: https://docs.openclaw.ai/fr/providers/zai
scraped_at: 2026-05-25
---

[Z.AI](<http://Z.AI>) est la plateforme d’API pour les modèles **GLM**. Elle fournit des API REST pour GLM et utilise des clés d’API pour l’authentification. Créez votre clé d’API dans la console [Z.AI](<http://Z.AI>). OpenClaw utilise le fournisseur `zai` avec une clé d’API [Z.AI](<http://Z.AI>).

  * Fournisseur : `zai`
  * Authentification : `ZAI_API_KEY`
  * API : Chat Completions [Z.AI](<http://Z.AI>) (authentification Bearer)


## Bien démarrer

### Détection automatique du point de terminaison

**Idéal pour :** la plupart des utilisateurs. OpenClaw détecte le point de terminaison [Z.AI](<http://Z.AI>) correspondant à partir de la clé et applique automatiquement la bonne URL de base.

* ### Exécuter l’onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice zai-api-key
[/code]

* ### Définir un modèle par défaut

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Vérifier que le modèle est listé

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

### Point de terminaison régional explicite

**Idéal pour :** les utilisateurs qui veulent forcer un Coding Plan spécifique ou une surface d’API générale.

* ### Choisir la bonne option d’onboarding

bashCopy code
[code]
    # Coding Plan Global (recommandé pour les utilisateurs du Coding Plan)openclaw onboard --auth-choice zai-coding-global # Coding Plan CN (région Chine)openclaw onboard --auth-choice zai-coding-cn # API généraleopenclaw onboard --auth-choice zai-global # API générale CN (région Chine)openclaw onboard --auth-choice zai-cn
[/code]

* ### Définir un modèle par défaut

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Vérifier que le modèle est listé

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

## Catalogue intégré

OpenClaw fournit le catalogue du fournisseur `zai` groupé dans le manifeste du plugin, afin que le listing en lecture seule puisse afficher les lignes GLM connues sans charger le runtime du fournisseur :

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

Le catalogue basé sur le manifeste comprend actuellement :

Réf. de modèle | Notes  
---|---  
`zai/glm-5.1` | Modèle par défaut  
`zai/glm-5` |   
`zai/glm-5-turbo` |   
`zai/glm-5v-turbo` |   
`zai/glm-4.7` |   
`zai/glm-4.7-flash` |   
`zai/glm-4.7-flashx` |   
`zai/glm-4.6` |   
`zai/glm-4.6v` |   
`zai/glm-4.5` |   
`zai/glm-4.5-air` |   
`zai/glm-4.5-flash` |   
`zai/glm-4.5v` |   
  
## Configuration avancée

Résolution prospective des modèles GLM-5 inconnus

Les identifiants `glm-5*` inconnus sont encore résolus prospectivement sur le chemin du fournisseur groupé en synthétisant les métadonnées appartenant au fournisseur à partir du modèle `glm-4.7` lorsque l’identifiant correspond à la forme actuelle de la famille GLM-5.

Streaming des appels d’outils

`tool_stream` est activé par défaut pour le streaming des appels d’outils [Z.AI](<http://Z.AI>). Pour le désactiver :

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/<model>": {          params: { tool_stream: false },        },      },    },  },}
[/code]

Thinking et thinking préservé

Le thinking [Z.AI](<http://Z.AI>) suit les contrôles `/think` d’OpenClaw. Lorsque le thinking est désactivé, OpenClaw envoie `thinking: { type: "disabled" }` pour éviter les réponses qui dépensent le budget de sortie en `reasoning_content` avant le texte visible.

Le thinking préservé est opt-in, car [Z.AI](<http://Z.AI>) exige que l’intégralité de l’historique `reasoning_content` soit rejouée, ce qui augmente le nombre de tokens du prompt. Activez-le par modèle :

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/glm-5.1": {          params: { preserveThinking: true },        },      },    },  },}
[/code]

Lorsqu’il est activé et que le thinking est actif, OpenClaw envoie `thinking: { type: "enabled", clear_thinking: false }` et rejoue le `reasoning_content` précédent pour la même transcription compatible OpenAI.

Les utilisateurs avancés peuvent toujours remplacer exactement la charge utile du fournisseur avec `params.extra_body.thinking`.

Compréhension d’image

Le plugin [Z.AI](<http://Z.AI>) groupé enregistre la compréhension d’image.

Propriété | Valeur  
---|---  
Modèle | `glm-4.6v`  
  
La compréhension d’image est automatiquement résolue à partir de l’authentification [Z.AI](<http://Z.AI>) configurée ; aucune configuration supplémentaire n’est nécessaire.

Détails d’authentification

  * [Z.AI](<http://Z.AI>) utilise l’authentification Bearer avec votre clé d’API.
  * L’option d’onboarding `zai-api-key` détecte automatiquement le point de terminaison [Z.AI](<http://Z.AI>) correspondant à partir du préfixe de la clé.
  * Utilisez les options régionales explicites (`zai-coding-global`, `zai-coding-cn`, `zai-global`, `zai-cn`) lorsque vous voulez forcer une surface d’API spécifique.


## Connexe

[**Famille de modèles GLM** Vue d’ensemble de la famille de modèles GLM. ](</fr/providers/glm>) [**Sélection de modèle** Choisir les fournisseurs, les références de modèle et le comportement de basculement. ](</fr/concepts/model-providers>)

Was this useful?YesNo