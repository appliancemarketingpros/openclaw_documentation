---
title: Text-zu-Sprache
source_url: https://docs.openclaw.ai/de/tools/tts
scraped_at: 2026-05-25
---

OpenClaw kann ausgehende Antworten bei **14 Speech-Providern** in Audio umwandeln und native Sprachnachrichten auf Feishu, Matrix, Telegram und WhatsApp, Audio-Anhänge überall sonst sowie PCM/Ulaw-Streams für Telefonie und Talk ausliefern.

TTS ist die Sprachausgabe-Hälfte von Talks `stt-tts`-Modus. Provider-native `realtime`-Talk-Sitzungen synthetisieren Sprache innerhalb des Echtzeit-Providers, statt diesen TTS-Pfad aufzurufen, während `transcription`-Sitzungen keine Assistenten-Sprachantwort synthetisieren.

## Schnellstart

* ### Pick a provider

OpenAI und ElevenLabs sind die zuverlässigsten gehosteten Optionen. Microsoft und Local CLI funktionieren ohne API-Schlüssel. Die vollständige Liste finden Sie in der Provider-Matrix.

* ### Set the API key

Exportieren Sie die Env-Var für Ihren Provider, zum Beispiel `OPENAI_API_KEY`, `ELEVENLABS_API_KEY`. Microsoft und Local CLI benötigen keinen Schlüssel.

* ### Enable in config

Setzen Sie `messages.tts.auto: "always"` und `messages.tts.provider`:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",    },  },}
[/code]

* ### Try it in chat

`/tts status` zeigt den aktuellen Zustand. `/tts audio Hello from OpenClaw` sendet eine einmalige Audio-Antwort.

## Unterstützte Provider

Provider | Authentifizierung | Hinweise  
---|---|---  
**Azure Speech** | `AZURE_SPEECH_KEY` \+ `AZURE_SPEECH_REGION` (auch `AZURE_SPEECH_API_KEY`, `SPEECH_KEY`, `SPEECH_REGION`) | Native Ogg/Opus-Sprachnotiz-Ausgabe und Telefonie.  
**DeepInfra** | `DEEPINFRA_API_KEY` | OpenAI-kompatibles TTS. Standardmäßig `hexgrad/Kokoro-82M`.  
**ElevenLabs** | `ELEVENLABS_API_KEY` oder `XI_API_KEY` | Voice Cloning, mehrsprachig, deterministisch über `seed`; gestreamt für Discord-Sprachwiedergabe.  
**Google Gemini** | `GEMINI_API_KEY` oder `GOOGLE_API_KEY` | Gemini-API-Batch-TTS; persona-bewusst über `promptTemplate: "audio-profile-v1"`.  
**Gradium** | `GRADIUM_API_KEY` | Sprachnotiz- und Telefonieausgabe.  
**Inworld** | `INWORLD_API_KEY` | Streaming-TTS-API. Native Opus-Sprachnotiz und PCM-Telefonie.  
**Local CLI** | keine | Führt einen konfigurierten lokalen TTS-Befehl aus.  
**Microsoft** | keine | Öffentliches Edge Neural TTS über `node-edge-tts`. Best Effort, kein SLA.  
**MiniMax** | `MINIMAX_API_KEY` (oder Token Plan: `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY`, `MINIMAX_CODING_API_KEY`) | T2A-v2-API. Standardmäßig `speech-2.8-hd`.  
**OpenAI** | `OPENAI_API_KEY` | Wird auch für automatische Zusammenfassungen verwendet; unterstützt Persona-`instructions`.  
**OpenRouter** | `OPENROUTER_API_KEY` (kann `models.providers.openrouter.apiKey` wiederverwenden) | Standardmodell `hexgrad/kokoro-82m`.  
**Volcengine** | `VOLCENGINE_TTS_API_KEY` oder `BYTEPLUS_SEED_SPEECH_API_KEY` (Legacy-AppID/Token: `VOLCENGINE_TTS_APPID`/`_TOKEN`) | BytePlus Seed Speech HTTP API.  
**Vydra** | `VYDRA_API_KEY` | Gemeinsamer Bild-, Video- und Speech-Provider.  
**xAI** | `XAI_API_KEY` | xAI-Batch-TTS. Native Opus-Sprachnotiz wird **nicht** unterstützt.  
**Xiaomi MiMo** | `XIAOMI_API_KEY` | MiMo-TTS über Xiaomi Chat Completions.  
  
Wenn mehrere Provider konfiguriert sind, wird der ausgewählte zuerst verwendet und die anderen sind Fallback-Optionen. Automatische Zusammenfassung verwendet `summaryModel` (oder `agents.defaults.model.primary`), daher muss dieser Provider ebenfalls authentifiziert sein, wenn Sie Zusammenfassungen aktiviert lassen.

## Konfiguration

Die TTS-Konfiguration liegt unter `messages.tts` in `~/.openclaw/openclaw.json`. Wählen Sie ein Preset und passen Sie den Provider-Block an:

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

### Sprachüberschreibungen pro Agent

Verwenden Sie `agents.list[].tts`, wenn ein Agent mit einem anderen Provider, einer anderen Stimme, einem anderen Modell, einer anderen Persona oder einem anderen Auto-TTS-Modus sprechen soll. Der Agent-Block wird per Deep Merge über `messages.tts` gelegt, sodass Provider-Anmeldedaten in der globalen Provider-Konfiguration bleiben können:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",      providers: {        elevenlabs: { apiKey: "${ELEVENLABS_API_KEY}", model: "eleven_multilingual_v2" },      },    },  },  agents: {    list: [      {        id: "reader",        tts: {          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL" },          },        },      },    ],  },}
[/code]

Um eine agentenspezifische Persona festzulegen, setzen Sie `agents.list[].tts.persona` zusammen mit der Provider-Konfiguration. Sie überschreibt die globale `messages.tts.persona` nur für diesen Agenten.

Rangfolge für automatische Antworten, `/tts audio`, `/tts status` und das Agent-Tool `tts`:

  1. `messages.tts`
  2. aktives `agents.list[].tts`
  3. Kanal-Override, wenn der Kanal `channels.<channel>.tts` unterstützt
  4. Konto-Override, wenn der Kanal `channels.<channel>.accounts.<id>.tts` übergibt
  5. lokale `/tts`-Einstellungen für diesen Host
  6. Inline-Direktiven `[[tts:...]]`, wenn Modell-Overrides aktiviert sind


Kanal- und Konto-Overrides verwenden dieselbe Struktur wie `messages.tts` und werden per Deep Merge über die früheren Ebenen gelegt. So können gemeinsame Provider-Anmeldedaten in `messages.tts` bleiben, während ein Kanal oder Bot-Konto nur Stimme, Modell, Persona oder Automatikmodus ändert:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "openai",      providers: {        openai: { apiKey: "${OPENAI_API_KEY}", model: "gpt-4o-mini-tts" },      },    },  },  channels: {    feishu: {      accounts: {        english: {          tts: {            providers: {              openai: { voice: "shimmer" },            },          },        },      },    },  },}
[/code]

## Personas

Eine **Persona** ist eine stabile gesprochene Identität, die deterministisch providerübergreifend angewendet werden kann. Sie kann einen Provider bevorzugen, eine providerneutrale Prompt-Absicht definieren und providerspezifische Bindings für Stimmen, Modelle, Prompt-Vorlagen, Seeds und Spracheinstellungen enthalten.

### Minimale Persona

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "narrator",      personas: {        narrator: {          label: "Narrator",          provider: "elevenlabs",          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL", modelId: "eleven_multilingual_v2" },          },        },      },    },  },}
[/code]

### Vollständige Persona (providerneutraler Prompt)

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "alfred",      personas: {        alfred: {          label: "Alfred",          description: "Dry, warm British butler narrator.",          provider: "google",          fallbackPolicy: "preserve-persona",          prompt: {            profile: "A brilliant British butler. Dry, witty, warm, charming, emotionally expressive, never generic.",            scene: "A quiet late-night study. Close-mic narration for a trusted operator.",            sampleContext: "The speaker is answering a private technical request with concise confidence and dry warmth.",            style: "Refined, understated, lightly amused.",            accent: "British English.",            pacing: "Measured, with short dramatic pauses.",            constraints: ["Do not read configuration values aloud.", "Do not explain the persona."],          },          providers: {            google: {              model: "gemini-3.1-flash-tts-preview",              voiceName: "Algieba",              promptTemplate: "audio-profile-v1",            },            openai: { model: "gpt-4o-mini-tts", voice: "cedar" },            elevenlabs: {              voiceId: "voice_id",              modelId: "eleven_multilingual_v2",              seed: 42,              voiceSettings: {                stability: 0.65,                similarityBoost: 0.8,                style: 0.25,                useSpeakerBoost: true,                speed: 0.95,              },            },          },        },      },    },  },}
[/code]

### Auflösung der Persona

Die aktive Persona wird deterministisch ausgewählt:

  1. lokale Einstellung `/tts persona <id>`, falls gesetzt.
  2. `messages.tts.persona`, falls gesetzt.
  3. Keine Persona.


Die Provider-Auswahl läuft mit expliziten Vorgaben zuerst:

  1. Direkte Overrides (CLI, Gateway, Talk, erlaubte TTS-Direktiven).
  2. lokale Einstellung `/tts provider <id>`.
  3. `provider` der aktiven Persona.
  4. `messages.tts.provider`.
  5. Automatische Auswahl aus der Registry.


Für jeden Provider-Versuch führt OpenClaw Konfigurationen in dieser Reihenfolge zusammen:

  1. `messages.tts.providers.<id>`
  2. `messages.tts.personas.<persona>.providers.<id>`
  3. Vertrauenswürdige Request-Overrides
  4. Erlaubte, vom Modell ausgegebene TTS-Direktiv-Overrides


### Wie Provider Persona-Prompts verwenden

Persona-Prompt-Felder (`profile`, `scene`, `sampleContext`, `style`, `accent`, `pacing`, `constraints`) sind **providerneutral**. Jeder Provider entscheidet selbst, wie er sie verwendet:

Google Gemini

Fasst Persona-Prompt-Felder in eine Gemini-TTS-Prompt-Struktur ein, **nur wenn** die effektive Google-Provider-Konfiguration `promptTemplate: "audio-profile-v1"` oder `personaPrompt` setzt. Die älteren Felder `audioProfile` und `speakerName` werden weiterhin als Google-spezifischer Prompt-Text vorangestellt. Inline-Audio-Tags wie `[whispers]` oder `[laughs]` innerhalb eines `[[tts:text]]`-Blocks bleiben im Gemini-Transkript erhalten; OpenClaw erzeugt diese Tags nicht.

OpenAI

Ordnet Persona-Prompt-Felder dem Request-Feld `instructions` zu, **nur wenn** keine expliziten OpenAI-`instructions` konfiguriert sind. Explizite `instructions` haben immer Vorrang.

Other providers

Verwenden nur die providerspezifischen Persona-Bindings unter `personas.<id>.providers.<provider>`. Persona-Prompt-Felder werden ignoriert, sofern der Provider keine eigene Zuordnung für Persona-Prompts implementiert.

### Fallback-Richtlinie

`fallbackPolicy` steuert das Verhalten, wenn eine Persona **kein Binding** für den versuchten Provider hat:

Richtlinie | Verhalten  
---|---  
`preserve-persona` | **Standard.** Providerneutrale Prompt-Felder bleiben verfügbar; der Provider kann sie verwenden oder ignorieren.  
`provider-defaults` | Die Persona wird für diesen Versuch aus der Prompt-Vorbereitung ausgelassen; der Provider verwendet seine neutralen Standardwerte, während der Fallback zu anderen Providern fortgesetzt wird.  
`fail` | Diesen Provider-Versuch mit `reasonCode: "not_configured"` und `personaBinding: "missing"` überspringen. Fallback-Provider werden weiterhin versucht.  
  
Der gesamte TTS-Request schlägt nur fehl, wenn **jeder** versuchte Provider übersprungen wird oder fehlschlägt.

Die Provider-Auswahl für Talk-Sitzungen ist sitzungsbezogen. Ein Talk-Client sollte Provider-IDs, Modell-IDs, Voice-IDs und Locales aus `talk.catalog` auswählen und sie über die Talk-Sitzung oder den Handoff-Request übergeben. Das Öffnen einer Sprachsitzung sollte `messages.tts` oder globale Talk-Provider-Standards nicht verändern.

## Modellgesteuerte Direktiven

Standardmäßig **kann** der Assistent `[[tts:...]]`-Direktiven ausgeben, um Stimme, Modell oder Geschwindigkeit für eine einzelne Antwort zu überschreiben, plus einen optionalen `[[tts:text]]...[[/tts:text]]`-Block für ausdrucksstarke Hinweise, die nur im Audio erscheinen sollen:

textCopy code
[code]
    Here you go. [[tts:voiceId=pMsXgVXv3BLzUgSXRplE model=eleven_v3 speed=1.1]][[tts:text]](laughs) Read the song once more.[[/tts:text]]
[/code]

Wenn `messages.tts.auto` `"tagged"` ist, sind **Direktiven erforderlich** , um Audio auszulösen. Die Streaming-Blockauslieferung entfernt Direktiven aus sichtbarem Text, bevor der Kanal sie sieht, auch wenn sie über benachbarte Blöcke verteilt sind.

`provider=...` wird ignoriert, sofern `modelOverrides.allowProvider: true` nicht gesetzt ist. Wenn eine Antwort `provider=...` deklariert, werden die anderen Schlüssel in dieser Direktive nur von diesem Provider geparst; nicht unterstützte Schlüssel werden entfernt und als TTS-Direktivwarnungen gemeldet.

**Verfügbare Direktivschlüssel:**

  * `provider` (registrierte Provider-ID; erfordert `allowProvider: true`)
  * `voice` / `voiceName` / `voice_name` / `google_voice` / `voiceId`
  * `model` / `google_model`
  * `stability`, `similarityBoost`, `style`, `speed`, `useSpeakerBoost`
  * `vol` / `volume` (MiniMax-Lautstärke, 0–10)
  * `pitch` (MiniMax-Ganzzahltonhöhe, −12 bis 12; Dezimalwerte werden abgeschnitten)
  * `emotion` (Volcengine-Emotions-Tag)
  * `applyTextNormalization` (`auto|on|off`)
  * `languageCode` (ISO 639-1)
  * `seed`


**Modell-Overrides vollständig deaktivieren:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: false } } } }
[/code]

**Provider-Wechsel erlauben, während andere Regler konfigurierbar bleiben:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: true, allowProvider: true, allowSeed: false } } } }
[/code]

## Slash-Befehle

Einzelner Befehl `/tts`. Auf Discord registriert OpenClaw zusätzlich `/voice`, weil `/tts` ein integrierter Discord-Befehl ist. Textuelles `/tts ...` funktioniert weiterhin.

textCopy code
[code]
    /tts off | on | status/tts chat on | off | default/tts latest/tts provider <id>/tts persona <id> | off/tts limit <chars>/tts summary off/tts audio <text>
[/code]

Verhaltenshinweise:

  * `/tts on` schreibt die lokale TTS-Einstellung auf `always`; `/tts off` schreibt sie auf `off`.
  * `/tts chat on|off|default` schreibt einen sitzungsbezogenen Auto-TTS-Override für den aktuellen Chat.
  * `/tts persona <id>` schreibt die lokale Persona-Einstellung; `/tts persona off` löscht sie.
  * `/tts latest` liest die neueste Assistentenantwort aus dem aktuellen Sitzungstranskript und sendet sie einmalig als Audio. Es speichert nur einen Hash dieser Antwort im Sitzungseintrag, um doppelte Sprachausgaben zu unterdrücken.
  * `/tts audio` erzeugt eine einmalige Audioantwort (schaltet TTS **nicht** ein).
  * `limit` und `summary` werden in **lokalen Einstellungen** gespeichert, nicht in der Hauptkonfiguration.
  * `/tts status` enthält Fallback-Diagnosen für den neuesten Versuch: `Fallback: <primary> -> <used>`, `Attempts: ...` sowie Details pro Versuch (`provider:outcome(reasonCode) latency`).
  * `/status` zeigt den aktiven TTS-Modus sowie den konfigurierten Provider, das Modell, die Stimme und bereinigte Metadaten für benutzerdefinierte Endpunkte, wenn TTS aktiviert ist.


## Benutzerspezifische Einstellungen

Slash-Befehle schreiben lokale Overrides nach `prefsPath`. Der Standard ist `~/.openclaw/settings/tts.json`; überschreiben Sie ihn mit der Umgebungsvariablen `OPENCLAW_TTS_PREFS` oder `messages.tts.prefsPath`.

Gespeichertes Feld | Wirkung  
---|---  
`auto` | Lokaler Auto-TTS-Override (`always`, `off`, …)  
`provider` | Lokaler Override des primären Providers  
`persona` | Lokaler Persona-Override  
`maxLength` | Schwellenwert für Zusammenfassung (standardmäßig `1500` Zeichen)  
`summarize` | Schalter für Zusammenfassung (standardmäßig `true`)  
  
Diese überschreiben die effektive Konfiguration aus `messages.tts` plus den aktiven Block `agents.list[].tts` für diesen Host.

## Ausgabeformate (fest)

Die TTS-Sprachauslieferung wird durch Kanalfähigkeiten gesteuert. Kanal-Plugins geben an, ob TTS im Sprachstil Provider nach einem nativen Ziel `voice-note` fragen soll oder ob normale `audio-file`-Synthese beibehalten und kompatible Ausgabe nur für die Sprachauslieferung markiert werden soll.

  * **Kanäle mit Sprachnotiz-Unterstützung** : Sprachnotiz-Antworten bevorzugen Opus (`opus_48000_64` von ElevenLabs, `opus` von OpenAI). 
    * 48 kHz / 64 kbit/s ist ein guter Kompromiss für Sprachnachrichten.
  * **Feishu / WhatsApp** : Wenn eine Sprachnotiz-Antwort als MP3/WebM/WAV/M4A oder eine andere wahrscheinliche Audiodatei erzeugt wird, transkodiert das Kanal-Plugin sie vor dem Senden der nativen Sprachnachricht mit `ffmpeg` nach 48 kHz Ogg/Opus. WhatsApp sendet das Ergebnis über die Baileys-`audio`-Payload mit `ptt: true` und `audio/ogg; codecs=opus`. Wenn die Konvertierung fehlschlägt, erhält Feishu die Originaldatei als Anhang; der WhatsApp-Versand schlägt fehl, statt eine inkompatible PTT-Payload zu posten.
  * **Andere Kanäle** : MP3 (`mp3_44100_128` von ElevenLabs, `mp3` von OpenAI). 
    * 44,1 kHz / 128 kbit/s ist die Standardbalance für Sprachverständlichkeit.
  * **MiniMax** : MP3 (`speech-2.8-hd`-Modell, 32-kHz-Abtastrate) für normale Audioanhänge. Für vom Kanal angegebene Sprachnotiz-Ziele transkodiert OpenClaw das MiniMax-MP3 vor der Auslieferung mit `ffmpeg` nach 48 kHz Opus, wenn der Kanal Transkodierung angibt.
  * **Xiaomi MiMo** : Standardmäßig MP3 oder WAV, wenn konfiguriert. Für vom Kanal angegebene Sprachnotiz-Ziele transkodiert OpenClaw die Xiaomi-Ausgabe vor der Auslieferung mit `ffmpeg` nach 48 kHz Opus, wenn der Kanal Transkodierung angibt.
  * **Lokale CLI** : verwendet das konfigurierte `outputFormat`. Sprachnotiz-Ziele werden nach Ogg/Opus konvertiert, und Telefonieausgabe wird mit `ffmpeg` in rohes 16-kHz-Mono-PCM konvertiert.
  * **Google Gemini** : Gemini API TTS gibt rohes 24-kHz-PCM zurück. OpenClaw verpackt es für Audioanhänge als WAV, transkodiert es für Sprachnotiz-Ziele nach 48 kHz Opus und gibt PCM für Talk/Telefonie direkt zurück.
  * **Gradium** : WAV für Audioanhänge, Opus für Sprachnotiz-Ziele und `ulaw_8000` bei 8 kHz für Telefonie.
  * **Inworld** : MP3 für normale Audioanhänge, natives `OGG_OPUS` für Sprachnotiz-Ziele und rohes `PCM` bei 22050 Hz für Talk/Telefonie.
  * **xAI** : standardmäßig MP3; `responseFormat` kann `mp3`, `wav`, `pcm`, `mulaw` oder `alaw` sein. OpenClaw verwendet den Batch-REST-TTS-Endpunkt von xAI und gibt einen vollständigen Audioanhang zurück; der Streaming-TTS-WebSocket von xAI wird von diesem Provider-Pfad nicht verwendet. Das native Opus-Sprachnotizformat wird von diesem Pfad nicht unterstützt.
  * **Microsoft** : verwendet `microsoft.outputFormat` (Standard `audio-24khz-48kbitrate-mono-mp3`). 
    * Der gebündelte Transport akzeptiert ein `outputFormat`, aber nicht alle Formate sind beim Dienst verfügbar.
    * Ausgabeformatwerte folgen den Microsoft Speech-Ausgabeformaten (einschließlich Ogg/WebM Opus).
    * Telegram `sendVoice` akzeptiert OGG/MP3/M4A; verwenden Sie OpenAI/ElevenLabs, wenn Sie garantierte Opus-Sprachnachrichten benötigen.
    * Wenn das konfigurierte Microsoft-Ausgabeformat fehlschlägt, versucht OpenClaw es erneut mit MP3.


OpenAI/ElevenLabs-Ausgabeformate sind je nach Kanal festgelegt (siehe oben).

## Auto-TTS-Verhalten

Wenn `messages.tts.auto` aktiviert ist, führt OpenClaw Folgendes aus:

  * Überspringt TTS, wenn die Antwort bereits Medien oder eine `MEDIA:`-Direktive enthält.
  * Überspringt sehr kurze Antworten (unter 10 Zeichen).
  * Fasst lange Antworten zusammen, wenn Zusammenfassungen aktiviert sind, unter Verwendung von `summaryModel` (oder `agents.defaults.model.primary`).
  * Hängt das erzeugte Audio an die Antwort an.
  * In `mode: "final"` wird weiterhin nur Audio-TTS für gestreamte finale Antworten gesendet, nachdem der Textstream abgeschlossen ist; die erzeugten Medien durchlaufen dieselbe Kanal-Mediennormalisierung wie normale Antwortanhänge.


Wenn die Antwort `maxLength` überschreitet und die Zusammenfassung deaktiviert ist (oder kein API-Schlüssel für das Zusammenfassungsmodell vorhanden ist), wird Audio übersprungen und die normale Textantwort gesendet.

textCopy code
[code]
    Reply -> TTS enabled?  no  -> send text  yes -> has media / MEDIA: / short?          yes -> send text          no  -> length > limit?                   no  -> TTS -> attach audio                   yes -> summary enabled?                            no  -> send text                            yes -> summarize -> TTS -> attach audio
[/code]

## Ausgabeformate nach Kanal

Ziel | Format  
---|---  
Feishu / Matrix / Telegram / WhatsApp | Sprachnotiz-Antworten bevorzugen **Opus** (`opus_48000_64` von ElevenLabs, `opus` von OpenAI). 48 kHz / 64 kbps bieten ein gutes Verhältnis aus Verständlichkeit und Größe.  
Andere Kanäle | **MP3** (`mp3_44100_128` von ElevenLabs, `mp3` von OpenAI). 44,1 kHz / 128 kbps als Standard für Sprache.  
Talk / Telefonie | Provider-eigenes **PCM** (Inworld 22050 Hz, Google 24 kHz) oder `ulaw_8000` von Gradium für Telefonie.  
  
Hinweise pro Provider:

  * **Feishu / WhatsApp-Transcodierung:** Wenn eine Sprachnotiz-Antwort als MP3/WebM/WAV/M4A ankommt, transcodiert das Kanal-Plugin sie mit `ffmpeg` zu 48 kHz Ogg/Opus. WhatsApp sendet über Baileys mit `ptt: true` und `audio/ogg; codecs=opus`. Wenn die Konvertierung fehlschlägt: Feishu fällt darauf zurück, die Originaldatei anzuhängen; der WhatsApp-Versand schlägt fehl, statt eine inkompatible PTT-Nutzlast zu posten.
  * **MiniMax / Xiaomi MiMo:** Standardmäßig MP3 (32 kHz für MiniMax `speech-2.8-hd`); wird für Sprachnotiz-Ziele über `ffmpeg` zu 48 kHz Opus transcodiert.
  * **Lokale CLI:** Verwendet das konfigurierte `outputFormat`. Sprachnotiz-Ziele werden zu Ogg/Opus konvertiert und Telefonie-Ausgabe zu rohem 16-kHz-Mono-PCM.
  * **Google Gemini:** Gibt rohes 24-kHz-PCM zurück. OpenClaw verpackt es für Anhänge als WAV, transcodiert es für Sprachnotiz-Ziele zu 48 kHz Opus und gibt PCM direkt für Talk/Telefonie zurück.
  * **Inworld:** MP3-Anhänge, natives `OGG_OPUS` für Sprachnotizen, rohes `PCM` mit 22050 Hz für Talk/Telefonie.
  * **xAI:** Standardmäßig MP3; `responseFormat` kann `mp3|wav|pcm|mulaw|alaw` sein. Verwendet den Batch-REST-Endpunkt von xAI — Streaming-WebSocket-TTS wird **nicht** verwendet. Natives Opus-Format für Sprachnotizen wird **nicht** unterstützt.
  * **Microsoft:** Verwendet `microsoft.outputFormat` (Standard `audio-24khz-48kbitrate-mono-mp3`). Telegram `sendVoice` akzeptiert OGG/MP3/M4A; verwenden Sie OpenAI/ElevenLabs, wenn Sie garantiert Opus-Sprachnachrichten benötigen. Wenn das konfigurierte Microsoft-Format fehlschlägt, versucht OpenClaw es erneut mit MP3.


OpenAI- und ElevenLabs-Ausgabeformate sind wie oben aufgeführt pro Kanal festgelegt.

## Feldreferenz

Top-level messages.tts.*

Auto-TTS-Modus. `inbound` sendet Audio nur nach einer eingehenden Sprachnachricht; `tagged` sendet Audio nur, wenn die Antwort `[[tts:...]]`-Direktiven oder einen `[[tts:text]]`-Block enthält.

Veralteter Umschalter. `openclaw doctor --fix` migriert dies zu `auto`.

`"all"` enthält zusätzlich zu finalen Antworten auch Tool-/Block-Antworten.

Sprach-Provider-ID. Wenn nicht gesetzt, verwendet OpenClaw den ersten konfigurierten Provider in der Registry-Auto-Select-Reihenfolge. Das veraltete `provider: "edge"` wird von `openclaw doctor --fix` zu `"microsoft"` umgeschrieben.

Aktive Persona-ID aus `personas`. Wird in Kleinbuchstaben normalisiert.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBlcnNvbmFzLjxpZA " type="object"> Stabile gesprochene Identität. Felder: `label`, `description`, `provider`, `fallbackPolicy`, `prompt`, `providers.<provider>`. Siehe Personas.

Günstiges Modell für automatische Zusammenfassung; Standard ist `agents.defaults.model.primary`. Akzeptiert `provider/model` oder einen konfigurierten Modellalias.

Erlaubt dem Modell, TTS-Direktiven auszugeben. `enabled` ist standardmäßig `true`; `allowProvider` ist standardmäßig `false`.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb3ZpZGVycy48aWQ " type="object"> Provider-eigene Einstellungen, indiziert nach Sprach-Provider-ID. Veraltete direkte Blöcke (`messages.tts.openai`, `.elevenlabs`, `.microsoft`, `.edge`) werden von `openclaw doctor --fix` umgeschrieben; committen Sie nur `messages.tts.providers.<id>`.

Harte Obergrenze für TTS-Eingabezeichen. `/tts audio` schlägt fehl, wenn sie überschritten wird.

Anfrage-Timeout in Millisekunden.

Überschreibt den lokalen Pfad für das Prefs-JSON (Provider/Limit/Zusammenfassung). Standard `~/.openclaw/settings/tts.json`.

Azure Speech

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `AZURE_SPEECH_KEY`, `AZURE_SPEECH_API_KEY` oder `SPEECH_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlZ2lvbiIgdHlwZT0ic3RyaW5nIg Azure Speech-Region (z. B. `eastus`). Env: `AZURE_SPEECH_REGION` oder `SPEECH_REGION`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVuZHBvaW50IiB0eXBlPSJzdHJpbmci Optionale Überschreibung des Azure Speech-Endpunkts (Alias `baseUrl`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Azure-Voice-ShortName. Standard `en-US-JennyNeural`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI SSML-Sprachcode. Standard `en-US`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Azure `X-Microsoft-OutputFormat` für Standard-Audio. Standard `audio-24khz-48kbitrate-mono-mp3`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTm90ZU91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Azure `X-Microsoft-OutputFormat` für Sprachnotiz-Ausgabe. Standard `ogg-24khz-16bit-mono-opus`. OPENCLAW_DOCS_MARKER:paramClose:

ElevenLabs

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Fällt auf `ELEVENLABS_API_KEY` oder `XI_API_KEY` zurück. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Modell-ID (z. B. `eleven_multilingual_v2`, `eleven_v3`). OPENCLAW_DOCS_MARKER:paramClose:

`stability`, `similarityBoost`, `style` (jeweils `0..1`), `useSpeakerBoost` (`true|false`), `speed` (`0.5..2.0`, `1.0` = normal).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlQ29kZSIgdHlwZT0ic3RyaW5nIg 2-stelliger ISO 639-1-Code (z. B. `en`, `de`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNlZWQiIHR5cGU9Im51bWJlciI Ganzzahl `0..4294967295` für Best-Effort-Determinismus. OPENCLAW_DOCS_MARKER:paramClose:

Google Gemini

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Fällt auf `GEMINI_API_KEY` / `GOOGLE_API_KEY` zurück. Wenn ausgelassen, kann TTS `models.providers.google.apiKey` vor dem Env-Fallback wiederverwenden. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Gemini-TTS-Modell. Standard `gemini-3.1-flash-tts-preview`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTmFtZSIgdHlwZT0ic3RyaW5nIg Vorgefertigter Gemini-Voice-Name. Standard `Kore`. Alias: `voice`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb21wdFRlbXBsYXRlIiB0eXBlPSciYXVkaW8tcHJvZmlsZS12MSIn Auf `audio-profile-v1` setzen, um aktive Persona-Prompt-Felder in eine deterministische Gemini-TTS-Prompt-Struktur einzubetten. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Nur `https://generativelanguage.googleapis.com` wird akzeptiert. OPENCLAW_DOCS_MARKER:paramClose:

Gradium

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `GRADIUM_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Standard `https://api.gradium.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Standard Emma (`YTpq7expH9539ERJ`). OPENCLAW_DOCS_MARKER:paramClose:

Inworld

### Inworld primär

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `INWORLD_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Standard `https://api.inworld.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsSWQiIHR5cGU9InN0cmluZyI Standard `inworld-tts-1.5-max`. Außerdem: `inworld-tts-1.5-mini`, `inworld-tts-1-max`, `inworld-tts-1`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Standard `Sarah`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRlbXBlcmF0dXJlIiB0eXBlPSJudW1iZXIi Sampling-Temperatur `0..2`. OPENCLAW_DOCS_MARKER:paramClose:

Local CLI (tts-local-cli)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFyZ3MiIHR5cGU9InN0cmluZ1tdIg Befehlsargumente. Unterstützt die Platzhalter `{{Text}}`, `{{OutputPath}}`, `{{OutputDir}}`, `{{OutputBase}}`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0nIm1wMyIgfCAib3B1cyIgfCAid2F2Iic Erwartetes CLI-Ausgabeformat. Standard `mp3` für Audio-Anhänge. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Befehls-Timeout in Millisekunden. Standard `120000`. OPENCLAW_DOCS_MARKER:paramClose:

Microsoft (no API key)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Name der neuronalen Microsoft-Stimme (z. B. `en-US-MichelleNeural`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI Sprachcode (z. B. `en-US`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Microsoft-Ausgabeformat. Standard `audio-24khz-48kbitrate-mono-mp3`. Nicht alle Formate werden vom gebündelten Edge-gestützten Transport unterstützt. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJhdGUgLyBwaXRjaCAvIHZvbHVtZSIgdHlwZT0ic3RyaW5nIg Prozentzeichenfolgen (z. B. `+10%`, `-5%`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVkZ2UuKiIgdHlwZT0ib2JqZWN0IiBkZXByZWNhdGVk Legacy-Alias. Führen Sie `openclaw doctor --fix` aus, um persistierte Konfiguration nach `providers.microsoft` umzuschreiben. OPENCLAW_DOCS_MARKER:paramClose:

MiniMax

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Fällt auf `MINIMAX_API_KEY` zurück. Token-Plan-Authentifizierung über `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY` oder `MINIMAX_CODING_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Standard `https://api.minimax.io`. Env: `MINIMAX_API_HOST`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Standard `speech-2.8-hd`. Env: `MINIMAX_TTS_MODEL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Standard `English_expressive_narrator`. Env: `MINIMAX_TTS_VOICE_ID`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWVkIiB0eXBlPSJudW1iZXIi `0.5..2.0`. Standard `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvbCIgdHlwZT0ibnVtYmVyIg `(0, 10]`. Standard `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBpdGNoIiB0eXBlPSJudW1iZXIi Ganzzahl `-12..12`. Standard `0`. Bruchwerte werden vor der Anfrage abgeschnitten. OPENCLAW_DOCS_MARKER:paramClose:

OpenAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Fällt auf `OPENAI_API_KEY` zurück. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci OpenAI-TTS-Modell-ID (z. B. `gpt-4o-mini-tts`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Stimmenname (z. B. `alloy`, `cedar`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imluc3RydWN0aW9ucyIgdHlwZT0ic3RyaW5nIg Explizites OpenAI-Feld `instructions`. Wenn gesetzt, werden Persona-Prompt-Felder **nicht** automatisch zugeordnet. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImV4dHJhQm9keSAvIGV4dHJhX2JvZHkiIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 ">Zusätzliche JSON-Felder, die nach generierten OpenAI-TTS-Feldern in `/audio/speech`-Anfrage-Bodys zusammengeführt werden. Verwenden Sie dies für OpenAI-kompatible Endpunkte wie Kokoro, die Provider-spezifische Schlüssel wie `lang` erfordern; unsichere Prototype-Schlüssel werden ignoriert. OPENCLAW_DOCS_MARKER:paramClose:

OpenAI-TTS-Endpunkt überschreiben. Auflösungsreihenfolge: Konfiguration → `OPENAI_TTS_BASE_URL` → `https://api.openai.com/v1`. Nicht standardmäßige Werte werden als OpenAI-kompatible TTS-Endpunkte behandelt, daher werden benutzerdefinierte Modell- und Stimmennamen akzeptiert.

OpenRouter

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `OPENROUTER_API_KEY`. Kann `models.providers.openrouter.apiKey` wiederverwenden. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Standard `https://openrouter.ai/api/v1`. Legacy `https://openrouter.ai/v1` wird normalisiert. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Standard `hexgrad/kokoro-82m`. Alias: `modelId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Standard `af_alloy`. Alias: `voiceId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJwY20iJw Standard `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Volcengine (BytePlus Seed Speech)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `VOLCENGINE_TTS_API_KEY` oder `BYTEPLUS_SEED_SPEECH_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc291cmNlSWQiIHR5cGU9InN0cmluZyI Standard `seed-tts-1.0`. Env: `VOLCENGINE_TTS_RESOURCE_ID`. Verwenden Sie `seed-tts-2.0`, wenn Ihr Projekt eine TTS-2.0-Berechtigung hat. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcEtleSIgdHlwZT0ic3RyaW5nIg App-Key-Header. Standard `aGjiRDfUWi`. Env: `VOLCENGINE_TTS_APP_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Den Seed-Speech-TTS-HTTP-Endpunkt überschreiben. Env: `VOLCENGINE_TTS_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Stimmentyp. Standard `en_female_anna_mars_bigtts`. Env: `VOLCENGINE_TTS_VOICE`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcElkIC8gdG9rZW4gLyBjbHVzdGVyIiB0eXBlPSJzdHJpbmciIGRlcHJlY2F0ZWQ Legacy-Felder der Volcengine Speech Console. Env: `VOLCENGINE_TTS_APPID`, `VOLCENGINE_TTS_TOKEN`, `VOLCENGINE_TTS_CLUSTER` (Standard `volcano_tts`). OPENCLAW_DOCS_MARKER:paramClose:

xAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `XAI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Standard `https://api.x.ai/v1`. Env: `XAI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Standard `eve`. Live-Stimmen: `ara`, `eve`, `leo`, `rex`, `sal`, `una`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlIiB0eXBlPSJzdHJpbmci BCP-47-Sprachcode oder `auto`. Standard `en`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJ3YXYiIHwgInBjbSIgfCAibXVsYXciIHwgImFsYXciJw Standard `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Xiaomi MiMo

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `XIAOMI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Standard `https://api.xiaomimimo.com/v1`. Env: `XIAOMI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Standard `mimo-v2.5-tts`. Env: `XIAOMI_TTS_MODEL`. Unterstützt auch `mimo-v2-tts`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Standard `mimo_default`. Env: `XIAOMI_TTS_VOICE`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImZvcm1hdCIgdHlwZT0nIm1wMyIgfCAid2F2Iic Standard `mp3`. Env: `XIAOMI_TTS_FORMAT`. OPENCLAW_DOCS_MARKER:paramClose:

## Agenten-Tool

Das Tool `tts` wandelt Text in Sprache um und gibt einen Audio-Anhang für die Antwortzustellung zurück. In Feishu, Matrix, Telegram und WhatsApp wird das Audio als Sprachnachricht statt als Datei-Anhang zugestellt. Feishu und WhatsApp können auf diesem Pfad Nicht-Opus-TTS-Ausgaben transkodieren, wenn `ffmpeg` verfügbar ist.

WhatsApp sendet Audio über Baileys als PTT-Sprachnotiz (`audio` mit `ptt: true`) und sendet sichtbaren Text **separat** von PTT-Audio, da Clients Beschriftungen auf Sprachnotizen nicht zuverlässig anzeigen.

Das Tool akzeptiert optionale Felder `channel` und `timeoutMs`; `timeoutMs` ist ein anrufbezogener Provider-Anfrage-Timeout in Millisekunden.

## Gateway-RPC

Methode | Zweck  
---|---  
`tts.status` | Aktuellen TTS-Status und letzten Versuch lesen.  
`tts.enable` | Lokale Auto-Präferenz auf `always` setzen.  
`tts.disable` | Lokale Auto-Präferenz auf `off` setzen.  
`tts.convert` | Einmalige Text-→-Audio-Konvertierung.  
`tts.setProvider` | Lokale Provider-Präferenz setzen.  
`tts.setPersona` | Lokale Persona-Präferenz setzen.  
`tts.providers` | Konfigurierte Provider und Status auflisten.  
  
## Service-Links

  * [OpenAI-Leitfaden für Text-to-Speech](<https://platform.openai.com/docs/guides/text-to-speech>)
  * [OpenAI Audio API-Referenz](<https://platform.openai.com/docs/api-reference/audio>)
  * [Azure Speech REST Text-to-Speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)
  * [Azure Speech Provider](</de/providers/azure-speech>)
  * [ElevenLabs Text to Speech](<https://elevenlabs.io/docs/api-reference/text-to-speech>)
  * [ElevenLabs-Authentifizierung](<https://elevenlabs.io/docs/api-reference/authentication>)
  * [Gradium](</de/providers/gradium>)
  * [Inworld TTS API](<https://docs.inworld.ai/tts/tts>)
  * [MiniMax T2A v2 API](<https://platform.minimaxi.com/document/T2A%20V2>)
  * [Volcengine TTS HTTP API](</de/providers/volcengine#text-to-speech>)
  * [Xiaomi MiMo-Sprachsynthese](</de/providers/xiaomi#text-to-speech>)
  * [node-edge-tts](<https://github.com/SchneeHertz/node-edge-tts>)
  * [Microsoft Speech-Ausgabeformate](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech#audio-outputs>)
  * [xAI Text-to-Speech](<https://docs.x.ai/developers/rest-api-reference/inference/voice#text-to-speech-rest>)


## Verwandt

  * [Medienüberblick](</de/tools/media-overview>)
  * [Musikgenerierung](</de/tools/music-generation>)
  * [Videogenerierung](</de/tools/video-generation>)
  * [Slash-Befehle](</de/tools/slash-commands>)
  * [Sprachanruf-Plugin](</de/plugins/voice-call>)


Was this useful?YesNo