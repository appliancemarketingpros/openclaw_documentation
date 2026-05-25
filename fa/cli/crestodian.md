---
title: کرستودیان
source_url: https://docs.openclaw.ai/fa/cli/crestodian
scraped_at: 2026-05-25
---

# `openclaw crestodian`

Crestodian دستیار محلی راه‌اندازی، تعمیر و پیکربندی OpenClaw است. این ابزار طوری طراحی شده که وقتی مسیر عادی عامل خراب است، همچنان در دسترس بماند.

اجرای `openclaw` بدون هیچ فرمانی، Crestodian را در یک ترمینال تعاملی شروع می‌کند. اجرای `openclaw crestodian` همان دستیار را به‌صورت صریح شروع می‌کند.

## آنچه Crestodian نشان می‌دهد

هنگام شروع، Crestodian تعاملی همان پوسته TUI مورد استفاده توسط `openclaw tui` را با یک بک‌اند چت Crestodian باز می‌کند. گزارش چت با یک خوشامدگویی کوتاه شروع می‌شود:

  * چه زمانی Crestodian را شروع کنید
  * مدل یا مسیر برنامه‌ریز قطعی که Crestodian واقعا از آن استفاده می‌کند
  * اعتبار پیکربندی و عامل پیش‌فرض
  * دسترس‌پذیری Gateway از نخستین بررسی شروع
  * اقدام اشکال‌زدایی بعدی که Crestodian می‌تواند انجام دهد


این ابزار برای شروع، اسرار را تخلیه نمی‌کند یا فرمان‌های CLI مربوط به plugin را بارگذاری نمی‌کند. TUI همچنان سربرگ عادی، گزارش چت، خط وضعیت، پابرگ، تکمیل خودکار، و کنترل‌های ویرایشگر را ارائه می‌دهد.

از `status` برای فهرست موجودی تفصیلی شامل مسیر پیکربندی، مسیرهای docs/source، بررسی‌های CLI محلی، وجود کلید API، عامل‌ها، مدل، و جزئیات Gateway استفاده کنید.

Crestodian از همان کشف مرجع OpenClaw استفاده می‌کند که عامل‌های عادی استفاده می‌کنند. در یک checkout گیت، خود را به `docs/` محلی و درخت منبع محلی اشاره می‌دهد. در نصب بسته npm، از مستندات بسته‌بندی‌شده بسته استفاده می‌کند و به <https://github.com/openclaw/openclaw> پیوند می‌دهد، با راهنمایی صریح برای بازبینی منبع هر زمان که مستندات کافی نیستند.

## مثال‌ها

bashCopy code
[code]
    openclawopenclaw crestodianopenclaw crestodian --jsonopenclaw crestodian --message "models"openclaw crestodian --message "validate config"openclaw crestodian --message "setup workspace ~/Projects/work model openai/gpt-5.5" --yesopenclaw crestodian --message "set default model openai/gpt-5.5" --yesopenclaw onboard --modern
[/code]

داخل TUI مربوط به Crestodian:

textCopy code
[code]
    statushealthdoctordoctor fixvalidate configsetupsetup workspace ~/Projects/work model openai/gpt-5.5config set gateway.port 19001config set-ref gateway.auth.token env OPENCLAW_GATEWAY_TOKENgateway statusrestart gatewayagentscreate agent work workspace ~/Projects/workmodelsset default model openai/gpt-5.5plugins listplugins search slackplugin install clawhub:openclaw-codex-app-serverplugin uninstall openclaw-codex-app-servertalk to work agenttalk to agent for ~/Projects/workauditquit
[/code]

## شروع امن

مسیر شروع Crestodian عمدا کوچک است. این ابزار می‌تواند اجرا شود وقتی:

  * `openclaw.json` وجود ندارد
  * `openclaw.json` نامعتبر است
  * Gateway از کار افتاده است
  * ثبت فرمان plugin در دسترس نیست
  * هنوز هیچ عاملی پیکربندی نشده است


`openclaw --help` و `openclaw --version` همچنان از مسیرهای سریع عادی استفاده می‌کنند. `openclaw` غیرتعاملی به‌جای چاپ راهنمای ریشه، با یک پیام کوتاه خارج می‌شود، چون محصول بدون فرمان Crestodian است.

