---
title: Volcengine (Doubao)
source_url: https://docs.openclaw.ai/id/providers/volcengine
scraped_at: 2026-05-25
---

Provider Volcengine memberikan akses ke model Doubao dan model pihak ketiga yang di-host di Volcano Engine, dengan endpoint terpisah untuk beban kerja umum dan coding. Plugin bawaan yang sama juga dapat mendaftarkan Volcengine Speech sebagai provider TTS.

Detail | Nilai  
---|---  
Provider | `volcengine` (umum + TTS) + `volcengine-plan` (coding)  
Auth model | `VOLCANO_ENGINE_API_KEY`  
Auth TTS | `VOLCENGINE_TTS_API_KEY` atau `BYTEPLUS_SEED_SPEECH_API_KEY`  
API | Model kompatibel OpenAI, BytePlus Seed Speech TTS  
  
## Memulai

* ### Atur API key

Jalankan onboarding interaktif:

bashCopy code
[code]
    openclaw onboard --auth-choice volcengine-api-key
[/code]

Ini mendaftarkan provider umum (`volcengine`) dan coding (`volcengine-plan`) dari satu API key.

* ### Atur model default

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "volcengine-plan/ark-code-latest" },    },  },}
[/code]

* ### Verifikasi model tersedia

bashCopy code
[code]
    openclaw models list --provider volcengineopenclaw models list --provider volcengine-plan
[/code]

## Provider dan endpoint

Provider | Endpoint | Kasus penggunaan  
---|---|---  
`volcengine` | `ark.cn-beijing.volces.com/api/v3` | Model umum  
`volcengine-plan` | `ark.cn-beijing.volces.com/api/coding/v3` | Model coding  
  
## Katalog bawaan

### Umum (volcengine)

Referensi model | Nama | Input | Konteks  
---|---|---|---  
`volcengine/doubao-seed-1-8-251228` | Doubao Seed 1.8 | text, image | 256,000  
`volcengine/doubao-seed-code-preview-251028` | doubao-seed-code-preview-251028 | text, image | 256,000  
`volcengine/kimi-k2-5-260127` | Kimi K2.5 | text, image | 256,000  
`volcengine/glm-4-7-251222` | GLM 4.7 | text, image | 200,000  
`volcengine/deepseek-v3-2-251201` | DeepSeek V3.2 | text, image | 128,000  
  
### Coding (volcengine-plan)

Referensi model | Nama | Input | Konteks  
---|---|---|---  
`volcengine-plan/ark-code-latest` | Ark Coding Plan | text | 256,000  
`volcengine-plan/doubao-seed-code` | Doubao Seed Code | text | 256,000  
`volcengine-plan/glm-4.7` | GLM 4.7 Coding | text | 200,000  
`volcengine-plan/kimi-k2-thinking` | Kimi K2 Thinking | text | 256,000  
`volcengine-plan/kimi-k2.5` | Kimi K2.5 Coding | text | 256,000  
`volcengine-plan/doubao-seed-code-preview-251028` | Doubao Seed Code Preview | text | 256,000  
  
## Text-to-speech

Volcengine TTS menggunakan API HTTP BytePlus Seed Speech dan dikonfigurasi secara terpisah dari API key model Doubao yang kompatibel dengan OpenAI. Di konsol BytePlus, buka Seed Speech > Settings > API Keys dan salin API key, lalu atur:

bashCopy code
[code]
    export VOLCENGINE_TTS_API_KEY="byteplus_seed_speech_api_key"export VOLCENGINE_TTS_RESOURCE_ID="seed-tts-1.0"
[/code]

Lalu aktifkan di `openclaw.json`:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "volcengine",      providers: {        volcengine: {          apiKey: "byteplus_seed_speech_api_key",          voice: "en_female_anna_mars_bigtts",          speedRatio: 1.0,        },      },    },  },}
[/code]

Untuk target voice-note, OpenClaw meminta `ogg_opus` native provider dari Volcengine. Untuk lampiran audio normal, OpenClaw meminta `mp3`. Alias provider `bytedance` dan `doubao` juga di-resolve ke provider speech yang sama.

ID resource default adalah `seed-tts-1.0` karena itulah yang diberikan BytePlus kepada API key Seed Speech yang baru dibuat dalam proyek default. Jika proyek Anda memiliki entitlement TTS 2.0, atur `VOLCENGINE_TTS_RESOURCE_ID=seed-tts-2.0`.

Autentikasi AppID/token lama tetap didukung untuk aplikasi Speech Console yang lebih lama:

bashCopy code
[code]
    export VOLCENGINE_TTS_APPID="speech_app_id"export VOLCENGINE_TTS_TOKEN="speech_access_token"export VOLCENGINE_TTS_CLUSTER="volcano_tts"
[/code]

## Konfigurasi lanjutan

Model default setelah onboarding

`openclaw onboard --auth-choice volcengine-api-key` saat ini menetapkan `volcengine-plan/ark-code-latest` sebagai model default sambil juga mendaftarkan katalog umum `volcengine`.

Perilaku fallback pemilih model

Selama pemilihan model pada onboarding/configure, pilihan auth Volcengine memprioritaskan baris `volcengine/*` dan `volcengine-plan/*`. Jika model tersebut belum dimuat, OpenClaw fallback ke katalog yang tidak difilter alih-alih menampilkan picker bercakupan provider yang kosong.

Variabel lingkungan untuk proses daemon

Jika Gateway berjalan sebagai daemon (launchd/systemd), pastikan env var model dan TTS seperti `VOLCANO_ENGINE_API_KEY`, `VOLCENGINE_TTS_API_KEY`, `BYTEPLUS_SEED_SPEECH_API_KEY`, `VOLCENGINE_TTS_APPID`, dan `VOLCENGINE_TTS_TOKEN` tersedia untuk proses tersebut (misalnya, di `~/.openclaw/.env` atau melalui `env.shellEnv`).

## Terkait

[**Pemilihan model** Memilih provider, referensi model, dan perilaku failover. ](</id/concepts/model-providers>) [**Konfigurasi** Referensi config lengkap untuk agen, model, dan provider. ](</id/gateway/configuration>) [**Pemecahan masalah** Masalah umum dan langkah debugging. ](</id/help/troubleshooting>) [**FAQ** Pertanyaan umum tentang penyiapan OpenClaw. ](</id/help/faq>)

Was this useful?YesNo