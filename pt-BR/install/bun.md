---
title: Bun (experimental)
source_url: https://docs.openclaw.ai/pt-BR/install/bun
scraped_at: 2026-05-25
---

Bun é um runtime local opcional para executar TypeScript diretamente (`bun run ...`, `bun --watch ...`). O gerenciador de pacotes padrão continua sendo `pnpm`, que é totalmente compatível e usado pelo ferramental da documentação. Bun não consegue usar `pnpm-lock.yaml` e o ignorará.

## Instalação

* ### Instalar dependências

shCopy code
[code]
    bun install
[/code]

`bun.lock` / `bun.lockb` estão no gitignore, portanto não há rotatividade no repositório. Para ignorar completamente gravações de lockfile:

shCopy code
[code]
    bun install --no-save
[/code]

* ### Compilar e testar

shCopy code
[code]
    bun run buildbun run vitest run
[/code]

## Scripts de ciclo de vida

Bun bloqueia scripts de ciclo de vida de dependências, a menos que sejam explicitamente confiáveis. Para este repositório, os scripts comumente bloqueados não são necessários:

  * `baileys` `preinstall` \-- verifica se a versão principal do Node é >= 20 (OpenClaw usa Node 24 por padrão e ainda oferece suporte ao Node 22 LTS, atualmente `22.16+`)
  * `protobufjs` `postinstall` \-- emite avisos sobre esquemas de versão incompatíveis (sem artefatos de build)


Se você encontrar um problema de runtime que exija esses scripts, confie neles explicitamente:

shCopy code
[code]
    bun pm trust baileys protobufjs
[/code]

## Ressalvas

Alguns scripts ainda fixam pnpm diretamente no código (por exemplo, `docs:build`, `ui:*`, `protocol:check`). Execute-os via pnpm por enquanto.

## Relacionado

  * [Visão geral da instalação](</pt-BR/install>)
  * [Node.js](</pt-BR/install/node>)
  * [Atualização](</pt-BR/install/updating>)


Was this useful?YesNo