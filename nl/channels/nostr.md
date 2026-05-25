---
title: Nostr
source_url: https://docs.openclaw.ai/nl/channels/nostr
scraped_at: 2026-05-25
---

**Status:** Optionele gebundelde Plugin (standaard uitgeschakeld totdat deze is geconfigureerd).

Nostr is een gedecentraliseerd protocol voor sociale netwerken. Dit kanaal stelt OpenClaw in staat versleutelde directe berichten (DM's) te ontvangen en te beantwoorden via NIP-04.

## Gebundelde Plugin

Huidige OpenClaw-releases leveren Nostr als gebundelde Plugin, dus normale verpakte builds hebben geen aparte installatie nodig.

### Oudere/aangepaste installaties

  * Onboarding (`openclaw onboard`) en `openclaw channels add` tonen Nostr nog steeds vanuit de gedeelde kanaalcatalogus.
  * Als je build gebundelde Nostr uitsluit, installeer dan het npm-pakket direct.

bashCopy code
[code]
    openclaw plugins install @openclaw/nostr
[/code]

Gebruik het kale pakket om de huidige officiele release-tag te volgen. Pin alleen een exacte versie wanneer je een reproduceerbare installatie nodig hebt.

Gebruik een lokale checkout (dev-workflows):

bashCopy code
[code]
    openclaw plugins install --link <path-to-local-nostr-plugin>
[/code]

Herstart de Gateway na het installeren of inschakelen van plugins.

### Niet-interactieve configuratie

bashCopy code
[code]
    openclaw channels add --channel nostr --private-key "$NOSTR_PRIVATE_KEY"openclaw channels add --channel nostr --private-key "$NOSTR_PRIVATE_KEY" --relay-urls "wss://relay.damus.io,wss://relay.primal.net"
[/code]

Gebruik `--use-env` om `NOSTR_PRIVATE_KEY` in de omgeving te houden in plaats van de sleutel in de config op te slaan.

## Snelle configuratie

  1. Genereer een Nostr-sleutelpaar (indien nodig):

bashCopy code
[code]
    # Using naknak key generate
[/code]

  2. Voeg toe aan config:

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",    },  },}
[/code]

  3. Exporteer de sleutel:

bashCopy code
[code]
    export NOSTR_PRIVATE_KEY="nsec1..."
[/code]

  4. Herstart de Gateway.


## Configuratiereferentie

Sleutel | Type | Standaard | Beschrijving  
---|---|---|---  
`privateKey` | string | vereist | Privesleutel in `nsec`\- of hex-indeling  
`relays` | string[] | `['wss://relay.damus.io', 'wss://nos.lol']` | Relay-URL's (WebSocket)  
`dmPolicy` | string | `pairing` | Toegangsbeleid voor DM's  
`allowFrom` | string[] | `[]` | Toegestane pubkeys van afzenders  
`enabled` | boolean | `true` | Kanaal inschakelen/uitschakelen  
`name` | string | - | Weergavenaam  
`profile` | object | - | NIP-01-profielmetadata  
  
## Profielmetadata

Profielgegevens worden gepubliceerd als een NIP-01 `kind:0`-event. Je kunt dit beheren vanuit de Control UI (Channels -> Nostr -> Profile) of direct instellen in config.

Voorbeeld:

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      profile: {        name: "openclaw",        displayName: "OpenClaw",        about: "Personal assistant DM bot",        picture: "https://example.com/avatar.png",        banner: "https://example.com/banner.png",        website: "https://example.com",        nip05: "openclaw@example.com",        lud16: "openclaw@example.com",      },    },  },}
[/code]

Opmerkingen:

  * Profiel-URL's moeten `https://` gebruiken.
  * Importeren vanuit relays voegt velden samen en behoudt lokale overschrijvingen.


## Toegangsbeheer

### DM-beleid

  * **pairing** (standaard): onbekende afzenders krijgen een koppelingscode.
  * **allowlist** : alleen pubkeys in `allowFrom` kunnen DM'en.
  * **open** : openbare inkomende DM's (vereist `allowFrom: ["*"]`).
  * **disabled** : negeer inkomende DM's.


