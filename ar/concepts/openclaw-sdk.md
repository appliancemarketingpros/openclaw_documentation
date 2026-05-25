---
title: حزمة تطوير تطبيقات OpenClaw
source_url: https://docs.openclaw.ai/ar/concepts/openclaw-sdk
scraped_at: 2026-05-25
---

يُعد **OpenClaw App SDK** واجهة API العامة للعميل للتطبيقات خارج عملية OpenClaw. استخدم `@openclaw/sdk` عندما يريد سكربت أو لوحة معلومات أو مهمة CI أو إضافة IDE أو تطبيق خارجي آخر الاتصال بـ Gateway، أو بدء تشغيلات الوكيل، أو بث الأحداث، أو انتظار النتائج، أو إلغاء العمل، أو فحص موارد Gateway.

## ما يتوفر اليوم

يأتي `@openclaw/sdk` مع:

السطح | الحالة | ما يفعله  
---|---|---  
`OpenClaw` | جاهز | نقطة الدخول الرئيسية للعميل. يمتلك النقل والاتصال والطلبات والأحداث.  
`GatewayClientTransport` | جاهز | نقل WebSocket مدعوم بعميل Gateway.  
`oc.agents` | جاهز | يسرد مقابض الوكلاء وينشئها ويحدثها ويحذفها ويحصل عليها.  
`Agent.run()` | جاهز | يبدأ تشغيل Gateway من نوع `agent` ويعيد `Run`.  
`oc.runs` | جاهز | ينشئ التشغيلات ويحصل عليها وينتظرها ويلغيها ويبثها.  
`Run.events()` | جاهز | يبث أحداثا موحدة لكل تشغيل مع إعادة تشغيل للتشغيلات السريعة.  
`Run.wait()` | جاهز | يستدعي `agent.wait` ويعيد `RunResult` مستقرا.  
`Run.cancel()` | جاهز | يستدعي `sessions.abort` بواسطة معرف التشغيل، مع مفتاح الجلسة عند توفره.  
`oc.sessions` | جاهز | ينشئ مقابض الجلسات ويحلها ويرسل إليها ويرقعها ويضغطها ويحصل عليها.  
`Session.send()` | جاهز | يستدعي `sessions.send` ويعيد `Run`.  
`oc.tasks` | جاهز | يسرد إدخالات سجل مهام Gateway ويقرأها ويلغيها.  
`oc.models` | جاهز | يستدعي `models.list` وRPC الحالة الحالي `models.authStatus`.  
`oc.tools` | جاهز | يسرد أدوات Gateway ويحدد نطاقها ويستدعيها عبر مسار السياسة.  
`oc.artifacts` | جاهز | يسرد عناصر Gateway النصية ويحصل عليها وينزلها.  
`oc.approvals` | جاهز | يسرد موافقات exec ويحلها عبر استدعاءات RPC الخاصة بموافقات Gateway.  
`oc.environments` | جزئي | يسرد مرشحي البيئات المحلية لـ Gateway وnode؛ الإنشاء/الحذف غير موصولين.  
`oc.rawEvents()` | جاهز | يتيح أحداث Gateway الخام للمستهلكين المتقدمين.  
`normalizeGatewayEvent()` | جاهز | يحول أحداث Gateway الخام إلى شكل حدث SDK المستقر.  
  
يصدر SDK أيضا الأنواع الأساسية التي تستخدمها هذه الأسطح: `AgentRunParams`, `RunResult`, `RunStatus`, `OpenClawEvent`, `OpenClawEventType`, `GatewayEvent`, `OpenClawTransport`, `GatewayRequestOptions`, `SessionCreateParams`, `SessionSendParams`, `ArtifactSummary`, `ArtifactQuery`, `ArtifactsListResult`, `ArtifactsGetResult`, `ArtifactsDownloadResult`, `TaskSummary`, `TaskStatus`, `TasksListParams`, `TasksListResult`, `TasksGetResult`, `TasksCancelResult`, `RuntimeSelection`, `EnvironmentSelection`, `WorkspaceSelection`, `ApprovalMode`، وأنواع النتائج ذات الصلة.

## الاتصال بـ Gateway

أنشئ عميلا بعنوان URL صريح لـ Gateway، أو مرر نقلا مخصصا للاختبارات وبيئات تشغيل التطبيقات المضمنة.

typescriptCopy code
[code]
     const oc = new OpenClaw({  url: "ws://127.0.0.1:18789",  token: process.env.OPENCLAW_GATEWAY_TOKEN,  requestTimeoutMs: 30_000,}); await oc.connect();
[/code]

`new OpenClaw({ gateway: "ws://..." })` يكافئ `url`. يقبل المنشئ الخيار `gateway: "auto"`، لكن اكتشاف Gateway التلقائي ليس ميزة SDK مستقلة بعد؛ مرر `url` عندما لا يعرف التطبيق مسبقا كيفية اكتشاف Gateway.

