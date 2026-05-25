---
title: Pencarian web
source_url: https://docs.openclaw.ai/id/tools/web
scraped_at: 2026-05-25
---

Alat `web_search` menelusuri web menggunakan penyedia yang Anda konfigurasi dan mengembalikan hasil. Hasil di-cache berdasarkan kueri selama 15 menit (dapat dikonfigurasi).

OpenClaw juga menyertakan `x_search` untuk postingan X (sebelumnya Twitter) dan `web_fetch` untuk pengambilan URL ringan. Pada fase ini, `web_fetch` tetap lokal sementara `web_search` dan `x_search` dapat menggunakan xAI Responses di balik layar.

## Mulai cepat

* ### Choose a provider

Pilih penyedia dan selesaikan penyiapan yang diperlukan. Beberapa penyedia bebas kunci, sementara yang lain menggunakan kunci API. Lihat halaman penyedia di bawah untuk detail.

* ### Configure

bashCopy code
[code]
    openclaw configure --section web
[/code]

Ini menyimpan penyedia dan kredensial yang diperlukan. Anda juga dapat menetapkan env var (misalnya `BRAVE_API_KEY`) dan melewati langkah ini untuk penyedia berbasis API.

* ### Use it

Agen sekarang dapat memanggil `web_search`:

javascriptCopy code
[code]
    await web_search({ query: "OpenClaw plugin SDK" });
[/code]

Untuk postingan X, gunakan:

javascriptCopy code
[code]
    await x_search({ query: "dinner recipes" });
[/code]

## Memilih penyedia

[**Brave Search** Hasil terstruktur dengan cuplikan. Mendukung mode `llm-context`, filter negara/bahasa. Tingkat gratis tersedia. ](</id/tools/brave-search>) [**DuckDuckGo** Fallback bebas kunci. Tidak perlu kunci API. Integrasi tidak resmi berbasis HTML. ](</id/tools/duckduckgo-search>) [**Exa** Pencarian neural + kata kunci dengan ekstraksi konten (sorotan, teks, ringkasan). ](</id/tools/exa-search>) [**Firecrawl** Hasil terstruktur. Paling baik dipasangkan dengan `firecrawl_search` dan `firecrawl_scrape` untuk ekstraksi mendalam. ](</id/tools/firecrawl>) [**Gemini** Jawaban yang disintesis AI dengan sitasi melalui grounding Google Search. ](</id/tools/gemini-search>) [**Grok** Jawaban yang disintesis AI dengan sitasi melalui grounding web xAI. ](</id/tools/grok-search>) [**Kimi** Jawaban yang disintesis AI dengan sitasi melalui pencarian web Moonshot; fallback chat tanpa grounding gagal secara eksplisit. ](</id/tools/kimi-search>) [**MiniMax Search** Hasil terstruktur melalui API pencarian MiniMax Token Plan. ](</id/tools/minimax-search>) [**Ollama Web Search** Pencarian melalui host Ollama lokal yang sudah masuk atau API Ollama yang di-host. ](</id/tools/ollama-search>) [**Perplexity** Hasil terstruktur dengan kontrol ekstraksi konten dan pemfilteran domain. ](</id/tools/perplexity-search>) [**SearXNG** Meta-pencarian yang di-host sendiri. Tidak perlu kunci API. Mengagregasi Google, Bing, DuckDuckGo, dan lainnya. ](</id/tools/searxng-search>) [**Tavily** Hasil terstruktur dengan kedalaman pencarian, pemfilteran topik, dan `tavily_extract` untuk ekstraksi URL. ](</id/tools/tavily>)

### Perbandingan penyedia

