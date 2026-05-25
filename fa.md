---
title: OpenClaw
source_url: https://docs.openclaw.ai/fa
scraped_at: 2026-05-25
---

# OpenClaw 🦞

![OpenClaw](/assets/openclaw-logo-text-dark.png) ![OpenClaw](/assets/openclaw-logo-text.png)

> _"EXFOLIATE! EXFOLIATE!"_ — احتمالاً یک خرچنگ فضایی

**Gateway برای هر سیستم‌عاملی، مخصوص عامل‌های هوش مصنوعی در Discord، Google Chat، iMessage، Matrix، Microsoft Teams، Signal، Slack، Telegram، WhatsApp، Zalo و موارد بیشتر.**

یک پیام بفرستید و از داخل جیب خود پاسخ عامل را دریافت کنید. یک Gateway را در میان کانال‌های داخلی، Pluginهای کانال همراه، WebChat و گره‌های موبایل اجرا کنید.

[**شروع کنید** OpenClaw را نصب کنید و Gateway را در چند دقیقه بالا بیاورید. ](</fa/start/getting-started>) [**اجرای راه‌اندازی اولیه** راه‌اندازی هدایت‌شده با `openclaw onboard` و جریان‌های جفت‌سازی. ](</fa/start/wizard>) [**باز کردن رابط کنترل** داشبورد مرورگر را برای چت، پیکربندی و نشست‌ها اجرا کنید. ](</fa/web/control-ui>)

## OpenClaw چیست؟

OpenClaw یک **Gateway خودمیزبان** است که برنامه‌های چت و سطح‌های کانالی محبوب شما را — کانال‌های داخلی به‌همراه Pluginهای کانال همراه یا خارجی مانند Discord، Google Chat، iMessage، Matrix، Microsoft Teams، Signal، Slack، Telegram، WhatsApp، Zalo و موارد بیشتر — به عامل‌های کدنویسی هوش مصنوعی مانند Pi وصل می‌کند. شما یک فرایند Gateway واحد را روی دستگاه خودتان (یا یک سرور) اجرا می‌کنید، و این فرایند به پل میان برنامه‌های پیام‌رسان شما و یک دستیار هوش مصنوعی همیشه در دسترس تبدیل می‌شود.

**برای چه کسانی است؟** توسعه‌دهندگان و کاربران حرفه‌ای که یک دستیار هوش مصنوعی شخصی می‌خواهند که بتوانند از هرجا به آن پیام بدهند — بدون این‌که کنترل داده‌هایشان را از دست بدهند یا به یک سرویس میزبانی‌شده وابسته باشند.

**چه چیزی آن را متفاوت می‌کند؟**

  * **خودمیزبان** : روی سخت‌افزار شما و طبق قواعد شما اجرا می‌شود
  * **چندکاناله** : یک Gateway هم‌زمان کانال‌های داخلی و Pluginهای کانال همراه یا خارجی را سرویس می‌دهد
  * **بومی عامل** : برای عامل‌های کدنویسی با استفاده از ابزار، نشست‌ها، حافظه و مسیریابی چندعاملی ساخته شده است
  * **متن‌باز** : دارای مجوز MIT و جامعه‌محور


**به چه چیزی نیاز دارید؟** Node 24 (پیشنهادی)، یا Node 22 LTS (`22.16+`) برای سازگاری، یک کلید API از ارائه‌دهنده انتخابی‌تان، و ۵ دقیقه زمان. برای بهترین کیفیت و امنیت، از قوی‌ترین مدل نسل جدید موجود استفاده کنید.

## سازوکار
[code] 
    flowchart LR
      A["Chat apps + plugins"] --> B["Gateway"]
      B --> C["Pi agent"]
      B --> D["CLI"]
      B --> E["Web Control UI"]
      B --> F["macOS app"]
      B --> G["iOS and Android nodes"]
[/code]

Gateway منبع واحد حقیقت برای نشست‌ها، مسیریابی و اتصال‌های کانال است.

## قابلیت‌های کلیدی

