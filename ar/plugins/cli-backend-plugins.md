---
title: بناء Plugins الواجهة الخلفية للـ CLI
source_url: https://docs.openclaw.ai/ar/plugins/cli-backend-plugins
scraped_at: 2026-05-25
---

تتيح Plugins الخلفية الخاصة بـ CLI لـ OpenClaw استدعاء CLI محلي للذكاء الاصطناعي بوصفه خلفية استدلال نصي backend. تظهر الخلفية كبادئة موفر في مراجع النماذج:

textCopy code
[code]
    acme-cli/acme-large
[/code]

استخدم خلفية CLI عندما يكون التكامل العلوي مكشوفًا بالفعل كأمر محلي، أو عندما يمتلك CLI حالة تسجيل الدخول المحلية، أو عندما يكون CLI بديلًا مفيدًا إذا كانت موفرو API غير متاحة.

## ما الذي يمتلكه Plugin

لدى Plugin خلفية CLI ثلاثة عقود:

العقد | الملف | الغرض  
---|---|---  
مدخل الحزمة | `package.json` | يوجّه OpenClaw إلى وحدة وقت تشغيل Plugin  
ملكية البيان | `openclaw.plugin.json` | يعلن معرّف الخلفية قبل تحميل وقت التشغيل  
تسجيل وقت التشغيل | `index.ts` | يستدعي `api.registerCliBackend(...)` مع افتراضيات الأمر  
  
البيان هو بيانات وصفية للاكتشاف. لا ينفّذ CLI ولا يسجّل سلوك وقت التشغيل. يبدأ سلوك وقت التشغيل عندما يستدعي مدخل Plugin `api.registerCliBackend(...)`.

## Plugin خلفية بالحد الأدنى

* ### Create package metadata

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-acme-cli",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./index.ts"],    "compat": {      "pluginApi": ">=2026.3.24-beta.2",      "minGatewayVersion": "2026.3.24-beta.2"    },    "build": {      "openclawVersion": "2026.3.24-beta.2",      "pluginSdkVersion": "2026.3.24-beta.2"    }  },  "dependencies": {    "openclaw": "^2026.3.24"  },  "devDependencies": {    "typescript": "^5.9.0"  }}
[/code]

يجب أن تشحن الحزم المنشورة ملفات وقت تشغيل JavaScript مبنية. إذا كان مدخل المصدر لديك هو `./src/index.ts`، فأضف `openclaw.runtimeExtensions` يشير إلى نظير JavaScript المبني. راجع [نقاط الدخول](</ar/plugins/sdk-entrypoints>).

* ### Declare backend ownership

openclaw.plugin.jsonCopy code
[code]
    {  "id": "acme-cli",  "name": "Acme CLI",  "description": "Run Acme's local AI CLI through OpenClaw",  "cliBackends": ["acme-cli"],  "setup": {    "cliBackends": ["acme-cli"],    "requiresRuntime": false  },  "activation": {    "onStartup": false  },  "configSchema": {    "type": "object",    "additionalProperties": false  }}
[/code]

`cliBackends` هي قائمة ملكية وقت التشغيل. تتيح لـ OpenClaw التحميل التلقائي لـ Plugin عندما يذكر الإعداد أو اختيار النموذج `acme-cli/...`.

`setup.cliBackends` هي سطح الإعداد القائم على الواصفات أولًا. أضفها عندما ينبغي لاكتشاف النماذج أو التهيئة الأولية أو الحالة التعرف على الخلفية دون تحميل وقت تشغيل Plugin. استخدم `requiresRuntime: false` فقط عندما تكون تلك الواصفات الثابتة كافية للإعداد.

* ### Register the backend

