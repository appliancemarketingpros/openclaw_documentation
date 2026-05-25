---
title: Toegangsgroepen
source_url: https://docs.openclaw.ai/nl/channels/access-groups
scraped_at: 2026-05-25
---

Toegangsgroepen zijn benoemde afzenderlijsten die je eenmaal definieert en vanuit kanaal-allowlists verwijst met `accessGroup:<name>`.

Gebruik ze wanneer dezelfde personen toegang moeten hebben tot meerdere berichtkanalen, of wanneer een vertrouwde set moet gelden voor zowel DM's als autorisatie van groepsafzenders.

Toegangsgroepen verlenen op zichzelf geen toegang. Een groep is alleen van belang wanneer een allowlist-veld ernaar verwijst.

## Statische groepen voor berichtafzenders

Statische afzendergroepen gebruiken `type: "message.senders"`.

json5Copy code
[code]
    {  accessGroups: {    operators: {      type: "message.senders",      members: {        "*": ["global-owner-id"],        discord: ["discord:123456789012345678"],        telegram: ["987654321"],        whatsapp: ["+15551234567"],      },    },  },}
[/code]

Ledenlijsten worden gesleuteld op berichtkanaal-id:

Sleutel | Betekenis  
---|---  
`"*"` | Gedeelde vermeldingen die worden gecontroleerd voor elk berichtkanaal dat naar de groep verwijst.  
`discord` | Vermeldingen die alleen worden gecontroleerd voor Discord-allowlistmatching.  
`telegram` | Vermeldingen die alleen worden gecontroleerd voor Telegram-allowlistmatching.  
`whatsapp` | Vermeldingen die alleen worden gecontroleerd voor WhatsApp-allowlistmatching.  
  
Vermeldingen worden gematcht met de normale `allowFrom`-regels van het doelkanaal. OpenClaw vertaalt geen afzender-id's tussen kanalen. Als Alice een Telegram-id en een Discord-id heeft, vermeld dan beide id's onder de juiste sleutels.

## Groepen verwijzen vanuit allowlists

Verwijs naar een groep met `accessGroup:<name>` overal waar het berichtkanaalpad afzender-allowlists ondersteunt.

Voorbeeld van DM-allowlist:

json5Copy code
[code]
    {  accessGroups: {    operators: {      type: "message.senders",      members: {        discord: ["discord:123456789012345678"],        telegram: ["987654321"],      },    },  },  channels: {    discord: {      dmPolicy: "allowlist",      allowFrom: ["accessGroup:operators"],    },    telegram: {      dmPolicy: "allowlist",      allowFrom: ["accessGroup:operators"],    },  },}
[/code]

Voorbeeld van allowlist voor groepsafzenders:

json5Copy code
[code]
    {  accessGroups: {    oncall: {      type: "message.senders",      members: {        whatsapp: ["+15551234567"],        googlechat: ["users/1234567890"],      },    },  },  channels: {    whatsapp: {      groupPolicy: "allowlist",      groupAllowFrom: ["accessGroup:oncall"],    },    googlechat: {      spaces: {        "spaces/AAA": {          users: ["accessGroup:oncall"],        },      },    },  },}
[/code]

Je kunt groepen en directe vermeldingen combineren:

json5Copy code
[code]
    {  channels: {    discord: {      dmPolicy: "allowlist",      allowFrom: ["accessGroup:operators", "discord:123456789012345678"],    },  },}
[/code]

## Ondersteunde berichtkanaalpaden

Toegangsgroepen zijn beschikbaar in gedeelde autorisatiepaden voor berichtkanalen, waaronder:

  * DM-afzender-allowlists zoals `channels.<channel>.allowFrom`
  * allowlists voor groepsafzenders zoals `channels.<channel>.groupAllowFrom`
  * kanaalspecifieke afzender-allowlists per ruimte die dezelfde regels voor afzendermatching gebruiken
  * opdracht-autorisatiepaden die afzender-allowlists van berichtkanalen hergebruiken


