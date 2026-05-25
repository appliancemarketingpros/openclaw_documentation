---
title: Web araması
source_url: https://docs.openclaw.ai/tr/tools/web
scraped_at: 2026-05-25
---

`web_search` aracı, yapılandırdığınız sağlayıcıyı kullanarak web'de arama yapar ve sonuçları döndürür. Sonuçlar sorguya göre 15 dakika boyunca önbelleğe alınır (yapılandırılabilir).

OpenClaw ayrıca X (eski adıyla Twitter) gönderileri için `x_search` ve hafif URL getirme için `web_fetch` içerir. Bu aşamada `web_fetch` yerel kalırken `web_search` ve `x_search` arka planda xAI Responses kullanabilir.

## Hızlı başlangıç

* ### Bir sağlayıcı seçin

Bir sağlayıcı seçin ve gerekli kurulumları tamamlayın. Bazı sağlayıcılar anahtar gerektirmezken, bazıları API anahtarları kullanır. Ayrıntılar için aşağıdaki sağlayıcı sayfalarına bakın.

* ### Yapılandırın

bashCopy code
[code]
    openclaw configure --section web
[/code]

Bu, sağlayıcıyı ve gereken kimlik bilgisini saklar. Ayrıca bir ortam değişkeni (örneğin `BRAVE_API_KEY`) ayarlayıp API destekli sağlayıcılar için bu adımı atlayabilirsiniz.

* ### Kullanın

Agent artık `web_search` çağırabilir:

javascriptCopy code
[code]
    await web_search({ query: "OpenClaw plugin SDK" });
[/code]

X gönderileri için şunu kullanın:

javascriptCopy code
[code]
    await x_search({ query: "dinner recipes" });
[/code]

## Sağlayıcı seçme

[**Brave Search** Kesitlerle yapılandırılmış sonuçlar. `llm-context` modunu ve ülke/dil filtrelerini destekler. Ücretsiz katman mevcut. ](</tr/tools/brave-search>) [**DuckDuckGo** Anahtarsız yedek. API anahtarı gerekmez. Resmi olmayan HTML tabanlı entegrasyon. ](</tr/tools/duckduckgo-search>) [**Exa** İçerik çıkarma (vurgular, metin, özetler) ile sinirsel + anahtar kelime araması. ](</tr/tools/exa-search>) [**Firecrawl** Yapılandırılmış sonuçlar. Derin çıkarım için `firecrawl_search` ve `firecrawl_scrape` ile birlikte en iyi çalışır. ](</tr/tools/firecrawl>) [**Gemini** Google Search ile temellendirme üzerinden atıflı, yapay zeka sentezli yanıtlar. ](</tr/tools/gemini-search>) [**Grok** xAI web temellendirmesi üzerinden atıflı, yapay zeka sentezli yanıtlar. ](</tr/tools/grok-search>) [**Kimi** Moonshot web araması üzerinden atıflı, yapay zeka sentezli yanıtlar; temellendirilmemiş sohbet yedekleri açıkça başarısız olur. ](</tr/tools/kimi-search>) [**MiniMax Search** MiniMax Token Plan arama API'si üzerinden yapılandırılmış sonuçlar. ](</tr/tools/minimax-search>) [**Ollama Web Search** Oturum açılmış yerel Ollama ana makinesi veya barındırılan Ollama API'si üzerinden arama. ](</tr/tools/ollama-search>) [**Perplexity** İçerik çıkarma denetimleri ve alan adı filtreleme ile yapılandırılmış sonuçlar. ](</tr/tools/perplexity-search>) [**SearXNG** Kendi kendine barındırılan meta arama. API anahtarı gerekmez. Google, Bing, DuckDuckGo ve daha fazlasını bir araya getirir. ](</tr/tools/searxng-search>) [**Tavily** Arama derinliği, konu filtreleme ve URL çıkarma için `tavily_extract` ile yapılandırılmış sonuçlar. ](</tr/tools/tavily>)

### Sağlayıcı karşılaştırması

Sağlayıcı | Sonuç biçimi | Filtreler | API anahtarı  
---|---|---|---  
[Brave](</tr/tools/brave-search>) | Yapılandırılmış kesitler | Ülke, dil, zaman, `llm-context` modu | `BRAVE_API_KEY`  
[DuckDuckGo](</tr/tools/duckduckgo-search>) | Yapılandırılmış kesitler | \-- | Yok (anahtarsız)  
[Exa](</tr/tools/exa-search>) | Yapılandırılmış + çıkarılmış | Sinirsel/anahtar kelime modu, tarih, içerik çıkarma | `EXA_API_KEY`  
[Firecrawl](</tr/tools/firecrawl>) | Yapılandırılmış kesitler | `firecrawl_search` aracı üzerinden | `FIRECRAWL_API_KEY`  
[Gemini](</tr/tools/gemini-search>) | Yapay zeka sentezli + atıflar | \-- | `GEMINI_API_KEY`  
[Grok](</tr/tools/grok-search>) | Yapay zeka sentezli + atıflar | \-- | `XAI_API_KEY`  
[Kimi](</tr/tools/kimi-search>) | Yapay zeka sentezli + atıflar; temellendirilmemiş sohbet yedeklerinde başarısız olur | \-- | `KIMI_API_KEY` / `MOONSHOT_API_KEY`  
[MiniMax Search](</tr/tools/minimax-search>) | Yapılandırılmış kesitler | Bölge (`global` / `cn`) | `MINIMAX_CODE_PLAN_KEY` / `MINIMAX_CODING_API_KEY` / `MINIMAX_OAUTH_TOKEN`  
[Ollama Web Search](</tr/tools/ollama-search>) | Yapılandırılmış kesitler | \-- | Oturum açılmış yerel ana makineler için yok; doğrudan `https://ollama.com` araması için `OLLAMA_API_KEY`  
[Perplexity](</tr/tools/perplexity-search>) | Yapılandırılmış kesitler | Ülke, dil, zaman, alan adları, içerik sınırları | `PERPLEXITY_API_KEY` / `OPENROUTER_API_KEY`  
[SearXNG](</tr/tools/searxng-search>) | Yapılandırılmış kesitler | Kategoriler, dil | Yok (kendi kendine barındırılan)  
[Tavily](</tr/tools/tavily>) | Yapılandırılmış kesitler | `tavily_search` aracı üzerinden | `TAVILY_API_KEY`  
  
## Otomatik algılama

## Yerel OpenAI web araması

Doğrudan OpenAI Responses modelleri, OpenClaw web araması etkin olduğunda ve yönetilen bir sağlayıcı sabitlenmediğinde OpenAI'nin barındırılan `web_search` aracını otomatik olarak kullanır. Bu, pakete dahil OpenAI Plugin'inde sağlayıcıya ait bir davranıştır ve yalnızca yerel OpenAI API trafiği için geçerlidir; OpenAI uyumlu proxy temel URL'leri veya Azure rotaları için geçerli değildir. OpenAI modelleri için yönetilen `web_search` aracını korumak üzere `tools.web.search.provider` değerini `brave` gibi başka bir sağlayıcıya ayarlayın veya hem yönetilen aramayı hem de yerel OpenAI aramasını devre dışı bırakmak için `tools.web.search.enabled: false` ayarlayın.

## Yerel Codex web araması

Codex özellikli modeller, OpenClaw'ın yönetilen `web_search` işlevi yerine isteğe bağlı olarak sağlayıcıya özgü Responses `web_search` aracını kullanabilir.

  * Bunu `tools.web.search.openaiCodex` altında yapılandırın
  * Yalnızca Codex özellikli modeller için etkinleşir (`openai-codex/*` veya `api: "openai-codex-responses"` kullanan sağlayıcılar)
  * Yönetilen `web_search`, Codex olmayan modeller için geçerli olmaya devam eder
  * `mode: "cached"` varsayılan ve önerilen ayardır
  * `tools.web.search.enabled: false`, hem yönetilen hem de yerel aramayı devre dışı bırakır

json5Copy code
[code]
    {  tools: {    web: {      search: {        enabled: true,        openaiCodex: {          enabled: true,          mode: "cached",          allowedDomains: ["example.com"],          contextSize: "high",          userLocation: {            country: "US",            city: "New York",            timezone: "America/New_York",          },        },      },    },  },}
[/code]

Yerel Codex araması etkinse ancak mevcut model Codex özellikli değilse OpenClaw normal yönetilen `web_search` davranışını korur.

## Ağ güvenliği

