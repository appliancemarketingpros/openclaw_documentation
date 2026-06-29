---
title: جعبه Upstash
source_url: https://docs.openclaw.ai/fa/install/upstash
scraped_at: 2026-06-29
---

InstallHosting

یک OpenClaw Gateway پایدار را روی Upstash Box، یک محیط لینوکس مدیریت‌شده با پشتیبانی از چرخه عمر keep-alive، اجرا کنید.

برای دسترسی به داشبورد از تونل SSH استفاده کنید. پورت Gateway را مستقیماً در معرض اینترنت عمومی قرار ندهید.

## پیش‌نیازها

  * حساب Upstash
  * Upstash Box با keep-alive
  * کلاینت SSH روی دستگاه محلی شما


## ایجاد یک Box

در Upstash Console یک Box با keep-alive ایجاد کنید. شناسه Box، مانند `right-flamingo-14486`، و کلید API Box خود را یادداشت کنید.

Upstash راهنمای فعلی OpenClaw Box خود را در [راه‌اندازی OpenClaw](<https://upstash.com/docs/box/guides/openclaw-setup>) نگه‌داری می‌کند.

## اتصال با تونل SSH

پورت داشبورد OpenClaw را به دستگاه محلی خود فوروارد کنید. هنگام درخواست، از کلید API Box خود به‌عنوان رمز عبور SSH استفاده کنید:

bashCopy code
[code]
    ssh -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

گزینه‌های keepalive افتادن تونل در زمان بیکاری هنگام راه‌اندازی اولیه را کاهش می‌دهند.

## نصب OpenClaw

داخل Box:

bashCopy code
[code]
    sudo npm install -g openclaw
[/code]

## اجرای راه‌اندازی اولیه

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

دستورالعمل‌ها را دنبال کنید. وقتی راه‌اندازی اولیه تمام شد، URL و توکن داشبورد را کپی کنید.

## شروع Gateway

Gateway را برای شبکه Box پیکربندی کنید و آن را در پس‌زمینه شروع کنید:

bashCopy code
[code]
    openclaw config set gateway.bind lannohup openclaw gateway > gateway.log 2>&1 &
[/code]

با فعال بودن تونل SSH، URL داشبورد را به‌صورت محلی باز کنید:

textCopy code
[code]
    http://127.0.0.1:18789/#token=<your-token>
[/code]

## راه‌اندازی مجدد خودکار

این فرمان را به‌عنوان اسکریپت init Box تنظیم کنید تا Gateway هنگام شروع Box دوباره راه‌اندازی شود:

bashCopy code
[code]
    nohup openclaw gateway > gateway.log 2>&1 &
[/code]

## عیب‌یابی

اگر SSH هنگام راه‌اندازی اولیه متوقف شد، با یک پیکربندی SSH تمیز و keepaliveها دوباره وصل شوید:

bashCopy code
[code]
    ssh -F /dev/null -o ControlMaster=no -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

این کار تنظیمات کهنه محلی `~/.ssh/config` را دور می‌زند و تونل را در دوره‌های بیکاری شبکه فعال نگه می‌دارد.

## مرتبط

  * [دسترسی از راه دور](</fa/gateway/remote>)
  * [امنیت Gateway](</fa/gateway/security>)
  * [به‌روزرسانی OpenClaw](</fa/install/updating>)


Was this useful?YesNo

Open issue