---
title: Verwijdering van BlueBubbles en het imsg-pad voor iMessage
source_url: https://docs.openclaw.ai/nl/announcements/bluebubbles-imessage
scraped_at: 2026-05-25
---

# Verwijdering van BlueBubbles en het imsg iMessage-pad

OpenClaw levert het BlueBubbles-kanaal niet meer mee. Ondersteuning voor iMessage loopt nu via de gebundelde `imessage` Plugin, die [`imsg`](<https://github.com/steipete/imsg>) lokaal of via een SSH-wrapper start en JSON-RPC via stdin/stdout gebruikt.

Als je configuratie nog `channels.bluebubbles` bevat, migreer dit dan naar `channels.imessage`. De oude docs-URL `/channels/bluebubbles` verwijst door naar [Overstappen vanaf BlueBubbles](</nl/channels/imessage-from-bluebubbles>), met de volledige vertaaltabel voor configuratie en de checklist voor de overstap.

## Wat is er veranderd

  * Er is geen BlueBubbles HTTP-server, Webhook-route, REST-wachtwoord of BlueBubbles Plugin-runtime in het ondersteunde OpenClaw iMessage-pad.
  * OpenClaw leest en volgt Berichten via `imsg` op de Mac waarop Messages.app is ingelogd.
  * Basisfuncties voor verzenden, ontvangen, geschiedenis en media gebruiken de normale `imsg`-oppervlakken en macOS-machtigingen.
  * Geavanceerde acties zoals antwoorden in threads, tapbacks, bewerken, verzenden ongedaan maken, effecten, leesbewijzen, typindicatoren en groepsbeheer vereisen `imsg launch` met de private API-bridge beschikbaar.
  * Linux- en Windows-gateways kunnen iMessage nog steeds gebruiken door `channels.imessage.cliPath` in te stellen op een SSH-wrapper die `imsg` uitvoert op de ingelogde Mac.


## Wat je moet doen

  1. Installeer en verifieer `imsg` op de Berichten-Mac:

bashCopy code
[code]brew install steipete/tap/imsgimsg --versionimsg chats --limit 3imsg rpc --help
[/code]

  2. Verleen Volledige schijftoegang en Automatisering-machtigingen aan de procescontext die `imsg` en OpenClaw uitvoert.

  3. Vertaal de oude configuratie:

json5Copy code
[code]{  channels: {    imessage: {      enabled: true,      cliPath: "/opt/homebrew/bin/imsg",      dmPolicy: "pairing",      allowFrom: ["+15555550123"],      groupPolicy: "allowlist",      groupAllowFrom: ["+15555550123"],      groups: {        "*": { requireMention: true },      },      includeAttachments: true,    },  },}
[/code]

  4. Herstart de Gateway en verifieer:

bashCopy code
[code]openclaw channels status --probe
[/code]

  5. Test DM's, groepen, bijlagen en alle private API-acties waarvan je afhankelijk bent voordat je je oude BlueBubbles-server verwijdert.


## Migratie-opmerkingen

  * `channels.bluebubbles.serverUrl` en `channels.bluebubbles.password` hebben geen iMessage-equivalent.
  * `channels.bluebubbles.allowFrom`, `groupAllowFrom`, `groups`, `includeAttachments`, bijlageroots, groottelimieten voor media, chunking en actie-schakelaars hebben iMessage-equivalenten.
  * `channels.imessage.includeAttachments` staat nog steeds standaard uit. Stel dit expliciet in als je verwacht dat binnenkomende foto's, spraakmemo's, video's of bestanden de agent bereiken.
  * Met `groupPolicy: "allowlist"` kopieer je het oude `groups`-blok, inclusief een eventuele wildcard-vermelding `"*"`. Toestaanlijsten voor groepsafzenders en het groepsregister zijn afzonderlijke poorten.
  * ACP-bindingen die overeenkwamen met `channel: "bluebubbles"` moeten worden gewijzigd naar `channel: "imessage"`.
  * Oude BlueBubbles-sessiesleutels worden geen iMessage-sessiesleutels. Koppelingsgoedkeuringen worden per handle overgenomen, maar gespreksgeschiedenis onder BlueBubbles-sessiesleutels niet.


## Zie ook

  * [Overstappen vanaf BlueBubbles](</nl/channels/imessage-from-bluebubbles>)
  * [iMessage](</nl/channels/imessage>)
  * [Configuratiereferentie - iMessage](</nl/gateway/config-channels#imessage>)


Was this useful?YesNo