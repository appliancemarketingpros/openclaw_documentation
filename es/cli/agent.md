---
title: Agente
source_url: https://docs.openclaw.ai/es/cli/agent
scraped_at: 2026-05-25
---

# `openclaw agent`

Ejecuta un turno de agente mediante el Gateway (usa `--local` para integrado). Usa `--agent <id>` para apuntar directamente a un agente configurado.

Pasa al menos un selector de sesión:

  * `--to <dest>`
  * `--session-id <id>`
  * `--agent <id>`


Relacionado:

  * Herramienta de envío de agente: [Envío de agente](</es/tools/agent-send>)


## Opciones

  * `-m, --message <text>`: cuerpo del mensaje obligatorio
  * `-t, --to <dest>`: destinatario usado para derivar la clave de sesión
  * `--session-id <id>`: id de sesión explícito
  * `--agent <id>`: id de agente; anula los enlaces de enrutamiento
  * `--model <id>`: anulación de modelo para esta ejecución (`provider/model` o id de modelo)
  * `--thinking <level>`: nivel de razonamiento del agente (`off`, `minimal`, `low`, `medium`, `high`, además de niveles personalizados admitidos por el proveedor, como `xhigh`, `adaptive` o `max`)
  * `--verbose <on|off>`: persiste el nivel detallado para la sesión
  * `--channel <channel>`: canal de entrega; omítelo para usar el canal principal de la sesión
  * `--reply-to <target>`: anulación del destino de entrega
  * `--reply-channel <channel>`: anulación del canal de entrega
  * `--reply-account <id>`: anulación de la cuenta de entrega
  * `--local`: ejecuta directamente el agente integrado (después de la precarga del registro de Plugin)
  * `--deliver`: envía la respuesta de vuelta al canal/destino seleccionado
  * `--timeout <seconds>`: anula el tiempo de espera del agente (predeterminado 600 o valor de configuración)
  * `--json`: genera JSON


## Ejemplos

bashCopy code
[code]
    openclaw agent --to +15555550123 --message "status update" --deliveropenclaw agent --agent ops --message "Summarize logs"openclaw agent --agent ops --model openai/gpt-5.4 --message "Summarize logs"openclaw agent --session-id 1234 --message "Summarize inbox" --thinking mediumopenclaw agent --to +15555550123 --message "Trace logs" --verbose on --jsonopenclaw agent --agent ops --message "Generate report" --deliver --reply-channel slack --reply-to "#reports"openclaw agent --agent ops --message "Run locally" --local
[/code]

## Notas

  * El modo Gateway recurre al agente integrado cuando falla la solicitud al Gateway. Usa `--local` para forzar la ejecución integrada desde el principio.
  * `--local` todavía precarga primero el registro de Plugin, por lo que los proveedores, herramientas y canales proporcionados por Plugins permanecen disponibles durante las ejecuciones integradas.
  * `--local` y las ejecuciones de respaldo integradas se tratan como ejecuciones de una sola vez. Los recursos de loopback MCP empaquetados y las sesiones stdio Claude preparadas abiertas para ese proceso local se retiran después de la respuesta, por lo que las invocaciones con scripts no mantienen vivos los procesos secundarios locales.
  * Las ejecuciones respaldadas por Gateway dejan los recursos de loopback MCP propiedad del Gateway bajo el proceso Gateway en ejecución; los clientes más antiguos aún pueden enviar la marca histórica de limpieza, pero el Gateway la acepta como una operación sin efecto por compatibilidad.
  * `--channel`, `--reply-channel` y `--reply-account` afectan la entrega de respuestas, no el enrutamiento de sesiones.
  * `--json` mantiene stdout reservado para la respuesta JSON. Los diagnósticos de Gateway, Plugin y respaldo integrado se enrutan a stderr para que los scripts puedan analizar stdout directamente.
  * El JSON de respaldo integrado incluye `meta.transport: "embedded"` y `meta.fallbackFrom: "gateway"` para que los scripts puedan distinguir las ejecuciones de respaldo de las ejecuciones de Gateway.
  * Si el Gateway acepta una ejecución de agente pero la CLI agota el tiempo de espera al esperar la respuesta final, el respaldo integrado usa un id explícito nuevo de sesión/ejecución `gateway-fallback-*` e informa `meta.fallbackReason: "gateway_timeout"` más los campos de la sesión de respaldo. Esto evita competir con el bloqueo de transcripción propiedad del Gateway o reemplazar silenciosamente la sesión de conversación enrutada original.
  * Cuando este comando activa la regeneración de `models.json`, las credenciales de proveedor gestionadas por SecretRef se persisten como marcadores no secretos (por ejemplo, nombres de variables de entorno, `secretref-env:ENV_VAR_NAME` o `secretref-managed`), no como texto sin formato de secretos resueltos.
  * Las escrituras de marcadores son autoritativas según la fuente: OpenClaw persiste marcadores desde la instantánea de configuración de fuente activa, no desde valores secretos resueltos en tiempo de ejecución.


