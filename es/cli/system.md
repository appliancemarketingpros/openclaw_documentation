---
title: Sistema
source_url: https://docs.openclaw.ai/es/cli/system
scraped_at: 2026-05-25
---

# `openclaw system`

Ayudantes a nivel de sistema para el Gateway: poner en cola eventos del sistema, controlar Heartbeat y ver la presencia.

Todos los subcomandos de `system` usan RPC del Gateway y aceptan las opciones compartidas del cliente:

  * `--url <url>`
  * `--token <token>`
  * `--timeout <ms>`
  * `--expect-final`


## Comandos comunes

bashCopy code
[code]
    openclaw system event --text "Check for urgent follow-ups" --mode nowopenclaw system event --text "Check for urgent follow-ups" --url ws://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"openclaw system heartbeat enableopenclaw system heartbeat lastopenclaw system presence
[/code]

## `system event`

Pone en cola un evento del sistema en la sesión **principal** de forma predeterminada. El siguiente Heartbeat lo inyectará como una línea `System:` en el prompt. Usa `--mode now` para activar el Heartbeat de inmediato; `next-heartbeat` espera el siguiente pulso programado.

Pasa `--session-key` para apuntar a una sesión específica (por ejemplo, para retransmitir la finalización de una tarea asíncrona al canal que la inició).

> **Excepción de temporización con`--session-key`:** cuando se proporciona `--session-key`, `--mode next-heartbeat` se reduce a una activación dirigida inmediata en lugar de esperar el siguiente pulso programado. Las activaciones dirigidas usan la intención de Heartbeat `immediate`, por lo que omiten la compuerta de no vencido del ejecutor, que de otro modo aplazaría (y, en la práctica, descartaría) una activación con intención `event`. Si quieres una entrega diferida, omite `--session-key` para que el evento llegue a la sesión principal y viaje con el siguiente Heartbeat regular.

Opciones:

  * `--text <text>`: texto obligatorio del evento del sistema.
  * `--mode <mode>`: `now` o `next-heartbeat` (predeterminado).
  * `--session-key <sessionKey>`: opcional; apunta a una sesión de agente específica en lugar de la sesión principal del agente. Las claves que no pertenecen al agente resuelto vuelven a la sesión principal del agente.
  * `--json`: salida legible por máquina.
  * `--url`, `--token`, `--timeout`, `--expect-final`: opciones RPC compartidas del Gateway.


## `system heartbeat last|enable|disable`

Controles de Heartbeat:

  * `last`: muestra el último evento de Heartbeat.
  * `enable`: vuelve a activar Heartbeat (usa esto si estaba desactivado).
  * `disable`: pausa Heartbeat.


Opciones:

  * `--json`: salida legible por máquina.
  * `--url`, `--token`, `--timeout`, `--expect-final`: opciones RPC compartidas del Gateway.


## `system presence`

Lista las entradas actuales de presencia del sistema que conoce el Gateway (nodos, instancias y líneas de estado similares).

Opciones:

  * `--json`: salida legible por máquina.
  * `--url`, `--token`, `--timeout`, `--expect-final`: opciones RPC compartidas del Gateway.


## Notas

  * Requiere un Gateway en ejecución accesible desde tu configuración actual (local o remota).
  * Los eventos del sistema son efímeros y no se conservan entre reinicios.


## Relacionado

  * [Referencia de CLI](</es/cli>)


Was this useful?YesNo