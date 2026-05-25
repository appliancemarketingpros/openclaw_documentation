---
title: Yuanbao
source_url: https://docs.openclaw.ai/nl/channels/yuanbao
scraped_at: 2026-05-25
---

Tencent Yuanbao is het AI-assistentplatform van Tencent. De OpenClaw-kanaal-Plugin verbindt Yuanbao-bots met OpenClaw via WebSocket, zodat ze met gebruikers kunnen communiceren via directe berichten en groepschats.

**Status:** productiegereed voor bot-DM's + groepschats. WebSocket is de enige ondersteunde verbindingsmodus.

* * *

## Snelstart

> **Vereist OpenClaw 2026.4.10 of hoger.** Voer `openclaw --version` uit om dit te controleren. Werk bij met `openclaw update`.

* ### Voeg het Yuanbao-kanaal toe met je referenties

bashCopy code
[code]
    openclaw channels add --channel yuanbao --token "appKey:appSecret"
[/code]

De waarde `--token` gebruikt de door dubbele punten gescheiden indeling `appKey:appSecret`. Je kunt deze verkrijgen in de Yuanbao-app door een robot te maken in je applicatie-instellingen.

* ### Nadat de configuratie is voltooid, herstart je de gateway om de wijzigingen toe te passen

bashCopy code
[code]
    openclaw gateway restart
[/code]

### Interactieve configuratie (alternatief)

Je kunt ook de interactieve wizard gebruiken:

bashCopy code
[code]
    openclaw channels login --channel yuanbao
[/code]

Volg de prompts om je App ID en App Secret in te voeren.

* * *

## Toegangscontrole

### Directe berichten

Configureer `dmPolicy` om te bepalen wie de bot een DM kan sturen:

  * `"pairing"` \- onbekende gebruikers ontvangen een koppelingscode; keur goed via CLI
  * `"allowlist"` \- alleen gebruikers die in `allowFrom` staan, kunnen chatten
  * `"open"` \- alle gebruikers toestaan (standaard)
  * `"disabled"` \- alle DM's uitschakelen


**Een koppelingsverzoek goedkeuren:**

bashCopy code
[code]
    openclaw pairing list yuanbaoopenclaw pairing approve yuanbao &lt;CODE&gt;
[/code]

### Groepschats

**Vermeldingsvereiste** (`channels.yuanbao.requireMention`):

  * `true` \- @mention vereisen (standaard)
  * `false` \- reageren zonder @mention


Antwoorden op het bericht van de bot in een groepschat wordt behandeld als een impliciete vermelding.

* * *

## Configuratievoorbeelden

### Basisconfiguratie met open DM-beleid

json5Copy code
[code]
    {  channels: {    yuanbao: {      appKey: "your_app_key",      appSecret: "your_app_secret",      dm: {        policy: "open",      },    },  },}
[/code]

### DM's beperken tot specifieke gebruikers

json5Copy code
[code]
    {  channels: {    yuanbao: {      appKey: "your_app_key",      appSecret: "your_app_secret",      dm: {        policy: "allowlist",        allowFrom: ["user_id_1", "user_id_2"],      },    },  },}
[/code]

### @mention-vereiste in groepen uitschakelen

json5Copy code
[code]
    {  channels: {    yuanbao: {      requireMention: false,    },  },}
[/code]

### Uitgaande berichtbezorging optimaliseren

