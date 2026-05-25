---
title: Einrichtung
source_url: https://docs.openclaw.ai/de/cli/setup
scraped_at: 2026-05-25
---

# `openclaw setup`

Initialisiert die Basiskonfiguration und den Agent-Arbeitsbereich. Wenn ein Onboarding-Flag vorhanden ist, wird außerdem der Assistent ausgeführt.

## Optionen

Flag | Beschreibung  
---|---  
`--workspace <dir>` | Agent-Arbeitsbereichsverzeichnis (Standard `~/.openclaw/workspace`; gespeichert als `agents.defaults.workspace`).  
`--wizard` | Interaktives Onboarding ausführen.  
`--non-interactive` | Onboarding ohne Eingabeaufforderungen ausführen.  
`--mode <mode>` | Onboarding-Modus: `local` oder `remote`.  
`--import-from <provider>` | Migrations-Provider, der während des Onboardings ausgeführt werden soll.  
`--import-source <path>` | Quell-Agent-Home für `--import-from`.  
`--import-secrets` | Unterstützte Secrets während der Onboarding-Migration importieren.  
`--remote-url <url>` | WebSocket-URL des Remote-Gateway.  
`--remote-token <token>` | Token für das Remote-Gateway (optional).  
  
### Automatische Auslösung des Assistenten

`openclaw setup` führt den Assistenten aus, wenn eines dieser Flags explizit vorhanden ist, auch ohne `--wizard`:

`--wizard`, `--non-interactive`, `--mode`, `--import-from`, `--import-source`, `--import-secrets`, `--remote-url`, `--remote-token`.

## Beispiele

bashCopy code
[code]
    openclaw setupopenclaw setup --workspace ~/.openclaw/workspaceopenclaw setup --wizardopenclaw setup --wizard --import-from hermes --import-source ~/.hermesopenclaw setup --non-interactive --mode remote --remote-url wss://gateway-host:18789 --remote-token <token>
[/code]

## Hinweise

  * Einfaches `openclaw setup` initialisiert Konfiguration und Arbeitsbereich, ohne den vollständigen Onboarding-Ablauf auszuführen.
  * Führen Sie nach einem einfachen setup `openclaw onboard` für den vollständig geführten Ablauf, `openclaw configure` für gezielte Änderungen oder `openclaw channels add` aus, um Channel-Konten hinzuzufügen.
  * Wenn Hermes-Zustand erkannt wird, kann interaktives Onboarding die Migration automatisch anbieten. Import-Onboarding erfordert ein frisches setup; verwenden Sie [Migrieren](</de/cli/migrate>) für Testlaufpläne, Backups und den Überschreibmodus außerhalb des Onboardings.


## Verwandte Themen

  * [CLI-Referenz](</de/cli>)
  * [Onboarding (CLI)](</de/start/wizard>)
  * [Erste Schritte](</de/start/getting-started>)
  * [Installationsübersicht](</de/install>)


Was this useful?YesNo