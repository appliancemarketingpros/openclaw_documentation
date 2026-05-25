---
title: Migrationsleitfaden
source_url: https://docs.openclaw.ai/de/install/migrating
scraped_at: 2026-05-25
---

OpenClaw unterstützt drei Migrationspfade: den Import aus einem anderen Agentensystem, den Umzug einer bestehenden Installation auf einen neuen Rechner und das direkte Upgrade eines Plugins.

## Import aus einem anderen Agentensystem

Verwenden Sie die mitgelieferten Migrations-Provider, um Anweisungen, MCP-Server, Skills, Modellkonfiguration und optional API-Schlüssel in OpenClaw zu übernehmen. Pläne werden vor jeder Änderung in der Vorschau angezeigt, Geheimnisse werden in Berichten redigiert, und die Anwendung wird durch ein verifiziertes Backup abgesichert.

[**Migration von Claude** Importieren Sie den Zustand von Claude Code und Claude Desktop, einschließlich `CLAUDE.md`, MCP-Servern, Skills und Projektbefehlen. ](</de/install/migrating-claude>) [**Migration von Hermes** Importieren Sie Hermes-Konfiguration, Provider, MCP-Server, Speicher, Skills und unterstützte `.env`-Schlüssel. ](</de/install/migrating-hermes>)

Der CLI-Einstiegspunkt ist [`openclaw migrate`](</de/cli/migrate>). Das Onboarding kann ebenfalls eine Migration anbieten, wenn es eine bekannte Quelle erkennt (`openclaw onboard --flow import`).

## OpenClaw auf einen neuen Rechner umziehen

Kopieren Sie das **Zustandsverzeichnis** (standardmäßig `~/.openclaw/`) und Ihren **Arbeitsbereich** , um Folgendes zu erhalten:

  * **Konfiguration** — `openclaw.json` und alle Gateway-Einstellungen.
  * **Authentifizierung** — agentenspezifische `auth-profiles.json` (API-Schlüssel plus OAuth) sowie beliebiger Channel- oder Provider-Zustand unter `credentials/`.
  * **Sitzungen** — Konversationsverlauf und Agentenzustand.
  * **Channel-Zustand** — WhatsApp-Anmeldung, Telegram-Sitzung und Ähnliches.
  * **Arbeitsbereichsdateien** — `MEMORY.md`, `USER.md`, Skills und Prompts.


### Migrationsschritte

* ### Gateway stoppen und Backup erstellen

Stoppen Sie auf dem **alten** Rechner das Gateway, damit sich Dateien während des Kopierens nicht ändern, und archivieren Sie anschließend:

bashCopy code
[code]
    openclaw gateway stopcd ~tar -czf openclaw-state.tgz .openclaw
[/code]

Wenn Sie mehrere Profile verwenden (zum Beispiel `~/.openclaw-work`), archivieren Sie jedes separat.

* ### OpenClaw auf dem neuen Rechner installieren

[Installieren](</de/install>) Sie die CLI (und Node, falls erforderlich) auf dem neuen Rechner. Es ist in Ordnung, wenn das Onboarding ein frisches `~/.openclaw/` erstellt. Sie überschreiben es im nächsten Schritt.

* ### Zustandsverzeichnis und Arbeitsbereich kopieren

Übertragen Sie das Archiv per `scp`, `rsync -a` oder über ein externes Laufwerk und extrahieren Sie es dann:

bashCopy code
[code]
    cd ~tar -xzf openclaw-state.tgz
[/code]

Stellen Sie sicher, dass versteckte Verzeichnisse enthalten waren und der Dateibesitz dem Benutzer entspricht, der das Gateway ausführen wird.

* ### Doctor ausführen und überprüfen

Führen Sie auf dem neuen Rechner [Doctor](</de/gateway/doctor>) aus, um Konfigurationsmigrationen anzuwenden und Dienste zu reparieren:

bashCopy code
[code]
    openclaw doctoropenclaw gateway restartopenclaw status
[/code]

