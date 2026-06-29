---
title: ds4
source_url: https://docs.openclaw.ai/ar/providers/ds4
scraped_at: 2026-06-29
---

ModelsProviders

[ds4](<https://github.com/antirez/ds4>) يقدّم DeepSeek V4 Flash من خلفية Metal محلية مع API `/v1` متوافقة مع OpenAI. يتصل OpenClaw بـ ds4 عبر عائلة المزوّد العامة `openai-completions`.

ds4 ليس Plugin مزوّدًا مضمنًا في OpenClaw. اضبطه ضمن `models.providers.ds4`، ثم اختر `ds4/deepseek-v4-flash`.

  * معرّف المزوّد: `ds4`
  * Plugin: لا يوجد
  * API: Chat Completions متوافقة مع OpenAI (`openai-completions`)
  * عنوان URL الأساسي المقترح: `http://127.0.0.1:18000/v1`
  * معرّف النموذج: `deepseek-v4-flash`
  * استدعاءات الأدوات: مدعومة عبر `tools` و `tool_calls` بأسلوب OpenAI
  * الاستدلال: `thinking` و `reasoning_effort` بأسلوب DeepSeek


## المتطلبات

  * macOS مع دعم Metal.
  * نسخة ds4 عاملة تحتوي على `ds4-server` وملف DeepSeek V4 Flash GGUF.
  * ذاكرة كافية للسياق الذي تختاره. قيم `--ctx` الأكبر تخصص ذاكرة KV أكبر عند بدء الخادم.


## البدء السريع

* ### بدء ds4-server

استبدل `&lt;DS4_DIR&gt;` بمسار نسخة ds4 لديك.

bashCopy code
[code]
    &lt;DS4_DIR&gt;/ds4-server \  --model &lt;DS4_DIR&gt;/ds4flash.gguf \  --host 127.0.0.1 \  --port 18000 \  --ctx 32768 \  --tokens 128
[/code]

* ### التحقق من نقطة النهاية المتوافقة مع OpenAI

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

يجب أن تتضمن الاستجابة `deepseek-v4-flash`.

* ### إضافة إعدادات مزوّد OpenClaw

أضف الإعدادات من الإعدادات الكاملة، ثم شغّل فحص نموذج لمرة واحدة:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

## الإعدادات الكاملة

استخدم هذه الإعدادات عندما يكون ds4 قيد التشغيل بالفعل على `127.0.0.1:18000`.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "ds4/deepseek-v4-flash" },      models: {        "ds4/deepseek-v4-flash": {          alias: "DS4 local",        },      },    },  },  models: {    mode: "merge",    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

أبقِ `contextWindow` متوافقًا مع قيمة `ds4-server --ctx`. وأبقِ `maxTokens` متوافقًا مع `--tokens` ما لم تكن تقصد أن يطلب OpenClaw مخرجات أقل من القيمة الافتراضية للخادم.

## بدء التشغيل عند الطلب

يمكن لـ OpenClaw بدء ds4 فقط عندما يتم اختيار نموذج `ds4/...`. أضف `localService` إلى إدخال المزوّد نفسه:

json5Copy code
[code]
    {  models: {    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "&lt;DS4_DIR&gt;/ds4-server",          args: [            "--model",            "&lt;DS4_DIR&gt;/ds4flash.gguf",            "--host",            "127.0.0.1",            "--port",            "18000",            "--ctx",            "32768",            "--tokens",            "128",          ],          cwd: "&lt;DS4_DIR&gt;",          healthUrl: "http://127.0.0.1:18000/v1/models",          readyTimeoutMs: 300000,          idleStopMs: 0,        },        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

يجب أن يكون `command` مسارًا مطلقًا لملف قابل للتنفيذ. لا يُستخدم بحث الصدفة ولا توسيع `~`. راجع [خدمات النماذج المحلية](</ar/gateway/local-model-services>) لكل حقل من حقول `localService`.

## Think Max

يطبّق ds4 وضع Think Max فقط عندما يتحقق الشرطان معًا:

  * يبدأ `ds4-server` مع `--ctx 393216` أو أعلى.
  * يستخدم الطلب `reasoning_effort: "max"` أو حقل الجهد المكافئ في ds4.


إذا شغّلت ذلك السياق الكبير، فحدّث كلًا من أعلام الخادم وبيانات نموذج OpenClaw الوصفية:

json5Copy code
[code]
    {  contextWindow: 393216,  maxTokens: 384000,  compat: {    supportsUsageInStreaming: true,    supportsReasoningEffort: true,    maxTokensField: "max_tokens",    supportsStrictMode: false,    thinkingFormat: "deepseek",    supportedReasoningEfforts: ["low", "medium", "high", "xhigh", "max"],  },}
[/code]

## الاختبار

ابدأ بفحص HTTP مباشر:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"Reply with exactly: ds4-ok"}],"max_tokens":16,"stream":false,"thinking":{"type":"disabled"}}'
[/code]

ثم اختبر توجيه نماذج OpenClaw:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

لاختبار دخان كامل للوكيل واستدعاء الأدوات، استخدم سياقًا لا يقل عن 32768:

bashCopy code
[code]
    openclaw agent \  --local \  --session-id ds4-tool-smoke \  --model ds4/deepseek-v4-flash \  --thinking off \  --message "Use the shell command pwd once, then reply exactly: tool-ok <output>" \  --json \  --timeout 240
[/code]

النتيجة المتوقعة:

  * `executionTrace.winnerProvider` هو `ds4`
  * `executionTrace.winnerModel` هو `deepseek-v4-flash`
  * `toolSummary.calls` لا يقل عن `1`
  * `finalAssistantVisibleText` يبدأ بـ `tool-ok`


## استكشاف الأخطاء وإصلاحها

يتعذر على curl /v1/models الاتصال

ds4 ليس قيد التشغيل أو غير مربوط بالمضيف والمنفذ في `baseUrl`. ابدأ `ds4-server`، ثم أعد المحاولة:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

500 prompt exceeds context

قيمة `--ctx` المضبوطة صغيرة جدًا لدورة OpenClaw. ارفع `ds4-server --ctx`، ثم حدّث `models.providers.ds4.models[].contextWindow` لتطابقها. تحتاج دورات الوكيل الكاملة مع الأدوات إلى سياق أكبر بكثير من طلب curl مباشر برسالة واحدة.

لا يتم تفعيل Think Max

يستخدم ds4 وضع Think Max فقط عندما يكون `--ctx` على الأقل `393216` ويطلب الطلب `reasoning_effort: "max"`. تعود السياقات الأصغر إلى الاستدلال العالي.

الطلب الأول بطيء

لدى ds4 مرحلة إقامة Metal باردة وتهيئة للنموذج. استخدم `localService.readyTimeoutMs: 300000` عندما يبدأ OpenClaw الخادم عند الطلب.

## ذات صلة

[**خدمات النماذج المحلية** ابدأ خوادم النماذج المحلية عند الطلب قبل طلبات النماذج. ](</ar/gateway/local-model-services>) [**النماذج المحلية** اختر خلفيات النماذج المحلية وشغّلها. ](</ar/gateway/local-models>) [**مزوّدو النماذج** اضبط مراجع المزوّدين والمصادقة وتجاوز الفشل. ](</ar/concepts/model-providers>) [**DeepSeek** سلوك مزوّد DeepSeek الأصلي وعناصر التحكم في التفكير. ](</ar/providers/deepseek>)

Was this useful?YesNo

Open issue