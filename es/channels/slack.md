---
title: Slack
source_url: https://docs.openclaw.ai/es/channels/slack
scraped_at: 2026-05-25
---

Listo para producción para mensajes directos y canales mediante integraciones de apps de Slack. El modo predeterminado es Socket Mode; también se admiten URL de solicitud HTTP.

[**Emparejamiento** Los mensajes directos de Slack usan el modo de emparejamiento de forma predeterminada. ](</es/channels/pairing>) [**Comandos de barra** Comportamiento de comandos nativos y catálogo de comandos. ](</es/tools/slash-commands>) [**Solución de problemas de canales** Diagnósticos entre canales y guías de reparación. ](</es/channels/troubleshooting>)

## Elegir Socket Mode o URL de solicitud HTTP

Ambos transportes están listos para producción y alcanzan paridad de funciones para mensajería, comandos de barra, App Home e interactividad. Elige según la forma de despliegue, no según las funciones.

Aspecto | Socket Mode (predeterminado) | URL de solicitud HTTP  
---|---|---  
URL pública del Gateway | No requerida | Requerida (DNS, TLS, proxy inverso o túnel)  
Red saliente | La WSS saliente hacia `wss-primary.slack.com` debe ser accesible | Sin WS saliente; solo HTTPS entrante  
Tokens necesarios | Token de bot (`xoxb-...`) + token de nivel de app (`xapp-...`) con `connections:write` | Token de bot (`xoxb-...`) + secreto de firma  
Portátil de desarrollo / detrás de firewall | Funciona tal cual | Necesita un túnel público (ngrok, Cloudflare Tunnel, Tailscale Funnel) o un Gateway de staging  
Escalado horizontal | Una sesión de Socket Mode por app y por host; varios Gateways necesitan apps de Slack separadas | Manejador POST sin estado; varias réplicas de Gateway pueden compartir una app detrás de un balanceador de carga  
Varias cuentas en un Gateway | Admitido; cada cuenta abre su propia WS | Admitido; cada cuenta necesita un `webhookPath` único (predeterminado `/slack/events`) para que los registros no colisionen  
Transporte de comandos de barra | Entregado mediante la conexión WS; `slash_commands[].url` se ignora | Slack hace POST a `slash_commands[].url`; el campo es requerido para despachar el comando  
Firma de solicitudes | No se usa (la autenticación es el token de nivel de app) | Slack firma cada solicitud; OpenClaw verifica con `signingSecret`  
Recuperación ante caída de conexión | El SDK de Slack se reconecta automáticamente; se aplica el ajuste de transporte de timeout de pong del Gateway | No hay conexión persistente que pueda caer; los reintentos son por solicitud desde Slack  
  
## Configuración rápida

### Socket Mode (predeterminado)

* ### Crear una nueva app de Slack

Abre [api.slack.com/apps](<https://api.slack.com/apps/new>) → **Create New App** → **From a manifest** → selecciona tu espacio de trabajo → pega uno de los manifiestos siguientes → **Next** → **Create**.

RecomendadoCopy code
[code]
    {"display_information": {"name": "OpenClaw","description": "Slack connector for OpenClaw"},"features": {"bot_user": { "display_name": "OpenClaw", "always_online": true },"app_home": {"home_tab_enabled": true,"messages_tab_enabled": true,"messages_tab_read_only_enabled": false},"slash_commands": [{"command": "/openclaw","description": "Send a message to OpenClaw","should_escape": false}]},"oauth_config": {"scopes": {"bot": ["app_mentions:read","assistant:write","channels:history","channels:read","chat:write","commands","emoji:read","files:read","files:write","groups:history","groups:read","im:history","im:read","im:write","mpim:history","mpim:read","mpim:write","pins:read","pins:write","reactions:read","reactions:write","usergroups:read","users:read"]}},"settings": {"socket_mode_enabled": true,"event_subscriptions": {"bot_events": ["app_home_opened","app_mention","channel_rename","member_joined_channel","member_left_channel","message.channels","message.groups","message.im","message.mpim","pin_added","pin_removed","reaction_added","reaction_removed"]}}}
[/code]

MínimoCopy code
[code]
    {"display_information": {"name": "OpenClaw","description": "Slack connector for OpenClaw"},"features": {"bot_user": { "display_name": "OpenClaw", "always_online": true },"app_home": {"home_tab_enabled": true,"messages_tab_enabled": true,"messages_tab_read_only_enabled": false},"slash_commands": [{"command": "/openclaw","description": "Send a message to OpenClaw","should_escape": false}]},"oauth_config": {"scopes": {"bot": ["app_mentions:read","assistant:write","channels:history","channels:read","chat:write","commands","groups:history","groups:read","im:history","im:read","im:write","users:read"]}},"settings": {"socket_mode_enabled": true,"event_subscriptions": {"bot_events": ["app_home_opened","app_mention","message.channels","message.groups","message.im"]}}}
[/code]

Después de que Slack cree la app:

  * **Basic Information → App-Level Tokens → Generate Token and Scopes** : añade `connections:write`, guarda y copia el valor `xapp-...`.
  * **Install App → Install to Workspace** : copia el token OAuth de usuario de bot `xoxb-...`.


* ### Configurar OpenClaw

Configuración SecretRef recomendada:

bashCopy code
[code]
    export SLACK_APP_TOKEN=xapp-...export SLACK_BOT_TOKEN=xoxb-...cat > slack.socket.patch.json5 <<'JSON5'{channels: {slack: {enabled: true,mode: "socket",appToken: { source: "env", provider: "default", id: "SLACK_APP_TOKEN" },botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },},},}JSON5openclaw config patch --file ./slack.socket.patch.json5 --dry-runopenclaw config patch --file ./slack.socket.patch.json5
[/code]

Fallback de entorno (solo cuenta predeterminada):

bashCopy code
[code]
    SLACK_APP_TOKEN=xapp-...SLACK_BOT_TOKEN=xoxb-...
[/code]

* ### Iniciar Gateway

bashCopy code
[code]
    openclaw gateway
[/code]

### URL de solicitud HTTP

* ### Crear una nueva app de Slack

