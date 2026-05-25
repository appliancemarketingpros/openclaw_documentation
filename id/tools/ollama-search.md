---
title: Pencarian web Ollama
source_url: https://docs.openclaw.ai/id/tools/ollama-search
scraped_at: 2026-05-25
---

OpenClaw mendukung **Ollama Web Search** sebagai penyedia `web_search` bawaan. Ini menggunakan API pencarian web Ollama dan mengembalikan hasil terstruktur dengan judul, URL, dan cuplikan.

Untuk Ollama lokal atau yang di-host sendiri, penyiapan ini tidak memerlukan kunci API secara default. Ini memang memerlukan:

  * host Ollama yang dapat dijangkau dari OpenClaw
  * `ollama signin`


Untuk pencarian hosted langsung, atur URL dasar penyedia Ollama ke `https://ollama.com` dan sediakan `OLLAMA_API_KEY` yang valid.

## Penyiapan

* ### Start Ollama

Pastikan Ollama sudah terpasang dan berjalan.

* ### Sign in

Jalankan:

bashCopy code
[code]
    ollama signin
[/code]

* ### Choose Ollama Web Search

Jalankan:

bashCopy code
[code]
    openclaw configure --section web
[/code]

Lalu pilih **Ollama Web Search** sebagai penyedia.

Jika Anda sudah menggunakan Ollama untuk model, Ollama Web Search menggunakan kembali host yang sama yang telah dikonfigurasi.

## Konfigurasi

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

Override host Ollama opsional:

json5Copy code
[code]
    {  plugins: {    entries: {      ollama: {        config: {          webSearch: {            baseUrl: "http://ollama-host:11434",          },        },      },    },  },}
[/code]

Jika Anda sudah mengonfigurasi Ollama sebagai penyedia model, penyedia pencarian web dapat menggunakan kembali host tersebut:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434",      },    },  },}
[/code]

Penyedia model Ollama menggunakan `baseUrl` sebagai kunci kanonis. Penyedia pencarian web juga menghormati `baseURL` pada `models.providers.ollama` untuk kompatibilitas dengan contoh konfigurasi bergaya OpenAI SDK.

Jika tidak ada URL dasar Ollama yang ditetapkan secara eksplisit, OpenClaw menggunakan `http://127.0.0.1:11434`.

Jika host Ollama Anda mengharapkan autentikasi bearer, OpenClaw menggunakan kembali `models.providers.ollama.apiKey` (atau autentikasi penyedia berbasis env yang cocok) untuk permintaan ke host yang dikonfigurasi tersebut.

Ollama Web Search hosted langsung:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",      },    },  },  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

## Catatan

  * Tidak diperlukan kolom kunci API khusus pencarian web untuk penyedia ini.
  * Jika host Ollama dilindungi autentikasi, OpenClaw menggunakan kembali kunci API penyedia Ollama normal saat tersedia.
  * Jika `baseUrl` adalah `https://ollama.com`, OpenClaw memanggil `https://ollama.com/api/web_search` secara langsung dan mengirimkan kunci API Ollama yang dikonfigurasi sebagai autentikasi bearer.
  * Jika host yang dikonfigurasi tidak mengekspos pencarian web dan `OLLAMA_API_KEY` ditetapkan, OpenClaw dapat fallback ke `https://ollama.com/api/web_search` tanpa mengirimkan kunci env tersebut ke host lokal.
  * OpenClaw memperingatkan saat penyiapan jika Ollama tidak dapat dijangkau atau belum masuk, tetapi tidak memblokir pemilihan.
  * Deteksi otomatis runtime dapat fallback ke Ollama Web Search saat tidak ada penyedia berkredensial dengan prioritas lebih tinggi yang dikonfigurasi.
  * Host daemon Ollama lokal menggunakan endpoint proxy lokal `/api/experimental/web_search`, yang menandatangani dan meneruskan ke Ollama Cloud.
  * Host `https://ollama.com` menggunakan endpoint hosted publik `/api/web_search` secara langsung dengan autentikasi kunci API bearer.


## Terkait

  * [Ikhtisar Pencarian Web](</id/tools/web>) \-- semua penyedia dan deteksi otomatis
  * [Ollama](</id/providers/ollama>) \-- penyiapan model Ollama dan mode cloud/lokal


Was this useful?YesNo