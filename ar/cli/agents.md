---
title: الوكلاء
source_url: https://docs.openclaw.ai/ar/cli/agents
scraped_at: 2026-05-25
---

# `openclaw agents`

إدارة الوكلاء المعزولين (مساحات العمل + المصادقة + التوجيه).

ذات صلة:

  * [التوجيه متعدد الوكلاء](</ar/concepts/multi-agent>)
  * [مساحة عمل الوكيل](</ar/concepts/agent-workspace>)
  * [تكوين Skills](</ar/tools/skills-config>): تكوين إتاحة المهارات.


## أمثلة

bashCopy code
[code]
    openclaw agents listopenclaw agents list --bindingsopenclaw agents add work --workspace ~/.openclaw/workspace-workopenclaw agents add ops --workspace ~/.openclaw/workspace-ops --bind telegram:ops --non-interactiveopenclaw agents bindingsopenclaw agents bind --agent work --bind telegram:opsopenclaw agents unbind --agent work --bind telegram:opsopenclaw agents set-identity --workspace ~/.openclaw/workspace --from-identityopenclaw agents set-identity --agent main --avatar avatars/openclaw.pngopenclaw agents delete work
[/code]

## ارتباطات التوجيه

استخدم ارتباطات التوجيه لتثبيت حركة مرور القنوات الواردة على وكيل محدد.

إذا كنت تريد أيضا Skills مرئية مختلفة لكل وكيل، فكوّن `agents.defaults.skills` و`agents.list[].skills` في `openclaw.json`. راجع [تكوين Skills](</ar/tools/skills-config>) و[مرجع التكوين](</ar/gateway/config-agents#agents-defaults-skills>).

عرض الارتباطات:

bashCopy code
[code]
    openclaw agents bindingsopenclaw agents bindings --agent workopenclaw agents bindings --json
[/code]

إضافة ارتباطات:

bashCopy code
[code]
    openclaw agents bind --agent work --bind telegram:ops --bind discord:guild-a
[/code]

إذا حذفت `accountId` (`--bind <channel>`)، فسيحله OpenClaw من إعدادات القناة الافتراضية وخطافات إعداد Plugin عند توفرها.

إذا حذفت `--agent` مع `bind` أو `unbind`، فسيستهدف OpenClaw الوكيل الافتراضي الحالي.

### سلوك نطاق الارتباط

  * الارتباط من دون `accountId` يطابق حساب القناة الافتراضي فقط.
  * `accountId: "*"` هو خيار الرجوع على مستوى القناة (كل الحسابات)، وهو أقل تحديدا من ارتباط حساب صريح.
  * إذا كان لدى الوكيل نفسه مسبقا ارتباط قناة مطابق من دون `accountId`، ثم ربطت لاحقا باستخدام `accountId` صريح أو محلول، فسيحدّث OpenClaw ذلك الارتباط الموجود في مكانه بدلا من إضافة نسخة مكررة.


مثال:

bashCopy code
[code]
    # initial channel-only bindingopenclaw agents bind --agent work --bind telegram # later upgrade to account-scoped bindingopenclaw agents bind --agent work --bind telegram:ops
[/code]

بعد الترقية، يصبح توجيه ذلك الارتباط محصورا في `telegram:ops`. إذا كنت تريد أيضا توجيه حساب افتراضي، فأضفه صراحة (مثلا `--bind telegram:default`).

إزالة الارتباطات:

bashCopy code
[code]
    openclaw agents unbind --agent work --bind telegram:opsopenclaw agents unbind --agent work --all
[/code]

يقبل `unbind` إما `--all` أو قيمة واحدة أو أكثر من قيم `--bind`، وليس كليهما.

## واجهة الأوامر

### `agents`

تشغيل `openclaw agents` بلا أمر فرعي يعادل `openclaw agents list`.

### `agents list`

الخيارات:

  * `--json`
  * `--bindings`: تضمين قواعد التوجيه الكاملة، وليس فقط الأعداد/الملخصات لكل وكيل


### `agents add [name]`

الخيارات:

  * `--workspace <dir>`
  * `--model <id>`
  * `--agent-dir <dir>`
  * `--bind <channel[:accountId]>` (قابل للتكرار)
  * `--non-interactive`
  * `--json`


ملاحظات:

  * تمرير أي أعلام إضافة صريحة ينقل الأمر إلى المسار غير التفاعلي.
  * يتطلب الوضع غير التفاعلي كلا من اسم وكيل و`--workspace`.
  * `main` محجوز ولا يمكن استخدامه كمعرف الوكيل الجديد.
  * في الوضع التفاعلي، تنسخ تعبئة المصادقة ملفات التعريف الثابتة القابلة للنقل فقط (`api_key` و`token` الثابت افتراضيا). تظل ملفات تعريف رموز تحديث OAuth متاحة فقط عبر الوراثة بالقراءة من مخزن وكيل `main` الحقيقي. إذا لم يكن الوكيل الافتراضي المكوّن هو `main`، فسجّل الدخول بشكل منفصل إلى ملفات تعريف OAuth على الوكيل الجديد.


### `agents bindings`

الخيارات:

  * `--agent <id>`
  * `--json`


### `agents bind`

الخيارات:

  * `--agent <id>` (يعود افتراضيا إلى الوكيل الافتراضي الحالي)
  * `--bind <channel[:accountId]>` (قابل للتكرار)
  * `--json`


### `agents unbind`

الخيارات:

  * `--agent <id>` (يعود افتراضيا إلى الوكيل الافتراضي الحالي)
  * `--bind <channel[:accountId]>` (قابل للتكرار)
  * `--all`
  * `--json`


### `agents delete <id>`

الخيارات:

  * `--force`
  * `--json`


ملاحظات:

  * لا يمكن حذف `main`.
  * من دون `--force`، يلزم تأكيد تفاعلي.
  * تُنقل أدلة مساحة العمل وحالة الوكيل ونصوص الجلسات إلى المهملات، ولا تُحذف حذفا نهائيا.
  * عندما يكون Gateway قابلا للوصول، يُرسل الحذف عبر Gateway بحيث يشترك تنظيف التكوين ومخزن الجلسات في الكاتب نفسه مثل حركة المرور وقت التشغيل. إذا تعذر الوصول إلى Gateway، يعود CLI إلى المسار المحلي غير المتصل.
  * إذا كانت مساحة عمل وكيل آخر هي المسار نفسه، أو داخل مساحة العمل هذه، أو تحتوي على مساحة العمل هذه، فيتم الاحتفاظ بمساحة العمل ويبلّغ `--json` عن `workspaceRetained`، و`workspaceRetainedReason`، و`workspaceSharedWith`.


## ملفات الهوية

يمكن أن تتضمن كل مساحة عمل وكيل ملف `IDENTITY.md` في جذر مساحة العمل:

  * مسار مثال: `~/.openclaw/workspace/IDENTITY.md`
  * يقرأ `set-identity --from-identity` من جذر مساحة العمل (أو من `--identity-file` صريح)


تُحل مسارات الصور الرمزية نسبيا إلى جذر مساحة العمل.

## تعيين الهوية

يكتب `set-identity` الحقول في `agents.list[].identity`:

  * `name`
  * `theme`
  * `emoji`
  * `avatar` (مسار نسبي إلى مساحة العمل، أو عنوان URL بنمط http(s)، أو URI بيانات)


الخيارات:

  * `--agent <id>`
  * `--workspace <dir>`
  * `--identity-file <path>`
  * `--from-identity`
  * `--name <name>`
  * `--theme <theme>`
  * `--emoji <emoji>`
  * `--avatar <value>`
  * `--json`


ملاحظات:

  * يمكن استخدام `--agent` أو `--workspace` لاختيار الوكيل الهدف.
  * إذا اعتمدت على `--workspace` وكان عدة وكلاء يتشاركون مساحة العمل تلك، فسيفشل الأمر ويطلب منك تمرير `--agent`.
  * عندما لا تُقدَّم حقول هوية صريحة، يقرأ الأمر بيانات الهوية من `IDENTITY.md`.


التحميل من `IDENTITY.md`:

bashCopy code
[code]
    openclaw agents set-identity --workspace ~/.openclaw/workspace --from-identity
[/code]

تجاوز الحقول صراحة:

bashCopy code
[code]
    openclaw agents set-identity --agent main --name "OpenClaw" --emoji "🦞" --avatar avatars/openclaw.png
[/code]

عينة تكوين:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "main",        identity: {          name: "OpenClaw",          theme: "space lobster",          emoji: "🦞",          avatar: "avatars/openclaw.png",        },      },    ],  },}
[/code]

## ذات صلة

  * [مرجع CLI](</ar/cli>)
  * [التوجيه متعدد الوكلاء](</ar/concepts/multi-agent>)
  * [مساحة عمل الوكيل](</ar/concepts/agent-workspace>)


Was this useful?YesNo