Abre [api.slack.com/apps](<https://api.slack.com/apps/new>) → **Create New App** → **From a manifest** → selecciona tu espacio de trabajo → pega uno de los manifiestos siguientes → reemplaza `https://gateway-host.example.com/slack/events` por tu URL pública de Gateway → **Next** → **Create**.

RecomendadoCopy code
[code]
    {"display_information": {"name": "OpenClaw","description": "Slack connector for OpenClaw"},"features": {"bot_user": { "display_name": "OpenClaw", "always_online": true },"app_home": {"home_tab_enabled": true,"messages_tab_enabled": true,"messages_tab_read_only_enabled": false},"slash_commands": [{"command": "/openclaw","description": "Send a message to OpenClaw","should_escape": false,"url": "https://gateway-host.example.com/slack/events"}]},"oauth_config": {"scopes": {"bot": ["app_mentions:read","assistant:write","channels:history","channels:read","chat:write","commands","emoji:read","files:read","files:write","groups:history","groups:read","im:history","im:read","im:write","mpim:history","mpim:read","mpim:write","pins:read","pins:write","reactions:read","reactions:write","usergroups:read","users:read"]}},"settings": {"event_subscriptions": {"request_url": "https://gateway-host.example.com/slack/events","bot_events": ["app_home_opened","app_mention","channel_rename","member_joined_channel","member_left_channel","message.channels","message.groups","message.im","message.mpim","pin_added","pin_removed","reaction_added","reaction_removed"]},"interactivity": {"is_enabled": true,"request_url": "https://gateway-host.example.com/slack/events","message_menu_options_url": "https://gateway-host.example.com/slack/events"}}}
[/code]

MinimalCopy code
[code]
    {"display_information": {"name": "OpenClaw","description": "Slack connector for OpenClaw"},"features": {"bot_user": { "display_name": "OpenClaw", "always_online": true },"app_home": {"home_tab_enabled": true,"messages_tab_enabled": true,"messages_tab_read_only_enabled": false},"slash_commands": [{"command": "/openclaw","description": "Send a message to OpenClaw","should_escape": false,"url": "https://gateway-host.example.com/slack/events"}]},"oauth_config": {"scopes": {"bot": ["app_mentions:read","assistant:write","channels:history","channels:read","chat:write","commands","groups:history","groups:read","im:history","im:read","im:write","users:read"]}},"settings": {"event_subscriptions": {"request_url": "https://gateway-host.example.com/slack/events","bot_events": ["app_home_opened","app_mention","message.channels","message.groups","message.im"]},"interactivity": {"is_enabled": true,"request_url": "https://gateway-host.example.com/slack/events","message_menu_options_url": "https://gateway-host.example.com/slack/events"}}}
[/code]

Después de que Slack cree la app:

  * **Basic Information → App Credentials** : copia el **Signing Secret** para la verificación de solicitudes.
  * **Install App → Install to Workspace** : copia el Bot User OAuth Token `xoxb-...`.


* ### Configure OpenClaw

Configuración recomendada de SecretRef:

bashCopy code
[code]
    export SLACK_BOT_TOKEN=xoxb-...export SLACK_SIGNING_SECRET=...cat > slack.http.patch.json5 <<'JSON5'{channels: {slack: {enabled: true,mode: "http",botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },signingSecret: { source: "env", provider: "default", id: "SLACK_SIGNING_SECRET" },webhookPath: "/slack/events",},},}JSON5openclaw config patch --file ./slack.http.patch.json5 --dry-runopenclaw config patch --file ./slack.http.patch.json5
[/code]

* ### Start gateway

bashCopy code
[code]
    openclaw gateway
[/code]

## Ajuste del transporte en Socket Mode

OpenClaw establece de forma predeterminada el tiempo de espera de pong del cliente del SDK de Slack en 15 segundos para Socket Mode. Sobrescribe la configuración de transporte solo cuando necesites ajustes específicos del espacio de trabajo o del host:

json5Copy code
[code]
    {  channels: {    slack: {      mode: "socket",      socketMode: {        clientPingTimeout: 20000,        serverPingTimeout: 30000,        pingPongLoggingEnabled: false,      },    },  },}
[/code]

Úsalo solo para espacios de trabajo en Socket Mode que registren tiempos de espera de pong/ping de servidor de websocket de Slack o que se ejecuten en hosts con bloqueo conocido del bucle de eventos. `clientPingTimeout` es la espera del pong después de que el SDK envía un ping de cliente; `serverPingTimeout` es la espera de pings del servidor de Slack. Los mensajes y eventos de la app siguen siendo estado de la aplicación, no señales de actividad del transporte.

## Lista de comprobación de manifiesto y alcances

El manifiesto base de la app de Slack es el mismo para Socket Mode y para las URL de solicitud HTTP. Solo difieren el bloque `settings` (y la `url` del comando de barra diagonal).

Manifiesto base (predeterminado de Socket Mode):

jsonCopy code
[code]
    {  "display_information": {    "name": "OpenClaw",    "description": "Slack connector for OpenClaw"  },  "features": {    "bot_user": { "display_name": "OpenClaw", "always_online": true },    "app_home": {      "home_tab_enabled": true,      "messages_tab_enabled": true,      "messages_tab_read_only_enabled": false    },    "slash_commands": [      {        "command": "/openclaw",        "description": "Send a message to OpenClaw",        "should_escape": false      }    ]  },  "oauth_config": {    "scopes": {      "bot": [        "app_mentions:read",        "assistant:write",        "channels:history",        "channels:read",        "chat:write",        "commands",        "emoji:read",        "files:read",        "files:write",        "groups:history",        "groups:read",        "im:history",        "im:read",        "im:write",        "mpim:history",        "mpim:read",        "mpim:write",        "pins:read",        "pins:write",        "reactions:read",        "reactions:write",        "usergroups:read",        "users:read"      ]    }  },  "settings": {    "socket_mode_enabled": true,    "event_subscriptions": {      "bot_events": [        "app_home_opened",        "app_mention",        "channel_rename",        "member_joined_channel",        "member_left_channel",        "message.channels",        "message.groups",        "message.im",        "message.mpim",        "pin_added",        "pin_removed",        "reaction_added",        "reaction_removed"      ]    }  }}
[/code]

Para el **modo de URL de solicitud HTTP** , reemplaza `settings` por la variante HTTP y añade `url` a cada comando de barra diagonal. Se requiere una URL pública:

