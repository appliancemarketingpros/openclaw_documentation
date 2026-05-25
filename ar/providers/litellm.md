---
title: LiteLLM
source_url: https://docs.openclaw.ai/ar/providers/litellm
scraped_at: 2026-05-25
---

[LiteLLM](<https://litellm.ai>) هي بوابة LLM مفتوحة المصدر توفر API موحدًا لأكثر من 100 موفر نماذج. مرّر OpenClaw عبر LiteLLM للحصول على تتبع مركزي للتكلفة، وتسجيل السجلات، ومرونة تبديل الخلفيات دون تغيير إعدادات OpenClaw.

## البدء السريع

### Onboarding (recommended)

**الأفضل لـ:** أسرع مسار إلى إعداد LiteLLM عامل.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice litellm-api-key
[/code]

للإعداد غير التفاعلي مع وكيل بعيد، مرّر عنوان URL للوكيل صراحةً:

bashCopy code
[code]
    openclaw onboard --non-interactive --auth-choice litellm-api-key --litellm-api-key "$LITELLM_API_KEY" --custom-base-url "https://litellm.example/v1"
[/code]

### Manual setup

**الأفضل لـ:** تحكم كامل في التثبيت والإعدادات.

* ### Start LiteLLM Proxy

bashCopy code
[code]
    pip install 'litellm[proxy]'litellm --model claude-opus-4-6
[/code]

* ### Point OpenClaw to LiteLLM

bashCopy code
[code]
    export LITELLM_API_KEY="your-litellm-key" openclaw
[/code]

هذا كل شيء. يمرّر OpenClaw الآن عبر LiteLLM.

## الإعدادات

### متغيرات البيئة

bashCopy code
[code]
    export LITELLM_API_KEY="sk-litellm-key"
[/code]

### ملف الإعدادات

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",        api: "openai-completions",        models: [          {            id: "claude-opus-4-6",            name: "Claude Opus 4.6",            reasoning: true,            input: ["text", "image"],            contextWindow: 200000,            maxTokens: 64000,          },          {            id: "gpt-4o",            name: "GPT-4o",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "litellm/claude-opus-4-6" },    },  },}
[/code]

## الإعدادات المتقدمة

### إنشاء الصور

يمكن لـ LiteLLM أيضًا دعم أداة `image_generate` من خلال مسارات متوافقة مع OpenAI مثل `/images/generations` و`/images/edits`. اضبط نموذج صور LiteLLM ضمن `agents.defaults.imageGenerationModel`:

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",      },    },  },  agents: {    defaults: {      imageGenerationModel: {        primary: "litellm/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

تعمل عناوين URL الخاصة بـ LiteLLM على حلقة الرجوع مثل `http://localhost:4000` دون تجاوز عام للشبكة الخاصة. بالنسبة إلى وكيل مستضاف على شبكة LAN، اضبط `models.providers.litellm.request.allowPrivateNetwork: true` لأن مفتاح API سيُرسل إلى مضيف الوكيل المضبوط.

Virtual keys

أنشئ مفتاحًا مخصصًا لـ OpenClaw مع حدود إنفاق:

bashCopy code
[code]
    curl -X POST "http://localhost:4000/key/generate" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \  -H "Content-Type: application/json" \  -d '{    "key_alias": "openclaw",    "max_budget": 50.00,    "budget_duration": "monthly"  }'
[/code]

استخدم المفتاح المُنشأ كـ `LITELLM_API_KEY`.

Model routing

يمكن لـ LiteLLM توجيه طلبات النماذج إلى خلفيات مختلفة. اضبط ذلك في `config.yaml` الخاص بـ LiteLLM:

yamlCopy code
[code]
    model_list:  - model_name: claude-opus-4-6    litellm_params:      model: claude-opus-4-6      api_key: os.environ/ANTHROPIC_API_KEY   - model_name: gpt-4o    litellm_params:      model: gpt-4o      api_key: os.environ/OPENAI_API_KEY
[/code]

يواصل OpenClaw طلب `claude-opus-4-6` — ويتولى LiteLLM التوجيه.

Viewing usage

تحقق من لوحة معلومات LiteLLM أو API:

bashCopy code
[code]
    # Key infocurl "http://localhost:4000/key/info" \  -H "Authorization: Bearer sk-litellm-key" # Spend logscurl "http://localhost:4000/spend/logs" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY"
[/code]

Proxy behavior notes

  * يعمل LiteLLM على `http://localhost:4000` افتراضيًا
  * يتصل OpenClaw عبر نقطة نهاية `/v1` المتوافقة مع OpenAI وبنمط الوكيل في LiteLLM
  * لا ينطبق تشكيل الطلبات الأصلي الخاص بـ OpenAI فقط عبر LiteLLM: لا `service_tier`، ولا `store` في Responses، ولا تلميحات لذاكرة التخزين المؤقت للمطالبات، ولا تشكيل حمولات متوافق مع استدلال OpenAI
  * لا تُحقن ترويسات الإسناد المخفية الخاصة بـ OpenClaw (`originator` و`version` و`User-Agent`) على عناوين URL الأساسية المخصصة لـ LiteLLM


## ذات صلة

[**LiteLLM Docs** وثائق LiteLLM الرسمية ومرجع API. ](<https://docs.litellm.ai>) [**Model selection** نظرة عامة على جميع الموفرين، ومراجع النماذج، وسلوك التحويل الاحتياطي. ](</ar/concepts/model-providers>) [**Configuration** مرجع الإعدادات الكامل. ](</ar/gateway/configuration>) [**Model selection** كيفية اختيار النماذج وضبطها. ](</ar/concepts/models>)

Was this useful?YesNo