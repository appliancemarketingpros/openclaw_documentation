---
title: التكوين
source_url: https://docs.openclaw.ai/ar/cli/configure
scraped_at: 2026-05-25
---

# `openclaw configure`

مطالبة تفاعلية لإجراء تغييرات موجّهة على إعداد موجود: بيانات الاعتماد، والأجهزة، وافتراضيات الوكيل، وGateway، والقنوات، وPlugins، وSkills، وفحوصات الصحة.

استخدم `openclaw onboard` لرحلة التشغيل الأول الكاملة والموجّهة، و`openclaw setup` للإعداد الأساسي/مساحة العمل فقط، و`openclaw channels add` عندما تحتاج فقط إلى إعداد حساب قناة.

عندما يبدأ configure من خيار مصادقة مزوّد، فإن منتقيات النموذج الافتراضي وقائمة السماح تفضّل ذلك المزوّد تلقائيًا. وبالنسبة إلى المزوّدين المقترنين مثل Volcengine وBytePlus، يطابق التفضيل نفسه أيضًا متغيرات خطط البرمجة الخاصة بهم (`volcengine-plan/*`، `byteplus-plan/*`). إذا كان مرشح المزوّد المفضل سينتج قائمة فارغة، يعود configure إلى الكتالوج غير المرشح بدلًا من عرض منتقي فارغ.

للبحث على الويب، يتيح لك `openclaw configure --section web` اختيار مزوّد وإعداد بيانات اعتماده. يعرض بعض المزوّدين أيضًا مطالبات متابعة خاصة بالمزوّد:

  * يمكن أن يوفّر **Grok** إعداد `x_search` اختياريًا باستخدام `XAI_API_KEY` نفسه وأن يتيح لك اختيار نموذج `x_search`.
  * يمكن أن يطلب **Kimi** منطقة Moonshot API (`api.moonshot.ai` مقابل `api.moonshot.cn`) ونموذج البحث على الويب الافتراضي من Kimi.


ذات صلة:

  * مرجع إعداد Gateway: [الإعداد](</ar/gateway/configuration>)
  * CLI للإعداد: [الإعداد](</ar/cli/config>)


## الخيارات

  * `--section <section>`: مرشح قسم قابل للتكرار


الأقسام المتاحة:

  * `workspace`
  * `model`
  * `web`
  * `gateway`
  * `daemon`
  * `channels`
  * `plugins`
  * `skills`
  * `health`


ملاحظات:

  * اختيار مكان تشغيل Gateway يحدّث دائمًا `gateway.mode`. يمكنك تحديد "متابعة" دون أقسام أخرى إذا كان هذا كل ما تحتاجه.
  * بعد عمليات كتابة الإعداد المحلي، يثبّت configure الـPlugins القابلة للتنزيل المحددة عندما يتطلبها مسار الإعداد المختار. لا يثبّت إعداد Gateway البعيد حزم Plugin المحلية.
  * الخدمات الموجّهة إلى القنوات (Slack/Discord/Matrix/Microsoft Teams) تطالب بقوائم سماح للقنوات/الغرف أثناء الإعداد. يمكنك إدخال أسماء أو معرّفات؛ ويحوّل المعالج الأسماء إلى معرّفات عندما يكون ذلك ممكنًا.
  * إذا شغّلت خطوة تثبيت الخفي، وكانت مصادقة الرمز تتطلب رمزًا، وكان `gateway.auth.token` مُدارًا بواسطة SecretRef، فإن configure يتحقق من SecretRef لكنه لا يحفظ قيم الرمز النصية الصريحة المحلولة في بيانات تعريف بيئة خدمة المشرف.
  * إذا كانت مصادقة الرمز تتطلب رمزًا وكان SecretRef للرمز المُعد غير محلول، يحظر configure تثبيت الخفي مع إرشادات معالجة قابلة للتنفيذ.
  * إذا تم إعداد كل من `gateway.auth.token` و`gateway.auth.password` وكان `gateway.auth.mode` غير معيّن، يحظر configure تثبيت الخفي حتى يتم تعيين الوضع صراحة.


## أمثلة

bashCopy code
[code]
    openclaw configureopenclaw configure --section webopenclaw configure --section model --section channelsopenclaw configure --section gateway --section daemon
[/code]

## ذات صلة

  * [مرجع CLI](</ar/cli>)
  * [الإعداد](</ar/gateway/configuration>)


Was this useful?YesNo