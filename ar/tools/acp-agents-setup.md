---
title: وكلاء ACP — الإعداد
source_url: https://docs.openclaw.ai/ar/tools/acp-agents-setup
scraped_at: 2026-05-25
---

للاطلاع على النظرة العامة، ودليل تشغيل المشغّل، والمفاهيم، راجع [وكلاء ACP](</ar/tools/acp-agents>).

تغطي الأقسام أدناه إعداد acpx harness، وإعداد Plugin لجسور MCP، وإعداد الأذونات.

استخدم هذه الصفحة فقط عند إعداد مسار ACP/acpx. لإعداد تشغيل Codex app-server الأصلي، استخدم [Codex harness](</ar/plugins/codex-harness>). بالنسبة إلى مفاتيح OpenAI API أو إعداد مزوّد نماذج Codex OAuth، استخدم [OpenAI](</ar/providers/openai>).

لدى Codex مساران في OpenClaw:

المسار | الإعداد/الأمر | صفحة الإعداد  
---|---|---  
Codex app-server الأصلي | `/codex ...`, `openai/gpt-*` مراجع الوكلاء | [Codex harness](</ar/plugins/codex-harness>)  
محوّل Codex ACP الصريح | `/acp spawn codex`, `runtime: "acp", agentId: "codex"` | هذه الصفحة  
  
فضّل المسار الأصلي ما لم تكن تحتاج صراحة إلى سلوك ACP/acpx.

## دعم acpx harness (الحالي)

الأسماء المستعارة الحالية المدمجة في acpx harness:

  * `claude`
  * `codex`
  * `copilot`
  * `cursor` (Cursor CLI: `cursor-agent acp`)
  * `droid`
  * `gemini`
  * `iflow`
  * `kilocode`
  * `kimi`
  * `kiro`
  * `openclaw`
  * `opencode`
  * `pi`
  * `qwen`


عندما يستخدم OpenClaw واجهة acpx الخلفية، فضّل هذه القيم لـ `agentId` ما لم يعرّف إعداد acpx لديك أسماء مستعارة مخصصة للوكلاء. إذا كان تثبيت Cursor المحلي لديك ما يزال يعرّض ACP باسم `agent acp`، فتجاوز أمر وكيل `cursor` في إعداد acpx لديك بدلا من تغيير القيمة الافتراضية المدمجة.

يمكن لاستخدام acpx CLI المباشر أيضا استهداف محوّلات عشوائية عبر `--agent <command>`، لكن منفذ الهروب الخام هذا ميزة في acpx CLI (وليس مسار OpenClaw `agentId` العادي).

يعتمد التحكم في النماذج على قدرات المحوّل. يطبّع OpenClaw مراجع نماذج Codex ACP قبل بدء التشغيل. تحتاج أنظمة harness الأخرى إلى ACP `models` إضافة إلى دعم `session/set_model`؛ إذا لم يعرّض harness تلك القدرة من ACP ولا علم نموذج بدء التشغيل الخاص به، فلا يمكن لـ OpenClaw/acpx فرض اختيار نموذج.

## الإعداد المطلوب

أساس ACP في Core:

