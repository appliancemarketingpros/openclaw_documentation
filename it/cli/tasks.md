---
title: `openclaw tasks`
source_url: https://docs.openclaw.ai/it/cli/tasks
scraped_at: 2026-05-25
---

Ispeziona le attività in background persistenti e lo stato di Task Flow. Senza sottocomando, `openclaw tasks` equivale a `openclaw tasks list`.

Vedi [Attività in background](</it/automation/tasks>) per il ciclo di vita e il modello di consegna.

## Utilizzo

bashCopy code
[code]
    openclaw tasksopenclaw tasks listopenclaw tasks list --runtime acpopenclaw tasks list --status runningopenclaw tasks show <lookup>openclaw tasks notify <lookup> state_changesopenclaw tasks cancel <lookup>openclaw tasks auditopenclaw tasks maintenanceopenclaw tasks maintenance --applyopenclaw tasks flow listopenclaw tasks flow show <lookup>openclaw tasks flow cancel <lookup>
[/code]

## Opzioni radice

  * `--json`: restituisce JSON.
  * `--runtime <name>`: filtra per tipo: `subagent`, `acp`, `cron` o `cli`.
  * `--status <name>`: filtra per stato: `queued`, `running`, `succeeded`, `failed`, `timed_out`, `cancelled` o `lost`.


## Sottocomandi

### `list`

bashCopy code
[code]
    openclaw tasks list [--runtime <name>] [--status <name>] [--json]
[/code]

Elenca le attività in background tracciate, dalla più recente.

### `show`

bashCopy code
[code]
    openclaw tasks show <lookup> [--json]
[/code]

Mostra una singola attività per ID attività, ID esecuzione o chiave di sessione.

### `notify`

bashCopy code
[code]
    openclaw tasks notify <lookup> <done_only|state_changes|silent>
[/code]

Modifica la policy di notifica per un’attività in esecuzione.

### `cancel`

bashCopy code
[code]
    openclaw tasks cancel <lookup>
[/code]

Annulla un’attività in background in esecuzione.

### `audit`

bashCopy code
[code]
    openclaw tasks audit [--severity <warn|error>] [--code <name>] [--limit <n>] [--json]
[/code]

Fa emergere record di attività e Task Flow obsoleti, persi, con consegna non riuscita o altrimenti incoerenti. Le attività perse mantenute fino a `cleanupAfter` sono avvisi; le attività perse scadute o senza marcatura temporale sono errori.

### `maintenance`

bashCopy code
[code]
    openclaw tasks maintenance [--apply] [--json]
[/code]

Mostra in anteprima o applica la riconciliazione di attività e Task Flow, la marcatura per la pulizia, la rimozione, e la pulizia del registro delle sessioni di esecuzione Cron obsolete. Per le attività Cron, la riconciliazione usa i log di esecuzione/lo stato dei job persistiti prima di contrassegnare una vecchia attività attiva come `lost`, quindi le esecuzioni Cron completate non diventano falsi errori di audit solo perché lo stato del runtime Gateway in memoria non è più presente. L’audit CLI offline non è autoritativo per l’insieme dei job Cron attivi locali al processo del Gateway. Le attività CLI con un ID esecuzione/ID sorgente vengono contrassegnate come `lost` quando il loro contesto di esecuzione Gateway attivo non è più presente, anche se rimane una vecchia riga di sessione figlia. Quando applicata, la manutenzione rimuove anche le righe del registro sessioni `cron:<jobId>:run:<uuid>` più vecchie di 7 giorni, preservando i job Cron attualmente in esecuzione e lasciando inalterate le righe di sessione non Cron.

### `flow`

bashCopy code
[code]
    openclaw tasks flow list [--status <name>] [--json]openclaw tasks flow show <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Ispeziona o annulla lo stato persistente di Task Flow nel registro delle attività.

## Correlati

  * [Riferimento CLI](</it/cli>)
  * [Attività in background](</it/automation/tasks>)


Was this useful?YesNo