---
title: بناء Plugins
source_url: https://docs.openclaw.ai/ar/plugins/building-plugins
scraped_at: 2026-05-25
---

توسّع Plugins إمكانات OpenClaw بإضافة قدرات جديدة: القنوات، ومزوّدي النماذج، والكلام، والنسخ الفوري، والصوت الفوري، وفهم الوسائط، وتوليد الصور، وتوليد الفيديو، وجلب الويب، وبحث الويب، وأدوات الوكيل، أو أي مزيج منها.

لست بحاجة إلى إضافة Plugin الخاص بك إلى مستودع OpenClaw. انشره إلى [ClawHub](</ar/clawhub>) ويثبّته المستخدمون باستخدام `openclaw plugins install clawhub:<package-name>`. ما زالت مواصفات الحزم المجرّدة تُثبَّت من npm أثناء مرحلة الانتقال عند الإطلاق.

## المتطلبات الأساسية

  * Node >= 22 ومدير حزم (npm أو pnpm)
  * الإلمام بـ TypeScript (ESM)
  * بالنسبة إلى Plugins داخل المستودع: يجب أن يكون المستودع مستنسخًا وأن يكون `pnpm install` قد نُفّذ. تطوير Plugin من نسخة مصدر checkout مخصص لـ pnpm فقط لأن OpenClaw يحمّل Plugins المضمّنة من حزم مساحة العمل `extensions/*`.


## ما نوع Plugin؟

[**Plugin قناة** وصّل OpenClaw بمنصة مراسلة (Discord، IRC، وما إلى ذلك) ](</ar/plugins/sdk-channel-plugins>) [**Plugin مزوّد** أضف مزوّد نماذج (LLM، أو وكيل، أو نقطة نهاية مخصصة) ](</ar/plugins/sdk-provider-plugins>) [**Plugin واجهة خلفية لـ CLI** اربط CLI ذكاء اصطناعي محليًا بمشغّل الرجوع النصي في OpenClaw ](</ar/plugins/cli-backend-plugins>) [**Plugin أداة / خطّاف** سجّل أدوات وكيل أو خطافات أحداث أو خدمات - تابع أدناه ](</ar/plugins/hooks>)

بالنسبة إلى Plugin قناة غير مضمون تثبيته عند تشغيل الإعداد/التهيئة الأولية، استخدم `createOptionalChannelSetupSurface(...)` من `openclaw/plugin-sdk/channel-setup`. ينتج ذلك زوجًا من محوّل الإعداد + المعالج الإرشادي يعلن عن متطلب التثبيت ويفشل بإغلاق آمن عند عمليات كتابة الإعدادات الفعلية إلى أن يتم تثبيت Plugin.

## البدء السريع: Plugin أداة

ينشئ هذا الدليل العملي Plugin بسيطًا يسجّل أداة وكيل. لدى Plugins القنوات والمزوّدين أدلة مخصصة مرتبطة أعلاه.

* ### أنشئ الحزمة والبيان

package.jsonCopy code
[code]
    {"name": "@myorg/openclaw-my-plugin","version": "1.0.0","type": "module","openclaw": {  "extensions": ["./index.ts"],  "compat": {    "pluginApi": ">=2026.3.24-beta.2",    "minGatewayVersion": "2026.3.24-beta.2"  },  "build": {    "openclawVersion": "2026.3.24-beta.2",    "pluginSdkVersion": "2026.3.24-beta.2"  }}}
[/code]

openclaw.plugin.jsonCopy code
[code]
    {"id": "my-plugin","name": "My Plugin","description": "Adds a custom tool to OpenClaw","contracts": {  "tools": ["my_tool"]},"activation": {  "onStartup": true},"configSchema": {  "type": "object",  "additionalProperties": false}}
[/code]

يحتاج كل Plugin إلى بيان، حتى من دون إعدادات. يجب إدراج الأدوات المسجّلة وقت التشغيل في `contracts.tools` لكي يتمكن OpenClaw من اكتشاف Plugin المالك من دون تحميل وقت تشغيل كل Plugin. يجب أن تصرّح Plugins أيضًا عن `activation.onStartup` بقصد واضح. يعيّن هذا المثال قيمته إلى `true`. راجع [البيان](</ar/plugins/manifest>) للاطلاع على المخطط الكامل. توجد مقتطفات النشر القانونية في ClawHub في `docs/snippets/plugin-publish/`.

* ### اكتب نقطة الدخول

typescriptCopy code
[code]
    // index.tsimport { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";import { Type } from "@sinclair/typebox"; export default definePluginEntry({  id: "my-plugin",  name: "My Plugin",  description: "Adds a custom tool to OpenClaw",  register(api) {    api.registerTool({      name: "my_tool",      description: "Do a thing",      parameters: Type.Object({ input: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: `Got: ${params.input}` }] };      },    });  },});
