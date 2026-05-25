---
title: مجموعات البث
source_url: https://docs.openclaw.ai/ar/channels/broadcast-groups
scraped_at: 2026-05-25
---

## نظرة عامة

تتيح مجموعات البث لعدة وكلاء معالجة الرسالة نفسها والرد عليها في الوقت نفسه. يتيح لك هذا إنشاء فرق وكلاء متخصصة تعمل معا داخل مجموعة WhatsApp واحدة أو رسالة مباشرة واحدة، وكل ذلك باستخدام رقم هاتف واحد.

النطاق الحالي: **WhatsApp فقط** (قناة الويب).

تُقيَّم مجموعات البث بعد قوائم السماح للقنوات وقواعد تفعيل المجموعات. في مجموعات WhatsApp، يعني ذلك أن البث يحدث عندما كان OpenClaw سيرد عادة (على سبيل المثال: عند الإشارة، حسب إعدادات مجموعتك).

## حالات الاستخدام

1\. فرق وكلاء متخصصة

انشر عدة وكلاء بمسؤوليات ذرية ومركزة:

CodeCopy code
[code]
    Group: "Development Team"Agents:  - CodeReviewer (reviews code snippets)  - DocumentationBot (generates docs)  - SecurityAuditor (checks for vulnerabilities)  - TestGenerator (suggests test cases)
[/code]

يعالج كل وكيل الرسالة نفسها ويقدم منظوره المتخصص.

2\. دعم متعدد اللغات CodeCopy code
[code]
    Group: "International Support"Agents:  - Agent_EN (responds in English)  - Agent_DE (responds in German)  - Agent_ES (responds in Spanish)
[/code]

3\. سير عمل ضمان الجودة CodeCopy code
[code]
    Group: "Customer Support"Agents:  - SupportAgent (provides answer)  - QAAgent (reviews quality, only responds if issues found)
[/code]

4\. أتمتة المهام CodeCopy code
[code]
    Group: "Project Management"Agents:  - TaskTracker (updates task database)  - TimeLogger (logs time spent)  - ReportGenerator (creates summaries)
[/code]

## الإعدادات

### الإعداد الأساسي

أضف قسما عالي المستوى باسم `broadcast` (بجوار `bindings`). المفاتيح هي معرفات أقران WhatsApp:

  * محادثات المجموعات: JID المجموعة (مثال: `120363403215116621@g.us`)
  * الرسائل المباشرة: رقم هاتف بصيغة E.164 (مثال: `+15551234567`)

jsonCopy code
[code]
    {  "broadcast": {    "120363403215116621@g.us": ["alfred", "baerbel", "assistant3"]  }}
[/code]

**النتيجة:** عندما كان OpenClaw سيرد في هذه المحادثة، سيشغّل الوكلاء الثلاثة جميعا.

### استراتيجية المعالجة

تحكم في كيفية معالجة الوكلاء للرسائل:

### parallel (الافتراضي)

يعالج جميع الوكلاء في الوقت نفسه:

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### sequential

يعالج الوكلاء بالترتيب (ينتظر كل واحد انتهاء السابق):

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### مثال كامل

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "code-reviewer",        "name": "Code Reviewer",        "workspace": "/path/to/code-reviewer",        "sandbox": { "mode": "all" }      },      {        "id": "security-auditor",        "name": "Security Auditor",        "workspace": "/path/to/security-auditor",        "sandbox": { "mode": "all" }      },      {        "id": "docs-generator",        "name": "Documentation Generator",        "workspace": "/path/to/docs-generator",        "sandbox": { "mode": "all" }      }    ]  },  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["code-reviewer", "security-auditor", "docs-generator"],    "120363424282127706@g.us": ["support-en", "support-de"],    "+15555550123": ["assistant", "logger"]  }}
[/code]

## كيف يعمل

### تدفق الرسائل

* ### وصول رسالة واردة

تصل رسالة مجموعة WhatsApp أو رسالة مباشرة.

* ### فحص البث

يتحقق النظام مما إذا كان معرف القرين موجودا في `broadcast`.

* ### إذا كان ضمن قائمة البث

  * يعالج جميع الوكلاء المدرجين الرسالة.
  * يمتلك كل وكيل مفتاح جلسة خاصا به وسياقا معزولا.
  * يعالج الوكلاء بالتوازي (الافتراضي) أو بالتتابع.


* ### إذا لم يكن ضمن قائمة البث

ينطبق التوجيه العادي (أول ربط مطابق).

### عزل الجلسات

