---
title: آلات macOS الافتراضية
source_url: https://docs.openclaw.ai/ar/install/macos-vm
scraped_at: 2026-05-25
---

## الإعداد الافتراضي الموصى به (معظم المستخدمين)

  * **خادم Linux VPS صغير** لتشغيل Gateway دائمًا وبتكلفة منخفضة. راجع [استضافة VPS](</ar/vps>).
  * **عتاد مخصص** (Mac mini أو جهاز Linux) إذا كنت تريد تحكمًا كاملًا و**عنوان IP سكنيًا** لأتمتة المتصفح. تحظر مواقع كثيرة عناوين IP الخاصة بمراكز البيانات، لذلك غالبًا ما يعمل التصفح المحلي بشكل أفضل.
  * **هجين:** أبقِ Gateway على VPS رخيص، ووصل جهاز Mac الخاص بك باعتباره **Node** عندما تحتاج إلى أتمتة المتصفح/واجهة المستخدم. راجع [Nodes](</ar/nodes>) و[Gateway عن بعد](</ar/gateway/remote>).


استخدم آلة macOS افتراضية عندما تحتاج تحديدًا إلى قدرات متاحة على macOS فقط مثل iMessage أو تريد عزلًا صارمًا عن جهاز Mac اليومي الخاص بك.

## خيارات آلة macOS الافتراضية

### آلة افتراضية محلية على جهاز Apple Silicon Mac الخاص بك (Lume)

شغّل OpenClaw في آلة macOS افتراضية معزولة على جهاز Apple Silicon Mac الحالي لديك باستخدام [Lume](<https://cua.ai/docs/lume>).

يمنحك هذا:

  * بيئة macOS كاملة ومعزولة (يبقى المضيف لديك نظيفًا)
  * دعم iMessage عبر `imsg` (المسار المحلي الافتراضي مستحيل على Linux/Windows)
  * إعادة ضبط فورية عبر استنساخ الآلات الافتراضية
  * دون عتاد إضافي أو تكاليف سحابية


### مزودو Mac المستضافون (السحابة)

إذا كنت تريد macOS في السحابة، فإن مزودي Mac المستضافين يعملون أيضًا:

  * [MacStadium](<https://www.macstadium.com/>) (أجهزة Mac مستضافة)
  * يعمل موردو Mac المستضافون الآخرون أيضًا؛ اتبع وثائقهم الخاصة بالآلة الافتراضية وSSH


بعد أن تحصل على وصول SSH إلى آلة macOS افتراضية، تابع من الخطوة 6 أدناه.

* * *

## المسار السريع (Lume، للمستخدمين ذوي الخبرة)

  1. ثبّت Lume
  2. `lume create openclaw --os macos --ipsw latest`
  3. أكمل مساعد الإعداد، وفعّل تسجيل الدخول عن بعد (SSH)
  4. `lume run openclaw --no-display`
  5. ادخل عبر SSH، وثبّت OpenClaw، واضبط القنوات
  6. انتهى


* * *

## ما تحتاجه (Lume)

  * جهاز Apple Silicon Mac ‏(M1/M2/M3/M4)
  * macOS Sequoia أو أحدث على المضيف
  * نحو 60 غيغابايت من مساحة القرص الحرة لكل آلة افتراضية
  * نحو 20 دقيقة


* * *

## 1) تثبيت Lume

bashCopy code
[code]
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"
[/code]

إذا لم يكن `~/.local/bin` ضمن PATH لديك:

bashCopy code
[code]
    echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.zshrc && source ~/.zshrc
[/code]

تحقق:

bashCopy code
[code]
    lume --version
[/code]

الوثائق: [تثبيت Lume](<https://cua.ai/docs/lume/guide/getting-started/installation>)

* * *

## 2) إنشاء آلة macOS الافتراضية

bashCopy code
[code]
    lume create openclaw --os macos --ipsw latest
[/code]

يؤدي هذا إلى تنزيل macOS وإنشاء الآلة الافتراضية. تُفتح نافذة VNC تلقائيًا.

* * *

## 3) إكمال مساعد الإعداد

في نافذة VNC:

  1. حدد اللغة والمنطقة
  2. تخطّ Apple ID (أو سجّل الدخول إذا كنت تريد iMessage لاحقًا)
  3. أنشئ حساب مستخدم (تذكر اسم المستخدم وكلمة المرور)
  4. تخطّ كل الميزات الاختيارية


بعد اكتمال الإعداد، فعّل SSH:

  1. افتح إعدادات النظام ← عام ← المشاركة
  2. فعّل "تسجيل الدخول عن بعد"


* * *

## 4) الحصول على عنوان IP للآلة الافتراضية

bashCopy code
[code]
    lume get openclaw
[/code]

ابحث عن عنوان IP (عادةً `192.168.64.x`).

* * *

## 5) الدخول إلى الآلة الافتراضية عبر SSH

bashCopy code
[code]
    ssh youruser@192.168.64.X
[/code]

استبدل `youruser` بالحساب الذي أنشأته، واستبدل عنوان IP بعنوان IP الخاص بآلتك الافتراضية.

* * *

## 6) تثبيت OpenClaw

داخل الآلة الافتراضية:

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

اتبع مطالبات الإعداد الأولي لإعداد مزود النموذج لديك (Anthropic وOpenAI وما إلى ذلك).

* * *

## 7) ضبط القنوات

حرر ملف الإعداد:

bashCopy code
[code]
    nano ~/.openclaw/openclaw.json
[/code]

أضف قنواتك:

json5Copy code
[code]
    {  channels: {    whatsapp: {      dmPolicy: "allowlist",      allowFrom: ["+15551234567"],    },    telegram: {      botToken: "YOUR_BOT_TOKEN",    },  },}
[/code]

ثم سجّل الدخول إلى WhatsApp (امسح رمز QR):

bashCopy code
[code]
    openclaw channels login
[/code]

* * *

## 8) تشغيل الآلة الافتراضية بلا واجهة عرض

أوقف الآلة الافتراضية وأعد تشغيلها دون عرض:

bashCopy code
[code]
    lume stop openclawlume run openclaw --no-display
[/code]

تعمل الآلة الافتراضية في الخلفية. يحافظ عفريت OpenClaw على تشغيل Gateway.

للتحقق من الحالة:

bashCopy code
[code]
    ssh youruser@192.168.64.X "openclaw status"
[/code]

* * *

## إضافة: تكامل iMessage

هذه هي الميزة الأهم للتشغيل على macOS. استخدم [iMessage](</ar/channels/imessage>) مع `imsg` لإضافة Messages إلى OpenClaw.

داخل الآلة الافتراضية:

  1. سجّل الدخول إلى Messages.
  2. ثبّت `imsg`.
  3. امنح إذن الوصول الكامل إلى القرص وإذن الأتمتة للعملية التي تشغّل OpenClaw/`imsg`.
  4. تحقق من دعم RPC باستخدام `imsg rpc --help`.


أضف إلى إعداد OpenClaw لديك:

json5Copy code
[code]
    {  channels: {    imessage: {      enabled: true,      cliPath: "imsg",      dbPath: "~/Library/Messages/chat.db",    },  },}
[/code]

أعد تشغيل Gateway. يمكن لوكيلك الآن إرسال رسائل iMessage واستلامها.

تفاصيل الإعداد الكاملة: [قناة iMessage](</ar/channels/imessage>)

* * *

## حفظ صورة ذهبية

قبل المزيد من التخصيص، التقط لقطة لحالتك النظيفة:

bashCopy code
[code]
    lume stop openclawlume clone openclaw openclaw-golden
[/code]

أعد الضبط في أي وقت:

bashCopy code
[code]
    lume stop openclaw && lume delete openclawlume clone openclaw-golden openclawlume run openclaw --no-display
[/code]

* * *

## التشغيل على مدار الساعة

أبقِ الآلة الافتراضية قيد التشغيل عبر:

  * إبقاء جهاز Mac موصولًا بالطاقة
  * تعطيل السكون في إعدادات النظام ← موفر الطاقة
  * استخدام `caffeinate` عند الحاجة


للتشغيل الدائم الحقيقي، فكّر في Mac mini مخصص أو VPS صغير. راجع [استضافة VPS](</ar/vps>).

* * *

## استكشاف الأخطاء وإصلاحها

المشكلة | الحل  
---|---  
لا يمكن الدخول إلى الآلة الافتراضية عبر SSH | تحقق من تفعيل "تسجيل الدخول عن بعد" في إعدادات النظام الخاصة بالآلة الافتراضية  
لا يظهر عنوان IP للآلة الافتراضية | انتظر حتى تكتمل عملية إقلاع الآلة الافتراضية، ثم شغّل `lume get openclaw` مرة أخرى  
لم يتم العثور على أمر Lume | أضف `~/.local/bin` إلى PATH لديك  
لا يتم مسح رمز WhatsApp QR | تأكد من أنك مسجل الدخول إلى الآلة الافتراضية (وليس المضيف) عند تشغيل `openclaw channels login`  
  
* * *

## الوثائق ذات الصلة

  * [استضافة VPS](</ar/vps>)
  * [Nodes](</ar/nodes>)
  * [Gateway عن بعد](</ar/gateway/remote>)
  * [قناة iMessage](</ar/channels/imessage>)
  * [بدء Lume السريع](<https://cua.ai/docs/lume/guide/getting-started/quickstart>)
  * [مرجع CLI الخاص بـ Lume](<https://cua.ai/docs/lume/reference/cli-reference>)
  * [إعداد آلة افتراضية دون حضور](<https://cua.ai/docs/lume/guide/fundamentals/unattended-setup>) (متقدم)
  * [عزل Docker](</ar/install/docker>) (نهج عزل بديل)


Was this useful?YesNo