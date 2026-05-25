---
title: Vydra
source_url: https://docs.openclaw.ai/id/providers/vydra
scraped_at: 2026-05-25
---

Plugin Vydra bawaan menambahkan:

  * Pembuatan gambar melalui `vydra/grok-imagine`
  * Pembuatan video melalui `vydra/veo3` dan `vydra/kling`
  * Sintesis ucapan melalui rute TTS Vydra yang didukung ElevenLabs


OpenClaw menggunakan `VYDRA_API_KEY` yang sama untuk ketiga kapabilitas tersebut.

Properti | Nilai  
---|---  
ID penyedia | `vydra`  
Plugin | bawaan, `enabledByDefault: true`  
Variabel env auth | `VYDRA_API_KEY`  
Flag onboarding | `--auth-choice vydra-api-key`  
Flag CLI langsung | `--vydra-api-key <key>`  
Kontrak | `imageGenerationProviders`, `videoGenerationProviders`, `speechProviders`  
URL dasar | `https://www.vydra.ai/api/v1` (gunakan host `www`)  
  
## Penyiapan

* ### Jalankan onboarding interaktif

bashCopy code
[code]
    openclaw onboard --auth-choice vydra-api-key
[/code]

Atau atur variabel env secara langsung:

bashCopy code
[code]
    export VYDRA_API_KEY="vydra_live_..."
[/code]

* ### Pilih kapabilitas default

Pilih satu atau beberapa kapabilitas di bawah ini (gambar, video, atau ucapan) dan terapkan konfigurasi yang sesuai.

## Kapabilitas

Pembuatan gambar

Model gambar default:

  * `vydra/grok-imagine`


Tetapkan sebagai penyedia gambar default:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "vydra/grok-imagine",      },    },  },}
[/code]

Dukungan bawaan saat ini hanya teks-ke-gambar. Rute edit yang dihosting Vydra mengharapkan URL gambar jarak jauh, dan OpenClaw belum menambahkan jembatan unggah khusus Vydra di Plugin bawaan.

Pembuatan video

Model video terdaftar:

  * `vydra/veo3` untuk teks-ke-video
  * `vydra/kling` untuk gambar-ke-video


Tetapkan Vydra sebagai penyedia video default:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "vydra/veo3",      },    },  },}
[/code]

Catatan:

  * `vydra/veo3` dibundel hanya sebagai teks-ke-video.
  * `vydra/kling` saat ini memerlukan referensi URL gambar jarak jauh. Unggahan file lokal ditolak sejak awal.
  * Rute HTTP `kling` Vydra saat ini tidak konsisten mengenai apakah memerlukan `image_url` atau `video_url`; penyedia bawaan memetakan URL gambar jarak jauh yang sama ke kedua bidang.
  * Plugin bawaan tetap konservatif dan tidak meneruskan pengaturan gaya yang tidak terdokumentasi seperti rasio aspek, resolusi, watermark, atau audio yang dihasilkan.

Pengujian live video

Cakupan live khusus penyedia:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_VYDRA_VIDEO=1 \pnpm test:live -- extensions/vydra/vydra.live.test.ts
[/code]

File live Vydra bawaan kini mencakup:

  * `vydra/veo3` teks-ke-video
  * `vydra/kling` gambar-ke-video menggunakan URL gambar jarak jauh


Timpa fixture gambar jarak jauh bila diperlukan:

bashCopy code
[code]
    export OPENCLAW_LIVE_VYDRA_KLING_IMAGE_URL="https://example.com/reference.png"
[/code]

Sintesis ucapan

Tetapkan Vydra sebagai penyedia ucapan:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "vydra",      providers: {        vydra: {          apiKey: "${VYDRA_API_KEY}",          voiceId: "21m00Tcm4TlvDq8ikWAM",        },      },    },  },}
[/code]

Default:

  * Model: `elevenlabs/tts`
  * ID suara: `21m00Tcm4TlvDq8ikWAM`


Plugin bawaan saat ini mengekspos satu suara default yang telah terbukti baik dan mengembalikan file audio MP3.

## Terkait

[**Direktori penyedia** Jelajahi semua penyedia yang tersedia. ](</id/providers>) [**Pembuatan gambar** Parameter alat gambar bersama dan pemilihan penyedia. ](</id/tools/image-generation>) [**Pembuatan video** Parameter alat video bersama dan pemilihan penyedia. ](</id/tools/video-generation>) [**Referensi konfigurasi** Default agen dan konfigurasi model. ](</id/gateway/config-agents#agent-defaults>)

Was this useful?YesNo