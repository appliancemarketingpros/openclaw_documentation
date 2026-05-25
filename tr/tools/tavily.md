---
title: Tavily
source_url: https://docs.openclaw.ai/tr/tools/tavily
scraped_at: 2026-05-25
---

[Tavily](<https://tavily.com>), AI uygulamaları için tasarlanmış bir arama API'sidir. OpenClaw bunu iki şekilde sunar:

  * genel arama aracı için `web_search` sağlayıcısı olarak
  * açık Plugin araçları olarak: `tavily_search` ve `tavily_extract`


Tavily, yapılandırılabilir arama derinliği, konu filtreleme, alan adı filtreleri, AI tarafından oluşturulan yanıt özetleri ve URL'lerden içerik çıkarma (JavaScript ile oluşturulan sayfalar dahil) ile LLM tüketimi için optimize edilmiş yapılandırılmış sonuçlar döndürür.

Özellik | Değer  
---|---  
Plugin kimliği | `tavily`  
Kimlik doğrulama | `TAVILY_API_KEY` veya config `apiKey`  
Temel URL | `https://api.tavily.com` (varsayılan)  
Paketli araçlar | `tavily_search`, `tavily_extract`  
  
## Başlarken

* ### Bir API anahtarı alın

[tavily.com](<https://tavily.com>) adresinde bir Tavily hesabı oluşturun, ardından panoda bir API anahtarı oluşturun.

* ### Plugin ve sağlayıcıyı yapılandırın

json5Copy code
[code]
    {  plugins: {    entries: {      tavily: {        enabled: true,        config: {          webSearch: {            apiKey: "tvly-...", // optional if TAVILY_API_KEY is set            baseUrl: "https://api.tavily.com",          },        },      },    },  },  tools: {    web: {      search: {        provider: "tavily",      },    },  },}
[/code]

* ### Aramanın çalıştığını doğrulayın

Herhangi bir agent'tan bir `web_search` tetikleyin veya doğrudan `tavily_search` çağırın.

## Araç referansı

### `tavily_search`

Genel `web_search` yerine Tavily'ye özgü arama kontrolleri istediğinizde bunu kullanın.

Parametre | Tür | Kısıtlamalar / varsayılan | Açıklama  
---|---|---|---  
`query` | string | gerekli | Arama sorgusu dizesi. 400 karakterin altında tutun.  
`search_depth` | enum | `basic` (varsayılan), `advanced` | `advanced` daha yavaştır ancak daha yüksek alaka düzeyi sağlar.  
`topic` | enum | `general` (varsayılan), `news`, `finance` | Konu ailesine göre filtreleyin.  
`max_results` | integer | 1-20 | Sonuç sayısı.  
`include_answer` | boolean | varsayılan `false` | Tavily AI tarafından oluşturulan bir yanıt özeti ekleyin.  
`time_range` | enum | `day`, `week`, `month`, `year` | Sonuçları güncelliğe göre filtreleyin.  
`include_domains` | string dizisi | (yok) | Yalnızca bu alan adlarından gelen sonuçları dahil edin.  
`exclude_domains` | string dizisi | (yok) | Bu alan adlarından gelen sonuçları hariç tutun.  
  
Arama derinliği ödünleşimi:

Derinlik | Hız | Alaka düzeyi | En uygun kullanım  
---|---|---|---  
`basic` | Daha hızlı | Yüksek | Genel amaçlı sorgular (varsayılan).  
`advanced` | Daha yavaş | En yüksek | Hassas araştırma ve doğruluk kontrolü.  
  
### `tavily_extract`

Bir veya daha fazla URL'den temiz içerik çıkarmak için bunu kullanın. JavaScript ile oluşturulan sayfaları işler ve hedefli çıkarım için sorgu odaklı parçalamayı destekler.

Parametre | Tür | Kısıtlamalar / varsayılan | Açıklama  
---|---|---|---  
`urls` | string dizisi | gerekli, 1-20 | İçerik çıkarılacak URL'ler.  
`query` | string | (isteğe bağlı) | Çıkarılan parçaları bu sorguya göre alaka düzeyiyle yeniden sıralayın.  
`extract_depth` | enum | `basic` (varsayılan), `advanced` | JS ağırlıklı sayfalar, SPA'lar veya dinamik tablolar için `advanced` kullanın.  
`chunks_per_source` | integer | 1-5; **`query` gerektirir** | URL başına döndürülen parçalar. `query` olmadan ayarlanırsa hata verir.  
`include_images` | boolean | varsayılan `false` | Sonuçlara görsel URL'lerini dahil edin.  
  
Çıkarma derinliği ödünleşimi:

Derinlik | Ne zaman kullanılmalı  
---|---  
`basic` | Basit sayfalar. Önce bunu deneyin.  
`advanced` | JS ile oluşturulan SPA'lar, dinamik içerik, tablolar.  
  
## Doğru aracı seçme

İhtiyaç | Araç  
---|---  
Hızlı web araması, özel seçenek yok | `web_search`  
Derinlik, konu ve AI yanıtlarıyla arama | `tavily_search`  
Belirli URL'lerden içerik çıkarma | `tavily_extract`  
  
## Gelişmiş yapılandırma

API anahtarı çözümleme sırası

Tavily istemcisi API anahtarını şu sırayla arar:

  1. `plugins.entries.tavily.config.webSearch.apiKey` (SecretRefs üzerinden çözümlenir).
  2. Gateway ortamından `TAVILY_API_KEY`.


Hiçbiri yoksa `tavily_extract` bir kurulum hatası verir.

Özel temel URL

Tavily'yi bir proxy üzerinden sunuyorsanız `plugins.entries.tavily.config.webSearch.baseUrl` değerini geçersiz kılın. Varsayılan `https://api.tavily.com` değeridir.

`chunks_per_source`, `query` gerektirir

`tavily_extract`, `query` olmadan `chunks_per_source` iletilen çağrıları reddeder. Tavily parçaları sorgu alaka düzeyine göre sıralar, bu nedenle bu parametre sorgu olmadan anlamsızdır.

## İlgili

[**Web Araması genel bakışı** Tüm sağlayıcılar ve otomatik algılama kuralları. ](</tr/tools/web>) [**Firecrawl** İçerik çıkarma ile arama ve scraping. ](</tr/tools/firecrawl>) [**Exa Search** İçerik çıkarma ile nöral arama. ](</tr/tools/exa-search>) [**Yapılandırma** Plugin girdileri ve araç yönlendirme için tam config şeması. ](</tr/gateway/configuration>)

Was this useful?YesNo