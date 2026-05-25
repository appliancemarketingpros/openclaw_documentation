---
title: Migración del SDK de Plugin
source_url: https://docs.openclaw.ai/es/plugins/sdk-migration
scraped_at: 2026-05-25
---

OpenClaw ha pasado de una amplia capa de compatibilidad con versiones anteriores a una arquitectura moderna de plugins con importaciones enfocadas y documentadas. Si tu plugin se creó antes de la nueva arquitectura, esta guía te ayuda a migrar.

## Qué está cambiando

El sistema de plugins anterior proporcionaba dos superficies completamente abiertas que permitían a los plugins importar todo lo que necesitaban desde un único punto de entrada:

  * **`openclaw/plugin-sdk/compat`** \- una única importación que reexportaba docenas de helpers. Se introdujo para mantener funcionando los plugins antiguos basados en hooks mientras se construía la nueva arquitectura de plugins.
  * **`openclaw/plugin-sdk/infra-runtime`** \- un amplio barrel de helpers de runtime que mezclaba eventos del sistema, estado de heartbeat, colas de entrega, helpers de fetch/proxy, helpers de archivos, tipos de aprobación y utilidades no relacionadas.
  * **`openclaw/plugin-sdk/config-runtime`** \- un amplio barrel de compatibilidad de configuración que aún conserva helpers directos de carga/escritura obsoletos durante la ventana de migración.
  * **`openclaw/extension-api`** \- un puente que daba a los plugins acceso directo a helpers del lado del host como el ejecutor de agente integrado.
  * **`api.registerEmbeddedExtensionFactory(...)`** \- un hook de extensión integrada eliminado, solo para Pi, que podía observar eventos del ejecutor integrado como `tool_result`.


Las superficies de importación amplias ahora están **obsoletas**. Todavía funcionan en runtime, pero los nuevos plugins no deben usarlas, y los plugins existentes deberían migrar antes de que la próxima versión principal las elimine. La API de registro de fábrica de extensión integrada solo para Pi se eliminó; usa middleware de resultado de herramienta en su lugar.

OpenClaw no elimina ni reinterpreta comportamiento de plugin documentado en el mismo cambio que introduce un reemplazo. Los cambios de contrato incompatibles primero deben pasar por un adaptador de compatibilidad, diagnósticos, documentación y una ventana de obsolescencia. Eso se aplica a importaciones del SDK, campos del manifiesto, API de configuración, hooks y comportamiento de registro en runtime.

## Por qué cambió esto

El enfoque anterior causaba problemas:

  * **Inicio lento** \- importar un helper cargaba docenas de módulos no relacionados
  * **Dependencias circulares** \- las reexportaciones amplias facilitaban crear ciclos de importación
  * **Superficie de API poco clara** \- no había forma de saber qué exports eran estables frente a internos


El SDK moderno de plugins corrige esto: cada ruta de importación (`openclaw/plugin-sdk/\<subpath\>`) es un módulo pequeño e independiente con un propósito claro y un contrato documentado.

Las costuras de conveniencia de providers heredadas para canales integrados también desaparecieron. Las costuras de helpers con marca de canal eran atajos privados del monorepo, no contratos estables de plugin. Usa subrutas genéricas y estrechas del SDK en su lugar. Dentro del workspace de plugins integrados, mantén los helpers propiedad del provider en el propio `api.ts` o `runtime-api.ts` de ese plugin.

Ejemplos actuales de providers integrados:

  * Anthropic mantiene helpers de stream específicos de Claude en su propia costura `api.ts` / `contract-api.ts`
  * OpenAI mantiene constructores de provider, helpers de modelo predeterminado y constructores de provider en tiempo real en su propio `api.ts`
  * OpenRouter mantiene el constructor de provider y los helpers de onboarding/configuración en su propio `api.ts`


## Plan de migración de Talk y voz en tiempo real

El código de Talk para voz en tiempo real, telefonía, reuniones y navegador se está moviendo de la contabilidad de turnos local de la superficie a un controlador compartido de sesiones Talk exportado por `openclaw/plugin-sdk/realtime-voice`. El nuevo controlador posee el sobre común de eventos de Talk, el estado de turno activo, el estado de captura, el estado de audio de salida, el historial reciente de eventos y el rechazo de turnos obsoletos. Los plugins de provider deberían seguir siendo dueños de las sesiones en tiempo real específicas del proveedor; los plugins de superficie deberían seguir siendo dueños de las particularidades de captura, reproducción, telefonía y reuniones.

Esta migración de Talk es intencionalmente una ruptura limpia:

  1. Mantén el controlador compartido y las primitivas de runtime en `plugin-sdk/realtime-voice`.
  2. Migra las superficies integradas al controlador compartido: relay de navegador, handoff de sala gestionada, llamadas de voz en tiempo real, STT en streaming de llamadas de voz, Google Meet en tiempo real y push-to-talk nativo.
  3. Sustituye las antiguas familias RPC de Talk por la API final `talk.session.*` y `talk.client.*`.
  4. Anuncia un canal de eventos Talk en vivo en Gateway `hello-ok.features.events`: `talk.event`.
  5. Elimina el antiguo endpoint HTTP en tiempo real y cualquier ruta de sobrescritura de instrucciones en tiempo de solicitud.


El código nuevo no debería llamar a `createTalkEventSequencer(...)` directamente salvo que esté implementando un adaptador de bajo nivel o una fixture de prueba. Prefiere el controlador compartido para que los eventos con alcance de turno no puedan emitirse sin un id de turno, las llamadas `turnEnd` / `turnCancel` obsoletas no puedan borrar un turno activo más nuevo, y los eventos de ciclo de vida de audio de salida permanezcan coherentes entre telefonía, reuniones, relay de navegador, handoff de sala gestionada y clientes Talk nativos.

La forma objetivo de la API pública es:

typescriptCopy code
[code]
    // Gateway-owned Talk session API.await gateway.request("talk.session.create", {  mode: "realtime",  transport: "gateway-relay",  brain: "agent-consult",  sessionKey: "main",});await gateway.request("talk.session.appendAudio", { sessionId, audioBase64 });await gateway.request("talk.session.cancelOutput", { sessionId, reason: "barge-in" });await gateway.request("talk.session.submitToolResult", {  sessionId,  callId,  result: { status: "working" },  options: { willContinue: true },});await gateway.request("talk.session.submitToolResult", {  sessionId,  callId,  result: { status: "already_delivered" },  options: { suppressResponse: true },});await gateway.request("talk.session.submitToolResult", { sessionId, callId, result });await gateway.request("talk.session.close", { sessionId }); // Client-owned provider session API.await gateway.request("talk.client.create", {  mode: "realtime",  transport: "webrtc",  brain: "agent-consult",  sessionKey: "main",});await gateway.request("talk.client.toolCall", { sessionKey, callId, name, args });
[/code]

Las sesiones WebRTC/provider-websocket propiedad del navegador usan `talk.client.create`, porque el navegador posee la negociación con el provider y el transporte de medios mientras que el Gateway posee las credenciales, las instrucciones y la política de herramientas. `talk.session.*` es la superficie común gestionada por Gateway para realtime de gateway-relay, transcripción de gateway-relay y sesiones nativas STT/TTS de salas gestionadas.

Las configuraciones heredadas que colocaban selectores en tiempo real junto a `talk.provider` / `talk.providers` deberían repararse con `openclaw doctor --fix`; Talk en runtime no reinterpreta la configuración de provider de voz/TTS como configuración de provider en tiempo real.

Las combinaciones admitidas de `talk.session.create` son intencionalmente reducidas:

Modo | Transporte | Cerebro | Propietario | Notas  
---|---|---|---|---  
`realtime` | `gateway-relay` | `agent-consult` | Gateway | Audio del provider full-duplex puenteado a través del Gateway; las llamadas a herramientas se enrutan mediante la herramienta agent-consult.  
`transcription` | `gateway-relay` | `none` | Gateway | Solo STT en streaming; los llamadores envían audio de entrada y reciben eventos de transcripción.  
`stt-tts` | `managed-room` | `agent-consult` | Sala nativa/cliente | Salas de estilo push-to-talk y walkie-talkie donde el cliente posee captura/reproducción y el Gateway posee el estado de turno.  
`stt-tts` | `managed-room` | `direct-tools` | Sala nativa/cliente | Modo de sala solo para administradores en superficies propias de confianza que ejecutan directamente acciones de herramientas del Gateway.  
  
