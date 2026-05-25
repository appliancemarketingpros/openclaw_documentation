---
title: Envío del agente
source_url: https://docs.openclaw.ai/es/tools/agent-send
scraped_at: 2026-05-25
---

`openclaw agent` ejecuta un solo turno de agente desde la línea de comandos sin necesitar un mensaje de chat entrante. Úsalo para flujos de trabajo con scripts, pruebas y entrega programática.

## Inicio rápido

* ### Ejecutar un turno de agente simple

bashCopy code
[code]
    openclaw agent --message "What is the weather today?"
[/code]

Esto envía el mensaje a través del Gateway e imprime la respuesta.

* ### Dirigir a un agente o una sesión específicos

bashCopy code
[code]
    # Target a specific agentopenclaw agent --agent ops --message "Summarize logs" # Target a phone number (derives session key)openclaw agent --to +15555550123 --message "Status update" # Reuse an existing sessionopenclaw agent --session-id abc123 --message "Continue the task"
[/code]

* ### Entregar la respuesta a un canal

bashCopy code
[code]
    # Deliver to WhatsApp (default channel)openclaw agent --to +15555550123 --message "Report ready" --deliver # Deliver to Slackopenclaw agent --agent ops --message "Generate report" \  --deliver --reply-channel slack --reply-to "#reports"
[/code]

## Indicadores

Indicador | Descripción  
---|---  
`--message \<text\>` | Mensaje para enviar (obligatorio)  
`--to \<dest\>` | Deriva la clave de sesión de un destino (teléfono, id de chat)  
`--agent \<id\>` | Dirige a un agente configurado (usa su sesión `main`)  
`--session-id \<id\>` | Reutiliza una sesión existente por id  
`--local` | Fuerza el runtime embebido local (omite el Gateway)  
`--deliver` | Envía la respuesta a un canal de chat  
`--channel \<name\>` | Canal de entrega (whatsapp, telegram, discord, slack, etc.)  
`--reply-to \<target\>` | Anulación del destino de entrega  
`--reply-channel \<name\>` | Anulación del canal de entrega  
`--reply-account \<id\>` | Anulación del id de cuenta de entrega  
`--thinking \<level\>` | Establece el nivel de pensamiento para el perfil de modelo seleccionado  
`--verbose \<on|full|off\>` | Establece el nivel de detalle  
`--timeout \<seconds\>` | Anula el tiempo de espera del agente  
`--json` | Emite JSON estructurado  
  
## Comportamiento

  * De forma predeterminada, la CLI pasa **por el Gateway**. Añade `--local` para forzar el runtime embebido en la máquina actual.
  * Si no se puede acceder al Gateway, la CLI **recurre** a la ejecución embebida local.
  * Selección de sesión: `--to` deriva la clave de sesión (los destinos de grupo/canal conservan el aislamiento; los chats directos se reducen a `main`).
  * Los indicadores de pensamiento y detalle persisten en el almacén de sesiones.
  * Salida: texto sin formato de forma predeterminada, o `--json` para carga útil estructurada + metadatos.
  * Con `--json --deliver`, el JSON incluye el estado de entrega para envíos enviados, suprimidos, parciales y fallidos. Consulta [estado de entrega JSON](</es/cli/agent#json-delivery-status>).


## Ejemplos

bashCopy code
[code]
    # Simple turn with JSON outputopenclaw agent --to +15555550123 --message "Trace logs" --verbose on --json # Turn with thinking levelopenclaw agent --session-id 1234 --message "Summarize inbox" --thinking medium # Deliver to a different channel than the sessionopenclaw agent --agent ops --message "Alert" --deliver --reply-channel telegram --reply-to "@admin"
[/code]

## Relacionado

[**Referencia de CLI del agente** Referencia completa de indicadores y opciones de `openclaw agent`. ](</es/cli/agent>) [**Subagentes** Generación de subagentes en segundo plano. ](</es/tools/subagents>) [**Sesiones** Cómo funcionan las claves de sesión y cómo `--to`, `--agent` y `--session-id` las resuelven. ](</es/concepts/session>) [**Comandos de barra** Catálogo de comandos nativos usados dentro de las sesiones de agente. ](</es/tools/slash-commands>)

Was this useful?YesNo