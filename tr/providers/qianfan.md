---
title: Qianfan
source_url: https://docs.openclaw.ai/tr/providers/qianfan
scraped_at: 2026-05-25
---

Qianfan, Baidu'nun MaaS platformudur; istekleri tek bir endpoint ve API anahtarı arkasındaki birçok modele yönlendiren **birleşik bir API** sağlar. OpenAI uyumludur, bu nedenle çoğu OpenAI SDK'sı temel URL değiştirilerek çalışır.

Özellik | Değer  
---|---  
Sağlayıcı | `qianfan`  
Kimlik doğrulama | `QIANFAN_API_KEY`  
API | OpenAI uyumlu  
Temel URL | `https://qianfan.baidubce.com/v2`  
  
## Başlarken

* ### Baidu Cloud hesabı oluşturun

[Qianfan Console](<https://console.bce.baidu.com/qianfan/ais/console/apiKey>) üzerinden kaydolun veya oturum açın ve Qianfan API erişiminizin etkin olduğundan emin olun.

* ### API anahtarı oluşturun

Yeni bir uygulama oluşturun veya mevcut bir uygulamayı seçin, ardından bir API anahtarı oluşturun. Anahtar biçimi `bce-v3/ALTAK-...` şeklindedir.

* ### Onboarding'i çalıştırın

bashCopy code
[code]
    openclaw onboard --auth-choice qianfan-api-key
[/code]

* ### Modelin kullanılabilir olduğunu doğrulayın

bashCopy code
[code]
    openclaw models list --provider qianfan
[/code]

## Yerleşik katalog

Model ref | Girdi | Bağlam | Maks. çıktı | Akıl yürütme | Notlar  
---|---|---|---|---|---  
`qianfan/deepseek-v3.2` | metin | 98,304 | 32,768 | Evet | Varsayılan model  
`qianfan/ernie-5.0-thinking-preview` | metin, görüntü | 119,000 | 64,000 | Evet | Çok modlu  
  
## Yapılandırma örneği

json5Copy code
[code]
    {  env: { QIANFAN_API_KEY: "bce-v3/ALTAK-..." },  agents: {    defaults: {      model: { primary: "qianfan/deepseek-v3.2" },      models: {        "qianfan/deepseek-v3.2": { alias: "QIANFAN" },      },    },  },  models: {    providers: {      qianfan: {        baseUrl: "https://qianfan.baidubce.com/v2",        api: "openai-completions",        models: [          {            id: "deepseek-v3.2",            name: "DEEPSEEK V3.2",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 98304,            maxTokens: 32768,          },          {            id: "ernie-5.0-thinking-preview",            name: "ERNIE-5.0-Thinking-Preview",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 119000,            maxTokens: 64000,          },        ],      },    },  },}
[/code]

Taşıma ve uyumluluk

Qianfan, yerel OpenAI istek biçimlendirmesiyle değil, OpenAI uyumlu taşıma yolu üzerinden çalışır. Bu, standart OpenAI SDK özelliklerinin çalıştığı, ancak sağlayıcıya özgü parametrelerin iletilmeyebileceği anlamına gelir.

Katalog ve geçersiz kılmalar

Paketlenmiş katalog şu anda `deepseek-v3.2` ve `ernie-5.0-thinking-preview` içerir. `models.providers.qianfan` değerini yalnızca özel bir temel URL'ye veya model meta verilerine ihtiyacınız olduğunda ekleyin ya da geçersiz kılın.

Sorun giderme

  * API anahtarınızın `bce-v3/ALTAK-` ile başladığından ve Baidu Cloud konsolunda Qianfan API erişiminin etkin olduğundan emin olun.
  * Modeller listelenmiyorsa, hesabınızda Qianfan hizmetinin etkinleştirildiğini doğrulayın.
  * Varsayılan temel URL `https://qianfan.baidubce.com/v2` şeklindedir. Yalnızca özel bir endpoint veya proxy kullanıyorsanız değiştirin.


## İlgili

[**Model seçimi** Sağlayıcıları, model ref değerlerini ve failover davranışını seçme. ](</tr/concepts/model-providers>) [**Yapılandırma referansı** Eksiksiz OpenClaw yapılandırma referansı. ](</tr/gateway/configuration-reference>) [**Agent kurulumu** Agent varsayılanlarını ve model atamalarını yapılandırma. ](</tr/concepts/agent>) [**Qianfan API belgeleri** Resmi Qianfan API belgeleri. ](<https://cloud.baidu.com/doc/qianfan-api/s/3m7of64lb>)

Was this useful?YesNo