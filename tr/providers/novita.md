---
title: NovitaAI
source_url: https://docs.openclaw.ai/tr/providers/novita
scraped_at: 2026-06-29
---

ModelsProviders

NovitaAI, OpenAI uyumlu bir model API’sine sahip barındırılan bir yapay zeka altyapı sağlayıcısıdır. OpenClaw’da paketle birlikte gelen bir model sağlayıcısıdır; bu nedenle sağlayıcı kimliği `novita` olur, kimlik bilgileri normal model kimlik doğrulama akışından geçer ve model başvuruları `novita/deepseek/deepseek-v3-0324` gibi görünür.

Kendi çıkarım sunucunuzu çalıştırmadan açık ağırlıklı ve üçüncü taraf model rotalarına barındırılan erişim istediğinizde Novita kullanın. Paketle birlikte gelen katalog, Novita tarafından sunulan DeepSeek, Moonshot, MiniMax, GLM ve Qwen rotaları dahil olmak üzere aracı turları için pratik olan sohbet modellerine odaklanır.

Bu sağlayıcı Novita’nın OpenAI uyumlu uç noktasını kullanır. OpenClaw sağlayıcı kaydını, kimlik doğrulamayı, takma adları, model başvurusu normalleştirmeyi ve temel URL seçimini yönetir; Novita ise canlı model kullanılabilirliğini, hesap izinlerini, fiyatlandırmayı ve hız sınırlarını kontrol eder.

## Kurulum

[novita.ai/settings/key-management](<https://novita.ai/settings/key-management>) adresinde bir API anahtarı oluşturun, ardından şunu çalıştırın:

bashCopy code
[code]
    openclaw onboard --auth-choice novita-api-key
[/code]

Veya şunu ayarlayın:

bashCopy code
[code]
    export NOVITA_API_KEY="<your-novita-api-key>" # pragma: allowlist secret
[/code]

## Varsayılanlar

  * Sağlayıcı: `novita`
  * Takma adlar: `novita-ai`, `novitaai`
  * Temel URL: `https://api.novita.ai/openai/v1`
  * Ortam değişkeni: `NOVITA_API_KEY`
  * Varsayılan model: `novita/deepseek/deepseek-v3-0324`


## Novita ne zaman seçilmeli

  * OpenAI uyumlu bir API ile barındırılan açık ağırlıklı model erişimi istiyorsunuz.
  * Tek bir sağlayıcı hesabı üzerinden DeepSeek, Kimi, MiniMax, GLM veya Qwen ailesi rotaları istiyorsunuz.
  * OpenRouter, GMI, DeepInfra veya doğrudan satıcı API’lerinin yanında başka bir barındırılan yedek yol istiyorsunuz.
  * vLLM, SGLang, LM Studio veya Ollama altyapısını sürdürmek yerine sağlayıcı tarafı model barındırmayı tercih ediyorsunuz.


Satıcıya özgü istek parametrelerine veya destek sözleşmelerine ihtiyacınız olduğunda doğrudan bir satıcı sağlayıcısı seçin. Modelin kendi donanımınızda veya kendi ağ sınırınızın arkasında çalışması gerektiğinde yerel bir sağlayıcı seçin.

## Modeller

Paketle birlikte gelen katalog, yaygın olarak kullanılabilen NovitaAI rota kimliklerini başlangıç olarak ekler; bunlar arasında şunlar bulunur:

  * `novita/moonshotai/kimi-k2.5`
  * `novita/minimax/minimax-m2.7`
  * `novita/zai-org/glm-5`
  * `novita/deepseek/deepseek-v3-0324`
  * `novita/deepseek/deepseek-r1-0528`
  * `novita/qwen/qwen3-235b-a22b-fp8`


Katalog, OpenClaw model seçimi için bir başlangıç noktasıdır. Hesabınız, bölgeniz veya Novita’nın mevcut kataloğu rotalar ekleyebilir, kaldırabilir veya kısıtlayebilir. Uzun süreli bir varsayılan ayarlamadan önce sağlayıcıyı CLI’dan kontrol edin:

bashCopy code
[code]
    openclaw models list --provider novita
[/code]

## Sorun Giderme

  * `401` veya `403`: Novita’nın anahtar yönetimi sayfasındaki anahtarı doğrulayın ve saklanan profil güncel değilse `openclaw onboard --auth-choice novita-api-key` komutunu yeniden çalıştırın.
  * Bilinmeyen model hataları: `openclaw models list --provider novita` tarafından döndürülen tam `novita/<route-id>` değerini kullanın.
  * Yavaş veya başarısız rotalar: başka bir Novita model rotasını deneyin veya sağlayıcıya özgü değişkenliği tolere edebilen iş yükleri için Novita’yı yedek sağlayıcı olarak ayarlayın.


## İlgili

  * [Model sağlayıcıları](</tr/concepts/model-providers>)
  * [Tüm sağlayıcılar](</tr/providers>)


Was this useful?YesNo

Open issue