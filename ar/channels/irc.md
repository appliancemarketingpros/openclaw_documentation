---
title: IRC
source_url: https://docs.openclaw.ai/ar/channels/irc
scraped_at: 2026-05-25
---

استخدم IRC عندما تريد OpenClaw في القنوات الكلاسيكية (`#room`) والرسائل المباشرة. يأتي IRC كـ Plugin مضمن، لكنه يُكوَّن في الإعدادات الرئيسية ضمن `channels.irc`.

## البدء السريع

  1. فعّل إعدادات IRC في `~/.openclaw/openclaw.json`.
  2. اضبط على الأقل:

json5Copy code
[code]
    {  channels: {    irc: {      enabled: true,      host: "irc.example.com",      port: 6697,      tls: true,      nick: "openclaw-bot",      channels: ["#openclaw"],    },  },}
[/code]

فضّل خادم IRC خاصًا لتنسيق البوتات. إذا كنت تستخدم شبكة IRC عامة عن قصد، فمن الخيارات الشائعة Libera.Chat وOFTC وSnoonet. تجنّب القنوات العامة المتوقعة لحركة مرور القناة الخلفية للبوتات أو السرب.

  3. ابدأ/أعد تشغيل Gateway:

bashCopy code
[code]
    openclaw gateway run
[/code]

## افتراضيات الأمان

  * يستخدم IRC مقابس TCP/TLS خامًا خارج توجيه وكيل التمرير الأمامي المُدار من مشغّل OpenClaw. في عمليات النشر التي تتطلب مرور كل الخروج عبر وكيل التمرير الأمامي هذا، اضبط `channels.irc.enabled=false` ما لم تتم الموافقة صراحةً على خروج IRC المباشر.
  * القيمة الافتراضية لـ `channels.irc.dmPolicy` هي `"pairing"`.
  * القيمة الافتراضية لـ `channels.irc.groupPolicy` هي `"allowlist"`.
  * مع `groupPolicy="allowlist"`، اضبط `channels.irc.groups` لتعريف القنوات المسموح بها.
  * استخدم TLS (`channels.irc.tls=true`) ما لم تكن تقبل النقل بالنص الصريح عن قصد.


## التحكم في الوصول

توجد "بوابتان" منفصلتان لقنوات IRC:

  1. **وصول القناة** (`groupPolicy` \+ `groups`): ما إذا كان البوت يقبل الرسائل من قناة أصلًا.
  2. **وصول المرسل** (`groupAllowFrom` / لكل قناة `groups["#channel"].allowFrom`): من يُسمح له بتشغيل البوت داخل تلك القناة.


مفاتيح الإعداد:

  * قائمة السماح للرسائل المباشرة (وصول مرسل الرسائل المباشرة): `channels.irc.allowFrom`
  * قائمة سماح مرسلي المجموعة (وصول مرسل القناة): `channels.irc.groupAllowFrom`
  * عناصر التحكم لكل قناة (قواعد القناة + المرسل + الإشارة): `channels.irc.groups["#channel"]`
  * يتيح `channels.irc.groupPolicy="open"` القنوات غير المكوّنة (**مع بقائها مقيّدة بالإشارة افتراضيًا**)


يجب أن تستخدم إدخالات قائمة السماح هويات مرسلين مستقرة (`nick!user@host`). مطابقة الاسم المستعار وحده قابلة للتغيير ولا تُفعّل إلا عند `channels.irc.dangerouslyAllowNameMatching: true`.

### مشكلة شائعة: `allowFrom` مخصص للرسائل المباشرة، وليس للقنوات

إذا رأيت سجلات مثل:

  * `irc: drop group sender alice!ident@host (policy=allowlist)`


...فهذا يعني أن المرسل لم يكن مسموحًا له برسائل **المجموعة/القناة**. أصلح ذلك بإحدى الطريقتين:

  * ضبط `channels.irc.groupAllowFrom` (عام لكل القنوات)، أو
  * ضبط قوائم سماح المرسلين لكل قناة: `channels.irc.groups["#channel"].allowFrom`


مثال (السماح لأي شخص في `#tuirc-dev` بالتحدث إلى البوت):

json5Copy code
[code]
    {  channels: {    irc: {      groupPolicy: "allowlist",      groups: {        "#tuirc-dev": { allowFrom: ["*"] },      },    },  },}
[/code]

## تشغيل الرد (الإشارات)

حتى إذا كانت القناة مسموحًا بها (عبر `groupPolicy` \+ `groups`) وكان المرسل مسموحًا به، فإن OpenClaw يستخدم افتراضيًا **تقييد الإشارة** في سياقات المجموعات.

وهذا يعني أنك قد ترى سجلات مثل `drop channel … (missing-mention)` ما لم تتضمن الرسالة نمط إشارة يطابق البوت.

لجعل البوت يرد في قناة IRC **من دون الحاجة إلى إشارة** ، عطّل تقييد الإشارة لتلك القناة:

