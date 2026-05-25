---
title: حذف BlueBubbles و مسیر imsg برای iMessage
source_url: https://docs.openclaw.ai/fa/announcements/bluebubbles-imessage
scraped_at: 2026-05-25
---

# حذف BlueBubbles و مسیر imsg برای iMessage

OpenClaw دیگر کانال BlueBubbles را ارائه نمی‌کند. پشتیبانی iMessage اکنون از طریق Plugin داخلی `imessage` اجرا می‌شود که [`imsg`](<https://github.com/steipete/imsg>) را به‌صورت محلی یا از طریق یک پوشش SSH راه‌اندازی می‌کند و با JSON-RPC روی stdin/stdout ارتباط می‌گیرد.

اگر پیکربندی شما هنوز شامل `channels.bluebubbles` است، آن را به `channels.imessage` مهاجرت دهید. نشانی مستندات قدیمی `/channels/bluebubbles` به [مهاجرت از BlueBubbles](</fa/channels/imessage-from-bluebubbles>) هدایت می‌شود که جدول کامل تبدیل پیکربندی و چک‌لیست جابه‌جایی را دارد.

## چه چیزی تغییر کرد

  * در مسیر پشتیبانی‌شده OpenClaw برای iMessage، هیچ سرور HTTP مربوط به BlueBubbles، مسیر webhook، گذرواژه REST، یا runtime مربوط به Plugin BlueBubbles وجود ندارد.
  * OpenClaw پیام‌ها را از طریق `imsg` روی همان Mac که Messages.app در آن وارد حساب شده است می‌خواند و پایش می‌کند.
  * ارسال، دریافت، تاریخچه، و رسانه‌های پایه از سطح‌های معمول `imsg` و مجوزهای macOS استفاده می‌کنند.
  * کنش‌های پیشرفته مانند پاسخ‌های رشته‌ای، tapbackها، ویرایش، لغو ارسال، افکت‌ها، رسیدهای خواندن، نشانگرهای در حال تایپ، و مدیریت گروه به `imsg launch` همراه با پل API خصوصی در دسترس نیاز دارند.
  * Gatewayهای Linux و Windows همچنان می‌توانند با تنظیم `channels.imessage.cliPath` روی یک پوشش SSH که `imsg` را روی Mac واردشده اجرا می‌کند، از iMessage استفاده کنند.


## چه کاری انجام دهید

  1. `imsg` را روی Mac مربوط به Messages نصب و تأیید کنید:

bashCopy code
[code]brew install steipete/tap/imsgimsg --versionimsg chats --limit 3imsg rpc --help
[/code]

  2. مجوزهای Full Disk Access و Automation را به زمینه فرایندی که `imsg` و OpenClaw را اجرا می‌کند اعطا کنید.

  3. پیکربندی قدیمی را تبدیل کنید:

json5Copy code
[code]{  channels: {    imessage: {      enabled: true,      cliPath: "/opt/homebrew/bin/imsg",      dmPolicy: "pairing",      allowFrom: ["+15555550123"],      groupPolicy: "allowlist",      groupAllowFrom: ["+15555550123"],      groups: {        "*": { requireMention: true },      },      includeAttachments: true,    },  },}
[/code]

  4. Gateway را بازراه‌اندازی و تأیید کنید:

bashCopy code
[code]openclaw channels status --probe
[/code]

  5. پیش از حذف سرور قدیمی BlueBubbles خود، پیام‌های مستقیم، گروه‌ها، پیوست‌ها، و هر کنش API خصوصی‌ای را که به آن وابسته‌اید آزمایش کنید.


## یادداشت‌های مهاجرت

  * `channels.bluebubbles.serverUrl` و `channels.bluebubbles.password` معادل iMessage ندارند.
  * `channels.bluebubbles.allowFrom`، `groupAllowFrom`، `groups`، `includeAttachments`، ریشه‌های پیوست، محدودیت‌های اندازه رسانه، قطعه‌بندی، و کلیدهای کنش معادل‌های iMessage دارند.
  * `channels.imessage.includeAttachments` همچنان به‌صورت پیش‌فرض خاموش است. اگر انتظار دارید عکس‌های ورودی، یادداشت‌های صوتی، ویدیوها، یا فایل‌ها به agent برسند، آن را صریحاً تنظیم کنید.
  * با `groupPolicy: "allowlist"`، بلوک قدیمی `groups` را، از جمله هر ورودی wildcard با مقدار `"*"`، کپی کنید. فهرست‌های مجاز فرستنده گروه و رجیستری گروه دروازه‌های جداگانه‌ای هستند.
  * اتصال‌های ACP که با `channel: "bluebubbles"` مطابقت داشتند باید به `channel: "imessage"` تغییر کنند.
  * کلیدهای نشست قدیمی BlueBubbles به کلیدهای نشست iMessage تبدیل نمی‌شوند. تأییدهای pairing بر اساس handle منتقل می‌شوند، اما تاریخچه گفت‌وگو زیر کلیدهای نشست BlueBubbles منتقل نمی‌شود.


## همچنین ببینید

  * [مهاجرت از BlueBubbles](</fa/channels/imessage-from-bluebubbles>)
  * [iMessage](</fa/channels/imessage>)
  * [مرجع پیکربندی - iMessage](</fa/gateway/config-channels#imessage>)


Was this useful?YesNo