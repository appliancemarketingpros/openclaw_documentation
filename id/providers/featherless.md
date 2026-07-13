---
title: Featherless AI
source_url: https://docs.openclaw.ai/id/providers/featherless
scraped_at: 2026-07-13
---

ModelsProviders

[Featherless AI](<https://featherless.ai>) menyediakan model terbuka melalui API yang kompatibel dengan OpenAI. OpenClaw memasang Featherless sebagai Plugin penyedia eksternal resmi dan mempertahankan katalog bawaan tetap ringkas, sekaligus menerima ID model persis dari Featherless saat runtime.

Properti | Nilai  
---|---  
ID penyedia | `featherless`  
Paket | `@openclaw/featherless-provider`  
Variabel lingkungan autentikasi | `FEATHERLESS_API_KEY`  
Flag orientasi awal | `--auth-choice featherless-api-key`  
Flag CLI langsung | `--featherless-api-key <key>`  
API | Kompatibel dengan OpenAI (`openai-completions`)  
URL dasar | `https://api.featherless.ai/v1`  
Model default | `featherless/Qwen/Qwen3-32B`  
  
## Penyiapan

Pasang Plugin dan mulai ulang Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/featherless-provideropenclaw gateway restart
[/code]

Jalankan orientasi awal:

bashCopy code
[code]
    openclaw onboard --auth-choice featherless-api-key
[/code]

Untuk penyiapan noninteraktif:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice featherless-api-key \  --featherless-api-key "$FEATHERLESS_API_KEY"
[/code]

Atau sediakan kunci tersebut bagi proses Gateway:

bashCopy code
[code]
    export FEATHERLESS_API_KEY="<your-featherless-api-key>" # pragma: allowlist secret
[/code]

Verifikasi penyedia:

bashCopy code
[code]
    openclaw models list --provider featherless
[/code]

## Model default

Plugin menggunakan `Qwen/Qwen3-32B` sebagai default penyiapan karena dokumentasi Featherless menyatakan dukungan pemanggilan alat native untuk keluarga Qwen 3. OpenClaw mengonfigurasi jendela konteks 32.768 token, batas keluaran konservatif sebesar 4.096 token, dan kontrol proses berpikir pada templat percakapan Qwen.

Kolom biaya katalog bernilai nol karena Featherless mendukung beberapa mode penagihan dan OpenClaw tidak menyematkan tarif paket atau harga per permintaan yang khusus untuk akun tertentu.

## Model Featherless lainnya

Gunakan ID model Featherless secara persis setelah prefiks penyedia `featherless/`:

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "featherless/moonshotai/Kimi-K2-Instruct",      },    },  },}
[/code]

OpenClaw sengaja tidak menyalin seluruh indeks model publik Featherless ke pemilih. Indeks tersebut berukuran besar dan tidak menyediakan metadata kemampuan terstruktur yang memadai untuk mengklasifikasikan setiap model teks, visi, penyematan, dan penalaran dengan aman. Oleh karena itu, ID yang tidak dikenal menggunakan default konservatif khusus teks tanpa penalaran: jendela konteks 4.096 token dan batas keluaran 1.024 token.

Tambahkan entri model penyedia secara eksplisit jika sebuah model memerlukan metadata yang berbeda:

json5Copy code
[code]
    {  models: {    mode: "merge",    providers: {      featherless: {        baseUrl: "https://api.featherless.ai/v1",        apiKey: "${FEATHERLESS_API_KEY}",        api: "openai-completions",        models: [          {            id: "google/gemma-3-27b-it",            name: "Gemma 3 27B",            input: ["text", "image"],            reasoning: false,            contextWindow: 32768,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

Periksa katalog model Featherless untuk mengetahui ketersediaan model dan tag kemampuan terkini sebelum menambahkan metadata khusus.

## Pemecahan masalah

  * `401` atau `403`: pastikan `FEATHERLESS_API_KEY` dapat diakses oleh proses Gateway, atau jalankan kembali orientasi awal.
  * Model tidak dikenal: gunakan ID persis yang peka huruf besar-kecil dari Featherless setelah prefiks `featherless/`.
  * Pemanggilan alat dikembalikan sebagai teks: pilih keluarga model yang menurut dokumentasi Featherless mendukung pemanggilan fungsi native, seperti Qwen 3.
  * Gateway terkelola tidak dapat mengakses kunci: simpan kunci di `~/.openclaw/.env` atau sumber lingkungan lain yang dimuat oleh layanan, lalu mulai ulang Gateway.


## Terkait

  * [Penyedia model](</id/concepts/model-providers>)
  * [Semua penyedia](</id/providers>)
  * [Mode berpikir](</id/tools/thinking>)


Was this useful?YesNo

Open issue