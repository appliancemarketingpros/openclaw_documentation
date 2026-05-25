---
title: Abläufe (Weiterleitung)
source_url: https://docs.openclaw.ai/de/cli/flows
scraped_at: 2026-05-25
---

# `openclaw tasks flow`

Es gibt keinen `openclaw flows`-Befehl auf oberster Ebene. Die dauerhafte TaskFlow-Inspektion befindet sich unter `openclaw tasks flow`.

## Unterbefehle

bashCopy code
[code]
    openclaw tasks flow list   [--json] [--status <name>]openclaw tasks flow show   <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Unterbefehl | Beschreibung | Argumente / Optionen  
---|---|---  
`list` | Nachverfolgte TaskFlows auflisten. | `--json` maschinenlesbare Ausgabe; `--status <name>` Filter (siehe Statuswerte unten).  
`show` | Einen TaskFlow anzeigen. | `<lookup>` Flow-ID oder Owner-Schlüssel; `--json` maschinenlesbare Ausgabe.  
`cancel` | Einen laufenden TaskFlow abbrechen. | `<lookup>` Flow-ID oder Owner-Schlüssel.  
  
`<lookup>` akzeptiert entweder eine Flow-ID (zurückgegeben von `list` / `show`) oder den Owner-Schlüssel des Flows (den stabilen Bezeichner, den das besitzende Subsystem verwendet, um den Flow nachzuverfolgen).

### Statusfilterwerte

`--status` bei `list` akzeptiert einen der folgenden Werte:

`queued`, `running`, `waiting`, `blocked`, `succeeded`, `failed`, `cancelled`, `lost`

## Beispiele

bashCopy code
[code]
    openclaw tasks flow listopenclaw tasks flow list --status runningopenclaw tasks flow list --jsonopenclaw tasks flow show flow_abc123openclaw tasks flow show flow_abc123 --jsonopenclaw tasks flow cancel flow_abc123
[/code]

Vollständige TaskFlow-Konzepte und Informationen zum Erstellen finden Sie unter [TaskFlow](</de/automation/taskflow>). Informationen zum übergeordneten Befehl `tasks` finden Sie in der [tasks-CLI-Referenz](</de/cli/tasks>).

## Verwandt

  * [CLI-Referenz](</de/cli>)
  * [Automatisierung](</de/automation>)
  * [TaskFlow](</de/automation/taskflow>)


Was this useful?YesNo