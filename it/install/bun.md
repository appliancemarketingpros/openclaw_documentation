---
title: Bun (sperimentale)
source_url: https://docs.openclaw.ai/it/install/bun
scraped_at: 2026-05-25
---

Bun è un runtime locale opzionale per eseguire TypeScript direttamente (`bun run ...`, `bun --watch ...`). Il package manager predefinito rimane `pnpm`, che è pienamente supportato e usato dagli strumenti della documentazione. Bun non può usare `pnpm-lock.yaml` e lo ignorerà.

## Installazione

* ### Install dependencies

shCopy code
[code]
    bun install
[/code]

`bun.lock` / `bun.lockb` sono ignorati da git, quindi non generano modifiche nel repo. Per evitare del tutto la scrittura del lockfile:

shCopy code
[code]
    bun install --no-save
[/code]

* ### Build and test

shCopy code
[code]
    bun run buildbun run vitest run
[/code]

## Script del ciclo di vita

Bun blocca gli script del ciclo di vita delle dipendenze, a meno che non siano considerati esplicitamente attendibili. Per questo repo, gli script comunemente bloccati non sono necessari:

  * `baileys` `preinstall` \-- verifica che la versione principale di Node sia >= 20 (OpenClaw usa per impostazione predefinita Node 24 e supporta ancora Node 22 LTS, attualmente `22.16+`)
  * `protobufjs` `postinstall` \-- emette avvisi su schemi di versione incompatibili (nessun artefatto di build)


Se riscontri un problema di runtime che richiede questi script, rendili esplicitamente attendibili:

shCopy code
[code]
    bun pm trust baileys protobufjs
[/code]

## Avvertenze

Alcuni script hanno ancora pnpm hardcoded (per esempio `docs:build`, `ui:*`, `protocol:check`). Per ora eseguili tramite pnpm.

## Correlati

  * [Panoramica dell'installazione](</it/install>)
  * [Node.js](</it/install/node>)
  * [Aggiornamento](</it/install/updating>)


Was this useful?YesNo