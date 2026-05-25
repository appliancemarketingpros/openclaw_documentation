---
title: راهنمای عملیاتی Gateway
source_url: https://docs.openclaw.ai/fa/gateway
scraped_at: 2026-05-25
---

از این صفحه برای راه‌اندازی روز اول و عملیات روز دوم سرویس Gateway استفاده کنید.

[**عیب‌یابی عمیق** عیب‌یابی مبتنی بر نشانه با نردبان‌های فرمان دقیق و امضاهای لاگ. ](</fa/gateway/troubleshooting>) [**پیکربندی** راهنمای راه‌اندازی وظیفه‌محور + مرجع کامل پیکربندی. ](</fa/gateway/configuration>) [**مدیریت اسرار** قرارداد SecretRef، رفتار snapshot زمان اجرا، و عملیات migrate/reload. ](</fa/gateway/secrets>) [**قرارداد طرح اسرار** قواعد دقیق هدف/مسیر `secrets apply` و رفتار auth-profile فقط-ارجاع. ](</fa/gateway/secrets-plan-contract>)

## راه‌اندازی محلی ۵ دقیقه‌ای

* ### Gateway را شروع کنید

bashCopy code
[code]
    openclaw gateway --port 18789# debug/trace mirrored to stdioopenclaw gateway --port 18789 --verbose# force-kill listener on selected port, then startopenclaw gateway --force
[/code]

* ### سلامت سرویس را تأیید کنید

bashCopy code
[code]
    openclaw gateway statusopenclaw statusopenclaw logs --follow
[/code]

مبنای سالم: `Runtime: running`، `Connectivity probe: ok`، و `Capability: ...` که با انتظار شما مطابقت دارد. وقتی به اثبات RPC با دامنه خواندن نیاز دارید، نه فقط دسترسی‌پذیری، از `openclaw gateway status --require-rpc` استفاده کنید.

* ### آمادگی channel را اعتبارسنجی کنید

bashCopy code
[code]
    openclaw channels status --probe
[/code]

با یک gateway در دسترس، این فرمان probeهای زنده channel برای هر حساب و auditهای اختیاری را اجرا می‌کند. اگر gateway در دسترس نباشد، CLI به‌جای خروجی probe زنده، به خلاصه‌های فقط-پیکربندی channel برمی‌گردد.

## مدل زمان اجرا

  * یک فرایند همیشه روشن برای مسیریابی، control plane، و اتصال‌های channel.
  * یک پورت multiplexed واحد برای: 
    * کنترل/RPC از طریق WebSocket
    * APIهای HTTP، سازگار با OpenAI (`/v1/models`، `/v1/embeddings`، `/v1/chat/completions`، `/v1/responses`، `/tools/invoke`)
    * UI کنترل و hookها
  * حالت bind پیش‌فرض: `loopback`.
  * احراز هویت به‌طور پیش‌فرض الزامی است. راه‌اندازی‌های shared-secret از `gateway.auth.token` / `gateway.auth.password` (یا `OPENCLAW_GATEWAY_TOKEN` / `OPENCLAW_GATEWAY_PASSWORD`) استفاده می‌کنند، و راه‌اندازی‌های reverse-proxy غیر-loopback می‌توانند از `gateway.auth.mode: "trusted-proxy"` استفاده کنند.


## endpointهای سازگار با OpenAI

سطح سازگاری با بیشترین اهرم در OpenClaw اکنون این‌هاست:

  * `GET /v1/models`
  * `GET /v1/models/{id}`
  * `POST /v1/embeddings`
  * `POST /v1/chat/completions`
  * `POST /v1/responses`


چرایی اهمیت این مجموعه:

  * بیشتر یکپارچه‌سازی‌های Open WebUI، LobeChat، و LibreChat ابتدا `/v1/models` را probe می‌کنند.
  * بسیاری از pipelineهای RAG و memory انتظار `/v1/embeddings` را دارند.
  * clientهای agent-native به‌طور فزاینده‌ای `/v1/responses` را ترجیح می‌دهند.


