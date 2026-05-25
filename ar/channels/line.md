---
title: سطر
source_url: https://docs.openclaw.ai/ar/channels/line
scraped_at: 2026-05-25
---

يتصل LINE بـ OpenClaw عبر LINE Messaging API. يعمل Plugin كمستقبِل Webhook على Gateway ويستخدم رمز وصول القناة + سر القناة لديك من أجل المصادقة.

الحالة: Plugin قابل للتنزيل. الرسائل المباشرة، ودردشات المجموعات، والوسائط، والمواقع، ورسائل Flex، ورسائل القوالب، والردود السريعة مدعومة. التفاعلات والسلاسل غير مدعومة.

## التثبيت

ثبّت LINE قبل تكوين القناة:

bashCopy code
[code]
    openclaw plugins install @openclaw/line
[/code]

نسخة محلية (عند التشغيل من مستودع git):

bashCopy code
[code]
    openclaw plugins install ./path/to/local/line-plugin
[/code]

## الإعداد

  1. أنشئ حساب LINE Developers وافتح Console: <https://developers.line.biz/console/>
  2. أنشئ Provider أو اختر واحدًا وأضف قناة **Messaging API**.
  3. انسخ **Channel access token** و **Channel secret** من إعدادات القناة.
  4. فعّل **Use webhook** في إعدادات Messaging API.
  5. اضبط عنوان Webhook URL على نقطة نهاية Gateway لديك (يتطلب HTTPS):

CodeCopy code
[code]
    https://gateway-host/line/webhook
[/code]

يستجيب Gateway للتحقق من Webhook الخاص بـ LINE (GET) والأحداث الواردة (POST). إذا كنت تحتاج إلى مسار مخصص، فاضبط `channels.line.webhookPath` أو `channels.line.accounts.<id>.webhookPath` وحدّث عنوان URL وفقًا لذلك.

ملاحظة أمنية:

  * يعتمد التحقق من توقيع LINE على المتن (HMAC على المتن الخام)، لذلك يطبّق OpenClaw حدودًا صارمة على المتن قبل المصادقة ومهلة زمنية قبل التحقق.
  * يعالج OpenClaw أحداث Webhook من بايتات الطلب الخام التي تم التحقق منها. يتم تجاهل قيم `req.body` المحوّلة عبر البرمجيات الوسيطة العليا حفاظًا على سلامة التوقيع.


## التكوين

تكوين حد أدنى:

json5Copy code
[code]
    {  channels: {    line: {      enabled: true,      channelAccessToken: "LINE_CHANNEL_ACCESS_TOKEN",      channelSecret: "LINE_CHANNEL_SECRET",      dmPolicy: "pairing",    },  },}
[/code]

تكوين الرسائل المباشرة العامة:

json5Copy code
[code]
    {  channels: {    line: {      enabled: true,      channelAccessToken: "LINE_CHANNEL_ACCESS_TOKEN",      channelSecret: "LINE_CHANNEL_SECRET",      dmPolicy: "open",      allowFrom: ["*"],    },  },}
[/code]

متغيرات البيئة (الحساب الافتراضي فقط):

  * `LINE_CHANNEL_ACCESS_TOKEN`
  * `LINE_CHANNEL_SECRET`


ملفات الرمز/السر:

json5Copy code
[code]
    {  channels: {    line: {      tokenFile: "/path/to/line-token.txt",      secretFile: "/path/to/line-secret.txt",    },  },}
[/code]

يجب أن يشير `tokenFile` و `secretFile` إلى ملفات عادية. يتم رفض الروابط الرمزية.

حسابات متعددة:

json5Copy code
[code]
    {  channels: {    line: {      accounts: {        marketing: {          channelAccessToken: "...",          channelSecret: "...",          webhookPath: "/line/marketing",        },      },    },  },}
[/code]

## التحكم في الوصول

تستخدم الرسائل المباشرة الاقتران افتراضيًا. يحصل المرسلون غير المعروفين على رمز اقتران ويتم تجاهل رسائلهم حتى تتم الموافقة عليهم.

bashCopy code
[code]
    openclaw pairing list lineopenclaw pairing approve line &lt;CODE&gt;
[/code]

قوائم السماح والسياسات:

  * `channels.line.dmPolicy`: `pairing | allowlist | open | disabled`
  * `channels.line.allowFrom`: معرّفات مستخدمي LINE المسموح بها للرسائل المباشرة؛ يتطلب `dmPolicy: "open"` القيمة `["*"]`
  * `channels.line.groupPolicy`: `allowlist | open | disabled`
  * `channels.line.groupAllowFrom`: معرّفات مستخدمي LINE المسموح بها للمجموعات
  * تجاوزات لكل مجموعة: `channels.line.groups.<groupId>.allowFrom`
  * يمكن الرجوع إلى مجموعات وصول المرسلين الثابتة من `allowFrom` و `groupAllowFrom` و `allowFrom` لكل مجموعة باستخدام `accessGroup:<name>`.
  * ملاحظة وقت التشغيل: إذا كان `channels.line` مفقودًا تمامًا، يعود وقت التشغيل إلى `groupPolicy="allowlist"` لفحوصات المجموعات (حتى إذا كان `channels.defaults.groupPolicy` مضبوطًا).


