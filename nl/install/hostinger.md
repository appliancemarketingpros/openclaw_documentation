---
title: Hostinger
source_url: https://docs.openclaw.ai/nl/install/hostinger
scraped_at: 2026-05-25
---

Draai een permanente OpenClaw Gateway op [Hostinger](<https://www.hostinger.com/openclaw>) via een beheerde implementatie met **1 klik** of een **VPS** -installatie.

## Vereisten

  * Hostinger-account ([registreren](<https://www.hostinger.com/openclaw>))
  * Ongeveer 5-10 minuten


## Optie A: OpenClaw met 1 klik

De snelste manier om aan de slag te gaan. Hostinger verzorgt infrastructuur, Docker en automatische updates.

* ### Purchase and launch

  1. Kies op de [Hostinger OpenClaw-pagina](<https://www.hostinger.com/openclaw>) een beheerd OpenClaw-abonnement en rond het afrekenen af.


* ### Select a messaging channel

Kies een of meer kanalen om te verbinden:

  * **WhatsApp** \-- scan de QR-code die in de installatiewizard wordt weergegeven.
  * **Telegram** \-- plak het bottoken van [BotFather](<https://t.me/BotFather>).


* ### Complete installation

Klik op **Finish** om de instantie te implementeren. Zodra deze gereed is, open je het OpenClaw-dashboard via **OpenClaw Overview** in hPanel.

## Optie B: OpenClaw op VPS

Meer controle over je server. Hostinger implementeert OpenClaw via Docker op je VPS en jij beheert het via de **Docker Manager** in hPanel.

* ### Purchase a VPS

  1. Kies op de [Hostinger OpenClaw-pagina](<https://www.hostinger.com/openclaw>) een OpenClaw op VPS-abonnement en rond het afrekenen af.


* ### Configure OpenClaw

Zodra de VPS is ingericht, vul je de configuratievelden in:

  * **Gateway-token** \-- automatisch gegenereerd; bewaar dit voor later gebruik.
  * **WhatsApp-nummer** \-- je nummer met landcode (optioneel).
  * **Telegram-bottoken** \-- van [BotFather](<https://t.me/BotFather>) (optioneel).
  * **API-sleutels** \-- alleen nodig als je tijdens het afrekenen geen Ready-to-Use AI-credits hebt geselecteerd.


* ### Start OpenClaw

Klik op **Deploy**. Zodra OpenClaw draait, open je het OpenClaw-dashboard vanuit hPanel door op **Open** te klikken.

Logs, herstarts en updates worden rechtstreeks beheerd vanuit de Docker Manager-interface in hPanel. Druk voor updates op **Update** in Docker Manager; daarmee wordt de nieuwste image opgehaald.

## Controleer je installatie

Stuur "Hi" naar je assistent op het kanaal dat je hebt verbonden. OpenClaw antwoordt en begeleidt je door de initiële voorkeuren.

## Probleemoplossing

**Dashboard wordt niet geladen** \-- Wacht een paar minuten totdat de container klaar is met inrichten. Controleer de Docker Manager-logs in hPanel.

**Docker-container blijft herstarten** \-- Open de Docker Manager-logs en zoek naar configuratiefouten (ontbrekende tokens, ongeldige API-sleutels).

**Telegram-bot reageert niet** \-- Stuur je koppelcodebericht rechtstreeks vanuit Telegram als bericht in je OpenClaw-chat om de verbinding te voltooien.

## Volgende stappen

  * [Kanalen](</nl/channels>) \-- verbind Telegram, WhatsApp, Discord en meer
  * [Gateway-configuratie](</nl/gateway/configuration>) \-- alle configuratieopties


## Gerelateerd

  * [Installatieoverzicht](</nl/install>)
  * [VPS-hosting](</nl/vps>)
  * [DigitalOcean](</nl/install/digitalocean>)


Was this useful?YesNo