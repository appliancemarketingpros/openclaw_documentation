---
title: `openclaw commitments`
source_url: https://docs.openclaw.ai/it/cli/commitments
scraped_at: 2026-05-25
---

Elenca e gestisce gli impegni di follow-up dedotti.

Gli impegni sono memorie di follow-up facoltative e di breve durata create dal contesto della conversazione. Consulta [Impegni dedotti](</it/concepts/commitments>) per la guida concettuale.

Senza sottocomando, `openclaw commitments` elenca gli impegni in sospeso.

## Utilizzo

bashCopy code
[code]
    openclaw commitments [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments list [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments dismiss <id...> [--json]
[/code]

## Opzioni

  * `--all`: mostra tutti gli stati invece dei soli impegni in sospeso.
  * `--agent <id>`: filtra per un singolo ID agente.
  * `--status <status>`: filtra per stato. Valori: `pending`, `sent`, `dismissed`, `snoozed` o `expired`.
  * `--json`: produce JSON leggibile dalle macchine.


## Esempi

Elenca gli impegni in sospeso:

bashCopy code
[code]
    openclaw commitments
[/code]

Elenca ogni impegno archiviato:

bashCopy code
[code]
    openclaw commitments --all
[/code]

Filtra per un singolo agente:

bashCopy code
[code]
    openclaw commitments --agent main
[/code]

Trova gli impegni posticipati:

bashCopy code
[code]
    openclaw commitments --status snoozed
[/code]

Ignora uno o più impegni:

bashCopy code
[code]
    openclaw commitments dismiss cm_abc123 cm_def456
[/code]

Esporta come JSON:

bashCopy code
[code]
    openclaw commitments --all --json
[/code]

## Output

L'output testuale include:

  * ID dell'impegno
  * stato
  * tipo
  * prima scadenza utile
  * ambito
  * testo di check-in suggerito


L'output JSON include anche il percorso dell'archivio degli impegni e i record archiviati completi.

## Correlati

  * [Impegni dedotti](</it/concepts/commitments>)
  * [Panoramica della memoria](</it/concepts/memory>)
  * [Heartbeat](</it/gateway/heartbeat>)
  * [Attività pianificate](</it/automation/cron-jobs>)


Was this useful?YesNo