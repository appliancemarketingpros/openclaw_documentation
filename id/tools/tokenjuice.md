---
title: Tokenjuice
source_url: https://docs.openclaw.ai/id/tools/tokenjuice
scraped_at: 2026-05-25
---

`tokenjuice` adalah Plugin bawaan opsional yang memadatkan hasil tool `exec` dan `bash` yang berisik setelah perintah sudah dijalankan.

Plugin ini mengubah `tool_result` yang dikembalikan, bukan perintah itu sendiri. Tokenjuice tidak menulis ulang input shell, menjalankan ulang perintah, atau mengubah exit code.

Saat ini hal ini berlaku untuk eksekusi tertanam PI dan tool dinamis OpenClaw dalam harness app-server Codex. Tokenjuice mengait ke middleware hasil tool OpenClaw dan memangkas output sebelum dikembalikan ke sesi harness yang aktif.

## Aktifkan Plugin

Jalur cepat:

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled true
[/code]

Setara:

bashCopy code
[code]
    openclaw plugins enable tokenjuice
[/code]

OpenClaw sudah menyertakan plugin ini. Tidak ada langkah terpisah `plugins install` atau `tokenjuice install openclaw`.

Jika Anda lebih suka mengedit config secara langsung:

json5Copy code
[code]
    {  plugins: {    entries: {      tokenjuice: {        enabled: true,      },    },  },}
[/code]

## Apa yang diubah tokenjuice

  * Memadatkan hasil `exec` dan `bash` yang berisik sebelum dikembalikan ke sesi.
  * Menjaga eksekusi perintah asli tetap tidak tersentuh.
  * Mempertahankan pembacaan konten file yang persis dan perintah lain yang harus dibiarkan mentah oleh tokenjuice.
  * Tetap opt-in: nonaktifkan plugin jika Anda menginginkan output verbatim di mana-mana.


## Verifikasi bahwa plugin berfungsi

  1. Aktifkan plugin.
  2. Mulai sesi yang dapat memanggil `exec`.
  3. Jalankan perintah yang berisik seperti `git status`.
  4. Periksa bahwa hasil tool yang dikembalikan lebih pendek dan lebih terstruktur daripada output shell mentah.


## Nonaktifkan Plugin

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled false
[/code]

Atau:

bashCopy code
[code]
    openclaw plugins disable tokenjuice
[/code]

## Terkait

  * [Tool Exec](</id/tools/exec>)
  * [Tingkat thinking](</id/tools/thinking>)
  * [Mesin konteks](</id/concepts/context-engine>)


Was this useful?YesNo