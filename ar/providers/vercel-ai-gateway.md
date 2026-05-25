---
title: Gateway الذكاء الاصطناعي من Vercel
source_url: https://docs.openclaw.ai/ar/providers/vercel-ai-gateway
scraped_at: 2026-05-25
---

يوفّر [Vercel AI Gateway](<https://vercel.com/ai-gateway>) واجهة API موحّدة للوصول إلى مئات النماذج عبر نقطة نهاية واحدة.

الخاصية | القيمة  
---|---  
المزوّد | `vercel-ai-gateway`  
المصادقة | `AI_GATEWAY_API_KEY`  
API | متوافق مع Anthropic Messages  
كتالوج النماذج | يُكتشف تلقائيًا عبر `/v1/models`  
  
## بدء الاستخدام

* ### Set the API key

شغّل الإعداد الأولي واختر خيار مصادقة AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice ai-gateway-api-key
[/code]

* ### Set a default model

أضف النموذج إلى إعدادات OpenClaw لديك:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.6" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider vercel-ai-gateway
[/code]

## مثال غير تفاعلي

لإعدادات السكربتات أو CI، مرّر كل القيم في سطر الأوامر:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
[/code]

## الاختصار المختصر لمعرّف النموذج

يقبل OpenClaw مراجع نماذج Vercel Claude المختصرة ويطبعها بالشكل الطبيعي أثناء التشغيل:

الإدخال المختصر | مرجع النموذج بعد التطبيع  
---|---  
`vercel-ai-gateway/claude-opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
`vercel-ai-gateway/opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4-6`  
  
## الإعدادات المتقدمة

Environment variable for daemon processes

إذا كان OpenClaw Gateway يعمل كخدمة خلفية (launchd/systemd)، فتأكد من إتاحة `AI_GATEWAY_API_KEY` لهذه العملية.

Provider routing

يوجّه Vercel AI Gateway الطلبات إلى المزوّد العلوي بناءً على بادئة مرجع النموذج. على سبيل المثال، يوجّه `vercel-ai-gateway/anthropic/claude-opus-4.6` عبر Anthropic، بينما يوجّه `vercel-ai-gateway/openai/gpt-5.5` عبر OpenAI ويوجّه `vercel-ai-gateway/moonshotai/kimi-k2.6` عبر MoonshotAI. يتولى `AI_GATEWAY_API_KEY` الوحيد لديك المصادقة لكل المزوّدين العلويين.

Thinking levels

تتبع خيارات `/think` بادئات النماذج العلوية الموثوقة عندما يعرف OpenClaw عقد المزوّد العلوي. يستخدم `vercel-ai-gateway/anthropic/...` ملف تعريف التفكير الخاص بـ Claude، بما في ذلك القيم الافتراضية التكيفية لنماذج Claude 4.6. تعرض مراجع `vercel-ai-gateway/openai/gpt-5.4` و`gpt-5.5` ومراجع نمط Codex خيار `/think xhigh` تمامًا مثل مزوّدي OpenAI/OpenAI Codex المباشرين. تحتفظ المراجع الأخرى ذات مساحات الأسماء بمستويات الاستدلال العادية ما لم تعلن بيانات كتالوجها الوصفية عن المزيد.

## ذو صلة

[**Model selection** اختيار المزوّدين، ومراجع النماذج، وسلوك تجاوز الفشل. ](</ar/concepts/model-providers>) [**Troubleshooting** استكشاف الأخطاء العامة وإصلاحها والأسئلة الشائعة. ](</ar/help/troubleshooting>)

Was this useful?YesNo