---
title: Plugin WhatsApp
source_url: https://docs.openclaw.ai/id/plugins/reference/whatsapp
scraped_at: 2026-05-25
---

# Plugin WhatsApp

Menambahkan permukaan saluran WhatsApp untuk mengirim dan menerima pesan OpenClaw.

## Distribusi

  * Paket: `@openclaw/whatsapp`
  * Rute instalasi: npm; ClawHub


## Permukaan

channels: whatsapp

## Catatan instalasi Windows

Di Windows, Plugin WhatsApp memerlukan Git pada `PATH` selama instalasi npm karena salah satu dependensi Baileys/libsignal-nya diambil dari URL git. Instal Git for Windows, lalu mulai ulang shell dan jalankan kembali instalasinya:

powershellCopy code
[code]
    winget install --id Git.Git -e
[/code]

Portable Git juga berfungsi jika direktori `bin`-nya ada di `PATH`.

## Dokumentasi terkait

  * [whatsapp](</id/channels/whatsapp>)


Was this useful?YesNo