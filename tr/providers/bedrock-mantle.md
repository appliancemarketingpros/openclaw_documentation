---
title: Amazon Bedrock Mantle
source_url: https://docs.openclaw.ai/tr/providers/bedrock-mantle
scraped_at: 2026-05-25
---

OpenClaw, Mantle OpenAI uyumlu uç noktasına bağlanan paketli bir **Amazon Bedrock Mantle** sağlayıcısı içerir. Mantle, açık kaynaklı ve üçüncü taraf modelleri (GPT-OSS, Qwen, Kimi, GLM ve benzerleri) Bedrock altyapısıyla desteklenen standart bir `/v1/chat/completions` yüzeyi üzerinden barındırır.

Özellik | Değer  
---|---  
Sağlayıcı Kimliği | `amazon-bedrock-mantle`  
API | `openai-completions` (OpenAI uyumlu) veya `anthropic-messages` (Anthropic Messages rotası)  
Kimlik doğrulama | Açık `AWS_BEARER_TOKEN_BEDROCK` veya IAM kimlik bilgisi zinciriyle bearer token oluşturma  
Varsayılan bölge | `us-east-1` (`AWS_REGION` veya `AWS_DEFAULT_REGION` ile geçersiz kılın)  
  
## Başlarken

Tercih ettiğiniz kimlik doğrulama yöntemini seçin ve kurulum adımlarını izleyin.

### Açık bearer token

**En uygun olduğu durum:** Zaten bir Mantle bearer token'ınız olan ortamlar.

* ### Bearer token'ı Gateway ana makinesinde ayarlayın

bashCopy code
[code]
    export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

İsteğe bağlı olarak bir bölge ayarlayın (varsayılan `us-east-1`):

bashCopy code
[code]
    export AWS_REGION="us-west-2"
[/code]

* ### Modellerin keşfedildiğini doğrulayın

bashCopy code
[code]
    openclaw models list
[/code]

Keşfedilen modeller `amazon-bedrock-mantle` sağlayıcısı altında görünür. Varsayılanları geçersiz kılmak istemiyorsanız ek yapılandırma gerekmez.

### IAM kimlik bilgileri

**En uygun olduğu durum:** AWS SDK uyumlu kimlik bilgilerini kullanma (paylaşılan yapılandırma, SSO, web kimliği, instance veya görev rolleri).

* ### Gateway ana makinesinde AWS kimlik bilgilerini yapılandırın

Herhangi bir AWS SDK uyumlu kimlik doğrulama kaynağı çalışır:

bashCopy code
[code]
    export AWS_PROFILE="default"export AWS_REGION="us-west-2"
[/code]

* ### Modellerin keşfedildiğini doğrulayın

bashCopy code
[code]
    openclaw models list
[/code]

OpenClaw, kimlik bilgisi zincirinden otomatik olarak bir Mantle bearer token oluşturur.

## Otomatik model keşfi

`AWS_BEARER_TOKEN_BEDROCK` ayarlandığında OpenClaw bunu doğrudan kullanır. Aksi takdirde, OpenClaw AWS varsayılan kimlik bilgisi zincirinden bir Mantle bearer token oluşturmayı dener. Ardından bölgenin `/v1/models` uç noktasını sorgulayarak kullanılabilir Mantle modellerini keşfeder.

Davranış | Ayrıntı  
---|---  
Keşif önbelleği | Sonuçlar 1 saat önbelleğe alınır  
IAM token yenileme | Saatlik  
  
Mantle Plugin'ini etkin tutup otomatik keşfi ve IAM bearer-token oluşturmayı bastırmak için Plugin'e ait keşif anahtarını devre dışı bırakın:

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock-mantle.config.discovery.enabled false
[/code]

### Desteklenen bölgeler

`us-east-1`, `us-east-2`, `us-west-2`, `ap-northeast-1`, `ap-south-1`, `ap-southeast-3`, `eu-central-1`, `eu-west-1`, `eu-west-2`, `eu-south-1`, `eu-north-1`, `sa-east-1`.

## Manuel yapılandırma

Otomatik keşif yerine açık yapılandırmayı tercih ediyorsanız:

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        baseUrl: "https://bedrock-mantle.us-east-1.api.aws/v1",        api: "openai-completions",        auth: "api-key",        apiKey: "env:AWS_BEARER_TOKEN_BEDROCK",        models: [          {            id: "gpt-oss-120b",            name: "GPT-OSS 120B",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32000,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

## Gelişmiş yapılandırma

Akıl yürütme desteği

Akıl yürütme desteği, `thinking`, `reasoner` veya `gpt-oss-120b` gibi kalıpları içeren model kimliklerinden çıkarılır. OpenClaw, keşif sırasında eşleşen modeller için `reasoning: true` değerini otomatik olarak ayarlar.

Uç nokta kullanılamazlığı

Mantle uç noktası kullanılamıyorsa veya model döndürmüyorsa sağlayıcı sessizce atlanır. OpenClaw hata vermez; yapılandırılmış diğer sağlayıcılar normal şekilde çalışmaya devam eder.

Anthropic Messages rotası üzerinden Claude Opus 4.7

Mantle ayrıca Claude modellerini aynı bearer kimlik doğrulamalı akış yolu üzerinden taşıyan bir Anthropic Messages rotası da sunar. Claude Opus 4.7 (`amazon-bedrock-mantle/claude-opus-4.7`), sağlayıcıya ait akışla bu rota üzerinden çağrılabilir; bu nedenle AWS bearer token'ları Anthropic API anahtarları gibi ele alınmaz.

Mantle sağlayıcısında bir Anthropic Messages modelini sabitlediğinizde OpenClaw, o model için `openai-completions` yerine `anthropic-messages` API yüzeyini kullanır. Kimlik doğrulama yine `AWS_BEARER_TOKEN_BEDROCK` üzerinden (veya üretilen IAM bearer token ile) gelir.

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        models: [          {            id: "claude-opus-4.7",            name: "Claude Opus 4.7",            api: "anthropic-messages",            reasoning: true,            input: ["text", "image"],            contextWindow: 1000000,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Amazon Bedrock sağlayıcısıyla ilişkisi

Bedrock Mantle, standart [Amazon Bedrock](</tr/providers/bedrock>) sağlayıcısından ayrı bir sağlayıcıdır. Mantle OpenAI uyumlu bir `/v1` yüzeyi kullanırken standart Bedrock sağlayıcısı yerel Bedrock API'sini kullanır.

Mevcut olduğunda iki sağlayıcı da aynı `AWS_BEARER_TOKEN_BEDROCK` kimlik bilgisini paylaşır.

## İlgili

[**Amazon Bedrock** Anthropic Claude, Titan ve diğer modeller için yerel Bedrock sağlayıcısı. ](</tr/providers/bedrock>) [**Model seçimi** Sağlayıcıları, model referanslarını ve yük devretme davranışını seçme. ](</tr/concepts/model-providers>) [**OAuth ve kimlik doğrulama** Kimlik doğrulama ayrıntıları ve kimlik bilgisi yeniden kullanım kuralları. ](</tr/gateway/authentication>) [**Sorun giderme** Yaygın sorunlar ve bunları çözme yolları. ](</tr/help/troubleshooting>)

Was this useful?YesNo