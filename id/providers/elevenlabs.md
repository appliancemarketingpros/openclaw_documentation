---
title: ElevenLabs
source_url: https://docs.openclaw.ai/id/providers/elevenlabs
scraped_at: 2026-05-25
---

OpenClaw menggunakan ElevenLabs untuk text-to-speech, speech-to-text batch dengan Scribe v2, dan STT streaming dengan Scribe v2 Realtime.

Kemampuan | Permukaan OpenClaw | Bawaan  
---|---|---  
Text-to-speech | `messages.tts` / `talk` | `eleven_multilingual_v2`  
Speech-to-text batch | `tools.media.audio` | `scribe_v2`  
Speech-to-text streaming | Streaming Voice Call atau Google Meet `realtime.transcriptionProvider` | `scribe_v2_realtime`  
  
## Autentikasi

Atur `ELEVENLABS_API_KEY` di lingkungan. `XI_API_KEY` juga diterima untuk kompatibilitas dengan tooling ElevenLabs yang sudah ada.

bashCopy code
[code]
    export ELEVENLABS_API_KEY="..."
[/code]

## Text-to-speech

json5Copy code
[code]
    {  messages: {    tts: {      providers: {        elevenlabs: {          apiKey: "${ELEVENLABS_API_KEY}",          voiceId: "pMsXgVXv3BLzUgSXRplE",          modelId: "eleven_multilingual_v2",        },      },    },  },}
[/code]

Atur `modelId` ke `eleven_v3` untuk menggunakan ElevenLabs v3 TTS. OpenClaw mempertahankan `eleven_multilingual_v2` sebagai bawaan untuk instalasi yang sudah ada.

Saluran suara Discord menggunakan endpoint TTS streaming ElevenLabs saat ElevenLabs menjadi penyedia `voice.tts`/`messages.tts` yang dipilih. Pemutaran dimulai dari stream audio yang dikembalikan alih-alih menunggu OpenClaw mengunduh dan menulis seluruh file audio terlebih dahulu. `latencyTier` dipetakan ke parameter kueri ElevenLabs `optimize_streaming_latency` untuk model yang menerimanya; OpenClaw menghilangkan parameter tersebut untuk `eleven_v3`, yang menolaknya.

## Speech-to-text

Gunakan Scribe v2 untuk lampiran audio masuk dan segmen suara rekaman pendek:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "elevenlabs", model: "scribe_v2" }],      },    },  },}
[/code]

OpenClaw mengirim audio multipart ke ElevenLabs `/v1/speech-to-text` dengan `model_id: "scribe_v2"`. Petunjuk bahasa dipetakan ke `language_code` bila ada.

## STT Streaming

Plugin `elevenlabs` bawaan mendaftarkan Scribe v2 Realtime untuk transkripsi streaming mode agen Voice Call dan Google Meet.

Pengaturan | Jalur konfigurasi | Bawaan  
---|---|---  
Kunci API | `plugins.entries.voice-call.config.streaming.providers.elevenlabs.apiKey` | Beralih ke `ELEVENLABS_API_KEY` / `XI_API_KEY`  
Model | `...elevenlabs.modelId` | `scribe_v2_realtime`  
Format audio | `...elevenlabs.audioFormat` | `ulaw_8000`  
Laju sampel | `...elevenlabs.sampleRate` | `8000`  
Strategi commit | `...elevenlabs.commitStrategy` | `vad`  
Bahasa | `...elevenlabs.languageCode` | (belum diatur)  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "elevenlabs",            providers: {              elevenlabs: {                apiKey: "${ELEVENLABS_API_KEY}",                audioFormat: "ulaw_8000",                commitStrategy: "vad",                languageCode: "en",              },            },          },        },      },    },  },}
[/code]

Untuk mode agen Google Meet, atur `plugins.entries.google-meet.config.realtime.transcriptionProvider` ke `"elevenlabs"` dan konfigurasikan blok penyedia yang sama di bawah `plugins.entries.google-meet.config.realtime.providers.elevenlabs`.

## Terkait

  * [Text-to-speech](</id/tools/tts>)
  * [Google Meet](</id/plugins/google-meet>)
  * [Pemilihan model](</id/concepts/model-providers>)


Was this useful?YesNo