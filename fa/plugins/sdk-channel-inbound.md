---
title: API ورودی کانال
source_url: https://docs.openclaw.ai/fa/plugins/sdk-channel-inbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

Channel Pluginها باید مسیرهای دریافت را با اسم‌های inbound و message مدل‌سازی کنند:

textCopy code
[code]
    platform event -> inbound facts/context -> agent reply -> message delivery
[/code]

از `openclaw/plugin-sdk/channel-inbound` برای نرمال‌سازی رویداد ورودی، قالب‌بندی، ریشه‌ها، و ارکستراسیون استفاده کنید. از `openclaw/plugin-sdk/channel-outbound` برای رفتار بومی ارسال، رسید، تحویل پایدار، و پیش‌نمایش زنده استفاده کنید.

## راهنماهای هسته

tsCopy code
[code]
       buildChannelInboundEventContext,  runChannelInboundEvent,  dispatchChannelInboundReply,} from "openclaw/plugin-sdk/channel-inbound";
[/code]

  * `buildChannelInboundEventContext(...)`: فکت‌های نرمال‌شده‌ی کانال را به زمینه‌ی prompt/session نگاشت کنید. از `channelContext` برای عبور دادن فراداده‌ی sender/chat متعلق به کانال به hook پلاگین `ctx.channelContext` استفاده کنید؛ `PluginHookChannelSenderContext` یا `PluginHookChannelChatContext` را از این زیرمسیر برای فیلدهای مخصوص کانال گسترش دهید.
  * `runChannelInboundEvent(...)`: ingest، طبقه‌بندی، preflight، resolve، ثبت، dispatch، و finalize را برای یک رویداد ورودی پلتفرم اجرا کنید.
  * `dispatchChannelInboundReply(...)`: یک پاسخ ورودی از پیش assembled شده را با یک آداپتر تحویل ثبت و dispatch کنید.


runtime پلاگین تزریق‌شده، همین راهنماهای سطح بالا را زیر `runtime.channel.inbound.*` برای کانال‌های bundled/native که از قبل شیء runtime را دریافت می‌کنند، ارائه می‌دهد.

tsCopy code
[code]
    await runtime.channel.inbound.run({  channel: "demo",  accountId,  raw: platformEvent,  adapter: {    ingest: normalizePlatformEvent,    resolveTurn: resolveInboundReply,  },});
[/code]

dispatcherهای سازگاری باید ورودی‌های `dispatchChannelInboundReply(...)` را assemble کنند و تحویل پلتفرم را در آداپتر تحویل نگه دارند. مسیرهای ارسال جدید باید آداپترهای message و راهنماهای message پایدار را ترجیح دهند.

## مهاجرت

aliasهای runtime قدیمی `runtime.channel.turn.*` حذف شدند. استفاده کنید از:

  * `runtime.channel.inbound.run(...)` برای رویدادهای ورودی خام.
  * `runtime.channel.inbound.dispatchReply(...)` برای زمینه‌های پاسخ assembled شده.
  * `runtime.channel.inbound.buildContext(...)` برای payloadهای زمینه‌ی inbound.
  * `runtime.channel.inbound.runPreparedReply(...)` فقط برای مسیرهای dispatch آماده‌ی متعلق به کانال که از قبل closure مربوط به dispatch خودشان را assemble می‌کنند.


کد Plugin جدید نباید APIهای کانال با نام `turn` معرفی کند. واژگان turn مربوط به model یا agent را داخل کد agent/provider نگه دارید؛ Pluginهای کانال از اصطلاحات inbound، message، delivery، و reply استفاده می‌کنند.

Was this useful?YesNo

Open issue