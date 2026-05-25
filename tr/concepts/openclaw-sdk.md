---
title: OpenClaw Uygulama SDK'sı
source_url: https://docs.openclaw.ai/tr/concepts/openclaw-sdk
scraped_at: 2026-05-25
---

**OpenClaw App SDK** , OpenClaw sürecinin dışındaki uygulamalar için herkese açık istemci API'sidir. Bir betik, pano, CI işi, IDE eklentisi veya başka bir dış uygulama Gateway'e bağlanmak, agent çalıştırmaları başlatmak, olayları yayınlamak, sonuçları beklemek, işleri iptal etmek ya da Gateway kaynaklarını incelemek istediğinde `@openclaw/sdk` kullanın.

## Bugün neler sunulur

`@openclaw/sdk` şunlarla birlikte gelir:

Yüzey | Durum | Ne yapar  
---|---|---  
`OpenClaw` | Hazır | Ana istemci giriş noktası. Aktarım, bağlantı, istekler ve olayları yönetir.  
`GatewayClientTransport` | Hazır | Gateway istemcisi tarafından desteklenen WebSocket aktarımı.  
`oc.agents` | Hazır | Agent tutamaçlarını listeler, oluşturur, günceller, siler ve getirir.  
`Agent.run()` | Hazır | Bir Gateway `agent` çalıştırması başlatır ve bir `Run` döndürür.  
`oc.runs` | Hazır | Çalıştırmaları oluşturur, getirir, bekler, iptal eder ve yayınlar.  
`Run.events()` | Hazır | Hızlı çalıştırmalar için yeniden oynatmayla normalize edilmiş çalıştırma başına olayları yayınlar.  
`Run.wait()` | Hazır | `agent.wait` çağrısı yapar ve kararlı bir `RunResult` döndürür.  
`Run.cancel()` | Hazır | Varsa oturum anahtarıyla, çalıştırma id'sine göre `sessions.abort` çağırır.  
`oc.sessions` | Hazır | Oturum tutamaçlarını oluşturur, çözümler, gönderir, yamalar, compaction uygular ve getirir.  
`Session.send()` | Hazır | `sessions.send` çağrısı yapar ve bir `Run` döndürür.  
`oc.tasks` | Hazır | Gateway görev defteri girdilerini listeler, okur ve iptal eder.  
`oc.models` | Hazır | `models.list` ve geçerli `models.authStatus` durum RPC'sini çağırır.  
`oc.tools` | Hazır | Gateway araçlarını ilke hattı üzerinden listeler, kapsamlandırır ve çağırır.  
`oc.artifacts` | Hazır | Gateway transcript artifact'lerini listeler, getirir ve indirir.  
`oc.approvals` | Hazır | Exec onaylarını Gateway onay RPC'leri üzerinden listeler ve çözümler.  
`oc.environments` | Kısmi | Gateway yerel ve node ortam adaylarını listeler; oluşturma/silme bağlı değildir.  
`oc.rawEvents()` | Hazır | Gelişmiş tüketiciler için ham Gateway olaylarını açığa çıkarır.  
`normalizeGatewayEvent()` | Hazır | Ham Gateway olaylarını kararlı SDK olay biçimine dönüştürür.  
  
SDK ayrıca bu yüzeyler tarafından kullanılan çekirdek türleri de dışa aktarır: `AgentRunParams`, `RunResult`, `RunStatus`, `OpenClawEvent`, `OpenClawEventType`, `GatewayEvent`, `OpenClawTransport`, `GatewayRequestOptions`, `SessionCreateParams`, `SessionSendParams`, `ArtifactSummary`, `ArtifactQuery`, `ArtifactsListResult`, `ArtifactsGetResult`, `ArtifactsDownloadResult`, `TaskSummary`, `TaskStatus`, `TasksListParams`, `TasksListResult`, `TasksGetResult`, `TasksCancelResult`, `RuntimeSelection`, `EnvironmentSelection`, `WorkspaceSelection`, `ApprovalMode` ve ilgili sonuç türleri.

## Bir Gateway'e bağlanma

Açık bir Gateway URL'siyle bir istemci oluşturun veya testler ve gömülü uygulama çalışma zamanları için özel bir aktarım enjekte edin.

typescriptCopy code
[code]
     const oc = new OpenClaw({  url: "ws://127.0.0.1:18789",  token: process.env.OPENCLAW_GATEWAY_TOKEN,  requestTimeoutMs: 30_000,}); await oc.connect();
[/code]

`new OpenClaw({ gateway: "ws://..." })`, `url` ile eşdeğerdir. `gateway: "auto"` seçeneği constructor tarafından kabul edilir, ancak otomatik Gateway keşfi henüz ayrı bir SDK özelliği değildir; uygulama Gateway'i nasıl keşfedeceğini zaten bilmiyorsa `url` iletin.

