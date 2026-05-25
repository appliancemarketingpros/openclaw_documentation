---
title: StepFun
source_url: https://docs.openclaw.ai/id/providers/stepfun
scraped_at: 2026-05-25
---

OpenClaw menyertakan Plugin penyedia StepFun bawaan dengan dua id penyedia:

  * `stepfun` untuk endpoint standar
  * `stepfun-plan` untuk endpoint Step Plan


## Ringkasan region dan endpoint

Endpoint | China (`.com`) | Global (`.ai`)  
---|---|---  
Standar | `https://api.stepfun.com/v1` | `https://api.stepfun.ai/v1`  
Step Plan | `https://api.stepfun.com/step_plan/v1` | `https://api.stepfun.ai/step_plan/v1`  
  
Variabel env autentikasi: `STEPFUN_API_KEY`

## Katalog bawaan

Standar (`stepfun`):

Ref model | Konteks | Output maks | Catatan  
---|---|---|---  
`stepfun/step-3.5-flash` | 262,144 | 65,536 | Model standar default  
  
Step Plan (`stepfun-plan`):

Ref model | Konteks | Output maks | Catatan  
---|---|---|---  
`stepfun-plan/step-3.5-flash` | 262,144 | 65,536 | Model Step Plan default  
`stepfun-plan/step-3.5-flash-2603` | 262,144 | 65,536 | Model Step Plan tambahan  
  
## Mulai menggunakan

Pilih permukaan penyedia Anda dan ikuti langkah penyiapannya.

### Standar

**Paling cocok untuk:** penggunaan umum melalui endpoint StepFun standar.

* ### Pilih region endpoint Anda

Pilihan autentikasi | Endpoint | Region  
---|---|---  
`stepfun-standard-api-key-intl` | `https://api.stepfun.ai/v1` | Internasional  
`stepfun-standard-api-key-cn` | `https://api.stepfun.com/v1` | China  
* ### Jalankan onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl
[/code]

Atau untuk endpoint China:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-cn
[/code]

* ### Alternatif noninteraktif

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Verifikasi model tersedia

bashCopy code
[code]
    openclaw models list --provider stepfun
[/code]

### Ref model

  * Model default: `stepfun/step-3.5-flash`


### Step Plan

**Paling cocok untuk:** endpoint penalaran Step Plan.

* ### Pilih region endpoint Anda

Pilihan autentikasi | Endpoint | Region  
---|---|---  
`stepfun-plan-api-key-intl` | `https://api.stepfun.ai/step_plan/v1` | Internasional  
`stepfun-plan-api-key-cn` | `https://api.stepfun.com/step_plan/v1` | China  
* ### Jalankan onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl
[/code]

Atau untuk endpoint China:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-cn
[/code]

* ### Alternatif noninteraktif

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Verifikasi model tersedia

bashCopy code
[code]
    openclaw models list --provider stepfun-plan
[/code]

### Ref model

  * Model default: `stepfun-plan/step-3.5-flash`
  * Model alternatif: `stepfun-plan/step-3.5-flash-2603`


## Konfigurasi lanjutan

Konfigurasi lengkap: Penyedia standar json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      stepfun: {        baseUrl: "https://api.stepfun.ai/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Konfigurasi lengkap: Penyedia Step Plan json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun-plan/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      "stepfun-plan": {        baseUrl: "https://api.stepfun.ai/step_plan/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },          {            id: "step-3.5-flash-2603",            name: "Step 3.5 Flash 2603",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Catatan

  * Penyedia ini dibundel dengan OpenClaw, jadi tidak ada langkah instalasi Plugin terpisah.
  * `step-3.5-flash-2603` saat ini hanya diekspos di `stepfun-plan`.
  * Satu alur autentikasi menulis profil yang cocok dengan region untuk `stepfun` dan `stepfun-plan`, sehingga kedua permukaan dapat ditemukan bersama-sama.
  * Gunakan `openclaw models list` dan `openclaw models set <provider/model>` untuk memeriksa atau mengganti model.


## Terkait

[**Pemilihan model** Ringkasan semua penyedia, ref model, dan perilaku failover. ](</id/concepts/model-providers>) [**Referensi konfigurasi** Skema konfigurasi lengkap untuk penyedia, model, dan plugins. ](</id/gateway/configuration-reference>) [**Pemilihan model** Cara memilih dan mengonfigurasi model. ](</id/concepts/models>) [**Platform StepFun** Pengelolaan kunci API dan dokumentasi StepFun. ](<https://platform.stepfun.com>)

Was this useful?YesNo