نکته برنامه‌ریزی:

  * `/v1/models` agent-first است: `openclaw`، `openclaw/default`، و `openclaw/<agentId>` را برمی‌گرداند.
  * `openclaw/default` alias پایدار است که همیشه به agent پیش‌فرض پیکربندی‌شده نگاشت می‌شود.
  * وقتی override برای provider/model پشتیبان می‌خواهید از `x-openclaw-model` استفاده کنید؛ در غیر این صورت تنظیمات معمول model و embedding مربوط به agent انتخاب‌شده کنترل را حفظ می‌کند.


همه این‌ها روی پورت اصلی Gateway اجرا می‌شوند و از همان مرز احراز هویت operator مورد اعتماد مانند بقیه API HTTP Gateway استفاده می‌کنند.

### اولویت پورت و bind

تنظیمات | ترتیب حل‌وفصل  
---|---  
پورت Gateway | `--port` → `OPENCLAW_GATEWAY_PORT` → `gateway.port` → `18789`  
حالت bind | CLI/override → `gateway.bind` → `loopback`  
  
سرویس‌های gateway نصب‌شده `--port` حل‌شده را در metadata ناظر ثبت می‌کنند. پس از تغییر `gateway.port`، `openclaw doctor --fix` یا `openclaw gateway install --force` را اجرا کنید تا launchd/systemd/schtasks فرایند را روی پورت جدید شروع کند.

راه‌اندازی Gateway هنگام seed کردن originهای محلی Control UI برای bindهای غیر-loopback از همان پورت و bind مؤثر استفاده می‌کند. برای مثال، `--bind lan --port 3000` پیش از اجرای اعتبارسنجی زمان اجرا، `http://localhost:3000` و `http://127.0.0.1:3000` را seed می‌کند. هر origin مرورگر راه‌دور، مانند URLهای proxy HTTPS، را صراحتاً به `gateway.controlUi.allowedOrigins` اضافه کنید.

### حالت‌های hot reload

`gateway.reload.mode` | رفتار  
---|---  
`off` | بدون بارگذاری مجدد پیکربندی  
`hot` | فقط تغییرات hot-safe را اعمال می‌کند  
`restart` | در تغییراتی که نیازمند reload هستند restart می‌کند  
`hybrid` (پیش‌فرض) | وقتی ایمن باشد hot-apply می‌کند، و وقتی لازم باشد restart می‌کند  
  
## مجموعه فرمان‌های operator

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway status --deep   # adds a system-level service scanopenclaw gateway status --jsonopenclaw gateway installopenclaw gateway restartopenclaw gateway stopopenclaw secrets reloadopenclaw logs --followopenclaw doctor
[/code]

`gateway status --deep` برای کشف سرویس اضافه است (LaunchDaemons/واحدهای systemd system /schtasks)، نه یک probe سلامت RPC عمیق‌تر.

## چند Gateway (همان میزبان)

بیشتر نصب‌ها باید روی هر ماشین یک gateway اجرا کنند. یک gateway واحد می‌تواند چندین agent و channel را میزبانی کند.

فقط وقتی به چند gateway نیاز دارید که عمداً جداسازی یا یک bot نجات بخواهید.

بررسی‌های مفید:

bashCopy code
[code]
    openclaw gateway status --deepopenclaw gateway probe
[/code]

انتظار چه چیزی را داشته باشید:

  * `gateway status --deep` می‌تواند `Other gateway-like services detected (best effort)` را گزارش کند و وقتی نصب‌های stale launchd/systemd/schtasks هنوز وجود دارند، راهنمای cleanup چاپ کند.
  * `gateway probe` وقتی بیش از یک هدف پاسخ دهد می‌تواند درباره `multiple reachable gateways` هشدار دهد.
  * اگر این عمدی است، پورت‌ها، config/state، و ریشه‌های workspace را برای هر gateway جدا کنید.


چک‌لیست برای هر instance:

  * `gateway.port` یکتا
  * `OPENCLAW_CONFIG_PATH` یکتا
  * `OPENCLAW_STATE_DIR` یکتا
  * `agents.defaults.workspace` یکتا


