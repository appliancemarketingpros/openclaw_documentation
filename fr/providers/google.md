---
title: Google (Gemini)
source_url: https://docs.openclaw.ai/fr/providers/google
scraped_at: 2026-05-25
---

Le Plugin Google donne accès aux modèles Gemini via Google AI Studio, ainsi qu’à la génération d’images, à la compréhension des médias (image/audio/vidéo), à la synthèse vocale et à la recherche web via Gemini Grounding.

  * Fournisseur : `google`
  * Authentification : `GEMINI_API_KEY` ou `GOOGLE_API_KEY`
  * API : API Google Gemini
  * Option d’exécution : provider/model `agentRuntime.id: "google-gemini-cli"` réutilise l’OAuth de Gemini CLI tout en conservant les références de modèle canoniques sous la forme `google/*`.


## Bien démarrer

Choisissez votre méthode d’authentification préférée et suivez les étapes de configuration.

### API key

**Idéal pour :** un accès standard à l’API Gemini via Google AI Studio.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice gemini-api-key
[/code]

Ou transmettez directement la clé :

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY"
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "google/gemini-3.1-pro-preview" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider google
[/code]

### Gemini CLI (OAuth)

**Idéal pour :** réutiliser une connexion Gemini CLI existante via PKCE OAuth au lieu d’une clé d’API séparée.

* ### Install the Gemini CLI

La commande locale `gemini` doit être disponible dans `PATH`.

bashCopy code
[code]
    # Homebrewbrew install gemini-cli # or npmnpm install -g @google/gemini-cli
[/code]

OpenClaw prend en charge les installations Homebrew et les installations npm globales, y compris les dispositions Windows/npm courantes.

* ### Log in via OAuth

bashCopy code
[code]
    openclaw models auth login --provider google-gemini-cli --set-default
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider google
[/code]

  * Modèle par défaut : `google/gemini-3.1-pro-preview`
  * Exécution : `google-gemini-cli`
  * Alias : `gemini-cli`


L’identifiant de modèle Gemini API de Gemini 3.1 Pro est `gemini-3.1-pro-preview`. OpenClaw accepte le raccourci `google/gemini-3.1-pro` comme alias pratique et le normalise avant les appels au fournisseur.

**Variables d’environnement :**

  * `OPENCLAW_GEMINI_OAUTH_CLIENT_ID`
  * `OPENCLAW_GEMINI_OAUTH_CLIENT_SECRET`


(Ou les variantes `GEMINI_CLI_*`.)

Les références de modèle `google-gemini-cli/*` sont des alias de compatibilité hérités. Les nouvelles configurations doivent utiliser des références de modèle `google/*` ainsi que le runtime `google-gemini-cli` lorsqu’elles veulent une exécution locale avec Gemini CLI.

## Capacités

Capacité | Pris en charge  
---|---  
Complétions de chat | Oui  
Génération d’images | Oui  
Génération de musique | Oui  
Synthèse vocale | Oui  
Voix en temps réel | Oui (Google Live API)  
Compréhension d’images | Oui  
Transcription audio | Oui  
Compréhension vidéo | Oui  
Recherche web (Grounding) | Oui  
Réflexion/raisonnement | Oui (Gemini 2.5+ / Gemini 3+)  
Modèles Gemma 4 | Oui  
  
## Recherche web

Le fournisseur de recherche web `gemini` intégré utilise l’ancrage Google Search de Gemini. Configurez une clé de recherche dédiée sous `plugins.entries.google.config.webSearch`, ou laissez-le réutiliser `models.providers.google.apiKey` après `GEMINI_API_KEY` :

