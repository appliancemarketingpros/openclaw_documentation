---
title: OpenClaw
source_url: https://docs.openclaw.ai/ar
scraped_at: 2026-05-25
---

# OpenClaw 🦞

![OpenClaw](/assets/openclaw-logo-text-dark.png) ![OpenClaw](/assets/openclaw-logo-text.png)

> _"قَشِّر! قَشِّر!"_ — سرطان فضائي، على الأرجح

**Gateway يعمل على أي نظام تشغيل لوكلاء الذكاء الاصطناعي عبر Discord وGoogle Chat وiMessage وMatrix وMicrosoft Teams وSignal وSlack وTelegram وWhatsApp وZalo والمزيد.**

أرسل رسالة، واحصل على رد من الوكيل من جيبك. شغّل Gateway واحدًا عبر القنوات المدمجة وPlugins القنوات المرفقة وWebChat وعُقد الهواتف المحمولة.

[**ابدأ** ثبّت OpenClaw وشغّل Gateway خلال دقائق. ](</ar/start/getting-started>) [**تشغيل الإعداد الأولي** إعداد موجّه باستخدام `openclaw onboard` وتدفقات الاقتران. ](</ar/start/wizard>) [**فتح واجهة التحكم** شغّل لوحة معلومات المتصفح للدردشة والإعدادات والجلسات. ](</ar/web/control-ui>)

## ما هو OpenClaw؟

OpenClaw هو **Gateway ذاتي الاستضافة** يربط تطبيقات الدردشة وأسطح القنوات المفضلة لديك — القنوات المدمجة بالإضافة إلى Plugins قنوات مرفقة أو خارجية مثل Discord وGoogle Chat وiMessage وMatrix وMicrosoft Teams وSignal وSlack وTelegram وWhatsApp وZalo والمزيد — بوكلاء البرمجة بالذكاء الاصطناعي مثل Pi. تشغّل عملية Gateway واحدة على جهازك الخاص (أو خادم)، لتصبح الجسر بين تطبيقات المراسلة لديك ومساعد ذكاء اصطناعي متاح دائمًا.

**لمن هو؟** للمطورين والمستخدمين المتقدمين الذين يريدون مساعد ذكاء اصطناعي شخصيًا يمكنهم مراسلته من أي مكان — من دون التخلي عن التحكم في بياناتهم أو الاعتماد على خدمة مستضافة.

**ما الذي يجعله مختلفًا؟**

  * **ذاتي الاستضافة** : يعمل على عتادك وبقواعدك
  * **متعدد القنوات** : يخدم Gateway واحد القنوات المدمجة بالإضافة إلى Plugins قنوات مرفقة أو خارجية في الوقت نفسه
  * **مصمم للوكلاء** : مبني لوكلاء البرمجة مع استخدام الأدوات والجلسات والذاكرة والتوجيه متعدد الوكلاء
  * **مفتوح المصدر** : مرخص بموجب MIT وتقوده المساهمة المجتمعية


**ماذا تحتاج؟** Node 24 (موصى به)، أو Node 22 LTS (`22.16+`) للتوافق، ومفتاح API من المزوّد الذي تختاره، و5 دقائق. للحصول على أفضل جودة وأمان، استخدم أقوى نموذج متاح من أحدث جيل.

## كيف يعمل
[code] 
    flowchart LR
      A["Chat apps + plugins"] --> B["Gateway"]
      B --> C["Pi agent"]
      B --> D["CLI"]
      B --> E["Web Control UI"]
      B --> F["macOS app"]
      B --> G["iOS and Android nodes"]
[/code]

Gateway هو مصدر الحقيقة الوحيد للجلسات والتوجيه واتصالات القنوات.

## القدرات الرئيسية

