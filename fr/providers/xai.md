---
title: xAI
source_url: https://docs.openclaw.ai/fr/providers/xai
scraped_at: 2026-05-25
---

OpenClaw fournit un plugin de fournisseur `xai` intégré pour les modèles Grok.

## Bien démarrer

* ### Créer une clé API

Créez une clé API dans la [console xAI](<https://console.x.ai/>).

* ### Définir votre clé API

Définissez `XAI_API_KEY`, ou exécutez :

bashCopy code
[code]
    openclaw onboard --auth-choice xai-api-key
[/code]

* ### Choisir un modèle

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "xai/grok-4.3" } } },}
[/code]

## Catalogue intégré

OpenClaw inclut directement ces familles de modèles xAI :

Famille | Identifiants de modèles  
---|---  
Grok 3 | `grok-3`, `grok-3-fast`, `grok-3-mini`, `grok-3-mini-fast`  
Grok 4.3 | `grok-4.3`  
Grok 4 | `grok-4`, `grok-4-0709`  
Grok 4 Fast | `grok-4-fast`, `grok-4-fast-non-reasoning`  
Grok 4.1 Fast | `grok-4-1-fast`, `grok-4-1-fast-non-reasoning`  
Grok 4.20 Beta | `grok-4.20-beta-latest-reasoning`, `grok-4.20-beta-latest-non-reasoning`  
Grok Code | `grok-code-fast-1`  
  
Le plugin résout également vers l’avant les identifiants plus récents `grok-4*` et `grok-code-fast*` lorsqu’ils suivent la même forme d’API.

## Couverture des fonctionnalités OpenClaw

Le plugin intégré mappe la surface d’API publique actuelle de xAI sur les contrats partagés de fournisseur et d’outils d’OpenClaw. Les capacités qui ne correspondent pas au contrat partagé (par exemple le TTS en streaming et la voix en temps réel) ne sont pas exposées ; consultez le tableau ci-dessous.

Capacité xAI | Surface OpenClaw | État  
---|---|---  
Chat / Responses | Fournisseur de modèles `xai/<model>` | Oui  
Recherche web côté serveur | Fournisseur `web_search` `grok` | Oui  
Recherche X côté serveur | Outil `x_search` | Oui  
Exécution de code côté serveur | Outil `code_execution` | Oui  
Images | `image_generate` | Oui  
Vidéos | `video_generate` | Oui  
Synthèse vocale par lot | `messages.tts.provider: "xai"` / `tts` | Oui  
TTS en streaming | - | Non exposé ; le contrat TTS d’OpenClaw renvoie des tampons audio complets  
Reconnaissance vocale par lot | `tools.media.audio` / compréhension multimédia | Oui  
Reconnaissance vocale en streaming | Voice Call `streaming.provider: "xai"` | Oui  
Voix en temps réel | - | Pas encore exposé ; contrat de session/WebSocket différent  
Fichiers / lots | Compatibilité API de modèle générique uniquement | Pas un outil OpenClaw de première classe  
  
### Mappages du mode rapide

`/fast on` ou `agents.defaults.models["xai/<model>"].params.fastMode: true` réécrit les requêtes xAI natives comme suit :

Modèle source | Cible du mode rapide  
---|---  
`grok-3` | `grok-3-fast`  
`grok-3-mini` | `grok-3-mini-fast`  
`grok-4` | `grok-4-fast`  
`grok-4-0709` | `grok-4-fast`  
  
### Alias de compatibilité hérités

Les alias hérités se normalisent toujours vers les identifiants intégrés canoniques :

Alias hérité | Identifiant canonique  
---|---  
`grok-4-fast-reasoning` | `grok-4-fast`  
`grok-4-1-fast-reasoning` | `grok-4-1-fast`  
`grok-4.20-reasoning` | `grok-4.20-beta-latest-reasoning`  
`grok-4.20-non-reasoning` | `grok-4.20-beta-latest-non-reasoning`  
  
## Fonctionnalités

Recherche web

Le fournisseur de recherche web `grok` intégré peut utiliser `XAI_API_KEY` ou une clé de recherche web du plugin :

bashCopy code
[code]
    openclaw config set tools.web.search.provider grok
[/code]

Génération de vidéos

Le plugin `xai` intégré enregistre la génération de vidéos via l’outil partagé `video_generate`.

  * Modèle vidéo par défaut : `xai/grok-imagine-video`
  * Modes : texte vers vidéo, image vers vidéo, génération d’image de référence, modification de vidéo distante et extension de vidéo distante
  * Formats d’image : `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`
  * Résolutions : `480P`, `720P`
  * Durée : 1 à 15 secondes pour la génération/image vers vidéo, 1 à 10 secondes lors de l’utilisation de rôles `reference_image`, 2 à 10 secondes pour l’extension
  * Génération par image de référence : définissez `imageRoles` sur `reference_image` pour chaque image fournie ; xAI accepte jusqu’à 7 images de ce type


