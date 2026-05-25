---
title: DeepInfra
source_url: https://docs.openclaw.ai/id/providers/deepinfra
scraped_at: 2026-05-25
---

DeepInfra menyediakan **API terpadu** yang merutekan permintaan ke model open source paling populer dan model frontier melalui satu endpoint dan kunci API. Layanan ini kompatibel dengan OpenAI, sehingga sebagian besar SDK OpenAI dapat bekerja dengan mengganti URL dasar.

## Mendapatkan kunci API

  1. Buka <https://deepinfra.com/>
  2. Masuk atau buat akun
  3. Buka Dasbor / Kunci dan buat kunci API baru atau gunakan kunci yang dibuat otomatis


## Penyiapan CLI

bashCopy code
[code]
    openclaw onboard --deepinfra-api-key <key>
[/code]

Atau atur variabel lingkungan:

bashCopy code
[code]
    export DEEPINFRA_API_KEY="<your-deepinfra-api-key>" # pragma: allowlist secret
[/code]

## Cuplikan konfigurasi

json5Copy code
[code]
    {  env: { DEEPINFRA_API_KEY: "<your-deepinfra-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "deepinfra/deepseek-ai/DeepSeek-V3.2" },    },  },}
[/code]

## Permukaan OpenClaw yang didukung

Plugin bawaan mendaftarkan semua permukaan DeepInfra yang cocok dengan kontrak penyedia OpenClaw saat ini:

Permukaan | Model default | Konfigurasi/alat OpenClaw  
---|---|---  
Obrolan / penyedia model | `deepseek-ai/DeepSeek-V3.2` | `agents.defaults.model`  
Pembuatan/penyuntingan gambar | `black-forest-labs/FLUX-1-schnell` | `image_generate`, `agents.defaults.imageGenerationModel`  
Pemahaman media | `moonshotai/Kimi-K2.5` untuk gambar | pemahaman gambar masuk  
Ucapan ke teks | `openai/whisper-large-v3-turbo` | transkripsi audio masuk  
Teks ke ucapan | `hexgrad/Kokoro-82M` | `messages.tts.provider: "deepinfra"`  
Pembuatan video | `Pixverse/Pixverse-T2V` | `video_generate`, `agents.defaults.videoGenerationModel`  
Embedding memori | `BAAI/bge-m3` | `agents.defaults.memorySearch.provider: "deepinfra"`  
  
DeepInfra juga menyediakan pemeringkatan ulang, klasifikasi, deteksi objek, dan jenis model native lainnya. OpenClaw saat ini belum memiliki kontrak penyedia kelas utama untuk kategori tersebut, sehingga Plugin ini belum mendaftarkannya.

## Model yang tersedia

OpenClaw secara dinamis menemukan model DeepInfra yang tersedia saat startup. Gunakan `/models deepinfra` untuk melihat daftar lengkap model yang tersedia.

Model apa pun yang tersedia di [DeepInfra.com](<https://deepinfra.com/>) dapat digunakan dengan prefiks `deepinfra/`:

CodeCopy code
[code]
    deepinfra/MiniMaxAI/MiniMax-M2.5deepinfra/deepseek-ai/DeepSeek-V3.2deepinfra/moonshotai/Kimi-K2.5deepinfra/zai-org/GLM-5.1...dan masih banyak lagi
[/code]

## Catatan

  * Referensi model adalah `deepinfra/<provider>/<model>` (misalnya, `deepinfra/Qwen/Qwen3-Max`).
  * Model default: `deepinfra/deepseek-ai/DeepSeek-V3.2`
  * URL dasar: `https://api.deepinfra.com/v1/openai`
  * Pembuatan video native menggunakan `https://api.deepinfra.com/v1/inference/<model>`.


## Terkait

  * [Penyedia model](</id/concepts/model-providers>)
  * [Semua penyedia](</id/providers>)


Was this useful?YesNo