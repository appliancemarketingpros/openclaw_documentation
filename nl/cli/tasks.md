---
title: `openclaw tasks`
source_url: https://docs.openclaw.ai/nl/cli/tasks
scraped_at: 2026-05-25
---

Inspecteer duurzame achtergrondtaken en Task Flow-status. Zonder subcommando is `openclaw tasks` gelijk aan `openclaw tasks list`.

Zie [Achtergrondtaken](</nl/automation/tasks>) voor de levenscyclus en het bezorgmodel.

## Gebruik

bashCopy code
[code]
    openclaw tasksopenclaw tasks listopenclaw tasks list --runtime acpopenclaw tasks list --status runningopenclaw tasks show <lookup>openclaw tasks notify <lookup> state_changesopenclaw tasks cancel <lookup>openclaw tasks auditopenclaw tasks maintenanceopenclaw tasks maintenance --applyopenclaw tasks flow listopenclaw tasks flow show <lookup>openclaw tasks flow cancel <lookup>
[/code]

## Hoofdopties

  * `--json`: voert JSON uit.
  * `--runtime <name>`: filter op soort: `subagent`, `acp`, `cron` of `cli`.
  * `--status <name>`: filter op status: `queued`, `running`, `succeeded`, `failed`, `timed_out`, `cancelled` of `lost`.


## Subcommando's

### `list`

bashCopy code
[code]
    openclaw tasks list [--runtime <name>] [--status <name>] [--json]
[/code]

Geeft bijgehouden achtergrondtaken weer, nieuwste eerst.

### `show`

bashCopy code
[code]
    openclaw tasks show <lookup> [--json]
[/code]

Toont één taak op taak-ID, run-ID of sessiesleutel.

### `notify`

bashCopy code
[code]
    openclaw tasks notify <lookup> <done_only|state_changes|silent>
[/code]

Wijzigt het meldingsbeleid voor een actieve taak.

### `cancel`

bashCopy code
[code]
    openclaw tasks cancel <lookup>
[/code]

Annuleert een actieve achtergrondtaak.

### `audit`

bashCopy code
[code]
    openclaw tasks audit [--severity <warn|error>] [--code <name>] [--limit <n>] [--json]
[/code]

Brengt verouderde, verloren, met mislukte bezorging of anderszins inconsistente taak- en Task Flow-records naar voren. Verloren taken die tot `cleanupAfter` worden bewaard, zijn waarschuwingen; verlopen of niet-gestempelde verloren taken zijn fouten.

### `maintenance`

bashCopy code
[code]
    openclaw tasks maintenance [--apply] [--json]
[/code]

Geeft een voorvertoning van taak- en Task Flow-reconciliatie, opruimstempeling, snoeien en opschoning van het sessieregister voor verouderde cron-runs, of past deze toe. Voor cron-taken gebruikt reconciliatie permanente runlogs/taakstatus voordat een oude actieve taak als `lost` wordt gemarkeerd, zodat voltooide cron-runs geen valse auditfouten worden alleen omdat de in-memory Gateway-runtime-status verdwenen is. Offline CLI-audit is niet gezaghebbend voor de proceslokale actieve-taakset van cron in de Gateway. CLI-taken met een run-ID/bron-ID worden als `lost` gemarkeerd wanneer hun live Gateway-runcontext verdwenen is, zelfs als er nog een oude onderliggende sessierij bestaat. Wanneer toegepast, snoeit onderhoud ook `cron:<jobId>:run:<uuid>`-sessieregisterrijen die ouder zijn dan 7 dagen, terwijl momenteel actieve cron-taken behouden blijven en niet-cron-sessierijen onaangeroerd blijven.

### `flow`

bashCopy code
[code]
    openclaw tasks flow list [--status <name>] [--json]openclaw tasks flow show <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Inspecteert of annuleert duurzame Task Flow-status onder het taakregister.

## Gerelateerd

  * [CLI-referentie](</nl/cli>)
  * [Achtergrondtaken](</nl/automation/tasks>)


Was this useful?YesNo