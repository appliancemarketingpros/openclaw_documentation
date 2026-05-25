---
title: OpenRouter
source_url: https://docs.openclaw.ai/tr/providers/openrouter
scraped_at: 2026-05-25
---

OpenRouter, istekleri tek bir uç nokta ve API anahtarı arkasındaki birçok modele yönlendiren **birleşik bir API** sağlar. OpenAI uyumludur, bu nedenle çoğu OpenAI SDK'sı temel URL değiştirilerek çalışır.

## Başlarken

* ### Get your API key

[openrouter.ai/keys](<https://openrouter.ai/keys>) adresinde bir API anahtarı oluşturun.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice openrouter-api-key
[/code]

* ### (Optional) Switch to a specific model

İlk katılım varsayılan olarak `openrouter/auto` kullanır. Daha sonra somut bir model seçin:

bashCopy code
[code]
    openclaw models set openrouter/<provider>/<model>
[/code]

## Yapılandırma örneği

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      model: { primary: "openrouter/auto" },    },  },}
[/code]

## Model referansları

Birlikte gelen yedek örnekler:

Model referansı | Notlar  
---|---  
`openrouter/auto` | OpenRouter otomatik yönlendirme  
`openrouter/moonshotai/kimi-k2.6` | MoonshotAI üzerinden Kimi K2.6  
`openrouter/moonshotai/kimi-k2.5` | MoonshotAI üzerinden Kimi K2.5  
  
## Görüntü üretimi

OpenRouter, `image_generate` aracını da destekleyebilir. `agents.defaults.imageGenerationModel` altında bir OpenRouter görüntü modeli kullanın:

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      imageGenerationModel: {        primary: "openrouter/google/gemini-3.1-flash-image-preview",        timeoutMs: 180_000,      },    },  },}
[/code]

OpenClaw, görüntü isteklerini `modalities: ["image", "text"]` ile OpenRouter'ın sohbet tamamlama görüntü API'sine gönderir. Gemini görüntü modelleri, desteklenen `aspectRatio` ve `resolution` ipuçlarını OpenRouter'ın `image_config` alanı üzerinden alır. Daha yavaş OpenRouter görüntü modelleri için `agents.defaults.imageGenerationModel.timeoutMs` kullanın; `image_generate` aracının çağrı başına `timeoutMs` parametresi yine önceliklidir.

## Video üretimi

OpenRouter, eşzamansız `/videos` API'si üzerinden `video_generate` aracını da destekleyebilir. `agents.defaults.videoGenerationModel` altında bir OpenRouter video modeli kullanın:

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      videoGenerationModel: {        primary: "openrouter/google/veo-3.1-fast",      },    },  },}
[/code]

OpenClaw, metinden videoya ve görüntüden videoya işleri OpenRouter'a gönderir, döndürülen `polling_url` değerini yoklar ve tamamlanan videoyu OpenRouter'ın `unsigned_urls` değerlerinden veya belgelenen iş içeriği uç noktasından indirir. Referans görüntüler varsayılan olarak ilk/son kare görüntüleri olarak gönderilir; `reference_image` ile etiketlenen görüntüler OpenRouter giriş referansları olarak gönderilir. Birlikte gelen `google/veo-3.1-fast` varsayılanı, şu anda desteklenen 4/6/8 saniyelik süreleri, `720P`/`1080P` çözünürlükleri ve `16:9`/`9:16` en boy oranlarını bildirir. Yukarı akış video üretim API'si şu anda metin ve görüntü referanslarını kabul ettiğinden, videodan videoya OpenRouter için kayıtlı değildir.

## Metinden sese

OpenRouter, OpenAI uyumlu `/audio/speech` uç noktası üzerinden TTS sağlayıcısı olarak da kullanılabilir.

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "openrouter",      providers: {        openrouter: {          model: "hexgrad/kokoro-82m",          voice: "af_alloy",          responseFormat: "mp3",        },      },    },  },}
[/code]

`messages.tts.providers.openrouter.apiKey` atlanırsa TTS, önce `models.providers.openrouter.apiKey` değerini, ardından `OPENROUTER_API_KEY` değerini yeniden kullanır.

## Konuşmadan metne (gelen ses)

OpenRouter, gelen ses/işitsel ekleri, STT uç noktasını (`/audio/transcriptions`) kullanarak paylaşılan `tools.media.audio` yolu üzerinden yazıya dökebilir. Bu, gelen ses/işitsel içeriği medya anlama ön denetimine ileten tüm kanal Plugin'leri için geçerlidir.

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "openrouter", model: "openai/whisper-large-v3-turbo" }],      },    },  },}
[/code]

OpenClaw, OpenRouter STT isteklerini çok parçalı OpenAI form yüklemeleri olarak değil, `input_audio` altında base64 ses içeren JSON olarak gönderir (OpenRouter STT sözleşmesi).

