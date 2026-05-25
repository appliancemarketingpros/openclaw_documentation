---
title: Fallo de Node + tsx
source_url: https://docs.openclaw.ai/es/debug/node-issue
scraped_at: 2026-05-25
---

# Fallo de Node + tsx "__name is not a function"

## Resumen

Ejecutar OpenClaw mediante Node con `tsx` falla al iniciar con:

CodeCopy code
[code]
    [openclaw] Failed to start CLI: TypeError: __name is not a function    at createSubsystemLogger (.../src/logging/subsystem.ts:203:25)    at .../src/agents/auth-profiles/constants.ts:25:20
[/code]

Esto comenzó después de cambiar los scripts de desarrollo de Bun a `tsx` (commit `2871657e`, 2026-01-06). La misma ruta de runtime funcionaba con Bun.

## Entorno

  * Node: v25.x (observado en v25.3.0)
  * tsx: 4.21.0
  * SO: macOS (la reproducción también es probable en otras plataformas que ejecuten Node 25)


## Reproducción (solo Node)

bashCopy code
[code]
    # in repo rootnode --versionpnpm installnode --import tsx src/entry.ts status
[/code]

## Reproducción mínima en el repositorio

bashCopy code
[code]
    node --import tsx scripts/repro/tsx-name-repro.ts
[/code]

## Comprobación de versión de Node

  * Node 25.3.0: falla
  * Node 22.22.0 (Homebrew `node@22`): falla
  * Node 24: aún no está instalado aquí; necesita verificación


## Notas / hipótesis

  * `tsx` usa esbuild para transformar TS/ESM. `keepNames` de esbuild emite un helper `__name` y envuelve las definiciones de funciones con `__name(...)`.
  * El fallo indica que `__name` existe pero no es una función en runtime, lo que implica que el helper falta o se sobrescribe para este módulo en la ruta del cargador de Node 25.
  * Se han informado problemas similares con el helper `__name` en otros consumidores de esbuild cuando el helper falta o se reescribe.


## Historial de regresión

  * `2871657e` (2026-01-06): los scripts cambiaron de Bun a tsx para hacer que Bun fuera opcional.
  * Antes de eso (ruta de Bun), `openclaw status` y `gateway:watch` funcionaban.


## Soluciones temporales

  * Usa Bun para los scripts de desarrollo (reversión temporal actual).

  * Usa `tsgo` para la comprobación de tipos del repositorio y luego ejecuta la salida compilada:

bashCopy code
[code]pnpm tsgonode openclaw.mjs status
[/code]

  * Nota histórica: aquí se usó `tsc` mientras se depuraba este problema de Node/tsx, pero las rutas de comprobación de tipos del repositorio ahora usan `tsgo`.

  * Desactiva keepNames de esbuild en el cargador de TS si es posible (evita la inserción del helper `__name`); tsx actualmente no expone esto.

  * Prueba Node LTS (22/24) con `tsx` para ver si el problema es específico de Node 25.


## Referencias

  * <https://opennext.js.org/cloudflare/howtos/keep_names>
  * <https://esbuild.github.io/api/#keep-names>
  * <https://github.com/evanw/esbuild/issues/1031>


## Próximos pasos

  * Reproducir en Node 22/24 para confirmar la regresión de Node 25.
  * Probar `tsx` nightly o fijar a una versión anterior si existe una regresión conocida.
  * Si se reproduce en Node LTS, abrir una reproducción mínima upstream con el stack trace de `__name`.


## Relacionado

  * [Instalación de Node.js](</es/install/node>)
  * [Solución de problemas del Gateway](</es/gateway/troubleshooting>)


Was this useful?YesNo