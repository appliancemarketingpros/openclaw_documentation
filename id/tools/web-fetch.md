---
title: Pengambilan web
source_url: https://docs.openclaw.ai/id/tools/web-fetch
scraped_at: 2026-05-25
---

Alat `web_fetch` melakukan HTTP GET biasa dan mengekstrak konten yang dapat dibaca (HTML ke markdown atau teks). Alat ini **tidak** menjalankan JavaScript.

Untuk situs yang sangat bergantung pada JS atau halaman yang dilindungi login, gunakan [Peramban Web](</id/tools/browser>) sebagai gantinya.

## Mulai cepat

`web_fetch` **diaktifkan secara default** \-- tidak perlu konfigurasi. Agent dapat memanggilnya langsung:

javascriptCopy code
[code]
    await web_fetch({ url: "https://example.com/article" });
[/code]

## Parameter alat

URL yang akan diambil. Hanya `http(s)`.

Format keluaran setelah ekstraksi konten utama.

Potong keluaran hingga sebanyak karakter ini.

## Cara kerjanya

* ### Fetch

Mengirim HTTP GET dengan User-Agent mirip Chrome dan header `Accept-Language`. Memblokir hostname privat/internal dan memeriksa ulang pengalihan.

* ### Extract

Menjalankan Readability (ekstraksi konten utama) pada respons HTML.

* ### Fallback (optional)

Jika Readability gagal dan Firecrawl dikonfigurasi, mencoba ulang melalui API Firecrawl dengan mode pengelakan bot.

* ### Cache

Hasil di-cache selama 15 menit (dapat dikonfigurasi) untuk mengurangi pengambilan berulang URL yang sama.

## Konfigurasi

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        enabled: true, // default: true        provider: "firecrawl", // optional; omit for auto-detect        maxChars: 50000, // max output chars        maxCharsCap: 50000, // hard cap for maxChars param        maxResponseBytes: 2000000, // max download size before truncation        timeoutSeconds: 30,        cacheTtlMinutes: 15,        maxRedirects: 3,        useTrustedEnvProxy: false, // let a trusted HTTP(S) env proxy resolve DNS        readability: true, // use Readability extraction        userAgent: "Mozilla/5.0 ...", // override User-Agent        ssrfPolicy: {          allowRfc2544BenchmarkRange: true, // opt-in for trusted fake-IP proxies using 198.18.0.0/15          allowIpv6UniqueLocalRange: true, // opt-in for trusted fake-IP proxies using fc00::/7        },      },    },  },}
[/code]

## Fallback Firecrawl

Jika ekstraksi Readability gagal, `web_fetch` dapat menggunakan fallback ke [Firecrawl](</id/tools/firecrawl>) untuk pengelakan bot dan ekstraksi yang lebih baik:

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        provider: "firecrawl", // optional; omit for auto-detect from available credentials      },    },  },  plugins: {    entries: {      firecrawl: {        enabled: true,        config: {          webFetch: {            apiKey: "fc-...", // optional if FIRECRAWL_API_KEY is set            baseUrl: "https://api.firecrawl.dev",            onlyMainContent: true,            maxAgeMs: 86400000, // cache duration (1 day)            timeoutSeconds: 60,          },        },      },    },  },}
[/code]

`plugins.entries.firecrawl.config.webFetch.apiKey` mendukung objek SecretRef. Konfigurasi legacy `tools.web.fetch.firecrawl.*` dimigrasikan otomatis oleh `openclaw doctor --fix`.

Perilaku runtime saat ini:

  * `tools.web.fetch.provider` memilih penyedia fallback pengambilan secara eksplisit.
  * Jika `provider` dihilangkan, OpenClaw mendeteksi otomatis penyedia web-fetch pertama yang siap dari kredensial yang tersedia. `web_fetch` non-sandbox dapat menggunakan plugin terpasang yang mendeklarasikan `contracts.webFetchProviders` dan mendaftarkan penyedia yang cocok pada runtime. Saat ini penyedia bawaan adalah Firecrawl.
  * Panggilan `web_fetch` yang di-sandbox tetap terbatas pada penyedia bawaan.
  * Jika Readability dinonaktifkan, `web_fetch` langsung melewati ke fallback penyedia yang dipilih. Jika tidak ada penyedia yang tersedia, alat ini gagal secara tertutup.


## Proxy env tepercaya

Jika deployment Anda mengharuskan `web_fetch` melewati proxy HTTP(S) keluar yang tepercaya, setel `tools.web.fetch.useTrustedEnvProxy: true`.

Dalam mode ini, OpenClaw tetap menerapkan pemeriksaan SSRF berbasis hostname sebelum mengirim permintaan, tetapi membiarkan proxy menyelesaikan DNS alih-alih melakukan pinning DNS lokal. Aktifkan ini hanya ketika proxy dikendalikan operator dan memberlakukan kebijakan keluar setelah resolusi DNS.

## Batasan dan keamanan

  * `maxChars` dibatasi ke `tools.web.fetch.maxCharsCap`
  * Body respons dibatasi pada `maxResponseBytes` sebelum parsing; respons yang terlalu besar dipotong dengan peringatan
  * Hostname privat/internal diblokir
  * `tools.web.fetch.ssrfPolicy.allowRfc2544BenchmarkRange` dan `tools.web.fetch.ssrfPolicy.allowIpv6UniqueLocalRange` adalah opt-in sempit untuk stack proxy fake-IP tepercaya; biarkan tidak disetel kecuali proxy Anda memiliki rentang sintetis tersebut dan memberlakukan kebijakan tujuannya sendiri
  * Pengalihan diperiksa dan dibatasi oleh `maxRedirects`
  * `useTrustedEnvProxy` adalah opt-in eksplisit dan sebaiknya hanya diaktifkan untuk proxy yang dikendalikan operator yang tetap memberlakukan kebijakan keluar setelah resolusi DNS
  * `web_fetch` bersifat best-effort -- beberapa situs memerlukan [Peramban Web](</id/tools/browser>)


## Profil alat

Jika Anda menggunakan profil alat atau allowlist, tambahkan `web_fetch` atau `group:web`:

json5Copy code
[code]
    {  tools: {    allow: ["web_fetch"],    // or: allow: ["group:web"]  (includes web_fetch, web_search, and x_search)  },}
[/code]

## Terkait

  * [Pencarian Web](</id/tools/web>) \-- cari di web dengan beberapa penyedia
  * [Peramban Web](</id/tools/browser>) \-- automasi browser penuh untuk situs yang sangat bergantung pada JS
  * [Firecrawl](</id/tools/firecrawl>) \-- alat pencarian dan scrape Firecrawl


Was this useful?YesNo