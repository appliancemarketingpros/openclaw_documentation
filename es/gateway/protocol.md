---
title: Protocolo de Gateway
source_url: https://docs.openclaw.ai/es/gateway/protocol
scraped_at: 2026-05-25
---

El protocolo WS del Gateway es el **único plano de control + transporte de nodos** para OpenClaw. Todos los clientes (CLI, interfaz web, app de macOS, nodos iOS/Android, nodos sin interfaz) se conectan por WebSocket y declaran su **rol** \+ **alcance** en el momento del handshake.

## Transporte

  * WebSocket, tramas de texto con cargas JSON.
  * La primera trama **debe** ser una solicitud `connect`.
  * Las tramas previas a la conexión tienen un límite de 64 KiB. Después de un handshake correcto, los clientes deben seguir los límites `hello-ok.policy.maxPayload` y `hello-ok.policy.maxBufferedBytes`. Con diagnósticos activados, las tramas entrantes sobredimensionadas y los búferes salientes lentos emiten eventos `payload.large` antes de que el gateway cierre o descarte la trama afectada. Estos eventos conservan tamaños, límites, superficies y códigos de motivo seguros. No conservan el cuerpo del mensaje, el contenido de adjuntos, el cuerpo de la trama sin procesar, tokens, cookies ni valores secretos.


## Handshake (connect)

Gateway → Cliente (desafío previo a la conexión):

jsonCopy code
[code]
    {  "type": "event",  "event": "connect.challenge",  "payload": { "nonce": "…", "ts": 1737264000000 }}
[/code]

Cliente → Gateway:

jsonCopy code
[code]
    {  "type": "req",  "id": "…",  "method": "connect",  "params": {    "minProtocol": 3,    "maxProtocol": 4,    "client": {      "id": "cli",      "version": "1.2.3",      "platform": "macos",      "mode": "operator"    },    "role": "operator",    "scopes": ["operator.read", "operator.write"],    "caps": [],    "commands": [],    "permissions": {},    "auth": { "token": "…" },    "locale": "en-US",    "userAgent": "openclaw-cli/1.2.3",    "device": {      "id": "device_fingerprint",      "publicKey": "…",      "signature": "…",      "signedAt": 1737264000000,      "nonce": "…"    }  }}
[/code]

Gateway → Cliente:

jsonCopy code
[code]
    {  "type": "res",  "id": "…",  "ok": true,  "payload": {    "type": "hello-ok",    "protocol": 4,    "server": { "version": "…", "connId": "…" },    "features": { "methods": ["…"], "events": ["…"] },    "snapshot": { "…": "…" },    "auth": {      "role": "operator",      "scopes": ["operator.read", "operator.write"]    },    "policy": {      "maxPayload": 26214400,      "maxBufferedBytes": 52428800,      "tickIntervalMs": 15000    }  }}
[/code]

Mientras el Gateway aún termina los procesos auxiliares de arranque, la solicitud `connect` puede devolver un error `UNAVAILABLE` reintentable con `details.reason` establecido en `"startup-sidecars"` y `retryAfterMs`. Los clientes deben reintentar esa respuesta dentro de su presupuesto global de conexión en lugar de mostrarla como un fallo terminal de handshake.

`server`, `features`, `snapshot` y `policy` son obligatorios según el esquema (`src/gateway/protocol/schema/frames.ts`). `auth` también es obligatorio e informa el rol/los alcances negociados. `pluginSurfaceUrls` es opcional y asigna nombres de superficies de plugin, como `canvas`, a URL alojadas con alcance.

Las URL de superficies de plugin con alcance pueden caducar. Los nodos pueden llamar a `node.pluginSurface.refresh` con `{ "surface": "canvas" }` para recibir una entrada nueva en `pluginSurfaceUrls`. La refactorización experimental del Plugin Canvas no admite la ruta de compatibilidad obsoleta `canvasHostUrl`, `canvasCapability` ni `node.canvas.capability.refresh`; los clientes nativos y gateways actuales deben usar superficies de plugin.

Cuando no se emite ningún token de dispositivo, `hello-ok.auth` informa los permisos negociados sin campos de token:

jsonCopy code
[code]
    {  "auth": {    "role": "operator",    "scopes": ["operator.read", "operator.write"]  }}
[/code]

Los clientes backend de confianza del mismo proceso (`client.id: "gateway-client"`, `client.mode: "backend"`) pueden omitir `device` en conexiones directas de loopback cuando se autentican con el token/contraseña compartido del gateway. Esta ruta está reservada para RPC internos del plano de control y evita que las líneas base obsoletas de emparejamiento CLI/dispositivo bloqueen trabajo backend local, como actualizaciones de sesiones de subagentes. Los clientes remotos, los clientes con origen de navegador, los clientes nodo y los clientes explícitos con token de dispositivo/identidad de dispositivo siguen usando las comprobaciones normales de emparejamiento y aumento de alcance.

Cuando se emite un token de dispositivo, `hello-ok` también incluye:

jsonCopy code
[code]
    {  "auth": {    "deviceToken": "…",    "role": "operator",    "scopes": ["operator.read", "operator.write"]  }}
[/code]

Durante la transferencia de arranque de confianza, `hello-ok.auth` también puede incluir entradas de rol adicionales y acotadas en `deviceTokens`:

jsonCopy code
[code]
    {  "auth": {    "deviceToken": "…",    "role": "node",    "scopes": [],    "deviceTokens": [      {        "deviceToken": "…",        "role": "operator",        "scopes": ["operator.approvals", "operator.read", "operator.talk.secrets", "operator.write"]      }    ]  }}
[/code]

Para el flujo de arranque integrado de nodo/operador, el token de nodo principal permanece `scopes: []` y cualquier token de operador transferido queda acotado a la lista de permitidos del operador de arranque (`operator.approvals`, `operator.read`, `operator.talk.secrets`, `operator.write`). Las comprobaciones de alcance de arranque siguen con prefijo de rol: las entradas de operador solo satisfacen solicitudes de operador, y los roles que no son operador siguen necesitando alcances bajo su propio prefijo de rol.

### Ejemplo de nodo

