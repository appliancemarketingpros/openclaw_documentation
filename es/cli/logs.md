---
title: Registros
source_url: https://docs.openclaw.ai/es/cli/logs
scraped_at: 2026-05-25
---

# `openclaw logs`

Sigue los registros de archivo del Gateway por RPC (funciona en modo remoto).

Relacionado:

  * Resumen de registro: [Registro](</es/logging>)
  * CLI de Gateway: [gateway](</es/cli/gateway>)


## Opciones

  * `--limit <n>`: número máximo de líneas de registro que se devolverán (predeterminado `200`)
  * `--max-bytes <n>`: bytes máximos que se leerán del archivo de registro (predeterminado `250000`)
  * `--follow`: seguir el flujo de registro
  * `--interval <ms>`: intervalo de sondeo mientras se sigue (predeterminado `1000`)
  * `--json`: emitir eventos JSON delimitados por líneas
  * `--plain`: salida de texto sin formato sin formato con estilo
  * `--no-color`: desactivar los colores ANSI
  * `--local-time`: representar las marcas de tiempo en tu zona horaria local


## Opciones RPC compartidas de Gateway

`openclaw logs` también acepta las opciones estándar del cliente Gateway:

  * `--url <url>`: URL WebSocket de Gateway
  * `--token <token>`: token de Gateway
  * `--timeout <ms>`: tiempo de espera en ms (predeterminado `30000`)
  * `--expect-final`: esperar una respuesta final cuando la llamada de Gateway esté respaldada por un agente


Cuando pasas `--url`, la CLI no aplica automáticamente la configuración ni las credenciales del entorno. Incluye `--token` explícitamente si el Gateway de destino requiere autenticación.

## Ejemplos

bashCopy code
[code]
    openclaw logsopenclaw logs --followopenclaw logs --follow --interval 2000openclaw logs --limit 500 --max-bytes 500000openclaw logs --jsonopenclaw logs --plainopenclaw logs --no-coloropenclaw logs --limit 500openclaw logs --local-timeopenclaw logs --follow --local-timeopenclaw logs --url ws://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"
[/code]

## Notas

  * Usa `--local-time` para representar las marcas de tiempo en tu zona horaria local.
  * Si el Gateway local loopback implícito solicita emparejamiento, se cierra durante la conexión o agota el tiempo de espera antes de que `logs.tail` responda, `openclaw logs` recurre automáticamente al archivo de registro de Gateway configurado. Los destinos `--url` explícitos no usan esta alternativa.
  * Al usar `--follow`, las desconexiones transitorias del Gateway (cierre de WebSocket, tiempo de espera, caída de conexión) activan la reconexión automática con retroceso exponencial (hasta 8 reintentos, con un límite de 30 s entre intentos). Se imprime una advertencia en stderr en cada reintento, y se imprime un aviso `[logs] gateway reconnected` cuando un sondeo se realiza correctamente. En modo `--json`, tanto la advertencia de reintento como la transición de reconexión se emiten como registros `{"type":"notice"}` en stderr. Los errores no recuperables (fallo de autenticación, configuración incorrecta) siguen saliendo inmediatamente.


## Relacionado

  * [Referencia de la CLI](</es/cli>)
  * [Registro de Gateway](</es/gateway/logging>)


Was this useful?YesNo