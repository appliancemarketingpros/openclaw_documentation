---
title: Nix
source_url: https://docs.openclaw.ai/ar/install/nix
scraped_at: 2026-05-25
---

ثبّت OpenClaw تصريحيًا باستخدام **[nix-openclaw](<https://github.com/openclaw/nix-openclaw>)** \- وحدة Home Manager الرسمية الشاملة.

## ما الذي تحصل عليه

  * Gateway + تطبيق macOS + الأدوات (whisper، spotify، الكاميرات) -- جميعها مثبتة الإصدارات
  * خدمة launchd تصمد بعد إعادة التشغيل
  * نظام Plugin مع إعدادات تصريحية
  * تراجع فوري: `home-manager switch --rollback`


## البدء السريع

* ### ثبّت Determinate Nix

إذا لم يكن Nix مثبتًا بالفعل، فاتبع تعليمات [مثبّت Determinate Nix](<https://github.com/DeterminateSystems/nix-installer>).

* ### أنشئ flake محليًا

استخدم قالب agent-first من مستودع nix-openclaw:

bashCopy code
[code]
    mkdir -p ~/code/openclaw-local# Copy templates/agent-first/flake.nix from the nix-openclaw repo
[/code]

* ### اضبط الأسرار

أعدّ رمز بوت المراسلة ومفتاح API لمزوّد النموذج. الملفات النصية البسيطة في `~/.secrets/` تعمل جيدًا.

* ### املأ عناصر نائبة القالب وبدّل

bashCopy code
[code]
    home-manager switch
[/code]

* ### تحقّق

تأكّد من أن خدمة launchd قيد التشغيل وأن بوتك يرد على الرسائل.

راجع [README الخاص بـ nix-openclaw](<https://github.com/openclaw/nix-openclaw>) للاطلاع على جميع خيارات الوحدة والأمثلة.

## سلوك وقت التشغيل في وضع Nix

عند تعيين `OPENCLAW_NIX_MODE=1` (تلقائيًا مع nix-openclaw)، يدخل OpenClaw وضعًا حتميًا للتثبيتات المُدارة بواسطة Nix. يمكن لحزم Nix الأخرى تعيين الوضع نفسه؛ ويُعد nix-openclaw المرجع الرسمي.

يمكنك أيضًا تعيينه يدويًا:

bashCopy code
[code]
    export OPENCLAW_NIX_MODE=1
[/code]

على macOS، لا يرث تطبيق الواجهة الرسومية متغيرات بيئة الصدفة تلقائيًا. فعّل وضع Nix عبر defaults بدلًا من ذلك:

bashCopy code
[code]
    defaults write ai.openclaw.mac openclaw.nixMode -bool true
[/code]

### ما الذي يتغير في وضع Nix

  * تُعطّل تدفقات التثبيت التلقائي والتعديل الذاتي
  * يُعامل `openclaw.json` كملف غير قابل للتغيير. تبقى القيم الافتراضية المشتقة عند بدء التشغيل خاصة بوقت التشغيل فقط، وترفض كاتبات الإعدادات مثل الإعداد الأولي، والتهيئة، و`openclaw update` المُعدِّل، وتثبيت/تحديث/إلغاء تثبيت/تمكين Plugin، و`doctor --fix`، و`doctor --generate-gateway-token`، و`openclaw config set` تعديل الملف.
  * ينبغي للوكلاء تعديل مصدر Nix بدلًا من ذلك. بالنسبة إلى nix-openclaw، استخدم [البدء السريع](<https://github.com/openclaw/nix-openclaw#quick-start>) الخاص بـ agent-first وعيّن الإعدادات ضمن `programs.openclaw.config` أو `instances.<name>.config`.
  * تعرض الاعتماديات المفقودة رسائل إصلاح خاصة بـ Nix
  * تعرض واجهة المستخدم شريط وضع Nix للقراءة فقط


### مسارات الإعدادات والحالة

يقرأ OpenClaw إعدادات JSON5 من `OPENCLAW_CONFIG_PATH` ويخزّن البيانات القابلة للتغيير في `OPENCLAW_STATE_DIR`. عند التشغيل تحت Nix، عيّن هذه القيم صراحةً إلى مواقع مُدارة بواسطة Nix حتى تبقى حالة وقت التشغيل والإعدادات خارج المخزن غير القابل للتغيير.

المتغير | الافتراضي  
---|---  
`OPENCLAW_HOME` | `HOME` / `USERPROFILE` / `os.homedir()`  
`OPENCLAW_STATE_DIR` | `~/.openclaw`  
`OPENCLAW_CONFIG_PATH` | `$OPENCLAW_STATE_DIR/openclaw.json`  
  
### اكتشاف PATH للخدمة

تكتشف خدمة Gateway في launchd/systemd ثنائيات ملف تعريف Nix تلقائيًا بحيث تعمل Plugin والأدوات التي تستدعي ملفات تنفيذية مثبتة عبر `nix` من الصدفة دون إعداد PATH يدويًا:

  * عند تعيين `NIX_PROFILES`، تُضاف كل خانة إلى PATH الخاص بالخدمة وفق أسبقية من اليمين إلى اليسار (تطابق أسبقية صدفة Nix - الأيمن يفوز).
  * عند عدم تعيين `NIX_PROFILES`، يُضاف `~/.nix-profile/bin` كبديل احتياطي.


ينطبق هذا على بيئات خدمة macOS launchd وLinux systemd كليهما.

## ذات صلة

[**nix-openclaw** وحدة Home Manager مصدر الحقيقة ودليل الإعداد الكامل. ](<https://github.com/openclaw/nix-openclaw>) [**معالج الإعداد** شرح تفصيلي لإعداد CLI من دون Nix. ](</ar/start/wizard>) [**Docker** إعداد حاويات كبديل غير قائم على Nix. ](</ar/install/docker>) [**التحديث** تحديث التثبيتات المُدارة بواسطة Home Manager مع الحزمة. ](</ar/install/updating>)

Was this useful?YesNo