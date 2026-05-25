---
title: Gezondheid
source_url: https://docs.openclaw.ai/nl/cli/health
scraped_at: 2026-05-25
---

# `openclaw health`

Haal de status op van de actieve Gateway.

## Opties

Vlag | Standaard | Beschrijving  
---|---|---  
`--json` | `false` | Druk machineleesbare JSON af in plaats van tekst.  
`--timeout <ms>` | `10000` | Verbindingstime-out in milliseconden.  
`--verbose` | `false` | Uitgebreide logging. Forceert een live probe en breidt uitvoer per agent uit.  
`--debug` | `false` | Alias voor `--verbose`.  
  
Voorbeelden:

bashCopy code
[code]
    openclaw healthopenclaw health --jsonopenclaw health --timeout 2500openclaw health --verboseopenclaw health --debug
[/code]

Opmerkingen:

  * Standaard vraagt `openclaw health` de actieve gateway om de health-snapshot. Wanneer de gateway al een recente gecachte snapshot heeft, kan deze die gecachte payload retourneren en op de achtergrond vernieuwen.
  * `--verbose` forceert een live probe, drukt verbindingsdetails van de gateway af en breidt de menselijk leesbare uitvoer uit over alle geconfigureerde accounts en agents.
  * Uitvoer bevat sessiestores per agent wanneer meerdere agents zijn geconfigureerd.


## Gerelateerd

  * [CLI-referentie](</nl/cli>)
  * [Gateway-status](</nl/gateway/health>)


Was this useful?YesNo