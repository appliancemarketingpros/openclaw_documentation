---
title: Featherless AI
source_url: https://docs.openclaw.ai/tr/providers/featherless
scraped_at: 2026-07-13
---

ModelsProviders

[Featherless AI](<https://featherless.ai>), açık modelleri OpenAI uyumlu bir API üzerinden sunar. OpenClaw, Featherless'ı resmî bir harici sağlayıcı Plugin'i olarak kurar ve yerleşik kataloğu küçük tutarken çalışma zamanında Featherless'tan gelen tam model kimliklerini kabul eder.

Özellik | Değer  
---|---  
Sağlayıcı kimliği | `featherless`  
Paket | `@openclaw/featherless-provider`  
Kimlik doğrulama ortam değişkeni | `FEATHERLESS_API_KEY`  
İlk kurulum bayrağı | `--auth-choice featherless-api-key`  
Doğrudan CLI bayrağı | `--featherless-api-key <key>`  
API | OpenAI uyumlu (`openai-completions`)  
Temel URL | `https://api.featherless.ai/v1`  
Varsayılan model | `featherless/Qwen/Qwen3-32B`  
  
## Kurulum

Plugin'i kurun ve Gateway'i yeniden başlatın:

bashCopy code
[code]
    openclaw plugins install @openclaw/featherless-provideropenclaw gateway restart
[/code]

İlk kurulumu çalıştırın:

bashCopy code
[code]
    openclaw onboard --auth-choice featherless-api-key
[/code]

Etkileşimsiz kurulum için:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice featherless-api-key \  --featherless-api-key "$FEATHERLESS_API_KEY"
[/code]

Alternatif olarak anahtarı Gateway işlemine sunun:

bashCopy code
[code]
    export FEATHERLESS_API_KEY="<your-featherless-api-key>" # pragma: allowlist secret
[/code]

Sağlayıcıyı doğrulayın:

bashCopy code
[code]
    openclaw models list --provider featherless
[/code]

## Varsayılan model

Plugin, Featherless Qwen 3 ailesi için yerel araç çağrısını belgelediğinden, kurulum varsayılanı olarak `Qwen/Qwen3-32B` kullanır. OpenClaw; modelin 32.768 tokenlık bağlam penceresini, ihtiyatlı bir 4.096 tokenlık çıktı sınırını ve Qwen sohbet şablonuna ait düşünme denetimlerini yapılandırır.

Featherless birden fazla faturalandırma modunu desteklediği ve OpenClaw hesaba özgü plan ya da istek fiyatlandırma oranlarını gömmediği için katalogdaki maliyet alanları sıfırdır.

## Diğer Featherless modelleri

`featherless/` sağlayıcı ön ekinden sonra tam Featherless model kimliğini kullanın:

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "featherless/moonshotai/Kimi-K2-Instruct",      },    },  },}
[/code]

OpenClaw, Featherless'ın herkese açık model dizininin tamamını bilinçli olarak seçiciye kopyalamaz. Dizin büyüktür ve her metin, görüntü, gömme ve akıl yürütme modelini güvenli biçimde sınıflandırmak için yeterli yapılandırılmış yetenek meta verisi sunmaz. Bu nedenle bilinmeyen kimlikler, ihtiyatlı ve yalnızca metin destekleyen, akıl yürütmeyen varsayılanlarla çözümlenir: 4.096 tokenlık bağlam penceresi ve 1.024 tokenlık çıktı sınırı.

Bir model farklı meta veriler gerektirdiğinde açık bir sağlayıcı model girdisi ekleyin:

json5Copy code
[code]
    {  models: {    mode: "merge",    providers: {      featherless: {        baseUrl: "https://api.featherless.ai/v1",        apiKey: "${FEATHERLESS_API_KEY}",        api: "openai-completions",        models: [          {            id: "google/gemma-3-27b-it",            name: "Gemma 3 27B",            input: ["text", "image"],            reasoning: false,            contextWindow: 32768,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

Özel meta veriler eklemeden önce güncel model kullanılabilirliği ve yetenek etiketleri için Featherless'ın model kataloğunu kontrol edin.

## Sorun giderme

  * `401` veya `403`: `FEATHERLESS_API_KEY` değişkeninin Gateway işlemi tarafından görülebildiğini doğrulayın ya da ilk kurulumu yeniden çalıştırın.
  * Bilinmeyen model: `featherless/` ön ekinden sonra Featherless'taki büyük-küçük harfe duyarlı tam kimliği kullanın.
  * Araç çağrıları metin olarak döndürüldiyse: Qwen 3 gibi Featherless'ın yerel işlev çağrısı için belgelediği bir model ailesi seçin.
  * Yönetilen Gateway anahtarı göremiyorsa: anahtarı `~/.openclaw/.env` dosyasına veya hizmet tarafından yüklenen başka bir ortam kaynağına ekleyin, ardından Gateway'i yeniden başlatın.


## İlgili

  * [Model sağlayıcıları](</tr/concepts/model-providers>)
  * [Tüm sağlayıcılar](</tr/providers>)
  * [Düşünme modları](</tr/tools/thinking>)


Was this useful?YesNo

Open issue