json5Copy code
[code]
    {  acp: {    enabled: true,    // Optional. Default is true; set false to pause ACP dispatch while keeping /acp controls.    dispatch: { enabled: true },    backend: "acpx",    defaultAgent: "codex",    allowedAgents: [      "claude",      "codex",      "copilot",      "cursor",      "droid",      "gemini",      "iflow",      "kilocode",      "kimi",      "kiro",      "openclaw",      "opencode",      "pi",      "qwen",    ],    maxConcurrentSessions: 8,    stream: {      coalesceIdleMs: 300,      maxChunkChars: 1200,    },    runtime: {      ttlMinutes: 120,    },  },}
[/code]

إعداد ربط المحادثات خاص بمحوّل القناة. مثال لـ Discord:

json5Copy code
[code]
    {  session: {    threadBindings: {      enabled: true,      idleHours: 24,      maxAgeHours: 0,    },  },  channels: {    discord: {      threadBindings: {        enabled: true,        spawnSessions: true,      },    },  },}
[/code]

إذا لم يعمل إنشاء ACP المرتبط بالمحادثة، فتحقق أولا من علم ميزة المحوّل:

  * Discord: `channels.discord.threadBindings.spawnSessions=true`


لا تتطلب روابط المحادثة الحالية إنشاء محادثة فرعية. إنها تتطلب سياق محادثة نشطا ومحوّل قناة يعرّض روابط محادثات ACP.

راجع [مرجع الإعداد](</ar/gateway/configuration-reference>).

## إعداد Plugin لواجهة acpx الخلفية

تستخدم التثبيتات المعبأة Plugin التشغيل الرسمي `@openclaw/acpx` لـ ACP. ثبّته ومكّنه قبل استخدام جلسات ACP harness:

bashCopy code
[code]
    openclaw plugins install @openclaw/acpxopenclaw config set plugins.entries.acpx.enabled true
[/code]

يمكن لمستنسخات المصدر أيضا استخدام Plugin مساحة العمل المحلية بعد `pnpm install`.

ابدأ بـ:

textCopy code
[code]
    /acp doctor
[/code]

إذا عطّلت `acpx`، أو منعته عبر `plugins.allow` / `plugins.deny`، أو أردت العودة إلى Plugin المعبأ، فاستخدم مسار الحزمة الصريح:

bashCopy code
[code]
    openclaw plugins install @openclaw/acpxopenclaw config set plugins.entries.acpx.enabled true
[/code]

تثبيت مساحة العمل المحلية أثناء التطوير:

bashCopy code
[code]
    openclaw plugins install ./path/to/local/acpx-plugin
[/code]

ثم تحقق من صحة الواجهة الخلفية:

textCopy code
[code]
    /acp doctor
[/code]

### إعداد أمر acpx وإصداره

افتراضيا، يفحص Plugin `acpx` واجهة ACP الخلفية المضمّنة أثناء بدء تشغيل Gateway وينتظر ذلك الفحص قبل إشارة `ready` الخاصة بالبوابة. اضبط `OPENCLAW_ACPX_RUNTIME_STARTUP_PROBE=0` لتجاوز فحص بدء التشغيل وتسجيل الواجهة الخلفية بشكل كسول بدلا من ذلك. شغّل `/acp doctor` لإجراء فحص صريح عند الطلب.

تجاوز الأمر أو الإصدار في إعداد Plugin:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "acpx": {        "enabled": true,        "config": {          "command": "../acpx/dist/cli.js",          "expectedVersion": "any"        }      }    }  }}
[/code]

  * يقبل `command` مسارا مطلقا، أو مسارا نسبيا (يُحل من مساحة عمل OpenClaw)، أو اسم أمر.
  * يعطّل `expectedVersion: "any"` مطابقة الإصدار الصارمة.
  * تعطّل مسارات `command` المخصصة التثبيت التلقائي المحلي داخل Plugin.


تجاوز أمر وكيل ACP فردي بوسائط منظّمة عندما ينبغي أن يبقى المسار أو قيمة العلم رمزا واحدا في argv:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "acpx": {        "enabled": true,        "config": {          "agents": {            "claude": {              "command": "node",              "args": ["/path/to/custom adapter.mjs", "--verbose"]            }          }        }      }    }  }}
[/code]

  * `agents.<id>.command` هو الملف التنفيذي أو سلسلة الأمر الموجودة لذلك وكيل ACP.
  * `agents.<id>.args` اختياري. يقتبس OpenClaw كل عنصر مصفوفة بأسلوب shell قبل تمريره عبر سجل سلسلة أوامر acpx الحالي.


راجع [Plugins](</ar/tools/plugin>).

### تثبيت الاعتماديات التلقائي

عند تثبيت OpenClaw عالميا باستخدام `npm install -g openclaw`، تُثبّت اعتماديات تشغيل acpx (الثنائيات الخاصة بالمنصة) تلقائيا عبر خطاف postinstall. إذا فشل التثبيت التلقائي، يظل Gateway يبدأ بشكل طبيعي ويبلّغ عن الاعتمادية المفقودة عبر `openclaw acp doctor`.

### جسر MCP لأدوات Plugin

افتراضيا، لا تعرّض جلسات ACPX أدوات OpenClaw المسجلة بواسطة Plugin إلى ACP harness.

إذا أردت من وكلاء ACP مثل Codex أو Claude Code استدعاء أدوات OpenClaw Plugin المثبتة مثل استدعاء/تخزين الذاكرة، فمكّن الجسر المخصص:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.pluginToolsMcpBridge true
[/code]

ما يفعله ذلك:

  * يحقن خادم MCP مدمجا باسم `openclaw-plugin-tools` في تمهيد جلسة ACPX.
  * يعرّض أدوات Plugin المسجلة مسبقا بواسطة OpenClaw plugins المثبتة والممكّنة.
  * يبقي الميزة صريحة ومعطّلة افتراضيا.


