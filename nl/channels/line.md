---
title: REGEL
source_url: https://docs.openclaw.ai/nl/channels/line
scraped_at: 2026-05-25
---

LINE maakt verbinding met OpenClaw via de LINE Messaging API. De Plugin draait als Webhook ontvanger op de Gateway en gebruikt je channel access token + channel secret voor authenticatie.

Status: downloadbare Plugin. Directe berichten, groepschats, media, locaties, Flex messages, template messages en quick replies worden ondersteund. Reacties en threads worden niet ondersteund.

## Installeren

Installeer LINE voordat je het kanaal configureert:

bashCopy code
[code]
    openclaw plugins install @openclaw/line
[/code]

Lokale checkout (bij draaien vanuit een git-repo):

bashCopy code
[code]
    openclaw plugins install ./path/to/local/line-plugin
[/code]

## Instellen

  1. Maak een LINE Developers-account aan en open de Console: <https://developers.line.biz/console/>
  2. Maak (of kies) een Provider en voeg een **Messaging API** -kanaal toe.
  3. Kopieer de **Channel access token** en **Channel secret** uit de kanaalinstellingen.
  4. Schakel **Use webhook** in de Messaging API-instellingen in.
  5. Stel de Webhook-URL in op je Gateway-eindpunt (HTTPS vereist):

CodeCopy code
[code]
    https://gateway-host/line/webhook
[/code]

De Gateway reageert op LINE's Webhook-verificatie (GET) en inkomende gebeurtenissen (POST). Als je een aangepast pad nodig hebt, stel dan `channels.line.webhookPath` of `channels.line.accounts.<id>.webhookPath` in en werk de URL dienovereenkomstig bij.

Beveiligingsopmerking:

  * LINE-handtekeningverificatie is afhankelijk van de body (HMAC over de ruwe body), dus OpenClaw past strikte pre-auth-bodylimieten en een timeout toe vóór verificatie.
  * OpenClaw verwerkt Webhook-gebeurtenissen vanuit de geverifieerde ruwe requestbytes. Door upstream middleware getransformeerde `req.body`-waarden worden genegeerd voor veilige handtekeningintegriteit.


## Configureren

Minimale configuratie:

json5Copy code
[code]
    {  channels: {    line: {      enabled: true,      channelAccessToken: "LINE_CHANNEL_ACCESS_TOKEN",      channelSecret: "LINE_CHANNEL_SECRET",      dmPolicy: "pairing",    },  },}
[/code]

Openbare DM-configuratie:

json5Copy code
[code]
    {  channels: {    line: {      enabled: true,      channelAccessToken: "LINE_CHANNEL_ACCESS_TOKEN",      channelSecret: "LINE_CHANNEL_SECRET",      dmPolicy: "open",      allowFrom: ["*"],    },  },}
[/code]

Omgevingsvariabelen (alleen standaardaccount):

  * `LINE_CHANNEL_ACCESS_TOKEN`
  * `LINE_CHANNEL_SECRET`


Token-/secret-bestanden:

json5Copy code
[code]
    {  channels: {    line: {      tokenFile: "/path/to/line-token.txt",      secretFile: "/path/to/line-secret.txt",    },  },}
[/code]

`tokenFile` en `secretFile` moeten naar gewone bestanden verwijzen. Symlinks worden geweigerd.

Meerdere accounts:

json5Copy code
[code]
    {  channels: {    line: {      accounts: {        marketing: {          channelAccessToken: "...",          channelSecret: "...",          webhookPath: "/line/marketing",        },      },    },  },}
[/code]

## Toegangsbeheer

Directe berichten gebruiken standaard pairing. Onbekende afzenders krijgen een pairingcode en hun berichten worden genegeerd totdat ze zijn goedgekeurd.

bashCopy code
[code]
    openclaw pairing list lineopenclaw pairing approve line &lt;CODE&gt;
[/code]

Toestemmingslijsten en beleid:

  * `channels.line.dmPolicy`: `pairing | allowlist | open | disabled`
  * `channels.line.allowFrom`: toegestane LINE-gebruikers-ID's voor DM's; `dmPolicy: "open"` vereist `["*"]`
  * `channels.line.groupPolicy`: `allowlist | open | disabled`
  * `channels.line.groupAllowFrom`: toegestane LINE-gebruikers-ID's voor groepen
  * Overrides per groep: `channels.line.groups.<groupId>.allowFrom`
  * Statische afzendertoegangsgroepen kunnen worden gebruikt vanuit `allowFrom`, `groupAllowFrom` en per-groep `allowFrom` met `accessGroup:<name>`.
  * Runtime-opmerking: als `channels.line` volledig ontbreekt, valt de runtime terug op `groupPolicy="allowlist"` voor groepscontroles (zelfs als `channels.defaults.groupPolicy` is ingesteld).


