---
title: Flussi (reindirizzamento)
source_url: https://docs.openclaw.ai/it/cli/flows
scraped_at: 2026-05-25
---

# `openclaw tasks flow`

Non esiste un comando di primo livello `openclaw flows`. L'ispezione persistente di TaskFlow si trova in `openclaw tasks flow`.

## Sottocomandi

bashCopy code
[code]
    openclaw tasks flow list   [--json] [--status <name>]openclaw tasks flow show   <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Sottocomando | Descrizione | Argomenti / opzioni  
---|---|---  
`list` | Elenca i TaskFlow monitorati. | Output leggibile dalla macchina con `--json`; filtro `--status <name>` (vedi i valori di stato sotto).  
`show` | Mostra un TaskFlow. | `<lookup>` id del flusso o chiave del proprietario; output leggibile dalla macchina con `--json`.  
`cancel` | Annulla un TaskFlow in esecuzione. | `<lookup>` id del flusso o chiave del proprietario.  
  
`<lookup>` accetta un id del flusso (restituito da `list` / `show`) oppure la chiave del proprietario del flusso (l'identificatore stabile usato dal sottosistema proprietario per tracciare il flusso).

### Valori del filtro di stato

`--status` su `list` accetta uno dei seguenti:

`queued`, `running`, `waiting`, `blocked`, `succeeded`, `failed`, `cancelled`, `lost`

## Esempi

bashCopy code
[code]
    openclaw tasks flow listopenclaw tasks flow list --status runningopenclaw tasks flow list --jsonopenclaw tasks flow show flow_abc123openclaw tasks flow show flow_abc123 --jsonopenclaw tasks flow cancel flow_abc123
[/code]

Per i concetti completi di TaskFlow e la creazione, vedi [TaskFlow](</it/automation/taskflow>). Per il comando padre `tasks`, vedi [riferimento CLI di tasks](</it/cli/tasks>).

## Correlati

  * [Riferimento CLI](</it/cli>)
  * [Automazione](</it/automation>)
  * [TaskFlow](</it/automation/taskflow>)


Was this useful?YesNo