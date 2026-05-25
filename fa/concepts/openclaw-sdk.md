---
title: SDK برنامه OpenClaw
source_url: https://docs.openclaw.ai/fa/concepts/openclaw-sdk
scraped_at: 2026-05-25
---

SDK برنامه **OpenClaw** ، API عمومی کلاینت برای برنامه‌های خارج از فرایند OpenClaw است. وقتی یک اسکریپت، داشبورد، کار CI، افزونه IDE یا برنامه خارجی دیگری می‌خواهد به Gateway وصل شود، اجرای agentها را آغاز کند، رویدادها را stream کند، منتظر نتایج بماند، کار را لغو کند، یا منابع Gateway را بررسی کند، از `@openclaw/sdk` استفاده کنید.

## آنچه امروز ارائه می‌شود

`@openclaw/sdk` شامل این موارد است:

سطح | وضعیت | کارکرد  
---|---|---  
`OpenClaw` | آماده | نقطه ورود اصلی کلاینت. transport، اتصال، درخواست‌ها و رویدادها را در اختیار دارد.  
`GatewayClientTransport` | آماده | transport وب‌سوکت که توسط کلاینت Gateway پشتیبانی می‌شود.  
`oc.agents` | آماده | handleهای agent را فهرست، ایجاد، به‌روزرسانی، حذف و دریافت می‌کند.  
`Agent.run()` | آماده | یک اجرای Gateway `agent` را شروع می‌کند و یک `Run` برمی‌گرداند.  
`oc.runs` | آماده | اجراها را ایجاد، دریافت، منتظر، لغو و stream می‌کند.  
`Run.events()` | آماده | رویدادهای نرمال‌شده هر اجرا را با replay برای اجراهای سریع stream می‌کند.  
`Run.wait()` | آماده | `agent.wait` را فراخوانی می‌کند و یک `RunResult` پایدار برمی‌گرداند.  
`Run.cancel()` | آماده | `sessions.abort` را بر اساس شناسه اجرا، همراه با کلید نشست در صورت وجود، فراخوانی می‌کند.  
`oc.sessions` | آماده | handleهای نشست را ایجاد، resolve، ارسال، patch، compact و دریافت می‌کند.  
`Session.send()` | آماده | `sessions.send` را فراخوانی می‌کند و یک `Run` برمی‌گرداند.  
`oc.tasks` | آماده | ورودی‌های دفترکل وظیفه Gateway را فهرست، خواندن و لغو می‌کند.  
`oc.models` | آماده | `models.list` و RPC وضعیت فعلی `models.authStatus` را فراخوانی می‌کند.  
`oc.tools` | آماده | ابزارهای Gateway را از مسیر pipeline سیاست فهرست، scope و invoke می‌کند.  
`oc.artifacts` | آماده | artifactهای transcript مربوط به Gateway را فهرست، دریافت و دانلود می‌کند.  
`oc.approvals` | آماده | تأییدیه‌های exec را از طریق RPCهای تأیید Gateway فهرست و resolve می‌کند.  
`oc.environments` | جزئی | گزینه‌های environment محلی Gateway و node را فهرست می‌کند؛ create/delete متصل نشده‌اند.  
`oc.rawEvents()` | آماده | رویدادهای خام Gateway را برای مصرف‌کنندگان پیشرفته در دسترس می‌گذارد.  
`normalizeGatewayEvent()` | آماده | رویدادهای خام Gateway را به شکل پایدار رویداد SDK تبدیل می‌کند.  
  
SDK همچنین typeهای اصلی استفاده‌شده توسط این سطح‌ها را export می‌کند: `AgentRunParams`, `RunResult`, `RunStatus`, `OpenClawEvent`, `OpenClawEventType`, `GatewayEvent`, `OpenClawTransport`, `GatewayRequestOptions`, `SessionCreateParams`, `SessionSendParams`, `ArtifactSummary`, `ArtifactQuery`, `ArtifactsListResult`, `ArtifactsGetResult`, `ArtifactsDownloadResult`, `TaskSummary`, `TaskStatus`, `TasksListParams`, `TasksListResult`, `TasksGetResult`, `TasksCancelResult`, `RuntimeSelection`, `EnvironmentSelection`, `WorkspaceSelection`, `ApprovalMode` و typeهای نتیجه مرتبط.

## اتصال به Gateway

یک کلاینت با URL صریح Gateway ایجاد کنید، یا برای تست‌ها و runtimeهای برنامه embedded یک transport سفارشی تزریق کنید.

typescriptCopy code
[code]
     const oc = new OpenClaw({  url: "ws://127.0.0.1:18789",  token: process.env.OPENCLAW_GATEWAY_TOKEN,  requestTimeoutMs: 30_000,}); await oc.connect();
[/code]

`new OpenClaw({ gateway: "ws://..." })` معادل `url` است. گزینه `gateway: "auto"` توسط constructor پذیرفته می‌شود، اما کشف خودکار Gateway هنوز قابلیت جداگانه‌ای در SDK نیست؛ وقتی برنامه از قبل نمی‌داند Gateway را چطور کشف کند، `url` را بدهید.

