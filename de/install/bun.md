---
title: Bun (experimentell)
source_url: https://docs.openclaw.ai/de/install/bun
scraped_at: 2026-05-25
---

Bun ist eine optionale lokale Runtime, um TypeScript direkt auszuführen (`bun run ...`, `bun --watch ...`). Der Standard-Paketmanager bleibt `pnpm`, der vollständig unterstützt und vom Dokumentations-Tooling verwendet wird. Bun kann `pnpm-lock.yaml` nicht verwenden und ignoriert es.

## Installation

* ### Install dependencies

shCopy code
[code]
    bun install
[/code]

`bun.lock` / `bun.lockb` werden von Git ignoriert, sodass keine Repo-Änderungen entstehen. Um das Schreiben von Lockfiles vollständig zu überspringen:

shCopy code
[code]
    bun install --no-save
[/code]

* ### Build and test

shCopy code
[code]
    bun run buildbun run vitest run
[/code]

## Lifecycle-Skripte

Bun blockiert Lifecycle-Skripte von Abhängigkeiten, sofern ihnen nicht ausdrücklich vertraut wird. Für dieses Repo sind die üblicherweise blockierten Skripte nicht erforderlich:

  * `baileys` `preinstall` \-- prüft Node-Major >= 20 (OpenClaw verwendet standardmäßig Node 24 und unterstützt weiterhin Node 22 LTS, derzeit `22.16+`)
  * `protobufjs` `postinstall` \-- gibt Warnungen zu inkompatiblen Versionsschemata aus (keine Build-Artefakte)


Wenn ein Runtime-Problem auftritt, das diese Skripte erfordert, vertrauen Sie ihnen ausdrücklich:

shCopy code
[code]
    bun pm trust baileys protobufjs
[/code]

## Einschränkungen

Einige Skripte codieren pnpm weiterhin fest (zum Beispiel `docs:build`, `ui:*`, `protocol:check`). Führen Sie diese vorerst über pnpm aus.

## Verwandte Themen

  * [Installationsübersicht](</de/install>)
  * [Node.js](</de/install/node>)
  * [Aktualisieren](</de/install/updating>)


Was this useful?YesNo