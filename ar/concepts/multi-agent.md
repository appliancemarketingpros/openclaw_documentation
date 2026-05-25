---
title: توجيه متعدد الوكلاء
source_url: https://docs.openclaw.ai/ar/concepts/multi-agent
scraped_at: 2026-05-25
---

شغّل عدة وكلاء _معزولين_ ، لكل منهم مساحة العمل الخاصة به، ودليل الحالة (`agentDir`)، وسجل الجلسات، إلى جانب عدة حسابات قنوات (مثل حسابي WhatsApp) في Gateway واحد قيد التشغيل. تُوجَّه الرسائل الواردة إلى الوكيل الصحيح عبر الارتباطات.

**الوكيل** هنا هو النطاق الكامل لكل شخصية: ملفات مساحة العمل، وملفات تعريف المصادقة، وسجل النماذج، ومخزن الجلسات. `agentDir` هو دليل الحالة على القرص الذي يحتوي إعدادات كل وكيل في `~/.openclaw/agents/<agentId>/`. **الارتباط** يربط حساب قناة (مثل مساحة عمل Slack أو رقم WhatsApp) بأحد هؤلاء الوكلاء.

## ما المقصود بـ "وكيل واحد"؟

**الوكيل** هو عقل محدد النطاق بالكامل وله:

  * **مساحة عمل** (ملفات، [AGENTS.md/SOUL.md/USER.md،](<http://AGENTS.md/SOUL.md/USER.md%D8%8C>) ملاحظات محلية، قواعد الشخصية).
  * **دليل حالة** (`agentDir`) لملفات تعريف المصادقة، وسجل النماذج، وإعدادات كل وكيل.
  * **مخزن جلسات** (سجل المحادثة + حالة التوجيه) تحت `~/.openclaw/agents/<agentId>/sessions`.


ملفات تعريف المصادقة تكون **لكل وكيل**. يقرأ كل وكيل من ملفه الخاص:

textCopy code
[code]
    ~/.openclaw/agents/<agentId>/agent/auth-profiles.json
[/code]

تُحمَّل Skills من مساحة عمل كل وكيل بالإضافة إلى الجذور المشتركة مثل `~/.openclaw/skills`، ثم تُرشَّح بواسطة قائمة السماح الفعالة للوكيل عند تكوينها. استخدم `agents.defaults.skills` لخط أساس مشترك و`agents.list[].skills` للاستبدال لكل وكيل. راجع [Skills: لكل وكيل مقابل المشتركة](</ar/tools/skills#per-agent-vs-shared-skills>) و[Skills: قوائم السماح لمهارات الوكيل](</ar/tools/skills#agent-skill-allowlists>).

يمكن لـ Gateway استضافة **وكيل واحد** (افتراضيًا) أو **عدة وكلاء** جنبًا إلى جنب.

## المسارات (خريطة سريعة)

  * الإعدادات: `~/.openclaw/openclaw.json` (أو `OPENCLAW_CONFIG_PATH`)
  * دليل الحالة: `~/.openclaw` (أو `OPENCLAW_STATE_DIR`)
  * مساحة العمل: `~/.openclaw/workspace` (أو `~/.openclaw/workspace-<agentId>`)
  * دليل الوكيل: `~/.openclaw/agents/<agentId>/agent` (أو `agents.list[].agentDir`)
  * الجلسات: `~/.openclaw/agents/<agentId>/sessions`


### وضع الوكيل الواحد (افتراضي)

إذا لم تفعل شيئًا، يشغّل OpenClaw وكيلًا واحدًا:

  * تكون قيمة `agentId` الافتراضية هي **`main`**.
  * تُفهرس الجلسات بالشكل `agent:main:<mainKey>`.
  * تكون مساحة العمل افتراضيًا `~/.openclaw/workspace` (أو `~/.openclaw/workspace-<profile>` عند تعيين `OPENCLAW_PROFILE`).
  * تكون الحالة افتراضيًا `~/.openclaw/agents/main/agent`.


## مساعد الوكلاء

استخدم معالج الوكلاء لإضافة وكيل جديد معزول:

bashCopy code
[code]
    openclaw agents add work
[/code]

ثم أضف `bindings` (أو دع المعالج يفعل ذلك) لتوجيه الرسائل الواردة.

تحقق عبر:

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

## البدء السريع

* ### Create each agent workspace

استخدم المعالج أو أنشئ مساحات العمل يدويًا:

bashCopy code
[code]
    openclaw agents add codingopenclaw agents add social
[/code]

يحصل كل وكيل على مساحة عمل خاصة به تحتوي `SOUL.md` و`AGENTS.md` و`USER.md` اختياريًا، بالإضافة إلى `agentDir` مخصص ومخزن جلسات تحت `~/.openclaw/agents/<agentId>`.

* ### Create channel accounts

أنشئ حسابًا واحدًا لكل وكيل على القنوات المفضلة لديك:

  * Discord: روبوت واحد لكل وكيل، فعّل Message Content Intent، وانسخ كل رمز.
  * Telegram: روبوت واحد لكل وكيل عبر BotFather، وانسخ كل رمز.
  * WhatsApp: اربط كل رقم هاتف لكل حساب.

bashCopy code
[code]
    openclaw channels login --channel whatsapp --account work
[/code]

راجع أدلة القنوات: [Discord](</ar/channels/discord>)، [Telegram](</ar/channels/telegram>)، [WhatsApp](</ar/channels/whatsapp>).

* ### Add agents, accounts, and bindings

أضف الوكلاء تحت `agents.list`، وحسابات القنوات تحت `channels.<channel>.accounts`، واربطها باستخدام `bindings` (الأمثلة أدناه).

* ### Restart and verify

bashCopy code
[code]
    openclaw gateway restartopenclaw agents list --bindingsopenclaw channels status --probe
[/code]

## عدة وكلاء = عدة أشخاص، عدة شخصيات

مع **عدة وكلاء** ، يصبح كل `agentId` **شخصية معزولة بالكامل** :

  * **أرقام هواتف/حسابات مختلفة** (لكل قناة `accountId`).
  * **شخصيات مختلفة** (ملفات مساحة العمل لكل وكيل مثل `AGENTS.md` و`SOUL.md`).
  * **مصادقة + جلسات منفصلة** (لا يحدث تداخل ما لم يُفعّل صراحة).


يتيح هذا لـ **عدة أشخاص** مشاركة خادم Gateway واحد مع إبقاء "عقول" الذكاء الاصطناعي وبياناتهم معزولة.

## البحث في ذاكرة QMD عبر الوكلاء

إذا كان ينبغي لوكيل ما البحث في نصوص جلسات QMD لوكيل آخر، فأضف مجموعات إضافية تحت `agents.list[].memorySearch.qmd.extraCollections`. استخدم `agents.defaults.memorySearch.qmd.extraCollections` فقط عندما ينبغي لكل وكيل أن يرث مجموعات النصوص المشتركة نفسها.

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/workspaces/main",      memorySearch: {        qmd: {          extraCollections: [{ path: "~/agents/family/sessions", name: "family-sessions" }],        },      },    },    list: [      {        id: "main",        workspace: "~/workspaces/main",        memorySearch: {          qmd: {            extraCollections: [{ path: "notes" }], // resolves inside workspace -> collection named "notes-main"          },        },      },      { id: "family", workspace: "~/workspaces/family" },    ],  },  memory: {    backend: "qmd",    qmd: { includeDefaultMemory: false },  },}
[/code]

يمكن مشاركة مسار المجموعة الإضافية بين الوكلاء، لكن يبقى اسم المجموعة صريحًا عندما يكون المسار خارج مساحة عمل الوكيل. تظل المسارات داخل مساحة العمل محددة النطاق للوكيل بحيث يحتفظ كل وكيل بمجموعة البحث الخاصة به في النصوص.

## رقم WhatsApp واحد، عدة أشخاص (تقسيم الرسائل المباشرة)

يمكنك توجيه **رسائل WhatsApp المباشرة المختلفة** إلى وكلاء مختلفين مع البقاء على **حساب WhatsApp واحد**. طابق على مرسل E.164 (مثل `+15551234567`) باستخدام `peer.kind: "direct"`. لا تزال الردود تأتي من رقم WhatsApp نفسه (لا توجد هوية مرسل لكل وكيل).

مثال:

json5Copy code
[code]
    {  agents: {    list: [      { id: "alex", workspace: "~/.openclaw/workspace-alex" },      { id: "mia", workspace: "~/.openclaw/workspace-mia" },    ],  },  bindings: [    {      agentId: "alex",      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551230001" } },    },    {      agentId: "mia",      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551230002" } },    },  ],  channels: {    whatsapp: {      dmPolicy: "allowlist",      allowFrom: ["+15551230001", "+15551230002"],    },  },}
[/code]

ملاحظات:

  * التحكم في وصول الرسائل المباشرة **عام لكل حساب WhatsApp** (الاقتران/قائمة السماح)، وليس لكل وكيل.
  * للمجموعات المشتركة، اربط المجموعة بوكيل واحد أو استخدم [مجموعات البث](</ar/channels/broadcast-groups>).


## قواعد التوجيه (كيف تختار الرسائل وكيلًا)

الارتباطات **حتمية** و**الأكثر تحديدًا يفوز** :

* ### peer match

مطابقة دقيقة لمعرف الرسالة المباشرة/المجموعة/القناة.

* ### parentPeer match

وراثة السلسلة.

* ### guildId + roles

توجيه أدوار Discord.

* ### guildId

Discord.

* ### teamId

Slack.

* ### accountId match for a channel

رجوع احتياطي لكل حساب.

* ### Channel-level match

`accountId: "*"`.

* ### Default agent

الرجوع إلى `agents.list[].default`، وإلا أول إدخال في القائمة، الافتراضي: `main`.

Tie-breaking and AND semantics

  * إذا طابقت عدة ارتباطات في المستوى نفسه، يفوز أول ارتباط بترتيب الإعدادات.
  * إذا عيّن ارتباط عدة حقول مطابقة (مثل `peer` \+ `guildId`)، فكل الحقول المحددة مطلوبة (دلالات `AND`).

Account-scope detail

  * الارتباط الذي يحذف `accountId` يطابق الحساب الافتراضي فقط.
  * استخدم `accountId: "*"` لرجوع احتياطي على مستوى القناة عبر كل الحسابات.
  * إذا أضفت لاحقًا الارتباط نفسه للوكيل نفسه مع معرف حساب صريح، يرقي OpenClaw الارتباط الحالي الخاص بالقناة فقط ليصبح محدد النطاق للحساب بدلًا من تكراره.


## عدة حسابات / أرقام هواتف

تستخدم القنوات التي تدعم **عدة حسابات** (مثل WhatsApp) `accountId` لتحديد كل تسجيل دخول. يمكن توجيه كل `accountId` إلى وكيل مختلف، لذلك يمكن لخادم واحد استضافة عدة أرقام هواتف من دون خلط الجلسات.

إذا أردت حسابًا افتراضيًا على مستوى القناة عندما يُحذف `accountId`، فعيّن `channels.<channel>.defaultAccount` (اختياري). عند عدم تعيينه، يعود OpenClaw إلى `default` إن كان موجودًا، وإلا إلى أول معرف حساب مكوّن (مرتب).

تشمل القنوات الشائعة التي تدعم هذا النمط:

  * `whatsapp`, `telegram`, `discord`, `slack`, `signal`, `imessage`
  * `irc`, `line`, `googlechat`, `mattermost`, `matrix`, `nextcloud-talk`
  * `zalo`, `zalouser`, `nostr`, `feishu`


## المفاهيم

  * `agentId`: "عقل" واحد (مساحة عمل، مصادقة لكل وكيل، مخزن جلسات لكل وكيل).
  * `accountId`: نسخة حساب قناة واحدة (مثل حساب WhatsApp `"personal"` مقابل `"biz"`).
  * `binding`: يوجّه الرسائل الواردة إلى `agentId` حسب `(channel, accountId, peer)` ومعرفات النقابة/الفريق اختياريًا.
  * تنهار المحادثات المباشرة إلى `agent:<agentId>:<mainKey>` ("الرئيسية" لكل وكيل؛ `session.mainKey`).


## أمثلة المنصات

Discord bots per agent

يعيَّن كل حساب روبوت Discord إلى `accountId` فريد. اربط كل حساب بوكيل وحافظ على قوائم السماح لكل روبوت.

json5Copy code
[code]
    {  agents: {    list: [      { id: "main", workspace: "~/.openclaw/workspace-main" },      { id: "coding", workspace: "~/.openclaw/workspace-coding" },    ],  },  bindings: [    { agentId: "main", match: { channel: "discord", accountId: "default" } },    { agentId: "coding", match: { channel: "discord", accountId: "coding" } },  ],  channels: {    discord: {      groupPolicy: "allowlist",      accounts: {        default: {          token: "DISCORD_BOT_TOKEN_MAIN",          guilds: {            "123456789012345678": {              channels: {                "222222222222222222": { allow: true, requireMention: false },              },            },          },        },        coding: {          token: "DISCORD_BOT_TOKEN_CODING",          guilds: {            "123456789012345678": {              channels: {                "333333333333333333": { allow: true, requireMention: false },              },            },          },        },      },    },  },}
[/code]

  * ادعُ كل بوت إلى الخادم وفعّل Message Content Intent.
  * تعيش الرموز في `channels.discord.accounts.<id>.token` (يمكن للحساب الافتراضي استخدام `DISCORD_BOT_TOKEN`).

بوتات Telegram لكل وكيل json5Copy code
[code]
    {  agents: {    list: [      { id: "main", workspace: "~/.openclaw/workspace-main" },      { id: "alerts", workspace: "~/.openclaw/workspace-alerts" },    ],  },  bindings: [    { agentId: "main", match: { channel: "telegram", accountId: "default" } },    { agentId: "alerts", match: { channel: "telegram", accountId: "alerts" } },  ],  channels: {    telegram: {      accounts: {        default: {          botToken: "123456:ABC...",          dmPolicy: "pairing",        },        alerts: {          botToken: "987654:XYZ...",          dmPolicy: "allowlist",          allowFrom: ["tg:123456789"],        },      },    },  },}
[/code]

  * أنشئ بوتًا واحدًا لكل وكيل باستخدام BotFather وانسخ كل رمز.
  * تعيش الرموز في `channels.telegram.accounts.<id>.botToken` (يمكن للحساب الافتراضي استخدام `TELEGRAM_BOT_TOKEN`).

أرقام WhatsApp لكل وكيل

اربط كل حساب قبل بدء Gateway:

bashCopy code
[code]
    openclaw channels login --channel whatsapp --account personalopenclaw channels login --channel whatsapp --account biz
[/code]

`~/.openclaw/openclaw.json` (JSON5):

jsCopy code
[code]
    {  agents: {    list: [      {        id: "home",        default: true,        name: "Home",        workspace: "~/.openclaw/workspace-home",        agentDir: "~/.openclaw/agents/home/agent",      },      {        id: "work",        name: "Work",        workspace: "~/.openclaw/workspace-work",        agentDir: "~/.openclaw/agents/work/agent",      },    ],  },   // Deterministic routing: first match wins (most-specific first).  bindings: [    { agentId: "home", match: { channel: "whatsapp", accountId: "personal" } },    { agentId: "work", match: { channel: "whatsapp", accountId: "biz" } },     // Optional per-peer override (example: send a specific group to work agent).    {      agentId: "work",      match: {        channel: "whatsapp",        accountId: "personal",        peer: { kind: "group", id: "1203630...@g.us" },      },    },  ],   // Off by default: agent-to-agent messaging must be explicitly enabled + allowlisted.  tools: {    agentToAgent: {      enabled: false,      allow: ["home", "work"],    },  },   channels: {    whatsapp: {      accounts: {        personal: {          // Optional override. Default: ~/.openclaw/credentials/whatsapp/personal          // authDir: "~/.openclaw/credentials/whatsapp/personal",        },        biz: {          // Optional override. Default: ~/.openclaw/credentials/whatsapp/biz          // authDir: "~/.openclaw/credentials/whatsapp/biz",        },      },    },  },}
[/code]

## الأنماط الشائعة

### WhatsApp اليومي + العمل العميق على Telegram

قسّم حسب القناة: وجّه WhatsApp إلى وكيل يومي سريع، وTelegram إلى وكيل Opus.

json5Copy code
[code]
    {  agents: {    list: [      {        id: "chat",        name: "Everyday",        workspace: "~/.openclaw/workspace-chat",        model: "anthropic/claude-sonnet-4-6",      },      {        id: "opus",        name: "Deep Work",        workspace: "~/.openclaw/workspace-opus",        model: "anthropic/claude-opus-4-6",      },    ],  },  bindings: [    { agentId: "chat", match: { channel: "whatsapp" } },    { agentId: "opus", match: { channel: "telegram" } },  ],}
[/code]

ملاحظات:

  * إذا كانت لديك حسابات متعددة لقناة، فأضف `accountId` إلى الربط (على سبيل المثال `{ channel: "whatsapp", accountId: "personal" }`).
  * لتوجيه رسالة مباشرة/مجموعة واحدة إلى Opus مع إبقاء البقية على الدردشة، أضف ربط `match.peer` لذلك النظير؛ تطابقات النظير تفوز دائمًا على القواعد العامة للقناة.


### القناة نفسها، نظير واحد إلى Opus

أبقِ WhatsApp على الوكيل السريع، لكن وجّه رسالة مباشرة واحدة إلى Opus:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "chat",        name: "Everyday",        workspace: "~/.openclaw/workspace-chat",        model: "anthropic/claude-sonnet-4-6",      },      {        id: "opus",        name: "Deep Work",        workspace: "~/.openclaw/workspace-opus",        model: "anthropic/claude-opus-4-6",      },    ],  },  bindings: [    {      agentId: "opus",      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551234567" } },    },    { agentId: "chat", match: { channel: "whatsapp" } },  ],}
[/code]

تفوز روابط النظير دائمًا، لذا أبقِها فوق القاعدة العامة للقناة.

### وكيل عائلي مربوط بمجموعة WhatsApp

اربط وكيلاً عائليًا مخصصًا بمجموعة WhatsApp واحدة، مع بوابة الإشارات وسياسة أدوات أكثر تشددًا:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "family",        name: "Family",        workspace: "~/.openclaw/workspace-family",        identity: { name: "Family Bot" },        groupChat: {          mentionPatterns: ["@family", "@familybot", "@Family Bot"],        },        sandbox: {          mode: "all",          scope: "agent",        },        tools: {          allow: [            "exec",            "read",            "sessions_list",            "sessions_history",            "sessions_send",            "sessions_spawn",            "session_status",          ],          deny: ["write", "edit", "apply_patch", "browser", "canvas", "nodes", "cron"],        },      },    ],  },  bindings: [    {      agentId: "family",      match: {        channel: "whatsapp",        peer: { kind: "group", id: "120363999999999999@g.us" },      },    },  ],}
[/code]