jsonCopy code
[code]
    {  "type": "req",  "id": "…",  "method": "connect",  "params": {    "minProtocol": 3,    "maxProtocol": 4,    "client": {      "id": "ios-node",      "version": "1.2.3",      "platform": "ios",      "mode": "node"    },    "role": "node",    "scopes": [],    "caps": ["camera", "canvas", "screen", "location", "voice"],    "commands": ["camera.snap", "canvas.navigate", "screen.record", "location.get"],    "permissions": { "camera.capture": true, "screen.record": false },    "auth": { "token": "…" },    "locale": "en-US",    "userAgent": "openclaw-ios/1.2.3",    "device": {      "id": "device_fingerprint",      "publicKey": "…",      "signature": "…",      "signedAt": 1737264000000,      "nonce": "…"    }  }}
[/code]

## Enmarcado

  * **Solicitud** : `{type:"req", id, method, params}`
  * **Respuesta** : `{type:"res", id, ok, payload|error}`
  * **Evento** : `{type:"event", event, payload, seq?, stateVersion?}`


Los métodos con efectos secundarios requieren **claves de idempotencia** (ver el esquema).

## Roles + alcances

Para el modelo completo de alcances de operador, las comprobaciones en el momento de aprobación y la semántica de secreto compartido, consulta [Alcances de operador](</es/gateway/operator-scopes>).

### Roles

  * `operator` = cliente del plano de control (CLI/UI/automatización).
  * `node` = host de capacidades (camera/screen/canvas/system.run).


### Alcances (operador)

Alcances comunes:

  * `operator.read`
  * `operator.write`
  * `operator.admin`
  * `operator.approvals`
  * `operator.pairing`
  * `operator.talk.secrets`


`talk.config` con `includeSecrets: true` requiere `operator.talk.secrets` (o `operator.admin`).

Los métodos RPC de gateway registrados por plugins pueden solicitar su propio alcance de operador, pero los prefijos reservados de administración del núcleo (`config.*`, `exec.approvals.*`, `wizard.*`, `update.*`) siempre se resuelven como `operator.admin`.

El alcance del método es solo la primera barrera. Algunos comandos de barra diagonal alcanzados mediante `chat.send` aplican comprobaciones más estrictas a nivel de comando encima. Por ejemplo, las escrituras persistentes `/config set` y `/config unset` requieren `operator.admin`.

`node.pair.approve` también tiene una comprobación de alcance adicional en el momento de aprobación además del alcance base del método:

  * solicitudes sin comandos: `operator.pairing`
  * solicitudes con comandos de nodo que no son exec: `operator.pairing` \+ `operator.write`
  * solicitudes que incluyen `system.run`, `system.run.prepare` o `system.which`: `operator.pairing` \+ `operator.admin`


### Caps/comandos/permisos (nodo)

Los nodos declaran reclamaciones de capacidad al conectarse:

  * `caps`: categorías de capacidad de alto nivel como `camera`, `canvas`, `screen`, `location`, `voice` y `talk`.
  * `commands`: lista de permitidos de comandos para invoke.
  * `permissions`: conmutadores granulares (p. ej., `screen.record`, `camera.capture`).


El Gateway trata estas como **reclamaciones** y aplica listas de permitidos del lado servidor.

## Presencia

  * `system-presence` devuelve entradas indexadas por identidad de dispositivo.
  * Las entradas de presencia incluyen `deviceId`, `roles` y `scopes` para que las UI puedan mostrar una sola fila por dispositivo incluso cuando se conecta como **operator** y **node**.
  * `node.list` incluye campos opcionales `lastSeenAtMs` y `lastSeenReason`. Los nodos conectados informan su hora de conexión actual como `lastSeenAtMs` con motivo `connect`; los nodos emparejados también pueden informar presencia duradera en segundo plano cuando un evento de nodo de confianza actualiza sus metadatos de emparejamiento.


### Evento alive de nodo en segundo plano

Los nodos pueden llamar a `node.event` con `event: "node.presence.alive"` para registrar que un nodo emparejado estaba activo durante una activación en segundo plano sin marcarlo como conectado.

jsonCopy code
[code]
    {  "event": "node.presence.alive",  "payloadJSON": "{\"trigger\":\"silent_push\",\"sentAtMs\":1737264000000,\"displayName\":\"Peter's iPhone\",\"version\":\"2026.4.28\",\"platform\":\"iOS 18.4.0\",\"deviceFamily\":\"iPhone\",\"modelIdentifier\":\"iPhone17,1\",\"pushTransport\":\"relay\"}"}
[/code]

`trigger` es un enum cerrado: `background`, `silent_push`, `bg_app_refresh`, `significant_location`, `manual` o `connect`. Las cadenas de trigger desconocidas se normalizan a `background` por el gateway antes de persistirse. El evento solo es duradero para sesiones de dispositivo de nodo autenticadas; las sesiones sin dispositivo o no emparejadas devuelven `handled: false`.

Los gateways correctos devuelven un resultado estructurado:

jsonCopy code
[code]
    {  "ok": true,  "event": "node.presence.alive",  "handled": true,  "reason": "persisted"}
[/code]

Los gateways más antiguos aún pueden devolver `{ "ok": true }` para `node.event`; los clientes deben tratarlo como un RPC reconocido, no como persistencia duradera de presencia.

## Alcance de eventos broadcast

Los eventos broadcast de WebSocket enviados por el servidor se limitan por alcance para que las sesiones con alcance de emparejamiento o solo de nodo no reciban pasivamente contenido de sesión.

  * **Tramas de chat, agente y resultados de herramientas** (incluidos eventos `agent` transmitidos y resultados de llamadas de herramientas) requieren al menos `operator.read`. Las sesiones sin `operator.read` omiten estas tramas por completo.
  * **Broadcasts`plugin.*` definidos por plugins** se limitan a `operator.write` u `operator.admin`, según cómo los haya registrado el plugin.
  * **Eventos de estado y transporte** (`heartbeat`, `presence`, `tick`, ciclo de vida de conexión/desconexión, etc.) permanecen sin restricciones para que el estado del transporte siga siendo observable para cada sesión autenticada.
  * **Familias de eventos broadcast desconocidas** se limitan por alcance de forma predeterminada (fallo cerrado) salvo que un manejador registrado las relaje explícitamente.


Cada conexión de cliente conserva su propio número de secuencia por cliente, de modo que los broadcasts mantienen un orden monótono en ese socket incluso cuando distintos clientes ven subconjuntos filtrados por alcance diferentes del flujo de eventos.

## Familias comunes de métodos RPC

La superficie pública de WS es más amplia que los ejemplos de handshake/autenticación anteriores. Esto no es un volcado generado: `hello-ok.features.methods` es una lista de descubrimiento conservadora creada a partir de `src/gateway/server-methods-list.ts` más exportaciones cargadas de métodos de plugin/canal. Trátala como descubrimiento de funciones, no como una enumeración completa de `src/gateway/server-methods/*.ts`.

