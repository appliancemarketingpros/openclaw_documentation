---
title: Pencarian SearXNG
source_url: https://docs.openclaw.ai/id/tools/searxng-search
scraped_at: 2026-05-25
---

OpenClaw mendukung [SearXNG](<https://docs.searxng.org/>) sebagai penyedia `web_search` **dihosting sendiri, tanpa kunci**. SearXNG adalah mesin metapencari sumber terbuka yang mengagregasi hasil dari Google, Bing, DuckDuckGo, dan sumber lain.

Keunggulan:

  * **Gratis dan tanpa batas** \-- tidak memerlukan kunci API atau langganan komersial
  * **Privasi / isolasi jaringan** \-- kueri tidak pernah keluar dari jaringan Anda
  * **Berfungsi di mana saja** \-- tidak ada batasan wilayah pada API pencarian komersial


## Penyiapan

* ### Run a SearXNG instance

bashCopy code
[code]
    docker run -d -p 8888:8080 searxng/searxng
[/code]

Atau gunakan deployment SearXNG yang sudah ada dan dapat Anda akses. Lihat [dokumentasi SearXNG](<https://docs.searxng.org/>) untuk penyiapan produksi.

* ### Configure

bashCopy code
[code]
    openclaw configure --section web# Select "searxng" as the provider
[/code]

Atau atur env var dan biarkan deteksi otomatis menemukannya:

bashCopy code
[code]
    export SEARXNG_BASE_URL="http://localhost:8888"
[/code]

## Konfigurasi

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "searxng",      },    },  },}
[/code]

Pengaturan tingkat Plugin untuk instans SearXNG:

json5Copy code
[code]
    {  plugins: {    entries: {      searxng: {        config: {          webSearch: {            baseUrl: "http://localhost:8888",            categories: "general,news", // optional            language: "en", // optional          },        },      },    },  },}
[/code]

Kolom `baseUrl` juga menerima objek SecretRef.

Aturan transport:

  * `https://` berfungsi untuk host SearXNG publik atau privat
  * `http://` hanya diterima untuk host jaringan privat tepercaya atau loopback
  * host SearXNG publik harus menggunakan `https://`
  * host privat/internal menggunakan pelindung jaringan yang dihosting sendiri; host `https://` publik tetap berada pada pelindung pencarian web yang ketat dan tidak dapat mengalihkan ke alamat privat


## Variabel lingkungan

Atur `SEARXNG_BASE_URL` sebagai alternatif konfigurasi:

bashCopy code
[code]
    export SEARXNG_BASE_URL="http://localhost:8888"
[/code]

Saat `SEARXNG_BASE_URL` diatur dan tidak ada penyedia eksplisit yang dikonfigurasi, deteksi otomatis memilih SearXNG secara otomatis (dengan prioritas terendah -- penyedia berbasis API apa pun dengan kunci akan dipilih lebih dulu).

## Referensi konfigurasi Plugin

Kolom | Deskripsi  
---|---  
`baseUrl` | URL dasar instans SearXNG Anda (wajib)  
`categories` | Kategori yang dipisahkan koma seperti `general`, `news`, atau `science`  
`language` | Kode bahasa untuk hasil seperti `en`, `de`, atau `fr`  
  
## Catatan

  * **API JSON** \-- menggunakan endpoint asli SearXNG `format=json`, bukan scraping HTML
  * **URL hasil gambar** \-- hasil kategori gambar menyertakan `img_src` saat SearXNG mengembalikan URL gambar langsung
  * **Tanpa kunci API** \-- berfungsi dengan instans SearXNG apa pun langsung dari awal
  * **Validasi URL dasar** \-- `baseUrl` harus berupa URL `http://` atau `https://` yang valid; host publik harus menggunakan `https://`
  * **Pelindung jaringan** \-- endpoint SearXNG privat/internal memilih untuk mengaktifkan akses jaringan privat; endpoint SearXNG `https://` publik mempertahankan perlindungan SSRF yang ketat
  * **Urutan deteksi otomatis** \-- SearXNG diperiksa terakhir (urutan 200) dalam deteksi otomatis. Penyedia berbasis API dengan kunci yang dikonfigurasi berjalan lebih dulu, lalu DuckDuckGo (urutan 100), lalu Ollama Web Search (urutan 110)
  * **Dihosting sendiri** \-- Anda mengendalikan instans, kueri, dan mesin pencari upstream
  * **Kategori** default ke `general` saat tidak dikonfigurasi
  * **Fallback kategori** \-- jika permintaan kategori non-`general` berhasil tetapi mengembalikan nol hasil, OpenClaw mencoba ulang kueri yang sama sekali lagi dengan `general` sebelum mengembalikan kumpulan hasil kosong


## Terkait

  * [Ikhtisar Web Search](</id/tools/web>) \-- semua penyedia dan deteksi otomatis
  * [DuckDuckGo Search](</id/tools/duckduckgo-search>) \-- fallback tanpa kunci lainnya
  * [Brave Search](</id/tools/brave-search>) \-- hasil terstruktur dengan tingkat gratis


Was this useful?YesNo