---
title: Agenten-Arbeitsbereich
source_url: https://docs.openclaw.ai/de/concepts/agent-workspace
scraped_at: 2026-05-25
---

Der Workspace ist das Zuhause des Agenten. Er ist das einzige Arbeitsverzeichnis, das für Datei-Tools und Workspace-Kontext verwendet wird. Halten Sie ihn privat und behandeln Sie ihn als Gedächtnis.

Dies ist getrennt von `~/.openclaw/`, wo Konfiguration, Anmeldedaten und Sitzungen gespeichert werden.

## Standardort

  * Standard: `~/.openclaw/workspace`
  * Wenn `OPENCLAW_PROFILE` gesetzt ist und nicht `"default"` ist, wird der Standard zu `~/.openclaw/workspace-<profile>`.
  * Überschreiben in `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/.openclaw/workspace",    },  },}
[/code]

`openclaw onboard`, `openclaw configure` oder `openclaw setup` erstellt den Workspace und befüllt die Bootstrap-Dateien, falls sie fehlen.

Wenn Sie die Workspace-Dateien bereits selbst verwalten, können Sie die Erstellung von Bootstrap-Dateien deaktivieren:

json5Copy code
[code]
    { agents: { defaults: { skipBootstrap: true } } }
[/code]

## Zusätzliche Workspace-Ordner

Ältere Installationen haben möglicherweise `~/openclaw` erstellt. Mehrere Workspace-Verzeichnisse beizubehalten kann zu verwirrenden Authentifizierungs- oder Zustandsabweichungen führen, da immer nur ein Workspace aktiv ist.

## Workspace-Dateizuordnung

Dies sind die Standarddateien, die OpenClaw innerhalb des Workspace erwartet:

AGENTS.md - operating instructions

Betriebsanweisungen für den Agenten und dazu, wie er das Gedächtnis verwenden soll. Wird zu Beginn jeder Sitzung geladen. Ein guter Ort für Regeln, Prioritäten und Details dazu, „wie er sich verhalten soll“.

SOUL.md - persona and tone

Persona, Ton und Grenzen. Wird in jeder Sitzung geladen. Leitfaden: [SOUL.md-Persönlichkeitsleitfaden](</de/concepts/soul>).

USER.md - who the user is

Wer der Benutzer ist und wie er angesprochen werden soll. Wird in jeder Sitzung geladen.

IDENTITY.md - name, vibe, emoji

Name, Stimmung und Emoji des Agenten. Wird während des Bootstrap-Rituals erstellt/aktualisiert.

TOOLS.md - local tool conventions

Notizen zu Ihren lokalen Tools und Konventionen. Steuert nicht die Tool-Verfügbarkeit; es dient nur als Anleitung.

HEARTBEAT.md - heartbeat checklist

Optionale kleine Checkliste für Heartbeat-Läufe. Halten Sie sie kurz, um Token-Verbrauch zu vermeiden.

BOOT.md - startup checklist

Optionale Startcheckliste, die beim Neustart des Gateway automatisch ausgeführt wird (wenn [interne Hooks](</de/automation/hooks>) aktiviert sind). Halten Sie sie kurz; verwenden Sie das Nachrichten-Tool für ausgehende Sendungen.

BOOTSTRAP.md - first-run ritual

Einmaliges Ritual beim ersten Start. Wird nur für einen brandneuen Workspace erstellt. Löschen Sie es, nachdem das Ritual abgeschlossen ist.

memory/YYYY-MM-DD.md - daily memory log

Tägliches Gedächtnisprotokoll (eine Datei pro Tag). Empfohlen wird, beim Sitzungsstart heute + gestern zu lesen.

MEMORY.md - curated long-term memory (optional)

Kuratiertes Langzeitgedächtnis: dauerhafte Fakten, Präferenzen, Entscheidungen und kurze Zusammenfassungen. Bewahren Sie detaillierte Protokolle in `memory/YYYY-MM-DD.md` auf, damit Gedächtnis-Tools sie bei Bedarf abrufen können, ohne sie in jeden Prompt einzufügen. Laden Sie `MEMORY.md` nur in der privaten Hauptsitzung (nicht in geteilten/Gruppenkontexten). Siehe [Gedächtnis](</de/concepts/memory>) für den Workflow und das automatische Leeren des Gedächtnisses.

skills/ - workspace skills (optional)

Workspace-spezifische Skills. Skill-Speicherort mit höchster Priorität für diesen Workspace. Überschreibt Projekt-Agent-Skills, persönliche Agent-Skills, verwaltete Skills, gebündelte Skills und `skills.load.extraDirs`, wenn Namen kollidieren.

canvas/ - Canvas UI files (optional)

Canvas-UI-Dateien für Node-Anzeigen (zum Beispiel `canvas/index.html`).

## Was NICHT im Workspace liegt

Diese befinden sich unter `~/.openclaw/` und sollten NICHT in das Workspace-Repo committed werden:

  * `~/.openclaw/openclaw.json` (Konfiguration)
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` (Modell-Authentifizierungsprofile: OAuth + API-Schlüssel)
  * `~/.openclaw/agents/<agentId>/agent/codex-home/` (agentenspezifisches Codex-Laufzeitkonto, Konfiguration, Skills, Plugins und nativer Thread-Zustand)
  * `~/.openclaw/credentials/` (Kanal-/Provider-Zustand plus ältere OAuth-Importdaten)
  * `~/.openclaw/agents/<agentId>/sessions/` (Sitzungstranskripte + Metadaten)
  * `~/.openclaw/skills/` (verwaltete Skills)


