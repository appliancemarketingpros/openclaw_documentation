---
title: ورشة عمل Skills
source_url: https://docs.openclaw.ai/ar/tools/skill-workshop
scraped_at: 2026-06-29
---

CapabilitiesSkills

ورشة Skills هي المسار المحكوم في OpenClaw لإنشاء Skills مساحة العمل وتحديثها.

لا يكتب الوكلاء والمشغلون ملفات `SKILL.md` النشطة مباشرة عبر هذا المسار. بل ينشئون **مقترحًا** أولًا. المقترح هو مسودة معلّقة تحتوي على محتوى Skill المقترح، وربط الهدف، وحالة الماسح، والتجزئات، وبيانات تعريف ملفات الدعم، وبيانات تعريف الرجوع. ولا يصبح Skill حيًا إلا عند تطبيقه.

تكتب ورشة Skills مهارات مساحة العمل فقط. ولا تعدّل Skills المضمّنة، أو Plugin، أو ClawHub، أو الجذر الإضافي، أو المُدارة، أو وكيلًا شخصيًا، أو Skills النظام.

## كيف تعمل

  * **المقترح أولًا:** يُخزّن محتوى Skill المُولّد باسم `PROPOSAL.md`، وليس `SKILL.md`.
  * **التطبيق هو الكتابة الحية الوحيدة:** لا تغيّر عمليات الإنشاء، والتحديث، والمراجعة Skills النشطة.
  * **مقيّدة بمساحة العمل:** تستهدف عمليات الإنشاء جذر `skills/` الخاص بمساحة العمل. ولا تُسمح التحديثات إلا لمهارات مساحة العمل القابلة للكتابة.
  * **لا استبدال قسري:** تفشل عملية الإنشاء إذا كان Skill الهدف موجودًا بالفعل.
  * **مربوط بالتجزئة:** ترتبط مقترحات التحديث بتجزئة الهدف الحالية وتصبح قديمة إذا تغيّر Skill الحي قبل التطبيق.
  * **محكومة بالماسح:** تعيد عملية التطبيق تشغيل الفحص قبل الكتابة.
  * **قابلة للاسترداد:** تكتب عملية التطبيق بيانات تعريف الرجوع قبل تغيير الملفات الحية.
  * **أسطح متسقة:** تستدعي الدردشة، وCLI، وGateway كلها خدمة ورشة Skills نفسها.


## دورة الحياة

textCopy code
[code]
    create/update -> pendingrevise        -> pendingapply         -> appliedreject        -> rejectedquarantine    -> quarantinedtarget change -> stale
[/code]

لا يمكن مراجعة أو تطبيق أو رفض أو عزل إلا المقترحات ذات الحالة `pending`.

## الدردشة

اطلب من الوكيل Skill الذي تريده. يستدعي الوكيل `skill_workshop` ويعيد معرّف مقترح.

إنشاء:

textCopy code
[code]
    Make a skill called morning-catchup that runs my Monday inbox routine.
[/code]

تحديث Skill موجود في مساحة العمل:

textCopy code
[code]
    Update trip-planning to also check seat maps before booking.
[/code]

التكرار على مقترح معلّق:

textCopy code
[code]
    Show me the morning-catchup proposal.Revise it to also flag anything marked urgent.Apply the morning-catchup proposal.
[/code]

افتراضيًا، تُظهر عمليات `apply` و`reject` و`quarantine` التي يبدأها الوكيل مطالبة موافقة قبل تشغيلها. اضبط `skills.workshop.approvalPolicy` على `"auto"` لتخطي المطالبة في البيئات الموثوقة.

## CLI

إنشاء مقترح Skill جديد:

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name morning-catchup \  --description "Daily inbox catch-up: triage, archive, surface, draft, plan" \  --proposal ./PROPOSAL.md
[/code]

إنشاء مقترح تحديث لـ Skill موجود في مساحة العمل:

