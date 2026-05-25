---
title: Gateway
source_url: https://docs.openclaw.ai/ar/cli/gateway
scraped_at: 2026-05-25
---

Gateway هو خادم WebSocket الخاص بـ OpenClaw (القنوات، العقد، الجلسات، الخطافات). تعيش الأوامر الفرعية في هذه الصفحة تحت `openclaw gateway …`.

[**اكتشاف Bonjour** إعداد mDNS محلي + DNS-SD واسع النطاق. ](</ar/gateway/bonjour>) [**نظرة عامة على الاكتشاف** كيف يعلن OpenClaw عن البوابات ويعثر عليها. ](</ar/gateway/discovery>) [**التكوين** مفاتيح تكوين Gateway على المستوى الأعلى. ](</ar/gateway/configuration>)

## تشغيل Gateway

شغّل عملية Gateway محلية:

bashCopy code
[code]
    openclaw gateway
[/code]

الاسم المستعار للتشغيل في المقدمة:

bashCopy code
[code]
    openclaw gateway run
[/code]

سلوك بدء التشغيل

  * افتراضيًا، ترفض Gateway البدء ما لم يتم تعيين `gateway.mode=local` في `~/.openclaw/openclaw.json`. استخدم `--allow-unconfigured` للتشغيلات المؤقتة/التطويرية.
  * من المتوقع أن يكتب `openclaw onboard --mode local` و`openclaw setup` القيمة `gateway.mode=local`. إذا كان الملف موجودًا لكن `gateway.mode` مفقود، فتعامل مع ذلك كتكوين معطوب أو مستبدل وأصلحه بدلًا من افتراض الوضع المحلي ضمنيًا.
  * إذا كان الملف موجودًا و`gateway.mode` مفقودًا، تتعامل Gateway مع ذلك كضرر مشبوه في التكوين وترفض "تخمين المحلي" نيابةً عنك.
  * يُحظر الربط خارج loopback دون مصادقة (حاجز أمان).
  * يطلق `SIGUSR1` إعادة تشغيل داخل العملية عندما يكون ذلك مصرحًا به (`commands.restart` مفعّل افتراضيًا؛ عيّن `commands.restart: false` لحظر إعادة التشغيل اليدوية، مع بقاء تطبيق/تحديث أداة Gateway/التكوين مسموحًا).
  * توقف معالجات `SIGINT`/`SIGTERM` عملية gateway، لكنها لا تستعيد أي حالة طرفية مخصصة. إذا لففت CLI باستخدام TUI أو إدخال raw-mode، فاستعد الطرفية قبل الخروج.


### الخيارات

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tcG9ydCA8cG9ydA " type="number"> منفذ WebSocket (تأتي القيمة الافتراضية من التكوين/البيئة؛ عادةً `18789`).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tdG9rZW4gPHRva2Vu " type="string"> تجاوز الرمز المميز (يضبط أيضًا `OPENCLAW_GATEWAY_TOKEN` للعملية).

إعادة ضبط تكوين serve/funnel في Tailscale عند إيقاف التشغيل.

السماح ببدء gateway دون `gateway.mode=local` في التكوين. يتجاوز حاجز بدء التشغيل للتمهيد المؤقت/التطويري فقط؛ ولا يكتب ملف التكوين أو يصلحه.