json5Copy code
[code]
    {  channels: {    yuanbao: {      // Send each chunk immediately without buffering      outboundQueueStrategy: "immediate",    },  },}
[/code]

### Merge-text-strategie afstemmen

json5Copy code
[code]
    {  channels: {    yuanbao: {      outboundQueueStrategy: "merge-text",      minChars: 2800, // buffer until this many chars      maxChars: 3000, // force split above this limit      idleMs: 5000, // auto-flush after idle timeout (ms)    },  },}
[/code]

* * *

## Veelgebruikte opdrachten

Opdracht | Beschrijving  
---|---  
`/help` | Beschikbare opdrachten tonen  
`/status` | Botstatus tonen  
`/new` | Een nieuwe sessie starten  
`/stop` | De huidige uitvoering stoppen  
`/restart` | OpenClaw herstarten  
`/compact` | De sessiecontext compacteren  
  
> Yuanbao ondersteunt native slash-command-menu's. Opdrachten worden automatisch met het platform gesynchroniseerd wanneer de gateway start.

* * *

## Probleemoplossing

### Bot reageert niet in groepschats

  1. Zorg dat de bot aan de groep is toegevoegd
  2. Zorg dat je de bot @mentiont (standaard vereist)
  3. Controleer logs: `openclaw logs --follow`


### Bot ontvangt geen berichten

  1. Zorg dat de bot is gemaakt en goedgekeurd in de Yuanbao-app
  2. Zorg dat `appKey` en `appSecret` correct zijn geconfigureerd
  3. Zorg dat de gateway draait: `openclaw gateway status`
  4. Controleer logs: `openclaw logs --follow`


### Bot stuurt lege of fallback-antwoorden

  1. Controleer of het AI-model geldige content retourneert
  2. Het standaard fallback-antwoord is: "暂时无法解答，你可以换个问题问问我哦"
  3. Pas dit aan via `channels.yuanbao.fallbackReply`


### App Secret gelekt

  1. Reset de App Secret in YuanBao APP
  2. Werk de waarde in je configuratie bij
  3. Herstart de gateway: `openclaw gateway restart`


* * *

## Geavanceerde configuratie

### Meerdere accounts

json5Copy code
[code]
    {  channels: {    yuanbao: {      defaultAccount: "main",      accounts: {        main: {          appKey: "key_xxx",          appSecret: "secret_xxx",          name: "Primary bot",        },        backup: {          appKey: "key_yyy",          appSecret: "secret_yyy",          name: "Backup bot",          enabled: false,        },      },    },  },}
[/code]

`defaultAccount` bepaalt welk account wordt gebruikt wanneer uitgaande API's geen `accountId` specificeren.

### Berichtlimieten

  * `maxChars` \- maximaal aantal tekens voor één bericht (standaard: `3000` tekens)
  * `mediaMaxMb` \- upload-/downloadlimiet voor media (standaard: `20` MB)
  * `overflowPolicy` \- gedrag wanneer bericht limiet overschrijdt: `"split"` (standaard) of `"stop"`


### Streaming

Yuanbao ondersteunt streaminguitvoer op blokniveau. Wanneer ingeschakeld, verzendt de bot tekst in chunks terwijl deze wordt gegenereerd.

json5Copy code
[code]
    {  channels: {    yuanbao: {      disableBlockStreaming: false, // block streaming enabled (default)    },  },}
[/code]

Stel `disableBlockStreaming: true` in om het volledige antwoord in één bericht te verzenden.

### Context van groepschatgeschiedenis

Bepaal hoeveel historische berichten worden opgenomen in de AI-context voor groepschats:

json5Copy code
[code]
    {  channels: {    yuanbao: {      historyLimit: 100, // default: 100, set 0 to disable    },  },}
[/code]

### Reply-to-modus

Bepaal hoe de bot berichten citeert bij antwoorden in groepschats:

json5Copy code
[code]
    {  channels: {    yuanbao: {      replyToMode: "first", // "off" | "first" | "all" (default: "first")    },  },}
[/code]

Waarde | Gedrag  
---|---  
`"off"` | Geen citaatantwoord  
`"first"` | Alleen het eerste antwoord per binnenkomend bericht citeren (standaard)  
`"all"` | Elk antwoord citeren  
  
### Markdown-hintinjectie

Standaard injecteert de bot instructies in de systeemprompt om te voorkomen dat het AI-model het volledige antwoord in markdown-codeblokken plaatst.

json5Copy code
[code]
    {  channels: {    yuanbao: {      markdownHintEnabled: true, // default: true    },  },}
[/code]

### Debugmodus

Schakel niet-gezuiverde loguitvoer in voor specifieke bot-ID's:

json5Copy code
[code]
    {  channels: {    yuanbao: {      debugBotIds: ["bot_user_id_1", "bot_user_id_2"],    },  },}
[/code]

### Routing voor meerdere agents

Gebruik `bindings` om Yuanbao-DM's of groepen naar verschillende agents te routeren.

json5Copy code
[code]
    {  agents: {    list: [      { id: "main" },      { id: "agent-a", workspace: "/home/user/agent-a" },      { id: "agent-b", workspace: "/home/user/agent-b" },    ],  },  bindings: [    {      agentId: "agent-a",      match: {        channel: "yuanbao",        peer: { kind: "direct", id: "user_xxx" },      },    },    {      agentId: "agent-b",      match: {        channel: "yuanbao",        peer: { kind: "group", id: "group_zzz" },      },    },  ],}
[/code]

Routingvelden:

  * `match.channel`: `"yuanbao"`
  * `match.peer.kind`: `"direct"` (DM) of `"group"` (groepschat)
  * `match.peer.id`: gebruikers-ID of groepscode


* * *

## Configuratiereferentie

Volledige configuratie: [Gateway-configuratie](</nl/gateway/configuration>)

Instelling | Beschrijving | Standaard  
---|---|---  
`channels.yuanbao.enabled` | Het kanaal in-/uitschakelen | `true`  
`channels.yuanbao.defaultAccount` | Standaardaccount voor uitgaande routing | `default`  
`channels.yuanbao.accounts.<id>.appKey` | App Key (gebruikt voor ondertekening en ticketgeneratie) | -  
`channels.yuanbao.accounts.<id>.appSecret` | App Secret (gebruikt voor ondertekening) | -  
`channels.yuanbao.accounts.<id>.token` | Vooraf ondertekend token (slaat automatische ticketondertekening over) | -  
`channels.yuanbao.accounts.<id>.name` | Weergavenaam van account | -  
`channels.yuanbao.accounts.<id>.enabled` | Een specifiek account in-/uitschakelen | `true`  
`channels.yuanbao.dm.policy` | DM-beleid | `open`  
`channels.yuanbao.dm.allowFrom` | DM-toestaanlijst (lijst met gebruikers-ID's) | -  
`channels.yuanbao.requireMention` | @mention vereisen in groepen | `true`  
`channels.yuanbao.overflowPolicy` | Afhandeling van lange berichten (`split` of `stop`) | `split`  
`channels.yuanbao.replyToMode` | Strategie voor groepsantwoord-citaten (`off`, `first`, `all`) | `first`  
`channels.yuanbao.outboundQueueStrategy` | Uitgaande strategie (`merge-text` of `immediate`) | `merge-text`  
`channels.yuanbao.minChars` | Merge-text: min. aantal tekens om verzending te activeren | `2800`  
`channels.yuanbao.maxChars` | Merge-text: max. aantal tekens per bericht | `3000`  
`channels.yuanbao.idleMs` | Merge-text: time-out bij inactiviteit vóór auto-flush (ms) | `5000`  
`channels.yuanbao.mediaMaxMb` | Limiet voor mediagrootte (MB) | `20`  
`channels.yuanbao.historyLimit` | Contextitems voor groepschatgeschiedenis | `100`  
`channels.yuanbao.disableBlockStreaming` | Streaminguitvoer op blokniveau uitschakelen | `false`  
`channels.yuanbao.fallbackReply` | Fallback-antwoord wanneer AI geen content retourneert | `暂时无法解答，你可以换个问题问问我哦`  
`channels.yuanbao.markdownHintEnabled` | Markdown-instructies tegen omwikkelen injecteren | `true`  
`channels.yuanbao.debugBotIds` | Debug-toestaanlijst met bot-ID's (niet-gezuiverde logs) | `[]`  
  
* * *

## Ondersteunde berichttypen

### Ontvangen

  * ✅ Tekst
  * ✅ Afbeeldingen
  * ✅ Bestanden
  * ✅ Audio / spraak
  * ✅ Video
  * ✅ Stickers / aangepaste emoji
  * ✅ Aangepaste elementen (linkkaarten, enz.)


### Verzenden

  * ✅ Tekst (met markdown-ondersteuning)
  * ✅ Afbeeldingen
  * ✅ Bestanden
  * ✅ Audio
  * ✅ Video
  * ✅ Stickers


### Threads en antwoorden

  * ✅ Citaatantwoorden (configureerbaar via `replyToMode`)
  * ❌ Thread-antwoorden (niet ondersteund door platform)


* * *

## Gerelateerd

  * [Kanalenoverzicht](</nl/channels>) \- alle ondersteunde kanalen
  * [Koppelen](</nl/channels/pairing>) \- DM-authenticatie en koppelingsflow
  * [Groepen](</nl/channels/groups>) \- groepschatgedrag en vermeldingsgating
  * [Kanaalrouting](</nl/channels/channel-routing>) \- sessierouting voor berichten
  * [Beveiliging](</nl/gateway/security>) \- toegangsmodel en hardening


Was this useful?YesNo