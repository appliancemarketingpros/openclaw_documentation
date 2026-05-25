---
title: Gateway
source_url: https://docs.openclaw.ai/fa/cli/gateway
scraped_at: 2026-05-25
---

Gateway سرور WebSocketِ OpenClaw است (کانال‌ها، Nodeها، نشست‌ها، هوک‌ها). زیر‌دستورهای این صفحه زیر `openclaw gateway …` قرار دارند.

[**کشف Bonjour** راه‌اندازی mDNS محلی + DNS-SD گستره‌وسیع. ](</fa/gateway/bonjour>) [**نمای کلی کشف** OpenClaw چگونه Gatewayها را اعلام می‌کند و می‌یابد. ](</fa/gateway/discovery>) [**پیکربندی** کلیدهای سطح‌بالای پیکربندی Gateway. ](</fa/gateway/configuration>)

## اجرای Gateway

یک فرایند Gateway محلی اجرا کنید:

bashCopy code
[code]
    openclaw gateway
[/code]

نام مستعار اجرای پیش‌زمینه:

bashCopy code
[code]
    openclaw gateway run
[/code]

رفتار راه‌اندازی

  * به‌صورت پیش‌فرض، Gateway از شروع خودداری می‌کند مگر اینکه `gateway.mode=local` در `~/.openclaw/openclaw.json` تنظیم شده باشد. برای اجراهای موردی/توسعه‌ای از `--allow-unconfigured` استفاده کنید.
  * `openclaw onboard --mode local` و `openclaw setup` باید `gateway.mode=local` را بنویسند. اگر فایل وجود دارد اما `gateway.mode` موجود نیست، آن را یک پیکربندی خراب یا بازنویسی‌شده تلقی کنید و به‌جای اینکه حالت محلی را به‌طور ضمنی فرض کنید، آن را تعمیر کنید.
  * اگر فایل وجود دارد و `gateway.mode` موجود نیست، Gateway آن را آسیب مشکوک به پیکربندی تلقی می‌کند و از حدس زدن «local» برای شما خودداری می‌کند.
  * بایند شدن فراتر از loopback بدون احراز هویت مسدود است (محدودیت ایمنی).
  * وقتی مجاز باشد، `SIGUSR1` یک راه‌اندازی مجدد درون‌فرایندی را فعال می‌کند (`commands.restart` به‌صورت پیش‌فرض فعال است؛ برای مسدود کردن راه‌اندازی مجدد دستی، `commands.restart: false` را تنظیم کنید، در حالی که اعمال/به‌روزرسانی ابزار/پیکربندی Gateway همچنان مجاز می‌ماند).
  * هندلرهای `SIGINT`/`SIGTERM` فرایند Gateway را متوقف می‌کنند، اما هیچ وضعیت سفارشی ترمینال را بازنمی‌گردانند. اگر CLI را با یک TUI یا ورودی حالت خام می‌پوشانید، پیش از خروج ترمینال را بازیابی کنید.


### گزینه‌ها

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tcG9ydCA8cG9ydA " type="number"> پورت WebSocket (پیش‌فرض از پیکربندی/محیط می‌آید؛ معمولاً `18789`).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tdG9rZW4gPHRva2Vu " type="string"> بازنویسی توکن (همچنین `OPENCLAW_GATEWAY_TOKEN` را برای فرایند تنظیم می‌کند).

پیکربندی serve/funnel در Tailscale را هنگام خاموشی بازنشانی کنید.

شروع Gateway را بدون `gateway.mode=local` در پیکربندی مجاز کنید. فقط برای راه‌اندازی اولیه موردی/توسعه‌ای، گارد راه‌اندازی را دور می‌زند؛ فایل پیکربندی را نمی‌نویسد یا تعمیر نمی‌کند.