Mapa de métodos eliminados:

Antiguo | Nuevo  
---|---  
`talk.realtime.session` | `talk.client.create`  
`talk.realtime.toolCall` | `talk.client.toolCall`  
`talk.realtime.relayAudio` | `talk.session.appendAudio`  
`talk.realtime.relayCancel` | `talk.session.cancelOutput` or `talk.session.cancelTurn`  
`talk.realtime.relayToolResult` | `talk.session.submitToolResult`  
`talk.realtime.relayStop` | `talk.session.close`  
`talk.transcription.session` | `talk.session.create({ mode: "transcription" })`  
`talk.transcription.relayAudio` | `talk.session.appendAudio`  
`talk.transcription.relayCancel` | `talk.session.cancelTurn`  
`talk.transcription.relayStop` | `talk.session.close`  
`talk.handoff.create` | `talk.session.create({ transport: "managed-room" })`  
`talk.handoff.join` | `talk.session.join`  
`talk.handoff.revoke` | `talk.session.close`  
  
El vocabulario de control unificado también es deliberadamente estrecho:

Método | Se aplica a | Contrato  
---|---|---  
`talk.session.appendAudio` | `realtime/gateway-relay`, `transcription/gateway-relay` | Añade un fragmento de audio PCM en base64 a la sesión del provider propiedad de la misma conexión Gateway.  
`talk.session.startTurn` | `stt-tts/managed-room` | Inicia un turno de usuario de sala gestionada.  
`talk.session.endTurn` | `stt-tts/managed-room` | Finaliza el turno activo después de la validación de turno obsoleto.  
`talk.session.cancelTurn` | todas las sesiones propiedad de Gateway | Cancela el trabajo activo de captura/provider/agente/TTS para un turno.  
`talk.session.cancelOutput` | `realtime/gateway-relay` | Detiene la salida de audio del asistente sin finalizar necesariamente el turno del usuario.  
`talk.session.submitToolResult` | `realtime/gateway-relay` | Completa una llamada a herramienta del provider emitida por el relay; pasa `options.willContinue` para salida provisional u `options.suppressResponse` para satisfacer la llamada sin otra respuesta del asistente.  
`talk.session.close` | todas las sesiones unificadas | Detiene las sesiones relay o revoca el estado de sala gestionada, y luego olvida el id de sesión unificado.  
  
No introduzcas casos especiales de proveedor o plataforma en el núcleo para hacer que esto funcione. El núcleo posee la semántica de las sesiones Talk. Los Plugin de proveedor poseen la configuración de sesiones del proveedor. Las llamadas de voz y Google Meet poseen los adaptadores de telefonía/reuniones. El navegador y las aplicaciones nativas poseen la UX de captura/reproducción del dispositivo.

## Política de compatibilidad

Para Plugin externos, el trabajo de compatibilidad sigue este orden:

  1. agregar el nuevo contrato
  2. mantener el comportamiento anterior conectado mediante un adaptador de compatibilidad
  3. emitir un diagnóstico o una advertencia que nombre la ruta anterior y su reemplazo
  4. cubrir ambas rutas en las pruebas
  5. documentar la obsolescencia y la ruta de migración
  6. eliminar solo después de la ventana de migración anunciada, normalmente en una versión mayor


Los mantenedores pueden auditar la cola de migración actual con `pnpm plugins:boundary-report`. Usa `pnpm plugins:boundary-report:summary` para conteos compactos, `--owner <id>` para un Plugin o propietario de compatibilidad, y `pnpm plugins:boundary-report:ci` cuando una puerta de CI deba fallar ante registros de compatibilidad vencidos, importaciones de SDK reservadas entre propietarios o subrutas de SDK reservadas sin usar. El informe agrupa los registros de compatibilidad obsoletos por fecha de eliminación, cuenta referencias locales de código/docs, muestra importaciones de SDK reservadas entre propietarios y resume el puente privado del SDK del host de memoria para que la limpieza de compatibilidad permanezca explícita en lugar de depender de búsquedas ad hoc. Las subrutas de SDK reservadas deben tener uso de propietario rastreado; las exportaciones de ayudantes reservados sin usar deben eliminarse del SDK público.

Si todavía se acepta un campo del manifiesto, los autores de Plugin pueden seguir usándolo hasta que los docs y los diagnósticos indiquen lo contrario. El código nuevo debe preferir el reemplazo documentado, pero los Plugin existentes no deben romperse durante versiones menores ordinarias.

## Cómo migrar

* ### Migrar ayudantes de carga/escritura de configuración en tiempo de ejecución

Los Plugin incluidos deben dejar de llamar directamente a `api.runtime.config.loadConfig()` y `api.runtime.config.writeConfigFile(...)`. Prefiere la configuración que ya se pasó a la ruta de llamada activa. Los controladores de larga duración que necesiten la instantánea del proceso actual pueden usar `api.runtime.config.current()`. Las herramientas de agente de larga duración deben usar `ctx.getRuntimeConfig()` del contexto de herramienta dentro de `execute` para que una herramienta creada antes de una escritura de configuración siga viendo la configuración de tiempo de ejecución actualizada.

Las escrituras de configuración deben pasar por los ayudantes transaccionales y elegir una política posterior a la escritura:

typescriptCopy code
[code]
    await api.runtime.config.mutateConfigFile({  afterWrite: { mode: "auto" },  mutate(draft) {    draft.plugins ??= {};  },});
[/code]

Usa `afterWrite: { mode: "restart", reason: "..." }` cuando el llamador sabe que el cambio requiere un reinicio limpio del gateway, y `afterWrite: { mode: "none", reason: "..." }` solo cuando el llamador posee el seguimiento y quiere suprimir deliberadamente el planificador de recarga. Los resultados de mutación incluyen un resumen `followUp` tipado para pruebas y registro; el gateway sigue siendo responsable de aplicar o programar el reinicio. `loadConfig` y `writeConfigFile` permanecen como ayudantes de compatibilidad obsoletos para Plugin externos durante la ventana de migración y advierten una vez con el código de compatibilidad `runtime-config-load-write`. Los Plugin incluidos y el código de tiempo de ejecución del repositorio están protegidos por barreras del escáner en `pnpm check:deprecated-api-usage` y `pnpm check:no-runtime-action-load-config`: el uso nuevo de Plugin de producción falla directamente, las escrituras directas de configuración fallan, los métodos del servidor gateway deben usar la instantánea de tiempo de ejecución de la solicitud, los ayudantes de envío/acción/cliente de canal en tiempo de ejecución deben recibir la configuración desde su límite, y los módulos de tiempo de ejecución de larga duración tienen cero llamadas ambientales permitidas a `loadConfig()`.

El código nuevo de Plugin también debe evitar importar el barril amplio de compatibilidad `openclaw/plugin-sdk/config-runtime`. Usa la subruta estrecha del SDK que coincida con la tarea:

Necesidad | Importación  
---|---  
Tipos de configuración como `OpenClawConfig` | `openclaw/plugin-sdk/config-contracts`  
Aserciones de configuración ya cargada y búsqueda de configuración de entrada de Plugin | `openclaw/plugin-sdk/plugin-config-runtime`  
Lecturas de la instantánea actual de tiempo de ejecución | `openclaw/plugin-sdk/runtime-config-snapshot`  
Escrituras de configuración | `openclaw/plugin-sdk/config-mutation`  
Ayudantes de almacén de sesiones | `openclaw/plugin-sdk/session-store-runtime`  
Configuración de tabla Markdown | `openclaw/plugin-sdk/markdown-table-runtime`  
Ayudantes de tiempo de ejecución de política de grupo | `openclaw/plugin-sdk/runtime-group-policy`  
Resolución de entrada secreta | `openclaw/plugin-sdk/secret-input-runtime`  
Sobrescrituras de modelo/sesión | `openclaw/plugin-sdk/model-session-runtime`  
  
