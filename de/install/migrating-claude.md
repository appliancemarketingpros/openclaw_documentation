---
title: Migration von Claude
source_url: https://docs.openclaw.ai/de/install/migrating-claude
scraped_at: 2026-05-25
---

OpenClaw importiert lokalen Claude-Zustand über den gebündelten Claude-Migrations-Provider. Der Provider zeigt jedes Element vor einer Zustandsänderung in einer Vorschau an, schwärzt Geheimnisse in Plänen und Berichten und erstellt vor der Anwendung ein verifiziertes Backup.

## Zwei Wege zum Importieren

### Onboarding-Assistent

Der Assistent bietet Claude an, wenn er lokalen Claude-Zustand erkennt.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

Oder geben Sie eine bestimmte Quelle an:

bashCopy code
[code]
    openclaw onboard --import-from claude --import-source ~/.claude
[/code]

### CLI

Verwenden Sie `openclaw migrate` für skriptgesteuerte oder wiederholbare Läufe. Die vollständige Referenz finden Sie unter [`openclaw migrate`](</de/cli/migrate>).

bashCopy code
[code]
    openclaw migrate claude --dry-runopenclaw migrate apply claude --yes
[/code]

Fügen Sie `--from <path>` hinzu, um ein bestimmtes Claude Code-Home oder Projektstammverzeichnis zu importieren.

## Was importiert wird

Anweisungen und Memory

  * Inhalte aus Projekt-`CLAUDE.md` und `.claude/CLAUDE.md` werden in den OpenClaw-Agentenarbeitsbereich `AGENTS.md` kopiert oder dort angehängt.
  * Inhalte aus Benutzer-`~/.claude/CLAUDE.md` werden an Arbeitsbereich-`USER.md` angehängt.

MCP-Server

MCP-Serverdefinitionen werden aus Projekt-`.mcp.json`, Claude Code-`~/.claude.json` und Claude Desktop-`claude_desktop_config.json` importiert, wenn sie vorhanden sind.

Skills und Befehle

  * Claude-Skills mit einer `SKILL.md`-Datei werden in das Skills-Verzeichnis des OpenClaw-Arbeitsbereichs kopiert.
  * Claude-Befehls-Markdown-Dateien unter `.claude/commands/` oder `~/.claude/commands/` werden in OpenClaw-Skills mit `disable-model-invocation: true` umgewandelt.


## Was nur archiviert bleibt

Der Provider kopiert diese Elemente zur manuellen Prüfung in den Migrationsbericht, lädt sie aber **nicht** in die aktive OpenClaw-Konfiguration:

  * Claude-Hooks
  * Claude-Berechtigungen und umfassende Tool-Zulassungslisten
  * Claude-Umgebungsstandards
  * `CLAUDE.local.md`
  * `.claude/rules/`
  * Claude-Subagents unter `.claude/agents/` oder `~/.claude/agents/`
  * Claude Code-Caches, Pläne und Projektverlaufsverzeichnisse
  * Claude Desktop-Erweiterungen und vom Betriebssystem gespeicherte Anmeldedaten


OpenClaw verweigert es, Hooks auszuführen, Berechtigungs-Zulassungslisten zu vertrauen oder undurchsichtigen OAuth- und Desktop-Anmeldedatenzustand automatisch zu dekodieren. Verschieben Sie das, was Sie benötigen, nach Prüfung des Archivs manuell.

## Quellenauswahl

Ohne `--from` untersucht OpenClaw das standardmäßige Claude Code-Home unter `~/.claude`, die stichprobenartige Claude Code-Zustandsdatei `~/.claude.json` und die Claude Desktop-MCP-Konfiguration unter macOS.

Wenn `--from` auf ein Projektstammverzeichnis zeigt, importiert OpenClaw nur die Claude-Dateien dieses Projekts, etwa `CLAUDE.md`, `.claude/settings.json`, `.claude/commands/`, `.claude/skills/` und `.mcp.json`. Ihr globales Claude-Home wird während eines Imports aus einem Projektstammverzeichnis nicht gelesen.

## Empfohlener Ablauf

* ### Planvorschau anzeigen

bashCopy code
[code]
    openclaw migrate claude --dry-run
[/code]

Der Plan listet alles auf, was geändert wird, einschließlich Konflikten, übersprungenen Elementen und sensiblen Werten, die aus verschachtelten MCP-`env`\- oder `headers`-Feldern geschwärzt wurden.

* ### Mit Backup anwenden

bashCopy code
[code]
    openclaw migrate apply claude --yes
[/code]

OpenClaw erstellt und verifiziert vor der Anwendung ein Backup.

* ### Doctor ausführen

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</de/gateway/doctor>) prüft nach dem Import auf Konfigurations- oder Zustandsprobleme.

* ### Neu starten und überprüfen

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

Bestätigen Sie, dass der Gateway fehlerfrei ist und Ihre importierten Anweisungen, MCP-Server und Skills geladen sind.

## Konfliktbehandlung

Die Anwendung verweigert die Fortsetzung, wenn der Plan Konflikte meldet (eine Datei oder ein Konfigurationswert existiert bereits am Ziel).

Bei einer frischen OpenClaw-Installation sind Konflikte ungewöhnlich. Sie treten typischerweise auf, wenn Sie den Import auf einer Einrichtung erneut ausführen, die bereits Benutzeränderungen enthält.

## JSON-Ausgabe für Automatisierung

bashCopy code
[code]
    openclaw migrate claude --dry-run --jsonopenclaw migrate apply claude --json --yes
[/code]

Mit `--json` und ohne `--yes` gibt die Anwendung den Plan aus und verändert keinen Zustand. Dies ist der sicherste Modus für CI und gemeinsam genutzte Skripte.

## Fehlerbehebung

Claude-Zustand liegt außerhalb von ~/.claude

Übergeben Sie `--from /actual/path` (CLI) oder `--import-source /actual/path` (Onboarding).

Onboarding verweigert den Import in eine vorhandene Einrichtung

Onboarding-Importe erfordern eine frische Einrichtung. Setzen Sie entweder den Zustand zurück und führen Sie das Onboarding erneut durch, oder verwenden Sie direkt `openclaw migrate apply claude`, das `--overwrite` und explizite Backup-Steuerung unterstützt.

MCP-Server aus Claude Desktop wurden nicht importiert

Claude Desktop liest `claude_desktop_config.json` aus einem plattformspezifischen Pfad. Richten Sie `--from` auf das Verzeichnis dieser Datei, wenn OpenClaw sie nicht automatisch erkannt hat.

Claude-Befehle wurden zu Skills mit deaktiviertem Modellaufruf

Dies ist beabsichtigt. Claude-Befehle werden vom Benutzer ausgelöst, daher importiert OpenClaw sie als Skills mit `disable-model-invocation: true`. Bearbeiten Sie das Frontmatter jedes Skills, wenn der Agent sie automatisch aufrufen soll.

## Verwandte Themen

  * [`openclaw migrate`](</de/cli/migrate>): vollständige CLI-Referenz, Plugin-Vertrag und JSON-Strukturen.
  * [Migrationsleitfaden](</de/install/migrating>): alle Migrationspfade.
  * [Migration von Hermes](</de/install/migrating-hermes>): der andere systemübergreifende Importpfad.
  * [Onboarding](</de/cli/onboard>): Assistentenablauf und nicht interaktive Flags.
  * [Doctor](</de/gateway/doctor>): Integritätsprüfung nach der Migration.
  * [Agentenarbeitsbereich](</de/concepts/agent-workspace>): wo `AGENTS.md`, `USER.md` und Skills gespeichert sind.


Was this useful?YesNo