Sistema e identidad

  * `health` devuelve la instantánea de estado del gateway almacenada en caché o recién sondeada.
  * `diagnostics.stability` devuelve el registrador de estabilidad de diagnóstico acotado reciente. Conserva metadatos operativos como nombres de eventos, conteos, tamaños en bytes, lecturas de memoria, estado de cola/sesión, nombres de canal/plugin e ids de sesión. No conserva texto de chat, cuerpos de webhook, salidas de herramientas, cuerpos de solicitud o respuesta sin procesar, tokens, cookies ni valores secretos. Se requiere alcance de lectura de operador.
  * `status` devuelve el resumen del gateway estilo `/status`; los campos sensibles se incluyen solo para clientes operador con alcance de administración.
  * `gateway.identity.get` devuelve la identidad de dispositivo del gateway usada por flujos de relay y emparejamiento.
  * `system-presence` devuelve la instantánea de presencia actual para dispositivos operador/nodo conectados.
  * `system-event` añade un evento del sistema y puede actualizar/difundir contexto de presencia.
  * `last-heartbeat` devuelve el último evento Heartbeat persistido.
  * `set-heartbeats` activa o desactiva el procesamiento de Heartbeat en el gateway.

Modelos y uso

  * `models.list` devuelve el catálogo de modelos permitido por el tiempo de ejecución. Pasa `{ "view": "configured" }` para obtener modelos configurados de tamaño adecuado para selectores (`agents.defaults.models` primero, luego `models.providers.*.models`), o `{ "view": "all" }` para el catálogo completo.
  * `usage.status` devuelve resúmenes de ventanas de uso/cuota restante del proveedor.
  * `usage.cost` devuelve resúmenes agregados de uso de costes para un intervalo de fechas.
  * `doctor.memory.status` devuelve la preparación de memoria vectorial / incrustaciones en caché para el espacio de trabajo del agente predeterminado activo. Pasa `{ "probe": true }` o `{ "deep": true }` solo cuando el llamador quiere explícitamente un ping en vivo al proveedor de incrustaciones.
  * `doctor.memory.remHarness` devuelve una vista previa acotada y de solo lectura del arnés REM para clientes remotos del plano de control. Puede incluir rutas de espacios de trabajo, fragmentos de memoria, Markdown fundamentado renderizado y candidatos de promoción profunda, por lo que los llamadores necesitan `operator.read`.
  * `sessions.usage` devuelve resúmenes de uso por sesión.
  * `sessions.usage.timeseries` devuelve uso en series temporales para una sesión.
  * `sessions.usage.logs` devuelve entradas de registro de uso para una sesión.

Canales y asistentes de inicio de sesión

  * `channels.status` devuelve resúmenes de estado de canales/Plugin integrados + incluidos.
  * `channels.logout` cierra la sesión de un canal/cuenta específico cuando el canal admite cierre de sesión.
  * `web.login.start` inicia un flujo de inicio de sesión QR/web para el proveedor de canal web actual con capacidad QR.
  * `web.login.wait` espera a que ese flujo de inicio de sesión QR/web se complete e inicia el canal si tiene éxito.
  * `push.test` envía una notificación push de prueba de APNs a un nodo iOS registrado.
  * `voicewake.get` devuelve los activadores de palabra de activación almacenados.
  * `voicewake.set` actualiza los activadores de palabra de activación y difunde el cambio.

Mensajería y registros

  * `send` es el RPC directo de entrega saliente para envíos dirigidos a canal/cuenta/hilo fuera del ejecutor de chat.
  * `logs.tail` devuelve la cola configurada del registro de archivo del Gateway con controles de cursor/límite y bytes máximos.

Talk y TTS

  * `talk.catalog` devuelve el catálogo de solo lectura de proveedores de Talk para voz, transcripción en streaming y voz en tiempo real. Incluye ids de proveedor, etiquetas, estado configurado, ids de modelo/voz expuestos, modos canónicos, transportes, estrategias de cerebro y flags de audio/capacidad en tiempo real sin devolver secretos del proveedor ni mutar la configuración global.
  * `talk.config` devuelve la carga útil efectiva de configuración de Talk; `includeSecrets` requiere `operator.talk.secrets` (u `operator.admin`).
  * `talk.session.create` crea una sesión de Talk propiedad del Gateway para `realtime/gateway-relay`, `transcription/gateway-relay` o `stt-tts/managed-room`. `brain: "direct-tools"` requiere `operator.admin`.
  * `talk.session.join` valida un token de sesión de sala administrada, emite eventos `session.ready` o `session.replaced` según sea necesario, y devuelve metadatos de sala/sesión más eventos recientes de Talk sin el token en texto plano ni el hash de token almacenado.
  * `talk.session.appendAudio` agrega audio de entrada PCM en base64 a sesiones de relay en tiempo real y transcripción propiedad del Gateway.
  * `talk.session.startTurn`, `talk.session.endTurn` y `talk.session.cancelTurn` controlan el ciclo de vida de turnos de sala administrada con rechazo de turnos obsoletos antes de borrar el estado.
  * `talk.session.cancelOutput` detiene la salida de audio del asistente, principalmente para interrupción con VAD en sesiones de relay del Gateway.
  * `talk.session.submitToolResult` completa una llamada a herramienta del proveedor emitida por una sesión de relay en tiempo real propiedad del Gateway. Pasa `options: { willContinue: true }` para salida de herramienta intermedia cuando seguirá un resultado final, u `options: { suppressResponse: true }` cuando el resultado de la herramienta debe satisfacer la llamada del proveedor sin iniciar otra respuesta de asistente en tiempo real.
  * `talk.session.close` cierra una sesión de relay, transcripción o sala administrada propiedad del Gateway y emite eventos terminales de Talk.
  * `talk.mode` establece/difunde el estado actual del modo Talk para clientes WebChat/Control UI.
  * `talk.client.create` crea una sesión de proveedor en tiempo real propiedad del cliente usando `webrtc` o `provider-websocket` mientras el Gateway posee la configuración, las credenciales, las instrucciones y la política de herramientas.
  * `talk.client.toolCall` permite que transportes en tiempo real propiedad del cliente reenvíen llamadas a herramientas del proveedor a la política del Gateway. La primera herramienta admitida es `openclaw_agent_consult`; los clientes reciben un id de ejecución y esperan eventos normales del ciclo de vida del chat antes de enviar el resultado de herramienta específico del proveedor.
  * `talk.event` es el único canal de eventos de Talk para adaptadores de tiempo real, transcripción, STT/TTS, sala administrada, telefonía y reuniones.
  * `talk.speak` sintetiza voz mediante el proveedor de voz de Talk activo.
  * `tts.status` devuelve el estado habilitado de TTS, proveedor activo, proveedores de respaldo y estado de configuración del proveedor.
  * `tts.providers` devuelve el inventario visible de proveedores TTS.
  * `tts.enable` y `tts.disable` alternan el estado de preferencias de TTS.
  * `tts.setProvider` actualiza el proveedor TTS preferido.
  * `tts.convert` ejecuta una conversión puntual de texto a voz.

