---
title: bot de QQ
source_url: https://docs.openclaw.ai/es/channels/qqbot
scraped_at: 2026-05-25
---

QQ Bot conecta con OpenClaw mediante la API oficial de QQ Bot (gateway WebSocket). El plugin admite chat privado C2C, @mensajes de grupo y mensajes de canales de guild con multimedia enriquecida (imágenes, voz, video, archivos).

Estado: plugin descargable. Se admiten mensajes directos, chats de grupo, canales de guild y multimedia. No se admiten reacciones ni hilos.

## Instalación

Instala QQ Bot antes de la configuración:

bashCopy code
[code]
    openclaw plugins install @openclaw/qqbot
[/code]

## Configuración inicial

  1. Ve a la [QQ Open Platform](<https://q.qq.com/>) y escanea el código QR con tu QQ del teléfono para registrarte / iniciar sesión.
  2. Haz clic en **Crear bot** para crear un nuevo bot de QQ.
  3. Busca **AppID** y **AppSecret** en la página de ajustes del bot y cópialos.


> AppSecret no se almacena en texto sin formato; si sales de la página sin guardarlo, tendrás que regenerar uno nuevo.

  4. Añade el canal:

bashCopy code
[code]
    openclaw channels add --channel qqbot --token "AppID:AppSecret"
[/code]

  5. Reinicia el Gateway.


Rutas de configuración interactiva:

bashCopy code
[code]
    openclaw channels addopenclaw configure --section channels
[/code]

## Configurar

Configuración mínima:

json5Copy code
[code]
    {  channels: {    qqbot: {      enabled: true,      appId: "YOUR_APP_ID",      clientSecret: "YOUR_APP_SECRET",    },  },}
[/code]

Variables de entorno de cuenta predeterminada:

  * `QQBOT_APP_ID`
  * `QQBOT_CLIENT_SECRET`


AppSecret respaldado por archivo:

json5Copy code
[code]
    {  channels: {    qqbot: {      enabled: true,      appId: "YOUR_APP_ID",      clientSecretFile: "/path/to/qqbot-secret.txt",    },  },}
[/code]

AppSecret de Env SecretRef:

json5Copy code
[code]
    {  channels: {    qqbot: {      enabled: true,      appId: "YOUR_APP_ID",      clientSecret: { source: "env", provider: "default", id: "QQBOT_CLIENT_SECRET" },    },  },}
[/code]

Notas:

  * La alternativa de entorno se aplica solo a la cuenta predeterminada de QQ Bot.
  * `openclaw channels add --channel qqbot --token-file ...` proporciona solo el AppSecret; el AppID ya debe estar establecido en la configuración o en `QQBOT_APP_ID`.
  * `clientSecret` también acepta entrada SecretRef, no solo una cadena de texto sin formato.
  * Las cadenas de marcador heredadas `secretref:/...` no son valores `clientSecret` válidos; usa objetos SecretRef estructurados como en el ejemplo anterior.


### Configuración de varias cuentas

Ejecuta varios bots de QQ bajo una sola instancia de OpenClaw:

json5Copy code
[code]
    {  channels: {    qqbot: {      enabled: true,      appId: "111111111",      clientSecret: "secret-of-bot-1",      accounts: {        bot2: {          enabled: true,          appId: "222222222",          clientSecret: "secret-of-bot-2",        },      },    },  },}
[/code]

Cada cuenta lanza su propia conexión WebSocket y mantiene una caché de tokens independiente (aislada por `appId`).

Añade un segundo bot mediante la CLI:

bashCopy code
[code]
    openclaw channels add --channel qqbot --account bot2 --token "222222222:secret-of-bot-2"
[/code]

### Chats de grupo

La compatibilidad de QQ Bot con chats de grupo usa OpenIDs de grupos de QQ, no nombres visibles. Añade el bot a un grupo y luego menciónalo o configura el grupo para ejecutarse sin una mención.

json5Copy code
[code]
    {  channels: {    qqbot: {      groupPolicy: "allowlist",      groupAllowFrom: ["member_openid"],      groups: {        "*": {          requireMention: true,          historyLimit: 50,          toolPolicy: "restricted",        },        GROUP_OPENID: {          name: "Release room",          requireMention: false,          ignoreOtherMentions: true,          historyLimit: 20,          prompt: "Keep replies short and operational.",        },      },    },  },}
[/code]

`groups["*"]` establece valores predeterminados para cada grupo, y una entrada concreta `groups.GROUP_OPENID` reemplaza esos valores predeterminados para un grupo. Los ajustes de grupo incluyen:

  * `requireMention`: requiere una @mención antes de que el bot responda. Valor predeterminado: `true`.
  * `ignoreOtherMentions`: descarta mensajes que mencionan a otra persona pero no al bot.
  * `historyLimit`: conserva mensajes recientes de grupo sin mención como contexto para el siguiente turno mencionado. Usa `0` para desactivar.
  * `toolPolicy`: `full`, `restricted` o `none` para herramientas con ámbito de grupo.
  * `name`: etiqueta descriptiva usada en registros y contexto de grupo.
  * `prompt`: prompt de comportamiento por grupo añadido al contexto del agente.


Los modos de activación son `mention` y `always`. `requireMention: true` se asigna a `mention`; `requireMention: false` se asigna a `always`. Una anulación de activación a nivel de sesión, cuando existe, tiene prioridad sobre la configuración.

La cola entrante es por interlocutor. Los interlocutores de grupo obtienen un límite de cola mayor, mantienen los mensajes humanos por delante de la charla escrita por bots cuando se llena, y fusionan ráfagas de mensajes normales de grupo en un turno atribuido. Los comandos con barra diagonal siguen ejecutándose uno por uno.

### Voz (STT / TTS)

STT y TTS admiten configuración de dos niveles con alternativa por prioridad:

Ajuste | Específico del plugin | Alternativa del framework  
---|---|---  
STT | `channels.qqbot.stt` | `tools.media.audio.models[0]`  
TTS | `channels.qqbot.tts`, `channels.qqbot.accounts.<id>.tts` | `messages.tts`  
json5Copy code
[code]
    {  channels: {    qqbot: {      stt: {        provider: "your-provider",        model: "your-stt-model",      },      tts: {        provider: "your-provider",        model: "your-tts-model",        voice: "your-voice",      },      accounts: {        "qq-main": {          tts: {            providers: {              openai: { voice: "shimmer" },            },          },        },      },    },  },}
[/code]

Establece `enabled: false` en cualquiera de los dos para desactivar. Las anulaciones de TTS a nivel de cuenta usan la misma forma que `messages.tts` y se fusionan en profundidad sobre la configuración de TTS del canal/global.

Los adjuntos de voz entrantes de QQ se exponen a los agentes como metadatos de medios de audio mientras se mantienen los archivos de voz sin procesar fuera de los `MediaPaths` genéricos. Las respuestas de texto sin formato `[[audio_as_voice]]` sintetizan TTS y envían un mensaje de voz nativo de QQ cuando TTS está configurado.

El comportamiento de subida/transcodificación de audio saliente también se puede ajustar con `channels.qqbot.audioFormatPolicy`:

  * `sttDirectFormats`
  * `uploadDirectFormats`
  * `transcodeEnabled`


## Formatos de destino

Formato | Descripción  
---|---  
`qqbot:c2c:OPENID` | Chat privado (C2C)  
`qqbot:group:GROUP_OPENID` | Chat de grupo  
`qqbot:channel:CHANNEL_ID` | Canal de guild  
  
> Cada bot tiene su propio conjunto de OpenIDs de usuario. Un OpenID recibido por el Bot A **no puede** usarse para enviar mensajes mediante el Bot B.

## Comandos con barra diagonal

Comandos integrados interceptados antes de la cola de IA:

Comando | Descripción  
---|---  
`/bot-ping` | Prueba de latencia  
`/bot-version` | Muestra la versión del framework de OpenClaw  
`/bot-help` | Lista todos los comandos  
`/bot-me` | Muestra el ID de usuario QQ del remitente (openid) para configurar `allowFrom`/`groupAllowFrom`  
`/bot-upgrade` | Muestra el enlace de la guía de actualización de QQBot  
`/bot-logs` | Exporta registros recientes del gateway como archivo  
`/bot-approve` | Aprueba una acción pendiente de QQ Bot (por ejemplo, confirmar una subida C2C o de grupo) mediante el flujo nativo.  
  
Añade `?` a cualquier comando para obtener ayuda de uso (por ejemplo `/bot-upgrade ?`).

Los comandos de administrador (`/bot-me`, `/bot-upgrade`, `/bot-logs`, `/bot-clear-storage`, `/bot-streaming`, `/bot-approve`) son solo para mensajes directos y requieren que el openid del remitente esté en una lista explícita `allowFrom` sin comodines. Un comodín `allowFrom: ["*"]` permite chatear, pero no concede acceso a comandos de administrador. Los mensajes de grupo se comparan primero con `groupAllowFrom` y recurren a `allowFrom`. Ejecutar un comando de administrador en un grupo devuelve una indicación en lugar de descartarlo silenciosamente.

## Arquitectura del motor

QQ Bot se distribuye como un motor autónomo dentro del plugin:

  * Cada cuenta posee una pila de recursos aislada (conexión WebSocket, cliente de API, caché de tokens, raíz de almacenamiento de medios) identificada por `appId`. Las cuentas nunca comparten estado entrante/saliente.
  * El registrador de varias cuentas etiqueta las líneas de registro con la cuenta propietaria para que los diagnósticos sigan siendo separables cuando ejecutas varios bots bajo un gateway.
  * Las rutas entrantes, salientes y de puente del gateway comparten una única raíz de carga útil de medios bajo `~/.openclaw/media`, por lo que las subidas, descargas y cachés de transcodificación quedan bajo un único directorio protegido en lugar de un árbol por subsistema.
  * La entrega de multimedia enriquecida pasa por una única ruta `sendMedia` para destinos C2C y de grupo. Los archivos locales y búferes por encima del umbral de archivo grande usan los endpoints de subida por fragmentos de QQ, mientras que las cargas útiles más pequeñas usan la API de medios de una sola operación.
  * Las credenciales pueden respaldarse y restaurarse como parte de las instantáneas de credenciales estándar de OpenClaw; el motor vuelve a adjuntar la pila de recursos de cada cuenta al restaurar sin requerir un nuevo par de código QR.


## Incorporación con código QR

Como alternativa a pegar `AppID:AppSecret` manualmente, el motor admite un flujo de incorporación con código QR para vincular un QQ Bot con OpenClaw:

  1. Ejecuta la ruta de configuración de QQ Bot (por ejemplo `openclaw channels add --channel qqbot`) y elige el flujo de código QR cuando se solicite.
  2. Escanea el código QR generado con la app del teléfono vinculada al QQ Bot de destino.
  3. Aprueba el emparejamiento en el teléfono. OpenClaw persiste las credenciales devueltas en `credentials/` bajo el ámbito de cuenta correcto.


Las solicitudes de aprobación generadas por el propio bot (por ejemplo, flujos de "¿permitir esta acción?" expuestos por la API de QQ Bot) aparecen como prompts nativos de OpenClaw que puedes aceptar con `/bot-approve` en lugar de responder mediante el cliente QQ sin procesar.

## Solución de problemas

  * **El bot responde "gone to Mars":** las credenciales no están configuradas o el Gateway no se inició.
  * **No hay mensajes entrantes:** verifica que `appId` y `clientSecret` sean correctos, y que el bot esté habilitado en la QQ Open Platform.
  * **Autorrespuestas repetidas:** OpenClaw registra los índices de referencia salientes de QQ como escritos por el bot e ignora eventos entrantes cuyo `msgIdx` actual coincide con esa misma cuenta de bot. Esto evita bucles de eco de la plataforma y a la vez permite que los usuarios citen o respondan a mensajes anteriores del bot.
  * **La configuración con`--token-file` sigue apareciendo como no configurada:** `--token-file` solo establece el AppSecret. Aún necesitas `appId` en la configuración o `QQBOT_APP_ID`.
  * **Los mensajes proactivos no llegan:** QQ puede interceptar mensajes iniciados por el bot si el usuario no ha interactuado recientemente.
  * **La voz no se transcribe:** asegúrate de que STT esté configurado y de que el proveedor esté accesible.


## Relacionado

  * [Emparejamiento](</es/channels/pairing>)
  * [Grupos](</es/channels/groups>)
  * [Solución de problemas de canales](</es/channels/troubleshooting>)


Was this useful?YesNo