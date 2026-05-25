---
title: Stromen (doorverwijzing)
source_url: https://docs.openclaw.ai/nl/cli/flows
scraped_at: 2026-05-25
---

# `openclaw tasks flow`

Er is geen top-level `openclaw flows`-commando. Persistente TaskFlow-inspectie bevindt zich onder `openclaw tasks flow`.

## Subcommando's

bashCopy code
[code]
    openclaw tasks flow list   [--json] [--status <name>]openclaw tasks flow show   <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Subcommando | Beschrijving | Argumenten / opties  
---|---|---  
`list` | Geef bijgehouden TaskFlows weer. | `--json` machinaal leesbare uitvoer; `--status <name>`-filter (zie statuswaarden hieronder).  
`show` | Toon één TaskFlow. | `<lookup>` flow-id of owner key; `--json` machinaal leesbare uitvoer.  
`cancel` | Annuleer een actieve TaskFlow. | `<lookup>` flow-id of owner key.  
  
`<lookup>` accepteert een flow-id (geretourneerd door `list` / `show`) of de owner key van de flow (de stabiele identificatie die het eigenaarssubsysteem gebruikt om de flow te volgen).

### Statusfilterwaarden

`--status` bij `list` accepteert een van:

`queued`, `running`, `waiting`, `blocked`, `succeeded`, `failed`, `cancelled`, `lost`

## Voorbeelden

bashCopy code
[code]
    openclaw tasks flow listopenclaw tasks flow list --status runningopenclaw tasks flow list --jsonopenclaw tasks flow show flow_abc123openclaw tasks flow show flow_abc123 --jsonopenclaw tasks flow cancel flow_abc123
[/code]

Zie [TaskFlow](</nl/automation/taskflow>) voor volledige TaskFlow-concepten en authoring. Zie [tasks CLI-referentie](</nl/cli/tasks>) voor het bovenliggende `tasks`-commando.

## Gerelateerd

  * [CLI-referentie](</nl/cli>)
  * [Automatisering](</nl/automation>)
  * [TaskFlow](</nl/automation/taskflow>)


Was this useful?YesNo