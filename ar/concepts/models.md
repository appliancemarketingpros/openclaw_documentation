---
title: واجهة CLI للنماذج
source_url: https://docs.openclaw.ai/ar/concepts/models
scraped_at: 2026-05-25
---

[**تجاوز فشل النموذج** تدوير ملفات تعريف المصادقة، وفترات التهدئة، وكيفية تفاعل ذلك مع البدائل. ](</ar/concepts/model-failover>) [**موفرو النماذج** نظرة عامة سريعة على الموفر وأمثلة. ](</ar/concepts/model-providers>) [**تشغيلات الوكلاء** PI وCodex وتشغيلات حلقات الوكلاء الأخرى. ](</ar/concepts/agent-runtimes>) [**مرجع التكوين** مفاتيح تكوين النموذج. ](</ar/gateway/config-agents#agent-defaults>)

تختار مراجع النماذج موفرًا ونموذجًا. وهي عادةً لا تختار تشغيل الوكيل منخفض المستوى. مراجع وكلاء OpenAI هي الاستثناء الرئيسي: يعمل `openai/gpt-5.5` عبر تشغيل خادم تطبيق Codex افتراضيًا على موفر OpenAI الرسمي. تنتمي تجاوزات التشغيل الصريحة إلى سياسة الموفر/النموذج، لا إلى الوكيل أو الجلسة بالكامل. في وضع تشغيل Codex، لا يعني مرجع `openai/gpt-*` الفوترة عبر مفتاح API؛ يمكن أن تأتي المصادقة من حساب Codex أو ملف تعريف مصادقة `openai-codex`. راجع [تشغيلات الوكلاء](</ar/concepts/agent-runtimes>).

## كيف يعمل اختيار النموذج

يختار OpenClaw النماذج بهذا الترتيب:

* ### النموذج الأساسي

`agents.defaults.model.primary` (أو `agents.defaults.model`).

* ### البدائل

`agents.defaults.model.fallbacks` (بالترتيب).

* ### تجاوز فشل مصادقة الموفر

يحدث تجاوز فشل المصادقة داخل الموفر قبل الانتقال إلى النموذج التالي.

أسطح النماذج ذات الصلة

  * `agents.defaults.models` هي قائمة السماح/فهرس النماذج التي يستطيع OpenClaw استخدامها (بالإضافة إلى الأسماء المستعارة). استخدم إدخالات `provider/*` لتقييد الموفرين المرئيين مع إبقاء اكتشاف الموفر ديناميكيًا.
  * يُستخدم `agents.defaults.imageModel` **فقط عندما** لا يستطيع النموذج الأساسي قبول الصور.
  * يُستخدم `agents.defaults.pdfModel` بواسطة أداة `pdf`. إذا حُذف، تعود الأداة إلى `agents.defaults.imageModel`، ثم نموذج الجلسة/النموذج الافتراضي المحسوم.
  * يُستخدم `agents.defaults.imageGenerationModel` بواسطة قدرة توليد الصور المشتركة. إذا حُذف، يمكن لـ `image_generate` مع ذلك استنتاج افتراضي لموفر مدعوم بالمصادقة. يحاول الموفر الافتراضي الحالي أولًا، ثم بقية موفري توليد الصور المسجلين بترتيب معرّف الموفر. إذا عيّنت موفرًا/نموذجًا محددًا، فاضبط أيضًا مصادقة ذلك الموفر/مفتاح API الخاص به.
  * يُستخدم `agents.defaults.musicGenerationModel` بواسطة قدرة توليد الموسيقى المشتركة. إذا حُذف، يمكن لـ `music_generate` مع ذلك استنتاج افتراضي لموفر مدعوم بالمصادقة. يحاول الموفر الافتراضي الحالي أولًا، ثم بقية موفري توليد الموسيقى المسجلين بترتيب معرّف الموفر. إذا عيّنت موفرًا/نموذجًا محددًا، فاضبط أيضًا مصادقة ذلك الموفر/مفتاح API الخاص به.
  * يُستخدم `agents.defaults.videoGenerationModel` بواسطة قدرة توليد الفيديو المشتركة. إذا حُذف، يمكن لـ `video_generate` مع ذلك استنتاج افتراضي لموفر مدعوم بالمصادقة. يحاول الموفر الافتراضي الحالي أولًا، ثم بقية موفري توليد الفيديو المسجلين بترتيب معرّف الموفر. إذا عيّنت موفرًا/نموذجًا محددًا، فاضبط أيضًا مصادقة ذلك الموفر/مفتاح API الخاص به.
  * يمكن للافتراضيات الخاصة بكل وكيل تجاوز `agents.defaults.model` عبر `agents.list[].model` بالإضافة إلى الارتباطات (راجع [توجيه الوكلاء المتعددين](</ar/concepts/multi-agent>)).


## مصدر الاختيار وسلوك البدائل

يمكن أن يعني نفس `provider/model` أشياء مختلفة حسب مصدره:

  * الافتراضيات المضبوطة (`agents.defaults.model.primary` والأساسيات الخاصة بالوكلاء) هي نقطة البداية المعتادة وتستخدم `agents.defaults.model.fallbacks`.
  * اختيارات البديل التلقائي هي حالة استرداد مؤقتة. تُخزن مع `modelOverrideSource: "auto"` حتى تتمكن المنعطفات اللاحقة من متابعة استخدام سلسلة البدائل دون اختبار نموذج أساسي معروف التعطل أولًا.
  * اختيارات جلسة المستخدم دقيقة. تخزن `/model`، ومنتقي النموذج، و`session_status(model=...)`، و`sessions.patch` القيمة `modelOverrideSource: "user"`؛ إذا تعذر الوصول إلى ذلك الموفر/النموذج المحدد، يفشل OpenClaw بشكل ظاهر بدلًا من الانتقال إلى نموذج آخر مضبوط.
  * يُعد Cron `--model` / حمولة `model` نموذجًا أساسيًا لكل مهمة. ولا يزال يستخدم البدائل المضبوطة إلا إذا وفرت المهمة حمولة `fallbacks` صريحة (استخدم `fallbacks: []` لتشغيل cron صارم).
  * تحترم منتقيات النموذج الافتراضي وقائمة السماح في CLI القيمة `models.mode: "replace"` عبر سرد `models.providers.*.models` الصريحة بدلًا من تحميل الفهرس المدمج الكامل.
  * يطلب منتقي النماذج في واجهة التحكم من Gateway عرض النموذج المضبوط لديه: `agents.defaults.models` عند وجوده، بما في ذلك إدخالات `provider/*` على مستوى الموفر، وإلا `models.providers.*.models` الصريحة بالإضافة إلى الموفرين ذوي المصادقة القابلة للاستخدام. يُحجز الفهرس المدمج الكامل لعروض التصفح الصريحة مثل `models.list` مع `view: "all"` أو `openclaw models list --all`.


## سياسة نموذج سريعة

  * اضبط النموذج الأساسي على أقوى نموذج من أحدث جيل متاح لك.
  * استخدم البدائل للمهام الحساسة للتكلفة/زمن الاستجابة والمحادثات الأقل خطورة.
  * بالنسبة إلى الوكلاء الممكّنين بالأدوات أو المدخلات غير الموثوقة، تجنب طبقات النماذج الأقدم/الأضعف.


## الإعداد الأولي (موصى به)

إذا لم ترغب في تعديل التكوين يدويًا، شغّل الإعداد الأولي:

bashCopy code
[code]
    openclaw onboard
[/code]

يمكنه إعداد النموذج + المصادقة للموفرين الشائعين، بما في ذلك **اشتراك OpenAI Code (Codex)** ‏(OAuth) و**Anthropic** (مفتاح API أو Claude CLI).

## مفاتيح التكوين (نظرة عامة)

  * `agents.defaults.model.primary` و`agents.defaults.model.fallbacks`
  * `agents.defaults.imageModel.primary` و`agents.defaults.imageModel.fallbacks`
  * `agents.defaults.pdfModel.primary` و`agents.defaults.pdfModel.fallbacks`
  * `agents.defaults.imageGenerationModel.primary` و`agents.defaults.imageGenerationModel.fallbacks`
  * `agents.defaults.videoGenerationModel.primary` و`agents.defaults.videoGenerationModel.fallbacks`
  * `agents.defaults.models` (قائمة السماح + الأسماء المستعارة + معاملات الموفر + إدخالات الموفر الديناميكية `provider/*`)
  * `models.providers` (موفرون مخصصون مكتوبون في `models.json`)


### تعديلات قائمة السماح الآمنة

استخدم الكتابات الإضافية عند تحديث `agents.defaults.models` يدويًا:

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --merge
[/code]

قواعد الحماية من الاستبدال

يحمي `openclaw config set` خرائط النماذج/الموفرين من الاستبدال العرضي. يُرفض إسناد كائن عادي إلى `agents.defaults.models` أو `models.providers` أو `models.providers.<id>.models` عندما يؤدي إلى إزالة إدخالات موجودة. استخدم `--merge` للتغييرات الإضافية؛ استخدم `--replace` فقط عندما ينبغي أن تصبح القيمة المقدمة هي القيمة الهدف الكاملة.

يدمج إعداد الموفر التفاعلي و`openclaw configure --section model` أيضًا الاختيارات ذات نطاق الموفر في قائمة السماح الموجودة، لذلك لا تؤدي إضافة Codex أو Ollama أو موفر آخر إلى إسقاط إدخالات نماذج غير ذات صلة. يحافظ Configure على `agents.defaults.model.primary` موجود عند إعادة تطبيق مصادقة الموفر. أوامر تعيين الافتراضي الصريحة مثل `openclaw models auth login --provider <id> --set-default` و`openclaw models set <model>` لا تزال تستبدل `agents.defaults.model.primary`.

## "النموذج غير مسموح به" (ولماذا تتوقف الردود)

إذا عُيّن `agents.defaults.models`، فإنه يصبح **قائمة السماح** لـ `/model` ولتجاوزات الجلسة. عندما يختار المستخدم نموذجًا غير موجود في قائمة السماح تلك، يعيد OpenClaw:

CodeCopy code
[code]
    Model "provider/model" is not allowed. Use /models to list providers, or /models <provider> to list models.Add it with: openclaw config set agents.defaults.models '{"provider/model":{}}' --strict-json --merge
[/code]

عندما يتضمن الأمر المرفوض تجاوز تشغيل مثل `/model openai/gpt-5.5 --runtime codex`، أصلح قائمة السماح أولًا، ثم أعد محاولة الأمر نفسه `/model ... --runtime ...`. بالنسبة إلى تنفيذ Codex الأصلي، يظل النموذج المحدد هو `openai/gpt-5.5`؛ يحدد تشغيل `codex` الحزمة ويستخدم مصادقة Codex بشكل منفصل.

بالنسبة إلى النماذج المحلية/GGUF، خزّن المرجع الكامل المسبوق بالموفر في قائمة السماح، على سبيل المثال `ollama/gemma4:26b` أو `lmstudio/Gemma4-26b-a4-it-gguf` أو الموفر/النموذج الدقيق المعروض بواسطة `openclaw models list --provider <provider>`. أسماء الملفات المحلية المجردة أو أسماء العرض ليست كافية عندما تكون قائمة السماح نشطة.

إذا أردت تقييد الموفرين دون سرد كل نموذج يدويًا، فأضف إدخالات `provider/*` إلى `agents.defaults.models`:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai-codex/*": {},        "vllm/*": {},      },    },  },}
[/code]

مع هذه السياسة، يعرض `/model` و`/models` ومنتقيات النماذج الفهرس المكتشف لهؤلاء الموفرين فقط. يمكن أن تظهر نماذج جديدة من الموفرين المحددين دون تعديل قائمة السماح. يمكن مزج إدخالات `provider/model` الدقيقة مع إدخالات `provider/*` عندما تحتاج إلى نموذج محدد واحد من موفر آخر.

مثال على تكوين قائمة السماح:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-sonnet-4-6" },      models: {        "anthropic/claude-sonnet-4-6": { alias: "Sonnet" },        "anthropic/claude-opus-4-6": { alias: "Opus" },      },    },  },}
[/code]

## تبديل النماذج في المحادثة (`/model`)

يمكنك تبديل النماذج للجلسة الحالية دون إعادة التشغيل:

CodeCopy code
[code]
    /model/model list/model 3/model openai/gpt-5.4/model status
[/code]

سلوك المنتقي

  * `/model` (و`/model list`) هو منتقي مدمج ومرقم (عائلة النموذج + الموفرون المتاحون).
  * على Discord، يفتح `/model` و`/models` منتقيًا تفاعليًا يحتوي على قوائم منسدلة للموفر والنموذج بالإضافة إلى خطوة إرسال.
  * على Telegram، تكون اختيارات منتقي `/models` محددة بنطاق الجلسة؛ ولا تغيّر الافتراضي الدائم للوكيل في `openclaw.json`.
  * أصبح `/models add` مهمَلًا ويعيد الآن رسالة إهمال بدلًا من تسجيل النماذج من المحادثة.
  * يختار `/model <#>` من ذلك المنتقي.

الاستمرارية والتبديل المباشر

  * يحفظ `/model` اختيار الجلسة الجديد فورًا.
  * إذا كان الوكيل خاملًا، يستخدم التشغيل التالي النموذج الجديد مباشرة.
  * إذا كان تشغيل نشطًا بالفعل، يضع OpenClaw علامة على التبديل المباشر كقيد الانتظار ولا يعيد التشغيل إلى النموذج الجديد إلا عند نقطة إعادة محاولة نظيفة.
  * إذا كان نشاط الأداة أو خرج الرد قد بدأ بالفعل، فقد يبقى التبديل المعلّق في الصف حتى فرصة إعادة محاولة لاحقة أو منعطف المستخدم التالي.
  * مرجع `/model` المحدد من المستخدم صارم لتلك الجلسة: إذا تعذر الوصول إلى الموفر/النموذج المحدد، يفشل الرد بشكل ظاهر بدلًا من الإجابة بصمت من `agents.defaults.model.fallbacks`. يختلف هذا عن الافتراضيات المضبوطة والأساسيات الخاصة بمهام cron، التي لا يزال بإمكانها استخدام سلاسل البدائل.
  * `/model status` هو العرض التفصيلي (مرشحو المصادقة، وعند ضبطه، `baseUrl` لنقطة نهاية الموفر + وضع `api`).

Ref parsing

  * تُحلَّل مراجع النماذج عبر التقسيم عند **أول** `/`. استخدم `provider/model` عند كتابة `/model <ref>`.
  * إذا كان معرّف النموذج نفسه يحتوي على `/` (بأسلوب OpenRouter)، فيجب تضمين بادئة المزوّد (مثال: `/model openrouter/moonshotai/kimi-k2`).
  * إذا حذفت المزوّد، فإن OpenClaw يحلّ الإدخال بهذا الترتيب: 
    1. تطابق الاسم المستعار
    2. تطابق فريد لمزوّد مهيأ مع معرّف النموذج غير المسبوق نفسه تمامًا
    3. رجوع احتياطي مهمل إلى المزوّد الافتراضي المهيأ — إذا لم يعد ذلك المزوّد يوفّر النموذج الافتراضي المهيأ، فإن OpenClaw يرجع بدلًا من ذلك إلى أول مزوّد/نموذج مهيأ لتجنب إظهار إعداد افتراضي قديم لمزوّد أُزيل.


السلوك/التكوين الكامل للأمر: [أوامر الشرطة المائلة](</ar/tools/slash-commands>).

## أوامر CLI

bashCopy code
[code]
    openclaw models listopenclaw models statusopenclaw models set <provider/model>openclaw models set-image <provider/model> openclaw models aliases listopenclaw models aliases add <alias> <provider/model>openclaw models aliases remove <alias> openclaw models fallbacks listopenclaw models fallbacks add <provider/model>openclaw models fallbacks remove <provider/model>openclaw models fallbacks clear openclaw models image-fallbacks listopenclaw models image-fallbacks add <provider/model>openclaw models image-fallbacks remove <provider/model>openclaw models image-fallbacks clear
[/code]

`openclaw models` (بلا أمر فرعي) اختصار لـ `models status`.

### `models list`

يعرض افتراضيًا النماذج المهيأة/المتاحة عبر المصادقة. علامات مفيدة:

الفهرس الكامل. يتضمن صفوف الفهرس الثابتة المملوكة للمزوّد والمضمّنة قبل تهيئة المصادقة، لذا يمكن لطرق العرض المخصصة للاستكشاف فقط إظهار نماذج غير متاحة إلى أن تضيف بيانات اعتماد المزوّد المطابقة.

المزوّدون المحليون فقط.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tcHJvdmlkZXIgPGlk " type="string"> التصفية حسب معرّف المزوّد، مثل `moonshot`. لا تُقبل تسميات العرض من أدوات الاختيار التفاعلية.

نموذج واحد في كل سطر.

خرج قابل للقراءة آليًا.

### `models status`

يعرض النموذج الأساسي المحلول، وخيارات الرجوع الاحتياطية، ونموذج الصور، ونظرة عامة على مصادقة المزوّدين المهيئين. كما يُظهر حالة انتهاء صلاحية OAuth للملفات الشخصية الموجودة في مخزن المصادقة (يحذّر افتراضيًا خلال 24 ساعة). يطبع `--plain` النموذج الأساسي المحلول فقط.

Auth and probe behavior

  * تُعرض حالة OAuth دائمًا (وتُضمَّن في خرج `--json`). إذا لم تكن لدى مزوّد مهيأ بيانات اعتماد، يطبع `models status` قسم **مصادقة مفقودة**.
  * يتضمن JSON ‏`auth.oauth` (نافذة التحذير + الملفات الشخصية) و`auth.providers` (المصادقة الفعلية لكل مزوّد، بما في ذلك بيانات الاعتماد المدعومة بالبيئة). `auth.oauth` هو صحة ملفات مخزن المصادقة الشخصية فقط؛ ولا تظهر فيه المزوّدات المعتمدة على البيئة فقط.
  * استخدم `--check` للأتمتة (رمز الخروج `1` عند الفقدان/انتهاء الصلاحية، و`2` عند قرب انتهاء الصلاحية).
  * استخدم `--probe` لفحوصات المصادقة الحية؛ يمكن أن تأتي صفوف الفحص من ملفات المصادقة الشخصية، أو بيانات اعتماد البيئة، أو `models.json`.
  * إذا حذف `auth.order.<provider>` الصريح ملفًا شخصيًا مخزنًا، يبلغ الفحص عن `excluded_by_auth_order` بدلًا من تجربته. إذا كانت المصادقة موجودة ولكن لا يمكن حل نموذج قابل للفحص لذلك المزوّد، يبلغ الفحص عن `status: no_model`.


مثال (Claude CLI):

bashCopy code
[code]
    claude auth loginopenclaw models status
[/code]

## الفحص (نماذج OpenRouter المجانية)

يفحص `openclaw models scan` **فهرس النماذج المجانية** في OpenRouter ويمكنه اختياريًا فحص النماذج لدعم الأدوات والصور.

تخطَّ الفحوصات الحية (بيانات وصفية فقط).

اضبط `agents.defaults.model.primary` على أول اختيار.

اضبط `agents.defaults.imageModel.primary` على أول اختيار للصور.

تُرتَّب نتائج الفحص حسب:

  1. دعم الصور
  2. زمن استجابة الأدوات
  3. حجم السياق
  4. عدد المعلمات


الإدخال:

  * قائمة OpenRouter ‏`/models` (مرشّح `:free`)
  * تتطلب الفحوصات الحية مفتاح OpenRouter API من ملفات المصادقة الشخصية أو `OPENROUTER_API_KEY` (راجع [متغيرات البيئة](</ar/help/environment>))
  * مرشحات اختيارية: `--max-age-days`، و`--min-params`، و`--provider`، و`--max-candidates`
  * عناصر التحكم في الطلب/الفحص: `--timeout`، و`--concurrency`


عند تشغيل الفحوصات الحية في TTY، يمكنك تحديد خيارات الرجوع الاحتياطية تفاعليًا. في الوضع غير التفاعلي، مرّر `--yes` لقبول الإعدادات الافتراضية. نتائج البيانات الوصفية فقط معلوماتية؛ وتتطلب `--set-default` و`--set-image` فحوصات حية حتى لا يهيئ OpenClaw نموذج OpenRouter غير قابل للاستخدام بلا مفتاح.

## سجل النماذج (`models.json`)

تُكتب المزوّدات المخصصة في `models.providers` إلى `models.json` ضمن دليل الوكيل (الافتراضي `~/.openclaw/agents/<agentId>/agent/models.json`). يُدمج هذا الملف افتراضيًا ما لم تُضبط `models.mode` على `replace`.

Merge mode precedence

أسبقية وضع الدمج لمعرّفات المزوّدين المتطابقة:

  * يفوز `baseUrl` غير الفارغ الموجود بالفعل في `models.json` الخاص بالوكيل.
  * يفوز `apiKey` غير الفارغ في `models.json` الخاص بالوكيل فقط عندما لا يكون ذلك المزوّد مُدارًا بواسطة SecretRef في سياق التكوين/ملف المصادقة الشخصي الحالي.
  * تُحدَّث قيم `apiKey` للمزوّدين المدارين بواسطة SecretRef من علامات المصدر (`ENV_VAR_NAME` لمراجع البيئة، و`secretref-managed` لمراجع الملف/التنفيذ) بدلًا من حفظ الأسرار المحلولة.
  * تُحدَّث قيم ترويسات المزوّدين المدارين بواسطة SecretRef من علامات المصدر (`secretref-env:ENV_VAR_NAME` لمراجع البيئة، و`secretref-managed` لمراجع الملف/التنفيذ).
  * يرجع `apiKey`/`baseUrl` الفارغ أو المفقود في الوكيل إلى `models.providers` في التكوين.
  * تُحدَّث حقول المزوّد الأخرى من التكوين وبيانات الفهرس المطبّعة.


## ذو صلة

  * [بيئات تشغيل الوكلاء](</ar/concepts/agent-runtimes>) — PI وCodex وبيئات تشغيل حلقات وكلاء أخرى
  * [مرجع التكوين](</ar/gateway/config-agents#agent-defaults>) — مفاتيح تكوين النماذج
  * [توليد الصور](</ar/tools/image-generation>) — تكوين نموذج الصور
  * [تجاوز فشل النموذج](</ar/concepts/model-failover>) — سلاسل الرجوع الاحتياطي
  * [مزوّدو النماذج](</ar/concepts/model-providers>) — توجيه المزوّدين والمصادقة
  * [توليد الموسيقى](</ar/tools/music-generation>) — تكوين نموذج الموسيقى
  * [توليد الفيديو](</ar/tools/video-generation>) — تكوين نموذج الفيديو


Was this useful?YesNo