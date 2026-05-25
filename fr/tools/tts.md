---
title: Synthèse vocale
source_url: https://docs.openclaw.ai/fr/tools/tts
scraped_at: 2026-05-25
---

OpenClaw peut convertir les réponses sortantes en audio avec **14 fournisseurs de synthèse vocale** et livrer des messages vocaux natifs sur Feishu, Matrix, Telegram et WhatsApp, des pièces jointes audio partout ailleurs, ainsi que des flux PCM/Ulaw pour la téléphonie et Talk.

Le TTS est la moitié de sortie vocale du mode `stt-tts` de Talk. Les sessions Talk `realtime` natives du fournisseur synthétisent la parole dans le fournisseur temps réel au lieu d’appeler ce chemin TTS, tandis que les sessions `transcription` ne synthétisent pas de réponse vocale de l’assistant.

## Démarrage rapide

* ### Pick a provider

OpenAI et ElevenLabs sont les options hébergées les plus fiables. Microsoft et Local CLI fonctionnent sans clé API. Consultez la matrice des fournisseurs pour la liste complète.

* ### Set the API key

Exportez la variable d’environnement de votre fournisseur (par exemple `OPENAI_API_KEY`, `ELEVENLABS_API_KEY`). Microsoft et Local CLI n’ont pas besoin de clé.

* ### Enable in config

Définissez `messages.tts.auto: "always"` et `messages.tts.provider` :

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",    },  },}
[/code]

* ### Try it in chat

`/tts status` affiche l’état actuel. `/tts audio Hello from OpenClaw` envoie une réponse audio ponctuelle.

## Fournisseurs pris en charge

Fournisseur | Auth | Notes  
---|---|---  
**Azure Speech** | `AZURE_SPEECH_KEY` \+ `AZURE_SPEECH_REGION` (aussi `AZURE_SPEECH_API_KEY`, `SPEECH_KEY`, `SPEECH_REGION`) | Sortie native de note vocale Ogg/Opus et téléphonie.  
**DeepInfra** | `DEEPINFRA_API_KEY` | TTS compatible OpenAI. Par défaut, `hexgrad/Kokoro-82M`.  
**ElevenLabs** | `ELEVENLABS_API_KEY` ou `XI_API_KEY` | Clonage vocal, multilingue, déterministe via `seed` ; diffusé en streaming pour la lecture vocale Discord.  
**Google Gemini** | `GEMINI_API_KEY` ou `GOOGLE_API_KEY` | TTS par lot de l’API Gemini ; tient compte de la persona via `promptTemplate: "audio-profile-v1"`.  
**Gradium** | `GRADIUM_API_KEY` | Sortie de note vocale et de téléphonie.  
**Inworld** | `INWORLD_API_KEY` | API TTS en streaming. Note vocale Opus native et téléphonie PCM.  
**Local CLI** | aucune | Exécute une commande TTS locale configurée.  
**Microsoft** | aucune | TTS neuronal public Edge via `node-edge-tts`. Au mieux, sans SLA.  
**MiniMax** | `MINIMAX_API_KEY` (ou Token Plan : `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY`, `MINIMAX_CODING_API_KEY`) | API T2A v2. Par défaut, `speech-2.8-hd`.  
**OpenAI** | `OPENAI_API_KEY` | Également utilisé pour le résumé automatique ; prend en charge les `instructions` de persona.  
**OpenRouter** | `OPENROUTER_API_KEY` (peut réutiliser `models.providers.openrouter.apiKey`) | Modèle par défaut `hexgrad/kokoro-82m`.  
**Volcengine** | `VOLCENGINE_TTS_API_KEY` ou `BYTEPLUS_SEED_SPEECH_API_KEY` (AppID/jeton hérité : `VOLCENGINE_TTS_APPID`/`_TOKEN`) | API HTTP BytePlus Seed Speech.  
**Vydra** | `VYDRA_API_KEY` | Fournisseur partagé d’images, de vidéos et de parole.  
**xAI** | `XAI_API_KEY` | TTS par lot xAI. La note vocale Opus native n’est **pas** prise en charge.  
**Xiaomi MiMo** | `XIAOMI_API_KEY` | TTS MiMo via les complétions de chat Xiaomi.  
  
Si plusieurs fournisseurs sont configurés, celui qui est sélectionné est utilisé en premier et les autres servent d’options de repli. Le résumé automatique utilise `summaryModel` (ou `agents.defaults.model.primary`) ; ce fournisseur doit donc également être authentifié si vous conservez les résumés activés.

## Configuration

La configuration TTS se trouve sous `messages.tts` dans `~/.openclaw/openclaw.json`. Choisissez un préréglage et adaptez le bloc du fournisseur :

### Azure Speech

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "azure-speech",  providers: {    "azure-speech": {      apiKey: "${AZURE_SPEECH_KEY}",      region: "eastus",      voice: "en-US-JennyNeural",      lang: "en-US",      outputFormat: "audio-24khz-48kbitrate-mono-mp3",      voiceNoteOutputFormat: "ogg-24khz-16bit-mono-opus",    },  },},},}
[/code]

### ElevenLabs

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "elevenlabs",  providers: {    elevenlabs: {      apiKey: "${ELEVENLABS_API_KEY}",      model: "eleven_multilingual_v2",      voiceId: "EXAVITQu4vr4xnSDxMaL",    },  },},},}
[/code]

