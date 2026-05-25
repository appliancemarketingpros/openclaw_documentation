---
title: مساحة عمل الوكيل
source_url: https://docs.openclaw.ai/ar/concepts/agent-workspace
scraped_at: 2026-05-25
---

مساحة العمل هي موطن الوكيل. وهي دليل العمل الوحيد المستخدم لأدوات الملفات ولسياق مساحة العمل. أبقها خاصة وتعامل معها كذاكرة.

هذا منفصل عن `~/.openclaw/`، الذي يخزن الإعدادات وبيانات الاعتماد والجلسات.

## الموقع الافتراضي

  * الافتراضي: `~/.openclaw/workspace`
  * إذا كان `OPENCLAW_PROFILE` مضبوطًا وليس `"default"`، يصبح الافتراضي `~/.openclaw/workspace-<profile>`.
  * يمكنك التجاوز في `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/.openclaw/workspace",    },  },}
[/code]

سينشئ `openclaw onboard` أو `openclaw configure` أو `openclaw setup` مساحة العمل ويضيف ملفات التمهيد الأولية إذا كانت مفقودة.

إذا كنت تدير ملفات مساحة العمل بنفسك بالفعل، فيمكنك تعطيل إنشاء ملفات التمهيد:

json5Copy code
[code]
    { agents: { defaults: { skipBootstrap: true } } }
[/code]

## مجلدات مساحة عمل إضافية

قد تكون التثبيتات الأقدم أنشأت `~/openclaw`. قد يؤدي إبقاء عدة أدلة لمساحات العمل إلى التباس في المصادقة أو انحراف في الحالة، لأن مساحة عمل واحدة فقط تكون نشطة في كل مرة.

## خريطة ملفات مساحة العمل

هذه هي الملفات القياسية التي يتوقع OpenClaw وجودها داخل مساحة العمل:

AGENTS.md - تعليمات التشغيل

تعليمات التشغيل للوكيل وكيف ينبغي له استخدام الذاكرة. تُحمّل عند بداية كل جلسة. مكان جيد للقواعد والأولويات وتفاصيل "كيفية التصرف".

SOUL.md - الشخصية والنبرة

الشخصية والنبرة والحدود. تُحمّل في كل جلسة. الدليل: [دليل شخصية SOUL.md](</ar/concepts/soul>).

USER.md - من هو المستخدم

من هو المستخدم وكيفية مخاطبته. يُحمّل في كل جلسة.

IDENTITY.md - الاسم والطابع والرمز التعبيري

اسم الوكيل وطابعه ورمزه التعبيري. يُنشأ/يُحدّث أثناء طقس التمهيد.

TOOLS.md - اصطلاحات الأدوات المحلية

ملاحظات عن أدواتك المحلية واصطلاحاتها. لا تتحكم في إتاحة الأدوات؛ فهي إرشادات فقط.

HEARTBEAT.md - قائمة تحقق Heartbeat

قائمة تحقق صغيرة اختيارية لتشغيلات Heartbeat. أبقها قصيرة لتجنب استهلاك الرموز.

BOOT.md - قائمة تحقق بدء التشغيل

قائمة تحقق اختيارية لبدء التشغيل تُشغّل تلقائيًا عند إعادة تشغيل Gateway (عند تمكين [الخطافات الداخلية](</ar/automation/hooks>)). أبقها قصيرة؛ واستخدم أداة الرسائل للإرسال الصادر.

BOOTSTRAP.md - طقس التشغيل الأول

طقس تشغيل أول لمرة واحدة. يُنشأ فقط لمساحة عمل جديدة تمامًا. احذفه بعد اكتمال الطقس.

memory/YYYY-MM-DD.md - سجل الذاكرة اليومي

سجل الذاكرة اليومي (ملف واحد لكل يوم). يُوصى بقراءة اليوم + أمس عند بدء الجلسة.

MEMORY.md - ذاكرة طويلة الأمد منتقاة (اختياري)

ذاكرة طويلة الأمد منتقاة: حقائق دائمة، وتفضيلات، وقرارات، وملخصات قصيرة. احتفظ بالسجلات المفصلة في `memory/YYYY-MM-DD.md` حتى تتمكن أدوات الذاكرة من استرجاعها عند الطلب دون حقنها في كل مطالبة. حمّل `MEMORY.md` فقط في الجلسة الرئيسية الخاصة (وليس في سياقات المشاركة/المجموعات). راجع [الذاكرة](</ar/concepts/memory>) لمعرفة سير العمل وتفريغ الذاكرة التلقائي.

skills/ - Skills مساحة العمل (اختياري)

Skills خاصة بمساحة العمل. موقع Skills الأعلى أولوية لتلك المساحة. يتجاوز Skills وكيل المشروع، وSkills الوكيل الشخصية، وSkills المُدارة، وSkills المضمّنة، و`skills.load.extraDirs` عند تعارض الأسماء.

canvas/ - ملفات واجهة Canvas (اختياري)

ملفات واجهة Canvas لعروض العقد (مثل `canvas/index.html`).

## ما ليس ضمن مساحة العمل

هذه العناصر موجودة ضمن `~/.openclaw/` ويجب ألا تُلتزم في مستودع مساحة العمل:

  * `~/.openclaw/openclaw.json` (الإعدادات)
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` (ملفات مصادقة النموذج: OAuth + مفاتيح API)
  * `~/.openclaw/agents/<agentId>/agent/codex-home/` (حساب تشغيل Codex لكل وكيل، والإعدادات، وSkills، وplugins، وحالة السلسلة الأصلية)
  * `~/.openclaw/credentials/` (حالة القناة/المزوّد بالإضافة إلى بيانات استيراد OAuth القديمة)
  * `~/.openclaw/agents/<agentId>/sessions/` (نصوص الجلسات + البيانات الوصفية)
  * `~/.openclaw/skills/` (Skills مُدارة)