[/code]

`definePluginEntry` مخصص لـ Plugins غير القنوات. بالنسبة إلى القنوات، استخدم `defineChannelPluginEntry` \- راجع [Plugins القنوات](</ar/plugins/sdk-channel-plugins>). للاطلاع على خيارات نقطة الدخول الكاملة، راجع [نقاط الدخول](</ar/plugins/sdk-entrypoints>).

* ### اختبر وانشر

**Plugins الخارجية:** تحقّق وانشر باستخدام ClawHub، ثم ثبّت:

bashCopy code
[code]
    clawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginopenclaw plugins install clawhub:@myorg/openclaw-my-plugin
[/code]

تُثبَّت مواصفات الحزم المجرّدة مثل `@myorg/openclaw-my-plugin` من npm أثناء مرحلة الانتقال عند الإطلاق. استخدم `clawhub:` عندما تريد الحل عبر ClawHub.

**Plugins داخل المستودع:** ضعها تحت شجرة مساحة عمل Plugins المضمّنة - وسيتم اكتشافها تلقائيًا.

bashCopy code
[code]
    pnpm test -- <bundled-plugin-root>/my-plugin/
[/code]

## إمكانات Plugin

يمكن لـ Plugin واحد تسجيل أي عدد من الإمكانات عبر كائن `api`:

