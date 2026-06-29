---
title: موفّر llama.cpp
source_url: https://docs.openclaw.ai/ar/plugins/llama-cpp
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

`llama-cpp` هو Plugin المزوّد الخارجي الرسمي لتضمينات GGUF المحلية. وهو يملك اعتمادية وقت التشغيل `node-llama-cpp` المستخدمة بواسطة `memorySearch.provider: "local"`.

ثبّته قبل استخدام تضمينات الذاكرة المحلية:

bashCopy code
[code]
    openclaw plugins install @openclaw/llama-cpp-provider
[/code]

لا تتضمن حزمة npm الرئيسية `openclaw` الحزمة `node-llama-cpp`. إن إبقاء الاعتمادية الأصلية في هذا Plugin يمنع تحديثات npm العادية لـ OpenClaw من حذف وقت تشغيل مثبّت يدويًا داخل دليل حزمة OpenClaw.

## التكوين

اضبط مزوّد بحث الذاكرة على `local`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        local: {          modelPath: "hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

النموذج الافتراضي هو `embeddinggemma-300m-qat-Q8_0.gguf`. يمكنك أيضًا توجيه `local.modelPath` إلى ملف `.gguf` محلي.

## وقت التشغيل الأصلي

استخدم Node 24 للحصول على أسلس مسار تثبيت أصلي. قد تحتاج نسخ المصدر التي تستخدم pnpm إلى الموافقة على الاعتمادية الأصلية وإعادة بنائها:

bashCopy code
[code]
    pnpm approve-buildspnpm rebuild node-llama-cpp
[/code]

لتضمينات محلية أقل احتكاكًا، استخدم مزوّد خدمة محليًا مثل Ollama أو LM Studio بدلًا من ذلك.

Was this useful?YesNo

Open issue