Secretos, configuración, actualización y asistente

  * `secrets.reload` vuelve a resolver SecretRefs activos e intercambia el estado de secretos del tiempo de ejecución solo si todo tiene éxito.
  * `secrets.resolve` resuelve asignaciones de secretos destinadas a comandos para un conjunto específico de comando/destino.
  * `config.get` devuelve la instantánea y el hash de la configuración actual.
  * `config.set` escribe una carga útil de configuración validada.
  * `config.patch` fusiona una actualización parcial de configuración.
  * `config.apply` valida + reemplaza la carga útil completa de configuración.
  * `config.schema` devuelve la carga útil del esquema de configuración en vivo usado por Control UI y herramientas CLI: esquema, `uiHints`, versión y metadatos de generación, incluidos metadatos de esquema de Plugin + canal cuando el tiempo de ejecución puede cargarlos. El esquema incluye metadatos de campo `title` / `description` derivados de las mismas etiquetas y texto de ayuda usados por la UI, incluidas ramas de composición de objeto anidado, comodín, elemento de arreglo y `anyOf` / `oneOf` / `allOf` cuando existe documentación de campo coincidente.
  * `config.schema.lookup` devuelve una carga útil de búsqueda con alcance de ruta para una ruta de configuración: ruta normalizada, un nodo de esquema superficial, pista coincidente + `hintPath` y resúmenes de hijos inmediatos para exploración en UI/CLI. Los nodos de esquema de búsqueda conservan la documentación orientada al usuario y los campos comunes de validación (`title`, `description`, `type`, `enum`, `const`, `format`, `pattern`, límites numéricos/de cadena/de arreglo/de objeto, y flags como `additionalProperties`, `deprecated`, `readOnly`, `writeOnly`). Los resúmenes de hijos exponen `key`, `path` normalizada, `type`, `required`, `hasChildren`, además del `hint` / `hintPath` coincidente.
  * `update.run` ejecuta el flujo de actualización del Gateway y programa un reinicio solo cuando la actualización en sí tuvo éxito; los llamadores con una sesión pueden incluir `continuationMessage` para que el inicio reanude un turno de agente de seguimiento mediante la cola de continuación de reinicio. Las actualizaciones del gestor de paquetes fuerzan un reinicio por actualización no diferido y sin tiempo de espera después del intercambio del paquete para que el proceso Gateway antiguo no siga cargando de forma diferida desde un árbol `dist` reemplazado.
  * `update.status` devuelve el último centinela en caché de reinicio por actualización, incluida la versión en ejecución posterior al reinicio cuando esté disponible.
  * `wizard.start`, `wizard.next`, `wizard.status` y `wizard.cancel` exponen el asistente de incorporación sobre WS RPC.

Asistentes de agente y espacio de trabajo

  * `agents.list` devuelve entradas de agentes configurados, incluidos el modelo efectivo y metadatos del tiempo de ejecución.
  * `agents.create`, `agents.update` y `agents.delete` administran registros de agentes y cableado de espacios de trabajo.
  * `agents.files.list`, `agents.files.get` y `agents.files.set` administran los archivos de espacio de trabajo de arranque expuestos para un agente.
  * `tasks.list`, `tasks.get` y `tasks.cancel` exponen el libro mayor de tareas del Gateway a clientes SDK y operadores.
  * `artifacts.list`, `artifacts.get` y `artifacts.download` exponen resúmenes y descargas de artefactos derivados de transcripciones para un alcance explícito `sessionKey`, `runId` o `taskId`. Las consultas de ejecución y tarea resuelven la sesión propietaria del lado del servidor y solo devuelven medios de transcripción con procedencia coincidente; las fuentes de URL no seguras o locales devuelven descargas no admitidas en lugar de recuperarlas del lado del servidor.
  * `environments.list` y `environments.status` exponen descubrimiento de entornos locales del Gateway y de nodos, de solo lectura, para clientes SDK.
  * `agent.identity.get` devuelve la identidad efectiva del asistente para un agente o sesión.
  * `agent.wait` espera a que una ejecución termine y devuelve la instantánea terminal cuando está disponible.

Control de sesiones

  * `sessions.list` devuelve el índice de sesiones actual, incluidos metadatos `agentRuntime` por fila cuando hay configurado un backend de tiempo de ejecución de agente.
  * `sessions.subscribe` y `sessions.unsubscribe` alternan las suscripciones a eventos de cambios de sesión para el cliente WS actual.
  * `sessions.messages.subscribe` y `sessions.messages.unsubscribe` alternan las suscripciones a eventos de transcripción/mensaje para una sesión.
  * `sessions.preview` devuelve vistas previas acotadas de transcripción para claves de sesión específicas.
  * `sessions.describe` devuelve una fila de sesión del Gateway para una clave de sesión exacta.
  * `sessions.resolve` resuelve o canonicaliza un destino de sesión.
  * `sessions.create` crea una nueva entrada de sesión.
  * `sessions.send` envía un mensaje a una sesión existente.
  * `sessions.steer` es la variante de interrumpir y dirigir para una sesión activa.
  * `sessions.abort` cancela trabajo activo para una sesión. Un llamador puede pasar `key` más `runId` opcional, o pasar solo `runId` para ejecuciones activas que el Gateway pueda resolver a una sesión.
  * `sessions.patch` actualiza metadatos/anulaciones de sesión e informa el modelo canónico resuelto más `agentRuntime` efectivo.
  * `sessions.reset`, `sessions.delete` y `sessions.compact` realizan mantenimiento de sesiones.
  * `sessions.get` devuelve la fila completa de sesión almacenada.
  * La ejecución de chat sigue usando `chat.history`, `chat.send`, `chat.abort` y `chat.inject`. `chat.history` se normaliza para visualización en clientes UI: las etiquetas de directivas en línea se eliminan del texto visible, las cargas útiles XML de llamadas a herramientas en texto plano (incluidas `<tool_call>...</tool_call>`, `<function_call>...</function_call>`, `<tool_calls>...</tool_calls>`, `<function_calls>...</function_calls>` y bloques de llamadas a herramientas truncados) y los tokens de control de modelo filtrados en ASCII/ancho completo se eliminan, las filas de asistente de token silencioso puro como `NO_REPLY` / `no_reply` exactos se omiten, y las filas demasiado grandes pueden reemplazarse con marcadores de posición.

