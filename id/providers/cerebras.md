---
title: Cerebras
source_url: https://docs.openclaw.ai/id/providers/cerebras
scraped_at: 2026-05-25
---

[Cerebras](<https://www.cerebras.ai>) menyediakan inferensi berkecepatan tinggi yang kompatibel dengan OpenAI pada perangkat keras inferensi khusus. OpenClaw menyertakan Plugin penyedia Cerebras yang dibundel dengan katalog statis empat model.

Properti | Nilai  
---|---  
ID penyedia | `cerebras`  
Plugin | dibundel, `enabledByDefault: true`  
Variabel env autentikasi | `CEREBRAS_API_KEY`  
Flag orientasi | `--auth-choice cerebras-api-key`  
Flag CLI langsung | `--cerebras-api-key <key>`  
API | kompatibel dengan OpenAI (`openai-completions`)  
URL dasar | `https://api.cerebras.ai/v1`  
Model bawaan | `cerebras/zai-glm-4.7`  
  
## Memulai

* ### Dapatkan kunci API

Buat kunci API di [Cerebras Cloud Console](<https://cloud.cerebras.ai>).

* ### Jalankan orientasi

OrientasiCopy code
[code]
    openclaw onboard --auth-choice cerebras-api-key
[/code]

Flag langsungCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice cerebras-api-key \--cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

Hanya envCopy code
[code]
    export CEREBRAS_API_KEY=csk-...
[/code]

* ### Verifikasi model tersedia

bashCopy code
[code]
    openclaw models list --provider cerebras
[/code]

Daftar tersebut seharusnya menyertakan keempat model yang dibundel. Jika `CEREBRAS_API_KEY` tidak terselesaikan, `openclaw models status --json` melaporkan kredensial yang hilang di bawah `auth.unusableProfiles`.

## Penyiapan non-interaktif

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cerebras-api-key \  --cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

## Katalog bawaan

OpenClaw mengirimkan katalog statis Cerebras yang mencerminkan endpoint publik yang kompatibel dengan OpenAI. Keempat model berbagi konteks 128k dan 8.192 token output maksimum.

Ref model | Nama | Penalaran | Catatan  
---|---|---|---  
`cerebras/zai-glm-4.7` | [Z.ai](<http://Z.ai>) GLM 4.7 | ya | Model bawaan; model penalaran pratinjau  
`cerebras/gpt-oss-120b` | GPT OSS 120B | ya | Model penalaran produksi  
`cerebras/qwen-3-235b-a22b-instruct-2507` | Qwen 3 235B Instruct | tidak | Model non-penalaran pratinjau  
`cerebras/llama3.1-8b` | Llama 3.1 8B | tidak | Model produksi yang berfokus pada kecepatan  
  
## Konfigurasi manual

Plugin yang dibundel biasanya berarti Anda hanya memerlukan kunci API. Gunakan konfigurasi eksplisit `models.providers.cerebras` ketika Anda ingin menimpa metadata model atau berjalan dalam `mode: "merge"` terhadap katalog statis:

json5Copy code
[code]
    {  env: { CEREBRAS_API_KEY: "csk-..." },  agents: {    defaults: {      model: { primary: "cerebras/zai-glm-4.7" },    },  },  models: {    mode: "merge",    providers: {      cerebras: {        baseUrl: "https://api.cerebras.ai/v1",        apiKey: "${CEREBRAS_API_KEY}",        api: "openai-completions",        models: [          { id: "zai-glm-4.7", name: "Z.ai GLM 4.7" },          { id: "gpt-oss-120b", name: "GPT OSS 120B" },        ],      },    },  },}
[/code]

## Terkait

[**Penyedia model** Memilih penyedia, ref model, dan perilaku failover. ](</id/concepts/model-providers>) [**Mode berpikir** Tingkat upaya penalaran untuk dua model Cerebras yang mendukung penalaran. ](</id/tools/thinking>) [**Referensi konfigurasi** Bawaan agen dan konfigurasi model. ](</id/gateway/config-agents#agent-defaults>) [**FAQ model** Profil autentikasi, mengganti model, dan menyelesaikan galat "no profile". ](</id/help/faq-models>)

Was this useful?YesNo