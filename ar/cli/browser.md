---
title: المتصفح
source_url: https://docs.openclaw.ai/ar/cli/browser
scraped_at: 2026-05-25
---

# `openclaw browser`

إدارة سطح تحكم المتصفح في OpenClaw وتشغيل إجراءات المتصفح (دورة الحياة، الملفات الشخصية، علامات التبويب، اللقطات، لقطات الشاشة، التنقل، الإدخال، محاكاة الحالة، وتصحيح الأخطاء).

ذات صلة:

  * أداة المتصفح + واجهة API: [أداة المتصفح](</ar/tools/browser>)


## العلامات الشائعة

  * `--url <gatewayWsUrl>`: عنوان URL الخاص بـ WebSocket في Gateway (يستخدم الإعدادات افتراضيًا).
  * `--token <token>`: رمز Gateway المميز (إذا كان مطلوبًا).
  * `--timeout <ms>`: مهلة الطلب (ms).
  * `--expect-final`: انتظار استجابة Gateway نهائية.
  * `--browser-profile <name>`: اختيار ملف شخصي للمتصفح (الافتراضي من الإعدادات).
  * `--json`: إخراج قابل للقراءة آليًا (حيثما كان مدعومًا).


## البدء السريع (محليًا)

bashCopy code
[code]
    openclaw browser profilesopenclaw browser --browser-profile openclaw startopenclaw browser --browser-profile openclaw open https://example.comopenclaw browser --browser-profile openclaw snapshot
[/code]

يمكن للوكلاء تشغيل فحص الجاهزية نفسه باستخدام `browser({ action: "doctor" })`.

## استكشاف الأخطاء السريع

إذا فشل `start` مع `not reachable after start`، فاستكشف جاهزية CDP أولًا. إذا نجح `start` و`tabs` لكن فشل `open` أو `navigate`، فإن مستوى التحكم بالمتصفح سليم، ويكون الفشل عادةً ناتجًا عن سياسة SSRF للتنقل.

تسلسل بسيط:

bashCopy code
[code]
    openclaw browser --browser-profile openclaw doctoropenclaw browser --browser-profile openclaw startopenclaw browser --browser-profile openclaw tabsopenclaw browser --browser-profile openclaw open https://example.com
[/code]