bashCopy code
[code]
    openclaw skills workshop propose-update trip-planning --proposal ./PROPOSAL.md
[/code]

السرد والفحص:

bashCopy code
[code]
    openclaw skills workshop listopenclaw skills workshop inspect <proposal-id>
[/code]

المراجعة قبل الموافقة:

bashCopy code
[code]
    openclaw skills workshop revise <proposal-id> --proposal ./PROPOSAL.md
[/code]

إغلاق المقترح:

bashCopy code
[code]
    openclaw skills workshop apply <proposal-id>openclaw skills workshop reject <proposal-id> --reason "Duplicate"openclaw skills workshop quarantine <proposal-id> --reason "Needs security review"
[/code]

## محتوى المقترح

أثناء التعليق، يُخزّن المقترح باسم `PROPOSAL.md` مع frontmatter خاص بالمقترح فقط:

markdownCopy code
[code]
    ---name: "morning-catchup"description: "Daily inbox catch-up: triage, archive, surface, draft, plan"status: proposalversion: "v1"date: "2026-05-30T00:00:00.000Z"---
[/code]

عند التطبيق، تكتب ورشة Skills ملف `SKILL.md` النشط وتزيل الحقول الخاصة بالمقترح فقط: `status`، و`version` الخاص بالمقترح، و`date` الخاص بالمقترح.

## ملفات الدعم

استخدم `--proposal-dir` عندما يحتاج Skill المقترح إلى ملفات بجانب `PROPOSAL.md`:

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name weekly-update \  --description "Friday wrap-up: stats, highlights, next week's top three" \  --proposal-dir ./weekly-update-proposal
[/code]

يجب أن يحتوي الدليل على `PROPOSAL.md`. يجب أن تكون ملفات الدعم ضمن:

  * `assets/`
  * `examples/`
  * `references/`
  * `scripts/`
  * `templates/`


تفحص ورشة Skills ملفات الدعم وتجزئها وتخزنها مع المقترح. ولا تُكتب بجانب ملف `SKILL.md` الحي إلا عند التطبيق.

تشمل مسارات ملفات الدعم المرفوضة المسارات المطلقة، ومقاطع المسار المخفية، واجتياز المسارات، والمسارات المتداخلة، والملفات التنفيذية من أدلة المقترحات، والنص غير UTF-8، والبايتات الفارغة، والملفات خارج مجلدات الدعم القياسية.

## أداة الوكيل

يستخدم النموذج `skill_workshop`:

textCopy code
[code]
    action: create | update | revise | list | inspect | apply | reject | quarantine
[/code]

يجب على الوكلاء استخدام `skill_workshop` لأعمال Skill المُولّدة. ويجب ألا ينشئوا أو يغيّروا ملفات المقترحات عبر `write` أو `edit` أو `exec` أو أوامر الصدفة أو عمليات نظام الملفات المباشرة.

## الموافقة والاستقلالية

json5Copy code
[code]
    {  skills: {    workshop: {      autonomous: {        enabled: false,      },      allowSymlinkTargetWrites: false,      approvalPolicy: "pending",      maxPending: 50,      maxSkillBytes: 40000,    },  },}
[/code]

  * `autonomous.enabled`: يسمح لـ OpenClaw بإنشاء مقترحات معلّقة من إشارات محادثة دائمة بعد دورات ناجحة. الافتراضي: `false`.
  * `allowSymlinkTargetWrites`: يسمح للتطبيق بالكتابة عبر روابط Skills الرمزية في مساحة العمل التي يكون هدفها الحقيقي مدرجًا في `skills.load.allowSymlinkTargets`. الافتراضي: `false`.
  * `approvalPolicy: "pending"`: يتطلب مطالبة موافقة قبل `apply` أو `reject` أو `quarantine` التي يبدأها الوكيل.
  * `approvalPolicy: "auto"`: يتخطى مطالبة الموافقة تلك. يجب أن يظل الوكيل مستدعيًا للإجراء.
  * `maxPending`: يحد عدد المقترحات المعلّقة والمعزولة لكل مساحة عمل.
  * `maxSkillBytes`: يحد حجم متن المقترح. الافتراضي: `40000`.