Yönetilen `web_search` sağlayıcı çağrıları OpenClaw'ın korumalı getirme yolunu kullanır. Güvenilen sağlayıcı API ana makineleri için OpenClaw, Surge, Clash ve sing-box fake-IP DNS yanıtlarına `198.18.0.0/15` ve `fc00::/7` içinde yalnızca ilgili sağlayıcı ana makine adı için izin verir. Diğer özel, geri döngü, bağlantı-yerel ve meta veri hedefleri engellenmiş kalır.

Bu otomatik izin, rastgele `web_fetch` URL'leri için geçerli değildir. `web_fetch` için `tools.web.fetch.ssrfPolicy.allowRfc2544BenchmarkRange` ve `tools.web.fetch.ssrfPolicy.allowIpv6UniqueLocalRange` seçeneklerini yalnızca güvenilir proxy'niz bu sentetik aralıkların sahibiyse açıkça etkinleştirin.

## Web aramasını ayarlama

Dokümanlardaki ve kurulum akışlarındaki sağlayıcı listeleri alfabetiktir. Otomatik algılama ayrı bir öncelik sırası kullanır.

Hiçbir `provider` ayarlanmamışsa OpenClaw sağlayıcıları bu sırayla denetler ve hazır olan ilkini kullanır:

Önce API destekli sağlayıcılar:

  1. **Brave** \-- `BRAVE_API_KEY` veya `plugins.entries.brave.config.webSearch.apiKey` (sıra 10)
  2. **MiniMax Search** \-- `MINIMAX_CODE_PLAN_KEY` / `MINIMAX_CODING_API_KEY` / `MINIMAX_OAUTH_TOKEN` / `MINIMAX_API_KEY` veya `plugins.entries.minimax.config.webSearch.apiKey` (sıra 15)
  3. **Gemini** \-- `plugins.entries.google.config.webSearch.apiKey`, `GEMINI_API_KEY` veya `models.providers.google.apiKey` (sıra 20)
  4. **Grok** \-- `XAI_API_KEY` veya `plugins.entries.xai.config.webSearch.apiKey` (sıra 30)
  5. **Kimi** \-- `KIMI_API_KEY` / `MOONSHOT_API_KEY` veya `plugins.entries.moonshot.config.webSearch.apiKey` (sıra 40)
  6. **Perplexity** \-- `PERPLEXITY_API_KEY` / `OPENROUTER_API_KEY` veya `plugins.entries.perplexity.config.webSearch.apiKey` (sıra 50)
  7. **Firecrawl** \-- `FIRECRAWL_API_KEY` veya `plugins.entries.firecrawl.config.webSearch.apiKey` (sıra 60)
  8. **Exa** \-- `EXA_API_KEY` veya `plugins.entries.exa.config.webSearch.apiKey`; isteğe bağlı `plugins.entries.exa.config.webSearch.baseUrl`, Exa uç noktasını geçersiz kılar (sıra 65)
  9. **Tavily** \-- `TAVILY_API_KEY` veya `plugins.entries.tavily.config.webSearch.apiKey` (sıra 70)


Bundan sonra anahtarsız yedekler:

  10. **DuckDuckGo** \-- hesap veya API anahtarı gerektirmeyen anahtarsız HTML yedeği (sıra 100)
  11. **Ollama Web Search** \-- yapılandırılmış yerel Ollama ana makineniz erişilebilir olduğunda ve `ollama signin` ile oturum açıldığında bu ana makine üzerinden anahtarsız yedek; ana makine ihtiyaç duyduğunda Ollama sağlayıcı bearer kimlik doğrulamasını yeniden kullanabilir ve `OLLAMA_API_KEY` ile yapılandırıldığında doğrudan `https://ollama.com` araması çağırabilir (sıra 110)
  12. **SearXNG** \-- `SEARXNG_BASE_URL` veya `plugins.entries.searxng.config.webSearch.baseUrl` (sıra 200)


Hiçbir sağlayıcı algılanmazsa Brave'e geri döner (bir tane yapılandırmanızı isteyen eksik anahtar hatası alırsınız).

## Yapılandırma

