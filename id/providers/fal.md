---
title: Fal
source_url: https://docs.openclaw.ai/id/providers/fal
scraped_at: 2026-05-25
---

OpenClaw menyertakan penyedia `fal` bawaan untuk pembuatan gambar dan video yang dihosting.

Properti | Nilai  
---|---  
Penyedia | `fal`  
Autentikasi | `FAL_KEY` (kanonis; `FAL_API_KEY` juga berfungsi sebagai fallback)  
API | endpoint model fal  
  
## Memulai

* ### Tetapkan kunci API

bashCopy code
[code]
    openclaw onboard --auth-choice fal-api-key
[/code]

* ### Tetapkan model gambar default

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Pembuatan gambar

Penyedia pembuatan gambar `fal` bawaan secara default menggunakan `fal/fal-ai/flux/dev`.

Kemampuan | Nilai  
---|---  
Gambar maksimum | 4 per permintaan  
Mode edit | Flux: 1 gambar referensi; GPT Image 2: 10; Nano Banana 2: 14  
Penggantian ukuran | Didukung  
Rasio aspek | Didukung untuk generate dan edit GPT Image 2/Nano Banana 2  
Resolusi | Didukung  
Format keluaran | `png` atau `jpeg`  
  
Gunakan `outputFormat: "png"` saat Anda menginginkan keluaran PNG. fal tidak mendeklarasikan kontrol latar belakang transparan eksplisit di OpenClaw, sehingga `background: "transparent"` dilaporkan sebagai penggantian yang diabaikan untuk model fal.

Untuk menggunakan fal sebagai penyedia gambar default:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Pembuatan video

Penyedia pembuatan video `fal` bawaan secara default menggunakan `fal/fal-ai/minimax/video-01-live`.

Kemampuan | Nilai  
---|---  
Mode | Teks-ke-video, referensi gambar tunggal, referensi-ke-video Seedance  
Runtime | Alur submit/status/result berbasis antrean untuk pekerjaan berdurasi lama  
  
Model video yang tersedia

**Agen video HeyGen:**

  * `fal/fal-ai/heygen/v2/video-agent`


**Seedance 2.0:**

  * `fal/bytedance/seedance-2.0/fast/text-to-video`
  * `fal/bytedance/seedance-2.0/fast/image-to-video`
  * `fal/bytedance/seedance-2.0/fast/reference-to-video`
  * `fal/bytedance/seedance-2.0/text-to-video`
  * `fal/bytedance/seedance-2.0/image-to-video`
  * `fal/bytedance/seedance-2.0/reference-to-video`

Contoh config Seedance 2.0 json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/text-to-video",      },    },  },}
[/code]

Contoh config reference-to-video Seedance 2.0 json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/reference-to-video",      },    },  },}
[/code]

Reference-to-video menerima hingga 9 gambar, 3 video, dan 3 referensi audio melalui parameter bersama `video_generate` `images`, `videos`, dan `audioRefs`, dengan total maksimal 12 file referensi.

Contoh config agen video HeyGen json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/fal-ai/heygen/v2/video-agent",      },    },  },}
[/code]

## Terkait

[**Pembuatan gambar** Parameter alat gambar bersama dan pemilihan penyedia. ](</id/tools/image-generation>) [**Pembuatan video** Parameter alat video bersama dan pemilihan penyedia. ](</id/tools/video-generation>) [**Referensi konfigurasi** Default agen termasuk pemilihan model gambar dan video. ](</id/gateway/config-agents#agent-defaults>)

Was this useful?YesNo