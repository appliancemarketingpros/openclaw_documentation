---
title: Arcee AI
source_url: https://docs.openclaw.ai/ar/providers/arcee
scraped_at: 2026-05-25
---

توفّر [Arcee AI](<https://arcee.ai>) إمكانية الوصول إلى عائلة Trinity من نماذج خليط الخبراء عبر API متوافقة مع OpenAI. جميع نماذج Trinity مرخّصة بموجب Apache 2.0.

يمكن الوصول إلى نماذج Arcee AI مباشرة عبر منصة Arcee أو من خلال [OpenRouter](</ar/providers/openrouter>).

الخاصية | القيمة  
---|---  
المزوّد | `arcee`  
المصادقة | `ARCEEAI_API_KEY` (مباشر) أو `OPENROUTER_API_KEY` (عبر OpenRouter)  
API | متوافقة مع OpenAI  
عنوان URL الأساسي | `https://api.arcee.ai/api/v1` (مباشر) أو `https://openrouter.ai/api/v1` (OpenRouter)  
  
## بدء الاستخدام

### مباشر (منصة Arcee)

* ### احصل على مفتاح API

أنشئ مفتاح API في [Arcee AI](<https://chat.arcee.ai/>).

* ### شغّل الإعداد الأولي

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-api-key
[/code]

* ### عيّن نموذجًا افتراضيًا

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

### عبر OpenRouter

* ### احصل على مفتاح API

أنشئ مفتاح API في [OpenRouter](<https://openrouter.ai/keys>).

* ### شغّل الإعداد الأولي

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-openrouter
[/code]

* ### عيّن نموذجًا افتراضيًا

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

تعمل مراجع النموذج نفسها لكل من إعدادات الاتصال المباشر وOpenRouter (على سبيل المثال `arcee/trinity-large-thinking`).

## إعداد غير تفاعلي

### مباشر (منصة Arcee)

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-api-key \  --arceeai-api-key "$ARCEEAI_API_KEY"
[/code]

### عبر OpenRouter

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-openrouter \  --openrouter-api-key "$OPENROUTER_API_KEY"
[/code]

## الكتالوج المضمّن

يشحن OpenClaw حاليًا كتالوج Arcee المضمّن هذا:

مرجع النموذج | الاسم | الإدخال | السياق | التكلفة (إدخال/إخراج لكل 1M) | ملاحظات  
---|---|---|---|---|---  
`arcee/trinity-large-thinking` | Trinity Large Thinking | نص | 256K | $0.25 / $0.90 | النموذج الافتراضي؛ التفكير مفعّل  
`arcee/trinity-large-preview` | Trinity Large Preview | نص | 128K | $0.25 / $1.00 | متعدد الأغراض؛ 400B معلمة، و13B نشطة  
`arcee/trinity-mini` | Trinity Mini 26B | نص | 128K | $0.045 / $0.15 | سريع وفعّال من حيث التكلفة؛ استدعاء الدوال  
  
## الميزات المدعومة

الميزة | مدعومة  
---|---  
البث | نعم  
استخدام الأدوات / استدعاء الدوال | نعم (Trinity Mini، Trinity Large Preview)  
الإخراج المنظّم (وضع JSON ومخطط JSON) | نعم  
التفكير الممتد | نعم (Trinity Large Thinking؛ الأدوات معطّلة)  
  
ملاحظة البيئة

إذا كان Gateway يعمل كخدمة خفية (launchd/systemd)، فتأكد من أن `ARCEEAI_API_KEY` (أو `OPENROUTER_API_KEY`) متاح لتلك العملية (على سبيل المثال، في `~/.openclaw/.env` أو عبر `env.shellEnv`).

توجيه OpenRouter

عند استخدام نماذج Arcee عبر OpenRouter، تنطبق مراجع النموذج نفسها `arcee/*`. يتولى OpenClaw التوجيه بشفافية بناءً على اختيار المصادقة لديك. راجع [مستندات مزوّد OpenRouter](</ar/providers/openrouter>) للحصول على تفاصيل التكوين الخاصة بـ OpenRouter.

## ذو صلة

[**OpenRouter** يمكنك الوصول إلى نماذج Arcee والعديد غيرها عبر مفتاح API واحد. ](</ar/providers/openrouter>) [**اختيار النموذج** اختيار المزوّدين ومراجع النماذج وسلوك تجاوز الفشل. ](</ar/concepts/model-providers>)

Was this useful?YesNo