---
title: Reglas de notificación de Matrix para previsualizaciones silenciosas
source_url: https://docs.openclaw.ai/es/channels/matrix-push-rules
scraped_at: 2026-05-25
---

Cuando `channels.matrix.streaming` es `"quiet"`, OpenClaw edita un único evento de vista previa en el mismo lugar y marca la edición finalizada con una bandera de contenido personalizada. Los clientes Matrix notifican solo en la edición final si una regla push por usuario coincide con esa bandera. Esta página es para operadores que autoalojan Matrix y quieren instalar esa regla para cada cuenta destinataria.

Si solo quieres el comportamiento de notificaciones estándar de Matrix, usa `streaming: "partial"` o deja el streaming desactivado. Consulta [Configuración del canal Matrix](</es/channels/matrix#streaming-previews>).

## Requisitos previos

  * usuario destinatario = la persona que debe recibir la notificación
  * usuario bot = la cuenta Matrix de OpenClaw que envía la respuesta
  * usa el token de acceso del usuario destinatario para las llamadas a la API siguientes
  * haz coincidir `sender` en la regla push con el MXID completo del usuario bot
  * la cuenta destinataria ya debe tener pushers funcionando: las reglas de vista previa silenciosa solo funcionan cuando la entrega push normal de Matrix está en buen estado


## Pasos

* ### Configurar vistas previas silenciosas

json5Copy code
[code]
    {channels: {matrix: {  streaming: "quiet",},},}
[/code]

* ### Obtener el token de acceso del destinatario

Reutiliza un token de sesión de cliente existente cuando sea posible. Para emitir uno nuevo:

bashCopy code
[code]
    curl -sS -X POST \"https://matrix.example.org/_matrix/client/v3/login" \-H "Content-Type: application/json" \--data '{"type": "m.login.password","identifier": { "type": "m.id.user", "user": "@alice:example.org" },"password": "REDACTED"}'
[/code]

* ### Verificar que existan pushers

bashCopy code
[code]
    curl -sS \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \"https://matrix.example.org/_matrix/client/v3/pushers"
[/code]

Si no se devuelve ningún pusher, corrige la entrega push normal de Matrix para esta cuenta antes de continuar.

* ### Instalar la regla push de sobrescritura

OpenClaw marca las ediciones de vista previa finalizadas solo de texto con `content["com.openclaw.finalized_preview"] = true`. Instala una regla que coincida con ese marcador y con el MXID del bot como remitente:

bashCopy code
[code]
    curl -sS -X PUT \"https://matrix.example.org/_matrix/client/v3/pushrules/global/override/openclaw-finalized-preview-botname" \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \-H "Content-Type: application/json" \--data '{"conditions": [  { "kind": "event_match", "key": "type", "pattern": "m.room.message" },  {    "kind": "event_property_is",    "key": "content.m\\.relates_to.rel_type",    "value": "m.replace"  },  {    "kind": "event_property_is",    "key": "content.com\\.openclaw\\.finalized_preview",    "value": true  },  { "kind": "event_match", "key": "sender", "pattern": "@bot:example.org" }],"actions": [  "notify",  { "set_tweak": "sound", "value": "default" },  { "set_tweak": "highlight", "value": false }]}'
[/code]

Sustituye antes de ejecutar:

  * `https://matrix.example.org`: la URL base de tu homeserver
  * `$USER_ACCESS_TOKEN`: el token de acceso del usuario destinatario
  * `openclaw-finalized-preview-botname`: un ID de regla único por bot y por destinatario (patrón: `openclaw-finalized-preview-<botname>`)
  * `@bot:example.org`: el MXID de tu bot de OpenClaw, no el del destinatario


* ### Verificar

bashCopy code
[code]
    curl -sS \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \"https://matrix.example.org/_matrix/client/v3/pushrules/global/override/openclaw-finalized-preview-botname"
[/code]

Luego prueba una respuesta emitida por streaming. En modo silencioso, la sala muestra una vista previa de borrador silenciosa y notifica una vez que termina el bloque o el turno.

Para quitar la regla más adelante, haz `DELETE` en la misma URL de regla con el token del destinatario.

## Notas para varios bots

Las reglas push se indexan por `ruleId`: volver a ejecutar `PUT` contra el mismo ID actualiza una sola regla. Para varios bots de OpenClaw que notifican al mismo destinatario, crea una regla por bot con una coincidencia de remitente distinta.

Las nuevas reglas `override` definidas por el usuario se insertan antes de las reglas de supresión predeterminadas, así que no se necesita ningún parámetro de orden adicional. La regla solo afecta a las ediciones de vista previa solo de texto que pueden finalizarse en el mismo lugar; los respaldos de medios y los respaldos de vista previa obsoleta usan la entrega normal de Matrix.

## Notas del homeserver

Synapse

No se requiere ningún cambio especial en `homeserver.yaml`. Si las notificaciones normales de Matrix ya llegan a este usuario, el token del destinatario y la llamada a `pushrules` anterior son el paso principal de configuración.

Si ejecutas Synapse detrás de un proxy inverso o workers, asegúrate de que `/_matrix/client/.../pushrules/` llegue correctamente a Synapse. La entrega push la gestiona el proceso principal o `synapse.app.pusher` / los workers de pusher configurados; asegúrate de que estén en buen estado.

La regla usa la condición de regla push `event_property_is` (MSC3758, regla push v1.10), que se agregó a Synapse en 2023. Las versiones anteriores de Synapse aceptan la llamada `PUT pushrules/...`, pero silenciosamente nunca coinciden con la condición; actualiza Synapse si no llega ninguna notificación en una edición de vista previa finalizada.

Tuwunel

El mismo flujo que Synapse; no se necesita ninguna configuración específica de Tuwunel para el marcador de vista previa finalizada.

Si las notificaciones desaparecen mientras el usuario está activo en otro dispositivo, comprueba si `suppress_push_when_active` está habilitado. Tuwunel agregó esta opción en 1.4.2 (septiembre de 2025) y puede suprimir intencionalmente los push a otros dispositivos mientras un dispositivo está activo.

## Relacionado

  * [Configuración del canal Matrix](</es/channels/matrix>)
  * [Conceptos de streaming](</es/concepts/streaming>)


Was this useful?YesNo