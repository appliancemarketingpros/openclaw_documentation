---
title: Llamada de voz
source_url: https://docs.openclaw.ai/es/cli/voicecall
scraped_at: 2026-05-25
---

# `openclaw voicecall`

`voicecall` es un comando proporcionado por un plugin. Solo aparece cuando el plugin de llamadas de voz está instalado y habilitado.

Cuando el Gateway está en ejecución, los comandos operativos (`call`, `start`, `continue`, `speak`, `dtmf`, `end`, `status`) se enrutan al runtime de llamadas de voz de ese Gateway. Si no se puede alcanzar ningún Gateway, recurren a un runtime de CLI independiente.

## Subcomandos

bashCopy code
[code]
    openclaw voicecall setup    [--json]openclaw voicecall smoke    [-t <phone>] [--message <text>] [--mode <m>] [--yes] [--json]openclaw voicecall call     -m <text> [-t <phone>] [--mode <m>]openclaw voicecall start    --to <phone> [--message <text>] [--mode <m>]openclaw voicecall continue --call-id <id> --message <text>openclaw voicecall speak    --call-id <id> --message <text>openclaw voicecall dtmf     --call-id <id> --digits <digits>openclaw voicecall end      --call-id <id>openclaw voicecall status   [--call-id <id>] [--json]openclaw voicecall tail     [--file <path>] [--since <n>] [--poll <ms>]openclaw voicecall latency  [--file <path>] [--last <n>]openclaw voicecall expose   [--mode <m>] [--path <p>] [--port <port>] [--serve-path <p>]
[/code]

Subcomando | Descripción  
---|---  
`setup` | Muestra comprobaciones de preparación del proveedor y del Webhook.  
`smoke` | Ejecuta comprobaciones de preparación; realiza una llamada de prueba en vivo solo con `--yes`.  
`call` | Inicia una llamada de voz saliente.  
`start` | Alias de `call` con `--to` requerido y `--message` opcional.  
`continue` | Reproduce un mensaje y espera la siguiente respuesta.  
`speak` | Reproduce un mensaje sin esperar respuesta.  
`dtmf` | Envía dígitos DTMF a una llamada activa.  
`end` | Cuelga una llamada activa.  
`status` | Inspecciona las llamadas activas (o una por `--call-id`).  
`tail` | Sigue `calls.jsonl` (útil durante pruebas de proveedor).  
`latency` | Resume métricas de latencia de turno desde `calls.jsonl`.  
`expose` | Alterna Tailscale serve/funnel para el endpoint del Webhook.  
  
## Configuración y smoke

### `setup`

Imprime comprobaciones de preparación legibles para humanos de forma predeterminada. Pasa `--json` para scripts.

bashCopy code
[code]
    openclaw voicecall setupopenclaw voicecall setup --json
[/code]

### `smoke`

Ejecuta las mismas comprobaciones de preparación. No realizará una llamada telefónica real a menos que estén presentes tanto `--to` como `--yes`.

Indicador | Predeterminado | Descripción  
---|---|---  
`-t, --to <phone>` | (ninguno) | Número de teléfono al que llamar para un smoke en vivo.  
`--message <text>` | `OpenClaw voice call smoke test.` | Mensaje que se reproducirá durante la llamada smoke.  
`--mode <mode>` | `notify` | Modo de llamada: `notify` o `conversation`.  
`--yes` | `false` | Realiza realmente la llamada saliente en vivo.  
`--json` | `false` | Imprime JSON legible por máquinas.  
bashCopy code
[code]
    openclaw voicecall smokeopenclaw voicecall smoke --to "+15555550123"        # dry runopenclaw voicecall smoke --to "+15555550123" --yes  # live notify call
[/code]

## Ciclo de vida de la llamada

### `call`

Inicia una llamada de voz saliente.

