---
title: SenseAudio
source_url: https://docs.openclaw.ai/id/providers/senseaudio
scraped_at: 2026-05-25
---

SenseAudio dapat mentranskripsi audio masuk dan lampiran catatan suara melalui pipeline bersama `tools.media.audio` OpenClaw. OpenClaw mengirim audio multipart ke endpoint transkripsi yang kompatibel dengan OpenAI dan menyisipkan teks yang dikembalikan sebagai `{{Transcript}}` ditambah blok `[Audio]`.

Properti | Nilai  
---|---  
Id penyedia | `senseaudio`  
Plugin | dibundel, `enabledByDefault: true`  
Kontrak | `mediaUnderstandingProviders` (audio)  
Var env autentikasi | `SENSEAUDIO_API_KEY`  
Model default | `senseaudio-asr-pro-1.5-260319`  
URL default | `https://api.senseaudio.cn/v1`  
Situs web | [senseaudio.cn](<https://senseaudio.cn>)  
Dokumentasi | [senseaudio.cn/docs](<https://senseaudio.cn/docs>)  
  
## Memulai

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

Kirim pesan audio melalui channel apa pun yang terhubung. OpenClaw mengunggah audio ke SenseAudio dan menggunakan transkrip dalam pipeline balasan.

## Opsi

Opsi | Path | Deskripsi  
---|---|---  
`model` | `tools.media.audio.models[].model` | Id model ASR SenseAudio  
`language` | `tools.media.audio.models[].language` | Petunjuk bahasa opsional  
`prompt` | `tools.media.audio.prompt` | Prompt transkripsi opsional  
`baseUrl` | `tools.media.audio.baseUrl` or model | Timpa basis yang kompatibel dengan OpenAI  
`headers` | `tools.media.audio.request.headers` | Header permintaan tambahan  
  
## Terkait

  * [Pemahaman media (audio)](</id/nodes/audio>)
  * [Penyedia model](</id/concepts/model-providers>)


Was this useful?YesNo