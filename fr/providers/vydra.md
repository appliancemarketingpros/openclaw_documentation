---
title: Vydra
source_url: https://docs.openclaw.ai/fr/providers/vydra
scraped_at: 2026-05-25
---

Le plugin Vydra inclus ajoute :

  * Génération d’images via `vydra/grok-imagine`
  * Génération de vidéos via `vydra/veo3` et `vydra/kling`
  * Synthèse vocale via la route TTS de Vydra adossée à ElevenLabs


OpenClaw utilise la même `VYDRA_API_KEY` pour les trois capacités.

Propriété | Valeur  
---|---  
ID fournisseur | `vydra`  
Plugin | inclus, `enabledByDefault: true`  
Var env d’auth | `VYDRA_API_KEY`  
Indicateur d’onboarding | `--auth-choice vydra-api-key`  
Indicateur CLI direct | `--vydra-api-key <key>`  
Contrats | `imageGenerationProviders`, `videoGenerationProviders`, `speechProviders`  
URL de base | `https://www.vydra.ai/api/v1` (utilisez l’hôte `www`)  
  
## Configuration

* ### Exécuter l’onboarding interactif

bashCopy code
[code]
    openclaw onboard --auth-choice vydra-api-key
[/code]

Ou définissez directement la variable d’environnement :

bashCopy code
[code]
    export VYDRA_API_KEY="vydra_live_..."
[/code]

* ### Choisir une capacité par défaut

Choisissez une ou plusieurs des capacités ci-dessous (image, vidéo ou voix) et appliquez la configuration correspondante.

## Capacités

Génération d’images

Modèle d’image par défaut :

  * `vydra/grok-imagine`


Définissez-le comme fournisseur d’images par défaut :

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "vydra/grok-imagine",      },    },  },}
[/code]

La prise en charge actuellement incluse couvre uniquement le texte vers image. Les routes de modification hébergées par Vydra attendent des URL d’images distantes, et OpenClaw n’ajoute pas encore de passerelle d’envoi propre à Vydra dans le plugin inclus.

Génération de vidéos

Modèles vidéo enregistrés :

  * `vydra/veo3` pour le texte vers vidéo
  * `vydra/kling` pour l’image vers vidéo


Définissez Vydra comme fournisseur vidéo par défaut :

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "vydra/veo3",      },    },  },}
[/code]

Notes :

  * `vydra/veo3` est inclus uniquement pour le texte vers vidéo.
  * `vydra/kling` nécessite actuellement une référence d’URL d’image distante. Les envois de fichiers locaux sont rejetés dès le départ.
  * La route HTTP `kling` actuelle de Vydra a été incohérente quant au champ requis, `image_url` ou `video_url` ; le fournisseur inclus mappe la même URL d’image distante dans les deux champs.
  * Le plugin inclus reste conservateur et ne transmet pas les réglages de style non documentés tels que le format d’image, la résolution, le filigrane ou l’audio généré.

Tests live vidéo

Couverture live propre au fournisseur :

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_VYDRA_VIDEO=1 \pnpm test:live -- extensions/vydra/vydra.live.test.ts
[/code]

Le fichier live Vydra inclus couvre maintenant :

  * `vydra/veo3` texte vers vidéo
  * `vydra/kling` image vers vidéo avec une URL d’image distante


Remplacez le fixture d’image distante lorsque nécessaire :

bashCopy code
[code]
    export OPENCLAW_LIVE_VYDRA_KLING_IMAGE_URL="https://example.com/reference.png"
[/code]

Synthèse vocale

Définissez Vydra comme fournisseur vocal :

json5Copy code
[code]
    {  messages: {    tts: {      provider: "vydra",      providers: {        vydra: {          apiKey: "${VYDRA_API_KEY}",          voiceId: "21m00Tcm4TlvDq8ikWAM",        },      },    },  },}
[/code]

Valeurs par défaut :

  * Modèle : `elevenlabs/tts`
  * ID de voix : `21m00Tcm4TlvDq8ikWAM`


Le plugin inclus expose actuellement une voix par défaut connue comme fiable et renvoie des fichiers audio MP3.

## Connexe

[**Répertoire des fournisseurs** Parcourez tous les fournisseurs disponibles. ](</fr/providers>) [**Génération d’images** Paramètres d’outil d’image partagés et sélection du fournisseur. ](</fr/tools/image-generation>) [**Génération de vidéos** Paramètres d’outil vidéo partagés et sélection du fournisseur. ](</fr/tools/video-generation>) [**Référence de configuration** Valeurs par défaut d’agent et configuration des modèles. ](</fr/gateway/config-agents#agent-defaults>)

Was this useful?YesNo