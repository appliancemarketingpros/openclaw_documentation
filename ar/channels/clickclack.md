---
title: كليك كلاك
source_url: https://docs.openclaw.ai/ar/channels/clickclack
scraped_at: 2026-05-25
---

يربط ClickClack OpenClaw بمساحة عمل ClickClack مستضافة ذاتيًا عبر رموز روبوت ClickClack من الدرجة الأولى.

استخدم هذا عندما تريد أن يظهر وكيل OpenClaw كمستخدم روبوت ClickClack. يدعم ClickClack روبوتات خدمة مستقلة وروبوتات مملوكة للمستخدمين؛ تحتفظ الروبوتات المملوكة للمستخدمين بـ `owner_user_id` وتتلقى فقط نطاقات الرمز التي تمنحها.

## الإعداد السريع

أنشئ رمز روبوت في ClickClack:

bashCopy code
[code]
    clickclack admin bot create \  --workspace <workspace_id_or_slug> \  --name "OpenClaw" \  --handle openclaw \  --scopes bot:write \  --plain
[/code]

لروبوت مملوك لمستخدم، أضف `--owner <user_id>`.

كوّن OpenClaw:

json5Copy code
[code]
    {  plugins: {    entries: {      clickclack: {        llm: {          allowAgentIdOverride: true,        },      },    },  },  channels: {    clickclack: {      enabled: true,      baseUrl: "https://app.clickclack.chat",      token: { source: "env", provider: "default", id: "CLICKCLACK_BOT_TOKEN" },      workspace: "default",      defaultTo: "channel:general",      agentId: "clickclack-bot",      replyMode: "model",    },  },}
[/code]

ثم شغّل:

bashCopy code
[code]
    export CLICKCLACK_BOT_TOKEN="ccb_..."openclaw gateway
[/code]

## روبوتات متعددة

يفتح كل حساب اتصال ClickClack فوريًا خاصًا به ويستخدم رمز الروبوت الخاص به.

json5Copy code
[code]
    {  plugins: {    entries: {      clickclack: {        llm: {          allowAgentIdOverride: true,        },      },    },  },  channels: {    clickclack: {      enabled: true,      baseUrl: "https://app.clickclack.chat",      defaultAccount: "service",      accounts: {        service: {          token: { source: "env", provider: "default", id: "CLICKCLACK_SERVICE_BOT_TOKEN" },          workspace: "default",          defaultTo: "channel:general",          agentId: "service-bot",          replyMode: "model",        },        peter: {          token: { source: "env", provider: "default", id: "CLICKCLACK_PETER_BOT_TOKEN" },          workspace: "default",          defaultTo: "dm:usr_...",          agentId: "peter-bot",          replyMode: "model",        },      },    },  },}
[/code]

يستخدم `replyMode: "model"` ‏`api.runtime.llm.complete` مباشرةً للردود القصيرة من الروبوت. عندما يضبط حساب `agentId`، يتطلب OpenClaw بت الثقة الصريح `plugins.entries.clickclack.llm.allowAgentIdOverride` كي يتمكن Plugin من تشغيل الإكمالات لوكيل الروبوت ذلك. أبقه معطّلًا إذا كنت تستخدم مسار الوكيل الافتراضي فقط.

## الأهداف

  * يرسل `channel:<name-or-id>` إلى قناة مساحة عمل. الأهداف المجردة تستخدم `channel:` افتراضيًا.
  * ينشئ `dm:<user_id>` محادثة مباشرة مع ذلك المستخدم أو يعيد استخدامها.
  * يرد `thread:<message_id>` في سلسلة موجودة.


أمثلة:

bashCopy code
[code]
    openclaw message send --channel clickclack --target channel:general --message "hello"openclaw message send --channel clickclack --target dm:usr_123 --message "hello"openclaw message send --channel clickclack --target thread:msg_123 --message "following up"
[/code]

## الأذونات

يفرض ClickClack API نطاقات رموز ClickClack.

  * `bot:read`: قراءة بيانات مساحة العمل/القناة/الرسالة/السلسلة/الرسائل المباشرة/الاتصال الفوري/الملف الشخصي.
  * `bot:write`: `bot:read` بالإضافة إلى رسائل القنوات، وردود السلاسل، والرسائل المباشرة، والتحميلات.
  * `bot:admin`: `bot:write` بالإضافة إلى إنشاء القنوات.


يحتاج OpenClaw فقط إلى `bot:write` لمحادثة الوكيل العادية.

## استكشاف الأخطاء وإصلاحها

  * `ClickClack is not configured`: اضبط `channels.clickclack.token` أو `CLICKCLACK_BOT_TOKEN`.
  * `workspace not found`: اضبط `workspace` إلى معرّف مساحة العمل أو الاسم المختصر الذي يعيده ClickClack.
  * لا توجد ردود واردة: تأكد من أن الرمز لديه صلاحية قراءة فورية وأن الروبوت لا يرد على رسائله الخاصة.
  * فشل الإرسال إلى القناة: تحقق من أن الروبوت عضو في مساحة العمل ولديه `bot:write`.


Was this useful?YesNo