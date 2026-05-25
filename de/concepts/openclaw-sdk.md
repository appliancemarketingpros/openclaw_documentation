---
title: OpenClaw App-SDK
source_url: https://docs.openclaw.ai/de/concepts/openclaw-sdk
scraped_at: 2026-05-25
---

Das **OpenClaw App SDK** ist die öffentliche Client-API für Apps außerhalb des OpenClaw-Prozesses. Verwenden Sie `@openclaw/sdk`, wenn ein Skript, Dashboard, CI-Job, eine IDE-Erweiterung oder eine andere externe App eine Verbindung zum Gateway herstellen, Agent-Ausführungen starten, Events streamen, auf Ergebnisse warten, Arbeit abbrechen oder Gateway-Ressourcen prüfen soll.

## Was heute ausgeliefert wird

`@openclaw/sdk` wird mit Folgendem ausgeliefert:

Oberfläche | Status | Was sie macht  
---|---|---  
`OpenClaw` | Bereit | Haupteinstiegspunkt für Clients. Besitzt Transport, Verbindung, Anfragen und Events.  
`GatewayClientTransport` | Bereit | WebSocket-Transport auf Basis des Gateway-Clients.  
`oc.agents` | Bereit | Listet, erstellt, aktualisiert, löscht und ruft Agent-Handles ab.  
`Agent.run()` | Bereit | Startet eine Gateway-`agent`-Ausführung und gibt einen `Run` zurück.  
`oc.runs` | Bereit | Erstellt, ruft ab, wartet auf, bricht ab und streamt Ausführungen.  
`Run.events()` | Bereit | Streamt normalisierte Events pro Ausführung mit Replay für schnelle Ausführungen.  
`Run.wait()` | Bereit | Ruft `agent.wait` auf und gibt ein stabiles `RunResult` zurück.  
`Run.cancel()` | Bereit | Ruft `sessions.abort` nach Ausführungs-ID auf, mit Sitzungsschlüssel, sofern verfügbar.  
`oc.sessions` | Bereit | Erstellt, löst auf, sendet an, patcht, kompaktiert und ruft Sitzungs-Handles ab.  
`Session.send()` | Bereit | Ruft `sessions.send` auf und gibt einen `Run` zurück.  
`oc.tasks` | Bereit | Listet, liest und bricht Gateway-Task-Ledger-Einträge ab.  
`oc.models` | Bereit | Ruft `models.list` und den aktuellen Status-RPC `models.authStatus` auf.  
`oc.tools` | Bereit | Listet, scoped und ruft Gateway-Tools über die Policy-Pipeline auf.  
`oc.artifacts` | Bereit | Listet, ruft ab und lädt Gateway-Transkript-Artefakte herunter.  
`oc.approvals` | Bereit | Listet und löst Exec-Freigaben über Gateway-Freigabe-RPCs auf.  
`oc.environments` | Teilweise | Listet Gateway-lokale und Node-Umgebungskandidaten; Erstellen/Löschen ist nicht verdrahtet.  
`oc.rawEvents()` | Bereit | Stellt rohe Gateway-Events für fortgeschrittene Consumer bereit.  
`normalizeGatewayEvent()` | Bereit | Wandelt rohe Gateway-Events in die stabile SDK-Event-Form um.  
  
Das SDK exportiert außerdem die Kerntypen, die von diesen Oberflächen verwendet werden: `AgentRunParams`, `RunResult`, `RunStatus`, `OpenClawEvent`, `OpenClawEventType`, `GatewayEvent`, `OpenClawTransport`, `GatewayRequestOptions`, `SessionCreateParams`, `SessionSendParams`, `ArtifactSummary`, `ArtifactQuery`, `ArtifactsListResult`, `ArtifactsGetResult`, `ArtifactsDownloadResult`, `TaskSummary`, `TaskStatus`, `TasksListParams`, `TasksListResult`, `TasksGetResult`, `TasksCancelResult`, `RuntimeSelection`, `EnvironmentSelection`, `WorkspaceSelection`, `ApprovalMode` und verwandte Ergebnistypen.

## Verbindung zu einem Gateway herstellen

Erstellen Sie einen Client mit einer expliziten Gateway-URL, oder injizieren Sie einen benutzerdefinierten Transport für Tests und eingebettete App-Runtimes.

typescriptCopy code
[code]
     const oc = new OpenClaw({  url: "ws://127.0.0.1:18789",  token: process.env.OPENCLAW_GATEWAY_TOKEN,  requestTimeoutMs: 30_000,}); await oc.connect();
[/code]

`new OpenClaw({ gateway: "ws://..." })` ist gleichwertig mit `url`. Die Option `gateway: "auto"` wird vom Konstruktor akzeptiert, aber automatische Gateway-Erkennung ist noch kein separates SDK-Feature; übergeben Sie `url`, wenn die App nicht bereits weiß, wie sie das Gateway erkennen soll.