index.tsCopy code
[code]
    import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";import {  CLI_FRESH_WATCHDOG_DEFAULTS,  CLI_RESUME_WATCHDOG_DEFAULTS,  type CliBackendPlugin,} from "openclaw/plugin-sdk/cli-backend"; function buildAcmeCliBackend(): CliBackendPlugin {  return {    id: "acme-cli",    liveTest: {      defaultModelRef: "acme-cli/acme-large",      defaultImageProbe: false,      defaultMcpProbe: false,      docker: {        npmPackage: "@acme/acme-cli",        binaryName: "acme",      },    },    config: {      command: "acme",      args: ["chat", "--json"],      output: "json",      input: "stdin",      modelArg: "--model",      sessionArg: "--session",      sessionMode: "existing",      sessionIdFields: ["session_id", "conversation_id"],      systemPromptFileArg: "--system-file",      systemPromptWhen: "first",      imageArg: "--image",      imageMode: "repeat",      reliability: {        watchdog: {          fresh: { ...CLI_FRESH_WATCHDOG_DEFAULTS },          resume: { ...CLI_RESUME_WATCHDOG_DEFAULTS },        },      },      serialize: true,    },  };} export default definePluginEntry({  id: "acme-cli",  name: "Acme CLI",  description: "Run Acme's local AI CLI through OpenClaw",  register(api) {    api.registerCliBackend(buildAcmeCliBackend());  },});
[/code]

يجب أن يطابق معرّف الخلفية إدخال `cliBackends` في البيان. `config` المسجّل هو الافتراضي فقط؛ يتم دمج إعداد المستخدم ضمن `agents.defaults.cliBackends.acme-cli` فوقه في وقت التشغيل.

## شكل الإعداد

يصف `CliBackendConfig` كيف ينبغي لـ OpenClaw تشغيل CLI وتحليل مخرجاته:

الحقل | الاستخدام  
---|---  
`command` | اسم الثنائي أو مسار أمر مطلق  
`args` | argv الأساسي للتشغيلات الجديدة  
`resumeArgs` | argv بديل للجلسات المستأنفة؛ يدعم `{sessionId}`  
`output` / `resumeOutput` | المحلّل: `json` أو `jsonl` أو `text`  
`input` | نقل الموجه: `arg` أو `stdin`  
`modelArg` | العلم المستخدم قبل معرّف النموذج  
`modelAliases` | ربط معرّفات نماذج OpenClaw بمعرّفات CLI الأصلية  
`sessionArg` / `sessionArgs` | كيفية تمرير معرّف جلسة  
`sessionMode` | `always` أو `existing` أو `none`  
`sessionIdFields` | حقول JSON التي يقرؤها OpenClaw من مخرجات CLI  
`systemPromptArg` / `systemPromptFileArg` | نقل موجه النظام  
`systemPromptWhen` | `first` أو `always` أو `never`  
`imageArg` / `imageMode` | دعم مسار الصورة  
`serialize` | إبقاء تشغيلات الخلفية نفسها مرتبة  
`reliability.watchdog` | ضبط مهلة عدم وجود مخرجات  
  
فضّل أصغر إعداد ثابت يطابق CLI. أضف استدعاءات راجعة لـ Plugin فقط للسلوك الذي ينتمي فعلًا إلى الخلفية.

## خطافات الخلفية المتقدمة

يمكن لـ `CliBackendPlugin` أيضًا تعريف:

الخطاف | الاستخدام  
---|---  
`normalizeConfig(config, context)` | إعادة كتابة إعداد المستخدم القديم بعد الدمج  
`resolveExecutionArgs(ctx)` | إضافة أعلام خاصة بالطلب مثل جهد التفكير  
`prepareExecution(ctx)` | إنشاء جسور مصادقة أو إعداد مؤقتة قبل التشغيل  
`transformSystemPrompt(ctx)` | تطبيق تحويل نهائي خاص بـ CLI لموجه النظام  
`textTransforms` | استبدالات ثنائية الاتجاه للموجه/المخرجات  
`defaultAuthProfileId` | تفضيل ملف مصادقة OpenClaw محدد  
`authEpochMode` | تحديد كيف تبطل تغييرات المصادقة جلسات CLI المخزنة  
`nativeToolMode` | إعلان ما إذا كان لدى CLI أدوات أصلية دائمة التشغيل  
`bundleMcp` / `bundleMcpMode` | الاشتراك في جسر أدوات MCP عبر local loopback الخاص بـ OpenClaw  
  
