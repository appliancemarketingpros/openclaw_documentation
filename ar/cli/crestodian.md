---
title: Crestodian
source_url: https://docs.openclaw.ai/ar/cli/crestodian
scraped_at: 2026-05-25
---

# `openclaw crestodian`

Crestodian هو مساعد OpenClaw المحلي للإعداد، والإصلاح، والتهيئة. وهو مصمَّم ليبقى متاحًا عندما يكون مسار الوكيل العادي معطّلًا.

تشغيل `openclaw` من دون أمر يبدأ Crestodian في طرفية تفاعلية. وتشغيل `openclaw crestodian` يبدأ المساعد نفسه صراحةً.

## ما يعرضه Crestodian

عند بدء التشغيل، يفتح Crestodian التفاعلي صدفة TUI نفسها التي يستخدمها `openclaw tui`، مع خلفية محادثة Crestodian. يبدأ سجل المحادثة بتحية قصيرة توضح:

  * متى تبدأ Crestodian
  * النموذج أو مسار المخطِّط الحتمي الذي يستخدمه Crestodian فعليًا
  * صلاحية التهيئة والوكيل الافتراضي
  * إمكانية الوصول إلى Gateway من أول فحص بدء تشغيل
  * إجراء التصحيح التالي الذي يستطيع Crestodian تنفيذه


لا يفرغ الأسرار ولا يحمّل أوامر CLI الخاصة بالإضافات لمجرد البدء. يظل TUI يوفر الترويسة العادية، وسجل المحادثة، وسطر الحالة، والتذييل، والإكمال التلقائي، وعناصر تحكم المحرر.

استخدم `status` للحصول على الجرد التفصيلي الذي يتضمن مسار التهيئة، ومسارات المستندات/المصدر، وفحوص CLI المحلية، ووجود مفاتيح API، والوكلاء، والنموذج، وتفاصيل Gateway.

يستخدم Crestodian اكتشاف مراجع OpenClaw نفسه الذي تستخدمه الوكلاء العاديون. في نسخة Git checkout، يوجه نفسه إلى `docs/` المحلية وشجرة المصدر المحلية. وفي تثبيت حزمة npm، فإنه يستخدم مستندات الحزمة المضمّنة ويربط إلى <https://github.com/openclaw/openclaw>، مع إرشاد صريح لمراجعة المصدر كلما لم تكن المستندات كافية.

## أمثلة

bashCopy code
[code]
    openclawopenclaw crestodianopenclaw crestodian --jsonopenclaw crestodian --message "models"openclaw crestodian --message "validate config"openclaw crestodian --message "setup workspace ~/Projects/work model openai/gpt-5.5" --yesopenclaw crestodian --message "set default model openai/gpt-5.5" --yesopenclaw onboard --modern
[/code]

داخل TUI الخاص بـ Crestodian:

textCopy code
[code]
    statushealthdoctordoctor fixvalidate configsetupsetup workspace ~/Projects/work model openai/gpt-5.5config set gateway.port 19001config set-ref gateway.auth.token env OPENCLAW_GATEWAY_TOKENgateway statusrestart gatewayagentscreate agent work workspace ~/Projects/workmodelsset default model openai/gpt-5.5plugins listplugins search slackplugin install clawhub:openclaw-codex-app-serverplugin uninstall openclaw-codex-app-servertalk to work agenttalk to agent for ~/Projects/workauditquit
[/code]

## بدء التشغيل الآمن

مسار بدء تشغيل Crestodian صغير عمدًا. يمكن تشغيله عندما:

  * يكون `openclaw.json` مفقودًا
  * يكون `openclaw.json` غير صالح
  * يكون Gateway متوقفًا
  * يكون تسجيل أوامر الإضافات غير متاح
  * لم تتم تهيئة أي وكيل بعد


لا يزال `openclaw --help` و`openclaw --version` يستخدمان المسارات السريعة العادية. يخرج `openclaw` غير التفاعلي برسالة قصيرة بدلًا من طباعة تعليمات الجذر، لأن المنتج من دون أمر هو Crestodian.

