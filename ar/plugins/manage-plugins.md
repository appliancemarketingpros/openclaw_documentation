---
title: إدارة Plugins
source_url: https://docs.openclaw.ai/ar/plugins/manage-plugins
scraped_at: 2026-05-25
---

معظم سير عمل Plugin عبارة عن بضعة أوامر: البحث، والتثبيت، وإعادة تشغيل Gateway، والتحقق، وإلغاء التثبيت عندما لا تعود بحاجة إلى Plugin.

## عرض Plugins

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --json
[/code]

استخدم `--json` مع السكربتات. فهو يتضمن تشخيصات السجل وحالة `dependencyStatus` الثابتة لكل Plugin عندما تعلن حزمة Plugin عن `dependencies` أو `optionalDependencies`.

bashCopy code
[code]
    openclaw plugins list --json \  | jq '.plugins[] | {id, enabled, format, source, dependencyStatus}'
[/code]

`plugins list` هو فحص مخزون بارد. يعرض ما يستطيع OpenClaw اكتشافه من الإعدادات والبيانات الوصفية وسجل Plugin؛ ولا يثبت أن عملية Gateway قيد التشغيل بالفعل قد استوردت وقت تشغيل Plugin.

## تثبيت Plugins

bashCopy code
[code]
    # Search ClawHub for plugin packages.openclaw plugins search "calendar" # Bare package specs try ClawHub first, then npm fallback.openclaw plugins install <package> # Force one source.openclaw plugins install clawhub:<package>openclaw plugins install npm:<package> # Install a specific version or dist-tag.openclaw plugins install clawhub:<package>@1.2.3openclaw plugins install clawhub:<package>@betaopenclaw plugins install npm:@scope/openclaw-plugin@1.2.3openclaw plugins install npm:@openclaw/codex # Install from git or a local development checkout.openclaw plugins install git:github.com/acme/openclaw-plugin@v1.0.0openclaw plugins install ./my-pluginopenclaw plugins install --link ./my-plugin
[/code]

بعد تثبيت كود Plugin، أعد تشغيل Gateway الذي يخدم قنواتك:

bashCopy code
[code]
    openclaw gateway restartopenclaw plugins inspect <plugin-id> --runtime --json
[/code]

استخدم `inspect --runtime` عندما تحتاج إلى دليل على أن Plugin سجّل أسطح وقت التشغيل مثل الأدوات أو الخطافات أو الخدمات أو أساليب Gateway أو أوامر CLI المملوكة لـ Plugin.

## تحديث Plugins

bashCopy code
[code]
    openclaw plugins update <plugin-id>openclaw plugins update <npm-package-or-spec>openclaw plugins update --all
[/code]

إذا كان Plugin قد ثُبّت من وسم توزيع npm مثل `@beta`، فإن استدعاءات `update <plugin-id>` اللاحقة تعيد استخدام ذلك الوسم المسجل. تمرير مواصفة npm صريحة يبدّل التثبيت المتتبَّع إلى تلك المواصفة للتحديثات المستقبلية.

bashCopy code
[code]
    openclaw plugins update @scope/openclaw-plugin@betaopenclaw plugins update @scope/openclaw-plugin
[/code]

يعيد الأمر الثاني Plugin إلى خط الإصدار الافتراضي في السجل عندما كان مثبتًا سابقًا على إصدار دقيق أو وسم محدد.

عند تشغيل `openclaw update` على قناة beta، تحاول سجلات Plugin الافتراضية من npm وClawHub استخدام إصدار Plugin المطابق `@beta` أولًا. إذا لم يكن إصدار beta هذا موجودًا، يعود OpenClaw إلى المواصفة الافتراضية/الأحدث المسجلة. بالنسبة إلى Plugins من npm، يعود OpenClaw أيضًا عندما تكون حزمة beta موجودة لكنها تفشل في تحقق التثبيت. تُحفظ الإصدارات الدقيقة والوسوم الصريحة مثل `@rc` أو `@beta`.

## إلغاء تثبيت Plugins

