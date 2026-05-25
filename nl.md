---
title: OpenClaw
source_url: https://docs.openclaw.ai/nl
scraped_at: 2026-05-25
---

# OpenClaw 🦞

![OpenClaw](/assets/openclaw-logo-text-dark.png) ![OpenClaw](/assets/openclaw-logo-text.png)

> _"EXFOLIEER! EXFOLIEER!"_ — Een ruimtekreeft, waarschijnlijk

**Gateway voor elk besturingssysteem voor AI-agenten via Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo en meer.**

Stuur een bericht en ontvang een agentantwoord vanuit je broekzak. Voer één Gateway uit voor ingebouwde kanalen, meegeleverde kanaalplugins, WebChat en mobiele nodes.

[**Aan de slag** Installeer OpenClaw en start de Gateway binnen enkele minuten. ](</nl/start/getting-started>) [**Onboarding uitvoeren** Begeleide installatie met `openclaw onboard` en koppelingsflows. ](</nl/start/wizard>) [**De beheerinterface openen** Start het browserdashboard voor chat, configuratie en sessies. ](</nl/web/control-ui>)

## Wat is OpenClaw?

OpenClaw is een **zelfgehoste gateway** die je favoriete chatapps en kanaaloppervlakken verbindt — ingebouwde kanalen plus meegeleverde of externe kanaalplugins zoals Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo en meer — met AI-codeeragenten zoals Pi. Je voert één Gateway-proces uit op je eigen machine (of een server), en dat wordt de brug tussen je berichtenapps en een altijd beschikbare AI-assistent.

**Voor wie is het bedoeld?** Ontwikkelaars en powerusers die een persoonlijke AI-assistent willen die ze overal vandaan kunnen berichten, zonder de controle over hun gegevens op te geven of afhankelijk te zijn van een gehoste service.

**Wat maakt het anders?**

  * **Zelfgehost** : draait op jouw hardware, volgens jouw regels
  * **Meerdere kanalen** : één Gateway bedient gelijktijdig ingebouwde kanalen plus meegeleverde of externe kanaalplugins
  * **Agent-native** : gebouwd voor codeeragenten met toolgebruik, sessies, geheugen en multi-agent-routering
  * **Open source** : MIT-gelicentieerd en communitygedreven


**Wat heb je nodig?** Node 24 (aanbevolen), of Node 22 LTS (`22.16+`) voor compatibiliteit, een API-sleutel van je gekozen provider en 5 minuten. Gebruik voor de beste kwaliteit en beveiliging het krachtigste beschikbare model van de nieuwste generatie.

## Hoe het werkt
[code] 
    flowchart LR
      A["Chat apps + plugins"] --> B["Gateway"]
      B --> C["Pi agent"]
      B --> D["CLI"]
      B --> E["Web Control UI"]
      B --> F["macOS app"]
      B --> G["iOS and Android nodes"]
[/code]

De Gateway is de enige bron van waarheid voor sessies, routering en kanaalverbindingen.

## Belangrijkste mogelijkheden

[**Gateway voor meerdere kanalen** Discord, iMessage, Signal, Slack, Telegram, WhatsApp, WebChat en meer met één Gateway-proces. ](</nl/channels>) [**Plugin-kanalen** Meegeleverde plugins voegen Matrix, Nostr, Twitch, Zalo en meer toe in normale huidige releases. ](</nl/tools/plugin>) [**Multi-agent-routering** Geïsoleerde sessies per agent, werkruimte of afzender. ](</nl/concepts/multi-agent>) [**Media-ondersteuning** Verzend en ontvang afbeeldingen, audio en documenten. ](</nl/nodes/images>) [**Webbeheerinterface** Browserdashboard voor chat, configuratie, sessies en nodes. ](</nl/web/control-ui>) [**Mobiele nodes** Koppel iOS- en Android-nodes voor Canvas, camera en spraakgestuurde workflows. ](</nl/nodes>)

## Snel starten

* ### OpenClaw installeren

bashCopy code
[code]
    npm install -g openclaw@latest
[/code]

* ### Onboarden en de service installeren

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

* ### Chatten

Open de beheerinterface in je browser en stuur een bericht:

bashCopy code
[code]
    openclaw dashboard
[/code]

Of verbind een kanaal ([Telegram](</nl/channels/telegram>) is het snelst) en chat vanaf je telefoon.

Heb je de volledige installatie- en ontwikkelsetup nodig? Zie [Aan de slag](</nl/start/getting-started>).

## Dashboard

Open de browserbeheerinterface nadat de Gateway is gestart.

  * Lokale standaard: <http://127.0.0.1:18789/>
  * Toegang op afstand: [Weboppervlakken](</nl/web>) en [Tailscale](</nl/gateway/tailscale>)


![OpenClaw](/whatsapp-openclaw.jpg)

## Configuratie (optioneel)

De configuratie staat op `~/.openclaw/openclaw.json`.

  * Als je **niets doet** , gebruikt OpenClaw de meegeleverde Pi-binary in RPC-modus met sessies per afzender.
  * Als je het wilt vergrendelen, begin dan met `channels.whatsapp.allowFrom` en (voor groepen) vermeldingsregels.


Voorbeeld:

json5Copy code
[code]
    {  channels: {    whatsapp: {      allowFrom: ["+15555550123"],      groups: { "*": { requireMention: true } },    },  },  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },}
[/code]

## Begin hier

[**Docshubs** Alle docs en handleidingen, georganiseerd per usecase. ](</nl/start/hubs>) [**Configuratie** Kerninstellingen van de Gateway, tokens en providerconfiguratie. ](</nl/gateway/configuration>) [**Toegang op afstand** Toegangspatronen voor SSH en tailnet. ](</nl/gateway/remote>) [**Kanalen** Kanaalspecifieke installatie voor Feishu, Microsoft Teams, WhatsApp, Telegram, Discord en meer. ](</nl/channels/telegram>) [**Nodes** iOS- en Android-nodes met koppeling, Canvas, camera en apparaatacties. ](</nl/nodes>) [**Help** Ingangspunt voor veelvoorkomende oplossingen en probleemoplossing. ](</nl/help>)

## Meer informatie

[**Volledige functielijst** Volledige mogelijkheden voor kanalen, routering en media. ](</nl/concepts/features>) [**Multi-agent-routering** Werkruimte-isolatie en sessies per agent. ](</nl/concepts/multi-agent>) [**Beveiliging** Tokens, allowlists en veiligheidscontroles. ](</nl/gateway/security>) [**Probleemoplossing** Gateway-diagnostiek en veelvoorkomende fouten. ](</nl/gateway/troubleshooting>) [**Over en credits** Projectoorsprong, bijdragers en licentie. ](</nl/reference/credits>)

Was this useful?YesNo