### Google Gemini

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "google",  providers: {    google: {      apiKey: "${GEMINI_API_KEY}",      model: "gemini-3.1-flash-tts-preview",      voiceName: "Kore",      // Optional natural-language style prompts:      // audioProfile: "Speak in a calm, podcast-host tone.",      // speakerName: "Alex",    },  },},},}
[/code]

### Gradium

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "gradium",  providers: {    gradium: {      apiKey: "${GRADIUM_API_KEY}",      voiceId: "YTpq7expH9539ERJ",    },  },},},}
[/code]

### Inworld

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "inworld",  providers: {    inworld: {      apiKey: "${INWORLD_API_KEY}",      modelId: "inworld-tts-1.5-max",      voiceId: "Sarah",      temperature: 0.7,    },  },},},}
[/code]

### Local CLI

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "tts-local-cli",  providers: {    "tts-local-cli": {      command: "say",      args: ["-o", "{{OutputPath}}", "{{Text}}"],      outputFormat: "wav",      timeoutMs: 120000,    },  },},},}
[/code]

### Microsoft (no key)

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "microsoft",  providers: {    microsoft: {      enabled: true,      voice: "en-US-MichelleNeural",      lang: "en-US",      outputFormat: "audio-24khz-48kbitrate-mono-mp3",      rate: "+0%",      pitch: "+0%",    },  },},},}
[/code]

### MiniMax

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "minimax",  providers: {    minimax: {      apiKey: "${MINIMAX_API_KEY}",      model: "speech-2.8-hd",      voiceId: "English_expressive_narrator",      speed: 1.0,      vol: 1.0,      pitch: 0,    },  },},},}
[/code]

### OpenAI + ElevenLabs

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "openai",  summaryModel: "openai/gpt-4.1-mini",  modelOverrides: { enabled: true },  providers: {    openai: {      apiKey: "${OPENAI_API_KEY}",      model: "gpt-4o-mini-tts",      voice: "alloy",    },    elevenlabs: {      apiKey: "${ELEVENLABS_API_KEY}",      model: "eleven_multilingual_v2",      voiceId: "EXAVITQu4vr4xnSDxMaL",      voiceSettings: { stability: 0.5, similarityBoost: 0.75, style: 0.0, useSpeakerBoost: true, speed: 1.0 },      applyTextNormalization: "auto",      languageCode: "en",    },  },},},}
[/code]

### OpenRouter

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "openrouter",  providers: {    openrouter: {      apiKey: "${OPENROUTER_API_KEY}",      model: "hexgrad/kokoro-82m",      voice: "af_alloy",      responseFormat: "mp3",    },  },},},}
[/code]

### Volcengine

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "volcengine",  providers: {    volcengine: {      apiKey: "${VOLCENGINE_TTS_API_KEY}",      resourceId: "seed-tts-1.0",      voice: "en_female_anna_mars_bigtts",    },  },},},}
[/code]

### xAI

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "xai",  providers: {    xai: {      apiKey: "${XAI_API_KEY}",      voiceId: "eve",      language: "en",      responseFormat: "mp3",    },  },},},}
[/code]

### Xiaomi MiMo

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "xiaomi",  providers: {    xiaomi: {      apiKey: "${XIAOMI_API_KEY}",      model: "mimo-v2.5-tts",      voice: "mimo_default",      format: "mp3",    },  },},},}
[/code]

### Remplacements de voix par agent

Utilisez `agents.list[].tts` lorsqu’un agent doit parler avec un autre fournisseur, une autre voix, un autre modèle, une autre persona ou un autre mode Auto-TTS. Le bloc de l’agent fusionne en profondeur avec `messages.tts`, ce qui permet de conserver les identifiants du fournisseur dans la configuration globale du fournisseur :

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",      providers: {        elevenlabs: { apiKey: "${ELEVENLABS_API_KEY}", model: "eleven_multilingual_v2" },      },    },  },  agents: {    list: [      {        id: "reader",        tts: {          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL" },          },        },      },    ],  },}
[/code]

Pour épingler une persona par agent, définissez `agents.list[].tts.persona` avec la configuration du fournisseur — cela remplace le `messages.tts.persona` global uniquement pour cet agent.

Ordre de priorité pour les réponses automatiques, `/tts audio`, `/tts status` et l’outil d’agent `tts` :

  1. `messages.tts`
  2. `agents.list[].tts` actif
  3. remplacement de canal, lorsque le canal prend en charge `channels.<channel>.tts`
  4. remplacement de compte, lorsque le canal transmet `channels.<channel>.accounts.<id>.tts`
  5. préférences locales `/tts` pour cet hôte
  6. directives intégrées `[[tts:...]]` lorsque les remplacements pilotés par le modèle sont activés


Les remplacements de canal et de compte utilisent la même forme que `messages.tts` et fusionnent en profondeur par-dessus les couches précédentes, afin que les identifiants partagés du fournisseur puissent rester dans `messages.tts` tandis qu’un canal ou un compte de bot modifie uniquement la voix, le modèle, la persona ou le mode automatique :

json5Copy code
[code]
    {  messages: {    tts: {      provider: "openai",      providers: {        openai: { apiKey: "${OPENAI_API_KEY}", model: "gpt-4o-mini-tts" },      },    },  },  channels: {    feishu: {      accounts: {        english: {          tts: {            providers: {              openai: { voice: "shimmer" },            },          },        },      },    },  },}
[/code]

## Personas