json5Copy code
[code]
    {  tools: {    web: {      search: {        enabled: true, // default: true        provider: "brave", // or omit for auto-detection        maxResults: 5,        timeoutSeconds: 30,        cacheTtlMinutes: 15,      },    },  },}
[/code]

Sağlayıcıya özgü yapılandırma (API anahtarları, temel URL'ler, modlar) `plugins.entries.<plugin>.config.webSearch.*` altında yer alır. Gemini ayrıca, özel web araması yapılandırmasından ve `GEMINI_API_KEY` değerinden sonra daha düşük öncelikli yedekler olarak `models.providers.google.apiKey` ve `models.providers.google.baseUrl` değerlerini yeniden kullanabilir. Örnekler için sağlayıcı sayfalarına bakın.

`tools.web.search.provider`, paketli ve yüklü Plugin manifestleri tarafından bildirilen web arama sağlayıcısı kimliklerine göre doğrulanır. `"brvae"` gibi bir yazım hatası, sessizce otomatik algılamaya geri dönmek yerine yapılandırma doğrulamasını başarısız kılar. Yapılandırılmış bir sağlayıcıda yalnızca eski Plugin kanıtı varsa, örneğin üçüncü taraf bir Plugin kaldırıldıktan sonra kalan bir `plugins.entries.<plugin>` bloğu gibi, OpenClaw başlatmayı dayanıklı tutar ve Plugin'i yeniden yükleyebilmeniz veya eski yapılandırmayı temizlemek için `openclaw doctor --fix` çalıştırabilmeniz amacıyla bir uyarı bildirir.

`web_fetch` yedek sağlayıcı seçimi ayrıdır:

  * bunu `tools.web.fetch.provider` ile seçin
  * veya bu alanı atlayın ve OpenClaw'ın kullanılabilir kimlik bilgilerinden hazır olan ilk web getirme sağlayıcısını otomatik algılamasına izin verin
  * sandbox dışı `web_fetch`, `contracts.webFetchProviders` bildiren yüklü Plugin sağlayıcılarını kullanabilir; sandbox içindeki getirmeler yalnızca paketli olanlarla sınırlı kalır
  * bugün paketli web getirme sağlayıcısı Firecrawl'dır ve `plugins.entries.firecrawl.config.webFetch.*` altında yapılandırılır


`openclaw onboard` veya `openclaw configure --section web` sırasında **Kimi** seçtiğinizde, OpenClaw ayrıca şunları sorabilir:

  * Moonshot API bölgesi (`https://api.moonshot.ai/v1` veya `https://api.moonshot.cn/v1`)
  * varsayılan Kimi web arama modeli (varsayılan: `kimi-k2.6`)


`x_search` için `plugins.entries.xai.config.xSearch.*` yapılandırmasını yapın. Sohbetle aynı xAI kimlik doğrulama profilini veya Grok web araması tarafından kullanılan `XAI_API_KEY` / Plugin web arama kimlik bilgisini kullanır. Eski `tools.web.x_search.*` yapılandırması `openclaw doctor --fix` tarafından otomatik geçirilir. `openclaw onboard` veya `openclaw configure --section web` sırasında Grok seçtiğinizde, OpenClaw aynı anahtarla isteğe bağlı `x_search` kurulumu da sunabilir. Bu, Grok yolu içinde ayrı bir takip adımıdır; ayrı bir üst düzey web arama sağlayıcısı seçimi değildir. Başka bir sağlayıcı seçerseniz OpenClaw `x_search` istemini göstermez.

### API anahtarlarını saklama

### Yapılandırma dosyası

`openclaw configure --section web` çalıştırın veya anahtarı doğrudan ayarlayın:

json5Copy code
[code]
    {  plugins: {    entries: {      brave: {        config: {          webSearch: {            apiKey: "YOUR_KEY", // pragma: allowlist secret          },        },      },    },  },}
[/code]

### Ortam değişkeni

Sağlayıcı ortam değişkenini Gateway süreç ortamında ayarlayın:

bashCopy code
[code]
    export BRAVE_API_KEY="YOUR_KEY"
[/code]

Bir Gateway kurulumu için bunu `~/.openclaw/.env` içine koyun. Bkz. [Ortam değişkenleri](</tr/help/faq#env-vars-and-env-loading>).

## Araç parametreleri

Parametre | Açıklama  
---|---  
`query` | Arama sorgusu (zorunlu)  
`count` | Döndürülecek sonuçlar (1-10, varsayılan: 5)  
`country` | 2 harfli ISO ülke kodu (örn. "US", "DE")  
`language` | ISO 639-1 dil kodu (örn. "en", "de")  
`search_lang` | Arama dili kodu (yalnızca Brave)  
`freshness` | Zaman filtresi: `day`, `week`, `month` veya `year`  
`date_after` | Bu tarihten sonraki sonuçlar (YYYY-MM-DD)  
`date_before` | Bu tarihten önceki sonuçlar (YYYY-MM-DD)  
`ui_lang` | Kullanıcı arayüzü dil kodu (yalnızca Brave)  
`domain_filter` | Alan adı izin listesi/ret listesi dizisi (yalnızca Perplexity)  
`max_tokens` | Toplam içerik bütçesi, varsayılan 25000 (yalnızca Perplexity)  
`max_tokens_per_page` | Sayfa başına token sınırı, varsayılan 2048 (yalnızca Perplexity)  
  
## x_search

`x_search`, xAI kullanarak X (eski adıyla Twitter) gönderilerini sorgular ve alıntılarla birlikte AI tarafından sentezlenmiş yanıtlar döndürür. Doğal dil sorgularını ve isteğe bağlı yapılandırılmış filtreleri kabul eder. OpenClaw yerleşik xAI `x_search` aracını yalnızca bu araç çağrısına hizmet eden istekte etkinleştirir.

### x_search yapılandırması

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          xSearch: {            enabled: true,            model: "grok-4-1-fast-non-reasoning",            baseUrl: "https://api.x.ai/v1", // optional, overrides webSearch.baseUrl            inlineCitations: false,            maxTurns: 2,            timeoutSeconds: 30,            cacheTtlMinutes: 15,          },          webSearch: {            apiKey: "xai-...", // optional if an xAI auth profile or XAI_API_KEY is set            baseUrl: "https://api.x.ai/v1", // optional shared xAI Responses base URL          },        },      },    },  },}
[/code]

`plugins.entries.xai.config.xSearch.baseUrl` ayarlandığında `x_search` `<baseUrl>/responses` adresine gönderir. Bu alan atlanırsa `plugins.entries.xai.config.webSearch.baseUrl`, ardından eski `tools.web.search.grok.baseUrl` ve son olarak herkese açık xAI uç noktasına geri döner.

### x_search parametreleri

Parametre | Açıklama  
---|---  
`query` | Arama sorgusu (zorunlu)  
`allowed_x_handles` | Sonuçları belirli X kullanıcı adlarıyla sınırla  
`excluded_x_handles` | Belirli X kullanıcı adlarını hariç tut  
`from_date` | Yalnızca bu tarihte veya sonrasında olan gönderileri dahil et (YYYY-MM-DD)  
`to_date` | Yalnızca bu tarihte veya öncesinde olan gönderileri dahil et (YYYY-MM-DD)  
`enable_image_understanding` | xAI'ın eşleşen gönderilere ekli görselleri incelemesine izin ver  
`enable_video_understanding` | xAI'ın eşleşen gönderilere ekli videoları incelemesine izin ver  
  
### x_search örneği

javascriptCopy code
[code]
    await x_search({  query: "dinner recipes",  allowed_x_handles: ["nytfood"],  from_date: "2026-03-01",});
[/code]

javascriptCopy code
[code]
    // Per-post stats: use the exact status URL or status ID when possibleawait x_search({  query: "https://x.com/huntharo/status/1905678901234567890",});
[/code]

## Örnekler

javascriptCopy code
[code]
    // Basic searchawait web_search({ query: "OpenClaw plugin SDK" }); // German-specific searchawait web_search({ query: "TV online schauen", country: "DE", language: "de" }); // Recent results (past week)await web_search({ query: "AI developments", freshness: "week" }); // Date rangeawait web_search({  query: "climate research",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (Perplexity only)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],});
[/code]

## Araç profilleri

Araç profilleri veya izin listeleri kullanıyorsanız `web_search`, `x_search` ya da `group:web` ekleyin:

json5Copy code
[code]
    {  tools: {    allow: ["web_search", "x_search"],    // or: allow: ["group:web"]  (includes web_search, x_search, and web_fetch)  },}
[/code]

## İlgili

  * [Web Getirme](</tr/tools/web-fetch>) \-- bir URL getirir ve okunabilir içeriği çıkarır
  * [Web Tarayıcısı](</tr/tools/browser>) \-- JS ağırlıklı siteler için tam tarayıcı otomasyonu
  * [Grok Arama](</tr/tools/grok-search>) \-- `web_search` sağlayıcısı olarak Grok
  * [Ollama Web Araması](</tr/tools/ollama-search>) \-- Ollama ana makineniz üzerinden anahtarsız web araması


Was this useful?YesNo