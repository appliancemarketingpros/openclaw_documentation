---
title: Fecha y hora
source_url: https://docs.openclaw.ai/es/date-time
scraped_at: 2026-05-25
---

OpenClaw usa de forma predeterminada **la hora local del host para las marcas de tiempo de transporte** y **la zona horaria del usuario solo en el prompt del sistema**. Las marcas de tiempo del proveedor se conservan para que las herramientas mantengan su semántica nativa (la hora actual está disponible mediante `session_status`).

## Envoltorios de mensajes (local de forma predeterminada)

Los mensajes entrantes se envuelven con una marca de tiempo (precisión de minutos):

CodeCopy code
[code]
    [Provider ... 2026-01-05 16:26 PST] message text
[/code]

Esta marca de tiempo del envoltorio es **local del host de forma predeterminada** , independientemente de la zona horaria del proveedor.

Puedes anular este comportamiento:

json5Copy code
[code]
    {  agents: {    defaults: {      envelopeTimezone: "local", // "utc" | "local" | "user" | IANA timezone      envelopeTimestamp: "on", // "on" | "off"      envelopeElapsed: "on", // "on" | "off"    },  },}
[/code]

  * `envelopeTimezone: "utc"` usa UTC.
  * `envelopeTimezone: "local"` usa la zona horaria del host.
  * `envelopeTimezone: "user"` usa `agents.defaults.userTimezone` (recurre a la zona horaria del host).
  * Usa una zona horaria IANA explícita (por ejemplo, `"America/Chicago"`) para una zona fija.
  * `envelopeTimestamp: "off"` elimina las marcas de tiempo absolutas de los encabezados del envoltorio.
  * `envelopeElapsed: "off"` elimina los sufijos de tiempo transcurrido (el estilo `+2m`).


### Ejemplos

**Local (predeterminado):**

CodeCopy code
[code]
    [WhatsApp +1555 2026-01-18 00:19 PST] hello
[/code]

**Zona horaria del usuario:**

CodeCopy code
[code]
    [WhatsApp +1555 2026-01-18 00:19 CST] hello
[/code]

**Tiempo transcurrido habilitado:**

CodeCopy code
[code]
    [WhatsApp +1555 +30s 2026-01-18T05:19Z] follow-up
[/code]

## Prompt del sistema: fecha y hora actuales

Si se conoce la zona horaria del usuario, el prompt del sistema incluye una sección dedicada **Fecha y hora actuales** con **solo la zona horaria** (sin formato de reloj/hora) para mantener estable el almacenamiento en caché del prompt:

CodeCopy code
[code]
    Time zone: America/Chicago
[/code]

Cuando el agente necesite la hora actual, usa la herramienta `session_status`; la tarjeta de estado incluye una línea de marca de tiempo.

## Líneas de eventos del sistema (locales de forma predeterminada)

Los eventos del sistema en cola insertados en el contexto del agente llevan como prefijo una marca de tiempo que usa la misma selección de zona horaria que los envoltorios de mensajes (predeterminado: local del host).

CodeCopy code
[code]
    System: [2026-01-12 12:19:17 PST] Model switched.
[/code]

### Configurar zona horaria del usuario + formato

json5Copy code
[code]
    {  agents: {    defaults: {      userTimezone: "America/Chicago",      timeFormat: "auto", // auto | 12 | 24    },  },}
[/code]

  * `userTimezone` establece la **zona horaria local del usuario** para el contexto del prompt.
  * `timeFormat` controla la **visualización de 12 h/24 h** en el prompt. `auto` sigue las preferencias del sistema operativo.


## Detección del formato de hora (auto)

Cuando `timeFormat: "auto"`, OpenClaw inspecciona la preferencia del sistema operativo (macOS/Windows) y recurre al formato regional. El valor detectado se **almacena en caché por proceso** para evitar llamadas repetidas al sistema.

## Cargas útiles de herramientas + conectores (hora del proveedor sin procesar + campos normalizados)

Las herramientas de canal devuelven **marcas de tiempo nativas del proveedor** y agregan campos normalizados para mantener la coherencia:

  * `timestampMs`: milisegundos desde la época (UTC)
  * `timestampUtc`: cadena ISO 8601 UTC


Los campos sin procesar del proveedor se conservan para que no se pierda nada.

  * Slack: cadenas similares a época provenientes de la API
  * Discord: marcas de tiempo ISO UTC
  * Telegram/WhatsApp: marcas de tiempo numéricas/ISO específicas del proveedor


Si necesitas la hora local, conviértela más adelante usando la zona horaria conocida.

## Documentos relacionados

  * [Prompt del sistema](</es/concepts/system-prompt>)
  * [Zonas horarias](</es/concepts/timezone>)
  * [Mensajes](</es/concepts/messages>)


Was this useful?YesNo