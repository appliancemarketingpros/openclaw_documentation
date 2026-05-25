---
title: Sandbox-CLI
source_url: https://docs.openclaw.ai/de/cli/sandbox
scraped_at: 2026-05-25
---

Sandbox-Laufzeitumgebungen für isolierte Agent-Ausführung verwalten.

## Überblick

OpenClaw kann Agents aus Sicherheitsgründen in isolierten Sandbox-Laufzeitumgebungen ausführen. Die `sandbox`-Befehle helfen Ihnen, diese Laufzeitumgebungen nach Updates oder Konfigurationsänderungen zu prüfen und neu zu erstellen.

Derzeit bedeutet das in der Regel:

  * Docker-Sandbox-Container
  * SSH-Sandbox-Laufzeitumgebungen, wenn `agents.defaults.sandbox.backend = "ssh"`
  * OpenShell-Sandbox-Laufzeitumgebungen, wenn `agents.defaults.sandbox.backend = "openshell"`


Für `ssh` und OpenShell `remote` ist das Neuerstellen wichtiger als bei Docker:

  * Der Remote-Arbeitsbereich ist nach dem initialen Seed maßgeblich
  * `openclaw sandbox recreate` löscht diesen maßgeblichen Remote-Arbeitsbereich für den ausgewählten Geltungsbereich
  * Bei der nächsten Verwendung wird er erneut aus dem aktuellen lokalen Arbeitsbereich befüllt


## Befehle

### `openclaw sandbox explain`

Prüfen Sie den **effektiven** Sandbox-Modus, Geltungsbereich, Arbeitsbereichszugriff, die Sandbox-Tool-Richtlinie und erhöhte Gates (mit Fix-it-Konfigurationsschlüsselpfaden).

bashCopy code
[code]
    openclaw sandbox explainopenclaw sandbox explain --session agent:main:mainopenclaw sandbox explain --agent workopenclaw sandbox explain --json
[/code]

### `openclaw sandbox list`

Listet alle Sandbox-Laufzeitumgebungen mit Status und Konfiguration auf.

bashCopy code
[code]
    openclaw sandbox listopenclaw sandbox list --browser  # List only browser containersopenclaw sandbox list --json     # JSON output
[/code]

**Ausgabe enthält:**

  * Name und Status der Laufzeitumgebung
  * Backend (`docker`, `openshell` usw.)
  * Konfigurationslabel und ob es mit der aktuellen Konfiguration übereinstimmt
  * Alter (Zeit seit Erstellung)
  * Leerlaufzeit (Zeit seit letzter Verwendung)
  * Zugeordnete Session/zugeordneter Agent


### `openclaw sandbox recreate`

Entfernt Sandbox-Laufzeitumgebungen, um eine Neuerstellung mit aktualisierter Konfiguration zu erzwingen.

bashCopy code
[code]
    openclaw sandbox recreate --all                # Recreate all containersopenclaw sandbox recreate --session main       # Specific sessionopenclaw sandbox recreate --agent mybot        # Specific agentopenclaw sandbox recreate --browser            # Only browser containersopenclaw sandbox recreate --all --force        # Skip confirmation
[/code]

**Optionen:**

  * `--all`: Alle Sandbox-Container neu erstellen
  * `--session <key>`: Container für eine bestimmte Session neu erstellen
  * `--agent <id>`: Container für einen bestimmten Agent neu erstellen
  * `--browser`: Nur Browser-Container neu erstellen
  * `--force`: Bestätigungsabfrage überspringen


## Anwendungsfälle

### Nach dem Aktualisieren eines Docker-Images

bashCopy code
[code]
    # Pull new imagedocker pull openclaw-sandbox:latestdocker tag openclaw-sandbox:latest openclaw-sandbox:bookworm-slim # Update config to use new image# Edit config: agents.defaults.sandbox.docker.image (or agents.list[].sandbox.docker.image) # Recreate containersopenclaw sandbox recreate --all
[/code]

### Nach dem Ändern der Sandbox-Konfiguration

bashCopy code
[code]
    # Edit config: agents.defaults.sandbox.* (or agents.list[].sandbox.*) # Recreate to apply new configopenclaw sandbox recreate --all
