---
title: SGLang
source_url: https://docs.openclaw.ai/tr/providers/sglang
scraped_at: 2026-05-25
---

SGLang, açık ağırlıklı modelleri OpenAI uyumlu bir HTTP API üzerinden sunar. OpenClaw, kullanılabilir modellerin otomatik keşfiyle `openai-completions` sağlayıcı ailesini kullanarak SGLang'e bağlanır.

Özellik | Değer  
---|---  
Sağlayıcı kimliği | `sglang`  
Plugin | pakete dahil, `enabledByDefault: true`  
Kimlik doğrulama ortam değişkeni | `SGLANG_API_KEY` (sunucuda kimlik doğrulama yoksa boş olmayan herhangi bir değer)  
Başlangıç kurulumu bayrağı | `--auth-choice sglang`  
API | OpenAI uyumlu (`openai-completions`)  
Varsayılan taban URL'si | `http://127.0.0.1:30000/v1`  
Varsayılan model yer tutucusu | `sglang/Qwen/Qwen3-8B`  
Akış kullanımı | Evet (`supportsStreamingUsage: true`)  
Fiyatlandırma | Harici ücretsiz olarak işaretlendi (`modelPricing.external: false`)  
  
OpenClaw ayrıca `SGLANG_API_KEY` ile katılım sağladığınızda SGLang'den kullanılabilir modelleri **otomatik olarak keşfeder**. Özel bir SGLang taban URL'si de yapılandırdığınızda keşfi dinamik tutmak için `agents.defaults.models` içinde `sglang/*` kullanın. Aşağıdaki Model keşfi (örtük sağlayıcı) bölümüne bakın.

## Başlarken

* ### SGLang'i başlat

SGLang'i OpenAI uyumlu bir sunucuyla başlatın. Taban URL'niz `/v1` uç noktalarını göstermelidir (örneğin `/v1/models`, `/v1/chat/completions`). SGLang genellikle şurada çalışır:

  * `http://127.0.0.1:30000/v1`


* ### Bir API anahtarı ayarla

Sunucunuzda kimlik doğrulama yapılandırılmadıysa herhangi bir değer çalışır:

bashCopy code
[code]
    export SGLANG_API_KEY="sglang-local"
[/code]

* ### Başlangıç kurulumunu çalıştır veya doğrudan bir model ayarla

bashCopy code
[code]
    openclaw onboard
[/code]

Ya da modeli elle yapılandırın:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "sglang/your-model-id" },    },  },}
[/code]

## Model keşfi (örtük sağlayıcı)

`SGLANG_API_KEY` ayarlandığında (veya bir kimlik doğrulama profili mevcut olduğunda) ve `models.providers.sglang` tanımlamadığınızda, OpenClaw şunu sorgular:

  * `GET http://127.0.0.1:30000/v1/models`


ve döndürülen kimlikleri model girdilerine dönüştürür.

## Açık yapılandırma (elle modeller)

Şu durumlarda açık yapılandırma kullanın:

  * SGLang farklı bir ana makinede/bağlantı noktasında çalışıyorsa.
  * `contextWindow`/`maxTokens` değerlerini sabitlemek istiyorsanız.
  * Sunucunuz gerçek bir API anahtarı gerektiriyorsa (veya başlıkları denetlemek istiyorsanız).

json5Copy code
[code]
    {  models: {    providers: {      sglang: {        baseUrl: "http://127.0.0.1:30000/v1",        apiKey: "${SGLANG_API_KEY}",        api: "openai-completions",        models: [          {            id: "your-model-id",            name: "Local SGLang Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## Gelişmiş yapılandırma

Proxy tarzı davranış

SGLang, yerel bir OpenAI uç noktası değil, proxy tarzı OpenAI uyumlu bir `/v1` arka ucu olarak ele alınır.

Davranış | SGLang  
---|---  
Yalnızca OpenAI'ye özgü istek şekillendirme | Uygulanmaz  
`service_tier`, Responses `store`, istem önbelleği ipuçları | Gönderilmez  
Akıl yürütme uyumluluğu yük şekillendirmesi | Uygulanmaz  
Gizli ilişkilendirme başlıkları (`originator`, `version`, `User-Agent`) | Özel SGLang taban URL'lerine enjekte edilmez  
Sorun giderme

**Sunucuya ulaşılamıyor**

Sunucunun çalıştığını ve yanıt verdiğini doğrulayın:

bashCopy code
[code]
    curl http://127.0.0.1:30000/v1/models
[/code]

**Kimlik doğrulama hataları**

İstekler kimlik doğrulama hatalarıyla başarısız olursa, sunucu yapılandırmanızla eşleşen gerçek bir `SGLANG_API_KEY` ayarlayın veya sağlayıcıyı `models.providers.sglang` altında açıkça yapılandırın.

## İlgili

[**Model seçimi** Sağlayıcıları, model referanslarını ve yük devretme davranışını seçme. ](</tr/concepts/model-providers>) [**Yapılandırma referansı** Sağlayıcı girdilerini içeren tam yapılandırma şeması. ](</tr/gateway/configuration-reference>)

Was this useful?YesNo