jsonCopy code
[code]
    {  "features": {    "slash_commands": [      {        "command": "/openclaw",        "description": "Send a message to OpenClaw",        "should_escape": false,        "url": "https://gateway-host.example.com/slack/events"      }    ]  },  "settings": {    "event_subscriptions": {      "request_url": "https://gateway-host.example.com/slack/events",      "bot_events": [        "app_home_opened",        "app_mention",        "channel_rename",        "member_joined_channel",        "member_left_channel",        "message.channels",        "message.groups",        "message.im",        "message.mpim",        "pin_added",        "pin_removed",        "reaction_added",        "reaction_removed"      ]    },    "interactivity": {      "is_enabled": true,      "request_url": "https://gateway-host.example.com/slack/events",      "message_menu_options_url": "https://gateway-host.example.com/slack/events"    }  }}
[/code]

### Configuración adicional del manifiesto

Expón distintas funciones que amplían los valores predeterminados anteriores.

El manifiesto predeterminado habilita la pestaña **Home** de Slack App Home y se suscribe a `app_home_opened`. Cuando un miembro del espacio de trabajo abre la pestaña Home, OpenClaw publica una vista Home predeterminada segura con `views.publish`; no se incluye ninguna carga útil de conversación ni configuración privada. La pestaña **Messages** permanece habilitada para los mensajes directos de Slack.

Optional native slash commands

Se pueden usar varios comandos de barra diagonal nativos en lugar de un único comando configurado, con matices:

  * Usa `/agentstatus` en lugar de `/status` porque el comando `/status` está reservado.
  * No pueden estar disponibles más de 25 comandos de barra diagonal a la vez.