Penyedia | Gaya hasil | Filter | Kunci API  
---|---|---|---  
[Brave](</id/tools/brave-search>) | Cuplikan terstruktur | Negara, bahasa, waktu, mode `llm-context` | `BRAVE_API_KEY`  
[DuckDuckGo](</id/tools/duckduckgo-search>) | Cuplikan terstruktur | \-- | Tidak ada (bebas kunci)  
[Exa](</id/tools/exa-search>) | Terstruktur + diekstrak | Mode neural/kata kunci, tanggal, ekstraksi konten | `EXA_API_KEY`  
[Firecrawl](</id/tools/firecrawl>) | Cuplikan terstruktur | Melalui alat `firecrawl_search` | `FIRECRAWL_API_KEY`  
[Gemini](</id/tools/gemini-search>) | Disintesis AI + sitasi | \-- | `GEMINI_API_KEY`  
[Grok](</id/tools/grok-search>) | Disintesis AI + sitasi | \-- | `XAI_API_KEY`  
[Kimi](</id/tools/kimi-search>) | Disintesis AI + sitasi; gagal pada fallback chat tanpa grounding | \-- | `KIMI_API_KEY` / `MOONSHOT_API_KEY`  
[MiniMax Search](</id/tools/minimax-search>) | Cuplikan terstruktur | Wilayah (`global` / `cn`) | `MINIMAX_CODE_PLAN_KEY` / `MINIMAX_CODING_API_KEY` / `MINIMAX_OAUTH_TOKEN`  
[Ollama Web Search](</id/tools/ollama-search>) | Cuplikan terstruktur | \-- | Tidak ada untuk host lokal yang sudah masuk; `OLLAMA_API_KEY` untuk pencarian langsung `https://ollama.com`  
[Perplexity](</id/tools/perplexity-search>) | Cuplikan terstruktur | Negara, bahasa, waktu, domain, batas konten | `PERPLEXITY_API_KEY` / `OPENROUTER_API_KEY`  
[SearXNG](</id/tools/searxng-search>) | Cuplikan terstruktur | Kategori, bahasa | Tidak ada (di-host sendiri)  
[Tavily](</id/tools/tavily>) | Cuplikan terstruktur | Melalui alat `tavily_search` | `TAVILY_API_KEY`  
  
## Deteksi otomatis

## Pencarian web OpenAI native

Model OpenAI Responses langsung menggunakan alat `web_search` yang di-host OpenAI secara otomatis ketika pencarian web OpenClaw diaktifkan dan tidak ada penyedia terkelola yang dipatok. Ini adalah perilaku milik penyedia di Plugin OpenAI bawaan dan hanya berlaku untuk lalu lintas API OpenAI native, bukan URL dasar proxy yang kompatibel dengan OpenAI atau rute Azure. Tetapkan `tools.web.search.provider` ke penyedia lain seperti `brave` untuk tetap menggunakan alat `web_search` terkelola bagi model OpenAI, atau tetapkan `tools.web.search.enabled: false` untuk menonaktifkan pencarian terkelola dan pencarian OpenAI native.

## Pencarian web Codex native

Model berkemampuan Codex secara opsional dapat menggunakan alat `web_search` Responses native penyedia, bukan fungsi `web_search` terkelola OpenClaw.

  * Konfigurasikan di bawah `tools.web.search.openaiCodex`
  * Ini hanya aktif untuk model berkemampuan Codex (`openai-codex/*` atau penyedia yang menggunakan `api: "openai-codex-responses"`)
  * `web_search` terkelola tetap berlaku untuk model non-Codex
  * `mode: "cached"` adalah pengaturan default dan direkomendasikan
  * `tools.web.search.enabled: false` menonaktifkan pencarian terkelola dan native

json5Copy code
[code]
    {  tools: {    web: {      search: {        enabled: true,        openaiCodex: {          enabled: true,          mode: "cached",          allowedDomains: ["example.com"],          contextSize: "high",          userLocation: {            country: "US",            city: "New York",            timezone: "America/New_York",          },        },      },    },  },}
[/code]

Jika pencarian Codex native diaktifkan tetapi model saat ini tidak berkemampuan Codex, OpenClaw mempertahankan perilaku `web_search` terkelola normal.

## Keamanan jaringan

Panggilan penyedia `web_search` terkelola menggunakan jalur fetch terlindungi milik OpenClaw. Untuk host API penyedia tepercaya, OpenClaw mengizinkan jawaban DNS fake-IP Surge, Clash, dan sing-box di `198.18.0.0/15` dan `fc00::/7` hanya untuk nama host penyedia tersebut. Tujuan privat, loopback, link-local, dan metadata lainnya tetap diblokir.

