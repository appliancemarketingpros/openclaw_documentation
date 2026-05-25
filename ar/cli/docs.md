---
title: المستندات
source_url: https://docs.openclaw.ai/ar/cli/docs
scraped_at: 2026-05-25
---

# `openclaw docs`

ابحث في فهرس وثائق OpenClaw الحية من الطرفية. يستدعي الأمر نقطة نهاية بحث MCP العامة لوثائق Mintlify المستضافة على `https://docs.openclaw.ai/mcp.SearchOpenClaw` ويعرض النتائج في الطرفية لديك.

## الاستخدام

bashCopy code
[code]
    openclaw docs                       # print docs entrypoint and example searchopenclaw docs <query...>            # search the live docs index
[/code]

الوسائط:

الوسيط | الوصف  
---|---  
`[query...]` | استعلام بحث حر الصياغة. تُدمج الاستعلامات متعددة الكلمات بمسافات وتُرسل كاستعلام واحد.  
  
## أمثلة

bashCopy code
[code]
    openclaw docs browser existing-sessionopenclaw docs sandbox allowHostControlopenclaw docs gateway token secretref
[/code]

من دون استعلام، يطبع `openclaw docs` عنوان URL لنقطة دخول الوثائق بالإضافة إلى أمر بحث نموذجي بدلاً من تشغيل بحث.

## آلية العمل

يستدعي `openclaw docs` أداة CLI المسماة `mcporter` لاستدعاء أداة بحث MCP في الوثائق، ثم يحلل كتل `Title: / Link: / Content:` من خرج الأداة إلى قائمة نتائج.

لحل `mcporter`، يتحقق OpenClaw بالترتيب:

  1. `mcporter` على `PATH` (يُستخدم مباشرة إذا كان موجوداً).
  2. `pnpm dlx mcporter ...` إذا كان `pnpm` مثبتاً.
  3. `npx -y mcporter ...` إذا كان `npx` مثبتاً.


إذا لم يكن أي منها متاحاً، يفشل الأمر مع تلميح لتثبيت `pnpm` (`npm install -g pnpm`).

تستخدم مكالمة البحث مهلة ثابتة قدرها 30 ثانية. تُختصر مقتطفات النتائج إلى نحو 220 حرفاً لكل إدخال.

## الخرج

في طرفية غنية (TTY)، تُعرض النتائج كعنوان يليه تعداد نقطي. تعرض كل نقطة عنوان الصفحة، وعنوان URL المرتبط للوثائق، ومقتطفاً قصيراً في السطر التالي. تطبع النتائج الفارغة "لا توجد نتائج.".

في الخرج غير الغني (عند التوجيه عبر الأنابيب، أو `--no-color`، أو السكربتات)، تُعرض البيانات نفسها بصيغة Markdown:

markdownCopy code
[code]
    # Docs search: <query> - [Title](https://docs.openclaw.ai/...) - snippet- [Title](https://docs.openclaw.ai/...) - snippet
[/code]

## رموز الخروج

الرمز | المعنى  
---|---  
`0` | نجح البحث (بما في ذلك الاستجابات ذات النتائج الصفرية).  
`1` | فشلت مكالمة أداة MCP؛ يُطبع stderr ضمن السطر.  
  
## ذو صلة

  * [مرجع CLI](</ar/cli>)
  * [الوثائق الحية](<https://docs.openclaw.ai>)


Was this useful?YesNo