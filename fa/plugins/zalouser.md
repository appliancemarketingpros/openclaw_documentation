---
title: Plugin شخصی Zalo
source_url: https://docs.openclaw.ai/fa/plugins/zalouser
scraped_at: 2026-05-25
---

پشتیبانی از Zalo Personal برای OpenClaw از طریق یک plugin، با استفاده از `zca-js` بومی برای خودکارسازی یک حساب کاربری عادی Zalo.

## نام‌گذاری

شناسهٔ کانال `zalouser` است تا صراحتا مشخص باشد که این یک **حساب کاربری شخصی Zalo** را خودکارسازی می‌کند (غیررسمی). ما `zalo` را برای یک ادغام احتمالی رسمی Zalo API در آینده رزرو نگه می‌داریم.

## محل اجرا

این plugin **داخل فرایند Gateway** اجرا می‌شود.

اگر از یک Gateway راه‌دور استفاده می‌کنید، آن را روی **دستگاهی که Gateway را اجرا می‌کند** نصب/پیکربندی کنید، سپس Gateway را بازراه‌اندازی کنید.

به هیچ باینری CLI خارجی `zca`/`openzca` نیاز نیست.

## نصب

### گزینهٔ A: نصب از npm

bashCopy code
[code]
    openclaw plugins install @openclaw/zalouser
[/code]

برای دنبال کردن تگ انتشار رسمی فعلی، از بستهٔ بدون نسخه استفاده کنید. فقط وقتی به نصبی بازتولیدپذیر نیاز دارید، نسخهٔ دقیق را پین کنید.

پس از آن Gateway را بازراه‌اندازی کنید.

### گزینهٔ B: نصب از یک پوشهٔ محلی (توسعه)

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/zalouser-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

پس از آن Gateway را بازراه‌اندازی کنید.

## پیکربندی

پیکربندی کانال زیر `channels.zalouser` قرار می‌گیرد (نه `plugins.entries.*`):

json5Copy code
[code]
    {  channels: {    zalouser: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

## CLI

bashCopy code
[code]
    openclaw channels login --channel zalouseropenclaw channels logout --channel zalouseropenclaw channels status --probeopenclaw message send --channel zalouser --target <threadId> --message "Hello from OpenClaw"openclaw directory peers list --channel zalouser --query "name"
[/code]

## ابزار عامل

نام ابزار: `zalouser`

کنش‌ها: `send`، `image`، `link`، `friends`، `groups`، `me`، `status`

کنش‌های پیام کانال همچنین برای واکنش‌های پیام از `react` پشتیبانی می‌کنند.

## مرتبط

  * [ساخت pluginها](</fa/plugins/building-plugins>)
  * [ClawHub](</fa/clawhub>)


Was this useful?YesNo