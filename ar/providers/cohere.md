---
title: Cohere
source_url: https://docs.openclaw.ai/ar/providers/cohere
scraped_at: 2026-06-29
---

ModelsProviders

يوفر [Cohere](<https://cohere.com>) الاستدلال المتوافق مع OpenAI عبر Compatibility API. يشحن OpenClaw مزود Cohere أثناء انتقاله إلى الإخراج الخارجي، وينشره أيضًا كـ Plugin خارجي رسمي مع كتالوج نماذج Command A.

الخاصية | القيمة  
---|---  
معرف المزود | `cohere`  
Plugin | مضمّن أثناء الانتقال؛ حزمة خارجية رسمية  
متغير بيئة المصادقة | `COHERE_API_KEY`  
علم الإعداد الأولي | `--auth-choice cohere-api-key`  
علم CLI المباشر | `--cohere-api-key <key>`  
API | متوافق مع OpenAI (`openai-completions`)  
عنوان URL الأساسي | `https://api.cohere.ai/compatibility/v1`  
النموذج الافتراضي | `cohere/command-a-03-2025`  
  
## ابدأ

  1. Cohere مضمن في حزم OpenClaw الحالية. إذا لم يكن متاحًا، فثبّت الحزمة الخارجية وأعد تشغيل Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/cohere-provideropenclaw gateway restart
[/code]

  2. أنشئ مفتاح Cohere API.
  3. شغّل الإعداد الأولي:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice cohere-api-key \  --cohere-api-key "$COHERE_API_KEY"
[/code]

  4. تأكد من توفر الكتالوج:

bashCopy code
[code]
    openclaw models list --provider cohere
[/code]

يتم تعيين النموذج الافتراضي فقط عندما لا يكون هناك نموذج أساسي مكوّن بالفعل.

## الإعداد باستخدام البيئة فقط

اجعل `COHERE_API_KEY` متاحًا لعملية Gateway، ثم اختر نموذج Cohere:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cohere/command-a-03-2025" },    },  },}
[/code]

## ذات صلة

  * [مزودو النماذج](</ar/concepts/model-providers>)
  * [Models CLI](</ar/cli/models>)
  * [دليل المزودين](</ar/providers>)


Was this useful?YesNo

Open issue