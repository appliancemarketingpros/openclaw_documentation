---
title: الدليل
source_url: https://docs.openclaw.ai/ar/cli/directory
scraped_at: 2026-05-25
---

# `openclaw directory`

عمليات البحث في الدليل للقنوات التي تدعم ذلك (جهات الاتصال/الأقران، والمجموعات، و"أنا").

## العلامات الشائعة

  * `--channel <name>`: معرّف/اسم مستعار للقناة (مطلوب عند تكوين عدة قنوات؛ تلقائي عند تكوين قناة واحدة فقط)
  * `--account <id>`: معرّف الحساب (الافتراضي: افتراضي القناة)
  * `--json`: إخراج JSON


## ملاحظات

  * يهدف `directory` إلى مساعدتك في العثور على المعرّفات التي يمكنك لصقها في أوامر أخرى (خصوصًا `openclaw message send --target ...`).
  * بالنسبة إلى كثير من القنوات، تكون النتائج مستندة إلى التكوين (قوائم السماح / المجموعات المكوّنة) بدلًا من دليل موفّر مباشر.
  * لا يزال بإمكان Plugins القنوات المثبتة إغفال دعم الدليل؛ في هذه الحالة يبلّغ الأمر عن عملية الدليل غير المدعومة بدلًا من إعادة تثبيت Plugin.
  * الإخراج الافتراضي هو `id` (وأحيانًا `name`) مفصولًا بعلامة تبويب؛ استخدم `--json` للبرمجة النصية.


## استخدام النتائج مع `message send`

bashCopy code
[code]
    openclaw directory peers list --channel slack --query "U0"openclaw message send --channel slack --target user:U012ABCDEF --message "hello"
[/code]

## صيغ المعرّفات (حسب القناة)

  * WhatsApp: `+15551234567` (رسالة مباشرة)، `1234567890-1234567890@g.us` (مجموعة)، `120363123456789@newsletter` (هدف صادر لقناة/نشرة إخبارية)
  * Telegram: `@username` أو معرّف دردشة رقمي؛ المجموعات هي معرّفات رقمية
  * Slack: `user:U…` و`channel:C…`
  * Discord: `user:<id>` و`channel:<id>`
  * Matrix (Plugin): `user:@user:server` أو `room:!roomId:server` أو `#alias:server`
  * Microsoft Teams (Plugin): `user:<id>` و`conversation:<id>`
  * Zalo (Plugin): معرّف المستخدم (Bot API)
  * Zalo Personal / `zalouser` (Plugin): معرّف سلسلة المحادثة (رسالة مباشرة/مجموعة) من `zca` (`me`، `friend list`، `group list`)


## الذات ("أنا")

bashCopy code
[code]
    openclaw directory self --channel zalouser
[/code]

## الأقران (جهات الاتصال/المستخدمون)

bashCopy code
[code]
    openclaw directory peers list --channel zalouseropenclaw directory peers list --channel zalouser --query "name"openclaw directory peers list --channel zalouser --limit 50
[/code]

## المجموعات

bashCopy code
[code]
    openclaw directory groups list --channel zalouseropenclaw directory groups list --channel zalouser --query "work"openclaw directory groups members --channel zalouser --group-id <id>
[/code]

## ذات صلة

  * [مرجع CLI](</ar/cli>)


Was this useful?YesNo