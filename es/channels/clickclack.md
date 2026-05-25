---
title: ClickClack
source_url: https://docs.openclaw.ai/es/channels/clickclack
scraped_at: 2026-05-25
---

ClickClack conecta OpenClaw con un espacio de trabajo ClickClack autohospedado mediante tokens de bot ClickClack de primera clase.

Usa esto cuando quieras que un agente de OpenClaw aparezca como usuario bot de ClickClack. ClickClack admite bots de servicio independientes y bots propiedad de usuarios; los bots propiedad de usuarios conservan un `owner_user_id` y reciben solo los alcances de token que concedas.

## Configuración rápida

Crea un token de bot en ClickClack:

bashCopy code
[code]
    clickclack admin bot create \  --workspace <workspace_id_or_slug> \  --name "OpenClaw" \  --handle openclaw \  --scopes bot:write \  --plain
[/code]

Para un bot propiedad de un usuario, agrega `--owner <user_id>`.

Configura OpenClaw:

json5Copy code
[code]
    {  plugins: {    entries: {      clickclack: {        llm: {          allowAgentIdOverride: true,        },      },    },  },  channels: {    clickclack: {      enabled: true,      baseUrl: "https://app.clickclack.chat",      token: { source: "env", provider: "default", id: "CLICKCLACK_BOT_TOKEN" },      workspace: "default",      defaultTo: "channel:general",      agentId: "clickclack-bot",      replyMode: "model",    },  },}
[/code]

Luego ejecuta:

bashCopy code
[code]
    export CLICKCLACK_BOT_TOKEN="ccb_..."openclaw gateway
[/code]

## Varios bots

Cada cuenta abre su propia conexión en tiempo real de ClickClack y usa su propio token de bot.

json5Copy code
[code]
    {  plugins: {    entries: {      clickclack: {        llm: {          allowAgentIdOverride: true,        },      },    },  },  channels: {    clickclack: {      enabled: true,      baseUrl: "https://app.clickclack.chat",      defaultAccount: "service",      accounts: {        service: {          token: { source: "env", provider: "default", id: "CLICKCLACK_SERVICE_BOT_TOKEN" },          workspace: "default",          defaultTo: "channel:general",          agentId: "service-bot",          replyMode: "model",        },        peter: {          token: { source: "env", provider: "default", id: "CLICKCLACK_PETER_BOT_TOKEN" },          workspace: "default",          defaultTo: "dm:usr_...",          agentId: "peter-bot",          replyMode: "model",        },      },    },  },}
[/code]

`replyMode: "model"` usa `api.runtime.llm.complete` directamente para respuestas breves del bot. Cuando una cuenta establece `agentId`, OpenClaw requiere el bit de confianza explícito `plugins.entries.clickclack.llm.allowAgentIdOverride` para que el plugin pueda ejecutar completados para ese agente bot. Mantenlo desactivado si solo usas la ruta de agente predeterminada.

## Destinos

  * `channel:<name-or-id>` envía a un canal del espacio de trabajo. Los destinos sin prefijo usan `channel:` de forma predeterminada.
  * `dm:<user_id>` crea o reutiliza una conversación directa con ese usuario.
  * `thread:<message_id>` responde en un hilo existente.


Ejemplos:

bashCopy code
[code]
    openclaw message send --channel clickclack --target channel:general --message "hello"openclaw message send --channel clickclack --target dm:usr_123 --message "hello"openclaw message send --channel clickclack --target thread:msg_123 --message "following up"
[/code]

## Permisos

La API de ClickClack aplica los alcances de token de ClickClack.

  * `bot:read`: leer datos de espacio de trabajo/canal/mensaje/hilo/MD/tiempo real/perfil.
  * `bot:write`: `bot:read` más mensajes de canal, respuestas en hilos, MD y cargas.
  * `bot:admin`: `bot:write` más creación de canales.


OpenClaw solo necesita `bot:write` para el chat normal de agentes.

## Solución de problemas

  * `ClickClack is not configured`: establece `channels.clickclack.token` o `CLICKCLACK_BOT_TOKEN`.
  * `workspace not found`: establece `workspace` con el id o slug del espacio de trabajo devuelto por ClickClack.
  * No hay respuestas entrantes: confirma que el token tenga acceso de lectura en tiempo real y que el bot no esté respondiendo a sus propios mensajes.
  * Fallan los envíos al canal: verifica que el bot sea miembro del espacio de trabajo y tenga `bot:write`.


Was this useful?YesNo