Pour utiliser xAI comme fournisseur vidéo par défaut :

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "xai/grok-imagine-video",      },    },  },}
[/code]

Génération d’images

Le plugin `xai` intégré enregistre la génération d’images via l’outil partagé `image_generate`.

  * Modèle d’image par défaut : `xai/grok-imagine-image`
  * Modèle supplémentaire : `xai/grok-imagine-image-pro`
  * Modes : texte vers image et modification avec image de référence
  * Entrées de référence : une `image` ou jusqu’à cinq `images`
  * Formats d’image : `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `2:3`, `3:2`
  * Résolutions : `1K`, `2K`
  * Nombre : jusqu’à 4 images


OpenClaw demande à xAI des réponses d’image `b64_json` afin que les médias générés puissent être stockés et distribués via le chemin normal des pièces jointes de canal. Les images de référence locales sont converties en URL de données ; les références `http(s)` distantes sont transmises telles quelles.

Pour utiliser xAI comme fournisseur d’images par défaut :

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "xai/grok-imagine-image",      },    },  },}
[/code]

Synthèse vocale

Le plugin `xai` intégré enregistre la synthèse vocale via la surface de fournisseur partagée `tts`.

  * Voix : `eve`, `ara`, `rex`, `sal`, `leo`, `una`
  * Voix par défaut : `eve`
  * Formats : `mp3`, `wav`, `pcm`, `mulaw`, `alaw`
  * Langue : code BCP-47 ou `auto`
  * Vitesse : remplacement de vitesse natif au fournisseur
  * Le format natif de note vocale Opus n’est pas pris en charge


Pour utiliser xAI comme fournisseur TTS par défaut :

json5Copy code
[code]
    {  messages: {    tts: {      provider: "xai",      providers: {        xai: {          voiceId: "eve",        },      },    },  },}
[/code]

Reconnaissance vocale

Le plugin `xai` intégré enregistre la reconnaissance vocale par lot via la surface de transcription de compréhension multimédia d’OpenClaw.

  * Modèle par défaut : `grok-stt`
  * Point de terminaison : REST xAI `/v1/stt`
  * Chemin d’entrée : téléversement de fichier audio multipart
  * Pris en charge par OpenClaw partout où la transcription audio entrante utilise `tools.media.audio`, y compris les segments de canal vocal Discord et les pièces jointes audio de canal


Pour forcer xAI pour la transcription audio entrante :

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [          {            type: "provider",            provider: "xai",            model: "grok-stt",          },        ],      },    },  },}
[/code]

La langue peut être fournie via la configuration multimédia audio partagée ou par requête de transcription individuelle. Les indications de prompt sont acceptées par la surface OpenClaw partagée, mais l’intégration STT REST xAI ne transmet que le fichier, le modèle et la langue, car ceux-ci correspondent proprement au point de terminaison xAI public actuel.

Reconnaissance vocale en streaming

Le plugin `xai` intégré enregistre également un fournisseur de transcription en temps réel pour l’audio des appels vocaux en direct.

  * Point de terminaison : WebSocket xAI `wss://api.x.ai/v1/stt`
  * Encodage par défaut : `mulaw`
  * Fréquence d’échantillonnage par défaut : `8000`
  * Détection de fin de parole par défaut : `800ms`
  * Transcriptions intermédiaires : activées par défaut


Le flux multimédia Twilio de Voice Call envoie des trames audio G.711 µ-law, donc le fournisseur xAI peut transmettre ces trames directement sans transcodage :

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "xai",            providers: {              xai: {                apiKey: "${XAI_API_KEY}",                endpointingMs: 800,                language: "en",              },            },          },        },      },    },  },}
[/code]

La configuration détenue par le fournisseur se trouve sous `plugins.entries.voice-call.config.streaming.providers.xai`. Les clés prises en charge sont `apiKey`, `baseUrl`, `sampleRate`, `encoding` (`pcm`, `mulaw` ou `alaw`), `interimResults`, `endpointingMs` et `language`.

Configuration de x_search

Le Plugin xAI intégré expose `x_search` comme outil OpenClaw pour rechercher du contenu X (anciennement Twitter) via Grok.

Chemin de configuration : `plugins.entries.xai.config.xSearch`

Clé | Type | Valeur par défaut | Description  
---|---|---|---  
`enabled` | boolean | - | Activer ou désactiver x_search  
`model` | string | `grok-4-1-fast` | Modèle utilisé pour les requêtes x_search  
`baseUrl` | string | - | Remplacement de l’URL de base xAI Responses  
`inlineCitations` | boolean | - | Inclure des citations en ligne dans les résultats  
`maxTurns` | number | - | Nombre maximal de tours de conversation  
`timeoutSeconds` | number | - | Délai d’expiration de la requête en secondes  
`cacheTtlMinutes` | number | - | Durée de vie du cache en minutes  
json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          xSearch: {            enabled: true,            model: "grok-4-1-fast",            baseUrl: "https://api.x.ai/v1",            inlineCitations: true,          },        },      },    },  },}
[/code]

