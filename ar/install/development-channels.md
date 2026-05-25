---
title: قنوات الإصدار
source_url: https://docs.openclaw.ai/ar/install/development-channels
scraped_at: 2026-05-25
---

يشحن OpenClaw ثلاث قنوات تحديث:

  * **stable** : npm dist-tag `latest`. موصى بها لمعظم المستخدمين.
  * **beta** : npm dist-tag `beta` عندما تكون حديثة؛ إذا كانت beta مفقودة أو أقدم من أحدث إصدار stable، يعود مسار التحديث إلى `latest`.
  * **dev** : الرأس المتحرك لـ `main` (git). npm dist-tag: `dev` (عند نشره). فرع `main` مخصص للتجريب والتطوير النشط. قد يحتوي على ميزات غير مكتملة أو تغييرات كاسرة. لا تستخدمه لـ gateways الإنتاجية.


عادة نشحن بنى stable إلى **beta** أولاً، ونختبرها هناك، ثم نشغّل خطوة ترقية صريحة تنقل البنية التي تم التحقق منها إلى `latest` دون تغيير رقم الإصدار. يمكن للمشرفين أيضاً نشر إصدار stable مباشرة إلى `latest` عند الحاجة. dist-tags هي مصدر الحقيقة لتثبيتات npm.

## تبديل القنوات

bashCopy code
[code]
    openclaw update --channel stableopenclaw update --channel betaopenclaw update --channel dev
[/code]

يُبقي `--channel` اختيارك في config (`update.channel`) ويوائم طريقة التثبيت:

  * **`stable`** (تثبيتات الحزمة): يتم التحديث عبر npm dist-tag `latest`.
  * **`beta`** (تثبيتات الحزمة): يفضل npm dist-tag `beta`، لكنه يعود إلى `latest` عندما تكون `beta` مفقودة أو أقدم من وسم stable الحالي.
  * **`stable`** (تثبيتات git): يسحب أحدث وسم git لإصدار stable.
  * **`beta`** (تثبيتات git): يفضل أحدث وسم git لإصدار beta، لكنه يعود إلى أحدث وسم git لإصدار stable عندما تكون beta مفقودة أو أقدم.
  * **`dev`** : يضمن وجود checkout من git (الافتراضي `~/openclaw`، ويمكن تجاوزه بـ `OPENCLAW_GIT_DIR`)، وينتقل إلى `main`، ويعيد الأساس على upstream، ويبني، و يثبّت CLI العام من ذلك checkout.


## استهداف إصدار أو وسم لمرة واحدة

استخدم `--tag` لاستهداف dist-tag محدد، أو إصدار، أو مواصفة حزمة لتحديث واحد **دون** تغيير القناة المحفوظة لديك:

bashCopy code
[code]
    # Install a specific versionopenclaw update --tag 2026.4.1-beta.1 # Install from the beta dist-tag (one-off, does not persist)openclaw update --tag beta # Install from GitHub main branch (npm tarball)openclaw update --tag main # Install a specific npm package specopenclaw update --tag openclaw@2026.4.1-beta.1
[/code]

ملاحظات:

  * ينطبق `--tag` على **تثبيتات الحزم (npm) فقط**. تتجاهله تثبيتات git.
  * لا يتم حفظ الوسم. يستخدم `openclaw update` التالي لديك القناة المضبوطة كالمعتاد.
  * حماية الرجوع إلى إصدار أقدم: إذا كان الإصدار المستهدف أقدم من إصدارك الحالي، يطلب OpenClaw تأكيداً (يمكن التخطي باستخدام `--yes`).
  * يختلف `--channel beta` عن `--tag beta`: يمكن لمسار القناة أن يعود إلى stable/latest عندما تكون beta مفقودة أو أقدم، بينما يستهدف `--tag beta` dist-tag الخام `beta` لتلك التشغيلية الواحدة.


## التشغيل التجريبي

عاين ما سيفعله `openclaw update` دون إجراء تغييرات:

bashCopy code
[code]
    openclaw update --dry-runopenclaw update --channel beta --dry-runopenclaw update --tag 2026.4.1-beta.1 --dry-runopenclaw update --dry-run --json
[/code]

يعرض التشغيل التجريبي القناة الفعلية، والإصدار المستهدف، والإجراءات المخطط لها، وما إذا كان تأكيد الرجوع إلى إصدار أقدم سيكون مطلوباً.

## Plugins والقنوات

عندما تبدل القنوات باستخدام `openclaw update`، يزامن OpenClaw أيضاً مصادر Plugins:

  * يفضل `dev` استخدام Plugins المضمنة من checkout الخاص بـ git.
  * يعيد `stable` و`beta` حزم Plugins المثبتة عبر npm.
  * يتم تحديث Plugins المثبتة عبر npm بعد اكتمال تحديث النواة.


## التحقق من الحالة الحالية

bashCopy code
[code]
    openclaw update status
[/code]

يعرض القناة النشطة، ونوع التثبيت (git أو حزمة)، والإصدار الحالي، و المصدر (config، أو وسم git، أو فرع git، أو الافتراضي).

## أفضل ممارسات الوسم

  * أضف وسوماً للإصدارات التي تريد أن تصل إليها checkouts الخاصة بـ git (`vYYYY.M.D` لـ stable، و`vYYYY.M.D-beta.N` لـ beta).
  * يتم التعرف أيضاً على `vYYYY.M.D.beta.N` للتوافق، لكن يُفضّل `-beta.N`.
  * لا تزال وسوم `vYYYY.M.D-<patch>` القديمة تُعرَف كإصدارات stable (غير beta).
  * أبقِ الوسوم غير قابلة للتغيير: لا تنقل الوسم ولا تعِد استخدامه أبداً.
  * تظل npm dist-tags مصدر الحقيقة لتثبيتات npm: 
    * `latest` -> stable
    * `beta` -> بنية مرشحة أو بنية stable تمر عبر beta أولاً
    * `dev` -> لقطة main (اختيارية)


## توفر تطبيق macOS

قد **لا** تتضمن بنى beta وdev إصدار تطبيق macOS. هذا مقبول:

  * لا يزال من الممكن نشر وسم git وnpm dist-tag.
  * اذكر "لا توجد بنية macOS لهذا beta" في ملاحظات الإصدار أو changelog.


## ذو صلة

  * [التحديث](</ar/install/updating>)
  * [الأجزاء الداخلية للمثبّت](</ar/install/installer>)


Was this useful?YesNo