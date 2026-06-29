---
title: Paralel arama
source_url: https://docs.openclaw.ai/tr/tools/parallel-search
scraped_at: 2026-06-29
---

CapabilitiesTools

Parallel Plugin'i iki [Parallel](<https://parallel.ai/>) `web_search` sağlayıcısı sunar:

  * **Parallel Search (Free)** (`parallel-free`) -- Parallel'ın ücretsiz [Search MCP](<https://docs.parallel.ai/integrations/mcp/search-mcp>) hizmeti. Hesap veya API anahtarı gerektirmez. Parallel'ın barındırılan, anahtarsız arama yolunu istediğinizde bunu açıkça seçin.
  * **Parallel Search** (`parallel`) -- Parallel'ın ücretli Search API'si. Bir `PARALLEL_API_KEY` gerektirir ve daha yüksek hız limitleri ile hedef ayarı sunar.


İkisi de AI agent'ları için oluşturulmuş bir web dizininden sıralanmış, LLM için optimize edilmiş alıntılar döndürür. Birini açıkça seçmek için `tools.web.search.provider` değerini `parallel-free` veya `parallel` olarak ayarlayın.

## Plugin'i yükleyin

Resmi Plugin'i yükleyin, ardından Gateway'i yeniden başlatın:

bashCopy code
[code]
    openclaw plugins install @openclaw/parallel-pluginopenclaw gateway restart
[/code]

## API anahtarı (ücretli sağlayıcı)

`parallel-free` API anahtarı gerektirmez, ancak yine de yönetilen sağlayıcı olarak seçilmelidir. Ücretli `parallel` sağlayıcısı bir API anahtarı gerektirir:

* ### Hesap oluşturun

[platform.parallel.ai](<https://platform.parallel.ai>) adresinden kaydolun ve panonuzdan bir API anahtarı oluşturun.

* ### Anahtarı depolayın

Gateway ortamında `PARALLEL_API_KEY` ayarlayın veya şu komutla yapılandırın:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## Yapılandırma

json5Copy code
[code]
    {  plugins: {    entries: {      parallel: {        config: {          webSearch: {            apiKey: "par-...", // optional if PARALLEL_API_KEY is set            baseUrl: "https://api.parallel.ai", // optional; OpenClaw appends /v1/search          },        },      },    },  },  tools: {    web: {      search: {        // Use "parallel-free" for the free Search MCP, or "parallel" for        // the paid API-backed provider shown here.        provider: "parallel",      },    },  },}
[/code]

**Ortam alternatifi:** Gateway ortamında `PARALLEL_API_KEY` ayarlayın. Bir gateway kurulumu için bunu `~/.openclaw/.env` içine koyun.

## Temel URL geçersiz kılma

Temel URL geçersiz kılması yalnızca ücretli `parallel` sağlayıcısına uygulanır. Ücretsiz `parallel-free` sağlayıcısı her zaman `https://search.parallel.ai/mcp` kullanır.

Parallel isteklerinin uyumlu bir proxy veya alternatif Parallel uç noktası (örneğin Cloudflare AI Gateway) üzerinden gitmesi gerektiğinde `plugins.entries.parallel.config.webSearch.baseUrl` ayarlayın. OpenClaw, çıplak ana makine adlarını başına `https://` ekleyerek normalleştirir ve yol zaten orada bitmiyorsa `/v1/search` ekler. Çözümlenen uç nokta arama önbellek anahtarına dahil edilir, bu nedenle farklı Parallel uç noktalarından gelen sonuçlar paylaşılmaz.

## Araç parametreleri

OpenClaw, modelin hem doğal dildeki hedefi hem de birkaç kısa anahtar kelime sorgusunu doldurabilmesi için Parallel'ın yerel arama şeklini sunar; bu eşleştirme, Parallel'ın en iyi sonuçlar için [önerdiği](<https://docs.parallel.ai/search/best-practices>) yaklaşımdır.

Alttaki sorunun veya hedefin doğal dilde açıklaması (en fazla 5000 karakter). Kendi başına anlaşılır olmalıdır.

Kısa anahtar kelime arama sorguları, her biri 3-6 kelime (1-5 giriş, her biri en fazla 200 karakter). En iyi sonuçlar için 2-3 çeşitli sorgu sağlayın.

Döndürülecek sonuç sayısı (1-40).

İsteğe bağlı Parallel oturum kimliği (`parallel` üzerinde en fazla 1000 karakter; ücretsiz `parallel-free` Search MCP bunu 100 ile sınırlar). Aynı görevin parçası olan takip aramalarında önceki bir Parallel sonucundan gelen `sessionId` değerini geçirin; böylece Parallel ilgili çağrıları gruplayabilir ve sonraki sonuçları iyileştirebilir. Sınırı aşan bir kimlik atılır ve yeni bir kimlik oluşturulur.

Çağrıyı yapan modelin isteğe bağlı tanımlayıcısı (örn. `claude-opus-4-7`, `gpt-5.5`). Parallel'ın modelinizin yeteneklerine göre varsayılan ayarları uyarlamasını sağlar. Tam etkin model slug'ını geçirin; bir aile takma adına kısaltmayın.

## Notlar

  * Parallel, sonuçları insan tıklama oranına göre değil LLM akıl yürütme faydasına göre sıralar ve sıkıştırır; tam sayfa içerik yerine her sonuçta yoğun alıntılar bekleyin
  * Sonuç alıntıları `excerpts` dizisi olarak döner ve genel `web_search` sözleşmesiyle uyumluluk için `description` alanında da birleştirilir
  * Parallel her yanıtta bir `session_id` döndürür; OpenClaw bunu araç yükünde `sessionId` olarak sunar, böylece çağıranlar takip aramalarını gruplayabilir
  * Parallel'dan gelen `searchId`, `warnings` ve `usage` mevcut olduklarında aynen geçirilir
  * OpenClaw, çözümlenmiş sonuç sayısını her zaman Parallel'a `advanced_settings.max_results` olarak iletir. Önce çağıranın `count` argümanı, sonra üst düzey `tools.web.search.maxResults` ayarı kazanır; aksi halde OpenClaw'ın genel `web_search` varsayılanı (5) kullanılır. Bu, sağlayıcılar arasında geçiş yaparken sonuç hacmini tutarlı tutar; Parallel kendi başına varsayılan olarak 10 kullanır
  * Sonuçlar varsayılan olarak 15 dakika önbelleğe alınır (`cacheTtlMinutes` ile yapılandırılabilir)
  * Ücretsiz `parallel-free` sağlayıcısı aynı parametreleri kabul eder. `count` değerini istemci tarafında uygular ve sağlanmadığında her çağrı için bir `session_id` oluşturur.


## İlgili

  * [Web Search genel bakışı](</tr/tools/web>) \-- tüm sağlayıcılar ve otomatik algılama
  * [Exa arama](</tr/tools/exa-search>) \-- içerik çıkarma ile nöral arama
  * [Perplexity Search](</tr/tools/perplexity-search>) \-- alan adı filtreleme ile yapılandırılmış sonuçlar


Was this useful?YesNo

Open issue