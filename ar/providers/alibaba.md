---
title: Alibaba Model Studio
source_url: https://docs.openclaw.ai/ar/providers/alibaba
scraped_at: 2026-05-25
---

OpenClaw يوفّر Plugin مضمّنًا باسم `alibaba` يسجّل موفّرًا لتوليد الفيديو لنماذج Wan على Alibaba Model Studio (الاسم الدولي لـ DashScope). يكون الـ Plugin مفعّلًا افتراضيًا؛ ما عليك سوى تعيين مفتاح API.

الخاصية | القيمة  
---|---  
معرّف الموفّر | `alibaba`  
Plugin | مضمّن، `enabledByDefault: true`  
متغيرات بيئة المصادقة | `MODELSTUDIO_API_KEY` → `DASHSCOPE_API_KEY` → `QWEN_API_KEY` (أول تطابق يفوز)  
علامة الإعداد الأولي | `--auth-choice alibaba-model-studio-api-key`  
علامة CLI المباشرة | `--alibaba-model-studio-api-key <key>`  
النموذج الافتراضي | `alibaba/wan2.6-t2v`  
عنوان URL الأساسي الافتراضي | `https://dashscope-intl.aliyuncs.com`  
  
## البدء

* ### Set an API key

استخدم الإعداد الأولي لتخزين المفتاح مقابل موفّر `alibaba`:

bashCopy code
[code]
    openclaw onboard --auth-choice alibaba-model-studio-api-key
[/code]

أو مرّر المفتاح مباشرة أثناء التثبيت/الإعداد الأولي:

bashCopy code
[code]
    openclaw onboard --alibaba-model-studio-api-key <your-key>
[/code]

أو صدّر أيًا من متغيرات البيئة المقبولة قبل بدء Gateway:

bashCopy code
[code]
    export MODELSTUDIO_API_KEY=sk-...# or DASHSCOPE_API_KEY=...# or QWEN_API_KEY=...
[/code]

* ### Set a default video model

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "alibaba/wan2.6-t2v",      },    },  },}
[/code]

* ### Verify the provider is configured

bashCopy code
[code]
    openclaw models list --provider alibaba
[/code]

يجب أن تتضمن القائمة جميع نماذج Wan الخمسة المضمّنة. إذا لم يتم حل `MODELSTUDIO_API_KEY`، فإن `openclaw models status --json` يبلّغ عن بيانات الاعتماد المفقودة ضمن `auth.unusableProfiles`.

## نماذج Wan المضمّنة

مرجع النموذج | الوضع  
---|---  
`alibaba/wan2.6-t2v` | نص إلى فيديو (افتراضي)  
`alibaba/wan2.6-i2v` | صورة إلى فيديو  
`alibaba/wan2.6-r2v` | مرجع إلى فيديو  
`alibaba/wan2.6-r2v-flash` | مرجع إلى فيديو (سريع)  
`alibaba/wan2.7-r2v` | مرجع إلى فيديو  
  
## القدرات والحدود

يعكس الموفّر المضمّن حدود واجهة API لفيديو Wan في DashScope. تشترك الأوضاع الثلاثة كلها في عدد الفيديوهات لكل طلب وحد مدة الفيديو نفسه؛ ويختلف شكل الإدخال فقط.

الوضع | الحد الأقصى للفيديوهات الناتجة | الحد الأقصى لصور الإدخال | الحد الأقصى لفيديوهات الإدخال | الحد الأقصى للمدة | عناصر التحكم المدعومة  
---|---|---|---|---|---  
نص إلى فيديو | 1 | غير متاح | غير متاح | 10 ث | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
صورة إلى فيديو | 1 | 1 | غير متاح | 10 ث | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
مرجع إلى فيديو | 1 | غير متاح | 4 | 10 ث | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
  
عندما لا يضمّن الطلب `durationSeconds`، يرسل الموفّر القيمة الافتراضية المقبولة لدى DashScope وهي **5 ثوانٍ**. عيّن `durationSeconds` صراحةً في [أداة توليد الفيديو](</ar/tools/video-generation>) للتمديد حتى 10 ثوانٍ.

## الإعدادات المتقدمة

Override the DashScope base URL

يستخدم الموفّر نقطة نهاية DashScope الدولية افتراضيًا. لاستهداف نقطة نهاية منطقة الصين، عيّن:

json5Copy code
[code]
    {  models: {    providers: {      alibaba: {        baseUrl: "https://dashscope.aliyuncs.com",      },    },  },}
[/code]

يزيل الموفّر الشرطات المائلة اللاحقة قبل إنشاء عناوين URL لمهام AIGC.

Auth env priority

يحل OpenClaw مفتاح API الخاص بـ Alibaba من متغيرات البيئة بهذا الترتيب، مع أخذ أول قيمة غير فارغة:

  1. `MODELSTUDIO_API_KEY`
  2. `DASHSCOPE_API_KEY`
  3. `QWEN_API_KEY`


تتجاوز إدخالات `auth.profiles` المضبوطة (عبر `openclaw models auth login`) حل متغيرات البيئة. راجع [ملفات تعريف المصادقة في الأسئلة الشائعة للنماذج](</ar/help/faq-models#what-is-an-auth-profile>) لمعرفة آليات تدوير الملفات الشخصية وفترات التهدئة والتجاوز.

Relationship to the Qwen plugin

يتصل كلا الـ Pluginين المضمّنين بـ DashScope ويقبلان مفاتيح API متداخلة. استخدم:

  * معرّفات `alibaba/wan*.*` لتشغيل موفّر فيديو Wan المخصص الموثّق في هذه الصفحة.
  * معرّفات `qwen/*` لدردشة Qwen والتضمين وفهم الوسائط (راجع [Qwen](</ar/providers/qwen>)).


تعيين `MODELSTUDIO_API_KEY` مرة واحدة يصادق كلا الـ Pluginين لأن قائمة متغيرات بيئة المصادقة تتداخل عمدًا؛ لست بحاجة إلى إعداد كل Plugin على حدة.

## ذات صلة

[**Video generation** معلمات أداة الفيديو المشتركة واختيار الموفّر. ](</ar/tools/video-generation>) [**Qwen** إعداد دردشة Qwen والتضمين وفهم الوسائط باستخدام مصادقة DashScope نفسها. ](</ar/providers/qwen>) [**Configuration reference** الإعدادات الافتراضية للوكلاء وإعدادات النماذج. ](</ar/gateway/config-agents#agent-defaults>) [**Models FAQ** ملفات تعريف المصادقة، وتبديل النماذج، وحل أخطاء "no profile". ](</ar/help/faq-models>)

Was this useful?YesNo