---
title: واجهة API الواردة للقناة
source_url: https://docs.openclaw.ai/ar/plugins/sdk-channel-inbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

ينبغي أن تمثل Plugins القنوات مسارات الاستقبال باستخدام أسماء inbound وmessage:

textCopy code
[code]
    platform event -> inbound facts/context -> agent reply -> message delivery
[/code]

استخدم `openclaw/plugin-sdk/channel-inbound` لتطبيع أحداث inbound، والتنسيق، والجذور، والتنسيق التشغيلي. استخدم `openclaw/plugin-sdk/channel-outbound` لسلوك الإرسال الأصلي، والإيصال، والتسليم الدائم، والمعاينة المباشرة.

## المساعدات الأساسية

tsCopy code
[code]
       buildChannelInboundEventContext,  runChannelInboundEvent,  dispatchChannelInboundReply,} from "openclaw/plugin-sdk/channel-inbound";
[/code]

  * `buildChannelInboundEventContext(...)`: إسقاط حقائق القناة المطبعة في سياق الموجه/الجلسة. استخدم `channelContext` لتمرير بيانات تعريف المرسل/الدردشة المملوكة للقناة إلى hook الـ Plugin `ctx.channelContext`؛ ووسّع `PluginHookChannelSenderContext` أو `PluginHookChannelChatContext` من هذا المسار الفرعي للحقول الخاصة بالقناة.
  * `runChannelInboundEvent(...)`: تشغيل الإدخال، والتصنيف، والتحقق المسبق، والحل، والتسجيل، والإرسال، والإنهاء لحدث منصة inbound واحد.
  * `dispatchChannelInboundReply(...)`: تسجيل وإرسال رد inbound مجمّع مسبقًا باستخدام محول تسليم.


يعرض runtime الـ Plugin المحقون المساعدات عالية المستوى نفسها ضمن `runtime.channel.inbound.*` للقنوات المضمنة/الأصلية التي تتلقى كائن runtime بالفعل.

tsCopy code
[code]
    await runtime.channel.inbound.run({  channel: "demo",  accountId,  raw: platformEvent,  adapter: {    ingest: normalizePlatformEvent,    resolveTurn: resolveInboundReply,  },});
[/code]

ينبغي أن تجمع مرسلات التوافق مدخلات `dispatchChannelInboundReply(...)` وتُبقي تسليم المنصة داخل محول التسليم. ينبغي أن تفضّل مسارات الإرسال الجديدة محولات الرسائل ومساعدات الرسائل الدائمة.

## الترحيل

أزيلت أسماء runtime المستعارة القديمة `runtime.channel.turn.*`. استخدم:

  * `runtime.channel.inbound.run(...)` لأحداث inbound الخام.
  * `runtime.channel.inbound.dispatchReply(...)` لسياقات الردود المجمّعة.
  * `runtime.channel.inbound.buildContext(...)` لحمولات سياق inbound.
  * `runtime.channel.inbound.runPreparedReply(...)` فقط لمسارات الإرسال المجهزة المملوكة للقناة التي تجمع مسبقًا closure الإرسال الخاص بها.


ينبغي ألا يقدم كود Plugin الجديد واجهات API للقنوات مسماة باسم `turn`. أبقِ مفردات model أو turn الخاصة بالوكيل داخل كود الوكيل/الموفر؛ تستخدم Plugins القنوات مصطلحات inbound، والرسالة، والتسليم، والرد.

Was this useful?YesNo

Open issue