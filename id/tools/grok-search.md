---
title: Pencarian Grok
source_url: https://docs.openclaw.ai/id/tools/grok-search
scraped_at: 2026-05-25
---

OpenClaw mendukung Grok sebagai penyedia `web_search`, menggunakan respons xAI berbasis web untuk menghasilkan jawaban yang disintesis AI dan didukung hasil pencarian langsung dengan sitasi.

Kunci API xAI yang sama juga dapat mendukung alat bawaan `x_search` untuk pencarian postingan X (sebelumnya Twitter) dan alat `code_execution`. Jika Anda menyimpan kunci di bawah `plugins.entries.xai.config.webSearch.apiKey`, OpenClaw sekarang menggunakannya kembali sebagai fallback untuk penyedia model xAI bawaan juga.

Untuk metrik X tingkat postingan seperti repost, balasan, bookmark, atau tayangan, gunakan `x_search` dengan URL postingan atau ID status yang tepat alih-alih kueri pencarian yang luas.

## Onboarding dan konfigurasi

Jika Anda memilih **Grok** saat:

  * `openclaw onboard`
  * `openclaw configure --section web`


OpenClaw dapat menampilkan langkah lanjutan terpisah untuk mengaktifkan `x_search` dengan `XAI_API_KEY` yang sama. Langkah lanjutan itu:

  * hanya muncul setelah Anda memilih Grok untuk `web_search`
  * bukan pilihan penyedia pencarian web tingkat atas yang terpisah
  * dapat secara opsional mengatur model `x_search` dalam alur yang sama


Jika Anda melewatinya, Anda dapat mengaktifkan atau mengubah `x_search` nanti di konfigurasi.

## Dapatkan kunci API

* ### Buat kunci

Dapatkan kunci API dari [xAI](<https://console.x.ai/>).

* ### Simpan kunci

Atur `XAI_API_KEY` di lingkungan Gateway, atau konfigurasi melalui:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## Konfigurasi

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          webSearch: {            apiKey: "xai-...", // optional if XAI_API_KEY is set            baseUrl: "https://api.x.ai/v1", // optional Responses API proxy/base URL override          },        },      },    },  },  tools: {    web: {      search: {        provider: "grok",      },    },  },}
[/code]

**Alternatif lingkungan:** atur `XAI_API_KEY` di lingkungan Gateway. Untuk instalasi gateway, letakkan di `~/.openclaw/.env`.

## Cara kerjanya

Grok menggunakan respons xAI berbasis web untuk menyintesis jawaban dengan sitasi inline, mirip dengan pendekatan grounding Google Search milik Gemini.

## Parameter yang didukung

Pencarian Grok mendukung `query`.

`count` diterima untuk kompatibilitas `web_search` bersama, tetapi Grok tetap mengembalikan satu jawaban tersintesis dengan sitasi, bukan daftar N hasil.

Filter khusus penyedia saat ini tidak didukung.

Grok menggunakan timeout default khusus penyedia selama 60 detik karena pencarian xAI Responses berbasis web dapat berjalan lebih lama daripada default `web_search` bersama. Atur `tools.web.search.timeoutSeconds` untuk menggantinya.

## Penggantian URL dasar

Atur `plugins.entries.xai.config.webSearch.baseUrl` saat pencarian web Grok harus dirutekan melalui proksi operator atau endpoint Responses yang kompatibel dengan xAI. OpenClaw memposting ke `<baseUrl>/responses` setelah memangkas garis miring di akhir. `x_search` menggunakan fallback `webSearch.baseUrl` yang sama kecuali `plugins.entries.xai.config.xSearch.baseUrl` diatur.

## Terkait

  * [Ikhtisar Pencarian Web](</id/tools/web>) \-- semua penyedia dan deteksi otomatis
  * [x_search di Pencarian Web](</id/tools/web#x_search>) \-- pencarian X kelas utama melalui xAI
  * [Pencarian Gemini](</id/tools/gemini-search>) \-- jawaban yang disintesis AI melalui grounding Google


Was this useful?YesNo