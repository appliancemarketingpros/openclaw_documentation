---
title: Mattermost
source_url: https://docs.openclaw.ai/ar/channels/mattermost
scraped_at: 2026-05-25
---

الحالة: Plugin قابل للتنزيل (رمز bot + أحداث WebSocket). القنوات والمجموعات والرسائل المباشرة مدعومة. Mattermost منصة مراسلة فرق قابلة للاستضافة الذاتية؛ راجع الموقع الرسمي على [mattermost.com](<https://mattermost.com>) لتفاصيل المنتج والتنزيلات.

## التثبيت

ثبّت Mattermost قبل تكوين القناة:

### سجل npm

bashCopy code
[code]
    openclaw plugins install @openclaw/mattermost
[/code]

### نسخة محلية

bashCopy code
[code]
    openclaw plugins install ./path/to/local/mattermost-plugin
[/code]

التفاصيل: [Plugins](</ar/tools/plugin>)

## الإعداد السريع

* ### تأكد من توفر Plugin

إصدارات OpenClaw الحالية المعبأة تتضمنه بالفعل. يمكن لعمليات التثبيت الأقدم/المخصصة إضافته يدويًا باستخدام الأوامر أعلاه.

* ### أنشئ bot في Mattermost

أنشئ حساب bot في Mattermost وانسخ **رمز bot**.

* ### انسخ عنوان URL الأساسي

انسخ **عنوان URL الأساسي** لـ Mattermost (مثل `https://chat.example.com`).

* ### كوّن OpenClaw وابدأ Gateway

الحد الأدنى من التكوين:

json5Copy code
[code]
    {  channels: {    mattermost: {      enabled: true,      botToken: "mm-token",      baseUrl: "https://chat.example.com",      dmPolicy: "pairing",    },  },}
[/code]

## أوامر الشرطة المائلة الأصلية

أوامر الشرطة المائلة الأصلية اختيارية. عند تفعيلها، يسجل OpenClaw أوامر الشرطة المائلة `oc_*` عبر API الخاص بـ Mattermost ويتلقى طلبات POST للاستدعاء الراجع على خادم HTTP الخاص بـ Gateway.

json5Copy code
[code]
    {  channels: {    mattermost: {      commands: {        native: true,        nativeSkills: true,        callbackPath: "/api/channels/mattermost/command",        // Use when Mattermost cannot reach the gateway directly (reverse proxy/public URL).        callbackUrl: "https://gateway.example.com/api/channels/mattermost/command",      },    },  },}
[/code]

ملاحظات السلوك

  * الإعداد `native: "auto"` يكون معطلًا افتراضيًا لـ Mattermost. اضبط `native: true` للتفعيل.
  * إذا حُذف `callbackUrl`، يستنتج OpenClaw واحدًا من مضيف/منفذ Gateway + `callbackPath`.
  * في إعدادات الحسابات المتعددة، يمكن ضبط `commands` في المستوى الأعلى أو تحت `channels.mattermost.accounts.<id>.commands` (قيم الحساب تتجاوز حقول المستوى الأعلى).
  * تُتحقق الاستدعاءات الراجعة للأوامر باستخدام رموز كل أمر التي يعيدها Mattermost عندما يسجل OpenClaw أوامر `oc_*`.
  * يحدّث OpenClaw تسجيل أوامر Mattermost الحالي قبل قبول كل استدعاء راجع، بحيث تتوقف الرموز القديمة من أوامر الشرطة المائلة المحذوفة أو المُعاد إنشاؤها عن القبول دون إعادة تشغيل Gateway.
  * يفشل تحقق الاستدعاء الراجع بشكل مغلق إذا تعذر على API الخاص بـ Mattermost تأكيد أن الأمر لا يزال حاليًا؛ تُخزن عمليات التحقق الفاشلة مؤقتًا لفترة وجيزة، وتُدمج عمليات البحث المتزامنة، وتُحدد بدايات البحث الجديدة بمعدل لكل أمر للحد من ضغط إعادة التشغيل.
  * تفشل استدعاءات الشرطة المائلة بشكل مغلق عندما يفشل التسجيل، أو يكون بدء التشغيل جزئيًا، أو لا يطابق رمز الاستدعاء الراجع الرمز المسجل للأمر المحلول (لا يمكن لرمز صالح لأمر واحد الوصول إلى التحقق upstream لأمر مختلف).

متطلب إمكانية الوصول

يجب أن تكون نقطة نهاية الاستدعاء الراجع قابلة للوصول من خادم Mattermost.

  * لا تضبط `callbackUrl` على `localhost` إلا إذا كان Mattermost يعمل على المضيف نفسه/نطاق الشبكة نفسه مثل OpenClaw.
  * لا تضبط `callbackUrl` على عنوان URL الأساسي لـ Mattermost إلا إذا كان ذلك العنوان يمرر عكسيًا `/api/channels/mattermost/command` إلى OpenClaw.
  * فحص سريع هو `curl https://<gateway-host>/api/channels/mattermost/command`؛ يجب أن يعيد طلب GET استجابة `405 Method Not Allowed` من OpenClaw، وليس `404`.

قائمة السماح لخروج Mattermost

إذا كان استدعاؤك الراجع يستهدف عناوين خاصة/tailnet/داخلية، فاضبط Mattermost `ServiceSettings.AllowedUntrustedInternalConnections` ليشمل مضيف/نطاق الاستدعاء الراجع.

استخدم إدخالات مضيف/نطاق، لا عناوين URL كاملة.

  * جيد: `gateway.tailnet-name.ts.net`
  * سيئ: `https://gateway.tailnet-name.ts.net`


## متغيرات البيئة (الحساب الافتراضي)

اضبط هذه على مضيف Gateway إذا كنت تفضل متغيرات البيئة:

  * `MATTERMOST_BOT_TOKEN=...`
  * `MATTERMOST_URL=https://chat.example.com`


## أوضاع الدردشة

يرد Mattermost على الرسائل المباشرة تلقائيًا. يتحكم `chatmode` في سلوك القناة:

### oncall (افتراضي)

الرد فقط عند @الإشارة في القنوات.

### onmessage

الرد على كل رسالة قناة.

### onchar

الرد عندما تبدأ الرسالة ببادئة تشغيل.

مثال تكوين:

json5Copy code
[code]
    {  channels: {    mattermost: {      chatmode: "onchar",      oncharPrefixes: [">", "!"],    },  },}
[/code]

ملاحظات:

  * لا يزال `onchar` يرد على @الإشارات الصريحة.
  * يُحترم `channels.mattermost.requireMention` للتكوينات القديمة، لكن `chatmode` هو المفضل.


## المحادثات المتفرعة والجلسات

استخدم `channels.mattermost.replyToMode` للتحكم في ما إذا كانت ردود القنوات والمجموعات تبقى في القناة الرئيسية أو تبدأ محادثة متفرعة تحت المنشور المُشغّل.

  * `off` (افتراضي): الرد في محادثة متفرعة فقط عندما يكون المنشور الوارد ضمن واحدة بالفعل.
  * `first`: لمنشورات القنوات/المجموعات ذات المستوى الأعلى، ابدأ محادثة متفرعة تحت ذلك المنشور ووجّه المحادثة إلى جلسة محددة بالمحادثة المتفرعة.
  * `all`: السلوك نفسه مثل `first` لـ Mattermost اليوم.
  * تتجاهل الرسائل المباشرة هذا الإعداد وتبقى غير متفرعة.


مثال تكوين:

json5Copy code
[code]
    {  channels: {    mattermost: {      replyToMode: "all",    },  },}
[/code]

ملاحظات:

  * تستخدم الجلسات المحددة بالمحادثة المتفرعة معرف المنشور المُشغّل كجذر للمحادثة المتفرعة.
  * `first` و`all` متكافئان حاليًا لأن Mattermost بمجرد أن يكون لديه جذر محادثة متفرعة، تستمر الأجزاء اللاحقة والوسائط في المحادثة المتفرعة نفسها.


## التحكم في الوصول (الرسائل المباشرة)

  * الافتراضي: `channels.mattermost.dmPolicy = "pairing"` (يحصل المرسلون غير المعروفين على رمز إقران).
  * الموافقة عبر: 
    * `openclaw pairing list mattermost`
    * `openclaw pairing approve mattermost &lt;CODE&gt;`
  * الرسائل المباشرة العامة: `channels.mattermost.dmPolicy="open"` بالإضافة إلى `channels.mattermost.allowFrom=["*"]`.
  * يقبل `channels.mattermost.allowFrom` إدخالات `accessGroup:<name>`. راجع [مجموعات الوصول](</ar/channels/access-groups>).


## القنوات (المجموعات)

  * الافتراضي: `channels.mattermost.groupPolicy = "allowlist"` (مقيدة بالإشارة).
  * اسمح للمرسلين باستخدام `channels.mattermost.groupAllowFrom` (يوصى بمعرفات المستخدمين).
  * يقبل `channels.mattermost.groupAllowFrom` إدخالات `accessGroup:<name>`. راجع [مجموعات الوصول](</ar/channels/access-groups>).
  * توجد تجاوزات الإشارة لكل قناة تحت `channels.mattermost.groups.<channelId>.requireMention` أو `channels.mattermost.groups["*"].requireMention` كقيمة افتراضية.
  * مطابقة `@username` قابلة للتغيير ولا تُفعّل إلا عند `channels.mattermost.dangerouslyAllowNameMatching: true`.
  * القنوات المفتوحة: `channels.mattermost.groupPolicy="open"` (مقيدة بالإشارة).
  * ملاحظة وقت التشغيل: إذا كان `channels.mattermost` مفقودًا تمامًا، يعود وقت التشغيل إلى `groupPolicy="allowlist"` لفحوصات المجموعات (حتى إذا كان `channels.defaults.groupPolicy` مضبوطًا).


مثال:

json5Copy code
[code]
    {  channels: {    mattermost: {      groupPolicy: "open",      groups: {        "*": { requireMention: true },        "team-channel-id": { requireMention: false },      },    },  },}
[/code]

## الأهداف للتسليم الصادر

استخدم صيغ الأهداف هذه مع `openclaw message send` أو cron/webhooks:

  * `channel:<id>` لقناة
  * `user:<id>` لرسالة مباشرة
  * `@username` لرسالة مباشرة (تُحل عبر API الخاص بـ Mattermost)


## إعادة محاولة قناة الرسائل المباشرة

عندما يرسل OpenClaw إلى هدف رسالة مباشرة في Mattermost ويحتاج إلى حل القناة المباشرة أولًا، فإنه يعيد محاولة حالات فشل إنشاء القناة المباشرة العابرة افتراضيًا.

استخدم `channels.mattermost.dmChannelRetry` لضبط هذا السلوك عالميًا لـ Mattermost plugin، أو `channels.mattermost.accounts.<id>.dmChannelRetry` لحساب واحد.

json5Copy code
[code]
    {  channels: {    mattermost: {      dmChannelRetry: {        maxRetries: 3,        initialDelayMs: 1000,        maxDelayMs: 10000,        timeoutMs: 30000,      },    },  },}
[/code]

ملاحظات:

  * ينطبق هذا فقط على إنشاء قناة الرسائل المباشرة (`/api/v4/channels/direct`)، وليس على كل استدعاء API لـ Mattermost.
  * تنطبق إعادة المحاولات على حالات الفشل العابرة مثل حدود المعدل، واستجابات 5xx، وأخطاء الشبكة أو انتهاء المهلة.
  * تُعامل أخطاء العميل 4xx غير `429` على أنها دائمة ولا تُعاد محاولتها.


## بث المعاينة

يبث Mattermost التفكير، ونشاط الأدوات، ونص الرد الجزئي في **منشور معاينة مسودة** واحد يُنهى في مكانه عندما تكون الإجابة النهائية آمنة للإرسال. تُحدّث المعاينة على معرف المنشور نفسه بدل إغراق القناة برسائل لكل جزء. تلغي النهائيات الخاصة بالوسائط/الأخطاء تعديلات المعاينة المعلقة وتستخدم التسليم العادي بدل إرسال منشور معاينة مؤقت.

فعّل عبر `channels.mattermost.streaming`:

json5Copy code
[code]
    {  channels: {    mattermost: {      streaming: "partial", // off | partial | block | progress    },  },}
[/code]

أوضاع البث

  * `partial` هو الخيار المعتاد: منشور معاينة واحد يُحرر مع نمو الرد، ثم يُنهى بالإجابة الكاملة.
  * يستخدم `block` أجزاء مسودة بأسلوب الإلحاق داخل منشور المعاينة.
  * يعرض `progress` معاينة حالة أثناء التوليد ولا ينشر الإجابة النهائية إلا عند الاكتمال.
  * يعطل `off` بث المعاينة.

ملاحظات سلوك البث

  * إذا تعذر إنهاء البث في مكانه (على سبيل المثال إذا حُذف المنشور أثناء البث)، يعود OpenClaw إلى إرسال منشور نهائي جديد حتى لا يضيع الرد أبدًا.
  * تُحجب الحمولات المخصصة للاستدلال فقط عن منشورات القناة، بما في ذلك النص الذي يصل كاقتباس `> Reasoning:`. اضبط `/reasoning on` لرؤية التفكير في أسطح أخرى؛ يحتفظ المنشور النهائي في Mattermost بالإجابة فقط.
  * راجع [البث](</ar/concepts/streaming#preview-streaming-modes>) لمصفوفة ربط القنوات.


## التفاعلات (أداة الرسائل)

  * استخدم `message action=react` مع `channel=mattermost`.
  * `messageId` هو معرف منشور Mattermost.
  * يقبل `emoji` أسماء مثل `thumbsup` أو `:+1:` (النقطتان اختياريتان).
  * اضبط `remove=true` (منطقي) لإزالة تفاعل.
  * تُمرر أحداث إضافة/إزالة التفاعل كأحداث نظام إلى جلسة الوكيل الموجهة.


أمثلة:

CodeCopy code
[code]
    message action=react channel=mattermost target=channel:<channelId> messageId=<postId> emoji=thumbsupmessage action=react channel=mattermost target=channel:<channelId> messageId=<postId> emoji=thumbsup remove=true
[/code]

التكوين:

  * `channels.mattermost.actions.reactions`: تفعيل/تعطيل إجراءات التفاعل (افتراضيًا true).
  * تجاوز لكل حساب: `channels.mattermost.accounts.<id>.actions.reactions`.


## الأزرار التفاعلية (أداة الرسائل)

أرسل رسائل تحتوي على أزرار قابلة للنقر. عندما ينقر مستخدم زرًا، يتلقى الوكيل التحديد ويمكنه الرد.

فعّل الأزرار بإضافة `inlineButtons` إلى إمكانات القناة:

json5Copy code
[code]
    {  channels: {    mattermost: {      capabilities: ["inlineButtons"],    },  },}
[/code]

استخدم `message action=send` مع معلمة `buttons`. الأزرار مصفوفة ثنائية الأبعاد (صفوف من الأزرار):

CodeCopy code
[code]
    message action=send channel=mattermost target=channel:<channelId> buttons=[[{"text":"Yes","callback_data":"yes"},{"text":"No","callback_data":"no"}]]
[/code]

حقول الأزرار:

تسمية العرض.

القيمة المرسلة مرة أخرى عند النقر (تُستخدم كمعرّف الإجراء).

نمط الزر.

عندما ينقر مستخدم على زر:

* ### Buttons replaced with confirmation

تُستبدل جميع الأزرار بسطر تأكيد (مثل، "✓ **Yes** selected by @user").

* ### Agent receives the selection

يتلقى الوكيل التحديد كرسالة واردة ويرد.

Implementation notes

  * تستخدم استدعاءات الأزرار التحقق عبر HMAC-SHA256 (تلقائي، ولا يحتاج إلى إعداد).
  * يزيل Mattermost بيانات الاستدعاء من استجابات API الخاصة به (ميزة أمان)، لذلك تُزال جميع الأزرار عند النقر - ولا يمكن الإزالة الجزئية.
  * تُنظَّف معرّفات الإجراءات التي تحتوي على واصلات أو شرطات سفلية تلقائيًا (قيد في توجيه Mattermost).

Config and reachability

  * `channels.mattermost.capabilities`: مصفوفة من سلاسل الإمكانات. أضف `"inlineButtons"` لتفعيل وصف أداة الأزرار في موجّه نظام الوكيل.
  * `channels.mattermost.interactions.callbackBaseUrl`: عنوان URL أساسي خارجي اختياري لاستدعاءات الأزرار (مثل `https://gateway.example.com`). استخدم هذا عندما لا يستطيع Mattermost الوصول إلى Gateway مباشرة على مضيف الربط الخاص به.
  * في إعدادات الحسابات المتعددة، يمكنك أيضًا ضبط الحقل نفسه ضمن `channels.mattermost.accounts.<id>.interactions.callbackBaseUrl`.
  * إذا حُذف `interactions.callbackBaseUrl`، يستنتج OpenClaw عنوان URL للاستدعاء من `gateway.customBindHost` \+ `gateway.port`، ثم يعود إلى `http://localhost:<port>`.
  * قاعدة قابلية الوصول: يجب أن يكون عنوان URL لاستدعاء الزر قابلًا للوصول من خادم Mattermost. يعمل `localhost` فقط عندما يعمل Mattermost وOpenClaw على المضيف نفسه/مساحة اسم الشبكة نفسها.
  * إذا كان هدف الاستدعاء خاصًا/ضمن tailnet/داخليًا، فأضف مضيفه/نطاقه إلى `ServiceSettings.AllowedUntrustedInternalConnections` في Mattermost.


### تكامل API مباشر (نصوص خارجية)

يمكن للنصوص الخارجية وwebhooks نشر الأزرار مباشرة عبر Mattermost REST API بدلًا من المرور عبر أداة `message` الخاصة بالوكيل. استخدم `buildButtonAttachments()` من Plugin عند الإمكان؛ وإذا كنت تنشر JSON خامًا، فاتبع هذه القواعد:

**بنية الحمولة:**

json5Copy code
[code]
    {  channel_id: "<channelId>",  message: "Choose an option:",  props: {    attachments: [      {        actions: [          {            id: "mybutton01", // alphanumeric only - see below            type: "button", // required, or clicks are silently ignored            name: "Approve", // display label            style: "primary", // optional: "default", "primary", "danger"            integration: {              url: "https://gateway.example.com/mattermost/interactions/default",              context: {                action_id: "mybutton01", // must match button id (for name lookup)                action: "approve",                // ... any custom fields ...                _token: "<hmac>", // see HMAC section below              },            },          },        ],      },    ],  },}
[/code]

**إنشاء رمز HMAC**

يتحقق Gateway من نقرات الأزرار باستخدام HMAC-SHA256. يجب أن تنشئ النصوص الخارجية رموزًا تطابق منطق التحقق في Gateway:

* ### Derive the secret from the bot token

`HMAC-SHA256(key="openclaw-mattermost-interactions", data=botToken)`

* ### Build the context object

ابنِ كائن السياق بكل الحقول **ما عدا** `_token`.

* ### Serialize with sorted keys

سلْسل باستخدام **مفاتيح مرتبة** ومن دون **مسافات** (يستخدم Gateway ‏`JSON.stringify` مع مفاتيح مرتبة، ما ينتج خرجًا مضغوطًا).

* ### Sign the payload

`HMAC-SHA256(key=secret, data=serializedContext)`

* ### Add the token

أضف ملخص hex الناتج كقيمة `_token` في السياق.

مثال Python:

pythonCopy code
[code]
     secret = hmac.new(    b"openclaw-mattermost-interactions",    bot_token.encode(), hashlib.sha256).hexdigest() ctx = {"action_id": "mybutton01", "action": "approve"}payload = json.dumps(ctx, sort_keys=True, separators=(",", ":"))token = hmac.new(secret.encode(), payload.encode(), hashlib.sha256).hexdigest() context = {**ctx, "_token": token}
[/code]

Common HMAC pitfalls

  * يضيف `json.dumps` في Python مسافات افتراضيًا (`{"key": "val"}`). استخدم `separators=(",", ":")` لمطابقة خرج JavaScript المضغوط (`{"key":"val"}`).
  * وقّع دائمًا **كل** حقول السياق (باستثناء `_token`). يزيل Gateway ‏`_token` ثم يوقّع كل ما تبقى. يؤدي توقيع مجموعة فرعية إلى فشل تحقق صامت.
  * استخدم `sort_keys=True` \- يرتب Gateway المفاتيح قبل التوقيع، وقد يعيد Mattermost ترتيب حقول السياق عند تخزين الحمولة.
  * اشتق السر من رمز البوت (حتمي)، وليس من بايتات عشوائية. يجب أن يكون السر نفسه عبر العملية التي تنشئ الأزرار وGateway الذي يتحقق منها.


## محوّل الدليل

يتضمن Mattermost Plugin محوّل دليل يحل أسماء القنوات والمستخدمين عبر Mattermost API. يتيح ذلك أهداف `#channel-name` و`@username` في `openclaw message send` وتسليمات cron/webhook.

لا حاجة إلى إعداد - يستخدم المحوّل رمز البوت من إعداد الحساب.

## حسابات متعددة

يدعم Mattermost حسابات متعددة ضمن `channels.mattermost.accounts`:

json5Copy code
[code]
    {  channels: {    mattermost: {      accounts: {        default: { name: "Primary", botToken: "mm-token", baseUrl: "https://chat.example.com" },        alerts: { name: "Alerts", botToken: "mm-token-2", baseUrl: "https://alerts.example.com" },      },    },  },}
[/code]

## استكشاف الأخطاء وإصلاحها

No replies in channels

تأكد من أن البوت موجود في القناة واذكره (oncall)، أو استخدم بادئة تشغيل (onchar)، أو اضبط `chatmode: "onmessage"`.

Auth or multi-account errors

  * تحقق من رمز البوت، وعنوان URL الأساسي، وما إذا كان الحساب مفعّلًا.
  * مشكلات الحسابات المتعددة: تنطبق متغيرات البيئة فقط على حساب `default`.

Native slash commands fail

  * `Unauthorized: invalid command token.`: لم يقبل OpenClaw رمز الاستدعاء. الأسباب المعتادة: 
    * فشل تسجيل أمر الشرطة المائلة أو اكتمل جزئيًا فقط عند بدء التشغيل
    * يصل الاستدعاء إلى Gateway/الحساب الخطأ
    * لا تزال لدى Mattermost أوامر قديمة تشير إلى هدف استدعاء سابق
    * أُعيد تشغيل Gateway من دون إعادة تنشيط أوامر الشرطة المائلة
  * إذا توقفت أوامر الشرطة المائلة الأصلية عن العمل، فتحقق من السجلات بحثًا عن `mattermost: failed to register slash commands` أو `mattermost: native slash commands enabled but no commands could be registered`.
  * إذا حُذف `callbackUrl` وحذرت السجلات من أن الاستدعاء حُل إلى `http://127.0.0.1:18789/...`، فمن المرجح أن عنوان URL هذا لا يمكن الوصول إليه إلا عندما يعمل Mattermost على المضيف نفسه/مساحة اسم الشبكة نفسها مثل OpenClaw. اضبط بدلًا من ذلك `commands.callbackUrl` صريحًا وقابلًا للوصول خارجيًا.

Buttons issues

  * تظهر الأزرار كمربعات بيضاء: قد يرسل الوكيل بيانات أزرار غير صحيحة. تحقق من أن كل زر يحتوي على حقلي `text` و`callback_data`.
  * تُعرض الأزرار لكن النقرات لا تفعل شيئًا: تحقق من أن `AllowedUntrustedInternalConnections` في إعداد خادم Mattermost يتضمن `127.0.0.1 localhost`، وأن `EnablePostActionIntegration` قيمته `true` في ServiceSettings.
  * ترجع الأزرار 404 عند النقر: من المرجح أن `id` الزر يحتوي على واصلات أو شرطات سفلية. يتعطل موجّه الإجراءات في Mattermost عند المعرّفات غير الأبجدية الرقمية. استخدم `[a-zA-Z0-9]` فقط.
  * تسجل Gateway ‏`invalid _token`: عدم تطابق HMAC. تحقق من أنك توقّع كل حقول السياق (وليس مجموعة فرعية)، وتستخدم مفاتيح مرتبة، وتستخدم JSON مضغوطًا (بلا مسافات). راجع قسم HMAC أعلاه.
  * تسجل Gateway ‏`missing _token in context`: حقل `_token` غير موجود في سياق الزر. تأكد من تضمينه عند بناء حمولة التكامل.
  * يعرض التأكيد معرّفًا خامًا بدلًا من اسم الزر: `context.action_id` لا يطابق `id` الزر. اضبط كليهما على القيمة المنظّفة نفسها.
  * لا يعرف الوكيل شيئًا عن الأزرار: أضف `capabilities: ["inlineButtons"]` إلى إعداد قناة Mattermost.


## ذات صلة

  * [توجيه القنوات](</ar/channels/channel-routing>) \- توجيه الجلسات للرسائل
  * [نظرة عامة على القنوات](</ar/channels>) \- جميع القنوات المدعومة
  * [المجموعات](</ar/channels/groups>) \- سلوك الدردشة الجماعية وبوابة الإشارة
  * [الاقتران](</ar/channels/pairing>) \- مصادقة الرسائل المباشرة وتدفق الاقتران
  * [الأمان](</ar/gateway/security>) \- نموذج الوصول والتقوية


Was this useful?YesNo