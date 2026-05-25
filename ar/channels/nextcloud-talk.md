---
title: Nextcloud Talk
source_url: https://docs.openclaw.ai/ar/channels/nextcloud-talk
scraped_at: 2026-05-25
---

الحالة: Plugin مضمّن (روبوت Webhook). الرسائل المباشرة، والغرف، والتفاعلات، ورسائل ماركداون مدعومة.

## Plugin مضمّن

يأتي Nextcloud Talk بصفته Plugin مضمّنًا في إصدارات OpenClaw الحالية، لذلك لا تحتاج البنيات العادية المعبأة إلى تثبيت منفصل.

إذا كنت تستخدم بنية أقدم أو تثبيتًا مخصصًا يستبعد Nextcloud Talk، فثبّت حزمة npm مباشرة:

التثبيت عبر CLI (سجل npm):

bashCopy code
[code]
    openclaw plugins install @openclaw/nextcloud-talk
[/code]

استخدم الحزمة المجرّدة لمتابعة وسم الإصدار الرسمي الحالي. ثبّت إصدارًا دقيقًا فقط عندما تحتاج إلى تثبيت قابل لإعادة الإنتاج.

نسخة محلية (عند التشغيل من مستودع git):

bashCopy code
[code]
    openclaw plugins install ./path/to/local/nextcloud-talk-plugin
[/code]

التفاصيل: [Plugins](</ar/tools/plugin>)

## الإعداد السريع (للمبتدئين)

  1. تأكد من توفر Plugin الخاص بـ Nextcloud Talk.

     * إصدارات OpenClaw المعبأة الحالية تتضمنه بالفعل.
     * يمكن للتثبيتات الأقدم/المخصصة إضافته يدويًا بالأوامر أعلاه.
  2. على خادم Nextcloud الخاص بك، أنشئ روبوتًا:

bashCopy code
[code]./occ talk:bot:install "OpenClaw" "<shared-secret>" "<webhook-url>" --feature webhook --feature response --feature reaction
[/code]

  3. فعّل الروبوت في إعدادات الغرفة المستهدفة.

  4. اضبط OpenClaw:

     * الإعداد: `channels.nextcloud-talk.baseUrl` \+ `channels.nextcloud-talk.botSecret`
     * أو متغير البيئة: `NEXTCLOUD_TALK_BOT_SECRET` (الحساب الافتراضي فقط)

إعداد CLI:

bashCopy code
[code]openclaw channels add --channel nextcloud-talk \  --url https://cloud.example.com \  --token "<shared-secret>"
[/code]

الحقول الصريحة المكافئة:

bashCopy code
[code]openclaw channels add --channel nextcloud-talk \  --base-url https://cloud.example.com \  --secret "<shared-secret>"
[/code]

سر مستند إلى ملف:

bashCopy code
[code]openclaw channels add --channel nextcloud-talk \  --base-url https://cloud.example.com \  --secret-file /path/to/nextcloud-talk-secret
[/code]

  5. أعد تشغيل Gateway (أو أكمل الإعداد).


إعداد بسيط:

json5Copy code
[code]
    {  channels: {    "nextcloud-talk": {      enabled: true,      baseUrl: "https://cloud.example.com",      botSecret: "shared-secret",      dmPolicy: "pairing",    },  },}
[/code]

## ملاحظات

  * لا يمكن للروبوتات بدء رسائل مباشرة. يجب أن يرسل المستخدم رسالة إلى الروبوت أولًا.
  * يجب أن يكون عنوان Webhook URL قابلًا للوصول من Gateway؛ اضبط `webhookPublicUrl` إذا كان خلف وكيل.
  * تحميلات الوسائط غير مدعومة بواسطة واجهة API الخاصة بالروبوت؛ تُرسل الوسائط كعناوين URL.
  * لا تميّز حمولة Webhook بين الرسائل المباشرة والغرف؛ اضبط `apiUser` \+ `apiPassword` لتمكين عمليات البحث عن نوع الغرفة (وإلا تُعامل الرسائل المباشرة كغرف).


## التحكم في الوصول (الرسائل المباشرة)

  * الافتراضي: `channels.nextcloud-talk.dmPolicy = "pairing"`. يحصل المرسلون غير المعروفين على رمز إقران.
  * الموافقة عبر: 
    * `openclaw pairing list nextcloud-talk`
    * `openclaw pairing approve nextcloud-talk &lt;CODE&gt;`
  * الرسائل المباشرة العامة: `channels.nextcloud-talk.dmPolicy="open"` بالإضافة إلى `channels.nextcloud-talk.allowFrom=["*"]`.
  * يطابق `allowFrom` معرّفات مستخدمي Nextcloud فقط؛ يتم تجاهل أسماء العرض.


