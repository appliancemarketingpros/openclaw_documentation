---
title: Plugin WhatsApp
source_url: https://docs.openclaw.ai/fr/plugins/reference/whatsapp
scraped_at: 2026-05-25
---

# Plugin WhatsApp

Ajoute la surface de canal WhatsApp pour l’envoi et la réception de messages OpenClaw.

## Distribution

  * Paquet : `@openclaw/whatsapp`
  * Mode d’installation : npm ; ClawHub


## Surface

channels: whatsapp

## Note d’installation sous Windows

Sous Windows, le Plugin WhatsApp a besoin que Git soit dans le `PATH` pendant l’installation npm, car l’une de ses dépendances Baileys/libsignal est récupérée depuis une URL git. Installez Git for Windows, puis redémarrez le shell et relancez l’installation :

powershellCopy code
[code]
    winget install --id Git.Git -e
[/code]

Portable Git fonctionne également si son répertoire `bin` est dans le `PATH`.

## Documentation associée

  * [whatsapp](</fr/channels/whatsapp>)


Was this useful?YesNo