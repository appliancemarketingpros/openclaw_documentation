---
title: Map
source_url: https://docs.openclaw.ai/nl/cli/directory
scraped_at: 2026-05-25
---

# `openclaw directory`

Directory-zoekacties voor kanalen die dit ondersteunen (contacten/peers, groepen en "me").

## Algemene vlaggen

  * `--channel <name>`: kanaal-id/alias (vereist wanneer meerdere kanalen zijn geconfigureerd; automatisch wanneer er maar één is geconfigureerd)
  * `--account <id>`: account-id (standaard: kanaalstandaard)
  * `--json`: voer JSON uit


## Opmerkingen

  * `directory` is bedoeld om je te helpen id's te vinden die je in andere commando's kunt plakken (vooral `openclaw message send --target ...`).
  * Voor veel kanalen zijn resultaten gebaseerd op configuratie (allowlists / geconfigureerde groepen) in plaats van op een live providerdirectory.
  * Geïnstalleerde kanaalplugins kunnen directory-ondersteuning nog steeds weglaten; in dat geval meldt het commando de niet-ondersteunde directorybewerking in plaats van de Plugin opnieuw te installeren.
  * Standaarduitvoer is `id` (en soms `name`), gescheiden door een tab; gebruik `--json` voor scripts.


## Resultaten gebruiken met `message send`

bashCopy code
[code]
    openclaw directory peers list --channel slack --query "U0"openclaw message send --channel slack --target user:U012ABCDEF --message "hello"
[/code]

## Id-indelingen (per kanaal)

  * WhatsApp: `+15551234567` (DM), `1234567890-1234567890@g.us` (groep), `120363123456789@newsletter` (uitgaand doel voor Channel/Newsletter)
  * Telegram: `@username` of numerieke chat-id; groepen zijn numerieke id's
  * Slack: `user:U…` en `channel:C…`
  * Discord: `user:<id>` en `channel:<id>`
  * Matrix (Plugin): `user:@user:server`, `room:!roomId:server`, of `#alias:server`
  * Microsoft Teams (Plugin): `user:<id>` en `conversation:<id>`
  * Zalo (Plugin): gebruikers-id (Bot API)
  * Zalo Personal / `zalouser` (Plugin): thread-id (DM/groep) van `zca` (`me`, `friend list`, `group list`)


## Zelf ("me")

bashCopy code
[code]
    openclaw directory self --channel zalouser
[/code]

## Peers (contacten/gebruikers)

bashCopy code
[code]
    openclaw directory peers list --channel zalouseropenclaw directory peers list --channel zalouser --query "name"openclaw directory peers list --channel zalouser --limit 50
[/code]

## Groepen

bashCopy code
[code]
    openclaw directory groups list --channel zalouseropenclaw directory groups list --channel zalouser --query "work"openclaw directory groups members --channel zalouser --group-id <id>
[/code]

## Gerelateerd

  * [CLI-referentie](</nl/cli>)


Was this useful?YesNo