ملاحظات الأمان والثقة:

  * يوسّع هذا سطح أدوات ACP harness.
  * يحصل وكلاء ACP على الوصول فقط إلى أدوات Plugin النشطة بالفعل في Gateway.
  * تعامل مع هذا باعتباره حد الثقة نفسه للسماح لتلك plugins بالتنفيذ داخل OpenClaw نفسه.
  * راجع plugins المثبتة قبل تمكينه.


تظل `mcpServers` المخصصة تعمل كما كانت. جسر أدوات Plugin المدمج هو وسيلة راحة اختيارية إضافية، وليس بديلا لإعداد خادم MCP العام.

### جسر MCP لأدوات OpenClaw

افتراضيا، لا تعرّض جلسات ACPX أيضا أدوات OpenClaw المدمجة عبر MCP. مكّن جسر أدوات Core المنفصل عندما يحتاج وكيل ACP إلى أدوات مدمجة محددة مثل `cron`:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.openClawToolsMcpBridge true
[/code]

ما يفعله ذلك:

  * يحقن خادم MCP مدمجا باسم `openclaw-tools` في تمهيد جلسة ACPX.
  * يعرّض أدوات OpenClaw مدمجة محددة. يعرّض الخادم الأولي `cron`.
  * يبقي تعريض أدوات Core صريحا ومعطلا افتراضيا.


### إعداد مهلة التشغيل

يضبط Plugin `acpx` افتراضيا أدوار التشغيل المضمّنة على مهلة مدتها 120 ثانية. يمنح ذلك أنظمة harness الأبطأ مثل Gemini CLI وقتا كافيا لإكمال بدء ACP وتهيئته. تجاوز ذلك إذا كان المضيف لديك يحتاج إلى حد تشغيل مختلف:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.timeoutSeconds 180
[/code]

أعد تشغيل Gateway بعد تغيير هذه القيمة.

### إعداد وكيل فحص الصحة

عندما يتحقق `/acp doctor` أو فحص بدء التشغيل من الواجهة الخلفية، يفحص Plugin `acpx` المضمّن وكيل harness واحدا. إذا كان `acp.allowedAgents` مضبوطا، فإنه يستخدم افتراضيا أول وكيل مسموح؛ وإلا فإنه يستخدم `codex` افتراضيا. إذا كان نشرُك يحتاج إلى وكيل ACP مختلف لفحوص الصحة، فاضبط وكيل الفحص صراحة:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.probeAgent claude
[/code]

أعد تشغيل Gateway بعد تغيير هذه القيمة.

## إعداد الأذونات

تعمل جلسات ACP بلا تفاعل - لا يوجد TTY للموافقة على مطالبات أذونات كتابة الملفات وتنفيذ shell أو رفضها. يوفر Plugin acpx مفتاحي إعداد يتحكمان في كيفية التعامل مع الأذونات:

أذونات ACPX harness هذه منفصلة عن موافقات تنفيذ OpenClaw ومنفصلة عن أعلام تجاوز مورّد واجهة CLI الخلفية مثل Claude CLI `--permission-mode bypassPermissions`. يمثّل ACPX `approve-all` مفتاح الطوارئ على مستوى harness لجلسات ACP.

### `permissionMode`

يتحكم في العمليات التي يستطيع وكيل harness تنفيذها دون مطالبة.

القيمة | السلوك  
---|---  
`approve-all` | الموافقة تلقائيا على جميع عمليات كتابة الملفات وأوامر shell.  
`approve-reads` | الموافقة تلقائيا على القراءات فقط؛ تتطلب الكتابات والتنفيذ مطالبات.  
`deny-all` | رفض جميع مطالبات الأذونات.  
  
### `nonInteractivePermissions`

يتحكم فيما يحدث عندما كان سيظهر طلب إذن لكن لا يتوفر TTY تفاعلي (وهذا هو الحال دائما لجلسات ACP).

القيمة | السلوك  
---|---  
`fail` | إيقاف الجلسة مع `AcpRuntimeError`. **(الافتراضي)**  
`deny` | رفض الإذن بصمت والمتابعة (تدهور تدريجي).  
  
### الإعداد

اضبطه عبر إعداد Plugin:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.permissionMode approve-allopenclaw config set plugins.entries.acpx.config.nonInteractivePermissions fail
[/code]

أعد تشغيل Gateway بعد تغيير هذه القيم.

## ذو صلة

  * [وكلاء ACP](</ar/tools/acp-agents>) \- النظرة العامة، دليل تشغيل المشغّل، المفاهيم
  * [الوكلاء الفرعيون](</ar/tools/subagents>)
  * [توجيه متعدد الوكلاء](</ar/concepts/multi-agent>)


Was this useful?YesNo