الإمكانية | طريقة التسجيل | الدليل التفصيلي  
---|---|---  
الاستدلال النصي (LLM) | `api.registerProvider(...)` | [Plugins المزوّدين](</ar/plugins/sdk-provider-plugins>)  
واجهة خلفية للاستدلال عبر CLI | `api.registerCliBackend(...)` | [Plugins الواجهة الخلفية لـ CLI](</ar/plugins/cli-backend-plugins>)  
القناة / المراسلة | `api.registerChannel(...)` | [Plugins القنوات](</ar/plugins/sdk-channel-plugins>)  
الكلام (TTS/STT) | `api.registerSpeechProvider(...)` | [Plugins المزوّدين](</ar/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
النسخ الفوري | `api.registerRealtimeTranscriptionProvider(...)` | [Plugins المزوّدين](</ar/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
الصوت الفوري | `api.registerRealtimeVoiceProvider(...)` | [Plugins المزوّدين](</ar/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
فهم الوسائط | `api.registerMediaUnderstandingProvider(...)` | [Plugins المزوّدين](</ar/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
توليد الصور | `api.registerImageGenerationProvider(...)` | [Plugins المزوّدين](</ar/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
توليد الموسيقى | `api.registerMusicGenerationProvider(...)` | [Plugins المزوّدين](</ar/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
توليد الفيديو | `api.registerVideoGenerationProvider(...)` | [Plugins المزوّدين](</ar/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
جلب الويب | `api.registerWebFetchProvider(...)` | [Plugins المزوّدين](</ar/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
بحث الويب | `api.registerWebSearchProvider(...)` | [Plugins المزوّدين](</ar/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
وسيط نتائج الأدوات | `api.registerAgentToolResultMiddleware(...)` | [نظرة عامة على SDK](</ar/plugins/sdk-overview#registration-api>)  
أدوات الوكيل | `api.registerTool(...)` | أدناه  
أوامر مخصصة | `api.registerCommand(...)` | [نقاط الدخول](</ar/plugins/sdk-entrypoints>)  
خطافات Plugin | `api.on(...)` | [خطافات Plugin](</ar/plugins/hooks>)  
خطافات أحداث داخلية | `api.registerHook(...)` | [نقاط الدخول](</ar/plugins/sdk-entrypoints>)  
مسارات HTTP | `api.registerHttpRoute(...)` | [العناصر الداخلية](</ar/plugins/architecture-internals#gateway-http-routes>)  
أوامر فرعية لـ CLI | `api.registerCli(...)` | [نقاط الدخول](</ar/plugins/sdk-entrypoints>)  
  
للاطلاع على API التسجيل الكامل، راجع [نظرة عامة على SDK](</ar/plugins/sdk-overview#registration-api>).

يمكن لـ Plugins المضمّنة استخدام `api.registerAgentToolResultMiddleware(...)` عندما تحتاج إلى إعادة كتابة نتائج الأدوات بصورة غير متزامنة قبل أن يرى النموذج المخرجات. صرّح عن أوقات التشغيل المستهدفة في `contracts.agentToolResultMiddleware`، على سبيل المثال `["pi", "codex"]`. هذه وصلة موثوقة خاصة بـ Plugin مضمّن؛ وينبغي لـ Plugins الخارجية تفضيل خطافات OpenClaw Plugin العادية ما لم يطوّر OpenClaw سياسة ثقة صريحة لهذه الإمكانية.

إذا كان Plugin الخاص بك يسجّل طرق RPC مخصصة في Gateway، فاحتفظ بها تحت بادئة خاصة بـ Plugin. تظل مساحات أسماء الإدارة الأساسية (`config.*`, `exec.approvals.*`, `wizard.*`, `update.*`) محجوزة وتُحل دائمًا إلى `operator.admin`، حتى إذا طلب Plugin نطاقًا أضيق.

دلالات حارس الخطافات التي يجب وضعها في الاعتبار:

  * `before_tool_call`: يكون `{ block: true }` نهائيًا ويوقف المعالجات ذات الأولوية الأدنى.
  * `before_tool_call`: يُعامَل `{ block: false }` على أنه لا قرار.
  * `before_tool_call`: يوقف `{ requireApproval: true }` تنفيذ الوكيل مؤقتًا ويطلب موافقة المستخدم عبر طبقة موافقات التنفيذ، أو أزرار Telegram، أو تفاعلات Discord، أو أمر `/approve` على أي قناة.
  * `before_install`: يكون `{ block: true }` نهائيًا ويوقف المعالجات ذات الأولوية الأدنى.
  * `before_install`: يُعامَل `{ block: false }` على أنه لا قرار.
  * `message_sending`: يكون `{ cancel: true }` نهائيًا ويوقف المعالجات ذات الأولوية الأدنى.
  * `message_sending`: يُعامَل `{ cancel: false }` على أنه لا قرار.
  * `message_received`: فضّل حقل `threadId` المطبوع عندما تحتاج إلى توجيه سلسلة/موضوع وارد. احتفظ بـ `metadata` للإضافات الخاصة بالقناة.
  * `message_sending`: فضّل حقول التوجيه المطبوعة `replyToId` / `threadId` على مفاتيح metadata الخاصة بالقناة.


يتعامل أمر `/approve` مع موافقات التنفيذ وPlugin معًا باستخدام رجوع محدود: عندما لا يُعثر على معرّف موافقة تنفيذ، يعيد OpenClaw تجربة المعرّف نفسه عبر موافقات Plugin. يمكن تكوين إعادة توجيه موافقات Plugin بشكل مستقل عبر `approvals.plugin` في الإعدادات.

إذا احتاجت سباكة الموافقات المخصصة إلى اكتشاف حالة الرجوع المحدود نفسها، فضّل `isApprovalNotFoundError` من `openclaw/plugin-sdk/error-runtime` بدلًا من مطابقة سلاسل انتهاء صلاحية الموافقات يدويًا.

راجع [خطافات Plugin](</ar/plugins/hooks>) للاطلاع على أمثلة ومرجع الخطافات.

## تسجيل أدوات الوكيل

الأدوات هي دوال مطبوعة يمكن لـ LLM استدعاؤها. يمكن أن تكون مطلوبة (متاحة دائمًا) أو اختيارية (يشترك فيها المستخدم):

typescriptCopy code
[code]
    register(api) {  // Required tool - always available  api.registerTool({    name: "my_tool",    description: "Do a thing",    parameters: Type.Object({ input: Type.String() }),    async execute(_id, params) {      return { content: [{ type: "text", text: params.input }] };    },  });   // Optional tool - user must add to allowlist  api.registerTool(    {      name: "workflow_tool",      description: "Run a workflow",      parameters: Type.Object({ pipeline: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: params.pipeline }] };      },    },    { optional: true },  );}
[/code]

تتلقى مصانع الأدوات كائن سياق يوفّره وقت التشغيل. استخدم `ctx.activeModel` عندما تحتاج الأداة إلى تسجيل النموذج النشط للدورة الحالية أو عرضه أو التكيّف معه. يمكن أن يتضمن الكائن `provider` و`modelId` و `modelRef`. تعامل معه باعتباره بيانات وصفية معلوماتية لوقت التشغيل، وليس حدا أمنيا ضد المشغّل المحلي أو كود Plugin المثبت أو وقت تشغيل OpenClaw معدل. بالنسبة إلى الأدوات المحلية الحساسة، أبق اشتراكا صريحا من Plugin أو المشغّل وافشل بإغلاق آمن عندما تكون بيانات النموذج النشط الوصفية مفقودة أو غير مناسبة.

يجب أيضا التصريح عن كل أداة مسجلة باستخدام `api.registerTool(...)` في بيان Plugin:

jsonCopy code
[code]
    {  "contracts": {    "tools": ["my_tool", "workflow_tool"]  },  "toolMetadata": {    "workflow_tool": {      "optional": true    }  }}
[/code]

يلتقط OpenClaw الوصف المتحقق منه من الأداة المسجلة ويخزّنه مؤقتا، لذلك لا تكرر Plugins بيانات `description` أو المخطط في البيان. يصرح عقد البيان بالملكية والاكتشاف فقط؛ أما التنفيذ فيستدعي تنفيذ الأداة المسجلة الحية. عيّن `toolMetadata.<tool>.optional: true` للأدوات المسجلة باستخدام `api.registerTool(..., { optional: true })` كي يستطيع OpenClaw تجنب تحميل وقت تشغيل ذلك Plugin إلى أن تُدرج الأداة صراحة في قائمة السماح.

يمكّن المستخدمون الأدوات الاختيارية في الإعدادات:

json5Copy code
[code]
    {  tools: { allow: ["workflow_tool"] },}
[/code]

  * يجب ألا تتعارض أسماء الأدوات مع أدوات النواة (يتم تخطي التعارضات)
  * يتم تخطي الأدوات ذات كائنات التسجيل غير السليمة، بما في ذلك غياب `parameters`، والإبلاغ عنها في تشخيصات Plugin بدلا من كسر تشغيلات الوكيل
  * استخدم `optional: true` للأدوات ذات الآثار الجانبية أو متطلبات الملفات الثنائية الإضافية
  * يمكن للمستخدمين تمكين كل أدوات Plugin بإضافة معرّف Plugin إلى `tools.allow`


## تسجيل أوامر CLI

يمكن أن تضيف Plugins مجموعات أوامر جذرية إلى `openclaw` باستخدام `api.registerCli`. وفّر `descriptors` لكل جذر أمر من المستوى الأعلى كي يستطيع OpenClaw عرض الأمر وتوجيهه دون تحميل كل وقت تشغيل Plugin بلهفة.

typescriptCopy code
[code]
    register(api) {  api.registerCli(    ({ program }) => {      const demo = program        .command("demo-plugin")        .description("Run demo plugin commands");       demo        .command("ping")        .description("Check that the plugin CLI is executable")        .action(() => {          console.log("demo-plugin:pong");        });    },    {      descriptors: [        {          name: "demo-plugin",          description: "Run demo plugin commands",          hasSubcommands: true,        },      ],    },  );}
[/code]

بعد التثبيت، تحقق من تسجيل وقت التشغيل ونفذ الأمر:

bashCopy code
[code]
    openclaw plugins inspect demo-plugin --runtime --jsonopenclaw demo-plugin ping
[/code]

## اصطلاحات الاستيراد

استورد دائما من مسارات `openclaw/plugin-sdk/<subpath>` المركزة:

typescriptCopy code
[code]
      // Wrong: monolithic root (deprecated, will be removed) 
[/code]

للمرجع الكامل للمسارات الفرعية، راجع [نظرة عامة على SDK](</ar/plugins/sdk-overview>).

داخل Plugin الخاص بك، استخدم ملفات البرميل المحلية (`api.ts` و`runtime-api.ts`) لعمليات الاستيراد الداخلية - ولا تستورد Plugin الخاص بك أبدا عبر مساره في SDK.

بالنسبة إلى Plugins المزوّد، أبق المساعدات الخاصة بالمزوّد في براميل جذر الحزمة تلك ما لم يكن الحد الفاصل عاما بحق. الأمثلة المضمنة الحالية:

  * Anthropic: مغلفات بث Claude ومساعدات `service_tier` / beta
  * OpenAI: بُناة المزوّد، ومساعدات النموذج الافتراضي، ومزوّدو الوقت الفعلي
  * OpenRouter: باني المزوّد مع مساعدات الإعداد الأولي/التكوين


إذا كان المساعد مفيدا فقط داخل حزمة مزوّد مضمنة واحدة، فأبقه على ذلك الحد الفاصل في جذر الحزمة بدلا من ترقيته إلى `openclaw/plugin-sdk/*`.

ما زالت بعض حدود المساعدات المولدة `openclaw/plugin-sdk/<bundled-id>` موجودة لصيانة Plugins المضمنة عندما يكون لها استخدام مالك متتبع. تعامل معها كأسطح محجوزة، لا كنمط افتراضي لـ Plugins الطرف الثالث الجديدة.

## قائمة تحقق ما قبل الإرسال

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s تحتوي **package.json** على بيانات `openclaw` الوصفية الصحيحة OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s بيان **openclaw.plugin.json** موجود وصالح OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s تستخدم نقطة الدخول `defineChannelPluginEntry` أو `definePluginEntry` OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s تستخدم كل عمليات الاستيراد مسارات `plugin-sdk/<subpath>` المركزة OPENCLAW_DOCS_MARKER:calloutClose:

Was this useful?YesNo