---
title: Azure Speech
source_url: https://docs.openclaw.ai/id/providers/azure-speech
scraped_at: 2026-05-25
---

Azure Speech adalah provider text-to-speech Azure AI Speech. Di OpenClaw, provider ini mensintesis audio balasan keluar sebagai MP3 secara default, Ogg/Opus native untuk voice note, dan audio mulaw 8 kHz untuk saluran telepon seperti Voice Call.

OpenClaw menggunakan REST API Azure Speech secara langsung dengan SSML dan mengirim format output milik provider melalui `X-Microsoft-OutputFormat`.

Detail | Nilai  
---|---  
Situs web | [Azure AI Speech](<https://azure.microsoft.com/products/ai-services/ai-speech>)  
Dokumen | [Speech REST text-to-speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)  
Auth | `AZURE_SPEECH_KEY` plus `AZURE_SPEECH_REGION`  
Voice default | `en-US-JennyNeural`  
Output file default | `audio-24khz-48kbitrate-mono-mp3`  
File voice-note default | `ogg-24khz-16bit-mono-opus`  
  
## Memulai

* ### Buat resource Azure Speech

Di portal Azure, buat resource Speech. Salin **KEY 1** dari Resource Management > Keys and Endpoint, dan salin lokasi resource seperti `eastus`.

CodeCopy code
[code]
    AZURE_SPEECH_KEY=<speech-resource-key>AZURE_SPEECH_REGION=eastus
[/code]

* ### Pilih Azure Speech di messages.tts

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "azure-speech",      providers: {        "azure-speech": {          voice: "en-US-JennyNeural",          lang: "en-US",        },      },    },  },}
[/code]

* ### Kirim pesan

Kirim balasan melalui saluran terhubung apa pun. OpenClaw mensintesis audio dengan Azure Speech dan mengirim MP3 untuk audio standar, atau Ogg/Opus ketika saluran mengharapkan voice note.

## Opsi konfigurasi

Opsi | Path | Deskripsi  
---|---|---  
`apiKey` | `messages.tts.providers.azure-speech.apiKey` | Key resource Azure Speech. Fallback ke `AZURE_SPEECH_KEY`, `AZURE_SPEECH_API_KEY`, atau `SPEECH_KEY`.  
`region` | `messages.tts.providers.azure-speech.region` | Region resource Azure Speech. Fallback ke `AZURE_SPEECH_REGION` atau `SPEECH_REGION`.  
`endpoint` | `messages.tts.providers.azure-speech.endpoint` | Override endpoint/base URL Azure Speech opsional.  
`baseUrl` | `messages.tts.providers.azure-speech.baseUrl` | Override base URL Azure Speech opsional.  
`voice` | `messages.tts.providers.azure-speech.voice` | ShortName voice Azure (default `en-US-JennyNeural`).  
`lang` | `messages.tts.providers.azure-speech.lang` | Kode bahasa SSML (default `en-US`).  
`outputFormat` | `messages.tts.providers.azure-speech.outputFormat` | Format output file audio (default `audio-24khz-48kbitrate-mono-mp3`).  
`voiceNoteOutputFormat` | `messages.tts.providers.azure-speech.voiceNoteOutputFormat` | Format output voice note (default `ogg-24khz-16bit-mono-opus`).  
  
## Catatan

Autentikasi

Azure Speech menggunakan key resource Speech, bukan key Azure OpenAI. Key dikirim sebagai `Ocp-Apim-Subscription-Key`; OpenClaw menurunkan `https://<region>.tts.speech.microsoft.com` dari `region` kecuali Anda memberikan `endpoint` atau `baseUrl`.

Nama voice

Gunakan nilai `ShortName` voice Azure Speech, misalnya `en-US-JennyNeural`. Provider bawaan dapat mencantumkan voice melalui resource Speech yang sama dan memfilter voice yang ditandai deprecated atau retired.

Output audio

Azure menerima format output seperti `audio-24khz-48kbitrate-mono-mp3`, `ogg-24khz-16bit-mono-opus`, dan `riff-24khz-16bit-mono-pcm`. OpenClaw meminta Ogg/Opus untuk target `voice-note` agar saluran dapat mengirim gelembung suara native tanpa konversi MP3 tambahan.

Alias

`azure` diterima sebagai alias provider untuk PR yang sudah ada dan konfigurasi pengguna, tetapi konfigurasi baru sebaiknya menggunakan `azure-speech` agar tidak membingungkan dengan provider model Azure OpenAI.

## Terkait

[**Text-to-speech** Ringkasan TTS, provider, dan konfigurasi `messages.tts`. ](</id/tools/tts>) [**Konfigurasi** Referensi konfigurasi lengkap termasuk pengaturan `messages.tts`. ](</id/gateway/configuration>) [**Provider** Semua provider OpenClaw bawaan. ](</id/providers>) [**Pemecahan masalah** Masalah umum dan langkah debugging. ](</id/help/troubleshooting>)

Was this useful?YesNo