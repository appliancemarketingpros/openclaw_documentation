---
title: Synthetic
source_url: https://docs.openclaw.ai/id/providers/synthetic
scraped_at: 2026-05-25
---

[Synthetic](<https://synthetic.new>) mengekspos endpoint yang kompatibel dengan Anthropic. OpenClaw mendaftarkannya sebagai provider `synthetic` dan menggunakan API Anthropic Messages.

Properti | Nilai  
---|---  
Provider | `synthetic`  
Auth | `SYNTHETIC_API_KEY`  
API | Anthropic Messages  
Base URL | `https://api.synthetic.new/anthropic`  
  
## Memulai

* ### Dapatkan API key

Dapatkan `SYNTHETIC_API_KEY` dari akun Synthetic Anda, atau biarkan wizard onboarding memintanya dari Anda.

* ### Jalankan onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice synthetic-api-key
[/code]

* ### Verifikasi model default

Setelah onboarding, model default diatur ke:

CodeCopy code
[code]
    synthetic/hf:MiniMaxAI/MiniMax-M2.5
[/code]

## Contoh konfigurasi

json5Copy code
[code]
    {  env: { SYNTHETIC_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.5" },      models: { "synthetic/hf:MiniMaxAI/MiniMax-M2.5": { alias: "MiniMax M2.5" } },    },  },  models: {    mode: "merge",    providers: {      synthetic: {        baseUrl: "https://api.synthetic.new/anthropic",        apiKey: "${SYNTHETIC_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "hf:MiniMaxAI/MiniMax-M2.5",            name: "MiniMax M2.5",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 192000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## Katalog bawaan

Semua model Synthetic menggunakan biaya `0` (input/output/cache).

ID Model | Jendela konteks | Token maks | Reasoning | Input  
---|---|---|---|---  
`hf:MiniMaxAI/MiniMax-M2.5` | 192,000 | 65,536 | tidak | text  
`hf:moonshotai/Kimi-K2-Thinking` | 256,000 | 8,192 | ya | text  
`hf:zai-org/GLM-4.7` | 198,000 | 128,000 | tidak | text  
`hf:deepseek-ai/DeepSeek-R1-0528` | 128,000 | 8,192 | tidak | text  
`hf:deepseek-ai/DeepSeek-V3-0324` | 128,000 | 8,192 | tidak | text  
`hf:deepseek-ai/DeepSeek-V3.1` | 128,000 | 8,192 | tidak | text  
`hf:deepseek-ai/DeepSeek-V3.1-Terminus` | 128,000 | 8,192 | tidak | text  
`hf:deepseek-ai/DeepSeek-V3.2` | 159,000 | 8,192 | tidak | text  
`hf:meta-llama/Llama-3.3-70B-Instruct` | 128,000 | 8,192 | tidak | text  
`hf:meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | 524,000 | 8,192 | tidak | text  
`hf:moonshotai/Kimi-K2-Instruct-0905` | 256,000 | 8,192 | tidak | text  
`hf:moonshotai/Kimi-K2.5` | 256,000 | 8,192 | ya | text + image  
`hf:openai/gpt-oss-120b` | 128,000 | 8,192 | tidak | text  
`hf:Qwen/Qwen3-235B-A22B-Instruct-2507` | 256,000 | 8,192 | tidak | text  
`hf:Qwen/Qwen3-Coder-480B-A35B-Instruct` | 256,000 | 8,192 | tidak | text  
`hf:Qwen/Qwen3-VL-235B-A22B-Instruct` | 250,000 | 8,192 | tidak | text + image  
`hf:zai-org/GLM-4.5` | 128,000 | 128,000 | tidak | text  
`hf:zai-org/GLM-4.6` | 198,000 | 128,000 | tidak | text  
`hf:zai-org/GLM-5` | 256,000 | 128,000 | ya | text + image  
`hf:deepseek-ai/DeepSeek-V3` | 128,000 | 8,192 | tidak | text  
`hf:Qwen/Qwen3-235B-A22B-Thinking-2507` | 256,000 | 8,192 | ya | text  
  
Allowlist model

Jika Anda mengaktifkan allowlist model (`agents.defaults.models`), tambahkan setiap model Synthetic yang ingin Anda gunakan. Model yang tidak ada di allowlist akan disembunyikan dari agen.

Override base URL

Jika Synthetic mengubah endpoint API-nya, override base URL di konfigurasi Anda:

json5Copy code
[code]
    {  models: {    providers: {      synthetic: {        baseUrl: "https://new-api.synthetic.new/anthropic",      },    },  },}
[/code]

Ingat bahwa OpenClaw otomatis menambahkan `/v1`.

## Terkait

[**Model selection** Aturan provider, referensi model, dan perilaku failover. ](</id/concepts/model-providers>) [**Configuration reference** Skema konfigurasi lengkap termasuk pengaturan provider. ](</id/gateway/configuration-reference>) [**Synthetic** Dashboard Synthetic dan dokumentasi API. ](<https://synthetic.new>)

Was this useful?YesNo