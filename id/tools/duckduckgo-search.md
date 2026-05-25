---
title: Pencarian DuckDuckGo
source_url: https://docs.openclaw.ai/id/tools/duckduckgo-search
scraped_at: 2026-05-25
---

OpenClaw mendukung DuckDuckGo sebagai penyedia `web_search` **tanpa kunci**. Tidak diperlukan kunci API atau akun.

## Penyiapan

Tidak perlu kunci API - cukup atur DuckDuckGo sebagai penyedia Anda:

* ### Konfigurasikan

bashCopy code
[code]
    openclaw configure --section web# Select "duckduckgo" as the provider
[/code]

## Konfigurasi

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "duckduckgo",      },    },  },}
[/code]

Pengaturan tingkat Plugin opsional untuk wilayah dan SafeSearch:

json5Copy code
[code]
    {  plugins: {    entries: {      duckduckgo: {        config: {          webSearch: {            region: "us-en", // DuckDuckGo region code            safeSearch: "moderate", // "strict", "moderate", or "off"          },        },      },    },  },}
[/code]

## Parameter alat

Kueri pencarian.

Hasil yang akan dikembalikan (1-10).

Kode wilayah DuckDuckGo (mis. `us-en`, `uk-en`, `de-de`).

Tingkat SafeSearch.

Wilayah dan SafeSearch juga dapat diatur dalam konfigurasi Plugin (lihat di atas) - parameter alat menggantikan nilai konfigurasi per kueri.

## Catatan

  * **Tidak ada kunci API** \- langsung berfungsi, tanpa konfigurasi
  * **Eksperimental** \- mengumpulkan hasil dari halaman pencarian HTML non-JavaScript DuckDuckGo, bukan API atau SDK resmi
  * **Risiko tantangan bot** \- DuckDuckGo dapat menyajikan CAPTCHA atau memblokir permintaan saat penggunaan berat atau otomatis
  * **Penguraian HTML** \- hasil bergantung pada struktur halaman, yang dapat berubah tanpa pemberitahuan
  * **Urutan deteksi otomatis** \- DuckDuckGo adalah fallback tanpa kunci pertama (urutan 100) dalam deteksi otomatis. Penyedia berbasis API dengan kunci yang dikonfigurasi berjalan terlebih dahulu, lalu Ollama Web Search (urutan 110), lalu SearXNG (urutan 200)
  * **SafeSearch default ke moderate** saat tidak dikonfigurasi


## Terkait

  * [Ikhtisar Web Search](</id/tools/web>) \-- semua penyedia dan deteksi otomatis
  * [Brave Search](</id/tools/brave-search>) \-- hasil terstruktur dengan tingkat gratis
  * [Exa Search](</id/tools/exa-search>) \-- pencarian neural dengan ekstraksi konten


Was this useful?YesNo