json5Copy code
[code]
    {  channels: {    irc: {      groupPolicy: "allowlist",      groups: {        "#tuirc-dev": {          requireMention: false,          allowFrom: ["*"],        },      },    },  },}
[/code]

أو للسماح **بكل** قنوات IRC (من دون قائمة سماح لكل قناة) مع الاستمرار في الرد من دون إشارات:

json5Copy code
[code]
    {  channels: {    irc: {      groupPolicy: "open",      groups: {        "*": { requireMention: false, allowFrom: ["*"] },      },    },  },}
[/code]

## ملاحظة أمنية (موصى بها للقنوات العامة)

إذا سمحت بـ `allowFrom: ["*"]` في قناة عامة، فيمكن لأي شخص إرسال مطالبات إلى البوت. لتقليل المخاطر، قيّد الأدوات لتلك القناة.

### الأدوات نفسها لكل شخص في القناة

json5Copy code
[code]
    {  channels: {    irc: {      groups: {        "#tuirc-dev": {          allowFrom: ["*"],          tools: {            deny: ["group:runtime", "group:fs", "gateway", "nodes", "cron", "browser"],          },        },      },    },  },}
[/code]

### أدوات مختلفة لكل مرسل (يحصل المالك على صلاحيات أكثر)

استخدم `toolsBySender` لتطبيق سياسة أكثر صرامة على `"*"` وسياسة أخف على اسمك المستعار:

json5Copy code
[code]
    {  channels: {    irc: {      groups: {        "#tuirc-dev": {          allowFrom: ["*"],          toolsBySender: {            "*": {              deny: ["group:runtime", "group:fs", "gateway", "nodes", "cron", "browser"],            },            "id:eigen": {              deny: ["gateway", "nodes", "cron"],            },          },        },      },    },  },}
[/code]

ملاحظات:

  * يجب أن تستخدم مفاتيح `toolsBySender` البادئة `id:` لقيم هوية مرسل IRC: `id:eigen` أو `id:eigen!~eigen@174.127.248.171` لمطابقة أقوى.
  * لا تزال المفاتيح القديمة غير المسبوقة مقبولة وتُطابق كـ `id:` فقط.
  * تفوز أول سياسة مرسل مطابقة؛ أما `"*"` فهي خيار الرجوع العام.


لمزيد من المعلومات حول وصول المجموعة مقابل تقييد الإشارة (وكيفية تفاعلهما)، راجع: [/channels/groups](</ar/channels/groups>).

## NickServ

للتعريف مع NickServ بعد الاتصال:

json5Copy code
[code]
    {  channels: {    irc: {      nickserv: {        enabled: true,        service: "NickServ",        password: "your-nickserv-password",      },    },  },}
[/code]

تسجيل اختياري لمرة واحدة عند الاتصال:

json5Copy code
[code]
    {  channels: {    irc: {      nickserv: {        register: true,        registerEmail: "bot@example.com",      },    },  },}
[/code]

عطّل `register` بعد تسجيل الاسم المستعار لتجنب محاولات REGISTER المتكررة.

## متغيرات البيئة

يدعم الحساب الافتراضي:

  * `IRC_HOST`
  * `IRC_PORT`
  * `IRC_TLS`
  * `IRC_NICK`
  * `IRC_USERNAME`
  * `IRC_REALNAME`
  * `IRC_PASSWORD`
  * `IRC_CHANNELS` (مفصولة بفواصل)
  * `IRC_NICKSERV_PASSWORD`
  * `IRC_NICKSERV_REGISTER_EMAIL`


لا يمكن ضبط `IRC_HOST` من ملف `.env` في مساحة العمل؛ راجع [ملفات `.env` لمساحة العمل](</ar/gateway/security>).

## استكشاف الأخطاء وإصلاحها

  * إذا كان البوت يتصل لكنه لا يرد أبدًا في القنوات، فتحقق من `channels.irc.groups` **ومن** ما إذا كان تقييد الإشارة يسقط الرسائل (`missing-mention`). إذا كنت تريده أن يرد من دون تنبيهات، فاضبط `requireMention:false` للقناة.
  * إذا فشل تسجيل الدخول، فتحقق من توفر الاسم المستعار وكلمة مرور الخادم.
  * إذا فشل TLS على شبكة مخصصة، فتحقق من المضيف/المنفذ وإعداد الشهادة.


## ذات صلة

  * [نظرة عامة على القنوات](</ar/channels>) — كل القنوات المدعومة
  * [الاقتران](</ar/channels/pairing>) — مصادقة الرسائل المباشرة وتدفق الاقتران
  * [المجموعات](</ar/channels/groups>) — سلوك دردشة المجموعة وتقييد الإشارة
  * [توجيه القنوات](</ar/channels/channel-routing>) — توجيه الجلسات للرسائل
  * [الأمان](</ar/gateway/security>) — نموذج الوصول والتقوية


Was this useful?YesNo