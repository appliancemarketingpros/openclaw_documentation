---
title: الخطافات
source_url: https://docs.openclaw.ai/ar/automation/hooks
scraped_at: 2026-05-25
---

Hooks هي سكربتات صغيرة تعمل عند حدوث شيء داخل Gateway. يمكن اكتشافها من الأدلة وفحصها باستخدام `openclaw hooks`. لا يحمّل Gateway الخطافات الداخلية إلا بعد تمكين الخطافات أو تكوين إدخال خطاف واحد على الأقل، أو حزمة خطافات، أو معالج قديم، أو دليل خطافات إضافي.

يوجد نوعان من الخطافات في OpenClaw:

  * **الخطافات الداخلية** (هذه الصفحة): تعمل داخل Gateway عند إطلاق أحداث الوكيل، مثل `/new` أو `/reset` أو `/stop` أو أحداث دورة الحياة.
  * **Webhooks** : نقاط نهاية HTTP خارجية تتيح للأنظمة الأخرى تشغيل العمل في OpenClaw. راجع [Webhooks](</ar/automation/cron-jobs#webhooks>).


يمكن أيضًا تضمين الخطافات داخل plugins. يعرض `openclaw hooks list` كلًا من الخطافات المستقلة والخطافات التي تديرها plugins.

## البدء السريع

bashCopy code
[code]
    # List available hooksopenclaw hooks list # Enable a hookopenclaw hooks enable session-memory # Check hook statusopenclaw hooks check # Get detailed informationopenclaw hooks info session-memory
[/code]

## أنواع الأحداث

الحدث | وقت إطلاقه  
---|---  
`command:new` | عند إصدار الأمر `/new`  
`command:reset` | عند إصدار الأمر `/reset`  
`command:stop` | عند إصدار الأمر `/stop`  
`command` | أي حدث أمر (مستمع عام)  
`session:compact:before` | قبل أن تلخص Compaction السجل  
`session:compact:after` | بعد اكتمال Compaction  
`session:patch` | عند تعديل خصائص الجلسة  
`agent:bootstrap` | قبل حقن ملفات تمهيد مساحة العمل  
`gateway:startup` | بعد بدء القنوات وتحميل الخطافات  
`gateway:shutdown` | عند بدء إيقاف Gateway  
`gateway:pre-restart` | قبل إعادة تشغيل متوقعة لـ Gateway  
`message:received` | رسالة واردة من أي قناة  
`message:transcribed` | بعد اكتمال تفريغ الصوت  
`message:preprocessed` | بعد اكتمال المعالجة المسبقة للوسائط والروابط أو تخطيها  
`message:sent` | تسليم رسالة صادرة  
  
## كتابة الخطافات

### بنية الخطاف

كل خطاف هو دليل يحتوي على ملفين:

CodeCopy code
[code]
    my-hook/├── HOOK.md          # Metadata + documentation└── handler.ts       # Handler implementation
[/code]

### تنسيق [HOOK.md](<http://HOOK.md>)

markdownCopy code
[code]
    ---name: my-hookdescription: "Short description of what this hook does"metadata:  { "openclaw": { "emoji": "🔗", "events": ["command:new"], "requires": { "bins": ["node"] } } }--- # My Hook Detailed documentation goes here.
[/code]

**حقول البيانات الوصفية** (`metadata.openclaw`):

الحقل | الوصف  
---|---  
`emoji` | رمز تعبيري للعرض في CLI  
`events` | مصفوفة من الأحداث التي يجب الاستماع إليها  
`export` | التصدير المسمى المراد استخدامه (الافتراضي هو `"default"`)  
`os` | المنصات المطلوبة (مثل `["darwin", "linux"]`)  
`requires` | مسارات `bins` أو `anyBins` أو `env` أو `config` المطلوبة  
`always` | تجاوز فحوصات الأهلية (قيمة منطقية)  
`install` | طرق التثبيت  
  
### تنفيذ المعالج

typescriptCopy code
[code]
    const handler = async (event) => {  if (event.type !== "command" || event.action !== "new") {    return;  }   console.log(`[my-hook] New command triggered`);  // Your logic here   // Optionally send message to user  event.messages.push("Hook executed!");}; export default handler;
[/code]

يتضمن كل حدث: `type` و`action` و`sessionKey` و`timestamp` و`messages` (أضف إليها للإرسال إلى المستخدم) و`context` (بيانات خاصة بالحدث). يمكن أن تتضمن سياقات خطافات Plugins الخاصة بالوكلاء والأدوات أيضًا `trace`، وهو سياق تتبع تشخيصي متوافق مع W3C للقراءة فقط يمكن لـ plugins تمريره إلى السجلات المنظمة لربط OTEL.

### أبرز سياقات الأحداث

**أحداث الأوامر** (`command:new`، `command:reset`): `context.sessionEntry` و`context.previousSessionEntry` و`context.commandSource` و`context.workspaceDir` و`context.cfg`.

**أحداث الرسائل** (`message:received`): `context.from` و`context.content` و`context.channelId` و`context.metadata` (بيانات خاصة بالمزود تتضمن `senderId` و`senderName` و`guildId`). يفضل `context.content` نص أمر غير فارغ للرسائل الشبيهة بالأوامر، ثم يعود إلى النص الوارد الخام والنص العام؛ ولا يتضمن إثراءً مخصصًا للوكيل فقط مثل سجل سلسلة النقاش أو ملخصات الروابط.

**أحداث الرسائل** (`message:sent`): `context.to` و`context.content` و`context.success` و`context.channelId`.

**أحداث الرسائل** (`message:transcribed`): `context.transcript` و`context.from` و`context.channelId` و`context.mediaPath`.

**أحداث الرسائل** (`message:preprocessed`): `context.bodyForAgent` (النص النهائي المُثرى) و`context.from` و`context.channelId`.

**أحداث التمهيد** (`agent:bootstrap`): `context.bootstrapFiles` (مصفوفة قابلة للتعديل) و`context.agentId`.

**أحداث تصحيح الجلسة** (`session:patch`): `context.sessionEntry` و`context.patch` (الحقول المتغيرة فقط) و`context.cfg`. لا يمكن إلا للعملاء ذوي الامتياز تشغيل أحداث التصحيح.

**أحداث Compaction** : يتضمن `session:compact:before` كلًا من `messageCount` و`tokenCount`. يضيف `session:compact:after` كلًا من `compactedCount` و`summaryLength` و`tokensBefore` و`tokensAfter`.

يراقب `command:stop` إصدار المستخدم للأمر `/stop`؛ فهو جزء من دورة حياة الإلغاء/الأمر، وليس بوابة لإنهاء الوكيل. يجب على Plugins التي تحتاج إلى فحص إجابة نهائية طبيعية وطلب مرور إضافي واحد من الوكيل استخدام خطاف Plugin المكتوب `before_agent_finalize` بدلًا من ذلك. راجع [خطافات Plugin](</ar/plugins/hooks>).

**أحداث دورة حياة Gateway** : يتضمن `gateway:shutdown` كلًا من `reason` و`restartExpectedMs` ويُطلق عند بدء إيقاف Gateway. يتضمن `gateway:pre-restart` السياق نفسه، لكنه يُطلق فقط عندما يكون الإيقاف جزءًا من إعادة تشغيل متوقعة وتُقدَّم قيمة `restartExpectedMs` محدودة. أثناء الإيقاف، يكون انتظار كل خطاف دورة حياة بأفضل جهد ومحدودًا بحيث يستمر الإيقاف إذا توقف معالج عن الاستجابة.

بين حدث `gateway:shutdown` (أو `gateway:pre-restart`) وبقية تسلسل الإيقاف، يطلق Gateway أيضًا خطاف Plugin مكتوبًا باسم `session_end` لكل جلسة كانت لا تزال نشطة عند توقف العملية. تكون قيمة `reason` في الحدث هي `shutdown` عند إيقاف SIGTERM/SIGINT عادي، و`restart` عندما يكون الإغلاق مجدولًا كجزء من إعادة تشغيل متوقعة. هذا التفريغ محدود بحيث لا يستطيع معالج `session_end` البطيء حظر خروج العملية، ويتم تخطي الجلسات التي أُنجز إنهاؤها مسبقًا عبر الاستبدال / إعادة الضبط / الحذف / Compaction لتجنب الإطلاق المزدوج.

## اكتشاف الخطافات

تُكتشف الخطافات من هذه الأدلة، بترتيب أسبقية تجاوز متزايدة:

  1. **الخطافات المضمنة** : تُشحن مع OpenClaw
  2. **خطافات Plugin** : خطافات مضمنة داخل plugins المثبتة
  3. **الخطافات المُدارة** : `~/.openclaw/hooks/` (مثبتة من المستخدم ومشتركة بين مساحات العمل). تشارك الأدلة الإضافية من `hooks.internal.load.extraDirs` هذه الأسبقية.
  4. **خطافات مساحة العمل** : `<workspace>/hooks/` (لكل وكيل، معطلة افتراضيًا حتى تُفعّل صراحة)


يمكن لخطافات مساحة العمل إضافة أسماء خطافات جديدة، لكنها لا تستطيع تجاوز الخطافات المضمنة أو المُدارة أو المقدمة من plugins التي تحمل الاسم نفسه.

يتخطى Gateway اكتشاف الخطافات الداخلية عند بدء التشغيل حتى تُكوَّن الخطافات الداخلية. فعّل خطافًا مضمنًا أو مُدارًا باستخدام `openclaw hooks enable <name>`، أو ثبّت حزمة خطافات، أو اضبط `hooks.internal.enabled=true` للاشتراك. عندما تفعّل خطافًا مسمى واحدًا، لا يحمّل Gateway إلا معالج ذلك الخطاف؛ أما `hooks.internal.enabled=true` وأدلة الخطافات الإضافية والمعالجات القديمة فتشترك في الاكتشاف الواسع.

### حزم الخطافات

حزم الخطافات هي حزم npm تصدّر الخطافات عبر `openclaw.hooks` في `package.json`. ثبّتها باستخدام:

bashCopy code
[code]
    openclaw plugins install <path-or-spec>
[/code]

مواصفات npm مقتصرة على السجل (اسم الحزمة + إصدار دقيق اختياري أو dist-tag). تُرفض مواصفات Git/URL/file ونطاقات semver.

## الخطافات المضمنة

الخطاف | الأحداث | ما يفعله  
---|---|---  
session-memory | `command:new`, `command:reset` | يحفظ سياق الجلسة في `<workspace>/memory/`  
bootstrap-extra-files | `agent:bootstrap` | يحقن ملفات تمهيد إضافية من أنماط glob  
command-logger | `command` | يسجل جميع الأوامر في `~/.openclaw/logs/commands.log`  
compaction-notifier | `session:compact:before`, `session:compact:after` | يرسل إشعارات دردشة مرئية عند بدء/انتهاء Compaction للجلسة  
boot-md | `gateway:startup` | يشغّل `BOOT.md` عند بدء Gateway  
  
فعّل أي خطاف مضمن:

bashCopy code
[code]
    openclaw hooks enable <hook-name>
[/code]

### تفاصيل session-memory

يستخرج آخر 15 رسالة للمستخدم/المساعد ويحفظها في `<workspace>/memory/YYYY-MM-DD-HHMM.md` باستخدام التاريخ المحلي للمضيف. يعمل التقاط الذاكرة في الخلفية بحيث لا تتأخر إقرارات `/new` و`/reset` بسبب قراءات النص أو إنشاء slug اختياري. اضبط `hooks.internal.entries.session-memory.llmSlug: true` لإنشاء slug وصفي لاسم الملف باستخدام النموذج المكوّن. يتطلب تكوين `workspace.dir`.

### إعداد bootstrap-extra-files

jsonCopy code
[code]
    {  "hooks": {    "internal": {      "entries": {        "bootstrap-extra-files": {          "enabled": true,          "paths": ["packages/*/AGENTS.md", "packages/*/TOOLS.md"]        }      }    }  }}
[/code]

تُحل المسارات نسبةً إلى مساحة العمل. لا تُحمّل إلا أسماء ملفات التمهيد الأساسية المعروفة (`AGENTS.md` و`SOUL.md` و`TOOLS.md` و`IDENTITY.md` و`USER.md` و`HEARTBEAT.md` و`BOOTSTRAP.md` و`MEMORY.md`).

### تفاصيل command-logger

يسجل كل أمر slash في `~/.openclaw/logs/commands.log`.

### تفاصيل compaction-notifier

يرسل رسائل حالة قصيرة إلى المحادثة الحالية عندما يبدأ OpenClaw وينتهي من ضغط نص الجلسة. يجعل هذا المنعطفات الطويلة أقل إرباكًا على واجهات الدردشة لأن المستخدم يستطيع رؤية أن المساعد يلخص السياق وسيواصل بعد Compaction.

### تفاصيل boot-md

يشغّل `BOOT.md` من مساحة العمل النشطة عند بدء Gateway.

## خطافات Plugin

يمكن لـ Plugins تسجيل خطافات مكتوبة عبر Plugin SDK لتكامل أعمق: اعتراض استدعاءات الأدوات، وتعديل المطالبات، والتحكم في تدفق الرسائل، وغير ذلك. استخدم خطافات Plugin عندما تحتاج إلى `before_tool_call` أو `before_agent_reply` أو `before_install` أو خطافات دورة حياة أخرى داخل العملية.

للاطلاع على مرجع خطافات Plugin الكامل، راجع [خطافات Plugin](</ar/plugins/hooks>).

## التكوين

jsonCopy code
[code]
    {  "hooks": {    "internal": {      "enabled": true,      "entries": {        "session-memory": { "enabled": true },        "command-logger": { "enabled": false }      }    }  }}
[/code]

متغيرات البيئة لكل خطاف:

jsonCopy code
[code]
    {  "hooks": {    "internal": {      "entries": {        "my-hook": {          "enabled": true,          "env": { "MY_CUSTOM_VAR": "value" }        }      }    }  }}
[/code]

أدلة الخطافات الإضافية:

jsonCopy code
[code]
    {  "hooks": {    "internal": {      "load": {        "extraDirs": ["/path/to/more/hooks"]      }    }  }}
[/code]

## مرجع CLI

bashCopy code
[code]
    # List all hooks (add --eligible, --verbose, or --json)openclaw hooks list # Show detailed info about a hookopenclaw hooks info <hook-name> # Show eligibility summaryopenclaw hooks check # Enable/disableopenclaw hooks enable <hook-name>openclaw hooks disable <hook-name>
[/code]

## أفضل الممارسات

  * **أبقِ المعالجات سريعة.** تعمل الخطافات أثناء معالجة الأوامر. شغّل الأعمال الثقيلة بأسلوب التشغيل والإهمال باستخدام `void processInBackground(event)`.
  * **تعامل مع الأخطاء بسلاسة.** لفّ العمليات الخطرة في try/catch؛ لا ترمِ استثناءات حتى تتمكن المعالجات الأخرى من العمل.
  * **رشّح الأحداث مبكرًا.** ارجع فورًا إذا لم يكن نوع الحدث/الإجراء ذا صلة.
  * **استخدم مفاتيح أحداث محددة.** فضّل `"events": ["command:new"]` على `"events": ["command"]` لتقليل الحمل الزائد.


## استكشاف الأخطاء وإصلاحها

### لم يتم اكتشاف الخطاف

bashCopy code
[code]
    # Verify directory structurels -la ~/.openclaw/hooks/my-hook/# Should show: HOOK.md, handler.ts # List all discovered hooksopenclaw hooks list
[/code]

### الخطاف غير مؤهل

bashCopy code
[code]
    openclaw hooks info my-hook
[/code]

تحقق من الملفات التنفيذية المفقودة (PATH)، أو متغيرات البيئة، أو قيم الإعدادات، أو توافق نظام التشغيل.

### الخطاف لا يُنفّذ

  1. تحقق من تمكين الخطاف: `openclaw hooks list`
  2. أعد تشغيل عملية Gateway حتى تعيد الخطافات التحميل.
  3. تحقق من سجلات Gateway: `./scripts/clawlog.sh | grep hook`


## ذو صلة

  * [مرجع CLI: الخطافات](</ar/cli/hooks>)
  * [Webhooks](</ar/automation/cron-jobs#webhooks>)
  * [خطافات Plugin](</ar/plugins/hooks>) — خطافات دورة حياة Plugin داخل العملية
  * [الإعدادات](</ar/gateway/configuration-reference#hooks>)


Was this useful?YesNo