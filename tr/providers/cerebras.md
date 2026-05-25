---
title: Cerebras
source_url: https://docs.openclaw.ai/tr/providers/cerebras
scraped_at: 2026-05-25
---

[Cerebras](<https://www.cerebras.ai>), özel çıkarım donanımı üzerinde yüksek hızlı, OpenAI uyumlu çıkarım sağlar. OpenClaw, statik dört modelli kataloğa sahip paketlenmiş bir Cerebras sağlayıcı Plugin’i içerir.

Özellik | Değer  
---|---  
Sağlayıcı kimliği | `cerebras`  
Plugin | paketlenmiş, `enabledByDefault: true`  
Kimlik doğrulama env var | `CEREBRAS_API_KEY`  
Başlatma bayrağı | `--auth-choice cerebras-api-key`  
Doğrudan CLI bayrağı | `--cerebras-api-key <key>`  
API | OpenAI uyumlu (`openai-completions`)  
Temel URL | `https://api.cerebras.ai/v1`  
Varsayılan model | `cerebras/zai-glm-4.7`  
  
## Başlarken

* ### Bir API anahtarı alın

[Cerebras Cloud Console](<https://cloud.cerebras.ai>) içinde bir API anahtarı oluşturun.

* ### Başlatmayı çalıştırın

OnboardingCopy code
[code]
    openclaw onboard --auth-choice cerebras-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice cerebras-api-key \--cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

Env onlyCopy code
[code]
    export CEREBRAS_API_KEY=csk-...
[/code]

* ### Modellerin kullanılabilir olduğunu doğrulayın

bashCopy code
[code]
    openclaw models list --provider cerebras
[/code]

Liste, paketlenmiş dört modelin tamamını içermelidir. `CEREBRAS_API_KEY` çözümlenmemişse, `openclaw models status --json` eksik kimlik bilgisini `auth.unusableProfiles` altında bildirir.

## Etkileşimsiz kurulum

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cerebras-api-key \  --cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

## Yerleşik katalog

OpenClaw, herkese açık OpenAI uyumlu uç noktayı yansıtan statik bir Cerebras kataloğuyla gelir. Dört modelin tamamı 128k bağlamı ve 8.192 maksimum çıktı token’ını paylaşır.

Model ref | Ad | Akıl yürütme | Notlar  
---|---|---|---  
`cerebras/zai-glm-4.7` | [Z.ai](<http://Z.ai>) GLM 4.7 | evet | Varsayılan model; önizleme akıl yürütme modeli  
`cerebras/gpt-oss-120b` | GPT OSS 120B | evet | Üretim akıl yürütme modeli  
`cerebras/qwen-3-235b-a22b-instruct-2507` | Qwen 3 235B Instruct | hayır | Önizleme akıl yürütmeyen model  
`cerebras/llama3.1-8b` | Llama 3.1 8B | hayır | Üretim için hız odaklı model  
  
## Manuel yapılandırma

Paketlenmiş Plugin genellikle yalnızca API anahtarına ihtiyaç duyduğunuz anlamına gelir. Model meta verilerini geçersiz kılmak veya statik kataloğa karşı `mode: "merge"` ile çalışmak istediğinizde açık `models.providers.cerebras` yapılandırması kullanın:

json5Copy code
[code]
    {  env: { CEREBRAS_API_KEY: "csk-..." },  agents: {    defaults: {      model: { primary: "cerebras/zai-glm-4.7" },    },  },  models: {    mode: "merge",    providers: {      cerebras: {        baseUrl: "https://api.cerebras.ai/v1",        apiKey: "${CEREBRAS_API_KEY}",        api: "openai-completions",        models: [          { id: "zai-glm-4.7", name: "Z.ai GLM 4.7" },          { id: "gpt-oss-120b", name: "GPT OSS 120B" },        ],      },    },  },}
[/code]

## İlgili

[**Model sağlayıcıları** Sağlayıcıları, model ref’lerini ve yük devretme davranışını seçme. ](</tr/concepts/model-providers>) [**Düşünme modları** Akıl yürütme yetenekli iki Cerebras modeli için akıl yürütme çabası düzeyleri. ](</tr/tools/thinking>) [**Yapılandırma referansı** Agent varsayılanları ve model yapılandırması. ](</tr/gateway/config-agents#agent-defaults>) [**Modeller SSS** Kimlik doğrulama profilleri, modeller arasında geçiş yapma ve "no profile" hatalarını çözme. ](</tr/help/faq-models>)

Was this useful?YesNo