## العمليات والموافقة

يستخدم Crestodian عمليات مُنمَّطة بدلًا من تعديل التهيئة بطريقة عشوائية.

يمكن تشغيل العمليات للقراءة فقط فورًا:

  * عرض نظرة عامة
  * سرد الوكلاء
  * سرد الإضافات المثبتة
  * البحث في إضافات ClawHub
  * عرض حالة النموذج/الخلفية
  * تشغيل فحوص الحالة أو الصحة
  * التحقق من إمكانية الوصول إلى Gateway
  * تشغيل doctor من دون إصلاحات تفاعلية
  * التحقق من التهيئة
  * عرض مسار سجل التدقيق


تتطلب العمليات الدائمة موافقة محادثية في الوضع التفاعلي إلا إذا مررت `--yes` لأمر مباشر:

  * كتابة التهيئة
  * تشغيل `config set`
  * ضبط قيم SecretRef المدعومة عبر `config set-ref`
  * تشغيل تهيئة الإعداد/الإلحاق
  * تغيير النموذج الافتراضي
  * بدء Gateway أو إيقافه أو إعادة تشغيله
  * إنشاء وكلاء
  * تثبيت إضافات من ClawHub أو npm
  * إلغاء تثبيت الإضافات
  * تشغيل إصلاحات doctor التي تعيد كتابة التهيئة أو الحالة


تُسجَّل عمليات الكتابة المطبقة في:

textCopy code
[code]
    ~/.openclaw/audit/crestodian.jsonl
[/code]

لا يتم تدقيق الاكتشاف. تُسجَّل فقط العمليات وعمليات الكتابة المطبقة.

يبدأ `openclaw onboard --modern` Crestodian كمعاينة الإلحاق الحديثة. أما `openclaw onboard` العادي فلا يزال يشغّل الإلحاق الكلاسيكي.

## تهيئة الإعداد

`setup` هو تهيئة الإلحاق التي تبدأ بالمحادثة. يكتب فقط عبر عمليات تهيئة مُنمَّطة ويطلب الموافقة أولًا.

textCopy code
[code]
    setupsetup workspace ~/Projects/worksetup workspace ~/Projects/work model openai/gpt-5.5
[/code]

عندما لا يكون أي نموذج مُهيّأ، يختار الإعداد أول خلفية قابلة للاستخدام بهذا الترتيب ويخبرك بما اختاره:

  * النموذج الصريح الموجود، إذا كان مُهيّأ مسبقًا
  * `OPENAI_API_KEY` -> `openai/gpt-5.5`
  * `ANTHROPIC_API_KEY` -> `anthropic/claude-opus-4-7`
  * Claude Code CLI -> `claude-cli/claude-opus-4-7`
  * Codex CLI -> `codex-cli/gpt-5.5`


إذا لم يكن أي منها متاحًا، يظل الإعداد يكتب مساحة العمل الافتراضية ويترك النموذج غير مضبوط. ثبّت Codex/Claude Code أو سجّل الدخول إليهما، أو اكشف `OPENAI_API_KEY`/`ANTHROPIC_API_KEY`، ثم شغّل الإعداد مرة أخرى.

## المخطِّط بمساعدة النموذج

يبدأ Crestodian دائمًا في الوضع الحتمي. بالنسبة إلى الأوامر الغامضة التي لا يفهمها المحلل الحتمي، يمكن لـ Crestodian المحلي إجراء دورة تخطيط محدودة واحدة عبر مسارات تشغيل OpenClaw العادية. يستخدم أولًا نموذج OpenClaw المُهيّأ. إذا لم يكن أي نموذج مُهيّأ قابلًا للاستخدام بعد، فيمكنه الرجوع إلى بيئات التشغيل المحلية الموجودة مسبقًا على الجهاز:

  * Claude Code CLI: `claude-cli/claude-opus-4-7`
  * حزمة Codex app-server: `openai/gpt-5.5`
  * Codex CLI: `codex-cli/gpt-5.5`


