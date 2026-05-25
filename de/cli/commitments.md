---
title: `openclaw commitments`
source_url: https://docs.openclaw.ai/de/cli/commitments
scraped_at: 2026-05-25
---

Abgeleitete Folgezusagen auflisten und verwalten.

Zusagen sind opt-in, kurzlebige Nachfass-Erinnerungen, die aus dem Gesprächskontext erstellt werden. Siehe [Abgeleitete Zusagen](</de/concepts/commitments>) für die konzeptionelle Anleitung.

Ohne Unterbefehl listet `openclaw commitments` ausstehende Zusagen auf.

## Verwendung

bashCopy code
[code]
    openclaw commitments [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments list [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments dismiss <id...> [--json]
[/code]

## Optionen

  * `--all`: alle Status anzeigen statt nur ausstehende Zusagen.
  * `--agent <id>`: auf eine Agent-ID filtern.
  * `--status <status>`: nach Status filtern. Werte: `pending`, `sent`, `dismissed`, `snoozed` oder `expired`.
  * `--json`: maschinenlesbares JSON ausgeben.


## Beispiele

Ausstehende Zusagen auflisten:

bashCopy code
[code]
    openclaw commitments
[/code]

Alle gespeicherten Zusagen auflisten:

bashCopy code
[code]
    openclaw commitments --all
[/code]

Auf einen Agent filtern:

bashCopy code
[code]
    openclaw commitments --agent main
[/code]

Zurückgestellte Zusagen finden:

bashCopy code
[code]
    openclaw commitments --status snoozed
[/code]

Eine oder mehrere Zusagen verwerfen:

bashCopy code
[code]
    openclaw commitments dismiss cm_abc123 cm_def456
[/code]

Als JSON exportieren:

bashCopy code
[code]
    openclaw commitments --all --json
[/code]

## Ausgabe

Die Textausgabe enthält:

  * Zusagen-ID
  * Status
  * Art
  * früheste Fälligkeitszeit
  * Geltungsbereich
  * vorgeschlagener Check-in-Text


Die JSON-Ausgabe enthält außerdem den Pfad des Zusagenspeichers und vollständige gespeicherte Datensätze.

## Verwandte Themen

  * [Abgeleitete Zusagen](</de/concepts/commitments>)
  * [Memory-Übersicht](</de/concepts/memory>)
  * [Heartbeat](</de/gateway/heartbeat>)
  * [Geplante Aufgaben](</de/automation/cron-jobs>)


Was this useful?YesNo