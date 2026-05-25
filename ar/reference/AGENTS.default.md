---
title: AGENTS.md الافتراضي
source_url: https://docs.openclaw.ai/ar/reference/AGENTS.default
scraped_at: 2026-05-25
---

## التشغيل الأول (موصى به)

يستخدم OpenClaw دليل مساحة عمل مخصصًا للوكيل. الافتراضي: `~/.openclaw/workspace` (قابل للتهيئة عبر `agents.defaults.workspace`).

  1. أنشئ مساحة العمل (إذا لم تكن موجودة بالفعل):

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace
[/code]

  2. انسخ قوالب مساحة العمل الافتراضية إلى مساحة العمل:

bashCopy code
[code]
    cp docs/reference/templates/AGENTS.md ~/.openclaw/workspace/AGENTS.mdcp docs/reference/templates/SOUL.md ~/.openclaw/workspace/SOUL.mdcp docs/reference/templates/TOOLS.md ~/.openclaw/workspace/TOOLS.md
[/code]

  3. اختياري: إذا كنت تريد قائمة Skills للمساعد الشخصي، فاستبدل [AGENTS.md](<http://AGENTS.md>) بهذا الملف:

bashCopy code
[code]
    cp docs/reference/AGENTS.default.md ~/.openclaw/workspace/AGENTS.md
[/code]

  4. اختياري: اختر مساحة عمل مختلفة عبر ضبط `agents.defaults.workspace` (يدعم `~`):

json5Copy code
[code]
    {  agents: { defaults: { workspace: "~/.openclaw/workspace" } },}
[/code]

## الإعدادات الافتراضية للسلامة

  * لا تُدرج الأدلة أو الأسرار في الدردشة.
  * لا تُشغّل أوامر مدمّرة إلا إذا طُلب منك ذلك صراحة.
  * لا ترسل ردودًا جزئية/متدفقة إلى واجهات المراسلة الخارجية (الردود النهائية فقط).


## بدء الجلسة (مطلوب)

  * اقرأ `SOUL.md` و`USER.md` واليوم+أمس في `memory/`.
  * اقرأ `MEMORY.md` عند وجوده.
  * افعل ذلك قبل الرد.


## الروح (مطلوب)

  * يعرّف `SOUL.md` الهوية والنبرة والحدود. أبقه محدّثًا.
  * إذا غيّرت `SOUL.md`، فأخبر المستخدم.
  * أنت نسخة جديدة في كل جلسة؛ الاستمرارية موجودة في هذه الملفات.


## المساحات المشتركة (موصى بها)

  * أنت لست صوت المستخدم؛ كن حذرًا في دردشات المجموعات أو القنوات العامة.
  * لا تشارك بيانات خاصة أو معلومات اتصال أو ملاحظات داخلية.


## نظام الذاكرة (موصى به)

  * السجل اليومي: `memory/YYYY-MM-DD.md` (أنشئ `memory/` إذا لزم الأمر).
  * الذاكرة طويلة الأمد: `MEMORY.md` للحقائق والتفضيلات والقرارات الدائمة.
  * `memory.md` بالأحرف الصغيرة هو إدخال إصلاح قديم فقط؛ لا تحتفظ بملفي الجذر معًا عمدًا.
  * عند بدء الجلسة، اقرأ اليوم + أمس + `MEMORY.md` عند وجوده.
  * الالتقاط: القرارات، التفضيلات، القيود، الحلقات المفتوحة.
  * تجنّب الأسرار إلا إذا طُلب منك ذلك صراحة.


## الأدوات وSkills

  * الأدوات موجودة داخل Skills؛ اتبع `SKILL.md` الخاص بكل Skill عند الحاجة إليها.
  * احتفظ بالملاحظات الخاصة بالبيئة في `TOOLS.md` (ملاحظات لـ Skills).


## نصيحة النسخ الاحتياطي (موصى بها)

إذا تعاملت مع مساحة العمل هذه كأنها "ذاكرة" Clawd، فاجعلها مستودع git (خاصًا على نحو مثالي) حتى تُنسخ `AGENTS.md` وملفات الذاكرة احتياطيًا.

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.mdgit commit -m "Add Clawd workspace"# Optional: add a private remote + push
[/code]

## ما يفعله OpenClaw

  * يشغّل WhatsApp gateway + وكيل ترميز Pi حتى يتمكن المساعد من قراءة/كتابة الدردشات، وجلب السياق، وتشغيل Skills عبر جهاز Mac المضيف.
  * يدير تطبيق macOS الأذونات (تسجيل الشاشة، الإشعارات، الميكروفون) ويكشف CLI `openclaw` عبر الملف الثنائي المضمّن فيه.
  * تنهار الدردشات المباشرة في جلسة `main` الخاصة بالوكيل افتراضيًا؛ تبقى المجموعات معزولة كـ `agent:<agentId>:<channel>:group:<id>` (الغرف/القنوات: `agent:<agentId>:<channel>:channel:<id>`); تُبقي Heartbeats المهام الخلفية نشطة.


## Skills الأساسية (فعّلها في الإعدادات → Skills)

  * **mcporter** \- وقت تشغيل/CLI لخادم الأدوات لإدارة خلفيات Skills الخارجية.
  * **Peekaboo** \- لقطات شاشة macOS سريعة مع تحليل رؤية اختياري بالذكاء الاصطناعي.
  * **camsnap** \- التقاط إطارات أو مقاطع أو تنبيهات حركة من كاميرات أمان RTSP/ONVIF.
  * **oracle** \- CLI وكيل جاهز لـ OpenAI مع إعادة تشغيل الجلسات والتحكم في المتصفح.
  * **eightctl** \- تحكّم في نومك من الطرفية.
  * **imsg** \- إرسال iMessage وSMS وقراءتهما وبثهما.
  * **wacli** \- CLI لـ WhatsApp: مزامنة، بحث، إرسال.
  * **discord** \- إجراءات Discord: تفاعلات، ملصقات، استطلاعات. استخدم أهداف `user:<id>` أو `channel:<id>` (المعرّفات الرقمية المجردة ملتبسة).
  * **gog** \- CLI لـ Google Suite: Gmail، Calendar، Drive، Contacts.
  * **spotify-player** \- عميل Spotify للطرفية للبحث/الإضافة إلى قائمة الانتظار/التحكم في التشغيل.
  * **sag** \- كلام ElevenLabs مع تجربة استخدام say بأسلوب mac؛ يتدفق إلى السماعات افتراضيًا.
  * **Sonos CLI** \- التحكّم في سماعات Sonos (الاكتشاف/الحالة/التشغيل/مستوى الصوت/التجميع) من السكربتات.
  * **blucli** \- تشغيل مشغلات BluOS وتجميعها وأتمتتها من السكربتات.
  * **OpenHue CLI** \- التحكّم في إضاءة Philips Hue للمشاهد والأتمتة.
  * **OpenAI Whisper** \- تحويل الكلام إلى نص محلي للإملاء السريع ونصوص البريد الصوتي.
  * **Gemini CLI** \- نماذج Google Gemini من الطرفية للأسئلة والأجوبة السريعة.
  * **agent-tools** \- مجموعة أدوات مساعدة للأتمتة والسكربتات المساعدة.


## ملاحظات الاستخدام

  * فضّل CLI `openclaw` للسكربتات؛ يتولى تطبيق mac الأذونات.
  * شغّل عمليات التثبيت من تبويب Skills؛ فهو يخفي الزر إذا كان الملف الثنائي موجودًا بالفعل.
  * أبقِ Heartbeats مفعّلة حتى يتمكن المساعد من جدولة التذكيرات، ومراقبة صناديق الوارد، وتشغيل التقاطات الكاميرا.
  * تعمل واجهة Canvas بملء الشاشة مع تراكبات أصلية. تجنّب وضع عناصر التحكم الحرجة في الحواف العلوية اليسرى/العلوية اليمنى/السفلية؛ أضف هوامش صريحة في التخطيط ولا تعتمد على هوامش المنطقة الآمنة.
  * للتحقق المعتمد على المتصفح، استخدم `openclaw browser` (التبويبات/الحالة/لقطة الشاشة) مع ملف Chrome الشخصي المُدار بواسطة OpenClaw.
  * لفحص DOM، استخدم `openclaw browser eval|query|dom|snapshot` (ومعه `--json`/`--out` عندما تحتاج إلى مخرجات قابلة للمعالجة آليًا).
  * للتفاعلات، استخدم `openclaw browser click|type|hover|drag|select|upload|press|wait|navigate|back|evaluate|run` (يتطلب click/type مراجع snapshot؛ استخدم `evaluate` لمحددات CSS).


## ذات صلة

  * [مساحة عمل الوكيل](</ar/concepts/agent-workspace>)
  * [وقت تشغيل الوكيل](</ar/concepts/agent>)


Was this useful?YesNo