---
title: Chutes
source_url: https://docs.openclaw.ai/id/providers/chutes
scraped_at: 2026-05-25
---

[Chutes](<https://chutes.ai>) mengekspos katalog model sumber terbuka melalui API yang kompatibel dengan OpenAI. OpenClaw mendukung autentikasi OAuth melalui peramban dan kunci API langsung untuk penyedia `chutes` bawaan.

Properti | Nilai  
---|---  
Penyedia | `chutes`  
API | Kompatibel dengan OpenAI  
URL Dasar | `https://llm.chutes.ai/v1`  
Autentikasi | OAuth atau kunci API (lihat di bawah)  
  
## Memulai

### OAuth

* ### Jalankan alur onboarding OAuth

bashCopy code
[code]
    openclaw onboard --auth-choice chutes
[/code]

OpenClaw menjalankan alur peramban secara lokal, atau menampilkan URL + alur tempel-pengalihan pada host jarak jauh/headless. Token OAuth diperbarui otomatis melalui profil autentikasi OpenClaw.

* ### Verifikasi model default

Setelah onboarding, model default diatur ke `chutes/zai-org/GLM-4.7-TEE` dan katalog Chutes bawaan didaftarkan.

### Kunci API

* ### Dapatkan kunci API

Buat kunci di [chutes.ai/settings/api-keys](<https://chutes.ai/settings/api-keys>).

* ### Jalankan alur onboarding kunci API

bashCopy code
[code]
    openclaw onboard --auth-choice chutes-api-key
[/code]

* ### Verifikasi model default

Setelah onboarding, model default diatur ke `chutes/zai-org/GLM-4.7-TEE` dan katalog Chutes bawaan didaftarkan.

## Perilaku penemuan

Saat autentikasi Chutes tersedia, OpenClaw mengkueri katalog Chutes dengan kredensial tersebut dan menggunakan model yang ditemukan. Jika penemuan gagal, OpenClaw kembali ke katalog statis bawaan agar onboarding dan startup tetap berfungsi.

## Alias default

OpenClaw mendaftarkan tiga alias praktis untuk katalog Chutes bawaan:

Alias | Model target  
---|---  
`chutes-fast` | `chutes/zai-org/GLM-4.7-FP8`  
`chutes-pro` | `chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes-vision` | `chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
  
## Katalog awal bawaan

Katalog fallback bawaan mencakup ref Chutes saat ini:

Ref model  
---  
`chutes/zai-org/GLM-4.7-TEE`  
`chutes/zai-org/GLM-5-TEE`  
`chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes/deepseek-ai/DeepSeek-R1-0528-TEE`  
`chutes/moonshotai/Kimi-K2.5-TEE`  
`chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
`chutes/Qwen/Qwen3-Coder-Next-TEE`  
`chutes/openai/gpt-oss-120b-TEE`  
  
## Contoh konfigurasi

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "chutes/zai-org/GLM-4.7-TEE" },      models: {        "chutes/zai-org/GLM-4.7-TEE": { alias: "Chutes GLM 4.7" },        "chutes/deepseek-ai/DeepSeek-V3.2-TEE": { alias: "Chutes DeepSeek V3.2" },      },    },  },}
[/code]

Override OAuth

Anda dapat menyesuaikan alur OAuth dengan variabel lingkungan opsional:

Variabel | Tujuan  
---|---  
`CHUTES_CLIENT_ID` | ID klien OAuth khusus  
`CHUTES_CLIENT_SECRET` | Rahasia klien OAuth khusus  
`CHUTES_OAUTH_REDIRECT_URI` | URI pengalihan khusus  
`CHUTES_OAUTH_SCOPES` | Cakupan OAuth khusus  
  
Lihat [dokumentasi OAuth Chutes](<https://chutes.ai/docs/sign-in-with-chutes/overview>) untuk persyaratan aplikasi pengalihan dan bantuan.

Catatan

  * Penemuan kunci API dan OAuth sama-sama menggunakan id penyedia `chutes`.
  * Model Chutes didaftarkan sebagai `chutes/<model-id>`.
  * Jika penemuan gagal saat startup, katalog statis bawaan digunakan secara otomatis.


## Terkait

[**Pemilihan model** Aturan penyedia, ref model, dan perilaku failover. ](</id/concepts/model-providers>) [**Referensi konfigurasi** Skema konfigurasi lengkap termasuk pengaturan penyedia. ](</id/gateway/configuration-reference>) [**Chutes** Dasbor Chutes dan dokumentasi API. ](<https://chutes.ai>) [**Kunci API Chutes** Buat dan kelola kunci API Chutes. ](<https://chutes.ai/settings/api-keys>)

Was this useful?YesNo