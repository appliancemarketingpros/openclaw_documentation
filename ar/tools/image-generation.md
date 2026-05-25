---
title: إنشاء الصور
source_url: https://docs.openclaw.ai/ar/tools/image-generation
scraped_at: 2026-05-25
---

تتيح أداة `image_generate` للوكيل إنشاء الصور وتحريرها باستخدام الموفرين الذين قمت بتكوينهم. تُسلَّم الصور المُنشأة تلقائيًا كمرفقات وسائط في رد الوكيل.

## البدء السريع

* ### تكوين المصادقة

عيّن مفتاح API لموفر واحد على الأقل (على سبيل المثال `OPENAI_API_KEY`، `GEMINI_API_KEY`، `OPENROUTER_API_KEY`) أو سجّل الدخول باستخدام OpenAI Codex OAuth.

* ### اختيار نموذج افتراضي (اختياري)

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openai/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

يستخدم Codex OAuth مرجع النموذج نفسه `openai/gpt-image-2`. عند تكوين ملف تعريف OAuth باسم `openai-codex`، يوجّه OpenClaw طلبات الصور عبر ملف تعريف OAuth هذا بدلًا من تجربة `OPENAI_API_KEY` أولًا. يؤدي تكوين `models.providers.openai` الصريح (مفتاح API، أو عنوان URL أساسي مخصص/Azure) إلى الرجوع إلى مسار OpenAI Images API المباشر.

* ### اسأل الوكيل

_"أنشئ صورة لتميمة روبوت ودودة."_

يستدعي الوكيل `image_generate` تلقائيًا. لا حاجة إلى قائمة سماح للأدوات - فهي مفعّلة افتراضيًا عند توفر موفر.

## المسارات الشائعة

الهدف | مرجع النموذج | المصادقة  
---|---|---  
توليد صور OpenAI مع فوترة API | `openai/gpt-image-2` | `OPENAI_API_KEY`  
توليد صور OpenAI باستخدام مصادقة اشتراك Codex | `openai/gpt-image-2` | OpenAI Codex OAuth  
OpenAI لخلفيات شفافة PNG/WebP | `openai/gpt-image-1.5` | `OPENAI_API_KEY` أو OpenAI Codex OAuth  
توليد صور DeepInfra | `deepinfra/black-forest-labs/FLUX-1-schnell` | `DEEPINFRA_API_KEY`  
توليد صور OpenRouter | `openrouter/google/gemini-3.1-flash-image-preview` | `OPENROUTER_API_KEY`  
توليد صور LiteLLM | `litellm/gpt-image-2` | `LITELLM_API_KEY`  
توليد صور Google Gemini | `google/gemini-3.1-flash-image-preview` | `GEMINI_API_KEY` أو `GOOGLE_API_KEY`  
  
تتعامل أداة `image_generate` نفسها مع التحويل من نص إلى صورة وتحرير الصور المرجعية. استخدم `image` لمرجع واحد أو `images` لعدة مراجع. تُمرَّر تلميحات الإخراج التي يدعمها الموفر مثل `quality` و`outputFormat` و `background` عند توفرها، ويُبلَّغ عنها على أنها مُتجاهلة عندما لا يدعمها الموفر. دعم الخلفية الشفافة المضمّن خاص بـ OpenAI؛ وقد يظل موفرون آخرون يحافظون على قناة ألفا في PNG إذا كان نظامهم الخلفي يُصدرها.

## الموفرون المدعومون

الموفر | النموذج الافتراضي | دعم التحرير | المصادقة  
---|---|---|---  
ComfyUI | `workflow` | نعم (صورة واحدة، مكوّنة عبر سير العمل) | `COMFY_API_KEY` أو `COMFY_CLOUD_API_KEY` للسحابة  
DeepInfra | `black-forest-labs/FLUX-1-schnell` | نعم (صورة واحدة) | `DEEPINFRA_API_KEY`  
fal | `fal-ai/flux/dev` | نعم (حدود خاصة بالنموذج) | `FAL_KEY`  
Google | `gemini-3.1-flash-image-preview` | نعم | `GEMINI_API_KEY` أو `GOOGLE_API_KEY`  
LiteLLM | `gpt-image-2` | نعم (حتى 5 صور إدخال) | `LITELLM_API_KEY`  
MiniMax | `image-01` | نعم (مرجع للموضوع) | `MINIMAX_API_KEY` أو MiniMax OAuth (`minimax-portal`)  
OpenAI | `gpt-image-2` | نعم (حتى 4 صور) | `OPENAI_API_KEY` أو OpenAI Codex OAuth  
OpenRouter | `google/gemini-3.1-flash-image-preview` | نعم (حتى 5 صور إدخال) | `OPENROUTER_API_KEY`  
Vydra | `grok-imagine` | لا | `VYDRA_API_KEY`  
xAI | `grok-imagine-image` | نعم (حتى 5 صور) | `XAI_API_KEY`  
  
