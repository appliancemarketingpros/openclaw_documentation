---
title: بحث MiniMax
source_url: https://docs.openclaw.ai/ar/tools/minimax-search
scraped_at: 2026-05-25
---

يدعم OpenClaw مزوّد `web_search` من MiniMax عبر API البحث MiniMax Token Plan. يُرجع نتائج بحث منظّمة تتضمن العناوين وعناوين URL والمقتطفات والاستعلامات ذات الصلة.

## الحصول على اعتماد Token Plan

* ### إنشاء مفتاح

أنشئ مفتاح MiniMax Token Plan أو انسخه من [MiniMax Platform](<https://platform.minimax.io/user-center/basic-information/interface-key>). يمكن لإعدادات OAuth إعادة استخدام `MINIMAX_OAUTH_TOKEN` بدلاً من ذلك.

* ### تخزين المفتاح

عيّن `MINIMAX_CODE_PLAN_KEY` في بيئة Gateway، أو اضبطه عبر:

bashCopy code
[code]
    openclaw configure --section web
[/code]

يقبل OpenClaw أيضاً `MINIMAX_CODING_API_KEY` و`MINIMAX_OAUTH_TOKEN` و `MINIMAX_API_KEY` كأسماء مستعارة لمتغيرات البيئة. يجب أن يشير `MINIMAX_API_KEY` إلى اعتماد Token Plan مفعّل للبحث؛ قد لا تقبل نقطة نهاية بحث Token Plan مفاتيح API العادية لنماذج MiniMax.

## الإعدادات

json5Copy code
[code]
    {  plugins: {    entries: {      minimax: {        config: {          webSearch: {            apiKey: "sk-cp-...", // optional if a MiniMax Token Plan env var is set            region: "global", // or "cn"          },        },      },    },  },  tools: {    web: {      search: {        provider: "minimax",      },    },  },}
[/code]

**بديل البيئة:** عيّن `MINIMAX_CODE_PLAN_KEY` أو `MINIMAX_CODING_API_KEY` أو `MINIMAX_OAUTH_TOKEN` أو `MINIMAX_API_KEY` في بيئة Gateway. لتثبيت gateway، ضعه في `~/.openclaw/.env`.

## اختيار المنطقة

يستخدم بحث MiniMax نقاط النهاية هذه:

  * عالمي: `https://api.minimax.io/v1/coding_plan/search`
  * CN: `https://api.minimaxi.com/v1/coding_plan/search`


إذا لم يتم تعيين `plugins.entries.minimax.config.webSearch.region`، فإن OpenClaw يحل المنطقة بهذا الترتيب:

  1. `tools.web.search.minimax.region` / `webSearch.region` المملوك من Plugin
  2. `MINIMAX_API_HOST`
  3. `models.providers.minimax.baseUrl`
  4. `models.providers.minimax-portal.baseUrl`


يعني ذلك أن إعداد CN أو `MINIMAX_API_HOST=https://api.minimaxi.com/...` يبقي بحث MiniMax تلقائياً على مضيف CN أيضاً.

حتى عندما تصادق مع MiniMax عبر مسار OAuth `minimax-portal`، لا يزال بحث الويب يسجَّل بمعرّف المزوّد `minimax`؛ ويُستخدم عنوان URL الأساسي لمزوّد OAuth كتلميح منطقة لاختيار مضيف CN/العالمي، ويمكن لـ `MINIMAX_OAUTH_TOKEN` تلبية اعتماد الحامل لبحث MiniMax.

## المعاملات المدعومة

المعامل | النوع | القيود | الوصف  
---|---|---|---  
`query` | string | مطلوب | سلسلة استعلام البحث.  
`count` | integer | 1-10 | عدد النتائج المراد إرجاعها. يقلّص OpenClaw القائمة المُرجعة إلى هذا الحجم.  
  
المرشحات الخاصة بالمزوّد غير مدعومة حالياً.

## ذات صلة

  * [نظرة عامة على بحث الويب](</ar/tools/web>) \-- جميع المزوّدين والاكتشاف التلقائي
  * [MiniMax](</ar/providers/minimax>) \-- إعداد النماذج والصور والكلام والمصادقة


Was this useful?YesNo