## Estado de entrega JSON

Cuando se usa `--json --deliver`, la respuesta JSON de la CLI puede incluir `deliveryStatus` de nivel superior para que los scripts puedan distinguir envíos entregados, suprimidos, parciales y fallidos:

jsonCopy code
[code]
    {  "payloads": [{ "text": "Report ready", "mediaUrl": null }],  "meta": { "durationMs": 1200 },  "deliveryStatus": {    "requested": true,    "attempted": true,    "status": "sent",    "succeeded": true,    "resultCount": 1  }}
[/code]

`deliveryStatus.status` es uno de `sent`, `suppressed`, `partial_failed` o `failed`. `suppressed` significa que la entrega no se envió intencionalmente, por ejemplo porque un hook de envío de mensajes la canceló o no hubo ningún resultado visible; sigue siendo un resultado terminal sin reintentos. `partial_failed` significa que al menos una carga útil se envió antes de que fallara una carga útil posterior. `failed` significa que no se completó ningún envío duradero o que falló la comprobación previa de entrega.

Las respuestas de CLI respaldadas por Gateway también preservan la forma sin procesar del resultado de Gateway, donde el mismo objeto está disponible en `result.deliveryStatus`.

Campos comunes:

  * `requested`: siempre `true` cuando el objeto está presente.
  * `attempted`: `true` después de que se ejecutó la ruta de envío duradero; `false` para fallos de comprobación previa o si no hay cargas útiles visibles.
  * `succeeded`: `true`, `false` o `"partial"`; `"partial"` se combina con `status: "partial_failed"`.
  * `reason`: un motivo en snake-case en minúsculas procedente de la entrega duradera o de la validación de comprobación previa. Los motivos conocidos incluyen `cancelled_by_message_sending_hook`, `no_visible_payload`, `no_visible_result`, `channel_resolved_to_internal`, `unknown_channel`, `invalid_delivery_target` y `no_delivery_target`; los envíos duraderos fallidos también pueden informar la etapa fallida. Trata los valores desconocidos como opacos porque el conjunto puede ampliarse.
  * `resultCount`: número de resultados de envío del canal cuando está disponible.
  * `sentBeforeError`: `true` cuando un fallo parcial envió al menos una carga útil antes del error.
  * `error`: booleano `true` para envíos fallidos o parcialmente fallidos.
  * `errorMessage`: se incluye solo cuando se captura un mensaje de error de entrega subyacente. Los fallos de comprobación previa llevan `error` y `reason`, pero no `errorMessage`.
  * `payloadOutcomes`: resultados opcionales por carga útil con `index`, `status`, `reason`, `resultCount`, `error`, `stage`, `sentBeforeError` o metadatos del hook cuando están disponibles.


## Relacionado

  * [Referencia de CLI](</es/cli>)
  * [Tiempo de ejecución de agente](</es/concepts/agent>)


Was this useful?YesNo