Une **persona** est une identité vocale stable qui peut être appliquée de façon déterministe entre fournisseurs. Elle peut privilégier un fournisseur, définir une intention d’invite indépendante du fournisseur, et transporter des liaisons propres aux fournisseurs pour les voix, les modèles, les modèles d’invite, les graines et les paramètres vocaux.

### Persona minimale

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "narrator",      personas: {        narrator: {          label: "Narrator",          provider: "elevenlabs",          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL", modelId: "eleven_multilingual_v2" },          },        },      },    },  },}
[/code]

### Persona complète (invite indépendante du fournisseur)

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "alfred",      personas: {        alfred: {          label: "Alfred",          description: "Dry, warm British butler narrator.",          provider: "google",          fallbackPolicy: "preserve-persona",          prompt: {            profile: "A brilliant British butler. Dry, witty, warm, charming, emotionally expressive, never generic.",            scene: "A quiet late-night study. Close-mic narration for a trusted operator.",            sampleContext: "The speaker is answering a private technical request with concise confidence and dry warmth.",            style: "Refined, understated, lightly amused.",            accent: "British English.",            pacing: "Measured, with short dramatic pauses.",            constraints: ["Do not read configuration values aloud.", "Do not explain the persona."],          },          providers: {            google: {              model: "gemini-3.1-flash-tts-preview",              voiceName: "Algieba",              promptTemplate: "audio-profile-v1",            },            openai: { model: "gpt-4o-mini-tts", voice: "cedar" },            elevenlabs: {              voiceId: "voice_id",              modelId: "eleven_multilingual_v2",              seed: 42,              voiceSettings: {                stability: 0.65,                similarityBoost: 0.8,                style: 0.25,                useSpeakerBoost: true,                speed: 0.95,              },            },          },        },      },    },  },}
[/code]

### Résolution de la persona

La persona active est sélectionnée de façon déterministe :

  1. Préférence locale `/tts persona <id>`, si elle est définie.
  2. `messages.tts.persona`, si elle est définie.
  3. Aucune persona.


La sélection du fournisseur applique d’abord les réglages explicites :

  1. Remplacements directs (CLI, Gateway, Talk, directives TTS autorisées).
  2. Préférence locale `/tts provider <id>`.
  3. `provider` de la persona active.
  4. `messages.tts.provider`.
  5. Sélection automatique du registre.


Pour chaque tentative de fournisseur, OpenClaw fusionne les configurations dans cet ordre :

  1. `messages.tts.providers.<id>`
  2. `messages.tts.personas.<persona>.providers.<id>`
  3. Remplacements de requête approuvés
  4. Remplacements de directives TTS émises par le modèle et autorisées


### Utilisation des invites de persona par les fournisseurs

Les champs d’invite de persona (`profile`, `scene`, `sampleContext`, `style`, `accent`, `pacing`, `constraints`) sont **indépendants du fournisseur**. Chaque fournisseur décide comment les utiliser :

Google Gemini

Encapsule les champs d’invite de persona dans une structure d’invite TTS Gemini **uniquement lorsque** la configuration effective du fournisseur Google définit `promptTemplate: "audio-profile-v1"` ou `personaPrompt`. Les anciens champs `audioProfile` et `speakerName` sont toujours préfixés comme texte d’invite propre à Google. Les balises audio intégrées telles que `[whispers]` ou `[laughs]` dans un bloc `[[tts:text]]` sont conservées dans la transcription Gemini ; OpenClaw ne génère pas ces balises.

OpenAI

Mappe les champs d’invite de persona vers le champ de requête `instructions` **uniquement lorsque** aucune `instructions` OpenAI explicite n’est configurée. Les `instructions` explicites sont toujours prioritaires.

Other providers

Utilisent uniquement les liaisons de persona propres au fournisseur sous `personas.<id>.providers.<provider>`. Les champs d’invite de persona sont ignorés, sauf si le fournisseur implémente son propre mappage d’invite de persona.

### Politique de repli

`fallbackPolicy` contrôle le comportement lorsqu’une persona n’a **aucune liaison** pour le fournisseur tenté :

Politique | Comportement  
---|---  
`preserve-persona` | **Par défaut.** Les champs d’invite indépendants du fournisseur restent disponibles ; le fournisseur peut les utiliser ou les ignorer.  
`provider-defaults` | La persona est omise de la préparation de l’invite pour cette tentative ; le fournisseur utilise ses valeurs par défaut neutres tandis que le repli vers d’autres fournisseurs continue.  
`fail` | Ignore cette tentative de fournisseur avec `reasonCode: "not_configured"` et `personaBinding: "missing"`. Les fournisseurs de repli sont quand même tentés.  
  
L’ensemble de la requête TTS échoue uniquement lorsque **chaque** fournisseur tenté est ignoré ou échoue.

La sélection de fournisseur pour une session Talk est limitée à la session. Un client Talk doit choisir les identifiants de fournisseur, de modèle, de voix et les locales depuis `talk.catalog` et les transmettre via la session Talk ou la requête de transfert. L’ouverture d’une session vocale ne doit pas modifier `messages.tts` ni les valeurs par défaut globales des fournisseurs Talk.

## Directives pilotées par le modèle

Par défaut, l’assistant **peut** émettre des directives `[[tts:...]]` pour remplacer la voix, le modèle ou la vitesse pour une seule réponse, ainsi qu’un bloc facultatif `[[tts:text]]...[[/tts:text]]` pour les indications expressives qui doivent apparaître uniquement dans l’audio :

