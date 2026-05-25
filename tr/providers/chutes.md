---
title: Chutes
source_url: https://docs.openclaw.ai/tr/providers/chutes
scraped_at: 2026-05-25
---

[Chutes](<https://chutes.ai>), açık kaynak model kataloglarını OpenAI uyumlu bir API üzerinden sunar. OpenClaw, yerleşik `chutes` sağlayıcısı için hem tarayıcı OAuth'u hem de doğrudan API anahtarıyla kimlik doğrulamayı destekler.

Özellik | Değer  
---|---  
Sağlayıcı | `chutes`  
API | OpenAI uyumlu  
Temel URL | `https://llm.chutes.ai/v1`  
Kimlik doğrulama | OAuth veya API anahtarı (aşağıya bakın)  
  
## Başlarken

### OAuth

* ### OAuth ilk kurulum akışını çalıştırın

bashCopy code
[code]
    openclaw onboard --auth-choice chutes
[/code]

OpenClaw, tarayıcı akışını yerel olarak başlatır veya uzak/başsız ana makinelerde bir URL + yönlendirme-yapıştırma akışı gösterir. OAuth token'ları OpenClaw kimlik doğrulama profilleri üzerinden otomatik yenilenir.

* ### Varsayılan modeli doğrulayın

İlk kurulumdan sonra varsayılan model `chutes/zai-org/GLM-4.7-TEE` olarak ayarlanır ve yerleşik Chutes kataloğu kaydedilir.

### API anahtarı

* ### Bir API anahtarı alın

[chutes.ai/settings/api-keys](<https://chutes.ai/settings/api-keys>) adresinde bir anahtar oluşturun.

* ### API anahtarı ilk kurulum akışını çalıştırın

bashCopy code
[code]
    openclaw onboard --auth-choice chutes-api-key
[/code]

* ### Varsayılan modeli doğrulayın

İlk kurulumdan sonra varsayılan model `chutes/zai-org/GLM-4.7-TEE` olarak ayarlanır ve yerleşik Chutes kataloğu kaydedilir.

## Keşif davranışı

Chutes kimlik doğrulaması kullanılabilir olduğunda OpenClaw, bu kimlik bilgisiyle Chutes kataloğunu sorgular ve bulunan modelleri kullanır. Keşif başarısız olursa OpenClaw, ilk kurulumun ve başlatmanın çalışmaya devam etmesi için yerleşik statik kataloğa geri döner.

## Varsayılan takma adlar

OpenClaw, yerleşik Chutes kataloğu için üç kullanışlı takma ad kaydeder:

Takma ad | Hedef model  
---|---  
`chutes-fast` | `chutes/zai-org/GLM-4.7-FP8`  
`chutes-pro` | `chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes-vision` | `chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
  
## Yerleşik başlangıç kataloğu

Yerleşik geri dönüş kataloğu güncel Chutes referanslarını içerir:

Model referansı  
---  
`chutes/zai-org/GLM-4.7-TEE`  
`chutes/zai-org/GLM-5-TEE`  
`chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes/deepseek-ai/DeepSeek-R1-0528-TEE`  
`chutes/moonshotai/Kimi-K2.5-TEE`  
`chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
`chutes/Qwen/Qwen3-Coder-Next-TEE`  
`chutes/openai/gpt-oss-120b-TEE`  
  
## Yapılandırma örneği

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "chutes/zai-org/GLM-4.7-TEE" },      models: {        "chutes/zai-org/GLM-4.7-TEE": { alias: "Chutes GLM 4.7" },        "chutes/deepseek-ai/DeepSeek-V3.2-TEE": { alias: "Chutes DeepSeek V3.2" },      },    },  },}
[/code]

OAuth geçersiz kılmaları

OAuth akışını isteğe bağlı ortam değişkenleriyle özelleştirebilirsiniz:

Değişken | Amaç  
---|---  
`CHUTES_CLIENT_ID` | Özel OAuth istemci kimliği  
`CHUTES_CLIENT_SECRET` | Özel OAuth istemci sırrı  
`CHUTES_OAUTH_REDIRECT_URI` | Özel yönlendirme URI'si  
`CHUTES_OAUTH_SCOPES` | Özel OAuth kapsamları  
  
Yönlendirme uygulaması gereksinimleri ve yardım için [Chutes OAuth belgelerine](<https://chutes.ai/docs/sign-in-with-chutes/overview>) bakın.

Notlar

  * API anahtarı ve OAuth keşfi aynı `chutes` sağlayıcı kimliğini kullanır.
  * Chutes modelleri `chutes/<model-id>` olarak kaydedilir.
  * Başlangıçta keşif başarısız olursa yerleşik statik katalog otomatik olarak kullanılır.


## İlgili

[**Model seçimi** Sağlayıcı kuralları, model referansları ve yük devretme davranışı. ](</tr/concepts/model-providers>) [**Yapılandırma referansı** Sağlayıcı ayarlarını da içeren tam yapılandırma şeması. ](</tr/gateway/configuration-reference>) [**Chutes** Chutes panosu ve API belgeleri. ](<https://chutes.ai>) [**Chutes API anahtarları** Chutes API anahtarları oluşturun ve yönetin. ](<https://chutes.ai/settings/api-keys>)

Was this useful?YesNo