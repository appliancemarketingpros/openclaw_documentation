---
title: Pencarian Exa
source_url: https://docs.openclaw.ai/id/tools/exa-search
scraped_at: 2026-05-25
---

OpenClaw mendukung [Exa AI](<https://exa.ai/>) sebagai penyedia `web_search`. Exa menawarkan mode pencarian neural, kata kunci, dan hibrida dengan ekstraksi konten bawaan (sorotan, teks, ringkasan).

## Dapatkan API key

* ### Buat akun

Daftar di [exa.ai](<https://exa.ai/>) dan buat API key dari dashboard Anda.

* ### Simpan kunci

Atur `EXA_API_KEY` di lingkungan Gateway, atau konfigurasikan melalui:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## Konfigurasi

json5Copy code
[code]
    {  plugins: {    entries: {      exa: {        config: {          webSearch: {            apiKey: "exa-...", // optional if EXA_API_KEY is set            baseUrl: "https://api.exa.ai", // optional; OpenClaw appends /search          },        },      },    },  },  tools: {    web: {      search: {        provider: "exa",      },    },  },}
[/code]

**Alternatif lingkungan:** atur `EXA_API_KEY` di lingkungan Gateway. Untuk instalasi gateway, letakkan di `~/.openclaw/.env`.

## Penggantian URL dasar

Atur `plugins.entries.exa.config.webSearch.baseUrl` ketika permintaan pencarian Exa harus melewati proxy yang kompatibel atau endpoint Exa alternatif. OpenClaw menormalkan host polos dengan menambahkan `https://` di depan dan menambahkan `/search` kecuali path sudah berakhir di sana. Endpoint yang diselesaikan disertakan dalam kunci cache pencarian, sehingga hasil dari endpoint Exa yang berbeda tidak dibagikan.

## Parameter tool

Kueri pencarian.

Hasil yang akan dikembalikan (1–100).

Mode pencarian.

Filter waktu.

Hasil setelah tanggal ini (`YYYY-MM-DD`).

Hasil sebelum tanggal ini (`YYYY-MM-DD`).

Opsi ekstraksi konten (lihat di bawah).

### Ekstraksi konten

Exa dapat mengembalikan konten yang diekstrak bersama hasil pencarian. Berikan objek `contents` untuk mengaktifkan:

javascriptCopy code
[code]
    await web_search({  query: "transformer architecture explained",  type: "neural",  contents: {    text: true, // full page text    highlights: { numSentences: 3 }, // key sentences    summary: true, // AI summary  },});
[/code]

Opsi contents | Tipe | Deskripsi  
---|---|---  
`text` | `boolean | { maxCharacters }` | Ekstrak teks halaman penuh  
`highlights` | `boolean | { maxCharacters, query, numSentences, highlightsPerUrl }` | Ekstrak kalimat kunci  
`summary` | `boolean | { query }` | Ringkasan yang dihasilkan AI  
  
### Mode pencarian

Mode | Deskripsi  
---|---  
`auto` | Exa memilih mode terbaik (default)  
`neural` | Pencarian semantik/berbasis makna  
`fast` | Pencarian kata kunci cepat  
`deep` | Pencarian mendalam yang menyeluruh  
`deep-reasoning` | Pencarian mendalam dengan penalaran  
`instant` | Hasil tercepat  
  
## Catatan

  * Jika tidak ada opsi `contents` yang diberikan, Exa menggunakan default `{ highlights: true }` sehingga hasil menyertakan cuplikan kalimat kunci
  * Hasil mempertahankan field `highlightScores` dan `summary` dari respons API Exa jika tersedia
  * Deskripsi hasil diselesaikan dari sorotan terlebih dahulu, lalu ringkasan, lalu teks penuh — mana pun yang tersedia
  * `freshness` dan `date_after`/`date_before` tidak dapat digabungkan — gunakan satu mode filter waktu
  * Hingga 100 hasil dapat dikembalikan per kueri (tunduk pada batas tipe pencarian Exa)
  * Hasil di-cache selama 15 menit secara default (dapat dikonfigurasi melalui `cacheTtlMinutes`)
  * Exa adalah integrasi API resmi dengan respons JSON terstruktur


## Terkait

  * [Ikhtisar Web Search](</id/tools/web>) \-- semua penyedia dan deteksi otomatis
  * [Brave Search](</id/tools/brave-search>) \-- hasil terstruktur dengan filter negara/bahasa
  * [Perplexity Search](</id/tools/perplexity-search>) \-- hasil terstruktur dengan pemfilteran domain


Was this useful?YesNo