---
title: Arresto anomalo di Node + tsx
source_url: https://docs.openclaw.ai/it/debug/node-issue
scraped_at: 2026-05-25
---

# Arresto anomalo di Node + tsx con "__name is not a function"

## Riepilogo

L'esecuzione di OpenClaw tramite Node con `tsx` non riesce all'avvio con:

CodeCopy code
[code]
    [openclaw] Failed to start CLI: TypeError: __name is not a function    at createSubsystemLogger (.../src/logging/subsystem.ts:203:25)    at .../src/agents/auth-profiles/constants.ts:25:20
[/code]

Il problema è iniziato dopo il passaggio degli script di sviluppo da Bun a `tsx` (commit `2871657e`, 2026-01-06). Lo stesso percorso di runtime funzionava con Bun.

## Ambiente

  * Node: v25.x (osservato su v25.3.0)
  * tsx: 4.21.0
  * OS: macOS (riproduzione probabilmente possibile anche su altre piattaforme che eseguono Node 25)


## Riproduzione (solo Node)

bashCopy code
[code]
    # in repo rootnode --versionpnpm installnode --import tsx src/entry.ts status
[/code]

## Riproduzione minima nel repo

bashCopy code
[code]
    node --import tsx scripts/repro/tsx-name-repro.ts
[/code]

## Verifica della versione di Node

  * Node 25.3.0: fallisce
  * Node 22.22.0 (Homebrew `node@22`): fallisce
  * Node 24: non ancora installato qui; richiede verifica


## Note / ipotesi

  * `tsx` usa esbuild per trasformare TS/ESM. Il `keepNames` di esbuild emette un helper `__name` e avvolge le definizioni di funzione con `__name(...)`.
  * L'arresto anomalo indica che `__name` esiste ma non è una funzione a runtime, il che implica che l'helper sia mancante o sovrascritto per questo modulo nel percorso del loader di Node 25.
  * Problemi simili dell'helper `__name` sono stati segnalati in altri consumer di esbuild quando l'helper è mancante o riscritto.


## Cronologia della regressione

  * `2871657e` (2026-01-06): gli script sono passati da Bun a tsx per rendere Bun opzionale.
  * Prima di allora (percorso Bun), `openclaw status` e `gateway:watch` funzionavano.


## Soluzioni alternative

  * Usare Bun per gli script di sviluppo (ripristino temporaneo attuale).

  * Usare `tsgo` per il controllo dei tipi del repo, poi eseguire l'output compilato:

bashCopy code
[code]pnpm tsgonode openclaw.mjs status
[/code]

  * Nota storica: `tsc` è stato usato qui durante il debug di questo problema Node/tsx, ma le lane di controllo dei tipi del repo ora usano `tsgo`.

  * Disabilitare esbuild keepNames nel loader TS, se possibile (impedisce l'inserimento dell'helper `__name`); attualmente tsx non lo espone.

  * Testare Node LTS (22/24) con `tsx` per vedere se il problema è specifico di Node 25.


## Riferimenti

  * <https://opennext.js.org/cloudflare/howtos/keep_names>
  * <https://esbuild.github.io/api/#keep-names>
  * <https://github.com/evanw/esbuild/issues/1031>


## Passaggi successivi

  * Riprodurre su Node 22/24 per confermare la regressione di Node 25.
  * Testare `tsx` nightly o fissarlo a una versione precedente se esiste una regressione nota.
  * Se si riproduce su Node LTS, aprire una riproduzione minima upstream con lo stack trace di `__name`.


## Correlati

  * [Installazione di Node.js](</it/install/node>)
  * [Risoluzione dei problemi del Gateway](</it/gateway/troubleshooting>)


Was this useful?YesNo