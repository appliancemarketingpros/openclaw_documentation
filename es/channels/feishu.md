---
title: Feishu
source_url: https://docs.openclaw.ai/es/channels/feishu
scraped_at: 2026-05-25
---

Feishu/Lark es una plataforma de colaboración integral donde los equipos conversan, comparten documentos, gestionan calendarios y trabajan juntos.

**Estado:** lista para producción para MD de bots + chats grupales. WebSocket es el modo predeterminado; el modo webhook es opcional.

* * *

## Inicio rápido

* ### Ejecuta el asistente de configuración del canal

bashCopy code
[code]
    openclaw channels login --channel feishu
[/code]

Elige la configuración manual para pegar un App ID y un App Secret de Feishu Open Platform, o elige la configuración por QR para crear un bot automáticamente. Si la aplicación móvil nacional de Feishu no reacciona al código QR, vuelve a ejecutar la configuración y elige la configuración manual.

* ### Una vez completada la configuración, reinicia el Gateway para aplicar los cambios

bashCopy code
[code]
    openclaw gateway restart
[/code]

* * *

## Control de acceso

### Mensajes directos

Configura `dmPolicy` para controlar quién puede enviar MD al bot:

  * `"pairing"` \- los usuarios desconocidos reciben un código de emparejamiento; apruébalo mediante la CLI
  * `"allowlist"` \- solo los usuarios indicados en `allowFrom` pueden chatear (predeterminado: solo el propietario del bot)
  * `"open"` \- permite MD públicos solo cuando `allowFrom` incluye `"*"`; con entradas restrictivas, solo los usuarios coincidentes pueden chatear
  * `"disabled"` \- desactiva todos los MD


**Aprobar una solicitud de emparejamiento:**

bashCopy code
[code]
    openclaw pairing list feishuopenclaw pairing approve feishu &lt;CODE&gt;
[/code]

### Chats grupales

**Política de grupo** (`channels.feishu.groupPolicy`):

Valor | Comportamiento  
---|---  
`"open"` | Responder a todos los mensajes en grupos  
`"allowlist"` | Responder solo a grupos en `groupAllowFrom` o configurados explícitamente en `groups.<chat_id>`  
`"disabled"` | Desactivar todos los mensajes de grupo; las entradas explícitas `groups.<chat_id>` no anulan esto  
  
Predeterminado: `allowlist`

**Requisito de mención** (`channels.feishu.requireMention`):

  * `true` \- requiere @mención (predeterminado)
  * `false` \- responde sin @mención
  * Anulación por grupo: `channels.feishu.groups.<chat_id>.requireMention`
  * `@all` y `@_all` de solo difusión no se tratan como menciones al bot. Un mensaje que menciona tanto a `@all` como directamente al bot sigue contando como mención al bot.


* * *

## Ejemplos de configuración de grupos

### Permitir todos los grupos, sin requerir @mención

json5Copy code
[code]
    {  channels: {    feishu: {      groupPolicy: "open",    },  },}
[/code]

### Permitir todos los grupos, seguir requiriendo @mención

json5Copy code
[code]
    {  channels: {    feishu: {      groupPolicy: "open",      requireMention: true,    },  },}
[/code]

### Permitir solo grupos específicos