لا يستطيع المخطِّط بمساعدة النموذج تعديل التهيئة مباشرة. يجب أن يترجم الطلب إلى أحد أوامر Crestodian المُنمَّطة، ثم تُطبَّق قواعد الموافقة والتدقيق العادية. يطبع Crestodian النموذج الذي استخدمه والأمر المفسَّر قبل تشغيل أي شيء. دورات مخطِّط الرجوع بلا تهيئة تكون مؤقتة، ومعطَّلة الأدوات حيثما تدعمه بيئة التشغيل، وتستخدم مساحة عمل/جلسة مؤقتة.

لا يستخدم وضع الإنقاذ عبر قناة الرسائل المخطِّط بمساعدة النموذج. يبقى الإنقاذ البعيد حتميًا حتى لا يمكن استخدام مسار وكيل عادي معطّل أو مخترق كمحرر تهيئة.

## التبديل إلى وكيل

استخدم محددًا باللغة الطبيعية لمغادرة Crestodian وفتح TUI العادي:

textCopy code
[code]
    talk to agenttalk to work agentswitch to main agent
[/code]

لا تزال `openclaw tui` و`openclaw chat` و`openclaw terminal` تفتح TUI الخاص بالوكيل العادي مباشرةً. وهي لا تبدأ Crestodian.

بعد التبديل إلى TUI العادي، استخدم `/crestodian` للعودة إلى Crestodian. يمكنك تضمين طلب متابعة:

textCopy code
[code]
    /crestodian/crestodian restart gateway
[/code]

تترك تبديلات الوكلاء داخل TUI علامة مسار تشير إلى أن `/crestodian` متاح.

## وضع الإنقاذ عبر الرسائل

وضع الإنقاذ عبر الرسائل هو نقطة دخول قناة الرسائل إلى Crestodian. وهو مخصص للحالة التي يكون فيها وكيلك العادي متوقفًا، لكن قناة موثوقة مثل WhatsApp ما زالت تستقبل الأوامر.

أمر النص المدعوم:

  * `/crestodian <request>`


تدفق المشغّل:

textCopy code
[code]
    You, in a trusted owner DM: /crestodian statusOpenClaw: Crestodian rescue mode. Gateway reachable: no. Config valid: no.You: /crestodian restart gatewayOpenClaw: Plan: restart the Gateway. Reply /crestodian yes to apply.You: /crestodian yesOpenClaw: Applied. Audit entry written.
[/code]

يمكن أيضًا وضع إنشاء الوكلاء في قائمة انتظار من الموجّه المحلي أو وضع الإنقاذ:

textCopy code
[code]
    create agent work workspace ~/Projects/work model openai/gpt-5.5/crestodian create agent work workspace ~/Projects/work
[/code]

وضع الإنقاذ البعيد سطح إداري. يجب التعامل معه كإصلاح تهيئة بعيد، وليس كمحادثة عادية.