ملاحظات:

  * قوائم السماح/المنع للأدوات هي **أدوات** ، وليست Skills. إذا احتاجت إحدى Skills إلى تشغيل ملف ثنائي، فتأكد من السماح بـ `exec` ومن وجود الملف الثنائي في صندوق العزل.
  * لبوابة أكثر تشددًا، اضبط `agents.list[].groupChat.mentionPatterns` وأبقِ قوائم السماح للمجموعات مفعّلة للقناة.


## إعداد صندوق العزل والأدوات لكل وكيل

يمكن لكل وكيل أن تكون لديه قيود صندوق عزل وأدوات خاصة به:

jsCopy code
[code]
    {  agents: {    list: [      {        id: "personal",        workspace: "~/.openclaw/workspace-personal",        sandbox: {          mode: "off",  // No sandbox for personal agent        },        // No tool restrictions - all tools available      },      {        id: "family",        workspace: "~/.openclaw/workspace-family",        sandbox: {          mode: "all",     // Always sandboxed          scope: "agent",  // One container per agent          docker: {            // Optional one-time setup after container creation            setupCommand: "apt-get update && apt-get install -y git curl",          },        },        tools: {          allow: ["read"],                    // Only read tool          deny: ["exec", "write", "edit", "apply_patch"],    // Deny others        },      },    ],  },}
[/code]

**الفوائد:**

  * **عزل أمني** : قيّد الأدوات للوكلاء غير الموثوقين.
  * **التحكم في الموارد** : اعزل وكلاء محددين مع إبقاء الآخرين على المضيف.
  * **سياسات مرنة** : أذونات مختلفة لكل وكيل.


راجع [صندوق العزل والأدوات متعددة الوكلاء](</ar/tools/multi-agent-sandbox-tools>) للاطلاع على أمثلة مفصلة.

## ذات صلة

  * [وكلاء ACP](</ar/tools/acp-agents>) — تشغيل حاضنات ترميز خارجية
  * [توجيه القنوات](</ar/channels/channel-routing>) — كيف تُوجَّه الرسائل إلى الوكلاء
  * [الحضور](</ar/concepts/presence>) — حضور الوكيل وتوفره
  * [الجلسة](</ar/concepts/session>) — عزل الجلسات وتوجيهها
  * [الوكلاء الفرعيون](</ar/tools/subagents>) — بدء تشغيلات وكلاء في الخلفية


Was this useful?YesNo