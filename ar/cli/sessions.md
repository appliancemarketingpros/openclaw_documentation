---
title: الجلسات
source_url: https://docs.openclaw.ai/ar/cli/sessions
scraped_at: 2026-05-25
---

# `openclaw sessions`

اعرض جلسات المحادثة المخزنة.

قوائم الجلسات ليست فحوصات حيوية للقنوات/المزوّدين. إنها تعرض صفوف محادثات محفوظة من مخازن الجلسات. يمكن لقناة Discord أو Slack أو Telegram أو أي قناة أخرى هادئة أن تعيد الاتصال بنجاح دون إنشاء صف جلسة جديد حتى تتم معالجة رسالة. استخدم `openclaw channels status --probe` أو `openclaw status --deep` أو `openclaw health --verbose` عندما تحتاج إلى اتصال حي بالقناة.

استجابات `openclaw sessions` و Gateway `sessions.list` تكون محدودة افتراضياً حتى لا تتمكن المخازن الكبيرة طويلة العمر من احتكار عملية CLI أو حلقة أحداث Gateway. يعيد CLI أحدث 100 جلسة افتراضياً؛ مرّر `--limit <n>` لنافذة أصغر/أكبر أو `--limit all` عندما تحتاج عمداً إلى المخزن الكامل. تتضمن استجابات JSON الحقول `totalCount` و`limitApplied` و`hasMore` عندما يحتاج المستدعون إلى إظهار وجود صفوف إضافية.

يمكن لعملاء RPC تمرير `configuredAgentsOnly: true` للاحتفاظ بمصدر الاكتشاف المدمج الواسع مع إرجاع الصفوف الخاصة بالوكلاء الموجودين حالياً في التهيئة فقط. تستخدم واجهة التحكم هذا الوضع افتراضياً حتى لا تعود مخازن الوكلاء المحذوفة أو الموجودة على القرص فقط للظهور في عرض الجلسات.

bashCopy code
[code]
    openclaw sessionsopenclaw sessions --agent workopenclaw sessions --all-agentsopenclaw sessions --active 120openclaw sessions --limit 25openclaw sessions --verboseopenclaw sessions --json
[/code]

اختيار النطاق:

  * الافتراضي: مخزن الوكيل الافتراضي المهيأ
  * `--verbose`: تسجيل مفصل
  * `--agent <id>`: مخزن وكيل مهيأ واحد
  * `--all-agents`: تجميع كل مخازن الوكلاء المهيأة
  * `--store <path>`: مسار مخزن صريح (لا يمكن دمجه مع `--agent` أو `--all-agents`)
  * `--limit <n|all>`: الحد الأقصى للصفوف المطلوب إخراجها (الافتراضي `100`؛ يعيد `all` الإخراج الكامل)


صدّر حزمة مسار لجلسة مخزنة:

bashCopy code
[code]
    openclaw sessions export-trajectory --session-key "agent:main:telegram:direct:123" --workspace .openclaw sessions export-trajectory --session-key "agent:main:telegram:direct:123" --output bug-123 --json
[/code]

هذا هو مسار الأمر الذي يستخدمه أمر الشرطة المائلة `/export-trajectory` بعد موافقة المالك على طلب التنفيذ. يتم دائماً حل دليل الإخراج داخل `.openclaw/trajectory-exports/` ضمن مساحة العمل المحددة.

يقرأ `openclaw sessions --all-agents` مخازن الوكلاء المهيأة. اكتشاف جلسات Gateway و ACP أوسع نطاقاً: فهو يتضمن أيضاً المخازن الموجودة على القرص فقط ضمن جذر `agents/` الافتراضي أو جذر `session.store` ذي القوالب. يجب أن تُحل تلك المخازن المكتشفة إلى ملفات `sessions.json` عادية داخل جذر الوكيل؛ يتم تخطي الروابط الرمزية والمسارات الخارجة عن الجذر.

أمثلة JSON:

`openclaw sessions --all-agents --json`:

jsonCopy code
[code]
    {  "path": null,  "stores": [    { "agentId": "main", "path": "/home/user/.openclaw/agents/main/sessions/sessions.json" },    { "agentId": "work", "path": "/home/user/.openclaw/agents/work/sessions/sessions.json" }  ],  "allAgents": true,  "count": 2,  "totalCount": 2,  "limitApplied": 100,  "hasMore": false,  "activeMinutes": null,  "sessions": [    { "agentId": "main", "key": "agent:main:main", "model": "gpt-5" },    { "agentId": "work", "key": "agent:work:main", "model": "claude-opus-4-6" }  ]}
[/code]

## صيانة التنظيف

شغّل الصيانة الآن (بدلاً من انتظار دورة الكتابة التالية):