Handhavingsopmerkingen:

  * Handtekeningen van inkomende events worden geverifieerd voor afzenderbeleid en NIP-04-ontsleuteling, zodat vervalste events vroeg worden geweigerd.
  * Koppelingsantwoorden worden verzonden zonder de oorspronkelijke DM-body te verwerken.
  * Inkomende DM's worden rate-limited en te grote payloads worden voor ontsleuteling gedropt.


### Voorbeeld van allowlist

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      dmPolicy: "allowlist",      allowFrom: ["npub1abc...", "npub1xyz..."],    },  },}
[/code]

## Sleutelindelingen

Geaccepteerde indelingen:

  * **Privesleutel:** `nsec...` of 64-tekens hex
  * **Pubkeys (`allowFrom`):** `npub...` of hex


## Relays

Standaarden: `relay.damus.io` en `nos.lol`.

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      relays: ["wss://relay.damus.io", "wss://relay.primal.net", "wss://nostr.wine"],    },  },}
[/code]

Tips:

  * Gebruik 2-3 relays voor redundantie.
  * Vermijd te veel relays (latentie, duplicatie).
  * Betaalde relays kunnen de betrouwbaarheid verbeteren.
  * Lokale relays zijn prima voor testen (`ws://localhost:7777`).


## Protocolondersteuning

NIP | Status | Beschrijving  
---|---|---  
NIP-01 | Ondersteund | Basis-eventindeling + profielmetadata  
NIP-04 | Ondersteund | Versleutelde DM's (`kind:4`)  
NIP-17 | Gepland | Gift-wrapped DM's  
NIP-44 | Gepland | Versleuteling met versies  
  
## Testen

### Lokale relay

bashCopy code
[code]
    # Start strfrydocker run -p 7777:7777 ghcr.io/hoytech/strfry
[/code]

json5Copy code
[code]
    {  channels: {    nostr: {      privateKey: "${NOSTR_PRIVATE_KEY}",      relays: ["ws://localhost:7777"],    },  },}
[/code]

### Handmatige test

  1. Noteer de bot-pubkey (npub) uit de logs.
  2. Open een Nostr-client (Damus, Amethyst, enz.).
  3. Stuur een DM naar de bot-pubkey.
  4. Controleer het antwoord.


## Problemen oplossen

### Ontvangt geen berichten

  * Controleer of de privesleutel geldig is.
  * Zorg dat relay-URL's bereikbaar zijn en `wss://` gebruiken (of `ws://` voor lokaal).
  * Bevestig dat `enabled` niet `false` is.
  * Controleer Gateway-logs op relay-verbindingsfouten.


### Verstuurt geen antwoorden

  * Controleer of de relay schrijfbewerkingen accepteert.
  * Controleer uitgaande connectiviteit.
  * Let op rate limits van relays.


### Dubbele antwoorden

  * Verwacht bij gebruik van meerdere relays.
  * Berichten worden ontdubbeld op event-ID; alleen de eerste levering triggert een antwoord.


## Beveiliging

  * Commit nooit privesleutels.
  * Gebruik omgevingsvariabelen voor sleutels.
  * Overweeg `allowlist` voor productiebots.
  * Handtekeningen worden geverifieerd voor afzenderbeleid, en afzenderbeleid wordt afgedwongen voor ontsleuteling, zodat vervalste events vroeg worden geweigerd en onbekende afzenders geen volledig cryptografisch werk kunnen afdwingen.


## Beperkingen (MVP)

  * Alleen directe berichten (geen groepschats).
  * Geen mediabijlagen.
  * Alleen NIP-04 (NIP-17 gift-wrap gepland).


## Gerelateerd

  * [Kanalenoverzicht](</nl/channels>) — alle ondersteunde kanalen
  * [Koppeling](</nl/channels/pairing>) — DM-authenticatie en koppelingsflow
  * [Groepen](</nl/channels/groups>) — gedrag van groepschats en mention-gating
  * [Kanaalroutering](</nl/channels/channel-routing>) — sessieroutering voor berichten
  * [Beveiliging](</nl/gateway/security>) — toegangsmodel en hardening


Was this useful?YesNo