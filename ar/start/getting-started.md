---
title: بدء الاستخدام
source_url: https://docs.openclaw.ai/ar/start/getting-started
scraped_at: 2026-05-25
---

ثبّت OpenClaw، وشغّل الإعداد الأولي، وتحدث مع مساعد الذكاء الاصطناعي الخاص بك — كل ذلك في نحو 5 دقائق. في النهاية سيكون لديك Gateway قيد التشغيل، ومصادقة مهيّأة، وجلسة دردشة عاملة.

## ما تحتاجه

  * **Node.js** — يُوصى باستخدام Node 24 (Node 22.16+ مدعوم أيضًا)
  * **مفتاح API** من مزوّد نماذج (Anthropic أو OpenAI أو Google أو غيرها) — سيطلبه منك الإعداد الأولي


## الإعداد السريع

* ### ثبّت OpenClaw

### macOS / Linux

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

![عملية سكربت التثبيت](/assets/install-script.svg)

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

* ### شغّل الإعداد الأولي

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

يرشدك المعالج خلال اختيار مزوّد نماذج، وتعيين مفتاح API، وتهيئة Gateway. يستغرق ذلك نحو دقيقتين.

راجع [الإعداد الأولي (CLI)](</ar/start/wizard>) للاطلاع على المرجع الكامل.

* ### تحقق من أن Gateway قيد التشغيل

bashCopy code
[code]
    openclaw gateway status
[/code]

ينبغي أن ترى Gateway يستمع على المنفذ 18789.

* ### افتح لوحة التحكم

bashCopy code
[code]
    openclaw dashboard
[/code]

يفتح هذا واجهة التحكم في متصفحك. إذا تم تحميلها، فكل شيء يعمل.

* ### أرسل رسالتك الأولى

اكتب رسالة في دردشة واجهة التحكم، وينبغي أن تتلقى ردًا من الذكاء الاصطناعي.

هل تريد الدردشة من هاتفك بدلًا من ذلك؟ أسرع قناة يمكن إعدادها هي [Telegram](</ar/channels/telegram>) (مجرد رمز بوت). راجع [القنوات](</ar/channels>) للاطلاع على كل الخيارات.

متقدم: تثبيت إصدار مخصص من واجهة التحكم

إذا كنت تدير إصدارًا مترجمًا أو مخصصًا من لوحة التحكم، فاجعل `gateway.controlUi.root` يشير إلى دليل يحتوي على الأصول الثابتة المبنية لديك و`index.html`.

bashCopy code
[code]
    mkdir -p "$HOME/.openclaw/control-ui-custom"# Copy your built static files into that directory.
[/code]

ثم عيّن:

jsonCopy code
[code]
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "$HOME/.openclaw/control-ui-custom"  }}}
[/code]

أعد تشغيل Gateway وافتح لوحة التحكم من جديد:

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## ما الخطوة التالية

[**وصّل قناة** Discord وFeishu وiMessage وMatrix وMicrosoft Teams وSignal وSlack وTelegram وWhatsApp وZalo والمزيد. ](</ar/channels>) [**الاقتران والسلامة** تحكّم في من يمكنه مراسلة وكيلك. ](</ar/channels/pairing>) [**هيّئ Gateway** النماذج والأدوات وبيئة العزل والإعدادات المتقدمة. ](</ar/gateway/configuration>) [**تصفّح الأدوات** المتصفح وexec وبحث الويب وSkills وPlugins. ](</ar/tools>)

متقدم: متغيرات البيئة

إذا كنت تشغّل OpenClaw كحساب خدمة أو تريد مسارات مخصصة:

  * `OPENCLAW_HOME` — الدليل الرئيسي لحلّ المسارات الداخلية
  * `OPENCLAW_STATE_DIR` — تجاوز دليل الحالة
  * `OPENCLAW_CONFIG_PATH` — تجاوز مسار ملف الإعدادات


المرجع الكامل: [متغيرات البيئة](</ar/help/environment>).

## ذات صلة

  * [نظرة عامة على التثبيت](</ar/install>)
  * [نظرة عامة على القنوات](</ar/channels>)
  * [الإعداد](</ar/start/setup>)


Was this useful?YesNo