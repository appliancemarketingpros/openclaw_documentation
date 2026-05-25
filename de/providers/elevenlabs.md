---
title: ElevenLabs
source_url: https://docs.openclaw.ai/de/providers/elevenlabs
scraped_at: 2026-05-25
---

OpenClaw verwendet ElevenLabs für Text-zu-Sprache, Batch-Spracherkennung mit Scribe v2 und Streaming-STT mit Scribe v2 Realtime.

Funktion | OpenClaw-Oberfläche | Standard  
---|---|---  
Text-zu-Sprache | `messages.tts` / `talk` | `eleven_multilingual_v2`  
Batch-Spracherkennung | `tools.media.audio` | `scribe_v2`  
Streaming-Spracherkennung | Voice Call-Streaming oder Google Meet `realtime.transcriptionProvider` | `scribe_v2_realtime`  
  
## Authentifizierung

Setzen Sie `ELEVENLABS_API_KEY` in der Umgebung. `XI_API_KEY` wird zur Kompatibilität mit bestehenden ElevenLabs-Tools ebenfalls akzeptiert.

bashCopy code
[code]
    export ELEVENLABS_API_KEY="..."
[/code]

## Text-zu-Sprache

json5Copy code
[code]
    {  messages: {    tts: {      providers: {        elevenlabs: {          apiKey: "${ELEVENLABS_API_KEY}",          voiceId: "pMsXgVXv3BLzUgSXRplE",          modelId: "eleven_multilingual_v2",        },      },    },  },}
[/code]

Setzen Sie `modelId` auf `eleven_v3`, um ElevenLabs v3 TTS zu verwenden. OpenClaw behält `eleven_multilingual_v2` als Standard für bestehende Installationen bei.

Discord-Sprachkanäle verwenden den Streaming-TTS-Endpunkt von ElevenLabs, wenn ElevenLabs der ausgewählte `voice.tts`-/`messages.tts`-Provider ist. Die Wiedergabe startet aus dem zurückgegebenen Audiostream, anstatt zuerst darauf zu warten, dass OpenClaw die gesamte Audiodatei herunterlädt und schreibt. `latencyTier` wird für Modelle, die dies akzeptieren, dem ElevenLabs-Abfrageparameter `optimize_streaming_latency` zugeordnet; OpenClaw lässt diesen Parameter für `eleven_v3` weg, da es ihn ablehnt.

## Sprache-zu-Text

Verwenden Sie Scribe v2 für eingehende Audioanhänge und kurze aufgezeichnete Sprachsegmente:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "elevenlabs", model: "scribe_v2" }],      },    },  },}
[/code]

OpenClaw sendet Multipart-Audio an ElevenLabs `/v1/speech-to-text` mit `model_id: "scribe_v2"`. Sprachhinweise werden, sofern vorhanden, `language_code` zugeordnet.

## Streaming-STT

Das gebündelte `elevenlabs`-Plugin registriert Scribe v2 Realtime für Voice Call und Streaming-Transkription im Google Meet-Agentenmodus.

Einstellung | Konfigurationspfad | Standard  
---|---|---  
API-Schlüssel | `plugins.entries.voice-call.config.streaming.providers.elevenlabs.apiKey` | Fällt auf `ELEVENLABS_API_KEY` / `XI_API_KEY` zurück  
Modell | `...elevenlabs.modelId` | `scribe_v2_realtime`  
Audioformat | `...elevenlabs.audioFormat` | `ulaw_8000`  
Abtastrate | `...elevenlabs.sampleRate` | `8000`  
Commit-Strategie | `...elevenlabs.commitStrategy` | `vad`  
Sprache | `...elevenlabs.languageCode` | (nicht gesetzt)  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "elevenlabs",            providers: {              elevenlabs: {                apiKey: "${ELEVENLABS_API_KEY}",                audioFormat: "ulaw_8000",                commitStrategy: "vad",                languageCode: "en",              },            },          },        },      },    },  },}
[/code]

Für den Google Meet-Agentenmodus setzen Sie `plugins.entries.google-meet.config.realtime.transcriptionProvider` auf `"elevenlabs"` und konfigurieren denselben Provider-Block unter `plugins.entries.google-meet.config.realtime.providers.elevenlabs`.

## Verwandte Themen

  * [Text-zu-Sprache](</de/tools/tts>)
  * [Google Meet](</de/plugins/google-meet>)
  * [Modellauswahl](</de/concepts/model-providers>)


Was this useful?YesNo