Los Plugin incluidos y sus pruebas están protegidos por escáner contra el barril amplio para que las importaciones y los mocks permanezcan locales al comportamiento que necesitan. El barril amplio todavía existe por compatibilidad externa, pero el código nuevo no debe depender de él.

* ### Migrar extensiones de resultados de herramientas de Pi a middleware

Los Plugin incluidos deben reemplazar los controladores de resultados de herramientas exclusivos de Pi `api.registerEmbeddedExtensionFactory(...)` con middleware neutral respecto al tiempo de ejecución.

typescriptCopy code
[code]
    // Pi and Codex runtime dynamic toolsapi.registerAgentToolResultMiddleware(async (event) => {  return compactToolResult(event);}, {  runtimes: ["pi", "codex"],});
[/code]

Actualiza el manifiesto del Plugin al mismo tiempo:

jsonCopy code
[code]
    {  "contracts": {    "agentToolResultMiddleware": ["pi", "codex"]  }}
[/code]

Los Plugin externos no pueden registrar middleware de resultados de herramientas porque puede reescribir salidas de herramientas de alta confianza antes de que el modelo las vea.

* ### Migrar controladores nativos de aprobación a hechos de capacidad

Los Plugin de canal con capacidad de aprobación ahora exponen comportamiento de aprobación nativo mediante `approvalCapability.nativeRuntime` más el registro compartido de contexto de tiempo de ejecución.

Cambios clave:

  * Reemplaza `approvalCapability.handler.loadRuntime(...)` con `approvalCapability.nativeRuntime`
  * Mueve autenticación/entrega específicas de aprobación fuera del cableado heredado de `plugin.auth` / `plugin.approvals` y hacia `approvalCapability`
  * `ChannelPlugin.approvals` se eliminó del contrato público de Plugin de canal; mueve los campos de entrega/nativo/renderizado a `approvalCapability`
  * `plugin.auth` permanece solo para flujos de inicio/cierre de sesión de canal; los hooks de autenticación de aprobación allí ya no los lee el núcleo
  * Registra objetos de tiempo de ejecución propiedad del canal, como clientes, tokens o aplicaciones Bolt, mediante `openclaw/plugin-sdk/channel-runtime-context`
  * No envíes avisos de redirección propiedad del Plugin desde controladores de aprobación nativos; el núcleo ahora posee los avisos de enrutado a otro lugar a partir de resultados reales de entrega
  * Al pasar `channelRuntime` a `createChannelManager(...)`, proporciona una superficie real de `createPluginRuntime().channel`. Los stubs parciales se rechazan.


Consulta `/plugins/sdk-channel-plugins` para ver el diseño actual de capacidad de aprobación.

* ### Auditar el comportamiento de reserva del wrapper de Windows

Si tu Plugin usa `openclaw/plugin-sdk/windows-spawn`, los wrappers `.cmd`/`.bat` de Windows no resueltos ahora fallan cerrados salvo que pases explícitamente `allowShellFallback: true`.

typescriptCopy code
[code]
    // Beforeconst program = applyWindowsSpawnProgramPolicy({ candidate }); // Afterconst program = applyWindowsSpawnProgramPolicy({  candidate,  // Only set this for trusted compatibility callers that intentionally  // accept shell-mediated fallback.  allowShellFallback: true,});
[/code]

Si tu llamador no depende intencionalmente de la reserva mediante shell, no establezcas `allowShellFallback` y maneja el error lanzado en su lugar.

* ### Buscar importaciones obsoletas

Busca en tu Plugin importaciones desde cualquiera de las superficies obsoletas:

bashCopy code
[code]
    grep -r "plugin-sdk/compat" my-plugin/grep -r "plugin-sdk/infra-runtime" my-plugin/grep -r "plugin-sdk/config-runtime" my-plugin/grep -r "openclaw/extension-api" my-plugin/
[/code]

* ### Reemplazar con importaciones enfocadas

Cada exportación de la superficie anterior se asigna a una ruta de importación moderna específica:

typescriptCopy code
[code]
    // Before (deprecated backwards-compatibility layer)import {  createChannelReplyPipeline,  createPluginRuntimeStore,  resolveControlCommandGate,} from "openclaw/plugin-sdk/compat"; // After (modern focused imports)import { createChannelReplyPipeline } from "openclaw/plugin-sdk/channel-reply-pipeline";import { createPluginRuntimeStore } from "openclaw/plugin-sdk/runtime-store";import { resolveControlCommandGate } from "openclaw/plugin-sdk/command-auth";
[/code]

Para ayudantes del lado del host, usa el tiempo de ejecución de Plugin inyectado en lugar de importar directamente:

typescriptCopy code
[code]
    // Before (deprecated extension-api bridge)import { runEmbeddedPiAgent } from "openclaw/extension-api";const result = await runEmbeddedPiAgent({ sessionId, prompt }); // After (injected runtime)const result = await api.runtime.agent.runEmbeddedPiAgent({ sessionId, prompt });
[/code]

El mismo patrón se aplica a otros ayudantes de puente heredados:

Importación anterior | Equivalente moderno  
---|---  
`resolveAgentDir` | `api.runtime.agent.resolveAgentDir`  
`resolveAgentWorkspaceDir` | `api.runtime.agent.resolveAgentWorkspaceDir`  
`resolveAgentIdentity` | `api.runtime.agent.resolveAgentIdentity`  
`resolveThinkingDefault` | `api.runtime.agent.resolveThinkingDefault`  
`resolveAgentTimeoutMs` | `api.runtime.agent.resolveAgentTimeoutMs`  
`ensureAgentWorkspace` | `api.runtime.agent.ensureAgentWorkspace`  
ayudantes de almacén de sesiones | `api.runtime.agent.session.*`  
* ### Reemplazar importaciones amplias de infra-runtime

`openclaw/plugin-sdk/infra-runtime` todavía existe por compatibilidad externa, pero el código nuevo debe importar la superficie enfocada de ayudantes que realmente necesita:

Necesidad | Importación  
---|---  
Ayudantes de cola de eventos del sistema | `openclaw/plugin-sdk/system-event-runtime`  
Ayudantes de activación, evento y visibilidad de Heartbeat | `openclaw/plugin-sdk/heartbeat-runtime`  
Vaciado de cola de entregas pendientes | `openclaw/plugin-sdk/delivery-queue-runtime`  
Telemetría de actividad de canal | `openclaw/plugin-sdk/channel-activity-runtime`  
Cachés de deduplicación en memoria | `openclaw/plugin-sdk/dedupe-runtime`  
Ayudantes seguros de rutas de archivos locales/medios | `openclaw/plugin-sdk/file-access-runtime`  
Fetch consciente del despachador | `openclaw/plugin-sdk/runtime-fetch`  
Ayudantes de proxy y fetch protegido | `openclaw/plugin-sdk/fetch-runtime`  
Tipos de política de despachador SSRF | `openclaw/plugin-sdk/ssrf-dispatcher`  
Tipos de solicitud/resolución de aprobación | `openclaw/plugin-sdk/approval-runtime`  
Ayudantes de payload de respuesta de aprobación y comandos | `openclaw/plugin-sdk/approval-reply-runtime`  
Ayudantes de formato de errores | `openclaw/plugin-sdk/error-runtime`  
Esperas de disponibilidad de transporte | `openclaw/plugin-sdk/transport-ready-runtime`  
Ayudantes de tokens seguros | `openclaw/plugin-sdk/secure-random-runtime`  
Concurrencia acotada de tareas asíncronas | `openclaw/plugin-sdk/concurrency-runtime`  
Coerción numérica | `openclaw/plugin-sdk/number-runtime`  
Bloqueo asíncrono local al proceso | `openclaw/plugin-sdk/async-lock-runtime`  
Bloqueos de archivos | `openclaw/plugin-sdk/file-lock`  
  
Los Plugin incluidos están protegidos por escáner contra `infra-runtime`, por lo que el código del repositorio no puede retroceder al barril amplio.

* ### Migrar ayudantes de rutas de canal

El código nuevo de rutas de canal debe usar `openclaw/plugin-sdk/channel-route`. Los nombres anteriores de clave de ruta y destino comparable permanecen como alias de compatibilidad durante la ventana de migración, pero los Plugin nuevos deben usar los nombres de ruta que describen el comportamiento directamente:

Función auxiliar antigua | Función auxiliar moderna  
---|---  
`channelRouteIdentityKey(...)` | `channelRouteDedupeKey(...)`  
`channelRouteKey(...)` | `channelRouteCompactKey(...)`  
`ComparableChannelTarget` | `ChannelRouteParsedTarget`  
`resolveComparableTargetForChannel(...)` | `resolveRouteTargetForChannel(...)`  
`resolveComparableTargetForLoadedChannel(...)` | `resolveRouteTargetForLoadedChannel(...)`  
`comparableChannelTargetsMatch(...)` | `channelRouteTargetsMatchExact(...)`  
`comparableChannelTargetsShareRoute(...)` | `channelRouteTargetsShareConversation(...)`  
  
Las funciones auxiliares de ruta modernas normalizan `{ channel, to, accountId, threadId }` de forma coherente en aprobaciones nativas, supresión de respuestas, desduplicación de entrada, entrega de Cron y enrutamiento de sesiones. Si tu Plugin posee una gramática de destino personalizada, usa `resolveChannelRouteTargetWithParser(...)` para adaptar ese analizador al mismo contrato de destino de ruta.

* ### Compilar y probar

bashCopy code
[code]
    pnpm buildpnpm test -- my-plugin/
[/code]

## Referencia de rutas de importación