استخدم `action: "list"` لفحص الموفرين والنماذج المتاحة في وقت التشغيل:

textCopy code
[code]
    /tool image_generate action=list
[/code]

## قدرات الموفرين

القدرة | ComfyUI | DeepInfra | fal | Google | MiniMax | OpenAI | Vydra | xAI  
---|---|---|---|---|---|---|---|---  
التوليد (العدد الأقصى) | محدد بسير العمل | 4 | 4 | 4 | 9 | 4 | 1 | 4  
التحرير / المرجع | صورة واحدة (سير العمل) | صورة واحدة | Flux: 1؛ GPT: 10؛ NB2: 14 | حتى 5 صور | صورة واحدة (مرجع الموضوع) | حتى 5 صور | - | حتى 5 صور  
التحكم في الحجم | - | ✓ | ✓ | ✓ | - | حتى 4K | - | -  
نسبة الأبعاد | - | - | ✓ | ✓ | ✓ | - | - | ✓  
الدقة (1K/2K/4K) | - | - | ✓ | ✓ | - | - | - | 1K, 2K  
  
## معاملات الأداة

مطالبة توليد الصورة. مطلوبة لـ `action: "generate"`.

استخدم `"list"` لفحص الموفرين والنماذج المتاحة في وقت التشغيل.

تجاوز الموفر/النموذج (مثل `openai/gpt-image-2`). استخدم `openai/gpt-image-1.5` لخلفيات OpenAI الشفافة.

مسار صورة مرجعية واحدة أو عنوان URL لوضع التحرير.

عدة صور مرجعية لوضع التحرير (حتى 5 لدى الموفرين الداعمين).

تلميح الحجم: `1024x1024`، `1536x1024`، `1024x1536`، `2048x2048`، `3840x2160`.

نسبة الأبعاد: `1:1`، `2:3`، `3:2`، `3:4`، `4:3`، `4:5`، `5:4`، `9:16`، `16:9`، `21:9`.

تلميح الجودة عندما يدعمه الموفر.

تلميح تنسيق الإخراج عندما يدعمه الموفر.

تلميح الخلفية عندما يدعمه الموفر. استخدم `transparent` مع `outputFormat: "png"` أو `"webp"` للموفرين القادرين على الشفافية.

مهلة اختيارية لطلب الموفر بالمللي ثانية. عندما يستدعي Codex `image_generate` عبر الأدوات الديناميكية، تظل هذه القيمة لكل استدعاء تتجاوز القيمة الافتراضية المكوّنة وتُحدَّد بسقف 600000 ms.

تلميحات خاصة بـ OpenAI فقط: `background` و`moderation` و`outputCompression` و`user`.

## التكوين

### اختيار النموذج

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openai/gpt-image-2",        timeoutMs: 180_000,        fallbacks: [          "openrouter/google/gemini-3.1-flash-image-preview",          "google/gemini-3.1-flash-image-preview",          "fal/fal-ai/flux/dev",        ],      },    },  },}
[/code]

### ترتيب اختيار الموفر

يحاول OpenClaw استخدام الموفرين بهذا الترتيب:

  1. معامل **`model`** من استدعاء الأداة (إذا حدده الوكيل).
  2. **`imageGenerationModel.primary`** من التكوين.
  3. **`imageGenerationModel.fallbacks`** بالترتيب.
  4. **الاكتشاف التلقائي** \- افتراضيات الموفرين المدعومة بالمصادقة فقط: 
     * الموفر الافتراضي الحالي أولًا؛
     * بقية موفري توليد الصور المسجلين بترتيب معرف الموفر.


إذا فشل أحد الموفرين (خطأ مصادقة، حد معدل، إلخ)، تُجرَّب المرشحات المكوّنة التالية تلقائيًا. إذا فشلت جميعها، يتضمن الخطأ تفاصيل من كل محاولة.

تجاوزات النموذج لكل استدعاء دقيقة

يحاول تجاوز `model` لكل استدعاء ذلك الموفر/النموذج فقط ولا يواصل إلى الموفرين الأساسي/الاحتياطي المكوّنين أو الموفرين المكتشفين تلقائيًا.

الاكتشاف التلقائي واعٍ بالمصادقة

لا يدخل افتراضي الموفر إلى قائمة المرشحين إلا عندما يستطيع OpenClaw مصادقة ذلك الموفر فعليًا. عيّن `agents.defaults.mediaGenerationAutoProviderFallback: false` لاستخدام إدخالات `model` و`primary` و`fallbacks` الصريحة فقط.

المهل

عيّن `agents.defaults.imageGenerationModel.timeoutMs` لأنظمة الصور الخلفية البطيئة. يتجاوز معامل الأداة `timeoutMs` لكل استدعاء القيمة الافتراضية المكوّنة. تحترم استدعاءات الأدوات الديناميكية في Codex ميزانية المهلة نفسها، ضمن حد جسر الأدوات الديناميكية الأقصى في OpenClaw وهو 600000 ms.

الفحص في وقت التشغيل

استخدم `action: "list"` لفحص الموفرين المسجلين حاليًا، ونماذجهم الافتراضية، وتلميحات متغيرات بيئة المصادقة.

### تحرير الصور

يدعم OpenAI وOpenRouter وGoogle وDeepInfra وfal وMiniMax وComfyUI وxAI تحرير الصور المرجعية. مرّر مسار صورة مرجعية أو عنوان URL:

textCopy code
[code]
    "Generate a watercolor version of this photo" + image: "/path/to/photo.jpg"
[/code]

OpenAI وOpenRouter وGoogle وxAI تدعم ما يصل إلى 5 صور مرجعية عبر معامل `images`. يدعم fal صورة مرجعية واحدة لـ Flux image-to-image، وما يصل إلى 10 لتعديلات GPT Image 2، وما يصل إلى 14 لتعديلات Nano Banana 2. يدعم MiniMax وComfyUI صورة واحدة.

## تعمّقات في المزوّدين

OpenAI gpt-image-2 (وgpt-image-1.5)

يستخدم توليد الصور في OpenAI افتراضيًا `openai/gpt-image-2`. إذا كان ملف تعريف OAuth لـ `openai-codex` مهيأ، يعيد OpenClaw استخدام ملف تعريف OAuth نفسه المستخدم بواسطة نماذج دردشة اشتراك Codex ويرسل طلب الصورة عبر واجهة Codex Responses الخلفية. تُحوّل عناوين URL الأساسية القديمة لـ Codex مثل `https://chatgpt.com/backend-api` إلى الصيغة القياسية `https://chatgpt.com/backend-api/codex` لطلبات الصور. لا يعود OpenClaw **بصمت** إلى `OPENAI_API_KEY` لذلك الطلب - لفرض التوجيه المباشر عبر OpenAI Images API، هيّئ `models.providers.openai` صراحةً باستخدام مفتاح API أو عنوان URL أساسي مخصص أو نقطة نهاية Azure.

لا يزال بالإمكان تحديد نماذج `openai/gpt-image-1.5` و`openai/gpt-image-1` و`openai/gpt-image-1-mini` صراحةً. استخدم `gpt-image-1.5` لمخرجات PNG/WebP ذات الخلفية الشفافة؛ ترفض واجهة API الحالية لـ `gpt-image-2` `background: "transparent"`.

يدعم `gpt-image-2` توليد الصور من النص وتحرير الصور المرجعية عبر أداة `image_generate` نفسها. يمرّر OpenClaw `prompt` و`count` و`size` و`quality` و`outputFormat` والصور المرجعية إلى OpenAI. لا تتلقى OpenAI `aspectRatio` أو `resolution` مباشرةً؛ عندما يكون ذلك ممكنًا، يحوّل OpenClaw تلك القيم إلى `size` مدعوم، وإلا فتبلغ الأداة عنها كتجاوزات متجاهَلة.

توجد الخيارات الخاصة بـ OpenAI ضمن كائن `openai`:

jsonCopy code
[code]
    {  "quality": "low",  "outputFormat": "jpeg",  "openai": {    "background": "opaque",    "moderation": "low",    "outputCompression": 60,    "user": "end-user-42"  }}
[/code]

يقبل `openai.background` القيم `transparent` أو `opaque` أو `auto`؛ تتطلب المخرجات الشفافة `outputFormat` بقيمة `png` أو `webp` ونموذج صور OpenAI قادرًا على الشفافية. يوجّه OpenClaw طلبات الخلفية الشفافة الافتراضية لـ `gpt-image-2` إلى `gpt-image-1.5`. ينطبق `openai.outputCompression` على مخرجات JPEG/WebP.

تلميح `background` في المستوى الأعلى محايد بين المزوّدين، ويُربط حاليًا بحقل طلب `background` نفسه في OpenAI عند تحديد مزوّد OpenAI. المزوّدون الذين لا يصرّحون بدعم الخلفية يعيدونه في `ignoredOverrides` بدلًا من تلقي المعامل غير المدعوم.

