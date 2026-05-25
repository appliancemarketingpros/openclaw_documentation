---
title: Nodos
source_url: https://docs.openclaw.ai/es/cli/nodes
scraped_at: 2026-05-25
---

# `openclaw nodes`

Gestiona nodos (dispositivos) emparejados e invoca capacidades de nodos.

Relacionado:

  * Resumen de nodos: [Nodos](</es/nodes>)
  * Cámara: [Nodos de cámara](</es/nodes/camera>)
  * Imágenes: [Nodos de imagen](</es/nodes/images>)


Opciones comunes:

  * `--url`, `--token`, `--timeout`, `--json`


## Comandos comunes

bashCopy code
[code]
    openclaw nodes listopenclaw nodes list --connectedopenclaw nodes list --last-connected 24hopenclaw nodes pendingopenclaw nodes approve <requestId>openclaw nodes reject <requestId>openclaw nodes remove --node <id|name|ip>openclaw nodes rename --node <id|name|ip> --name <displayName>openclaw nodes statusopenclaw nodes status --connectedopenclaw nodes status --last-connected 24h
[/code]

`nodes list` imprime tablas de solicitudes pendientes y nodos emparejados. Las filas emparejadas incluyen la antigüedad de la conexión más reciente (Última conexión). Usa `--connected` para mostrar solo los nodos conectados actualmente. Usa `--last-connected <duration>` para filtrar a los nodos que se conectaron dentro de una duración (por ejemplo, `24h`, `7d`). Usa `nodes remove --node <id|name|ip>` para eliminar un registro obsoleto de emparejamiento de nodo propiedad del Gateway.

Nota de aprobación:

  * `openclaw nodes pending` solo necesita el ámbito de emparejamiento.
  * `gateway.nodes.pairing.autoApproveCidrs` puede omitir el paso pendiente solo para el emparejamiento de dispositivos `role: node` explícitamente confiables y por primera vez. Está desactivado de forma predeterminada y no aprueba actualizaciones.
  * `openclaw nodes approve <requestId>` hereda requisitos de ámbito adicionales de la solicitud pendiente: 
    * solicitud sin comando: solo emparejamiento
    * comandos de nodo no exec: emparejamiento + escritura
    * `system.run` / `system.run.prepare` / `system.which`: emparejamiento + administrador


## Invocar

bashCopy code
[code]
    openclaw nodes invoke --node <id|name|ip> --command <command> --params <json>
[/code]

Banderas de invocación:

  * `--params <json>`: cadena de objeto JSON (predeterminado `{}`).
  * `--invoke-timeout <ms>`: tiempo de espera de invocación del nodo (predeterminado `15000`).
  * `--idempotency-key <key>`: clave de idempotencia opcional.
  * `system.run` y `system.run.prepare` están bloqueados aquí; usa la herramienta `exec` con `host=node` para la ejecución de shell.


Para la ejecución de shell en un nodo, usa la herramienta `exec` con `host=node` en lugar de `openclaw nodes run`. La CLI `nodes` ahora se centra en capacidades: RPC directo mediante `nodes invoke`, además de emparejamiento, cámara, pantalla, ubicación, Canvas y notificaciones. Los comandos de Canvas se implementan mediante el Plugin experimental de Canvas incluido; el núcleo conserva un enlace de compatibilidad para que sigan estando bajo `openclaw nodes canvas`.

## Relacionado

  * [Referencia de CLI](</es/cli>)
  * [Nodos](</es/nodes>)


Was this useful?YesNo