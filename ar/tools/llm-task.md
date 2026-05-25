---
title: مهمة نموذج اللغة الكبير
source_url: https://docs.openclaw.ai/ar/tools/llm-task
scraped_at: 2026-05-25
---

`llm-task` هي **أداة Plugin اختيارية** تشغّل مهمة LLM بصيغة JSON فقط وتُرجع مخرجات منظّمة (مع التحقق اختياريًا مقابل JSON Schema).

هذا مثالي لمحركات سير العمل مثل Lobster: يمكنك إضافة خطوة LLM واحدة بدون كتابة كود OpenClaw مخصص لكل سير عمل.

## تفعيل الـ Plugin

  1. فعّل الـ Plugin:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": { "enabled": true }    }  }}
[/code]

  2. اسمح بالأداة الاختيارية:

jsonCopy code
[code]
    {  "tools": {    "alsoAllow": ["llm-task"]  }}
[/code]

استخدم `tools.allow` فقط عندما تريد وضع قائمة السماح المقيّدة.

## الإعدادات (اختيارية)

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": {        "enabled": true,        "config": {          "defaultProvider": "openai-codex",          "defaultModel": "gpt-5.5",          "defaultAuthProfileId": "main",          "allowedModels": ["openai/gpt-5.4"],          "maxTokens": 800,          "timeoutMs": 30000        }      }    }  }}
[/code]

`allowedModels` هي قائمة سماح لسلاسل `provider/model`. إذا ضُبطت، فسيُرفض أي طلب خارج القائمة.

## معلمات الأداة

  * `prompt` (سلسلة، مطلوب)
  * `input` (أي نوع، اختياري)
  * `schema` (كائن، JSON Schema اختياري)
  * `provider` (سلسلة، اختياري)
  * `model` (سلسلة، اختياري)
  * `thinking` (سلسلة، اختياري)
  * `authProfileId` (سلسلة، اختياري)
  * `temperature` (رقم، اختياري)
  * `maxTokens` (رقم، اختياري)
  * `timeoutMs` (رقم، اختياري)


يقبل `thinking` إعدادات الاستدلال القياسية في OpenClaw، مثل `low` أو `medium`.

## المخرجات

يُرجع `details.json` يحتوي على JSON المحلّل (ويتحقق منه مقابل `schema` عند توفيره).

## مثال: خطوة سير عمل Lobster

### قيد مهم

يفترض المثال أدناه أن **Lobster CLI المستقل** يعمل في بيئة يكون فيها `openclaw.invoke` لديه بالفعل عنوان URL الصحيح للـ Gateway وسياق المصادقة الصحيح.

بالنسبة إلى مشغّل Lobster **المضمن** داخل OpenClaw، فإن نمط CLI المتداخل هذا **ليس موثوقًا به حاليًا** :

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{ ... }'
[/code]

إلى أن يتوفر في Lobster المضمن جسر مدعوم لهذا التدفق، فضّل إما:

  * استدعاءات أداة `llm-task` مباشرة خارج Lobster، أو
  * خطوات Lobster التي لا تعتمد على استدعاءات `openclaw.invoke` المتداخلة.


مثال Lobster CLI المستقل:

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{  "prompt": "Given the input email, return intent and draft.",  "thinking": "low",  "input": {    "subject": "Hello",    "body": "Can you help?"  },  "schema": {    "type": "object",    "properties": {      "intent": { "type": "string" },      "draft": { "type": "string" }    },    "required": ["intent", "draft"],    "additionalProperties": false  }}'
[/code]

## ملاحظات السلامة

  * الأداة **تعتمد JSON فقط** وتوجّه النموذج لإخراج JSON فقط (بدون أسوار كود، وبدون تعليقات).
  * لا تُعرَض أي أدوات للنموذج في هذا التشغيل.
  * تعامل مع المخرجات على أنها غير موثوقة ما لم تتحقق منها باستخدام `schema`.
  * ضع الموافقات قبل أي خطوة ذات آثار جانبية (إرسال، نشر، تنفيذ).


## ذات صلة

  * [مستويات التفكير](</ar/tools/thinking>)
  * [الوكلاء الفرعيون](</ar/tools/subagents>)
  * [أوامر الشرطة المائلة](</ar/tools/slash-commands>)


Was this useful?YesNo