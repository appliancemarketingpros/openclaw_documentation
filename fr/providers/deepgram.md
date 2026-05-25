---
title: Deepgram
source_url: https://docs.openclaw.ai/fr/providers/deepgram
scraped_at: 2026-05-25
---

Deepgram est une API de reconnaissance vocale. Dans OpenClaw, elle est utilisée pour la transcription des fichiers audio/notes vocales entrants via `tools.media.audio` et pour la reconnaissance vocale en streaming de Voice Call via `plugins.entries.voice-call.config.streaming`.

Pour la transcription par lot, OpenClaw téléverse le fichier audio complet vers Deepgram et injecte la transcription dans le pipeline de réponse (`{{Transcript}}` \+ bloc `[Audio]`). Pour la transcription en streaming Voice Call, OpenClaw transfère des trames G.711 u-law live via le point de terminaison WebSocket `listen` de Deepgram et émet des transcriptions partielles ou finales à mesure que Deepgram les renvoie.

Détail | Valeur  
---|---  
Site web | [deepgram.com](<https://deepgram.com>)  
Documentation | [developers.deepgram.com](<https://developers.deepgram.com>)  
Authentification | `DEEPGRAM_API_KEY`  
Modèle par défaut | `nova-3`  
  
## Démarrage

* ### Définir votre clé API

Ajoutez votre clé API Deepgram à l’environnement :

CodeCopy code
[code]
    DEEPGRAM_API_KEY=dg_...
[/code]

* ### Activer le fournisseur audio

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

* ### Envoyer une note vocale

Envoyez un message audio via n’importe quel canal connecté. OpenClaw le transcrit via Deepgram et injecte la transcription dans le pipeline de réponse.

## Options de configuration

Option | Chemin | Description  
---|---|---  
`model` | `tools.media.audio.models[].model` | Identifiant du modèle Deepgram (par défaut : `nova-3`)  
`language` | `tools.media.audio.models[].language` | Indice de langue (facultatif)  
`detect_language` | `tools.media.audio.providerOptions.deepgram.detect_language` | Activer la détection de langue (facultatif)  
`punctuate` | `tools.media.audio.providerOptions.deepgram.punctuate` | Activer la ponctuation (facultatif)  
`smart_format` | `tools.media.audio.providerOptions.deepgram.smart_format` | Activer le formatage intelligent (facultatif)  
  
### Avec un indice de langue

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3", language: "en" }],      },    },  },}
[/code]

### Avec les options Deepgram

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        providerOptions: {          deepgram: {            detect_language: true,            punctuate: true,            smart_format: true,          },        },        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

## Reconnaissance vocale en streaming Voice Call

Le Plugin intégré `deepgram` enregistre aussi un fournisseur de transcription temps réel pour le Plugin Voice Call.

Paramètre | Chemin de configuration | Par défaut  
---|---|---  
Clé API | `plugins.entries.voice-call.config.streaming.providers.deepgram.apiKey` | Se replie sur `DEEPGRAM_API_KEY`  
Modèle | `...deepgram.model` | `nova-3`  
Langue | `...deepgram.language` | (non défini)  
Encodage | `...deepgram.encoding` | `mulaw`  
Taux d’échantillonnage | `...deepgram.sampleRate` | `8000`  
Endpointing | `...deepgram.endpointingMs` | `800`  
Résultats intermédiaires | `...deepgram.interimResults` | `true`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "deepgram",            providers: {              deepgram: {                apiKey: "${DEEPGRAM_API_KEY}",                model: "nova-3",                endpointingMs: 800,                language: "en-US",              },            },          },        },      },    },  },}
[/code]

## Remarques

Authentification

L’authentification suit l’ordre standard d’authentification des fournisseurs. `DEEPGRAM_API_KEY` est le chemin le plus simple.

Proxy et points de terminaison personnalisés

Remplacez les points de terminaison ou les en-têtes avec `tools.media.audio.baseUrl` et `tools.media.audio.headers` lors de l’utilisation d’un proxy.

Comportement de sortie

La sortie suit les mêmes règles audio que les autres fournisseurs (plafonds de taille, délais, injection de transcription).

## Liens associés

[**Outils média** Vue d’ensemble du pipeline de traitement audio, image et vidéo. ](</fr/tools/media-overview>) [**Configuration** Référence complète de configuration, y compris les paramètres des outils média. ](</fr/gateway/configuration>) [**Dépannage** Problèmes courants et étapes de débogage. ](</fr/help/troubleshooting>) [**FAQ** Questions fréquemment posées sur la configuration d’OpenClaw. ](</fr/help/faq>)

Was this useful?YesNo