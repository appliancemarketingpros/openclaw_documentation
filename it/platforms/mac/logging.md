---
title: Registrazione dei log di macOS
source_url: https://docs.openclaw.ai/it/platforms/mac/logging
scraped_at: 2026-05-25
---

# Logging (macOS)

## Log diagnostico su file a rotazione (pannello Debug)

OpenClaw instrada i log dell'app macOS tramite swift-log (logging unificato per impostazione predefinita) e può scrivere su disco un log locale su file, con rotazione, quando serve un'acquisizione persistente.

  * Verbosità: **pannello Debug → Log → Logging dell'app → Verbosità**
  * Abilita: **pannello Debug → Log → Logging dell'app → "Scrivi log diagnostico a rotazione (JSONL)"**
  * Posizione: `~/Library/Logs/OpenClaw/diagnostics.jsonl` (ruota automaticamente; i file vecchi hanno suffissi `.1`, `.2`, …)
  * Cancella: **pannello Debug → Log → Logging dell'app → "Cancella"**


Note:

  * È **disattivato per impostazione predefinita**. Abilitalo solo durante il debug attivo.
  * Tratta il file come sensibile; non condividerlo senza revisione.


## Dati privati del logging unificato su macOS

Il logging unificato redige la maggior parte dei payload a meno che un sottosistema non attivi `privacy -off`. Secondo l'articolo di Peter sulle [bizzarrie della privacy del logging](<https://steipete.me/posts/2025/logging-privacy-shenanigans>) su macOS (2025), questa impostazione è controllata da un plist in `/Library/Preferences/Logging/Subsystems/` indicizzato per nome del sottosistema. Solo le nuove voci di log recepiscono il flag, quindi abilitalo prima di riprodurre un problema.

## Abilitare per OpenClaw (`ai.openclaw`)

  * Scrivi prima il plist in un file temporaneo, poi installalo atomicamente come root:

bashCopy code
[code]
    cat <<'EOF' >/tmp/ai.openclaw.plist<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>    <key>DEFAULT-OPTIONS</key>    <dict>        <key>Enable-Private-Data</key>        <true/>    </dict></dict></plist>EOFsudo install -m 644 -o root -g wheel /tmp/ai.openclaw.plist /Library/Preferences/Logging/Subsystems/ai.openclaw.plist
[/code]

  * Non è richiesto alcun riavvio; logd rileva rapidamente il file, ma solo le nuove righe di log includeranno i payload privati.
  * Visualizza l'output più ricco con l'helper esistente, ad esempio `./scripts/clawlog.sh --category WebChat --last 5m`.


## Disabilitare dopo il debug

  * Rimuovi l'override: `sudo rm /Library/Preferences/Logging/Subsystems/ai.openclaw.plist`.
  * Facoltativamente esegui `sudo log config --reload` per forzare logd a scartare subito l'override.
  * Ricorda che questa superficie può includere numeri di telefono e corpi dei messaggi; lascia il plist in posizione solo mentre hai attivamente bisogno del dettaglio aggiuntivo.


## Correlati

  * [app macOS](</it/platforms/macos>)
  * [Logging del Gateway](</it/gateway/logging>)


Was this useful?YesNo