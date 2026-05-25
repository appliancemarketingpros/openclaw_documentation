---
title: SGLang
source_url: https://docs.openclaw.ai/id/providers/sglang
scraped_at: 2026-05-25
---

SGLang menyajikan model open-weight melalui API HTTP yang kompatibel dengan OpenAI. OpenClaw terhubung ke SGLang menggunakan keluarga penyedia `openai-completions` dengan penemuan otomatis model yang tersedia.

Properti | Nilai  
---|---  
id penyedia | `sglang`  
Plugin | dibundel, `enabledByDefault: true`  
Variabel env autentikasi | `SGLANG_API_KEY` (nilai tidak kosong apa pun jika server tidak memiliki auth)  
Flag onboarding | `--auth-choice sglang`  
API | kompatibel dengan OpenAI (`openai-completions`)  
URL dasar default | `http://127.0.0.1:30000/v1`  
Placeholder model default | `sglang/Qwen/Qwen3-8B`  
Penggunaan streaming | Ya (`supportsStreamingUsage: true`)  
Penetapan harga | Ditandai external-free (`modelPricing.external: false`)  
  
OpenClaw juga **menemukan otomatis** model yang tersedia dari SGLang saat Anda ikut serta dengan `SGLANG_API_KEY`. Gunakan `sglang/*` di `agents.defaults.models` agar penemuan tetap dinamis saat Anda juga mengonfigurasi URL dasar SGLang kustom. Lihat Penemuan model (penyedia implisit) di bawah.

## Memulai

* ### Mulai SGLang

Jalankan SGLang dengan server yang kompatibel dengan OpenAI. URL dasar Anda harus mengekspos endpoint `/v1` (misalnya `/v1/models`, `/v1/chat/completions`). SGLang umumnya berjalan pada:

  * `http://127.0.0.1:30000/v1`


* ### Tetapkan kunci API

Nilai apa pun berfungsi jika tidak ada auth yang dikonfigurasi pada server Anda:

bashCopy code
[code]
    export SGLANG_API_KEY="sglang-local"
[/code]

* ### Jalankan onboarding atau tetapkan model secara langsung

bashCopy code
[code]
    openclaw onboard
[/code]

Atau konfigurasikan model secara manual:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "sglang/your-model-id" },    },  },}
[/code]

## Penemuan model (penyedia implisit)

Saat `SGLANG_API_KEY` ditetapkan (atau profil auth ada) dan Anda **tidak** mendefinisikan `models.providers.sglang`, OpenClaw akan membuat kueri ke:

  * `GET http://127.0.0.1:30000/v1/models`


dan mengonversi ID yang dikembalikan menjadi entri model.

## Konfigurasi eksplisit (model manual)

Gunakan konfigurasi eksplisit saat:

  * SGLang berjalan pada host/port yang berbeda.
  * Anda ingin menyematkan nilai `contextWindow`/`maxTokens`.
  * Server Anda memerlukan kunci API nyata (atau Anda ingin mengontrol header).

json5Copy code
[code]
    {  models: {    providers: {      sglang: {        baseUrl: "http://127.0.0.1:30000/v1",        apiKey: "${SGLANG_API_KEY}",        api: "openai-completions",        models: [          {            id: "your-model-id",            name: "Local SGLang Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## Konfigurasi lanjutan

Perilaku bergaya proxy

SGLang diperlakukan sebagai backend `/v1` yang kompatibel dengan OpenAI bergaya proxy, bukan endpoint OpenAI native.

Perilaku | SGLang  
---|---  
Pembentukan permintaan khusus OpenAI | Tidak diterapkan  
`service_tier`, Responses `store`, petunjuk prompt-cache | Tidak dikirim  
Pembentukan payload reasoning-compat | Tidak diterapkan  
Header atribusi tersembunyi (`originator`, `version`, `User-Agent`) | Tidak disuntikkan pada URL dasar SGLang kustom  
Pemecahan masalah

**Server tidak dapat dijangkau**

Verifikasi server sedang berjalan dan merespons:

bashCopy code
[code]
    curl http://127.0.0.1:30000/v1/models
[/code]

**Kesalahan auth**

Jika permintaan gagal dengan kesalahan auth, tetapkan `SGLANG_API_KEY` nyata yang cocok dengan konfigurasi server Anda, atau konfigurasikan penyedia secara eksplisit di bawah `models.providers.sglang`.

## Terkait

[**Pemilihan model** Memilih penyedia, referensi model, dan perilaku failover. ](</id/concepts/model-providers>) [**Referensi konfigurasi** Skema konfigurasi lengkap termasuk entri penyedia. ](</id/gateway/configuration-reference>)

Was this useful?YesNo