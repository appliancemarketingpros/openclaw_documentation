---
title: Logboeken
source_url: https://docs.openclaw.ai/nl/cli/logs
scraped_at: 2026-05-25
---

# `openclaw logs`

Volg Gateway-bestandslogs live via RPC (werkt in externe modus).

Gerelateerd:

  * Overzicht van logregistratie: [Logregistratie](</nl/logging>)
  * Gateway-CLI: [gateway](</nl/cli/gateway>)


## Opties

  * `--limit <n>`: maximaal aantal logregels om terug te geven (standaard `200`)
  * `--max-bytes <n>`: maximaal aantal bytes om uit het logbestand te lezen (standaard `250000`)
  * `--follow`: volg de logstream
  * `--interval <ms>`: pollinginterval tijdens volgen (standaard `1000`)
  * `--json`: geef regelgescheiden JSON-gebeurtenissen uit
  * `--plain`: plattetekstuitvoer zonder gestileerde opmaak
  * `--no-color`: schakel ANSI-kleuren uit
  * `--local-time`: geef tijdstempels weer in je lokale tijdzone


## Gedeelde Gateway-RPC-opties

`openclaw logs` accepteert ook de standaard Gateway-clientvlaggen:

  * `--url <url>`: Gateway-WebSocket-URL
  * `--token <token>`: Gateway-token
  * `--timeout <ms>`: time-out in ms (standaard `30000`)
  * `--expect-final`: wacht op een definitieve reactie wanneer de Gateway-aanroep door een agent wordt ondersteund


Wanneer je `--url` meegeeft, past de CLI configuratie- of omgevingsreferenties niet automatisch toe. Voeg `--token` expliciet toe als de doel-Gateway authenticatie vereist.

## Voorbeelden

bashCopy code
[code]
    openclaw logsopenclaw logs --followopenclaw logs --follow --interval 2000openclaw logs --limit 500 --max-bytes 500000openclaw logs --jsonopenclaw logs --plainopenclaw logs --no-coloropenclaw logs --limit 500openclaw logs --local-timeopenclaw logs --follow --local-timeopenclaw logs --url ws://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"
[/code]

## Opmerkingen

  * Gebruik `--local-time` om tijdstempels weer te geven in je lokale tijdzone.
  * Als de impliciete local loopback-Gateway om koppeling vraagt, sluit tijdens het verbinden, of een time-out krijgt voordat `logs.tail` antwoordt, valt `openclaw logs` automatisch terug op het geconfigureerde Gateway-bestandslog. Expliciete `--url`-doelen gebruiken deze fallback niet.
  * Bij gebruik van `--follow` leiden tijdelijke gateway-verbindingsverbrekingen (WebSocket sluiten, time-out, wegvallende verbinding) tot automatische herverbinding met exponentiële back-off (tot 8 nieuwe pogingen, begrensd op 30 s tussen pogingen). Bij elke nieuwe poging wordt een waarschuwing naar stderr geschreven, en zodra een poll slaagt wordt een melding `[logs] gateway reconnected` geschreven. In `--json`-modus worden zowel de waarschuwing voor de nieuwe poging als de overgang naar herverbinding als `{"type":"notice"}`-records naar stderr uitgevoerd. Niet-herstelbare fouten (authenticatiefout, ongeldige configuratie) sluiten nog steeds onmiddellijk af.


## Gerelateerd

  * [CLI-referentie](</nl/cli>)
  * [Gateway-logregistratie](</nl/gateway/logging>)


Was this useful?YesNo