عقد الأمان للإنقاذ البعيد:

  * معطّل عندما تكون العزلية نشطة. إذا كان وكيل/جلسة معزولًا، يجب أن يرفض Crestodian الإنقاذ البعيد ويوضح أن إصلاح CLI المحلي مطلوب.
  * الحالة الفعالة الافتراضية هي `auto`: السماح بالإنقاذ البعيد فقط في تشغيل YOLO موثوق، حيث تمتلك بيئة التشغيل أصلًا صلاحية محلية غير معزولة.
  * يتطلب هوية مالك صريحة. يجب ألا يقبل الإنقاذ قواعد مرسل بدل شامل، أو سياسة مجموعة مفتوحة، أو webhooks غير موثقة، أو قنوات مجهولة.
  * رسائل المالك المباشرة فقط افتراضيًا. يتطلب إنقاذ المجموعات/القنوات اشتراكًا صريحًا.
  * البحث عن الإضافات وسردها للقراءة فقط. تثبيت الإضافات محلي فقط افتراضيًا لأنه ينزّل شيفرة قابلة للتنفيذ. يمكن السماح بإلغاء تثبيت الإضافات كعملية إصلاح معتمدة عندما تسمح سياسة الإنقاذ بعمليات الكتابة الدائمة.
  * لا يستطيع الإنقاذ البعيد فتح TUI المحلي أو التبديل إلى جلسة وكيل تفاعلية. استخدم `openclaw` المحلي لتسليم الوكيل.
  * لا تزال عمليات الكتابة الدائمة تتطلب موافقة، حتى في وضع الإنقاذ.
  * دقّق كل عملية إنقاذ مطبقة. يسجل إنقاذ قناة الرسائل بيانات وصفية للقناة، والحساب، والمرسل، وعنوان المصدر. وتسجل العمليات التي تغيّر التهيئة أيضًا تجزئات التهيئة قبل وبعد.
  * لا تردد الأسرار مطلقًا. يجب أن يبلّغ فحص SecretRef عن التوفر، لا القيم.
  * إذا كان Gateway حيًا، ففضّل عمليات Gateway المُنمَّطة. إذا كان Gateway متوقفًا، فاستخدم فقط سطح الإصلاح المحلي الأدنى الذي لا يعتمد على حلقة الوكيل العادية.


شكل التهيئة:

jsoncCopy code
[code]
    {  "crestodian": {    "rescue": {      "enabled": "auto",      "ownerDmOnly": true,    },  },}
[/code]

يجب أن يقبل `enabled`:

  * `"auto"`: الافتراضي. السماح فقط عندما تكون بيئة التشغيل الفعالة YOLO والعزلية متوقفة.
  * `false`: عدم السماح مطلقًا بالإنقاذ عبر قناة الرسائل.
  * `true`: السماح صراحةً بالإنقاذ عندما تنجح فحوص المالك/القناة. هذا لا يزال يجب ألا يتجاوز رفض العزلية.


وضعية YOLO الافتراضية لـ `"auto"` هي:

  * يتحول وضع العزل إلى `off`
  * يتحول `tools.exec.security` إلى `full`
  * يتحول `tools.exec.ask` إلى `off`


يغطي مسار Docker الإنقاذ البعيد:

bashCopy code
[code]
    pnpm test:docker:crestodian-rescue
[/code]

تتم تغطية رجوع المخطِّط المحلي بلا تهيئة بواسطة:

bashCopy code
[code]
    pnpm test:docker:crestodian-planner
[/code]

يفحص اختبار smoke مباشر اختياري لسطح أوامر القناة `/crestodian status` بالإضافة إلى رحلة موافقة دائمة ذهابًا وإيابًا عبر معالج الإنقاذ:

bashCopy code
[code]
    pnpm test:live:crestodian-rescue-channel
[/code]

تتم تغطية الإعداد الجديد بلا تهيئة عبر Crestodian بواسطة:

bashCopy code
[code]
    pnpm test:docker:crestodian-first-run
[/code]

يبدأ ذلك المسار بدليل حالة فارغ، ويوجه `openclaw` المجرد إلى Crestodian، ويضبط النموذج الافتراضي، وينشئ وكيلًا إضافيًا، ويهيّئ Discord عبر تمكين إضافة مع SecretRef للرمز، ويتحقق من التهيئة، ويفحص سجل التدقيق. لدى QA Lab أيضًا سيناريو مدعومًا بالمستودع لتدفق Ring 0 نفسه:

bashCopy code
[code]
    pnpm openclaw qa suite --scenario crestodian-ring-zero-setup
[/code]

## ذات صلة

  * [مرجع CLI](</ar/cli>)
  * [Doctor](</ar/cli/doctor>)
  * [TUI](</ar/cli/tui>)
  * [Sandbox](</ar/cli/sandbox>)
  * [الأمان](</ar/cli/security>)


Was this useful?YesNo