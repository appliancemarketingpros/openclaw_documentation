---
title: Pencarian Perplexity
source_url: https://docs.openclaw.ai/id/tools/perplexity-search
scraped_at: 2026-05-25
---

OpenClaw mendukung Perplexity Search API sebagai penyedia `web_search`. API ini mengembalikan hasil terstruktur dengan bidang `title`, `url`, dan `snippet`.

Untuk kompatibilitas, OpenClaw juga mendukung penyiapan Perplexity Sonar/OpenRouter lama. Jika Anda menggunakan `OPENROUTER_API_KEY`, kunci `sk-or-...` di `plugins.entries.perplexity.config.webSearch.apiKey`, atau mengatur `plugins.entries.perplexity.config.webSearch.baseUrl` / `model`, penyedia beralih ke jalur chat-completions dan mengembalikan jawaban yang disintesis AI dengan sitasi, bukan hasil Search API terstruktur.

## Mendapatkan kunci API Perplexity

  1. Buat akun Perplexity di [perplexity.ai/settings/api](<https://www.perplexity.ai/settings/api>)
  2. Buat kunci API di dasbor
  3. Simpan kunci dalam konfigurasi atau atur `PERPLEXITY_API_KEY` di lingkungan Gateway.


## Kompatibilitas OpenRouter

Jika Anda sudah menggunakan OpenRouter untuk Perplexity Sonar, pertahankan `provider: "perplexity"` dan atur `OPENROUTER_API_KEY` di lingkungan Gateway, atau simpan kunci `sk-or-...` di `plugins.entries.perplexity.config.webSearch.apiKey`.

Kontrol kompatibilitas opsional:

  * `plugins.entries.perplexity.config.webSearch.baseUrl`
  * `plugins.entries.perplexity.config.webSearch.model`


## Contoh konfigurasi

### Perplexity Search API native

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "pplx-...",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

### Kompatibilitas OpenRouter / Sonar

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "<openrouter-api-key>",            baseUrl: "https://openrouter.ai/api/v1",            model: "perplexity/sonar-pro",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

## Tempat mengatur kunci

**Melalui konfigurasi:** jalankan `openclaw configure --section web`. Perintah ini menyimpan kunci di `~/.openclaw/openclaw.json` pada `plugins.entries.perplexity.config.webSearch.apiKey`. Bidang itu juga menerima objek SecretRef.

**Melalui lingkungan:** atur `PERPLEXITY_API_KEY` atau `OPENROUTER_API_KEY` di lingkungan proses Gateway. Untuk instalasi gateway, letakkan di `~/.openclaw/.env` (atau lingkungan layanan Anda). Lihat [Variabel env](</id/help/faq#env-vars-and-env-loading>).

Jika `provider: "perplexity"` dikonfigurasi dan SecretRef kunci Perplexity tidak terselesaikan tanpa fallback env, startup/reload gagal cepat.

## Parameter alat

Parameter ini berlaku untuk jalur Perplexity Search API native.

Kueri pencarian.

Jumlah hasil yang dikembalikan (1-10).

Kode negara ISO 2 huruf (mis. `US`, `DE`).

Kode bahasa ISO 639-1 (mis. `en`, `de`, `fr`).

Filter waktu - `day` adalah 24 jam.

Hanya hasil yang dipublikasikan setelah tanggal ini (`YYYY-MM-DD`).

Hanya hasil yang dipublikasikan sebelum tanggal ini (`YYYY-MM-DD`).

Array allowlist/denylist domain (maks. 20).

Total anggaran konten (maks. 1000000).

Batas token per halaman.

Untuk jalur kompatibilitas Sonar/OpenRouter lama:

  * `query`, `count`, dan `freshness` diterima
  * `count` hanya untuk kompatibilitas di sana; respons tetap berupa satu jawaban tersintesis dengan sitasi, bukan daftar N hasil
  * Filter khusus Search API seperti `country`, `language`, `date_after`, `date_before`, `domain_filter`, `max_tokens`, dan `max_tokens_per_page` mengembalikan error eksplisit


**Contoh:**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (allowlist)await web_search({  query: "climate research",  domain_filter: ["nature.com", "science.org", ".edu"],}); // Domain filtering (denylist - prefix with -)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],}); // More content extractionawait web_search({  query: "detailed AI research",  max_tokens: 50000,  max_tokens_per_page: 4096,});
[/code]

### Aturan filter domain

  * Maksimum 20 domain per filter
  * Tidak dapat mencampur allowlist dan denylist dalam permintaan yang sama
  * Gunakan prefiks `-` untuk entri denylist (mis., `["-reddit.com"]`)


## Catatan

  * Perplexity Search API mengembalikan hasil pencarian web terstruktur (`title`, `url`, `snippet`)
  * OpenRouter atau `plugins.entries.perplexity.config.webSearch.baseUrl` / `model` eksplisit mengalihkan Perplexity kembali ke chat completions Sonar untuk kompatibilitas
  * Kompatibilitas Sonar/OpenRouter mengembalikan satu jawaban tersintesis dengan sitasi, bukan baris hasil terstruktur
  * Hasil disimpan dalam cache selama 15 menit secara default (dapat dikonfigurasi melalui `cacheTtlMinutes`)


## Terkait

[**Web search overview** Semua penyedia dan aturan deteksi otomatis. ](</id/tools/web>) [**Brave search** Hasil terstruktur dengan filter negara dan bahasa. ](</id/tools/brave-search>) [**Exa search** Pencarian neural dengan ekstraksi konten. ](</id/tools/exa-search>) [**Perplexity Search API docs** Quickstart dan referensi resmi Perplexity Search API. ](<https://docs.perplexity.ai/docs/search/quickstart>)

Was this useful?YesNo