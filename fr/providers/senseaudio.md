---
title: SenseAudio
source_url: https://docs.openclaw.ai/fr/providers/senseaudio
scraped_at: 2026-05-25
---

SenseAudio peut transcrire les pièces jointes audio entrantes et les notes vocales via le pipeline partagé `tools.media.audio` d’OpenClaw. OpenClaw publie l’audio multipart vers le point de terminaison de transcription compatible OpenAI et injecte le texte retourné sous forme de `{{Transcript}}` ainsi qu’un bloc `[Audio]`.

Propriété | Valeur  
---|---  
Identifiant du fournisseur | `senseaudio`  
Plugin | intégré, `enabledByDefault: true`  
Contrat | `mediaUnderstandingProviders` (audio)  
Variable d’environnement d’authentification | `SENSEAUDIO_API_KEY`  
Modèle par défaut | `senseaudio-asr-pro-1.5-260319`  
URL par défaut | `https://api.senseaudio.cn/v1`  
Site web | [senseaudio.cn](<https://senseaudio.cn>)  
Documentation | [senseaudio.cn/docs](<https://senseaudio.cn/docs>)  
  
## Bien démarrer

* ### Set your API key

bashCopy code
[code]
    export SENSEAUDIO_API_KEY="..."
[/code]

* ### Enable the audio provider

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "senseaudio", model: "senseaudio-asr-pro-1.5-260319" }],      },    },  },}
[/code]

* ### Send a voice note

Envoyez un message audio via n’importe quel canal connecté. OpenClaw téléverse l’audio vers SenseAudio et utilise la transcription dans le pipeline de réponse.

## Options

Option | Chemin | Description  
---|---|---  
`model` | `tools.media.audio.models[].model` | Identifiant du modèle ASR SenseAudio  
`language` | `tools.media.audio.models[].language` | Indication de langue facultative  
`prompt` | `tools.media.audio.prompt` | Invite de transcription facultative  
`baseUrl` | `tools.media.audio.baseUrl` ou modèle | Remplacer la base compatible OpenAI  
`headers` | `tools.media.audio.request.headers` | En-têtes de requête supplémentaires  
  
## Connexe

  * [Compréhension des médias (audio)](</fr/nodes/audio>)
  * [Fournisseurs de modèles](</fr/concepts/model-providers>)


Was this useful?YesNo