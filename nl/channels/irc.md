---
title: IRC
source_url: https://docs.openclaw.ai/nl/channels/irc
scraped_at: 2026-05-25
---

Gebruik IRC wanneer je OpenClaw wilt gebruiken in klassieke kanalen (`#room`) en directe berichten. IRC wordt geleverd als een gebundelde Plugin, maar wordt geconfigureerd in de hoofdconfiguratie onder `channels.irc`.

## Snel starten

  1. Schakel IRC-configuratie in `~/.openclaw/openclaw.json` in.
  2. Stel minimaal het volgende in:

json5Copy code
[code]
    {  channels: {    irc: {      enabled: true,      host: "irc.example.com",      port: 6697,      tls: true,      nick: "openclaw-bot",      channels: ["#openclaw"],    },  },}
[/code]

Gebruik bij voorkeur een private IRC-server voor botcoördinatie. Als je bewust een publiek IRC-netwerk gebruikt, zijn veelvoorkomende keuzes Libera.Chat, OFTC en Snoonet. Vermijd voorspelbare publieke kanalen voor bot- of swarm-backchannelverkeer.

  3. Start/herstart de Gateway:

bashCopy code
[code]
    openclaw gateway run
[/code]

## Standaardbeveiliging

  * IRC gebruikt ruwe TCP/TLS-sockets buiten de door OpenClaw-operators beheerde forward-proxyroutering. Zet in implementaties die vereisen dat alle uitgaande verbindingen via die forward proxy lopen `channels.irc.enabled=false`, tenzij directe uitgaande IRC-verbindingen expliciet zijn goedgekeurd.
  * `channels.irc.dmPolicy` staat standaard op `"pairing"`.
  * `channels.irc.groupPolicy` staat standaard op `"allowlist"`.
  * Stel bij `groupPolicy="allowlist"` `channels.irc.groups` in om toegestane kanalen te definiëren.
  * Gebruik TLS (`channels.irc.tls=true`), tenzij je bewust transport in platte tekst accepteert.


## Toegangscontrole

Er zijn twee afzonderlijke "poorten" voor IRC-kanalen:

  1. **Kanaaltoegang** (`groupPolicy` \+ `groups`): of de bot berichten uit een kanaal überhaupt accepteert.
  2. **Afzendertoegang** (`groupAllowFrom` / per-kanaal `groups["#channel"].allowFrom`): wie de bot binnen dat kanaal mag activeren.


Configuratiesleutels:

  * DM-allowlist (DM-afzendertoegang): `channels.irc.allowFrom`
  * Groepsafzender-allowlist (kanaalafzendertoegang): `channels.irc.groupAllowFrom`
  * Per-kanaal instellingen (kanaal + afzender + vermeldingsregels): `channels.irc.groups["#channel"]`
  * `channels.irc.groupPolicy="open"` staat ongeconfigureerde kanalen toe (**standaard nog steeds gated op vermeldingen**)


Allowlist-vermeldingen moeten stabiele afzenderidentiteiten gebruiken (`nick!user@host`). Matching op alleen nick is veranderlijk en alleen ingeschakeld wanneer `channels.irc.dangerouslyAllowNameMatching: true`.

### Veelvoorkomende valkuil: `allowFrom` is voor DM's, niet voor kanalen

Als je logs ziet zoals:

  * `irc: drop group sender alice!ident@host (policy=allowlist)`


...betekent dit dat de afzender niet was toegestaan voor **groeps-/kanaalberichten**. Los dit op door:

  * `channels.irc.groupAllowFrom` in te stellen (globaal voor alle kanalen), of
  * per-kanaal afzender-allowlists in te stellen: `channels.irc.groups["#channel"].allowFrom`


Voorbeeld (sta iedereen in `#tuirc-dev` toe om met de bot te praten):

json5Copy code
[code]
    {  channels: {    irc: {      groupPolicy: "allowlist",      groups: {        "#tuirc-dev": { allowFrom: ["*"] },      },    },  },}
[/code]

## Antwoorden activeren (vermeldingen)

Zelfs als een kanaal is toegestaan (via `groupPolicy` \+ `groups`) en de afzender is toegestaan, gebruikt OpenClaw standaard **vermeldingsgating** in groepscontexten.

Dat betekent dat je logs kunt zien zoals `drop channel … (missing-mention)`, tenzij het bericht een vermeldingspatroon bevat dat overeenkomt met de bot.

Schakel vermeldingsgating voor dat kanaal uit om de bot in een IRC-kanaal te laten antwoorden **zonder dat een vermelding nodig is** :

