---
title: الرسائل القصيرة
source_url: https://docs.openclaw.ai/ar/channels/sms
scraped_at: 2026-06-29
---

Get started

يمكن لـ OpenClaw استلام رسائل SMS وإرسالها عبر رقم هاتف Twilio أو Messaging Service. يسجل Gateway مسار Webhook واردًا، ويتحقق افتراضيًا من توقيعات طلبات Twilio، ويرسل الردود مرة أخرى عبر Messages API في Twilio.

[**الإقران** سياسة الرسائل المباشرة الافتراضية لـ SMS هي الإقران. ](</ar/channels/pairing>) [**أمان Gateway** راجع تعرّض Webhook للإنترنت وضوابط وصول المرسلين. ](</ar/gateway/security>) [**استكشاف أخطاء القنوات وإصلاحها** تشخيصات عبر القنوات وخطط إصلاح. ](</ar/channels/troubleshooting>)

## قبل أن تبدأ

تحتاج إلى:

  * تثبيت Plugin SMS الرسمي باستخدام `openclaw plugins install @openclaw/sms`.
  * حساب Twilio مع رقم هاتف يدعم SMS، أو Twilio Messaging Service.
  * Account SID و Auth Token من Twilio.
  * عنوان URL عام عبر HTTPS يصل إلى OpenClaw Gateway.
  * اختيار سياسة مرسل: `pairing` للاستخدام الخاص، أو `allowlist` لأرقام الهواتف الموافق عليها مسبقًا، أو `open` فقط للوصول العام المقصود عبر SMS.


استخدم رقم Twilio واحدًا لكل من SMS و Voice Call إذا كان الرقم يدعم كلتا الميزتين. اضبط Webhook الخاص بـ SMS و Webhook الخاص بالصوت كلًا على حدة في Twilio؛ تغطي هذه الصفحة Webhook الخاص بـ SMS فقط.

## الإعداد السريع

* ### ثبّت Plugin

bashCopy code
[code]
    openclaw plugins install @openclaw/sms
[/code]

* ### أنشئ مرسل Twilio أو اختر واحدًا

