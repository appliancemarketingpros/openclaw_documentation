---
title: TUI
source_url: https://docs.openclaw.ai/ar/cli/tui
scraped_at: 2026-05-25
---

# `openclaw tui`

افتح واجهة الطرفية المتصلة بـ Gateway، أو شغّلها في الوضع المحلي المضمّن.

ذات صلة:

  * دليل TUI: [TUI](</ar/web/tui>)


## الخيارات

العلم | الافتراضي | الوصف  
---|---|---  
`--local` | `false` | التشغيل مقابل وقت تشغيل الوكيل المحلي المضمّن بدلًا من Gateway.  
`--url <url>` | `gateway.remote.url` من الإعداد | عنوان URL لـ WebSocket الخاص بـ Gateway.  
`--token <token>` | (لا شيء) | رمز Gateway إذا كان مطلوبًا.  
`--password <pass>` | (لا شيء) | كلمة مرور Gateway إذا كانت مطلوبة.  
`--session <key>` | `main` (أو `global` عندما يكون النطاق عامًا) | مفتاح الجلسة. داخل مساحة عمل وكيل، يحدد ذلك الوكيل تلقائيًا ما لم تُستخدم بادئة.  
`--deliver` | `false` | تسليم ردود المساعد عبر القنوات المُكوَّنة.  
`--thinking <level>` | (افتراضي النموذج) | تجاوز مستوى التفكير.  
`--message <text>` | (لا شيء) | إرسال رسالة أولية بعد الاتصال.  
`--timeout-ms <ms>` | `agents.defaults.timeoutSeconds` | مهلة الوكيل. القيم غير الصالحة تسجل تحذيرًا ويتم تجاهلها.  
`--history-limit <n>` | `200` | إدخالات السجل المراد تحميلها عند الإرفاق.  
  
الأسماء المستعارة: يستدعي `openclaw chat` و`openclaw terminal` الأمر نفسه مع تضمين `--local` ضمنيًا.

ملاحظات:

  * `chat` و`terminal` اسمان مستعاران لـ `openclaw tui --local`.
  * لا يمكن دمج `--local` مع `--url` أو `--token` أو `--password`.
  * يحل `tui` مراجع SecretRefs لمصادقة Gateway المُكوَّنة لمصادقة الرمز/كلمة المرور عندما يكون ذلك ممكنًا (موفرو `env`/`file`/`exec`).
  * عند تشغيله من داخل دليل مساحة عمل وكيل مُكوَّنة، يحدد TUI ذلك الوكيل تلقائيًا كافتراضي لمفتاح الجلسة (ما لم تكن `--session` صراحةً بالشكل `agent:<id>:...`).
  * يستخدم الوضع المحلي وقت تشغيل الوكيل المضمّن مباشرةً. تعمل معظم الأدوات المحلية، لكن الميزات الخاصة بـ Gateway فقط غير متاحة.
  * يضيف الوضع المحلي `/auth [provider]` داخل سطح أوامر TUI.
  * تظل بوابات موافقة Plugin مطبقة في الوضع المحلي. الأدوات التي تتطلب الموافقة تطلب قرارًا في الطرفية؛ لا تتم الموافقة التلقائية بصمت على أي شيء لمجرد أن Gateway غير مشارك.


## أمثلة

bashCopy code
[code]
    openclaw chatopenclaw tui --localopenclaw tuiopenclaw tui --url ws://127.0.0.1:18789 --token <token>openclaw tui --session main --deliveropenclaw chat --message "Compare my config to the docs and tell me what to fix"# when run inside an agent workspace, infers that agent automaticallyopenclaw tui --session bugfix
[/code]

## حلقة إصلاح الإعداد

استخدم الوضع المحلي عندما يكون الإعداد الحالي صالحًا بالفعل وتريد من الوكيل المضمّن فحصه ومقارنته بالوثائق والمساعدة في إصلاحه من الطرفية نفسها:

إذا كان `openclaw config validate` يفشل بالفعل، فاستخدم `openclaw configure` أو `openclaw doctor --fix` أولًا. لا يتجاوز `openclaw chat` حارس الإعداد غير الصالح.

bashCopy code
[code]
    openclaw chat
[/code]

ثم داخل TUI:

textCopy code
[code]
    !openclaw config file!openclaw docs gateway auth token secretref!openclaw config validate!openclaw doctor
[/code]

طبّق إصلاحات موجّهة باستخدام `openclaw config set` أو `openclaw configure`، ثم أعد تشغيل `openclaw config validate`. راجع [TUI](</ar/web/tui>) و[الإعداد](</ar/cli/config>).

## ذات صلة

  * [مرجع CLI](</ar/cli>)
  * [TUI](</ar/web/tui>)


Was this useful?YesNo