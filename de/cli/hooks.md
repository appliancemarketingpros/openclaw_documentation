---
title: Einhängepunkte
source_url: https://docs.openclaw.ai/de/cli/hooks
scraped_at: 2026-05-25
---

# `openclaw hooks`

Agent-Hooks verwalten (ereignisgesteuerte Automatisierungen für Befehle wie `/new`, `/reset` und den Gateway-Start).

Das Ausführen von `openclaw hooks` ohne Unterbefehl entspricht `openclaw hooks list`.

Verwandt:

  * Hooks: [Hooks](</de/automation/hooks>)
  * Plugin-Hooks: [Plugin-Hooks](</de/plugins/hooks>)


## Alle Hooks auflisten

bashCopy code
[code]
    openclaw hooks list
[/code]

Listet alle erkannten Hooks aus Workspace-, verwalteten, zusätzlichen und gebündelten Verzeichnissen auf. Der Gateway-Start lädt interne Hook-Handler erst, wenn mindestens ein interner Hook konfiguriert ist.

**Optionen:**

  * `--eligible`: Nur geeignete Hooks anzeigen (Anforderungen erfüllt)
  * `--json`: Als JSON ausgeben
  * `-v, --verbose`: Detaillierte Informationen einschließlich fehlender Anforderungen anzeigen


**Beispielausgabe:**

CodeCopy code
[code]
    Hooks (4/4 ready) Ready:  🚀 boot-md ✓ - Run BOOT.md on gateway startup  📎 bootstrap-extra-files ✓ - Inject extra workspace bootstrap files during agent bootstrap  📝 command-logger ✓ - Log all command events to a centralized audit file  💾 session-memory ✓ - Save session context to memory when /new or /reset command is issued
[/code]

**Beispiel (ausführlich):**

bashCopy code
[code]
    openclaw hooks list --verbose
[/code]

Zeigt fehlende Anforderungen für nicht geeignete Hooks an.

**Beispiel (JSON):**

bashCopy code
[code]
    openclaw hooks list --json
[/code]

Gibt strukturiertes JSON zur programmgesteuerten Verwendung zurück.

## Hook-Informationen abrufen

bashCopy code
[code]
    openclaw hooks info <name>
[/code]

Detaillierte Informationen zu einem bestimmten Hook anzeigen.

**Argumente:**

  * `<name>`: Hook-Name oder Hook-Schlüssel (z. B. `session-memory`)


**Optionen:**

  * `--json`: Als JSON ausgeben


**Beispiel:**

bashCopy code
[code]
    openclaw hooks info session-memory
[/code]

**Ausgabe:**

CodeCopy code
[code]
    💾 session-memory ✓ Ready Save session context to memory when /new or /reset command is issued Details:  Source: openclaw-bundled  Path: /path/to/openclaw/hooks/bundled/session-memory/HOOK.md  Handler: /path/to/openclaw/hooks/bundled/session-memory/handler.ts  Homepage: https://docs.openclaw.ai/automation/hooks#session-memory  Events: command:new, command:reset Requirements:  Config: ✓ workspace.dir
[/code]

## Hook-Eignung prüfen

bashCopy code
[code]
    openclaw hooks check
[/code]

Zusammenfassung des Hook-Eignungsstatus anzeigen (wie viele bereit bzw. nicht bereit sind).

**Optionen:**

  * `--json`: Als JSON ausgeben


**Beispielausgabe:**

CodeCopy code
[code]
    Hooks Status Total hooks: 4Ready: 4Not ready: 0
[/code]

## Hook aktivieren

bashCopy code
[code]
    openclaw hooks enable <name>
[/code]

Einen bestimmten Hook aktivieren, indem er zu Ihrer Konfiguration hinzugefügt wird (standardmäßig `~/.openclaw/openclaw.json`).

