---
title: WhatsApp-Plugin
source_url: https://docs.openclaw.ai/nl/plugins/reference/whatsapp
scraped_at: 2026-05-25
---

# WhatsApp Plugin

Voegt het WhatsApp-kanaaloppervlak toe voor het verzenden en ontvangen van OpenClaw-berichten.

## Distributie

  * Pakket: `@openclaw/whatsapp`
  * Installatieroute: npm; ClawHub


## Oppervlak

channels: whatsapp

## Installatieopmerking voor Windows

Op Windows heeft de WhatsApp Plugin Git op `PATH` nodig tijdens npm install, omdat een van de Baileys/libsignal-afhankelijkheden via een git-URL wordt opgehaald. Installeer Git for Windows, herstart daarna de shell en voer de installatie opnieuw uit:

powershellCopy code
[code]
    winget install --id Git.Git -e
[/code]

Portable Git werkt ook als de `bin`-directory ervan op `PATH` staat.

## Gerelateerde documentatie

  * [whatsapp](</nl/channels/whatsapp>)


Was this useful?YesNo