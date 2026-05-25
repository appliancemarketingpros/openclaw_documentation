---
title: Runway
source_url: https://docs.openclaw.ai/id/providers/runway
scraped_at: 2026-05-25
---

OpenClaw menyertakan penyedia `runway` bawaan untuk pembuatan video yang dihosting. Plugin ini diaktifkan secara default dan mendaftarkan penyedia `runway` pada kontrak `videoGenerationProviders`.

Properti | Nilai  
---|---  
ID penyedia | `runway`  
Plugin | bawaan, `enabledByDefault: true`  
Variabel env auth | `RUNWAYML_API_SECRET` (kanonis) atau `RUNWAY_API_KEY`  
Flag onboarding | `--auth-choice runway-api-key`  
Flag CLI langsung | `--runway-api-key <key>`  
API | Pembuatan video berbasis tugas Runway (polling `GET /v1/tasks/{id}`)  
Model default | `runway/gen4.5`  
  
## Mulai

* ### Tetapkan kunci API

bashCopy code
[code]
    openclaw onboard --auth-choice runway-api-key
[/code]

* ### Tetapkan Runway sebagai penyedia video default

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "runway/gen4.5"
[/code]

* ### Buat video

Minta agent untuk membuat video. Runway akan digunakan secara otomatis.

## Mode dan model yang didukung

Penyedia ini mengekspos tujuh model Runway yang dibagi ke dalam tiga mode. ID model yang sama dapat melayani lebih dari satu mode (misalnya `gen4.5` berfungsi untuk teks-ke-video dan gambar-ke-video).

Mode | Model | Input referensi  
---|---|---  
Teks-ke-video | `gen4.5` (default), `veo3.1`, `veo3.1_fast`, `veo3` | Tidak ada  
Gambar-ke-video | `gen4.5`, `gen4_turbo`, `gen3a_turbo`, `veo3.1`, `veo3.1_fast`, `veo3` | 1 gambar lokal atau remote  
Video-ke-video | `gen4_aleph` | 1 video lokal atau remote  
  
Referensi gambar dan video lokal didukung melalui URI data.

Rasio aspek | Nilai yang diizinkan  
---|---  
Teks-ke-video | `16:9`, `9:16`  
Edit gambar dan video | `1:1`, `16:9`, `9:16`, `3:4`, `4:3`, `21:9`  
  
## Konfigurasi

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "runway/gen4.5",      },    },  },}
[/code]

## Konfigurasi lanjutan

Alias variabel lingkungan

OpenClaw mengenali `RUNWAYML_API_SECRET` (kanonis) dan `RUNWAY_API_KEY`. Salah satu variabel tersebut akan mengautentikasi penyedia Runway.

Polling tugas

Runway menggunakan API berbasis tugas. Setelah mengirimkan permintaan pembuatan, OpenClaw melakukan polling `GET /v1/tasks/{id}` sampai video siap. Tidak ada konfigurasi tambahan yang diperlukan untuk perilaku polling.

## Terkait

[**Pembuatan video** Parameter alat bersama, pemilihan penyedia, dan perilaku asinkron. ](</id/tools/video-generation>) [**Referensi konfigurasi** Pengaturan default agent termasuk model pembuatan video. ](</id/gateway/config-agents#agent-defaults>)

Was this useful?YesNo