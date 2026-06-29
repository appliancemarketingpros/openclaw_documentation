---
title: Upstash Box
source_url: https://docs.openclaw.ai/nl/install/upstash
scraped_at: 2026-06-29
---

InstallHosting

Voer een permanente OpenClaw Gateway uit op Upstash Box, een beheerde Linux-omgeving met ondersteuning voor keep-alive-levenscycli.

Gebruik een SSH-tunnel voor dashboardtoegang. Stel de Gateway-poort niet rechtstreeks bloot aan het openbare internet.

## Vereisten

  * Upstash-account
  * Keep-alive Upstash Box
  * SSH-client op je lokale machine


## Een Box maken

Maak een keep-alive Box in de Upstash Console. Noteer de Box-ID, zoals `right-flamingo-14486`, en je Box-API-sleutel.

Upstash onderhoudt de actuele OpenClaw Box-walkthrough op [OpenClaw-installatie](<https://upstash.com/docs/box/guides/openclaw-setup>).

## Verbinden met een SSH-tunnel

Stuur de OpenClaw-dashboardpoort door naar je lokale machine. Gebruik je Box-API-sleutel als het SSH-wachtwoord wanneer daarom wordt gevraagd:

bashCopy code
[code]
    ssh -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

De keepalive-opties verminderen het wegvallen van inactieve tunnels tijdens onboarding.

## OpenClaw installeren

Binnen de Box:

bashCopy code
[code]
    sudo npm install -g openclaw
[/code]

## Onboarding uitvoeren

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Volg de prompts. Kopieer de dashboard-URL en token wanneer onboarding is voltooid.

## De Gateway starten

Configureer de Gateway voor het Box-netwerk en start deze op de achtergrond:

bashCopy code
[code]
    openclaw config set gateway.bind lannohup openclaw gateway > gateway.log 2>&1 &
[/code]

Open de dashboard-URL lokaal terwijl de SSH-tunnel actief is:

textCopy code
[code]
    http://127.0.0.1:18789/#token=<your-token>
[/code]

## Automatisch herstarten

Stel deze opdracht in als het Box-init-script, zodat de Gateway opnieuw start wanneer de Box start:

bashCopy code
[code]
    nohup openclaw gateway > gateway.log 2>&1 &
[/code]

## Problemen oplossen

Als SSH vastloopt tijdens onboarding, maak dan opnieuw verbinding met een schone SSH-configuratie en keepalives:

bashCopy code
[code]
    ssh -F /dev/null -o ControlMaster=no -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

Dit omzeilt verouderde lokale `~/.ssh/config`-instellingen en houdt de tunnel actief tijdens inactieve netwerkperioden.

## Gerelateerd

  * [Externe toegang](</nl/gateway/remote>)
  * [Gateway-beveiliging](</nl/gateway/security>)
  * [OpenClaw bijwerken](</nl/install/updating>)


Was this useful?YesNo

Open issue