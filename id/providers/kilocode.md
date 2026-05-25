---
title: Kilo Gateway
source_url: https://docs.openclaw.ai/id/providers/kilocode
scraped_at: 2026-05-25
---

Kilo Gateway menyediakan **API terpadu** yang merutekan permintaan ke banyak model di balik satu endpoint dan kunci API. API ini kompatibel dengan OpenAI, sehingga sebagian besar OpenAI SDK berfungsi dengan mengganti URL dasar.

Properti | Nilai  
---|---  
Penyedia | `kilocode`  
Autentikasi | `KILOCODE_API_KEY`  
API | Kompatibel dengan OpenAI  
URL Dasar | `https://api.kilo.ai/api/gateway/`  
  
## Memulai

* ### Create an account

Buka [app.kilo.ai](<https://app.kilo.ai>), masuk atau buat akun, lalu navigasikan ke API Keys dan buat kunci baru.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice kilocode-api-key
[/code]

Atau atur variabel lingkungan secara langsung:

bashCopy code
[code]
    export KILOCODE_API_KEY="<your-kilocode-api-key>" # pragma: allowlist secret
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider kilocode
[/code]

## Model default

Model default adalah `kilocode/kilo/auto`, model perutean cerdas milik penyedia yang dikelola oleh Kilo Gateway.

## Katalog bawaan

OpenClaw menemukan model yang tersedia secara dinamis dari Kilo Gateway saat startup. Gunakan `/models kilocode` untuk melihat daftar lengkap model yang tersedia dengan akun Anda.

Model apa pun yang tersedia di gateway dapat digunakan dengan prefiks `kilocode/`:

Ref model | Catatan  
---|---  
`kilocode/kilo/auto` | Default — perutean cerdas  
`kilocode/anthropic/claude-sonnet-4` | Anthropic melalui Kilo  
`kilocode/openai/gpt-5.5` | OpenAI melalui Kilo  
`kilocode/google/gemini-3.1-pro-preview` | Google melalui Kilo  
...dan banyak lagi | Gunakan `/models kilocode` untuk mencantumkan semuanya  
  
## Contoh konfigurasi

json5Copy code
[code]
    {  env: { KILOCODE_API_KEY: "<your-kilocode-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "kilocode/kilo/auto" },    },  },}
[/code]

Transport and compatibility

Kilo Gateway didokumentasikan dalam sumber sebagai kompatibel dengan OpenRouter, sehingga tetap berada di jalur bergaya proxy yang kompatibel dengan OpenAI, bukan pembentukan permintaan OpenAI native.

  * Ref Kilo yang didukung Gemini tetap berada di jalur proxy-Gemini, sehingga OpenClaw mempertahankan sanitasi tanda tangan pemikiran Gemini di sana tanpa mengaktifkan validasi replay Gemini native atau penulisan ulang bootstrap.
  * Kilo Gateway menggunakan token Bearer dengan kunci API Anda di balik layar.

Stream wrapper and reasoning

Pembungkus stream bersama Kilo menambahkan header aplikasi penyedia dan menormalkan payload reasoning proxy untuk ref model konkret yang didukung.

Troubleshooting

  * Jika penemuan model gagal saat startup, OpenClaw beralih ke katalog statis yang dibundel berisi `kilocode/kilo/auto`.
  * Pastikan kunci API Anda valid dan akun Kilo Anda telah mengaktifkan model yang diinginkan.
  * Saat Gateway berjalan sebagai daemon, pastikan `KILOCODE_API_KEY` tersedia untuk proses tersebut (misalnya di `~/.openclaw/.env` atau melalui `env.shellEnv`).


## Terkait

[**Model selection** Memilih penyedia, ref model, dan perilaku failover. ](</id/concepts/model-providers>) [**Configuration reference** Referensi konfigurasi lengkap OpenClaw. ](</id/gateway/configuration-reference>) [**Kilo Gateway** Dasbor Kilo Gateway, kunci API, dan pengelolaan akun. ](<https://app.kilo.ai>)

Was this useful?YesNo