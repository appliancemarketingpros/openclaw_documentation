---
title: Flujos (redirección)
source_url: https://docs.openclaw.ai/es/cli/flows
scraped_at: 2026-05-25
---

# `openclaw tasks flow`

No hay un comando de nivel superior `openclaw flows`. La inspección persistente de TaskFlow está en `openclaw tasks flow`.

## Subcomandos

bashCopy code
[code]
    openclaw tasks flow list   [--json] [--status <name>]openclaw tasks flow show   <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Subcomando | Descripción | Argumentos / opciones  
---|---|---  
`list` | Lista TaskFlows rastreados. | salida legible por máquina `--json`; filtro `--status <name>` (consulta los valores de estado a continuación).  
`show` | Muestra un TaskFlow. | id de flujo `<lookup>` o clave del propietario; salida legible por máquina `--json`.  
`cancel` | Cancela un TaskFlow en ejecución. | id de flujo `<lookup>` o clave del propietario.  
  
`<lookup>` acepta un id de flujo (devuelto por `list` / `show`) o la clave del propietario del flujo (el identificador estable que usa el subsistema propietario para rastrear el flujo).

### Valores del filtro de estado

`--status` en `list` acepta uno de:

`queued`, `running`, `waiting`, `blocked`, `succeeded`, `failed`, `cancelled`, `lost`

## Ejemplos

bashCopy code
[code]
    openclaw tasks flow listopenclaw tasks flow list --status runningopenclaw tasks flow list --jsonopenclaw tasks flow show flow_abc123openclaw tasks flow show flow_abc123 --jsonopenclaw tasks flow cancel flow_abc123
[/code]

Para ver los conceptos completos de TaskFlow y la creación, consulta [TaskFlow](</es/automation/taskflow>). Para el comando principal `tasks`, consulta la [referencia de CLI de tasks](</es/cli/tasks>).

## Relacionado

  * [Referencia de CLI](</es/cli>)
  * [Automatización](</es/automation>)
  * [TaskFlow](</es/automation/taskflow>)


Was this useful?YesNo