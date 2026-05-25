---
title: Bun (experimental)
source_url: https://docs.openclaw.ai/es/install/bun
scraped_at: 2026-05-25
---

Bun es un runtime local opcional para ejecutar TypeScript directamente (`bun run ...`, `bun --watch ...`). El gestor de paquetes predeterminado sigue siendo `pnpm`, que es totalmente compatible y lo usan las herramientas de documentación. Bun no puede usar `pnpm-lock.yaml` y lo ignorará.

## Instalar

* ### Instalar dependencias

shCopy code
[code]
    bun install
[/code]

`bun.lock` / `bun.lockb` están ignorados por git, así que no hay cambios en el repo. Para omitir por completo las escrituras del archivo de bloqueo:

shCopy code
[code]
    bun install --no-save
[/code]

* ### Compilar y probar

shCopy code
[code]
    bun run buildbun run vitest run
[/code]

## Scripts de ciclo de vida

Bun bloquea los scripts de ciclo de vida de las dependencias a menos que se confíe explícitamente en ellos. Para este repo, los scripts que se bloquean con frecuencia no son necesarios:

  * `baileys` `preinstall` \-- comprueba que la versión mayor de Node sea >= 20 (OpenClaw usa Node 24 de forma predeterminada y aún admite Node 22 LTS, actualmente `22.16+`)
  * `protobufjs` `postinstall` \-- emite advertencias sobre esquemas de versión incompatibles (sin artefactos de compilación)


Si encuentras un problema de runtime que requiere estos scripts, confía en ellos explícitamente:

shCopy code
[code]
    bun pm trust baileys protobufjs
[/code]

## Advertencias

Algunos scripts aún tienen pnpm codificado directamente (por ejemplo, `docs:build`, `ui:*`, `protocol:check`). Ejecútalos mediante pnpm por ahora.

## Relacionado

  * [Resumen de instalación](</es/install>)
  * [Node.js](</es/install/node>)
  * [Actualizar](</es/install/updating>)


Was this useful?YesNo