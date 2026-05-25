---
title: تحليل موقع القناة
source_url: https://docs.openclaw.ai/ar/channels/location
scraped_at: 2026-05-25
---

يقوم OpenClaw بتوحيد المواقع المشتركة الواردة من قنوات الدردشة إلى:

  * نص موجز للإحداثيات يُلحَق بنص الرسالة الواردة، و
  * حقول منظَّمة في حمولة سياق الرد التلقائي. يتم عرض التسميات والعناوين والتعليقات/الأوصاف التي توفرها القناة داخل المطالبة عبر كتلة JSON مشتركة للبيانات الوصفية غير الموثوقة، وليس بشكل مضمَّن داخل نص المستخدم.


المدعوم حاليًا:

  * **Telegram** (دبابيس المواقع + الأماكن + المواقع المباشرة)
  * **WhatsApp** (`locationMessage` \+ `liveLocationMessage`)
  * **Matrix** (`m.location` مع `geo_uri`)


## تنسيق النص

تُعرَض المواقع كسطور واضحة من دون أقواس:

  * دبوس: 
    * `📍 48.858844, 2.294351 ±12m`
  * مكان مُسمّى: 
    * `📍 48.858844, 2.294351 ±12m`
  * مشاركة مباشرة: 
    * `🛰 الموقع المباشر: 48.858844, 2.294351 ±12m`


إذا تضمنت القناة تسمية أو عنوانًا أو تعليقًا/وصفًا، فسيتم الاحتفاظ به في حمولة السياق وسيظهر في المطالبة على شكل JSON غير موثوق داخل كتلة مسوَّرة:

textCopy code
[code]
    الموقع (بيانات وصفية غير موثوقة):```json{  "latitude": 48.858844,  "longitude": 2.294351,  "name": "Eiffel Tower",  "address": "Champ de Mars, Paris",  "caption": "Meet here"}```
[/code]

## حقول السياق

عند وجود موقع، تتم إضافة هذه الحقول إلى `ctx`:

  * `LocationLat` (رقم)
  * `LocationLon` (رقم)
  * `LocationAccuracy` (رقم، بالأمتار؛ اختياري)
  * `LocationName` (سلسلة نصية؛ اختياري)
  * `LocationAddress` (سلسلة نصية؛ اختياري)
  * `LocationSource` (`pin | place | live`)
  * `LocationIsLive` (قيمة منطقية)
  * `LocationCaption` (سلسلة نصية؛ اختياري)


يتعامل عارض المطالبة مع `LocationName` و`LocationAddress` و`LocationCaption` على أنها بيانات وصفية غير موثوقة ويحوّلها إلى JSON عبر نفس المسار المقيّد المستخدم لسياقات القنوات الأخرى.

## ملاحظات القناة

  * **Telegram** : تُربَط الأماكن بالقيمتين `LocationName/LocationAddress`؛ وتستخدم المواقع المباشرة `live_period`.
  * **WhatsApp** : تملأ `locationMessage.comment` و`liveLocationMessage.caption` الحقل `LocationCaption`.
  * **Matrix** : يتم تحليل `geo_uri` كموقع دبوس؛ ويتم تجاهل الارتفاع وتكون `LocationIsLive` دائمًا false.


## ذو صلة

  * [أمر الموقع (العُقد)](</ar/nodes/location-command>)
  * [التقاط الكاميرا](</ar/nodes/camera>)
  * [فهم الوسائط](</ar/nodes/media-understanding>)


Was this useful?YesNo