textCopy code
[code]
    Here you go. [[tts:voiceId=pMsXgVXv3BLzUgSXRplE model=eleven_v3 speed=1.1]][[tts:text]](laughs) Read the song once more.[[/tts:text]]
[/code]

Lorsque `messages.tts.auto` vaut `"tagged"`, les **directives sont requises** pour déclencher l’audio. La diffusion de blocs en streaming retire les directives du texte visible avant que le canal ne les voie, même lorsqu’elles sont réparties sur des blocs adjacents.

`provider=...` est ignoré sauf si `modelOverrides.allowProvider: true`. Lorsqu’une réponse déclare `provider=...`, les autres clés de cette directive sont analysées uniquement par ce fournisseur ; les clés non prises en charge sont retirées et signalées comme avertissements de directive TTS.

**Clés de directive disponibles :**

  * `provider` (identifiant de fournisseur enregistré ; nécessite `allowProvider: true`)
  * `voice` / `voiceName` / `voice_name` / `google_voice` / `voiceId`
  * `model` / `google_model`
  * `stability`, `similarityBoost`, `style`, `speed`, `useSpeakerBoost`
  * `vol` / `volume` (volume MiniMax, 0–10)
  * `pitch` (hauteur entière MiniMax, −12 à 12 ; les valeurs fractionnaires sont tronquées)
  * `emotion` (balise d’émotion Volcengine)
  * `applyTextNormalization` (`auto|on|off`)
  * `languageCode` (ISO 639-1)
  * `seed`


**Désactiver entièrement les remplacements de modèle :**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: false } } } }
[/code]

**Autoriser le changement de fournisseur tout en gardant les autres réglages configurables :**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: true, allowProvider: true, allowSeed: false } } } }
[/code]

## Commandes slash

Commande unique `/tts`. Sur Discord, OpenClaw enregistre aussi `/voice`, car `/tts` est une commande Discord intégrée — le texte `/tts ...` fonctionne toujours.

textCopy code
[code]
    /tts off | on | status/tts chat on | off | default/tts latest/tts provider <id>/tts persona <id> | off/tts limit <chars>/tts summary off/tts audio <text>
[/code]

Notes de comportement :

  * `/tts on` écrit la préférence TTS locale sur `always` ; `/tts off` l’écrit sur `off`.
  * `/tts chat on|off|default` écrit un remplacement auto-TTS limité à la session pour le chat courant.
  * `/tts persona <id>` écrit la préférence locale de persona ; `/tts persona off` l’efface.
  * `/tts latest` lit la dernière réponse de l’assistant dans la transcription de la session courante et l’envoie une fois en audio. Elle stocke uniquement un hachage de cette réponse dans l’entrée de session afin de supprimer les envois vocaux en double.
  * `/tts audio` génère une réponse audio ponctuelle (n’active **pas** TTS).
  * `limit` et `summary` sont stockés dans les **préférences locales** , pas dans la configuration principale.
  * `/tts status` inclut les diagnostics de repli pour la dernière tentative — `Fallback: <primary> -> <used>`, `Attempts: ...`, et les détails par tentative (`provider:outcome(reasonCode) latency`).
  * `/status` affiche le mode TTS actif ainsi que le fournisseur, le modèle, la voix et les métadonnées de point de terminaison personnalisé nettoyées configurés lorsque TTS est activé.


## Préférences par utilisateur

Les commandes slash écrivent les remplacements locaux dans `prefsPath`. La valeur par défaut est `~/.openclaw/settings/tts.json` ; remplacez-la avec la variable d’environnement `OPENCLAW_TTS_PREFS` ou `messages.tts.prefsPath`.

Champ stocké | Effet  
---|---  
`auto` | Remplacement auto-TTS local (`always`, `off`, …)  
`provider` | Remplacement local du fournisseur principal  
`persona` | Remplacement local de persona  
`maxLength` | Seuil de résumé (`1500` caractères par défaut)  
`summarize` | Bascule de résumé (`true` par défaut)  
  
Ceux-ci remplacent la configuration effective issue de `messages.tts` plus le bloc `agents.list[].tts` actif pour cet hôte.

## Formats de sortie (fixes)

La diffusion vocale TTS est pilotée par les capacités du canal. Les plugins de canal annoncent si le TTS de style vocal doit demander aux fournisseurs une cible native `voice-note` ou conserver la synthèse `audio-file` normale et uniquement marquer la sortie compatible pour la diffusion vocale.

  * **Canaux compatibles avec les notes vocales** : les réponses sous forme de note vocale privilégient Opus (`opus_48000_64` depuis ElevenLabs, `opus` depuis OpenAI). 
    * 48 kHz / 64 kbps constitue un bon compromis pour les messages vocaux.
  * **Feishu / WhatsApp** : lorsqu’une réponse sous forme de note vocale est produite en MP3/WebM/WAV/M4A ou dans un autre fichier probablement audio, le plugin de canal la transcode en Ogg/Opus 48 kHz avec `ffmpeg` avant d’envoyer le message vocal natif. WhatsApp envoie le résultat via la charge utile Baileys `audio` avec `ptt: true` et `audio/ogg; codecs=opus`. Si la conversion échoue, Feishu reçoit le fichier original en pièce jointe ; l’envoi WhatsApp échoue au lieu de publier une charge utile PTT incompatible.
  * **Autres canaux** : MP3 (`mp3_44100_128` depuis ElevenLabs, `mp3` depuis OpenAI). 
    * 44,1 kHz / 128 kbps est l’équilibre par défaut pour la clarté de la parole.
  * **MiniMax** : MP3 (modèle `speech-2.8-hd`, fréquence d’échantillonnage de 32 kHz) pour les pièces jointes audio normales. Pour les cibles de notes vocales annoncées par le canal, OpenClaw transcode le MP3 MiniMax en Opus 48 kHz avec `ffmpeg` avant la livraison lorsque le canal annonce le transcodage.
  * **Xiaomi MiMo** : MP3 par défaut, ou WAV lorsqu’il est configuré. Pour les cibles de notes vocales annoncées par le canal, OpenClaw transcode la sortie Xiaomi en Opus 48 kHz avec `ffmpeg` avant la livraison lorsque le canal annonce le transcodage.
  * **CLI locale** : utilise le `outputFormat` configuré. Les cibles de notes vocales sont converties en Ogg/Opus et la sortie téléphonique est convertie en PCM mono brut 16 kHz avec `ffmpeg`.
  * **Google Gemini** : le TTS de l’API Gemini renvoie du PCM brut 24 kHz. OpenClaw l’encapsule en WAV pour les pièces jointes audio, le transcode en Opus 48 kHz pour les cibles de notes vocales, et renvoie directement le PCM pour Talk/la téléphonie.
  * **Gradium** : WAV pour les pièces jointes audio, Opus pour les cibles de notes vocales, et `ulaw_8000` à 8 kHz pour la téléphonie.
  * **Inworld** : MP3 pour les pièces jointes audio normales, `OGG_OPUS` natif pour les cibles de notes vocales, et `PCM` brut à 22050 Hz pour Talk/la téléphonie.
  * **xAI** : MP3 par défaut ; `responseFormat` peut être `mp3`, `wav`, `pcm`, `mulaw` ou `alaw`. OpenClaw utilise le point de terminaison TTS REST par lots de xAI et renvoie une pièce jointe audio complète ; le WebSocket TTS en streaming de xAI n’est pas utilisé par ce chemin de fournisseur. Le format natif Opus pour les notes vocales n’est pas pris en charge par ce chemin.
  * **Microsoft** : utilise `microsoft.outputFormat` (par défaut `audio-24khz-48kbitrate-mono-mp3`). 
    * Le transport groupé accepte un `outputFormat`, mais tous les formats ne sont pas disponibles depuis le service.
    * Les valeurs de format de sortie suivent les formats de sortie Microsoft Speech (y compris Ogg/WebM Opus).
    * Telegram `sendVoice` accepte OGG/MP3/M4A ; utilisez OpenAI/ElevenLabs si vous avez besoin de messages vocaux Opus garantis.
    * Si le format de sortie Microsoft configuré échoue, OpenClaw réessaie avec MP3.


Les formats de sortie OpenAI/ElevenLabs sont fixes par canal (voir ci-dessus).

## Comportement Auto-TTS

Lorsque `messages.tts.auto` est activé, OpenClaw :

  * Ignore le TTS si la réponse contient déjà un média ou une directive `MEDIA:`.
  * Ignore les réponses très courtes (moins de 10 caractères).
  * Résume les réponses longues lorsque les résumés sont activés, à l’aide de `summaryModel` (ou `agents.defaults.model.primary`).
  * Joint l’audio généré à la réponse.
  * En `mode: "final"`, envoie toujours le TTS audio seul pour les réponses finales diffusées une fois le flux de texte terminé ; le média généré passe par la même normalisation des médias du canal que les pièces jointes de réponse normales.


Si la réponse dépasse `maxLength` et que le résumé est désactivé (ou qu’aucune clé API n’est disponible pour le modèle de résumé), l’audio est ignoré et la réponse textuelle normale est envoyée.

textCopy code
[code]
    Réponse -> TTS activé ?  non -> envoyer le texte  oui -> contient un média / MEDIA: / court ?          oui -> envoyer le texte          non -> longueur > limite ?                   non -> TTS -> joindre l’audio                   oui -> résumé activé ?                            non -> envoyer le texte                            oui -> résumer -> TTS -> joindre l’audio
[/code]

## Formats de sortie par canal

Cible | Format  
---|---  
Feishu / Matrix / Telegram / WhatsApp | Les réponses par note vocale privilégient **Opus** (`opus_48000_64` from ElevenLabs, `opus` from OpenAI). 48 kHz / 64 kbps équilibre clarté et taille.  
Autres canaux | **MP3** (`mp3_44100_128` from ElevenLabs, `mp3` from OpenAI). 44,1 kHz / 128 kbps par défaut pour la parole.  
Talk / téléphonie | **PCM** natif du fournisseur (Inworld 22050 Hz, Google 24 kHz), ou `ulaw_8000` de Gradium pour la téléphonie.  
  