في Twilio، افتح **Phone Numbers > Manage > Active numbers** واختر رقمًا يدعم SMS. احفظ:

  * Account SID، مثلًا `ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
  * Auth Token
  * رقم هاتف المرسل، مثلًا `+15551234567`


إذا كنت تستخدم Messaging Service بدلًا من رقم مرسل ثابت، فاحفظ Messaging Service SID، مثلًا `MGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`.

* ### اضبط قناة SMS

احفظ هذا باسم `sms.patch.json5` وغيّر العناصر النائبة:

json5Copy code
[code]
    {channels: {sms: {  enabled: true,  accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  authToken: "twilio-auth-token",  fromNumber: "+15551234567",  publicWebhookUrl: "https://gateway.example.com/webhooks/sms",  dmPolicy: "pairing",},},}
[/code]

طبّقه:

bashCopy code
[code]
    openclaw config patch --file ./sms.patch.json5 --dry-runopenclaw config patch --file ./sms.patch.json5
[/code]

* ### وجّه Twilio إلى Webhook الخاص بـ Gateway

في إعدادات رقم هاتف Twilio، افتح **Messaging** واضبط **A message comes in** على:

textCopy code
[code]
    https://gateway.example.com/webhooks/sms
[/code]

استخدم HTTP `POST`. المسار المحلي الافتراضي هو `/webhooks/sms`؛ غيّر `channels.sms.webhookPath` إذا كنت تحتاج إلى مسار مختلف.

* ### اكشف مسار Webhook الدقيق لـ SMS

يجب أن يوجّه عنوان URL العام لديك مسار SMS إلى عملية Gateway. إذا كنت تستخدم Tailscale Funnel للاختبار المحلي، فاكشف `/webhooks/sms` صراحةً:

bashCopy code
[code]
    tailscale funnel --bg --set-path /webhooks/sms http://127.0.0.1:<gateway-port>/webhooks/smstailscale funnel status
[/code]

يستخدم Voice Call و SMS مسارات Webhook منفصلة. إذا كان رقم Twilio نفسه يتعامل مع كليهما، فأبقِ كلا المسارين مضبوطين في Twilio وفي النفق لديك.

* ### ابدأ Gateway ووافق على أول مرسل

bashCopy code
[code]
    openclaw gateway
[/code]

أرسل رسالة نصية إلى رقم Twilio. تنشئ الرسالة الأولى طلب إقران. وافق عليه:

bashCopy code
[code]
    openclaw pairing list smsopenclaw pairing approve sms &lt;CODE&gt;
[/code]

تنتهي صلاحية رموز الإقران بعد ساعة واحدة.

## أمثلة التهيئة

### ملف التهيئة

استخدم إعداد ملف التهيئة عندما تريد أن ينتقل تعريف القناة مع تهيئة Gateway:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

### متغيرات البيئة

استخدم إعداد env لعمليات النشر ذات الحساب الواحد عندما تأتي الأسرار من بيئة المضيف:

bashCopy code
[code]
    export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"export TWILIO_AUTH_TOKEN="<twilio-auth-token>"export TWILIO_PHONE_NUMBER="+15551234567"export SMS_PUBLIC_WEBHOOK_URL="https://gateway.example.com/webhooks/sms"
[/code]

ثم فعّل القناة في التهيئة:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

يُقبل `TWILIO_SMS_FROM` كاسم بديل لـ `TWILIO_PHONE_NUMBER`. استخدم `TWILIO_MESSAGING_SERVICE_SID` بدلًا من مرسل رقم الهاتف عندما ينبغي أن يختار Twilio المرسل من Messaging Service.

### رمز مصادقة SecretRef

يمكن أن يكون `authToken` من نوع SecretRef. استخدم هذا عندما ينبغي أن يحل Gateway قيمة Twilio Auth Token من بيئة تشغيل أسرار OpenClaw بدلًا من تخزين تهيئة نصية صريحة:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: { source: "env", provider: "default", id: "TWILIO_AUTH_TOKEN" },      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

يجب أن يكون متغير البيئة المشار إليه أو موفر الأسرار مرئيًا لبيئة تشغيل Gateway. أعد تشغيل عمليات Gateway المُدارة بعد تغيير متغيرات بيئة المضيف.

### رقم خاص بقائمة سماح فقط

استخدم `allowlist` عندما ينبغي أن تتمكن أرقام الهواتف المعروفة فقط من التحدث إلى الوكيل:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "allowlist",      allowFrom: ["+15557654321"],    },  },}
[/code]

### مرسل Messaging Service

استخدم `messagingServiceSid` بدلًا من `fromNumber` عندما ينبغي أن يختار Twilio المرسل عبر Messaging Service:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      messagingServiceSid: "MGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

إذا كان كل من `fromNumber` و `messagingServiceSid` موجودين بعد حل التهيئة و env، فسيُستخدم `fromNumber`.

### الهدف الصادر الافتراضي

اضبط `defaultTo` عندما ينبغي أن يكون للأتمتة أو التسليم الذي يبدأه الوكيل وجهة افتراضية إذا أغفل مسار الإرسال هدفًا صريحًا:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      defaultTo: "+15557654321",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",    },  },}
[/code]

## التحكم في الوصول

يتحكم `channels.sms.dmPolicy` في الوصول المباشر عبر SMS:

  * `pairing` (افتراضي)
  * `allowlist` (يتطلب مرسلًا واحدًا على الأقل في `allowFrom`)
  * `open` (يتطلب أن يتضمن `allowFrom` القيمة `"*"`)
  * `disabled`


ينبغي أن تكون إدخالات `allowFrom` أرقام هواتف بصيغة E.164 مثل `+15551234567`. تُقبل بادئات `sms:` وتُطبّع. لمساعد خاص، فضّل `dmPolicy: "allowlist"` مع أرقام هواتف صريحة.

## إرسال SMS

تستخدم أهداف SMS الصادرة بادئة الخدمة `sms:` مع تحديد قناة SMS:

bashCopy code
[code]
    openclaw message send --channel sms --target sms:+15551234567 --message "hello"
[/code]

عندما يكون اختيار القناة ضمنيًا، يحدد `twilio-sms:+15551234567` هذه القناة دون الاستحواذ على بادئة الخدمة الحالية `sms:` المملوكة للقناة والمستخدمة بواسطة iMessage.

bashCopy code
[code]
    openclaw message send --target twilio-sms:+15551234567 --message "hello"
[/code]

يتطلب CLI تحديد `--target` صراحةً. `defaultTo` مخصص لمسارات الأتمتة والتسليم التي يبدأها الوكيل حيث يمكن حل الهدف من تهيئة القناة.

تعود ردود الوكيل من محادثات SMS الواردة تلقائيًا إلى المرسل عبر مرسل Twilio المضبوط.

مخرجات SMS نص عادي. يزيل OpenClaw تنسيق markdown، ويسطّح كتل التعليمات البرمجية المسيّجة، ويحافظ على الروابط القابلة للقراءة، ويقسّم الردود الطويلة قبل إرسالها عبر Twilio.

## التحقق من الإعداد

بعد بدء Gateway:

  1. تأكد من أن سجل Gateway يعرض مسار Webhook الخاص بـ SMS.
  2. شغّل اختبارًا من جانب Twilio:

bashCopy code
[code]
    openclaw channels capabilities --channel smsopenclaw channels status --channel sms --probe --json
[/code]

  3. أرسل SMS إلى رقم Twilio من هاتفك.
  4. شغّل `openclaw pairing list sms`.
  5. وافق على رمز الإقران باستخدام `openclaw pairing approve sms &lt;CODE&gt;`.
  6. أرسل SMS أخرى وتأكد من أن الوكيل يرد.


لاختبار الإرسال الصادر فقط، استخدم:

bashCopy code
[code]
    openclaw message send --channel sms --target sms:+15557654321 --message "OpenClaw SMS test"
[/code]

### اختبار شامل من macOS iMessage/SMS

على Mac يمكنه إرسال SMS عبر شركة الاتصالات من خلال Messages، يمكنك استخدام `imsg` لتشغيل جانب المرسل دون لمس هاتفك:

bashCopy code
[code]
    imsg send --to "+15551234567" --service sms --text "OpenClaw SMS E2E $(date -u +%Y%m%dT%H%M%SZ)" --jsonopenclaw pairing list smsopenclaw pairing approve sms &lt;CODE&gt;imsg send --to "+15551234567" --service sms --text "reply exactly SMS pong" --json
[/code]

ينبغي أن تنشئ الرسالة الأولى طلب إقران. ينبغي أن تتلقى الرسالة الثانية رد الوكيل عبر Twilio.

## أمان Webhook

افتراضيًا، يتحقق OpenClaw من `X-Twilio-Signature` باستخدام `publicWebhookUrl` و `authToken`. أبقِ `publicWebhookUrl` مطابقًا حرفيًا لعنوان URL المضبوط في Twilio، بما في ذلك المخطط والمضيف والمسار وسلسلة الاستعلام.

لاختبار النفق المحلي فقط، يمكنك ضبط:

json5Copy code
[code]
    {  channels: {    sms: {      dangerouslyDisableSignatureValidation: true,    },  },}
[/code]

لا تستخدم التحقق المعطل من التوقيع على Gateway عام.

## تهيئة متعددة الحسابات

استخدم `accounts` عندما تدير أكثر من رقم Twilio واحد:

json5Copy code
[code]
    {  channels: {    sms: {      accounts: {        support: {          enabled: true,          accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",          authToken: "twilio-auth-token",          fromNumber: "+15551234567",          publicWebhookUrl: "https://gateway.example.com/webhooks/sms/support",          webhookPath: "/webhooks/sms/support",          dmPolicy: "allowlist",          allowFrom: ["+15557654321"],        },      },    },  },}
[/code]

ينبغي أن يستخدم كل حساب `webhookPath` مميزًا.

## استكشاف الأخطاء وإصلاحها

### يُرجع Twilio 403 أو يرفض OpenClaw الـ Webhook

تحقق من أن `publicWebhookUrl` يطابق تمامًا عنوان URL المضبوط في Twilio، بما في ذلك المخطط والمضيف والمسار وسلسلة الاستعلام. يوقّع Twilio سلسلة عنوان URL العامة، لذلك يمكن أن تؤدي عمليات إعادة كتابة الوكيل وأسماء المضيف البديلة إلى كسر التحقق من التوقيع.

### لا يظهر طلب إقران

تحقق من عنوان URL وطريقة Webhook في **Messaging** لرقم Twilio. يجب أن يشير إلى عنوان URL الخاص بـ Webhook لـ SMS وأن يستخدم `POST`. تأكد أيضًا من أن Gateway قابل للوصول من الإنترنت العام أو عبر النفق لديك.

إذا أظهر سجل رسائل Twilio الخطأ `11200`، فهذا يعني أن Twilio قبل SMS الواردة لكنه لم يتمكن من الوصول إلى Webhook لديك. تحقق مما يلي:

  * يشير **Messaging > A message comes in** في Twilio إلى `publicWebhookUrl`.
  * الطريقة هي `POST`.
  * يكشف النفق أو الوكيل العكسي `webhookPath` الدقيق؛ بالنسبة إلى Tailscale Funnel، شغّل `tailscale funnel status` وتأكد من أن `/webhooks/sms` مدرج.
  * يستخدم `publicWebhookUrl` المخطط والمضيف والمسار وسلسلة الاستعلام نفسها التي يرسلها Twilio، بحيث يمكن للتحقق من التوقيع إعادة إنتاج عنوان URL الموقّع.


### تفشل عمليات الإرسال الصادرة

تأكد من حل `accountSid` و `authToken` وإما `fromNumber` أو `messagingServiceSid`. إذا كنت تستخدم حساب Twilio تجريبيًا، فقد يلزم التحقق من رقم الوجهة في Twilio قبل إرسال SMS الصادرة.

### تصل الرسائل لكن الوكيل لا يجيب

تحقق من `dmPolicy` و`allowFrom`. مع سياسة `pairing` الافتراضية، يجب اعتماد المرسل قبل معالجة دورات الوكيل العادية.

Was this useful?YesNo

Open issue