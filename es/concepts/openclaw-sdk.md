---
title: SDK de la aplicación OpenClaw
source_url: https://docs.openclaw.ai/es/concepts/openclaw-sdk
scraped_at: 2026-05-25
---

El **OpenClaw App SDK** es la API pública de cliente para apps fuera del proceso de OpenClaw. Usa `@openclaw/sdk` cuando un script, panel, tarea de CI, extensión de IDE u otra app externa quiera conectarse al Gateway, iniciar ejecuciones de agente, transmitir eventos, esperar resultados, cancelar trabajo o inspeccionar recursos del Gateway.

## Lo que se entrega hoy

`@openclaw/sdk` se entrega con:

Superficie | Estado | Qué hace  
---|---|---  
`OpenClaw` | Listo | Punto de entrada principal del cliente. Administra transporte, conexión, solicitudes y eventos.  
`GatewayClientTransport` | Listo | Transporte WebSocket respaldado por el cliente del Gateway.  
`oc.agents` | Listo | Lista, crea, actualiza, elimina y obtiene handles de agente.  
`Agent.run()` | Listo | Inicia una ejecución `agent` del Gateway y devuelve un `Run`.  
`oc.runs` | Listo | Crea, obtiene, espera, cancela y transmite ejecuciones.  
`Run.events()` | Listo | Transmite eventos normalizados por ejecución con reproducción para ejecuciones rápidas.  
`Run.wait()` | Listo | Llama a `agent.wait` y devuelve un `RunResult` estable.  
`Run.cancel()` | Listo | Llama a `sessions.abort` por id de ejecución, con clave de sesión cuando está disponible.  
`oc.sessions` | Listo | Crea, resuelve, envía a, parchea, compacta y obtiene handles de sesión.  
`Session.send()` | Listo | Llama a `sessions.send` y devuelve un `Run`.  
`oc.tasks` | Listo | Lista, lee y cancela entradas del registro de tareas del Gateway.  
`oc.models` | Listo | Llama a `models.list` y al RPC de estado actual `models.authStatus`.  
`oc.tools` | Listo | Lista, delimita e invoca herramientas del Gateway a través del pipeline de políticas.  
`oc.artifacts` | Listo | Lista, obtiene y descarga artefactos de transcripción del Gateway.  
`oc.approvals` | Listo | Lista y resuelve aprobaciones de exec mediante RPCs de aprobación del Gateway.  
`oc.environments` | Parcial | Lista candidatos de entorno locales del Gateway y del nodo; crear/eliminar no están conectados.  
`oc.rawEvents()` | Listo | Expone eventos sin procesar del Gateway para consumidores avanzados.  
`normalizeGatewayEvent()` | Listo | Convierte eventos sin procesar del Gateway a la forma de evento estable del SDK.  
  
El SDK también exporta los tipos principales usados por esas superficies: `AgentRunParams`, `RunResult`, `RunStatus`, `OpenClawEvent`, `OpenClawEventType`, `GatewayEvent`, `OpenClawTransport`, `GatewayRequestOptions`, `SessionCreateParams`, `SessionSendParams`, `ArtifactSummary`, `ArtifactQuery`, `ArtifactsListResult`, `ArtifactsGetResult`, `ArtifactsDownloadResult`, `TaskSummary`, `TaskStatus`, `TasksListParams`, `TasksListResult`, `TasksGetResult`, `TasksCancelResult`, `RuntimeSelection`, `EnvironmentSelection`, `WorkspaceSelection`, `ApprovalMode` y tipos de resultado relacionados.

## Conectarse a un Gateway

Crea un cliente con una URL explícita del Gateway, o inyecta un transporte personalizado para pruebas y runtimes de apps embebidas.

typescriptCopy code
[code]
     const oc = new OpenClaw({  url: "ws://127.0.0.1:18789",  token: process.env.OPENCLAW_GATEWAY_TOKEN,  requestTimeoutMs: 30_000,}); await oc.connect();
[/code]

`new OpenClaw({ gateway: "ws://..." })` es equivalente a `url`. La opción `gateway: "auto"` es aceptada por el constructor, pero el descubrimiento automático del Gateway aún no es una función separada del SDK; pasa `url` cuando la app aún no sepa cómo descubrir el Gateway.

Para pruebas, pasa un objeto que implemente `OpenClawTransport`:

typescriptCopy code
[code]
    const oc = new OpenClaw({  transport: {    async request(method, params) {      return { method, params };    },    async *events() {},  },});
[/code]

## Ejecutar un agente

Usa `oc.agents.get(id)` cuando la app quiera un handle de agente y luego llama a `agent.run()`.

typescriptCopy code
[code]
    const agent = await oc.agents.get("main"); const run = await agent.run({  input: "Review this pull request and suggest the smallest safe fix.",  model: "openai/gpt-5.5",  sessionKey: "main",  timeoutMs: 30_000,}); for await (const event of run.events()) {  const data = event.data as { delta?: unknown };  if (event.type === "assistant.delta" && typeof data.delta === "string") {    process.stdout.write(data.delta);  }} const result = await run.wait({ timeoutMs: 120_000 });console.log(result.status);
[/code]

Las referencias de modelo calificadas por proveedor, como `openai/gpt-5.5`, se dividen en sobreescrituras `provider` y `model` del Gateway. `timeoutMs` permanece en milisegundos en el SDK y se convierte a segundos de timeout del Gateway para el RPC `agent`.

`run.wait()` usa el RPC `agent.wait` del Gateway. Un plazo de espera que vence mientras la ejecución sigue activa devuelve `status: "accepted"` en lugar de simular que la propia ejecución agotó el tiempo. Los timeouts de runtime, las ejecuciones abortadas y las ejecuciones canceladas se normalizan a `timed_out` o `cancelled`.

## Crear y reutilizar sesiones

Usa sesiones cuando la app quiera estado duradero de transcripción.

typescriptCopy code
[code]
    const session = await oc.sessions.create({  agentId: "main",  label: "release-review",}); const run = await session.send("Prepare release notes from the current diff.");await run.wait();
[/code]

`Session.send()` llama a `sessions.send` y devuelve un `Run`. Los handles de sesión también admiten:

typescriptCopy code
[code]
    await session.abort(run.id);await session.patch({ label: "renamed-session" });await session.compact({ maxLines: 200 });
[/code]

## Transmitir eventos

El SDK normaliza eventos sin procesar del Gateway en un sobre estable `OpenClawEvent`:

typescriptCopy code
[code]
    type OpenClawEvent = {  version: 1;  id: string;  ts: number;  type: OpenClawEventType;  runId?: string;  sessionId?: string;  sessionKey?: string;  taskId?: string;  agentId?: string;  data: unknown;  raw?: GatewayEvent;};
[/code]

Los tipos de evento comunes incluyen:

Tipo de evento | Evento de Gateway de origen  
---|---  
`run.started` | Inicio del ciclo de vida de `agent`  
`run.completed` | Fin del ciclo de vida de `agent`  
`run.failed` | Error del ciclo de vida de `agent`  
`run.cancelled` | Fin del ciclo de vida abortado/cancelado  
`run.timed_out` | Fin del ciclo de vida por timeout  
`assistant.delta` | Delta de transmisión del asistente  
`assistant.message` | Mensaje del asistente  
`thinking.delta` | Flujo de pensamiento o plan  
`tool.call.started` | Inicio de herramienta/elemento/comando  
`tool.call.delta` | Actualización de herramienta/elemento/comando  
`tool.call.completed` | Finalización de herramienta/elemento/comando  
`tool.call.failed` | Fallo o estado bloqueado de herramienta/elemento/comando  
`approval.requested` | Solicitud de aprobación de exec o plugin  
`approval.resolved` | Resolución de aprobación de exec o plugin  
`session.created` | Creación de `sessions.changed`  
`session.updated` | Actualización de `sessions.changed`  
`session.compacted` | Compactación de `sessions.changed`  
`task.updated` | Eventos de actualización de tarea  
`artifact.updated` | Eventos de flujo de parches  
`raw` | Cualquier evento sin mapeo estable del SDK aún  
  
`Run.events()` filtra eventos a un id de ejecución y reproduce eventos ya vistos para ejecuciones rápidas. Eso significa que el flujo documentado es seguro:

typescriptCopy code
[code]
    const run = await agent.run("Summarize the latest session."); for await (const event of run.events()) {  if (event.type === "run.completed") {    break;  }}
[/code]

Para flujos de toda la app, usa `oc.events()`. Para frames sin procesar del Gateway, usa `oc.rawEvents()`.

## Modelos, herramientas, artefactos y aprobaciones