معرّفات LINE حساسة لحالة الأحرف. تبدو المعرّفات الصالحة كما يلي:

  * المستخدم: `U` \+ 32 حرفًا سداسيًا عشريًا
  * المجموعة: `C` \+ 32 حرفًا سداسيًا عشريًا
  * الغرفة: `R` \+ 32 حرفًا سداسيًا عشريًا


## سلوك الرسائل

  * يتم تقسيم النص عند 5000 حرف.
  * تتم إزالة تنسيق Markdown؛ ويتم تحويل كتل التعليمات البرمجية والجداول إلى بطاقات Flex عندما يكون ذلك ممكنًا.
  * يتم تخزين الاستجابات المتدفقة مؤقتًا؛ يتلقى LINE المقاطع كاملة مع رسم متحرك للتحميل أثناء عمل الوكيل.
  * يتم تقييد تنزيلات الوسائط بواسطة `channels.line.mediaMaxMb` (الافتراضي 10).
  * يتم حفظ الوسائط الواردة تحت `~/.openclaw/media/inbound/` قبل تمريرها إلى الوكيل، بما يطابق مخزن الوسائط المشترك الذي تستخدمه Plugins القنوات المضمنة الأخرى.


## بيانات القناة (الرسائل الغنية)

استخدم `channelData.line` لإرسال ردود سريعة، أو مواقع، أو بطاقات Flex، أو رسائل قوالب.

json5Copy code
[code]
    {  text: "Here you go",  channelData: {    line: {      quickReplies: ["Status", "Help"],      location: {        title: "Office",        address: "123 Main St",        latitude: 35.681236,        longitude: 139.767125,      },      flexMessage: {        altText: "Status card",        contents: {          /* Flex payload */        },      },      templateMessage: {        type: "confirm",        text: "Proceed?",        confirmLabel: "Yes",        confirmData: "yes",        cancelLabel: "No",        cancelData: "no",      },    },  },}
[/code]

يوفر LINE Plugin أيضًا أمر `/card` لإعدادات رسائل Flex المسبقة:

CodeCopy code
[code]
    /card info "Welcome" "Thanks for joining!"
[/code]

## دعم ACP

يدعم LINE ارتباطات محادثات ACP (بروتوكول تواصل الوكلاء):

  * يربط `/acp spawn <agent> --bind here` دردشة LINE الحالية بجلسة ACP من دون إنشاء سلسلة فرعية.
  * تعمل ارتباطات ACP المكوّنة وجلسات ACP النشطة المرتبطة بالمحادثة على LINE مثل قنوات المحادثة الأخرى.


راجع [وكلاء ACP](</ar/tools/acp-agents>) للحصول على التفاصيل.

## الوسائط الصادرة

يدعم LINE Plugin إرسال الصور، ومقاطع الفيديو، وملفات الصوت عبر أداة رسائل الوكيل. يتم إرسال الوسائط عبر مسار التسليم الخاص بـ LINE مع المعالجة المناسبة للمعاينة والتتبع:

  * **الصور** : تُرسل كرسائل صور LINE مع إنشاء معاينة تلقائي.
  * **مقاطع الفيديو** : تُرسل مع معالجة صريحة للمعاينة ونوع المحتوى.
  * **الصوت** : يُرسل كرسائل صوت LINE.


يجب أن تكون عناوين URL للوسائط الصادرة عناوين HTTPS عامة. يتحقق OpenClaw من اسم مضيف الهدف قبل تسليم عنوان URL إلى LINE ويرفض أهداف loopback، وlink-local، والشبكات الخاصة.

تعود عمليات إرسال الوسائط العامة إلى مسار الصور فقط الحالي عندما لا يتوفر مسار خاص بـ LINE.

## استكشاف الأخطاء وإصلاحها

  * **يفشل التحقق من Webhook:** تأكد من أن عنوان Webhook URL يستخدم HTTPS وأن `channelSecret` يطابق LINE console.
  * **لا توجد أحداث واردة:** تأكد من أن مسار Webhook يطابق `channels.line.webhookPath` وأن Gateway قابل للوصول من LINE.
  * **أخطاء تنزيل الوسائط:** ارفع `channels.line.mediaMaxMb` إذا تجاوزت الوسائط الحد الافتراضي.


## ذات صلة

  * [نظرة عامة على القنوات](</ar/channels>) — جميع القنوات المدعومة
  * [الاقتران](</ar/channels/pairing>) — مصادقة الرسائل المباشرة وتدفق الاقتران
  * [المجموعات](</ar/channels/groups>) — سلوك دردشات المجموعات وبوابة الإشارات
  * [توجيه القنوات](</ar/channels/channel-routing>) — توجيه الجلسات للرسائل
  * [الأمان](</ar/gateway/security>) — نموذج الوصول والتقوية


Was this useful?YesNo