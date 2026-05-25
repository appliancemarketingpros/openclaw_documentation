---
title: Xiaomi MiMo
source_url: https://docs.openclaw.ai/id/providers/xiaomi
scraped_at: 2026-05-25
---

Xiaomi MiMo adalah platform API untuk model **MiMo**. OpenClaw menyertakan Plugin `xiaomi` bawaan yang mendaftarkan penyedia chat yang kompatibel dengan OpenAI dan penyedia suara (TTS) terhadap `XIAOMI_API_KEY` yang sama.

Properti | Nilai  
---|---  
ID penyedia | `xiaomi`  
Plugin | terbundel, `enabledByDefault: true`  
Variabel env autentikasi | `XIAOMI_API_KEY`  
Flag onboarding | `--auth-choice xiaomi-api-key`  
Flag CLI langsung | `--xiaomi-api-key <key>`  
Kontrak | penyelesaian chat + `speechProviders`  
API | kompatibel dengan OpenAI (`openai-completions`)  
URL dasar | `https://api.xiaomimimo.com/v1`  
Model default | `xiaomi/mimo-v2-flash`  
Default TTS | `mimo-v2.5-tts`, suara `mimo_default`  
  
## Mulai menggunakan

* ### Dapatkan kunci API

Buat kunci API di [konsol Xiaomi MiMo](<https://platform.xiaomimimo.com/#/console/api-keys>).

* ### Jalankan onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key
[/code]

Atau teruskan kunci secara langsung:

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key --xiaomi-api-key "$XIAOMI_API_KEY"
[/code]

* ### Verifikasi bahwa model tersedia

bashCopy code
[code]
    openclaw models list --provider xiaomi
[/code]

## Katalog bawaan

Ref model | Input | Konteks | Output maks | Penalaran | Catatan  
---|---|---|---|---|---  
`xiaomi/mimo-v2-flash` | teks | 262.144 | 8.192 | Tidak | Model default  
`xiaomi/mimo-v2-pro` | teks | 1.048.576 | 32.000 | Ya | Konteks besar  
`xiaomi/mimo-v2-omni` | teks, gambar | 262.144 | 32.000 | Ya | Multimodal  
  
## Teks-ke-suara

Plugin `xiaomi` bawaan juga mendaftarkan Xiaomi MiMo sebagai penyedia suara untuk `messages.tts`. Plugin ini memanggil kontrak TTS chat-completions Xiaomi dengan teks sebagai pesan `assistant` dan panduan gaya opsional sebagai pesan `user`.

Properti | Nilai  
---|---  
ID TTS | `xiaomi` (alias `mimo`)  
Autentikasi | `XIAOMI_API_KEY`  
API | `POST /v1/chat/completions` dengan `audio`  
Default | `mimo-v2.5-tts`, suara `mimo_default`  
Output | MP3 secara default; WAV saat dikonfigurasi  
json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "xiaomi",      providers: {        xiaomi: {          apiKey: "xiaomi_api_key",          model: "mimo-v2.5-tts",          voice: "mimo_default",          format: "mp3",          style: "Bright, natural, conversational tone.",        },      },    },  },}
[/code]

Suara bawaan yang didukung mencakup `mimo_default`, `default_zh`, `default_en`, `Mia`, `Chloe`, `Milo`, dan `Dean`. `mimo-v2-tts` didukung untuk akun TTS MiMo lama; default menggunakan model TTS MiMo-V2.5 saat ini. Untuk target catatan suara seperti Feishu dan Telegram, OpenClaw mentranskode output Xiaomi ke Opus 48 kHz dengan `ffmpeg` sebelum pengiriman.

## Contoh konfigurasi

json5Copy code
[code]
    {  env: { XIAOMI_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "xiaomi/mimo-v2-flash" } } },  models: {    mode: "merge",    providers: {      xiaomi: {        baseUrl: "https://api.xiaomimimo.com/v1",        api: "openai-completions",        apiKey: "XIAOMI_API_KEY",        models: [          {            id: "mimo-v2-flash",            name: "Xiaomi MiMo V2 Flash",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 8192,          },          {            id: "mimo-v2-pro",            name: "Xiaomi MiMo V2 Pro",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 1048576,            maxTokens: 32000,          },          {            id: "mimo-v2-omni",            name: "Xiaomi MiMo V2 Omni",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Perilaku injeksi otomatis

Penyedia `xiaomi` disuntikkan secara otomatis saat `XIAOMI_API_KEY` ditetapkan di lingkungan Anda atau profil autentikasi tersedia. Anda tidak perlu mengonfigurasi penyedia secara manual kecuali ingin mengganti metadata model atau URL dasar.

Detail model

  * **mimo-v2-flash** — ringan dan cepat, ideal untuk tugas teks tujuan umum. Tidak ada dukungan penalaran.
  * **mimo-v2-pro** — mendukung penalaran dengan jendela konteks 1 juta token untuk beban kerja dokumen panjang.
  * **mimo-v2-omni** — model multimodal berkemampuan penalaran yang menerima input teks dan gambar.

Pemecahan masalah

  * Jika model tidak muncul, pastikan `XIAOMI_API_KEY` ditetapkan dan valid.
  * Saat Gateway berjalan sebagai daemon, pastikan kunci tersedia untuk proses tersebut (misalnya di `~/.openclaw/.env` atau melalui `env.shellEnv`).


## Terkait

[**Pemilihan model** Memilih penyedia, ref model, dan perilaku failover. ](</id/concepts/model-providers>) [**Referensi konfigurasi** Referensi konfigurasi OpenClaw lengkap. ](</id/gateway/configuration-reference>) [**Konsol Xiaomi MiMo** Dasbor Xiaomi MiMo dan pengelolaan kunci API. ](<https://platform.xiaomimimo.com>)

Was this useful?YesNo