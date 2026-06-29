---
title: واجهة API الصادرة للقناة
source_url: https://docs.openclaw.ai/ar/plugins/sdk-channel-outbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

ينبغي أن تكشف Plugins القنوات سلوك الرسائل الصادرة من `openclaw/plugin-sdk/channel-outbound`. استخدم `openclaw/plugin-sdk/channel-inbound` لتنسيق الاستلام/السياق/الإرسال.

يمتلك القلب الطوابير، والمتانة، وسياسة إعادة المحاولة العامة، والخطافات، والإيصالات، وأداة `message` المشتركة. ويمتلك Plugin استدعاءات الإرسال/التحرير/الحذف الأصلية، وتطبيع الهدف، وترابط المنصة، والاقتباسات المحددة، وعلامات الإشعارات، وحالة الحساب، والآثار الجانبية الخاصة بالمنصة.

## المحوّل

تعرّف معظم Plugins محوّل `message` واحدًا:

tsCopy code
[code]
       defineChannelMessageAdapter,  createMessageReceiptFromOutboundResults,} from "openclaw/plugin-sdk/channel-outbound"; export const demoMessageAdapter = defineChannelMessageAdapter({  id: "demo",  durableFinal: {    capabilities: {      text: true,      replyTo: true,      thread: true,      messageSendingHooks: true,    },  },  send: {    text: async ({ cfg, to, text, accountId, replyToId, threadId, signal }) => {      const sent = await sendDemoMessage({        cfg,        to,        text,        accountId: accountId ?? undefined,        replyToId: replyToId ?? undefined,        threadId: threadId == null ? undefined : String(threadId),        signal,      });       return {        receipt: createMessageReceiptFromOutboundResults({          results: [{ channel: "demo", messageId: sent.id, conversationId: to }],          kind: "text",          threadId: threadId == null ? undefined : String(threadId),          replyToId: replyToId ?? undefined,        }),      };    },  },});
[/code]

أعلن فقط عن الإمكانات التي يحافظ عليها النقل الأصلي فعليًا. غطِّ كل إمكانية معلنة للإرسال، والإيصال، والمعاينة المباشرة، وإقرار الاستلام باستخدام مساعدات العقد المصدّرة من هذا المسار الفرعي.

## محوّلات الصادر الحالية

إذا كانت القناة تملك بالفعل محوّل `outbound` متوافقًا، فاشتق محوّل الرسائل بدلًا من تكرار كود الإرسال:

tsCopy code
[code]
     export const messageAdapter = createChannelMessageAdapterFromOutbound({  id: "demo",  outbound,  durableFinal: {    capabilities: {      text: true,      media: true,    },  },});
[/code]

## الإرسال المتين

توجد مساعدات الإرسال في وقت التشغيل أيضًا على `channel-outbound`:

  * `sendDurableMessageBatch(...)`
  * `withDurableMessageSendContext(...)`
  * `deliverInboundReplyWithMessageSendContext(...)`
  * مساعدات بث/تقدم المسودات مثل `resolveChannelDraftStreamingChunking(...)`


يعيد `sendDurableMessageBatch(...)` نتيجة صريحة واحدة:

  * `sent`: تم تسليم رسالة منصة مرئية واحدة على الأقل.
  * `suppressed`: لا ينبغي التعامل مع غياب أي رسالة منصة على أنه مفقود.
  * `partial_failed`: تم تسليم رسالة منصة واحدة على الأقل قبل فشل حمولة لاحقة أو أثر جانبي لاحق.
  * `failed`: لم يُنتَج أي إيصال منصة.


استخدم `payloadOutcomes` عندما تخلط الدفعة بين حمولات مرسلة ومكبوتة وفاشلة. لا تستنتج إلغاء الخطاف من نتيجة تسليم مباشر قديمة فارغة.

## إرسال التوافق

ينبغي تجميع إرسال الردود الواردة عبر `dispatchChannelInboundReply(...)` من `channel-inbound`. أبقِ تسليم المنصة في محوّل التسليم؛ واستخدم `channel-outbound` لمحوّلات الرسائل، والإرسال المتين، والإيصالات، والمعاينة المباشرة، وخيارات مسار الرد.

Was this useful?YesNo

Open issue