Tabla de rutas de importación comunes Ruta de importación | Propósito | Exportaciones clave  
---|---|---  
`plugin-sdk/plugin-entry` | Helper de entrada de plugin canónico | `definePluginEntry`  
`plugin-sdk/core` | Reexportación paraguas heredada para definiciones/constructores de entradas de canal | `defineChannelPluginEntry`, `createChatChannelPlugin`  
`plugin-sdk/config-schema` | Exportación del esquema de configuración raíz | `OpenClawSchema`  
`plugin-sdk/provider-entry` | Helper de entrada de proveedor único | `defineSingleProviderPluginEntry`  
`plugin-sdk/channel-core` | Definiciones y constructores enfocados de entradas de canal | `defineChannelPluginEntry`, `defineSetupPluginEntry`, `createChatChannelPlugin`, `createChannelPluginBase`  
`plugin-sdk/setup` | Helpers compartidos del asistente de configuración | Prompts de lista de permitidos, constructores de estado de configuración  
`plugin-sdk/setup-runtime` | Helpers de runtime para tiempo de configuración | Adaptadores de parche de configuración seguros para importar, helpers de notas de búsqueda, `promptResolvedAllowFrom`, `splitSetupEntries`, proxies de configuración delegada  
`plugin-sdk/setup-adapter-runtime` | Alias de adaptador de configuración obsoleto | Usa `plugin-sdk/setup-runtime`  
`plugin-sdk/setup-tools` | Helpers de herramientas de configuración | `formatCliCommand`, `detectBinary`, `extractArchive`, `resolveBrewExecutable`, `formatDocsLink`, `CONFIG_DIR`  
`plugin-sdk/account-core` | Helpers multicuenta | Helpers de lista/configuración/puerta de acción de cuentas  
`plugin-sdk/account-id` | Helpers de id de cuenta | `DEFAULT_ACCOUNT_ID`, normalización de id de cuenta  
`plugin-sdk/account-resolution` | Helpers de búsqueda de cuentas | Helpers de búsqueda de cuentas y fallback predeterminado  
`plugin-sdk/account-helpers` | Helpers acotados de cuentas | Helpers de lista de cuentas/acciones de cuenta  
`plugin-sdk/channel-setup` | Adaptadores del asistente de configuración | `createOptionalChannelSetupSurface`, `createOptionalChannelSetupAdapter`, `createOptionalChannelSetupWizard`, además de `DEFAULT_ACCOUNT_ID`, `createTopLevelChannelDmPolicy`, `setSetupChannelEnabled`, `splitSetupEntries`  
`plugin-sdk/channel-pairing` | Primitivas de emparejamiento de DM | `createChannelPairingController`  
`plugin-sdk/channel-reply-pipeline` | Cableado de prefijo de respuesta, escritura y entrega de origen | `createChannelReplyPipeline`, `resolveChannelSourceReplyDeliveryMode`  
`plugin-sdk/channel-config-helpers` | Fábricas de adaptadores de configuración y helpers de acceso a DM | `createHybridChannelConfigAdapter`, `resolveChannelDmAccess`, `resolveChannelDmAllowFrom`, `resolveChannelDmPolicy`, `normalizeChannelDmPolicy`, `normalizeLegacyDmAliases`  
`plugin-sdk/channel-config-schema` | Constructores de esquemas de configuración | Primitivas compartidas de esquema de configuración de canal y solo el constructor genérico  
`plugin-sdk/bundled-channel-config-schema` | Esquemas de configuración incluidos | Solo plugins incluidos mantenidos por OpenClaw; los plugins nuevos deben definir esquemas locales del plugin  
`plugin-sdk/channel-config-schema-legacy` | Esquemas de configuración incluidos obsoletos | Solo alias de compatibilidad; usa `plugin-sdk/bundled-channel-config-schema` para plugins incluidos mantenidos  
`plugin-sdk/telegram-command-config` | Helpers de configuración de comandos de Telegram | Normalización de nombres de comando, recorte de descripciones, validación de duplicados/conflictos  
`plugin-sdk/channel-policy` | Resolución de políticas de grupo/DM | `resolveChannelGroupRequireMention`  
`plugin-sdk/channel-lifecycle` | Helpers de estado de cuenta y ciclo de vida del flujo de borradores | `createAccountStatusSink`, helpers de finalización de vista previa de borrador  
`plugin-sdk/inbound-envelope` | Helpers de sobre entrante | Helpers compartidos de ruta y constructor de sobre  
`plugin-sdk/inbound-reply-dispatch` | Helpers de respuesta entrante | Helpers compartidos de registro y despacho  
`plugin-sdk/messaging-targets` | Análisis de destino de mensajería | Helpers de análisis/coincidencia de destinos  
`plugin-sdk/outbound-media` | Helpers de medios salientes | Carga compartida de medios salientes  
`plugin-sdk/outbound-send-deps` | Helpers de dependencias de envío saliente | Búsqueda ligera de `resolveOutboundSendDep` sin importar el runtime saliente completo  
`plugin-sdk/outbound-runtime` | Helpers de runtime saliente | Helpers de entrega saliente, delegado de identidad/envío, sesión, formato y planificación de payload  
`plugin-sdk/thread-bindings-runtime` | Helpers de enlace de hilos | Helpers de ciclo de vida de enlaces de hilos y adaptadores  
`plugin-sdk/agent-media-payload` | Helpers heredados de payload multimedia | Constructor de payload multimedia de agente para diseños de campos heredados  
`plugin-sdk/channel-runtime` | Shim de compatibilidad obsoleto | Solo utilidades heredadas de runtime de canal  
`plugin-sdk/channel-send-result` | Tipos de resultado de envío | Tipos de resultado de respuesta  
`plugin-sdk/runtime-store` | Almacenamiento persistente de plugin | `createPluginRuntimeStore`  
`plugin-sdk/runtime` | Helpers amplios de runtime | Helpers de runtime/registro/copia de seguridad/instalación de plugins  
`plugin-sdk/runtime-env` | Helpers acotados de entorno de runtime | Logger/entorno de runtime, timeout, reintento y backoff  
`plugin-sdk/plugin-runtime` | Helpers compartidos de runtime de plugin | Helpers de comandos/hooks/http/interactivos de plugin  
`plugin-sdk/hook-runtime` | Helpers de pipeline de hooks | Helpers compartidos de pipeline de webhook/hook interno  
`plugin-sdk/lazy-runtime` | Helpers de runtime diferido | `createLazyRuntimeModule`, `createLazyRuntimeMethod`, `createLazyRuntimeMethodBinder`, `createLazyRuntimeNamedExport`, `createLazyRuntimeSurface`  
`plugin-sdk/process-runtime` | Helpers de proceso | Helpers compartidos de exec  
`plugin-sdk/cli-runtime` | Helpers de runtime de CLI | Formato de comandos, esperas, helpers de versión  
`plugin-sdk/gateway-runtime` | Helpers de Gateway | Cliente de Gateway, helper de inicio listo para bucle de eventos y helpers de parche de estado de canal  
`plugin-sdk/config-runtime` | Shim de compatibilidad de configuración obsoleto | Prefiere `config-contracts`, `plugin-config-runtime`, `runtime-config-snapshot` y `config-mutation`  
`plugin-sdk/telegram-command-config` | Helpers de comandos de Telegram | Helpers de validación de comandos de Telegram estables con fallback cuando la superficie de contrato incluida de Telegram no está disponible  
`plugin-sdk/approval-runtime` | Helpers de prompt de aprobación | Payload de aprobación de exec/plugin, helpers de capacidad/perfil de aprobación, helpers de enrutamiento/runtime de aprobación nativa y formato de ruta de visualización de aprobación estructurada  
`plugin-sdk/approval-auth-runtime` | Helpers de autenticación de aprobación | Resolución de aprobador, autenticación de acción en el mismo chat  
`plugin-sdk/approval-client-runtime` | Helpers de cliente de aprobación | Helpers nativos de perfil/filtro de aprobación de exec  
`plugin-sdk/approval-delivery-runtime` | Helpers de entrega de aprobación | Adaptadores nativos de capacidad/entrega de aprobación  
`plugin-sdk/approval-gateway-runtime` | Helpers de Gateway de aprobación | Helper compartido de resolución de Gateway de aprobación  
`plugin-sdk/approval-handler-adapter-runtime` | Helpers de adaptador de aprobación | Helpers ligeros de carga de adaptador de aprobación nativa para puntos de entrada de canal activos  
`plugin-sdk/approval-handler-runtime` | Helpers de gestor de aprobación | Helpers de runtime de gestor de aprobación más amplios; prefiere las superficies más acotadas de adaptador/Gateway cuando sean suficientes  
`plugin-sdk/approval-native-runtime` | Helpers de destino de aprobación | Helpers nativos de enlace de destino/cuenta de aprobación  
`plugin-sdk/approval-reply-runtime` | Helpers de respuesta de aprobación | Helpers de payload de respuesta de aprobación de exec/plugin  
`plugin-sdk/channel-runtime-context` | Helpers de contexto de runtime de canal | Helpers genéricos de registrar/obtener/observar contexto de runtime de canal  
`plugin-sdk/security-runtime` | Helpers de seguridad | Helpers compartidos de confianza, control de DM, archivo/ruta acotados a la raíz, contenido externo y recopilación de secretos  
`plugin-sdk/ssrf-policy` | Helpers de política SSRF | Helpers de lista de hosts permitidos y política de red privada  
`plugin-sdk/ssrf-runtime` | Helpers de runtime SSRF | Dispatcher fijado, fetch protegido, helpers de política SSRF  
`plugin-sdk/system-event-runtime` | Helpers de eventos del sistema | `enqueueSystemEvent`, `peekSystemEventEntries`  
`plugin-sdk/heartbeat-runtime` | Helpers de Heartbeat | Helpers de activación, evento y visibilidad de Heartbeat  
`plugin-sdk/delivery-queue-runtime` | Helpers de cola de entrega | `drainPendingDeliveries`  
`plugin-sdk/channel-activity-runtime` | Helpers de actividad de canal | `recordChannelActivity`  
`plugin-sdk/dedupe-runtime` | Helpers de deduplicación | Cachés de deduplicación en memoria  
`plugin-sdk/file-access-runtime` | Helpers de acceso a archivos | Helpers seguros de rutas de archivos/medios locales  
`plugin-sdk/transport-ready-runtime` | Helpers de disponibilidad de transporte | `waitForTransportReady`  
`plugin-sdk/collection-runtime` | Helpers de caché acotada | `pruneMapToMaxSize`  
`plugin-sdk/diagnostic-runtime` | Helpers de control de diagnósticos | `isDiagnosticFlagEnabled`, `isDiagnosticsEnabled`  
`plugin-sdk/error-runtime` | Helpers de formato de errores | `formatUncaughtError`, `isApprovalNotFoundError`, helpers de grafo de errores  
`plugin-sdk/fetch-runtime` | Helpers de fetch/proxy envueltos | `resolveFetch`, helpers de proxy, helpers de opciones de EnvHttpProxyAgent  
`plugin-sdk/host-runtime` | Helpers de normalización de host | `normalizeHostname`, `normalizeScpRemoteHost`  
`plugin-sdk/retry-runtime` | Helpers de reintento | `RetryConfig`, `retryAsync`, ejecutores de políticas  
`plugin-sdk/allow-from` | Formato de lista de permitidos | `formatAllowFromLowercase`  
`plugin-sdk/allowlist-resolution` | Mapeo de entrada de lista de permitidos | `mapAllowlistResolutionInputs`  
`plugin-sdk/command-auth` | Control de comandos y helpers de superficie de comandos | `resolveControlCommandGate`, helpers de autorización de remitente, helpers de registro de comandos incluido el formato de menú de argumentos dinámicos  
`plugin-sdk/command-status` | Renderizadores de estado/ayuda de comandos | `buildCommandsMessage`, `buildCommandsMessagePaginated`, `buildHelpMessage`  
`plugin-sdk/secret-input` | Análisis de entrada secreta | Helpers de entrada secreta  
`plugin-sdk/webhook-ingress` | Helpers de solicitud de Webhook | Utilidades de destino de Webhook  
`plugin-sdk/webhook-request-guards` | Helpers de protección de cuerpo de Webhook | Helpers de lectura/límite de cuerpo de solicitud  
`plugin-sdk/reply-runtime` | Runtime compartido de respuesta | Despacho entrante, Heartbeat, planificador de respuestas, fragmentación  
`plugin-sdk/reply-dispatch-runtime` | Helpers acotados de despacho de respuestas | Helpers de finalización, despacho de proveedor y etiqueta de conversación  
`plugin-sdk/reply-history` | Helpers de historial de respuestas | `buildHistoryContext`, `buildPendingHistoryContextFromMap`, `recordPendingHistoryEntry`, `clearHistoryEntriesIfEnabled`  
`plugin-sdk/reply-reference` | Planificación de referencia de respuesta | `createReplyReferencePlanner`  
`plugin-sdk/reply-chunking` | Helpers de fragmentos de respuesta | Helpers de fragmentación de texto/markdown  
`plugin-sdk/session-store-runtime` | Helpers de almacén de sesión | Helpers de ruta de almacén y fecha de actualización  
`plugin-sdk/state-paths` | Helpers de rutas de estado | Helpers de estado y directorio OAuth  
`plugin-sdk/routing` | Helpers de enrutamiento/clave de sesión | `resolveAgentRoute`, `buildAgentSessionKey`, `resolveDefaultAgentBoundAccountId`, helpers de normalización de clave de sesión  
`plugin-sdk/status-helpers` | Helpers de estado de canal | Constructores de resumen de estado de canal/cuenta, valores predeterminados de estado de runtime, helpers de metadatos de incidencia  
`plugin-sdk/target-resolver-runtime` | Helpers de resolvedor de destinos | Helpers compartidos de resolvedor de destinos  
`plugin-sdk/string-normalization-runtime` | Helpers de normalización de cadenas | Helpers de normalización de slug/cadena  
`plugin-sdk/request-url` | Helpers de URL de solicitud | Extraer URL de cadena desde entradas similares a solicitudes  
`plugin-sdk/run-command` | Helpers de comandos temporizados | Ejecutor de comandos temporizados con stdout/stderr normalizados  
`plugin-sdk/param-readers` | Lectores de parámetros | Lectores comunes de parámetros de herramientas/CLI  
`plugin-sdk/tool-payload` | Extracción de payload de herramienta | Extrae payloads normalizados de objetos de resultado de herramienta  
`plugin-sdk/tool-send` | Extracción de envío de herramienta | Extrae los campos canónicos de destino de envío desde argumentos de herramienta  
`plugin-sdk/temp-path` | Ayudantes de rutas temporales | Ayudantes compartidos de rutas de descarga temporal  
`plugin-sdk/logging-core` | Ayudantes de registro | Ayudantes de registrador de subsistema y redacción  
`plugin-sdk/markdown-table-runtime` | Ayudantes de tablas Markdown | Ayudantes de modo de tabla Markdown  
`plugin-sdk/reply-payload` | Tipos de respuesta de mensaje | Tipos de payload de respuesta  
`plugin-sdk/provider-setup` | Ayudantes seleccionados para configurar proveedores locales/autoalojados | Ayudantes de descubrimiento/configuración de proveedores autoalojados  
`plugin-sdk/self-hosted-provider-setup` | Ayudantes enfocados para configurar proveedores autoalojados compatibles con OpenAI | Los mismos ayudantes de descubrimiento/configuración de proveedores autoalojados  
`plugin-sdk/provider-auth-runtime` | Ayudantes de autenticación en runtime de proveedores | Ayudantes de resolución de claves de API en runtime  
`plugin-sdk/provider-auth-api-key` | Ayudantes de configuración de claves de API de proveedores | Ayudantes de incorporación/escritura de perfiles con claves de API  
`plugin-sdk/provider-auth-result` | Ayudantes de resultado de autenticación de proveedores | Constructor estándar de resultado de autenticación OAuth  
`plugin-sdk/provider-selection-runtime` | Ayudantes de selección de proveedores | Selección de proveedor configurado o automático y combinación de configuración sin procesar de proveedor  
`plugin-sdk/provider-env-vars` | Ayudantes de variables de entorno de proveedores | Ayudantes de búsqueda de variables de entorno de autenticación de proveedores  
`plugin-sdk/provider-model-shared` | Ayudantes compartidos de modelos/reproducción de proveedores | `ProviderReplayFamily`, `buildProviderReplayFamilyHooks`, `normalizeModelCompat`, constructores compartidos de políticas de reproducción, ayudantes de endpoints de proveedor y ayudantes de normalización de ID de modelo  
`plugin-sdk/provider-catalog-shared` | Ayudantes compartidos de catálogo de proveedores | `findCatalogTemplate`, `buildSingleProviderApiKeyCatalog`, `buildManifestModelProviderConfig`, `supportsNativeStreamingUsageCompat`, `applyProviderNativeStreamingUsageCompat`  
`plugin-sdk/provider-onboard` | Parches de incorporación de proveedores | Ayudantes de configuración de incorporación  
`plugin-sdk/provider-http` | Ayudantes HTTP de proveedores | Ayudantes genéricos de capacidades HTTP/endpoint de proveedores, incluidos los ayudantes de formulario multiparte para transcripción de audio  
`plugin-sdk/provider-web-fetch` | Ayudantes de web-fetch de proveedores | Ayudantes de registro/caché de proveedores de web-fetch  
`plugin-sdk/provider-web-search-config-contract` | Ayudantes de configuración de búsqueda web de proveedores | Ayudantes específicos de configuración/credenciales de búsqueda web para proveedores que no necesitan cableado de activación de plugin  
`plugin-sdk/provider-web-search-contract` | Ayudantes de contrato de búsqueda web de proveedores | Ayudantes específicos de contrato de configuración/credenciales de búsqueda web, como `createWebSearchProviderContractFields`, `enablePluginInConfig`, `resolveProviderWebSearchPluginConfig`, y setters/getters de credenciales con ámbito  
`plugin-sdk/provider-web-search` | Ayudantes de búsqueda web de proveedores | Ayudantes de registro/caché/runtime de proveedores de búsqueda web  
`plugin-sdk/provider-tools` | Ayudantes de compatibilidad de herramientas/esquemas de proveedores | `ProviderToolCompatFamily`, `buildProviderToolCompatFamilyHooks`, y limpieza de esquemas de Gemini + diagnósticos  
`plugin-sdk/provider-usage` | Ayudantes de uso de proveedores | `fetchClaudeUsage`, `fetchGeminiUsage`, `fetchGithubCopilotUsage`, y otros ayudantes de uso de proveedores  
`plugin-sdk/provider-stream` | Ayudantes de envoltorios de flujo de proveedores | `ProviderStreamFamily`, `buildProviderStreamFamilyHooks`, `composeProviderStreamWrappers`, tipos de envoltorios de flujo y ayudantes compartidos de envoltorios para Anthropic/Bedrock/DeepSeek V4/Google/Kilocode/Moonshot/OpenAI/OpenRouter/Z.A.I/MiniMax/Copilot  
`plugin-sdk/provider-transport-runtime` | Ayudantes de transporte de proveedores | Ayudantes de transporte nativo de proveedores, como fetch protegido, transformaciones de mensajes de transporte y flujos de eventos de transporte escribibles  
`plugin-sdk/keyed-async-queue` | Cola asíncrona ordenada | `KeyedAsyncQueue`  
`plugin-sdk/media-runtime` | Ayudantes multimedia compartidos | Ayudantes de obtención/transformación/almacenamiento de medios, sondeo de dimensiones de video basado en ffprobe y constructores de payloads multimedia  
`plugin-sdk/media-generation-runtime` | Ayudantes compartidos de generación multimedia | Ayudantes compartidos de conmutación por error, selección de candidatos y mensajes de modelo faltante para generación de imágenes/video/música  
`plugin-sdk/media-understanding` | Ayudantes de comprensión multimedia | Tipos de proveedores de comprensión multimedia y exportaciones de ayudantes de imagen/audio orientadas a proveedores  
`plugin-sdk/text-runtime` | Exportación amplia obsoleta de compatibilidad de texto | Usa `string-coerce-runtime`, `text-chunking`, `text-utility-runtime` y `logging-core`  
`plugin-sdk/text-chunking` | Ayudantes de fragmentación de texto | Ayudante de fragmentación de texto saliente  
`plugin-sdk/speech` | Ayudantes de voz | Tipos de proveedores de voz más ayudantes de directivas, registro y validación orientados a proveedores, y constructor TTS compatible con OpenAI  
`plugin-sdk/speech-core` | Núcleo de voz compartido | Tipos de proveedores de voz, registro, directivas, normalización  
`plugin-sdk/realtime-transcription` | Ayudantes de transcripción en tiempo real | Tipos de proveedores, ayudantes de registro y ayudante compartido de sesión WebSocket  
`plugin-sdk/realtime-voice` | Ayudantes de voz en tiempo real | Tipos de proveedores, ayudantes de registro/resolución, ayudantes de sesión de puente, colas compartidas de respuesta de agente, estado de transcripción/eventos, supresión de eco y ayudantes rápidos de consulta de contexto  
`plugin-sdk/image-generation` | Ayudantes de generación de imágenes | Tipos de proveedores de generación de imágenes más ayudantes de URL de datos/recursos de imagen y el constructor de proveedor de imágenes compatible con OpenAI  
`plugin-sdk/image-generation-core` | Núcleo compartido de generación de imágenes | Tipos de generación de imágenes, conmutación por error, autenticación y ayudantes de registro  
`plugin-sdk/music-generation` | Ayudantes de generación de música | Tipos de proveedor/solicitud/resultado de generación de música  
`plugin-sdk/music-generation-core` | Núcleo compartido de generación de música | Tipos de generación de música, ayudantes de conmutación por error, búsqueda de proveedores y análisis de referencias de modelo  
`plugin-sdk/video-generation` | Ayudantes de generación de video | Tipos de proveedor/solicitud/resultado de generación de video  
`plugin-sdk/video-generation-core` | Núcleo compartido de generación de video | Tipos de generación de video, ayudantes de conmutación por error, búsqueda de proveedores y análisis de referencias de modelo  
`plugin-sdk/interactive-runtime` | Ayudantes de respuesta interactiva | Normalización/reducción de payloads de respuesta interactiva  
`plugin-sdk/channel-config-primitives` | Primitivas de configuración de canales | Primitivas específicas de esquema de configuración de canales  
`plugin-sdk/channel-config-writes` | Ayudantes de escritura de configuración de canales | Ayudantes de autorización de escritura de configuración de canales  
`plugin-sdk/channel-plugin-common` | Preludio compartido de canales | Exportaciones compartidas de preludio de plugins de canal  
`plugin-sdk/channel-status` | Ayudantes de estado de canales | Ayudantes compartidos de instantánea/resumen de estado de canales  
`plugin-sdk/allowlist-config-edit` | Ayudantes de configuración de lista de permitidos | Ayudantes de edición/lectura de configuración de lista de permitidos  
`plugin-sdk/group-access` | Ayudantes de acceso grupal | Ayudantes compartidos de decisión de acceso grupal  
`plugin-sdk/direct-dm` | Ayudantes de DM directo | Ayudantes compartidos de autenticación/protección de DM directo  
`plugin-sdk/extension-shared` | Ayudantes compartidos de extensión | Primitivas de ayudantes de canal pasivo/estado y proxy ambiental  
`plugin-sdk/webhook-targets` | Ayudantes de destino de Webhook | Ayudantes de registro de destinos de Webhook e instalación de rutas  
`plugin-sdk/webhook-path` | Alias obsoleto de ruta de Webhook | Usa `plugin-sdk/webhook-ingress`  
`plugin-sdk/web-media` | Ayudantes compartidos de medios web | Ayudantes de carga de medios remotos/locales  
`plugin-sdk/zod` | Reexportación obsoleta de compatibilidad con Zod | Importa `zod` desde `zod` directamente  
`plugin-sdk/memory-core` | Ayudantes memory-core incluidos | Superficie de ayudantes de administrador/configuración/archivo/CLI de memoria  
`plugin-sdk/memory-core-engine-runtime` | Fachada de runtime del motor de memoria | Fachada de runtime de índice/búsqueda de memoria  
`plugin-sdk/memory-core-host-engine-foundation` | Motor de base del host de memoria | Exportaciones del motor de base del host de memoria  
`plugin-sdk/memory-core-host-engine-embeddings` | Motor de embeddings del host de memoria | Contratos de embeddings de memoria, acceso al registro, proveedor local y ayudantes genéricos de lote/remotos; los proveedores remotos concretos viven en sus plugins propietarios  
`plugin-sdk/memory-core-host-engine-qmd` | Motor QMD del host de memoria | Exportaciones del motor QMD del host de memoria  
`plugin-sdk/memory-core-host-engine-storage` | Motor de almacenamiento del host de memoria | Exportaciones del motor de almacenamiento del host de memoria  
`plugin-sdk/memory-core-host-multimodal` | Ayudantes multimodales del host de memoria | Ayudantes multimodales del host de memoria  
`plugin-sdk/memory-core-host-query` | Ayudantes de consulta del host de memoria | Ayudantes de consulta del host de memoria  
`plugin-sdk/memory-core-host-secret` | Ayudantes de secretos del host de memoria | Ayudantes de secretos del host de memoria  
`plugin-sdk/memory-core-host-events` | Alias obsoleto de eventos de memoria | Usa `plugin-sdk/memory-host-events`  
`plugin-sdk/memory-core-host-status` | Ayudantes de estado del host de memoria | Ayudantes de estado del host de memoria  
`plugin-sdk/memory-core-host-runtime-cli` | Runtime de CLI del host de memoria | Ayudantes de runtime de CLI del host de memoria  
`plugin-sdk/memory-core-host-runtime-core` | Runtime central del host de memoria | Ayudantes de runtime central del host de memoria  
`plugin-sdk/memory-core-host-runtime-files` | Ayudantes de archivos/runtime del host de memoria | Ayudantes de archivos/runtime del host de memoria  
`plugin-sdk/memory-host-core` | Alias del runtime central del host de memoria | Alias independiente del proveedor para ayudantes de runtime central del host de memoria  
`plugin-sdk/memory-host-events` | Alias del diario de eventos del host de memoria | Alias independiente del proveedor para ayudantes del diario de eventos del host de memoria  
`plugin-sdk/memory-host-files` | Alias obsoleto de archivos/runtime de memoria | Usa `plugin-sdk/memory-core-host-runtime-files`  
`plugin-sdk/memory-host-markdown` | Ayudantes de Markdown administrado | Ayudantes compartidos de Markdown administrado para plugins adyacentes a memoria  
`plugin-sdk/memory-host-search` | Fachada de búsqueda de memoria activa | Fachada de runtime diferida del administrador de búsqueda de memoria activa  
`plugin-sdk/memory-host-status` | Alias obsoleto de estado del host de memoria | Usa `plugin-sdk/memory-core-host-status`  
`plugin-sdk/testing` | Utilidades de prueba | Barrel de compatibilidad obsoleto local al repositorio; usa subrutas de prueba específicas locales al repositorio como `plugin-sdk/plugin-test-runtime`, `plugin-sdk/channel-test-helpers`, `plugin-sdk/channel-target-testing`, `plugin-sdk/test-env` y `plugin-sdk/test-fixtures`  
  
