---
title: CLI de transcripciones
source_url: https://docs.openclaw.ai/es/cli/transcripts
scraped_at: 2026-06-29
---

Get started

# `openclaw transcripts`

Inspecciona las transcripciones escritas por la herramienta principal `transcripts` de OpenClaw. Esta CLI es de solo lectura; la captura, la importación y el resumen pertenecen a la herramienta del agente y a las fuentes de inicio automático configuradas.

Usa la CLI cuando quieras encontrar las notas de ayer, abrir el archivo Markdown en un editor, enviar una transcripción a otra herramienta o depurar dónde quedó guardada una sesión en el disco. No inicia ni detiene la captura.

Los artefactos se encuentran en el directorio de estado de OpenClaw:

textCopy code
[code]
    $OPENCLAW_STATE_DIR/transcripts/YYYY-MM-DD/<session>/  metadata.json  transcript.jsonl  summary.json  summary.md
[/code]

El directorio de estado predeterminado es `~/.openclaw`; configura `OPENCLAW_STATE_DIR` para usar uno diferente. El directorio de fecha proviene de la hora de inicio de la sesión, y el directorio de sesión es un segmento seguro del sistema de archivos derivado del id de la sesión.

## Comandos

bashCopy code
[code]
    openclaw transcripts listopenclaw transcripts show <session>openclaw transcripts show YYYY-MM-DD/<session>openclaw transcripts path <session>openclaw transcripts path YYYY-MM-DD/<session>openclaw transcripts path <session> --diropenclaw transcripts path <session> --metadataopenclaw transcripts path <session> --transcriptopenclaw transcripts list --jsonopenclaw transcripts show <session> --jsonopenclaw transcripts path <session> --json
[/code]

  * `list`: enumera las sesiones almacenadas, el selector con fecha, la hora de inicio, el título y la ruta de `summary.md`.
  * `show <session>`: imprime el `summary.md` almacenado.
  * `path <session>`: imprime la ruta de `summary.md`.
  * `path <session> --dir`: imprime el directorio de la sesión.
  * `path <session> --metadata`: imprime `metadata.json`.
  * `path <session> --transcript`: imprime `transcript.jsonl`.
  * `--json`: imprime salida legible por máquina.


Cuando un id de sesión legible por humanos se repite en varios días, usa el selector con fecha de `list`, por ejemplo `openclaw transcripts show 2026-05-22/standup`. Los ids de sesión predeterminados incluyen una marca de tiempo y un sufijo aleatorio; configura ids de sesión fijos solo cuando sean únicos dentro del día.

## Salida

`list` imprime una sesión por línea:

textCopy code
[code]
    2026-05-22/standup  2026-05-22T09:00:00.000Z  Weekly standup  /Users/alex/.openclaw/transcripts/2026-05-22/standup/summary.md
[/code]

La salida está separada por tabulaciones. Las columnas son selector, hora de inicio, título y ruta del resumen. El selector es el valor más seguro para volver a pasarlo a `show` o `path`.

`list --json` imprime objetos con:

  * `sessionId`
  * `selector`
  * `date`
  * `title`
  * `startedAt`
  * `stoppedAt`
  * `source`
  * `path`
  * `summaryPath`
  * `hasSummary`


`show --json` devuelve los metadatos de sesión almacenados, el selector, el directorio de la sesión, la ruta del resumen y el texto Markdown del resumen. `path --json` devuelve la ruta seleccionada y si ese archivo existe.

## Muchas reuniones por día

Transcripts agrupa las sesiones por fecha y luego por id de sesión. Diez reuniones en un día se convierten en diez carpetas hermanas:

textCopy code
[code]
    ~/.openclaw/transcripts/2026-05-22/  transcript-2026-05-22T09-00-00-000Z-a1b2c3d4/  transcript-2026-05-22T10-30-00-000Z-b2c3d4e5/  standup/
[/code]

Usa ids generados de forma predeterminada para la mayoría de las automatizaciones. Usa un id fijo como `standup` solo cuando el mismo id no se vaya a usar dos veces en la misma fecha.

## Resúmenes faltantes

Las sesiones en vivo escriben `summary.md` cuando la sesión se detiene. Las transcripciones importadas escriben `summary.md` inmediatamente después de la importación. Una sesión aún puede aparecer en `list` sin resumen cuando la captura está activa, un proveedor falló durante la detención o los metadatos se escribieron antes de que llegara cualquier intervención.

Usa `path <session> --transcript` para inspeccionar la transcripción de solo anexado y usa la acción `summarize` de la herramienta `transcripts` para regenerar el resumen Markdown.

## Configuración

La captura de transcripciones es opcional porque las fuentes en vivo pueden unirse al audio de reuniones y grabarlo. Habilita la herramienta con `transcripts.enabled` de nivel superior:

jsonCopy code
[code]
    {  "transcripts": {    "enabled": true,    "maxUtterances": 2000  }}
[/code]

Configura las fuentes de inicio automático con `transcripts.autoStart` en `openclaw.json`. Cada entrada se habilita al estar presente; omite una entrada para deshabilitar esa fuente.

jsonCopy code
[code]
    {  "transcripts": {    "enabled": true,    "autoStart": [      {        "providerId": "discord-voice",        "guildId": "1234567890",        "channelId": "2345678901"      },      {        "providerId": "slack-huddle",        "accountId": "workspace",        "channelId": "C123"      }    ]  }}
[/code]

Was this useful?YesNo

Open issue