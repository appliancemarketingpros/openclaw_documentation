---
title: Génération d’images
source_url: https://docs.openclaw.ai/fr/tools/image-generation
scraped_at: 2026-05-25
---

L’outil `image_generate` permet à l’agent de créer et de modifier des images avec vos fournisseurs configurés. Les images générées sont livrées automatiquement sous forme de pièces jointes multimédias dans la réponse de l’agent.

## Démarrage rapide

* ### Configurer l’authentification

Définissez une clé d’API pour au moins un fournisseur (par exemple `OPENAI_API_KEY`, `GEMINI_API_KEY`, `OPENROUTER_API_KEY`) ou connectez-vous avec OpenAI Codex OAuth.

* ### Choisir un modèle par défaut (facultatif)

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openai/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

Codex OAuth utilise la même référence de modèle `openai/gpt-image-2`. Lorsqu’un profil OAuth `openai-codex` est configuré, OpenClaw achemine les requêtes d’image via ce profil OAuth au lieu d’essayer d’abord `OPENAI_API_KEY`. Une configuration explicite `models.providers.openai` (clé d’API, URL de base personnalisée/Azure) réactive l’acheminement direct via l’API OpenAI Images.

* ### Interroger l’agent

_« Génère une image d’une mascotte robot amicale. »_

L’agent appelle `image_generate` automatiquement. Aucune liste d’autorisation d’outils n’est nécessaire : il est activé par défaut lorsqu’un fournisseur est disponible.

## Routes courantes

Objectif | Référence de modèle | Authentification  
---|---|---  
Génération d’images OpenAI avec facturation API | `openai/gpt-image-2` | `OPENAI_API_KEY`  
Génération d’images OpenAI avec authentification par abonnement Codex | `openai/gpt-image-2` | OpenAI Codex OAuth  
PNG/WebP à arrière-plan transparent OpenAI | `openai/gpt-image-1.5` | `OPENAI_API_KEY` ou OpenAI Codex OAuth  
Génération d’images DeepInfra | `deepinfra/black-forest-labs/FLUX-1-schnell` | `DEEPINFRA_API_KEY`  
Génération d’images OpenRouter | `openrouter/google/gemini-3.1-flash-image-preview` | `OPENROUTER_API_KEY`  
Génération d’images LiteLLM | `litellm/gpt-image-2` | `LITELLM_API_KEY`  
Génération d’images Google Gemini | `google/gemini-3.1-flash-image-preview` | `GEMINI_API_KEY` ou `GOOGLE_API_KEY`  
  
Le même outil `image_generate` gère le texte-vers-image et la modification avec image de référence. Utilisez `image` pour une référence ou `images` pour plusieurs références. Les indications de sortie prises en charge par le fournisseur, telles que `quality`, `outputFormat` et `background`, sont transmises lorsqu’elles sont disponibles et signalées comme ignorées lorsqu’un fournisseur ne les prend pas en charge. La prise en charge intégrée des arrière-plans transparents est spécifique à OpenAI ; d’autres fournisseurs peuvent tout de même préserver l’alpha PNG si leur backend l’émet.

## Fournisseurs pris en charge

Fournisseur | Modèle par défaut | Prise en charge de la modification | Authentification  
---|---|---|---  
ComfyUI | `workflow` | Oui (1 image, configurée par le workflow) | `COMFY_API_KEY` ou `COMFY_CLOUD_API_KEY` pour le cloud  
DeepInfra | `black-forest-labs/FLUX-1-schnell` | Oui (1 image) | `DEEPINFRA_API_KEY`  
fal | `fal-ai/flux/dev` | Oui (limites propres au modèle) | `FAL_KEY`  
Google | `gemini-3.1-flash-image-preview` | Oui | `GEMINI_API_KEY` ou `GOOGLE_API_KEY`  
LiteLLM | `gpt-image-2` | Oui (jusqu’à 5 images d’entrée) | `LITELLM_API_KEY`  
MiniMax | `image-01` | Oui (référence du sujet) | `MINIMAX_API_KEY` ou MiniMax OAuth (`minimax-portal`)  
OpenAI | `gpt-image-2` | Oui (jusqu’à 4 images) | `OPENAI_API_KEY` ou OpenAI Codex OAuth  
OpenRouter | `google/gemini-3.1-flash-image-preview` | Oui (jusqu’à 5 images d’entrée) | `OPENROUTER_API_KEY`  
Vydra | `grok-imagine` | Non | `VYDRA_API_KEY`  
xAI | `grok-imagine-image` | Oui (jusqu’à 5 images) | `XAI_API_KEY`  
  