json5Copy code
[code]
    {  plugins: {    entries: {      google: {        config: {          webSearch: {            apiKey: "AIza...", // optional if GEMINI_API_KEY or models.providers.google.apiKey is set            baseUrl: "https://generativelanguage.googleapis.com/v1beta", // falls back to models.providers.google.baseUrl            model: "gemini-2.5-flash",          },        },      },    },  },}
[/code]

L’ordre de priorité des identifiants est `webSearch.apiKey` dédié, puis `GEMINI_API_KEY`, puis `models.providers.google.apiKey`. `webSearch.baseUrl` est facultatif et existe pour les proxys d’opérateur ou les points de terminaison compatibles avec l’API Gemini ; lorsqu’il est omis, la recherche web Gemini réutilise `models.providers.google.baseUrl`. Consultez [Recherche Gemini](</fr/tools/gemini-search>) pour le comportement de l’outil propre au fournisseur.

## Génération d’images

Le fournisseur de génération d’images `google` intégré utilise par défaut `google/gemini-3.1-flash-image-preview`.

  * Prend aussi en charge `google/gemini-3-pro-image-preview`
  * Génération : jusqu’à 4 images par requête
  * Mode édition : activé, jusqu’à 5 images d’entrée
  * Contrôles de géométrie : `size`, `aspectRatio` et `resolution`


Pour utiliser Google comme fournisseur d’images par défaut :

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

## Génération vidéo

Le Plugin `google` intégré enregistre également la génération vidéo via l’outil partagé `video_generate`.

  * Modèle vidéo par défaut : `google/veo-3.1-fast-generate-preview`
  * Modes : texte vers vidéo, image vers vidéo et flux de référence à vidéo unique
  * Prend en charge `aspectRatio` (`16:9`, `9:16`) et `resolution` (`720P`, `1080P`) ; la sortie audio n’est pas prise en charge par Veo aujourd’hui
  * Durées prises en charge : **4, 6 ou 8 secondes** (les autres valeurs sont ramenées à la valeur autorisée la plus proche)


Pour utiliser Google comme fournisseur vidéo par défaut :

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",      },    },  },}
[/code]

## Génération de musique

Le Plugin `google` intégré enregistre également la génération de musique via l’outil partagé `music_generate`.

  * Modèle musical par défaut : `google/lyria-3-clip-preview`
  * Prend aussi en charge `google/lyria-3-pro-preview`
  * Contrôles de prompt : `lyrics` et `instrumental`
  * Format de sortie : `mp3` par défaut, plus `wav` sur `google/lyria-3-pro-preview`
  * Entrées de référence : jusqu’à 10 images
  * Les exécutions adossées à une session se détachent via le flux partagé de tâche/statut, y compris `action: "status"`


Pour utiliser Google comme fournisseur de musique par défaut :

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

## Synthèse vocale

Le fournisseur vocal `google` intégré utilise le chemin TTS de l’API Gemini avec `gemini-3.1-flash-tts-preview`.

  * Voix par défaut : `Kore`
  * Authentification : `messages.tts.providers.google.apiKey`, `models.providers.google.apiKey`, `GEMINI_API_KEY` ou `GOOGLE_API_KEY`
  * Sortie : WAV pour les pièces jointes TTS classiques, Opus pour les cibles de notes vocales, PCM pour Talk/téléphonie
  * Sortie de note vocale : le PCM Google est enveloppé en WAV et transcodé en Opus 48 kHz avec `ffmpeg`


Le chemin Gemini TTS par lots de Google renvoie l’audio généré dans la réponse `generateContent` terminée. Pour les conversations parlées à latence minimale, utilisez le fournisseur de voix en temps réel Google adossé à l’API Gemini Live plutôt que la TTS par lots.

Pour utiliser Google comme fournisseur TTS par défaut :

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "google",      providers: {        google: {          model: "gemini-3.1-flash-tts-preview",          voiceName: "Kore",          audioProfile: "Speak professionally with a calm tone.",        },      },    },  },}
[/code]

Gemini API TTS utilise des prompts en langage naturel pour contrôler le style. Définissez `audioProfile` pour préfixer le texte prononcé avec un prompt de style réutilisable. Définissez `speakerName` lorsque le texte de votre prompt fait référence à un locuteur nommé.

Gemini API TTS accepte également des balises audio expressives entre crochets dans le texte, comme `[whispers]` ou `[laughs]`. Pour éviter que les balises n’apparaissent dans la réponse de chat visible tout en les envoyant à TTS, placez-les dans un bloc `[[tts:text]]...[[/tts:text]]` :

textCopy code
[code]
    Here is the clean reply text. [[tts:text]][whispers] Here is the spoken version.[[/tts:text]]
[/code]

## Voix en temps réel

Le Plugin `google` intégré enregistre un fournisseur de voix en temps réel adossé à l’API Gemini Live pour les ponts audio backend tels que Voice Call et Google Meet.

Paramètre | Chemin de configuration | Par défaut  
---|---|---  
Modèle | `plugins.entries.voice-call.config.realtime.providers.google.model` | `gemini-2.5-flash-native-audio-preview-12-2025`  
Voix | `...google.voice` | `Kore`  
Température | `...google.temperature` | (non défini)  
Sensibilité de début VAD | `...google.startSensitivity` | (non défini)  
Sensibilité de fin VAD | `...google.endSensitivity` | (non défini)  
Durée de silence | `...google.silenceDurationMs` | (non défini)  
Gestion de l’activité | `...google.activityHandling` | Valeur par défaut de Google, `start-of-activity-interrupts`  
Couverture du tour | `...google.turnCoverage` | Valeur par défaut de Google, `only-activity`  
Désactiver le VAD automatique | `...google.automaticActivityDetectionDisabled` | `false`  
Reprise de session | `...google.sessionResumption` | `true`  
Compression du contexte | `...google.contextWindowCompression` | `true`  
Clé d’API | `...google.apiKey` | Se rabat sur `models.providers.google.apiKey`, `GEMINI_API_KEY` ou `GOOGLE_API_KEY`  
  
Exemple de configuration realtime pour Voice Call :

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          realtime: {            enabled: true,            provider: "google",            providers: {              google: {                model: "gemini-2.5-flash-native-audio-preview-12-2025",                voice: "Kore",                activityHandling: "start-of-activity-interrupts",                turnCoverage: "only-activity",              },            },          },        },      },    },  },}
[/code]

