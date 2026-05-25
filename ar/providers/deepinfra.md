---
title: DeepInfra
source_url: https://docs.openclaw.ai/ar/providers/deepinfra
scraped_at: 2026-05-25
---

توفر DeepInfra **API موحّدة** توجّه الطلبات إلى أشهر النماذج مفتوحة المصدر والنماذج الرائدة عبر نقطة نهاية واحدة ومفتاح API واحد. وهي متوافقة مع OpenAI، لذا تعمل معظم حزم OpenAI SDK بمجرد تغيير عنوان URL الأساسي.

## الحصول على مفتاح API

  1. انتقل إلى <https://deepinfra.com/>
  2. سجّل الدخول أو أنشئ حسابًا
  3. انتقل إلى Dashboard / Keys وأنشئ مفتاح API جديدًا أو استخدم المفتاح المُنشأ تلقائيًا


## إعداد CLI

bashCopy code
[code]
    openclaw onboard --deepinfra-api-key <key>
[/code]

أو اضبط متغير البيئة:

bashCopy code
[code]
    export DEEPINFRA_API_KEY="<your-deepinfra-api-key>" # pragma: allowlist secret
[/code]

## مقتطف الإعداد

json5Copy code
[code]
    {  env: { DEEPINFRA_API_KEY: "<your-deepinfra-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "deepinfra/deepseek-ai/DeepSeek-V3.2" },    },  },}
[/code]

## أسطح OpenClaw المدعومة

يسجّل Plugin المضمّن جميع أسطح DeepInfra التي تطابق عقود مزوّد OpenClaw الحالية:

السطح | النموذج الافتراضي | إعداد/أداة OpenClaw  
---|---|---  
مزوّد المحادثة / النموذج | `deepseek-ai/DeepSeek-V3.2` | `agents.defaults.model`  
توليد/تحرير الصور | `black-forest-labs/FLUX-1-schnell` | `image_generate`, `agents.defaults.imageGenerationModel`  
فهم الوسائط | `moonshotai/Kimi-K2.5` للصور | فهم الصور الواردة  
تحويل الكلام إلى نص | `openai/whisper-large-v3-turbo` | نسخ الصوت الوارد  
تحويل النص إلى كلام | `hexgrad/Kokoro-82M` | `messages.tts.provider: "deepinfra"`  
توليد الفيديو | `Pixverse/Pixverse-T2V` | `video_generate`, `agents.defaults.videoGenerationModel`  
تضمينات الذاكرة | `BAAI/bge-m3` | `agents.defaults.memorySearch.provider: "deepinfra"`  
  
تعرض DeepInfra أيضًا إعادة الترتيب، والتصنيف، واكتشاف الأجسام، وأنواع نماذج أصلية أخرى. لا يملك OpenClaw حاليًا عقود مزوّد من الدرجة الأولى لهذه الفئات، لذلك لا يسجّلها هذا Plugin بعد.

## النماذج المتاحة

يكتشف OpenClaw نماذج DeepInfra المتاحة ديناميكيًا عند بدء التشغيل. استخدم `/models deepinfra` للاطلاع على القائمة الكاملة للنماذج المتاحة.

يمكن استخدام أي نموذج متاح على [DeepInfra.com](<https://deepinfra.com/>) مع البادئة `deepinfra/`:

CodeCopy code
[code]
    deepinfra/MiniMaxAI/MiniMax-M2.5deepinfra/deepseek-ai/DeepSeek-V3.2deepinfra/moonshotai/Kimi-K2.5deepinfra/zai-org/GLM-5.1...وغير ذلك الكثير
[/code]

## ملاحظات

  * مراجع النماذج هي `deepinfra/<provider>/<model>` (مثل `deepinfra/Qwen/Qwen3-Max`).
  * النموذج الافتراضي: `deepinfra/deepseek-ai/DeepSeek-V3.2`
  * عنوان URL الأساسي: `https://api.deepinfra.com/v1/openai`
  * يستخدم توليد الفيديو الأصلي `https://api.deepinfra.com/v1/inference/<model>`.


## ذو صلة

  * [مزوّدو النماذج](</ar/concepts/model-providers>)
  * [جميع المزوّدين](</ar/providers>)


Was this useful?YesNo