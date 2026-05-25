---
title: Fal
source_url: https://docs.openclaw.ai/fr/providers/fal
scraped_at: 2026-05-25
---

OpenClaw inclut un fournisseur `fal` groupé pour la génération hébergée d’images et de vidéos.

Propriété | Valeur  
---|---  
Fournisseur | `fal`  
Authentification | `FAL_KEY` (canonique ; `FAL_API_KEY` fonctionne aussi comme solution de repli)  
API | Points de terminaison de modèles fal  
  
## Bien démarrer

* ### Définir la clé API

bashCopy code
[code]
    openclaw onboard --auth-choice fal-api-key
[/code]

* ### Définir un modèle d’image par défaut

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Génération d’images

Le fournisseur de génération d’images `fal` groupé utilise par défaut `fal/fal-ai/flux/dev`.

Capacité | Valeur  
---|---  
Nombre maximal d’images | 4 par requête  
Mode édition | Flux : 1 image de référence ; GPT Image 2 : 10 ; Nano Banana 2 : 14  
Remplacements de taille | Pris en charge  
Rapport d’aspect | Pris en charge pour la génération et l’édition GPT Image 2/Nano Banana 2  
Résolution | Prise en charge  
Format de sortie | `png` ou `jpeg`  
  
Utilisez `outputFormat: "png"` lorsque vous voulez une sortie PNG. fal ne déclare pas de contrôle explicite d’arrière-plan transparent dans OpenClaw, donc `background: "transparent"` est signalé comme un remplacement ignoré pour les modèles fal.

Pour utiliser fal comme fournisseur d’images par défaut :

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Génération de vidéos

Le fournisseur de génération de vidéos `fal` groupé utilise par défaut `fal/fal-ai/minimax/video-01-live`.

Capacité | Valeur  
---|---  
Modes | Texte-vers-vidéo, référence d’image unique, référence-vers-vidéo Seedance  
Exécution | Flux soumission/état/résultat adossé à une file d’attente pour les tâches longues  
  
Modèles vidéo disponibles

**HeyGen video-agent :**

  * `fal/fal-ai/heygen/v2/video-agent`


**Seedance 2.0 :**

  * `fal/bytedance/seedance-2.0/fast/text-to-video`
  * `fal/bytedance/seedance-2.0/fast/image-to-video`
  * `fal/bytedance/seedance-2.0/fast/reference-to-video`
  * `fal/bytedance/seedance-2.0/text-to-video`
  * `fal/bytedance/seedance-2.0/image-to-video`
  * `fal/bytedance/seedance-2.0/reference-to-video`

Exemple de configuration Seedance 2.0 json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/text-to-video",      },    },  },}
[/code]

Exemple de configuration référence-vers-vidéo Seedance 2.0 json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/reference-to-video",      },    },  },}
[/code]

La référence-vers-vidéo accepte jusqu’à 9 images, 3 vidéos et 3 références audio via les paramètres partagés `video_generate` `images`, `videos` et `audioRefs`, avec au maximum 12 fichiers de référence au total.

Exemple de configuration HeyGen video-agent json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/fal-ai/heygen/v2/video-agent",      },    },  },}
[/code]

## Connexe

[**Génération d’images** Paramètres partagés de l’outil d’image et sélection du fournisseur. ](</fr/tools/image-generation>) [**Génération de vidéos** Paramètres partagés de l’outil vidéo et sélection du fournisseur. ](</fr/tools/video-generation>) [**Référence de configuration** Valeurs par défaut des agents, y compris la sélection des modèles d’image et de vidéo. ](</fr/gateway/config-agents#agent-defaults>)

Was this useful?YesNo