---
title: Eliminación de BlueBubbles y la ruta imsg de iMessage
source_url: https://docs.openclaw.ai/es/announcements/bluebubbles-imessage
scraped_at: 2026-05-25
---

# Eliminación de BlueBubbles y la ruta de iMessage con imsg

OpenClaw ya no incluye el canal BlueBubbles. La compatibilidad con iMessage ahora funciona mediante el plugin `imessage` incluido, que inicia [`imsg`](<https://github.com/steipete/imsg>) localmente o mediante un contenedor SSH, y se comunica por JSON-RPC a través de stdin/stdout.

Si tu configuración todavía contiene `channels.bluebubbles`, mígrala a `channels.imessage`. La URL de documentación heredada `/channels/bluebubbles` redirige a [Migración desde BlueBubbles](</es/channels/imessage-from-bluebubbles>), que contiene la tabla completa de traducción de configuración y la lista de comprobación para el cambio.

## Qué cambió

  * No hay servidor HTTP de BlueBubbles, ruta de webhook, contraseña REST ni tiempo de ejecución del plugin BlueBubbles en la ruta iMessage compatible de OpenClaw.
  * OpenClaw lee y supervisa Messages mediante `imsg` en el Mac donde se ha iniciado sesión en Messages.app.
  * El envío, la recepción, el historial y los medios básicos usan las superficies normales de `imsg` y los permisos de macOS.
  * Las acciones avanzadas, como respuestas en hilos, tapbacks, edición, deshacer envío, efectos, confirmaciones de lectura, indicadores de escritura y administración de grupos, requieren `imsg launch` con el puente de API privada disponible.
  * Los gateways de Linux y Windows todavía pueden usar iMessage configurando `channels.imessage.cliPath` como un contenedor SSH que ejecuta `imsg` en el Mac con la sesión iniciada.


## Qué hacer

  1. Instala y verifica `imsg` en el Mac de Messages:

bashCopy code
[code]brew install steipete/tap/imsgimsg --versionimsg chats --limit 3imsg rpc --help
[/code]

  2. Concede permisos de Acceso total al disco y Automatización al contexto de proceso que ejecuta `imsg` y OpenClaw.

  3. Traduce la configuración anterior:

json5Copy code
[code]{  channels: {    imessage: {      enabled: true,      cliPath: "/opt/homebrew/bin/imsg",      dmPolicy: "pairing",      allowFrom: ["+15555550123"],      groupPolicy: "allowlist",      groupAllowFrom: ["+15555550123"],      groups: {        "*": { requireMention: true },      },      includeAttachments: true,    },  },}
[/code]

  4. Reinicia el gateway y verifica:

bashCopy code
[code]openclaw channels status --probe
[/code]

  5. Prueba los mensajes directos, grupos, adjuntos y cualquier acción de API privada de la que dependas antes de eliminar tu antiguo servidor BlueBubbles.


## Notas de migración

  * `channels.bluebubbles.serverUrl` y `channels.bluebubbles.password` no tienen equivalente en iMessage.
  * `channels.bluebubbles.allowFrom`, `groupAllowFrom`, `groups`, `includeAttachments`, las raíces de adjuntos, los límites de tamaño de medios, la fragmentación y los conmutadores de acciones tienen equivalentes en iMessage.
  * `channels.imessage.includeAttachments` sigue desactivado de forma predeterminada. Configúralo explícitamente si esperas que fotos, notas de voz, videos o archivos entrantes lleguen al agente.
  * Con `groupPolicy: "allowlist"`, copia el bloque `groups` anterior, incluida cualquier entrada comodín `"*"`. Las listas de permitidos de remitentes de grupo y el registro de grupos son barreras independientes.
  * Los enlaces ACP que coincidían con `channel: "bluebubbles"` deben cambiarse a `channel: "imessage"`.
  * Las claves de sesión antiguas de BlueBubbles no se convierten en claves de sesión de iMessage. Las aprobaciones de emparejamiento se conservan por identificador, pero el historial de conversaciones bajo claves de sesión de BlueBubbles no.


## Consulta también

  * [Migración desde BlueBubbles](</es/channels/imessage-from-bluebubbles>)
  * [iMessage](</es/channels/imessage>)
  * [Referencia de configuración - iMessage](</es/gateway/config-channels#imessage>)


Was this useful?YesNo