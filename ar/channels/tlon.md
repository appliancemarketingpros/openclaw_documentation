---
title: Tlon
source_url: https://docs.openclaw.ai/ar/channels/tlon
scraped_at: 2026-05-25
---

Tlon هو مراسل لامركزي مبني على Urbit. يتصل OpenClaw بسفينة Urbit الخاصة بك ويمكنه الرد على الرسائل المباشرة ورسائل الدردشة الجماعية. تتطلب ردود المجموعات إشارة @ افتراضيًا ويمكن تقييدها أكثر عبر قوائم السماح.

الحالة: Plugin مضمّن. الرسائل المباشرة، وإشارات المجموعات، وردود السلاسل، وتنسيق النص الغني، و رفع الصور مدعومة. التفاعلات والاستطلاعات غير مدعومة بعد.

## Plugin مضمّن

يأتي Tlon بصفته Plugin مضمّنًا في إصدارات OpenClaw الحالية، لذلك لا تحتاج البُنى المعبأة العادية إلى تثبيت منفصل.

إذا كنت تستخدم بنية أقدم أو تثبيتًا مخصصًا يستبعد Tlon، فثبّت حزمة npm حالية:

التثبيت عبر CLI (سجل npm):

bashCopy code
[code]
    openclaw plugins install @openclaw/tlon
[/code]

استخدم الحزمة المجردة لمتابعة وسم الإصدار الرسمي الحالي. ثبّت إصدارًا محددًا بدقة فقط عندما تحتاج إلى تثبيت قابل لإعادة الإنتاج.

نسخة محلية من المستودع (عند التشغيل من مستودع git):

bashCopy code
[code]
    openclaw plugins install ./path/to/local/tlon-plugin
[/code]

التفاصيل: [Plugins](</ar/tools/plugin>)

## الإعداد

  1. تأكد من أن Tlon Plugin متاح. 
     * إصدارات OpenClaw المعبأة الحالية تتضمنه بالفعل.
     * يمكن للتثبيتات الأقدم/المخصصة إضافته يدويًا باستخدام الأوامر أعلاه.
  2. اجمع عنوان URL الخاص بسفينتك ورمز تسجيل الدخول.
  3. اضبط `channels.tlon`.
  4. أعد تشغيل Gateway.
  5. أرسل رسالة مباشرة إلى البوت أو اذكره في قناة جماعية.


إعداد بسيط (حساب واحد):

json5Copy code
[code]
    {  channels: {    tlon: {      enabled: true,      ship: "~sampel-palnet",      url: "https://your-ship-host",      code: "lidlut-tabwed-pillex-ridrup",      ownerShip: "~your-main-ship", // recommended: your ship, always allowed    },  },}
[/code]

## السفن الخاصة/شبكة LAN

افتراضيًا، يحظر OpenClaw أسماء المضيفين ونطاقات عناوين IP الخاصة/الداخلية للحماية من SSRF. إذا كانت سفينتك تعمل على شبكة خاصة (localhost أو عنوان LAN IP أو اسم مضيف داخلي)، فيجب أن توافق على ذلك صراحةً:

json5Copy code
[code]
    {  channels: {    tlon: {      url: "http://localhost:8080",      allowPrivateNetwork: true,    },  },}
[/code]

ينطبق هذا على عناوين URL مثل:

  * `http://localhost:8080`
  * `http://192.168.x.x:8080`
  * `http://my-ship.local:8080`


⚠️ فعّل هذا فقط إذا كنت تثق بشبكتك المحلية. يعطّل هذا الإعداد حمايات SSRF للطلبات المرسلة إلى عنوان URL الخاص بسفينتك.

## القنوات الجماعية

الاكتشاف التلقائي مفعّل افتراضيًا. يمكنك أيضًا تثبيت القنوات يدويًا:

json5Copy code
[code]
    {  channels: {    tlon: {      groupChannels: ["chat/~host-ship/general", "chat/~host-ship/support"],    },  },}
[/code]

تعطيل الاكتشاف التلقائي:

json5Copy code
[code]
    {  channels: {    tlon: {      autoDiscoverChannels: false,    },  },}
[/code]

## التحكم في الوصول

قائمة سماح الرسائل المباشرة (فارغة = لا يُسمح بأي رسائل مباشرة، استخدم `ownerShip` لتدفق الموافقة):

json5Copy code
[code]
    {  channels: {    tlon: {      dmAllowlist: ["~zod", "~nec"],    },  },}
[/code]

تفويض المجموعات (مقيّد افتراضيًا):

json5Copy code
[code]
    {  channels: {    tlon: {      defaultAuthorizedShips: ["~zod"],      authorization: {        channelRules: {          "chat/~host-ship/general": {            mode: "restricted",            allowedShips: ["~zod", "~nec"],          },          "chat/~host-ship/announcements": {            mode: "open",          },        },      },    },  },}
[/code]

## نظام المالك والموافقة

عيّن سفينة مالك لتلقي طلبات الموافقة عندما يحاول مستخدمون غير مصرّح لهم التفاعل:

json5Copy code
[code]
    {  channels: {    tlon: {      ownerShip: "~your-main-ship",    },  },}
[/code]

سفينة المالك **مصرّح لها تلقائيًا في كل مكان** — تُقبَل دعوات الرسائل المباشرة تلقائيًا و تُسمح رسائل القنوات دائمًا. لا تحتاج إلى إضافة المالك إلى `dmAllowlist` أو `defaultAuthorizedShips`.

عند تعيينه، يتلقى المالك إشعارات عبر الرسائل المباشرة بشأن:

  * طلبات الرسائل المباشرة من سفن غير موجودة في قائمة السماح
  * الإشارات في القنوات من دون تفويض
  * طلبات دعوات المجموعات


## إعدادات القبول التلقائي

قبول دعوات الرسائل المباشرة تلقائيًا (للسفن الموجودة في dmAllowlist):

json5Copy code
[code]
    {  channels: {    tlon: {      autoAcceptDmInvites: true,    },  },}
[/code]

قبول دعوات المجموعات تلقائيًا من السفن الموثوقة:

json5Copy code
[code]
    {  channels: {    tlon: {      autoAcceptGroupInvites: true,      groupInviteAllowlist: ["~zod"],    },  },}
[/code]

يفشل `autoAcceptGroupInvites` بشكل مغلق عندما تكون `groupInviteAllowlist` فارغة. عيّن قائمة السماح إلى السفن التي ينبغي قبول دعوات مجموعاتها تلقائيًا.

## أهداف التسليم (CLI/cron)

استخدم هذه مع `openclaw message send` أو تسليم cron:

  * رسالة مباشرة: `~sampel-palnet` أو `dm/~sampel-palnet`
  * مجموعة: `chat/~host-ship/channel` أو `group:~host-ship/channel`


## Skill مضمّنة

يتضمن Tlon Plugin Skill مضمّنة ([`@tloncorp/tlon-skill`](<https://github.com/tloncorp/tlon-skill>)) توفر وصول CLI إلى عمليات Tlon:

  * **جهات الاتصال** : جلب/تحديث الملفات الشخصية، سرد جهات الاتصال
  * **القنوات** : السرد، الإنشاء، نشر الرسائل، جلب السجل
  * **المجموعات** : السرد، الإنشاء، إدارة الأعضاء
  * **الرسائل المباشرة** : إرسال الرسائل، التفاعل مع الرسائل
  * **التفاعلات** : إضافة/إزالة تفاعلات emoji على المنشورات والرسائل المباشرة
  * **الإعدادات** : إدارة أذونات Plugin عبر أوامر slash


تكون Skill متاحة تلقائيًا عند تثبيت Plugin.

## القدرات

الميزة | الحالة  
---|---  
الرسائل المباشرة | ✅ مدعومة  
المجموعات/القنوات | ✅ مدعومة (مقيّدة بالإشارة افتراضيًا)  
السلاسل | ✅ مدعومة (ردود تلقائية داخل السلسلة)  
النص الغني | ✅ يتم تحويل Markdown إلى تنسيق Tlon  
الصور | ✅ يتم رفعها إلى تخزين Tlon  
التفاعلات | ✅ عبر Skill المضمّنة  
الاستطلاعات | ❌ غير مدعومة بعد  
الأوامر الأصلية | ✅ مدعومة (للمالك فقط افتراضيًا)  
  
## استكشاف الأخطاء وإصلاحها

شغّل هذا التسلسل أولًا:

bashCopy code
[code]
    openclaw statusopenclaw gateway statusopenclaw logs --followopenclaw doctor
[/code]

الإخفاقات الشائعة:

  * **يتم تجاهل الرسائل المباشرة** : المرسل غير موجود في `dmAllowlist` ولا يوجد `ownerShip` مضبوط لتدفق الموافقة.
  * **يتم تجاهل رسائل المجموعات** : القناة غير مكتشفة أو المرسل غير مصرّح له.
  * **أخطاء الاتصال** : تحقق من إمكانية الوصول إلى عنوان URL الخاص بالسفينة؛ فعّل `allowPrivateNetwork` للسفن المحلية.
  * **أخطاء المصادقة** : تحقق من أن رمز تسجيل الدخول حديث (تتغير الرموز دوريًا).


## مرجع الإعداد

الإعداد الكامل: [الإعداد](</ar/gateway/configuration>)

خيارات المزوّد:

  * `channels.tlon.enabled`: تفعيل/تعطيل بدء تشغيل القناة.
  * `channels.tlon.ship`: اسم سفينة Urbit الخاصة بالبوت (مثل `~sampel-palnet`).
  * `channels.tlon.url`: عنوان URL للسفينة (مثل `https://sampel-palnet.tlon.network`).
  * `channels.tlon.code`: رمز تسجيل الدخول إلى السفينة.
  * `channels.tlon.allowPrivateNetwork`: السماح بعناوين URL الخاصة بـ localhost/LAN (تجاوز SSRF).
  * `channels.tlon.ownerShip`: سفينة المالك لنظام الموافقة (مصرّح لها دائمًا).
  * `channels.tlon.dmAllowlist`: السفن المسموح لها بإرسال رسائل مباشرة (فارغة = لا شيء).
  * `channels.tlon.autoAcceptDmInvites`: قبول الرسائل المباشرة تلقائيًا من السفن الموجودة في قائمة السماح.
  * `channels.tlon.autoAcceptGroupInvites`: قبول دعوات المجموعات تلقائيًا من السفن الموجودة في قائمة السماح.
  * `channels.tlon.groupInviteAllowlist`: السفن التي يمكن قبول دعوات مجموعاتها تلقائيًا.
  * `channels.tlon.autoDiscoverChannels`: اكتشاف القنوات الجماعية تلقائيًا (الافتراضي: true).
  * `channels.tlon.groupChannels`: أعشاش القنوات المثبتة يدويًا.
  * `channels.tlon.defaultAuthorizedShips`: السفن المصرّح لها لكل القنوات.
  * `channels.tlon.authorization.channelRules`: قواعد المصادقة لكل قناة.
  * `channels.tlon.showModelSignature`: إلحاق اسم النموذج بالرسائل.


## ملاحظات

  * تتطلب ردود المجموعات إشارة (مثل `~your-bot-ship`) للرد.
  * ردود السلاسل: إذا كانت الرسالة الواردة ضمن سلسلة، يرد OpenClaw داخل السلسلة.
  * النص الغني: يتم تحويل تنسيق Markdown (غامق، مائل، كود، رؤوس، قوائم) إلى تنسيق Tlon الأصلي.
  * الصور: تُرفع عناوين URL إلى تخزين Tlon وتُضمّن ككتل صور.


## ذات صلة

  * [نظرة عامة على القنوات](</ar/channels>) — كل القنوات المدعومة
  * [الاقتران](</ar/channels/pairing>) — مصادقة الرسائل المباشرة وتدفق الاقتران
  * [المجموعات](</ar/channels/groups>) — سلوك الدردشة الجماعية وتقييدها بالإشارة
  * [توجيه القنوات](</ar/channels/channel-routing>) — توجيه الجلسات للرسائل
  * [الأمان](</ar/gateway/security>) — نموذج الوصول والتقوية


Was this useful?YesNo