---
title: إنشاء Skills
source_url: https://docs.openclaw.ai/ar/tools/creating-skills
scraped_at: 2026-05-25
---

Skills تعلّم الوكيل كيف ومتى يستخدم الأدوات. كل مهارة هي دليل يحتوي على ملف `SKILL.md` يتضمن frontmatter بصيغة YAML وتعليمات markdown.

للتعرّف على كيفية تحميل Skills وترتيب أولويتها، راجع [Skills](</ar/tools/skills>).

## أنشئ أول مهارة لك

* ### أنشئ دليل المهارة

تعيش Skills في مساحة عملك. أنشئ مجلدًا جديدًا:

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace/skills/hello-world
[/code]

* ### اكتب SKILL.md

أنشئ `SKILL.md` داخل ذلك الدليل. يعرّف frontmatter البيانات الوصفية، ويحتوي متن markdown على تعليمات للوكيل.

markdownCopy code
[code]
    ---name: hello-worlddescription: A simple skill that says hello.--- # Hello World Skill When the user asks for a greeting, use the `echo` tool to say"Hello from your custom skill!".
[/code]

استخدم hyphen-case بأحرف صغيرة وأرقام وواصلات لاسم المهارة `name`. أبقِ اسم المجلد و`name` في frontmatter متطابقين.

* ### أضف أدوات (اختياري)

يمكنك تعريف مخططات أدوات مخصصة في frontmatter أو إرشاد الوكيل إلى استخدام أدوات النظام الحالية (مثل `exec` أو `browser`). يمكن أيضًا أن تُشحن Skills داخل الإضافات إلى جانب الأدوات التي توثقها.

* ### حمّل المهارة

ابدأ جلسة جديدة لكي يلتقط OpenClaw المهارة:

bashCopy code
[code]
    # From chat/new # Or restart the gatewayopenclaw gateway restart
[/code]

تحقّق من تحميل المهارة:

bashCopy code
[code]
    openclaw skills list
[/code]

* ### اختبرها

أرسل رسالة ينبغي أن تشغّل المهارة:

bashCopy code
[code]
    openclaw agent --message "give me a greeting"
[/code]

أو تحدّث ببساطة مع الوكيل واطلب تحية.

## مرجع بيانات المهارة الوصفية

يدعم frontmatter بصيغة YAML هذه الحقول:

الحقل | مطلوب | الوصف  
---|---|---  
`name` | نعم | معرّف فريد يستخدم أحرفًا صغيرة وأرقامًا وواصلات  
`description` | نعم | وصف من سطر واحد يظهر للوكيل  
`metadata.openclaw.os` | لا | مرشح نظام التشغيل (`["darwin"]`, `["linux"]`, إلخ)  
`metadata.openclaw.requires.bins` | لا | الثنائيات المطلوبة في PATH  
`metadata.openclaw.requires.config` | لا | مفاتيح الإعدادات المطلوبة  
  
## أفضل الممارسات

  * **كن موجزًا** — أرشد النموذج إلى _ما_ يجب فعله، لا إلى كيف يكون ذكاءً اصطناعيًا
  * **السلامة أولًا** — إذا كانت مهارتك تستخدم `exec`، فتأكد من أن المطالبات لا تسمح بحقن أوامر عشوائية من إدخال غير موثوق
  * **اختبر محليًا** — استخدم `openclaw agent --message "..."` للاختبار قبل المشاركة
  * **استخدم ClawHub** — تصفح Skills وساهم بها في [ClawHub](<https://clawhub.ai>)


## أين توجد Skills

الموقع | الأسبقية | النطاق  
---|---|---  
`\<workspace\>/skills/` | الأعلى | لكل وكيل  
`\<workspace\>/.agents/skills/` | عالية | لكل وكيل في مساحة العمل  
`~/.agents/skills/` | متوسطة | ملف تعريف وكيل مشترك  
`~/.openclaw/skills/` | متوسطة | مشتركة (كل الوكلاء)  
مضمّنة (مشحونة مع OpenClaw) | منخفضة | عام  
`skills.load.extraDirs` | الأدنى | مجلدات مشتركة مخصصة  
  
## ذات صلة

  * [مرجع Skills](</ar/tools/skills>) — قواعد التحميل والأسبقية والحجب
  * [إعدادات Skills](</ar/tools/skills-config>) — مخطط إعدادات `skills.*`
  * [ClawHub](</ar/clawhub>) — سجل المهارات العام
  * [بناء الإضافات](</ar/plugins/building-plugins>) — يمكن للإضافات شحن Skills


Was this useful?YesNo