Pengecualian otomatis ini tidak berlaku untuk URL `web_fetch` sembarang. Untuk `web_fetch`, aktifkan `tools.web.fetch.ssrfPolicy.allowRfc2544BenchmarkRange` dan `tools.web.fetch.ssrfPolicy.allowIpv6UniqueLocalRange` secara eksplisit hanya ketika proxy tepercaya Anda memiliki rentang sintetis tersebut.

## Menyiapkan pencarian web

Daftar penyedia dalam docs dan alur penyiapan disusun alfabetis. Deteksi otomatis mempertahankan urutan prioritas terpisah.

Jika tidak ada `provider` yang ditetapkan, OpenClaw memeriksa penyedia dalam urutan ini dan menggunakan yang pertama siap:

Penyedia berbasis API lebih dahulu:

  1. **Brave** \-- `BRAVE_API_KEY` atau `plugins.entries.brave.config.webSearch.apiKey` (urutan 10)
  2. **MiniMax Search** \-- `MINIMAX_CODE_PLAN_KEY` / `MINIMAX_CODING_API_KEY` / `MINIMAX_OAUTH_TOKEN` / `MINIMAX_API_KEY` atau `plugins.entries.minimax.config.webSearch.apiKey` (urutan 15)
  3. **Gemini** \-- `plugins.entries.google.config.webSearch.apiKey`, `GEMINI_API_KEY`, atau `models.providers.google.apiKey` (urutan 20)
  4. **Grok** \-- `XAI_API_KEY` atau `plugins.entries.xai.config.webSearch.apiKey` (urutan 30)
  5. **Kimi** \-- `KIMI_API_KEY` / `MOONSHOT_API_KEY` atau `plugins.entries.moonshot.config.webSearch.apiKey` (urutan 40)
  6. **Perplexity** \-- `PERPLEXITY_API_KEY` / `OPENROUTER_API_KEY` atau `plugins.entries.perplexity.config.webSearch.apiKey` (urutan 50)
  7. **Firecrawl** \-- `FIRECRAWL_API_KEY` atau `plugins.entries.firecrawl.config.webSearch.apiKey` (urutan 60)
  8. **Exa** \-- `EXA_API_KEY` atau `plugins.entries.exa.config.webSearch.apiKey`; `plugins.entries.exa.config.webSearch.baseUrl` opsional mengganti endpoint Exa (urutan 65)
  9. **Tavily** \-- `TAVILY_API_KEY` atau `plugins.entries.tavily.config.webSearch.apiKey` (urutan 70)


Fallback bebas kunci setelah itu:

  10. **DuckDuckGo** \-- fallback HTML bebas kunci tanpa akun atau kunci API (urutan 100)
  11. **Ollama Web Search** \-- fallback bebas kunci melalui host Ollama lokal yang Anda konfigurasi ketika dapat dijangkau dan sudah masuk dengan `ollama signin`; dapat menggunakan ulang autentikasi bearer penyedia Ollama ketika host memerlukannya, dan dapat memanggil pencarian langsung `https://ollama.com` ketika dikonfigurasi dengan `OLLAMA_API_KEY` (urutan 110)
  12. **SearXNG** \-- `SEARXNG_BASE_URL` atau `plugins.entries.searxng.config.webSearch.baseUrl` (urutan 200)


Jika tidak ada penyedia yang terdeteksi, sistem melakukan fallback ke Brave (Anda akan mendapatkan error kunci hilang yang meminta Anda mengonfigurasinya).

## Konfigurasi

