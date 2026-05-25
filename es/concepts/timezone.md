---
title: Zonas horarias
source_url: https://docs.openclaw.ai/es/concepts/timezone
scraped_at: 2026-05-25
---

OpenClaw estandariza las marcas de tiempo para que el modelo vea una **única hora de referencia** en lugar de una mezcla de relojes locales del proveedor. Hay tres superficies donde aparecen las zonas horarias, cada una con su propio propósito:

## Tres superficies de zona horaria

Superficie | Qué muestra | Predeterminado | Configurado mediante  
---|---|---|---  
Envoltorios de mensajes | Envuelven los mensajes entrantes del canal: `[Signal +1555 2026-01-18 00:19 PST] hello` | Local del host | `agents.defaults.envelopeTimezone`  
Cargas útiles de herramientas | Las herramientas de estilo `readMessages` del canal devuelven la hora sin procesar del proveedor + `timestampMs` / `timestampUtc` normalizados | Los campos UTC siempre están presentes | No configurable — conserva las marcas de tiempo nativas del proveedor  
Prompt del sistema | Un pequeño bloque `Current Date & Time` con **solo la zona horaria** (sin valor de reloj, para estabilidad de caché) | Zona horaria del host si `userTimezone` no está definido | `agents.defaults.userTimezone`  
  
El prompt del sistema omite deliberadamente el reloj en vivo para mantener estable el almacenamiento en caché del prompt entre turnos. Cuando el agente necesita la hora actual, llama a `session_status`.

## Configurar la zona horaria del usuario

json5Copy code
[code]
    {  agents: {    defaults: {      userTimezone: "America/Chicago",    },  },}
[/code]

Si `userTimezone` no está definido, OpenClaw resuelve la zona horaria del host en tiempo de ejecución (sin escribir configuración). `agents.defaults.timeFormat` (`auto` | `12` | `24`) controla la representación en formato de 12 h/24 h en envoltorios y superficies posteriores, no en la sección del prompt del sistema.

## Cuándo sobrescribir

  * **Usa envoltorios UTC** (`envelopeTimezone: "utc"`) cuando quieras marcas de tiempo estables entre hosts de distintas regiones, o cuando quieras que los registros alineados con UTC coincidan con la salida de diagnóstico.
  * **Usa una zona IANA fija** (por ejemplo, `"Europe/Vienna"`) cuando el host del Gateway esté en una zona pero el usuario esté en otra y quieras que los envoltorios se lean en la zona del usuario independientemente de la migración del host.
  * **Configura`envelopeTimestamp: "off"`** para envoltorios de bajo consumo de tokens cuando el contexto de marca de tiempo no sea útil para la conversación.


Para ver la referencia completa del comportamiento, ejemplos por proveedor y formato de tiempo transcurrido, consulta [Fecha y hora](</es/date-time>).

## Relacionado

  * [Fecha y hora](</es/date-time>) — comportamiento y ejemplos completos de envoltorios/herramientas/prompts.
  * [Heartbeat](</es/gateway/heartbeat>) — las horas activas usan la zona horaria para la programación.
  * [Trabajos Cron](</es/automation/cron-jobs>) — las expresiones Cron usan la zona horaria para la programación.


Was this useful?YesNo