إرشادات مفصلة: [استكشاف أخطاء المتصفح](</ar/tools/browser#cdp-startup-failure-vs-navigation-ssrf-block>)

## دورة الحياة

bashCopy code
[code]
    openclaw browser statusopenclaw browser doctoropenclaw browser doctor --deepopenclaw browser startopenclaw browser start --headlessopenclaw browser stopopenclaw browser --browser-profile openclaw reset-profile
[/code]

ملاحظات:

  * يضيف `doctor --deep` فحص لقطة مباشرًا. يكون ذلك مفيدًا عندما تكون جاهزية CDP الأساسية سليمة، لكنك تريد إثباتًا أن علامة التبويب الحالية قابلة للفحص.
  * بالنسبة إلى ملفات `attachOnly` وCDP البعيدة، يغلق `openclaw browser stop` جلسة التحكم النشطة ويمسح تجاوزات المحاكاة المؤقتة حتى عندما لا يكون OpenClaw قد شغّل عملية المتصفح بنفسه.
  * بالنسبة إلى الملفات الشخصية المحلية المُدارة، يوقف `openclaw browser stop` عملية المتصفح التي تم إنشاؤها.
  * لا ينطبق `openclaw browser start --headless` إلا على طلب البدء هذا فقط وفقط عندما يشغّل OpenClaw متصفحًا محليًا مُدارًا. ولا يعيد كتابة `browser.headless` أو إعدادات الملف الشخصي، ولا يفعل شيئًا لمتصفح قيد التشغيل بالفعل.
  * على مضيفات Linux التي لا تحتوي على `DISPLAY` أو `WAYLAND_DISPLAY`، تعمل الملفات الشخصية المحلية المُدارة بلا واجهة تلقائيًا ما لم يطلب `OPENCLAW_BROWSER_HEADLESS=0` أو `browser.headless=false` أو `browser.profiles.<name>.headless=false` متصفحًا مرئيًا صراحةً.


## إذا كان الأمر مفقودًا

إذا كان `openclaw browser` أمرًا غير معروف، فتحقق من `plugins.allow` في `~/.openclaw/openclaw.json`.

عند وجود `plugins.allow`، أدرج Plugin المتصفح المضمّن صراحةً ما لم تكن الإعدادات تحتوي بالفعل على كتلة `browser` جذرية:

json5Copy code
[code]
    {  plugins: {    allow: ["telegram", "browser"],  },}
[/code]

تؤدي كتلة `browser` جذرية صريحة، مثل `browser.enabled=true` أو `browser.profiles.<name>`، أيضًا إلى تفعيل Plugin المتصفح المضمّن ضمن قائمة سماح Plugin تقييدية.

ذات صلة: [أداة المتصفح](</ar/tools/browser#missing-browser-command-or-tool>)

## الملفات الشخصية

الملفات الشخصية هي إعدادات توجيه متصفح مسماة. عمليًا:

  * `openclaw`: يشغّل مثيل Chrome مخصصًا تديره OpenClaw أو يتصل به (دليل بيانات مستخدم معزول).
  * `user`: يتحكم في جلسة Chrome الحالية المسجّل دخولك إليها عبر Chrome DevTools MCP.
  * ملفات CDP الشخصية المخصصة: تشير إلى نقطة نهاية CDP محلية أو بعيدة.

bashCopy code
[code]
    openclaw browser profilesopenclaw browser create-profile --name work --color "#FF5A36"openclaw browser create-profile --name chrome-live --driver existing-sessionopenclaw browser create-profile --name remote --cdp-url https://browser-host.example.comopenclaw browser delete-profile --name work
[/code]

استخدم ملفًا شخصيًا محددًا:

bashCopy code
[code]
    openclaw browser --browser-profile work tabs
[/code]

## علامات التبويب

bashCopy code
[code]
    openclaw browser tabsopenclaw browser tab new --label docsopenclaw browser tab label t1 docsopenclaw browser tab select 2openclaw browser tab close 2openclaw browser open https://docs.openclaw.ai --label docsopenclaw browser focus docsopenclaw browser close t1
[/code]

يعيد `tabs` قيمة `suggestedTargetId` أولًا، ثم `tabId` المستقر مثل `t1`، والتسمية الاختيارية، و`targetId` الخام. يجب على الوكلاء تمرير `suggestedTargetId` مجددًا إلى `focus` و`close` واللقطات والإجراءات. يمكنك تعيين تسمية باستخدام `open --label` أو `tab new --label` أو `tab label`؛ وتُقبل التسميات ومعرّفات علامات التبويب ومعرّفات الهدف الخام والبادئات الفريدة لمعرّف الهدف كلها. عندما يستبدل Chromium الهدف الخام الأساسي أثناء التنقل أو إرسال نموذج، يبقي OpenClaw قيمة `tabId`/التسمية المستقرة مرتبطة بعلامة التبويب البديلة عندما يستطيع إثبات التطابق. تبقى معرّفات الهدف الخام متقلبة؛ فضّل `suggestedTargetId`.

## اللقطة / لقطة الشاشة / الإجراءات

اللقطة:

bashCopy code
[code]
    openclaw browser snapshotopenclaw browser snapshot --urls
[/code]

لقطة الشاشة:

bashCopy code
[code]
    openclaw browser screenshotopenclaw browser screenshot --full-pageopenclaw browser screenshot --ref e12openclaw browser screenshot --labels
[/code]

ملاحظات:

  * `--full-page` مخصص لالتقاط الصفحات فقط؛ ولا يمكن دمجه مع `--ref` أو `--element`.
  * تدعم ملفات `existing-session` / `user` لقطات شاشة الصفحة ولقطات شاشة `--ref` من إخراج اللقطة، لكنها لا تدعم لقطات شاشة CSS عبر `--element`.
  * يضع `--labels` مراجع اللقطة الحالية فوق لقطة الشاشة.
  * يضيف `snapshot --urls` وجهات الروابط المكتشفة إلى لقطات الذكاء الاصطناعي حتى يتمكن الوكلاء من اختيار أهداف تنقل مباشرة بدلًا من التخمين من نص الرابط وحده.


التنقل/النقر/الكتابة (أتمتة واجهة المستخدم المعتمدة على المرجع):

bashCopy code
[code]
    openclaw browser navigate https://example.comopenclaw browser click <ref>openclaw browser click-coords 120 340openclaw browser type <ref> "hello"openclaw browser press Enteropenclaw browser hover <ref>openclaw browser scrollintoview <ref>openclaw browser drag <startRef> <endRef>openclaw browser select <ref> OptionA OptionBopenclaw browser fill --fields '[{"ref":"1","value":"Ada"}]'openclaw browser wait --text "Done"openclaw browser evaluate --fn '(el) => el.textContent' --ref <ref>
[/code]

تعيد استجابات الإجراء قيمة `targetId` الخام الحالية بعد استبدال الصفحة المشغّل بإجراء عندما يستطيع OpenClaw إثبات علامة التبويب البديلة. ومع ذلك ينبغي للبرامج النصية تخزين وتمرير `suggestedTargetId`/التسميات لسير العمل طويل الأمد.

مساعدات الملفات ومربعات الحوار:

bashCopy code
[code]
    openclaw browser upload /tmp/openclaw/uploads/file.pdf --ref <ref>openclaw browser waitfordownloadopenclaw browser download <ref> report.pdfopenclaw browser dialog --accept
[/code]

تحفظ ملفات Chrome الشخصية المُدارة التنزيلات العادية الناتجة عن النقر في دليل تنزيلات OpenClaw (`/tmp/openclaw/downloads` افتراضيًا، أو جذر الملفات المؤقتة المضبوط). استخدم `waitfordownload` أو `download` عندما يحتاج الوكيل إلى انتظار ملف محدد وإعادة مساره؛ تمتلك أدوات الانتظار الصريحة هذه التنزيل التالي.

## الحالة والتخزين

إطار العرض + المحاكاة:

bashCopy code
[code]
    openclaw browser resize 1280 720openclaw browser set viewport 1280 720openclaw browser set offline onopenclaw browser set media darkopenclaw browser set timezone Europe/Londonopenclaw browser set locale en-GBopenclaw browser set geo 51.5074 -0.1278 --accuracy 25openclaw browser set device "iPhone 14"openclaw browser set headers '{"x-test":"1"}'openclaw browser set credentials myuser mypass
[/code]

ملفات تعريف الارتباط + التخزين:

bashCopy code
[code]
    openclaw browser cookiesopenclaw browser cookies set session abc123 --url https://example.comopenclaw browser cookies clearopenclaw browser storage local getopenclaw browser storage local set token abc123openclaw browser storage session clear
[/code]

## تصحيح الأخطاء

bashCopy code
[code]
    openclaw browser console --level erroropenclaw browser pdfopenclaw browser responsebody "**/api"openclaw browser highlight <ref>openclaw browser errors --clearopenclaw browser requests --filter apiopenclaw browser trace startopenclaw browser trace stop --out trace.zip
[/code]

## Chrome موجود عبر MCP

استخدم الملف الشخصي المضمّن `user`، أو أنشئ ملف `existing-session` خاصًا بك:

bashCopy code
[code]
    openclaw browser --browser-profile user tabsopenclaw browser create-profile --name chrome-live --driver existing-sessionopenclaw browser create-profile --name brave-live --driver existing-session --user-data-dir "~/Library/Application Support/BraveSoftware/Brave-Browser"openclaw browser --browser-profile chrome-live tabs
[/code]

هذا المسار خاص بالمضيف فقط. بالنسبة إلى Docker أو الخوادم بلا واجهة أو Browserless أو الإعدادات البعيدة الأخرى، استخدم ملف CDP شخصيًا بدلًا من ذلك.

قيود `existing-session` الحالية:

  * تستخدم الإجراءات المعتمدة على اللقطات المراجع، وليس محددات CSS
  * يضبط `browser.actionTimeoutMs` قيمة الطلبات المدعومة `act` افتراضيًا إلى 60000 ms عندما يحذف المستدعون `timeoutMs`؛ وتظل قيمة `timeoutMs` لكل استدعاء هي الأعلى أولوية.
  * `click` نقر أيسر فقط
  * لا يدعم `type` قيمة `slowly=true`
  * لا يدعم `press` قيمة `delayMs`
  * ترفض `hover` و`scrollintoview` و`drag` و`select` و`fill` و`evaluate` تجاوزات المهلة لكل استدعاء
  * يدعم `select` قيمة واحدة فقط
  * `wait --load networkidle` غير مدعوم
  * تتطلب عمليات رفع الملفات `--ref` / `--input-ref`، ولا تدعم CSS عبر `--element`، وتدعم حاليًا ملفًا واحدًا في كل مرة
  * لا تدعم خطافات مربع الحوار `--timeout`
  * تدعم لقطات الشاشة التقاط الصفحات و`--ref`، لكن ليس CSS عبر `--element`
  * ما زالت `responsebody` واعتراض التنزيلات وتصدير PDF والإجراءات الدفعية تتطلب متصفحًا مُدارًا أو ملف CDP خامًا


## التحكم بالمتصفح عن بُعد (وكيل مضيف العقدة)

إذا كان Gateway يعمل على جهاز مختلف عن المتصفح، فشغّل **مضيف عقدة** على الجهاز الذي يحتوي على Chrome/Brave/Edge/Chromium. سيقوم Gateway بتمرير إجراءات المتصفح إلى تلك العقدة (لا يلزم خادم تحكم منفصل بالمتصفح).

استخدم `gateway.nodes.browser.mode` للتحكم في التوجيه التلقائي و`gateway.nodes.browser.node` لتثبيت عقدة محددة إذا كانت هناك عدة عقد متصلة.

الأمان + الإعداد البعيد: [أداة المتصفح](</ar/tools/browser>)، [الوصول البعيد](</ar/gateway/remote>)، [Tailscale](</ar/gateway/tailscale>)، [الأمان](</ar/gateway/security>)

## ذات صلة

  * [مرجع CLI](</ar/cli>)
  * [المتصفح](</ar/tools/browser>)


Was this useful?YesNo