---
title: Exa araması
source_url: https://docs.openclaw.ai/tr/tools/exa-search
scraped_at: 2026-05-25
---

OpenClaw, `web_search` sağlayıcısı olarak [Exa AI](<https://exa.ai/>) desteği sunar. Exa, yerleşik içerik çıkarımıyla (vurgular, metin, özetler) neural, anahtar kelime ve hibrit arama modları sunar.

## API anahtarı alma

* ### Hesap oluşturun

[exa.ai](<https://exa.ai/>) üzerinde kaydolun ve panonuzdan bir API anahtarı oluşturun.

* ### Anahtarı saklayın

Gateway ortamında `EXA_API_KEY` ayarlayın veya şu şekilde yapılandırın:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## Yapılandırma

json5Copy code
[code]
    {  plugins: {    entries: {      exa: {        config: {          webSearch: {            apiKey: "exa-...", // optional if EXA_API_KEY is set            baseUrl: "https://api.exa.ai", // optional; OpenClaw appends /search          },        },      },    },  },  tools: {    web: {      search: {        provider: "exa",      },    },  },}
[/code]

**Ortam alternatifi:** Gateway ortamında `EXA_API_KEY` ayarlayın. Bir gateway kurulumu için bunu `~/.openclaw/.env` içine koyun.

## Temel URL geçersiz kılma

Exa arama isteklerinin uyumlu bir proxy veya alternatif Exa uç noktası üzerinden geçmesi gerektiğinde `plugins.entries.exa.config.webSearch.baseUrl` ayarlayın. OpenClaw, yalın ana makinelerin başına `https://` ekleyerek normalleştirir ve yol zaten orada bitmiyorsa `/search` ekler. Çözümlenen uç nokta arama önbellek anahtarına dahil edilir; böylece farklı Exa uç noktalarından gelen sonuçlar paylaşılmaz.

## Araç parametreleri

Arama sorgusu.

Döndürülecek sonuçlar (1-100).

Arama modu.

Zaman filtresi.

Bu tarihten sonraki sonuçlar (`YYYY-MM-DD`).

Bu tarihten önceki sonuçlar (`YYYY-MM-DD`).

İçerik çıkarımı seçenekleri (aşağıya bakın).

### İçerik çıkarımı

Exa, arama sonuçlarının yanında çıkarılmış içerik döndürebilir. Etkinleştirmek için bir `contents` nesnesi iletin:

javascriptCopy code
[code]
    await web_search({  query: "transformer architecture explained",  type: "neural",  contents: {    text: true, // full page text    highlights: { numSentences: 3 }, // key sentences    summary: true, // AI summary  },});
[/code]

İçerik seçeneği | Tür | Açıklama  
---|---|---  
`text` | `boolean | { maxCharacters }` | Tam sayfa metnini çıkar  
`highlights` | `boolean | { maxCharacters, query, numSentences, highlightsPerUrl }` | Önemli cümleleri çıkar  
`summary` | `boolean | { query }` | Yapay zeka tarafından oluşturulan özet  
  
### Arama modları

Mod | Açıklama  
---|---  
`auto` | Exa en iyi modu seçer (varsayılan)  
`neural` | Anlamsal/anlama dayalı arama  
`fast` | Hızlı anahtar kelime araması  
`deep` | Kapsamlı derin arama  
`deep-reasoning` | Akıl yürütmeli derin arama  
`instant` | En hızlı sonuçlar  
  
## Notlar

  * Hiçbir `contents` seçeneği sağlanmazsa Exa varsayılan olarak `{ highlights: true }` kullanır; böylece sonuçlar önemli cümle alıntıları içerir
  * Kullanılabilir olduğunda sonuçlar, Exa API yanıtındaki `highlightScores` ve `summary` alanlarını korur
  * Sonuç açıklamaları önce vurgulardan, sonra özetten, sonra da tam metinden çözümlenir; hangisi kullanılabilirse
  * `freshness` ve `date_after`/`date_before` birlikte kullanılamaz; tek bir zaman filtresi modu kullanın
  * Sorgu başına en fazla 100 sonuç döndürülebilir (Exa arama türü sınırlarına tabidir)
  * Sonuçlar varsayılan olarak 15 dakika önbelleğe alınır (`cacheTtlMinutes` ile yapılandırılabilir)
  * Exa, yapılandırılmış JSON yanıtları sunan resmi bir API entegrasyonudur


## İlgili

  * [Web Search genel bakışı](</tr/tools/web>) \-- tüm sağlayıcılar ve otomatik algılama
  * [Brave Search](</tr/tools/brave-search>) \-- ülke/dil filtreleriyle yapılandırılmış sonuçlar
  * [Perplexity Search](</tr/tools/perplexity-search>) \-- alan adı filtrelemeyle yapılandırılmış sonuçlar


Was this useful?YesNo