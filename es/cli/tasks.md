---
title: `openclaw tasks`
source_url: https://docs.openclaw.ai/es/cli/tasks
scraped_at: 2026-05-25
---

Inspecciona tareas en segundo plano duraderas y el estado de Task Flow. Sin subcomando, `openclaw tasks` equivale a `openclaw tasks list`.

Consulta [Tareas en segundo plano](</es/automation/tasks>) para ver el ciclo de vida y el modelo de entrega.

## Uso

bashCopy code
[code]
    openclaw tasksopenclaw tasks listopenclaw tasks list --runtime acpopenclaw tasks list --status runningopenclaw tasks show <lookup>openclaw tasks notify <lookup> state_changesopenclaw tasks cancel <lookup>openclaw tasks auditopenclaw tasks maintenanceopenclaw tasks maintenance --applyopenclaw tasks flow listopenclaw tasks flow show <lookup>openclaw tasks flow cancel <lookup>
[/code]

## Opciones Raíz

  * `--json`: genera JSON.
  * `--runtime <name>`: filtra por tipo: `subagent`, `acp`, `cron` o `cli`.
  * `--status <name>`: filtra por estado: `queued`, `running`, `succeeded`, `failed`, `timed_out`, `cancelled` o `lost`.


## Subcomandos

### `list`

bashCopy code
[code]
    openclaw tasks list [--runtime <name>] [--status <name>] [--json]
[/code]

Enumera las tareas en segundo plano rastreadas, de la más reciente a la más antigua.

### `show`

bashCopy code
[code]
    openclaw tasks show <lookup> [--json]
[/code]

Muestra una tarea por ID de tarea, ID de ejecución o clave de sesión.

### `notify`

bashCopy code
[code]
    openclaw tasks notify <lookup> <done_only|state_changes|silent>
[/code]

Cambia la política de notificaciones de una tarea en ejecución.

### `cancel`

bashCopy code
[code]
    openclaw tasks cancel <lookup>
[/code]

Cancela una tarea en segundo plano en ejecución.

### `audit`

bashCopy code
[code]
    openclaw tasks audit [--severity <warn|error>] [--code <name>] [--limit <n>] [--json]
[/code]

Expone registros de tareas y Task Flow obsoletos, perdidos, con entrega fallida o incoherentes de otro modo. Las tareas perdidas retenidas hasta `cleanupAfter` son advertencias; las tareas perdidas vencidas o sin marca de tiempo son errores.

### `maintenance`

bashCopy code
[code]
    openclaw tasks maintenance [--apply] [--json]
[/code]

Previsualiza o aplica la reconciliación de tareas y Task Flow, el marcado de limpieza, la poda y la limpieza del registro de sesiones de ejecuciones cron obsoletas. Para las tareas cron, la reconciliación usa registros de ejecución persistidos/estado del trabajo antes de marcar una tarea activa antigua como `lost`, por lo que las ejecuciones cron completadas no se convierten en falsos errores de auditoría solo porque el estado en memoria del runtime de Gateway ya no exista. La auditoría de CLI sin conexión no es autoritativa para el conjunto de trabajos cron activos local al proceso de Gateway. Las tareas de CLI con un ID de ejecución/ID de origen se marcan como `lost` cuando su contexto de ejecución vivo de Gateway desaparece, incluso si queda una fila antigua de sesión hija. Cuando se aplica, el mantenimiento también poda las filas del registro de sesiones `cron:<jobId>:run:<uuid>` con más de 7 días de antigüedad mientras conserva los trabajos cron actualmente en ejecución y deja intactas las filas de sesiones que no son cron.

### `flow`

bashCopy code
[code]
    openclaw tasks flow list [--status <name>] [--json]openclaw tasks flow show <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Inspecciona o cancela el estado duradero de Task Flow bajo el libro mayor de tareas.

## Relacionado

  * [Referencia de CLI](</es/cli>)
  * [Tareas en segundo plano](</es/automation/tasks>)


Was this useful?YesNo