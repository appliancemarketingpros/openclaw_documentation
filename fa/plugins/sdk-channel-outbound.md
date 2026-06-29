---
title: API خروجی کانال
source_url: https://docs.openclaw.ai/fa/plugins/sdk-channel-outbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

Pluginهای کانال باید رفتار پیام خروجی را از `openclaw/plugin-sdk/channel-outbound` ارائه کنند. برای هماهنگ‌سازی دریافت/زمینه/ارسال از `openclaw/plugin-sdk/channel-inbound` استفاده کنید.

هسته مالک صف‌بندی، پایداری، سیاست تلاش مجدد عمومی، hookها، رسیدها و ابزار مشترک `message` است. Plugin مالک فراخوانی‌های بومی ارسال/ویرایش/حذف، نرمال‌سازی مقصد، رشته‌بندی پلتفرم، نقل‌قول‌های انتخاب‌شده، پرچم‌های اعلان، وضعیت حساب و اثرات جانبی مخصوص پلتفرم است.

## آداپتور

بیشتر Pluginها یک آداپتور `message` تعریف می‌کنند:

tsCopy code
[code]
       defineChannelMessageAdapter,  createMessageReceiptFromOutboundResults,} from "openclaw/plugin-sdk/channel-outbound"; export const demoMessageAdapter = defineChannelMessageAdapter({  id: "demo",  durableFinal: {    capabilities: {      text: true,      replyTo: true,      thread: true,      messageSendingHooks: true,    },  },  send: {    text: async ({ cfg, to, text, accountId, replyToId, threadId, signal }) => {      const sent = await sendDemoMessage({        cfg,        to,        text,        accountId: accountId ?? undefined,        replyToId: replyToId ?? undefined,        threadId: threadId == null ? undefined : String(threadId),        signal,      });       return {        receipt: createMessageReceiptFromOutboundResults({          results: [{ channel: "demo", messageId: sent.id, conversationId: to }],          kind: "text",          threadId: threadId == null ? undefined : String(threadId),          replyToId: replyToId ?? undefined,        }),      };    },  },});
[/code]

فقط قابلیت‌هایی را اعلام کنید که انتقال بومی واقعا حفظ می‌کند. هر قابلیت اعلام‌شده برای ارسال، رسید، پیش‌نمایش زنده و تأیید دریافت را با کمک‌تابع‌های قرارداد صادرشده از این زیربخش پوشش دهید.

## آداپتورهای خروجی موجود

اگر کانال از قبل یک آداپتور سازگار `outbound` دارد، به‌جای تکرار کد ارسال، آداپتور پیام را از آن مشتق کنید:

tsCopy code
[code]
     export const messageAdapter = createChannelMessageAdapterFromOutbound({  id: "demo",  outbound,  durableFinal: {    capabilities: {      text: true,      media: true,    },  },});
[/code]

## ارسال‌های پایدار

کمک‌تابع‌های ارسال زمان اجرا نیز روی `channel-outbound` قرار دارند:

  * `sendDurableMessageBatch(...)`
  * `withDurableMessageSendContext(...)`
  * `deliverInboundReplyWithMessageSendContext(...)`
  * کمک‌تابع‌های پیش‌نویس جریان‌دهی/پیشرفت مانند `resolveChannelDraftStreamingChunking(...)`


`sendDurableMessageBatch(...)` یکی از نتایج صریح زیر را برمی‌گرداند:

  * `sent`: حداقل یک پیام قابل مشاهده پلتفرم تحویل داده شد.
  * `suppressed`: هیچ پیام پلتفرمی نباید مفقود تلقی شود.
  * `partial_failed`: حداقل یک پیام پلتفرم پیش از شکست یک payload یا اثر جانبی بعدی تحویل داده شد.
  * `failed`: هیچ رسید پلتفرمی تولید نشد.


وقتی یک دسته، payloadهای ارسال‌شده، سرکوب‌شده و ناموفق را ترکیب می‌کند، از `payloadOutcomes` استفاده کنید. لغو hook را از نتیجه خالی تحویل مستقیم legacy استنباط نکنید.

## ارسال سازگاری

ارسال پاسخ ورودی باید از طریق `dispatchChannelInboundReply(...)` از `channel-inbound` ساخته شود. تحویل پلتفرم را در آداپتور تحویل نگه دارید؛ برای آداپتورهای پیام، ارسال‌های پایدار، رسیدها، پیش‌نمایش زنده و گزینه‌های خط لوله پاسخ از `channel-outbound` استفاده کنید.

Was this useful?YesNo

Open issue