Notes par fournisseur :

  * **Transcodage Feishu / WhatsApp :** lorsqu’une réponse par note vocale arrive en MP3/WebM/WAV/M4A, le Plugin de canal transcode en Ogg/Opus 48 kHz avec `ffmpeg`. WhatsApp envoie via Baileys avec `ptt: true` et `audio/ogg; codecs=opus`. Si la conversion échoue : Feishu revient à l’ajout du fichier original en pièce jointe ; l’envoi WhatsApp échoue plutôt que de publier une charge utile PTT incompatible.
  * **MiniMax / Xiaomi MiMo :** MP3 par défaut (32 kHz pour MiniMax `speech-2.8-hd`) ; transcodé en Opus 48 kHz pour les cibles de notes vocales via `ffmpeg`.
  * **CLI locale :** utilise le `outputFormat` configuré. Les cibles de notes vocales sont converties en Ogg/Opus et la sortie téléphonie en PCM mono 16 kHz brut.
  * **Google Gemini :** renvoie du PCM 24 kHz brut. OpenClaw l’encapsule en WAV pour les pièces jointes, le transcode en Opus 48 kHz pour les cibles de notes vocales, renvoie directement le PCM pour Talk/la téléphonie.
  * **Inworld :** pièces jointes MP3, note vocale native `OGG_OPUS`, `PCM` brut 22050 Hz pour Talk/la téléphonie.
  * **xAI :** MP3 par défaut ; `responseFormat` peut valoir `mp3|wav|pcm|mulaw|alaw`. Utilise le point de terminaison REST par lot de xAI — le TTS WebSocket en streaming n’est **pas** utilisé. Le format natif Opus pour notes vocales n’est **pas** pris en charge.
  * **Microsoft :** utilise `microsoft.outputFormat` (par défaut `audio-24khz-48kbitrate-mono-mp3`). Telegram `sendVoice` accepte OGG/MP3/M4A ; utilisez OpenAI/ElevenLabs si vous avez besoin de messages vocaux Opus garantis. Si le format Microsoft configuré échoue, OpenClaw réessaie avec MP3.


Les formats de sortie OpenAI et ElevenLabs sont fixes par canal, comme indiqué ci-dessus.

## Référence des champs

Top-level messages.tts.*

Mode Auto-TTS. `inbound` n’envoie de l’audio qu’après un message vocal entrant ; `tagged` n’envoie de l’audio que lorsque la réponse inclut des directives `[[tts:...]]` ou un bloc `[[tts:text]]`.

Ancien interrupteur. `openclaw doctor --fix` le migre vers `auto`.

`"all"` inclut les réponses d’outil/bloc en plus des réponses finales.

Identifiant du fournisseur vocal. Lorsqu’il n’est pas défini, OpenClaw utilise le premier fournisseur configuré dans l’ordre de sélection automatique du registre. L’ancien `provider: "edge"` est réécrit en `"microsoft"` par `openclaw doctor --fix`.

Identifiant de persona actif issu de `personas`. Normalisé en minuscules.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBlcnNvbmFzLjxpZA " type="object"> Identité vocale stable. Champs : `label`, `description`, `provider`, `fallbackPolicy`, `prompt`, `providers.<provider>`. Voir Personas.

Modèle économique pour le résumé automatique ; utilise par défaut `agents.defaults.model.primary`. Accepte `provider/model` ou un alias de modèle configuré.

Autorise le modèle à émettre des directives TTS. `enabled` vaut `true` par défaut ; `allowProvider` vaut `false` par défaut.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb3ZpZGVycy48aWQ " type="object"> Paramètres détenus par le fournisseur, indexés par identifiant de fournisseur vocal. Les anciens blocs directs (`messages.tts.openai`, `.elevenlabs`, `.microsoft`, `.edge`) sont réécrits par `openclaw doctor --fix` ; validez uniquement `messages.tts.providers.<id>`.

Plafond strict pour les caractères d’entrée TTS. `/tts audio` échoue s’il est dépassé.

Délai d’expiration de la requête en millisecondes.

Remplace le chemin JSON des préférences locales (fournisseur/limite/résumé). Par défaut `~/.openclaw/settings/tts.json`.

Azure Speech

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env : `AZURE_SPEECH_KEY`, `AZURE_SPEECH_API_KEY`, ou `SPEECH_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlZ2lvbiIgdHlwZT0ic3RyaW5nIg Région Azure Speech (par ex. `eastus`). Env : `AZURE_SPEECH_REGION` ou `SPEECH_REGION`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVuZHBvaW50IiB0eXBlPSJzdHJpbmci Remplacement facultatif du point de terminaison Azure Speech (alias `baseUrl`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci ShortName de la voix Azure. Par défaut `en-US-JennyNeural`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI Code de langue SSML. Par défaut `en-US`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Azure `X-Microsoft-OutputFormat` pour l’audio standard. Par défaut `audio-24khz-48kbitrate-mono-mp3`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTm90ZU91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Azure `X-Microsoft-OutputFormat` pour la sortie note vocale. Par défaut `ogg-24khz-16bit-mono-opus`. OPENCLAW_DOCS_MARKER:paramClose:

ElevenLabs

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Se replie sur `ELEVENLABS_API_KEY` ou `XI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Identifiant de modèle (par ex. `eleven_multilingual_v2`, `eleven_v3`). OPENCLAW_DOCS_MARKER:paramClose:

`stability`, `similarityBoost`, `style` (chacun `0..1`), `useSpeakerBoost` (`true|false`), `speed` (`0.5..2.0`, `1.0` = normal).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlQ29kZSIgdHlwZT0ic3RyaW5nIg ISO 639-1 à 2 lettres (par ex. `en`, `de`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNlZWQiIHR5cGU9Im51bWJlciI Entier `0..4294967295` pour un déterminisme au mieux. OPENCLAW_DOCS_MARKER:paramClose:

Google Gemini

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Se replie sur `GEMINI_API_KEY` / `GOOGLE_API_KEY`. S’il est omis, le TTS peut réutiliser `models.providers.google.apiKey` avant le repli sur l’environnement. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Modèle TTS Gemini. Par défaut `gemini-3.1-flash-tts-preview`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTmFtZSIgdHlwZT0ic3RyaW5nIg Nom de voix prédéfinie Gemini. Par défaut `Kore`. Alias : `voice`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb21wdFRlbXBsYXRlIiB0eXBlPSciYXVkaW8tcHJvZmlsZS12MSIn Définissez sur `audio-profile-v1` pour encapsuler les champs d’invite de persona actif dans une structure d’invite TTS Gemini déterministe. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Seul `https://generativelanguage.googleapis.com` est accepté. OPENCLAW_DOCS_MARKER:paramClose:

Gradium

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env. : `GRADIUM_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Par défaut `https://api.gradium.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Emma par défaut (`YTpq7expH9539ERJ`). OPENCLAW_DOCS_MARKER:paramClose:

Inworld

### Principal Inworld

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env. : `INWORLD_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Par défaut `https://api.inworld.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsSWQiIHR5cGU9InN0cmluZyI Par défaut `inworld-tts-1.5-max`. Également : `inworld-tts-1.5-mini`, `inworld-tts-1-max`, `inworld-tts-1`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Par défaut `Sarah`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRlbXBlcmF0dXJlIiB0eXBlPSJudW1iZXIi Température d’échantillonnage `0..2`. OPENCLAW_DOCS_MARKER:paramClose:

CLI locale (tts-local-cli)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFyZ3MiIHR5cGU9InN0cmluZ1tdIg Arguments de commande. Prend en charge les espaces réservés `{{Text}}`, `{{OutputPath}}`, `{{OutputDir}}`, `{{OutputBase}}`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0nIm1wMyIgfCAib3B1cyIgfCAid2F2Iic Format de sortie CLI attendu. Par défaut `mp3` pour les pièces jointes audio. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Délai d’expiration de la commande en millisecondes. Par défaut `120000`. OPENCLAW_DOCS_MARKER:paramClose:

Microsoft (sans clé API)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Nom de voix neuronale Microsoft (par exemple `en-US-MichelleNeural`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI Code de langue (par exemple `en-US`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Format de sortie Microsoft. Par défaut `audio-24khz-48kbitrate-mono-mp3`. Tous les formats ne sont pas pris en charge par le transport inclus adossé à Edge. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJhdGUgLyBwaXRjaCAvIHZvbHVtZSIgdHlwZT0ic3RyaW5nIg Chaînes de pourcentage (par exemple `+10%`, `-5%`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVkZ2UuKiIgdHlwZT0ib2JqZWN0IiBkZXByZWNhdGVk Alias hérité. Exécutez `openclaw doctor --fix` pour réécrire la configuration persistante vers `providers.microsoft`. OPENCLAW_DOCS_MARKER:paramClose:

MiniMax

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Se rabat sur `MINIMAX_API_KEY`. Authentification Token Plan via `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY` ou `MINIMAX_CODING_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Par défaut `https://api.minimax.io`. Env. : `MINIMAX_API_HOST`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Par défaut `speech-2.8-hd`. Env. : `MINIMAX_TTS_MODEL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Par défaut `English_expressive_narrator`. Env. : `MINIMAX_TTS_VOICE_ID`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWVkIiB0eXBlPSJudW1iZXIi `0.5..2.0`. Par défaut `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvbCIgdHlwZT0ibnVtYmVyIg `(0, 10]`. Par défaut `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBpdGNoIiB0eXBlPSJudW1iZXIi Entier `-12..12`. Par défaut `0`. Les valeurs fractionnaires sont tronquées avant la requête. OPENCLAW_DOCS_MARKER:paramClose:

OpenAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Se rabat sur `OPENAI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Identifiant du modèle TTS OpenAI (par exemple `gpt-4o-mini-tts`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Nom de voix (par exemple `alloy`, `cedar`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imluc3RydWN0aW9ucyIgdHlwZT0ic3RyaW5nIg Champ OpenAI `instructions` explicite. Lorsqu’il est défini, les champs de prompt de persona ne sont **pas** mappés automatiquement. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImV4dHJhQm9keSAvIGV4dHJhX2JvZHkiIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 ">Champs JSON supplémentaires fusionnés dans les corps de requête `/audio/speech` après les champs TTS OpenAI générés. Utilisez ceci pour les points de terminaison compatibles OpenAI tels que Kokoro qui exigent des clés propres au fournisseur comme `lang` ; les clés de prototype non sûres sont ignorées. OPENCLAW_DOCS_MARKER:paramClose:

Remplacer le point de terminaison TTS OpenAI. Ordre de résolution : configuration → `OPENAI_TTS_BASE_URL` → `https://api.openai.com/v1`. Les valeurs non par défaut sont traitées comme des points de terminaison TTS compatibles OpenAI, les noms de modèle et de voix personnalisés sont donc acceptés.

OpenRouter

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env. : `OPENROUTER_API_KEY`. Peut réutiliser `models.providers.openrouter.apiKey`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Par défaut `https://openrouter.ai/api/v1`. L’ancien `https://openrouter.ai/v1` est normalisé. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Par défaut `hexgrad/kokoro-82m`. Alias : `modelId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Par défaut `af_alloy`. Alias : `voiceId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJwY20iJw Par défaut `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Volcengine (BytePlus Seed Speech)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env. : `VOLCENGINE_TTS_API_KEY` ou `BYTEPLUS_SEED_SPEECH_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc291cmNlSWQiIHR5cGU9InN0cmluZyI Par défaut `seed-tts-1.0`. Env. : `VOLCENGINE_TTS_RESOURCE_ID`. Utilisez `seed-tts-2.0` lorsque votre projet dispose du droit TTS 2.0. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcEtleSIgdHlwZT0ic3RyaW5nIg En-tête de clé d’application. Par défaut `aGjiRDfUWi`. Env. : `VOLCENGINE_TTS_APP_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Remplacer le point de terminaison HTTP TTS Seed Speech. Env. : `VOLCENGINE_TTS_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Type de voix. Par défaut `en_female_anna_mars_bigtts`. Env. : `VOLCENGINE_TTS_VOICE`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcElkIC8gdG9rZW4gLyBjbHVzdGVyIiB0eXBlPSJzdHJpbmciIGRlcHJlY2F0ZWQ Champs hérités de la console Volcengine Speech. Env. : `VOLCENGINE_TTS_APPID`, `VOLCENGINE_TTS_TOKEN`, `VOLCENGINE_TTS_CLUSTER` (par défaut `volcano_tts`). OPENCLAW_DOCS_MARKER:paramClose:

xAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env. : `XAI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Par défaut `https://api.x.ai/v1`. Env. : `XAI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Par défaut `eve`. Voix disponibles en direct : `ara`, `eve`, `leo`, `rex`, `sal`, `una`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlIiB0eXBlPSJzdHJpbmci Code de langue BCP-47 ou `auto`. Par défaut `en`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJ3YXYiIHwgInBjbSIgfCAibXVsYXciIHwgImFsYXciJw Par défaut `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Xiaomi MiMo

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env. : `XIAOMI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Par défaut `https://api.xiaomimimo.com/v1`. Env. : `XIAOMI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Par défaut `mimo-v2.5-tts`. Env. : `XIAOMI_TTS_MODEL`. Prend également en charge `mimo-v2-tts`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Par défaut `mimo_default`. Env. : `XIAOMI_TTS_VOICE`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImZvcm1hdCIgdHlwZT0nIm1wMyIgfCAid2F2Iic Par défaut `mp3`. Env. : `XIAOMI_TTS_FORMAT`. OPENCLAW_DOCS_MARKER:paramClose:

## Outil d’agent

L’outil `tts` convertit le texte en parole et retourne une pièce jointe audio pour la livraison de la réponse. Sur Feishu, Matrix, Telegram et WhatsApp, l’audio est livré comme message vocal plutôt que comme pièce jointe de fichier. Feishu et WhatsApp peuvent transcoder la sortie TTS non Opus sur ce chemin lorsque `ffmpeg` est disponible.

WhatsApp envoie l’audio via Baileys comme note vocale PTT (`audio` avec `ptt: true`) et envoie le texte visible **séparément** de l’audio PTT, car les clients n’affichent pas toujours les légendes sur les notes vocales.

L’outil accepte les champs facultatifs `channel` et `timeoutMs` ; `timeoutMs` est un délai d’expiration de requête fournisseur par appel, en millisecondes.

## RPC Gateway

Méthode | Objectif  
---|---  
`tts.status` | Lire l’état TTS actuel et la dernière tentative.  
`tts.enable` | Définir la préférence automatique locale sur `always`.  
`tts.disable` | Définir la préférence automatique locale sur `off`.  
`tts.convert` | Conversion ponctuelle texte → audio.  
`tts.setProvider` | Définir la préférence locale de fournisseur.  
`tts.setPersona` | Définir la préférence locale de persona.  
`tts.providers` | Lister les fournisseurs configurés et leur état.  
  
## Liens de service

  * [Guide de synthèse vocale OpenAI](<https://platform.openai.com/docs/guides/text-to-speech>)
  * [Référence de l’API audio OpenAI](<https://platform.openai.com/docs/api-reference/audio>)
  * [Synthèse vocale REST Azure Speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)
  * [Fournisseur Azure Speech](</fr/providers/azure-speech>)
  * [Synthèse vocale ElevenLabs](<https://elevenlabs.io/docs/api-reference/text-to-speech>)
  * [Authentification ElevenLabs](<https://elevenlabs.io/docs/api-reference/authentication>)
  * [Gradium](</fr/providers/gradium>)
  * [API TTS Inworld](<https://docs.inworld.ai/tts/tts>)
  * [API MiniMax T2A v2](<https://platform.minimaxi.com/document/T2A%20V2>)
  * [API HTTP TTS Volcengine](</fr/providers/volcengine#text-to-speech>)
  * [Synthèse vocale Xiaomi MiMo](</fr/providers/xiaomi#text-to-speech>)
  * [node-edge-tts](<https://github.com/SchneeHertz/node-edge-tts>)
  * [Formats de sortie Microsoft Speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech#audio-outputs>)
  * [Synthèse vocale xAI](<https://docs.x.ai/developers/rest-api-reference/inference/voice#text-to-speech-rest>)


## Connexe

  * [Vue d’ensemble des médias](</fr/tools/media-overview>)
  * [Génération musicale](</fr/tools/music-generation>)
  * [Génération vidéo](</fr/tools/video-generation>)
  * [Commandes slash](</fr/tools/slash-commands>)
  * [Plugin d’appel vocal](</fr/plugins/voice-call>)


Was this useful?YesNo