لتوجيه توليد الصور في OpenAI عبر نشر Azure OpenAI بدلًا من `api.openai.com`، راجع [نقاط نهاية Azure OpenAI](</ar/providers/openai#azure-openai-endpoints>).

نماذج صور OpenRouter

يستخدم توليد الصور في OpenRouter مفتاح `OPENROUTER_API_KEY` نفسه ويُوجَّه عبر واجهة API لصور إكمالات الدردشة في OpenRouter. حدّد نماذج صور OpenRouter باستخدام البادئة `openrouter/`:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openrouter/google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

يمرّر OpenClaw `prompt` و`count` والصور المرجعية وتلميحات `aspectRatio` / `resolution` المتوافقة مع Gemini إلى OpenRouter. تشمل اختصارات نماذج صور OpenRouter المدمجة الحالية `google/gemini-3.1-flash-image-preview` و `google/gemini-3-pro-image-preview` و`openai/gpt-5.4-image-2`. استخدم `action: "list"` لمعرفة ما يعرّضه Plugin المهيأ لديك.

مصادقة MiniMax المزدوجة

يتوفر توليد الصور في MiniMax عبر مساري مصادقة MiniMax المدمجين:

  * `minimax/image-01` لإعدادات مفتاح API
  * `minimax-portal/image-01` لإعدادات OAuth

xAI grok-imagine-image

يستخدم مزوّد xAI المدمج `/v1/images/generations` للطلبات القائمة على الموجه فقط، و`/v1/images/edits` عند وجود `image` أو `images`.

  * النماذج: `xai/grok-imagine-image`، `xai/grok-imagine-image-pro`
  * العدد: ما يصل إلى 4
  * المراجع: `image` واحدة أو ما يصل إلى خمس `images`
  * نسب الأبعاد: `1:1`، `16:9`، `9:16`، `4:3`، `3:4`، `2:3`، `3:2`
  * الدقات: `1K`، `2K`
  * المخرجات: تُعاد كمرفقات صور يديرها OpenClaw


يتعمد OpenClaw عدم تعريض `quality` أو `mask` أو `user` الأصلية في xAI أو نسب الأبعاد الإضافية الأصلية فقط إلى أن توجد هذه عناصر التحكم في عقد `image_generate` المشترك بين المزوّدين.

## أمثلة

### توليد (منظر طبيعي 4K)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="A clean editorial poster for OpenClaw image generation" size=3840x2160 count=1
[/code]

### توليد (PNG شفاف)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-1.5 prompt="A simple red circle sticker on a transparent background" outputFormat=png background=transparent
[/code]

CLI المكافئ:

bashCopy code
[code]
    openclaw infer image generate \--model openai/gpt-image-1.5 \--output-format png \--background transparent \--prompt "A simple red circle sticker on a transparent background" \--json
[/code]

### توليد (صورتان مربعتان)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Two visual directions for a calm productivity app icon" size=1024x1024 count=2
[/code]

### تحرير (مرجع واحد)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Keep the subject, replace the background with a bright studio setup" image=/path/to/reference.png size=1024x1536
[/code]

### تحرير (مراجع متعددة)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Combine the character identity from the first image with the color palette from the second" images='["/path/to/character.png","/path/to/palette.jpg"]' size=1536x1024
[/code]

تتوفر رايتا `--output-format` و`--background` نفسهما في `openclaw infer image edit`؛ تظل `--openai-background` اسمًا بديلًا خاصًا بـ OpenAI. لا يصرّح المزوّدون المدمجون غير OpenAI حاليًا بتحكم صريح في الخلفية، لذلك يُبلغ عن `background: "transparent"` كتجاوز متجاهَل لهم.

## ذو صلة

  * [نظرة عامة على الأدوات](</ar/tools>) \- جميع أدوات الوكيل المتاحة
  * [ComfyUI](</ar/providers/comfy>) \- إعداد سير عمل ComfyUI المحلي وComfy Cloud
  * [fal](</ar/providers/fal>) \- إعداد مزوّد الصور والفيديو fal
  * [Google (Gemini)](</ar/providers/google>) \- إعداد مزوّد صور Gemini
  * [MiniMax](</ar/providers/minimax>) \- إعداد مزوّد صور MiniMax
  * [OpenAI](</ar/providers/openai>) \- إعداد مزوّد OpenAI Images
  * [Vydra](</ar/providers/vydra>) \- إعداد الصور والفيديو والكلام في Vydra
  * [xAI](</ar/providers/xai>) \- إعداد صور وفيديو وبحث وتنفيذ كود وTTS في Grok
  * [مرجع التكوين](</ar/gateway/config-agents#agent-defaults>) \- تكوين `imageGenerationModel`
  * [النماذج](</ar/concepts/models>) \- تكوين النماذج والتجاوز عند الفشل


Was this useful?YesNo