للاختبارات، مرر كائنا ينفذ `OpenClawTransport`:

typescriptCopy code
[code]
    const oc = new OpenClaw({  transport: {    async request(method, params) {      return { method, params };    },    async *events() {},  },});
[/code]

## تشغيل وكيل

استخدم `oc.agents.get(id)` عندما يريد التطبيق مقبض وكيل، ثم استدع `agent.run()`.

typescriptCopy code
[code]
    const agent = await oc.agents.get("main"); const run = await agent.run({  input: "Review this pull request and suggest the smallest safe fix.",  model: "openai/gpt-5.5",  sessionKey: "main",  timeoutMs: 30_000,}); for await (const event of run.events()) {  const data = event.data as { delta?: unknown };  if (event.type === "assistant.delta" && typeof data.delta === "string") {    process.stdout.write(data.delta);  }} const result = await run.wait({ timeoutMs: 120_000 });console.log(result.status);
[/code]

تُقسم مراجع النماذج المؤهلة بالمزود مثل `openai/gpt-5.5` إلى تجاوزات Gateway `provider` و`model`. يبقى `timeoutMs` بالمللي ثانية في SDK ويُحول إلى ثواني مهلة Gateway من أجل RPC الخاص بـ `agent`.

يستخدم `run.wait()` استدعاء RPC الخاص بـ Gateway `agent.wait`. عندما تنتهي مهلة انتظار بينما لا يزال التشغيل نشطا، يعيد `status: "accepted"` بدلا من الادعاء بأن التشغيل نفسه انتهت مهلته. تُوحد مهل التشغيل، والتشغيلات التي أُجهضت، والتشغيلات الملغاة إلى `timed_out` أو `cancelled`.

## إنشاء الجلسات وإعادة استخدامها

استخدم الجلسات عندما يريد التطبيق حالة نصية دائمة.

typescriptCopy code
[code]
    const session = await oc.sessions.create({  agentId: "main",  label: "release-review",}); const run = await session.send("Prepare release notes from the current diff.");await run.wait();
[/code]

يستدعي `Session.send()` الدالة `sessions.send` ويعيد `Run`. تدعم مقابض الجلسات أيضا:

typescriptCopy code
[code]
    await session.abort(run.id);await session.patch({ label: "renamed-session" });await session.compact({ maxLines: 200 });
[/code]

## بث الأحداث

يوحد SDK أحداث Gateway الخام في غلاف `OpenClawEvent` مستقر:

typescriptCopy code
[code]
    type OpenClawEvent = {  version: 1;  id: string;  ts: number;  type: OpenClawEventType;  runId?: string;  sessionId?: string;  sessionKey?: string;  taskId?: string;  agentId?: string;  data: unknown;  raw?: GatewayEvent;};
[/code]

تشمل أنواع الأحداث الشائعة:

نوع الحدث | حدث Gateway المصدر  
---|---  
`run.started` | بداية دورة حياة `agent`  
`run.completed` | نهاية دورة حياة `agent`  
`run.failed` | خطأ دورة حياة `agent`  
`run.cancelled` | نهاية دورة حياة مُجهضة/ملغاة  
`run.timed_out` | نهاية دورة حياة بسبب انتهاء المهلة  
`assistant.delta` | فرق بث المساعد  
`assistant.message` | رسالة المساعد  
`thinking.delta` | بث التفكير أو الخطة  
`tool.call.started` | بدء أداة/عنصر/أمر  
`tool.call.delta` | تحديث أداة/عنصر/أمر  
`tool.call.completed` | اكتمال أداة/عنصر/أمر  
`tool.call.failed` | فشل أداة/عنصر/أمر أو حالة محظورة  
`approval.requested` | طلب موافقة exec أو plugin  
`approval.resolved` | حل موافقة exec أو plugin  
`session.created` | إنشاء `sessions.changed`  
`session.updated` | تحديث `sessions.changed`  
`session.compacted` | ضغط `sessions.changed`  
`task.updated` | أحداث تحديث المهمة  
`artifact.updated` | أحداث بث الرقع  
`raw` | أي حدث لا يملك بعد ربط SDK مستقرا  
  
يرشح `Run.events()` الأحداث إلى معرف تشغيل واحد ويعيد تشغيل الأحداث التي شوهدت بالفعل للتشغيلات السريعة. هذا يعني أن التدفق الموثق آمن:

typescriptCopy code
[code]
    const run = await agent.run("Summarize the latest session."); for await (const event of run.events()) {  if (event.type === "run.completed") {    break;  }}
[/code]

للبث على مستوى التطبيق، استخدم `oc.events()`. ولإطارات Gateway الخام، استخدم `oc.rawEvents()`.

## النماذج والأدوات والعناصر والموافقات

