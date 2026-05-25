---
title: OpenCode
source_url: https://docs.openclaw.ai/ar/providers/opencode
scraped_at: 2026-05-25
---

يعرض OpenCode كتالوجين مستضافين في OpenClaw:

الكتالوج | البادئة | مزوّد وقت التشغيل  
---|---|---  
**Zen** | `opencode/...` | `opencode`  
**Go** | `opencode-go/...` | `opencode-go`  
  
يستخدم كلا الكتالوجين مفتاح OpenCode API نفسه. ويُبقي OpenClaw معرّفات مزوّدي وقت التشغيل منفصلة حتى يظل التوجيه لكل نموذج من المصدر الأعلى صحيحًا، لكن الإعداد الأولي والمستندات يعاملانهما كإعداد OpenCode واحد.

## البدء

### كتالوج Zen

**الأفضل لـ:** proxy متعدد النماذج المنسّق من OpenCode (Claude، وGPT، وGemini).

* ### شغّل الإعداد الأولي

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zen
[/code]

أو مرّر المفتاح مباشرة:

bashCopy code
[code]
    openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
[/code]

* ### اضبط نموذج Zen كنموذج افتراضي

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode/claude-opus-4-6"
[/code]

* ### تحقق من أن النماذج متاحة

bashCopy code
[code]
    openclaw models list --provider opencode
[/code]

### كتالوج Go

**الأفضل لـ:** تشكيلة Kimi وGLM وMiniMax المستضافة عبر OpenCode.

* ### شغّل الإعداد الأولي

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

أو مرّر المفتاح مباشرة:

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### اضبط نموذج Go كنموذج افتراضي

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### تحقق من أن النماذج متاحة

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## مثال على الإعدادات

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

## الكتالوجات المضمّنة

### Zen

الخاصية | القيمة  
---|---  
مزوّد وقت التشغيل | `opencode`  
نماذج مثال | `opencode/claude-opus-4-6`، و`opencode/gpt-5.5`، و`opencode/gemini-3-pro`  
  
### Go

الخاصية | القيمة  
---|---  
مزوّد وقت التشغيل | `opencode-go`  
نماذج مثال | `opencode-go/kimi-k2.6`، و`opencode-go/glm-5`، و`opencode-go/minimax-m2.5`  
  
## إعدادات متقدمة

الأسماء المستعارة لمفتاح API

كما أن `OPENCODE_ZEN_API_KEY` مدعوم أيضًا كاسم مستعار لـ `OPENCODE_API_KEY`.

بيانات الاعتماد المشتركة

يؤدي إدخال مفتاح OpenCode واحد أثناء الإعداد إلى تخزين بيانات الاعتماد لكلا مزوّدي وقت التشغيل. ولا تحتاج إلى إعداد كل كتالوج على حدة.

الفوترة ولوحة التحكم

تقوم بتسجيل الدخول إلى OpenCode، وإضافة تفاصيل الفوترة، ونسخ مفتاح API الخاص بك. وتتم إدارة الفوترة وتوفر الكتالوج من لوحة تحكم OpenCode.

سلوك replay في Gemini

تبقى مراجع OpenCode المدعومة من Gemini على مسار proxy-Gemini، ولذلك يحافظ OpenClaw على تنظيف thought-signature الخاص بـ Gemini هناك من دون تفعيل التحقق الأصلي من replay في Gemini أو إعادة كتابة التهيئة.

سلوك replay لغير Gemini

تبقي مراجع OpenCode غير المدعومة من Gemini على سياسة replay الدنيا المتوافقة مع OpenAI.

## ذو صلة

[**اختيار النموذج** اختيار المزوّدين، ومراجع النماذج، وسلوك الرجوع الاحتياطي. ](</ar/concepts/model-providers>) [**مرجع الإعدادات** المرجع الكامل لإعدادات الوكلاء، والنماذج، والمزوّدين. ](</ar/gateway/configuration-reference>)

Was this useful?YesNo