Los helpers de modelo se asignan a métodos actuales del Gateway:

typescriptCopy code
[code]
    await oc.models.list();await oc.models.status({ probe: false }); // calls models.authStatus
[/code]

Los helpers de herramienta exponen el catálogo del Gateway, la vista efectiva de herramientas y la invocación directa de herramientas del Gateway. `oc.tools.invoke()` devuelve un sobre tipado en lugar de lanzar errores por rechazos de política o aprobación.

typescriptCopy code
[code]
    await oc.tools.list();await oc.tools.effective({ sessionKey: "main" });await oc.tools.invoke("tool-name", {  args: { input: "value" },  sessionKey: "main",  confirm: false,  idempotencyKey: "tool-call-1",});
[/code]

Los helpers de artefacto exponen la proyección de artefactos del Gateway para contexto de sesión, ejecución o tarea. Cada llamada requiere un ámbito explícito `sessionKey`, `runId` o `taskId`:

typescriptCopy code
[code]
    const { artifacts } = await oc.artifacts.list({ sessionKey: "main" });const first = artifacts[0]; if (first) {  const { artifact } = await oc.artifacts.get(first.id, { sessionKey: "main" });  const download = await oc.artifacts.download(artifact.id, { sessionKey: "main" });  console.log(download.encoding, download.url);}
[/code]

Los helpers de aprobación usan los RPCs de aprobación de exec:

typescriptCopy code
[code]
    const approvals = await oc.approvals.list();await oc.approvals.respond("approval-id", { decision: "approve" });
[/code]

Los helpers de tarea usan el registro duradero de tareas que también respalda `openclaw tasks`:

typescriptCopy code
[code]
    const tasks = await oc.tasks.list({ status: "running", sessionKey: "agent:main:main" });const task = await oc.tasks.get(tasks.tasks[0].id);await oc.tasks.cancel(task.task.id, { reason: "user stopped task" });
[/code]

Los helpers de entorno exponen descubrimiento de solo lectura local del Gateway y del nodo:

typescriptCopy code
[code]
    const { environments } = await oc.environments.list();await oc.environments.status(environments[0].id);
[/code]

## Explícitamente no admitido hoy

El SDK incluye nombres para el modelo de producto que queremos, pero no simula silenciosamente que existan RPCs del Gateway. Estas llamadas actualmente lanzan errores explícitos de no compatibilidad:

typescriptCopy code
[code]
    await oc.environments.create({});await oc.environments.delete("environment-id");
[/code]

Los campos por ejecución `workspace`, `runtime`, `environment` y `approvals` están tipados como forma futura, pero el Gateway actual no admite esas sobreescrituras en el RPC `agent`. Si los llamadores los pasan, el SDK lanza un error antes de enviar la ejecución para que el trabajo no se ejecute accidentalmente con el comportamiento predeterminado de workspace, runtime, entorno o aprobación.

## App SDK frente a Plugin SDK

Usa el App SDK cuando el código vive fuera de OpenClaw:

  * scripts de Node que inician u observan ejecuciones de agente
  * tareas de CI que llaman a un Gateway
  * paneles y paneles de administración
  * extensiones de IDE
  * puentes externos que no necesitan convertirse en plugins de canal
  * pruebas de integración con transportes de Gateway falsos o reales


Usa el Plugin SDK cuando el código se ejecuta dentro de OpenClaw:

  * plugins de proveedor
  * plugins de canal
  * hooks de herramienta o ciclo de vida
  * plugins de harness de agente
  * helpers de runtime de confianza


El código de App SDK debe importar desde `@openclaw/sdk`. El código de Plugin debe importar desde subrutas documentadas de `openclaw/plugin-sdk/*`. No mezcles los dos contratos.

## Relacionado

  * [Diseño de la API del SDK de apps de OpenClaw](</es/reference/openclaw-sdk-api-design>)
  * [Referencia de RPC de Gateway](</es/reference/rpc>)
  * [Bucle del agente](</es/concepts/agent-loop>)
  * [Entornos de ejecución de agentes](</es/concepts/agent-runtimes>)
  * [Sesiones](</es/concepts/session>)
  * [Tareas en segundo plano](</es/automation/tasks>)
  * [Agentes ACP](</es/tools/acp-agents>)
  * [Descripción general del SDK de Plugin](</es/plugins/sdk-overview>)


Was this useful?YesNo