---
title: `openclaw commitments`
source_url: https://docs.openclaw.ai/es/cli/commitments
scraped_at: 2026-05-25
---

Enumera y gestiona compromisos de seguimiento inferidos.

Los compromisos son memorias de seguimiento opcionales y de corta duración creadas a partir del contexto de la conversación. Consulta [Compromisos inferidos](</es/concepts/commitments>) para ver la guía conceptual.

Sin subcomando, `openclaw commitments` enumera los compromisos pendientes.

## Uso

bashCopy code
[code]
    openclaw commitments [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments list [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments dismiss <id...> [--json]
[/code]

## Opciones

  * `--all`: muestra todos los estados en lugar de solo los compromisos pendientes.
  * `--agent <id>`: filtra por un id de agente.
  * `--status <status>`: filtra por estado. Valores: `pending`, `sent`, `dismissed`, `snoozed` o `expired`.
  * `--json`: genera JSON legible por máquina.


## Ejemplos

Enumera los compromisos pendientes:

bashCopy code
[code]
    openclaw commitments
[/code]

Enumera todos los compromisos almacenados:

bashCopy code
[code]
    openclaw commitments --all
[/code]

Filtra por un agente:

bashCopy code
[code]
    openclaw commitments --agent main
[/code]

Busca compromisos pospuestos:

bashCopy code
[code]
    openclaw commitments --status snoozed
[/code]

Descarta uno o más compromisos:

bashCopy code
[code]
    openclaw commitments dismiss cm_abc123 cm_def456
[/code]

Exporta como JSON:

bashCopy code
[code]
    openclaw commitments --all --json
[/code]

## Salida

La salida de texto incluye:

  * id del compromiso
  * estado
  * tipo
  * hora de vencimiento más temprana
  * alcance
  * texto sugerido para el seguimiento


La salida JSON también incluye la ruta del almacén de compromisos y los registros almacenados completos.

## Relacionado

  * [Compromisos inferidos](</es/concepts/commitments>)
  * [Resumen de la memoria](</es/concepts/memory>)
  * [Heartbeat](</es/gateway/heartbeat>)
  * [Tareas programadas](</es/automation/cron-jobs>)


Was this useful?YesNo