Indicador | Requerido | Predeterminado | Descripción  
---|---|---|---  
`-m, --message <text>` | sí | (ninguno) | Mensaje que se reproducirá cuando la llamada se conecte.  
`-t, --to <phone>` | no | config `toNumber` | Número de teléfono E.164 al que llamar.  
`--mode <mode>` | no | `conversation` | Modo de llamada: `notify` (colgar después del mensaje) o `conversation` (mantener abierta).  
bashCopy code
[code]
    openclaw voicecall call --to "+15555550123" --message "Hello"openclaw voicecall call -m "Heads up" --mode notify
[/code]

### `start`

Alias de `call` con una forma de indicadores predeterminada diferente.

Indicador | Requerido | Predeterminado | Descripción  
---|---|---|---  
`--to <phone>` | sí | (ninguno) | Número de teléfono al que llamar.  
`--message <text>` | no | (ninguno) | Mensaje que se reproducirá cuando la llamada se conecte.  
`--mode <mode>` | no | `conversation` | Modo de llamada: `notify` o `conversation`.  
  
### `continue`

Reproduce un mensaje y espera una respuesta.

Indicador | Requerido | Descripción  
---|---|---  
`--call-id <id>` | sí | ID de llamada.  
`--message <text>` | sí | Mensaje que reproducir.  
  
### `speak`

Reproduce un mensaje sin esperar respuesta.

Indicador | Requerido | Descripción  
---|---|---  
`--call-id <id>` | sí | ID de llamada.  
`--message <text>` | sí | Mensaje que reproducir.  
  
### `dtmf`

Envía dígitos DTMF a una llamada activa.

Indicador | Requerido | Descripción  
---|---|---  
`--call-id <id>` | sí | ID de llamada.  
`--digits <digits>` | sí | Dígitos DTMF (p. ej., `ww123456#` para esperas).  
  
### `end`

Cuelga una llamada activa.

Indicador | Requerido | Descripción  
---|---|---  
`--call-id <id>` | sí | ID de llamada.  
  
### `status`

Inspecciona las llamadas activas.

Indicador | Predeterminado | Descripción  
---|---|---  
`--call-id <id>` | (ninguno) | Restringe la salida a una llamada.  
`--json` | `false` | Imprime JSON legible por máquinas.  
bashCopy code
[code]
    openclaw voicecall statusopenclaw voicecall status --jsonopenclaw voicecall status --call-id <id>
[/code]

## Registros y métricas

### `tail`

Sigue el registro JSONL de llamadas de voz. Imprime las últimas `--since` líneas al iniciar y luego transmite las líneas nuevas a medida que se escriben.

Indicador | Predeterminado | Descripción  
---|---|---  
`--file <path>` | resuelto desde el almacén del plugin | Ruta a `calls.jsonl`.  
`--since <n>` | `25` | Líneas que imprimir antes de seguir.  
`--poll <ms>` | `250` (mínimo 50) | Intervalo de sondeo en milisegundos.  
  
### `latency`

Resume las métricas de latencia de turno y espera de escucha desde `calls.jsonl`. La salida es JSON con resúmenes de `recordsScanned`, `turnLatency` y `listenWait`.

Indicador | Predeterminado | Descripción  
---|---|---  
`--file <path>` | resuelto desde el almacén del plugin | Ruta a `calls.jsonl`.  
`--last <n>` | `200` (mínimo 1) | Número de registros recientes que analizar.  
  
## Exposición de Webhooks

### `expose`

Habilita, deshabilita o cambia la configuración de Tailscale serve/funnel para el Webhook de voz.

Indicador | Predeterminado | Descripción  
---|---|---  
`--mode <mode>` | `funnel` | `off`, `serve` (tailnet) o `funnel` (público).  
`--path <path>` | config `tailscale.path` o `--serve-path` | Ruta de Tailscale que exponer.  
`--port <port>` | config `serve.port` o `3334` | Puerto local del Webhook.  
`--serve-path <path>` | config `serve.path` o `/voice/webhook` | Ruta local del Webhook.  
bashCopy code
[code]
    openclaw voicecall expose --mode serveopenclaw voicecall expose --mode funnelopenclaw voicecall expose --mode off
[/code]

## Relacionado

  * [Referencia de CLI](</es/cli>)
  * [Plugin de llamadas de voz](</es/plugins/voice-call>)


Was this useful?YesNo