Übergeben Sie für Tests ein Objekt, das `OpenClawTransport` implementiert:

typescriptCopy code
[code]
    const oc = new OpenClaw({  transport: {    async request(method, params) {      return { method, params };    },    async *events() {},  },});
[/code]

## Einen Agent ausführen

Verwenden Sie `oc.agents.get(id)`, wenn die App ein Agent-Handle benötigt, und rufen Sie dann `agent.run()` auf.

typescriptCopy code
[code]
    const agent = await oc.agents.get("main"); const run = await agent.run({  input: "Review this pull request and suggest the smallest safe fix.",  model: "openai/gpt-5.5",  sessionKey: "main",  timeoutMs: 30_000,}); for await (const event of run.events()) {  const data = event.data as { delta?: unknown };  if (event.type === "assistant.delta" && typeof data.delta === "string") {    process.stdout.write(data.delta);  }} const result = await run.wait({ timeoutMs: 120_000 });console.log(result.status);
[/code]

Provider-qualifizierte Modellreferenzen wie `openai/gpt-5.5` werden in Gateway-Overrides für `provider` und `model` aufgeteilt. `timeoutMs` bleibt im SDK in Millisekunden und wird für den `agent`-RPC in Gateway-Timeout-Sekunden umgewandelt.

`run.wait()` verwendet den Gateway-RPC `agent.wait`. Eine Wait-Deadline, die abläuft, während die Ausführung noch aktiv ist, gibt `status: "accepted"` zurück, anstatt vorzutäuschen, dass die Ausführung selbst einen Timeout hatte. Runtime-Timeouts, abgebrochene Ausführungen und stornierte Ausführungen werden zu `timed_out` oder `cancelled` normalisiert.

## Sitzungen erstellen und wiederverwenden

Verwenden Sie Sitzungen, wenn die App dauerhaften Transkriptzustand benötigt.

typescriptCopy code
[code]
    const session = await oc.sessions.create({  agentId: "main",  label: "release-review",}); const run = await session.send("Prepare release notes from the current diff.");await run.wait();
[/code]

`Session.send()` ruft `sessions.send` auf und gibt einen `Run` zurück. Sitzungs-Handles unterstützen außerdem:

typescriptCopy code
[code]
    await session.abort(run.id);await session.patch({ label: "renamed-session" });await session.compact({ maxLines: 200 });
[/code]

## Events streamen

Das SDK normalisiert rohe Gateway-Events in einen stabilen `OpenClawEvent`-Umschlag:

typescriptCopy code
[code]
    type OpenClawEvent = {  version: 1;  id: string;  ts: number;  type: OpenClawEventType;  runId?: string;  sessionId?: string;  sessionKey?: string;  taskId?: string;  agentId?: string;  data: unknown;  raw?: GatewayEvent;};
[/code]

Häufige Event-Typen sind:

Event-Typ | Gateway-Quell-Event  
---|---  
`run.started` | Start des `agent`-Lebenszyklus  
`run.completed` | Ende des `agent`-Lebenszyklus  
`run.failed` | Fehler im `agent`-Lebenszyklus  
`run.cancelled` | Ende eines abgebrochenen/stornierten Lebenszyklus  
`run.timed_out` | Ende eines Timeout-Lebenszyklus  
`assistant.delta` | Streaming-Delta des Assistenten  
`assistant.message` | Assistentennachricht  
`thinking.delta` | Denk- oder Plan-Stream  
`tool.call.started` | Start von Tool/Item/Befehl  
`tool.call.delta` | Aktualisierung von Tool/Item/Befehl  
`tool.call.completed` | Abschluss von Tool/Item/Befehl  
`tool.call.failed` | Fehler oder blockierter Status von Tool/Item/Befehl  
`approval.requested` | Exec- oder Plugin-Freigabeanforderung  
`approval.resolved` | Exec- oder Plugin-Freigabeauflösung  
`session.created` | `sessions.changed`-Erstellung  
`session.updated` | `sessions.changed`-Aktualisierung  
`session.compacted` | `sessions.changed`-Compaction  
`task.updated` | Task-Aktualisierungs-Events  
`artifact.updated` | Patch-Stream-Events  
`raw` | Jedes Event ohne bisher stabiles SDK-Mapping  
  
`Run.events()` filtert Events auf eine Ausführungs-ID und spielt bereits gesehene Events für schnelle Ausführungen erneut ab. Das bedeutet, dass der dokumentierte Ablauf sicher ist:

typescriptCopy code
[code]
    const run = await agent.run("Summarize the latest session."); for await (const event of run.events()) {  if (event.type === "run.completed") {    break;  }}
[/code]

Verwenden Sie für appweite Streams `oc.events()`. Verwenden Sie für rohe Gateway-Frames `oc.rawEvents()`.

## Modelle, Tools, Artefakte und Freigaben

