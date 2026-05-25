---
title: Bun (experimenteel)
source_url: https://docs.openclaw.ai/nl/install/bun
scraped_at: 2026-05-25
---

Bun is een optionele lokale runtime om TypeScript rechtstreeks uit te voeren (`bun run ...`, `bun --watch ...`). De standaard pakketbeheerder blijft `pnpm`, dat volledig wordt ondersteund en door documentatietooling wordt gebruikt. Bun kan `pnpm-lock.yaml` niet gebruiken en zal het negeren.

## Installeren

* ### Afhankelijkheden installeren

shCopy code
[code]
    bun install
[/code]

`bun.lock` / `bun.lockb` staan in gitignore, dus er is geen repo-ruis. Om lockfile-wijzigingen volledig over te slaan:

shCopy code
[code]
    bun install --no-save
[/code]

* ### Bouwen en testen

shCopy code
[code]
    bun run buildbun run vitest run
[/code]

## Levenscyclusscripts

Bun blokkeert levenscyclusscripts van afhankelijkheden tenzij ze expliciet worden vertrouwd. Voor deze repo zijn de scripts die vaak worden geblokkeerd niet vereist:

  * `baileys` `preinstall` \-- controleert Node major >= 20 (OpenClaw gebruikt standaard Node 24 en ondersteunt nog steeds Node 22 LTS, momenteel `22.16+`)
  * `protobufjs` `postinstall` \-- geeft waarschuwingen over incompatibele versieschema's (geen buildartefacten)


Als je een runtimeprobleem tegenkomt waarvoor deze scripts nodig zijn, vertrouw ze dan expliciet:

shCopy code
[code]
    bun pm trust baileys protobufjs
[/code]

## Kanttekeningen

Sommige scripts bevatten nog steeds hardcoded pnpm (bijvoorbeeld `docs:build`, `ui:*`, `protocol:check`). Voer die voorlopig uit via pnpm.

## Gerelateerd

  * [Installatieoverzicht](</nl/install>)
  * [Node.js](</nl/install/node>)
  * [Bijwerken](</nl/install/updating>)


Was this useful?YesNo