Esta tabla es intencionalmente el subconjunto de migración común, no toda la superficie del SDK. El inventario del punto de entrada del compilador vive en `scripts/lib/plugin-sdk-entrypoints.json`; las exportaciones de paquetes se generan a partir del subconjunto público.

Las uniones auxiliares reservadas de plugins incluidos se han retirado del mapa de exportaciones públicas del SDK, excepto por las fachadas de compatibilidad documentadas explícitamente, como el shim obsoleto `plugin-sdk/discord` conservado para el paquete publicado `@openclaw/discord@2026.3.13`. Los auxiliares específicos del propietario viven dentro del paquete del plugin propietario; el comportamiento compartido del host debe pasar por contratos genéricos del SDK como `plugin-sdk/gateway-runtime`, `plugin-sdk/security-runtime` y `plugin-sdk/plugin-config-runtime`.

Usa la importación más específica que coincida con la tarea. Si no encuentras una exportación, revisa el código fuente en `src/plugin-sdk/` o pregunta a los mantenedores qué contrato genérico debería poseerla.

## Obsolescencias activas

Obsolescencias más específicas que se aplican en todo el SDK de plugins, el contrato del proveedor, la superficie de runtime y el manifiesto. Todas siguen funcionando hoy, pero se eliminarán en una versión mayor futura. La entrada debajo de cada elemento asigna la API anterior a su reemplazo canónico.

