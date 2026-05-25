---
title: Perplexity
source_url: https://docs.openclaw.ai/tr/providers/perplexity-provider
scraped_at: 2026-05-25
---

Perplexity Plugin'i, Perplexity Search API veya OpenRouter üzerinden Perplexity Sonar aracılığıyla web arama özellikleri sağlar.

Özellik | Değer  
---|---  
Tür | Web arama sağlayıcısı (model sağlayıcısı değil)  
Kimlik doğrulama | `PERPLEXITY_API_KEY` (doğrudan) veya `OPENROUTER_API_KEY` (OpenRouter üzerinden)  
Yapılandırma yolu | `plugins.entries.perplexity.config.webSearch.apiKey`  
  
## Başlarken

* ### API anahtarını ayarlayın

Etkileşimli web arama yapılandırma akışını çalıştırın:

bashCopy code
[code]
    openclaw configure --section web
[/code]

Veya anahtarı doğrudan ayarlayın:

bashCopy code
[code]
    openclaw config set plugins.entries.perplexity.config.webSearch.apiKey "pplx-xxxxxxxxxxxx"
[/code]

* ### Aramaya başlayın

Anahtar yapılandırıldıktan sonra ajan, web aramaları için Perplexity'yi otomatik olarak kullanır. Ek adım gerekmez.

## Arama modları

Plugin, API anahtarı önekine göre aktarımı otomatik seçer:

### Yerel Perplexity API (pplx-)

Anahtarınız `pplx-` ile başladığında OpenClaw, yerel Perplexity Search API'yi kullanır. Bu aktarım yapılandırılmış sonuçlar döndürür ve etki alanı, dil ve tarih filtrelerini destekler (aşağıdaki filtreleme seçeneklerine bakın).

### OpenRouter / Sonar (sk-or-)

Anahtarınız `sk-or-` ile başladığında OpenClaw, Perplexity Sonar modelini kullanarak OpenRouter üzerinden yönlendirir. Bu aktarım, alıntılarla birlikte yapay zeka tarafından sentezlenmiş yanıtlar döndürür.

Anahtar öneki | Aktarım | Özellikler  
---|---|---  
`pplx-` | Yerel Perplexity Search API | Yapılandırılmış sonuçlar, etki alanı/dil/tarih filtreleri  
`sk-or-` | OpenRouter (Sonar) | Alıntılarla birlikte yapay zeka tarafından sentezlenmiş yanıtlar  
  
## Yerel API filtreleme

Yerel Perplexity API kullanılırken aramalar aşağıdaki filtreleri destekler:

Filtre | Açıklama | Örnek  
---|---|---  
Ülke | 2 harfli ülke kodu | `us`, `de`, `jp`  
Dil | ISO 639-1 dil kodu | `en`, `fr`, `zh`  
Tarih aralığı | Güncellik penceresi | `day`, `week`, `month`, `year`  
Etki alanı filtreleri | İzin listesi veya ret listesi (en fazla 20 etki alanı) | `example.com`  
İçerik bütçesi | Yanıt başına / sayfa başına token sınırları | `max_tokens`, `max_tokens_per_page`  
  
## Gelişmiş yapılandırma

Daemon süreçleri için ortam değişkeni

OpenClaw Gateway bir daemon (launchd/systemd) olarak çalışıyorsa, `PERPLEXITY_API_KEY` değerinin bu süreç tarafından kullanılabilir olduğundan emin olun.

OpenRouter proxy kurulumu

Perplexity aramalarını OpenRouter üzerinden yönlendirmeyi tercih ediyorsanız, yerel bir Perplexity anahtarı yerine bir `OPENROUTER_API_KEY` (`sk-or-` öneki) ayarlayın. OpenClaw öneki algılar ve otomatik olarak Sonar aktarımına geçer.

## İlgili

[**Perplexity arama aracı** Ajanın Perplexity aramalarını nasıl çağırdığı ve sonuçları nasıl yorumladığı. ](</tr/tools/perplexity-search>) [**Yapılandırma referansı** Plugin girdileri dahil tam yapılandırma referansı. ](</tr/gateway/configuration-reference>)

Was this useful?YesNo