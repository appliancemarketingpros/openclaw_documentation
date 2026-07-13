---
title: LongCat
source_url: https://docs.openclaw.ai/ar/providers/longcat
scraped_at: 2026-07-13
---

ModelsProviders

[LongCat](<https://longcat.ai>) توفّر واجهة API مستضافة لنموذج LongCat-2.0، وهو نموذج استدلال مصمم لأعباء عمل البرمجة والوكلاء. توفّر OpenClaw Plugin الرسمي `longcat` لنقطة نهاية LongCat المتوافقة مع OpenAI.

الخاصية | القيمة  
---|---  
المزوّد | `longcat`  
المصادقة | `LONGCAT_API_KEY`  
API | إكمالات المحادثة المتوافقة مع OpenAI  
عنوان URL الأساسي | `https://api.longcat.chat/openai`  
النموذج | `longcat/LongCat-2.0`  
السياق | 1,048,576 رمزًا  
الحد الأقصى للمخرجات | 131,072 رمزًا  
الإدخال | نص  
  
## تثبيت Plugin

ثبّت الحزمة الرسمية، ثم أعد تشغيل Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/longcat-provideropenclaw gateway restart
[/code]

## بدء الاستخدام

* ### إنشاء مفتاح API

سجّل الدخول إلى [منصة LongCat API](<https://longcat.chat/platform/>) وأنشئ مفتاحًا في صفحة [مفاتيح API](<https://longcat.chat/platform/api_keys>).

* ### تشغيل الإعداد الأولي

bashCopy code
[code]
    openclaw onboard --auth-choice longcat-api-key
[/code]

* ### التحقق من النموذج

bashCopy code
[code]
    openclaw models list --provider longcat
[/code]

يضيف الإعداد الأولي الكتالوج المستضاف ويحدد `longcat/LongCat-2.0` عندما لا يكون هناك نموذج أساسي مُهيأ بالفعل.

### الإعداد غير التفاعلي

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice longcat-api-key \  --longcat-api-key "$LONGCAT_API_KEY"
[/code]

## سلوك الاستدلال

توفّر LongCat تحكمًا ثنائيًا في التفكير. تربط OpenClaw مستويات التفكير المفعّلة بـ `thinking: { type: "enabled" }`، وتربط `/think off` بـ `thinking: { type: "disabled" }`. لا توثّق LongCat حاليًا `reasoning_effort`، ولذلك لا ترسله OpenClaw.

تعيد LongCat الاستدلال في `reasoning_content`. تحتفظ OpenClaw بهذا الحقل عند إعادة تشغيل أدوار استدعاء الأدوات الخاصة بالمساعد، بحيث تحافظ جلسات الوكيل متعددة الأدوار على بنية الرسائل التي يتوقعها المزوّد.

## التسعير

يستخدم الكتالوج المضمّن أسعار LongCat المعلنة بنظام الدفع حسب الاستخدام، بالدولار الأمريكي لكل مليون رمز: 0.75 دولار للإدخال غير المخزّن مؤقتًا، و0.015 دولار للإدخال المخزّن مؤقتًا، و2.95 دولار للمخرجات. قد تقدّم LongCat خصومات مؤقتة؛ وتُعد [صفحة التسعير](<https://longcat.chat/platform/docs/Pricing/LongCat-2.0.html>) وسجلات الفوترة الخاصة بك المرجع المعتمد.

## LongCat-2.0 المستضاف ذاتيًا

يستهدف مزوّد `longcat` واجهة API المستضافة من LongCat. لاستخدام الأوزان المفتوحة على [Hugging Face](<https://huggingface.co/meituan-longcat/LongCat-2.0>)، شغّل النموذج من خلال بيئة تشغيل متوافقة مع OpenAI، واستخدم بدلًا من ذلك مزوّد [vLLM](</ar/providers/vllm>) أو [SGLang](</ar/providers/sglang>) الموجود في OpenClaw.

احتفظ بمعرّف النموذج الدقيق لبيئة التشغيل في كتالوج المزوّد المستضاف ذاتيًا؛ ولا توجّه نشرًا محليًا عبر `longcat/LongCat-2.0`.

## استكشاف الأخطاء وإصلاحها

يعمل المفتاح في الصدفة، ولكن ليس في Gateway

لا ترث عمليات Gateway التي تديرها الخدمات الخفية جميع متغيرات الصدفة التفاعلية. ضع `LONGCAT_API_KEY` في `~/.openclaw/.env`، أو هيّئه من خلال الإعداد الأولي، أو استخدم مرجع أسرار معتمدًا.

تفشل الطلبات بالرمز 402 أو 429

يعني `402` أن الحساب لا يملك حصة رموز كافية. ويعني `429` أن مفتاح API بلغ حد المعدل. تحقّق من [استخدام LongCat](<https://longcat.chat/platform/usage>) وأعد محاولة الطلبات المحدودة بالمعدل بعد انتهاء فترة التراجع الخاصة بالمزوّد.

لا يظهر النموذج

شغّل `openclaw plugins list` وتأكد من أن Plugin ‏`longcat` مفعّل، ثم شغّل `openclaw models list --provider longcat`.

## ذو صلة

[**مزوّدو النماذج** تهيئة المزوّد، ومراجع النماذج، وسلوك تجاوز الفشل. ](</ar/concepts/model-providers>) [**وثائق LongCat API** نقاط نهاية API المستضافة، والمصادقة، والحدود، والأمثلة. ](<https://longcat.chat/platform/docs/>) [**بطاقة نموذج LongCat-2.0** البنية، وإرشادات النشر، وتفاصيل النموذج. ](<https://huggingface.co/meituan-longcat/LongCat-2.0>) [**الأسرار** خزّن بيانات اعتماد المزوّد دون تضمين نص صريح في الإعدادات. ](</ar/gateway/secrets>)

Was this useful?YesNo

Open issue