تُقيّد أوصاف المقترحات دائمًا بـ 160 بايت.

## أساليب Gateway

textCopy code
[code]
    skills.proposals.listskills.proposals.inspectskills.proposals.createskills.proposals.updateskills.proposals.reviseskills.proposals.applyskills.proposals.rejectskills.proposals.quarantine
[/code]

تتطلب الأساليب للقراءة فقط `operator.read`. وتتطلب الأساليب المُعدِّلة `operator.admin`.

## التخزين

textCopy code
[code]
    &lt;OPENCLAW_STATE_DIR&gt;/skill-workshop/  proposals.json  proposals/<proposal-id>/    proposal.json    PROPOSAL.md    rollback.json    assets/    examples/    references/    scripts/    templates/
[/code]

دليل الحالة الافتراضي: `~/.openclaw`.

  * `proposal.json`: سجل المقترح القانوني.
  * `proposals.json`: فهرس سرد سريع، قابل لإعادة البناء من مجلدات المقترحات.
  * `PROPOSAL.md`: مقترح Skill معلّق.
  * `rollback.json`: بيانات تعريف الاسترداد المكتوبة قبل أن يغيّر التطبيق الملفات الحية.


## الحدود

  * الوصف: 160 بايت.
  * متن المقترح: `skills.workshop.maxSkillBytes` (الافتراضي 40,000).
  * ملفات الدعم: 64 لكل مقترح.
  * حجم ملف الدعم: 256 كيلوبايت لكل ملف، و2 ميغابايت إجمالًا.
  * المقترحات المعلّقة والمعزولة: `skills.workshop.maxPending` لكل مساحة عمل (الافتراضي 50).


## استكشاف الأخطاء وإصلاحها

المشكلة | الحل  
---|---  
`Skill proposal description is too large` | اختصر `description` إلى 160 بايت أو أقل.  
`Skill proposal content is too large` | اختصر متن المقترح أو ارفع `skills.workshop.maxSkillBytes`.  
`Target skill changed after proposal creation` | راجع المقترح مقابل الهدف الحالي، أو أنشئ مقترحًا جديدًا.  
`Proposal scan failed` | افحص نتائج الماسح، ثم راجع المقترح أو اعزله.  
`untrusted symlink target` | اضبط `skills.load.allowSymlinkTargets` ومكّن `skills.workshop.allowSymlinkTargetWrites` فقط لجذور Skills المشتركة المقصودة.  
`Support file paths must be under one of...` | انقل ملفات الدعم إلى `assets/` أو `examples/` أو `references/` أو `scripts/` أو `templates/`.  
لا يظهر المقترح في القائمة | تحقق من مساحة العمل المحددة عبر `--agent` و`OPENCLAW_STATE_DIR`.  
لا يستطيع الوكيل استدعاء `skill_workshop` | تحقق من سياسة الأدوات النشطة ووضع التشغيل. يتضمن `coding` الأداة؛ ويجب أن تدرج سياسات `tools.allow` التقييدية الأداة صراحةً، كما يجب أن تستخدم عمليات التشغيل المعزولة جلسة وكيل عادية على جانب المضيف أو CLI.  
  
## ذات صلة

  * [Skills](</ar/tools/skills>) لترتيب التحميل، والأسبقية، والرؤية
  * [إنشاء Skills](</ar/tools/creating-skills>) للأساسيات المكتوبة يدويًا في `SKILL.md`
  * [إعدادات Skills](</ar/tools/skills-config>) للمخطط الكامل لـ `skills.workshop`
  * [CLI الخاص بـ Skills](</ar/cli/skills>) لأوامر `openclaw skills`


Was this useful?YesNo

Open issue