**Hinweis:** Workspace-Hooks sind standardmäßig deaktiviert, bis sie hier oder in der Konfiguration aktiviert werden. Von Plugins verwaltete Hooks zeigen `plugin:<id>` in `openclaw hooks list` und können hier nicht aktiviert/deaktiviert werden. Aktivieren/deaktivieren Sie stattdessen das Plugin.

**Argumente:**

  * `<name>`: Hook-Name (z. B. `session-memory`)


**Beispiel:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Ausgabe:**

CodeCopy code
[code]
    ✓ Enabled hook: 💾 session-memory
[/code]

**Was dabei passiert:**

  * Prüft, ob der Hook existiert und geeignet ist
  * Aktualisiert `hooks.internal.entries.<name>.enabled = true` in Ihrer Konfiguration
  * Speichert die Konfiguration auf der Festplatte


Wenn der Hook aus `<workspace>/hooks/` stammt, ist dieser Opt-in-Schritt erforderlich, bevor der Gateway ihn lädt.

**Nach der Aktivierung:**

  * Starten Sie den Gateway neu, damit Hooks neu geladen werden (Neustart der Menüleisten-App unter macOS oder Neustart Ihres Gateway-Prozesses in der Entwicklung).


## Hook deaktivieren

bashCopy code
[code]
    openclaw hooks disable <name>
[/code]

Einen bestimmten Hook durch Aktualisieren Ihrer Konfiguration deaktivieren.

**Argumente:**

  * `<name>`: Hook-Name (z. B. `command-logger`)


**Beispiel:**

bashCopy code
[code]
    openclaw hooks disable command-logger
[/code]

**Ausgabe:**

CodeCopy code
[code]
    ⏸ Disabled hook: 📝 command-logger
[/code]

**Nach der Deaktivierung:**

  * Starten Sie den Gateway neu, damit Hooks neu geladen werden


## Hinweise

  * `openclaw hooks list --json`, `info --json` und `check --json` schreiben strukturiertes JSON direkt nach stdout.
  * Von Plugins verwaltete Hooks können hier nicht aktiviert oder deaktiviert werden; aktivieren oder deaktivieren Sie stattdessen das zugehörige Plugin.


## Hook-Pakete installieren

bashCopy code
[code]
    openclaw plugins install <package>        # npm by defaultopenclaw plugins install npm:<package>    # npm onlyopenclaw plugins install <package> --pin  # pin versionopenclaw plugins install <path>           # local path
[/code]

Hook-Pakete über den einheitlichen Plugins-Installer installieren.

`openclaw hooks install` funktioniert weiterhin als Kompatibilitätsalias, gibt jedoch eine Veraltungshinweis aus und leitet an `openclaw plugins install` weiter.

Npm-Spezifikationen sind **nur registrybasiert** (Paketname + optionale **exakte Version** oder **dist-tag**). Git-/URL-/Datei-Spezifikationen und semver-Bereiche werden abgelehnt. Abhängigkeitsinstallationen laufen aus Sicherheitsgründen projektlokal mit `--ignore-scripts`, auch wenn Ihre Shell globale npm-Installationseinstellungen hat.

Unqualifizierte Spezifikationen und `@latest` bleiben auf dem stabilen Track. Wenn npm eines von beiden zu einer Vorabversion auflöst, stoppt OpenClaw und fordert Sie auf, sich ausdrücklich mit einem Vorabversions-Tag wie `@beta`/`@rc` oder einer exakten Vorabversion dafür zu entscheiden.

**Was dabei passiert:**

  * Kopiert das Hook-Paket nach `~/.openclaw/hooks/<id>`
  * Aktiviert die installierten Hooks in `hooks.internal.entries.*`
  * Zeichnet die Installation unter `hooks.internal.installs` auf


**Optionen:**

  * `-l, --link`: Ein lokales Verzeichnis verlinken statt kopieren (fügt es zu `hooks.internal.load.extraDirs` hinzu)
  * `--pin`: Npm-Installationen als exakt aufgelöstes `name@version` in `hooks.internal.installs` aufzeichnen


**Unterstützte Archive:** `.zip`, `.tgz`, `.tar.gz`, `.tar`

**Beispiele:**

bashCopy code
[code]
    # Local directoryopenclaw plugins install ./my-hook-pack # Local archiveopenclaw plugins install ./my-hook-pack.zip # NPM packageopenclaw plugins install @openclaw/my-hook-pack # Link a local directory without copyingopenclaw plugins install -l ./my-hook-pack
[/code]

Verlinkte Hook-Pakete werden als verwaltete Hooks aus einem vom Operator konfigurierten Verzeichnis behandelt, nicht als Workspace-Hooks.

## Hook-Pakete aktualisieren

bashCopy code
[code]
    openclaw plugins update <id>openclaw plugins update --all
[/code]

Verfolgte npm-basierte Hook-Pakete über den einheitlichen Plugins-Updater aktualisieren.

`openclaw hooks update` funktioniert weiterhin als Kompatibilitätsalias, gibt jedoch eine Veraltungshinweis aus und leitet an `openclaw plugins update` weiter.

**Optionen:**

  * `--all`: Alle verfolgten Hook-Pakete aktualisieren
  * `--dry-run`: Anzeigen, was sich ändern würde, ohne zu schreiben


Wenn ein gespeicherter Integritäts-Hash vorhanden ist und sich der Hash des abgerufenen Artefakts ändert, gibt OpenClaw eine Warnung aus und fragt vor dem Fortfahren nach Bestätigung. Verwenden Sie global `--yes`, um Eingabeaufforderungen in CI-/nicht interaktiven Läufen zu umgehen.

## Gebündelte Hooks

### session-memory

Speichert Sitzungskontext im Speicher, wenn Sie `/new` oder `/reset` ausführen.

**Aktivieren:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Ausgabe:** Standardmäßig `~/.openclaw/workspace/memory/YYYY-MM-DD-HHMM.md`. Setzen Sie `hooks.internal.entries.session-memory.llmSlug: true` für modellgenerierte Dateinamens-Slugs.

**Siehe:** [session-memory-Dokumentation](</de/automation/hooks#session-memory>)

### bootstrap-extra-files

Injiziert zusätzliche Bootstrap-Dateien (zum Beispiel monorepo-lokale `AGENTS.md` / `TOOLS.md`) während `agent:bootstrap`.

**Aktivieren:**

bashCopy code
[code]
    openclaw hooks enable bootstrap-extra-files
[/code]

**Siehe:** [bootstrap-extra-files-Dokumentation](</de/automation/hooks#bootstrap-extra-files>)

### command-logger

Protokolliert alle Befehlsereignisse in einer zentralisierten Audit-Datei.

**Aktivieren:**

bashCopy code
[code]
    openclaw hooks enable command-logger
[/code]

**Ausgabe:** `~/.openclaw/logs/commands.log`

**Logs anzeigen:**

bashCopy code
[code]
    # Recent commandstail -n 20 ~/.openclaw/logs/commands.log # Pretty-printcat ~/.openclaw/logs/commands.log | jq . # Filter by actiongrep '"action":"new"' ~/.openclaw/logs/commands.log | jq .
[/code]

**Siehe:** [command-logger-Dokumentation](</de/automation/hooks#command-logger>)

### boot-md

Führt `BOOT.md` aus, wenn der Gateway startet (nach dem Start der Channels).

**Ereignisse** : `gateway:startup`

**Aktivieren** :

bashCopy code
[code]
    openclaw hooks enable boot-md
[/code]

**Siehe:** [boot-md-Dokumentation](</de/automation/hooks#boot-md>)

## Verwandt

  * [CLI-Referenz](</de/cli>)
  * [Automatisierungs-Hooks](</de/automation/hooks>)


Was this useful?YesNo