## عملیات‌ها و تأیید

Crestodian به‌جای ویرایش موردی پیکربندی، از عملیات‌های نوع‌دار استفاده می‌کند.

عملیات‌های فقط‌خواندنی می‌توانند بلافاصله اجرا شوند:

  * نمایش نمای کلی
  * فهرست کردن عامل‌ها
  * فهرست کردن pluginهای نصب‌شده
  * جست‌وجوی pluginهای ClawHub
  * نمایش وضعیت مدل/بک‌اند
  * اجرای بررسی‌های وضعیت یا سلامت
  * بررسی دسترس‌پذیری Gateway
  * اجرای doctor بدون اصلاح‌های تعاملی
  * اعتبارسنجی پیکربندی
  * نمایش مسیر گزارش حسابرسی


عملیات‌های پایدار در حالت تعاملی به تأیید مکالمه‌ای نیاز دارند، مگر اینکه برای یک فرمان مستقیم `--yes` را پاس کنید:

  * نوشتن پیکربندی
  * اجرای `config set`
  * تنظیم مقادیر SecretRef پشتیبانی‌شده از طریق `config set-ref`
  * اجرای bootstrap راه‌اندازی/onboarding
  * تغییر مدل پیش‌فرض
  * شروع، توقف، یا راه‌اندازی دوباره Gateway
  * ایجاد عامل‌ها
  * نصب pluginها از ClawHub یا npm
  * حذف نصب pluginها
  * اجرای تعمیرات doctor که پیکربندی یا وضعیت را بازنویسی می‌کنند


نوشتن‌های اعمال‌شده در اینجا ثبت می‌شوند:

textCopy code
[code]
    ~/.openclaw/audit/crestodian.jsonl
[/code]

کشف حسابرسی نمی‌شود. فقط عملیات‌های اعمال‌شده و نوشتن‌ها ثبت می‌شوند.

`openclaw onboard --modern`، Crestodian را به‌عنوان پیش‌نمایش onboarding مدرن شروع می‌کند. `openclaw onboard` ساده همچنان onboarding کلاسیک را اجرا می‌کند.

## Bootstrap راه‌اندازی

`setup`، bootstrap onboarding با اولویت چت است. فقط از طریق عملیات‌های پیکربندی نوع‌دار می‌نویسد و ابتدا تأیید می‌خواهد.

textCopy code
[code]
    setupsetup workspace ~/Projects/worksetup workspace ~/Projects/work model openai/gpt-5.5
[/code]

وقتی هیچ مدلی پیکربندی نشده باشد، setup نخستین بک‌اند قابل استفاده را به این ترتیب انتخاب می‌کند و به شما می‌گوید چه چیزی را انتخاب کرده است:

  * مدل صریح موجود، اگر از قبل پیکربندی شده باشد
  * `OPENAI_API_KEY` -> `openai/gpt-5.5`
  * `ANTHROPIC_API_KEY` -> `anthropic/claude-opus-4-7`
  * Claude Code CLI -> `claude-cli/claude-opus-4-7`
  * Codex CLI -> `codex-cli/gpt-5.5`


اگر هیچ‌کدام در دسترس نباشند، setup همچنان workspace پیش‌فرض را می‌نویسد و مدل را تنظیم‌نشده باقی می‌گذارد. Codex/Claude Code را نصب کنید یا وارد آن شوید، یا `OPENAI_API_KEY`/`ANTHROPIC_API_KEY` را در دسترس قرار دهید، سپس setup را دوباره اجرا کنید.

## برنامه‌ریز کمک‌گرفته از مدل

Crestodian همیشه در حالت قطعی شروع می‌شود. برای فرمان‌های مبهمی که تجزیه‌گر قطعی نمی‌فهمد، Crestodian محلی می‌تواند یک نوبت برنامه‌ریز محدود از طریق مسیرهای runtime عادی OpenClaw انجام دهد. ابتدا از مدل پیکربندی‌شده OpenClaw استفاده می‌کند. اگر هنوز هیچ مدل پیکربندی‌شده‌ای قابل استفاده نباشد، می‌تواند به runtimeهای محلی که از قبل روی ماشین حاضرند fallback کند:

  * Claude Code CLI: `claude-cli/claude-opus-4-7`
  * Codex app-server harness: `openai/gpt-5.5`
  * Codex CLI: `codex-cli/gpt-5.5`


