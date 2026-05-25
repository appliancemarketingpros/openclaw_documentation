---
title: exe.dev
source_url: https://docs.openclaw.ai/fa/install/exe-dev
scraped_at: 2026-05-25
---

هدف: اجرای OpenClaw Gateway روی یک VM در exe.dev که از لپ‌تاپ شما از این مسیر در دسترس باشد: `https://<vm-name>.exe.xyz`

این صفحه فرض می‌کند از تصویر پیش‌فرض **exeuntu** در exe.dev استفاده می‌کنید. اگر توزیع دیگری را انتخاب کرده‌اید، بسته‌ها را متناسب با آن تطبیق دهید.

## مسیر سریع برای مبتدیان

  1. <https://exe.new/openclaw>
  2. کلید/توکن احراز هویت خود را در صورت نیاز وارد کنید
  3. کنار VM خود روی «عامل» کلیک کنید و منتظر بمانید تا Shelley فرایند آماده‌سازی را تمام کند
  4. `https://<vm-name>.exe.xyz/` را باز کنید و با راز مشترک پیکربندی‌شده احراز هویت کنید (این راهنما به‌طور پیش‌فرض از احراز هویت توکنی استفاده می‌کند، اما اگر `gateway.auth.mode` را تغییر دهید، احراز هویت با گذرواژه هم کار می‌کند)
  5. هر درخواست جفت‌سازی دستگاه در انتظار را با `openclaw devices approve <requestId>` تأیید کنید


