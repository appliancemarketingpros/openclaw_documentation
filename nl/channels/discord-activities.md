---
title: Discord-activiteiten
source_url: https://docs.openclaw.ai/nl/channels/discord-activities
scraped_at: 2026-10-12
---

ChannelsMainstream messaging

Met Discord Activities kan een agent een interactieve, zelfstandige HTML-widget in het huidige Discord-kanaal plaatsen. Het bericht bevat een knop **Open widget** ; als je erop klikt, wordt de widget binnen Discord geopend.

De functie is standaard uitgeschakeld. OpenClaw registreert de HTTP-routes voor de Activity, de agenttool `show_widget` en de handler voor de startknop alleen wanneer `channels.discord.activities` aanwezig is en een clientgeheim kan worden gevonden. De verouderde alias `discord_widget` blijft nog één release beschikbaar.

## Vereisten

  * een bestaande [OpenClaw Discord-bot](</nl/channels/discord>)
  * een openbare HTTPS-hostnaam die de OpenClaw Gateway bereikt
  * toestemming om Activities en OAuth2 te configureren voor de Discord-applicatie van de bot


Elke HTTPS-reverseproxy of tunnel werkt. Een benoemde Cloudflare Tunnel biedt een stabiele hostnaam zonder de Gateway-poort rechtstreeks openbaar te maken.

yamlCopy code
[code]
    # ~/.cloudflared/config.ymltunnel: openclaw-discordcredentials-file: /home/you/.cloudflared/TUNNEL-ID.jsoningress:  - hostname: openclaw.example.com    service: http://127.0.0.1:18789  - service: http_status:404
[/code]

bashCopy code
[code]
    cloudflared tunnel logincloudflared tunnel create openclaw-discordcloudflared tunnel route dns openclaw-discord openclaw.example.comcloudflared tunnel run openclaw-discord
[/code]

Laat de normale Gateway-authenticatie ingeschakeld. Alleen het Activity-voorvoegsel is openbaar en de plugin valideert zelf OAuth, het lidmaatschap van de Activity-instantie, de kanaalkoppeling, sessies en eenmalige documentmogelijkheden.

## Configuratie

* ### Stel de gateway beschikbaar via HTTPS

Start je tunnel of reverseproxy en controleer of `https://openclaw.example.com/discord/activity/` de Gateway bereikt nadat de Activities-configuratie is toegevoegd. Vervang de voorbeeldhostnaam door je eigen hostnaam.

* ### Schakel Activities in Discord in

