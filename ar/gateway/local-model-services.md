---
title: خدمات النماذج المحلية
source_url: https://docs.openclaw.ai/ar/gateway/local-model-services
scraped_at: 2026-05-25
---

`models.providers.<id>.localService` يتيح لـ OpenClaw بدء خادم نماذج محلي مملوك للمزوّد عند الطلب. هذا إعداد على مستوى المزوّد: عندما ينتمي النموذج المحدد إلى ذلك المزوّد، يفحص OpenClaw الخدمة، ويبدأ العملية إذا كانت نقطة النهاية متوقفة، وينتظر الجاهزية، ثم يرسل طلب النموذج.

استخدمه للخوادم المحلية التي تكون مكلفة إذا بقيت قيد التشغيل طوال اليوم، أو للإعدادات اليدوية التي ينبغي أن يكون اختيار النموذج فيها كافيًا لتشغيل الواجهة الخلفية.

## كيف يعمل

  1. يُحل طلب النموذج إلى مزوّد مهيأ.
  2. إذا كان لدى ذلك المزوّد `localService`، يفحص OpenClaw `healthUrl`.
  3. إذا نجح الفحص، يستخدم OpenClaw الخادم الموجود.
  4. إذا فشل الفحص، يبدأ OpenClaw تشغيل `command` مع `args`.
  5. يستطلع OpenClaw الجاهزية حتى تنتهي مدة `readyTimeoutMs`.
  6. يُرسل طلب النموذج عبر نقل المزوّد المعتاد.
  7. إذا كان OpenClaw قد بدأ العملية وكانت `idleStopMs` موجبة، فستُوقف العملية بعد أن يظل آخر طلب قيد التنفيذ خاملًا لتلك المدة.


لا يثبّت OpenClaw launchd أو systemd أو Docker أو عفريتًا لهذا الغرض. يكون الخادم عملية فرعية لعملية OpenClaw التي احتاجت إليه أولًا.

## شكل الإعداد

json5Copy code
[code]
    {  models: {    providers: {      local: {        baseUrl: "http://127.0.0.1:8000/v1",        apiKey: "local-model",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/absolute/path/to/server",          args: ["--host", "127.0.0.1", "--port", "8000"],          cwd: "/absolute/path/to/working-dir",          env: { LOCAL_MODEL_CACHE: "/absolute/path/to/cache" },          healthUrl: "http://127.0.0.1:8000/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "my-local-model",            name: "My Local Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## الحقول

  * `command`: مسار تنفيذي مطلق. لا يُستخدم بحث الصدفة.
  * `args`: وسائط العملية. لا تُطبّق أي قواعد لتوسيع الصدفة أو الأنابيب أو أنماط glob أو الاقتباس.
  * `cwd`: دليل العمل الاختياري للعملية.
  * `env`: متغيرات بيئة اختيارية تُدمج فوق بيئة عملية OpenClaw.
  * `healthUrl`: عنوان URL للجاهزية. إذا حُذف، يلحق OpenClaw `/models` بـ `baseUrl`، بحيث يصبح `http://127.0.0.1:8000/v1` هو `http://127.0.0.1:8000/v1/models`.
  * `readyTimeoutMs`: مهلة جاهزية بدء التشغيل. الافتراضي: `120000`.
  * `idleStopMs`: تأخير إيقاف الخمول للعمليات التي يبدأها OpenClaw. القيمة `0` أو الحذف يبقيان العملية حية حتى يخرج OpenClaw.


## مثال Inferrs

Inferrs واجهة خلفية مخصصة متوافقة مع OpenAI عبر `/v1`، لذلك تعمل واجهة خدمة محلية API نفسها مع إدخال مزوّد `inferrs`.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "inferrs/google/gemma-4-E2B-it" },    },  },  models: {    mode: "merge",    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/opt/homebrew/bin/inferrs",          args: [            "serve",            "google/gemma-4-E2B-it",            "--host",            "127.0.0.1",            "--port",            "8080",            "--device",            "metal",          ],          healthUrl: "http://127.0.0.1:8080/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

استبدل `command` بنتيجة `which inferrs` على الجهاز الذي يشغّل OpenClaw.

## مثال ds4

json5Copy code
[code]
    {  models: {    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/Users/you/Projects/oss/ds4/ds4-server",          args: [            "--model",            "/Users/you/Projects/oss/ds4/ds4flash.gguf",            "--host",            "127.0.0.1",            "--port",            "18000",            "--ctx",            "393216",          ],          cwd: "/Users/you/Projects/oss/ds4",          healthUrl: "http://127.0.0.1:18000/v1/models",          readyTimeoutMs: 300000,          idleStopMs: 0,        },        models: [],      },    },  },}
[/code]

## ملاحظات تشغيلية

  * تدير عملية OpenClaw واحدة العملية الفرعية التي بدأتها. أي عملية OpenClaw أخرى ترى عنوان URL للصحة نفسه قيد التشغيل بالفعل ستعيد استخدامه دون تبنيه.
  * يُسلسل بدء التشغيل لكل أمر مزوّد ومجموعة وسائط، لذلك لا تؤدي الطلبات المتزامنة إلى إنشاء خوادم مكررة للإعداد نفسه.
  * تحتفظ استجابات البث النشطة بإيجار؛ وينتظر إيقاف الخمول حتى تكتمل معالجة جسم الاستجابة.
  * استخدم `timeoutSeconds` على المزوّدين المحليين البطيئين حتى لا تصطدم عمليات البدء الباردة وعمليات التوليد الطويلة بمهلة طلب النموذج الافتراضية.
  * استخدم `healthUrl` صريحًا إذا كان خادمك يعرّض الجاهزية في مكان آخر غير `/v1/models`.


## ذو صلة

[**النماذج المحلية** إعداد النموذج المحلي، وخيارات المزوّد، وإرشادات السلامة. ](</ar/gateway/local-models>) [**Inferrs** شغّل OpenClaw عبر خادم inferrs المحلي المتوافق مع OpenAI. ](</ar/providers/inferrs>)

Was this useful?YesNo