Constructores de ayuda command-auth → command-status

**Anterior (`openclaw/plugin-sdk/command-auth`)**: `buildCommandsMessage`, `buildCommandsMessagePaginated`, `buildHelpMessage`.

**Nuevo (`openclaw/plugin-sdk/command-status`)**: mismas firmas, mismas exportaciones - solo importadas desde la subruta más específica. `command-auth` las reexporta como stubs de compatibilidad.

typescriptCopy code
[code]
    // Beforeimport { buildHelpMessage } from "openclaw/plugin-sdk/command-auth"; // Afterimport { buildHelpMessage } from "openclaw/plugin-sdk/command-status";
[/code]

Auxiliares de compuerta de menciones → resolveInboundMentionDecision

**Anterior** : `resolveInboundMentionRequirement({ facts, policy })` y `shouldDropInboundForMention(...)` desde `openclaw/plugin-sdk/channel-inbound` u `openclaw/plugin-sdk/channel-mention-gating`.

**Nuevo** : `resolveInboundMentionDecision({ facts, policy })` \- devuelve un único objeto de decisión en lugar de dos llamadas separadas.

Los plugins de canal downstream (Slack, Discord, Matrix, MS Teams) ya han cambiado.

Shim de runtime de canal y auxiliares de acciones de canal

`openclaw/plugin-sdk/channel-runtime` es un shim de compatibilidad para plugins de canal antiguos. No lo importes desde código nuevo; usa `openclaw/plugin-sdk/channel-runtime-context` para registrar objetos de runtime.

Los auxiliares `channelActions*` en `openclaw/plugin-sdk/channel-actions` están obsoletos junto con las exportaciones de canal "actions" sin procesar. Expón capacidades mediante la superficie semántica `presentation` en su lugar: los plugins de canal declaran qué renderizan (tarjetas, botones, selectores) en lugar de qué nombres de acción sin procesar aceptan.

