---
title: `openclaw commitments`
source_url: https://docs.openclaw.ai/nl/cli/commitments
scraped_at: 2026-05-25
---

Lijst en beheer afgeleide vervolgtoezeggingen.

Toezeggingen zijn opt-in, kortlevende vervolgherinneringen die worden gemaakt op basis van gesprekscontext. Zie [Afgeleide toezeggingen](</nl/concepts/commitments>) voor de conceptuele gids.

Zonder subopdracht toont `openclaw commitments` openstaande toezeggingen.

## Gebruik

bashCopy code
[code]
    openclaw commitments [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments list [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments dismiss <id...> [--json]
[/code]

## Opties

  * `--all`: toon alle statussen in plaats van alleen openstaande toezeggingen.
  * `--agent <id>`: filter op een agent-id.
  * `--status <status>`: filter op status. Waarden: `pending`, `sent`, `dismissed`, `snoozed` of `expired`.
  * `--json`: voer machineleesbare JSON uit.


## Voorbeelden

Openstaande toezeggingen weergeven:

bashCopy code
[code]
    openclaw commitments
[/code]

Elke opgeslagen toezegging weergeven:

bashCopy code
[code]
    openclaw commitments --all
[/code]

Filteren op een agent:

bashCopy code
[code]
    openclaw commitments --agent main
[/code]

Gesnoozede toezeggingen vinden:

bashCopy code
[code]
    openclaw commitments --status snoozed
[/code]

Een of meer toezeggingen negeren:

bashCopy code
[code]
    openclaw commitments dismiss cm_abc123 cm_def456
[/code]

Exporteren als JSON:

bashCopy code
[code]
    openclaw commitments --all --json
[/code]

## Uitvoer

Tekstuitvoer bevat:

  * toezegging-id
  * status
  * soort
  * vroegste geplande tijd
  * bereik
  * voorgestelde tekst voor inchecken


JSON-uitvoer bevat ook het pad van de toezeggingenopslag en de volledige opgeslagen records.

## Gerelateerd

  * [Afgeleide toezeggingen](</nl/concepts/commitments>)
  * [Overzicht van Memory](</nl/concepts/memory>)
  * [Heartbeat](</nl/gateway/heartbeat>)
  * [Geplande taken](</nl/automation/cron-jobs>)


Was this useful?YesNo