Wenn Telegram oder Discord den standardmäßigen Env-Fallback (`TELEGRAM_BOT_TOKEN` oder `DISCORD_BOT_TOKEN`) verwendet, verifizieren Sie, dass die migrierte `.env` im Zustandsverzeichnis diese Schlüssel enthält, ohne die geheimen Werte auszugeben:

bashCopy code
[code]
    awk -F= '/^(TELEGRAM_BOT_TOKEN|DISCORD_BOT_TOKEN)=/ { print $1 "=present" }' ~/.openclaw/.env
[/code]

`openclaw doctor` warnt außerdem, wenn ein aktiviertes Standardkonto für Telegram oder Discord kein konfiguriertes Token hat und die passende Umgebungsvariable für den Doctor-Prozess nicht verfügbar ist.

### Häufige Fallstricke

Profil- oder Zustandsverzeichnis stimmt nicht überein

Wenn das alte Gateway `--profile` oder `OPENCLAW_STATE_DIR` verwendet hat und das neue nicht, erscheinen Channels als abgemeldet und Sitzungen sind leer. Starten Sie das Gateway mit demselben Profil oder Zustandsverzeichnis, das Sie migriert haben, und führen Sie dann erneut `openclaw doctor` aus.

Nur openclaw.json kopieren

Die Konfigurationsdatei allein reicht nicht aus. Modell-Authentifizierungsprofile liegen unter `agents/<agentId>/agent/auth-profiles.json`, und Channel- sowie Provider-Zustand liegt unter `credentials/`. Migrieren Sie immer das **gesamte** Zustandsverzeichnis.

Berechtigungen und Besitz

Wenn Sie als root kopiert oder den Benutzer gewechselt haben, kann das Gateway möglicherweise keine Zugangsdaten lesen. Stellen Sie sicher, dass das Zustandsverzeichnis und der Arbeitsbereich dem Benutzer gehören, der das Gateway ausführt.

Remote-Modus

Wenn Ihre UI auf ein **entferntes** Gateway zeigt, besitzt der entfernte Host Sitzungen und Arbeitsbereich. Migrieren Sie den Gateway-Host selbst, nicht Ihren lokalen Laptop. Siehe [FAQ](</de/help/faq#where-things-live-on-disk>).

Geheimnisse in Backups

Das Zustandsverzeichnis enthält Authentifizierungsprofile, Channel-Zugangsdaten und anderen Provider-Zustand. Speichern Sie Backups verschlüsselt, vermeiden Sie unsichere Übertragungskanäle und rotieren Sie Schlüssel, wenn Sie eine Offenlegung vermuten.

### Prüfliste zur Verifizierung

Bestätigen Sie auf dem neuen Rechner:

  * [ ] `openclaw status` zeigt, dass das Gateway läuft.
  * [ ] Channels sind weiterhin verbunden (keine erneute Kopplung erforderlich).
  * [ ] Das Dashboard öffnet sich und zeigt bestehende Sitzungen.
  * [ ] Arbeitsbereichsdateien (Speicher, Konfigurationen) sind vorhanden.


## Plugin direkt upgraden

Direkte Plugin-Upgrades behalten dieselbe Plugin-ID und dieselben Konfigurationsschlüssel bei, können aber den Zustand auf dem Datenträger in das aktuelle Layout verschieben. Plugin-spezifische Upgrade-Anleitungen befinden sich neben ihren Channels:

  * [Matrix-Migration](</de/channels/matrix-migration>): Grenzen der Wiederherstellung verschlüsselten Zustands, automatisches Snapshot-Verhalten und manuelle Wiederherstellungsbefehle.


## Verwandte Themen

  * [`openclaw migrate`](</de/cli/migrate>): CLI-Referenz für systemübergreifende Importe.
  * [Installationsübersicht](</de/install>): alle Installationsmethoden.
  * [Doctor](</de/gateway/doctor>): Integritätsprüfung nach der Migration.
  * [Deinstallation](</de/install/uninstall>): OpenClaw sauber entfernen.


Was this useful?YesNo