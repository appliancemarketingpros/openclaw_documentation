---
title: Migration von Hermes
source_url: https://docs.openclaw.ai/de/install/migrating-hermes
scraped_at: 2026-05-25
---

OpenClaw importiert den Hermes-Zustand über einen gebündelten Migrations-Provider. Der Provider zeigt vor jeder Zustandsänderung eine Vorschau an, redigiert Geheimnisse in Plänen und Berichten und erstellt vor der Anwendung ein verifiziertes Backup.

## Zwei Möglichkeiten für den Import

### Onboarding-Assistent

Der schnellste Weg. Der Assistent erkennt Hermes unter `~/.hermes` und zeigt vor der Anwendung eine Vorschau an.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

Oder geben Sie eine bestimmte Quelle an:

bashCopy code
[code]
    openclaw onboard --import-from hermes --import-source ~/.hermes
[/code]

### CLI

Verwenden Sie `openclaw migrate` für skriptgesteuerte oder wiederholbare Läufe. Die vollständige Referenz finden Sie unter [`openclaw migrate`](</de/cli/migrate>).

bashCopy code
[code]
    openclaw migrate hermes --dry-run    # preview onlyopenclaw migrate apply hermes --yes  # apply with confirmation skipped
[/code]

Fügen Sie `--from <path>` hinzu, wenn Hermes außerhalb von `~/.hermes` liegt.

## Was importiert wird

Modellkonfiguration

  * Standard-Modellauswahl aus Hermes `config.yaml`.
  * Konfigurierte Modell-Provider und benutzerdefinierte OpenAI-kompatible Endpunkte aus `providers` und `custom_providers`.

MCP-Server

MCP-Serverdefinitionen aus `mcp_servers` oder `mcp.servers`.

Arbeitsbereichsdateien

  * `SOUL.md` und `AGENTS.md` werden in den OpenClaw-Agent-Arbeitsbereich kopiert.
  * `memories/MEMORY.md` und `memories/USER.md` werden an die passenden OpenClaw-Speicherdateien **angehängt** , statt sie zu überschreiben.

Speicherkonfiguration

Standardwerte der Speicherkonfiguration für den OpenClaw-Dateispeicher. Externe Speicher-Provider wie Honcho werden als Archiv- oder manuell zu prüfende Einträge erfasst, damit Sie sie bewusst migrieren können.

Skills

Skills mit einer `SKILL.md`-Datei unter `skills/<name>/` werden zusammen mit Skill-spezifischen Konfigurationswerten aus `skills.config` kopiert.

API-Schlüssel (optional)

Setzen Sie `--include-secrets`, um unterstützte `.env`-Schlüssel zu importieren: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `OPENROUTER_API_KEY`, `GOOGLE_API_KEY`, `GEMINI_API_KEY`, `GROQ_API_KEY`, `XAI_API_KEY`, `MISTRAL_API_KEY`, `DEEPSEEK_API_KEY`. Ohne das Flag werden Geheimnisse nie kopiert.

## Was nur im Archiv bleibt

Der Provider kopiert diese Einträge zur manuellen Prüfung in das Migrationsberichtsverzeichnis, lädt sie aber **nicht** in die aktive OpenClaw-Konfiguration oder die Anmeldedaten:

  * `plugins/`
  * `sessions/`
  * `logs/`
  * `cron/`
  * `mcp-tokens/`
  * `auth.json`
  * `state.db`


OpenClaw weigert sich, diesen Zustand automatisch auszuführen oder ihm zu vertrauen, weil Formate und Vertrauensannahmen zwischen Systemen abweichen können. Verschieben Sie benötigte Inhalte nach der Prüfung des Archivs manuell.

## Empfohlener Ablauf

* ### Plan in der Vorschau anzeigen

bashCopy code
[code]
    openclaw migrate hermes --dry-run
[/code]

Der Plan listet alles auf, was geändert wird, einschließlich Konflikten, übersprungener Einträge und sensibler Einträge. Die Planausgabe redigiert verschachtelte Schlüssel, die wie Geheimnisse aussehen.

* ### Mit Backup anwenden

bashCopy code
[code]
    openclaw migrate apply hermes --yes