Testler için `OpenClawTransport` uygulayan bir nesne iletin:

typescriptCopy code
[code]
    const oc = new OpenClaw({  transport: {    async request(method, params) {      return { method, params };    },    async *events() {},  },});
[/code]

## Bir agent çalıştırma

Uygulama bir agent tutamacı istediğinde `oc.agents.get(id)` kullanın, ardından `agent.run()` çağırın.

typescriptCopy code
[code]
    const agent = await oc.agents.get("main"); const run = await agent.run({  input: "Review this pull request and suggest the smallest safe fix.",  model: "openai/gpt-5.5",  sessionKey: "main",  timeoutMs: 30_000,}); for await (const event of run.events()) {  const data = event.data as { delta?: unknown };  if (event.type === "assistant.delta" && typeof data.delta === "string") {    process.stdout.write(data.delta);  }} const result = await run.wait({ timeoutMs: 120_000 });console.log(result.status);
[/code]

`openai/gpt-5.5` gibi sağlayıcı nitelikli model referansları Gateway `provider` ve `model` geçersiz kılmalarına ayrılır. `timeoutMs` SDK'da milisaniye olarak kalır ve `agent` RPC'si için Gateway zaman aşımı saniyelerine dönüştürülür.

`run.wait()`, Gateway `agent.wait` RPC'sini kullanır. Çalıştırma hâlâ etkinken süresi dolan bir bekleme son tarihi, çalıştırmanın kendisinin zaman aşımına uğradığını varsaymak yerine `status: "accepted"` döndürür. Çalışma zamanı zaman aşımları, durdurulmuş çalıştırmalar ve iptal edilmiş çalıştırmalar `timed_out` veya `cancelled` olarak normalize edilir.

## Oturum oluşturma ve yeniden kullanma

Uygulama kalıcı transcript durumu istediğinde oturumları kullanın.

typescriptCopy code
[code]
    const session = await oc.sessions.create({  agentId: "main",  label: "release-review",}); const run = await session.send("Prepare release notes from the current diff.");await run.wait();
[/code]

`Session.send()`, `sessions.send` çağrısı yapar ve bir `Run` döndürür. Oturum tutamaçları ayrıca şunları destekler:

typescriptCopy code
[code]
    await session.abort(run.id);await session.patch({ label: "renamed-session" });await session.compact({ maxLines: 200 });
[/code]

## Olayları yayınlama

SDK, ham Gateway olaylarını kararlı bir `OpenClawEvent` zarfına normalize eder:

typescriptCopy code
[code]
    type OpenClawEvent = {  version: 1;  id: string;  ts: number;  type: OpenClawEventType;  runId?: string;  sessionId?: string;  sessionKey?: string;  taskId?: string;  agentId?: string;  data: unknown;  raw?: GatewayEvent;};
[/code]

Yaygın olay türleri şunları içerir:

Olay türü | Kaynak Gateway olayı  
---|---  
`run.started` | `agent` yaşam döngüsü başlangıcı  
`run.completed` | `agent` yaşam döngüsü sonu  
`run.failed` | `agent` yaşam döngüsü hatası  
`run.cancelled` | Durdurulmuş/iptal edilmiş yaşam döngüsü sonu  
`run.timed_out` | Zaman aşımı yaşam döngüsü sonu  
`assistant.delta` | Assistant yayın deltası  
`assistant.message` | Assistant mesajı  
`thinking.delta` | Düşünme veya plan akışı  
`tool.call.started` | Araç/öğe/komut başlangıcı  
`tool.call.delta` | Araç/öğe/komut güncellemesi  
`tool.call.completed` | Araç/öğe/komut tamamlanması  
`tool.call.failed` | Araç/öğe/komut hatası veya engellenmiş durum  
`approval.requested` | Exec veya Plugin onay isteği  
`approval.resolved` | Exec veya Plugin onay çözümü  
`session.created` | `sessions.changed` oluşturma  
`session.updated` | `sessions.changed` güncelleme  
`session.compacted` | `sessions.changed` compaction  
`task.updated` | Görev güncelleme olayları  
`artifact.updated` | Yama akışı olayları  
`raw` | Henüz kararlı SDK eşlemesi olmayan herhangi bir olay  
  
`Run.events()`, olayları tek bir çalıştırma id'sine göre filtreler ve hızlı çalıştırmalar için daha önce görülmüş olayları yeniden oynatır. Bu, belgelenen akışın güvenli olduğu anlamına gelir:

typescriptCopy code
[code]
    const run = await agent.run("Summarize the latest session."); for await (const event of run.events()) {  if (event.type === "run.completed") {    break;  }}
[/code]

Uygulama genelindeki akışlar için `oc.events()` kullanın. Ham Gateway çerçeveleri için `oc.rawEvents()` kullanın.

