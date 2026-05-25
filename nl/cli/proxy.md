---
title: Proxy
source_url: https://docs.openclaw.ai/nl/cli/proxy
scraped_at: 2026-05-25
---

# `openclaw proxy`

Valideer door de operator beheerde proxyrouting, of voer de lokale expliciete debugproxy uit en inspecteer vastgelegd verkeer.

Gebruik `validate` om een door de operator beheerde forward proxy vooraf te controleren voordat OpenClaw-proxyrouting wordt ingeschakeld. De andere opdrachten zijn foutopsporingstools voor onderzoek op transportniveau: ze kunnen een lokale proxy starten, een onderliggende opdracht uitvoeren met vastlegging ingeschakeld, vastleggingssessesies weergeven, veelvoorkomende verkeerspatronen opvragen, vastgelegde blobs lezen en lokale vastleggingsgegevens opschonen.

## Opdrachten

bashCopy code
[code]
    openclaw proxy start [--host <host>] [--port <port>]openclaw proxy run [--host <host>] [--port <port>] -- <cmd...>openclaw proxy validate [--json] [--proxy-url <url>] [--allowed-url <url>] [--denied-url <url>] [--apns-reachable] [--apns-authority <url>] [--timeout-ms <ms>]openclaw proxy coverageopenclaw proxy sessions [--limit <count>]openclaw proxy query --preset <name> [--session <id>]openclaw proxy blob --id <blobId>openclaw proxy purge
[/code]

## Valideren

`openclaw proxy validate` controleert de effectieve door de operator beheerde proxy-URL uit `--proxy-url`, configuratie of `OPENCLAW_PROXY_URL`. Het meldt een configuratieprobleem wanneer geen proxy is ingeschakeld en geconfigureerd; gebruik `--proxy-url` voor een eenmalige voorcontrole voordat je de configuratie wijzigt. Standaard wordt gecontroleerd of een openbare bestemming via de proxy slaagt en dat de proxy geen tijdelijke loopback-canary kan bereiken. Aangepaste geweigerde bestemmingen zijn fail-closed: HTTP-antwoorden en dubbelzinnige transportfouten mislukken beide, tenzij je een implementatiespecifiek weigeringssignaal apart kunt verifiëren. Voeg `--apns-reachable` toe om ook een APNs HTTP/2 CONNECT-tunnel via de proxy te openen en te bevestigen dat sandbox-APNs antwoordt; de probe gebruikt een opzettelijk ongeldige providertoken, dus een APNs `403 InvalidProviderToken`-antwoord is een succesvol bereikbaarheidsignaal.

Opties:

  * `--json`: druk machineleesbare JSON af.
  * `--proxy-url <url>`: valideer deze proxy-URL in plaats van configuratie of omgeving.
  * `--allowed-url <url>`: voeg een bestemming toe die naar verwachting via de proxy slaagt. Herhaal om meerdere bestemmingen te controleren.
  * `--denied-url <url>`: voeg een bestemming toe die naar verwachting door de proxy wordt geblokkeerd. Herhaal om meerdere bestemmingen te controleren.
  * `--apns-reachable`: controleer ook of sandbox-APNs HTTP/2 bereikbaar is via de proxy.
  * `--apns-authority <url>`: APNs-authority om te proben met `--apns-reachable` (standaard `https://api.sandbox.push.apple.com`; productie is `https://api.push.apple.com`).
  * `--timeout-ms <ms>`: time-out per aanvraag in milliseconden.


Zie [Netwerkproxy](</nl/security/network-proxy>) voor implementatierichtlijnen en weigeringssemantiek.

## Querypresets

`openclaw proxy query --preset <name>` accepteert:

  * `double-sends`
  * `retry-storms`
  * `cache-busting`
  * `ws-duplicate-frames`
  * `missing-ack`
  * `error-bursts`


## Opmerkingen

  * `start` gebruikt standaard `127.0.0.1`, tenzij `--host` is ingesteld.
  * `run` start een lokale debugproxy en voert daarna de opdracht na `--` uit.
  * De directe upstream-forwarding van de debugproxy opent upstream-sockets voor diagnostiek. Wanneer de beheerde proxymodus van OpenClaw actief is, is directe forwarding voor proxy-aanvragen en CONNECT-tunnels standaard uitgeschakeld; stel `OPENCLAW_DEBUG_PROXY_ALLOW_DIRECT_CONNECT_WITH_MANAGED_PROXY=1` alleen in voor goedgekeurde lokale diagnostiek.
  * `validate` sluit af met code 1 wanneer proxyconfiguratie of bestemmingscontroles mislukken.
  * Vastleggingen zijn lokale foutopsporingsgegevens; gebruik `openclaw proxy purge` wanneer je klaar bent.


## Gerelateerd

  * [CLI-referentie](</nl/cli>)
  * [Netwerkproxy](</nl/security/network-proxy>)
  * [Vertrouwde proxyauthenticatie](</nl/gateway/trusted-proxy-auth>)


Was this useful?YesNo