Modell-Helfer ordnen aktuellen Gateway-Methoden zu:

typescriptCopy code
[code]
    await oc.models.list();await oc.models.status({ probe: false }); // calls models.authStatus
[/code]

Tool-Helfer stellen den Gateway-Katalog, die effektive Tool-Ansicht und den direkten Gateway-Tool-Aufruf bereit. `oc.tools.invoke()` gibt einen typisierten Umschlag zurück, anstatt bei Policy- oder Freigabeverweigerungen eine Exception auszulösen.

typescriptCopy code
[code]
    await oc.tools.list();await oc.tools.effective({ sessionKey: "main" });await oc.tools.invoke("tool-name", {  args: { input: "value" },  sessionKey: "main",  confirm: false,  idempotencyKey: "tool-call-1",});
[/code]

Artefakt-Helfer stellen die Gateway-Artefaktprojektion für Sitzungs-, Ausführungs- oder Task-Kontext bereit. Jeder Aufruf erfordert genau einen expliziten Scope `sessionKey`, `runId` oder `taskId`:

typescriptCopy code
[code]
    const { artifacts } = await oc.artifacts.list({ sessionKey: "main" });const first = artifacts[0]; if (first) {  const { artifact } = await oc.artifacts.get(first.id, { sessionKey: "main" });  const download = await oc.artifacts.download(artifact.id, { sessionKey: "main" });  console.log(download.encoding, download.url);}
[/code]

Freigabe-Helfer verwenden die Exec-Freigabe-RPCs:

typescriptCopy code
[code]
    const approvals = await oc.approvals.list();await oc.approvals.respond("approval-id", { decision: "approve" });
[/code]

Task-Helfer verwenden das dauerhafte Task-Ledger, das auch `openclaw tasks` unterstützt:

typescriptCopy code
[code]
    const tasks = await oc.tasks.list({ status: "running", sessionKey: "agent:main:main" });const task = await oc.tasks.get(tasks.tasks[0].id);await oc.tasks.cancel(task.task.id, { reason: "user stopped task" });
[/code]

Umgebungs-Helfer stellen schreibgeschützte Gateway-lokale und Node-Erkennung bereit:

typescriptCopy code
[code]
    const { environments } = await oc.environments.list();await oc.environments.status(environments[0].id);
[/code]

## Heute ausdrücklich nicht unterstützt

Das SDK enthält Namen für das Produktmodell, das wir anstreben, tut aber nicht stillschweigend so, als ob Gateway-RPCs existierten. Diese Aufrufe lösen derzeit explizite Nicht-unterstützt-Fehler aus:

typescriptCopy code
[code]
    await oc.environments.create({});await oc.environments.delete("environment-id");
[/code]

Die Felder `workspace`, `runtime`, `environment` und `approvals` pro Ausführung sind als zukünftige Form typisiert, aber das aktuelle Gateway unterstützt diese Overrides im `agent`-RPC nicht. Wenn Aufrufer sie übergeben, löst das SDK vor dem Absenden der Ausführung eine Exception aus, damit Arbeit nicht versehentlich mit Standardverhalten für Workspace, Runtime, Umgebung oder Freigaben ausgeführt wird.

## App SDK vs. Plugin SDK

Verwenden Sie das App SDK, wenn Code außerhalb von OpenClaw lebt:

  * Node-Skripte, die Agent-Ausführungen starten oder beobachten
  * CI-Jobs, die ein Gateway aufrufen
  * Dashboards und Admin-Panels
  * IDE-Erweiterungen
  * externe Bridges, die nicht zu Kanal-Plugins werden müssen
  * Integrationstests mit gefälschten oder echten Gateway-Transporten


Verwenden Sie das Plugin SDK, wenn Code innerhalb von OpenClaw läuft:

  * Provider-Plugins
  * Kanal-Plugins
  * Tool- oder Lebenszyklus-Hooks
  * Agent-Harness-Plugins
  * vertrauenswürdige Runtime-Helfer


App-SDK-Code sollte aus `@openclaw/sdk` importieren. Plugin-Code sollte aus dokumentierten `openclaw/plugin-sdk/*`-Unterpfaden importieren. Mischen Sie die beiden Verträge nicht.

## Verwandte Themen

  * [API-Design des OpenClaw App SDK](</de/reference/openclaw-sdk-api-design>)
  * [Gateway-RPC-Referenz](</de/reference/rpc>)
  * [Agenten-Loop](</de/concepts/agent-loop>)
  * [Agent-Runtimes](</de/concepts/agent-runtimes>)
  * [Sitzungen](</de/concepts/session>)
  * [Hintergrundaufgaben](</de/automation/tasks>)
  * [ACP-Agenten](</de/tools/acp-agents>)
  * [Plugin-SDK-Übersicht](</de/plugins/sdk-overview>)


Was this useful?YesNo