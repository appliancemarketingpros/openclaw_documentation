---
title: iMessage
source_url: https://docs.openclaw.ai/es/channels/imessage
scraped_at: 2026-05-25
---

Estado: integración nativa de CLI externa. Gateway inicia `imsg rpc` y se comunica mediante JSON-RPC por stdio (sin demonio/puerto separado). Las acciones avanzadas requieren `imsg launch` y una comprobación correcta de la API privada.

**Private API actions** Respuestas, tapbacks, efectos, adjuntos y gestión de grupos. [**Pairing** Los DM de iMessage usan el modo de emparejamiento de forma predeterminada. ](</es/channels/pairing>) **Remote Mac** Usa un envoltorio SSH cuando el Gateway no se esté ejecutando en el Mac de Messages. [**Configuration reference** Referencia completa de campos de iMessage. ](</es/gateway/config-channels#imessage>)

## Configuración rápida

### Local Mac (fast path)

* ### Install and verify imsg

bashCopy code
[code]
    brew install steipete/tap/imsgimsg rpc --helpimsg launchopenclaw channels status --probe
[/code]

* ### Configure OpenClaw

json5Copy code
[code]
    {channels: {imessage: {enabled: true,cliPath: "/usr/local/bin/imsg",dbPath: "/Users/user/Library/Messages/chat.db",},},}
[/code]

* ### Start gateway

bashCopy code
[code]
    openclaw gateway
[/code]

* ### Approve first DM pairing (default dmPolicy)

bashCopy code
[code]
    openclaw pairing list imessageopenclaw pairing approve imessage &lt;CODE&gt;
[/code]

Las solicitudes de emparejamiento caducan después de 1 hora.

### Remote Mac over SSH

OpenClaw solo requiere un `cliPath` compatible con stdio, por lo que puedes apuntar `cliPath` a un script envoltorio que se conecte por SSH a un Mac remoto y ejecute `imsg`.

bashCopy code
[code]
    #!/usr/bin/env bashexec ssh -T gateway-host imsg "$@"
[/code]

Configuración recomendada cuando los adjuntos están habilitados:

json5Copy code
[code]
    {channels: {imessage: {  enabled: true,  cliPath: "~/.openclaw/scripts/imsg-ssh",  remoteHost: "user@gateway-host", // used for SCP attachment fetches  includeAttachments: true,  // Optional: override allowed attachment roots.  // Defaults include /Users/*/Library/Messages/Attachments  attachmentRoots: ["/Users/*/Library/Messages/Attachments"],  remoteAttachmentRoots: ["/Users/*/Library/Messages/Attachments"],},},}
[/code]

Si `remoteHost` no está configurado, OpenClaw intenta detectarlo automáticamente analizando el script envoltorio SSH. `remoteHost` debe ser `host` o `user@host` (sin espacios ni opciones SSH). OpenClaw usa comprobación estricta de claves de host para SCP, por lo que la clave del host de retransmisión ya debe existir en `~/.ssh/known_hosts`. Las rutas de adjuntos se validan contra las raíces permitidas (`attachmentRoots` / `remoteAttachmentRoots`).

## Requisitos y permisos (macOS)

  * Messages debe tener sesión iniciada en el Mac que ejecuta `imsg`.
  * Se requiere Acceso total al disco para el contexto de proceso que ejecuta OpenClaw/`imsg` (acceso a la base de datos de Messages).
  * Se requiere permiso de Automatización para enviar mensajes mediante Messages.app.
  * Para acciones avanzadas (reaccionar / editar / anular envío / respuesta en hilo / efectos / operaciones de grupo), System Integrity Protection debe estar deshabilitado — consulta Habilitar la API privada de imsg más abajo. El envío/recepción básico de texto y multimedia funciona sin ello.


## Habilitar la API privada de imsg

`imsg` se distribuye en dos modos operativos:

  * **Modo básico** (predeterminado, no requiere cambios en SIP): texto y multimedia salientes mediante `send`, observación/historial entrante, lista de chats. Esto es lo que obtienes de inmediato con una instalación nueva de `brew install steipete/tap/imsg` más los permisos estándar de macOS anteriores.
  * **Modo de API privada** : `imsg` inyecta una dylib auxiliar en `Messages.app` para llamar a funciones internas de `IMCore`. Esto habilita `react`, `edit`, `unsend`, `reply` (en hilo), `sendWithEffect`, `renameGroup`, `setGroupIcon`, `addParticipant`, `removeParticipant`, `leaveGroup`, además de indicadores de escritura y confirmaciones de lectura.


Para acceder a la superficie de acciones avanzadas que documenta esta página del canal, necesitas el modo de API privada. El README de `imsg` es explícito sobre el requisito:

> Las funciones avanzadas como `read`, `typing`, `launch`, envío enriquecido respaldado por bridge, mutación de mensajes y gestión de chats son optativas. Requieren que SIP esté deshabilitado y que se inyecte una dylib auxiliar en `Messages.app`. `imsg launch` se niega a inyectar cuando SIP está habilitado.

La técnica de inyección del auxiliar usa la propia dylib de `imsg` para acceder a las API privadas de Messages. No hay servidor de terceros ni runtime de BlueBubbles en la ruta de iMessage de OpenClaw.

### Configuración

  1. **Instala (o actualiza)`imsg`** en el Mac que ejecuta Messages.app:

bashCopy code
[code]brew install steipete/tap/imsgimsg --versionimsg status --json
[/code]

La salida de `imsg status --json` informa `bridge_version`, `rpc_methods` y `selectors` por método para que puedas ver qué admite la compilación actual antes de empezar.

  2. **Deshabilita System Integrity Protection.** Esto depende de la versión de macOS porque el requisito subyacente de Apple depende del SO y del hardware:

     * **macOS 10.13–10.15 (Sierra–Catalina):** deshabilita Library Validation mediante Terminal, reinicia en Recovery Mode, ejecuta `csrutil disable`, reinicia.
     * **macOS 11+ (Big Sur y posterior), Intel:** Recovery Mode (o Internet Recovery), `csrutil disable`, reinicia.
     * **macOS 11+, Apple Silicon:** secuencia de inicio con el botón de encendido para entrar en Recovery; en versiones recientes de macOS mantén pulsada la tecla **Left Shift** cuando hagas clic en Continue, luego `csrutil disable`. Las configuraciones de máquinas virtuales siguen un flujo separado — toma primero una instantánea de la VM.
     * **macOS 26 / Tahoe:** las políticas de validación de bibliotecas y las comprobaciones de derechos privados de `imagent` se han endurecido aún más; `imsg` puede necesitar una compilación actualizada para mantenerse al día. Si la inyección de `imsg launch` o `selectors` específicos empiezan a devolver falso después de una actualización mayor de macOS, revisa las notas de versión de `imsg` antes de asumir que el paso de SIP se completó correctamente.

Sigue el flujo de Recovery Mode de Apple para tu Mac para deshabilitar SIP antes de ejecutar `imsg launch`.

  3. **Inyecta el auxiliar.** Con SIP deshabilitado y sesión iniciada en Messages.app:

bashCopy code
[code]imsg launch
[/code]

`imsg launch` se niega a inyectar cuando SIP sigue habilitado, por lo que esto también sirve como confirmación de que el paso 2 surtió efecto.

  4. **Verifica el bridge desde OpenClaw:**

bashCopy code
[code]openclaw channels status --probe
[/code]

La entrada de iMessage debe informar `works`, y `imsg status --json | jq '.selectors'` debe mostrar `retractMessagePart: true` más los selectores de edición / escritura / lectura que exponga tu compilación de macOS. La compuerta por método del Plugin de OpenClaw en `actions.ts` solo anuncia acciones cuyo selector subyacente es `true`, por lo que la superficie de acciones que ves en la lista de herramientas del agente refleja lo que el bridge realmente puede hacer en este host.


Si `openclaw channels status --probe` informa que el canal está en `works` pero acciones específicas lanzan "iMessage `<action>` requires the imsg private API bridge" en el momento de despacho, ejecuta `imsg launch` de nuevo — el auxiliar puede dejar de estar activo (reinicio de Messages.app, actualización del SO, etc.) y el estado en caché `available: true` seguirá anunciando acciones hasta que la siguiente comprobación lo actualice.

### Cuando no puedes deshabilitar SIP

Si SIP deshabilitado no es aceptable para tu modelo de amenazas:

  * `imsg` vuelve al modo básico — solo texto + multimedia + recepción.
  * El Plugin de OpenClaw sigue anunciando envío de texto/multimedia y monitoreo entrante; simplemente oculta `react`, `edit`, `unsend`, `reply`, `sendWithEffect` y operaciones de grupo de la superficie de acciones (según la compuerta de capacidad por método).
  * Puedes ejecutar un Mac separado que no sea Apple Silicon (o un Mac bot dedicado) con SIP desactivado para la carga de trabajo de iMessage, mientras mantienes SIP habilitado en tus dispositivos principales. Consulta Usuario macOS bot dedicado (identidad de iMessage separada) más abajo.


## Control de acceso y enrutamiento

### DM policy

`channels.imessage.dmPolicy` controla los mensajes directos:

  * `pairing` (predeterminado)
  * `allowlist`
  * `open` (requiere que `allowFrom` incluya `"*"`)
  * `disabled`


Campo de lista de permitidos: `channels.imessage.allowFrom`.

Las entradas de la lista de permitidos deben identificar a los remitentes: identificadores o grupos estáticos de acceso de remitentes (`accessGroup:<name>`). Usa `channels.imessage.groupAllowFrom` para destinos de chat como `chat_id:*`, `chat_guid:*` o `chat_identifier:*`; usa `channels.imessage.groups` para claves de registro numéricas de `chat_id`.

### Group policy + mentions

`channels.imessage.groupPolicy` controla el manejo de grupos:

  * `allowlist` (predeterminado cuando está configurado)
  * `open`
  * `disabled`


Lista de permitidos de remitentes de grupo: `channels.imessage.groupAllowFrom`.

Las entradas de `groupAllowFrom` también pueden hacer referencia a grupos estáticos de acceso de remitentes (`accessGroup:<name>`).

Respaldo en runtime: si `groupAllowFrom` no está configurado, las comprobaciones de remitente de grupo de iMessage usan `allowFrom`; configura `groupAllowFrom` cuando la admisión de DM y de grupo deba diferir. Nota de runtime: si `channels.imessage` falta por completo, runtime vuelve a `groupPolicy="allowlist"` y registra una advertencia (aunque `channels.defaults.groupPolicy` esté configurado).

Control por menciones para grupos:

  * iMessage no tiene metadatos nativos de menciones
  * la detección de menciones usa patrones regex (`agents.list[].groupChat.mentionPatterns`, alternativa `messages.groupChat.mentionPatterns`)
  * sin patrones configurados, no se puede aplicar el control por menciones


Los comandos de control de remitentes autorizados pueden omitir el control por menciones en grupos.

`systemPrompt` por grupo:

Cada entrada bajo `channels.imessage.groups.*` acepta una cadena opcional `systemPrompt`. El valor se inyecta en el prompt del sistema del agente en cada turno que maneja un mensaje en ese grupo. La resolución refleja la resolución de prompt por grupo usada por `channels.whatsapp.groups`:

  1. **Prompt del sistema específico del grupo** (`groups["<chat_id>"].systemPrompt`): se usa cuando la entrada específica del grupo existe en el mapa **y** su clave `systemPrompt` está definida. Si `systemPrompt` es una cadena vacía (`""`), se suprime el comodín y no se aplica ningún prompt del sistema a ese grupo.
  2. **Prompt del sistema comodín de grupo** (`groups["*"].systemPrompt`): se usa cuando la entrada específica del grupo está totalmente ausente del mapa, o cuando existe pero no define ninguna clave `systemPrompt`.

json5Copy code
[code]
    {  channels: {    imessage: {      groupPolicy: "allowlist",      groupAllowFrom: ["+15555550123"],      groups: {        "*": { systemPrompt: "Use British spelling." },        "8421": {          requireMention: true,          systemPrompt: "This is the on-call rotation chat. Keep replies under 3 sentences.",        },        "9907": {          // explicit suppression: the wildcard "Use British spelling." does not apply here          systemPrompt: "",        },      },    },  },}
[/code]

Los prompts por grupo solo se aplican a mensajes de grupo; los mensajes directos de este canal no se ven afectados.

### Sessions and deterministic replies

  * Los MD usan enrutamiento directo; los grupos usan enrutamiento de grupo.
  * Con `session.dmScope=main` predeterminado, los MD de iMessage se fusionan en la sesión principal del agente.
  * Las sesiones de grupo están aisladas (`agent:<agentId>:imessage:group:<chat_id>`).
  * Las respuestas se enrutan de vuelta a iMessage usando los metadatos de canal/objetivo de origen.


Comportamiento de hilos similares a grupos:

Algunos hilos de iMessage con varios participantes pueden llegar con `is_group=false`. Si ese `chat_id` está configurado explícitamente bajo `channels.imessage.groups`, OpenClaw lo trata como tráfico de grupo (control de grupo + aislamiento de sesión de grupo).

## Enlaces de conversación ACP

Los chats heredados de iMessage también se pueden vincular a sesiones ACP.

Flujo rápido para operadores:

  * Ejecuta `/acp spawn codex --bind here` dentro del MD o chat de grupo permitido.
  * Los mensajes futuros en esa misma conversación de iMessage se enrutan a la sesión ACP generada.
  * `/new` y `/reset` restablecen la misma sesión ACP vinculada en el lugar.
  * `/acp close` cierra la sesión ACP y elimina el enlace.


Se admiten enlaces persistentes configurados mediante entradas de nivel superior `bindings[]` con `type: "acp"` y `match.channel: "imessage"`.

`match.peer.id` puede usar:

  * identificador de MD normalizado como `+15555550123` o `user@example.com`
  * `chat_id:<id>` (recomendado para enlaces de grupo estables)
  * `chat_guid:<guid>`
  * `chat_identifier:<identifier>`


Ejemplo:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "codex",        runtime: {          type: "acp",          acp: { agent: "codex", backend: "acpx", mode: "persistent" },        },      },    ],  },  bindings: [    {      type: "acp",      agentId: "codex",      match: {        channel: "imessage",        accountId: "default",        peer: { kind: "group", id: "chat_id:123" },      },      acp: { label: "codex-group" },    },  ],}
[/code]

Consulta [Agentes ACP](</es/tools/acp-agents>) para ver el comportamiento compartido de los enlaces ACP.

## Patrones de despliegue

Dedicated bot macOS user (separate iMessage identity)

Usa un ID de Apple y un usuario de macOS dedicados para que el tráfico del bot quede aislado de tu perfil personal de Mensajes.

Flujo típico:

  1. Crea/inicia sesión en un usuario de macOS dedicado.
  2. Inicia sesión en Mensajes con el ID de Apple del bot en ese usuario.
  3. Instala `imsg` en ese usuario.
  4. Crea un contenedor SSH para que OpenClaw pueda ejecutar `imsg` en el contexto de ese usuario.
  5. Apunta `channels.imessage.accounts.<id>.cliPath` y `.dbPath` a ese perfil de usuario.


La primera ejecución puede requerir aprobaciones de GUI (Automatización + Acceso total al disco) en esa sesión de usuario del bot.

Remote Mac over Tailscale (example)

Topología común:

  * el Gateway se ejecuta en Linux/VM
  * iMessage + `imsg` se ejecuta en una Mac en tu tailnet
  * el contenedor `cliPath` usa SSH para ejecutar `imsg`
  * `remoteHost` habilita las obtenciones de adjuntos por SCP


Ejemplo:

json5Copy code
[code]
    {  channels: {    imessage: {      enabled: true,      cliPath: "~/.openclaw/scripts/imsg-ssh",      remoteHost: "bot@mac-mini.tailnet-1234.ts.net",      includeAttachments: true,      dbPath: "/Users/bot/Library/Messages/chat.db",    },  },}
[/code]

bashCopy code
[code]
    #!/usr/bin/env bashexec ssh -T bot@mac-mini.tailnet-1234.ts.net imsg "$@"
[/code]

Usa claves SSH para que tanto SSH como SCP sean no interactivos. Asegúrate de que la clave del host sea de confianza primero (por ejemplo, `ssh bot@mac-mini.tailnet-1234.ts.net`) para que se rellene `known_hosts`.

Multi-account pattern

iMessage admite configuración por cuenta bajo `channels.imessage.accounts`.

Cada cuenta puede sobrescribir campos como `cliPath`, `dbPath`, `allowFrom`, `groupPolicy`, `mediaMaxMb`, la configuración del historial y las listas de permitidos de raíces de adjuntos.

## Medios, fragmentación y destinos de entrega

Adjuntos y medios

  * la ingesta de adjuntos entrantes está **desactivada de forma predeterminada** — establece `channels.imessage.includeAttachments: true` para reenviar fotos, notas de voz, videos y otros adjuntos al agente. Con esto desactivado, los iMessages que solo contienen adjuntos se descartan antes de llegar al agente y pueden no producir ninguna línea de registro `Inbound message`.
  * las rutas de adjuntos remotos se pueden obtener mediante SCP cuando `remoteHost` está configurado
  * las rutas de adjuntos deben coincidir con raíces permitidas: 
    * `channels.imessage.attachmentRoots` (local)
    * `channels.imessage.remoteAttachmentRoots` (modo SCP remoto)
    * patrón de raíz predeterminado: `/Users/*/Library/Messages/Attachments`
  * SCP usa comprobación estricta de clave de host (`StrictHostKeyChecking=yes`)
  * el tamaño de medios salientes usa `channels.imessage.mediaMaxMb` (16 MB de forma predeterminada)

Fragmentación saliente

  * límite de fragmento de texto: `channels.imessage.textChunkLimit` (4000 de forma predeterminada)
  * modo de fragmentación: `channels.imessage.chunkMode`
    * `length` (predeterminado)
    * `newline` (división priorizando párrafos)

Formatos de direccionamiento

Destinos explícitos preferidos:

  * `chat_id:123` (recomendado para enrutamiento estable)
  * `chat_guid:...`
  * `chat_identifier:...`


También se admiten destinos de identificador:

  * `imessage:+1555...`
  * `sms:+1555...`
  * `user@example.com`

bashCopy code
[code]
    imsg chats --limit 20
[/code]

## Acciones de API privada

Cuando `imsg launch` está en ejecución y `openclaw channels status --probe` informa `privateApi.available: true`, la herramienta de mensajes puede usar acciones nativas de iMessage además de los envíos de texto normales.

json5Copy code
[code]
    {  channels: {    imessage: {      actions: {        reactions: true,        edit: true,        unsend: true,        reply: true,        sendWithEffect: true,        sendAttachment: true,        renameGroup: true,        setGroupIcon: true,        addParticipant: true,        removeParticipant: true,        leaveGroup: true,      },    },  },}
[/code]

Acciones disponibles

  * **react** : Agrega/elimina tapbacks de iMessage (`messageId`, `emoji`, `remove`). Los tapbacks admitidos corresponden a amor, me gusta, no me gusta, risa, énfasis y pregunta.
  * **reply** : Envía una respuesta en hilo a un mensaje existente (`messageId`, `text` o `message`, más `chatGuid`, `chatId`, `chatIdentifier` o `to`).
  * **sendWithEffect** : Envía texto con un efecto de iMessage (`text` o `message`, `effect` o `effectId`).
  * **edit** : Edita un mensaje enviado en versiones compatibles de macOS/API privada (`messageId`, `text` o `newText`).
  * **unsend** : Retrae un mensaje enviado en versiones compatibles de macOS/API privada (`messageId`).
  * **upload-file** : Envía medios/archivos (`buffer` como base64 o un `media`/`path`/`filePath` hidratado, `filename`, `asVoice` opcional). Alias heredado: `sendAttachment`.
  * **renameGroup** , **setGroupIcon** , **addParticipant** , **removeParticipant** , **leaveGroup** : Gestiona chats grupales cuando el destino actual es una conversación grupal.

ID de mensajes

El contexto entrante de iMessage incluye tanto valores `MessageSid` cortos como GUIDs completos de mensajes cuando están disponibles. Los ID cortos tienen alcance limitado a la caché reciente de respuestas en memoria y se comprueban contra el chat actual antes de usarse. Si un ID corto ha expirado o pertenece a otro chat, vuelve a intentarlo con el `MessageSidFull` completo.

Detección de capacidades

OpenClaw oculta las acciones de API privada solo cuando el estado de la sonda en caché indica que el puente no está disponible. Si el estado es desconocido, las acciones siguen siendo visibles y ejecutan sondas de forma diferida para que la primera acción pueda tener éxito después de `imsg launch` sin una actualización manual de estado por separado.

Confirmaciones de lectura y escritura

Cuando el puente de API privada está activo, los chats entrantes aceptados se marcan como leídos antes del despacho y se muestra una burbuja de escritura al remitente mientras el agente genera la respuesta. Desactiva el marcado de lectura con:

json5Copy code
[code]
    {  channels: {    imessage: {      sendReadReceipts: false,    },  },}
[/code]

Las compilaciones antiguas de `imsg` anteriores a la lista de capacidades por método desactivarán silenciosamente la escritura/lectura; OpenClaw registra una advertencia única por reinicio para que la confirmación faltante sea atribuible.

Tapbacks entrantes

OpenClaw se suscribe a los tapbacks de iMessage y enruta las reacciones aceptadas como eventos del sistema en lugar de texto de mensaje normal, por lo que un tapback de usuario no desencadena un bucle de respuesta ordinario.

El modo de notificación se controla mediante `channels.imessage.reactionNotifications`:

  * `"own"` (predeterminado): notifica solo cuando los usuarios reaccionan a mensajes escritos por el bot.
  * `"all"`: notifica todos los tapbacks entrantes de remitentes autorizados.
  * `"off"`: ignora los tapbacks entrantes.


Las sobrescrituras por cuenta usan `channels.imessage.accounts.<id>.reactionNotifications`.

## Escrituras de configuración

iMessage permite escrituras de configuración iniciadas por el canal de forma predeterminada (para `/config set|unset` cuando `commands.config: true`).

Desactivar:

json5Copy code
[code]
    {  channels: {    imessage: {      configWrites: false,    },  },}
[/code]

## Fusión de mensajes directos de envío dividido (comando + URL en una composición)

Cuando un usuario escribe un comando y una URL juntos — por ejemplo, `Dump https://example.com/article` — la app Mensajes de Apple divide el envío en **dos filas separadas de`chat.db`**:

  1. Un mensaje de texto (`"Dump"`).
  2. Un globo de vista previa de URL (`"https://..."`) con imágenes de vista previa OG como adjuntos.


Las dos filas llegan a OpenClaw con una separación de ~0,8-2,0 s en la mayoría de las configuraciones. Sin fusionarlas, el agente recibe solo el comando en el turno 1, responde (a menudo "envíame la URL") y solo ve la URL en el turno 2, momento en el que el contexto del comando ya se perdió. Esto es parte del canal de envío de Apple, no algo que OpenClaw o `imsg` introduzcan.

`channels.imessage.coalesceSameSenderDms` permite que un DM fusione filas consecutivas del mismo remitente en un único turno del agente. Los chats grupales siguen despachándose por mensaje para preservar la estructura de turnos de múltiples usuarios.

### Cuándo habilitarlo

Habilítalo cuando:

  * Distribuyes Skills que esperan `command + payload` en un solo mensaje (volcar, pegar, guardar, encolar, etc.).
  * Tus usuarios pegan URL, imágenes o contenido largo junto con comandos.
  * Puedes aceptar la latencia adicional en turnos de DM (consulta abajo).


Déjalo deshabilitado cuando:

  * Necesitas latencia mínima de comandos para disparadores de DM de una sola palabra.
  * Todos tus flujos son comandos únicos sin seguimientos de carga útil.


### Habilitación

json5Copy code
[code]
    {  channels: {    imessage: {      coalesceSameSenderDms: true, // opt in (default: false)    },  },}
[/code]

Con la marca activada y sin `messages.inbound.byChannel.imessage` explícito, la ventana de debounce se amplía a **2500 ms** (el valor predeterminado heredado es 0 ms, sin debounce). La ventana más amplia es necesaria porque la cadencia de envío dividido de Apple de 0,8-2,0 s no cabe en un valor predeterminado más ajustado.

Para ajustar la ventana tú mismo:

json5Copy code
[code]
    {  messages: {    inbound: {      byChannel: {        // 2500 ms works for most setups; raise to 4000 ms if your Mac is        // slow or under memory pressure (observed gap can stretch past 2 s        // then).        imessage: 2500,      },    },  },}
[/code]

### Compensaciones

  * **Latencia añadida para mensajes de DM.** Con la marca activada, cada DM (incluidos los comandos de control independientes y los seguimientos de texto único) espera hasta la ventana de debounce antes de despacharse, por si viene una fila de carga útil. Los mensajes de chat grupal mantienen el despacho instantáneo.
  * **La salida fusionada está acotada.** El texto fusionado se limita a 4000 caracteres con un marcador explícito `…[truncated]`; los adjuntos se limitan a 20; las entradas de origen se limitan a 10 (se conservan la primera y las más recientes más allá de eso). Cada GUID de origen se registra en `coalescedMessageGuids` para telemetría posterior.
  * **Solo DM.** Los chats grupales pasan al despacho por mensaje para que el bot siga respondiendo cuando varias personas estén escribiendo.
  * **Opt-in, por canal.** Otros canales (Telegram, WhatsApp, Slack, …) no se ven afectados. Las configuraciones heredadas de BlueBubbles que establecen `channels.bluebubbles.coalesceSameSenderDms` deben migrar ese valor a `channels.imessage.coalesceSameSenderDms`.


### Escenarios y lo que ve el agente

El usuario compone | `chat.db` produce | Marca desactivada (predeterminado) | Marca activada + ventana de 2500 ms  
---|---|---|---  
`Dump https://example.com` (un envío) | 2 filas con ~1 s de separación | Dos turnos del agente: solo "Dump", luego URL | Un turno: texto fusionado `Dump https://example.com`  
`Save this 📎image.jpg caption` (adjunto + texto) | 2 filas | Dos turnos (adjunto descartado en la fusión) | Un turno: texto + imagen preservados  
`/status` (comando independiente) | 1 fila | Despacho instantáneo | **Espera hasta la ventana y luego despacha**  
URL pegada sola | 1 fila | Despacho instantáneo | Despacho instantáneo (solo una entrada en el bucket)  
Texto + URL enviados como dos mensajes separados deliberados, con minutos de diferencia | 2 filas fuera de la ventana | Dos turnos | Dos turnos (la ventana vence entre ellos)  
Ráfaga rápida (>10 DM pequeños dentro de la ventana) | N filas | N turnos | Un turno, salida acotada (primero + más recientes, límites de texto/adjuntos aplicados)  
Dos personas escribiendo en un chat grupal | N filas de M remitentes | M+ turnos (uno por bucket de remitente) | M+ turnos; los chats grupales no se fusionan  
  
## Ponerse al día tras una caída del Gateway

Cuando el Gateway está sin conexión (cierre inesperado, reinicio, reposo del Mac, máquina apagada), `imsg watch` se reanuda desde el estado actual de `chat.db` cuando el Gateway vuelve a estar disponible; por defecto, cualquier cosa que haya llegado durante la interrupción nunca se ve. La recuperación reproduce esos mensajes en el siguiente inicio para que el agente no pierda tráfico entrante silenciosamente.

La recuperación está **deshabilitada de forma predeterminada**. Habilítala por canal:

tsCopy code
[code]
    channels: {  imessage: {    catchup: {      enabled: true,             // master switch (default: false)      maxAgeMinutes: 120,        // skip rows older than now - 2h (default: 120, clamp 1..720)      perRunLimit: 50,           // max rows replayed per startup (default: 50, clamp 1..500)      firstRunLookbackMinutes: 30, // first run with no cursor: look back 30 min (default: 30)      maxFailureRetries: 10,     // give up on a wedged guid after 10 dispatch failures (default: 10)    },  },}
[/code]

### Cómo se ejecuta

Una pasada por cada inicio de `monitorIMessageProvider`, secuenciada como `imsg launch` listo → `watch.subscribe` → `performIMessageCatchup` → bucle de despacho en vivo. La recuperación usa `chats.list` \+ `messages.history` por chat contra el mismo cliente JSON-RPC que usa `imsg watch`. Cualquier cosa que llegue durante la pasada de recuperación fluye por el despacho en vivo normalmente; la caché de deduplicación entrante existente absorbe cualquier solapamiento con las filas reproducidas.

Cada fila reproducida se envía por la ruta de despacho en vivo (`evaluateIMessageInbound` \+ `dispatchInboundMessage`), por lo que las listas de permitidos, la política de grupos, el debouncer, la caché de eco y las confirmaciones de lectura se comportan de forma idéntica en mensajes reproducidos y en vivo.

### Semántica de cursor y reintento

La recuperación mantiene un cursor por cuenta en `<openclawStateDir>/imessage/catchup/<account>__<hash>.json` (el directorio de estado de OpenClaw tiene como valor predeterminado `~/.openclaw`, se puede sobrescribir con `OPENCLAW_STATE_DIR`):

jsonCopy code
[code]
    {  "lastSeenMs": 1717900800000,  "lastSeenRowid": 482910,  "updatedAt": 1717900801234,  "failureRetries": { "<guid>": 1 }}
[/code]

  * El cursor avanza tras cada despacho correcto y se mantiene cuando el despacho de una fila lanza una excepción; el siguiente inicio reintenta la misma fila desde el cursor retenido.
  * Después de `maxFailureRetries` excepciones consecutivas contra el mismo `guid`, la recuperación registra un `warn` y fuerza el avance del cursor más allá del mensaje bloqueado para que los inicios posteriores puedan progresar.
  * Los GUID ya abandonados se omiten al detectarlos (sin intento de despacho) en ejecuciones posteriores y se contabilizan bajo `skippedGivenUp` en el resumen de ejecución.


### Señales visibles para el operador

CodeCopy code
[code]
    imessage catchup: replayed=N skippedFromMe=… skippedGivenUp=… failed=… givenUp=… fetchedCount=…imessage catchup: giving up on guid=<guid> after &lt;N&gt; failures; advancing cursor past itimessage catchup: fetched &lt;X&gt; rows across chats, capped to perRunLimit=&lt;Y&gt;
[/code]

Una línea `WARN ... capped to perRunLimit` significa que un único inicio no agotó todo el backlog. Aumenta `perRunLimit` (máximo 500) si tus interrupciones superan regularmente la pasada predeterminada de 50 filas.

### Cuándo dejarlo desactivado

  * El Gateway se ejecuta continuamente con reinicio automático por watchdog y las interrupciones siempre son de menos de unos segundos; el valor predeterminado desactivado está bien.
  * El volumen de DM es bajo y los mensajes perdidos no cambiarían el comportamiento del agente; la ventana inicial `firstRunLookbackMinutes` puede despachar contexto antiguo inesperado al habilitarlo por primera vez.


Cuando activas la recuperación, el primer inicio sin cursor solo mira hacia atrás `firstRunLookbackMinutes` (30 min de forma predeterminada), no la ventana completa de `maxAgeMinutes`; esto evita reproducir un historial largo de mensajes anteriores a la habilitación.

## Solución de problemas

imsg no encontrado o RPC no compatible

Valida el binario y la compatibilidad con RPC:

bashCopy code
[code]
    imsg rpc --helpimsg status --jsonopenclaw channels status --probe
[/code]

Si la comprobación informa que RPC no es compatible, actualiza `imsg`. Si las acciones de API privada no están disponibles, ejecuta `imsg launch` en la sesión del usuario de macOS con sesión iniciada y vuelve a comprobar. Si el Gateway no se está ejecutando en macOS, usa la configuración de Mac remoto por SSH anterior en lugar de la ruta local predeterminada de `imsg`.

El Gateway no se está ejecutando en macOS

El `cliPath: "imsg"` predeterminado debe ejecutarse en el Mac con sesión iniciada en Mensajes. En Linux o Windows, establece `channels.imessage.cliPath` en un script envoltorio que se conecte por SSH a ese Mac y ejecute `imsg "$@"`.

bashCopy code
[code]
    #!/usr/bin/env bashexec ssh -T messages-mac imsg "$@"
[/code]

Luego ejecuta:

bashCopy code
[code]
    openclaw channels status --probe --channel imessage
[/code]

Los DM se ignoran

Comprueba:

  * `channels.imessage.dmPolicy`
  * `channels.imessage.allowFrom`
  * aprobaciones de emparejamiento (`openclaw pairing list imessage`)

Los mensajes grupales se ignoran

Comprueba:

  * `channels.imessage.groupPolicy`
  * `channels.imessage.groupAllowFrom`
  * comportamiento de lista de permitidos de `channels.imessage.groups`
  * configuración de patrones de mención (`agents.list[].groupChat.mentionPatterns`)

Fallan los adjuntos remotos

Comprueba:

  * `channels.imessage.remoteHost`
  * `channels.imessage.remoteAttachmentRoots`
  * autenticación con clave SSH/SCP desde el host del Gateway
  * la clave de host existe en `~/.ssh/known_hosts` en el host del Gateway
  * legibilidad de la ruta remota en el Mac que ejecuta Mensajes

Se pasaron por alto los avisos de permisos de macOS

Vuelve a ejecutar en una terminal GUI interactiva en el mismo contexto de usuario/sesión y aprueba los avisos:

bashCopy code
[code]
    imsg chats --limit 1imsg send <handle> "test"
[/code]

Confirma que Full Disk Access + Automation estén concedidos para el contexto del proceso que ejecuta OpenClaw/`imsg`.

## Punteros de referencia de configuración

  * [Referencia de configuración - iMessage](</es/gateway/config-channels#imessage>)
  * [Configuración del Gateway](</es/gateway/configuration>)
  * [Emparejamiento](</es/channels/pairing>)


## Relacionado

  * [Resumen de canales](</es/channels>) — todos los canales compatibles
  * [Eliminación de BlueBubbles y la ruta iMessage de imsg](</es/announcements/bluebubbles-imessage>) — anuncio y resumen de migración
  * [Migrar desde BlueBubbles](</es/channels/imessage-from-bluebubbles>) — tabla de traducción de configuración y migración paso a paso
  * [Emparejamiento](</es/channels/pairing>) — autenticación de DM y flujo de emparejamiento
  * [Grupos](</es/channels/groups>) — comportamiento de chats grupales y compuerta por mención
  * [Enrutamiento de canales](</es/channels/channel-routing>) — enrutamiento de sesiones para mensajes
  * [Seguridad](</es/gateway/security>) — modelo de acceso y endurecimiento


Was this useful?YesNo