json5Copy code
[code]
    {  channels: {    irc: {      groupPolicy: "allowlist",      groups: {        "#tuirc-dev": {          requireMention: false,          allowFrom: ["*"],        },      },    },  },}
[/code]

Of om **alle** IRC-kanalen toe te staan (zonder per-kanaal allowlist) en toch zonder vermeldingen te antwoorden:

json5Copy code
[code]
    {  channels: {    irc: {      groupPolicy: "open",      groups: {        "*": { requireMention: false, allowFrom: ["*"] },      },    },  },}
[/code]

## Beveiligingsopmerking (aanbevolen voor publieke kanalen)

Als je `allowFrom: ["*"]` toestaat in een publiek kanaal, kan iedereen de bot prompten. Beperk de tools voor dat kanaal om risico's te verminderen.

### Dezelfde tools voor iedereen in het kanaal

json5Copy code
[code]
    {  channels: {    irc: {      groups: {        "#tuirc-dev": {          allowFrom: ["*"],          tools: {            deny: ["group:runtime", "group:fs", "gateway", "nodes", "cron", "browser"],          },        },      },    },  },}
[/code]

### Verschillende tools per afzender (eigenaar krijgt meer rechten)

Gebruik `toolsBySender` om een strikter beleid toe te passen op `"*"` en een ruimer beleid op je nick:

json5Copy code
[code]
    {  channels: {    irc: {      groups: {        "#tuirc-dev": {          allowFrom: ["*"],          toolsBySender: {            "*": {              deny: ["group:runtime", "group:fs", "gateway", "nodes", "cron", "browser"],            },            "id:eigen": {              deny: ["gateway", "nodes", "cron"],            },          },        },      },    },  },}
[/code]

Opmerkingen:

  * `toolsBySender`-sleutels moeten `id:` gebruiken voor IRC-afzenderidentiteitswaarden: `id:eigen` of `id:eigen!~eigen@174.127.248.171` voor sterkere matching.
  * Verouderde sleutels zonder prefix worden nog steeds geaccepteerd en alleen als `id:` gematcht.
  * Het eerste overeenkomende afzenderbeleid wint; `"*"` is de wildcard-fallback.


Zie voor meer over groepstoegang versus vermeldingsgating (en hoe ze samen werken): [/channels/groups](</nl/channels/groups>).

## NickServ

Om je na verbinden te identificeren bij NickServ:

json5Copy code
[code]
    {  channels: {    irc: {      nickserv: {        enabled: true,        service: "NickServ",        password: "your-nickserv-password",      },    },  },}
[/code]

Optionele eenmalige registratie bij verbinden:

json5Copy code
[code]
    {  channels: {    irc: {      nickserv: {        register: true,        registerEmail: "bot@example.com",      },    },  },}
[/code]

Schakel `register` uit nadat de nick is geregistreerd om herhaalde REGISTER-pogingen te voorkomen.

## Omgevingsvariabelen

Het standaardaccount ondersteunt:

  * `IRC_HOST`
  * `IRC_PORT`
  * `IRC_TLS`
  * `IRC_NICK`
  * `IRC_USERNAME`
  * `IRC_REALNAME`
  * `IRC_PASSWORD`
  * `IRC_CHANNELS` (komma-gescheiden)
  * `IRC_NICKSERV_PASSWORD`
  * `IRC_NICKSERV_REGISTER_EMAIL`


`IRC_HOST` kan niet worden ingesteld vanuit een workspace-`.env`; zie [Workspace-`.env`-bestanden](</nl/gateway/security>).

## Probleemoplossing

  * Als de bot verbinding maakt maar nooit antwoordt in kanalen, controleer `channels.irc.groups` **en** of vermeldingsgating berichten laat vallen (`missing-mention`). Als je wilt dat de bot zonder pings antwoordt, stel dan `requireMention:false` in voor het kanaal.
  * Als aanmelden mislukt, controleer de beschikbaarheid van de nick en het serverwachtwoord.
  * Als TLS faalt op een aangepast netwerk, controleer de host/poort en certificaatconfiguratie.


## Gerelateerd

  * [Kanalenoverzicht](</nl/channels>) — alle ondersteunde kanalen
  * [Pairing](</nl/channels/pairing>) — DM-authenticatie en pairing-flow
  * [Groepen](</nl/channels/groups>) — gedrag van groepschats en vermeldingsgating
  * [Kanaalroutering](</nl/channels/channel-routing>) — sessieroutering voor berichten
  * [Beveiliging](</nl/gateway/security>) — toegangsmodel en hardening


Was this useful?YesNo