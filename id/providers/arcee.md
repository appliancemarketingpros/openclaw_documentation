---
title: Arcee AI
source_url: https://docs.openclaw.ai/id/providers/arcee
scraped_at: 2026-05-25
---

[Arcee AI](<https://arcee.ai>) menyediakan akses ke keluarga model mixture-of-experts Trinity melalui API yang kompatibel dengan OpenAI. Semua model Trinity berlisensi Apache 2.0.

Model Arcee AI dapat diakses langsung melalui platform Arcee atau melalui [OpenRouter](</id/providers/openrouter>).

Properti | Nilai  
---|---  
Penyedia | `arcee`  
Autentikasi | `ARCEEAI_API_KEY` (langsung) atau `OPENROUTER_API_KEY` (melalui OpenRouter)  
API | Kompatibel dengan OpenAI  
URL Dasar | `https://api.arcee.ai/api/v1` (langsung) atau `https://openrouter.ai/api/v1` (OpenRouter)  
  
## Memulai

### Langsung (platform Arcee)

* ### Dapatkan kunci API

Buat kunci API di [Arcee AI](<https://chat.arcee.ai/>).

* ### Jalankan onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-api-key
[/code]

* ### Tetapkan model default

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

### Melalui OpenRouter

* ### Dapatkan kunci API

Buat kunci API di [OpenRouter](<https://openrouter.ai/keys>).

* ### Jalankan onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-openrouter
[/code]

* ### Tetapkan model default

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

Referensi model yang sama berfungsi untuk penyiapan langsung maupun OpenRouter (misalnya `arcee/trinity-large-thinking`).

## Penyiapan non-interaktif

### Langsung (platform Arcee)

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-api-key \  --arceeai-api-key "$ARCEEAI_API_KEY"
[/code]

### Melalui OpenRouter

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-openrouter \  --openrouter-api-key "$OPENROUTER_API_KEY"
[/code]

## Katalog bawaan

OpenClaw saat ini menyertakan katalog Arcee bawaan berikut:

Referensi model | Nama | Input | Konteks | Biaya (masuk/keluar per 1 juta) | Catatan  
---|---|---|---|---|---  
`arcee/trinity-large-thinking` | Trinity Large Thinking | teks | 256K | $0.25 / $0.90 | Model default; penalaran diaktifkan  
`arcee/trinity-large-preview` | Trinity Large Preview | teks | 128K | $0.25 / $1.00 | Serbaguna; 400B parameter, 13B aktif  
`arcee/trinity-mini` | Trinity Mini 26B | teks | 128K | $0.045 / $0.15 | Cepat dan hemat biaya; pemanggilan fungsi  
  
## Fitur yang didukung

Fitur | Didukung  
---|---  
Streaming | Ya  
Penggunaan alat / pemanggilan fungsi | Ya (Trinity Mini, Trinity Large Preview)  
Output terstruktur (mode JSON dan skema JSON) | Ya  
Pemikiran yang diperluas | Ya (Trinity Large Thinking; alat dinonaktifkan)  
  
Catatan lingkungan

Jika Gateway berjalan sebagai daemon (launchd/systemd), pastikan `ARCEEAI_API_KEY` (atau `OPENROUTER_API_KEY`) tersedia untuk proses tersebut (misalnya, di `~/.openclaw/.env` atau melalui `env.shellEnv`).

Perutean OpenRouter

Saat menggunakan model Arcee melalui OpenRouter, referensi model `arcee/*` yang sama berlaku. OpenClaw menangani perutean secara transparan berdasarkan pilihan autentikasi Anda. Lihat [dokumentasi penyedia OpenRouter](</id/providers/openrouter>) untuk detail konfigurasi khusus OpenRouter.

## Terkait

[**OpenRouter** Akses model Arcee dan banyak model lain melalui satu kunci API. ](</id/providers/openrouter>) [**Pemilihan model** Memilih penyedia, referensi model, dan perilaku failover. ](</id/concepts/model-providers>)

Was this useful?YesNo