إنشاء تكوين تطوير + مساحة عمل إذا كانت مفقودة (يتخطى [BOOTSTRAP.md](<http://BOOTSTRAP.md>)).

إعادة ضبط تكوين التطوير + بيانات الاعتماد + الجلسات + مساحة العمل (يتطلب `--dev`).

إنهاء أي مستمع موجود على المنفذ المحدد قبل البدء.

سجلات تفصيلية.

عرض سجلات خلفية CLI فقط في وحدة التحكم (وتفعيل stdout/stderr).

اسم مستعار لـ `--ws-log compact`.

تسجيل أحداث دفق النموذج الخام إلى jsonl.

## إعادة تشغيل Gateway

bashCopy code
[code]
    openclaw gateway restartopenclaw gateway restart --safeopenclaw gateway restart --safe --skip-deferralopenclaw gateway restart --force
[/code]

يطلب `openclaw gateway restart --safe` من Gateway العاملة إجراء فحص تمهيدي لأعمال OpenClaw النشطة قبل إعادة التشغيل. إذا كانت هناك عمليات في الطابور، أو تسليم ردود، أو تشغيلات مضمّنة، أو تشغيلات مهام نشطة، فتبلغ Gateway عن العوائق، وتدمج طلبات إعادة التشغيل الآمنة المكررة، وتعيد التشغيل عندما ينضب العمل النشط. يحافظ `restart` العادي على سلوك مدير الخدمة الحالي للتوافق. استخدم `--force` فقط عندما تريد صراحةً مسار التجاوز الفوري.

ينفذ `openclaw gateway restart --safe --skip-deferral` إعادة التشغيل المنسقة نفسها والواعية بـ OpenClaw مثل `--safe`، لكنه يتجاوز بوابة تأجيل العمل النشط بحيث تصدر Gateway إعادة التشغيل فورًا حتى عند الإبلاغ عن عوائق. استخدمه كمخرج طوارئ للمشغّل عندما يكون التأجيل مثبتًا بسبب تشغيل مهمة عالق وكان `--safe` وحده سينتظر إلى أجل غير مسمى. يتطلب `--skip-deferral` الخيار `--safe`.

### توصيف بدء التشغيل

  * اضبط `OPENCLAW_GATEWAY_STARTUP_TRACE=1` لتسجيل توقيتات المراحل أثناء بدء Gateway، بما في ذلك تأخير `eventLoopMax` لكل مرحلة وتوقيتات جداول بحث Plugin للفهرس المثبت، وسجل manifest، وتخطيط بدء التشغيل، وعمل خريطة المالكين.
  * اضبط `OPENCLAW_DIAGNOSTICS=timeline` مع `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=<path>` لكتابة مخطط زمني لتشخيصات بدء التشغيل بصيغة JSONL وبأفضل جهد لحزم QA الخارجية. يمكنك أيضًا تفعيل العلم باستخدام `diagnostics.flags: ["timeline"]` في التكوين؛ يظل المسار مقدمًا من البيئة. أضف `OPENCLAW_DIAGNOSTICS_EVENT_LOOP=1` لتضمين عينات حلقة الأحداث.
  * شغّل `pnpm test:startup:gateway -- --runs 5 --warmup 1` لقياس أداء بدء Gateway. يسجل المعيار أول خرج للعملية، و`/healthz`، و`/readyz`، وتوقيتات تتبع بدء التشغيل، وتأخير حلقة الأحداث، وتفاصيل توقيت جدول بحث Plugin.


## الاستعلام عن Gateway عاملة

تستخدم جميع أوامر الاستعلام WebSocket RPC.

### أوضاع الإخراج

  * الافتراضي: قابل للقراءة البشرية (ملون في TTY).
  * `--json`: JSON قابل للقراءة آليًا (دون تنسيق/مؤشر تحميل).
  * `--no-color` (أو `NO_COLOR=1`): تعطيل ANSI مع الحفاظ على التخطيط البشري.


### الخيارات المشتركة

  * `--url <url>`: عنوان URL لـ WebSocket الخاص بـ Gateway.
  * `--token <token>`: رمز Gateway المميز.
  * `--password <password>`: كلمة مرور Gateway.
  * `--timeout <ms>`: المهلة/الميزانية (تختلف حسب الأمر).
  * `--expect-final`: انتظار استجابة "final" (استدعاءات الوكيل).


### `gateway health`

bashCopy code
[code]
    openclaw gateway health --url ws://127.0.0.1:18789
[/code]

نقطة نهاية HTTP `/healthz` هي فحص حيوية: تعود بمجرد أن يتمكن الخادم من الرد عبر HTTP. نقطة نهاية HTTP `/readyz` أكثر صرامة وتبقى حمراء بينما لا تزال ملحقات Plugin الجانبية عند بدء التشغيل أو القنوات أو الخطافات المكوّنة تستقر. تتضمن استجابات الجاهزية التفصيلية المحلية أو المصادق عليها كتلة تشخيص `eventLoop` مع تأخير حلقة الأحداث، واستخدام حلقة الأحداث، ونسبة أنوية CPU، وعلم `degraded`.

### `gateway usage-cost`

جلب ملخصات تكلفة الاستخدام من سجلات الجلسات.

bashCopy code
[code]
    openclaw gateway usage-costopenclaw gateway usage-cost --days 7openclaw gateway usage-cost --json
[/code]

### `gateway stability`

جلب مسجل الاستقرار التشخيصي الحديث من Gateway عاملة.

bashCopy code
[code]
    openclaw gateway stabilityopenclaw gateway stability --type payload.largeopenclaw gateway stability --bundle latestopenclaw gateway stability --bundle latest --exportopenclaw gateway stability --json
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tbGltaXQgPGxpbWl0 " type="number" default="25"> الحد الأقصى لعدد الأحداث الحديثة المراد تضمينها (الحد الأقصى `1000`).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tdHlwZSA8dHlwZQ " type="string"> التصفية حسب نوع حدث التشخيص، مثل `payload.large` أو `diagnostic.memory.pressure`.

قراءة حزمة استقرار مستمرة بدلًا من استدعاء Gateway العاملة. استخدم `--bundle latest` (أو فقط `--bundle`) لأحدث حزمة ضمن دليل الحالة، أو مرّر مسار JSON لحزمة مباشرةً.

كتابة ملف zip لتشخيصات دعم قابل للمشاركة بدلًا من طباعة تفاصيل الاستقرار.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tb3V0cHV0IDxwYXRo " type="string"> مسار الإخراج لـ `--export`.

الخصوصية وسلوك الحزم

  * تحتفظ السجلات بالبيانات الوصفية التشغيلية: أسماء الأحداث، والعدادات، وأحجام البايت، وقراءات الذاكرة، وحالة الطابور/الجلسة، وأسماء القنوات/Plugin، وملخصات الجلسات المنقحة. ولا تحتفظ بنص الدردشة، أو أجسام Webhook، أو مخرجات الأدوات، أو أجسام الطلبات أو الاستجابات الخام، أو الرموز المميزة، أو ملفات تعريف الارتباط، أو القيم السرية، أو أسماء المضيفين، أو معرّفات الجلسات الخام. عيّن `diagnostics.enabled: false` لتعطيل المسجل بالكامل.
  * عند مخارج Gateway الفادحة، ومهل إيقاف التشغيل، وفشل بدء التشغيل بعد إعادة التشغيل، يكتب OpenClaw اللقطة التشخيصية نفسها إلى `~/.openclaw/logs/stability/openclaw-stability-*.json` عندما يحتوي المسجل على أحداث. افحص أحدث حزمة باستخدام `openclaw gateway stability --bundle latest`؛ وتنطبق أيضًا `--limit` و`--type` و`--since-seq` على إخراج الحزمة.


### `gateway diagnostics export`

اكتب ملف zip محليًا للتشخيصات مصممًا لإرفاقه بتقارير الأخطاء. لنموذج الخصوصية ومحتويات الحزمة، راجع [تصدير التشخيصات](</ar/gateway/diagnostics>).

bashCopy code
[code]
    openclaw gateway diagnostics exportopenclaw gateway diagnostics export --output openclaw-diagnostics.zipopenclaw gateway diagnostics export --json
[/code]

تخطي البحث عن حزمة الاستقرار المستمرة.

طباعة المسار المكتوب، والحجم، والبيان بصيغة JSON.

يحتوي التصدير على بيان، وملخص Markdown، وشكل التكوين، وتفاصيل تكوين منقحة، وملخصات سجلات منقحة، ولقطات حالة/صحة Gateway منقحة، وأحدث حزمة استقرار عند وجودها.

وهو مخصص للمشاركة. يحتفظ بتفاصيل تشغيلية تساعد في تصحيح الأخطاء، مثل حقول سجل OpenClaw الآمنة، وأسماء الأنظمة الفرعية، ورموز الحالة، والمدد، والأوضاع المكوّنة، والمنافذ، ومعرّفات Plugin، ومعرّفات المزوّدين، وإعدادات الميزات غير السرية، ورسائل السجل التشغيلية المنقحة. ويحذف أو ينقح نص الدردشة، وأجسام Webhook، ومخرجات الأدوات، وبيانات الاعتماد، وملفات تعريف الارتباط، ومعرّفات الحساب/الرسالة، ونص المطالبة/التعليمات، وأسماء المضيفين، والقيم السرية. عندما تبدو رسالة بنمط LogTape مثل نص حمولة مستخدم/دردشة/أداة، يحتفظ التصدير فقط بأن رسالة حُذفت بالإضافة إلى عدد بايتاتها.

### `gateway status`

يعرض `gateway status` خدمة Gateway (launchd/systemd/schtasks) بالإضافة إلى فحص اختياري لإمكانية الاتصال/المصادقة.

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway status --jsonopenclaw gateway status --require-rpc
[/code]

تخطَّ فحص الاتصال (عرض الخدمة فقط).

افحص الخدمات على مستوى النظام أيضا.

رقِّ فحص الاتصال الافتراضي إلى فحص قراءة واخرج برمز غير صفري عند فشل فحص القراءة هذا. لا يمكن دمجه مع `--no-probe`.

دلالات الحالة

  * يظل `gateway status` متاحا للتشخيص حتى عندما يكون إعداد CLI المحلي مفقودا أو غير صالح.
  * يثبت `gateway status` الافتراضي حالة الخدمة، واتصال WebSocket، وإمكانية المصادقة المرئية وقت المصافحة. ولا يثبت عمليات القراءة/الكتابة/الإدارة.
  * فحوصات التشخيص لا تغيّر حالة مصادقة الجهاز لأول مرة: فهي تعيد استخدام رمز جهاز مخزّن مؤقتا موجودا عندما يتوفر، لكنها لا تنشئ هوية جهاز CLI جديدة أو سجل إقران جهاز للقراءة فقط لمجرد التحقق من الحالة.
  * يحل `gateway status` مراجع SecretRefs للمصادقة المكوّنة لمصادقة الفحص عندما يكون ذلك ممكنا.
  * إذا لم يتم حل SecretRef مطلوب للمصادقة في مسار الأمر هذا، فإن `gateway status --json` يبلّغ عن `rpc.authWarning` عندما يفشل اتصال/مصادقة الفحص؛ مرّر `--token`/`--password` صراحة أو حل مصدر السر أولا.
  * إذا نجح الفحص، تُكبت تحذيرات مراجع المصادقة غير المحلولة لتجنب النتائج الإيجابية الكاذبة.
  * استخدم `--require-rpc` في السكربتات والأتمتة عندما لا تكفي خدمة تستمع وتحتاج أيضا إلى أن تكون استدعاءات RPC ذات نطاق القراءة سليمة.
  * يضيف `--deep` فحصا بأفضل جهد لتثبيتات launchd/systemd/schtasks الإضافية. عند اكتشاف عدة خدمات شبيهة بالـ Gateway، تطبع المخرجات البشرية تلميحات تنظيف وتحذر من أن معظم الإعدادات ينبغي أن تشغّل Gateway واحدا لكل جهاز.
  * يبلّغ `--deep` أيضا عن تسليم إعادة تشغيل حديث لمشرف Gateway عندما تخرج عملية الخدمة بنظافة لإعادة تشغيل من مشرف خارجي.
  * يشغّل `--deep` التحقق من الإعداد في وضع واعٍ بالـ Plugin (`pluginValidation: "full"`) ويعرض تحذيرات بيان الـ Plugin المكوّنة (على سبيل المثال بيانات تعريف إعداد قناة مفقودة) كي تلتقطها فحوصات سلامة التثبيت والتحديث. يحافظ `gateway status` الافتراضي على مسار القراءة فقط السريع الذي يتخطى التحقق من الـ Plugin.
  * تتضمن المخرجات البشرية مسار سجل الملف المحلول إضافة إلى لقطة لمسارات/صلاحية إعداد CLI مقابل الخدمة للمساعدة في تشخيص انجراف الملف الشخصي أو دليل الحالة.

فحوصات انحراف مصادقة systemd على Linux

  * في تثبيتات systemd على Linux، تقرأ فحوصات انحراف مصادقة الخدمة قيم `Environment=` و`EnvironmentFile=` من الوحدة (بما في ذلك `%h`، والمسارات المقتبسة، والملفات المتعددة، وملفات `-` الاختيارية).
  * تحل فحوصات الانحراف SecretRefs الخاصة بـ `gateway.auth.token` باستخدام بيئة التشغيل المدمجة (بيئة أمر الخدمة أولا، ثم بيئة العملية كبديل).
  * إذا لم تكن مصادقة الرمز فعالة فعليا (وجود `gateway.auth.mode` صريح بقيمة `password`/`none`/`trusted-proxy`، أو عدم ضبط الوضع حيث يمكن أن تفوز كلمة المرور ولا يمكن لأي مرشح رمز أن يفوز)، تتخطى فحوصات انحراف الرمز حل رمز الإعداد.


### `gateway probe`

`gateway probe` هو أمر "تصحيح كل شيء". يفحص دائما:

  * Gateway البعيد المكوّن لديك (إذا كان مضبوطا)، و
  * localhost (loopback) **حتى لو كان البعيد مكوّنا**.


إذا مررت `--url`، يُضاف ذلك الهدف الصريح قبل كليهما. تسمي المخرجات البشرية الأهداف كالتالي:

  * `URL (explicit)`
  * `Remote (configured)` أو `Remote (configured, inactive)`
  * `Local loopback`

bashCopy code
[code]
    openclaw gateway probeopenclaw gateway probe --json
[/code]

التفسير

  * تعني `Reachable: yes` أن هدفا واحدا على الأقل قبل اتصال WebSocket.
  * يبلّغ `Capability: read-only|write-capable|admin-capable|pairing-pending|connect-only` عما استطاع الفحص إثباته بشأن المصادقة. وهو منفصل عن قابلية الوصول.
  * تعني `Read probe: ok` أن استدعاءات RPC التفصيلية ذات نطاق القراءة (`health`/`status`/`system-presence`/`config.get`) نجحت أيضا.
  * تعني `Read probe: limited - missing scope: operator.read` أن الاتصال نجح لكن RPC ذات نطاق القراءة محدودة. يُبلّغ عن هذا كقابلية وصول **متدهورة** ، وليس فشلا كاملا.
  * تعني `Read probe: failed` بعد `Connect: ok` أن Gateway قبل اتصال WebSocket، لكن تشخيصات القراءة اللاحقة انتهت مهلتها أو فشلت. وهذا أيضا قابلية وصول **متدهورة** ، وليس Gateway غير قابل للوصول.
  * مثل `gateway status`، يعيد الفحص استخدام مصادقة الجهاز المخزنة مؤقتا الموجودة، لكنه لا ينشئ هوية جهاز لأول مرة أو حالة إقران.
  * يكون رمز الخروج غير صفري فقط عندما لا يكون أي هدف مفحوص قابلا للوصول.

مخرجات JSON

المستوى الأعلى:

  * `ok`: هدف واحد على الأقل قابل للوصول.
  * `degraded`: هدف واحد على الأقل قبل اتصالا لكنه لم يكمل تشخيصات RPC التفصيلية الكاملة.
  * `capability`: أفضل إمكانية شوهدت عبر الأهداف القابلة للوصول (`read_only`، أو `write_capable`، أو `admin_capable`، أو `pairing_pending`، أو `connected_no_operator_scope`، أو `unknown`).
  * `primaryTargetId`: أفضل هدف للتعامل معه كفائز نشط بهذا الترتيب: عنوان URL صريح، نفق SSH، البعيد المكوّن، ثم local loopback.
  * `warnings[]`: سجلات تحذير بأفضل جهد تحتوي على `code` و`message` و`targetIds` اختيارية.
  * `network`: تلميحات عناوين URL لـ local loopback/tailnet مشتقة من الإعداد الحالي وشبكة المضيف.
  * `discovery.timeoutMs` و`discovery.count`: ميزانية/عدد نتائج الاكتشاف الفعلية المستخدمة لجولة الفحص هذه.


لكل هدف (`targets[].connect`):

  * `ok`: قابلية الوصول بعد الاتصال + تصنيف التدهور.
  * `rpcOk`: نجاح RPC التفصيلي الكامل.
  * `scopeLimited`: فشل RPC التفصيلي بسبب نطاق عامل مفقود.


لكل هدف (`targets[].auth`):

  * `role`: دور المصادقة المبلّغ عنه في `hello-ok` عند توفره.
  * `scopes`: النطاقات الممنوحة المبلّغ عنها في `hello-ok` عند توفرها.
  * `capability`: تصنيف إمكانية المصادقة المعروض لذلك الهدف.

رموز التحذير الشائعة

  * `ssh_tunnel_failed`: فشل إعداد نفق SSH؛ عاد الأمر إلى الفحوصات المباشرة.
  * `multiple_gateways`: كان أكثر من هدف واحد قابلا للوصول؛ هذا غير معتاد إلا إذا كنت تشغّل ملفات شخصية معزولة عمدا، مثل بوت إنقاذ.
  * `auth_secretref_unresolved`: تعذر حل SecretRef مصادقة مكوّن لهدف فاشل.
  * `probe_scope_limited`: نجح اتصال WebSocket، لكن فحص القراءة كان محدودا بسبب فقدان `operator.read`.


#### البعيد عبر SSH (تكافؤ تطبيق Mac)

يستخدم وضع "البعيد عبر SSH" في تطبيق macOS إعادة توجيه منفذ محلي بحيث يصبح Gateway البعيد (الذي قد يكون مربوطا بـ loopback فقط) قابلا للوصول عند `ws://127.0.0.1:<port>`.

المكافئ في CLI:

bashCopy code
[code]
    openclaw gateway probe --ssh user@gateway-host
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tc3NoIDx0YXJnZXQ " type="string"> `user@host` أو `user@host:port` (يكون المنفذ افتراضيا `22`).

اختر أول مضيف Gateway مكتشف كهدف SSH من نقطة نهاية الاكتشاف المحلولة (`local.` إضافة إلى نطاق واسع المدى المكوّن، إن وجد). تُتجاهل تلميحات TXT فقط.

الإعداد (اختياري، يُستخدم كقيم افتراضية):

  * `gateway.remote.sshTarget`
  * `gateway.remote.sshIdentity`


### `gateway call <method>`

مساعد RPC منخفض المستوى.

bashCopy code
[code]
    openclaw gateway call statusopenclaw gateway call logs.tail --params '{"sinceMs": 60000}'
[/code]

بشكل أساسي لاستدعاءات RPC بنمط الوكيل التي تبث أحداثا وسيطة قبل حمولة نهائية.

مخرجات JSON قابلة للقراءة آليا.

## إدارة خدمة Gateway

bashCopy code
[code]
    openclaw gateway installopenclaw gateway startopenclaw gateway stopopenclaw gateway restartopenclaw gateway uninstall
[/code]

### التثبيت باستخدام غلاف

استخدم `--wrapper` عندما يجب أن تبدأ الخدمة المُدارة عبر ملف تنفيذي آخر، على سبيل المثال طبقة مدير أسرار أو مساعد تشغيل باسم مستخدم آخر. يتلقى الغلاف وسائط Gateway العادية ويكون مسؤولا في النهاية عن تنفيذ `openclaw` أو Node بهذه الوسائط.

bashCopy code
[code]
    cat > ~/.local/bin/openclaw-doppler <<'EOF'#!/usr/bin/env bashset -euo pipefailexec doppler run --project my-project --config production -- openclaw "$@"EOFchmod +x ~/.local/bin/openclaw-doppler openclaw gateway install --wrapper ~/.local/bin/openclaw-doppler --forceopenclaw gateway restart
[/code]

يمكنك أيضا ضبط الغلاف عبر البيئة. يتحقق `gateway install` من أن المسار ملف تنفيذي، ويكتب الغلاف في `ProgramArguments` الخاصة بالخدمة، ويثبّت `OPENCLAW_WRAPPER` في بيئة الخدمة لإعادة التثبيت القسرية والتحديثات وإصلاحات الطبيب لاحقا.

bashCopy code
[code]
    OPENCLAW_WRAPPER="$HOME/.local/bin/openclaw-doppler" openclaw gateway install --forceopenclaw doctor
[/code]

لإزالة غلاف مثبت، امسح `OPENCLAW_WRAPPER` أثناء إعادة التثبيت:

bashCopy code
[code]
    OPENCLAW_WRAPPER= openclaw gateway install --forceopenclaw gateway restart
[/code]

خيارات الأمر

  * `gateway status`: `--url`, `--token`, `--password`, `--timeout`, `--no-probe`, `--require-rpc`, `--deep`, `--json`
  * `gateway install`: `--port`, `--runtime <node|bun>`, `--token`, `--wrapper <path>`, `--force`, `--json`
  * `gateway restart`: `--safe`, `--skip-deferral`, `--force`, `--wait <duration>`, `--json`
  * `gateway uninstall|start`: `--json`
  * `gateway stop`: `--disable`, `--json`

سلوك دورة الحياة

  * استخدم `gateway restart` لإعادة تشغيل خدمة مُدارة. لا تسلسل `gateway stop` و`gateway start` كبديل لإعادة التشغيل.
  * على macOS، يستخدم `gateway stop` الأمر `launchctl bootout` افتراضيًا، ما يزيل LaunchAgent من جلسة الإقلاع الحالية من دون الإبقاء على تعطيل مستمر — يظل الاسترداد التلقائي عبر KeepAlive نشطًا للأعطال المستقبلية، ويعيد `gateway start` التمكين بشكل نظيف من دون `launchctl enable` يدوي. مرّر `--disable` لتعطيل KeepAlive وRunAtLoad بشكل مستمر كي لا يعاود Gateway الظهور حتى تنفيذ `gateway start` الصريح التالي؛ استخدم هذا عندما يجب أن يصمد الإيقاف اليدوي بعد إعادة الإقلاع أو إعادة تشغيل النظام.
  * يطلب `gateway restart --safe` من Gateway الجاري تشغيله إجراء فحص مسبق لأعمال OpenClaw النشطة وتأجيل إعادة التشغيل حتى يكتمل تسليم الردود وعمليات التشغيل المضمّنة وتشغيلات المهام. لا يمكن دمج `--safe` مع `--force` أو `--wait`.
  * يتجاوز `gateway restart --wait 30s` ميزانية تصريف إعادة التشغيل المكوّنة لإعادة التشغيل هذه. الأرقام المجرّدة تعني المللي ثانية؛ وتُقبل الوحدات مثل `s` و`m` و`h`. ينتظر `--wait 0` إلى أجل غير مسمى.
  * يشغّل `gateway restart --safe --skip-deferral` إعادة التشغيل الآمنة الواعية بـ OpenClaw لكنه يتجاوز بوابة التأجيل لكي يصدر Gateway إعادة التشغيل فورًا حتى عند الإبلاغ عن موانع. هذا مخرج طوارئ للمشغّل لتأجيلات تشغيلات المهام العالقة؛ ويتطلب `--safe`.
  * يتخطى `gateway restart --force` تصريف العمل النشط ويعيد التشغيل فورًا. استخدمه عندما يكون المشغّل قد فحص بالفعل موانع المهام المدرجة ويريد عودة Gateway الآن.
  * تقبل أوامر دورة الحياة `--json` للاستخدام في السكربتات.

المصادقة وSecretRefs وقت التثبيت

  * عندما تتطلب مصادقة الرمز رمزًا ويكون `gateway.auth.token` مُدارًا عبر SecretRef، يتحقق `gateway install` من إمكانية حل SecretRef لكنه لا يحفظ الرمز المحلول في بيانات تعريف بيئة الخدمة.
  * إذا كانت مصادقة الرمز تتطلب رمزًا وكان SecretRef للرمز المكوّن غير محلول، يفشل التثبيت بأمان بدلًا من حفظ نص عادي احتياطي.
  * لمصادقة كلمة المرور في `gateway run`، فضّل `OPENCLAW_GATEWAY_PASSWORD` أو `--password-file` أو `gateway.auth.password` المدعوم بـ SecretRef على `--password` المضمّنة.
  * في وضع المصادقة المستنتج، لا يخفف `OPENCLAW_GATEWAY_PASSWORD` المتاح للصدفة فقط متطلبات رمز التثبيت؛ استخدم إعدادًا دائمًا (`gateway.auth.password` أو `env` في الإعدادات) عند تثبيت خدمة مُدارة.
  * إذا كان كل من `gateway.auth.token` و`gateway.auth.password` مكوّنين وكان `gateway.auth.mode` غير معيّن، يُحظر التثبيت حتى يُعيّن الوضع صراحةً.


## اكتشاف الـ gateways (Bonjour)

يفحص `gateway discover` إشارات Gateway (`_openclaw-gw._tcp`).

  * Multicast DNS-SD: `local.`
  * Unicast DNS-SD (Wide-Area Bonjour): اختر نطاقًا (مثال: `openclaw.internal.`) واضبط split DNS + خادم DNS؛ راجع [Bonjour](</ar/gateway/bonjour>).


لا تعلن الإشارة إلا الـ gateways التي تم تمكين اكتشاف Bonjour لها (افتراضيًا).

يمكن أن تتضمن سجلات الاكتشاف واسع النطاق تلميحات TXT هذه:

  * `role` (تلميح دور gateway)
  * `transport` (تلميح النقل، مثل `gateway`)
  * `gatewayPort` (منفذ WebSocket، عادةً `18789`)
  * `sshPort` (وضع الاكتشاف الكامل فقط؛ يضبط العملاء أهداف SSH الافتراضية على `22` عند غيابه)
  * `tailnetDns` (اسم مضيف MagicDNS، عند توفره)
  * `gatewayTls` / `gatewayTlsSha256` (TLS مفعّل + بصمة الشهادة)
  * `cliPath` (وضع الاكتشاف الكامل فقط)


### `gateway discover`

bashCopy code
[code]
    openclaw gateway discover
[/code]

مخرجات قابلة للقراءة آليًا (وتعطل أيضًا التنسيق/مؤشر التحميل).

أمثلة:

bashCopy code
[code]
    openclaw gateway discover --timeout 4000openclaw gateway discover --json | jq '.beacons[].wsUrl'
[/code]

## ذات صلة

  * [مرجع CLI](</ar/cli>)
  * [دليل تشغيل Gateway](</ar/gateway>)


Was this useful?YesNo