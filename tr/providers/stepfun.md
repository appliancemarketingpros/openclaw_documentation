---
title: StepFun
source_url: https://docs.openclaw.ai/tr/providers/stepfun
scraped_at: 2026-05-25
---

OpenClaw, iki sağlayıcı kimliğine sahip paketlenmiş bir StepFun sağlayıcı Plugin'i içerir:

  * Standart uç nokta için `stepfun`
  * Step Plan uç noktası için `stepfun-plan`


## Bölge ve uç nokta özeti

Uç nokta | China (`.com`) | Global (`.ai`)  
---|---|---  
Standard | `https://api.stepfun.com/v1` | `https://api.stepfun.ai/v1`  
Step Plan | `https://api.stepfun.com/step_plan/v1` | `https://api.stepfun.ai/step_plan/v1`  
  
Kimlik doğrulama env var: `STEPFUN_API_KEY`

## Yerleşik katalog

Standard (`stepfun`):

Model ref | Bağlam | Maks. çıktı | Notlar  
---|---|---|---  
`stepfun/step-3.5-flash` | 262,144 | 65,536 | Varsayılan standart model  
  
Step Plan (`stepfun-plan`):

Model ref | Bağlam | Maks. çıktı | Notlar  
---|---|---|---  
`stepfun-plan/step-3.5-flash` | 262,144 | 65,536 | Varsayılan Step Plan modeli  
`stepfun-plan/step-3.5-flash-2603` | 262,144 | 65,536 | Ek Step Plan modeli  
  
## Başlarken

Sağlayıcı yüzeyinizi seçin ve kurulum adımlarını izleyin.

### Standard

**En uygun olduğu kullanım:** standart StepFun uç noktası üzerinden genel amaçlı kullanım.

* ### Uç nokta bölgenizi seçin

Kimlik doğrulama seçimi | Uç nokta | Bölge  
---|---|---  
`stepfun-standard-api-key-intl` | `https://api.stepfun.ai/v1` | International  
`stepfun-standard-api-key-cn` | `https://api.stepfun.com/v1` | China  
* ### Onboarding çalıştırın

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl
[/code]

Veya China uç noktası için:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-cn
[/code]

* ### Etkileşimsiz alternatif

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Modellerin kullanılabilir olduğunu doğrulayın

bashCopy code
[code]
    openclaw models list --provider stepfun
[/code]

### Model ref'leri

  * Varsayılan model: `stepfun/step-3.5-flash`


### Step Plan

**En uygun olduğu kullanım:** Step Plan akıl yürütme uç noktası.

* ### Uç nokta bölgenizi seçin

Kimlik doğrulama seçimi | Uç nokta | Bölge  
---|---|---  
`stepfun-plan-api-key-intl` | `https://api.stepfun.ai/step_plan/v1` | International  
`stepfun-plan-api-key-cn` | `https://api.stepfun.com/step_plan/v1` | China  
* ### Onboarding çalıştırın

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl
[/code]

Veya China uç noktası için:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-cn
[/code]

* ### Etkileşimsiz alternatif

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Modellerin kullanılabilir olduğunu doğrulayın

bashCopy code
[code]
    openclaw models list --provider stepfun-plan
[/code]

### Model ref'leri

  * Varsayılan model: `stepfun-plan/step-3.5-flash`
  * Alternatif model: `stepfun-plan/step-3.5-flash-2603`


## Gelişmiş yapılandırma

Tam yapılandırma: Standard sağlayıcı json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      stepfun: {        baseUrl: "https://api.stepfun.ai/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Tam yapılandırma: Step Plan sağlayıcı json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun-plan/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      "stepfun-plan": {        baseUrl: "https://api.stepfun.ai/step_plan/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },          {            id: "step-3.5-flash-2603",            name: "Step 3.5 Flash 2603",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Notlar

  * Sağlayıcı OpenClaw ile paketlenmiş olarak gelir, bu nedenle ayrı bir Plugin yükleme adımı yoktur.
  * `step-3.5-flash-2603` şu anda yalnızca `stepfun-plan` üzerinde sunulur.
  * Tek bir kimlik doğrulama akışı hem `stepfun` hem de `stepfun-plan` için bölgeyle eşleşen profiller yazar; böylece iki yüzey birlikte keşfedilebilir.
  * Modelleri incelemek veya değiştirmek için `openclaw models list` ve `openclaw models set <provider/model>` kullanın.


## İlgili

[**Model seçimi** Tüm sağlayıcılara, model ref'lerine ve failover davranışına genel bakış. ](</tr/concepts/model-providers>) [**Yapılandırma referansı** Sağlayıcılar, modeller ve Plugin'ler için tam yapılandırma şeması. ](</tr/gateway/configuration-reference>) [**Model seçimi** Modelleri seçme ve yapılandırma yöntemi. ](</tr/concepts/models>) [**StepFun Platform** StepFun API anahtarı yönetimi ve dokümantasyonu. ](<https://platform.stepfun.com>)

Was this useful?YesNo