Emparejamiento de dispositivos y tokens de dispositivo

  * `device.pair.list` devuelve dispositivos emparejados pendientes y aprobados.
  * `device.pair.approve`, `device.pair.reject` y `device.pair.remove` administran registros de emparejamiento de dispositivos.
  * `device.token.rotate` rota un token de dispositivo emparejado dentro de los límites de su rol aprobado y alcance del llamador.
  * `device.token.revoke` revoca un token de dispositivo emparejado dentro de los límites de su rol aprobado y alcance del llamador.

Emparejamiento de Node, invocación y trabajo pendiente

  * `node.pair.request`, `node.pair.list`, `node.pair.approve`, `node.pair.reject`, `node.pair.remove` y `node.pair.verify` cubren el emparejamiento de nodos y la verificación de arranque.
  * `node.list` y `node.describe` devuelven el estado de nodos conocidos/conectados.
  * `node.rename` actualiza la etiqueta de un nodo emparejado.
  * `node.invoke` reenvía un comando a un nodo conectado.
  * `node.invoke.result` devuelve el resultado de una solicitud de invocación.
  * `node.event` transporta eventos originados por nodos de vuelta al gateway.
  * `node.pending.pull` y `node.pending.ack` son las API de cola de nodos conectados.
  * `node.pending.enqueue` y `node.pending.drain` administran trabajo pendiente duradero para nodos sin conexión/desconectados.

Familias de aprobación

  * `exec.approval.request`, `exec.approval.get`, `exec.approval.list` y `exec.approval.resolve` cubren solicitudes puntuales de aprobación de exec, además de la búsqueda/reproducción de aprobaciones pendientes.
  * `exec.approval.waitDecision` espera una aprobación de exec pendiente y devuelve la decisión final (o `null` si se agota el tiempo de espera).
  * `exec.approvals.get` y `exec.approvals.set` gestionan instantáneas de la política de aprobación de exec del Gateway.
  * `exec.approvals.node.get` y `exec.approvals.node.set` gestionan la política de aprobación de exec local del nodo mediante comandos de retransmisión del nodo.
  * `plugin.approval.request`, `plugin.approval.list`, `plugin.approval.waitDecision` y `plugin.approval.resolve` cubren flujos de aprobación definidos por plugins.

Automatización, Skills y herramientas

  * Automatización: `wake` programa una inyección de texto de activación inmediata o en el siguiente Heartbeat; `cron.get`, `cron.list`, `cron.status`, `cron.add`, `cron.update`, `cron.remove`, `cron.run`, `cron.runs` gestionan trabajo programado.
  * Skills y herramientas: `commands.list`, `skills.*`, `tools.catalog`, `tools.effective`, `tools.invoke`.


### Familias de eventos comunes

  * `chat`: actualizaciones del chat de la interfaz, como `chat.inject` y otros eventos de chat solo de transcripción.
  * `session.message` y `session.tool`: actualizaciones de transcripción/flujo de eventos para una sesión suscrita.
  * `sessions.changed`: el índice o los metadatos de sesión cambiaron.
  * `presence`: actualizaciones de instantáneas de presencia del sistema.
  * `tick`: evento periódico de keepalive / actividad.
  * `health`: actualización de instantánea de salud del Gateway.
  * `heartbeat`: actualización del flujo de eventos de Heartbeat.
  * `cron`: evento de cambio de ejecución/tarea de Cron.
  * `shutdown`: notificación de apagado del Gateway.
  * `node.pair.requested` / `node.pair.resolved`: ciclo de vida de emparejamiento de nodos.
  * `node.invoke.request`: difusión de solicitud de invocación de nodo.
  * `device.pair.requested` / `device.pair.resolved`: ciclo de vida de dispositivos emparejados.
  * `voicewake.changed`: la configuración del disparador de palabra de activación cambió.
  * `exec.approval.requested` / `exec.approval.resolved`: ciclo de vida de aprobación de exec.
  * `plugin.approval.requested` / `plugin.approval.resolved`: ciclo de vida de aprobación de plugin.


### Métodos auxiliares de Node

  * Los nodos pueden llamar a `skills.bins` para obtener la lista actual de ejecutables de Skills para comprobaciones de autorización automática.


### RPC del registro de tareas

Los clientes operadores pueden inspeccionar y cancelar registros de tareas en segundo plano del Gateway mediante los RPC del registro de tareas. Estos métodos devuelven resúmenes de tareas saneados, no el estado bruto del runtime.

  * `tasks.list` requiere `operator.read`. 
    * Parámetros: `status` opcional (`"queued"`, `"running"`, `"completed"`, `"failed"`, `"cancelled"` o `"timed_out"`) o un arreglo de esos estados, `agentId` opcional, `sessionKey` opcional, `limit` opcional de `1` a `500` y `cursor` de cadena opcional.
    * Resultado: `{ "tasks": TaskSummary[], "nextCursor"?: string }`.
  * `tasks.get` requiere `operator.read`. 
    * Parámetros: `{ "taskId": string }`.
    * Resultado: `{ "task": TaskSummary }`.
    * Los ids de tarea faltantes devuelven la forma de error not-found del Gateway.
  * `tasks.cancel` requiere `operator.write`. 
    * Parámetros: `{ "taskId": string, "reason"?: string }`.
    * Resultado: `{ "found": boolean, "cancelled": boolean, "reason"?: string, "task"?: TaskSummary }`.
    * `found` informa si el registro tenía una tarea coincidente. `cancelled` informa si el runtime aceptó o registró la cancelación.


`TaskSummary` incluye `id`, `status` y metadatos opcionales como `kind`, `runtime`, `title`, `agentId`, `sessionKey`, `childSessionKey`, `ownerKey`, `runId`, `taskId`, `flowId`, `parentTaskId`, `sourceId`, marcas de tiempo, progreso, resumen terminal y texto de error saneado.

