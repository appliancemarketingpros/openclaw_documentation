---
title: Gateway الذكاء الاصطناعي من Cloudflare
source_url: https://docs.openclaw.ai/ar/providers/cloudflare-ai-gateway
scraped_at: 2026-05-25
---

يقع Cloudflare AI Gateway أمام واجهات API للمزوّدين ويتيح لك إضافة التحليلات والتخزين المؤقت وعناصر التحكم. بالنسبة إلى Anthropic، يستخدم OpenClaw واجهة Anthropic Messages API عبر نقطة نهاية Gateway الخاصة بك.

الخاصية | القيمة  
---|---  
المزوّد | `cloudflare-ai-gateway`  
عنوان URL الأساسي | `https://gateway.ai.cloudflare.com/v1/<account_id>/<gateway_id>/anthropic`  
النموذج الافتراضي | `cloudflare-ai-gateway/claude-sonnet-4-6`  
مفتاح API | `CLOUDFLARE_AI_GATEWAY_API_KEY` (مفتاح API الخاص بالمزوّد لديك للطلبات عبر Gateway)  
  
عند تمكين التفكير لنماذج Anthropic Messages، يزيل OpenClaw أدوار الملء المسبق اللاحقة الخاصة بالمساعد قبل إرسال الحمولة عبر Cloudflare AI Gateway. ترفض Anthropic الملء المسبق للاستجابة مع التفكير الموسّع، بينما يظل الملء المسبق العادي من دون تفكير متاحًا.

## البدء

* ### عيّن مفتاح API للمزوّد وتفاصيل Gateway

شغّل الإعداد الأولي واختر خيار مصادقة Cloudflare AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice cloudflare-ai-gateway-api-key
[/code]

سيطلب ذلك معرّف الحساب ومعرّف Gateway ومفتاح API.

* ### عيّن نموذجًا افتراضيًا

أضف النموذج إلى إعدادات OpenClaw لديك:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cloudflare-ai-gateway/claude-sonnet-4-6" },    },  },}
[/code]

* ### تحقق من أن النموذج متاح

bashCopy code
[code]
    openclaw models list --provider cloudflare-ai-gateway
[/code]

## مثال غير تفاعلي

لإعدادات البرمجة النصية أو CI، مرّر كل القيم في سطر الأوامر:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY"
[/code]

## الإعدادات المتقدمة

Gateways مصادَق عليها

إذا فعّلت مصادقة Gateway في Cloudflare، فأضف ترويسة `cf-aig-authorization`. هذا **إضافةً إلى** مفتاح API الخاص بالمزوّد لديك.

json5Copy code
[code]
    {  models: {    providers: {      "cloudflare-ai-gateway": {        headers: {          "cf-aig-authorization": "Bearer <cloudflare-ai-gateway-token>",        },      },    },  },}
[/code]

ملاحظة عن البيئة

إذا كان Gateway يعمل كخدمة خفية (launchd/systemd)، فتأكد من أن `CLOUDFLARE_AI_GATEWAY_API_KEY` متاح لتلك العملية.

## ذات صلة

[**اختيار النموذج** اختيار المزوّدين ومراجع النماذج وسلوك تجاوز الفشل. ](</ar/concepts/model-providers>) [**استكشاف الأخطاء وإصلاحها** استكشاف الأخطاء وإصلاحها العام والأسئلة الشائعة. ](</ar/help/troubleshooting>)

Was this useful?YesNo