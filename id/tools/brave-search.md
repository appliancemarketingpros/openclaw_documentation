---
title: Pencarian Brave
source_url: https://docs.openclaw.ai/id/tools/brave-search
scraped_at: 2026-05-25
---

OpenClaw mendukung Brave Search API sebagai penyedia `web_search`.

## Dapatkan kunci API

  1. Buat akun Brave Search API di <https://brave.com/search/api/>
  2. Di dasbor, pilih paket **Search** dan buat kunci API.
  3. Simpan kunci di konfigurasi atau atur `BRAVE_API_KEY` di lingkungan Gateway.


## Contoh konfigurasi

json5Copy code
[code]
    {  plugins: {    entries: {      brave: {        config: {          webSearch: {            apiKey: "BRAVE_API_KEY_HERE",            mode: "web", // or "llm-context"            baseUrl: "https://api.search.brave.com", // optional proxy/base URL override          },        },      },    },  },  tools: {    web: {      search: {        provider: "brave",        maxResults: 5,        timeoutSeconds: 30,      },    },  },}
[/code]

Pengaturan pencarian Brave khusus penyedia kini berada di bawah `plugins.entries.brave.config.webSearch.*`. `tools.web.search.apiKey` lama masih dimuat melalui shim kompatibilitas, tetapi itu bukan lagi jalur konfigurasi kanonis.

`webSearch.mode` mengontrol transport Brave:

  * `web` (default): pencarian web Brave normal dengan judul, URL, dan cuplikan
  * `llm-context`: Brave LLM Context API dengan potongan teks dan sumber yang sudah diekstrak untuk grounding


`webSearch.baseUrl` dapat mengarahkan permintaan Brave ke proxy atau gateway kompatibel Brave yang tepercaya. OpenClaw menambahkan `/res/v1/web/search` atau `/res/v1/llm/context` ke URL dasar yang dikonfigurasi dan menyimpan URL dasar di kunci cache. Endpoint publik harus menggunakan `https://`; `http://` hanya diterima untuk host proxy loopback atau jaringan privat yang tepercaya.

## Parameter alat

Kueri pencarian.

Jumlah hasil yang akan dikembalikan (1–10).

Kode negara ISO 2 huruf (mis. `US`, `DE`).

Kode bahasa ISO 639-1 untuk hasil pencarian (mis. `en`, `de`, `fr`).

Kode bahasa pencarian Brave (mis. `en`, `en-gb`, `zh-hans`).

Kode bahasa ISO untuk elemen UI.

Filter waktu — `day` adalah 24 jam.

Hanya hasil yang diterbitkan setelah tanggal ini (`YYYY-MM-DD`).

Hanya hasil yang diterbitkan sebelum tanggal ini (`YYYY-MM-DD`).

**Contoh:**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",});
[/code]

## Catatan

  * OpenClaw menggunakan paket Brave **Search**. Jika Anda memiliki langganan lama (mis. paket Free asli dengan 2.000 kueri/bulan), langganan itu tetap valid tetapi tidak menyertakan fitur yang lebih baru seperti LLM Context atau batas laju yang lebih tinggi.
  * Setiap paket Brave menyertakan **kredit gratis $5/bulan** (diperbarui). Paket Search berbiaya $5 per 1.000 permintaan, sehingga kredit tersebut mencakup 1.000 kueri/bulan. Atur batas penggunaan Anda di dasbor Brave untuk menghindari biaya tak terduga. Lihat [portal API Brave](<https://brave.com/search/api/>) untuk paket saat ini.
  * Paket Search menyertakan endpoint LLM Context dan hak inferensi AI. Menyimpan hasil untuk melatih atau menyetel model memerlukan paket dengan hak penyimpanan eksplisit. Lihat [Ketentuan Layanan](<https://api-dashboard.search.brave.com/terms-of-service>) Brave.
  * Mode `llm-context` mengembalikan entri sumber ber-grounding, bukan bentuk cuplikan pencarian web normal.
  * Mode `llm-context` mendukung `freshness` dan rentang `date_after` \+ `date_before` terbatas. Mode ini tidak mendukung `ui_lang`; `date_before` tanpa `date_after` ditolak karena Brave mengharuskan rentang freshness khusus menyertakan tanggal mulai dan akhir.
  * `ui_lang` harus menyertakan subtag wilayah seperti `en-US`.
  * Hasil di-cache selama 15 menit secara default (dapat dikonfigurasi melalui `cacheTtlMinutes`).
  * Nilai `webSearch.baseUrl` khusus disertakan dalam identitas cache Brave, sehingga respons khusus proxy tidak bertabrakan.
  * Aktifkan flag diagnostik `brave.http` untuk mencatat URL/parameter kueri permintaan Brave, status/waktu respons, serta peristiwa hit/miss/write cache pencarian saat memecahkan masalah. Flag ini tidak pernah mencatat kunci API atau isi respons, tetapi kueri pencarian bisa bersifat sensitif.


## Terkait

  * [Gambaran umum Web Search](</id/tools/web>) \-- semua penyedia dan deteksi otomatis
  * [Perplexity Search](</id/tools/perplexity-search>) \-- hasil terstruktur dengan pemfilteran domain
  * [Exa Search](</id/tools/exa-search>) \-- pencarian neural dengan ekstraksi konten


Was this useful?YesNo