bashCopy code
[code]
    openclaw plugins uninstall <plugin-id> --dry-runopenclaw plugins uninstall <plugin-id>openclaw plugins uninstall <plugin-id> --keep-filesopenclaw gateway restart
[/code]

يزيل إلغاء التثبيت إدخال إعدادات Plugin، وسجل فهرس Plugin، وإدخالات قوائم السماح/الحظر، ومسارات التحميل المرتبطة عند الاقتضاء. تُزال أدلة التثبيت المُدارة ما لم تمرر `--keep-files`.

في وضع Nix (`OPENCLAW_NIX_MODE=1`)، تكون أوامر تثبيت Plugin وتحديثه وإلغاء تثبيته وتمكينه وتعطيله معطلة. أدِر هذه الاختيارات في مصدر Nix الخاص بالتثبيت بدلًا من ذلك؛ بالنسبة إلى nix-openclaw، استخدم [البداية السريعة](<https://github.com/openclaw/nix-openclaw#quick-start>) المعتمدة على الوكيل أولًا.

## نشر Plugins

يمكنك نشر Plugins خارجية إلى [ClawHub](<https://clawhub.ai>)، أو [npmjs.com](<http://npmjs.com>)، أو كليهما.

### النشر إلى ClawHub

ClawHub هو سطح الاكتشاف العام الأساسي لـ Plugins في OpenClaw. فهو يمنح المستخدمين بيانات وصفية قابلة للبحث، وسجل الإصدارات، ونتائج فحص السجل قبل التثبيت.

bashCopy code
[code]
    npm i -g clawhubclawhub loginclawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginclawhub package publish your-org/your-plugin@v1.0.0
[/code]

يثبّت المستخدمون من ClawHub باستخدام:

bashCopy code
[code]
    openclaw plugins install clawhub:<package>openclaw plugins install <package>
[/code]

لا يزال الشكل المجرد يفحص ClawHub أولًا.

### النشر إلى [npmjs.com](<http://npmjs.com>)

يجب أن تتضمن Plugins الأصلية من npm بيان Plugin وبيانات وصفية لنقطة دخول OpenClaw في `package.json`.

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-plugin",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./dist/index.js"]  }}
[/code]

bashCopy code
[code]
    npm publish --access public
[/code]

يثبّت المستخدمون Plugins المتاحة عبر npm فقط باستخدام:

bashCopy code
[code]
    openclaw plugins install npm:@acme/openclaw-pluginopenclaw plugins install npm:@acme/openclaw-plugin@betaopenclaw plugins install npm:@acme/openclaw-plugin@1.0.0
[/code]

إذا كانت الحزمة نفسها متاحة أيضًا على ClawHub، فإن `npm:` يتجاوز البحث في ClawHub ويفرض الحل عبر npm.

## اختيار المصدر

  * **ClawHub** : استخدمه عندما تريد اكتشافًا أصليًا لـ OpenClaw، وملخصات فحص، وإصدارات، وتلميحات تثبيت.
  * **[npmjs.com](<http://npmjs.com>)** : استخدمه عندما تكون قد بدأت بالفعل في شحن حزم JavaScript أو تحتاج إلى وسوم توزيع npm أو سير عمل السجلات الخاصة.
  * **Git** : استخدمه عندما تريد التثبيت مباشرة من فرع أو وسم أو commit.
  * **مسار محلي** : استخدمه عندما تطوّر أو تختبر Plugin على الجهاز نفسه.


## ذات صلة

  * [Plugins](</ar/tools/plugin>) \- نظرة عامة واستكشاف الأخطاء وإصلاحها
  * [`openclaw plugins`](</ar/cli/plugins>) \- مرجع CLI الكامل
  * [ClawHub](</ar/clawhub/cli>) \- عمليات النشر والسجل
  * [بناء Plugins](</ar/plugins/building-plugins>) \- إنشاء حزمة Plugin
  * [بيان Plugin](</ar/plugins/manifest>) \- البيان والبيانات الوصفية للحزمة


Was this useful?YesNo