[**Gateway چندکاناله** Discord، iMessage، Signal، Slack، Telegram، WhatsApp، WebChat و موارد بیشتر با یک فرایند Gateway واحد. ](</fa/channels>) [**کانال‌های Plugin** Pluginهای همراه، Matrix، Nostr، Twitch، Zalo و موارد بیشتر را در انتشارهای عادی و فعلی اضافه می‌کنند. ](</fa/tools/plugin>) [**مسیریابی چندعاملی** نشست‌های ایزوله برای هر عامل، فضای کاری یا فرستنده. ](</fa/concepts/multi-agent>) [**پشتیبانی رسانه** تصویر، صدا و سند ارسال و دریافت کنید. ](</fa/nodes/images>) [**رابط کنترل وب** داشبورد مرورگر برای چت، پیکربندی، نشست‌ها و گره‌ها. ](</fa/web/control-ui>) [**گره‌های موبایل** گره‌های iOS و Android را برای جریان‌های کاری دارای Canvas، دوربین و صدا جفت کنید. ](</fa/nodes>)

## شروع سریع

* ### نصب OpenClaw

bashCopy code
[code]
    npm install -g openclaw@latest
[/code]

* ### راه‌اندازی اولیه و نصب سرویس

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

* ### چت

رابط کنترل را در مرورگر خود باز کنید و یک پیام بفرستید:

bashCopy code
[code]
    openclaw dashboard
[/code]

یا یک کانال وصل کنید ([Telegram](</fa/channels/telegram>) سریع‌ترین است) و از گوشی خود چت کنید.

به نصب کامل و راه‌اندازی توسعه نیاز دارید؟ [شروع به کار](</fa/start/getting-started>) را ببینید.

## داشبورد

پس از شروع Gateway، رابط کنترل مرورگر را باز کنید.

  * پیش‌فرض محلی: <http://127.0.0.1:18789/>
  * دسترسی از راه دور: [سطح‌های وب](</fa/web>) و [Tailscale](</fa/gateway/tailscale>)


![OpenClaw](/whatsapp-openclaw.jpg)

## پیکربندی (اختیاری)

پیکربندی در `~/.openclaw/openclaw.json` قرار دارد.

  * اگر **هیچ کاری نکنید** ، OpenClaw از باینری Pi همراه در حالت RPC با نشست‌های جداگانه برای هر فرستنده استفاده می‌کند.
  * اگر می‌خواهید آن را محدود کنید، با `channels.whatsapp.allowFrom` و (برای گروه‌ها) قواعد اشاره شروع کنید.


مثال:

json5Copy code
[code]
    {  channels: {    whatsapp: {      allowFrom: ["+15555550123"],      groups: { "*": { requireMention: true } },    },  },  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },}
[/code]

## از اینجا شروع کنید

[**مرکزهای مستندات** همه مستندات و راهنماها، سازمان‌دهی‌شده بر اساس مورد استفاده. ](</fa/start/hubs>) [**پیکربندی** تنظیمات اصلی Gateway، توکن‌ها و پیکربندی ارائه‌دهنده. ](</fa/gateway/configuration>) [**دسترسی از راه دور** الگوهای دسترسی SSH و tailnet. ](</fa/gateway/remote>) [**کانال‌ها** راه‌اندازی مخصوص کانال برای Feishu، Microsoft Teams، WhatsApp، Telegram، Discord و موارد بیشتر. ](</fa/channels/telegram>) [**گره‌ها** گره‌های iOS و Android با جفت‌سازی، Canvas، دوربین و کنش‌های دستگاه. ](</fa/nodes>) [**راهنما** نقطه ورود برای رفع مشکلات رایج و عیب‌یابی. ](</fa/help>)

## بیشتر بیاموزید

[**فهرست کامل قابلیت‌ها** قابلیت‌های کامل کانال، مسیریابی و رسانه. ](</fa/concepts/features>) [**مسیریابی چندعاملی** ایزوله‌سازی فضای کاری و نشست‌های جداگانه برای هر عامل. ](</fa/concepts/multi-agent>) [**امنیت** توکن‌ها، فهرست‌های مجاز و کنترل‌های ایمنی. ](</fa/gateway/security>) [**عیب‌یابی** تشخیص‌های Gateway و خطاهای رایج. ](</fa/gateway/troubleshooting>) [**درباره و قدردانی‌ها** خاستگاه پروژه، مشارکت‌کنندگان و مجوز. ](</fa/reference/credits>)

Was this useful?YesNo