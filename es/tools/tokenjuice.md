---
title: Tokenjuice
source_url: https://docs.openclaw.ai/es/tools/tokenjuice
scraped_at: 2026-05-25
---

`tokenjuice` es un plugin incluido opcional que compacta los resultados ruidosos de las herramientas `exec` y `bash` después de que el comando ya se haya ejecutado.

Cambia el `tool_result` devuelto, no el comando en sí. Tokenjuice no reescribe la entrada del shell, no vuelve a ejecutar comandos ni cambia los códigos de salida.

Hoy esto se aplica a ejecuciones incrustadas de Pi y a herramientas dinámicas de OpenClaw en el arnés app-server de Codex. Tokenjuice se engancha al middleware de resultados de herramientas de OpenClaw y recorta la salida antes de que vuelva a la sesión activa del arnés.

## Habilitar el plugin

Ruta rápida:

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled true
[/code]

Equivalente:

bashCopy code
[code]
    openclaw plugins enable tokenjuice
[/code]

OpenClaw ya incluye el plugin. No hay un paso separado de `plugins install` ni `tokenjuice install openclaw`.

Si prefieres editar la configuración directamente:

json5Copy code
[code]
    {  plugins: {    entries: {      tokenjuice: {        enabled: true,      },    },  },}
[/code]

## Qué cambia tokenjuice

  * Compacta los resultados ruidosos de `exec` y `bash` antes de que se devuelvan a la sesión.
  * Mantiene intacta la ejecución original del comando.
  * Conserva las lecturas exactas de contenido de archivos y otros comandos que tokenjuice debe dejar sin procesar.
  * Sigue siendo opcional: desactiva el plugin si quieres salida literal en todas partes.


## Verificar que funciona

  1. Habilita el plugin.
  2. Inicia una sesión que pueda llamar a `exec`.
  3. Ejecuta un comando ruidoso como `git status`.
  4. Comprueba que el resultado devuelto por la herramienta sea más corto y más estructurado que la salida sin procesar del shell.


## Deshabilitar el plugin

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled false
[/code]

O bien:

bashCopy code
[code]
    openclaw plugins disable tokenjuice
[/code]

## Relacionado

  * [Exec tool](</es/tools/exec>)
  * [Thinking levels](</es/tools/thinking>)
  * [Context engine](</es/concepts/context-engine>)


Was this useful?YesNo