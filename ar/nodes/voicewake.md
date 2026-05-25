---
title: الإيقاظ الصوتي
source_url: https://docs.openclaw.ai/ar/nodes/voicewake
scraped_at: 2026-05-25
---

OpenClaw يتعامل مع **كلمات التنبيه كقائمة عامة واحدة** يملكها **Gateway**.

  * لا توجد **كلمات تنبيه مخصصة لكل عقدة**.
  * يمكن **لأي واجهة مستخدم لعقدة/تطبيق تعديل** القائمة؛ يحفظ Gateway التغييرات ويبثها للجميع.
  * يحتفظ macOS وiOS بمفاتيح تبديل محلية **لتفعيل/تعطيل التنبيه الصوتي** (تختلف تجربة المستخدم المحلية + الأذونات).
  * يحتفظ Android حاليًا بإيقاف التنبيه الصوتي ويستخدم تدفق ميكروفون يدويًا في علامة تبويب الصوت.


## التخزين (مضيف Gateway)

تُخزَّن كلمات التنبيه على جهاز Gateway في:

  * `~/.openclaw/settings/voicewake.json`


الشكل:

jsonCopy code
[code]
    { "triggers": ["openclaw", "claude", "computer"], "updatedAtMs": 1730000000000 }
[/code]

## البروتوكول

### الطرق

  * `voicewake.get` → `{ triggers: string[] }`
  * `voicewake.set` مع المعاملات `{ triggers: string[] }` → `{ triggers: string[] }`


ملاحظات:

  * تُطبَّع المشغلات (إزالة المسافات الزائدة، وإسقاط القيم الفارغة). تعود القوائم الفارغة إلى القيم الافتراضية.
  * تُفرض حدود للسلامة (حدود العدد/الطول).


### طرق التوجيه (المشغل → الهدف)

  * `voicewake.routing.get` → `{ config: VoiceWakeRoutingConfig }`
  * `voicewake.routing.set` مع المعاملات `{ config: VoiceWakeRoutingConfig }` → `{ config: VoiceWakeRoutingConfig }`


شكل `VoiceWakeRoutingConfig`:

jsonCopy code
[code]
    {  "version": 1,  "defaultTarget": { "mode": "current" },  "routes": [{ "trigger": "robot wake", "target": { "sessionKey": "agent:main:main" } }],  "updatedAtMs": 1730000000000}
[/code]

تدعم أهداف المسارات واحدًا فقط من الآتي:

  * `{ "mode": "current" }`
  * `{ "agentId": "main" }`
  * `{ "sessionKey": "agent:main:main" }`


### الأحداث

  * حمولة `voicewake.changed` هي `{ triggers: string[] }`
  * حمولة `voicewake.routing.changed` هي `{ config: VoiceWakeRoutingConfig }`


من يتلقاها:

  * جميع عملاء WebSocket (تطبيق macOS وWebChat وما إلى ذلك)
  * جميع العقد المتصلة (iOS/Android)، وكذلك عند اتصال العقدة كدفع أولي لـ"الحالة الحالية".


## سلوك العميل

### تطبيق macOS

  * يستخدم القائمة العامة للتحكم في مشغلات `VoiceWakeRuntime`.
  * تعديل "كلمات التشغيل" في إعدادات التنبيه الصوتي يستدعي `voicewake.set` ثم يعتمد على البث لإبقاء العملاء الآخرين متزامنين.


### عقدة iOS

  * تستخدم القائمة العامة لاكتشاف مشغلات `VoiceWakeManager`.
  * تعديل كلمات التنبيه في الإعدادات يستدعي `voicewake.set` (عبر Gateway WS) ويحافظ أيضًا على استجابة اكتشاف كلمات التنبيه المحلي.


### عقدة Android

  * التنبيه الصوتي معطل حاليًا في وقت تشغيل/إعدادات Android.
  * يستخدم صوت Android التقاط الميكروفون اليدوي في علامة تبويب الصوت بدلًا من مشغلات كلمات التنبيه.


## ذات صلة

  * [وضع التحدث](</ar/nodes/talk>)
  * [ملاحظات الصوت والصوتيات](</ar/nodes/audio>)
  * [فهم الوسائط](</ar/nodes/media-understanding>)


Was this useful?YesNo