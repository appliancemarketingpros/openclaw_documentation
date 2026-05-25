---
title: سرور لینوکس
source_url: https://docs.openclaw.ai/fa/vps
scraped_at: 2026-05-25
---

OpenClaw Gateway را روی هر سرور لینوکس یا VPS ابری اجرا کنید. این صفحه به شما کمک می‌کند یک ارائه‌دهنده انتخاب کنید، توضیح می‌دهد استقرارهای ابری چگونه کار می‌کنند، و تنظیمات عمومی لینوکس را که همه‌جا کاربرد دارد پوشش می‌دهد.

## انتخاب ارائه‌دهنده

[**Railway** [**Northflank** [**DigitalOcean** [**Oracle Cloud** [**Fly.io** [**Hetzner** [**Hostinger** [**GCP** [**Azure** [**exe.dev** [**Raspberry Pi** **AWS (EC2 / Lightsail / سطح رایگان)** هم به‌خوبی کار می‌کند. یک راهنمای ویدیویی جامعه در [x.com/techfrenAJ/status/2014934471095812547](<https://x.com/techfrenAJ/status/2014934471095812547>) در دسترس است (منبع جامعه -- ممکن است از دسترس خارج شود). راه‌اندازی‌های ابری چگونه کار می‌کنند

  * **Gateway روی VPS اجرا می‌شود** و مالک وضعیت + فضای کاری است.
  * از لپ‌تاپ یا گوشی خود از طریق **رابط کاربری کنترل** یا **Tailscale/SSH** متصل می‌شوید.
  * با VPS به‌عنوان منبع حقیقت رفتار کنید و از وضعیت + فضای کاری به‌طور منظم **پشتیبان بگیرید**.
  * پیش‌فرض امن: Gateway را روی loopback نگه دارید و از طریق تونل SSH یا Tailscale Serve به آن دسترسی پیدا کنید. اگر به `lan` یا `tailnet` bind می‌کنید، `gateway.auth.token` یا `gateway.auth.password` را الزامی کنید.

صفحه‌های مرتبط: [دسترسی راه دور Gateway](</fa/gateway/remote>)، [هاب پلتفرم‌ها](</fa/platforms>). ابتدا دسترسی مدیریتی را سخت‌سازی کنید پیش از نصب OpenClaw روی یک VPS عمومی، تصمیم بگیرید چگونه می‌خواهید خود سرور را مدیریت کنید.

  * اگر دسترسی مدیریتی فقط از طریق Tailnet می‌خواهید، ابتدا Tailscale را نصب کنید، VPS را به tailnet خود وصل کنید، یک نشست دوم SSH را از طریق IP متعلق به Tailscale یا نام MagicDNS تأیید کنید، سپس SSH عمومی را محدود کنید.
  * اگر از Tailscale استفاده نمی‌کنید، سخت‌سازی معادل را برای مسیر SSH خود پیش از در معرض گذاشتن سرویس‌های بیشتر اعمال کنید.
  * این از دسترسی Gateway جداست. همچنان می‌توانید OpenClaw را محدود به loopback نگه دارید و برای داشبورد از تونل SSH یا Tailscale Serve استفاده کنید.

گزینه‌های اختصاصی Tailscale برای Gateway در [Tailscale](</fa/gateway/tailscale>) قرار دارند. عامل مشترک شرکت روی VPS اجرای یک عامل واحد برای یک تیم، وقتی همه کاربران در یک مرز اعتماد مشترک هستند و عامل فقط کاری است، راه‌اندازی معتبری است.

  * آن را روی یک runtime اختصاصی نگه دارید (VPS/VM/container + کاربر/حساب‌های اختصاصی سیستم‌عامل).
  * آن runtime را به حساب‌های شخصی Apple/Google یا پروفایل‌های شخصی مرورگر/مدیر گذرواژه وارد نکنید.
  * اگر کاربران نسبت به یکدیگر خصمانه هستند، آن‌ها را بر اساس gateway/host/کاربر سیستم‌عامل جدا کنید.

جزئیات مدل امنیتی: [امنیت](</fa/gateway/security>). استفاده از نودها با VPS می‌توانید Gateway را در ابر نگه دارید و **نودها** را روی دستگاه‌های محلی خود (Mac/iOS/Android/headless) جفت کنید. نودها قابلیت‌های صفحه‌نمایش/دوربین/canvas محلی و `system.run` را فراهم می‌کنند، در حالی که Gateway در ابر می‌ماند. مستندات: [نودها](</fa/nodes>)، [CLI نودها](</fa/cli/nodes>). تنظیم شروع به کار برای VMهای کوچک و میزبان‌های ARM اگر فرمان‌های CLI روی VMهای کم‌مصرف (یا میزبان‌های ARM) کند به نظر می‌رسند، کش کامپایل ماژول Node را فعال کنید: bashCopy code
[code]
    grep -q 'NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache' ~/.bashrc || cat >> ~/.bashrc <<'EOF'export NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cachemkdir -p /var/tmp/openclaw-compile-cacheexport OPENCLAW_NO_RESPAWN=1EOFsource ~/.bashrc
[/code]

  * `NODE_COMPILE_CACHE` زمان‌های شروع فرمان‌های تکراری را بهبود می‌دهد.
  * `OPENCLAW_NO_RESPAWN=1` سربار اضافی شروع به کار از مسیر respawn خودکار را حذف می‌کند.
  * اجرای نخستین فرمان کش را گرم می‌کند؛ اجراهای بعدی سریع‌تر هستند.
  * برای جزئیات اختصاصی Raspberry Pi، [Raspberry Pi](</fa/install/raspberry-pi>) را ببینید.

چک‌لیست تنظیم systemd (اختیاری) برای میزبان‌های VM که از `systemd` استفاده می‌کنند، در نظر بگیرید:

  * افزودن env سرویس برای مسیر شروع پایدار: 
    * `OPENCLAW_NO_RESPAWN=1`
    * `NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache`
  * صریح نگه داشتن رفتار راه‌اندازی مجدد: 
    * `Restart=always`
    * `RestartSec=2`
    * `TimeoutStartSec=90`
  * برای مسیرهای وضعیت/کش، دیسک‌های مبتنی بر SSD را ترجیح دهید تا جریمه‌های شروع سرد ناشی از I/O تصادفی کاهش یابد.

برای مسیر استاندارد `openclaw onboard --install-daemon`، واحد کاربر را ویرایش کنید: bashCopy code
[code]
    systemctl --user edit openclaw-gateway.service
[/code]

iniCopy code
[code]
    [Service]Environment=OPENCLAW_NO_RESPAWN=1Environment=NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cacheRestart=alwaysRestartSec=2TimeoutStartSec=90
[/code]

اگر عمداً یک واحد سیستمی نصب کرده‌اید، به‌جای آن `openclaw-gateway.service` را از طریق `sudo systemctl edit openclaw-gateway.service` ویرایش کنید. این‌که سیاست‌های `Restart=` چگونه به بازیابی خودکار کمک می‌کنند: [systemd می‌تواند بازیابی سرویس را خودکار کند](<https://www.redhat.com/en/blog/systemd-automate-recovery>). برای رفتار OOM در لینوکس، انتخاب فرایند فرزند قربانی، و عیب‌یابی `exit 137`، [فشار حافظه لینوکس و killهای OOM](</fa/platforms/linux#memory-pressure-and-oom-kills>) را ببینید. مرتبط

  * [نمای کلی نصب](</fa/install>)
  * [DigitalOcean](</fa/install/digitalocean>)
  * [Fly.io](</fa/install/fly>)
  * [Hetzner](</fa/install/hetzner>)

](</fa/install/raspberry-pi>) Was this useful?YesNo ](</fa/install/exe-dev>)](</fa/install/azure>)](</fa/install/gcp>)](</fa/install/hostinger>)](</fa/install/hetzner>)](</fa/install/fly>)](</fa/install/oracle>)](</fa/install/digitalocean>)](</fa/install/northflank>)](</fa/install/railway>)