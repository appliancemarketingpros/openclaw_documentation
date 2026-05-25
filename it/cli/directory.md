---
title: Cartella
source_url: https://docs.openclaw.ai/it/cli/directory
scraped_at: 2026-05-25
---

# `openclaw directory`

Ricerche nella directory per i canali che le supportano (contatti/peer, gruppi e "me").

## Flag comuni

  * `--channel <name>`: ID/alias del canale (obbligatorio quando sono configurati più canali; automatico quando ne è configurato uno solo)
  * `--account <id>`: ID account (predefinito: valore predefinito del canale)
  * `--json`: output JSON


## Note

  * `directory` serve ad aiutarti a trovare ID che puoi incollare in altri comandi (specialmente `openclaw message send --target ...`).
  * Per molti canali, i risultati sono basati sulla configurazione (allowlist / gruppi configurati) invece che su una directory live del provider.
  * I Plugin di canale installati possono comunque omettere il supporto alla directory; in quel caso il comando segnala l'operazione di directory non supportata invece di reinstallare il Plugin.
  * L'output predefinito è `id` (e talvolta `name`) separato da una tabulazione; usa `--json` per gli script.


## Uso dei risultati con `message send`

bashCopy code
[code]
    openclaw directory peers list --channel slack --query "U0"openclaw message send --channel slack --target user:U012ABCDEF --message "hello"
[/code]

## Formati ID (per canale)

  * WhatsApp: `+15551234567` (DM), `1234567890-1234567890@g.us` (gruppo), `120363123456789@newsletter` (target in uscita Canale/Newsletter)
  * Telegram: `@username` o ID numerico della chat; i gruppi sono ID numerici
  * Slack: `user:U…` e `channel:C…`
  * Discord: `user:<id>` e `channel:<id>`
  * Matrix (Plugin): `user:@user:server`, `room:!roomId:server` o `#alias:server`
  * Microsoft Teams (Plugin): `user:<id>` e `conversation:<id>`
  * Zalo (Plugin): ID utente (Bot API)
  * Zalo Personal / `zalouser` (Plugin): ID thread (DM/gruppo) da `zca` (`me`, `friend list`, `group list`)


## Sé ("me")

bashCopy code
[code]
    openclaw directory self --channel zalouser
[/code]

## Peer (contatti/utenti)

bashCopy code
[code]
    openclaw directory peers list --channel zalouseropenclaw directory peers list --channel zalouser --query "name"openclaw directory peers list --channel zalouser --limit 50
[/code]

## Gruppi

bashCopy code
[code]
    openclaw directory groups list --channel zalouseropenclaw directory groups list --channel zalouser --query "work"openclaw directory groups members --channel zalouser --group-id <id>
[/code]

## Correlati

  * [Riferimento CLI](</it/cli>)


Was this useful?YesNo