[/code]

### Nach dem Ändern des SSH-Ziels oder des SSH-Authentifizierungsmaterials

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - agents.defaults.sandbox.ssh.target# - agents.defaults.sandbox.ssh.workspaceRoot# - agents.defaults.sandbox.ssh.identityFile / certificateFile / knownHostsFile# - agents.defaults.sandbox.ssh.identityData / certificateData / knownHostsData openclaw sandbox recreate --all
[/code]

Für das Core-Backend `ssh` löscht das Neuerstellen das Remote-Arbeitsbereichs-Root pro Geltungsbereich auf dem SSH-Ziel. Der nächste Lauf befüllt ihn erneut aus dem lokalen Arbeitsbereich.

### Nach dem Ändern von OpenShell-Quelle, Richtlinie oder Modus

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - plugins.entries.openshell.config.from# - plugins.entries.openshell.config.mode# - plugins.entries.openshell.config.policy openclaw sandbox recreate --all
[/code]

Im OpenShell-`remote`-Modus löscht das Neuerstellen den maßgeblichen Remote-Arbeitsbereich für diesen Geltungsbereich. Der nächste Lauf befüllt ihn erneut aus dem lokalen Arbeitsbereich.

### Nach dem Ändern von setupCommand

bashCopy code
[code]
    openclaw sandbox recreate --all# or just one agent:openclaw sandbox recreate --agent family
[/code]

### Nur für einen bestimmten Agent

bashCopy code
[code]
    # Update only one agent's containersopenclaw sandbox recreate --agent alfred
[/code]

## Warum dies erforderlich ist

Wenn Sie die Sandbox-Konfiguration aktualisieren:

  * Vorhandene Laufzeitumgebungen laufen mit alten Einstellungen weiter.
  * Laufzeitumgebungen werden erst nach 24 Stunden Inaktivität bereinigt.
  * Regelmäßig verwendete Agents halten alte Laufzeitumgebungen unbegrenzt aktiv.


Verwenden Sie `openclaw sandbox recreate`, um das Entfernen alter Laufzeitumgebungen zu erzwingen. Sie werden bei Bedarf automatisch mit den aktuellen Einstellungen neu erstellt.

## Registry-Migration

OpenClaw speichert Metadaten zu Sandbox-Laufzeitumgebungen als einen JSON-Shard pro Container-/Browser-Eintrag im Sandbox-Statusverzeichnis. Ältere Installationen haben möglicherweise noch monolithische Legacy-Dateien:

  * `~/.openclaw/sandbox/containers.json`
  * `~/.openclaw/sandbox/browsers.json`


Reguläre Lesevorgänge für Sandbox-Laufzeitumgebungen schreiben diese Dateien nicht neu. Führen Sie `openclaw doctor --fix` aus, um gültige Legacy-Einträge in die geshardeten Registry-Verzeichnisse zu migrieren. Ungültige Legacy-Dateien werden unter Quarantäne gestellt, damit eine fehlerhafte alte Registry keine aktuellen Laufzeiteinträge verbergen kann.

## Konfiguration

Sandbox-Einstellungen befinden sich in `~/.openclaw/openclaw.json` unter `agents.defaults.sandbox` (Überschreibungen pro Agent stehen in `agents.list[].sandbox`):

jsoncCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "all", // off, non-main, all        "backend": "docker", // docker, ssh, openshell        "scope": "agent", // session, agent, shared        "docker": {          "image": "openclaw-sandbox:bookworm-slim",          "containerPrefix": "openclaw-sbx-",          // ... more Docker options        },        "prune": {          "idleHours": 24, // Auto-prune after 24h idle          "maxAgeDays": 7, // Auto-prune after 7 days        },      },    },  },}
[/code]

## Verwandte Themen

  * [CLI-Referenz](</de/cli>)
  * [Sandboxing](</de/gateway/sandboxing>)
  * [Agent-Arbeitsbereich](</de/concepts/agent-workspace>)
  * [Doctor](</de/gateway/doctor>): prüft die Sandbox-Einrichtung.


Was this useful?YesNo