---
title: Bun (expérimental)
source_url: https://docs.openclaw.ai/fr/install/bun
scraped_at: 2026-05-25
---

Bun est un runtime local facultatif permettant d’exécuter TypeScript directement (`bun run ...`, `bun --watch ...`). Le gestionnaire de paquets par défaut reste `pnpm`, qui est entièrement pris en charge et utilisé par l’outillage de documentation. Bun ne peut pas utiliser `pnpm-lock.yaml` et l’ignorera.

## Installation

* ### Install dependencies

shCopy code
[code]
    bun install
[/code]

`bun.lock` / `bun.lockb` sont ignorés par git, il n’y a donc pas de modifications inutiles dans le dépôt. Pour ignorer entièrement l’écriture du fichier de verrouillage :

shCopy code
[code]
    bun install --no-save
[/code]

* ### Build and test

shCopy code
[code]
    bun run buildbun run vitest run
[/code]

## Scripts de cycle de vie

Bun bloque les scripts de cycle de vie des dépendances sauf s’ils sont explicitement approuvés. Pour ce dépôt, les scripts couramment bloqués ne sont pas requis :

  * `baileys` `preinstall` \-- vérifie que la version majeure de Node est >= 20 (OpenClaw utilise Node 24 par défaut et prend toujours en charge Node 22 LTS, actuellement `22.16+`)
  * `protobufjs` `postinstall` \-- émet des avertissements sur des schémas de version incompatibles (aucun artefact de build)


Si vous rencontrez un problème d’exécution qui nécessite ces scripts, approuvez-les explicitement :

shCopy code
[code]
    bun pm trust baileys protobufjs
[/code]

## Points à connaître

Certains scripts codent encore pnpm en dur (par exemple `docs:build`, `ui:*`, `protocol:check`). Exécutez-les via pnpm pour le moment.

## Connexe

  * [Vue d’ensemble de l’installation](</fr/install>)
  * [Node.js](</fr/install/node>)
  * [Mise à jour](</fr/install/updating>)


Was this useful?YesNo