مثال:

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=~/.openclaw/a.json OPENCLAW_STATE_DIR=~/.openclaw-a openclaw gateway --port 19001OPENCLAW_CONFIG_PATH=~/.openclaw/b.json OPENCLAW_STATE_DIR=~/.openclaw-b openclaw gateway --port 19002
[/code]

راه‌اندازی تفصیلی: [/gateway/multiple-gateways](</fa/gateway/multiple-gateways>).

## دسترسی راه‌دور

ترجیحی: Tailscale/VPN. Fallback: تونل SSH.

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 user@host
[/code]

سپس clientها را به‌صورت محلی به `ws://127.0.0.1:18789` وصل کنید.

ببینید: [Gateway راه‌دور](</fa/gateway/remote>)، [احراز هویت](</fa/gateway/authentication>)، [Tailscale](</fa/gateway/tailscale>).

## نظارت و چرخه‌عمر سرویس

برای قابلیت اتکای شبیه production از اجراهای تحت نظارت استفاده کنید.

### macOS (launchd)

bashCopy code
[code]
    openclaw gateway installopenclaw gateway statusopenclaw gateway restartopenclaw gateway stop
[/code]

برای restartها از `openclaw gateway restart` استفاده کنید. `openclaw gateway stop` و `openclaw gateway start` را به‌عنوان جایگزین restart زنجیره نکنید.

در macOS، `gateway stop` به‌طور پیش‌فرض از `launchctl bootout` استفاده می‌کند — این کار LaunchAgent را از نشست boot فعلی بدون پایدار کردن disable حذف می‌کند، بنابراین بازیابی خودکار KeepAlive پس از crashهای غیرمنتظره همچنان کار می‌کند و `gateway start` دوباره به‌صورت تمیز فعال می‌شود. برای جلوگیری پایدار از auto-respawn در restartهای سیستم، `--disable` را پاس کنید: `openclaw gateway stop --disable`.

labelهای LaunchAgent برابر `ai.openclaw.gateway` (پیش‌فرض) یا `ai.openclaw.<profile>` (profile نام‌دار) هستند. `openclaw doctor` drift پیکربندی سرویس را audit و repair می‌کند.

### Linux (systemd user)

bashCopy code
[code]
    openclaw gateway installsystemctl --user enable --now openclaw-gateway[-<profile>].serviceopenclaw gateway status
[/code]

برای پایداری پس از logout، lingering را فعال کنید:

bashCopy code
[code]
    sudo loginctl enable-linger <user>
[/code]

نمونه user-unit دستی وقتی به مسیر نصب سفارشی نیاز دارید:

iniCopy code
[code]
    [Unit]Description=OpenClaw GatewayAfter=network-online.targetWants=network-online.target [Service]ExecStart=/usr/local/bin/openclaw gateway --port 18789Restart=alwaysRestartSec=5TimeoutStopSec=30TimeoutStartSec=30SuccessExitStatus=0 143KillMode=control-group [Install]WantedBy=default.target
[/code]

### Windows (native)

powershellCopy code
[code]
    openclaw gateway installopenclaw gateway status --jsonopenclaw gateway restartopenclaw gateway stop
[/code]

راه‌اندازی مدیریت‌شده native Windows از یک Scheduled Task با نام `OpenClaw Gateway` (یا `OpenClaw Gateway (<profile>)` برای profileهای نام‌دار) استفاده می‌کند. اگر ایجاد Scheduled Task رد شود، OpenClaw به یک launcher پوشه Startup برای هر کاربر برمی‌گردد که به `gateway.cmd` داخل دایرکتوری state اشاره می‌کند.

### Linux (system service)

برای میزبان‌های چندکاربره/همیشه‌روشن از یک system unit استفاده کنید.

bashCopy code
[code]
    sudo systemctl daemon-reloadsudo systemctl enable --now openclaw-gateway[-<profile>].service
[/code]

از همان بدنه سرویس user unit استفاده کنید، اما آن را زیر `/etc/systemd/system/openclaw-gateway[-<profile>].service` نصب کنید و اگر binary `openclaw` شما جای دیگری است `ExecStart=` را تنظیم کنید.