LINE-ID's zijn hoofdlettergevoelig. Geldige ID's zien eruit als:

  * Gebruiker: `U` \+ 32 hex-tekens
  * Groep: `C` \+ 32 hex-tekens
  * Ruimte: `R` \+ 32 hex-tekens


## Berichtgedrag

  * Tekst wordt opgesplitst bij 5000 tekens.
  * Markdown-opmaak wordt verwijderd; codeblokken en tabellen worden waar mogelijk omgezet naar Flex cards.
  * Streaming-antwoorden worden gebufferd; LINE ontvangt volledige chunks met een laadanimatie terwijl de agent werkt.
  * Mediadownloads worden begrensd door `channels.line.mediaMaxMb` (standaard 10).
  * Inkomende media worden opgeslagen onder `~/.openclaw/media/inbound/` voordat ze worden doorgegeven aan de agent, overeenkomend met de gedeelde mediaopslag die door andere gebundelde kanaalplugins wordt gebruikt.


## Kanaalgegevens (rijke berichten)

Gebruik `channelData.line` om quick replies, locaties, Flex cards of template messages te verzenden.

json5Copy code
[code]
    {  text: "Here you go",  channelData: {    line: {      quickReplies: ["Status", "Help"],      location: {        title: "Office",        address: "123 Main St",        latitude: 35.681236,        longitude: 139.767125,      },      flexMessage: {        altText: "Status card",        contents: {          /* Flex payload */        },      },      templateMessage: {        type: "confirm",        text: "Proceed?",        confirmLabel: "Yes",        confirmData: "yes",        cancelLabel: "No",        cancelData: "no",      },    },  },}
[/code]

De LINE-Plugin levert ook een `/card`-opdracht voor Flex message-presets:

CodeCopy code
[code]
    /card info "Welcome" "Thanks for joining!"
[/code]

## ACP-ondersteuning

LINE ondersteunt ACP-conversatiebindings (Agent Communication Protocol):

  * `/acp spawn <agent> --bind here` bindt de huidige LINE-chat aan een ACP-sessie zonder een child thread te maken.
  * Geconfigureerde ACP-bindings en actieve conversatiegebonden ACP-sessies werken op LINE zoals op andere conversatiekanalen.


Zie [ACP-agents](</nl/tools/acp-agents>) voor details.

## Uitgaande media

De LINE-Plugin ondersteunt het verzenden van afbeeldingen, video's en audiobestanden via de berichttool van de agent. Media worden verzonden via het LINE-specifieke bezorgpad met passende preview- en trackingafhandeling:

  * **Afbeeldingen** : verzonden als LINE-afbeeldingsberichten met automatische previewgeneratie.
  * **Video's** : verzonden met expliciete preview- en content-type-afhandeling.
  * **Audio** : verzonden als LINE-audioberichten.


Uitgaande media-URL's moeten openbare HTTPS-URL's zijn. OpenClaw valideert de doelhostnaam voordat de URL aan LINE wordt doorgegeven en weigert local loopback-, link-local- en private-netwerkdoelen.

Algemene mediaverzendingen vallen terug op de bestaande route voor alleen afbeeldingen wanneer een LINE-specifiek pad niet beschikbaar is.

## Probleemoplossing

  * **Webhook-verificatie mislukt:** zorg ervoor dat de Webhook-URL HTTPS gebruikt en dat `channelSecret` overeenkomt met de LINE-console.
  * **Geen inkomende gebeurtenissen:** controleer of het Webhook-pad overeenkomt met `channels.line.webhookPath` en dat de Gateway bereikbaar is vanaf LINE.
  * **Mediadownloadfouten:** verhoog `channels.line.mediaMaxMb` als media de standaardlimiet overschrijden.


## Gerelateerd

  * [Kanalenoverzicht](</nl/channels>) — alle ondersteunde kanalen
  * [Pairing](</nl/channels/pairing>) — DM-authenticatie en pairingflow
  * [Groepen](</nl/channels/groups>) — gedrag van groepschats en mention gating
  * [Kanaalroutering](</nl/channels/channel-routing>) — sessieroutering voor berichten
  * [Beveiliging](</nl/gateway/security>) — toegangsmodel en hardening


Was this useful?YesNo