---
title: GMI Cloud
source_url: https://docs.openclaw.ai/tr/providers/gmi
scraped_at: 2026-06-29
---

ModelsProviders

GMI Cloud, OpenAI uyumlu bir API arkasında öncü ve açık ağırlıklı modeller için barındırılan bir çıkarım platformudur. OpenClaw'da resmi bir harici sağlayıcı Plugin'idir; bu, onu bir kez kuracağınız, `gmi` sağlayıcı kimliğiyle seçeceğiniz, kimlik bilgilerini normal model kimlik doğrulaması üzerinden saklayacağınız ve `gmi/google/gemini-3.1-flash-lite` gibi model referansları kullanacağınız anlamına gelir.

GMI'nin kataloğunda sunulan Google, Anthropic, OpenAI, DeepSeek, Moonshot ve Z.AI rotaları dahil olmak üzere birkaç barındırılan model ailesi için tek bir API anahtarı istediğinizde GMI kullanın. Model yedeklemesi için ikincil sağlayıcı olarak, satıcılar arasında barındırılan rotaları karşılaştırmak için veya GMI bir modeli birincil sağlayıcınızdan önce kullanıma sunduğunda yararlıdır.

Bu sağlayıcı OpenAI uyumlu sohbet semantiği kullanır. OpenClaw sağlayıcı kimliğini, kimlik doğrulama profilini, takma adları, model kataloğu başlangıcını ve temel URL'yi sahiplenir; GMI ise canlı model kullanılabilirliğini, faturalandırmayı, hız sınırlarını ve sağlayıcı tarafındaki tüm yönlendirme politikalarını sahiplenir.

## Kurulum

Plugin'i kurun, Gateway'i yeniden başlatın, ardından GMI Cloud'da bir API anahtarı oluşturun:

bashCopy code
[code]
    openclaw plugins install @openclaw/gmi-provideropenclaw gateway restart
[/code]

Ardından şunu çalıştırın:

bashCopy code
[code]
    openclaw onboard --auth-choice gmi-api-key
[/code]

Veya şunu ayarlayın:

bashCopy code
[code]
    export GMI_API_KEY="<your-gmi-api-key>" # pragma: allowlist secret
[/code]

## Varsayılanlar

  * Sağlayıcı: `gmi`
  * Takma adlar: `gmi-cloud`, `gmicloud`
  * Temel URL: `https://api.gmi-serving.com/v1`
  * Ortam değişkeni: `GMI_API_KEY`
  * Varsayılan model: `gmi/google/gemini-3.1-flash-lite`


## Ne zaman GMI seçilmeli

  * Yerel bir model sunucusu yerine barındırılan OpenAI uyumlu bir uç nokta istiyorsunuz.
  * Tek bir sağlayıcı hesabı üzerinden birkaç ticari ve açık ağırlıklı model ailesini denemek istiyorsunuz.
  * OpenRouter, DeepInfra, Together veya doğrudan satıcı API'lerinden farklı yukarı akış yönlendirmesine sahip bir yedek sağlayıcı istiyorsunuz.
  * GMI'ye özgü model kimliklerine, fiyatlandırmaya veya hesap denetimlerine ihtiyacınız var.


GMI'nin OpenAI uyumlu rotası üzerinden sunmadığı satıcıya özgü özelliklere ihtiyacınız olduğunda bunun yerine doğrudan satıcı sağlayıcısını seçin. Veri yerelliği veya yerel GPU denetimi, barındırma kolaylığından daha önemli olduğunda Ollama, LM Studio, vLLM veya SGLang gibi yerel bir sağlayıcı seçin.

## Modeller

Plugin kataloğu, yaygın olarak kullanılabilen GMI Cloud rota kimliklerini başlangıç olarak ekler; bunlara şunlar dahildir:

  * `gmi/zai-org/GLM-5.1-FP8`
  * `gmi/deepseek-ai/DeepSeek-V3.2`
  * `gmi/moonshotai/Kimi-K2.5`
  * `gmi/google/gemini-3.1-flash-lite`
  * `gmi/anthropic/claude-sonnet-4.6`
  * `gmi/openai/gpt-5.4`


Katalog bir başlangıçtır; her hesabın her modeli her zaman çağırabileceğinin garantisi değildir. Yapılandırılmış sağlayıcının ortamınızda ne bildirdiğini görmek için OpenClaw'ın model listeleme komutunu kullanın:

bashCopy code
[code]
    openclaw models list --provider gmi
[/code]

## Sorun giderme

  * `401` veya `403`: `GMI_API_KEY` değişkeninin OpenClaw'ı çalıştıran süreç için ayarlandığını kontrol edin ya da anahtarı sağlayıcı kimlik doğrulama profilinde saklamak için onboard işlemini yeniden çalıştırın.
  * Bilinmeyen model hataları: modelin GMI hesabınızda mevcut olduğunu doğrulayın ve `openclaw models list --provider gmi` tarafından gösterilen tam `gmi/<route-id>` referansını kullanın.
  * Aralıklı sağlayıcı hataları: farklı bir GMI rotası deneyin veya GMI'yi tek birincil model sağlayıcısı yerine yedek olarak yapılandırın.


## İlgili

  * [Model sağlayıcıları](</tr/concepts/model-providers>)
  * [Tüm sağlayıcılar](</tr/providers>)


Was this useful?YesNo

Open issue