Utilisez `action: "list"` pour inspecter les fournisseurs et modèles disponibles au moment de l’exécution :

textCopy code
[code]
    /tool image_generate action=list
[/code]

## Capacités des fournisseurs

Capacité | ComfyUI | DeepInfra | fal | Google | MiniMax | OpenAI | Vydra | xAI  
---|---|---|---|---|---|---|---|---  
Génération (nombre max.) | Définie par le workflow | 4 | 4 | 4 | 9 | 4 | 1 | 4  
Modification / référence | 1 image (workflow) | 1 image | Flux : 1 ; GPT : 10 ; NB2 : 14 | Jusqu’à 5 images | 1 image (réf. sujet) | Jusqu’à 5 images | - | Jusqu’à 5 images  
Contrôle de la taille | - | ✓ | ✓ | ✓ | - | Jusqu’à 4K | - | -  
Rapport d’aspect | - | - | ✓ | ✓ | ✓ | - | - | ✓  
Résolution (1K/2K/4K) | - | - | ✓ | ✓ | - | - | - | 1K, 2K  
  
## Paramètres de l’outil

Invite de génération d’image. Requise pour `action: "generate"`.

Utilisez `"list"` pour inspecter les fournisseurs et modèles disponibles au moment de l’exécution.

Remplacement de fournisseur/modèle (par ex. `openai/gpt-image-2`). Utilisez `openai/gpt-image-1.5` pour les arrière-plans OpenAI transparents.

Chemin ou URL d’une seule image de référence pour le mode modification.

Plusieurs images de référence pour le mode modification (jusqu’à 5 chez les fournisseurs compatibles).

Indication de taille : `1024x1024`, `1536x1024`, `1024x1536`, `2048x2048`, `3840x2160`.

Rapport d’aspect : `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`.

Indication de qualité lorsque le fournisseur la prend en charge.

Indication de format de sortie lorsque le fournisseur la prend en charge.

Indication d’arrière-plan lorsque le fournisseur la prend en charge. Utilisez `transparent` avec `outputFormat: "png"` ou `"webp"` pour les fournisseurs compatibles avec la transparence.

Délai d’expiration facultatif de la requête fournisseur, en millisecondes. Lorsque Codex appelle `image_generate` via des outils dynamiques, cette valeur par appel remplace toujours la valeur par défaut configurée et est plafonnée à 600000 ms.

Indications propres à OpenAI : `background`, `moderation`, `outputCompression` et `user`.

## Configuration

### Sélection du modèle

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openai/gpt-image-2",        timeoutMs: 180_000,        fallbacks: [          "openrouter/google/gemini-3.1-flash-image-preview",          "google/gemini-3.1-flash-image-preview",          "fal/fal-ai/flux/dev",        ],      },    },  },}
[/code]

### Ordre de sélection des fournisseurs

OpenClaw essaie les fournisseurs dans cet ordre :

  1. **Paramètre`model`** de l’appel d’outil (si l’agent en spécifie un).
  2. **`imageGenerationModel.primary`** depuis la configuration.
  3. **`imageGenerationModel.fallbacks`** dans l’ordre.
  4. **Détection automatique** : valeurs par défaut de fournisseur adossées à l’authentification uniquement : 
     * fournisseur par défaut actuel en premier ;
     * autres fournisseurs de génération d’images enregistrés dans l’ordre des identifiants de fournisseur.


Si un fournisseur échoue (erreur d’authentification, limite de débit, etc.), le candidat configuré suivant est essayé automatiquement. Si tous échouent, l’erreur inclut les détails de chaque tentative.

Les remplacements de modèle par appel sont exacts

Un remplacement `model` par appel essaie uniquement ce fournisseur/modèle et ne poursuit pas vers les fournisseurs primary/fallback configurés ou détectés automatiquement.

La détection automatique tient compte de l’authentification

Une valeur par défaut de fournisseur n’entre dans la liste des candidats que lorsqu’OpenClaw peut effectivement authentifier ce fournisseur. Définissez `agents.defaults.mediaGenerationAutoProviderFallback: false` pour utiliser uniquement les entrées explicites `model`, `primary` et `fallbacks`.