## Kimlik doğrulama ve başlıklar

OpenRouter, arka planda API anahtarınızla bir Bearer belirteci kullanır.

Gerçek OpenRouter isteklerinde (`https://openrouter.ai/api/v1`), OpenClaw ayrıca OpenRouter'ın belgelenen uygulama atıf başlıklarını ekler:

Başlık | Değer  
---|---  
`HTTP-Referer` | `https://openclaw.ai`  
`X-OpenRouter-Title` | `OpenClaw`  
`X-OpenRouter-Categories` | `cli-agent,cloud-agent,programming-app,creative-writing,writing-assistant,general-chat,personal-agent`  
  
## Gelişmiş yapılandırma

Response caching

OpenRouter yanıt önbelleğe alma isteğe bağlıdır. Bunu model parametreleriyle OpenRouter modeli başına etkinleştirin:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openrouter/auto": {          params: {            responseCache: true,            responseCacheTtlSeconds: 300,          },        },      },    },  },}
[/code]

OpenClaw, `X-OpenRouter-Cache: true` ve yapılandırıldığında `X-OpenRouter-Cache-TTL` gönderir. `responseCacheClear: true`, geçerli istek için yenilemeyi zorunlu kılar ve yerine geçen yanıtı depolar. Snake_case takma adları (`response_cache`, `response_cache_ttl_seconds` ve `response_cache_clear`) da kabul edilir.

Bu, sağlayıcı istem önbelleğe almadan ve OpenRouter'ın Anthropic `cache_control` işaretleyicilerinden ayrıdır. Özel proxy temel URL'lerine değil, yalnızca doğrulanmış `openrouter.ai` rotalarına uygulanır.

Anthropic cache markers

Doğrulanmış OpenRouter rotalarında, Anthropic model referansları OpenClaw'ın sistem/geliştirici istem bloklarında daha iyi istem önbelleği yeniden kullanımı için kullandığı OpenRouter'a özgü Anthropic `cache_control` işaretleyicilerini korur.

Anthropic reasoning prefill

Doğrulanmış OpenRouter rotalarında, akıl yürütme etkinleştirilmiş Anthropic model referansları, istek OpenRouter'a ulaşmadan önce sondaki asistan ön doldurma turlarını kaldırır; bu, Anthropic'in akıl yürütme konuşmalarının bir kullanıcı turuyla bitmesi gereksinimiyle eşleşir.

Thinking / reasoning injection

Desteklenen `auto` dışı rotalarda OpenClaw, seçili düşünme düzeyini OpenRouter proxy akıl yürütme yüklerine eşler. Desteklenmeyen model ipuçları ve `openrouter/auto` bu akıl yürütme enjeksiyonunu atlar. Hunter Alpha ayrıca bayat yapılandırılmış model referansları için proxy akıl yürütmeyi atlar, çünkü OpenRouter bu emekliye ayrılmış rota için akıl yürütme alanlarında nihai yanıt metni döndürebilir.

DeepSeek V4 reasoning replay

Doğrulanmış OpenRouter rotalarında, `openrouter/deepseek/deepseek-v4-flash` ve `openrouter/deepseek/deepseek-v4-pro`, düşünme/araç konuşmalarının DeepSeek V4'ün gerekli takip biçimini koruması için yeniden oynatılan asistan turlarında eksik `reasoning_content` değerini doldurur. OpenClaw bu rotalar için OpenRouter destekli `reasoning_effort` değerlerini gönderir; `xhigh` bildirilen en yüksek düzeydir ve bayat `max` geçersiz kılmaları `xhigh` değerine eşlenir.

OpenAI-only request shaping

OpenRouter hâlâ proxy tarzı OpenAI uyumlu yoldan çalışır, bu nedenle `serviceTier`, Responses `store`, OpenAI akıl yürütme uyumluluğu yükleri ve istem önbelleği ipuçları gibi yerel yalnızca OpenAI istek biçimlendirmeleri iletilmez.

Gemini-backed routes

Gemini destekli OpenRouter referansları proxy-Gemini yolunda kalır: OpenClaw burada Gemini düşünce imzası temizlemesini korur, ancak yerel Gemini yeniden oynatma doğrulamasını veya önyükleme yeniden yazımlarını etkinleştirmez.

Provider routing metadata

Model parametreleri altında OpenRouter sağlayıcı yönlendirmesi geçirirseniz OpenClaw, paylaşılan akış sarmalayıcıları çalışmadan önce bunu OpenRouter yönlendirme meta verileri olarak iletir.

## İlgili

[**Model selection** Sağlayıcıları, model referanslarını ve yük devretme davranışını seçme. ](</tr/concepts/model-providers>) [**Configuration reference** Ajanlar, modeller ve sağlayıcılar için tam yapılandırma referansı. ](</tr/gateway/configuration-reference>)

Was this useful?YesNo