أبق هذه الخطافات مملوكة للموفر. لا تضف فروعًا خاصة بـ CLI إلى النواة عندما يمكن لخطاف خلفية التعبير عن السلوك.

## جسر أدوات MCP

لا تتلقى خلفيات CLI أدوات OpenClaw افتراضيًا. إذا كان CLI يستطيع استهلاك إعداد MCP، فاشترك صراحة:

typescriptCopy code
[code]
    return {  id: "acme-cli",  bundleMcp: true,  bundleMcpMode: "codex-config-overrides",  config: {    command: "acme",    args: ["chat", "--json"],    output: "json",  },};
[/code]

أوضاع الجسر المدعومة هي:

الوضع | الاستخدام  
---|---  
`claude-config-file` | CLIs التي تقبل ملف إعداد MCP  
`codex-config-overrides` | CLIs التي تقبل تجاوزات الإعداد عبر argv  
`gemini-system-settings` | CLIs التي تقرأ إعدادات MCP من دليل إعدادات النظام الخاص بها  
  
فعّل الجسر فقط عندما يستطيع CLI استهلاكه فعليًا. إذا كان لدى CLI طبقة أدوات مدمجة خاصة به لا يمكن تعطيلها، فعيّن `nativeToolMode: "always-on"` لكي يتمكن OpenClaw من الفشل مغلقًا عندما يتطلب المستدعي عدم وجود أدوات أصلية.

## إعداد المستخدم

يمكن للمستخدمين تجاوز أي افتراضي للخلفية:

json5Copy code
[code]
    {  agents: {    defaults: {      cliBackends: {        "acme-cli": {          command: "/opt/acme/bin/acme",          args: ["chat", "--json", "--profile", "work"],          modelAliases: {            large: "acme-large-2026",          },        },      },      model: {        primary: "openai/gpt-5.5",        fallbacks: ["acme-cli/large"],      },    },  },}
[/code]

وثّق الحد الأدنى من التجاوزات التي سيحتاجها المستخدمون غالبًا. عادةً يكون ذلك `command` فقط عندما يكون الثنائي خارج `PATH`.

## التحقق

بالنسبة إلى Plugins المضمّنة، أضف اختبارًا مركزًا حول الباني وتسجيل الإعداد، ثم شغّل مسار الاختبار المستهدف الخاص بـ Plugin:

bashCopy code
[code]
    pnpm test extensions/acme-cli
[/code]

بالنسبة إلى Plugins المحلية أو المثبتة، تحقق من الاكتشاف ومن تشغيل نموذج حقيقي واحد:

bashCopy code
[code]
    openclaw plugins inspect acme-cli --runtime --jsonopenclaw agent --message "reply exactly: backend ok" --model acme-cli/acme-large
[/code]

إذا كانت الخلفية تدعم الصور أو MCP، فأضف اختبار دخان حيًا يثبت تلك المسارات مع CLI الحقيقي. لا تعتمد على الفحص الثابت لسلوك الموجه أو الصورة أو MCP أو استئناف الجلسة.

## قائمة التحقق

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s يحتوي `package.json` على `openclaw.extensions` ومدخلات وقت تشغيل مبنية للحزم المنشورة OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s يعلن `openclaw.plugin.json` عن `cliBackends` و`activation.onStartup` المقصود OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s يكون `setup.cliBackends` موجودًا عندما ينبغي للإعداد/اكتشاف النماذج رؤية الخلفية باردة OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s يستخدم `api.registerCliBackend(...)` معرّف الخلفية نفسه الموجود في البيان OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s لا تزال تجاوزات المستخدم ضمن `agents.defaults.cliBackends.<id>` هي التي تسود OPENCLAW_DOCS_MARKER:calloutClose:

Was this useful?YesNo