إذا كنت بحاجة إلى ترحيل الجلسات أو الإعدادات، فانسخها بشكل منفصل وأبقها خارج التحكم في الإصدارات.

## النسخ الاحتياطي عبر Git (موصى به، خاص)

تعامل مع مساحة العمل كذاكرة خاصة. ضعها في مستودع git **خاص** بحيث تكون منسوخة احتياطيًا وقابلة للاسترداد.

شغّل هذه الخطوات على الجهاز الذي يعمل عليه Gateway (فهذا هو مكان وجود مساحة العمل).

* ### تهيئة المستودع

إذا كان git مثبتًا، تتم تهيئة مساحات العمل الجديدة تمامًا تلقائيًا. إذا لم تكن مساحة العمل هذه مستودعًا بالفعل، فشغّل:

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.md SOUL.md TOOLS.md IDENTITY.md USER.md HEARTBEAT.md memory/git commit -m "Add agent workspace"
[/code]

* ### إضافة مستودع بعيد خاص

### واجهة GitHub على الويب

  1. أنشئ مستودعًا **خاصًا** جديدًا على GitHub.
  2. لا تهيئه بملف README (لتجنب تعارضات الدمج).
  3. انسخ عنوان URL البعيد عبر HTTPS.
  4. أضف المستودع البعيد وادفع:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

### GitHub CLI (gh)

bashCopy code
[code]
    gh auth logingh repo create openclaw-workspace --private --source . --remote origin --push
[/code]

### واجهة GitLab على الويب

  1. أنشئ مستودعًا **خاصًا** جديدًا على GitLab.
  2. لا تهيئه بملف README (لتجنب تعارضات الدمج).
  3. انسخ عنوان URL البعيد عبر HTTPS.
  4. أضف المستودع البعيد وادفع:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

* ### التحديثات المستمرة

bashCopy code
[code]
    git statusgit add .git commit -m "Update memory"git push
[/code]

## لا تلتزم الأسرار

بداية مقترحة لملف `.gitignore`:

gitignoreCopy code
[code]
    .DS_Store.env**/*.key**/*.pem**/secrets*
[/code]

## نقل مساحة العمل إلى جهاز جديد

* ### استنساخ المستودع

استنسخ المستودع إلى المسار المطلوب (الافتراضي `~/.openclaw/workspace`).

* ### تحديث الإعدادات

اضبط `agents.defaults.workspace` على ذلك المسار في `~/.openclaw/openclaw.json`.

* ### زرع الملفات المفقودة

شغّل `openclaw setup --workspace <path>` لزرع أي ملفات مفقودة.

* ### نسخ الجلسات (اختياري)

إذا كنت بحاجة إلى الجلسات، فانسخ `~/.openclaw/agents/<agentId>/sessions/` من الجهاز القديم بشكل منفصل.

## ملاحظات متقدمة

  * يمكن للتوجيه متعدد الوكلاء استخدام مساحات عمل مختلفة لكل وكيل. راجع [توجيه القنوات](</ar/channels/channel-routing>) لإعدادات التوجيه.
  * إذا كان `agents.defaults.sandbox` ممكّنًا، فيمكن للجلسات غير الرئيسية استخدام مساحات عمل عزل لكل جلسة ضمن `agents.defaults.sandbox.workspaceRoot`.


## ذو صلة

  * [Heartbeat](</ar/gateway/heartbeat>) \- ملف مساحة العمل [HEARTBEAT.md](<http://HEARTBEAT.md>)
  * [العزل](</ar/gateway/sandboxing>) \- الوصول إلى مساحة العمل في البيئات المعزولة
  * [الجلسة](</ar/concepts/session>) \- مسارات تخزين الجلسات
  * [الأوامر الدائمة](</ar/automation/standing-orders>) \- التعليمات المستمرة في ملفات مساحة العمل


Was this useful?YesNo