يحافظ كل وكيل في مجموعة بث على ما يلي بشكل منفصل تماما:

  * **مفاتيح الجلسات** (`agent:alfred:whatsapp:group:120363...` مقابل `agent:baerbel:whatsapp:group:120363...`)
  * **سجل المحادثة** (لا يرى الوكيل رسائل الوكلاء الآخرين)
  * **مساحة العمل** (صناديق عزل منفصلة إذا تم إعدادها)
  * **الوصول إلى الأدوات** (قوائم سماح/منع مختلفة)
  * **الذاكرة/السياق** (ملفات [IDENTITY.md](<http://IDENTITY.md>) [وSOUL.md](<http://xn--SOUL-pbg.md>) منفصلة، إلخ)
  * **مخزن سياق المجموعة** (رسائل المجموعة الحديثة المستخدمة للسياق) مشترك لكل قرين، لذلك يرى جميع وكلاء البث السياق نفسه عند تشغيلهم


يتيح هذا لكل وكيل امتلاك:

  * شخصيات مختلفة
  * وصول مختلف إلى الأدوات (مثلا، قراءة فقط مقابل قراءة وكتابة)
  * نماذج مختلفة (مثلا، opus مقابل sonnet)
  * Skills مختلفة مثبتة


### مثال: جلسات معزولة

في المجموعة `120363403215116621@g.us` مع الوكلاء `["alfred", "baerbel"]`:

### سياق Alfred

CodeCopy code
[code]
    Session: agent:alfred:whatsapp:group:120363403215116621@g.usHistory: [user message, alfred's previous responses]Workspace: /Users/user/openclaw-alfred/Tools: read, write, exec
[/code]

### سياق Bärbel

CodeCopy code
[code]
    Session: agent:baerbel:whatsapp:group:120363403215116621@g.usHistory: [user message, baerbel's previous responses]Workspace: /Users/user/openclaw-baerbel/Tools: read only
[/code]

## أفضل الممارسات

1\. أبق الوكلاء مركزين

صمم كل وكيل بمسؤولية واحدة واضحة:

jsonCopy code
[code]
    {  "broadcast": {    "DEV_GROUP": ["formatter", "linter", "tester"]  }}
[/code]

✅ **جيد:** لكل وكيل مهمة واحدة. ❌ **سيئ:** وكيل عام واحد باسم "dev-helper".

2\. استخدم أسماء وصفية

اجعل وظيفة كل وكيل واضحة:

jsonCopy code
[code]
    {  "agents": {    "security-scanner": { "name": "Security Scanner" },    "code-formatter": { "name": "Code Formatter" },    "test-generator": { "name": "Test Generator" }  }}
[/code]

3\. اضبط وصولا مختلفا للأدوات

امنح الوكلاء الأدوات التي يحتاجونها فقط:

jsonCopy code
[code]
    {  "agents": {    "reviewer": {      "tools": { "allow": ["read", "exec"] }    },    "fixer": {      "tools": { "allow": ["read", "write", "edit", "exec"] }    }  }}
[/code]

`reviewer` للقراءة فقط. يستطيع `fixer` القراءة والكتابة.

4\. راقب الأداء

عند وجود عدد كبير من الوكلاء، ضع في اعتبارك:

  * استخدام `"strategy": "parallel"` (الافتراضي) للسرعة
  * حصر مجموعات البث في 5-10 وكلاء
  * استخدام نماذج أسرع للوكلاء الأبسط

5\. تعامل مع الإخفاقات بسلاسة

يفشل الوكلاء بشكل مستقل. خطأ وكيل واحد لا يحظر الآخرين:

CodeCopy code
[code]
    Message → [Agent A ✓, Agent B ✗ error, Agent C ✓]Result: Agent A and C respond, Agent B logs error
[/code]

## التوافق

### المزودون

تعمل مجموعات البث حاليا مع:

  * ✅ WhatsApp (منفذ)
  * 🚧 Telegram (مخطط له)
  * 🚧 Discord (مخطط له)
  * 🚧 Slack (مخطط له)


### التوجيه

تعمل مجموعات البث إلى جانب التوجيه الحالي:

jsonCopy code
[code]
    {  "bindings": [    {      "match": { "channel": "whatsapp", "peer": { "kind": "group", "id": "GROUP_A" } },      "agentId": "alfred"    }  ],  "broadcast": {    "GROUP_B": ["agent1", "agent2"]  }}
[/code]

  * `GROUP_A`: يرد alfred فقط (توجيه عادي).
  * `GROUP_B`: يرد agent1 وagent2 (بث).


## استكشاف الأخطاء وإصلاحها

الوكلاء لا يردون

**تحقق من:**

  1. معرفات الوكلاء موجودة في `agents.list`.
  2. تنسيق معرف القرين صحيح (مثلا، `120363403215116621@g.us`).
  3. الوكلاء غير موجودين في قوائم المنع.


**تصحيح الأخطاء:**

bashCopy code
[code]
    tail -f ~/.openclaw/logs/gateway.log | grep broadcast
[/code]

وكيل واحد فقط يرد

**السبب:** قد يكون معرف القرين موجودا في `bindings` لكن ليس في `broadcast`.

**الإصلاح:** أضفه إلى إعدادات البث أو أزله من الربط.

مشكلات الأداء

إذا كان بطيئا مع عدد كبير من الوكلاء:

  * قلل عدد الوكلاء لكل مجموعة.
  * استخدم نماذج أخف (sonnet بدلا من opus).
  * تحقق من وقت بدء صندوق العزل.


## أمثلة

مثال 1: فريق مراجعة الكود jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": [      "code-formatter",      "security-scanner",      "test-coverage",      "docs-checker"    ]  },  "agents": {    "list": [      {        "id": "code-formatter",        "workspace": "~/agents/formatter",        "tools": { "allow": ["read", "write"] }      },      {        "id": "security-scanner",        "workspace": "~/agents/security",        "tools": { "allow": ["read", "exec"] }      },      {        "id": "test-coverage",        "workspace": "~/agents/testing",        "tools": { "allow": ["read", "exec"] }      },      { "id": "docs-checker", "workspace": "~/agents/docs", "tools": { "allow": ["read"] } }    ]  }}
[/code]

**يرسل المستخدم:** مقتطف كود.

**الردود:**

  * code-formatter: "تم إصلاح المسافات البادئة وإضافة تلميحات النوع"
  * security-scanner: "⚠️ ثغرة حقن SQL في السطر 12"
  * test-coverage: "التغطية 45%، وتوجد اختبارات مفقودة لحالات الخطأ"
  * docs-checker: "سلسلة توثيق مفقودة للدالة `process_data`"

مثال 2: دعم متعدد اللغات jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "+15555550123": ["detect-language", "translator-en", "translator-de"]  },  "agents": {    "list": [      { "id": "detect-language", "workspace": "~/agents/lang-detect" },      { "id": "translator-en", "workspace": "~/agents/translate-en" },      { "id": "translator-de", "workspace": "~/agents/translate-de" }    ]  }}
[/code]

## مرجع API

### مخطط الإعدادات

typescriptCopy code
[code]
    interface OpenClawConfig {  broadcast?: {    strategy?: "parallel" | "sequential";    [peerId: string]: string[];  };}
[/code]

### الحقول

كيفية معالجة الوكلاء. يشغّل `parallel` جميع الوكلاء في الوقت نفسه؛ ويشغلهم `sequential` بترتيب المصفوفة.

JID مجموعة WhatsApp، أو رقم E.164، أو معرف قرين آخر. القيمة هي مصفوفة معرفات الوكلاء التي يجب أن تعالج الرسائل.

## القيود

  1. **الحد الأقصى للوكلاء:** لا يوجد حد صارم، لكن 10+ وكلاء قد يكونون بطيئين.
  2. **السياق المشترك:** لا يرى الوكلاء ردود بعضهم البعض (حسب التصميم).
  3. **ترتيب الرسائل:** قد تصل الردود المتوازية بأي ترتيب.
  4. **حدود المعدل:** يحتسب جميع الوكلاء ضمن حدود معدل WhatsApp.


## التحسينات المستقبلية

الميزات المخطط لها:

  * [ ] وضع السياق المشترك (يرى الوكلاء ردود بعضهم البعض)
  * [ ] تنسيق الوكلاء (يمكن للوكلاء إرسال إشارات لبعضهم البعض)
  * [ ] اختيار الوكلاء ديناميكيا (اختيار الوكلاء بناء على محتوى الرسالة)
  * [ ] أولويات الوكلاء (يرد بعض الوكلاء قبل الآخرين)


## ذات صلة

  * [توجيه القنوات](</ar/channels/channel-routing>)
  * [المجموعات](</ar/channels/groups>)
  * [أدوات وضع الحماية متعددة الوكلاء](</ar/tools/multi-agent-sandbox-tools>)
  * [الإقران](</ar/channels/pairing>)
  * [إدارة الجلسات](</ar/concepts/session>)


Was this useful?YesNo