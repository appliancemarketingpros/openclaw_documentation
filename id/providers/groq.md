---
title: Groq
source_url: https://docs.openclaw.ai/id/providers/groq
scraped_at: 2026-05-25
---

[Groq](<https://groq.com>) menyediakan inferensi sangat cepat pada model berbobot terbuka (Llama, Gemma, Kimi, Qwen, GPT OSS, dan lainnya) menggunakan perangkat keras LPU khusus. OpenClaw menyertakan Plugin Groq bawaan yang mendaftarkan penyedia chat yang kompatibel dengan OpenAI dan penyedia pemahaman media audio.

Properti | Nilai  
---|---  
ID penyedia | `groq`  
Plugin | bawaan, `enabledByDefault: true`  
Var env autentikasi | `GROQ_API_KEY`  
Flag onboarding | `--auth-choice groq-api-key`  
API | kompatibel dengan OpenAI (`openai-completions`)  
URL dasar | `https://api.groq.com/openai/v1`  
Transkripsi audio | `whisper-large-v3-turbo` (default)  
Default chat yang disarankan | `groq/llama-3.3-70b-versatile`  
  
## Memulai

* ### Dapatkan kunci API

Buat kunci API di [console.groq.com/keys](<https://console.groq.com/keys>).

* ### Tetapkan kunci API

OnboardingCopy code
[code]
    openclaw onboard --auth-choice groq-api-key
[/code]

Env onlyCopy code
[code]
    export GROQ_API_KEY=gsk_...
[/code]

* ### Tetapkan model default

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

* ### Verifikasi katalog dapat dijangkau

bashCopy code
[code]
    openclaw models list --provider groq
[/code]

### Contoh file konfigurasi

json5Copy code
[code]
    {  env: { GROQ_API_KEY: "gsk_..." },  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

## Katalog bawaan

OpenClaw menyertakan katalog Groq berbasis manifes dengan entri reasoning dan non-reasoning. Jalankan `openclaw models list --provider groq` untuk melihat baris bawaan bagi versi yang terpasang, atau periksa [console.groq.com/docs/models](<https://console.groq.com/docs/models>) untuk daftar resmi Groq.

Ref model | Nama | Reasoning | Input | Konteks  
---|---|---|---|---  
`groq/llama-3.3-70b-versatile` | Llama 3.3 70B Versatile | tidak | teks | 131,072  
`groq/llama-3.1-8b-instant` | Llama 3.1 8B Instant | tidak | teks | 131,072  
`groq/meta-llama/llama-4-maverick-17b-128e-instruct` | Llama 4 Maverick 17B | tidak | teks + gambar | 131,072  
`groq/meta-llama/llama-4-scout-17b-16e-instruct` | Llama 4 Scout 17B | tidak | teks + gambar | 131,072  
`groq/llama3-70b-8192` | Llama 3 70B | tidak | teks | 8,192  
`groq/llama3-8b-8192` | Llama 3 8B | tidak | teks | 8,192  
`groq/gemma2-9b-it` | Gemma 2 9B | tidak | teks | 8,192  
`groq/mistral-saba-24b` | Mistral Saba 24B | tidak | teks | 32,768  
`groq/moonshotai/kimi-k2-instruct` | Kimi K2 Instruct | tidak | teks | 131,072  
`groq/moonshotai/kimi-k2-instruct-0905` | Kimi K2 Instruct 0905 | tidak | teks | 262,144  
`groq/openai/gpt-oss-120b` | GPT OSS 120B | ya | teks | 131,072  
`groq/openai/gpt-oss-20b` | GPT OSS 20B | ya | teks | 131,072  
`groq/openai/gpt-oss-safeguard-20b` | Safety GPT OSS 20B | ya | teks | 131,072  
`groq/qwen-qwq-32b` | Qwen QwQ 32B | ya | teks | 131,072  
`groq/qwen/qwen3-32b` | Qwen3 32B | ya | teks | 131,072  
`groq/deepseek-r1-distill-llama-70b` | DeepSeek R1 Distill Llama 70B | ya | teks | 131,072  
`groq/groq/compound` | Compound | ya | teks | 131,072  
`groq/groq/compound-mini` | Compound Mini | ya | teks | 131,072  
  
## Model reasoning

OpenClaw memetakan level `/think` bersama ke nilai `reasoning_effort` khusus model milik Groq:

  * Untuk `qwen/qwen3-32b`, thinking yang dinonaktifkan mengirim `none` dan thinking yang diaktifkan mengirim `default`.
  * Untuk model reasoning Groq GPT OSS (`openai/gpt-oss-*`), OpenClaw mengirim `low`, `medium`, atau `high` berdasarkan level `/think`. Thinking yang dinonaktifkan menghilangkan `reasoning_effort` karena model tersebut tidak mendukung nilai nonaktif.
  * DeepSeek R1 Distill, Qwen QwQ, dan Compound menggunakan surface reasoning native milik Groq; `/think` mengontrol visibilitas, tetapi model selalu melakukan reasoning.


Lihat [Mode thinking](</id/tools/thinking>) untuk level `/think` bersama dan cara OpenClaw menerjemahkannya per penyedia.

## Transkripsi audio

Plugin bawaan Groq juga mendaftarkan **penyedia pemahaman media audio** agar pesan suara dapat ditranskripsi melalui surface bersama `tools.media.audio`.

Properti | Nilai  
---|---  
Jalur konfigurasi bersama | `tools.media.audio`  
URL dasar default | `https://api.groq.com/openai/v1`  
Model default | `whisper-large-v3-turbo`  
Prioritas otomatis | 20  
Endpoint API | kompatibel dengan OpenAI `/audio/transcriptions`  
  
Untuk menjadikan Groq sebagai backend audio default:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [{ provider: "groq" }],      },    },  },}
[/code]

Ketersediaan lingkungan untuk daemon

Jika Gateway berjalan sebagai layanan terkelola (launchd, systemd, Docker), `GROQ_API_KEY` harus terlihat oleh proses tersebut — bukan hanya oleh shell interaktif Anda.

ID model Groq kustom

OpenClaw menerima ID model Groq apa pun saat runtime. Gunakan ID persis seperti yang ditampilkan Groq dan beri prefiks `groq/`. Katalog bawaan mencakup kasus umum; ID yang tidak ada di katalog akan diteruskan ke template default yang kompatibel dengan OpenAI.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/<your-model-id>" },    },  },}
[/code]

## Terkait

[**Penyedia model** Memilih penyedia, ref model, dan perilaku failover. ](</id/concepts/model-providers>) [**Mode thinking** Level upaya reasoning dan interaksi kebijakan penyedia. ](</id/tools/thinking>) [**Referensi konfigurasi** Skema konfigurasi lengkap termasuk pengaturan penyedia dan audio. ](</id/gateway/configuration-reference>) [**Groq Console** Dasbor Groq, dokumentasi API, dan harga. ](<https://console.groq.com>)

Was this useful?YesNo