برای تست‌ها، یک شیء بدهید که `OpenClawTransport` را پیاده‌سازی می‌کند:

typescriptCopy code
[code]
    const oc = new OpenClaw({  transport: {    async request(method, params) {      return { method, params };    },    async *events() {},  },});
[/code]

## اجرای یک agent

وقتی برنامه به handle یک agent نیاز دارد، از `oc.agents.get(id)` استفاده کنید، سپس `agent.run()` را فراخوانی کنید.

typescriptCopy code
[code]
    const agent = await oc.agents.get("main"); const run = await agent.run({  input: "Review this pull request and suggest the smallest safe fix.",  model: "openai/gpt-5.5",  sessionKey: "main",  timeoutMs: 30_000,}); for await (const event of run.events()) {  const data = event.data as { delta?: unknown };  if (event.type === "assistant.delta" && typeof data.delta === "string") {    process.stdout.write(data.delta);  }} const result = await run.wait({ timeoutMs: 120_000 });console.log(result.status);
[/code]

ارجاع‌های مدل دارای provider، مانند `openai/gpt-5.5`، به overrideهای Gateway `provider` و `model` تقسیم می‌شوند. `timeoutMs` در SDK بر حسب میلی‌ثانیه می‌ماند و برای RPC `agent` به timeout بر حسب ثانیه در Gateway تبدیل می‌شود.

`run.wait()` از RPC Gateway با نام `agent.wait` استفاده می‌کند. deadline انتظار که در حالی منقضی شود که اجرا هنوز فعال است، به‌جای اینکه وانمود کند خود اجرا timeout شده، `status: "accepted"` برمی‌گرداند. timeoutهای runtime، اجراهای abort شده و اجراهای cancel شده به `timed_out` یا `cancelled` نرمال می‌شوند.

## ایجاد و استفاده دوباره از نشست‌ها

وقتی برنامه به وضعیت transcript پایدار نیاز دارد، از نشست‌ها استفاده کنید.

typescriptCopy code
[code]
    const session = await oc.sessions.create({  agentId: "main",  label: "release-review",}); const run = await session.send("Prepare release notes from the current diff.");await run.wait();
[/code]

`Session.send()`، `sessions.send` را فراخوانی می‌کند و یک `Run` برمی‌گرداند. handleهای نشست همچنین از این موارد پشتیبانی می‌کنند:

typescriptCopy code
[code]
    await session.abort(run.id);await session.patch({ label: "renamed-session" });await session.compact({ maxLines: 200 });
[/code]

## Stream کردن رویدادها

SDK رویدادهای خام Gateway را به یک envelope پایدار `OpenClawEvent` نرمال می‌کند:

typescriptCopy code
[code]
    type OpenClawEvent = {  version: 1;  id: string;  ts: number;  type: OpenClawEventType;  runId?: string;  sessionId?: string;  sessionKey?: string;  taskId?: string;  agentId?: string;  data: unknown;  raw?: GatewayEvent;};
[/code]

نوع‌های رایج رویداد شامل این موارد هستند:

نوع رویداد | رویداد مبدأ Gateway  
---|---  
`run.started` | شروع lifecycle مربوط به `agent`  
`run.completed` | پایان lifecycle مربوط به `agent`  
`run.failed` | خطای lifecycle مربوط به `agent`  
`run.cancelled` | پایان lifecycle abort/cancel شده  
`run.timed_out` | پایان lifecycle به دلیل timeout  
`assistant.delta` | delta مربوط به streaming دستیار  
`assistant.message` | پیام دستیار  
`thinking.delta` | stream فکر کردن یا طرح  
`tool.call.started` | شروع ابزار/آیتم/دستور  
`tool.call.delta` | به‌روزرسانی ابزار/آیتم/دستور  
`tool.call.completed` | تکمیل ابزار/آیتم/دستور  
`tool.call.failed` | شکست ابزار/آیتم/دستور یا وضعیت blocked  
`approval.requested` | درخواست تأیید exec یا Plugin  
`approval.resolved` | resolve شدن تأیید exec یا Plugin  
`session.created` | create مربوط به `sessions.changed`  
`session.updated` | update مربوط به `sessions.changed`  
`session.compacted` | compaction مربوط به `sessions.changed`  
`task.updated` | رویدادهای به‌روزرسانی وظیفه  
`artifact.updated` | رویدادهای stream مربوط به patch  
`raw` | هر رویدادی که هنوز نگاشت پایدار SDK ندارد  
  
`Run.events()` رویدادها را به یک شناسه اجرا filter می‌کند و رویدادهای قبلاً دیده‌شده را برای اجراهای سریع replay می‌کند. یعنی جریان مستندشده امن است:

typescriptCopy code
[code]
    const run = await agent.run("Summarize the latest session."); for await (const event of run.events()) {  if (event.type === "run.completed") {    break;  }}
[/code]

برای streamهای سراسری برنامه، از `oc.events()` استفاده کنید. برای frameهای خام Gateway، از `oc.rawEvents()` استفاده کنید.