json5Copy code
[code]
    {  tools: {    web: {      search: {        enabled: true, // default: true        provider: "brave", // or omit for auto-detection        maxResults: 5,        timeoutSeconds: 30,        cacheTtlMinutes: 15,      },    },  },}
[/code]

Konfigurasi khusus penyedia (kunci API, URL dasar, mode) berada di bawah `plugins.entries.<plugin>.config.webSearch.*`. Gemini juga dapat menggunakan kembali `models.providers.google.apiKey` dan `models.providers.google.baseUrl` sebagai fallback berprioritas lebih rendah setelah konfigurasi pencarian web khususnya dan `GEMINI_API_KEY`. Lihat halaman penyedia untuk contoh.

`tools.web.search.provider` divalidasi terhadap id penyedia pencarian web yang dideklarasikan oleh manifes Plugin bawaan dan terinstal. Kesalahan ketik seperti `"brvae"` menggagalkan validasi konfigurasi alih-alih diam-diam kembali ke deteksi otomatis. Jika penyedia yang dikonfigurasi hanya memiliki bukti Plugin yang usang, seperti blok `plugins.entries.<plugin>` tersisa setelah menghapus Plugin pihak ketiga, OpenClaw menjaga startup tetap tangguh dan melaporkan peringatan agar Anda dapat menginstal ulang Plugin atau menjalankan `openclaw doctor --fix` untuk membersihkan konfigurasi usang.

Pemilihan penyedia fallback `web_fetch` terpisah:

  * pilih dengan `tools.web.fetch.provider`
  * atau hilangkan kolom itu dan biarkan OpenClaw mendeteksi otomatis penyedia web-fetch siap pertama dari kredensial yang tersedia
  * `web_fetch` non-sandbox dapat menggunakan penyedia Plugin terinstal yang mendeklarasikan `contracts.webFetchProviders`; fetch tersandbox tetap hanya bawaan
  * saat ini penyedia web-fetch bawaan adalah Firecrawl, dikonfigurasi di bawah `plugins.entries.firecrawl.config.webFetch.*`


Saat Anda memilih **Kimi** selama `openclaw onboard` atau `openclaw configure --section web`, OpenClaw juga dapat meminta:

  * wilayah API Moonshot (`https://api.moonshot.ai/v1` atau `https://api.moonshot.cn/v1`)
  * model pencarian web Kimi default (default ke `kimi-k2.6`)


Untuk `x_search`, konfigurasikan `plugins.entries.xai.config.xSearch.*`. Ini menggunakan profil autentikasi xAI yang sama seperti chat, atau `XAI_API_KEY` / kredensial pencarian web Plugin yang digunakan oleh pencarian web Grok. Konfigurasi lama `tools.web.x_search.*` dimigrasikan otomatis oleh `openclaw doctor --fix`. Saat Anda memilih Grok selama `openclaw onboard` atau `openclaw configure --section web`, OpenClaw juga dapat menawarkan penyiapan `x_search` opsional dengan kunci yang sama. Ini adalah langkah lanjutan terpisah di dalam jalur Grok, bukan pilihan penyedia pencarian web tingkat atas yang terpisah. Jika Anda memilih penyedia lain, OpenClaw tidak menampilkan prompt `x_search`.

### Menyimpan kunci API

### File konfigurasi

Jalankan `openclaw configure --section web` atau atur kunci secara langsung:

json5Copy code
[code]
    {  plugins: {    entries: {      brave: {        config: {          webSearch: {            apiKey: "YOUR_KEY", // pragma: allowlist secret          },        },      },    },  },}
[/code]

### Variabel lingkungan

Atur variabel env penyedia di lingkungan proses Gateway:

bashCopy code
[code]
    export BRAVE_API_KEY="YOUR_KEY"
[/code]

Untuk instalasi gateway, letakkan di `~/.openclaw/.env`. Lihat [Variabel env](</id/help/faq#env-vars-and-env-loading>).

## Parameter alat

Parameter | Deskripsi  
---|---  
`query` | Kueri pencarian (wajib)  
`count` | Hasil yang dikembalikan (1-10, default: 5)  
`country` | Kode negara ISO 2 huruf (mis. "US", "DE")  
`language` | Kode bahasa ISO 639-1 (mis. "en", "de")  
`search_lang` | Kode bahasa pencarian (hanya Brave)  
`freshness` | Filter waktu: `day`, `week`, `month`, atau `year`  
`date_after` | Hasil setelah tanggal ini (YYYY-MM-DD)  
`date_before` | Hasil sebelum tanggal ini (YYYY-MM-DD)  
`ui_lang` | Kode bahasa UI (hanya Brave)  
`domain_filter` | Array daftar izinkan/tolak domain (hanya Perplexity)  
`max_tokens` | Total anggaran konten, default 25000 (hanya Perplexity)  
`max_tokens_per_page` | Batas token per halaman, default 2048 (hanya Perplexity)  
  
## x_search

`x_search` mengueri postingan X (sebelumnya Twitter) menggunakan xAI dan mengembalikan jawaban yang disintesis AI dengan sitasi. Ini menerima kueri bahasa alami dan filter terstruktur opsional. OpenClaw hanya mengaktifkan alat `x_search` xAI bawaan pada permintaan yang melayani panggilan alat ini.

### Konfigurasi x_search

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          xSearch: {            enabled: true,            model: "grok-4-1-fast-non-reasoning",            baseUrl: "https://api.x.ai/v1", // optional, overrides webSearch.baseUrl            inlineCitations: false,            maxTurns: 2,            timeoutSeconds: 30,            cacheTtlMinutes: 15,          },          webSearch: {            apiKey: "xai-...", // optional if an xAI auth profile or XAI_API_KEY is set            baseUrl: "https://api.x.ai/v1", // optional shared xAI Responses base URL          },        },      },    },  },}
[/code]

`x_search` memposting ke `<baseUrl>/responses` ketika `plugins.entries.xai.config.xSearch.baseUrl` diatur. Jika kolom itu dihilangkan, ia fallback ke `plugins.entries.xai.config.webSearch.baseUrl`, lalu `tools.web.search.grok.baseUrl` lama, dan terakhir endpoint publik xAI.

### Parameter x_search

Parameter | Deskripsi  
---|---  
`query` | Kueri pencarian (wajib)  
`allowed_x_handles` | Batasi hasil ke handle X tertentu  
`excluded_x_handles` | Kecualikan handle X tertentu  
`from_date` | Hanya sertakan postingan pada atau setelah tanggal ini (YYYY-MM-DD)  
`to_date` | Hanya sertakan postingan pada atau sebelum tanggal ini (YYYY-MM-DD)  
`enable_image_understanding` | Izinkan xAI memeriksa gambar yang dilampirkan ke postingan yang cocok  
`enable_video_understanding` | Izinkan xAI memeriksa video yang dilampirkan ke postingan yang cocok  
  
### Contoh x_search

javascriptCopy code
[code]
    await x_search({  query: "dinner recipes",  allowed_x_handles: ["nytfood"],  from_date: "2026-03-01",});
[/code]

javascriptCopy code
[code]
    // Per-post stats: use the exact status URL or status ID when possibleawait x_search({  query: "https://x.com/huntharo/status/1905678901234567890",});
[/code]

## Contoh

javascriptCopy code
[code]
    // Basic searchawait web_search({ query: "OpenClaw plugin SDK" }); // German-specific searchawait web_search({ query: "TV online schauen", country: "DE", language: "de" }); // Recent results (past week)await web_search({ query: "AI developments", freshness: "week" }); // Date rangeawait web_search({  query: "climate research",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (Perplexity only)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],});
[/code]

## Profil alat

Jika Anda menggunakan profil alat atau allowlist, tambahkan `web_search`, `x_search`, atau `group:web`:

json5Copy code
[code]
    {  tools: {    allow: ["web_search", "x_search"],    // or: allow: ["group:web"]  (includes web_search, x_search, and web_fetch)  },}
[/code]

## Terkait

  * [Web Fetch](</id/tools/web-fetch>) \-- fetch URL dan ekstrak konten yang dapat dibaca
  * [Web Browser](</id/tools/browser>) \-- otomasi browser penuh untuk situs berat JS
  * [Grok Search](</id/tools/grok-search>) \-- Grok sebagai penyedia `web_search`
  * [Ollama Web Search](</id/tools/ollama-search>) \-- pencarian web tanpa kunci melalui host Ollama Anda


Was this useful?YesNo