## الغرف (المجموعات)

  * الافتراضي: `channels.nextcloud-talk.groupPolicy = "allowlist"` (مقيّد بالإشارة).
  * أدرج الغرف في قائمة السماح باستخدام `channels.nextcloud-talk.rooms`:

json5Copy code
[code]
    {  channels: {    "nextcloud-talk": {      rooms: {        "room-token": { requireMention: true },      },    },  },}
[/code]

  * للسماح بعدم وجود أي غرف، اترك قائمة السماح فارغة أو اضبط `channels.nextcloud-talk.groupPolicy="disabled"`.


## القدرات

الميزة | الحالة  
---|---  
الرسائل المباشرة | مدعوم  
الغرف | مدعوم  
سلاسل المحادثة | غير مدعوم  
الوسائط | URL فقط  
التفاعلات | مدعوم  
الأوامر الأصلية | غير مدعوم  
  
## مرجع الإعداد (Nextcloud Talk)

الإعداد الكامل: [الإعداد](</ar/gateway/configuration>)

خيارات المزوّد:

  * `channels.nextcloud-talk.enabled`: تمكين/تعطيل بدء القناة.
  * `channels.nextcloud-talk.baseUrl`: عنوان URL لمثيل Nextcloud.
  * `channels.nextcloud-talk.botSecret`: السر المشترك للروبوت.
  * `channels.nextcloud-talk.botSecretFile`: مسار سر في ملف عادي. تُرفض الروابط الرمزية.
  * `channels.nextcloud-talk.apiUser`: مستخدم API لعمليات البحث عن الغرف (اكتشاف الرسائل المباشرة).
  * `channels.nextcloud-talk.apiPassword`: كلمة مرور API/التطبيق لعمليات البحث عن الغرف.
  * `channels.nextcloud-talk.apiPasswordFile`: مسار ملف كلمة مرور API.
  * `channels.nextcloud-talk.webhookPort`: منفذ مستمع Webhook (الافتراضي: 8788).
  * `channels.nextcloud-talk.webhookHost`: مضيف Webhook (الافتراضي: 0.0.0.0).
  * `channels.nextcloud-talk.webhookPath`: مسار Webhook (الافتراضي: /nextcloud-talk-webhook).
  * `channels.nextcloud-talk.webhookPublicUrl`: عنوان Webhook URL قابل للوصول خارجيًا.
  * `channels.nextcloud-talk.dmPolicy`: `pairing | allowlist | open | disabled`.
  * `channels.nextcloud-talk.allowFrom`: قائمة السماح للرسائل المباشرة (معرّفات المستخدمين). يتطلب `open` القيمة `"*"`.
  * `channels.nextcloud-talk.groupPolicy`: `allowlist | open | disabled`.
  * `channels.nextcloud-talk.groupAllowFrom`: قائمة السماح للمجموعات (معرّفات المستخدمين).
  * `channels.nextcloud-talk.rooms`: إعدادات وقائمة سماح لكل غرفة.
  * يمكن الرجوع إلى مجموعات وصول المرسلين الثابتة من `allowFrom` و`groupAllowFrom` باستخدام `accessGroup:<name>`.
  * `channels.nextcloud-talk.historyLimit`: حد سجل المجموعة (0 يعطّل).
  * `channels.nextcloud-talk.dmHistoryLimit`: حد سجل الرسائل المباشرة (0 يعطّل).
  * `channels.nextcloud-talk.dms`: تجاوزات لكل رسالة مباشرة (historyLimit).
  * `channels.nextcloud-talk.textChunkLimit`: حجم جزء النص الصادر (أحرف).
  * `channels.nextcloud-talk.chunkMode`: `length` (الافتراضي) أو `newline` للتقسيم عند الأسطر الفارغة (حدود الفقرات) قبل التقسيم حسب الطول.
  * `channels.nextcloud-talk.blockStreaming`: تعطيل بث الكتل لهذه القناة.
  * `channels.nextcloud-talk.blockStreamingCoalesce`: ضبط دمج بث الكتل.
  * `channels.nextcloud-talk.mediaMaxMb`: حد الوسائط الواردة (MB).


## ذو صلة

  * [نظرة عامة على القنوات](</ar/channels>) — كل القنوات المدعومة
  * [الإقران](</ar/channels/pairing>) — مصادقة الرسائل المباشرة وتدفق الإقران
  * [المجموعات](</ar/channels/groups>) — سلوك محادثة المجموعة والتقييد بالإشارة
  * [توجيه القنوات](</ar/channels/channel-routing>) — توجيه الجلسات للرسائل
  * [الأمان](</ar/gateway/security>) — نموذج الوصول والتحصين


Was this useful?YesNo