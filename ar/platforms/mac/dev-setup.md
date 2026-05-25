---
title: إعداد بيئة تطوير macOS
source_url: https://docs.openclaw.ai/ar/platforms/mac/dev-setup
scraped_at: 2026-05-25
---

# إعداد المطور على macOS

ابنِ تطبيق OpenClaw على macOS وشغّله من المصدر.

## المتطلبات الأساسية

قبل بناء التطبيق، تأكد من تثبيت ما يلي:

  1. **Xcode 26.2+** : مطلوب لتطوير Swift.
  2. **Node.js 24 و pnpm** : موصى بهما لـ Gateway وCLI وسكربتات التغليف. لا يزال Node 22 LTS، حاليًا `22.16+`، مدعومًا للتوافق.


## 1\. تثبيت التبعيات

ثبّت تبعيات المشروع بالكامل:

bashCopy code
[code]
    pnpm install
[/code]

## 2\. بناء التطبيق وتغليفه

لبناء تطبيق macOS وتغليفه في `dist/OpenClaw.app`، شغّل:

bashCopy code
[code]
    ./scripts/package-mac-app.sh
[/code]

إذا لم تكن لديك شهادة Apple Developer ID، فسيستخدم السكربت تلقائيًا **التوقيع المخصص** (`-`).

لأوضاع التشغيل التطويرية، وأعلام التوقيع، واستكشاف مشكلات Team ID وإصلاحها، راجع README الخاص بتطبيق macOS: <https://github.com/openclaw/openclaw/blob/main/apps/macos/README.md>

> **ملاحظة** : قد تؤدي التطبيقات الموقّعة توقيعًا مخصصًا إلى ظهور مطالبات أمنية. إذا تعطل التطبيق فورًا برسالة "Abort trap 6"، فراجع قسم استكشاف الأخطاء وإصلاحها.

## 3\. تثبيت CLI

يتوقع تطبيق macOS تثبيت `openclaw` CLI عالميًا لإدارة المهام الخلفية.

**لتثبيته (موصى به):**

  1. افتح تطبيق OpenClaw.
  2. انتقل إلى تبويب إعدادات **عام**.
  3. انقر على **"تثبيت CLI"**.


بدلًا من ذلك، ثبّته يدويًا:

bashCopy code
[code]
    npm install -g openclaw@<version>
[/code]

يعمل أيضًا `pnpm add -g openclaw@<version>` و `bun add -g openclaw@<version>`. بالنسبة إلى وقت تشغيل Gateway، يظل Node هو المسار الموصى به.

## استكشاف الأخطاء وإصلاحها

### فشل البناء: عدم تطابق سلسلة الأدوات أو SDK

يتوقع بناء تطبيق macOS أحدث macOS SDK وسلسلة أدوات Swift 6.2.

**تبعيات النظام (مطلوبة):**

  * **أحدث إصدار من macOS متاح في Software Update** (مطلوب بواسطة حزم Xcode 26.2 SDK)
  * **Xcode 26.2** (سلسلة أدوات Swift 6.2)


**الفحوصات:**

bashCopy code
[code]
    xcodebuild -versionxcrun swift --version
[/code]

إذا لم تتطابق الإصدارات، فحدّث macOS/Xcode وأعد تشغيل البناء.

### تعطل التطبيق عند منح الإذن

إذا تعطل التطبيق عند محاولة السماح بالوصول إلى **التعرف على الكلام** أو **الميكروفون** ، فقد يكون ذلك بسبب تلف ذاكرة TCC المؤقتة أو عدم تطابق التوقيع.

**الإصلاح:**

  1. أعد ضبط أذونات TCC:

bashCopy code
[code]tccutil reset All ai.openclaw.mac.debug
[/code]

  2. إذا فشل ذلك، فغيّر `BUNDLE_ID` مؤقتًا في [`scripts/package-mac-app.sh`](<https://github.com/openclaw/openclaw/blob/main/scripts/package-mac-app.sh>) لإجبار macOS على البدء "من صفحة نظيفة".


### بقاء Gateway على "Starting..." إلى أجل غير مسمى

إذا بقيت حالة Gateway على "Starting..."، فتحقق مما إذا كانت عملية خاملة تمسك بالمنفذ:

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway stop # If you're not using a LaunchAgent (dev mode / manual runs), find the listener:lsof -nP -iTCP:18789 -sTCP:LISTEN
[/code]

إذا كان تشغيل يدوي يمسك بالمنفذ، فأوقف تلك العملية (Ctrl+C). كملاذ أخير، أنهِ PID الذي وجدته أعلاه.

## ذات صلة

  * [تطبيق macOS](</ar/platforms/macos>)
  * [نظرة عامة على التثبيت](</ar/install>)


Was this useful?YesNo