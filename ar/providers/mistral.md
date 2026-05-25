---
title: Mistral
source_url: https://docs.openclaw.ai/ar/providers/mistral
scraped_at: 2026-05-25
---

OpenClaw يتضمّن Plugin Mistral مضمّنًا يسجّل أربعة عقود: إكمالات المحادثة، وفهم الوسائط (نسخ Voxtral الدفعي)، وSTT الفوري لـ Voice Call (Voxtral Realtime)، وتضمينات الذاكرة (`mistral-embed`).

الخاصية | القيمة  
---|---  
معرّف المزوّد | `mistral`  
Plugin | مضمّن، `enabledByDefault: true`  
متغيّر بيئة المصادقة | `MISTRAL_API_KEY`  
علم التهيئة | `--auth-choice mistral-api-key`  
علم CLI المباشر | `--mistral-api-key <key>`  
API | متوافق مع OpenAI (`openai-completions`)  
عنوان URL الأساسي | `https://api.mistral.ai/v1`  
النموذج الافتراضي | `mistral/mistral-large-latest`  
نموذج التضمين | `mistral-embed`  
Voxtral الدفعي | `voxtral-mini-latest` (نسخ الصوت)  
Voxtral الفوري | `voxtral-mini-transcribe-realtime-2602`  
  
## البدء

* ### Get your API key

أنشئ مفتاح API في [Mistral Console](<https://console.mistral.ai/>).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice mistral-api-key
[/code]

أو مرّر المفتاح مباشرة:

bashCopy code
[code]
    openclaw onboard --mistral-api-key "$MISTRAL_API_KEY"
[/code]

* ### Set a default model

json5Copy code
[code]
    {  env: { MISTRAL_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "mistral/mistral-large-latest" } } },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider mistral
[/code]

## فهرس LLM المضمّن

[Mistral Medium 3.5](<https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04>) هو نموذج Medium المدمج الحالي في الفهرس المضمّن: أوزان كثيفة بحجم 128B، وإدخال نصوص وصور، وسياق 256K، واستدعاء الدوال، وإخراج منظّم، وبرمجة، واستدلال قابل للضبط عبر Chat Completions API. استخدم `mistral/mistral-medium-3-5` عندما تريد نموذج Mistral الأحدث الموحّد للاستخدامات الوكيلية/البرمجية بدلًا من النموذج الافتراضي `mistral/mistral-large-latest`.

يشحن OpenClaw حاليًا فهرس Mistral المضمّن هذا:

مرجع النموذج | الإدخال | السياق | أقصى إخراج | ملاحظات  
---|---|---|---|---  
`mistral/mistral-large-latest` | نص، صورة | 262,144 | 16,384 | النموذج الافتراضي  
`mistral/mistral-medium-2508` | نص، صورة | 262,144 | 8,192 | Mistral Medium 3.1  
`mistral/mistral-medium-3-5` | نص، صورة | 262,144 | 8,192 | Mistral Medium 3.5؛ استدلال قابل للضبط  
`mistral/mistral-small-latest` | نص، صورة | 128,000 | 16,384 | Mistral Small 4؛ استدلال قابل للضبط عبر API `reasoning_effort`  
`mistral/pixtral-large-latest` | نص، صورة | 128,000 | 32,768 | Pixtral  
`mistral/codestral-latest` | نص | 256,000 | 4,096 | البرمجة  
`mistral/devstral-medium-latest` | نص | 262,144 | 32,768 | Devstral 2  
`mistral/magistral-small` | نص | 128,000 | 40,000 | مفعّل للاستدلال  
  
بعد التهيئة، نفّذ اختبار دخان لـ Medium 3.5 من دون تشغيل Gateway:

bashCopy code
[code]
    openclaw infer model run --local \  --model mistral/mistral-medium-3-5 \  --prompt "Reply with exactly: mistral-ok" \  --json
[/code]

لتصفّح صف الفهرس المضمّن قبل تغيير الإعدادات:

bashCopy code
[code]
    openclaw models list --all --provider mistral --plain
[/code]

## نسخ الصوت (Voxtral)

استخدم Voxtral لنسخ الصوت دفعيًا عبر مسار فهم الوسائط.

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "mistral", model: "voxtral-mini-latest" }],      },    },  },}
[/code]

## STT المتدفق لـ Voice Call

يسجّل Plugin `mistral` المضمّن Voxtral Realtime كمزوّد STT متدفق لـ Voice Call.

الإعداد | مسار الإعداد | الافتراضي  
---|---|---  
مفتاح API | `plugins.entries.voice-call.config.streaming.providers.mistral.apiKey` | يرجع إلى `MISTRAL_API_KEY`  
النموذج | `...mistral.model` | `voxtral-mini-transcribe-realtime-2602`  
الترميز | `...mistral.encoding` | `pcm_mulaw`  
معدل العينة | `...mistral.sampleRate` | `8000`  
التأخير المستهدف | `...mistral.targetStreamingDelayMs` | `800`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "mistral",            providers: {              mistral: {                apiKey: "${MISTRAL_API_KEY}",                targetStreamingDelayMs: 800,              },            },          },        },      },    },  },}
[/code]

## الإعدادات المتقدمة

Adjustable reasoning

يدعم `mistral/mistral-small-latest` (Mistral Small 4) و`mistral/mistral-medium-3-5` [الاستدلال القابل للضبط](<https://docs.mistral.ai/studio-api/conversations/reasoning/adjustable>) على Chat Completions API عبر `reasoning_effort` (`none` يقلّل التفكير الإضافي في الإخراج؛ و`high` يعرض آثار التفكير الكاملة قبل الإجابة النهائية). توصي Mistral باستخدام `reasoning_effort="high"` لحالات استخدام Medium 3.5 الوكيلية والبرمجية.

يربط OpenClaw مستوى **thinking** في الجلسة بـ API الخاص بـ Mistral:

مستوى التفكير في OpenClaw | `reasoning_effort` في Mistral  
---|---  
**off** / **minimal** | `none`  
**low** / **medium** / **high** / **xhigh** / **adaptive** / **max** | `high`  
  
مثال على إعداد محدود بالنموذج لاستدلال Medium 3.5:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "mistral/mistral-medium-3-5" },      models: {        "mistral/mistral-medium-3-5": {          params: { thinking: "high" },        },      },    },  },}
[/code]

Memory embeddings

يمكن لـ Mistral تقديم تضمينات الذاكرة عبر `/v1/embeddings` (النموذج الافتراضي: `mistral-embed`).

json5Copy code
[code]
    {  memorySearch: { provider: "mistral" },}
[/code]

Auth and base URL

  * تستخدم مصادقة Mistral `MISTRAL_API_KEY` (ترويسة Bearer).
  * يكون عنوان URL الأساسي للمزوّد افتراضيًا `https://api.mistral.ai/v1` ويقبل شكل طلب chat-completions القياسي المتوافق مع OpenAI.
  * نموذج التهيئة الافتراضي هو `mistral/mistral-large-latest`.
  * تجاوز عنوان URL الأساسي ضمن `models.providers.mistral.baseUrl` فقط عندما تنشر Mistral صراحة نقطة نهاية إقليمية تحتاج إليها.


## ذو صلة

[**Model selection** اختيار المزوّدين ومراجع النماذج وسلوك تجاوز الفشل. ](</ar/concepts/model-providers>) [**Media understanding** إعداد نسخ الصوت واختيار المزوّد. ](</ar/nodes/media-understanding>)

Was this useful?YesNo