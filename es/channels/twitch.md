---
title: Twitch
source_url: https://docs.openclaw.ai/es/channels/twitch
scraped_at: 2026-05-25
---

Compatibilidad con el chat de Twitch mediante conexión IRC. OpenClaw se conecta como un usuario de Twitch (cuenta de bot) para recibir y enviar mensajes en canales.

## Plugin incluido

Si usas una compilación antigua o una instalación personalizada que excluye Twitch, instala directamente el paquete npm:

### npm registry

bashCopy code
[code]
    openclaw plugins install @openclaw/twitch
[/code]

### Local checkout

bashCopy code
[code]
    openclaw plugins install ./path/to/local/twitch-plugin
[/code]

Usa el paquete sin versión para seguir la etiqueta de versión oficial actual. Fija una versión exacta solo cuando necesites una instalación reproducible.

Detalles: [Plugins](</es/tools/plugin>)

## Configuración rápida (principiante)

* ### Ensure plugin is available

Las versiones empaquetadas actuales de OpenClaw ya lo incluyen. Las instalaciones antiguas o personalizadas pueden agregarlo manualmente con los comandos anteriores.

* ### Create a Twitch bot account

Crea una cuenta de Twitch dedicada para el bot (o usa una cuenta existente).

* ### Generate credentials

Usa [Twitch Token Generator](<https://twitchtokengenerator.com/>):

  * Selecciona **Bot Token**
  * Verifica que los alcances `chat:read` y `chat:write` estén seleccionados
  * Copia el **Client ID** y el **Access Token**


* ### Find your Twitch user ID

Usa <https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/> para convertir un nombre de usuario en un ID de usuario de Twitch.

* ### Configure the token

  * Env: `OPENCLAW_TWITCH_ACCESS_TOKEN=...` (solo cuenta predeterminada)
  * O configuración: `channels.twitch.accessToken`


Si ambos están definidos, la configuración tiene prioridad (la alternativa de env es solo para la cuenta predeterminada).

* ### Start the gateway

Inicia el Gateway con el canal configurado.

Configuración mínima:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw", // Bot's Twitch account      accessToken: "oauth:abc123...", // OAuth Access Token (or use OPENCLAW_TWITCH_ACCESS_TOKEN env var)      clientId: "xyz789...", // Client ID from Token Generator      channel: "vevisk", // Which Twitch channel's chat to join (required)      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only - get it from https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/    },  },}
[/code]

## Qué es

  * Un canal de Twitch propiedad del Gateway.
  * Enrutamiento determinista: las respuestas siempre vuelven a Twitch.
  * Cada cuenta se asigna a una clave de sesión aislada `agent:<agentId>:twitch:<accountName>`.
  * `username` es la cuenta del bot (quien se autentica), `channel` es la sala de chat a la que se une.


## Configuración (detallada)

### Generar credenciales

Usa [Twitch Token Generator](<https://twitchtokengenerator.com/>):

  * Selecciona **Bot Token**
  * Verifica que los alcances `chat:read` y `chat:write` estén seleccionados
  * Copia el **Client ID** y el **Access Token**


### Configurar el bot

### Env var (default account only)

bashCopy code
[code]
    OPENCLAW_TWITCH_ACCESS_TOKEN=oauth:abc123...
[/code]

### Config

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",    },  },}
[/code]

Si tanto env como la configuración están definidos, la configuración tiene prioridad.

### Control de acceso (recomendado)

json5Copy code
[code]
    {  channels: {    twitch: {      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only    },  },}
[/code]

Prefiere `allowFrom` para una lista de permitidos estricta. Usa `allowedRoles` en su lugar si quieres acceso basado en roles.

**Roles disponibles:** `"moderator"`, `"owner"`, `"vip"`, `"subscriber"`, `"all"`.

## Actualización de token (opcional)

Los tokens de [Twitch Token Generator](<https://twitchtokengenerator.com/>) no se pueden actualizar automáticamente; regénéralos cuando caduquen.

Para la actualización automática de tokens, crea tu propia aplicación de Twitch en [Twitch Developer Console](<https://dev.twitch.tv/console>) y agrégala a la configuración:

json5Copy code
[code]
    {  channels: {    twitch: {      clientSecret: "your_client_secret",      refreshToken: "your_refresh_token",    },  },}
[/code]

El bot actualiza automáticamente los tokens antes de que caduquen y registra los eventos de actualización.

## Compatibilidad con varias cuentas

Usa `channels.twitch.accounts` con tokens por cuenta. Consulta [Configuración](</es/gateway/configuration>) para ver el patrón compartido.

Ejemplo (una cuenta de bot en dos canales):

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        channel1: {          username: "openclaw",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "vevisk",        },        channel2: {          username: "openclaw",          accessToken: "oauth:def456...",          clientId: "uvw012...",          channel: "secondchannel",        },      },    },  },}
[/code]

## Control de acceso

### User ID allowlist (most secure)

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowFrom: ["123456789", "987654321"],        },      },    },  },}
[/code]

