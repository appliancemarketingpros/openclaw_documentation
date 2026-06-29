---
title: PixVerse
source_url: https://docs.openclaw.ai/fr/providers/pixverse
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw fournit `pixverse` comme Plugin externe officiel pour la génération vidéo PixVerse hébergée. Le Plugin enregistre le fournisseur `pixverse` auprès du contrat `videoGenerationProviders`.

Propriété | Valeur  
---|---  
ID du fournisseur | `pixverse`  
Paquet Plugin | `@openclaw/pixverse-provider`  
Variable d’env. auth | `PIXVERSE_API_KEY`  
Indicateur d’onboarding | `--auth-choice pixverse-api-key`  
Indicateur CLI direct | `--pixverse-api-key <key>`  
API | API PixVerse Platform v2 (soumission de `video_id` et interrogation du résultat)  
Modèle par défaut | `pixverse/v6`  
Région API par défaut | Internationale  
  
## Premiers pas

* ### Installer le Plugin

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/pixverse-provideropenclaw gateway restart
[/code]

* ### Définir la clé API

bashCopy code
[code]
    openclaw onboard --auth-choice pixverse-api-key
[/code]

L’assistant demande s’il faut utiliser le point de terminaison international (`https://app-api.pixverse.ai/openapi/v2`) ou le point de terminaison CN (`https://app-api.pixverseai.cn/openapi/v2`) avant d’écrire `region` et `baseUrl` dans la configuration du fournisseur.

* ### Définir PixVerse comme fournisseur vidéo par défaut

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "pixverse/v6"
[/code]

* ### Générer une vidéo

Demandez à l’agent de générer une vidéo. PixVerse sera utilisé automatiquement.

## Modes et modèles pris en charge

Le fournisseur expose les modèles de génération PixVerse via l’outil vidéo partagé d’OpenClaw.

Mode | Modèles | Entrée de référence  
---|---|---  
Texte vers vidéo | `v6` (par défaut), `c1` | Aucune  
Image vers vidéo | `v6` (par défaut), `c1` | 1 image locale ou distante  
  
Les références d’images locales sont téléversées vers PixVerse avant la requête image vers vidéo. Les URL d’images distantes sont transmises via le point de terminaison de téléversement d’image PixVerse en tant que `image_url`.

Option | Valeurs prises en charge  
---|---  
Durée | 1 à 15 secondes  
Résolution | `360P`, `540P`, `720P`, `1080P`  
Format d’image | `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `2:3`, `3:2`, `21:9` pour texte vers vidéo  
Audio généré | `audio: true`  
  
## Options du fournisseur

Le fournisseur vidéo accepte ces clés facultatives propres au fournisseur :

Option | Type | Effet  
---|---|---  
`seed` | number | Graine déterministe lorsque prise en charge  
`negativePrompt` / `negative_prompt` | string | Invite négative  
`quality` | string | Qualité PixVerse, par exemple `720p`  
`motionMode` / `motion_mode` | string | Mode de mouvement image vers vidéo  
`cameraMovement` / `camera_movement` | string | Préréglage de mouvement de caméra PixVerse  
`templateId` / `template_id` | number | Identifiant de modèle PixVerse activé  
  
## Configuration

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "pixverse/v6",      },    },  },}
[/code]

## Configuration avancée

Région API

OpenClaw utilise par défaut l’API PixVerse internationale. Définissez `models.providers.pixverse.region` manuellement lorsque votre clé appartient à une région spécifique de la plateforme PixVerse, ou utilisez `openclaw onboard --auth-choice pixverse-api-key` pour en choisir une dans l’assistant de configuration :

Valeur de région | URL de base de l’API PixVerse  
---|---  
`international` | `https://app-api.pixverse.ai/openapi/v2`  
`cn` | `https://app-api.pixverseai.cn/openapi/v2`  
  
json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        region: "cn", // "international" or "cn"        baseUrl: "https://app-api.pixverseai.cn/openapi/v2",        models: [],      },    },  },}
[/code]

URL de base personnalisée

Définissez `models.providers.pixverse.baseUrl` uniquement lors du routage via un proxy compatible de confiance. `baseUrl` est prioritaire sur `region`.

json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        baseUrl: "https://app-api.pixverse.ai/openapi/v2",      },    },  },}
[/code]

Interrogation des tâches

PixVerse renvoie un `video_id` depuis la requête de génération. OpenClaw interroge `/openapi/v2/video/result/{video_id}` jusqu’à ce que la tâche réussisse, échoue ou expire.

## Connexe

[**Génération vidéo** Paramètres de l’outil partagé, sélection du fournisseur et comportement asynchrone. ](</fr/tools/video-generation>) [**Référence de configuration** Paramètres par défaut de l’agent, y compris le modèle de génération vidéo. ](</fr/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue