---
title: Inloggen via browser
source_url: https://docs.openclaw.ai/nl/tools/browser-login
scraped_at: 2026-05-25
---

## Handmatig inloggen (aanbevolen)

Wanneer een site inloggen vereist, **log dan handmatig in** in het **host** browserprofiel (de openclaw-browser).

Geef het model **niet** je inloggegevens. Geautomatiseerde logins activeren vaak anti-botbeveiliging en kunnen het account blokkeren.

Terug naar de hoofddocumentatie voor de browser: [Browser](</nl/tools/browser>).

## Welk Chrome-profiel wordt gebruikt?

OpenClaw bestuurt een **speciaal Chrome-profiel** (genaamd `openclaw`, oranje getinte UI). Dit staat los van je dagelijkse browserprofiel.

Voor aanroepen van de browsertool door agents:

  * Standaardkeuze: de agent moet zijn geïsoleerde `openclaw`-browser gebruiken.
  * Gebruik `profile="user"` alleen wanneer bestaande ingelogde sessies belangrijk zijn en de gebruiker achter de computer zit om op een eventuele koppelingsprompt te klikken of deze goed te keuren.
  * Als je meerdere gebruikersbrowserprofielen hebt, geef het profiel dan expliciet op in plaats van te gokken.


Twee eenvoudige manieren om toegang te krijgen:

  1. **Vraag de agent om de browser te openen** en log daarna zelf in.
  2. **Open deze via de CLI** :

bashCopy code
[code]
    openclaw browser startopenclaw browser open https://x.com
[/code]

Als je meerdere profielen hebt, geef dan `--browser-profile <name>` mee (de standaard is `openclaw`).

## X/Twitter: aanbevolen flow

  * **Lezen/zoeken/threads:** gebruik de **host** browser (handmatig inloggen).
  * **Updates posten:** gebruik de **host** browser (handmatig inloggen).


## Sandboxing + toegang tot hostbrowser

Gesandboxte browsersessies activeren **vaker** botdetectie. Voor X/Twitter (en andere strikte sites) geef je de voorkeur aan de **host** browser.

Als de agent gesandboxed is, gebruikt de browsertool standaard de sandbox. Om hostbesturing toe te staan:

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "non-main",        browser: {          allowHostControl: true,        },      },    },  },}
[/code]

Open daarna zelf de hostbrowser (CLI-aanroepen worden altijd uitgevoerd tegen de hostbrowser):

bashCopy code
[code]
    openclaw browser open https://x.com --browser-profile openclaw
[/code]

De `browser`-toolaanroepen van de agent kunnen dan de host als doel gebruiken zodra `sandbox.browser.allowHostControl: true` is ingesteld. Je kunt ook sandboxing uitschakelen voor de agent die updates post.

## Gerelateerd

  * [Browser](</nl/tools/browser>)
  * [Probleemoplossing voor Browser op Linux](</nl/tools/browser-linux-troubleshooting>)
  * [Probleemoplossing voor Browser met WSL2](</nl/tools/browser-wsl2-windows-remote-cdp-troubleshooting>)


Was this useful?YesNo