### Métodos auxiliares de operador

  * Los operadores pueden llamar a `commands.list` (`operator.read`) para obtener el inventario de comandos del runtime para un agente. 
    * `agentId` es opcional; omítelo para leer el espacio de trabajo predeterminado del agente.
    * `scope` controla a qué superficie apunta el `name` principal: 
      * `text` devuelve el token principal de comando de texto sin la `/` inicial
      * `native` y la ruta predeterminada `both` devuelven nombres nativos conscientes del proveedor cuando están disponibles
    * `textAliases` lleva alias de barra exactos como `/model` y `/m`.
    * `nativeName` lleva el nombre de comando nativo consciente del proveedor cuando existe.
    * `provider` es opcional y solo afecta la nomenclatura nativa más la disponibilidad de comandos nativos de plugin.
    * `includeArgs=false` omite de la respuesta los metadatos de argumentos serializados.
  * Los operadores pueden llamar a `tools.catalog` (`operator.read`) para obtener el catálogo de herramientas del runtime para un agente. La respuesta incluye herramientas agrupadas y metadatos de procedencia: 
    * `source`: `core` o `plugin`
    * `pluginId`: propietario del plugin cuando `source="plugin"`
    * `optional`: si una herramienta de plugin es opcional
  * Los operadores pueden llamar a `tools.effective` (`operator.read`) para obtener el inventario de herramientas efectivo en runtime para una sesión. 
    * `sessionKey` es obligatorio.
    * El gateway deriva contexto de runtime confiable de la sesión en el servidor en lugar de aceptar contexto de autenticación o entrega suministrado por el llamador.
    * La respuesta tiene alcance de sesión y refleja lo que la conversación activa puede usar ahora mismo, incluidas herramientas de core, plugin y canal.
  * Los operadores pueden llamar a `tools.invoke` (`operator.write`) para invocar una herramienta disponible mediante la misma ruta de política del gateway que `/tools/invoke`. 
    * `name` es obligatorio. `args`, `sessionKey`, `agentId`, `confirm` e `idempotencyKey` son opcionales.
    * Si tanto `sessionKey` como `agentId` están presentes, el agente de la sesión resuelta debe coincidir con `agentId`.
    * La respuesta es un sobre orientado al SDK con `ok`, `toolName`, `output` opcional y campos `error` tipados. Los rechazos de aprobación o política devuelven `ok:false` en la carga útil en lugar de omitir la canalización de políticas de herramientas del gateway.
  * Los operadores pueden llamar a `skills.status` (`operator.read`) para obtener el inventario visible de Skills para un agente. 
    * `agentId` es opcional; omítelo para leer el espacio de trabajo predeterminado del agente.
    * La respuesta incluye elegibilidad, requisitos faltantes, comprobaciones de configuración y opciones de instalación saneadas sin exponer valores secretos sin procesar.
  * Los operadores pueden llamar a `skills.search` y `skills.detail` (`operator.read`) para metadatos de descubrimiento de ClawHub.
  * Los operadores pueden llamar a `skills.upload.begin`, `skills.upload.chunk` y `skills.upload.commit` (`operator.admin`) para preparar un archivo privado de Skills antes de instalarlo. Esta es una ruta de carga de administrador separada para clientes de confianza, no el flujo normal de instalación de Skills de ClawHub, y está deshabilitada de forma predeterminada salvo que `skills.install.allowUploadedArchives` esté habilitado. 
    * `skills.upload.begin({ kind: "skill-archive", slug, sizeBytes, sha256?, force?, idempotencyKey? })` crea una carga vinculada a ese slug y valor de force.
    * `skills.upload.chunk({ uploadId, offset, dataBase64 })` anexa bytes en el desplazamiento decodificado exacto.
    * `skills.upload.commit({ uploadId, sha256? })` verifica el tamaño final y SHA-256. Commit solo finaliza la carga; no instala la Skill.
    * Los archivos de Skills cargados son archivos zip que contienen una raíz `SKILL.md`. El nombre de directorio interno del archivo nunca selecciona el destino de instalación.
  * Los operadores pueden llamar a `skills.install` (`operator.admin`) en tres modos: 
    * Modo ClawHub: `{ source: "clawhub", slug, version?, force? }` instala una carpeta de Skills en el directorio `skills/` del espacio de trabajo predeterminado del agente.
    * Modo de carga: `{ source: "upload", uploadId, slug, force?, sha256?, timeoutMs? }` instala una carga confirmada en el directorio `skills/<slug>` del espacio de trabajo predeterminado del agente. El slug y el valor de force deben coincidir con la solicitud original `skills.upload.begin`. Este modo se rechaza salvo que `skills.install.allowUploadedArchives` esté habilitado. La configuración no afecta las instalaciones de ClawHub.
    * Modo instalador de Gateway: `{ name, installId, dangerouslyForceUnsafeInstall?, timeoutMs? }` ejecuta una acción declarada `metadata.openclaw.install` en el host del Gateway.
  * Los operadores pueden llamar a `skills.update` (`operator.admin`) en dos modos: 
    * El modo ClawHub actualiza un slug rastreado o todas las instalaciones rastreadas de ClawHub en el espacio de trabajo predeterminado del agente.
    * El modo de configuración parchea valores de `skills.entries.<skillKey>` como `enabled`, `apiKey` y `env`.


### Vistas de `models.list`

`models.list` acepta un parámetro opcional `view`:

  * Omitido o `"default"`: comportamiento actual del runtime. Si `agents.defaults.models` está configurado, la respuesta es el catálogo permitido, incluidos los modelos descubiertos dinámicamente para entradas `provider/*`. De lo contrario, la respuesta es el catálogo completo del Gateway.
  * `"configured"`: comportamiento de tamaño adecuado para selector. Si `agents.defaults.models` está configurado, sigue teniendo prioridad, incluido el descubrimiento con alcance de proveedor para entradas `provider/*`. Sin una lista de permitidos, la respuesta usa entradas explícitas de `models.providers.*.models`, recurriendo al catálogo completo solo cuando no existen filas de modelos configuradas.
  * `"all"`: catálogo completo del Gateway, omitiendo `agents.defaults.models`. Usa esto para diagnósticos e interfaces de descubrimiento, no para selectores de modelos normales.