Auxiliar tool() del proveedor de búsqueda web → createTool() en el plugin

**Anterior** : fábrica `tool()` desde `openclaw/plugin-sdk/provider-web-search`.

**Nuevo** : implementa `createTool(...)` directamente en el plugin proveedor. OpenClaw ya no necesita el auxiliar del SDK para registrar el wrapper de la herramienta.

Sobres de canal en texto plano → BodyForAgent

**Anterior** : `formatInboundEnvelope(...)` (y `ChannelMessageForAgent.channelEnvelope`) para crear un sobre de prompt plano en texto a partir de mensajes de canal entrantes.

**Nuevo** : `BodyForAgent` más bloques estructurados de contexto de usuario. Los plugins de canal adjuntan metadatos de enrutamiento (hilo, tema, responder a, reacciones) como campos tipados en lugar de concatenarlos en una cadena de prompt. El auxiliar `formatAgentEnvelope(...)` sigue admitiéndose para sobres sintetizados orientados al asistente, pero los sobres entrantes en texto plano están en retirada.

Áreas afectadas: `inbound_claim`, `message_received` y cualquier plugin de canal personalizado que posprocesara texto de `channelEnvelope`.

Tipos de descubrimiento de proveedor → tipos de catálogo de proveedor

Cuatro alias de tipos de descubrimiento ahora son wrappers ligeros sobre los tipos de la era de catálogo:

Alias anterior | Tipo nuevo  
---|---  
`ProviderDiscoveryOrder` | `ProviderCatalogOrder`  
`ProviderDiscoveryContext` | `ProviderCatalogContext`  
`ProviderDiscoveryResult` | `ProviderCatalogResult`  
`ProviderPluginDiscovery` | `ProviderPluginCatalog`  
  
Además de la bolsa estática heredada `ProviderCapabilities`: los plugins proveedores deben usar hooks de proveedor explícitos como `buildReplayPolicy`, `normalizeToolSchemas` y `wrapStreamFn` en lugar de un objeto estático.

Hooks de política de razonamiento → resolveThinkingProfile

**Anterior** (tres hooks separados en `ProviderThinkingPolicy`): `isBinaryThinking(ctx)`, `supportsXHighThinking(ctx)` y `resolveDefaultThinkingLevel(ctx)`.

**Nuevo** : un único `resolveThinkingProfile(ctx)` que devuelve un `ProviderThinkingProfile` con el `id` canónico, `label` opcional y lista de niveles clasificada. OpenClaw reduce automáticamente los valores almacenados obsoletos según el rango del perfil.

Implementa un hook en lugar de tres. Los hooks heredados siguen funcionando durante la ventana de obsolescencia, pero no se componen con el resultado del perfil.

Fallback de proveedor OAuth externo → contracts.externalAuthProviders

**Anterior** : implementar `resolveExternalOAuthProfiles(...)` sin declarar el proveedor en el manifiesto del plugin.

**Nuevo** : declara `contracts.externalAuthProviders` en el manifiesto del plugin **e** implementa `resolveExternalAuthProfiles(...)`. La ruta antigua de "auth fallback" emite una advertencia en runtime y se eliminará.

jsonCopy code
[code]
    {  "contracts": {    "externalAuthProviders": ["anthropic", "openai"]  }}
[/code]

Búsqueda de variables de entorno de proveedor → setup.providers[].envVars

**Anterior** campo de manifiesto: `providerAuthEnvVars: { anthropic: ["ANTHROPIC_API_KEY"] }`.

**Nuevo** : refleja la misma búsqueda de variables de entorno en `setup.providers[].envVars` dentro del manifiesto. Esto consolida los metadatos de entorno de configuración/estado en un solo lugar y evita iniciar el runtime del plugin solo para responder búsquedas de variables de entorno.

`providerAuthEnvVars` sigue admitiéndose mediante un adaptador de compatibilidad hasta que se cierre la ventana de obsolescencia.

Registro de plugin de memoria → registerMemoryCapability

**Anterior** : tres llamadas separadas: `api.registerMemoryPromptSection(...)`, `api.registerMemoryFlushPlan(...)`, `api.registerMemoryRuntime(...)`.

**Nuevo** : una llamada en la API de estado de memoria: `registerMemoryCapability(pluginId, { promptBuilder, flushPlanResolver, runtime })`.

Mismos espacios, una sola llamada de registro. Los auxiliares de memoria aditivos (`registerMemoryPromptSupplement`, `registerMemoryCorpusSupplement`, `registerMemoryEmbeddingProvider`) no se ven afectados.

Tipos de mensajes de sesión de subagente renombrados

Dos alias de tipos heredados siguen exportándose desde `src/plugins/runtime/types.ts`:

Anterior | Nuevo  
---|---  
`SubagentReadSessionParams` | `SubagentGetSessionMessagesParams`  
`SubagentReadSessionResult` | `SubagentGetSessionMessagesResult`  
  
El método de runtime `readSession` está obsoleto a favor de `getSessionMessages`. Misma firma; el método anterior llama al nuevo.

runtime.tasks.flow → runtime.tasks.managedFlows

**Anterior** : `runtime.tasks.flow` (singular) devolvía un accesor activo de flujo de tareas.

**Nuevo** : `runtime.tasks.managedFlows` conserva el runtime de mutación de TaskFlow gestionado para plugins que crean, actualizan, cancelan o ejecutan tareas hijas desde un flujo. Usa `runtime.tasks.flows` cuando el plugin solo necesita lecturas basadas en DTO.

typescriptCopy code
[code]
    // Beforeconst flow = api.runtime.tasks.flow.fromToolContext(ctx);// Afterconst flow = api.runtime.tasks.managedFlows.fromToolContext(ctx);
[/code]

Fábricas de extensión incrustadas → middleware de resultados de herramienta del agente

Cubierto arriba en "Cómo migrar → Migrar extensiones de resultados de herramienta de Pi a middleware". Incluido aquí por completitud: la ruta eliminada exclusiva de Pi `api.registerEmbeddedExtensionFactory(...)` se reemplaza por `api.registerAgentToolResultMiddleware(...)` con una lista explícita de runtime en `contracts.agentToolResultMiddleware`.

Alias OpenClawSchemaType → OpenClawConfig

`OpenClawSchemaType` reexportado desde `openclaw/plugin-sdk` ahora es un alias de una línea para `OpenClawConfig`. Prefiere el nombre canónico.

typescriptCopy code
[code]
    // Beforeimport type { OpenClawSchemaType } from "openclaw/plugin-sdk";// Afterimport type { OpenClawConfig } from "openclaw/plugin-sdk/config-schema";
[/code]

## Cronograma de eliminación

Cuándo | Qué ocurre  
---|---  
**Ahora** | Las superficies obsoletas emiten advertencias en runtime  
**Próxima versión mayor** | Las superficies obsoletas se eliminarán; los plugins que sigan usándolas fallarán  
  
Todos los plugins centrales ya se han migrado. Los plugins externos deben migrar antes de la próxima versión mayor.

## Suprimir las advertencias temporalmente

Configura estas variables de entorno mientras trabajas en la migración:

bashCopy code
[code]
    OPENCLAW_SUPPRESS_PLUGIN_SDK_COMPAT_WARNING=1 openclaw gateway runOPENCLAW_SUPPRESS_EXTENSION_API_WARNING=1 openclaw gateway run
[/code]

Esta es una vía de escape temporal, no una solución permanente.

## Relacionado

  * [Primeros pasos](</es/plugins/building-plugins>) \- crea tu primer plugin
  * [Resumen del SDK](</es/plugins/sdk-overview>) \- referencia completa de importaciones por subruta
  * [Plugins de canal](</es/plugins/sdk-channel-plugins>) \- crear plugins de canal
  * [Plugins de proveedor](</es/plugins/sdk-provider-plugins>) \- crear plugins de proveedor
  * [Internos de Plugin](</es/plugins/architecture>) \- análisis profundo de la arquitectura
  * [Manifiesto de Plugin](</es/plugins/manifest>) \- referencia del esquema del manifiesto


Was this useful?YesNo