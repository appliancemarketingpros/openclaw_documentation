---
title: مؤشرات الكتابة
source_url: https://docs.openclaw.ai/ar/concepts/typing-indicators
scraped_at: 2026-05-25
---

تُرسل مؤشرات الكتابة إلى قناة الدردشة أثناء نشاط التشغيل. استخدم `agents.defaults.typingMode` للتحكم في **وقت** بدء الكتابة و`typingIntervalSeconds` للتحكم في **مدى تكرار** تحديثها.

## الإعدادات الافتراضية

عندما يكون `agents.defaults.typingMode` **غير معيّن** ، يحافظ OpenClaw على السلوك القديم:

  * **الدردشات المباشرة** : تبدأ الكتابة فور بدء حلقة النموذج.
  * **دردشات المجموعة مع إشارة** : تبدأ الكتابة فورًا.
  * **دردشات المجموعة بدون إشارة** : تبدأ الكتابة فقط عند بدء تدفق نص الرسالة.
  * **تشغيلات Heartbeat** : تبدأ الكتابة عندما يبدأ تشغيل Heartbeat إذا كان هدف Heartbeat الذي تم حله دردشة تدعم الكتابة ولم تكن الكتابة معطلة.


## الأوضاع

عيّن `agents.defaults.typingMode` إلى أحد الخيارات التالية:

  * `never` \- لا يوجد مؤشر كتابة، أبدًا.
  * `instant` \- ابدأ الكتابة **بمجرد أن تبدأ حلقة النموذج** ، حتى إذا كان التشغيل يعيد لاحقًا رمز الرد الصامت فقط.
  * `thinking` \- ابدأ الكتابة عند **أول فرق استدلال** (يتطلب `reasoningLevel: "stream"` للتشغيل).
  * `message` \- ابدأ الكتابة عند **أول فرق نصي غير صامت** (يتجاهل رمز الصمت `NO_REPLY`).


ترتيب "مدى تبكير تشغيله": `never` → `message` → `thinking` → `instant`

## التكوين

عيّن الإعداد الافتراضي على مستوى الوكيل:

json5Copy code
[code]
    {  agents: {    defaults: {      typingMode: "thinking",      typingIntervalSeconds: 6,    },  },}
[/code]

تجاوز الوضع أو الإيقاع لكل جلسة:

json5Copy code
[code]
    {  session: {    typingMode: "message",    typingIntervalSeconds: 4,  },}
[/code]

## ملاحظات

  * لن يعرض وضع `message` الكتابة للردود الصامتة فقط عندما تكون الحمولة كلها رمز الصمت الدقيق (على سبيل المثال `NO_REPLY` / `no_reply`، مع مطابقة غير حساسة لحالة الأحرف).
  * لا يعمل `thinking` إلا إذا كان التشغيل يبث الاستدلال (`reasoningLevel: "stream"`). إذا لم يصدر النموذج فروق استدلال، فلن تبدأ الكتابة.
  * كتابة Heartbeat هي إشارة حيوية لهدف التسليم الذي تم حله. تبدأ عند بدء تشغيل Heartbeat بدلًا من اتباع توقيت تدفق `message` أو `thinking`. عيّن `typingMode: "never"` لتعطيلها.
  * لا تعرض Heartbeats الكتابة عندما يكون `target: "none"`، أو عندما يتعذر حل الهدف، أو عندما يكون تسليم الدردشة معطلًا لـ Heartbeat، أو عندما لا تدعم القناة الكتابة.
  * يتحكم `typingIntervalSeconds` في **إيقاع التحديث** ، وليس وقت البدء. القيمة الافتراضية هي 6 ثوانٍ.


## ذو صلة

[**Presence** كيف يتتبع Gateway العملاء المتصلين ويعرضهم في علامة تبويب مثيلات macOS. ](</ar/concepts/presence>) [**Streaming and chunking** سلوك البث الصادر، وحدود الأجزاء، والتسليم الخاص بكل قناة. ](</ar/concepts/streaming>)

Was this useful?YesNo