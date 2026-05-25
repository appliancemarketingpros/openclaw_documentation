---
title: Flusso di lavoro di sviluppo per Pi
source_url: https://docs.openclaw.ai/it/pi-dev
scraped_at: 2026-05-25
---

Un flusso di lavoro sensato per lavorare sull’integrazione di Pi in OpenClaw.

## Controllo dei tipi e linting

  * Gate locale predefinito: `pnpm check`
  * Gate di build: `pnpm build` quando la modifica può influire sull’output di build, sul packaging o sui confini di lazy-loading/moduli
  * Gate completo prima del landing per modifiche sostanziali a Pi: `pnpm check && pnpm test`


## Esecuzione dei test Pi

Esegui direttamente con Vitest il set di test dedicato a Pi:

bashCopy code
[code]
    pnpm test \  "src/agents/pi-*.test.ts" \  "src/agents/pi-embedded-*.test.ts" \  "src/agents/pi-tools*.test.ts" \  "src/agents/pi-settings.test.ts" \  "src/agents/pi-tool-definition-adapter*.test.ts" \  "src/agents/pi-hooks/**/*.test.ts"
[/code]

Per includere l’esercizio live del provider:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test src/agents/pi-embedded-runner-extraparams.live.test.ts
[/code]

Questo copre le principali suite unit di Pi:

  * `src/agents/pi-*.test.ts`
  * `src/agents/pi-embedded-*.test.ts`
  * `src/agents/pi-tools*.test.ts`
  * `src/agents/pi-settings.test.ts`
  * `src/agents/pi-tool-definition-adapter.test.ts`
  * `src/agents/pi-hooks/*.test.ts`


## Test manuali

Flusso consigliato:

  * Esegui il Gateway in modalità dev: 
    * `pnpm gateway:dev`
  * Attiva direttamente l’agente: 
    * `pnpm openclaw agent --message "Hello" --thinking low`
  * Usa la TUI per il debug interattivo: 
    * `pnpm tui`


Per il comportamento delle chiamate agli strumenti, richiedi un’azione `read` o `exec` in modo da poter vedere lo streaming degli strumenti e la gestione dei payload.

## Ripristino da zero

Lo stato si trova nella directory di stato di OpenClaw. Il valore predefinito è `~/.openclaw`. Se `OPENCLAW_STATE_DIR` è impostato, usa invece quella directory.

Per reimpostare tutto:

  * `openclaw.json` per la configurazione
  * `agents/<agentId>/agent/auth-profiles.json` per i profili di autenticazione del modello (chiavi API + OAuth)
  * `credentials/` per lo stato di provider/canali che vive ancora fuori dall’archivio dei profili di autenticazione
  * `agents/<agentId>/sessions/` per la cronologia delle sessioni dell’agente
  * `agents/<agentId>/sessions/sessions.json` per l’indice delle sessioni
  * `sessions/` se esistono percorsi legacy
  * `workspace/` se vuoi uno spazio di lavoro vuoto


Se vuoi reimpostare solo le sessioni, elimina `agents/<agentId>/sessions/` per quell’agente. Se vuoi mantenere l’autenticazione, lascia al loro posto `agents/<agentId>/agent/auth-profiles.json` e qualsiasi stato del provider sotto `credentials/`.

## Riferimenti

  * [Test](</it/help/testing>)
  * [Primi passi](</it/start/getting-started>)


## Correlati

  * [Architettura dell’integrazione Pi](</it/pi>)


Was this useful?YesNo