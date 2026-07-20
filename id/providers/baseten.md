---
title: Baseten
source_url: https://docs.openclaw.ai/id/providers/baseten
scraped_at: 2026-07-20
---

Get started

[API Model Baseten](<https://docs.baseten.co/inference/model-apis/overview>) menyediakan akses terhosting yang kompatibel dengan OpenAI ke model-model terdepan. Plugin eksternal resmi menggunakan penemuan terautentikasi, sehingga OpenClaw mengikuti set model lengkap yang diaktifkan untuk akun Baseten Anda. Fallback luringnya berisi setiap API Model yang tersedia saat rilis OpenClaw ini dibuat.

Properti | Nilai  
---|---  
Id penyedia | `baseten`  
Plugin | paket eksternal resmi (`@openclaw/baseten-provider`)  
Variabel lingkungan autentikasi | `BASETEN_API_KEY`  
Flag orientasi awal | `--auth-choice baseten-api-key`  
Flag CLI langsung | `--baseten-api-key <key>`  
API | kompatibel dengan OpenAI (`openai-completions`)  
URL dasar | `https://inference.baseten.co/v1`  
Model default | `baseten/thinkingmachines/inkling`  
  
## Instal Plugin

bashCopy code
[code]
    openclaw plugins install @openclaw/baseten-provideropenclaw gateway restart
[/code]

## Memulai

* ### Buat akun Baseten dan kunci API

Paket Basic Baseten tidak memiliki biaya platform bulanan; panggilan API Model dikenai biaya berdasarkan penggunaan. Buat kunci di [pengaturan kunci API Baseten](<https://app.baseten.co/settings/api_keys>) dan periksa tarif terkini di [halaman harga](<https://www.baseten.co/pricing>).

* ### Jalankan orientasi awal

Orientasi awalCopy code
[code]
    openclaw onboard --auth-choice baseten-api-key
[/code]

Flag langsungCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice baseten-api-key \--baseten-api-key "$BASETEN_API_KEY"
[/code]

Hanya variabel lingkunganCopy code
[code]
    export BASETEN_API_KEY=...
[/code]

* ### Verifikasi katalog langsung

bashCopy code
[code]
    openclaw models list --provider baseten
[/code]

Dengan autentikasi yang dapat digunakan, Plugin meminta `GET /v1/models` dan mencantumkan setiap model yang dikembalikan untuk akun tersebut. Tanpa autentikasi, Plugin tetap luring dan menggunakan fallback bawaan.

## Inkling

[Inkling dari Thinking Machines Lab](<https://thinkingmachines.ai/news/introducing-inkling/>) adalah model default. Di OpenClaw, model ini mendukung masukan teks dan gambar, pemanggilan alat, skema alat terstruktur, tingkat upaya penalaran yang dapat dikonfigurasi, jendela konteks 1.048 juta token, dan hingga 32 ribu token keluaran:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "baseten/thinkingmachines/inkling" },    },  },}
[/code]

Gunakan `/model baseten/thinkingmachines/inkling` untuk mengganti model pada percakapan yang sudah ada.

## Katalog fallback bawaan

Katalog langsung yang terautentikasi merupakan sumber otoritatif. Baris-baris ini menjaga agar penyiapan dan pemilihan model tetap berguna sebelum penemuan berhasil:

Referensi model | Masukan | Konteks | Keluaran maks.  
---|---|---|---  
`baseten/deepseek-ai/DeepSeek-V4-Pro` | teks | 262k | 262k  
`baseten/zai-org/GLM-4.7` | teks | 200k | 200k  
`baseten/zai-org/GLM-5` | teks | 202k | 202k  
`baseten/zai-org/GLM-5.1` | teks | 202k | 202k  
`baseten/zai-org/GLM-5.2` | teks | 202k | 202k  
`baseten/thinkingmachines/inkling` | teks, gambar | 1.048M | 32k  
`baseten/moonshotai/Kimi-K2.5` | teks, gambar | 262k | 262k  
`baseten/moonshotai/Kimi-K2.6` | teks, gambar | 262k | 262k  
`baseten/moonshotai/Kimi-K2.7-Code` | teks, gambar | 262k | 262k  
`baseten/nvidia/Nemotron-120B-A12B` | teks | 202k | 202k  
`baseten/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B` | teks | 202k | 202k  
`baseten/openai/gpt-oss-120b` | teks | 128k | 128k  
  
Semua model bawaan mendukung pemanggilan alat dan penalaran. OpenClaw memetakan tingkat pemikirannya ke model dengan `reasoning_effort` bawaan. Model GLM, Kimi, dan Nemotron Baseten yang bersifat opsional menggunakan pemikiran nonaktif secara default; sebagian besar menyediakan kontrol biner nonaktif/aktif, sedangkan GLM 5.2 menyediakan nonaktif, tinggi, dan maksimum. OpenClaw mengirimkan pilihan ini melalui kontrol `chat_template_args.enable_thinking` milik Baseten dan, untuk GLM 5.2, parameter tingkat atas `reasoning_effort` yang telah divalidasi.

## Konfigurasi manual

Sebagian besar penyiapan hanya memerlukan kunci API. Untuk menetapkan penyedia secara eksplisit:

json5Copy code
[code]
    {  env: { BASETEN_API_KEY: "..." },  agents: {    defaults: {      model: { primary: "baseten/thinkingmachines/inkling" },    },  },  models: {    mode: "merge",    providers: {      baseten: {        baseUrl: "https://inference.baseten.co/v1",        apiKey: "${BASETEN_API_KEY}",        api: "openai-completions",        models: [          {            id: "thinkingmachines/inkling",            name: "Inkling",            reasoning: true,            input: ["text", "image"],            contextWindow: 1048000,            maxTokens: 32000,            compat: {              supportsStore: false,              supportsDeveloperRole: false,              supportsUsageInStreaming: true,              supportsStrictMode: true,              supportsTools: true,              supportsReasoningEffort: true,              supportedReasoningEfforts: ["none", "minimal", "low", "medium", "high", "xhigh"],              reasoningEffortMap: {                off: "none",                none: "none",                adaptive: "xhigh",                max: "xhigh",              },              maxTokensField: "max_tokens",            },          },        ],      },    },  },}
[/code]

## Terkait

[**Penyedia model** Memilih penyedia, referensi model, dan perilaku failover. ](</id/concepts/model-providers>) [**Mode pemikiran** Pilih tingkat upaya penalaran OpenClaw. ](</id/tools/thinking>) [**CLI model** Cantumkan, periksa, dan pilih model yang ditemukan. ](</id/cli/models>) [**Tanya jawab model** Pemecahan masalah profil autentikasi dan pemilihan model. ](</id/help/faq-models>)

Was this useful?YesNo

Open issue