---
title: تنفيذ التعليمات البرمجية
source_url: https://docs.openclaw.ai/ar/tools/code-execution
scraped_at: 2026-05-25
---

`code_execution` يشغّل تحليل Python عن بُعد داخل صندوق حماية على واجهة Responses API الخاصة بـ xAI. يتم تسجيله بواسطة Plugin `xai` المضمّن (ضمن عقد `tools`) ويوجّه الطلبات إلى نقطة النهاية نفسها `https://api.x.ai/v1/responses` التي يستخدمها `x_search`.

الخاصية | القيمة  
---|---  
اسم الأداة | `code_execution`  
Plugin المزوّد | `xai` (مضمّن، `enabledByDefault: true`)  
المصادقة | ملف تعريف مصادقة xAI، أو `XAI_API_KEY`، أو `plugins.entries.xai.config.webSearch.apiKey`  
النموذج الافتراضي | `grok-4-1-fast`  
المهلة الافتراضية | 30 ثانية  
`maxTurns` الافتراضي | غير مضبوط (تطبّق xAI حدّها الداخلي الخاص)  
  
يختلف هذا عن [`exec`](</ar/tools/exec>) المحلي:

  * يشغّل `exec` أوامر shell على جهازك أو Node مقترن.
  * يشغّل `code_execution` Python في صندوق الحماية البعيد الخاص بـ xAI.


استخدم `code_execution` من أجل:

  * الحسابات.
  * الجدولة.
  * الإحصاءات السريعة.
  * التحليل بنمط المخططات.
  * تحليل البيانات التي يُرجعها `x_search` أو `web_search`.


لا تستخدمه عندما تحتاج إلى ملفات محلية، أو shell الخاص بك، أو مستودعك، أو أجهزة مقترنة. استخدم [`exec`](</ar/tools/exec>) لذلك.

## الإعداد

* ### Provide an xAI API key

شغّل `openclaw onboard --auth-choice xai-api-key` من أجل `code_execution` و `x_search`، أو اضبط `XAI_API_KEY` / هيّئ المفتاح ضمن Plugin الخاص بـ xAI عندما تريد أيضًا أن يستخدم بحث الويب من Grok بيانات الاعتماد نفسها:

bashCopy code
[code]
    export XAI_API_KEY=xai-...
[/code]

أو عبر الإعدادات:

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          webSearch: {            apiKey: "xai-...",          },        },      },    },  },}
[/code]

* ### Enable and tune code_execution

الأداة محكومة بـ `plugins.entries.xai.config.codeExecution.enabled`. الافتراضي أنها معطّلة.

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast", // override the default xAI code-execution model            maxTurns: 2,            // optional cap on internal tool turns            timeoutSeconds: 30,     // request timeout (default: 30)          },        },      },    },  },}
[/code]

* ### Restart the Gateway

bashCopy code
[code]
    openclaw gateway restart
[/code]

يظهر `code_execution` في قائمة أدوات الوكيل بمجرد أن يعيد Plugin xAI التسجيل مع `enabled: true`.

## كيفية استخدامه

اطلب بشكل طبيعي واجعل نية التحليل صريحة:

textCopy code
[code]
    Use code_execution to calculate the 7-day moving average for these numbers: ...
[/code]

textCopy code
[code]
    Use x_search to find posts mentioning OpenClaw this week, then use code_execution to count them by day.
[/code]

textCopy code
[code]
    Use web_search to gather the latest AI benchmark numbers, then use code_execution to compare percent changes.
[/code]

تأخذ الأداة داخليًا وسيط `task` واحدًا، لذلك ينبغي للوكيل إرسال طلب التحليل الكامل وأي بيانات مضمنة في موجه واحد.

## الأخطاء

عندما تعمل الأداة من دون مصادقة، تُرجع خطأً منظّمًا من نوع `missing_xai_api_key` يشير إلى ملف تعريف المصادقة، ومتغير البيئة، وخيارات الإعدادات. الخطأ بصيغة JSON، وليس استثناءً مرميًا، لذلك يمكن للوكيل تصحيح نفسه:

jsonCopy code
[code]
    {  "error": "missing_xai_api_key",  "message": "code_execution needs an xAI API key. Run openclaw onboard --auth-choice xai-api-key, set XAI_API_KEY in the Gateway environment, or configure plugins.entries.xai.config.webSearch.apiKey.",  "docs": "https://docs.openclaw.ai/tools/code-execution"}
[/code]

## الحدود

  * هذا تنفيذ بعيد لدى xAI، وليس تنفيذ عملية محلية.
  * تعامل مع النتائج كتحليل مؤقت، لا كجلسة دفتر ملاحظات دائمة.
  * لا تفترض الوصول إلى الملفات المحلية أو مساحة العمل الخاصة بك.
  * للحصول على بيانات X حديثة، استخدم [`x_search`](</ar/tools/web#x_search>) أولًا ومرّر النتيجة إلى `code_execution`.


## ذو صلة

[**Exec tool** تنفيذ shell محلي على جهازك أو Node مقترن. ](</ar/tools/exec>) [**Exec approvals** سياسة السماح/الرفض لتنفيذ shell. ](</ar/tools/exec-approvals>) [**Web tools** `web_search` و`x_search` و`web_fetch`. ](</ar/tools/web>) [**xAI provider** نماذج Grok، وبحث الويب/X، وإعدادات تنفيذ الكود. ](</ar/providers/xai>)

Was this useful?YesNo