[**Gateway متعدد القنوات** Discord وiMessage وSignal وSlack وTelegram وWhatsApp وWebChat والمزيد عبر عملية Gateway واحدة. ](</ar/channels>) [**قنوات Plugin** تضيف Plugins المرفقة Matrix وNostr وTwitch وZalo والمزيد في الإصدارات الحالية العادية. ](</ar/tools/plugin>) [**توجيه متعدد الوكلاء** جلسات معزولة لكل وكيل أو مساحة عمل أو مُرسل. ](</ar/concepts/multi-agent>) [**دعم الوسائط** أرسل واستقبل الصور والصوت والمستندات. ](</ar/nodes/images>) [**واجهة التحكم في الويب** لوحة معلومات في المتصفح للدردشة والإعدادات والجلسات والعُقد. ](</ar/web/control-ui>) [**عُقد الهواتف المحمولة** اقترن بعُقد iOS وAndroid لتدفقات العمل المعتمدة على Canvas والكاميرا والصوت. ](</ar/nodes>)

## البدء السريع

* ### ثبّت OpenClaw

bashCopy code
[code]
    npm install -g openclaw@latest
[/code]

* ### ابدأ الإعداد وثبّت الخدمة

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

* ### ابدأ الدردشة

افتح واجهة التحكم في المتصفح وأرسل رسالة:

bashCopy code
[code]
    openclaw dashboard
[/code]

أو صِل قناة ([Telegram](</ar/channels/telegram>) هو الأسرع) ودردش من هاتفك.

هل تحتاج إلى الإعداد الكامل للتثبيت والتطوير؟ راجع [البدء](</ar/start/getting-started>).

## لوحة المعلومات

افتح واجهة التحكم في المتصفح بعد بدء Gateway.

  * الافتراضي المحلي: <http://127.0.0.1:18789/>
  * الوصول عن بُعد: [أسطح الويب](</ar/web>) و[Tailscale](</ar/gateway/tailscale>)


![OpenClaw](/whatsapp-openclaw.jpg)

## الإعدادات (اختياري)

توجد الإعدادات في `~/.openclaw/openclaw.json`.

  * إذا **لم تفعل شيئًا** ، يستخدم OpenClaw ملف Pi الثنائي المرفق في وضع RPC مع جلسات لكل مُرسل.
  * إذا أردت تقييده، فابدأ بـ `channels.whatsapp.allowFrom` وقواعد الإشارة (للمجموعات).


مثال:

json5Copy code
[code]
    {  channels: {    whatsapp: {      allowFrom: ["+15555550123"],      groups: { "*": { requireMention: true } },    },  },  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },}
[/code]

## ابدأ من هنا

[**مراكز الوثائق** جميع الوثائق والأدلة، منظمة حسب حالة الاستخدام. ](</ar/start/hubs>) [**الإعدادات** إعدادات Gateway الأساسية والرموز وإعدادات المزوّد. ](</ar/gateway/configuration>) [**الوصول عن بُعد** أنماط الوصول عبر SSH وtailnet. ](</ar/gateway/remote>) [**القنوات** إعداد خاص بالقنوات لـ Feishu وMicrosoft Teams وWhatsApp وTelegram وDiscord والمزيد. ](</ar/channels/telegram>) [**العُقد** عُقد iOS وAndroid مع الاقتران وCanvas والكاميرا وإجراءات الجهاز. ](</ar/nodes>) [**المساعدة** نقطة دخول للإصلاحات الشائعة واستكشاف الأخطاء وإصلاحها. ](</ar/help>)

## تعلّم المزيد

[**قائمة الميزات الكاملة** قدرات القنوات والتوجيه والوسائط الكاملة. ](</ar/concepts/features>) [**توجيه متعدد الوكلاء** عزل مساحات العمل والجلسات لكل وكيل. ](</ar/concepts/multi-agent>) [**الأمان** الرموز وقوائم السماح وعناصر التحكم في السلامة. ](</ar/gateway/security>) [**استكشاف الأخطاء وإصلاحها** تشخيص Gateway والأخطاء الشائعة. ](</ar/gateway/troubleshooting>) [**نبذة وشكر** أصول المشروع والمساهمون والترخيص. ](</ar/reference/credits>)

Was this useful?YesNo