---
title: Gateway-levenscyclus op macOS
source_url: https://docs.openclaw.ai/nl/platforms/mac/child-process
scraped_at: 2026-05-25
---

De macOS-app **beheert de Gateway via launchd** standaard en start de Gateway niet als onderliggend proces. De app probeert eerst verbinding te maken met een al draaiende Gateway op de geconfigureerde poort; als er geen bereikbaar is, schakelt de app de launchd-service in via de externe `openclaw` CLI (geen ingebedde runtime). Dit geeft je betrouwbare automatische start bij inloggen en herstart bij crashes.

Onderliggend-procesmodus (Gateway rechtstreeks door de app gestart) is vandaag **niet in gebruik**. Als je nauwere koppeling met de UI nodig hebt, voer de Gateway handmatig uit in een terminal.

## Standaardgedrag (launchd)

  * De app installeert een LaunchAgent per gebruiker met het label `ai.openclaw.gateway` (of `ai.openclaw.<profile>` wanneer je `--profile`/`OPENCLAW_PROFILE` gebruikt; verouderde `com.openclaw.*` wordt ondersteund).
  * Wanneer de lokale modus is ingeschakeld, zorgt de app dat de LaunchAgent is geladen en start deze de Gateway indien nodig.
  * Logs worden geschreven naar het launchd-gatewaylogpad (zichtbaar in foutopsporingsinstellingen).


Veelgebruikte opdrachten:

bashCopy code
[code]
    launchctl kickstart -k gui/$UID/ai.openclaw.gatewaylaunchctl bootout gui/$UID/ai.openclaw.gateway
[/code]

Vervang het label door `ai.openclaw.<profile>` wanneer je een benoemd profiel gebruikt.

## Niet-ondertekende dev-builds

`scripts/restart-mac.sh --no-sign` is bedoeld voor snelle lokale builds wanneer je geen ondertekeningssleutels hebt. Om te voorkomen dat launchd naar een niet-ondertekende relay-binary wijst, doet dit het volgende:

  * Schrijft `~/.openclaw/disable-launchagent`.


Ondertekende uitvoeringen van `scripts/restart-mac.sh` wissen deze override als de marker aanwezig is. Handmatig resetten:

bashCopy code
[code]
    rm ~/.openclaw/disable-launchagent
[/code]

## Alleen-koppelen-modus

Om af te dwingen dat de macOS-app **launchd nooit installeert of beheert** , start je deze met `--attach-only` (of `--no-launchd`). Dit stelt `~/.openclaw/disable-launchagent` in, zodat de app alleen verbinding maakt met een Gateway die al draait. Je kunt hetzelfde gedrag omschakelen in foutopsporingsinstellingen.

## Externe modus

Externe modus start nooit een lokale Gateway. De app gebruikt een SSH-tunnel naar de externe host en maakt verbinding via die tunnel.

## Waarom we launchd verkiezen

  * Automatische start bij inloggen.
  * Ingebouwde semantiek voor herstarten/KeepAlive.
  * Voorspelbare logs en supervisie.


Als een echte onderliggend-procesmodus ooit opnieuw nodig is, moet die worden gedocumenteerd als een aparte, expliciete modus alleen voor ontwikkeling.

## Gerelateerd

  * [macOS-app](</nl/platforms/macos>)
  * [Gateway-runbook](</nl/gateway>)


Was this useful?YesNo