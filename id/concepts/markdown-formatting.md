---
title: Pemformatan Markdown
source_url: https://docs.openclaw.ai/id/concepts/markdown-formatting
scraped_at: 2026-05-25
---

OpenClaw memformat Markdown keluar dengan mengonversinya menjadi representasi perantara (IR) bersama sebelum merender output spesifik kanal. IR menjaga teks sumber tetap utuh sambil membawa rentang gaya/tautan sehingga pemotongan dan rendering dapat tetap konsisten di berbagai kanal.

## Tujuan

  * **Konsistensi:** satu langkah parse, beberapa renderer.
  * **Pemotongan aman:** pisahkan teks sebelum rendering sehingga pemformatan inline tidak pernah terputus di antara potongan.
  * **Kesesuaian kanal:** petakan IR yang sama ke Slack mrkdwn, HTML Telegram, dan rentang gaya Signal tanpa mem-parse ulang Markdown.


## Pipeline

  1. **Parse Markdown - > IR**
     * IR adalah teks biasa ditambah rentang gaya (bold/italic/strike/code/spoiler) dan rentang tautan.
     * Offset adalah unit kode UTF-16 agar rentang gaya Signal selaras dengan API-nya.
     * Tabel di-parse hanya saat kanal memilih ikut dalam konversi tabel.
  2. **Potong IR (format-first)**
     * Pemotongan terjadi pada teks IR sebelum rendering.
     * Pemformatan inline tidak terpisah di antara potongan; rentang dipotong per potongan.
  3. **Render per kanal**
     * **Slack:** token mrkdwn (bold/italic/strike/code), tautan sebagai `<url|label>`.
     * **Telegram:** tag HTML (`<b>`, `<i>`, `<s>`, `<code>`, `<pre><code>`, `<a href>`).
     * **Signal:** teks biasa + rentang `text-style`; tautan menjadi `label (url)` saat label berbeda.


## Contoh IR

Input Markdown:

markdownCopy code
[code]
    Hello **world** - see [docs](https://docs.openclaw.ai).
[/code]

IR (skematis):

jsonCopy code
[code]
    {  "text": "Hello world - see docs.",  "styles": [{ "start": 6, "end": 11, "style": "bold" }],  "links": [{ "start": 19, "end": 23, "href": "https://docs.openclaw.ai" }]}
[/code]

## Tempat penggunaannya

  * Adapter keluar Slack, Telegram, dan Signal merender dari IR.
  * Kanal lain (WhatsApp, iMessage, Microsoft Teams, Discord) masih menggunakan teks biasa atau aturan pemformatannya sendiri, dengan konversi tabel Markdown diterapkan sebelum pemotongan saat diaktifkan.


## Penanganan tabel

Tabel Markdown tidak didukung secara konsisten di berbagai klien chat. Gunakan `markdown.tables` untuk mengontrol konversi per kanal (dan per akun).

  * `code`: render tabel sebagai blok kode (default untuk sebagian besar kanal).
  * `bullets`: konversi setiap baris menjadi poin bullet (default untuk Matrix, Signal, dan WhatsApp).
  * `off`: nonaktifkan parsing dan konversi tabel; teks tabel mentah diteruskan.


Kunci konfigurasi:

yamlCopy code
[code]
    channels:  discord:    markdown:      tables: code    accounts:      work:        markdown:          tables: off
[/code]

## Aturan pemotongan

  * Batas potongan berasal dari adapter/konfigurasi kanal dan diterapkan ke teks IR.
  * Code fence dipertahankan sebagai satu blok dengan baris baru di akhir agar kanal merendernya dengan benar.
  * Prefiks daftar dan prefiks blockquote adalah bagian dari teks IR, sehingga pemotongan tidak memisahkan di tengah prefiks.
  * Gaya inline (bold/italic/strike/inline-code/spoiler) tidak pernah dipisahkan di antara potongan; renderer membuka ulang gaya di dalam setiap potongan.


Jika Anda memerlukan informasi lebih lanjut tentang perilaku pemotongan di berbagai kanal, lihat [Streaming + pemotongan](</id/concepts/streaming>).

## Kebijakan tautan

  * **Slack:** `[label](url)` -> `<url|label>`; URL polos tetap polos. Autolink dinonaktifkan selama parse untuk menghindari penautan ganda.
  * **Telegram:** `[label](url)` -> `<a href="url">label</a>` (mode parse HTML).
  * **Signal:** `[label](url)` -> `label (url)` kecuali label cocok dengan URL.


## Spoiler

Marker spoiler (`||spoiler||`) di-parse hanya untuk Signal, tempat marker tersebut dipetakan ke rentang gaya SPOILER. Kanal lain memperlakukannya sebagai teks biasa.

## Cara menambah atau memperbarui formatter kanal

  1. **Parse sekali:** gunakan helper bersama `markdownToIR(...)` dengan opsi yang sesuai kanal (autolink, gaya heading, prefiks blockquote).
  2. **Render:** implementasikan renderer dengan `renderMarkdownWithMarkers(...)` dan peta marker gaya (atau rentang gaya Signal).
  3. **Potong:** panggil `chunkMarkdownIR(...)` sebelum rendering; render setiap potongan.
  4. **Hubungkan adapter:** perbarui adapter keluar kanal agar menggunakan pemotong dan renderer baru.
  5. **Uji:** tambahkan atau perbarui pengujian format dan pengujian pengiriman keluar jika kanal menggunakan pemotongan.


## Hal umum yang perlu diwaspadai

  * Token kurung sudut Slack (`<@U123>`, `<#C123>`, `<https://...>`) harus dipertahankan; escape HTML mentah dengan aman.
  * HTML Telegram memerlukan escaping teks di luar tag untuk menghindari markup rusak.
  * Rentang gaya Signal bergantung pada offset UTF-16; jangan gunakan offset titik kode.
  * Pertahankan baris baru di akhir untuk blok kode berpagar agar marker penutup berada di barisnya sendiri.


## Terkait

[**Streaming dan pemotongan** Perilaku streaming keluar, batas potongan, dan pengiriman spesifik kanal. ](</id/concepts/streaming>) [**Prompt sistem** Apa yang dilihat model sebelum percakapan, termasuk file workspace yang disisipkan. ](</id/concepts/system-prompt>)

Was this useful?YesNo