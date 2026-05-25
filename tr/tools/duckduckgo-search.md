---
title: DuckDuckGo araması
source_url: https://docs.openclaw.ai/tr/tools/duckduckgo-search
scraped_at: 2026-05-25
---

OpenClaw, DuckDuckGo'yu **anahtarsız** bir `web_search` sağlayıcısı olarak destekler. API anahtarı veya hesap gerekmez.

## Kurulum

API anahtarı gerekmez; sağlayıcınız olarak DuckDuckGo'yu ayarlamanız yeterlidir:

* ### Yapılandır

bashCopy code
[code]
    openclaw configure --section web# Sağlayıcı olarak "duckduckgo" seçin
[/code]

## Yapılandırma

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "duckduckgo",      },    },  },}
[/code]

Bölge ve SafeSearch için isteğe bağlı Plugin düzeyi ayarlar:

json5Copy code
[code]
    {  plugins: {    entries: {      duckduckgo: {        config: {          webSearch: {            region: "us-en", // DuckDuckGo bölge kodu            safeSearch: "moderate", // "strict", "moderate" veya "off"          },        },      },    },  },}
[/code]

## Araç parametreleri

Arama sorgusu.

Döndürülecek sonuçlar (1-10).

DuckDuckGo bölge kodu (örn. `us-en`, `uk-en`, `de-de`).

SafeSearch düzeyi.

Bölge ve SafeSearch, Plugin yapılandırmasında da ayarlanabilir (yukarıya bakın); araç parametreleri, sorgu bazında yapılandırma değerlerini geçersiz kılar.

## Notlar

  * **API anahtarı yok** ; kutudan çıktığı gibi çalışır, sıfır yapılandırma
  * **Deneysel** ; sonuçları resmi bir API veya SDK'den değil, DuckDuckGo'nun JavaScript dışı HTML arama sayfalarından toplar
  * **Bot doğrulama riski** ; DuckDuckGo yoğun veya otomatik kullanımda CAPTCHA sunabilir ya da istekleri engelleyebilir
  * **HTML ayrıştırma** ; sonuçlar sayfa yapısına bağlıdır ve bu yapı bildirimde bulunulmadan değişebilir
  * **Otomatik algılama sırası** ; DuckDuckGo, otomatik algılamadaki ilk anahtarsız geri dönüş seçeneğidir (sıra 100). Yapılandırılmış anahtarları olan API destekli sağlayıcılar önce çalışır, ardından Ollama Web Search (sıra 110), sonra SearXNG (sıra 200) gelir
  * **SafeSearch, yapılandırılmadığında varsayılan olarak moderate değerini kullanır**


## İlgili

  * [Web Search genel bakışı](</tr/tools/web>) \-- tüm sağlayıcılar ve otomatik algılama
  * [Brave Search](</tr/tools/brave-search>) \-- ücretsiz katmanla yapılandırılmış sonuçlar
  * [Exa Search](</tr/tools/exa-search>) \-- içerik çıkarma özellikli nöral arama


Was this useful?YesNo