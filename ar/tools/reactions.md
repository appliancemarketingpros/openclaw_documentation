---
title: التفاعلات
source_url: https://docs.openclaw.ai/ar/tools/reactions
scraped_at: 2026-05-25
---

يمكن للوكيل إضافة تفاعلات emoji وإزالتها على الرسائل باستخدام أداة `message` مع الإجراء `react`. يختلف سلوك التفاعلات حسب القناة ووسيلة النقل.

## آلية العمل

jsonCopy code
[code]
    {  "action": "react",  "messageId": "msg-123",  "emoji": "thumbsup"}
[/code]

  * يكون `emoji` مطلوبًا عند إضافة تفاعل.
  * عيّن `emoji` إلى سلسلة فارغة (`""`) لإزالة تفاعل/تفاعلات البوت.
  * عيّن `remove: true` لإزالة emoji محدد (يتطلب `emoji` غير فارغ).
  * في القنوات التي تدعم تفاعلات الحالة، يتيح `trackToolCalls: true` على التفاعل لبيئة التشغيل استخدام تلك الرسالة المتفاعَل معها لتفاعلات تقدم الأدوات اللاحقة أثناء الدور نفسه.


## سلوك القنوات

Discord و Slack

  * يزيل `emoji` الفارغ كل تفاعلات البوت على الرسالة.
  * يزيل `remove: true` فقط emoji المحدد.

Google Chat

  * يزيل `emoji` الفارغ تفاعلات التطبيق على الرسالة.
  * يزيل `remove: true` فقط emoji المحدد.

Telegram

  * يزيل `emoji` الفارغ تفاعلات البوت.
  * يزيل `remove: true` التفاعلات أيضًا لكنه لا يزال يتطلب `emoji` غير فارغ للتحقق من صحة الأداة.

WhatsApp

  * يزيل `emoji` الفارغ تفاعل البوت.
  * يُطابَق `remove: true` مع emoji فارغ داخليًا (ولا يزال يتطلب `emoji` في استدعاء الأداة).

Zalo Personal (zalouser)

  * يتطلب `emoji` غير فارغ.
  * يزيل `remove: true` تفاعل emoji المحدد ذلك.

Feishu/Lark

  * استخدم أداة `feishu_reaction` مع الإجراءات `add` و`remove` و`list`.
  * تتطلب الإضافة/الإزالة `emoji_type`؛ وتتطلب الإزالة أيضًا `reaction_id`.

Signal

  * يتم التحكم في إشعارات التفاعلات الواردة بواسطة `channels.signal.reactionNotifications`: يعطلها `"off"`، ويصدر `"own"` (الافتراضي) أحداثًا عندما يتفاعل المستخدمون مع رسائل البوت، ويصدر `"all"` أحداثًا لكل التفاعلات.

iMessage

  * تكون التفاعلات الصادرة عبارة عن tapbacks في iMessage (`love` و`like` و`dislike` و`laugh` و`emphasize` و`question`).
  * يتم التحكم في إشعارات tapback الواردة بواسطة `channels.imessage.reactionNotifications`: يعطلها `"off"`، ويصدر `"own"` (الافتراضي) أحداثًا عندما يتفاعل المستخدمون مع الرسائل التي كتبها البوت، ويصدر `"all"` أحداثًا لكل tapbacks من المرسلين المصرح لهم.


## مستوى التفاعل

يتحكم إعداد `reactionLevel` لكل قناة في مدى استخدام الوكيل للتفاعلات. تكون القيم عادةً `off` أو `ack` أو `minimal` أو `extensive`.

  * [Telegram reactionLevel](</ar/channels/telegram#reaction-notifications>) — `channels.telegram.reactionLevel`
  * [WhatsApp reactionLevel](</ar/channels/whatsapp#reaction-level>) — `channels.whatsapp.reactionLevel`


عيّن `reactionLevel` على القنوات الفردية لضبط مدى نشاط تفاعل الوكيل مع الرسائل على كل منصة.

## ذو صلة

  * [إرسال الوكيل](</ar/tools/agent-send>) — أداة `message` التي تتضمن `react`
  * [القنوات](</ar/channels>) — إعداد خاص بكل قناة


Was this useful?YesNo