Kanaalondersteuning hangt ervan af of dat kanaal is aangesloten op de gedeelde OpenClaw-helpers voor afzenderautorisatie. De huidige gebundelde ondersteuning omvat Discord, Feishu, Google Chat, iMessage, LINE, Mattermost, Microsoft Teams, Nextcloud Talk, Nostr, QQBot, Signal, WhatsApp, Zalo en Zalo Personal. Statische `message.senders`-groepen zijn ontworpen om kanaalonafhankelijk te zijn, dus nieuwe berichtkanalen zouden ze moeten ondersteunen door de gedeelde Plugin SDK-helpers te gebruiken in plaats van aangepaste allowlist-uitbreiding.

## Plugin-diagnostiek

Plugin-auteurs kunnen gestructureerde toegangsgroepstatus inspecteren zonder die terug uit te breiden naar een platte allowlist:

typescriptCopy code
[code]
     const state = await resolveAccessGroupAllowFromState({  accessGroups: cfg.accessGroups,  allowFrom: channelConfig.allowFrom,  channel: "my-channel",  accountId: "default",  senderId,  isSenderAllowed,});
[/code]

Het resultaat rapporteert verwezen, gematchte, ontbrekende, niet-ondersteunde en mislukte groepen. Gebruik dit wanneer je diagnostiek of conformiteitstests nodig hebt. Gebruik `expandAllowFromWithAccessGroups(...)` alleen voor compatibiliteitspaden die nog steeds een platte `allowFrom`-array verwachten.

## Discord-kanaaldoelgroepen

Discord ondersteunt ook een dynamisch toegangsgroeptype:

json5Copy code
[code]
    {  accessGroups: {    maintainers: {      type: "discord.channelAudience",      guildId: "1456350064065904867",      channelId: "1456744319972282449",      membership: "canViewChannel",    },  },  channels: {    discord: {      dmPolicy: "allowlist",      allowFrom: ["accessGroup:maintainers"],    },  },}
[/code]

`discord.channelAudience` betekent "sta Discord-DM-afzenders toe die dit guildkanaal momenteel kunnen bekijken." OpenClaw resolveert de afzender via Discord op het moment van autorisatie en past de Discord-`ViewChannel`-machtigingsregels toe.

Gebruik dit wanneer een Discord-kanaal al de bron van waarheid is voor een team, zoals `#maintainers` of `#on-call`.

Vereisten en gedrag bij fouten:

  * De bot heeft toegang nodig tot de guild en het kanaal.
  * De bot heeft de Discord Developer Portal **Server Members Intent** nodig.
  * De toegangsgroep faalt gesloten wanneer Discord `Missing Access` retourneert, de afzender niet als guildlid kan worden geresolveerd, of het kanaal bij een andere guild hoort.


Meer Discord-specifieke voorbeelden: [Discord-toegangsbeheer](</nl/channels/discord#access-control-and-routing>)

## Beveiligingsnotities

  * Toegangsgroepen zijn allowlist-aliassen, geen rollen. Ze maken op zichzelf geen eigenaren aan, keuren geen koppelingsverzoeken goed en verlenen geen toolmachtigingen.
  * `dmPolicy: "open"` vereist nog steeds `"*"` in de effectieve DM-allowlist. Verwijzen naar een toegangsgroep is niet hetzelfde als openbare toegang.
  * Ontbrekende groepsnamen falen gesloten. Als `allowFrom` `accessGroup:operators` bevat en `accessGroups.operators` ontbreekt, autoriseert die vermelding niemand.
  * Houd kanaal-id's stabiel. Geef de voorkeur aan numerieke/gebruikers-id's boven weergavenamen wanneer het kanaal beide ondersteunt.


## Problemen oplossen

Als een afzender zou moeten matchen maar wordt geblokkeerd:

  1. Controleer of het allowlist-veld de exacte verwijzing `accessGroup:<name>` bevat.
  2. Controleer of `accessGroups.<name>.type` correct is.
  3. Controleer of de afzender-id onder de overeenkomende kanaalsleutel staat, of onder `"*"`.
  4. Controleer of de vermelding de normale allowlist-syntaxis van dat kanaal gebruikt.
  5. Controleer voor Discord-kanaaldoelgroepen of de bot het guildkanaal kan zien en Server Members Intent heeft ingeschakeld.


Voer `openclaw doctor` uit nadat je de toegangsbeheerconfiguratie hebt bewerkt. Dit vangt veel ongeldige combinaties van allowlists en beleid op vóór runtime.

Was this useful?YesNo