تتطابق مساعدات النماذج مع طرق Gateway الحالية:

typescriptCopy code
[code]
    await oc.models.list();await oc.models.status({ probe: false }); // calls models.authStatus
[/code]

تعرض مساعدات الأدوات كتالوج Gateway، وعرض الأدوات الفعال، والاستدعاء المباشر لأدوات Gateway. يعيد `oc.tools.invoke()` غلافا مكتوبا بدلا من الرمي عند رفض السياسة أو الموافقة.

typescriptCopy code
[code]
    await oc.tools.list();await oc.tools.effective({ sessionKey: "main" });await oc.tools.invoke("tool-name", {  args: { input: "value" },  sessionKey: "main",  confirm: false,  idempotencyKey: "tool-call-1",});
[/code]

تعرض مساعدات العناصر إسقاط عناصر Gateway لسياق الجلسة أو التشغيل أو المهمة. يتطلب كل استدعاء نطاقا صريحا واحدا من `sessionKey` أو `runId` أو `taskId`:

typescriptCopy code
[code]
    const { artifacts } = await oc.artifacts.list({ sessionKey: "main" });const first = artifacts[0]; if (first) {  const { artifact } = await oc.artifacts.get(first.id, { sessionKey: "main" });  const download = await oc.artifacts.download(artifact.id, { sessionKey: "main" });  console.log(download.encoding, download.url);}
[/code]

تستخدم مساعدات الموافقة استدعاءات RPC الخاصة بموافقات exec:

typescriptCopy code
[code]
    const approvals = await oc.approvals.list();await oc.approvals.respond("approval-id", { decision: "approve" });
[/code]

تستخدم مساعدات المهام سجل المهام الدائم الذي يدعم أيضا `openclaw tasks`:

typescriptCopy code
[code]
    const tasks = await oc.tasks.list({ status: "running", sessionKey: "agent:main:main" });const task = await oc.tasks.get(tasks.tasks[0].id);await oc.tasks.cancel(task.task.id, { reason: "user stopped task" });
[/code]

تعرض مساعدات البيئة اكتشاف Gateway المحلي وnode للقراءة فقط:

typescriptCopy code
[code]
    const { environments } = await oc.environments.list();await oc.environments.status(environments[0].id);
[/code]

## غير مدعوم صراحة اليوم

يتضمن SDK أسماء لنموذج المنتج الذي نريده، لكنه لا يتظاهر بصمت بأن استدعاءات RPC الخاصة بـ Gateway موجودة. ترمي هذه الاستدعاءات حاليا أخطاء صريحة لعدم الدعم:

typescriptCopy code
[code]
    await oc.environments.create({});await oc.environments.delete("environment-id");
[/code]

حقول كل تشغيل `workspace` و`runtime` و`environment` و`approvals` مكتوبة كشكل مستقبلي، لكن Gateway الحالي لا يدعم تلك التجاوزات على RPC الخاص بـ `agent`. إذا مررها المستدعون، يرمي SDK قبل إرسال التشغيل حتى لا ينفذ العمل بالخطأ بسلوك مساحة العمل أو وقت التشغيل أو البيئة أو الموافقة الافتراضي.

## App SDK مقابل Plugin SDK

استخدم App SDK عندما يعيش الكود خارج OpenClaw:

  * سكربتات Node التي تبدأ تشغيلات الوكلاء أو تراقبها
  * مهام CI التي تستدعي Gateway
  * لوحات المعلومات ولوحات الإدارة
  * إضافات IDE
  * الجسور الخارجية التي لا تحتاج إلى أن تصبح plugins قنوات
  * اختبارات التكامل مع نقل Gateway وهمي أو حقيقي


استخدم Plugin SDK عندما يعمل الكود داخل OpenClaw:

  * plugins المزودين
  * plugins القنوات
  * خطافات الأدوات أو دورة الحياة
  * plugins حاضنة الوكيل
  * مساعدات وقت التشغيل الموثوقة


ينبغي لكود App SDK الاستيراد من `@openclaw/sdk`. وينبغي لكود Plugin الاستيراد من مسارات `openclaw/plugin-sdk/*` الفرعية الموثقة. لا تخلط بين العقدين.

## ذات صلة

  * [تصميم API لـ OpenClaw App SDK](</ar/reference/openclaw-sdk-api-design>)
  * [مرجع RPC لـ Gateway](</ar/reference/rpc>)
  * [حلقة الوكيل](</ar/concepts/agent-loop>)
  * [بيئات تشغيل الوكيل](</ar/concepts/agent-runtimes>)
  * [الجلسات](</ar/concepts/session>)
  * [مهام الخلفية](</ar/automation/tasks>)
  * [وكلاء ACP](</ar/tools/acp-agents>)
  * [نظرة عامة على Plugin SDK](</ar/plugins/sdk-overview>)


Was this useful?YesNo