---
title: Skills
source_url: https://docs.openclaw.ai/de/cli/skills
scraped_at: 2026-05-25
---

# `openclaw skills`

Lokale Skills prüfen und Skills aus ClawHub installieren/aktualisieren.

Verwandt:

  * Skills-System: [Skills](</de/tools/skills>)
  * Skills-Konfiguration: [Skills-Konfiguration](</de/tools/skills-config>)
  * ClawHub-Installationen: [ClawHub](</de/clawhub/cli>)


## Befehle

bashCopy code
[code]
    openclaw skills search "calendar"openclaw skills search --limit 20 --jsonopenclaw skills install <slug>openclaw skills install <slug> --version <version>openclaw skills install <slug> --forceopenclaw skills install <slug> --agent <id>openclaw skills update <slug>openclaw skills update --allopenclaw skills update --all --agent <id>openclaw skills listopenclaw skills list --eligibleopenclaw skills list --jsonopenclaw skills list --verboseopenclaw skills list --agent <id>openclaw skills info <name>openclaw skills info <name> --jsonopenclaw skills info <name> --agent <id>openclaw skills checkopenclaw skills check --agent <id>openclaw skills check --json
[/code]

`search`/`install`/`update` verwenden ClawHub direkt und installieren in das `skills/`-Verzeichnis des aktiven Workspace. `list`/`info`/`check` prüfen weiterhin die lokalen Skills, die für den aktuellen Workspace und die aktuelle Konfiguration sichtbar sind. Workspace-gestützte Befehle lösen den Ziel-Workspace über `--agent <id>` auf, dann über das aktuelle Arbeitsverzeichnis, wenn es sich innerhalb eines konfigurierten Agent-Workspace befindet, und dann über den Standard- Agent.

Dieser CLI-Befehl `install` lädt Skill-Ordner aus ClawHub herunter. Gateway-gestützte Installationen von Skill-Abhängigkeiten, die aus dem Onboarding oder aus Skills-Einstellungen ausgelöst werden, verwenden stattdessen den separaten `skills.install`-Anfragepfad.

Hinweise:

  * `search [query...]` akzeptiert eine optionale Abfrage; lassen Sie sie weg, um den standardmäßigen ClawHub-Suchfeed zu durchsuchen.
  * `search --limit <n>` begrenzt die zurückgegebenen Ergebnisse.
  * `install --force` überschreibt einen vorhandenen Workspace-Skill-Ordner für denselben Slug.
  * `--agent <id>` zielt auf einen konfigurierten Agent-Workspace und überschreibt die Ableitung aus dem aktuellen Arbeitsverzeichnis.
  * `update --all` aktualisiert nur nachverfolgte ClawHub-Installationen im aktiven Workspace.
  * `check --agent <id>` prüft den Workspace des ausgewählten Agents und meldet, welche bereiten Skills tatsächlich für die Prompt- oder Befehlsoberfläche dieses Agents sichtbar sind.
  * `list` ist die Standardaktion, wenn kein Unterbefehl angegeben wird.
  * `list`, `info` und `check` schreiben ihre gerenderte Ausgabe nach stdout. Mit `--json` bedeutet das, dass die maschinenlesbare Nutzlast für Pipes und Skripte auf stdout bleibt.


## Verwandt

  * [CLI-Referenz](</de/cli>)
  * [Skills](</de/tools/skills>)


Was this useful?YesNo