### Role-based

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowedRoles: ["moderator", "vip"],        },      },    },  },}
[/code]

`allowFrom` es una lista de permitidos estricta. Cuando está definida, solo se permiten esos IDs de usuario. Si quieres acceso basado en roles, deja `allowFrom` sin definir y configura `allowedRoles` en su lugar.

### Disable @mention requirement

De forma predeterminada, `requireMention` es `true`. Para desactivarlo y responder a todos los mensajes:

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          requireMention: false,        },      },    },  },}
[/code]

## Solución de problemas

Primero, ejecuta comandos de diagnóstico:

bashCopy code
[code]
    openclaw doctoropenclaw channels status --probe
[/code]

Bot does not respond to messages

  * **Revisa el control de acceso:** Asegúrate de que tu ID de usuario esté en `allowFrom`, o elimina temporalmente `allowFrom` y define `allowedRoles: ["all"]` para probar.
  * **Comprueba que el bot esté en el canal:** El bot debe unirse al canal especificado en `channel`.

Token issues

"Failed to connect" o errores de autenticación:

  * Verifica que `accessToken` sea el valor del token de acceso OAuth (normalmente empieza con el prefijo `oauth:`)
  * Comprueba que el token tenga los alcances `chat:read` y `chat:write`
  * Si usas actualización de tokens, verifica que `clientSecret` y `refreshToken` estén definidos

Token refresh not working

Revisa los registros para ver eventos de actualización:

CodeCopy code
[code]
    Using env token source for mybotAccess token refreshed for user 123456 (expires in 14400s)
[/code]

Si ves "token refresh disabled (no refresh token)":

  * Asegúrate de que se proporcione `clientSecret`
  * Asegúrate de que se proporcione `refreshToken`


## Configuración

### Configuración de cuenta

Nombre de usuario del bot.

Token de acceso OAuth con `chat:read` y `chat:write`.

Client ID de Twitch (desde Token Generator o tu aplicación).

Canal al que unirse.

Habilita esta cuenta.

Opcional: para actualización automática de tokens.

Opcional: para actualización automática de tokens.

Caducidad del token en segundos.

Marca de tiempo de obtención del token.

Lista de permitidos de IDs de usuario.

Requiere @mención.

### Opciones del proveedor

  * `channels.twitch.enabled` \- Habilita/deshabilita el inicio del canal
  * `channels.twitch.username` \- Nombre de usuario del bot (configuración simplificada de cuenta única)
  * `channels.twitch.accessToken` \- Token de acceso OAuth (configuración simplificada de cuenta única)
  * `channels.twitch.clientId` \- Client ID de Twitch (configuración simplificada de cuenta única)
  * `channels.twitch.channel` \- Canal al que unirse (configuración simplificada de cuenta única)
  * `channels.twitch.accounts.<accountName>` \- Configuración de varias cuentas (todos los campos de cuenta anteriores)


Ejemplo completo:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",      clientSecret: "secret123...",      refreshToken: "refresh456...",      allowFrom: ["123456789"],      allowedRoles: ["moderator", "vip"],      accounts: {        default: {          username: "mybot",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "your_channel",          enabled: true,          clientSecret: "secret123...",          refreshToken: "refresh456...",          expiresIn: 14400,          obtainmentTimestamp: 1706092800000,          allowFrom: ["123456789", "987654321"],          allowedRoles: ["moderator"],        },      },    },  },}
[/code]

## Acciones de herramienta

El agente puede llamar a `twitch` con la acción:

  * `send` \- Envía un mensaje a un canal


Ejemplo:

json5Copy code
[code]
    {  action: "twitch",  params: {    message: "Hello Twitch!",    to: "#mychannel",  },}
[/code]

## Seguridad y operaciones

  * **Trata los tokens como contraseñas** — Nunca confirmes tokens en git.
  * **Usa actualización automática de tokens** para bots de larga duración.
  * **Usa listas de permitidos de IDs de usuario** en lugar de nombres de usuario para el control de acceso.
  * **Supervisa los registros** para ver eventos de actualización de tokens y el estado de conexión.
  * **Limita al mínimo los alcances de los tokens** — Solicita solo `chat:read` y `chat:write`.
  * **Si te bloqueas** : Reinicia el Gateway después de confirmar que ningún otro proceso posee la sesión.


## Límites

  * **500 caracteres** por mensaje (dividido automáticamente en fragmentos en límites de palabra).
  * Markdown se elimina antes de fragmentar.
  * Sin limitación de velocidad (usa los límites de velocidad integrados de Twitch).


## Relacionado

  * [Enrutamiento de canales](</es/channels/channel-routing>) — enrutamiento de sesión para mensajes
  * [Descripción general de canales](</es/channels>) — todos los canales compatibles
  * [Grupos](</es/channels/groups>) — comportamiento de chat grupal y control de menciones
  * [Emparejamiento](</es/channels/pairing>) — autenticación por DM y flujo de emparejamiento
  * [Seguridad](</es/gateway/security>) — modelo de acceso y endurecimiento


Was this useful?YesNo