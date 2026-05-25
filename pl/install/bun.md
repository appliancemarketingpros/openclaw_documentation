---
title: Bun (eksperymentalny)
source_url: https://docs.openclaw.ai/pl/install/bun
scraped_at: 2026-05-25
---

Bun to opcjonalne lokalne środowisko uruchomieniowe do bezpośredniego uruchamiania TypeScript (`bun run ...`, `bun --watch ...`). Domyślnym menedżerem pakietów pozostaje `pnpm`, który jest w pełni obsługiwany i używany przez narzędzia dokumentacji. Bun nie może używać `pnpm-lock.yaml` i będzie go ignorować.

## Instalacja

* ### Zainstaluj zależności

shCopy code
[code]
    bun install
[/code]

`bun.lock` / `bun.lockb` są ignorowane przez git, więc w repozytorium nie powstają zmiany. Aby całkowicie pominąć zapisywanie pliku lockfile:

shCopy code
[code]
    bun install --no-save
[/code]

* ### Zbuduj i przetestuj

shCopy code
[code]
    bun run buildbun run vitest run
[/code]

## Skrypty cyklu życia

Bun blokuje skrypty cyklu życia zależności, chyba że zostaną jawnie uznane za zaufane. W tym repozytorium często blokowane skrypty nie są wymagane:

  * `baileys` `preinstall` \-- sprawdza główną wersję Node >= 20 (OpenClaw domyślnie używa Node 24 i nadal obsługuje Node 22 LTS, obecnie `22.16+`)
  * `protobufjs` `postinstall` \-- emituje ostrzeżenia o niezgodnych schematach wersjonowania (brak artefaktów kompilacji)


Jeśli napotkasz problem w czasie działania, który wymaga tych skryptów, jawnie oznacz je jako zaufane:

shCopy code
[code]
    bun pm trust baileys protobufjs
[/code]

## Zastrzeżenia

Niektóre skrypty nadal mają na stałe wpisane pnpm (na przykład `docs:build`, `ui:*`, `protocol:check`). Na razie uruchamiaj je przez pnpm.

## Powiązane

  * [Przegląd instalacji](</pl/install>)
  * [Node.js](</pl/install/node>)
  * [Aktualizowanie](</pl/install/updating>)


Was this useful?YesNo