Pour la vérification live par les mainteneurs, exécutez `OPENAI_API_KEY=... GEMINI_API_KEY=... node --import tsx scripts/dev/realtime-talk-live-smoke.ts`. Le smoke couvre également les chemins backend/WebRTC OpenAI ; la partie Google émet la même forme de jeton Live API contraint que celle utilisée par Control UI Talk, ouvre le point de terminaison WebSocket du navigateur, envoie la charge utile de configuration initiale et attend `setupComplete`.

## Configuration avancée

Réutilisation directe du cache Gemini

Pour les exécutions directes de l’API Gemini (`api: "google-generative-ai"`), OpenClaw transmet un handle `cachedContent` configuré aux requêtes Gemini.

  * Configurez les paramètres par modèle ou globaux avec `cachedContent` ou l’ancien `cached_content`
  * Si les deux sont présents, `cachedContent` l’emporte
  * Exemple de valeur : `cachedContents/prebuilt-context`
  * L’utilisation des cache hits Gemini est normalisée dans `cacheRead` OpenClaw depuis `cachedContentTokenCount` en amont

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "google/gemini-2.5-pro": {          params: {            cachedContent: "cachedContents/prebuilt-context",          },        },      },    },  },}
[/code]

Notes d’utilisation JSON de Gemini CLI

Lors de l’utilisation du fournisseur OAuth `google-gemini-cli`, OpenClaw normalise la sortie JSON de la CLI comme suit :

  * Le texte de réponse provient du champ `response` du JSON de la CLI.
  * L’utilisation se rabat sur `stats` lorsque la CLI laisse `usage` vide.
  * `stats.cached` est normalisé dans `cacheRead` OpenClaw.
  * Si `stats.input` est absent, OpenClaw déduit les jetons d’entrée depuis `stats.input_tokens - stats.cached`.

Configuration de l’environnement et du démon

Si le Gateway s’exécute comme un démon (launchd/systemd), assurez-vous que `GEMINI_API_KEY` est disponible pour ce processus (par exemple dans `~/.openclaw/.env` ou via `env.shellEnv`).

## Connexe

[**Sélection de modèle** Choix des fournisseurs, des références de modèle et du comportement de basculement. ](</fr/concepts/model-providers>) [**Génération d’images** Paramètres d’outil d’image partagés et sélection du fournisseur. ](</fr/tools/image-generation>) [**Génération de vidéos** Paramètres d’outil vidéo partagés et sélection du fournisseur. ](</fr/tools/video-generation>) [**Génération de musique** Paramètres d’outil de musique partagés et sélection du fournisseur. ](</fr/tools/music-generation>)

Was this useful?YesNo