اگر موجود نیست، پیکربندی توسعه + فضای کاری ایجاد کنید (از [BOOTSTRAP.md](<http://BOOTSTRAP.md>) عبور می‌کند).

پیکربندی توسعه + اعتبارنامه‌ها + نشست‌ها + فضای کاری را بازنشانی کنید (به `--dev` نیاز دارد).

پیش از شروع، هر شنونده موجود روی پورت انتخاب‌شده را خاتمه دهید.

گزارش‌های مفصل.

فقط گزارش‌های بک‌اند CLI را در کنسول نشان دهید (و stdout/stderr را فعال کنید).

نام مستعار برای `--ws-log compact`.

رویدادهای جریان خام مدل را در jsonl ثبت کنید.

## راه‌اندازی مجدد Gateway

bashCopy code
[code]
    openclaw gateway restartopenclaw gateway restart --safeopenclaw gateway restart --safe --skip-deferralopenclaw gateway restart --force
[/code]

`openclaw gateway restart --safe` از Gateway در حال اجرا می‌خواهد پیش از راه‌اندازی مجدد، کار فعال OpenClaw را پیش‌بررسی کند. اگر عملیات صف‌شده، تحویل پاسخ، اجراهای تعبیه‌شده، یا اجراهای وظیفه فعال باشند، Gateway مسدودکننده‌ها را گزارش می‌کند، درخواست‌های تکراری راه‌اندازی مجدد ایمن را ادغام می‌کند، و وقتی کار فعال تخلیه شد راه‌اندازی مجدد انجام می‌دهد. `restart` ساده برای سازگاری، رفتار موجود مدیر سرویس را حفظ می‌کند. فقط زمانی از `--force` استفاده کنید که صراحتاً مسیر override فوری را می‌خواهید.

`openclaw gateway restart --safe --skip-deferral` همان راه‌اندازی مجدد هماهنگ و آگاه از OpenClaw را مانند `--safe` اجرا می‌کند، اما گیت تعویق کار فعال را دور می‌زند تا Gateway حتی وقتی مسدودکننده‌ها گزارش شده‌اند، راه‌اندازی مجدد را فوراً صادر کند. وقتی یک تعویق به‌خاطر اجرای وظیفه گیرکرده قفل شده و `--safe` به‌تنهایی برای همیشه منتظر می‌ماند، از آن به‌عنوان گزینه خروج اپراتور استفاده کنید. `--skip-deferral` به `--safe` نیاز دارد.

### پروفایل‌گیری راه‌اندازی

  * `OPENCLAW_GATEWAY_STARTUP_TRACE=1` را تنظیم کنید تا زمان‌بندی فازها هنگام راه‌اندازی Gateway ثبت شود، از جمله تأخیر `eventLoopMax` برای هر فاز و زمان‌بندی‌های جدول جست‌وجوی Plugin برای شاخص نصب‌شده، رجیستری مانیفست، برنامه‌ریزی راه‌اندازی، و کار نقشه مالک.
  * `OPENCLAW_DIAGNOSTICS=timeline` را همراه با `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=<path>` تنظیم کنید تا یک timeline تشخیصی راه‌اندازی JSONL با بهترین تلاش برای هارنس‌های QA خارجی نوشته شود. همچنین می‌توانید این پرچم را با `diagnostics.flags: ["timeline"]` در پیکربندی فعال کنید؛ مسیر همچنان از محیط تأمین می‌شود. برای شامل کردن نمونه‌های حلقه رویداد، `OPENCLAW_DIAGNOSTICS_EVENT_LOOP=1` را اضافه کنید.
  * برای بنچمارک کردن راه‌اندازی Gateway، `pnpm test:startup:gateway -- --runs 5 --warmup 1` را اجرا کنید. بنچمارک اولین خروجی فرایند، `/healthz`، `/readyz`، زمان‌بندی‌های ردگیری راه‌اندازی، تأخیر حلقه رویداد، و جزئیات زمان‌بندی جدول جست‌وجوی Plugin را ثبت می‌کند.


## پرس‌وجو از یک Gateway در حال اجرا

همه دستورهای پرس‌وجو از WebSocket RPC استفاده می‌کنند.

### حالت‌های خروجی

  * پیش‌فرض: قابل‌خواندن برای انسان (رنگی در TTY).
  * `--json`: JSON قابل‌خواندن برای ماشین (بدون سبک‌دهی/نشانگر چرخان).
  * `--no-color` (یا `NO_COLOR=1`): ANSI را غیرفعال کنید، با حفظ چینش انسانی.


### گزینه‌های مشترک

  * `--url <url>`: URL مربوط به WebSocket Gateway.
  * `--token <token>`: توکن Gateway.
  * `--password <password>`: گذرواژه Gateway.
  * `--timeout <ms>`: مهلت/بودجه زمانی (بسته به دستور متفاوت است).
  * `--expect-final`: منتظر یک پاسخ «final» بمانید (فراخوانی‌های عامل).


### `gateway health`

bashCopy code
[code]
    openclaw gateway health --url ws://127.0.0.1:18789
[/code]

اندپوینت HTTP `/healthz` یک پروب زنده‌بودن است: به‌محض اینکه سرور بتواند به HTTP پاسخ دهد، برمی‌گردد. اندپوینت HTTP `/readyz` سخت‌گیرتر است و تا وقتی سایدکارهای Plugin راه‌اندازی، کانال‌ها، یا هوک‌های پیکربندی‌شده هنوز در حال پایدار شدن هستند، قرمز می‌ماند. پاسخ‌های تفصیلی آمادگی محلی یا احراز هویت‌شده شامل یک بلوک تشخیصی `eventLoop` با تأخیر حلقه رویداد، بهره‌برداری حلقه رویداد، نسبت هسته CPU، و یک پرچم `degraded` هستند.

### `gateway usage-cost`

خلاصه‌های هزینه مصرف را از گزارش‌های نشست دریافت کنید.

bashCopy code
[code]
    openclaw gateway usage-costopenclaw gateway usage-cost --days 7openclaw gateway usage-cost --json
[/code]

### `gateway stability`

ثبت‌کننده اخیر پایداری تشخیصی را از یک Gateway در حال اجرا دریافت کنید.

bashCopy code
[code]
    openclaw gateway stabilityopenclaw gateway stability --type payload.largeopenclaw gateway stability --bundle latestopenclaw gateway stability --bundle latest --exportopenclaw gateway stability --json
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tbGltaXQgPGxpbWl0 " type="number" default="25"> حداکثر تعداد رویدادهای اخیر برای شامل کردن (حداکثر `1000`).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tdHlwZSA8dHlwZQ " type="string"> بر اساس نوع رویداد تشخیصی، مانند `payload.large` یا `diagnostic.memory.pressure` فیلتر کنید.

به‌جای فراخوانی Gateway در حال اجرا، یک بسته پایداری ذخیره‌شده را بخوانید. برای جدیدترین بسته زیر دایرکتوری وضعیت، از `--bundle latest` (یا فقط `--bundle`) استفاده کنید، یا مسیر JSON بسته را مستقیماً بدهید.

به‌جای چاپ جزئیات پایداری، یک zip تشخیص پشتیبانی قابل‌اشتراک بنویسید.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tb3V0cHV0IDxwYXRo " type="string"> مسیر خروجی برای `--export`.

حریم خصوصی و رفتار بسته

  * رکوردها فراداده عملیاتی را نگه می‌دارند: نام رویدادها، شمارش‌ها، اندازه‌های بایت، خوانش‌های حافظه، وضعیت صف/نشست، نام کانال/Plugin، و خلاصه‌های نشست ویرایش‌شده. آن‌ها متن چت، بدنه‌های Webhook، خروجی‌های ابزار، بدنه‌های خام درخواست یا پاسخ، توکن‌ها، کوکی‌ها، مقادیر محرمانه، نام میزبان‌ها، یا شناسه‌های خام نشست را نگه نمی‌دارند. برای غیرفعال کردن کامل ثبت‌کننده، `diagnostics.enabled: false` را تنظیم کنید.
  * هنگام خروج‌های fatal از Gateway، timeoutهای خاموشی، و شکست‌های راه‌اندازی پس از restart، وقتی ثبت‌کننده رویداد دارد، OpenClaw همان اسنپ‌شات تشخیصی را در `~/.openclaw/logs/stability/openclaw-stability-*.json` می‌نویسد. جدیدترین بسته را با `openclaw gateway stability --bundle latest` بررسی کنید؛ `--limit`، `--type`، و `--since-seq` نیز برای خروجی بسته اعمال می‌شوند.


### `gateway diagnostics export`

یک zip تشخیصی محلی بنویسید که برای پیوست کردن به گزارش‌های باگ طراحی شده است. برای مدل حریم خصوصی و محتوای بسته، [صدور تشخیص‌ها](</fa/gateway/diagnostics>) را ببینید.

bashCopy code
[code]
    openclaw gateway diagnostics exportopenclaw gateway diagnostics export --output openclaw-diagnostics.zipopenclaw gateway diagnostics export --json
[/code]

جست‌وجوی بسته پایداری ذخیره‌شده را رد کنید.

مسیر نوشته‌شده، اندازه، و مانیفست را به‌صورت JSON چاپ کنید.

خروجی شامل یک مانیفست، یک خلاصه Markdown، شکل پیکربندی، جزئیات پیکربندی پاک‌سازی‌شده، خلاصه‌های گزارش پاک‌سازی‌شده، اسنپ‌شات‌های وضعیت/سلامت Gateway پاک‌سازی‌شده، و جدیدترین بسته پایداری در صورت وجود است.

این خروجی برای اشتراک‌گذاری در نظر گرفته شده است. جزئیات عملیاتی کمک‌کننده به اشکال‌زدایی را نگه می‌دارد، مانند فیلدهای ایمن گزارش OpenClaw، نام‌های زیرسیستم، کدهای وضعیت، مدت‌زمان‌ها، حالت‌های پیکربندی‌شده، پورت‌ها، شناسه‌های Plugin، شناسه‌های ارائه‌دهنده، تنظیمات غیرمحرمانه قابلیت‌ها، و پیام‌های گزارش عملیاتی ویرایش‌شده. متن چت، بدنه‌های Webhook، خروجی‌های ابزار، اعتبارنامه‌ها، کوکی‌ها، شناسه‌های حساب/پیام، متن پرامپت/دستورالعمل، نام میزبان‌ها، و مقادیر محرمانه را حذف یا ویرایش می‌کند. وقتی یک پیام به سبک LogTape شبیه متن payload کاربر/چت/ابزار باشد، خروجی فقط این را نگه می‌دارد که یک پیام حذف شده است، همراه با تعداد بایت‌های آن.

### `gateway status`

`gateway status` سرویس Gateway (launchd/systemd/schtasks) را به‌همراه یک پروب اختیاری از قابلیت اتصال/احراز هویت نشان می‌دهد.

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway status --jsonopenclaw gateway status --require-rpc
[/code]

از probe اتصال صرف‌نظر کنید (نمای فقط سرویس).

سرویس‌های سطح سیستم را هم اسکن کنید.

probe اتصال پیش‌فرض را به یک probe خواندن ارتقا دهید و وقتی آن probe خواندن شکست خورد با کد غیرصفر خارج شوید. نمی‌توان آن را با `--no-probe` ترکیب کرد.

معناشناسی وضعیت

  * `gateway status` حتی وقتی پیکربندی محلی CLI وجود ندارد یا نامعتبر است، برای عیب‌یابی در دسترس می‌ماند.
  * `gateway status` پیش‌فرض وضعیت سرویس، اتصال WebSocket، و قابلیت احراز هویتِ قابل مشاهده در زمان handshake را اثبات می‌کند. عملیات خواندن/نوشتن/مدیریت را اثبات نمی‌کند.
  * probeهای عیب‌یابی برای احراز هویت دستگاه در بار نخست غیرتغییردهنده هستند: وقتی توکن دستگاه کش‌شده‌ای وجود داشته باشد از همان استفاده می‌کنند، اما فقط برای بررسی وضعیت، هویت دستگاه CLI جدید یا رکورد pairing دستگاه فقط‌خواندنی ایجاد نمی‌کنند.
  * `gateway status` در صورت امکان SecretRefهای احراز هویت پیکربندی‌شده را برای احراز هویت probe resolve می‌کند.
  * اگر یک SecretRef احراز هویت لازم در این مسیر فرمان resolve نشود، `gateway status --json` هنگام شکست اتصال/احراز هویت probe مقدار `rpc.authWarning` را گزارش می‌کند؛ `--token`/`--password` را صریحا پاس دهید یا ابتدا منبع secret را resolve کنید.
  * اگر probe موفق شود، هشدارهای auth-ref resolveنشده برای جلوگیری از مثبت‌های کاذب سرکوب می‌شوند.
  * وقتی یک سرویس در حال گوش‌دادن کافی نیست و لازم دارید فراخوانی‌های RPC با محدوده خواندن هم سالم باشند، در اسکریپت‌ها و اتوماسیون از `--require-rpc` استفاده کنید.
  * `--deep` یک اسکن best-effort برای نصب‌های اضافی launchd/systemd/schtasks اضافه می‌کند. وقتی چند سرویس شبیه Gateway شناسایی شوند، خروجی انسانی راهنمای پاک‌سازی چاپ می‌کند و هشدار می‌دهد که بیشتر راه‌اندازی‌ها باید برای هر ماشین یک Gateway اجرا کنند.
  * `--deep` همچنین وقتی فرایند سرویس برای restart توسط supervisor خارجی به‌صورت تمیز خارج شده باشد، handoff اخیر restart ناظر Gateway را گزارش می‌کند.
  * `--deep` اعتبارسنجی پیکربندی را در حالت آگاه از Plugin اجرا می‌کند (`pluginValidation: "full"`) و هشدارهای manifest مربوط به Pluginهای پیکربندی‌شده را نمایش می‌دهد (برای مثال metadata پیکربندی channel جاافتاده) تا smoke checkهای نصب و به‌روزرسانی آن‌ها را بگیرند. `gateway status` پیش‌فرض مسیر سریع فقط‌خواندنی را حفظ می‌کند که اعتبارسنجی Plugin را رد می‌کند.
  * خروجی انسانی مسیر resolveشده لاگ فایل را به‌همراه snapshot مسیرها/اعتبار پیکربندی CLI در برابر سرویس شامل می‌شود تا به عیب‌یابی drift در profile یا state-dir کمک کند.

بررسی‌های auth-drift در Linux systemd

  * در نصب‌های Linux systemd، بررسی‌های drift احراز هویت هر دو مقدار `Environment=` و `EnvironmentFile=` را از unit می‌خوانند (شامل `%h`، مسیرهای quoted، چند فایل، و فایل‌های اختیاری `-`).
  * بررسی‌های drift، SecretRefهای `gateway.auth.token` را با env زمان اجرای ادغام‌شده resolve می‌کنند (ابتدا env فرمان سرویس، سپس fallback به env فرایند).
  * اگر احراز هویت توکنی عملا فعال نباشد (`gateway.auth.mode` صریح برابر `password`/`none`/`trusted-proxy`، یا mode تنظیم نشده باشد در وضعیتی که password می‌تواند برنده شود و هیچ token candidate نمی‌تواند برنده شود)، بررسی‌های token-drift از resolve کردن توکن پیکربندی صرف‌نظر می‌کنند.


### `gateway probe`

`gateway probe` فرمان «debug everything» است. همیشه این موارد را probe می‌کند:

  * remote gateway پیکربندی‌شده شما (اگر تنظیم شده باشد)، و
  * localhost (loopback) **حتی اگر remote پیکربندی شده باشد**.


اگر `--url` را پاس دهید، آن هدف صریح پیش از هر دو اضافه می‌شود. خروجی انسانی هدف‌ها را این‌طور برچسب می‌زند:

  * `URL (explicit)`
  * `Remote (configured)` یا `Remote (configured, inactive)`
  * `Local loopback`

bashCopy code
[code]
    openclaw gateway probeopenclaw gateway probe --json
[/code]

تفسیر

  * `Reachable: yes` یعنی دست‌کم یک هدف اتصال WebSocket را پذیرفت.
  * `Capability: read-only|write-capable|admin-capable|pairing-pending|connect-only` گزارش می‌دهد که probe چه چیزی را درباره احراز هویت توانسته اثبات کند. این از دسترسی‌پذیری جداست.
  * `Read probe: ok` یعنی فراخوانی‌های RPC جزئیات با محدوده خواندن (`health`/`status`/`system-presence`/`config.get`) هم موفق شدند.
  * `Read probe: limited - missing scope: operator.read` یعنی اتصال موفق شد اما RPC با محدوده خواندن محدود است. این به‌عنوان دسترسی‌پذیری **degraded** گزارش می‌شود، نه شکست کامل.
  * `Read probe: failed` پس از `Connect: ok` یعنی Gateway اتصال WebSocket را پذیرفت، اما عیب‌یابی‌های خواندن بعدی timeout شدند یا شکست خوردند. این هم دسترسی‌پذیری **degraded** است، نه Gateway غیرقابل دسترسی.
  * مانند `gateway status`، probe از احراز هویت دستگاه کش‌شده موجود استفاده مجدد می‌کند اما هویت دستگاه بار نخست یا state مربوط به pairing ایجاد نمی‌کند.
  * کد خروج فقط وقتی غیرصفر است که هیچ هدف probeشده‌ای قابل دسترسی نباشد.

خروجی JSON

سطح بالا:

  * `ok`: دست‌کم یک هدف قابل دسترسی است.
  * `degraded`: دست‌کم یک هدف اتصال را پذیرفته اما عیب‌یابی کامل RPC جزئیات را تکمیل نکرده است.
  * `capability`: بهترین قابلیتی که بین هدف‌های قابل دسترسی دیده شده است (`read_only`، `write_capable`، `admin_capable`، `pairing_pending`، `connected_no_operator_scope`، یا `unknown`).
  * `primaryTargetId`: بهترین هدف برای در نظر گرفتن به‌عنوان برنده فعال با این ترتیب: URL صریح، SSH tunnel، remote پیکربندی‌شده، سپس local loopback.
  * `warnings[]`: رکوردهای هشدار best-effort با `code`، `message`، و `targetIds` اختیاری.
  * `network`: hintهای URL مربوط به local loopback/tailnet که از پیکربندی فعلی و networking میزبان به‌دست آمده‌اند.
  * `discovery.timeoutMs` و `discovery.count`: بودجه/تعداد نتیجه واقعی discovery که برای این گذر probe استفاده شده است.


برای هر هدف (`targets[].connect`):

  * `ok`: دسترسی‌پذیری پس از connect + طبقه‌بندی degraded.
  * `rpcOk`: موفقیت کامل RPC جزئیات.
  * `scopeLimited`: RPC جزئیات به‌دلیل نبود scope اپراتور شکست خورده است.


برای هر هدف (`targets[].auth`):

  * `role`: نقش احراز هویت گزارش‌شده در `hello-ok` وقتی موجود باشد.
  * `scopes`: scopeهای اعطاشده گزارش‌شده در `hello-ok` وقتی موجود باشند.
  * `capability`: طبقه‌بندی قابلیت احراز هویت نمایش‌داده‌شده برای آن هدف.

کدهای هشدار رایج

  * `ssh_tunnel_failed`: راه‌اندازی SSH tunnel شکست خورد؛ فرمان به probeهای مستقیم fallback کرد.
  * `multiple_gateways`: بیش از یک هدف قابل دسترسی بود؛ این غیرمعمول است مگر اینکه عمدا profileهای ایزوله اجرا کنید، مانند یک rescue bot.
  * `auth_secretref_unresolved`: یک SecretRef احراز هویت پیکربندی‌شده برای یک هدف شکست‌خورده resolve نشد.
  * `probe_scope_limited`: اتصال WebSocket موفق شد، اما probe خواندن به‌دلیل نبود `operator.read` محدود شد.


#### Remote از طریق SSH (برابری با اپ Mac)

حالت «Remote over SSH» در اپ macOS از یک port-forward محلی استفاده می‌کند تا remote gateway (که ممکن است فقط به loopback bind شده باشد) در `ws://127.0.0.1:<port>` قابل دسترسی شود.

معادل CLI:

bashCopy code
[code]
    openclaw gateway probe --ssh user@gateway-host
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tc3NoIDx0YXJnZXQ " type="string"> `user@host` یا `user@host:port` (پورت به‌طور پیش‌فرض `22` است).

نخستین میزبان Gateway کشف‌شده را به‌عنوان هدف SSH از endpoint کشف resolveشده انتخاب کنید (`local.` به‌علاوه دامنه wide-area پیکربندی‌شده، اگر وجود داشته باشد). hintهای فقط TXT نادیده گرفته می‌شوند.

پیکربندی (اختیاری، به‌عنوان پیش‌فرض استفاده می‌شود):

  * `gateway.remote.sshTarget`
  * `gateway.remote.sshIdentity`


### `gateway call <method>`

کمک‌کننده RPC سطح پایین.

bashCopy code
[code]
    openclaw gateway call statusopenclaw gateway call logs.tail --params '{"sinceMs": 60000}'
[/code]

عمدتا برای RPCهای سبک agent که پیش از payload نهایی، رویدادهای میانی را stream می‌کنند.

خروجی JSON قابل خواندن برای ماشین.

## مدیریت سرویس Gateway

bashCopy code
[code]
    openclaw gateway installopenclaw gateway startopenclaw gateway stopopenclaw gateway restartopenclaw gateway uninstall
[/code]

### نصب با wrapper

وقتی سرویس managed باید از طریق یک executable دیگر شروع شود، مثلا یک shim مدیر secretها یا یک run-as helper، از `--wrapper` استفاده کنید. wrapper آرگومان‌های عادی Gateway را دریافت می‌کند و مسئول است در نهایت `openclaw` یا Node را با همان آرگومان‌ها exec کند.

bashCopy code
[code]
    cat > ~/.local/bin/openclaw-doppler <<'EOF'#!/usr/bin/env bashset -euo pipefailexec doppler run --project my-project --config production -- openclaw "$@"EOFchmod +x ~/.local/bin/openclaw-doppler openclaw gateway install --wrapper ~/.local/bin/openclaw-doppler --forceopenclaw gateway restart
[/code]

می‌توانید wrapper را از طریق محیط هم تنظیم کنید. `gateway install` اعتبارسنجی می‌کند که مسیر یک فایل executable باشد، wrapper را در `ProgramArguments` سرویس می‌نویسد، و `OPENCLAW_WRAPPER` را در محیط سرویس برای reinstallهای اجباری، به‌روزرسانی‌ها، و تعمیرهای doctor بعدی پایدار می‌کند.

bashCopy code
[code]
    OPENCLAW_WRAPPER="$HOME/.local/bin/openclaw-doppler" openclaw gateway install --forceopenclaw doctor
[/code]

برای حذف یک wrapper پایدارشده، هنگام reinstall مقدار `OPENCLAW_WRAPPER` را پاک کنید:

bashCopy code
[code]
    OPENCLAW_WRAPPER= openclaw gateway install --forceopenclaw gateway restart
[/code]

گزینه‌های فرمان

  * `gateway status`: `--url`, `--token`, `--password`, `--timeout`, `--no-probe`, `--require-rpc`, `--deep`, `--json`
  * `gateway install`: `--port`, `--runtime <node|bun>`, `--token`, `--wrapper <path>`, `--force`, `--json`
  * `gateway restart`: `--safe`, `--skip-deferral`, `--force`, `--wait <duration>`, `--json`
  * `gateway uninstall|start`: `--json`
  * `gateway stop`: `--disable`, `--json`

رفتار چرخه عمر

  * از `gateway restart` برای راه‌اندازی دوباره یک سرویس مدیریت‌شده استفاده کنید. `gateway stop` و `gateway start` را به‌عنوان جایگزین راه‌اندازی دوباره پشت‌سرهم اجرا نکنید.
  * در macOS، `gateway stop` به‌طور پیش‌فرض از `launchctl bootout` استفاده می‌کند، که LaunchAgent را از جلسه بوت فعلی حذف می‌کند بدون اینکه غیرفعال‌سازی را پایدار کند — بازیابی خودکار KeepAlive برای خرابی‌های آینده فعال می‌ماند و `gateway start` بدون نیاز به `launchctl enable` دستی، دوباره به‌صورت تمیز فعال می‌شود. برای سرکوب پایدار KeepAlive و RunAtLoad، گزینه `--disable` را بدهید تا gateway تا `gateway start` صریح بعدی دوباره اجرا نشود؛ وقتی توقف دستی باید پس از راه‌اندازی‌های دوباره سیستم یا ریبوت‌ها باقی بماند، از این استفاده کنید.
  * `gateway restart --safe` از Gateway در حال اجرا می‌خواهد کار فعال OpenClaw را پیش‌بررسی کند و راه‌اندازی دوباره را تا تخلیه تحویل پاسخ، اجراهای جاسازی‌شده، و اجرای وظیفه‌ها به تعویق بیندازد. `--safe` را نمی‌توان با `--force` یا `--wait` ترکیب کرد.
  * `gateway restart --wait 30s` بودجه تخلیه راه‌اندازی دوباره پیکربندی‌شده را برای همان راه‌اندازی دوباره بازنویسی می‌کند. عددهای بدون واحد برحسب میلی‌ثانیه هستند؛ واحدهایی مانند `s`، `m`، و `h` پذیرفته می‌شوند. `--wait 0` به‌صورت نامحدود منتظر می‌ماند.
  * `gateway restart --safe --skip-deferral` راه‌اندازی دوباره امنِ آگاه از OpenClaw را اجرا می‌کند اما gate تعویق را دور می‌زند تا Gateway حتی وقتی مسدودکننده‌ها گزارش شده‌اند، راه‌اندازی دوباره را فوراً صادر کند. راه خروج اپراتور برای تعویق‌های گیرکرده اجرای وظیفه؛ به `--safe` نیاز دارد.
  * `gateway restart --force` تخلیه کار فعال را رد می‌کند و فوراً راه‌اندازی دوباره انجام می‌دهد. وقتی اپراتور مسدودکننده‌های وظیفه فهرست‌شده را از قبل بررسی کرده و اکنون می‌خواهد gateway برگردد، از آن استفاده کنید.
  * فرمان‌های چرخه عمر برای اسکریپت‌نویسی `--json` را می‌پذیرند.

احراز هویت و SecretRefها هنگام نصب

  * وقتی احراز هویت توکنی به یک توکن نیاز دارد و `gateway.auth.token` با SecretRef مدیریت می‌شود، `gateway install` اعتبارسنجی می‌کند که SecretRef قابل حل باشد، اما توکن حل‌شده را در فراداده محیط سرویس پایدار نمی‌کند.
  * اگر احراز هویت توکنی به یک توکن نیاز داشته باشد و SecretRef توکن پیکربندی‌شده حل‌نشده باشد، نصب به‌جای پایدار کردن متن ساده جایگزین، به‌صورت بسته شکست می‌خورد.
  * برای احراز هویت گذرواژه در `gateway run`، `OPENCLAW_GATEWAY_PASSWORD`، `--password-file`، یا `gateway.auth.password` پشتیبانی‌شده با SecretRef را به `--password` درون‌خطی ترجیح دهید.
  * در حالت احراز هویت استنباط‌شده، `OPENCLAW_GATEWAY_PASSWORD` فقط در shell الزامات توکن نصب را سست نمی‌کند؛ هنگام نصب یک سرویس مدیریت‌شده از پیکربندی بادوام (`gateway.auth.password` یا پیکربندی `env`) استفاده کنید.
  * اگر هم `gateway.auth.token` و هم `gateway.auth.password` پیکربندی شده باشند و `gateway.auth.mode` تنظیم نشده باشد، نصب تا زمانی که mode صریحاً تنظیم شود مسدود می‌شود.


## کشف Gatewayها (Bonjour)

`gateway discover` به‌دنبال beaconهای Gateway (`_openclaw-gw._tcp`) اسکن می‌کند.

  * Multicast DNS-SD: `local.`
  * Unicast DNS-SD (Wide-Area Bonjour): یک دامنه انتخاب کنید (مثال: `openclaw.internal.`) و split DNS + یک سرور DNS راه‌اندازی کنید؛ [Bonjour](</fa/gateway/bonjour>) را ببینید.


فقط gatewayهایی که کشف Bonjour برایشان فعال است (پیش‌فرض)، beacon را تبلیغ می‌کنند.

رکوردهای کشف wide-area می‌توانند این راهنمایی‌های TXT را شامل شوند:

  * `role` (راهنمای نقش gateway)
  * `transport` (راهنمای transport، مثلاً `gateway`)
  * `gatewayPort` (درگاه WebSocket، معمولاً `18789`)
  * `sshPort` (فقط حالت کشف کامل؛ وقتی وجود ندارد، کلاینت‌ها مقصدهای پیش‌فرض SSH را `22` قرار می‌دهند)
  * `tailnetDns` (نام میزبان MagicDNS، وقتی در دسترس باشد)
  * `gatewayTls` / `gatewayTlsSha256` (TLS فعال + اثرانگشت گواهی)
  * `cliPath` (فقط حالت کشف کامل)


### `gateway discover`

bashCopy code
[code]
    openclaw gateway discover
[/code]

خروجی قابل‌خواندن برای ماشین (همچنین styling/spinner را غیرفعال می‌کند).

مثال‌ها:

bashCopy code
[code]
    openclaw gateway discover --timeout 4000openclaw gateway discover --json | jq '.beacons[].wsUrl'
[/code]

## مرتبط

  * [مرجع CLI](</fa/cli>)
  * [runbook Gateway](</fa/gateway>)


Was this useful?YesNo