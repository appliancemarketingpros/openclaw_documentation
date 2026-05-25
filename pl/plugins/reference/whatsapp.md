---
title: Plugin WhatsApp
source_url: https://docs.openclaw.ai/pl/plugins/reference/whatsapp
scraped_at: 2026-05-25
---

# Plugin WhatsApp

Dodaje interfejs kanału WhatsApp do wysyłania i odbierania wiadomości OpenClaw.

## Dystrybucja

  * Pakiet: `@openclaw/whatsapp`
  * Ścieżka instalacji: npm; ClawHub


## Interfejs

channels: whatsapp

## Uwaga dotycząca instalacji w Windows

W Windows plugin WhatsApp wymaga Git w `PATH` podczas instalacji npm, ponieważ jedna z jego zależności Baileys/libsignal jest pobierana z adresu URL git. Zainstaluj Git for Windows, następnie uruchom ponownie powłokę i ponownie uruchom instalację:

powershellCopy code
[code]
    winget install --id Git.Git -e
[/code]

Portable Git również działa, jeśli jego katalog `bin` znajduje się w `PATH`.

## Powiązana dokumentacja

  * [whatsapp](</pl/channels/whatsapp>)


Was this useful?YesNo