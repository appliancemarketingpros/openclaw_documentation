---
title: Plugin personal de Zalo
source_url: https://docs.openclaw.ai/es/plugins/zalouser
scraped_at: 2026-05-25
---

Compatibilidad de Zalo Personal para OpenClaw mediante un Plugin, usando `zca-js` nativo para automatizar una cuenta normal de usuario de Zalo.

## Nomenclatura

El id de canal es `zalouser` para dejar explícito que esto automatiza una **cuenta personal de usuario de Zalo** (no oficial). Mantenemos `zalo` reservado para una posible integración futura con la API oficial de Zalo.

## Dónde se ejecuta

Este Plugin se ejecuta **dentro del proceso del Gateway**.

Si usa un Gateway remoto, instálelo/configúrelo en la **máquina que ejecuta el Gateway** y luego reinicie el Gateway.

No se requiere ningún binario externo de CLI `zca`/`openzca`.

## Instalación

### Opción A: instalar desde npm

bashCopy code
[code]
    openclaw plugins install @openclaw/zalouser
[/code]

Use el paquete sin versión para seguir la etiqueta de versión oficial actual. Fije una versión exacta solo cuando necesite una instalación reproducible.

Reinicie el Gateway después.

### Opción B: instalar desde una carpeta local (desarrollo)

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/zalouser-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

Reinicie el Gateway después.

## Configuración

La configuración del canal reside bajo `channels.zalouser` (no `plugins.entries.*`):

json5Copy code
[code]
    {  channels: {    zalouser: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

## CLI

bashCopy code
[code]
    openclaw channels login --channel zalouseropenclaw channels logout --channel zalouseropenclaw channels status --probeopenclaw message send --channel zalouser --target <threadId> --message "Hello from OpenClaw"openclaw directory peers list --channel zalouser --query "name"
[/code]

## Herramienta de agente

Nombre de la herramienta: `zalouser`

Acciones: `send`, `image`, `link`, `friends`, `groups`, `me`, `status`

Las acciones de mensaje de canal también admiten `react` para reacciones a mensajes.

## Relacionado

  * [Crear plugins](</es/plugins/building-plugins>)
  * [ClawHub](</es/clawhub>)


Was this useful?YesNo