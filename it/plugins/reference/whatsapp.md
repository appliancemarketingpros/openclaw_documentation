---
title: Plugin WhatsApp
source_url: https://docs.openclaw.ai/it/plugins/reference/whatsapp
scraped_at: 2026-05-25
---

# Plugin WhatsApp

Aggiunge la superficie del canale WhatsApp per inviare e ricevere messaggi OpenClaw.

## Distribuzione

  * Pacchetto: `@openclaw/whatsapp`
  * Percorso di installazione: npm; ClawHub


## Superficie

canali: whatsapp

## Nota di installazione per Windows

Su Windows, il Plugin WhatsApp richiede Git in `PATH` durante l'installazione npm perché una delle sue dipendenze Baileys/libsignal viene recuperata da un URL git. Installa Git per Windows, quindi riavvia la shell ed esegui di nuovo l'installazione:

powershellCopy code
[code]
    winget install --id Git.Git -e
[/code]

Anche Git portabile funziona se la sua directory `bin` è in `PATH`.

## Documentazione correlata

  * [whatsapp](</it/channels/whatsapp>)


Was this useful?YesNo