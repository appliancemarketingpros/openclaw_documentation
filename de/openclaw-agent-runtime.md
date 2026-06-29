---
title: OpenClaw-Agentenlaufzeit-Workflow
source_url: https://docs.openclaw.ai/de/openclaw-agent-runtime
scraped_at: 2026-06-29
---

InstallAdvanced setup

Ein sinnvoller Workflow für die Arbeit an der OpenClaw-Agent-Runtime in OpenClaw.

## Typprüfung und Linting

  * Standardmäßiges lokales Gate: `pnpm check`
  * Build-Gate: `pnpm build`, wenn die Änderung Build-Ausgabe, Paketierung oder Lazy-Loading-/Modulgrenzen beeinflussen kann
  * Vollständiges Landing-Gate für Änderungen an der Agent-Runtime: `pnpm check && pnpm test`


## Agent-Runtime-Tests ausführen

Führen Sie das Agent-Runtime-Testset direkt mit Vitest aus:

bashCopy code
[code]
    pnpm test \  "src/agents/agent-*.test.ts" \  "src/agents/embedded-agent-*.test.ts" \  "src/agents/agent-tools*.test.ts" \  "src/agents/agent-settings.test.ts" \  "src/agents/agent-tool-definition-adapter*.test.ts" \  "src/agents/agent-hooks/**/*.test.ts"
[/code]

Um die Live-Provider-Übung einzuschließen:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test src/agents/embedded-agent-runner-extraparams.live.test.ts
[/code]

Dies deckt die wichtigsten Unit-Test-Suites der Agent-Runtime ab:

  * `src/agents/agent-*.test.ts`
  * `src/agents/embedded-agent-*.test.ts`
  * `src/agents/agent-tools*.test.ts`
  * `src/agents/agent-settings.test.ts`
  * `src/agents/agent-tool-definition-adapter.test.ts`
  * `src/agents/agent-hooks/*.test.ts`


## Manuelles Testen

Empfohlener Ablauf:

  * Führen Sie den Gateway im Entwicklungsmodus aus: 
    * `pnpm gateway:dev`
  * Lösen Sie den Agent direkt aus: 
    * `pnpm openclaw agent --message "Hello" --thinking low`
  * Verwenden Sie die TUI für interaktives Debugging: 
    * `pnpm tui`


Fordern Sie für das Verhalten von Tool-Aufrufen eine `read`\- oder `exec`-Aktion an, damit Sie Tool-Streaming und Payload-Verarbeitung sehen können.

## Zurücksetzen auf einen sauberen Ausgangszustand

Der State befindet sich im OpenClaw-State-Verzeichnis. Standard ist `~/.openclaw`. Wenn `OPENCLAW_STATE_DIR` gesetzt ist, verwenden Sie stattdessen dieses Verzeichnis.

Um alles zurückzusetzen:

  * `openclaw.json` für die Konfiguration
  * `agents/<agentId>/agent/auth-profiles.json` für Modell-Auth-Profile (API-Schlüssel + OAuth)
  * `credentials/` für Provider-/Channel-State, der sich noch außerhalb des Auth-Profile-Stores befindet
  * `agents/<agentId>/sessions/` für den Agent-Sitzungsverlauf
  * `agents/<agentId>/sessions/sessions.json` für den Sitzungsindex
  * `sessions/`, falls Legacy-Pfade vorhanden sind
  * `workspace/`, wenn Sie einen leeren Workspace möchten


Wenn Sie nur Sitzungen zurücksetzen möchten, löschen Sie `agents/<agentId>/sessions/` für diesen Agent. Wenn Sie Auth beibehalten möchten, lassen Sie `agents/<agentId>/agent/auth-profiles.json` und jeglichen Provider-State unter `credentials/` unverändert.

## Referenzen

  * [Testen](</de/help/testing>)
  * [Erste Schritte](</de/start/getting-started>)


## Verwandt

  * [OpenClaw-Agent-Runtime-Architektur](</de/agent-runtime-architecture>)


Was this useful?YesNo

Open issue