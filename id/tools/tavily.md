---
title: Tavily
source_url: https://docs.openclaw.ai/id/tools/tavily
scraped_at: 2026-05-25
---

[Tavily](<https://tavily.com>) adalah API pencarian yang dirancang untuk aplikasi AI. OpenClaw mengeksposnya dalam dua cara:

  * sebagai penyedia `web_search` untuk alat pencarian generik
  * sebagai alat Plugin eksplisit: `tavily_search` dan `tavily_extract`


Tavily mengembalikan hasil terstruktur yang dioptimalkan untuk konsumsi LLM dengan kedalaman pencarian yang dapat dikonfigurasi, pemfilteran topik, filter domain, ringkasan jawaban yang dihasilkan AI, dan ekstraksi konten dari URL (termasuk halaman yang dirender JavaScript).

Properti | Nilai  
---|---  
Id Plugin | `tavily`  
Autentikasi | `TAVILY_API_KEY` atau config `apiKey`  
URL dasar | `https://api.tavily.com` (default)  
Alat bawaan | `tavily_search`, `tavily_extract`  
  
## Memulai

* ### Dapatkan kunci API

Buat akun Tavily di [tavily.com](<https://tavily.com>), lalu buat kunci API di dasbor.

* ### Konfigurasikan plugin dan penyedia

json5Copy code
[code]
    {  plugins: {    entries: {      tavily: {        enabled: true,        config: {          webSearch: {            apiKey: "tvly-...", // optional if TAVILY_API_KEY is set            baseUrl: "https://api.tavily.com",          },        },      },    },  },  tools: {    web: {      search: {        provider: "tavily",      },    },  },}
[/code]

* ### Verifikasi pencarian berjalan

Picu `web_search` dari agent mana pun, atau panggil `tavily_search` secara langsung.

## Referensi alat

### `tavily_search`

Gunakan ini ketika Anda menginginkan kontrol pencarian khusus Tavily, bukan `web_search` generik.

Parameter | Jenis | Batasan / default | Deskripsi  
---|---|---|---  
`query` | string | wajib | String kueri pencarian. Jaga agar di bawah 400 karakter.  
`search_depth` | enum | `basic` (default), `advanced` | `advanced` lebih lambat tetapi relevansinya lebih tinggi.  
`topic` | enum | `general` (default), `news`, `finance` | Filter berdasarkan keluarga topik.  
`max_results` | integer | 1-20 | Jumlah hasil.  
`include_answer` | boolean | default `false` | Sertakan ringkasan jawaban yang dihasilkan AI Tavily.  
`time_range` | enum | `day`, `week`, `month`, `year` | Filter hasil berdasarkan kebaruan.  
`include_domains` | array string | (tidak ada) | Hanya sertakan hasil dari domain-domain ini.  
`exclude_domains` | array string | (tidak ada) | Kecualikan hasil dari domain-domain ini.  
  
Tradeoff kedalaman pencarian:

Kedalaman | Kecepatan | Relevansi | Paling cocok untuk  
---|---|---|---  
`basic` | Lebih cepat | Tinggi | Kueri serbaguna (default).  
`advanced` | Lebih lambat | Tertinggi | Riset presisi dan pencarian fakta.  
  
### `tavily_extract`

Gunakan ini untuk mengekstrak konten bersih dari satu atau beberapa URL. Menangani halaman yang dirender JavaScript dan mendukung pemotongan berfokus kueri untuk ekstraksi yang ditargetkan.

Parameter | Jenis | Batasan / default | Deskripsi  
---|---|---|---  
`urls` | array string | wajib, 1-20 | URL untuk mengekstrak konten.  
`query` | string | (opsional) | Urutkan ulang potongan yang diekstrak berdasarkan relevansi terhadap kueri ini.  
`extract_depth` | enum | `basic` (default), `advanced` | Gunakan `advanced` untuk halaman yang berat JS, SPA, atau tabel dinamis.  
`chunks_per_source` | integer | 1-5; **membutuhkan`query`** | Potongan yang dikembalikan per URL. Error jika disetel tanpa `query`.  
`include_images` | boolean | default `false` | Sertakan URL gambar dalam hasil.  
  
Tradeoff kedalaman ekstraksi:

Kedalaman | Kapan digunakan  
---|---  
`basic` | Halaman sederhana. Coba ini terlebih dahulu.  
`advanced` | SPA yang dirender JS, konten dinamis, tabel.  
  
## Memilih alat yang tepat

Kebutuhan | Alat  
---|---  
Pencarian web cepat, tanpa opsi khusus | `web_search`  
Pencarian dengan kedalaman, topik, jawaban AI | `tavily_search`  
Ekstrak konten dari URL tertentu | `tavily_extract`  
  
## Konfigurasi lanjutan

Urutan resolusi kunci API

Klien Tavily mencari kunci API-nya dalam urutan ini:

  1. `plugins.entries.tavily.config.webSearch.apiKey` (diresolusikan melalui SecretRefs).
  2. `TAVILY_API_KEY` dari lingkungan Gateway.


`tavily_extract` memunculkan error penyiapan jika keduanya tidak ada.

URL dasar khusus

Timpa `plugins.entries.tavily.config.webSearch.baseUrl` jika Anda menyalurkan Tavily melalui proksi. Default-nya adalah `https://api.tavily.com`.

`chunks_per_source` membutuhkan `query`

`tavily_extract` menolak panggilan yang meneruskan `chunks_per_source` tanpa `query`. Tavily memeringkat potongan berdasarkan relevansi kueri, sehingga parameter tersebut tidak bermakna tanpa kueri.

## Terkait

[**Ringkasan Web Search** Semua penyedia dan aturan deteksi otomatis. ](</id/tools/web>) [**Firecrawl** Pencarian plus scraping dengan ekstraksi konten. ](</id/tools/firecrawl>) [**Exa Search** Pencarian neural dengan ekstraksi konten. ](</id/tools/exa-search>) [**Konfigurasi** Skema config lengkap untuk entri Plugin dan perutean alat. ](</id/gateway/configuration>)

Was this useful?YesNo