اجازه ندهید `openclaw doctor --fix` هم برای همان profile/port یک سرویس gateway در سطح کاربر نصب کند. وقتی Doctor یک سرویس Gateway OpenClaw در سطح system پیدا کند، از آن نصب خودکار خودداری می‌کند؛ وقتی system unit مالک چرخه‌عمر است از `OPENCLAW_SERVICE_REPAIR_POLICY=external` استفاده کنید.

## مسیر سریع profile توسعه

bashCopy code
[code]
    openclaw --dev setupopenclaw --dev gateway --allow-unconfiguredopenclaw --dev status
[/code]

پیش‌فرض‌ها شامل state/config جداافتاده و پورت پایه gateway برابر `19001` هستند.

## مرجع سریع protocol (نمای operator)

  * نخستین frame client باید `connect` باشد.
  * Gateway snapshot `hello-ok` را برمی‌گرداند (`presence`، `health`، `stateVersion`، `uptimeMs`، limits/policy).
  * `hello-ok.features.methods` / `events` یک فهرست کشف محافظه‌کارانه هستند، نه dump تولیدشده از هر مسیر helper قابل فراخوانی.
  * درخواست‌ها: `req(method, params)` → `res(ok/payload|error)`.
  * eventهای رایج شامل `connect.challenge`، `agent`، `chat`، `session.message`، `session.tool`، `sessions.changed`، `presence`، `tick`، `health`، `heartbeat`، eventهای چرخه‌عمر pairing/approval، و `shutdown` هستند.


اجرای agent دو مرحله‌ای است:

  1. ack پذیرش فوری (`status:"accepted"`)
  2. پاسخ تکمیل نهایی (`status:"ok"|"error"`)، همراه با eventهای `agent` streamشده در این بین.


مستندات کامل protocol را ببینید: [Protocol Gateway](</fa/gateway/protocol>).

## بررسی‌های عملیاتی

### زنده بودن

  * WS را باز کنید و `connect` بفرستید.
  * انتظار پاسخ `hello-ok` با snapshot را داشته باشید.


### آمادگی

bashCopy code
[code]
    openclaw gateway statusopenclaw channels status --probeopenclaw health
[/code]

### بازیابی gap

eventها replay نمی‌شوند. در gapهای sequence، پیش از ادامه state (`health`، `system-presence`) را refresh کنید.

## امضاهای رایج خرابی

امضا | مشکل محتمل  
---|---  
`refusing to bind gateway ... without auth` | bind غیر loopback بدون مسیر معتبر احراز هویت Gateway  
`another gateway instance is already listening` / `EADDRINUSE` | تداخل پورت  
`Gateway start blocked: set gateway.mode=local` | پیکربندی روی حالت راه دور تنظیم شده، یا نشان حالت محلی از پیکربندی آسیب‌دیده حذف شده است  
`unauthorized` هنگام اتصال | ناهماهنگی احراز هویت بین کلاینت و Gateway  
  
برای نردبان‌های کامل تشخیص، از [عیب‌یابی Gateway](</fa/gateway/troubleshooting>) استفاده کنید.

## تضمین‌های ایمنی

  * کلاینت‌های پروتکل Gateway وقتی Gateway در دسترس نباشد سریع شکست می‌خورند (بدون fallback ضمنی به کانال مستقیم).
  * فریم‌های نخست نامعتبر/غیراتصالی رد و بسته می‌شوند.
  * خاموشی graceful رویداد `shutdown` را پیش از بسته‌شدن سوکت صادر می‌کند.


* * *

مرتبط:

  * [عیب‌یابی](</fa/gateway/troubleshooting>)
  * [فرایند پس‌زمینه](</fa/gateway/background-process>)
  * [پیکربندی](</fa/gateway/configuration>)
  * [سلامت](</fa/gateway/health>)
  * [Doctor](</fa/gateway/doctor>)
  * [احراز هویت](</fa/gateway/authentication>)


## مرتبط

  * [پیکربندی](</fa/gateway/configuration>)
  * [عیب‌یابی Gateway](</fa/gateway/troubleshooting>)
  * [دسترسی راه دور](</fa/gateway/remote>)
  * [مدیریت اسرار](</fa/gateway/secrets>)


Was this useful?YesNo