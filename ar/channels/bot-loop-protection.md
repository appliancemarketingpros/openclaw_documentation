---
title: الحماية من حلقات البوت
source_url: https://docs.openclaw.ai/ar/channels/bot-loop-protection
scraped_at: 2026-06-29
---

Get started

# حماية حلقات البوتات

يمكن لـ OpenClaw قبول الرسائل التي تكتبها بوتات أخرى على القنوات التي تدعم `allowBots`. عند تفعيل هذا المسار، تمنع حماية حلقات الأزواج هويتين لبوتين من الرد على بعضهما إلى أجل غير مسمى.

يفرض مشغّل الردود الواردة الأساسي هذه الحماية. تحوّل كل قناة داعمة حدثها الوارد إلى حقائق عامة: الحساب أو النطاق، معرّف المحادثة، معرّف بوت المرسل، ومعرّف بوت المستقبل. ثم يتتبع القلب زوج المشاركين في كلا الاتجاهين، ويطبّق ميزانية نافذة منزلقة، ويكبح الزوج أثناء فترة تهدئة بعد تجاوز الميزانية.

## الإعدادات الافتراضية

تكون حماية حلقات الأزواج نشطة عندما تسمح قناة للرسائل المؤلفة من بوتات بالوصول إلى التوجيه. الإعدادات الافتراضية المدمجة هي:

  * `maxEventsPerWindow: 20` \- يمكن لزوج بوتات تبادل 20 حدثا ضمن النافذة
  * `windowSeconds: 60` \- طول النافذة المنزلقة
  * `cooldownSeconds: 60` \- مدة الكبح بعد تجاوز الزوج للميزانية


لا تؤثر الحماية في الرسائل العادية المؤلفة من البشر، أو نشر بوت واحد، أو تصفية الرسائل الذاتية، أو ردود البوت لمرة واحدة التي تبقى دون الميزانية.

## تكوين الإعدادات الافتراضية المشتركة

اضبط `channels.defaults.botLoopProtection` مرة واحدة لمنح كل قناة داعمة خط الأساس نفسه. لا تزال تجاوزات القناة والحساب قادرة على ضبط الأسطح الفردية.

json5Copy code
[code]
    {  channels: {    defaults: {      botLoopProtection: {        maxEventsPerWindow: 20,        windowSeconds: 60,        cooldownSeconds: 60,      },    },  },}
[/code]

اضبط `enabled: false` فقط عندما تسمح سياسة قناتك عمدا بمحادثات بوت إلى بوت دون كبح تلقائي.

## التجاوز لكل قناة أو حساب

تضيف القنوات الداعمة تكوينها الخاص فوق الإعداد الافتراضي المشترك. ترتيب الأولوية هو:

  * `channels.<channel>.<room-or-space>.botLoopProtection`، عندما تدعم القناة التجاوزات لكل محادثة
  * `channels.<channel>.accounts.<account>.botLoopProtection`، عندما تدعم القناة الحسابات
  * `channels.<channel>.botLoopProtection`، عندما تدعم القناة الإعدادات الافتراضية ذات المستوى الأعلى
  * `channels.defaults.botLoopProtection`
  * الإعدادات الافتراضية المدمجة

json5Copy code
[code]
    {  channels: {    defaults: {      botLoopProtection: {        maxEventsPerWindow: 20,      },    },    discord: {      botLoopProtection: {        maxEventsPerWindow: 8,      },      accounts: {        molty: {          allowBots: "mentions",          botLoopProtection: {            maxEventsPerWindow: 5,            cooldownSeconds: 90,          },        },      },    },    slack: {      allowBots: "mentions",      botLoopProtection: {        maxEventsPerWindow: 8,      },    },    matrix: {      allowBots: "mentions",      groups: {        "!roomid:example.org": {          botLoopProtection: {            maxEventsPerWindow: 5,          },        },      },    },    googlechat: {      allowBots: true,      groups: {        "spaces/AAAA": {          botLoopProtection: {            maxEventsPerWindow: 5,          },        },      },    },  },}
[/code]

## دعم القنوات

  * Discord: حقائق `author.bot` الأصلية، مرتبطة بحساب Discord والقناة وزوج البوتات.
  * Slack: حقائق `bot_id` الأصلية للرسائل المقبولة المؤلفة من بوتات، مرتبطة بحساب Slack والقناة وزوج البوتات.
  * Matrix: حسابات بوت Matrix المكوّنة، مرتبطة بحساب Matrix والغرفة وزوج البوتات المكوّن.
  * Google Chat: حقائق `sender.type=BOT` الأصلية للرسائل المقبولة المؤلفة من بوتات، مرتبطة بالحساب والمساحة وزوج البوتات.


تستمر القنوات التي لا تعرض هوية بوت واردة موثوقة في استخدام مرشحات الرسائل الذاتية وسياسة الوصول العادية الخاصة بها. يجب ألا تشترك في هذه الحماية حتى تتمكن من تحديد كلا المشاركين في زوج البوتات.

راجع [وقت تشغيل SDK](</ar/plugins/sdk-runtime#reusable-runtime-utilities>) لمعرفة تفاصيل تنفيذ Plugin.

Was this useful?YesNo

Open issue