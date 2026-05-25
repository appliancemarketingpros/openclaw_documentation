---
title: Verzeichnis
source_url: https://docs.openclaw.ai/de/cli/directory
scraped_at: 2026-05-25
---

# `openclaw directory`

Verzeichnisabfragen für Kanäle, die dies unterstützen (Kontakte/Peers, Gruppen und „me“).

## Gemeinsame Flags

  * `--channel <name>`: Kanal-ID/-Alias (erforderlich, wenn mehrere Kanäle konfiguriert sind; automatisch, wenn nur einer konfiguriert ist)
  * `--account <id>`: Konto-ID (Standard: Kanalstandard)
  * `--json`: JSON ausgeben


## Hinweise

  * `directory` soll Ihnen helfen, IDs zu finden, die Sie in andere Befehle einfügen können (insbesondere `openclaw message send --target ...`).
  * Bei vielen Kanälen sind die Ergebnisse konfigurationsbasiert (Allowlisten / konfigurierte Gruppen) statt aus einem Live-Provider-Verzeichnis.
  * Installierte Kanal-Plugins können Verzeichnisunterstützung dennoch auslassen; in diesem Fall meldet der Befehl den nicht unterstützten Verzeichnisvorgang, statt das Plugin neu zu installieren.
  * Die Standardausgabe ist `id` (und manchmal `name`), durch einen Tabulator getrennt; verwenden Sie `--json` für Skripting.


## Ergebnisse mit `message send` verwenden

bashCopy code
[code]
    openclaw directory peers list --channel slack --query "U0"openclaw message send --channel slack --target user:U012ABCDEF --message "hello"
[/code]

## ID-Formate (nach Kanal)

  * WhatsApp: `+15551234567` (DM), `1234567890-1234567890@g.us` (Gruppe), `120363123456789@newsletter` (ausgehendes Ziel für Channel/Newsletter)
  * Telegram: `@username` oder numerische Chat-ID; Gruppen sind numerische IDs
  * Slack: `user:U…` und `channel:C…`
  * Discord: `user:<id>` und `channel:<id>`
  * Matrix (Plugin): `user:@user:server`, `room:!roomId:server` oder `#alias:server`
  * Microsoft Teams (Plugin): `user:<id>` und `conversation:<id>`
  * Zalo (Plugin): Benutzer-ID (Bot API)
  * Zalo Personal / `zalouser` (Plugin): Thread-ID (DM/Gruppe) aus `zca` (`me`, `friend list`, `group list`)


## Selbst („me“)

bashCopy code
[code]
    openclaw directory self --channel zalouser
[/code]

## Peers (Kontakte/Benutzer)

bashCopy code
[code]
    openclaw directory peers list --channel zalouseropenclaw directory peers list --channel zalouser --query "name"openclaw directory peers list --channel zalouser --limit 50
[/code]

## Gruppen

bashCopy code
[code]
    openclaw directory groups list --channel zalouseropenclaw directory groups list --channel zalouser --query "work"openclaw directory groups members --channel zalouser --group-id <id>
[/code]

## Verwandt

  * [CLI-Referenz](</de/cli>)


Was this useful?YesNo