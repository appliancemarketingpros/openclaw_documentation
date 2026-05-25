---
title: Pi-Entwicklungsworkflow
source_url: https://docs.openclaw.ai/de/pi-dev
scraped_at: 2026-05-25
---

Ein sinnvoller Workflow für die Arbeit an der Pi-Integration in OpenClaw.

## Typprüfung und Linting

  * Standardmäßiger lokaler Gate: `pnpm check`
  * Build-Gate: `pnpm build`, wenn sich die Änderung auf Build-Ausgaben, Paketierung oder Lazy-Loading-/Modulgrenzen auswirken kann
  * Vollständiger Landing-Gate für Pi-lastige Änderungen: `pnpm check && pnpm test`


## Pi-Tests ausführen

Führen Sie die Pi-fokussierte Testsuite direkt mit Vitest aus:

bashCopy code
[code]
    pnpm test \  "src/agents/pi-*.test.ts" \  "src/agents/pi-embedded-*.test.ts" \  "src/agents/pi-tools*.test.ts" \  "src/agents/pi-settings.test.ts" \  "src/agents/pi-tool-definition-adapter*.test.ts" \  "src/agents/pi-hooks/**/*.test.ts"
[/code]

So schließen Sie die Live-Provider-Übung ein:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test src/agents/pi-embedded-runner-extraparams.live.test.ts
[/code]

Dies deckt die wichtigsten Pi-Unit-Suites ab:

  * `src/agents/pi-*.test.ts`
  * `src/agents/pi-embedded-*.test.ts`
  * `src/agents/pi-tools*.test.ts`
  * `src/agents/pi-settings.test.ts`
  * `src/agents/pi-tool-definition-adapter.test.ts`
  * `src/agents/pi-hooks/*.test.ts`


## Manuelles Testen

Empfohlener Ablauf:

  * Führen Sie den Gateway im Entwicklungsmodus aus: 
    * `pnpm gateway:dev`
  * Lösen Sie den Agenten direkt aus: 
    * `pnpm openclaw agent --message "Hello" --thinking low`
  * Verwenden Sie die TUI für interaktives Debugging: 
    * `pnpm tui`


Fordern Sie für Tool-Call-Verhalten eine `read`\- oder `exec`-Aktion an, damit Sie Tool-Streaming und Payload-Verarbeitung sehen können.

## Zurücksetzen auf einen sauberen Ausgangszustand

Der Status befindet sich im OpenClaw-Statusverzeichnis. Standardmäßig ist das `~/.openclaw`. Wenn `OPENCLAW_STATE_DIR` gesetzt ist, verwenden Sie stattdessen dieses Verzeichnis.

So setzen Sie alles zurück:

  * `openclaw.json` für die Konfiguration
  * `agents/<agentId>/agent/auth-profiles.json` für Modell-Authentifizierungsprofile (API-Schlüssel + OAuth)
  * `credentials/` für Provider-/Kanalstatus, der sich noch außerhalb des Authentifizierungsprofil-Speichers befindet
  * `agents/<agentId>/sessions/` für den Sitzungsverlauf des Agenten
  * `agents/<agentId>/sessions/sessions.json` für den Sitzungsindex
  * `sessions/`, falls Legacy-Pfade vorhanden sind
  * `workspace/`, wenn Sie einen leeren Arbeitsbereich möchten


Wenn Sie nur Sitzungen zurücksetzen möchten, löschen Sie `agents/<agentId>/sessions/` für diesen Agenten. Wenn Sie die Authentifizierung behalten möchten, lassen Sie `agents/<agentId>/agent/auth-profiles.json` und jeglichen Provider-Status unter `credentials/` unverändert.

## Referenzen

  * [Testen](</de/help/testing>)
  * [Erste Schritte](</de/start/getting-started>)


## Verwandt

  * [Architektur der Pi-Integration](</de/pi>)


Was this useful?YesNo