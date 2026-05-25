---
title: Kilo Gateway
source_url: https://docs.openclaw.ai/ar/providers/kilocode
scraped_at: 2026-05-25
---

يوفّر Kilo Gateway **واجهة API موحّدة** تُوجّه الطلبات إلى العديد من النماذج خلف نقطة نهاية واحدة ومفتاح API واحد. وهو متوافق مع OpenAI، لذلك تعمل معظم حِزم SDK الخاصة بـ OpenAI بمجرد تبديل عنوان URL الأساسي.

الخاصية | القيمة  
---|---  
المزوّد | `kilocode`  
المصادقة | `KILOCODE_API_KEY`  
واجهة API | متوافقة مع OpenAI  
عنوان URL الأساسي | `https://api.kilo.ai/api/gateway/`  
  
## البدء

* ### أنشئ حسابًا

انتقل إلى [app.kilo.ai](<https://app.kilo.ai>)، وسجّل الدخول أو أنشئ حسابًا، ثم انتقل إلى مفاتيح API وأنشئ مفتاحًا جديدًا.

* ### شغّل الإعداد الأولي

bashCopy code
[code]
    openclaw onboard --auth-choice kilocode-api-key
[/code]

أو عيّن متغير البيئة مباشرةً:

bashCopy code
[code]
    export KILOCODE_API_KEY="<your-kilocode-api-key>" # pragma: allowlist secret
[/code]

* ### تحقّق من أن النموذج متاح

bashCopy code
[code]
    openclaw models list --provider kilocode
[/code]

## النموذج الافتراضي

النموذج الافتراضي هو `kilocode/kilo/auto`، وهو نموذج توجيه ذكي مملوك للمزوّد وتتم إدارته بواسطة Kilo Gateway.

## الفهرس المضمّن

يكتشف OpenClaw النماذج المتاحة ديناميكيًا من Kilo Gateway عند بدء التشغيل. استخدم `/models kilocode` للاطلاع على القائمة الكاملة للنماذج المتاحة في حسابك.

يمكن استخدام أي نموذج متاح على Gateway مع البادئة `kilocode/`:

مرجع النموذج | الملاحظات  
---|---  
`kilocode/kilo/auto` | الافتراضي — توجيه ذكي  
`kilocode/anthropic/claude-sonnet-4` | Anthropic عبر Kilo  
`kilocode/openai/gpt-5.5` | OpenAI عبر Kilo  
`kilocode/google/gemini-3.1-pro-preview` | Google عبر Kilo  
...وغيرها الكثير | استخدم `/models kilocode` لسردها جميعًا  
  
## مثال على الإعدادات

json5Copy code
[code]
    {  env: { KILOCODE_API_KEY: "<your-kilocode-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "kilocode/kilo/auto" },    },  },}
[/code]

النقل والتوافق

Kilo Gateway موثّق في المصدر على أنه متوافق مع OpenRouter، لذلك يبقى على مسار الوكيل المتوافق مع OpenAI بدلًا من تشكيل طلبات OpenAI الأصلية.

  * تبقى مراجع Kilo المدعومة بـ Gemini على مسار وكيل Gemini، لذلك يحتفظ OpenClaw بتنقية توقيعات التفكير الخاصة بـ Gemini هناك من دون تمكين تحقق إعادة التشغيل الأصلي لـ Gemini أو إعادة كتابة التهيئة.
  * يستخدم Kilo Gateway رمز Bearer مع مفتاح API الخاص بك داخليًا.

مغلّف البث والاستدلال

يضيف مغلّف البث المشترك في Kilo ترويسة تطبيق المزوّد ويوحّد حمولات استدلال الوكيل لمراجع النماذج الفعلية المدعومة.

استكشاف الأخطاء وإصلاحها

  * إذا فشل اكتشاف النماذج عند بدء التشغيل، يرجع OpenClaw إلى الفهرس الثابت المضمّن الذي يحتوي على `kilocode/kilo/auto`.
  * تأكّد من أن مفتاح API الخاص بك صالح وأن حساب Kilo الخاص بك لديه النماذج المطلوبة مفعّلة.
  * عندما يعمل Gateway كخدمة خفية، تأكّد من أن `KILOCODE_API_KEY` متاح لتلك العملية (على سبيل المثال في `~/.openclaw/.env` أو عبر `env.shellEnv`).


## ذو صلة

[**اختيار النموذج** اختيار المزوّدين ومراجع النماذج وسلوك تجاوز الفشل. ](</ar/concepts/model-providers>) [**مرجع الإعدادات** مرجع إعدادات OpenClaw الكامل. ](</ar/gateway/configuration-reference>) [**Kilo Gateway** لوحة تحكم Kilo Gateway ومفاتيح API وإدارة الحساب. ](<https://app.kilo.ai>)

Was this useful?YesNo