Délais d’expiration

Définissez `agents.defaults.imageGenerationModel.timeoutMs` pour les backends d’images lents. Un paramètre d’outil `timeoutMs` par appel remplace la valeur par défaut configurée. Les appels d’outils dynamiques Codex respectent le même budget de délai d’expiration, limité par le maximum de 600000 ms du pont d’outils dynamiques d’OpenClaw.

Inspecter au moment de l’exécution

Utilisez `action: "list"` pour inspecter les fournisseurs actuellement enregistrés, leurs modèles par défaut et les indications de variables d’environnement d’authentification.

### Modification d’images

OpenAI, OpenRouter, Google, DeepInfra, fal, MiniMax, ComfyUI et xAI prennent en charge la modification d’images de référence. Fournissez un chemin ou une URL d’image de référence :

textCopy code
[code]
    "Generate a watercolor version of this photo" + image: "/path/to/photo.jpg"
[/code]

OpenAI, OpenRouter, Google et xAI prennent en charge jusqu'à 5 images de référence via le paramètre `images`. fal prend en charge 1 image de référence pour le Flux image-to-image, jusqu'à 10 pour les modifications GPT Image 2, et jusqu'à 14 pour les modifications Nano Banana 2. MiniMax et ComfyUI en prennent en charge 1.

## Analyses approfondies des fournisseurs

OpenAI gpt-image-2 (and gpt-image-1.5)

La génération d'images OpenAI utilise `openai/gpt-image-2` par défaut. Si un profil OAuth `openai-codex` est configuré, OpenClaw réutilise le même profil OAuth utilisé par les modèles de chat avec abonnement Codex et envoie la requête d'image via le backend Codex Responses. Les anciennes URL de base Codex, comme `https://chatgpt.com/backend-api`, sont canonisées en `https://chatgpt.com/backend-api/codex` pour les requêtes d'image. OpenClaw ne se rabat **pas** silencieusement sur `OPENAI_API_KEY` pour cette requête - pour forcer un routage direct vers l'API OpenAI Images, configurez explicitement `models.providers.openai` avec une clé d'API, une URL de base personnalisée ou un endpoint Azure.

Les modèles `openai/gpt-image-1.5`, `openai/gpt-image-1` et `openai/gpt-image-1-mini` peuvent toujours être sélectionnés explicitement. Utilisez `gpt-image-1.5` pour une sortie PNG/WebP à arrière-plan transparent ; l'API `gpt-image-2` actuelle rejette `background: "transparent"`.

`gpt-image-2` prend en charge à la fois la génération texte-vers-image et la modification avec image de référence via le même outil `image_generate`. OpenClaw transmet `prompt`, `count`, `size`, `quality`, `outputFormat` et les images de référence à OpenAI. OpenAI ne reçoit **pas** directement `aspectRatio` ni `resolution` ; lorsque c'est possible, OpenClaw les mappe vers une `size` prise en charge, sinon l'outil les signale comme remplacements ignorés.

Les options propres à OpenAI se trouvent sous l'objet `openai` :

jsonCopy code
[code]
    {  "quality": "low",  "outputFormat": "jpeg",  "openai": {    "background": "opaque",    "moderation": "low",    "outputCompression": 60,    "user": "end-user-42"  }}
[/code]

`openai.background` accepte `transparent`, `opaque` ou `auto` ; les sorties transparentes nécessitent un `outputFormat` `png` ou `webp` et un modèle d'image OpenAI compatible avec la transparence. OpenClaw route les requêtes par défaut `gpt-image-2` à arrière-plan transparent vers `gpt-image-1.5`. `openai.outputCompression` s'applique aux sorties JPEG/WebP.

L'indice de premier niveau `background` est indépendant du fournisseur et se mappe actuellement vers le même champ de requête OpenAI `background` lorsque le fournisseur OpenAI est sélectionné. Les fournisseurs qui ne déclarent pas la prise en charge des arrière-plans le renvoient dans `ignoredOverrides` au lieu de recevoir le paramètre non pris en charge.

Pour router la génération d'images OpenAI via un déploiement Azure OpenAI au lieu de `api.openai.com`, consultez [endpoints Azure OpenAI](</fr/providers/openai#azure-openai-endpoints>).