## آنچه نیاز دارید

  * حساب exe.dev
  * دسترسی `ssh exe.dev` به ماشین‌های مجازی [exe.dev](<https://exe.dev>) (اختیاری)


## نصب خودکار با Shelley

Shelley، عامل [exe.dev](<https://exe.dev>)، می‌تواند OpenClaw را فوراً با prompt ما نصب کند. prompt استفاده‌شده به شکل زیر است:

CodeCopy code
[code]
    Set up OpenClaw (https://docs.openclaw.ai/install) on this VM. Use the non-interactive and accept-risk flags for openclaw onboarding. Add the supplied auth or token as needed. Configure nginx to forward from the default port 18789 to the root location on the default enabled site config, making sure to enable Websocket support. Pairing is done by "openclaw devices list" and "openclaw devices approve <request id>". Make sure the dashboard shows that OpenClaw's health is OK. exe.dev handles forwarding from port 8000 to port 80/443 and HTTPS for us, so the final "reachable" should be <vm-name>.exe.xyz, without port specification.
[/code]

## نصب دستی

## 1) ساخت VM

از دستگاه خود:

bashCopy code
[code]
    ssh exe.dev new
[/code]

سپس متصل شوید:

bashCopy code
[code]
    ssh <vm-name>.exe.xyz
[/code]

## 2) نصب پیش‌نیازها (روی VM)

bashCopy code
[code]
    sudo apt-get updatesudo apt-get install -y git curl jq ca-certificates openssl
[/code]

## 3) نصب OpenClaw

اسکریپت نصب OpenClaw را اجرا کنید:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

## 4) راه‌اندازی nginx برای پروکسی‌کردن OpenClaw به پورت 8000

`/etc/nginx/sites-enabled/default` را با این محتوا ویرایش کنید

CodeCopy code
[code]
    server {    listen 80 default_server;    listen [::]:80 default_server;    listen 8000;    listen [::]:8000;     server_name _;     location / {        proxy_pass http://127.0.0.1:18789;        proxy_http_version 1.1;         # WebSocket support        proxy_set_header Upgrade $http_upgrade;        proxy_set_header Connection "upgrade";         # Standard proxy headers        proxy_set_header Host $host;        proxy_set_header X-Real-IP $remote_addr;        proxy_set_header X-Forwarded-For $remote_addr;        proxy_set_header X-Forwarded-Proto $scheme;         # Timeout settings for long-lived connections        proxy_read_timeout 86400s;        proxy_send_timeout 86400s;    }}
[/code]

هدرهای forwarding را بازنویسی کنید، نه اینکه زنجیره‌های ارسال‌شده توسط کلاینت را حفظ کنید. OpenClaw فراداده IP ارسال‌شده را فقط از پروکسی‌هایی که صراحتاً پیکربندی شده‌اند قابل اعتماد می‌داند، و زنجیره‌های `X-Forwarded-For` از نوع append-style به‌عنوان ریسک سخت‌سازی تلقی می‌شوند.

## 5) دسترسی به OpenClaw و اعطای مجوزها

به `https://<vm-name>.exe.xyz/` دسترسی پیدا کنید (خروجی Control UI از onboarding را ببینید). اگر درخواست احراز هویت کرد، راز مشترک پیکربندی‌شده را از VM جای‌گذاری کنید. این راهنما از احراز هویت توکنی استفاده می‌کند، بنابراین `gateway.auth.token` را با `openclaw config get gateway.auth.token` بازیابی کنید (یا با `openclaw doctor --generate-gateway-token` یکی بسازید). اگر Gateway را به احراز هویت با گذرواژه تغییر داده‌اید، به‌جای آن از `gateway.auth.password` / `OPENCLAW_GATEWAY_PASSWORD` استفاده کنید. دستگاه‌ها را با `openclaw devices list` و `openclaw devices approve <requestId>` تأیید کنید. وقتی تردید دارید، از Shelley در مرورگر خود استفاده کنید!

## راه‌اندازی کانال راه دور

برای میزبان‌های راه دور، به‌جای تعداد زیادی فراخوانی SSH به `config set`، یک فراخوانی `config patch` را ترجیح دهید. توکن‌های واقعی را در محیط VM یا `~/.openclaw/.env` نگه دارید و فقط SecretRefs را در `openclaw.json` قرار دهید.

روی VM، کاری کنید محیط سرویس شامل رازهای مورد نیازش باشد:

bashCopy code
[code]
    cat >> ~/.openclaw/.env <<'EOF'SLACK_BOT_TOKEN=xoxb-...SLACK_APP_TOKEN=xapp-...DISCORD_BOT_TOKEN=...OPENAI_API_KEY=sk-...EOF
[/code]

از ماشین محلی خود، یک فایل patch بسازید و آن را به VM pipe کنید:

json5Copy code
[code]
    // openclaw.remote.patch.json5{  secrets: {    providers: {      default: { source: "env" },    },  },  channels: {    slack: {      enabled: true,      mode: "socket",      botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },      appToken: { source: "env", provider: "default", id: "SLACK_APP_TOKEN" },      groupPolicy: "open",      requireMention: false,    },    discord: {      enabled: true,      token: { source: "env", provider: "default", id: "DISCORD_BOT_TOKEN" },      dmPolicy: "disabled",      dm: { enabled: false },      groupPolicy: "allowlist",    },  },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },      models: {        "openai/gpt-5.5": { params: { fastMode: true } },      },    },  },}
[/code]

bashCopy code
[code]
    ssh <vm-name>.exe.xyz 'openclaw config patch --stdin --dry-run' < ./openclaw.remote.patch.json5ssh <vm-name>.exe.xyz 'openclaw config patch --stdin' < ./openclaw.remote.patch.json5ssh <vm-name>.exe.xyz 'openclaw gateway restart && openclaw health'
[/code]

وقتی یک allowlist تو در تو باید دقیقاً به مقدار patch تبدیل شود، از `--replace-path` استفاده کنید؛ برای مثال هنگام جایگزینی allowlist کانال Discord:

bashCopy code
[code]
    ssh <vm-name>.exe.xyz 'openclaw config patch --stdin --replace-path "channels.discord.guilds[\"123\"].channels"' < ./discord.patch.json5
[/code]

## دسترسی راه دور

دسترسی راه دور توسط احراز هویت [exe.dev](<https://exe.dev>) مدیریت می‌شود. به‌طور پیش‌فرض، ترافیک HTTP از پورت 8000 با احراز هویت ایمیلی به `https://<vm-name>.exe.xyz` forward می‌شود.

## به‌روزرسانی

bashCopy code
[code]
    npm i -g openclaw@latestopenclaw doctoropenclaw gateway restartopenclaw health
[/code]

راهنما: [به‌روزرسانی](</fa/install/updating>)

## مرتبط

  * [Gateway راه دور](</fa/gateway/remote>)
  * [نمای کلی نصب](</fa/install>)


Was this useful?YesNo