Configuration de l’exécution de code

Le Plugin xAI intégré expose `code_execution` comme outil OpenClaw pour l’exécution de code à distance dans l’environnement sandbox de xAI.

Chemin de configuration : `plugins.entries.xai.config.codeExecution`

Clé | Type | Valeur par défaut | Description  
---|---|---|---  
`enabled` | boolean | `true` (si clé disponible) | Activer ou désactiver l’exécution de code  
`model` | string | `grok-4-1-fast` | Modèle utilisé pour les requêtes d’exécution de code  
`maxTurns` | number | - | Nombre maximal de tours de conversation  
`timeoutSeconds` | number | - | Délai d’expiration de la requête en secondes  
json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast",          },        },      },    },  },}
[/code]

Limites connues

  * L’authentification se fait uniquement par clé d’API aujourd’hui. La clé d’API peut être stockée dans un profil d’authentification xAI, une variable d’environnement ou la configuration du Plugin ; il n’existe pas encore de flux OAuth xAI ni de flux par code d’appareil dans OpenClaw.
  * `grok-4.20-multi-agent-experimental-beta-0304` n’est pas pris en charge sur le chemin normal du fournisseur xAI, car il nécessite une surface d’API amont différente du transport xAI OpenClaw standard.
  * La voix xAI Realtime n’est pas encore enregistrée comme fournisseur OpenClaw. Elle nécessite un contrat de session vocale bidirectionnelle différent de la STT par lot ou de la transcription en streaming.
  * Les paramètres d’image xAI `quality`, `mask` d’image et les formats d’image supplémentaires uniquement natifs ne sont pas exposés tant que l’outil partagé `image_generate` ne dispose pas des contrôles multifournisseurs correspondants.

Notes avancées

  * OpenClaw applique automatiquement les correctifs de compatibilité propres à xAI pour les schémas d’outils et les appels d’outils sur le chemin du runner partagé.
  * Les requêtes xAI natives utilisent `tool_stream: true` par défaut. Définissez `agents.defaults.models["xai/<model>"].params.tool_stream` sur `false` pour le désactiver.
  * Le wrapper xAI intégré supprime les indicateurs de schéma d’outils stricts non pris en charge et les clés de charge utile de raisonnement avant d’envoyer les requêtes xAI natives.
  * `web_search`, `x_search` et `code_execution` sont exposés comme outils OpenClaw. OpenClaw active l’outil intégré xAI précis dont il a besoin dans chaque requête d’outil au lieu d’attacher tous les outils natifs à chaque tour de chat.
  * Grok `web_search` lit `plugins.entries.xai.config.webSearch.baseUrl`. `x_search` lit `plugins.entries.xai.config.xSearch.baseUrl`, puis revient à l’URL de base de la recherche web Grok.
  * `x_search` et `code_execution` appartiennent au Plugin xAI intégré plutôt que d’être codés en dur dans le runtime du modèle principal.
  * `code_execution` correspond à l’exécution à distance dans la sandbox xAI, et non à [`exec`](</fr/tools/exec>) local.


## Tests live

Les chemins média xAI sont couverts par des tests unitaires et des suites live à activation explicite. Les commandes live chargent les secrets depuis votre shell de connexion, y compris `~/.profile`, avant de sonder `XAI_API_KEY`.

bashCopy code
[code]
    pnpm test extensions/xaiOPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_TEST_QUIET=1 pnpm test:live -- extensions/xai/xai.live.test.tsOPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_TEST_QUIET=1 OPENCLAW_LIVE_IMAGE_GENERATION_PROVIDERS=xai pnpm test:live -- test/image-generation.runtime.live.test.ts
[/code]

Le fichier live propre au fournisseur synthétise du TTS normal, du TTS PCM adapté à la téléphonie, transcrit l’audio via la STT par lot xAI, diffuse le même PCM via la STT en temps réel xAI, génère une sortie texte-vers-image et modifie une image de référence. Le fichier live d’image partagé vérifie le même fournisseur xAI via la sélection de runtime, le fallback, la normalisation et le chemin des pièces jointes média d’OpenClaw.

## Associé

[**Sélection de modèle** Choisir les fournisseurs, les références de modèle et le comportement de basculement. ](</fr/concepts/model-providers>) [**Génération vidéo** Paramètres de l’outil vidéo partagé et sélection du fournisseur. ](</fr/tools/video-generation>) [**Tous les fournisseurs** La vue d’ensemble plus large des fournisseurs. ](</fr/providers>) [**Dépannage** Problèmes courants et correctifs. ](</fr/help/troubleshooting>)

Was this useful?YesNo