برنامه‌ریز کمک‌گرفته از مدل نمی‌تواند پیکربندی را مستقیما تغییر دهد. باید درخواست را به یکی از فرمان‌های نوع‌دار Crestodian ترجمه کند، سپس قواعد عادی تأیید و حسابرسی اعمال می‌شوند. Crestodian قبل از اجرای هر چیزی، مدلی را که استفاده کرده و فرمان تفسیرشده را چاپ می‌کند. نوبت‌های fallback برنامه‌ریز بدون پیکربندی موقتی هستند، در جایی که runtime پشتیبانی کند ابزارغیرفعال هستند، و از یک workspace/session موقت استفاده می‌کنند.

حالت نجات کانال پیام از برنامه‌ریز کمک‌گرفته از مدل استفاده نمی‌کند. نجات راه‌دور قطعی می‌ماند تا مسیر عامل عادی خراب یا در معرض نفوذ نتواند به‌عنوان ویرایشگر پیکربندی استفاده شود.

## جابه‌جایی به یک عامل

از یک انتخاب‌گر زبان طبیعی برای خروج از Crestodian و باز کردن TUI عادی استفاده کنید:

textCopy code
[code]
    talk to agenttalk to work agentswitch to main agent
[/code]

`openclaw tui`، `openclaw chat`، و `openclaw terminal` همچنان TUI عامل عادی را مستقیما باز می‌کنند. آن‌ها Crestodian را شروع نمی‌کنند.

پس از جابه‌جایی به TUI عادی، از `/crestodian` برای بازگشت به Crestodian استفاده کنید. می‌توانید یک درخواست پیگیری هم اضافه کنید:

textCopy code
[code]
    /crestodian/crestodian restart gateway
[/code]

جابه‌جایی‌های عامل داخل TUI یک breadcrumb باقی می‌گذارند که `/crestodian` در دسترس است.

## حالت نجات پیام

حالت نجات پیام نقطه ورود کانال پیام برای Crestodian است. این حالت برای زمانی است که عامل عادی شما از کار افتاده، اما یک کانال مورد اعتماد مانند WhatsApp هنوز فرمان‌ها را دریافت می‌کند.

فرمان متنی پشتیبانی‌شده:

  * `/crestodian <request>`


جریان اپراتور:

textCopy code
[code]
    You, in a trusted owner DM: /crestodian statusOpenClaw: Crestodian rescue mode. Gateway reachable: no. Config valid: no.You: /crestodian restart gatewayOpenClaw: Plan: restart the Gateway. Reply /crestodian yes to apply.You: /crestodian yesOpenClaw: Applied. Audit entry written.
[/code]

ایجاد عامل را نیز می‌توان از اعلان محلی یا حالت نجات در صف گذاشت:

textCopy code
[code]
    create agent work workspace ~/Projects/work model openai/gpt-5.5/crestodian create agent work workspace ~/Projects/work
[/code]

حالت نجات راه‌دور یک سطح ادمین است. باید مانند تعمیر پیکربندی راه‌دور با آن رفتار شود، نه مانند چت عادی.