OpenRouter image models

La génération d'images OpenRouter utilise la même `OPENROUTER_API_KEY` et passe par l'API d'images des complétions de chat d'OpenRouter. Sélectionnez les modèles d'image OpenRouter avec le préfixe `openrouter/` :

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openrouter/google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

OpenClaw transmet `prompt`, `count`, les images de référence, ainsi que les indices `aspectRatio` / `resolution` compatibles Gemini à OpenRouter. Les raccourcis intégrés actuels de modèles d'image OpenRouter incluent `google/gemini-3.1-flash-image-preview`, `google/gemini-3-pro-image-preview` et `openai/gpt-5.4-image-2`. Utilisez `action: "list"` pour voir ce qu'expose votre plugin configuré.

MiniMax dual-auth

La génération d'images MiniMax est disponible via les deux chemins d'authentification MiniMax intégrés :

  * `minimax/image-01` pour les configurations avec clé d'API
  * `minimax-portal/image-01` pour les configurations OAuth

xAI grok-imagine-image

Le fournisseur xAI intégré utilise `/v1/images/generations` pour les requêtes avec prompt uniquement et `/v1/images/edits` lorsque `image` ou `images` est présent.

  * Modèles : `xai/grok-imagine-image`, `xai/grok-imagine-image-pro`
  * Nombre : jusqu'à 4
  * Références : une `image` ou jusqu'à cinq `images`
  * Formats d'image : `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `2:3`, `3:2`
  * Résolutions : `1K`, `2K`
  * Sorties : renvoyées sous forme de pièces jointes d'image gérées par OpenClaw


OpenClaw n'expose volontairement pas les options natives xAI `quality`, `mask`, `user` ni les formats d'image supplémentaires propres à xAI tant que ces contrôles n'existent pas dans le contrat partagé inter-fournisseurs `image_generate`.

## Exemples

### Generate (4K landscape)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="A clean editorial poster for OpenClaw image generation" size=3840x2160 count=1
[/code]

### Generate (transparent PNG)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-1.5 prompt="A simple red circle sticker on a transparent background" outputFormat=png background=transparent
[/code]

CLI équivalente :

bashCopy code
[code]
    openclaw infer image generate \--model openai/gpt-image-1.5 \--output-format png \--background transparent \--prompt "A simple red circle sticker on a transparent background" \--json
[/code]

### Generate (two square)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Two visual directions for a calm productivity app icon" size=1024x1024 count=2
[/code]

### Edit (one reference)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Keep the subject, replace the background with a bright studio setup" image=/path/to/reference.png size=1024x1536
[/code]

### Edit (multiple references)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Combine the character identity from the first image with the color palette from the second" images='["/path/to/character.png","/path/to/palette.jpg"]' size=1536x1024
[/code]

Les mêmes indicateurs `--output-format` et `--background` sont disponibles sur `openclaw infer image edit` ; `--openai-background` reste un alias spécifique à OpenAI. Les fournisseurs intégrés autres qu'OpenAI ne déclarent pas aujourd'hui de contrôle explicite de l'arrière-plan ; `background: "transparent"` est donc signalé comme ignoré pour eux.

## Voir aussi

  * [Vue d'ensemble des outils](</fr/tools>) \- tous les outils d'agent disponibles
  * [ComfyUI](</fr/providers/comfy>) \- configuration des workflows ComfyUI local et Comfy Cloud
  * [fal](</fr/providers/fal>) \- configuration du fournisseur d'images et de vidéos fal
  * [Google (Gemini)](</fr/providers/google>) \- configuration du fournisseur d'images Gemini
  * [MiniMax](</fr/providers/minimax>) \- configuration du fournisseur d'images MiniMax
  * [OpenAI](</fr/providers/openai>) \- configuration du fournisseur OpenAI Images
  * [Vydra](</fr/providers/vydra>) \- configuration des images, vidéos et de la parole Vydra
  * [xAI](</fr/providers/xai>) \- configuration de Grok pour l'image, la vidéo, la recherche, l'exécution de code et TTS
  * [Référence de configuration](</fr/gateway/config-agents#agent-defaults>) \- configuration `imageGenerationModel`
  * [Modèles](</fr/concepts/models>) \- configuration des modèles et basculement en cas d'échec


Was this useful?YesNo