## مدل‌ها، ابزارها، artifactها و تأییدیه‌ها

helperهای مدل به methodهای فعلی Gateway map می‌شوند:

typescriptCopy code
[code]
    await oc.models.list();await oc.models.status({ probe: false }); // calls models.authStatus
[/code]

helperهای ابزار، catalog Gateway، نمای مؤثر ابزار و invocation مستقیم ابزار Gateway را expose می‌کنند. `oc.tools.invoke()` به‌جای throw کردن برای رد شدن توسط سیاست یا تأیید، یک envelope typed برمی‌گرداند.

typescriptCopy code
[code]
    await oc.tools.list();await oc.tools.effective({ sessionKey: "main" });await oc.tools.invoke("tool-name", {  args: { input: "value" },  sessionKey: "main",  confirm: false,  idempotencyKey: "tool-call-1",});
[/code]

helperهای artifact، projection artifact Gateway را برای زمینه نشست، اجرا یا وظیفه expose می‌کنند. هر فراخوانی به یک scope صریح `sessionKey`، `runId` یا `taskId` نیاز دارد:

typescriptCopy code
[code]
    const { artifacts } = await oc.artifacts.list({ sessionKey: "main" });const first = artifacts[0]; if (first) {  const { artifact } = await oc.artifacts.get(first.id, { sessionKey: "main" });  const download = await oc.artifacts.download(artifact.id, { sessionKey: "main" });  console.log(download.encoding, download.url);}
[/code]

helperهای تأیید از RPCهای تأیید exec استفاده می‌کنند:

typescriptCopy code
[code]
    const approvals = await oc.approvals.list();await oc.approvals.respond("approval-id", { decision: "approve" });
[/code]

helperهای وظیفه از دفترکل وظیفه پایدار استفاده می‌کنند که پشتوانه `openclaw tasks` نیز هست:

typescriptCopy code
[code]
    const tasks = await oc.tasks.list({ status: "running", sessionKey: "agent:main:main" });const task = await oc.tasks.get(tasks.tasks[0].id);await oc.tasks.cancel(task.task.id, { reason: "user stopped task" });
[/code]

helperهای environment کشف فقط‌خواندنی محلی Gateway و node را expose می‌کنند:

typescriptCopy code
[code]
    const { environments } = await oc.environments.list();await oc.environments.status(environments[0].id);
[/code]

## موارد صریحاً پشتیبانی‌نشده امروز

SDK نام‌هایی را برای مدل محصولی که می‌خواهیم شامل می‌شود، اما بی‌صدا وانمود نمی‌کند RPCهای Gateway وجود دارند. این فراخوانی‌ها در حال حاضر خطاهای پشتیبانی‌نشده صریح throw می‌کنند:

typescriptCopy code
[code]
    await oc.environments.create({});await oc.environments.delete("environment-id");
[/code]

فیلدهای هر اجرا با نام‌های `workspace`، `runtime`، `environment` و `approvals` به‌عنوان شکل آینده typed شده‌اند، اما Gateway فعلی از آن overrideها روی RPC `agent` پشتیبانی نمی‌کند. اگر فراخوان‌ها آن‌ها را بدهند، SDK پیش از ارسال اجرا throw می‌کند تا کار به‌طور تصادفی با رفتار پیش‌فرض workspace، runtime، environment یا approval اجرا نشود.

## SDK برنامه در برابر SDK Plugin

وقتی کد خارج از OpenClaw قرار دارد، از SDK برنامه استفاده کنید:

  * اسکریپت‌های Node که اجراهای agent را شروع یا مشاهده می‌کنند
  * کارهای CI که یک Gateway را فراخوانی می‌کنند
  * داشبوردها و پنل‌های مدیریت
  * افزونه‌های IDE
  * bridgeهای خارجی که لازم نیست به Plugin کانال تبدیل شوند
  * تست‌های integration با transportهای Gateway واقعی یا fake


وقتی کد داخل OpenClaw اجرا می‌شود، از SDK Plugin استفاده کنید:

  * Pluginهای provider
  * Pluginهای کانال
  * hookهای ابزار یا lifecycle
  * Pluginهای harness مربوط به agent
  * helperهای runtime مورد اعتماد


کد SDK برنامه باید از `@openclaw/sdk` import کند. کد Plugin باید از subpathهای مستندشده `openclaw/plugin-sdk/*` import کند. این دو قرارداد را با هم مخلوط نکنید.

## مرتبط

  * [طراحی API ‏SDK برنامه OpenClaw](</fa/reference/openclaw-sdk-api-design>)
  * [مرجع RPC ‏Gateway](</fa/reference/rpc>)
  * [حلقه عامل](</fa/concepts/agent-loop>)
  * [زمان‌های اجرای عامل](</fa/concepts/agent-runtimes>)
  * [نشست‌ها](</fa/concepts/session>)
  * [وظایف پس‌زمینه](</fa/automation/tasks>)
  * [عامل‌های ACP](</fa/tools/acp-agents>)
  * [نمای کلی SDK ‏Plugin](</fa/plugins/sdk-overview>)


Was this useful?YesNo