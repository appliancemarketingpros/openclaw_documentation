---
title: `openclaw tasks`
source_url: https://docs.openclaw.ai/de/cli/tasks
scraped_at: 2026-05-25
---

Dauerhafte Hintergrundaufgaben und den Task Flow-Zustand prüfen. Ohne Unterbefehl ist `openclaw tasks` gleichbedeutend mit `openclaw tasks list`.

Siehe [Hintergrundaufgaben](</de/automation/tasks>) für das Lebenszyklus- und Zustellmodell.

## Verwendung

bashCopy code
[code]
    openclaw tasksopenclaw tasks listopenclaw tasks list --runtime acpopenclaw tasks list --status runningopenclaw tasks show <lookup>openclaw tasks notify <lookup> state_changesopenclaw tasks cancel <lookup>openclaw tasks auditopenclaw tasks maintenanceopenclaw tasks maintenance --applyopenclaw tasks flow listopenclaw tasks flow show <lookup>openclaw tasks flow cancel <lookup>
[/code]

## Root-Optionen

  * `--json`: JSON ausgeben.
  * `--runtime <name>`: Nach Art filtern: `subagent`, `acp`, `cron` oder `cli`.
  * `--status <name>`: Nach Status filtern: `queued`, `running`, `succeeded`, `failed`, `timed_out`, `cancelled` oder `lost`.


## Unterbefehle

### `list`

bashCopy code
[code]
    openclaw tasks list [--runtime <name>] [--status <name>] [--json]
[/code]

Listet erfasste Hintergrundaufgaben, neueste zuerst.

### `show`

bashCopy code
[code]
    openclaw tasks show <lookup> [--json]
[/code]

Zeigt eine Aufgabe anhand von Aufgaben-ID, Run-ID oder Sitzungsschlüssel an.

### `notify`

bashCopy code
[code]
    openclaw tasks notify <lookup> <done_only|state_changes|silent>
[/code]

Ändert die Benachrichtigungsrichtlinie für eine laufende Aufgabe.

### `cancel`

bashCopy code
[code]
    openclaw tasks cancel <lookup>
[/code]

Bricht eine laufende Hintergrundaufgabe ab.

### `audit`

bashCopy code
[code]
    openclaw tasks audit [--severity <warn|error>] [--code <name>] [--limit <n>] [--json]
[/code]

Zeigt veraltete, verlorene, zustellungsfehlgeschlagene oder anderweitig inkonsistente Aufgaben- und Task Flow-Datensätze an. Bis `cleanupAfter` aufbewahrte verlorene Aufgaben sind Warnungen; abgelaufene oder nicht gestempelte verlorene Aufgaben sind Fehler.

### `maintenance`

bashCopy code
[code]
    openclaw tasks maintenance [--apply] [--json]
[/code]

Zeigt eine Vorschau der Aufgaben- und Task Flow-Abstimmung, Bereinigungsstempelung, Ausdünnung und Bereinigung der Sitzungsregistrierung für veraltete Cron-Runs an oder wendet sie an. Für Cron-Aufgaben verwendet die Abstimmung persistierte Run-Protokolle bzw. den Job-Zustand, bevor eine alte aktive Aufgabe als `lost` markiert wird, sodass abgeschlossene Cron-Runs nicht zu falschen Audit-Fehlern werden, nur weil der speicherinterne Gateway-Laufzeitstatus nicht mehr vorhanden ist. Offline-CLI-Audit ist nicht maßgeblich für die prozesslokale aktive Cron-Job-Menge des Gateway. CLI-Aufgaben mit Run-ID/Quell-ID werden als `lost` markiert, wenn ihr Live-Gateway-Run-Kontext nicht mehr vorhanden ist, selbst wenn eine alte Kind-Sitzungszeile bestehen bleibt. Bei Anwendung entfernt die Wartung außerdem Sitzungsregistrierungszeilen der Form `cron:<jobId>:run:<uuid>`, die älter als 7 Tage sind, bewahrt dabei aktuell laufende Cron-Jobs und lässt Nicht-Cron-Sitzungszeilen unverändert.

### `flow`

bashCopy code
[code]
    openclaw tasks flow list [--status <name>] [--json]openclaw tasks flow show <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Prüft oder bricht dauerhaften Task Flow-Zustand im Aufgaben-Ledger ab.

## Verwandte Themen

  * [CLI-Referenz](</de/cli>)
  * [Hintergrundaufgaben](</de/automation/tasks>)


Was this useful?YesNo