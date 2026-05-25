---
title: WhatsApp-Plugin
source_url: https://docs.openclaw.ai/de/plugins/reference/whatsapp
scraped_at: 2026-05-25
---

# WhatsApp-Plugin

Fügt die WhatsApp-Kanaloberfläche zum Senden und Empfangen von OpenClaw-Nachrichten hinzu.

## Distribution

  * Paket: `@openclaw/whatsapp`
  * Installationsweg: npm; ClawHub


## Oberfläche

channels: whatsapp

## Hinweis zur Windows-Installation

Unter Windows benötigt das WhatsApp-Plugin während der npm-Installation Git auf `PATH`, weil eine seiner Baileys/libsignal-Abhängigkeiten von einer Git-URL abgerufen wird. Installieren Sie Git for Windows, starten Sie dann die Shell neu und führen Sie die Installation erneut aus:

powershellCopy code
[code]
    winget install --id Git.Git -e
[/code]

Portable Git funktioniert ebenfalls, wenn sich sein `bin`-Verzeichnis auf `PATH` befindet.

## Zugehörige Dokumentation

  * [whatsapp](</de/channels/whatsapp>)


Was this useful?YesNo