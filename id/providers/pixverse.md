---
title: PixVerse
source_url: https://docs.openclaw.ai/id/providers/pixverse
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw menyediakan `pixverse` sebagai Plugin eksternal resmi untuk pembuatan video PixVerse yang dihosting. Plugin ini mendaftarkan penyedia `pixverse` terhadap kontrak `videoGenerationProviders`.

Properti | Nilai  
---|---  
ID penyedia | `pixverse`  
Paket Plugin | `@openclaw/pixverse-provider`  
Variabel env auth | `PIXVERSE_API_KEY`  
Flag onboarding | `--auth-choice pixverse-api-key`  
Flag CLI langsung | `--pixverse-api-key <key>`  
API | PixVerse Platform API v2 (pengiriman `video_id` plus polling hasil)  
Model default | `pixverse/v6`  
Wilayah API default | Internasional  
  
## Memulai

* ### Instal Plugin

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/pixverse-provideropenclaw gateway restart
[/code]

* ### Atur kunci API

bashCopy code
[code]
    openclaw onboard --auth-choice pixverse-api-key
[/code]

Wizard menanyakan apakah akan menggunakan endpoint Internasional (`https://app-api.pixverse.ai/openapi/v2`) atau endpoint CN (`https://app-api.pixverseai.cn/openapi/v2`) sebelum menulis `region` dan `baseUrl` ke dalam konfigurasi penyedia.

* ### Atur PixVerse sebagai penyedia video default

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "pixverse/v6"
[/code]

* ### Buat video

Minta agen untuk membuat video. PixVerse akan digunakan secara otomatis.

## Mode dan model yang didukung

Penyedia mengekspos model pembuatan PixVerse melalui alat video bersama OpenClaw.

Mode | Model | Input referensi  
---|---|---  
Teks-ke-video | `v6` (default), `c1` | Tidak ada  
Gambar-ke-video | `v6` (default), `c1` | 1 gambar lokal atau jarak jauh  
  
Referensi gambar lokal diunggah ke PixVerse sebelum permintaan gambar-ke-video. URL gambar jarak jauh diteruskan melalui endpoint unggah gambar PixVerse sebagai `image_url`.

Opsi | Nilai yang didukung  
---|---  
Durasi | 1-15 detik  
Resolusi | `360P`, `540P`, `720P`, `1080P`  
Rasio aspek | `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `2:3`, `3:2`, `21:9` untuk teks-ke-video  
Audio yang dihasilkan | `audio: true`  
  
## Opsi penyedia

Penyedia video menerima kunci opsional khusus penyedia berikut:

Opsi | Tipe | Efek  
---|---|---  
`seed` | number | Seed deterministik saat didukung  
`negativePrompt` / `negative_prompt` | string | Prompt negatif  
`quality` | string | Kualitas PixVerse seperti `720p`  
`motionMode` / `motion_mode` | string | Mode gerakan gambar-ke-video  
`cameraMovement` / `camera_movement` | string | Preset gerakan kamera PixVerse  
`templateId` / `template_id` | number | ID templat PixVerse yang diaktifkan  
  
## Konfigurasi

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "pixverse/v6",      },    },  },}
[/code]

## Konfigurasi lanjutan

Wilayah API

OpenClaw secara default menggunakan API PixVerse internasional. Atur `models.providers.pixverse.region` secara manual saat kunci Anda berasal dari wilayah platform PixVerse tertentu, atau gunakan `openclaw onboard --auth-choice pixverse-api-key` untuk memilihnya di wizard penyiapan:

Nilai wilayah | URL dasar API PixVerse  
---|---  
`international` | `https://app-api.pixverse.ai/openapi/v2`  
`cn` | `https://app-api.pixverseai.cn/openapi/v2`  
  
json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        region: "cn", // "international" or "cn"        baseUrl: "https://app-api.pixverseai.cn/openapi/v2",        models: [],      },    },  },}
[/code]

URL dasar khusus

Atur `models.providers.pixverse.baseUrl` hanya saat merutekan melalui proxy kompatibel yang tepercaya. `baseUrl` lebih diprioritaskan daripada `region`.

json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        baseUrl: "https://app-api.pixverse.ai/openapi/v2",      },    },  },}
[/code]

Polling tugas

PixVerse mengembalikan `video_id` dari permintaan pembuatan. OpenClaw melakukan polling `/openapi/v2/video/result/{video_id}` hingga tugas berhasil, gagal, atau waktu habis.

## Terkait

[**Pembuatan video** Parameter alat bersama, pemilihan penyedia, dan perilaku asinkron. ](</id/tools/video-generation>) [**Referensi konfigurasi** Pengaturan default agen termasuk model pembuatan video. ](</id/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue