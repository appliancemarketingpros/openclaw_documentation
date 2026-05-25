---
title: Twitch
source_url: https://docs.openclaw.ai/ar/channels/twitch
scraped_at: 2026-05-25
---

دعم دردشة Twitch عبر اتصال IRC. يتصل OpenClaw بصفته مستخدم Twitch (حساب بوت) لاستقبال الرسائل وإرسالها في القنوات.

## Plugin مضمّن

إذا كنت تستخدم إصدارًا أقدم أو تثبيتًا مخصصًا يستبعد Twitch، فثبّت حزمة npm مباشرة:

### سجل npm

bashCopy code
[code]
    openclaw plugins install @openclaw/twitch
[/code]

### نسخة محلية

bashCopy code
[code]
    openclaw plugins install ./path/to/local/twitch-plugin
[/code]

استخدم الحزمة المجردة لمتابعة وسم الإصدار الرسمي الحالي. ثبّت إصدارًا دقيقًا فقط عندما تحتاج إلى تثبيت قابل لإعادة الإنتاج.

التفاصيل: [Plugins](</ar/tools/plugin>)

## إعداد سريع (للمبتدئين)

* ### تأكد من توفر Plugin

إصدارات OpenClaw المعبأة الحالية تضمنه بالفعل. يمكن للتثبيتات الأقدم/المخصصة إضافته يدويًا بالأوامر أعلاه.

* ### أنشئ حساب بوت Twitch

أنشئ حساب Twitch مخصصًا للبوت (أو استخدم حسابًا موجودًا).

* ### أنشئ بيانات الاعتماد

استخدم [مولّد رموز Twitch](<https://twitchtokengenerator.com/>):

  * اختر **رمز البوت**
  * تحقق من تحديد النطاقين `chat:read` و`chat:write`
  * انسخ **معرّف العميل** و**رمز الوصول**


* ### اعثر على معرّف مستخدم Twitch الخاص بك

استخدم <https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/> لتحويل اسم مستخدم إلى معرّف مستخدم Twitch.

* ### اضبط الرمز

  * متغير البيئة: `OPENCLAW_TWITCH_ACCESS_TOKEN=...` (الحساب الافتراضي فقط)
  * أو الإعداد: `channels.twitch.accessToken`


إذا تم ضبطهما معًا، تكون للأعداد أولوية (الرجوع إلى متغير البيئة للحساب الافتراضي فقط).

* ### شغّل Gateway

شغّل Gateway بالقناة المضبوطة.

الحد الأدنى من الإعداد:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw", // Bot's Twitch account      accessToken: "oauth:abc123...", // OAuth Access Token (or use OPENCLAW_TWITCH_ACCESS_TOKEN env var)      clientId: "xyz789...", // Client ID from Token Generator      channel: "vevisk", // Which Twitch channel's chat to join (required)      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only - get it from https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/    },  },}
[/code]

## ما هو

  * قناة Twitch يملكها Gateway.
  * توجيه حتمي: تعود الردود دائمًا إلى Twitch.
  * يرتبط كل حساب بمفتاح جلسة معزول `agent:<agentId>:twitch:<accountName>`.
  * `username` هو حساب البوت (الذي يصادق)، و`channel` هي غرفة الدردشة التي سينضم إليها.


## الإعداد (مفصل)

### إنشاء بيانات الاعتماد

استخدم [مولّد رموز Twitch](<https://twitchtokengenerator.com/>):

  * اختر **رمز البوت**
  * تحقق من تحديد النطاقين `chat:read` و`chat:write`
  * انسخ **معرّف العميل** و**رمز الوصول**


### ضبط البوت

### متغير البيئة (الحساب الافتراضي فقط)

bashCopy code
[code]
    OPENCLAW_TWITCH_ACCESS_TOKEN=oauth:abc123...
[/code]

### الإعداد

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",    },  },}
[/code]

إذا تم ضبط متغير البيئة والإعداد معًا، تكون للأعداد أولوية.

### التحكم في الوصول (موصى به)

json5Copy code
[code]
    {  channels: {    twitch: {      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only    },  },}
[/code]

فضّل `allowFrom` لقائمة سماح صارمة. استخدم `allowedRoles` بدلًا من ذلك إذا كنت تريد وصولًا قائمًا على الأدوار.

**الأدوار المتاحة:** `"moderator"`، `"owner"`، `"vip"`، `"subscriber"`، `"all"`.

## تحديث الرمز (اختياري)

لا يمكن تحديث الرموز من [مولّد رموز Twitch](<https://twitchtokengenerator.com/>) تلقائيًا - أعد إنشاءها عند انتهاء الصلاحية.

للتحديث التلقائي للرمز، أنشئ تطبيق Twitch الخاص بك في [وحدة تحكم مطوري Twitch](<https://dev.twitch.tv/console>) وأضفه إلى الإعداد:

json5Copy code
[code]
    {  channels: {    twitch: {      clientSecret: "your_client_secret",      refreshToken: "your_refresh_token",    },  },}
[/code]

يحدّث البوت الرموز تلقائيًا قبل انتهاء الصلاحية ويسجل أحداث التحديث.

## دعم الحسابات المتعددة

استخدم `channels.twitch.accounts` مع رموز لكل حساب. راجع [الإعدادات](</ar/gateway/configuration>) للنمط المشترك.

مثال (حساب بوت واحد في قناتين):

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        channel1: {          username: "openclaw",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "vevisk",        },        channel2: {          username: "openclaw",          accessToken: "oauth:def456...",          clientId: "uvw012...",          channel: "secondchannel",        },      },    },  },}
[/code]

## التحكم في الوصول

### قائمة سماح لمعرّفات المستخدمين (الأكثر أمانًا)

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowFrom: ["123456789", "987654321"],        },      },    },  },}
[/code]

### قائم على الدور

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowedRoles: ["moderator", "vip"],        },      },    },  },}
[/code]

`allowFrom` هي قائمة سماح صارمة. عند ضبطها، يُسمح فقط لمعرّفات المستخدمين هذه. إذا كنت تريد وصولًا قائمًا على الأدوار، فاترك `allowFrom` غير مضبوطة واضبط `allowedRoles` بدلًا من ذلك.

### تعطيل شرط @mention

افتراضيًا، `requireMention` هي `true`. للتعطيل والرد على جميع الرسائل:

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          requireMention: false,        },      },    },  },}
[/code]

## استكشاف الأخطاء وإصلاحها

أولًا، شغّل أوامر التشخيص:

bashCopy code
[code]
    openclaw doctoropenclaw channels status --probe
[/code]

البوت لا يرد على الرسائل

  * **تحقق من التحكم في الوصول:** تأكد من وجود معرّف المستخدم الخاص بك في `allowFrom`، أو أزل `allowFrom` مؤقتًا واضبط `allowedRoles: ["all"]` للاختبار.
  * **تحقق من وجود البوت في القناة:** يجب أن ينضم البوت إلى القناة المحددة في `channel`.

مشكلات الرمز

أخطاء "فشل الاتصال" أو أخطاء المصادقة:

  * تحقق من أن `accessToken` هو قيمة رمز وصول OAuth (عادةً يبدأ بالبادئة `oauth:`)
  * تحقق من أن الرمز يحتوي على نطاقي `chat:read` و`chat:write`
  * إذا كنت تستخدم تحديث الرمز، فتحقق من ضبط `clientSecret` و`refreshToken`

تحديث الرمز لا يعمل

تحقق من السجلات بحثًا عن أحداث التحديث:

CodeCopy code
[code]
    Using env token source for mybotAccess token refreshed for user 123456 (expires in 14400s)
[/code]

إذا رأيت "token refresh disabled (no refresh token)":

  * تأكد من توفير `clientSecret`
  * تأكد من توفير `refreshToken`


## الإعدادات

### إعداد الحساب

اسم مستخدم البوت.

رمز وصول OAuth مع `chat:read` و`chat:write`.

معرّف عميل Twitch (من مولّد الرموز أو تطبيقك).

القناة المراد الانضمام إليها.

فعّل هذا الحساب.

اختياري: للتحديث التلقائي للرمز.

اختياري: للتحديث التلقائي للرمز.

انتهاء صلاحية الرمز بالثواني.

الطابع الزمني للحصول على الرمز.

قائمة سماح لمعرّفات المستخدمين.

يتطلب @mention.

### خيارات المزوّد

  * `channels.twitch.enabled` \- تفعيل/تعطيل بدء تشغيل القناة
  * `channels.twitch.username` \- اسم مستخدم البوت (إعداد مبسط لحساب واحد)
  * `channels.twitch.accessToken` \- رمز وصول OAuth (إعداد مبسط لحساب واحد)
  * `channels.twitch.clientId` \- معرّف عميل Twitch (إعداد مبسط لحساب واحد)
  * `channels.twitch.channel` \- القناة المراد الانضمام إليها (إعداد مبسط لحساب واحد)
  * `channels.twitch.accounts.<accountName>` \- إعداد حسابات متعددة (كل حقول الحساب أعلاه)


مثال كامل:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",      clientSecret: "secret123...",      refreshToken: "refresh456...",      allowFrom: ["123456789"],      allowedRoles: ["moderator", "vip"],      accounts: {        default: {          username: "mybot",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "your_channel",          enabled: true,          clientSecret: "secret123...",          refreshToken: "refresh456...",          expiresIn: 14400,          obtainmentTimestamp: 1706092800000,          allowFrom: ["123456789", "987654321"],          allowedRoles: ["moderator"],        },      },    },  },}
[/code]

## إجراءات الأدوات

يمكن للوكيل استدعاء `twitch` بالإجراء:

  * `send` \- إرسال رسالة إلى قناة


مثال:

json5Copy code
[code]
    {  action: "twitch",  params: {    message: "Hello Twitch!",    to: "#mychannel",  },}
[/code]

## السلامة والعمليات

  * **عامل الرموز مثل كلمات المرور** — لا تلتزم بالرموز في git أبدًا.
  * **استخدم التحديث التلقائي للرموز** للبوتات طويلة التشغيل.
  * **استخدم قوائم السماح لمعرّفات المستخدمين** بدلًا من أسماء المستخدمين للتحكم في الوصول.
  * **راقب السجلات** لأحداث تحديث الرموز وحالة الاتصال.
  * **اجعل نطاق الرموز في الحد الأدنى** — اطلب فقط `chat:read` و`chat:write`.
  * **إذا تعثرت** : أعد تشغيل Gateway بعد التأكد من عدم امتلاك أي عملية أخرى للجلسة.


## الحدود

  * **500 حرف** لكل رسالة (تقسيم تلقائي عند حدود الكلمات).
  * تتم إزالة Markdown قبل التقسيم.
  * لا يوجد تحديد معدل (يستخدم حدود المعدل المدمجة في Twitch).


## ذات صلة

  * [توجيه القنوات](</ar/channels/channel-routing>) — توجيه الجلسات للرسائل
  * [نظرة عامة على القنوات](</ar/channels>) — كل القنوات المدعومة
  * [المجموعات](</ar/channels/groups>) — سلوك دردشة المجموعات وبوابة الذكر
  * [الاقتران](</ar/channels/pairing>) — مصادقة الرسائل المباشرة وتدفق الاقتران
  * [الأمان](</ar/gateway/security>) — نموذج الوصول والتقوية


Was this useful?YesNo