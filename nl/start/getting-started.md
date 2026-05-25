---
title: Aan de slag
source_url: https://docs.openclaw.ai/nl/start/getting-started
scraped_at: 2026-05-25
---

Installeer OpenClaw, doorloop de onboarding en chat met je AI-assistent, alles in ongeveer 5 minuten. Aan het einde heb je een draaiende Gateway, geconfigureerde auth en een werkende chatsessie.

## Wat je nodig hebt

  * **Node.js** — Node 24 aanbevolen (Node 22.16+ ook ondersteund)
  * **Een API-sleutel** van een modelprovider (Anthropic, OpenAI, Google, enz.) — onboarding vraagt hierom


## Snelle setup

* ### OpenClaw installeren

### macOS / Linux

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

![Proces van installatiescript](/assets/install-script.svg)

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

* ### Onboarding uitvoeren

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

De wizard begeleidt je bij het kiezen van een modelprovider, het instellen van een API-sleutel en het configureren van de Gateway. Dit duurt ongeveer 2 minuten.

Zie [Onboarding (CLI)](</nl/start/wizard>) voor de volledige referentie.

* ### Controleren of de Gateway draait

bashCopy code
[code]
    openclaw gateway status
[/code]

Je zou moeten zien dat de Gateway luistert op poort 18789.

* ### Het dashboard openen

bashCopy code
[code]
    openclaw dashboard
[/code]

Dit opent de Control UI in je browser. Als deze laadt, werkt alles.

* ### Je eerste bericht verzenden

Typ een bericht in de Control UI-chat en je zou een AI-antwoord moeten krijgen.

Wil je liever vanaf je telefoon chatten? Het snelste kanaal om in te stellen is [Telegram](</nl/channels/telegram>) (alleen een bottoken). Zie [Kanalen](</nl/channels>) voor alle opties.

Geavanceerd: een aangepaste Control UI-build koppelen

Als je een gelokaliseerde of aangepaste dashboardbuild onderhoudt, laat `gateway.controlUi.root` verwijzen naar een map die je gebouwde statische assets en `index.html` bevat.

bashCopy code
[code]
    mkdir -p "$HOME/.openclaw/control-ui-custom"# Kopieer je gebouwde statische bestanden naar die map.
[/code]

Stel vervolgens in:

jsonCopy code
[code]
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "$HOME/.openclaw/control-ui-custom"  }}}
[/code]

Herstart de gateway en open het dashboard opnieuw:

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## Wat je hierna kunt doen

[**Een kanaal verbinden** Discord, Feishu, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo en meer. ](</nl/channels>) [**Koppelen en veiligheid** Bepaal wie je agent berichten kan sturen. ](</nl/channels/pairing>) [**De Gateway configureren** Modellen, tools, sandbox en geavanceerde instellingen. ](</nl/gateway/configuration>) [**Tools bekijken** Browser, exec, webzoekfunctie, Skills en plugins. ](</nl/tools>)

Geavanceerd: omgevingsvariabelen

Als je OpenClaw als serviceaccount uitvoert of aangepaste paden wilt:

  * `OPENCLAW_HOME` — homedirectory voor interne padresolutie
  * `OPENCLAW_STATE_DIR` — overschrijf de statusdirectory
  * `OPENCLAW_CONFIG_PATH` — overschrijf het pad naar het configbestand


Volledige referentie: [Omgevingsvariabelen](</nl/help/environment>).

## Gerelateerd

  * [Installatieoverzicht](</nl/install>)
  * [Kanalenoverzicht](</nl/channels>)
  * [Setup](</nl/start/setup>)


Was this useful?YesNo