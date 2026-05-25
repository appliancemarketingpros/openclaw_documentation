---
title: Kilo Gateway
source_url: https://docs.openclaw.ai/tr/providers/kilocode
scraped_at: 2026-05-25
---

Kilo Gateway, istekleri tek bir endpoint ve API anahtarı arkasındaki birçok modele yönlendiren **birleşik API** sağlar. OpenAI uyumludur; bu nedenle çoğu OpenAI SDK'sı, temel URL değiştirilerek çalışır.

Özellik | Değer  
---|---  
Sağlayıcı | `kilocode`  
Kimlik doğrulama | `KILOCODE_API_KEY`  
API | OpenAI uyumlu  
Temel URL | `https://api.kilo.ai/api/gateway/`  
  
## Başlangıç

* ### Hesap oluşturun

[app.kilo.ai](<https://app.kilo.ai>) adresine gidin, oturum açın veya bir hesap oluşturun, ardından API Keys bölümüne gidip yeni bir anahtar oluşturun.

* ### Onboarding'i çalıştırın

bashCopy code
[code]
    openclaw onboard --auth-choice kilocode-api-key
[/code]

Veya ortam değişkenini doğrudan ayarlayın:

bashCopy code
[code]
    export KILOCODE_API_KEY="<your-kilocode-api-key>" # pragma: allowlist secret
[/code]

* ### Modelin kullanılabilir olduğunu doğrulayın

bashCopy code
[code]
    openclaw models list --provider kilocode
[/code]

## Varsayılan model

Varsayılan model, Kilo Gateway tarafından yönetilen ve sağlayıcıya ait bir akıllı yönlendirme modeli olan `kilocode/kilo/auto` modelidir.

## Yerleşik katalog

OpenClaw, başlangıçta Kilo Gateway üzerinden kullanılabilir modelleri dinamik olarak keşfeder. Hesabınızla kullanılabilen modellerin tam listesini görmek için `/models kilocode` kullanın.

Gateway üzerinde kullanılabilen herhangi bir model, `kilocode/` önekiyle kullanılabilir:

Model referansı | Notlar  
---|---  
`kilocode/kilo/auto` | Varsayılan — akıllı yönlendirme  
`kilocode/anthropic/claude-sonnet-4` | Kilo üzerinden Anthropic  
`kilocode/openai/gpt-5.5` | Kilo üzerinden OpenAI  
`kilocode/google/gemini-3.1-pro-preview` | Kilo üzerinden Google  
...ve çok daha fazlası | Tümünü listelemek için `/models kilocode` kullanın  
  
## Yapılandırma örneği

json5Copy code
[code]
    {  env: { KILOCODE_API_KEY: "<your-kilocode-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "kilocode/kilo/auto" },    },  },}
[/code]

Aktarım ve uyumluluk

Kilo Gateway kaynakta OpenRouter uyumlu olarak belgelenmiştir; bu nedenle yerel OpenAI istek biçimlendirmesi yerine proxy tarzı OpenAI uyumlu yolda kalır.

  * Gemini destekli Kilo referansları proxy-Gemini yolunda kalır; bu nedenle OpenClaw, yerel Gemini yeniden oynatma doğrulamasını veya bootstrap yeniden yazımlarını etkinleştirmeden Gemini düşünce imzası temizliğini orada korur.
  * Kilo Gateway, arka planda API anahtarınızla birlikte Bearer token kullanır.

Akış sarmalayıcı ve akıl yürütme

Kilo'nun paylaşılan akış sarmalayıcısı, sağlayıcı uygulama başlığını ekler ve desteklenen somut model referansları için proxy akıl yürütme yüklerini normalleştirir.

Sorun giderme

  * Başlangıçta model keşfi başarısız olursa OpenClaw, `kilocode/kilo/auto` içeren paketli statik kataloğa geri döner.
  * API anahtarınızın geçerli olduğunu ve Kilo hesabınızda istediğiniz modellerin etkinleştirildiğini doğrulayın.
  * Gateway bir daemon olarak çalıştığında, `KILOCODE_API_KEY` değerinin bu işlem tarafından kullanılabilir olduğundan emin olun (örneğin `~/.openclaw/.env` içinde veya `env.shellEnv` aracılığıyla).


## İlgili

[**Model seçimi** Sağlayıcıları, model referanslarını ve yük devretme davranışını seçme. ](</tr/concepts/model-providers>) [**Yapılandırma başvurusu** Tam OpenClaw yapılandırma başvurusu. ](</tr/gateway/configuration-reference>) [**Kilo Gateway** Kilo Gateway panosu, API anahtarları ve hesap yönetimi. ](<https://app.kilo.ai>)

Was this useful?YesNo