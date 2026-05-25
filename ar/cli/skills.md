---
title: Skills
source_url: https://docs.openclaw.ai/ar/cli/skills
scraped_at: 2026-05-25
---

# `openclaw skills`

افحص Skills المحلية وثبّت/حدّث Skills من ClawHub.

ذات صلة:

  * نظام Skills: [Skills](</ar/tools/skills>)
  * إعدادات Skills: [إعدادات Skills](</ar/tools/skills-config>)
  * تثبيتات ClawHub: [ClawHub](</ar/clawhub/cli>)


## الأوامر

bashCopy code
[code]
    openclaw skills search "calendar"openclaw skills search --limit 20 --jsonopenclaw skills install <slug>openclaw skills install <slug> --version <version>openclaw skills install <slug> --forceopenclaw skills install <slug> --agent <id>openclaw skills update <slug>openclaw skills update --allopenclaw skills update --all --agent <id>openclaw skills listopenclaw skills list --eligibleopenclaw skills list --jsonopenclaw skills list --verboseopenclaw skills list --agent <id>openclaw skills info <name>openclaw skills info <name> --jsonopenclaw skills info <name> --agent <id>openclaw skills checkopenclaw skills check --agent <id>openclaw skills check --json
[/code]

تستخدم `search`/`install`/`update` ClawHub مباشرة وتثبّت في دليل `skills/` لمساحة العمل النشطة. لا تزال `list`/`info`/`check` تفحص Skills المحلية المرئية لمساحة العمل الحالية والإعدادات. تحل الأوامر المدعومة بمساحة العمل مساحة العمل الهدف من `--agent <id>`، ثم دليل العمل الحالي عندما يكون داخل مساحة عمل وكيل مهيأة، ثم الوكيل الافتراضي.

ينزّل أمر `install` في CLI هذا مجلدات Skills من ClawHub. أما تثبيتات تبعيات Skills المدعومة من Gateway والتي تُشغّل من الإعداد الأولي أو إعدادات Skills فتستخدم مسار طلب `skills.install` المنفصل بدلا من ذلك.

ملاحظات:

  * يقبل `search [query...]` استعلاما اختياريا؛ احذفه لتصفح موجز بحث ClawHub الافتراضي.
  * يحد `search --limit <n>` عدد النتائج المُعادة.
  * يستبدل `install --force` مجلد Skill موجودا في مساحة العمل للـ slug نفسه.
  * يستهدف `--agent <id>` مساحة عمل وكيل مهيأة واحدة ويتجاوز استنتاج دليل العمل الحالي.
  * يحدّث `update --all` فقط تثبيتات ClawHub المتتبعة في مساحة العمل النشطة.
  * يفحص `check --agent <id>` مساحة عمل الوكيل المحدد ويبلغ عن Skills الجاهزة المرئية فعليا لسطح أوامر ذلك الوكيل أو موجّهه.
  * `list` هو الإجراء الافتراضي عند عدم تقديم أمر فرعي.
  * تكتب `list` و`info` و`check` المخرجات المعروضة إلى stdout. مع `--json`، يعني ذلك أن الحمولة المقروءة آليا تبقى على stdout للأنابيب والسكربتات.


## ذات صلة

  * [مرجع CLI](</ar/cli>)
  * [Skills](</ar/tools/skills>)


Was this useful?YesNo