bashCopy code
[code]
    openclaw sessions cleanup --dry-runopenclaw sessions cleanup --agent work --dry-runopenclaw sessions cleanup --all-agents --dry-runopenclaw sessions cleanup --enforceopenclaw sessions cleanup --enforce --active-key "agent:main:telegram:direct:123"openclaw sessions cleanup --dry-run --fix-dm-scopeopenclaw sessions cleanup --json
[/code]

يستخدم `openclaw sessions cleanup` إعدادات `session.maintenance` من التهيئة:

  * ملاحظة النطاق: يصون `openclaw sessions cleanup` مخازن الجلسات والنصوص الجانبية وملفات المسارات الجانبية. لا يقلّم سجلات تشغيل Cron (`cron/runs/<jobId>.jsonl`)، التي يديرها `cron.runLog.maxBytes` و`cron.runLog.keepLines` في [تهيئة Cron](</ar/automation/cron-jobs#configuration>) والموضحة في [صيانة Cron](</ar/automation/cron-jobs#maintenance>).

  * يزيل التنظيف أيضاً النصوص الجانبية الأساسية غير المرجعية ونقاط تحقق Compaction وملفات المسارات الجانبية الأقدم من `session.maintenance.pruneAfter`؛ تُحفظ الملفات التي لا تزال مشاراً إليها في `sessions.json`.

  * `--dry-run`: معاينة عدد الإدخالات التي ستُقلّم/تُحد دون كتابة.

    * في وضع النص، تطبع التجربة الجافة جدول إجراءات لكل جلسة (`Action`, `Key`, `Age`, `Model`, `Flags`) حتى تتمكن من رؤية ما سيُحتفظ به مقابل ما سيُزال.
  * `--enforce`: تطبيق الصيانة حتى عندما يكون `session.maintenance.mode` هو `warn`.

  * `--fix-missing`: إزالة الإدخالات التي تكون ملفات نصوصها الجانبية مفقودة، حتى لو لم تكن لتخرج عادةً بسبب العمر/العدد بعد.

  * `--fix-dm-scope`: عندما يكون `session.dmScope` هو `main`، تخلص من صفوف الرسائل المباشرة القديمة ذات مفاتيح النظراء التي خلّفتها طرق توجيه `per-peer` أو `per-channel-peer` أو `per-account-channel-peer` السابقة. استخدم `--dry-run` أولاً؛ يؤدي تطبيق التنظيف إلى إزالة تلك الصفوف من `sessions.json` ويحفظ نصوصها الجانبية كأرشيفات محذوفة.

  * `--active-key <key>`: حماية مفتاح نشط محدد من الإخلاء بسبب ميزانية القرص. تُحتفظ أيضاً بمؤشرات المحادثات الخارجية الدائمة، مثل جلسات المجموعات وجلسات الدردشة ذات نطاق السلاسل، عبر صيانة العمر/العدد/ميزانية القرص.

  * `--agent <id>`: تشغيل التنظيف لمخزن وكيل مهيأ واحد.

  * `--all-agents`: تشغيل التنظيف لكل مخازن الوكلاء المهيأة.

  * `--store <path>`: التشغيل مقابل ملف `sessions.json` محدد.

  * `--json`: طباعة ملخص JSON. مع `--all-agents`، يتضمن الإخراج ملخصاً واحداً لكل مخزن.


عندما يكون Gateway قابلاً للوصول، يتم إرسال التنظيف غير التجريبي لمخازن الوكلاء المهيأة عبر Gateway حتى يشارك كاتب مخزن الجلسات نفسه المستخدم لحركة مرور وقت التشغيل. استخدم `--store <path>` للإصلاح الصريح دون اتصال لملف مخزن.

`openclaw sessions cleanup --all-agents --dry-run --json`:

jsonCopy code
[code]
    {  "allAgents": true,  "mode": "warn",  "dryRun": true,  "stores": [    {      "agentId": "main",      "storePath": "/home/user/.openclaw/agents/main/sessions/sessions.json",      "beforeCount": 120,      "afterCount": 80,      "missing": 0,      "dmScopeRetired": 0,      "pruned": 40,      "capped": 0    },    {      "agentId": "work",      "storePath": "/home/user/.openclaw/agents/work/sessions/sessions.json",      "beforeCount": 18,      "afterCount": 18,      "missing": 0,      "dmScopeRetired": 0,      "pruned": 0,      "capped": 0    }  ]}
[/code]

ذات صلة:

  * تهيئة الجلسة: [مرجع التهيئة](</ar/gateway/config-agents#session>)


## ذات صلة

  * [مرجع CLI](</ar/cli>)
  * [إدارة الجلسات](</ar/concepts/session>)


Was this useful?YesNo