قرارداد امنیتی برای نجات راه‌دور:

  * وقتی sandboxing فعال است غیرفعال می‌شود. اگر یک agent/session sandbox شده باشد، Crestodian باید نجات راه‌دور را رد کند و توضیح دهد که تعمیر CLI محلی لازم است.
  * حالت مؤثر پیش‌فرض `auto` است: نجات راه‌دور را فقط در عملیات YOLO مورد اعتماد مجاز کن، جایی که runtime از قبل اختیار محلی بدون sandbox دارد.
  * به یک هویت مالک صریح نیاز دارد. نجات نباید قواعد فرستنده wildcard، سیاست گروه باز، webhooks احرازنشده، یا کانال‌های ناشناس را بپذیرد.
  * به‌صورت پیش‌فرض فقط DMهای مالک. نجات گروه/کانال به opt-in صریح نیاز دارد.
  * جست‌وجو و فهرست plugin فقط‌خواندنی هستند. نصب plugin به‌صورت پیش‌فرض فقط محلی است چون کد اجرایی دانلود می‌کند. حذف نصب plugin را می‌توان به‌عنوان یک عملیات تعمیر تأییدشده مجاز دانست وقتی سیاست نجات نوشتن‌های پایدار را مجاز می‌کند.
  * نجات راه‌دور نمی‌تواند TUI محلی را باز کند یا به یک session عامل تعاملی جابه‌جا شود. برای تحویل به عامل از `openclaw` محلی استفاده کنید.
  * نوشتن‌های پایدار همچنان به تأیید نیاز دارند، حتی در حالت نجات.
  * هر عملیات نجات اعمال‌شده را حسابرسی کنید. نجات کانال پیام metadata مربوط به کانال، حساب، فرستنده، و نشانی منبع را ثبت می‌کند. عملیات‌های تغییردهنده پیکربندی همچنین hashهای پیکربندی قبل و بعد را ثبت می‌کنند.
  * هرگز اسرار را echo نکنید. بازرسی SecretRef باید وجود داشتن را گزارش کند، نه مقادیر را.
  * اگر Gateway زنده است، عملیات‌های نوع‌دار Gateway را ترجیح دهید. اگر Gateway از کار افتاده است، فقط از سطح تعمیر محلی حداقلی استفاده کنید که به حلقه عامل عادی وابسته نیست.


شکل پیکربندی:

jsoncCopy code
[code]
    {  "crestodian": {    "rescue": {      "enabled": "auto",      "ownerDmOnly": true,    },  },}
[/code]

`enabled` باید این‌ها را بپذیرد:

  * `"auto"`: پیش‌فرض. فقط وقتی اجازه بده که runtime مؤثر YOLO باشد و sandboxing خاموش باشد.
  * `false`: هرگز نجات کانال پیام را مجاز نکن.
  * `true`: وقتی بررسی‌های مالک/کانال موفق باشند، نجات را صریحا مجاز کن. این همچنان نباید رد sandboxing را دور بزند.


وضعیت YOLO پیش‌فرض `"auto"` این است:

  * حالت sandbox به `off` resolve شود
  * `tools.exec.security` به `full` resolve شود
  * `tools.exec.ask` به `off` resolve شود


نجات راه‌دور توسط lane داکر پوشش داده می‌شود:

bashCopy code
[code]
    pnpm test:docker:crestodian-rescue
[/code]

Fallback برنامه‌ریز محلی بدون پیکربندی توسط این پوشش داده می‌شود:

bashCopy code
[code]
    pnpm test:docker:crestodian-planner
[/code]

یک smoke سطح فرمان کانال زنده opt-in، `/crestodian status` به‌علاوه یک roundtrip تأیید پایدار از طریق handler نجات را بررسی می‌کند:

bashCopy code
[code]
    pnpm test:live:crestodian-rescue-channel
[/code]

راه‌اندازی تازه بدون پیکربندی از طریق Crestodian توسط این پوشش داده می‌شود:

bashCopy code
[code]
    pnpm test:docker:crestodian-first-run
[/code]

آن lane با یک دایرکتوری وضعیت خالی شروع می‌کند، `openclaw` بدون آرگومان را به Crestodian هدایت می‌کند، مدل پیش‌فرض را تنظیم می‌کند، یک عامل اضافی ایجاد می‌کند، Discord را از طریق فعال‌سازی plugin به‌علاوه SecretRef توکن پیکربندی می‌کند، پیکربندی را اعتبارسنجی می‌کند، و گزارش حسابرسی را بررسی می‌کند. QA Lab نیز یک سناریوی مبتنی بر repo برای همان جریان Ring 0 دارد:

bashCopy code
[code]
    pnpm openclaw qa suite --scenario crestodian-ring-zero-setup
[/code]

## مرتبط

  * [مرجع CLI](</fa/cli>)
  * [Doctor](</fa/cli/doctor>)
  * [TUI](</fa/cli/tui>)
  * [Sandbox](</fa/cli/sandbox>)
  * [امنیت](</fa/cli/security>)


Was this useful?YesNo