## Aprobaciones de exec

  * Cuando una solicitud de exec necesita aprobación, el gateway difunde `exec.approval.requested`.
  * Los clientes operadores la resuelven llamando a `exec.approval.resolve` (requiere el alcance `operator.approvals`).
  * Para `host=node`, `exec.approval.request` debe incluir `systemRunPlan` (`argv`/`cwd`/`rawCommand`/metadatos de sesión canónicos). Las solicitudes que no tengan `systemRunPlan` se rechazan.
  * Después de la aprobación, las llamadas reenviadas `node.invoke system.run` reutilizan ese `systemRunPlan` canónico como contexto autoritativo de comando/cwd/sesión.
  * Si un llamador muta `command`, `rawCommand`, `cwd`, `agentId` o `sessionKey` entre la preparación y el reenvío final aprobado de `system.run`, el gateway rechaza la ejecución en lugar de confiar en la carga útil mutada.


## Fallback de entrega de agentes

  * Las solicitudes `agent` pueden incluir `deliver=true` para solicitar entrega saliente.
  * `bestEffortDeliver=false` mantiene el comportamiento estricto: los destinos de entrega no resueltos o solo internos devuelven `INVALID_REQUEST`.
  * `bestEffortDeliver=true` permite fallback a ejecución solo de sesión cuando no se puede resolver una ruta entregable externa (por ejemplo, sesiones internas/webchat o configuraciones multicanal ambiguas).
  * Los resultados finales de `agent` pueden incluir `result.deliveryStatus` cuando se haya solicitado la entrega, usando los mismos estados `sent`, `suppressed`, `partial_failed` y `failed` documentados para [`openclaw agent --json --deliver`](</es/cli/agent#json-delivery-status>).


## Versionado

  * `PROTOCOL_VERSION` vive en `src/gateway/protocol/version.ts`.
  * Los clientes envían `minProtocol` \+ `maxProtocol`; el servidor rechaza rangos que no incluyen su protocolo actual. Los clientes nativos usan un límite inferior v3 para que los clientes v4 aditivos aún puedan alcanzar gateways v3.
  * Los esquemas + modelos se generan a partir de definiciones TypeBox: 
    * `pnpm protocol:gen`
    * `pnpm protocol:gen:swift`
    * `pnpm protocol:check`


### Constantes de cliente

El cliente de referencia en `src/gateway/client.ts` usa estos valores predeterminados. Los valores son estables en el protocolo v4 y son la línea base esperada para clientes de terceros.

Constante | Valor predeterminado | Fuente  
---|---|---  
`PROTOCOL_VERSION` | `4` | `src/gateway/protocol/version.ts`  
`MIN_CLIENT_PROTOCOL_VERSION` | `3` | `src/gateway/protocol/version.ts`  
Tiempo de espera de solicitud (por RPC) | `30_000` ms | `src/gateway/client.ts` (`requestTimeoutMs`)  
Tiempo de espera de preautenticación / connect-challenge | `15_000` ms | `src/gateway/handshake-timeouts.ts` (config/env puede aumentar el presupuesto emparejado de servidor/cliente)  
Backoff de reconexión inicial | `1_000` ms | `src/gateway/client.ts` (`backoffMs`)  
Backoff máximo de reconexión | `30_000` ms | `src/gateway/client.ts` (`scheduleReconnect`)  
Límite de reintento rápido tras cierre por token de dispositivo | `250` ms | `src/gateway/client.ts`  
Periodo de gracia de detención forzada antes de `terminate()` | `250` ms | `FORCE_STOP_TERMINATE_GRACE_MS`  
Tiempo de espera predeterminado de `stopAndWait()` | `1_000` ms | `STOP_AND_WAIT_TIMEOUT_MS`  
Intervalo de tick predeterminado (antes de `hello-ok`) | `30_000` ms | `src/gateway/client.ts`  
Cierre por tiempo de espera de tick | código `4000` cuando el silencio supera `tickIntervalMs * 2` | `src/gateway/client.ts`  
`MAX_PAYLOAD_BYTES` | `25 * 1024 * 1024` (25 MB) | `src/gateway/server-constants.ts`  
  
El servidor anuncia los valores efectivos de `policy.tickIntervalMs`, `policy.maxPayload` y `policy.maxBufferedBytes` en `hello-ok`; los clientes deben respetar esos valores en lugar de los valores predeterminados previos al handshake.

## Autenticación

  * La autenticación del Gateway con secreto compartido usa `connect.params.auth.token` o `connect.params.auth.password`, según el modo de autenticación configurado.
  * Los modos con identidad, como Tailscale Serve (`gateway.auth.allowTailscale: true`) o `gateway.auth.mode: "trusted-proxy"` que no sea loopback, satisfacen la comprobación de autenticación de conexión desde los encabezados de solicitud en lugar de `connect.params.auth.*`.
  * `gateway.auth.mode: "none"` para ingreso privado omite por completo la autenticación de conexión con secreto compartido; no expongas ese modo en ingresos públicos o no confiables.
  * Después del emparejamiento, el Gateway emite un **token de dispositivo** limitado al rol y los alcances de la conexión. Se devuelve en `hello-ok.auth.deviceToken` y el cliente debe persistirlo para conexiones futuras.
  * Los clientes deben persistir el `hello-ok.auth.deviceToken` principal después de cualquier conexión correcta.
  * Al reconectar con ese token de dispositivo **almacenado** , también debe reutilizarse el conjunto de alcances aprobados almacenado para ese token. Esto conserva el acceso de lectura/sondeo/estado que ya se había concedido y evita que las reconexiones se reduzcan silenciosamente a un alcance implícito más estrecho de solo administrador.
  * Ensamblaje de autenticación de conexión del lado del cliente (`selectConnectAuth` en `src/gateway/client.ts`): 
    * `auth.password` es ortogonal y siempre se reenvía cuando está configurado.
    * `auth.token` se rellena por orden de prioridad: primero el token compartido explícito, luego un `deviceToken` explícito y después un token almacenado por dispositivo (con clave por `deviceId` \+ `role`).
    * `auth.bootstrapToken` se envía solo cuando nada de lo anterior resolvió un `auth.token`. Un token compartido o cualquier token de dispositivo resuelto lo suprime.
    * La promoción automática de un token de dispositivo almacenado en el reintento único `AUTH_TOKEN_MISMATCH` está limitada a **endpoints confiables** : loopback, o `wss://` con un `tlsFingerprint` fijado. `wss://` público sin fijación no cumple los requisitos.
  * Las entradas adicionales de `hello-ok.auth.deviceTokens` son tokens de traspaso de bootstrap. Persístelas solo cuando la conexión haya usado autenticación de bootstrap en un transporte confiable como `wss://` o emparejamiento local/loopback.
  * Si un cliente proporciona un `deviceToken` **explícito** o `scopes` explícitos, ese conjunto de alcances solicitado por el llamador sigue siendo autoritativo; los alcances en caché solo se reutilizan cuando el cliente reutiliza el token por dispositivo almacenado.
  * Los tokens de dispositivo pueden rotarse/revocarse mediante `device.token.rotate` y `device.token.revoke` (requiere el alcance `operator.pairing`).
  * `device.token.rotate` devuelve metadatos de rotación. Repite el token portador de reemplazo solo para llamadas del mismo dispositivo que ya están autenticadas con ese token de dispositivo, para que los clientes que solo usan token puedan persistir su reemplazo antes de reconectar. Las rotaciones compartidas/de administrador no repiten el token portador.
  * La emisión, rotación y revocación de tokens permanecen limitadas al conjunto de roles aprobado registrado en la entrada de emparejamiento de ese dispositivo; la mutación de tokens no puede ampliar ni dirigirse a un rol de dispositivo que la aprobación de emparejamiento nunca concedió.
  * Para sesiones de token de dispositivo emparejado, la gestión de dispositivos tiene alcance propio salvo que el llamador también tenga `operator.admin`: los llamadores que no son administradores solo pueden eliminar/revocar/rotar su **propia** entrada de dispositivo.
  * `device.token.rotate` y `device.token.revoke` también comprueban el conjunto de alcances del token de operador de destino contra los alcances de sesión actuales del llamador. Los llamadores que no son administradores no pueden rotar ni revocar un token de operador más amplio que el que ya poseen.
  * Los fallos de autenticación incluyen `error.details.code` además de sugerencias de recuperación: 
    * `error.details.canRetryWithDeviceToken` (booleano)
    * `error.details.recommendedNextStep` (`retry_with_device_token`, `update_auth_configuration`, `update_auth_credentials`, `wait_then_retry`, `review_auth_configuration`)
  * Comportamiento del cliente para `AUTH_TOKEN_MISMATCH`: 
    * Los clientes confiables pueden intentar un reintento acotado con un token por dispositivo en caché.
    * Si ese reintento falla, los clientes deben detener los bucles de reconexión automática y mostrar orientación de acción al operador.
  * `AUTH_SCOPE_MISMATCH` significa que se reconoció el token de dispositivo, pero no cubre el rol/los alcances solicitados. Los clientes no deben presentarlo como un token incorrecto; solicita al operador que vuelva a emparejar o apruebe el contrato de alcance más estrecho/amplio.


## Identidad del dispositivo + emparejamiento

  * Los nodos deben incluir una identidad de dispositivo estable (`device.id`) derivada de una huella de par de claves.
  * Los Gateways emiten tokens por dispositivo + rol.
  * Se requieren aprobaciones de emparejamiento para nuevos ID de dispositivo, salvo que la aprobación automática local esté habilitada.
  * La aprobación automática de emparejamiento se centra en conexiones directas de local loopback.
  * OpenClaw también tiene una ruta estrecha de autoconexión local de backend/contenedor para flujos auxiliares confiables con secreto compartido.
  * Las conexiones del mismo host por tailnet o LAN siguen tratándose como remotas para el emparejamiento y requieren aprobación.
  * Los clientes WS normalmente incluyen identidad `device` durante `connect` (operador + nodo). Las únicas excepciones de operador sin dispositivo son rutas de confianza explícitas: 
    * `gateway.controlUi.allowInsecureAuth=true` para compatibilidad con HTTP inseguro solo en localhost.
    * autenticación correcta de operador en Control UI con `gateway.auth.mode: "trusted-proxy"`.
    * `gateway.controlUi.dangerouslyDisableDeviceAuth=true` (ruptura de emergencia, degradación grave de seguridad).
    * RPCs backend directos por loopback de `gateway-client` autenticados con el token/contraseña compartidos del Gateway.
  * Todas las conexiones deben firmar el nonce `connect.challenge` proporcionado por el servidor.


### Diagnósticos de migración de autenticación de dispositivo

Para clientes heredados que aún usan comportamiento de firma previo al desafío, `connect` ahora devuelve códigos de detalle `DEVICE_AUTH_*` bajo `error.details.code` con un `error.details.reason` estable.

Fallos comunes de migración:

Mensaje | details.code | details.reason | Significado  
---|---|---|---  
`device nonce required` | `DEVICE_AUTH_NONCE_REQUIRED` | `device-nonce-missing` | El cliente omitió `device.nonce` (o lo envió en blanco).  
`device nonce mismatch` | `DEVICE_AUTH_NONCE_MISMATCH` | `device-nonce-mismatch` | El cliente firmó con un nonce obsoleto/incorrecto.  
`device signature invalid` | `DEVICE_AUTH_SIGNATURE_INVALID` | `device-signature` | La carga útil de firma no coincide con la carga útil v2.  
`device signature expired` | `DEVICE_AUTH_SIGNATURE_EXPIRED` | `device-signature-stale` | La marca de tiempo firmada está fuera del desfase permitido.  
`device identity mismatch` | `DEVICE_AUTH_DEVICE_ID_MISMATCH` | `device-id-mismatch` | `device.id` no coincide con la huella de la clave pública.  
`device public key invalid` | `DEVICE_AUTH_PUBLIC_KEY_INVALID` | `device-public-key` | Falló el formato/la canonicalización de la clave pública.  
  
Objetivo de migración:

  * Espera siempre a `connect.challenge`.
  * Firma la carga útil v2 que incluye el nonce del servidor.
  * Envía el mismo nonce en `connect.params.device.nonce`.
  * La carga útil de firma preferida es `v3`, que vincula `platform` y `deviceFamily` además de los campos de dispositivo/cliente/rol/alcances/token/nonce.
  * Las firmas heredadas `v2` siguen aceptándose por compatibilidad, pero la fijación de metadatos de dispositivo emparejado sigue controlando la política de comandos al reconectar.


## TLS + fijación

  * TLS es compatible con conexiones WS.
  * Los clientes pueden fijar opcionalmente la huella del certificado del gateway (consulta la configuración `gateway.tls` además de `gateway.remote.tlsFingerprint` o la CLI `--tls-fingerprint`).


## Alcance

Este protocolo expone la **API completa del gateway** (estado, canales, modelos, chat, agente, sesiones, nodos, aprobaciones, etc.). La superficie exacta está definida por los esquemas TypeBox en `src/gateway/protocol/schema.ts`.

## Relacionado

  * [Protocolo de puente](</es/gateway/bridge-protocol>)
  * [Runbook del Gateway](</es/gateway>)


Was this useful?YesNo