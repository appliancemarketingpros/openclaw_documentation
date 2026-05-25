---
title: Together AI
source_url: https://docs.openclaw.ai/id/providers/together
scraped_at: 2026-05-25
---

[Together AI](<https://together.ai>) menyediakan akses ke model open-source terkemuka termasuk Llama, DeepSeek, Kimi, dan lainnya melalui API terpadu.

Properti | Nilai  
---|---  
Penyedia | `together`  
Autentikasi | `TOGETHER_API_KEY`  
API | Kompatibel dengan OpenAI  
URL dasar | `https://api.together.xyz/v1`  
  
## Memulai

* ### Dapatkan kunci API

Buat kunci API di [api.together.ai/settings/api-keys](<https://api.together.ai/settings/api-keys>).

* ### Jalankan onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice together-api-key
[/code]

* ### Tetapkan model default

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "together/moonshotai/Kimi-K2.5" },    },  },}
[/code]

### Contoh noninteraktif

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice together-api-key \  --together-api-key "$TOGETHER_API_KEY"
[/code]

## Katalog bawaan

OpenClaw menyertakan katalog Together bawaan ini:

Ref model | Nama | Input | Konteks | Catatan  
---|---|---|---|---  
`together/moonshotai/Kimi-K2.5` | Kimi K2.5 | teks, gambar | 262,144 | Model default; penalaran diaktifkan  
`together/zai-org/GLM-4.7` | GLM 4.7 Fp8 | teks | 202,752 | Model teks serbaguna  
`together/meta-llama/Llama-3.3-70B-Instruct-Turbo` | Llama 3.3 70B Instruct Turbo | teks | 131,072 | Model instruksi cepat  
`together/meta-llama/Llama-4-Scout-17B-16E-Instruct` | Llama 4 Scout 17B 16E Instruct | teks, gambar | 10,000,000 | Multimodal  
`together/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | Llama 4 Maverick 17B 128E Instruct FP8 | teks, gambar | 20,000,000 | Multimodal  
`together/deepseek-ai/DeepSeek-V3.1` | DeepSeek V3.1 | teks | 131,072 | Model teks umum  
`together/deepseek-ai/DeepSeek-R1` | DeepSeek R1 | teks | 131,072 | Model penalaran  
`together/moonshotai/Kimi-K2-Instruct-0905` | Kimi K2-Instruct 0905 | teks | 262,144 | Model teks Kimi sekunder  
  
## Pembuatan video

Plugin `together` bawaan juga mendaftarkan pembuatan video melalui alat bersama `video_generate`.

Properti | Nilai  
---|---  
Model video default | `together/Wan-AI/Wan2.2-T2V-A14B`  
Mode | teks-ke-video, referensi gambar tunggal  
Parameter yang didukung | `aspectRatio`, `resolution`  
  
Untuk menggunakan Together sebagai penyedia video default:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "together/Wan-AI/Wan2.2-T2V-A14B",      },    },  },}
[/code]

Catatan lingkungan

Jika Gateway berjalan sebagai daemon (launchd/systemd), pastikan `TOGETHER_API_KEY` tersedia untuk proses tersebut (misalnya, di `~/.openclaw/.env` atau melalui `env.shellEnv`).

Pemecahan masalah

  * Verifikasi kunci Anda berfungsi: `openclaw models list --provider together`
  * Jika model tidak muncul, pastikan kunci API diatur di lingkungan yang benar untuk proses Gateway Anda.
  * Ref model menggunakan bentuk `together/<model-id>`.


## Terkait

[**Pemilihan model** Aturan penyedia, ref model, dan perilaku failover. ](</id/concepts/model-providers>) [**Pembuatan video** Parameter alat pembuatan video bersama dan pemilihan penyedia. ](</id/tools/video-generation>) [**Referensi konfigurasi** Skema konfigurasi lengkap termasuk pengaturan penyedia. ](</id/gateway/configuration-reference>) [**Together AI** Dasbor Together AI, dokumentasi API, dan harga. ](<https://together.ai>)

Was this useful?YesNo