[/code]

OpenClaw erstellt und verifiziert vor der Anwendung ein Backup. Wenn API-Schlüssel importiert werden sollen, fügen Sie `--include-secrets` hinzu.

* ### Doctor ausführen

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</de/gateway/doctor>) wendet ausstehende Konfigurationsmigrationen erneut an und prüft auf Probleme, die während des Imports eingeführt wurden.

* ### Neu starten und prüfen

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

Bestätigen Sie, dass der Gateway fehlerfrei ist und Ihr importiertes Modell, Ihr Speicher und Ihre Skills geladen sind.

## Konfliktbehandlung

Die Anwendung wird verweigert, wenn der Plan Konflikte meldet (eine Datei oder ein Konfigurationswert existiert bereits am Ziel).

Bei einer frischen OpenClaw-Installation sind Konflikte ungewöhnlich. Sie treten typischerweise auf, wenn Sie den Import auf einer Einrichtung erneut ausführen, die bereits Benutzeränderungen enthält.

Wenn während der Anwendung ein Konflikt auftritt (zum Beispiel ein unerwarteter Wettlauf um eine Konfigurationsdatei), markiert Hermes verbleibende abhängige Konfigurationseinträge als `skipped` mit dem Grund `blocked by earlier apply conflict`, statt sie teilweise zu schreiben. Der Migrationsbericht erfasst jeden blockierten Eintrag, damit Sie den ursprünglichen Konflikt beheben und den Import erneut ausführen können.

## Geheimnisse

Geheimnisse werden standardmäßig nie importiert.

  * Führen Sie zuerst `openclaw migrate apply hermes --yes` aus, um Zustand ohne Geheimnisse zu importieren.
  * Wenn Sie auch unterstützte `.env`-Schlüssel kopieren möchten, führen Sie den Befehl erneut mit `--include-secrets` aus.
  * Konfigurieren Sie für SecretRef-verwaltete Anmeldedaten die SecretRef-Quelle, nachdem der Import abgeschlossen ist.


## JSON-Ausgabe für Automatisierung

bashCopy code
[code]
    openclaw migrate hermes --dry-run --jsonopenclaw migrate apply hermes --json --yes
[/code]

Mit `--json` und ohne `--yes` gibt apply den Plan aus und verändert keinen Zustand. Dies ist der sicherste Modus für CI und gemeinsam genutzte Skripte.

## Fehlerbehebung

Apply verweigert die Ausführung wegen Konflikten

Prüfen Sie die Planausgabe. Jeder Konflikt identifiziert den Quellpfad und das vorhandene Ziel. Entscheiden Sie pro Eintrag, ob Sie ihn überspringen, das Ziel bearbeiten oder den Befehl mit `--overwrite` erneut ausführen.

Hermes liegt außerhalb von ~/.hermes

Übergeben Sie `--from /actual/path` (CLI) oder `--import-source /actual/path` (Onboarding).

Onboarding verweigert den Import bei einer bestehenden Einrichtung

Onboarding-Importe erfordern eine frische Einrichtung. Setzen Sie entweder den Zustand zurück und führen Sie das Onboarding erneut aus, oder verwenden Sie direkt `openclaw migrate apply hermes`, das `--overwrite` und explizite Backup-Steuerung unterstützt.

API-Schlüssel wurden nicht importiert

`--include-secrets` ist erforderlich, und nur die oben aufgeführten Schlüssel werden erkannt. Andere Variablen in `.env` werden ignoriert.

## Verwandte Themen

  * [`openclaw migrate`](</de/cli/migrate>): vollständige CLI-Referenz, Plugin-Vertrag und JSON-Strukturen.
  * [Onboarding](</de/cli/onboard>): Assistentenablauf und nicht interaktive Flags.
  * [Migration](</de/install/migrating>): eine OpenClaw-Installation zwischen Rechnern verschieben.
  * [Doctor](</de/gateway/doctor>): Integritätsprüfung nach der Migration.
  * [Agent-Arbeitsbereich](</de/concepts/agent-workspace>): wo `SOUL.md`, `AGENTS.md` und Speicherdateien liegen.


Was this useful?YesNo