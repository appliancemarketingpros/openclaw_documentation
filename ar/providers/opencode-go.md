---
title: OpenCode Go
source_url: https://docs.openclaw.ai/ar/providers/opencode-go
scraped_at: 2026-05-25
---

يُعد OpenCode Go كتالوج Go ضمن [OpenCode](</ar/providers/opencode>). ويستخدم مفتاح `OPENCODE_API_KEY` نفسه الذي يستخدمه كتالوج Zen، لكنه يحتفظ بمعرّف موفّر وقت التشغيل `opencode-go` لكي يبقى التوجيه لكل نموذج من المنبع صحيحًا.

الخاصية | القيمة  
---|---  
موفّر وقت التشغيل | `opencode-go`  
المصادقة | `OPENCODE_API_KEY`  
الإعداد الأب | [OpenCode](</ar/providers/opencode>)  
  
## الكتالوج المدمج

يستمد OpenClaw معظم صفوف كتالوج Go من سجل نماذج pi المجمّع ويستكمل الصفوف الحالية من المنبع إلى أن يلحق بها السجل. شغّل `openclaw models list --provider opencode-go` للحصول على قائمة النماذج الحالية.

يتضمن الموفّر ما يلي:

مرجع النموذج | الاسم  
---|---  
`opencode-go/glm-5` | GLM-5  
`opencode-go/glm-5.1` | GLM-5.1  
`opencode-go/kimi-k2.5` | Kimi K2.5  
`opencode-go/kimi-k2.6` | Kimi K2.6 (حدود 3x)  
`opencode-go/deepseek-v4-pro` | DeepSeek V4 Pro  
`opencode-go/deepseek-v4-flash` | DeepSeek V4 Flash  
`opencode-go/mimo-v2-omni` | MiMo V2 Omni  
`opencode-go/mimo-v2-pro` | MiMo V2 Pro  
`opencode-go/minimax-m2.5` | MiniMax M2.5  
`opencode-go/minimax-m2.7` | MiniMax M2.7  
`opencode-go/qwen3.5-plus` | Qwen3.5 Plus  
`opencode-go/qwen3.6-plus` | Qwen3.6 Plus  
  
## البدء

### تفاعلي

* ### شغّل الإعداد الأولي

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

* ### عيّن نموذج Go كافتراضي

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### تحقق من توفر النماذج

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

### غير تفاعلي

* ### مرّر المفتاح مباشرة

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### تحقق من توفر النماذج

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## مثال على التهيئة

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "YOUR_API_KEY_HERE" }, // pragma: allowlist secret  agents: { defaults: { model: { primary: "opencode-go/kimi-k2.6" } } },}
[/code]

## تهيئة متقدمة

سلوك التوجيه

يتولى OpenClaw التوجيه لكل نموذج تلقائيًا عندما يستخدم مرجع النموذج `opencode-go/...`. ولا يلزم أي إعداد إضافي للموفّر.

اصطلاح مرجع وقت التشغيل

تبقى مراجع وقت التشغيل صريحة: `opencode/...` لـ Zen، و`opencode-go/...` لـ Go. وهذا يحافظ على صحة التوجيه من المنبع لكل نموذج عبر الكتالوجين.

بيانات اعتماد مشتركة

يُستخدم `OPENCODE_API_KEY` نفسه لكل من كتالوجي Zen وGo. ويؤدي إدخال المفتاح أثناء الإعداد إلى تخزين بيانات الاعتماد لكلا موفّري وقت التشغيل.

## ذي صلة

[**OpenCode (الأب)** الإعداد المشترك، ونظرة عامة على الكتالوج، وملاحظات متقدمة. ](</ar/providers/opencode>) [**اختيار النموذج** اختيار الموفّرين، ومراجع النماذج، وسلوك التبديل الاحتياطي. ](</ar/concepts/model-providers>)

Was this useful?YesNo