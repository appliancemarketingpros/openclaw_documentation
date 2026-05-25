---
title: Perplexity
source_url: https://docs.openclaw.ai/id/providers/perplexity-provider
scraped_at: 2026-05-25
---

Plugin Perplexity menyediakan kemampuan pencarian web melalui Perplexity Search API atau Perplexity Sonar melalui OpenRouter.

Properti | Nilai  
---|---  
Jenis | Penyedia pencarian web (bukan penyedia model)  
Autentikasi | `PERPLEXITY_API_KEY` (langsung) atau `OPENROUTER_API_KEY` (melalui OpenRouter)  
Jalur konfigurasi | `plugins.entries.perplexity.config.webSearch.apiKey`  
  
## Mulai

* ### Atur kunci API

Jalankan alur konfigurasi pencarian web interaktif:

bashCopy code
[code]
    openclaw configure --section web
[/code]

Atau atur kunci secara langsung:

bashCopy code
[code]
    openclaw config set plugins.entries.perplexity.config.webSearch.apiKey "pplx-xxxxxxxxxxxx"
[/code]

* ### Mulai mencari

Agen akan otomatis menggunakan Perplexity untuk pencarian web setelah kunci dikonfigurasi. Tidak diperlukan langkah tambahan.

## Mode pencarian

Plugin memilih transport secara otomatis berdasarkan prefiks kunci API:

### API Perplexity asli (pplx-)

Saat kunci Anda dimulai dengan `pplx-`, OpenClaw menggunakan Perplexity Search API asli. Transport ini mengembalikan hasil terstruktur dan mendukung filter domain, bahasa, dan tanggal (lihat opsi pemfilteran di bawah).

### OpenRouter / Sonar (sk-or-)

Saat kunci Anda dimulai dengan `sk-or-`, OpenClaw merutekan melalui OpenRouter menggunakan model Perplexity Sonar. Transport ini mengembalikan jawaban yang disintesis AI dengan sitasi.

Prefiks kunci | Transport | Fitur  
---|---|---  
`pplx-` | Perplexity Search API asli | Hasil terstruktur, filter domain/bahasa/tanggal  
`sk-or-` | OpenRouter (Sonar) | Jawaban yang disintesis AI dengan sitasi  
  
## Pemfilteran API asli

Saat menggunakan API Perplexity asli, pencarian mendukung filter berikut:

Filter | Deskripsi | Contoh  
---|---|---  
Negara | Kode negara 2 huruf | `us`, `de`, `jp`  
Bahasa | Kode bahasa ISO 639-1 | `en`, `fr`, `zh`  
Rentang tanggal | Jendela keterkinian | `day`, `week`, `month`, `year`  
Filter domain | Daftar izinkan atau daftar tolak (maks 20 domain) | `example.com`  
Anggaran konten | Batas token per respons / per halaman | `max_tokens`, `max_tokens_per_page`  
  
## Konfigurasi lanjutan

Variabel lingkungan untuk proses daemon

Jika OpenClaw Gateway berjalan sebagai daemon (launchd/systemd), pastikan `PERPLEXITY_API_KEY` tersedia untuk proses tersebut.

Penyiapan proksi OpenRouter

Jika Anda lebih memilih merutekan pencarian Perplexity melalui OpenRouter, atur `OPENROUTER_API_KEY` (prefiks `sk-or-`) sebagai pengganti kunci Perplexity asli. OpenClaw akan mendeteksi prefiks dan beralih ke transport Sonar secara otomatis.

## Terkait

[**Alat pencarian Perplexity** Cara agen menjalankan pencarian Perplexity dan menafsirkan hasil. ](</id/tools/perplexity-search>) [**Referensi konfigurasi** Referensi konfigurasi lengkap termasuk entri Plugin. ](</id/gateway/configuration-reference>)

Was this useful?YesNo