Wenn Sie Sitzungen oder Konfiguration migrieren müssen, kopieren Sie sie separat und halten Sie sie aus der Versionskontrolle heraus.

## Git-Backup (empfohlen, privat)

Behandeln Sie den Workspace als privates Gedächtnis. Legen Sie ihn in einem **privaten** Git-Repo ab, damit er gesichert und wiederherstellbar ist.

Führen Sie diese Schritte auf dem Rechner aus, auf dem das Gateway läuft (dort befindet sich der Workspace).

* ### Initialize the repo

Wenn Git installiert ist, werden brandneue Workspaces automatisch initialisiert. Wenn dieser Workspace noch kein Repo ist, führen Sie Folgendes aus:

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.md SOUL.md TOOLS.md IDENTITY.md USER.md HEARTBEAT.md memory/git commit -m "Add agent workspace"
[/code]

* ### Add a private remote

### GitHub web UI

  1. Erstellen Sie ein neues **privates** Repository auf GitHub.
  2. Nicht mit einer README initialisieren (vermeidet Merge-Konflikte).
  3. Kopieren Sie die HTTPS-Remote-URL.
  4. Fügen Sie den Remote hinzu und pushen Sie:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

### GitHub CLI (gh)

bashCopy code
[code]
    gh auth logingh repo create openclaw-workspace --private --source . --remote origin --push
[/code]

### GitLab web UI

  1. Erstellen Sie ein neues **privates** Repository auf GitLab.
  2. Nicht mit einer README initialisieren (vermeidet Merge-Konflikte).
  3. Kopieren Sie die HTTPS-Remote-URL.
  4. Fügen Sie den Remote hinzu und pushen Sie:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

* ### Ongoing updates

bashCopy code
[code]
    git statusgit add .git commit -m "Update memory"git push
[/code]

## Keine Secrets committen

Vorgeschlagener `.gitignore`-Start:

gitignoreCopy code
[code]
    .DS_Store.env**/*.key**/*.pem**/secrets*
[/code]

## Workspace auf einen neuen Rechner verschieben

* ### Clone the repo

Klonen Sie das Repo in den gewünschten Pfad (Standard `~/.openclaw/workspace`).

* ### Update config

Setzen Sie `agents.defaults.workspace` in `~/.openclaw/openclaw.json` auf diesen Pfad.

* ### Seed missing files

Führen Sie `openclaw setup --workspace <path>` aus, um fehlende Dateien zu befüllen.

* ### Copy sessions (optional)

Wenn Sie Sitzungen benötigen, kopieren Sie `~/.openclaw/agents/<agentId>/sessions/` separat vom alten Rechner.

## Erweiterte Hinweise

  * Multi-Agent-Routing kann unterschiedliche Workspaces pro Agent verwenden. Siehe [Kanalrouting](</de/channels/channel-routing>) für die Routing-Konfiguration.
  * Wenn `agents.defaults.sandbox` aktiviert ist, können Nicht-Hauptsitzungen sitzungsspezifische Sandbox-Workspaces unter `agents.defaults.sandbox.workspaceRoot` verwenden.


## Verwandt

  * [Heartbeat](</de/gateway/heartbeat>) \- HEARTBEAT.md-Workspace-Datei
  * [Sandboxing](</de/gateway/sandboxing>) \- Workspace-Zugriff in Sandbox-Umgebungen
  * [Sitzung](</de/concepts/session>) \- Speicherpfade für Sitzungen
  * [Dauerhafte Anweisungen](</de/automation/standing-orders>) \- persistente Anweisungen in Workspace-Dateien


Was this useful?YesNo