Reemplaza tu sección `features.slash_commands` existente por un subconjunto de los [comandos disponibles](</es/tools/slash-commands#command-list>):

### Socket Mode (default)

jsonCopy code
[code]
    {"slash_commands": [{"command": "/new","description": "Start a new session","usage_hint": "[model]"},{"command": "/reset","description": "Reset the current session"},{"command": "/compact","description": "Compact the session context","usage_hint": "[instructions]"},{"command": "/stop","description": "Stop the current run"},{"command": "/session","description": "Manage thread-binding expiry","usage_hint": "idle <duration|off> or max-age <duration|off>"},{"command": "/think","description": "Set the thinking level","usage_hint": "<level>"},{"command": "/verbose","description": "Toggle verbose output","usage_hint": "on|off|full"},{"command": "/fast","description": "Show or set fast mode","usage_hint": "[status|on|off]"},{"command": "/reasoning","description": "Toggle reasoning visibility","usage_hint": "[on|off|stream]"},{"command": "/elevated","description": "Toggle elevated mode","usage_hint": "[on|off|ask|full]"},{"command": "/exec","description": "Show or set exec defaults","usage_hint": "host=<auto|sandbox|gateway|node> security=<deny|allowlist|full> ask=<off|on-miss|always> node=<id>"},{"command": "/model","description": "Show or set the model","usage_hint": "[name|#|status]"},{"command": "/models","description": "List providers/models","usage_hint": "[provider] [page] [limit=<n>|size=<n>|all]"},{"command": "/help","description": "Show the short help summary"},{"command": "/commands","description": "Show the generated command catalog"},{"command": "/tools","description": "Show what the current agent can use right now","usage_hint": "[compact|verbose]"},{"command": "/agentstatus","description": "Show runtime status, including provider usage/quota when available"},{"command": "/tasks","description": "List active/recent background tasks for the current session"},{"command": "/context","description": "Explain how context is assembled","usage_hint": "[list|detail|json]"},{"command": "/whoami","description": "Show your sender identity"},{"command": "/skill","description": "Run a skill by name","usage_hint": "<name> [input]"},{"command": "/btw","description": "Ask a side question without changing session context","usage_hint": "<question>"},{"command": "/side","description": "Ask a side question without changing session context","usage_hint": "<question>"},{"command": "/usage","description": "Control the usage footer or show cost summary","usage_hint": "off|tokens|full|cost"}]}
[/code]

### HTTP Request URLs

Usa la misma lista `slash_commands` que en Socket Mode arriba y añade `"url": "https://gateway-host.example.com/slack/events"` a cada entrada. Ejemplo:

jsonCopy code
[code]
    {"slash_commands": [{"command": "/new","description": "Start a new session","usage_hint": "[model]","url": "https://gateway-host.example.com/slack/events"},{"command": "/help","description": "Show the short help summary","url": "https://gateway-host.example.com/slack/events"}]}
[/code]

Repite ese valor de `url` en todos los comandos de la lista.

Optional authorship scopes (write operations)

Añade el alcance de bot `chat:write.customize` si quieres que los mensajes salientes usen la identidad del agente activo (nombre de usuario e icono personalizados) en lugar de la identidad predeterminada de la aplicación de Slack.

Si usas un icono de emoji, Slack espera la sintaxis `:emoji_name:`.

Optional user-token scopes (read operations)

Si configuras `channels.slack.userToken`, los alcances de lectura típicos son:

  * `channels:history`, `groups:history`, `im:history`, `mpim:history`
  * `channels:read`, `groups:read`, `im:read`, `mpim:read`
  * `users:read`
  * `reactions:read`
  * `pins:read`
  * `emoji:read`
  * `search:read` (si dependes de lecturas de búsqueda de Slack)


## Modelo de tokens

  * `botToken` \+ `appToken` son obligatorios para Socket Mode.
  * El modo HTTP requiere `botToken` \+ `signingSecret`.
  * `botToken`, `appToken`, `signingSecret` y `userToken` aceptan cadenas de texto sin formato u objetos SecretRef.
  * Los tokens de configuración anulan el respaldo de env.
  * El respaldo de env `SLACK_BOT_TOKEN` / `SLACK_APP_TOKEN` se aplica solo a la cuenta predeterminada.
  * `userToken` (`xoxp-...`) solo se configura por configuración (sin respaldo de env) y usa de forma predeterminada un comportamiento de solo lectura (`userTokenReadOnly: true`).


Comportamiento de instantánea de estado:

  * La inspección de cuenta de Slack rastrea campos `*Source` y `*Status` por credencial (`botToken`, `appToken`, `signingSecret`, `userToken`).
  * El estado es `available`, `configured_unavailable` o `missing`.
  * `configured_unavailable` significa que la cuenta está configurada mediante SecretRef u otra fuente secreta no integrada en línea, pero la ruta actual de comando/runtime no pudo resolver el valor real.
  * En modo HTTP, se incluye `signingSecretStatus`; en Socket Mode, el par requerido es `botTokenStatus` \+ `appTokenStatus`.


## Acciones y puertas

Las acciones de Slack se controlan mediante `channels.slack.actions.*`.

Grupos de acciones disponibles en las herramientas actuales de Slack:

Grupo | Predeterminado  
---|---  
mensajes | habilitado  
reacciones | habilitado  
pins | habilitado  
memberInfo | habilitado  
emojiList | habilitado  
  
Las acciones actuales de mensajes de Slack incluyen `send`, `upload-file`, `download-file`, `read`, `edit`, `delete`, `pin`, `unpin`, `list-pins`, `member-info` y `emoji-list`. `download-file` acepta IDs de archivo de Slack que se muestran en marcadores de posición de archivos entrantes y devuelve vistas previas de imágenes para imágenes o metadatos de archivo local para otros tipos de archivo.

## Control de acceso y enrutamiento

### DM policy

`channels.slack.dmPolicy` controla el acceso a DM. `channels.slack.allowFrom` es la lista de permitidos canónica de DM.

  * `pairing` (predeterminado)
  * `allowlist`
  * `open` (requiere que `channels.slack.allowFrom` incluya `"*"`)
  * `disabled`


Indicadores de DM:

  * `dm.enabled` (predeterminado true)
  * `channels.slack.allowFrom`
  * `dm.allowFrom` (heredado)
  * `dm.groupEnabled` (DM de grupo predeterminados false)
  * `dm.groupChannels` (lista de permitidos opcional de MPIM)


Precedencia de varias cuentas:

  * `channels.slack.accounts.default.allowFrom` se aplica solo a la cuenta `default`.
  * Las cuentas con nombre heredan `channels.slack.allowFrom` cuando su propio `allowFrom` no está definido.
  * Las cuentas con nombre no heredan `channels.slack.accounts.default.allowFrom`.


`channels.slack.dm.policy` y `channels.slack.dm.allowFrom` heredados se siguen leyendo por compatibilidad. `openclaw doctor --fix` los migra a `dmPolicy` y `allowFrom` cuando puede hacerlo sin cambiar el acceso.

El emparejamiento en DM usa `openclaw pairing approve slack <code>`.

### Channel policy

`channels.slack.groupPolicy` controla el manejo de canales:

  * `open`
  * `allowlist`
  * `disabled`


La lista de permitidos de canales está en `channels.slack.channels` y **debe usar IDs estables de canal de Slack** (por ejemplo `C12345678`) como claves de configuración.

Nota de runtime: si `channels.slack` falta por completo (configuración solo con env), el runtime vuelve a `groupPolicy="allowlist"` y registra una advertencia (incluso si `channels.defaults.groupPolicy` está definido).

Resolución de nombre/ID:

  * las entradas de listas de permitidos de canales y DM se resuelven al inicio cuando el acceso al token lo permite
  * las entradas de nombre de canal sin resolver se conservan tal como están configuradas, pero se ignoran para el enrutamiento de forma predeterminada
  * la autorización entrante y el enrutamiento de canales priorizan el ID de forma predeterminada; la coincidencia directa por nombre de usuario/slug requiere `channels.slack.dangerouslyAllowNameMatching: true`


### Mentions and channel users

Los mensajes de canal están protegidos por mención de forma predeterminada.

Fuentes de mención:

  * mención explícita de la aplicación (`<@botId>`)
  * mención de grupo de usuarios de Slack (`<!subteam^S...>`) cuando el usuario bot es miembro de ese grupo de usuarios; requiere `usergroups:read`
  * patrones regex de mención (`agents.list[].groupChat.mentionPatterns`, respaldo `messages.groupChat.mentionPatterns`)
  * comportamiento implícito de hilo de respuesta al bot (deshabilitado cuando `thread.requireExplicitMention` es `true`)


Controles por canal (`channels.slack.channels.<id>`; nombres solo mediante resolución al inicio o `dangerouslyAllowNameMatching`):

  * `requireMention`
  * `users` (lista de permitidos)
  * `allowBots`
  * `skills`
  * `systemPrompt`
  * `tools`, `toolsBySender`
  * formato de clave de `toolsBySender`: `channel:`, `id:`, `e164:`, `username:`, `name:` o comodín `"*"` (las claves heredadas sin prefijo aún se asignan solo a `id:`)


`allowBots` es conservador para canales y canales privados: los mensajes de sala redactados por bots se aceptan solo cuando el bot remitente aparece explícitamente en la lista de permitidos `users` de esa sala, o cuando al menos un ID de propietario explícito de Slack de `channels.slack.allowFrom` es actualmente miembro de la sala. Los comodines y las entradas de propietario por nombre para mostrar no satisfacen la presencia del propietario. La presencia del propietario usa `conversations.members` de Slack; asegúrate de que la aplicación tenga el alcance de lectura correspondiente para el tipo de sala (`channels:read` para canales públicos, `groups:read` para canales privados). Si falla la búsqueda de miembros, OpenClaw descarta el mensaje de sala redactado por bot.

## Hilos, sesiones y etiquetas de respuesta

  * Los DM se enrutan como `direct`; los canales como `channel`; los MPIM como `group`.
  * Los vínculos de ruta de Slack aceptan IDs de par sin procesar además de formas de destino de Slack como `channel:C12345678`, `user:U12345678` y `<@U12345678>`.
  * Con `session.dmScope=main` predeterminado, los DM de Slack se contraen a la sesión principal del agente.
  * Sesiones de canal: `agent:<agentId>:slack:channel:<channelId>`.
  * Las respuestas de hilo pueden crear sufijos de sesión de hilo (`:thread:<threadTs>`) cuando corresponde.
  * En canales donde OpenClaw maneja mensajes de nivel superior sin requerir una mención explícita, los `replyToMode` que no sean `off` enrutan cada raíz manejada a `agent:<agentId>:slack:channel:<channelId>:thread:<rootTs>` para que el hilo visible de Slack se asigne a una sesión de OpenClaw desde el primer turno.
  * El valor predeterminado de `channels.slack.thread.historyScope` es `thread`; el valor predeterminado de `thread.inheritParent` es `false`.
  * `channels.slack.thread.initialHistoryLimit` controla cuántos mensajes de hilo existentes se recuperan cuando se inicia una nueva sesión de hilo (predeterminado `20`; establece `0` para deshabilitarlo).
  * `channels.slack.thread.requireExplicitMention` (predeterminado `false`): cuando es `true`, suprime las menciones implícitas de hilo para que el bot solo responda a menciones explícitas de `@bot` dentro de hilos, incluso cuando el bot ya participó en el hilo. Sin esto, las respuestas en un hilo en el que participó el bot omiten la puerta de `requireMention`.


Controles de hilos de respuesta:

  * `channels.slack.replyToMode`: `off|first|all|batched` (predeterminado `off`)
  * `channels.slack.replyToModeByChatType`: por `direct|group|channel`
  * respaldo heredado para chats directos: `channels.slack.dm.replyToMode`


Se admiten etiquetas de respuesta manuales:

  * `[[reply_to_current]]`
  * `[[reply_to:<id>]]`


Para respuestas explícitas de hilo de Slack desde la herramienta `message`, establece `replyBroadcast: true` con `action: "send"` y `threadId` o `replyTo` para pedir a Slack que también difunda la respuesta de hilo al canal principal. Esto se asigna al indicador `reply_broadcast` de `chat.postMessage` de Slack y solo se admite para envíos de texto o Block Kit, no para cargas de medios.

Cuando una llamada a la herramienta `message` se ejecuta dentro de un hilo de Slack y apunta al mismo canal, OpenClaw normalmente hereda el hilo actual de Slack según `replyToMode`. Establece `topLevel: true` en `action: "send"` o `action: "upload-file"` para forzar un nuevo mensaje en el canal principal. `threadId: null` se acepta como la misma exclusión de nivel superior.

## Reacciones de confirmación

`ackReaction` envía un emoji de confirmación mientras OpenClaw procesa un mensaje entrante.

Orden de resolución:

  * `channels.slack.accounts.<accountId>.ackReaction`
  * `channels.slack.ackReaction`
  * `messages.ackReaction`
  * respaldo de emoji de identidad del agente (`agents.list[].identity.emoji`, si no, "👀")


Notas:

  * Slack espera shortcodes (por ejemplo `"eyes"`).
  * Usa `""` para deshabilitar la reacción para la cuenta de Slack o globalmente.


## Streaming de texto

`channels.slack.streaming` controla el comportamiento de vista previa en vivo:

  * `off`: deshabilitar el streaming de vista previa en vivo.
  * `partial` (predeterminado): reemplazar el texto de vista previa por la salida parcial más reciente.
  * `block`: anexar actualizaciones de vista previa por fragmentos.
  * `progress`: mostrar texto de estado de progreso mientras se genera y luego enviar el texto final.
  * `streaming.preview.toolProgress`: cuando la vista previa de borrador está activa, enrutar las actualizaciones de herramienta/progreso al mismo mensaje de vista previa editado (predeterminado: `true`). Establece `false` para mantener mensajes de herramienta/progreso separados.
  * `streaming.preview.commandText` / `streaming.progress.commandText`: establece en `status` para conservar líneas compactas de progreso de herramientas mientras se oculta el texto sin procesar de command/exec (predeterminado: `raw`).


Ocultar texto sin procesar de command/exec mientras se conservan líneas compactas de progreso:

jsonCopy code
[code]
    {  "channels": {    "slack": {      "streaming": {        "mode": "progress",        "progress": {          "toolProgress": true,          "commandText": "status"        }      }    }  }}
[/code]

`channels.slack.streaming.nativeTransport` controla el streaming de texto nativo de Slack cuando `channels.slack.streaming.mode` es `partial` (predeterminado: `true`).

  * Debe haber un hilo de respuesta disponible para que aparezcan el streaming de texto nativo y el estado de hilo del asistente de Slack. La selección de hilo sigue obedeciendo `replyToMode`.
  * Las raíces de canal, chat de grupo y DM de nivel superior pueden seguir usando la vista previa de borrador normal cuando el streaming nativo no está disponible o no existe ningún hilo de respuesta.
  * Los DM de Slack de nivel superior permanecen fuera de hilo de forma predeterminada, por lo que no muestran la vista previa de streaming/estado nativa con estilo de hilo de Slack; en su lugar, OpenClaw publica y edita una vista previa de borrador en el DM.
  * Los medios y las cargas útiles que no son texto recurren a la entrega normal.
  * Los finales de medios/errores cancelan las ediciones de vista previa pendientes; los finales de texto/bloque elegibles se vacían solo cuando pueden editar la vista previa en el mismo lugar.
  * Si el streaming falla a mitad de respuesta, OpenClaw recurre a la entrega normal para las cargas útiles restantes.


Usar la vista previa de borrador en lugar del streaming de texto nativo de Slack:

json5Copy code
[code]
    {  channels: {    slack: {      streaming: {        mode: "partial",        nativeTransport: false,      },    },  },}
[/code]

Claves heredadas:

  * `channels.slack.streamMode` (`replace | status_final | append`) es un alias de tiempo de ejecución heredado para `channels.slack.streaming.mode`.
  * El booleano `channels.slack.streaming` es un alias de tiempo de ejecución heredado para `channels.slack.streaming.mode` y `channels.slack.streaming.nativeTransport`.
  * `channels.slack.nativeStreaming` heredado es un alias de tiempo de ejecución para `channels.slack.streaming.nativeTransport`.
  * Ejecuta `openclaw doctor --fix` para reescribir la configuración de streaming de Slack persistida a las claves canónicas.


## Alternativa de reacción de escritura

`typingReaction` agrega una reacción temporal al mensaje entrante de Slack mientras OpenClaw procesa una respuesta, y luego la elimina cuando termina la ejecución. Esto es más útil fuera de las respuestas en hilos, que usan un indicador de estado predeterminado "is typing...".

Orden de resolución:

  * `channels.slack.accounts.<accountId>.typingReaction`
  * `channels.slack.typingReaction`


Notas:

  * Slack espera shortcodes (por ejemplo, `"hourglass_flowing_sand"`).
  * La reacción es de mejor esfuerzo y la limpieza se intenta automáticamente después de que se completa la respuesta o la ruta de fallo.


## Medios, fragmentación y entrega

Adjuntos entrantes

Los archivos adjuntos de Slack se descargan desde URL privadas alojadas en Slack (flujo de solicitud autenticado con token) y se escriben en el almacén de medios cuando la obtención se realiza correctamente y los límites de tamaño lo permiten. Los marcadores de archivo incluyen el `fileId` de Slack para que los agentes puedan obtener el archivo original con `download-file`.

Las descargas usan tiempos de espera acotados totales y de inactividad. Si la recuperación de archivos de Slack se queda bloqueada o falla, OpenClaw sigue procesando el mensaje y recurre al marcador de archivo.

El límite de tamaño entrante en tiempo de ejecución se establece de forma predeterminada en `20MB`, a menos que `channels.slack.mediaMaxMb` lo sobrescriba.

Texto y archivos salientes

  * los fragmentos de texto usan `channels.slack.textChunkLimit` (predeterminado 4000)
  * `channels.slack.chunkMode="newline"` habilita la división priorizando párrafos
  * los envíos de archivos usan las API de carga de Slack y pueden incluir respuestas en hilos (`thread_ts`)
  * el límite de medios salientes sigue `channels.slack.mediaMaxMb` cuando está configurado; de lo contrario, los envíos del canal usan los valores predeterminados por tipo MIME del canal de medios

Destinos de entrega

Destinos explícitos preferidos:

  * `user:<id>` para DM
  * `channel:<id>` para canales


Los DM de Slack de solo texto/bloques pueden publicar directamente en ID de usuario; las cargas de archivos y los envíos en hilos abren primero el DM mediante las API de conversación de Slack porque esas rutas requieren un ID de conversación concreto.

## Comandos y comportamiento de barra diagonal

Los comandos de barra diagonal aparecen en Slack como un único comando configurado o como varios comandos nativos. Configura `channels.slack.slashCommand` para cambiar los valores predeterminados del comando:

  * `enabled: false`
  * `name: "openclaw"`
  * `sessionPrefix: "slack:slash"`
  * `ephemeral: true`

txtCopy code
[code]
    /openclaw /help
[/code]

Los comandos nativos requieren ajustes de manifiesto adicionales en tu aplicación de Slack y se habilitan con `channels.slack.commands.native: true` o `commands.native: true` en configuraciones globales.

  * El modo automático de comandos nativos está **desactivado** para Slack, por lo que `commands.native: "auto"` no habilita los comandos nativos de Slack.

txtCopy code
[code]
    /help
[/code]

Los menús de argumentos nativos usan una estrategia de renderizado adaptable que muestra un modal de confirmación antes de despachar un valor de opción seleccionado:

  * hasta 5 opciones: bloques de botones
  * 6-100 opciones: menú de selección estática
  * más de 100 opciones: selección externa con filtrado asíncrono de opciones cuando hay manejadores de opciones de interactividad disponibles
  * límites de Slack excedidos: los valores de opción codificados recurren a botones

txtCopy code
[code]
    /think
[/code]

Las sesiones de barra diagonal usan claves aisladas como `agent:<agentId>:slack:slash:<userId>` y siguen enrutando las ejecuciones de comandos a la sesión de conversación de destino mediante `CommandTargetSessionKey`.

## Respuestas interactivas

Slack puede renderizar controles de respuesta interactiva creados por agentes, pero esta característica está deshabilitada de forma predeterminada.

Habilítala globalmente:

json5Copy code
[code]
    {  channels: {    slack: {      capabilities: {        interactiveReplies: true,      },    },  },}
[/code]

O habilítala solo para una cuenta de Slack:

json5Copy code
[code]
    {  channels: {    slack: {      accounts: {        ops: {          capabilities: {            interactiveReplies: true,          },        },      },    },  },}
[/code]

Cuando está habilitada, los agentes pueden emitir directivas de respuesta solo para Slack:

  * `[[slack_buttons: Approve:approve, Reject:reject]]`
  * `[[slack_select: Choose a target | Canary:canary, Production:production]]`


Estas directivas se compilan en Slack Block Kit y enrutan los clics o selecciones de vuelta a través de la ruta existente de eventos de interacción de Slack.

Notas:

  * Esta es una interfaz de usuario específica de Slack. Otros canales no traducen directivas de Slack Block Kit a sus propios sistemas de botones.
  * Los valores de callback interactivos son tokens opacos generados por OpenClaw, no valores sin procesar creados por agentes.
  * Si los bloques interactivos generados superaran los límites de Slack Block Kit, OpenClaw recurre a la respuesta de texto original en lugar de enviar una carga útil de bloques no válida.


## Aprobaciones de exec en Slack

Slack puede actuar como cliente de aprobación nativo con botones e interacciones interactivas, en lugar de recurrir a la Web UI o la terminal.

  * Las aprobaciones de exec usan `channels.slack.execApprovals.*` para el enrutamiento nativo de DM/canal.
  * Las aprobaciones de Plugin aún pueden resolverse mediante la misma superficie de botones nativa de Slack cuando la solicitud ya llega a Slack y el tipo de ID de aprobación es `plugin:`.
  * La autorización de aprobadores se sigue aplicando: solo los usuarios identificados como aprobadores pueden aprobar o denegar solicitudes mediante Slack.


Esto usa la misma superficie compartida de botones de aprobación que otros canales. Cuando `interactivity` está habilitado en los ajustes de tu aplicación de Slack, los prompts de aprobación se renderizan como botones de Block Kit directamente en la conversación. Cuando esos botones están presentes, son la UX de aprobación principal; OpenClaw solo debe incluir un comando manual `/approve` cuando el resultado de la herramienta indique que las aprobaciones por chat no están disponibles o que la aprobación manual es la única ruta.

Ruta de configuración:

  * `channels.slack.execApprovals.enabled`
  * `channels.slack.execApprovals.approvers` (opcional; recurre a `commands.ownerAllowFrom` cuando sea posible)
  * `channels.slack.execApprovals.target` (`dm` | `channel` | `both`, predeterminado: `dm`)
  * `agentFilter`, `sessionFilter`


Slack habilita automáticamente las aprobaciones de exec nativas cuando `enabled` no está definido o es `"auto"` y se resuelve al menos un aprobador. Establece `enabled: false` para deshabilitar explícitamente Slack como cliente de aprobación nativo. Establece `enabled: true` para forzar las aprobaciones nativas cuando se resuelven aprobadores.

Comportamiento predeterminado sin configuración explícita de aprobación de exec de Slack:

json5Copy code
[code]
    {  commands: {    ownerAllowFrom: ["slack:U12345678"],  },}
[/code]

La configuración nativa de Slack explícita solo es necesaria cuando quieres sobrescribir aprobadores, agregar filtros u optar por la entrega en el chat de origen:

json5Copy code
[code]
    {  channels: {    slack: {      execApprovals: {        enabled: true,        approvers: ["U12345678"],        target: "both",      },    },  },}
[/code]

El reenvío compartido de `approvals.exec` es independiente. Úsalo solo cuando los prompts de aprobación de exec también deban enrutarse a otros chats o destinos explícitos fuera de banda. El reenvío compartido de `approvals.plugin` también es independiente; los botones nativos de Slack aún pueden resolver aprobaciones de Plugin cuando esas solicitudes ya llegan a Slack.

`/approve` en el mismo chat también funciona en canales y DM de Slack que ya admiten comandos. Consulta [Aprobaciones de exec](</es/tools/exec-approvals>) para ver el modelo completo de reenvío de aprobaciones.

## Eventos y comportamiento operativo

  * Las ediciones/eliminaciones de mensajes se asignan a eventos del sistema.
  * Las difusiones de hilo (respuestas de hilo con "Also send to channel") se procesan como mensajes de usuario normales.
  * Los eventos de agregar/eliminar reacción se asignan a eventos del sistema.
  * Los eventos de unión/salida de miembros, creación/cambio de nombre de canal y agregar/eliminar fijación se asignan a eventos del sistema.
  * `channel_id_changed` puede migrar claves de configuración de canal cuando `configWrites` está habilitado.
  * Los metadatos de tema/propósito del canal se tratan como contexto no confiable y pueden inyectarse en el contexto de enrutamiento.
  * El iniciador del hilo y la inicialización del contexto de historial inicial del hilo se filtran mediante listas de permitidos de remitentes configuradas cuando corresponda.
  * Las acciones de bloque y las interacciones modales emiten eventos del sistema estructurados `Slack interaction: ...` con campos de carga útil enriquecidos: 
    * acciones de bloque: valores seleccionados, etiquetas, valores de selector y metadatos `workflow_*`
    * eventos modales `view_submission` y `view_closed` con metadatos de canal enrutado y entradas de formulario


## Referencia de configuración

Referencia principal: [Referencia de configuración - Slack](</es/gateway/config-channels#slack>).

Campos de Slack de alta señal

  * modo/autenticación: `mode`, `botToken`, `appToken`, `signingSecret`, `webhookPath`, `accounts.*`
  * acceso a DM: `dm.enabled`, `dmPolicy`, `allowFrom` (heredado: `dm.policy`, `dm.allowFrom`), `dm.groupEnabled`, `dm.groupChannels`
  * alternancia de compatibilidad: `dangerouslyAllowNameMatching` (break-glass; mantener desactivado salvo que sea necesario)
  * acceso a canales: `groupPolicy`, `channels.*`, `channels.*.users`, `channels.*.requireMention`
  * hilos/historial: `replyToMode`, `replyToModeByChatType`, `thread.*`, `historyLimit`, `dmHistoryLimit`, `dms.*.historyLimit`
  * entrega: `textChunkLimit`, `chunkMode`, `mediaMaxMb`, `streaming`, `streaming.nativeTransport`, `streaming.preview.toolProgress`
  * despliegues de vista previa: `unfurlLinks`, `unfurlMedia` para el control de vista previa de enlaces/medios de `chat.postMessage`
  * operaciones/características: `configWrites`, `commands.native`, `slashCommand.*`, `actions.*`, `userToken`, `userTokenReadOnly`


## Solución de problemas

No hay respuestas en canales

Comprueba, en orden:

  * `groupPolicy`
  * lista de permitidos de canales (`channels.slack.channels`) — **las claves deben ser ID de canal** (`C12345678`), no nombres (`#channel-name`). Las claves basadas en nombre fallan silenciosamente con `groupPolicy: "allowlist"` porque el enrutamiento de canales prioriza los ID de forma predeterminada. Para encontrar un ID: haz clic derecho en el canal en Slack → **Copy link** — el valor `C...` al final de la URL es el ID del canal.
  * `requireMention`
  * lista de permitidos `users` por canal


Comandos útiles:

bashCopy code
[code]
    openclaw channels status --probeopenclaw logs --followopenclaw doctor
[/code]

Mensajes de DM ignorados

Comprueba:

  * `channels.slack.dm.enabled`
  * `channels.slack.dmPolicy` (o el heredado `channels.slack.dm.policy`)
  * aprobaciones de emparejamiento / entradas de lista de permitidos
  * eventos de DM de Slack Assistant: los registros detallados que mencionan `drop message_changed` normalmente significan que Slack envió un evento de hilo de Assistant editado sin un remitente humano recuperable en los metadatos del mensaje

bashCopy code
[code]
    openclaw pairing list slack
[/code]

Socket mode no conecta

Valida los tokens de bot y app, y la habilitación de Socket Mode en los ajustes de la aplicación de Slack.

Si `openclaw channels status --probe --json` muestra `botTokenStatus` o `appTokenStatus: "configured_unavailable"`, la cuenta de Slack está configurada, pero el tiempo de ejecución actual no pudo resolver el valor respaldado por SecretRef.

Modo HTTP no recibe eventos

Valida:

  * secreto de firma
  * ruta del webhook
  * URLs de solicitud de Slack (Events + Interactivity + Slash Commands)
  * `webhookPath` único por cuenta HTTP


Si `signingSecretStatus: "configured_unavailable"` aparece en las instantáneas de la cuenta, la cuenta HTTP está configurada, pero el runtime actual no pudo resolver el secreto de firma respaldado por SecretRef.

Los comandos nativos/slash no se activan

Verifica si pretendías usar:

  * modo de comandos nativos (`channels.slack.commands.native: true`) con comandos slash coincidentes registrados en Slack
  * o modo de comando slash único (`channels.slack.slashCommand.enabled: true`)


Comprueba también `commands.useAccessGroups` y las listas de permitidos de canales/usuarios.

## Referencia de visión para adjuntos

Slack puede adjuntar medios descargados al turno del agente cuando las descargas de archivos de Slack se realizan correctamente y los límites de tamaño lo permiten. Los archivos de imagen pueden pasarse por la ruta de comprensión de medios o directamente a un modelo de respuesta compatible con visión; otros archivos se conservan como contexto de archivo descargable en lugar de tratarse como entrada de imagen.

### Tipos de medios compatibles

Tipo de medio | Origen | Comportamiento actual | Notas  
---|---|---|---  
Imágenes JPEG / PNG / GIF / WebP | URL de archivo de Slack | Descargadas y adjuntadas al turno para manejo compatible con visión | Límite por archivo: `channels.slack.mediaMaxMb` (predeterminado 20 MB)  
Archivos PDF | URL de archivo de Slack | Descargados y expuestos como contexto de archivo para herramientas como `download-file` o `pdf` | La entrada de Slack no convierte los PDF automáticamente en entrada de visión de imagen  
Otros archivos | URL de archivo de Slack | Descargados cuando es posible y expuestos como contexto de archivo | Los archivos binarios no se tratan como entrada de imagen  
Respuestas de hilo | Archivos del mensaje inicial del hilo | Los archivos del mensaje raíz pueden hidratarse como contexto cuando la respuesta no tiene medios directos | Los mensajes iniciales solo con archivos usan un marcador de posición de adjunto  
Mensajes con varias imágenes | Varios archivos de Slack | Cada archivo se evalúa de forma independiente | El procesamiento de Slack está limitado a ocho archivos por mensaje  
  
### Canalización de entrada

Cuando llega un mensaje de Slack con archivos adjuntos:

  1. OpenClaw descarga el archivo desde la URL privada de Slack usando el token del bot (`xoxb-...`).
  2. El archivo se escribe en el almacén de medios si la descarga se completa correctamente.
  3. Las rutas de medios descargados y los tipos de contenido se agregan al contexto de entrada.
  4. Las rutas de modelos/herramientas compatibles con imágenes pueden usar adjuntos de imagen de ese contexto.
  5. Los archivos que no son imágenes permanecen disponibles como metadatos de archivo o referencias de medios para las herramientas que pueden manejarlos.


### Herencia de adjuntos del mensaje raíz del hilo

Cuando llega un mensaje en un hilo (tiene un padre `thread_ts`):

  * Si la respuesta en sí no tiene medios directos y el mensaje raíz incluido tiene archivos, Slack puede hidratar los archivos raíz como contexto del inicio del hilo.
  * Los adjuntos directos de la respuesta tienen prioridad sobre los adjuntos del mensaje raíz.
  * Un mensaje raíz que solo tiene archivos y no texto se representa con un marcador de posición de adjunto para que el mecanismo de respaldo aún pueda incluir sus archivos.


### Manejo de varios adjuntos

Cuando un solo mensaje de Slack contiene varios archivos adjuntos:

  * Cada adjunto se procesa de forma independiente mediante la canalización de medios.
  * Las referencias de medios descargados se agregan al contexto del mensaje.
  * El orden de procesamiento sigue el orden de archivos de Slack en la carga útil del evento.
  * Un fallo en la descarga de un adjunto no bloquea los demás.


### Límites de tamaño, descarga y modelo

  * **Límite de tamaño** : Predeterminado de 20 MB por archivo. Configurable mediante `channels.slack.mediaMaxMb`.
  * **Fallos de descarga** : Los archivos que Slack no puede servir, las URLs expiradas, los archivos inaccesibles, los archivos demasiado grandes y las respuestas HTML de autenticación/inicio de sesión de Slack se omiten en lugar de notificarse como formatos no compatibles.
  * **Modelo de visión** : El análisis de imágenes usa el modelo de respuesta activo cuando admite visión, o el modelo de imagen configurado en `agents.defaults.imageModel`.


### Límites conocidos

Escenario | Comportamiento actual | Solución alternativa  
---|---|---  
URL de archivo de Slack expirada | Archivo omitido; no se muestra ningún error | Vuelve a subir el archivo en Slack  
Modelo de visión no configurado | Los adjuntos de imagen se almacenan como referencias de medios, pero no se analizan como imágenes | Configura `agents.defaults.imageModel` o usa un modelo de respuesta compatible con visión  
Imágenes muy grandes (> 20 MB de forma predeterminada) | Omitidas según el límite de tamaño | Aumenta `channels.slack.mediaMaxMb` si Slack lo permite  
Adjuntos reenviados/compartidos | El texto y los medios de imagen/archivo alojados en Slack se manejan en modo de mejor esfuerzo | Vuelve a compartirlos directamente en el hilo de OpenClaw  
Adjuntos PDF | Almacenados como contexto de archivo/medios, no enrutados automáticamente mediante visión de imagen | Usa `download-file` para metadatos de archivo o la herramienta `pdf` para análisis de PDF  
  
### Documentación relacionada

  * [Canalización de comprensión de medios](</es/nodes/media-understanding>)
  * [Herramienta PDF](</es/tools/pdf>)
  * Epic: [#51349](<https://github.com/openclaw/openclaw/issues/51349>) — habilitación de visión para adjuntos de Slack
  * Pruebas de regresión: [#51353](<https://github.com/openclaw/openclaw/issues/51353>)
  * Verificación en vivo: [#51354](<https://github.com/openclaw/openclaw/issues/51354>)


## Relacionado

[**Emparejamiento** Empareja un usuario de Slack con el gateway. ](</es/channels/pairing>) [**Grupos** Comportamiento de canales y mensajes directos de grupo. ](</es/channels/groups>) [**Enrutamiento de canales** Enruta mensajes entrantes a agentes. ](</es/channels/channel-routing>) [**Seguridad** Modelo de amenazas y endurecimiento. ](</es/gateway/security>) [**Configuración** Diseño y precedencia de configuración. ](</es/gateway/configuration>) [**Comandos slash** Catálogo y comportamiento de comandos. ](</es/tools/slash-commands>)

Was this useful?YesNo