Open de bestaande botapplicatie in de [Discord Developer Portal](<https://discord.com/developers/applications>). Open **Activities** , schakel Activities in en maak een URL-toewijzing:

  * voorvoegsel: `ROOT` (`/`)
  * doel: `openclaw.example.com/discord/activity`


Het doel is de openbare hostnaam plus `/discord/activity`, zonder afsluitende slash.

* ### Kopieer het OAuth2-clientgeheim

Open **OAuth2** in de Developer Portal. Discord vereist minstens één omleidings-URI. Voeg daarom een lokale tijdelijke aanduiding toe, zoals het loopbackadres, als de applicatie er nog geen heeft; de Embedded App SDK verwerkt de retourstroom van de Activity. Kopieer of herstel het clientgeheim van de applicatie. Behandel dit als een aanmeldgegeven: plak het niet in chats, logboeken of een vastgelegd configuratiebestand.

* ### Configureer OpenClaw

Voeg één blok toe aan het Discord-account dat widgets moet aanbieden:

json5Copy code
[code]
    {  channels: {    discord: {      token: "${DISCORD_BOT_TOKEN}",      activities: {        clientSecret: "${DISCORD_CLIENT_SECRET}",        // Optioneel. Standaard wordt de bij het opstarten verkregen applicatie-ID van de bot gebruikt.        applicationId: "YOUR_DISCORD_APPLICATION_ID",      },    },  },}
[/code]

Je mag `clientSecret` uit het blok weglaten wanneer `DISCORD_CLIENT_SECRET` is ingesteld. Het blok zelf moet aanwezig blijven om deze functie in te schakelen.

De normale instellingen voor Discord-toegang blijven afzonderlijk. `allowFrom` bepaalt bijvoorbeeld nog steeds wie de agent een DM kan sturen; deze instelling bepaalt niet wie een widget kan openen die al in een kanaal is geplaatst.

* ### Start opnieuw en test

Start de Gateway opnieuw. Vraag de agent in een Discord-gesprek om een interactieve widget weer te geven. De agent roept `show_widget` aan; klik op **Open widget** in het geplaatste bericht.

## Beveiligingsmodel

  * OAuth identificeert de Discord-gebruiker voordat widgetmetadata worden geretourneerd.
  * De Get Activity Instance-API van Discord moet bevestigen dat de OAuth-gebruiker aanwezig is in de huidige Activity-instantie. Het kanaal van de instantie moet overeenkomen met het kanaal waarin de widget is geplaatst.
  * Iedereen die van Discord toegang tot dat kanaal krijgt, kan de bijbehorende widgets openen. Gebruik Discord-kanaalmachtigingen om de doelgroep te beperken. Toelatingslijsten voor OpenClaw-opdrachten en DM's verlenen of verwijderen geen toegang tot kanaalinhoud die al is geplaatst.
  * OAuth-sessies verlopen na 15 minuten. Documentmogelijkheden van widgets verlopen na 60 seconden en werken één keer.
  * Widgets verlopen na zeven dagen, waarbij per Discord-plugininstantie maximaal 64 widgets worden bewaard.
  * De HTML van widgets wordt door je agent geschreven en moet als vertrouwde inhoud worden behandeld. Neem geen geheimen op die een widget met fouten niet zou mogen blootstellen.
  * De widget kan binnen het eigen geneste frame navigeren. Het iframe `sandbox="allow-scripts"` blokkeert navigatie op het hoogste niveau, pop-ups en toegang tot dezelfde oorsprong, terwijl het Content Security Policy ervan netwerkverbindingen en externe bronnen blokkeert. Deze maatregelen bieden gelaagde beveiliging, maar vormen geen beveiligingsgrens tegen de agent die de widget heeft geschreven.
  * Wanneer Activities is uitgeschakeld, wordt `/discord/activity` helemaal niet geregistreerd.


De openbare Activity-shell en route voor tokenuitwisseling worden via je tunnel bereikbaar wanneer de functie is ingeschakeld. Ze stellen geen widget-HTML beschikbaar zonder een geldige OAuth-sessie en een eenmalige documentmogelijkheid.

## Problemen oplossen

### De Activity meldt “Gateway offline”

  * controleer of de tunnel actief is en doorstuurt naar de daadwerkelijke bindpoort van de Gateway
  * controleer of het doel in de Developer Portal `/discord/activity` bevat
  * start de Gateway opnieuw nadat je de configuratie van Discord of OpenClaw hebt gewijzigd
  * controleer de Gateway-logboeken op de waarschuwing van één regel over een ontbrekend Activities-clientgeheim


### Discord opent een lege pagina of meldt `blocked:csp`

  * controleer of de URL-toewijzing `ROOT` gebruikt en geen tweede `/discord/activity`-segment toevoegt
  * controleer of de shell, `shell.js` en de SDK-module allemaal via de Discord-proxy worden geretourneerd
  * controleer de Gateway-logboeken op verzoeken onder `/discord/activity/`


Netwerkverzoeken van widgets worden opzettelijk geblokkeerd. Neem alle CSS, JavaScript, afbeeldingen en gegevens die de widget nodig heeft rechtstreeks in de widget op.

### “Widget unavailable”

Start de widget met de knop vanuit het kanaal waarin de agent deze heeft geplaatst. OpenClaw houdt het starten na een klik aan de serverzijde bij, zodat een nieuwe startregistratie de exacte widget kan vinden, zelfs wanneer Discord de aangepaste ID van de knop weglaat of beschadigt. Wanneer noch de aangepaste ID noch een startregistratie kan worden gevonden, opent OpenClaw de meest recent geplaatste actieve widget in dat kanaal. Oudere widgets blijven bereikbaar via knoppen die hun aangepaste ID behouden.

### “You cannot launch Activities in this channel”

Discord start Activities niet vanuit threads van forumberichten. OpenClaw kan het widgetbericht en de knop daar plaatsen, maar start de Activity in plaats daarvan vanuit een normaal tekstkanaal. Deze beperking is afkomstig van Discord, niet van OpenClaw.

Was this useful?YesNo

Open issue