---
title: Qwen OAuth / Portalı
source_url: https://docs.openclaw.ai/tr/providers/qwen-oauth
scraped_at: 2026-06-29
---

ModelsProviders

`qwen-oauth`, Qwen Portal sağlayıcı kimliğidir. Qwen Portal uç noktasını hedefler ve eski Qwen OAuth / portal kurulumlarının ayrı bir sağlayıcı kimliğiyle adreslenebilir kalmasını sağlar.

Bu sağlayıcıyı özellikle `https://portal.qwen.ai/v1` için güncel bir Qwen Portal token’ınız varsa veya eski bir Qwen Portal / Qwen CLI kurulumunu taşıyor ve bu kimlik bilgilerini kanonik Qwen Cloud sağlayıcısından ayrı tutmak istiyorsanız kullanın. Yeni Qwen kullanıcıları için önerilen ilk seçenek değildir.

Yeni Qwen Cloud kurulumları için, özellikle güncel bir Qwen Portal token’ınız yoksa Standard ModelStudio uç noktasıyla [Qwen](</tr/providers/qwen>) sağlayıcısını tercih edin.

## Kurulum

Portal token’ınızı onboarding üzerinden sağlayın:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-oauth
[/code]

Veya şunu ayarlayın:

bashCopy code
[code]
    export QWEN_API_KEY="<your-qwen-portal-token>" # pragma: allowlist secret
[/code]

## Varsayılanlar

  * Sağlayıcı: `qwen-oauth`
  * Takma adlar: `qwen-portal`, `qwen-cli`
  * Temel URL: `https://portal.qwen.ai/v1`
  * Ortam değişkeni: `QWEN_API_KEY`
  * API stili: OpenAI uyumlu
  * Varsayılan model: `qwen-oauth/qwen3.5-plus`


## Bunun Qwen’den farkı

OpenClaw’da Qwen’e yönelik iki sağlayıcı kimliği vardır:

Sağlayıcı | Uç nokta ailesi | En uygun kullanım  
---|---|---  
`qwen` | Qwen Cloud / Alibaba DashScope ve Coding Plan uç noktaları | Yeni API anahtarı kurulumları, Standard kullandıkça öde, Coding Plan, çok modlu DashScope özellikleri  
`qwen-oauth` | `portal.qwen.ai/v1` adresindeki Qwen Portal uç noktası | Mevcut Qwen Portal token’ları ve eski Qwen OAuth / CLI kurulumları  
  
Her iki sağlayıcı da OpenAI uyumlu istek şekilleri kullanır, ancak ayrı kimlik doğrulama yüzeyleridir. `qwen-oauth` için saklanan bir token DashScope veya ModelStudio anahtarı olarak değerlendirilmemeli; yeni bir DashScope anahtarı ise bunun yerine kanonik `qwen` sağlayıcısını kullanmalıdır.

## Qwen OAuth / Portal ne zaman seçilmeli

  * Zaten çalışan bir Qwen Portal token’ınız var.
  * OpenClaw’ın sağlayıcı modeline geçerken eski bir Qwen OAuth veya Qwen CLI iş akışını koruyorsunuz.
  * Özellikle Qwen Portal uç noktasıyla uyumluluğu test etmeniz gerekiyor.


Yeni kurulum, daha geniş uç nokta seçenekleri, Standard ModelStudio, Coding Plan ve tam Qwen Plugin kataloğu için [Qwen](</tr/providers/qwen>) seçeneğini kullanın.

## Modeller

Qwen Plugin kataloğu, Qwen Portal varsayılanını başlatır:

  * `qwen-oauth/qwen3.5-plus`


Kullanılabilirlik, güncel Qwen Portal hesabına ve token’a bağlıdır. Hesabınız bunun yerine ModelStudio / DashScope API anahtarları kullanıyorsa kanonik `qwen` sağlayıcısını yapılandırın:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-keyopenclaw models set qwen/qwen3-coder-plus
[/code]

## Geçiş

Eski Qwen Portal OAuth profilleri yenilenebilir olmayabilir. Bir portal profili çalışmayı durdurursa güncel bir token ile yeniden kimlik doğrulayın veya Standard Qwen sağlayıcısına geçin:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key
[/code]

Standard global ModelStudio şunu kullanır:

textCopy code
[code]
    https://dashscope-intl.aliyuncs.com/compatible-mode/v1
[/code]

## Sorun giderme

  * Portal OAuth yenileme hataları: eski Qwen Portal OAuth profilleri yenilenebilir olmayabilir. Güncel bir token ile onboarding’i yeniden çalıştırın.
  * Yanlış uç nokta hataları: portal token’ı kullanırken model referansının `qwen-oauth/` ile başladığını doğrulayın. `qwen/` referanslarını yalnızca kanonik Qwen sağlayıcısı için kullanın.
  * `QWEN_API_KEY` karışıklığı: Her iki Qwen sayfası da bu ortam değişkeninden bahseder, ancak onboarding kimlik bilgilerini seçilen sağlayıcı kimliği altında saklar. Aynı makinede hem `qwen` hem de `qwen-oauth` kullanılabilir durumdaysa onboarding’i tercih edin.


## İlgili

  * [Qwen](</tr/providers/qwen>)
  * [Alibaba Model Studio](</tr/providers/alibaba>)
  * [Model sağlayıcıları](</tr/concepts/model-providers>)
  * [Tüm sağlayıcılar](</tr/providers>)


Was this useful?YesNo

Open issue