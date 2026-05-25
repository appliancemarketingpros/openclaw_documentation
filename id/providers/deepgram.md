---
title: Deepgram
source_url: https://docs.openclaw.ai/id/providers/deepgram
scraped_at: 2026-05-25
---

Deepgram adalah API speech-to-text. Di OpenClaw, Deepgram digunakan untuk transkripsi audio/voice note masuk melalui `tools.media.audio` dan untuk STT streaming Voice Call melalui `plugins.entries.voice-call.config.streaming`.

Untuk transkripsi batch, OpenClaw mengunggah file audio lengkap ke Deepgram dan menyisipkan transkrip ke pipeline balasan (`{{Transcript}}` \+ blok `[Audio]`). Untuk Voice Call streaming, OpenClaw meneruskan frame G.711 u-law langsung melalui endpoint WebSocket `listen` milik Deepgram dan memancarkan transkrip parsial atau final saat Deepgram mengembalikannya.

Detail | Nilai  
---|---  
Website | [deepgram.com](<https://deepgram.com>)  
Docs | [developers.deepgram.com](<https://developers.deepgram.com>)  
Auth | `DEEPGRAM_API_KEY`  
Model default | `nova-3`  
  
## Memulai

* ### Set your API key

Tambahkan API key Deepgram Anda ke environment:

CodeCopy code
[code]
    DEEPGRAM_API_KEY=dg_...
[/code]

* ### Enable the audio provider

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

* ### Send a voice note

Kirim pesan audio melalui channel terhubung apa pun. OpenClaw mentranskripsikannya melalui Deepgram dan menyisipkan transkrip ke pipeline balasan.

## Opsi konfigurasi

Option | Path | Deskripsi  
---|---|---  
`model` | `tools.media.audio.models[].model` | ID model Deepgram (default: `nova-3`)  
`language` | `tools.media.audio.models[].language` | Petunjuk bahasa (opsional)  
`detect_language` | `tools.media.audio.providerOptions.deepgram.detect_language` | Aktifkan deteksi bahasa (opsional)  
`punctuate` | `tools.media.audio.providerOptions.deepgram.punctuate` | Aktifkan tanda baca (opsional)  
`smart_format` | `tools.media.audio.providerOptions.deepgram.smart_format` | Aktifkan pemformatan cerdas (opsional)  
  
### With language hint

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3", language: "en" }],      },    },  },}
[/code]

### With Deepgram options

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        providerOptions: {          deepgram: {            detect_language: true,            punctuate: true,            smart_format: true,          },        },        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

## Voice Call streaming STT

Plugin `deepgram` bawaan juga mendaftarkan provider transkripsi realtime untuk plugin Voice Call.

Setting | Path konfigurasi | Default  
---|---|---  
API key | `plugins.entries.voice-call.config.streaming.providers.deepgram.apiKey` | Fallback ke `DEEPGRAM_API_KEY`  
Model | `...deepgram.model` | `nova-3`  
Language | `...deepgram.language` | (tidak disetel)  
Encoding | `...deepgram.encoding` | `mulaw`  
Sample rate | `...deepgram.sampleRate` | `8000`  
Endpointing | `...deepgram.endpointingMs` | `800`  
Interim results | `...deepgram.interimResults` | `true`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "deepgram",            providers: {              deepgram: {                apiKey: "${DEEPGRAM_API_KEY}",                model: "nova-3",                endpointingMs: 800,                language: "en-US",              },            },          },        },      },    },  },}
[/code]

## Catatan

Authentication

Auth mengikuti urutan auth provider standar. `DEEPGRAM_API_KEY` adalah jalur yang paling sederhana.

Proxy and custom endpoints

Timpa endpoint atau header dengan `tools.media.audio.baseUrl` dan `tools.media.audio.headers` saat menggunakan proxy.

Output behavior

Output mengikuti aturan audio yang sama seperti provider lain (batas ukuran, timeout, penyisipan transkrip).

## Terkait

[**Media tools** Ikhtisar pipeline pemrosesan audio, gambar, dan video. ](</id/tools/media-overview>) [**Configuration** Referensi konfigurasi lengkap termasuk pengaturan tool media. ](</id/gateway/configuration>) [**Troubleshooting** Masalah umum dan langkah debug. ](</id/help/troubleshooting>) [**FAQ** Pertanyaan umum tentang penyiapan OpenClaw. ](</id/help/faq>)

Was this useful?YesNo