json5Copy code
[code]
    {  channels: {    feishu: {      groupPolicy: "allowlist",      // Group IDs look like: oc_xxx      groupAllowFrom: ["oc_xxx", "oc_yyy"],    },  },}
[/code]

En modo `allowlist`, también puedes admitir un grupo añadiendo una entrada explícita `groups.<chat_id>`. Las entradas explícitas no anulan `groupPolicy: "disabled"`. Los valores predeterminados con comodín en `groups.*` configuran los grupos coincidentes, pero no admiten grupos por sí solos.

json5Copy code
[code]
    {  channels: {    feishu: {      groupPolicy: "allowlist",      groups: {        oc_xxx: {          requireMention: false,        },      },    },  },}
[/code]

### Restringir remitentes dentro de un grupo

json5Copy code
[code]
    {  channels: {    feishu: {      groupPolicy: "allowlist",      groupAllowFrom: ["oc_xxx"],      groups: {        oc_xxx: {          // User open_ids look like: ou_xxx          allowFrom: ["ou_user1", "ou_user2"],        },      },    },  },}
[/code]

* * *

## Obtener ID de grupo/usuario

### ID de grupo (`chat_id`, formato: `oc_xxx`)

Abre el grupo en Feishu/Lark, haz clic en el icono de menú en la esquina superior derecha y ve a **Configuración**. El ID del grupo (`chat_id`) aparece en la página de configuración.

![Obtener ID de grupo](/images/feishu-get-group-id.png)

### ID de usuario (`open_id`, formato: `ou_xxx`)

Inicia el Gateway, envía un MD al bot y luego revisa los registros:

bashCopy code
[code]
    openclaw logs --follow
[/code]

Busca `open_id` en la salida del registro. También puedes revisar las solicitudes de emparejamiento pendientes:

bashCopy code
[code]
    openclaw pairing list feishu
[/code]

* * *

## Comandos comunes

Comando | Descripción  
---|---  
`/status` | Mostrar el estado del bot  
`/reset` | Restablecer la sesión actual  
`/model` | Mostrar o cambiar el modelo de IA  
  
* * *

## Solución de problemas

### El bot no responde en chats grupales

  1. Asegúrate de que el bot se haya añadido al grupo
  2. Asegúrate de @mencionar al bot (requerido de forma predeterminada)
  3. Verifica que `groupPolicy` no sea `"disabled"`
  4. Revisa los registros: `openclaw logs --follow`


### El bot no recibe mensajes

  1. Asegúrate de que el bot esté publicado y aprobado en Feishu Open Platform / Lark Developer
  2. Asegúrate de que la suscripción de eventos incluya `im.message.receive_v1`
  3. Asegúrate de que esté seleccionada la **conexión persistente** (WebSocket)
  4. Asegúrate de que se hayan concedido todos los alcances de permisos requeridos
  5. Asegúrate de que el Gateway esté en ejecución: `openclaw gateway status`
  6. Revisa los registros: `openclaw logs --follow`


### La configuración por QR no reacciona en la aplicación móvil de Feishu

  1. Vuelve a ejecutar la configuración: `openclaw channels login --channel feishu`
  2. Elige la configuración manual
  3. En Feishu Open Platform, crea una aplicación autoconstruida y copia su App ID y App Secret
  4. Pega esas credenciales en el asistente de configuración


### App Secret filtrado

  1. Restablece el App Secret en Feishu Open Platform / Lark Developer
  2. Actualiza el valor en tu configuración
  3. Reinicia el Gateway: `openclaw gateway restart`


* * *

## Configuración avanzada

### Varias cuentas

json5Copy code
[code]
    {  channels: {    feishu: {      defaultAccount: "main",      accounts: {        main: {          appId: "cli_xxx",          appSecret: "xxx",          name: "Primary bot",          tts: {            providers: {              openai: { voice: "shimmer" },            },          },        },        backup: {          appId: "cli_yyy",          appSecret: "yyy",          name: "Backup bot",          enabled: false,        },      },    },  },}
[/code]

`defaultAccount` controla qué cuenta se usa cuando las API salientes no especifican un `accountId`. `accounts.<id>.tts` usa la misma forma que `messages.tts` y se fusiona en profundidad sobre la configuración global de TTS, por lo que las configuraciones de Feishu con varios bots pueden mantener globalmente las credenciales compartidas de proveedor y anular solo la voz, el modelo, la persona o el modo automático por cuenta.

### Límites de mensajes

  * `textChunkLimit` \- tamaño de fragmento de texto saliente (predeterminado: `2000` caracteres)
  * `mediaMaxMb` \- límite de carga/descarga de medios (predeterminado: `30` MB)


### Streaming

Feishu/Lark admite respuestas en streaming mediante tarjetas interactivas. Cuando está habilitado, el bot actualiza la tarjeta en tiempo real mientras genera texto.

json5Copy code
[code]
    {  channels: {    feishu: {      streaming: true, // enable streaming card output (default: true)      blockStreaming: true, // opt into completed-block streaming    },  },}
[/code]

Establece `streaming: false` para enviar la respuesta completa en un solo mensaje. `blockStreaming` está desactivado de forma predeterminada; actívalo solo cuando quieras vaciar los bloques completados del asistente antes de la respuesta final.

### Optimización de cuota

Reduce el número de llamadas a la API de Feishu/Lark con dos marcas opcionales:

  * `typingIndicator` (predeterminado `true`): establece `false` para omitir las llamadas de reacción de escritura
  * `resolveSenderNames` (predeterminado `true`): establece `false` para omitir las consultas de perfil del remitente

json5Copy code
[code]
    {  channels: {    feishu: {      typingIndicator: false,      resolveSenderNames: false,    },  },}
[/code]

### Sesiones ACP

Feishu/Lark admite ACP para MD y mensajes de hilos grupales. El ACP de Feishu/Lark se controla con comandos de texto: no hay menús nativos de comandos con barra, así que usa mensajes `/acp ...` directamente en la conversación.

#### Vinculación persistente de ACP

json5Copy code
[code]
    {  agents: {    list: [      {        id: "codex",        runtime: {          type: "acp",          acp: {            agent: "codex",            backend: "acpx",            mode: "persistent",            cwd: "/workspace/openclaw",          },        },      },    ],  },  bindings: [    {      type: "acp",      agentId: "codex",      match: {        channel: "feishu",        accountId: "default",        peer: { kind: "direct", id: "ou_1234567890" },      },    },    {      type: "acp",      agentId: "codex",      match: {        channel: "feishu",        accountId: "default",        peer: { kind: "group", id: "oc_group_chat:topic:om_topic_root" },      },      acp: { label: "codex-feishu-topic" },    },  ],}
[/code]

#### Generar ACP desde el chat

En un MD o hilo de Feishu/Lark:

textCopy code
[code]
    /acp spawn codex --thread here
[/code]

`--thread here` funciona para MD y mensajes de hilo de Feishu/Lark. Los mensajes posteriores en la conversación vinculada se enrutan directamente a esa sesión ACP.

### Enrutamiento multiagente

Usa `bindings` para enrutar MD o grupos de Feishu/Lark a diferentes agentes.

json5Copy code
[code]
    {  agents: {    list: [      { id: "main" },      { id: "agent-a", workspace: "/home/user/agent-a" },      { id: "agent-b", workspace: "/home/user/agent-b" },    ],  },  bindings: [    {      agentId: "agent-a",      match: {        channel: "feishu",        peer: { kind: "direct", id: "ou_xxx" },      },    },    {      agentId: "agent-b",      match: {        channel: "feishu",        peer: { kind: "group", id: "oc_zzz" },      },    },  ],}
[/code]

Campos de enrutamiento:

  * `match.channel`: `"feishu"`
  * `match.peer.kind`: `"direct"` (MD) o `"group"` (chat grupal)
  * `match.peer.id`: Open ID de usuario (`ou_xxx`) o ID de grupo (`oc_xxx`)


Consulta Obtener ID de grupo/usuario para ver consejos de búsqueda.

* * *

## Referencia de configuración

Configuración completa: [Configuración del Gateway](</es/gateway/configuration>)

Configuración | Descripción | Predeterminado  
---|---|---  
`channels.feishu.enabled` | Activar/desactivar el canal | `true`  
`channels.feishu.domain` | Dominio de API (`feishu` o `lark`) | `feishu`  
`channels.feishu.connectionMode` | Transporte de eventos (`websocket` o `webhook`) | `websocket`  
`channels.feishu.defaultAccount` | Cuenta predeterminada para el enrutamiento saliente | `default`  
`channels.feishu.verificationToken` | Requerido para el modo Webhook | -  
`channels.feishu.encryptKey` | Requerido para el modo Webhook | -  
`channels.feishu.webhookPath` | Ruta de la ruta Webhook | `/feishu/events`  
`channels.feishu.webhookHost` | Host de enlace de Webhook | `127.0.0.1`  
`channels.feishu.webhookPort` | Puerto de enlace de Webhook | `3000`  
`channels.feishu.accounts.<id>.appId` | ID de la aplicación | -  
`channels.feishu.accounts.<id>.appSecret` | Secreto de la aplicación | -  
`channels.feishu.accounts.<id>.domain` | Anulación de dominio por cuenta | `feishu`  
`channels.feishu.accounts.<id>.tts` | Anulación de TTS por cuenta | `messages.tts`  
`channels.feishu.dmPolicy` | Política de DM | `allowlist`  
`channels.feishu.allowFrom` | Lista de permitidos de DM (lista de open_id) | [BotOwnerId]  
`channels.feishu.groupPolicy` | Política de grupos | `allowlist`  
`channels.feishu.groupAllowFrom` | Lista de permitidos de grupos | -  
`channels.feishu.requireMention` | Requerir @mención en grupos | `true`  
`channels.feishu.groups.<chat_id>.requireMention` | Anulación de @mención por grupo; los ID explícitos también admiten el grupo en modo de lista de permitidos | heredado  
`channels.feishu.groups.<chat_id>.enabled` | Activar/desactivar un grupo específico | `true`  
`channels.feishu.textChunkLimit` | Tamaño de fragmento de mensaje | `2000`  
`channels.feishu.mediaMaxMb` | Límite de tamaño de multimedia | `30`  
`channels.feishu.streaming` | Salida de tarjeta en streaming | `true`  
`channels.feishu.blockStreaming` | Streaming de respuesta de bloque completado | `false`  
`channels.feishu.typingIndicator` | Enviar reacciones de escritura | `true`  
`channels.feishu.resolveSenderNames` | Resolver nombres para mostrar de remitentes | `true`  
  
* * *

## Tipos de mensajes compatibles

### Recibir

  * ✅ Texto
  * ✅ Texto enriquecido (post)
  * ✅ Imágenes
  * ✅ Archivos
  * ✅ Audio
  * ✅ Video/multimedia
  * ✅ Stickers


Los mensajes de audio entrantes de Feishu/Lark se normalizan como marcadores de posición multimedia en lugar de JSON `file_key` sin procesar. Cuando `tools.media.audio` está configurado, OpenClaw descarga el recurso de nota de voz y ejecuta la transcripción de audio compartida antes del turno del agente, por lo que el agente recibe la transcripción hablada. Si Feishu incluye texto de transcripción directamente en la carga de audio, ese texto se usa sin otra llamada ASR. Sin un proveedor de transcripción de audio, el agente aún recibe un marcador de posición `<media:audio>` más el adjunto guardado, no la carga de recurso Feishu sin procesar.

### Enviar

  * ✅ Texto
  * ✅ Imágenes
  * ✅ Archivos
  * ✅ Audio
  * ✅ Video/multimedia
  * ✅ Tarjetas interactivas (incluidas actualizaciones de streaming)
  * ⚠️ Texto enriquecido (formato estilo post; no admite todas las capacidades de autoría de Feishu/Lark)


Las burbujas de audio nativas de Feishu/Lark usan el tipo de mensaje `audio` de Feishu y requieren multimedia de carga Ogg/Opus (`file_type: "opus"`). Los medios `.opus` y `.ogg` existentes se envían directamente como audio nativo. MP3/WAV/M4A y otros formatos probablemente de audio se transcodifican a Ogg/Opus de 48 kHz con `ffmpeg` solo cuando la respuesta solicita entrega de voz (`audioAsVoice` / herramienta de mensajes `asVoice`, incluidas las respuestas de nota de voz con TTS). Los adjuntos MP3 ordinarios permanecen como archivos regulares. Si falta `ffmpeg` o la conversión falla, OpenClaw recurre a un adjunto de archivo y registra el motivo.

### Hilos y respuestas

  * ✅ Respuestas en línea
  * ✅ Respuestas en hilos
  * ✅ Las respuestas multimedia permanecen conscientes del hilo al responder a un mensaje de hilo


Para `groupSessionScope: "group_topic"` y `"group_topic_sender"`, los grupos de tema nativos de Feishu/Lark usan el `thread_id` del evento (`omt_*`) como clave canónica de sesión de tema. Si un evento iniciador de tema nativo omite `thread_id`, OpenClaw lo hidrata desde Feishu antes de enrutar el turno. Las respuestas de grupo normales que OpenClaw convierte en hilos siguen usando el ID del mensaje raíz de respuesta (`om_*`) para que el primer turno y el turno de seguimiento permanezcan en la misma sesión.

* * *

## Relacionado

  * [Resumen de canales](</es/channels>) \- todos los canales compatibles
  * [Emparejamiento](</es/channels/pairing>) \- autenticación de DM y flujo de emparejamiento
  * [Grupos](</es/channels/groups>) \- comportamiento del chat grupal y control de menciones
  * [Enrutamiento de canales](</es/channels/channel-routing>) \- enrutamiento de sesión para mensajes
  * [Seguridad](</es/gateway/security>) \- modelo de acceso y endurecimiento


Was this useful?YesNo