## Modeller, araçlar, artifact'ler ve onaylar

Model yardımcıları geçerli Gateway yöntemleriyle eşleşir:

typescriptCopy code
[code]
    await oc.models.list();await oc.models.status({ probe: false }); // calls models.authStatus
[/code]

Araç yardımcıları Gateway kataloğunu, etkin araç görünümünü ve doğrudan Gateway araç çağrısını açığa çıkarır. `oc.tools.invoke()`, ilke veya onay retlerinde hata fırlatmak yerine türlenmiş bir zarf döndürür.

typescriptCopy code
[code]
    await oc.tools.list();await oc.tools.effective({ sessionKey: "main" });await oc.tools.invoke("tool-name", {  args: { input: "value" },  sessionKey: "main",  confirm: false,  idempotencyKey: "tool-call-1",});
[/code]

Artifact yardımcıları, oturum, çalıştırma veya görev bağlamı için Gateway artifact projeksiyonunu açığa çıkarır. Her çağrı açık bir `sessionKey`, `runId` veya `taskId` kapsamı gerektirir:

typescriptCopy code
[code]
    const { artifacts } = await oc.artifacts.list({ sessionKey: "main" });const first = artifacts[0]; if (first) {  const { artifact } = await oc.artifacts.get(first.id, { sessionKey: "main" });  const download = await oc.artifacts.download(artifact.id, { sessionKey: "main" });  console.log(download.encoding, download.url);}
[/code]

Onay yardımcıları exec onay RPC'lerini kullanır:

typescriptCopy code
[code]
    const approvals = await oc.approvals.list();await oc.approvals.respond("approval-id", { decision: "approve" });
[/code]

Görev yardımcıları, `openclaw tasks` için de temel oluşturan kalıcı görev defterini kullanır:

typescriptCopy code
[code]
    const tasks = await oc.tasks.list({ status: "running", sessionKey: "agent:main:main" });const task = await oc.tasks.get(tasks.tasks[0].id);await oc.tasks.cancel(task.task.id, { reason: "user stopped task" });
[/code]

Ortam yardımcıları salt okunur Gateway yerel ve node keşfini açığa çıkarır:

typescriptCopy code
[code]
    const { environments } = await oc.environments.list();await oc.environments.status(environments[0].id);
[/code]

## Bugün açıkça desteklenmeyenler

SDK, istediğimiz ürün modeli için adlar içerir, ancak Gateway RPC'leri varmış gibi sessizce davranmaz. Bu çağrılar şu anda açık desteklenmeyen hata fırlatır:

typescriptCopy code
[code]
    await oc.environments.create({});await oc.environments.delete("environment-id");
[/code]

Çalıştırma başına `workspace`, `runtime`, `environment` ve `approvals` alanları gelecekteki biçim olarak türlenmiştir, ancak geçerli Gateway bu geçersiz kılmaları `agent` RPC'sinde desteklemez. Çağıranlar bunları iletirse SDK, işin varsayılan workspace, runtime, environment veya approval davranışıyla yanlışlıkla yürütülmemesi için çalıştırmayı göndermeden önce hata fırlatır.

## App SDK ve Plugin SDK karşılaştırması

Kod OpenClaw dışında yaşadığında App SDK kullanın:

  * Agent çalıştırmaları başlatan veya gözlemleyen Node betikleri
  * Bir Gateway çağıran CI işleri
  * panolar ve yönetim panelleri
  * IDE eklentileri
  * kanal Plugin'leri hâline gelmesi gerekmeyen dış köprüler
  * sahte veya gerçek Gateway aktarımlarıyla entegrasyon testleri


Kod OpenClaw içinde çalıştığında Plugin SDK kullanın:

  * sağlayıcı Plugin'leri
  * kanal Plugin'leri
  * araç veya yaşam döngüsü hook'ları
  * agent harness Plugin'leri
  * güvenilen çalışma zamanı yardımcıları


App SDK kodu `@openclaw/sdk` içinden import etmelidir. Plugin kodu belgelenmiş `openclaw/plugin-sdk/*` alt yollarından import etmelidir. İki sözleşmeyi karıştırmayın.

## İlgili

  * [OpenClaw Uygulama SDK API tasarımı](</tr/reference/openclaw-sdk-api-design>)
  * [Gateway RPC referansı](</tr/reference/rpc>)
  * [Ajan döngüsü](</tr/concepts/agent-loop>)
  * [Ajan çalışma zamanları](</tr/concepts/agent-runtimes>)
  * [Oturumlar](</tr/concepts/session>)
  * [Arka plan görevleri](</tr/automation/tasks>)
  * [ACP ajanları](</tr/tools/acp-agents>)
  * [Plugin SDK genel bakışı](</tr/plugins/sdk-overview>)


Was this useful?YesNo