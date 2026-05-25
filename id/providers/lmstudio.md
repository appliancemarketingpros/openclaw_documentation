---
title: LM Studio
source_url: https://docs.openclaw.ai/id/providers/lmstudio
scraped_at: 2026-05-25
---

LM Studio adalah aplikasi yang ramah sekaligus andal untuk menjalankan model open-weight di perangkat keras Anda sendiri. Aplikasi ini memungkinkan Anda menjalankan model llama.cpp (GGUF) atau MLX (Apple Silicon). Tersedia sebagai paket GUI atau daemon headless (`llmster`). Untuk dokumentasi produk dan penyiapan, lihat [lmstudio.ai](<https://lmstudio.ai/>).

## Mulai cepat

  1. Instal LM Studio (desktop) atau `llmster` (headless), lalu mulai server lokal:

bashCopy code
[code]
    curl -fsSL https://lmstudio.ai/install.sh | bash
[/code]

  2. Mulai server


Pastikan Anda memulai aplikasi desktop atau menjalankan daemon menggunakan perintah berikut:

bashCopy code
[code]
    lms daemon up
[/code]

bashCopy code
[code]
    lms server start --port 1234
[/code]

Jika Anda menggunakan aplikasi, pastikan JIT diaktifkan untuk pengalaman yang lancar. Pelajari selengkapnya di [panduan JIT dan TTL LM Studio](<https://lmstudio.ai/docs/developer/core/ttl-and-auto-evict>).

  3. Jika autentikasi LM Studio diaktifkan, tetapkan `LM_API_TOKEN`:

bashCopy code
[code]
    export LM_API_TOKEN="your-lm-studio-api-token"
[/code]

Jika autentikasi LM Studio dinonaktifkan, Anda dapat membiarkan kunci API kosong selama penyiapan interaktif OpenClaw.

Untuk detail penyiapan autentikasi LM Studio, lihat [Autentikasi LM Studio](<https://lmstudio.ai/docs/developer/core/authentication>).

  4. Jalankan onboarding dan pilih `LM Studio`:

bashCopy code
[code]
    openclaw onboard
[/code]

  5. Dalam onboarding, gunakan prompt `Default model` untuk memilih model LM Studio Anda.


Anda juga dapat menetapkan atau mengubahnya nanti:

bashCopy code
[code]
    openclaw models set lmstudio/qwen/qwen3.5-9b
[/code]

Kunci model LM Studio mengikuti format `author/model-name` (misalnya `qwen/qwen3.5-9b`). Referensi model OpenClaw menambahkan nama penyedia di depan: `lmstudio/qwen/qwen3.5-9b`. Anda dapat menemukan kunci yang tepat untuk sebuah model dengan menjalankan `curl http://localhost:1234/api/v1/models` dan melihat bidang `key`.

## Onboarding noninteraktif

Gunakan onboarding noninteraktif saat Anda ingin membuat skrip penyiapan (CI, provisioning, bootstrap jarak jauh):

bashCopy code
[code]
    openclaw onboard \  --non-interactive \  --accept-risk \  --auth-choice lmstudio
[/code]

Atau tentukan URL dasar, model, dan kunci API opsional:

bashCopy code
[code]
    openclaw onboard \  --non-interactive \  --accept-risk \  --auth-choice lmstudio \  --custom-base-url http://localhost:1234/v1 \  --lmstudio-api-key "$LM_API_TOKEN" \  --custom-model-id qwen/qwen3.5-9b
[/code]

`--custom-model-id` menerima kunci model seperti yang dikembalikan oleh LM Studio (misalnya `qwen/qwen3.5-9b`), tanpa prefiks penyedia `lmstudio/`.

Untuk server LM Studio yang diautentikasi, teruskan `--lmstudio-api-key` atau tetapkan `LM_API_TOKEN`. Untuk server LM Studio tanpa autentikasi, hilangkan kunci; OpenClaw menyimpan penanda lokal nonrahasia.

`--custom-api-key` tetap didukung untuk kompatibilitas, tetapi `--lmstudio-api-key` lebih disarankan untuk LM Studio.

Ini menulis `models.providers.lmstudio` dan menetapkan model default ke `lmstudio/<custom-model-id>`. Saat Anda memberikan kunci API, penyiapan juga menulis profil autentikasi `lmstudio:default`.

Penyiapan interaktif dapat meminta panjang konteks pemuatan pilihan opsional dan menerapkannya ke semua model LM Studio yang ditemukan yang disimpan ke konfigurasi. Konfigurasi Plugin LM Studio mempercayai endpoint LM Studio yang dikonfigurasi untuk permintaan model, termasuk host loopback, LAN, dan tailnet. Anda dapat menonaktifkannya dengan menetapkan `models.providers.lmstudio.request.allowPrivateNetwork: false`.

## Konfigurasi

### Kompatibilitas penggunaan streaming

LM Studio kompatibel dengan penggunaan streaming. Saat tidak memancarkan objek `usage` berbentuk OpenAI, OpenClaw memulihkan hitungan token dari metadata bergaya llama.cpp `timings.prompt_n` / `timings.predicted_n` sebagai gantinya.

Perilaku penggunaan streaming yang sama berlaku untuk backend lokal yang kompatibel dengan OpenAI berikut:

  * vLLM
  * SGLang
  * llama.cpp
  * LocalAI
  * Jan
  * TabbyAPI
  * text-generation-webui


### Kompatibilitas thinking

Saat discovery `/api/v1/models` LM Studio melaporkan opsi penalaran khusus model, OpenClaw mengekspos nilai `reasoning_effort` yang kompatibel dengan OpenAI yang sesuai dalam metadata kompatibilitas model. Build LM Studio saat ini dapat mengiklankan opsi UI biner seperti `allowed_options: ["off", "on"]` sambil menolak nilai tersebut pada `/v1/chat/completions`; OpenClaw menormalkan bentuk discovery biner tersebut menjadi `none`, `minimal`, `low`, `medium`, `high`, dan `xhigh` sebelum mengirim permintaan. Konfigurasi LM Studio tersimpan yang lebih lama yang berisi peta penalaran `off`/`on` dinormalkan dengan cara yang sama saat katalog dimuat.

### Konfigurasi eksplisit

json5Copy code
[code]
    {  models: {    providers: {      lmstudio: {        baseUrl: "http://localhost:1234/v1",        apiKey: "${LM_API_TOKEN}",        api: "openai-completions",        models: [          {            id: "qwen/qwen3-coder-next",            name: "Qwen 3 Coder Next",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## Pemecahan masalah

### LM Studio tidak terdeteksi

Pastikan LM Studio sedang berjalan. Jika autentikasi diaktifkan, tetapkan juga `LM_API_TOKEN`:

bashCopy code
[code]
    # Start via desktop app, or headless:lms server start --port 1234
[/code]

Verifikasi bahwa API dapat diakses:

bashCopy code
[code]
    curl http://localhost:1234/api/v1/models
[/code]

### Kesalahan autentikasi (HTTP 401)

Jika penyiapan melaporkan HTTP 401, verifikasi kunci API Anda:

  * Periksa bahwa `LM_API_TOKEN` cocok dengan kunci yang dikonfigurasi di LM Studio.
  * Untuk detail penyiapan autentikasi LM Studio, lihat [Autentikasi LM Studio](<https://lmstudio.ai/docs/developer/core/authentication>).
  * Jika server Anda tidak memerlukan autentikasi, biarkan kunci kosong selama penyiapan.


### Pemuatan model just-in-time

LM Studio mendukung pemuatan model just-in-time (JIT), yaitu model dimuat pada permintaan pertama. OpenClaw secara default melakukan pramuat model melalui endpoint pemuatan native LM Studio, yang membantu saat JIT dinonaktifkan. Untuk membiarkan JIT, TTL diam, dan perilaku auto-evict LM Studio mengelola siklus hidup model, nonaktifkan langkah pramuat OpenClaw:

json5Copy code
[code]
    {  models: {    providers: {      lmstudio: {        baseUrl: "http://localhost:1234/v1",        api: "openai-completions",        params: { preload: false },        models: [{ id: "qwen/qwen3.5-9b" }],      },    },  },}
[/code]

### Host LM Studio LAN atau tailnet

Gunakan alamat host LM Studio yang dapat dijangkau, pertahankan `/v1`, dan pastikan LM Studio terikat melampaui loopback pada mesin tersebut:

json5Copy code
[code]
    {  models: {    providers: {      lmstudio: {        baseUrl: "http://gpu-box.local:1234/v1",        apiKey: "lmstudio",        api: "openai-completions",        models: [{ id: "qwen/qwen3.5-9b" }],      },    },  },}
[/code]

Berbeda dengan penyedia generik yang kompatibel dengan OpenAI, `lmstudio` secara otomatis mempercayai endpoint lokal/pribadi yang dikonfigurasi untuk permintaan model yang dilindungi. ID penyedia loopback kustom seperti `localhost` atau `127.0.0.1` juga dipercaya secara otomatis; untuk ID penyedia kustom LAN, tailnet, atau DNS privat, tetapkan `models.providers.<id>.request.allowPrivateNetwork: true` secara eksplisit.

## Terkait

  * [Pemilihan model](</id/concepts/model-providers>)
  * [Ollama](</id/providers/ollama>)
  * [Model lokal](</id/gateway/local-models>)


Was this useful?YesNo