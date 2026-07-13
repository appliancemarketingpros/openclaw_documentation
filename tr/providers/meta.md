---
title: Meta
source_url: https://docs.openclaw.ai/tr/providers/meta
scraped_at: 2026-07-13
---

ModelsProviders

**Meta API** , `muse-spark-1.1` akıl yürütme modeli için OpenAI uyumlu **Responses API** 'yi (`POST /v1/responses`) kullanır. Sağlayıcı, OpenClaw ile birlikte gelen bir Plugin olarak sunulur.

Özellik | Değer  
---|---  
Sağlayıcı kimliği | `meta`  
Plugin | birlikte gelen sağlayıcı  
Kimlik doğrulama ortam değişkeni | `MODEL_API_KEY`  
İlk kurulum bayrağı | `--auth-choice meta-api-key`  
Doğrudan CLI bayrağı | `--meta-api-key <key>`  
API | Responses API (`openai-responses`)  
Temel URL | `https://api.meta.ai/v1`  
Varsayılan model | `meta/muse-spark-1.1`  
Varsayılan akıl yürütme | `high` (`reasoning.effort`)  
  
## Başlarken

* ### API anahtarını ayarlayın

OnboardingCopy code
[code]
    openclaw onboard --auth-choice meta-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \--auth-choice meta-api-key \--meta-api-key "$MODEL_API_KEY"
[/code]

Env onlyCopy code
[code]
    export MODEL_API_KEY=<key>
[/code]

* ### Modellerin kullanılabilir olduğunu doğrulayın

bashCopy code
[code]
    openclaw models list --provider meta
[/code]

Statik `muse-spark-1.1` katalog girdisini listeler. `MODEL_API_KEY` çözümlenemiyorsa `openclaw models status --json`, eksik kimlik bilgisini `auth.unusableProfiles` altında bildirir.

## Etkileşimsiz kurulum

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --mode local \  --auth-choice meta-api-key \  --meta-api-key "$MODEL_API_KEY"
[/code]

## Yerleşik katalog

Model referansı | Ad | Akıl yürütme | Bağlam penceresi | En fazla çıktı  
---|---|---|---|---  
`meta/muse-spark-1.1` | Muse Spark 1.1 | evet | 1,048,576 | 131,072  
  
Yetenekler:

  * Metin + görüntü girdisi
  * Araç çağırma ve akış
  * Akıl yürütme yoğunluğu: `minimal`, `low`, `medium`, `high`, `xhigh` (varsayılan: `high`)
  * Durumsuz şifreli akıl yürütme yeniden oynatımı (`store: false`, `include: ["reasoning.encrypted_content"]`)


## Elle yapılandırma

json5Copy code
[code]
    {  env: { MODEL_API_KEY: "<key>" },  agents: {    defaults: {      model: { primary: "meta/muse-spark-1.1" },      models: {        "meta/muse-spark-1.1": { alias: "Muse Spark 1.1" },      },    },  },}
[/code]

## Hızlı doğrulama testi

bashCopy code
[code]
    export MODEL_API_KEY=<key>pnpm test:live -- extensions/meta/meta.live.test.ts
[/code]

Canlı testler, `POST /v1/responses` uç noktasına karşı `muse-spark-1.1` kullanır.

## İlgili konular

[**Model sağlayıcıları** Sağlayıcıları, model referanslarını ve yük devretme davranışını seçme. ](</tr/concepts/model-providers>) [**Düşünme modları** muse-spark-1.1 için akıl yürütme yoğunluğu düzeyleri. ](</tr/tools/thinking>) [**Yapılandırma başvurusu** Ajan varsayılanları ve model yapılandırması. ](</tr/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue