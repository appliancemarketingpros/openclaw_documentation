---
title: راه‌اندازی اولیه
source_url: https://docs.openclaw.ai/fa/cli/onboard
scraped_at: 2026-05-25
---

# `openclaw onboard`

آنبوردینگ هدایت‌شدهٔ کامل برای راه‌اندازی Gateway محلی یا راه‌دور. وقتی از این استفاده کنید که می‌خواهید OpenClaw احراز هویت مدل، فضای کاری، Gateway، کانال‌ها، Skills و سلامت را در یک جریان مرحله‌به‌مرحله پیش ببرد.

## راهنماهای مرتبط

[**CLI onboarding hub** راهنمای گام‌به‌گام جریان تعاملی CLI. ](</fa/start/wizard>) [**Onboarding overview** اینکه آنبوردینگ OpenClaw چگونه در کنار هم قرار می‌گیرد. ](</fa/start/onboarding-overview>) [**CLI setup reference** خروجی‌ها، سازوکارهای داخلی، و رفتار هر مرحله. ](</fa/start/wizard-cli-reference>) [**CLI automation** پرچم‌های غیرتعاملی و راه‌اندازی‌های اسکریپتی. ](</fa/start/wizard-cli-automation>) [**macOS app onboarding** جریان آنبوردینگ برای برنامهٔ نوار منوی macOS. ](</fa/start/onboarding>)

## نمونه‌ها

bashCopy code
[code]
    openclaw onboardopenclaw onboard --modernopenclaw onboard --flow quickstartopenclaw onboard --flow manualopenclaw onboard --flow importopenclaw onboard --import-from hermes --import-source ~/.hermesopenclaw onboard --skip-bootstrapopenclaw onboard --mode remote --remote-url wss://gateway-host:18789
[/code]

`--flow import` از ارائه‌دهنده‌های مهاجرت متعلق به Plugin مانند Hermes استفاده می‌کند. این گزینه فقط روی یک راه‌اندازی تازهٔ OpenClaw اجرا می‌شود؛ اگر پیکربندی، اعتبارنامه‌ها، نشست‌ها، یا فایل‌های حافظه/هویت فضای کاری موجود باشند، پیش از واردکردن، بازنشانی کنید یا یک راه‌اندازی تازه انتخاب کنید.

`--modern` پیش‌نمایش آنبوردینگ گفت‌وگومحور Crestodian را شروع می‌کند. بدون `--modern`، `openclaw onboard` جریان آنبوردینگ کلاسیک را نگه می‌دارد.

برای مقصدهای plaintext شبکهٔ خصوصی `ws://` (فقط شبکه‌های مورد اعتماد)، `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` را در محیط فرایند آنبوردینگ تنظیم کنید. برای این break-glass انتقال سمت کلاینت، معادل `openclaw.json` وجود ندارد.

ارائه‌دهندهٔ سفارشی غیرتعاملی:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --secret-input-mode plaintext \  --custom-compatibility openai \  --custom-image-input
[/code]

`--custom-api-key` در حالت غیرتعاملی اختیاری است. اگر حذف شود، آنبوردینگ `CUSTOM_API_KEY` را بررسی می‌کند. OpenClaw شناسه‌های رایج مدل‌های بینایی را به‌طور خودکار دارای قابلیت تصویر علامت‌گذاری می‌کند. برای شناسه‌های ناشناختهٔ بینایی سفارشی، `--custom-image-input` را بدهید، یا برای اجبار فرادادهٔ فقط متنی، `--custom-text-input` را بدهید.

LM Studio همچنین در حالت غیرتعاملی از یک پرچم کلید مخصوص ارائه‌دهنده پشتیبانی می‌کند:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice lmstudio \  --custom-base-url "http://localhost:1234/v1" \  --custom-model-id "qwen/qwen3.5-9b" \  --lmstudio-api-key "$LM_API_TOKEN" \  --accept-risk
[/code]

Ollama غیرتعاملی:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice ollama \  --custom-base-url "http://ollama-host:11434" \  --custom-model-id "qwen3.5:27b" \  --accept-risk
[/code]

`--custom-base-url` به‌طور پیش‌فرض `http://127.0.0.1:11434` است. `--custom-model-id` اختیاری است؛ اگر حذف شود، آنبوردینگ از پیش‌فرض‌های پیشنهادی Ollama استفاده می‌کند. شناسه‌های مدل ابری مانند `kimi-k2.5:cloud` نیز اینجا کار می‌کنند.

کلیدهای ارائه‌دهنده را به‌جای plaintext به‌صورت ارجاع ذخیره کنید:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

با `--secret-input-mode ref`، آنبوردینگ به‌جای مقدارهای کلید plaintext، ارجاع‌های مبتنی بر env می‌نویسد. برای ارائه‌دهنده‌های مبتنی بر auth-profile این کار ورودی‌های `keyRef` را می‌نویسد؛ برای ارائه‌دهنده‌های سفارشی، `models.providers.<id>.apiKey` را به‌صورت یک ارجاع env می‌نویسد (برای مثال `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`).

قرارداد حالت `ref` غیرتعاملی:

  * متغیر env ارائه‌دهنده را در محیط فرایند آنبوردینگ تنظیم کنید (برای مثال `OPENAI_API_KEY`).
  * پرچم‌های کلید inline را پاس ندهید (برای مثال `--openai-api-key`) مگر اینکه آن متغیر env نیز تنظیم شده باشد.
  * اگر یک پرچم کلید inline بدون متغیر env لازم پاس داده شود، آنبوردینگ سریعاً با راهنمایی شکست می‌خورد.


گزینه‌های توکن Gateway در حالت غیرتعاملی:

  * `--gateway-auth token --gateway-token <token>` یک توکن plaintext ذخیره می‌کند.
  * `--gateway-auth token --gateway-token-ref-env <name>` مقدار `gateway.auth.token` را به‌صورت یک SecretRef از نوع env ذخیره می‌کند.
  * `--gateway-token` و `--gateway-token-ref-env` با هم ناسازگارند.
  * `--gateway-token-ref-env` به یک متغیر env غیرخالی در محیط فرایند آنبوردینگ نیاز دارد.
  * با `--install-daemon`، وقتی احراز هویت توکنی به توکن نیاز دارد، توکن‌های Gateway مدیریت‌شده با SecretRef اعتبارسنجی می‌شوند اما به‌صورت plaintext حل‌شده در فرادادهٔ محیط سرویس supervisor پایدار نمی‌شوند.
  * با `--install-daemon`، اگر حالت توکن به توکن نیاز داشته باشد و SecretRef توکن پیکربندی‌شده حل‌نشده باشد، آنبوردینگ با راهنمای اصلاح به‌صورت بسته شکست می‌خورد.
  * با `--install-daemon`، اگر هم `gateway.auth.token` و هم `gateway.auth.password` پیکربندی شده باشند و `gateway.auth.mode` تنظیم نشده باشد، آنبوردینگ نصب را تا زمانی که حالت به‌صراحت تنظیم شود مسدود می‌کند.
  * آنبوردینگ محلی `gateway.mode="local"` را در پیکربندی می‌نویسد. اگر فایل پیکربندی بعدی `gateway.mode` را نداشته باشد، آن را خرابی پیکربندی یا ویرایش دستی ناقص بدانید، نه میان‌بر معتبر حالت محلی.
  * آنبوردینگ محلی وقتی مسیر راه‌اندازی انتخاب‌شده به آن‌ها نیاز داشته باشد، Pluginهای قابل دانلود انتخاب‌شده را نصب می‌کند.
  * آنبوردینگ راه‌دور فقط اطلاعات اتصال برای Gateway راه‌دور را می‌نویسد و بسته‌های Plugin محلی را نصب نمی‌کند.
  * `--allow-unconfigured` یک دریچهٔ گریز جداگانه برای runtime Gateway است. این به این معنی نیست که آنبوردینگ می‌تواند `gateway.mode` را حذف کند.


نمونه:

bashCopy code
[code]
    export OPENCLAW_GATEWAY_TOKEN="your-token"openclaw onboard --non-interactive \  --mode local \  --auth-choice skip \  --gateway-auth token \  --gateway-token-ref-env OPENCLAW_GATEWAY_TOKEN \  --accept-risk
[/code]

سلامت Gateway محلی غیرتعاملی:

  * مگر اینکه `--skip-health` را بدهید، آنبوردینگ پیش از خروج موفق، منتظر یک Gateway محلی قابل دسترس می‌ماند.
  * `--install-daemon` ابتدا مسیر نصب Gateway مدیریت‌شده را شروع می‌کند. بدون آن، باید از قبل یک Gateway محلی در حال اجرا داشته باشید، برای مثال `openclaw gateway run`.
  * اگر در automation فقط نوشتن پیکربندی/فضای کاری/bootstrap را می‌خواهید، از `--skip-health` استفاده کنید.
  * اگر فایل‌های فضای کاری را خودتان مدیریت می‌کنید، `--skip-bootstrap` را پاس دهید تا `agents.defaults.skipBootstrap: true` تنظیم شود و ساختن `AGENTS.md`، `SOUL.md`، `TOOLS.md`، `IDENTITY.md`، `USER.md`، `HEARTBEAT.md`، و `BOOTSTRAP.md` رد شود.
  * در Windows بومی، `--install-daemon` ابتدا Scheduled Tasks را امتحان می‌کند و اگر ساخت task رد شود، به یک آیتم ورود پوشهٔ Startup مختص کاربر fallback می‌کند.


رفتار آنبوردینگ تعاملی با حالت ارجاع:

  * وقتی پرسیده شد، **Use secret reference** را انتخاب کنید.
  * سپس یکی از این‌ها را انتخاب کنید: 
    * متغیر محیطی
    * ارائه‌دهندهٔ secret پیکربندی‌شده (`file` یا `exec`)
  * آنبوردینگ پیش از ذخیرهٔ ارجاع، یک اعتبارسنجی preflight سریع انجام می‌دهد. 
    * اگر اعتبارسنجی شکست بخورد، آنبوردینگ خطا را نشان می‌دهد و اجازه می‌دهد دوباره تلاش کنید.


### گزینه‌های endpoint غیرتعاملی [Z.AI](<http://Z.AI>)

bashCopy code
[code]
    # Promptless endpoint selectionopenclaw onboard --non-interactive \  --auth-choice zai-coding-global \  --zai-api-key "$ZAI_API_KEY" # Other Z.AI endpoint choices:# --auth-choice zai-coding-cn# --auth-choice zai-global# --auth-choice zai-cn
[/code]

نمونهٔ Mistral غیرتعاملی:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice mistral-api-key \  --mistral-api-key "$MISTRAL_API_KEY"
[/code]

## یادداشت‌های جریان

Flow types

  * `quickstart`: اعلان‌های کمینه، تولید خودکار یک توکن Gateway.
  * `manual`: اعلان‌های کامل برای port، bind، و auth (نام مستعار `advanced`).
  * `import`: یک ارائه‌دهندهٔ مهاجرت شناسایی‌شده را اجرا می‌کند، طرح را پیش‌نمایش می‌دهد، سپس پس از تأیید اعمال می‌کند.

Provider prefiltering

وقتی یک انتخاب auth یک ارائه‌دهندهٔ ترجیحی را القا کند، آنبوردینگ انتخاب‌گرهای مدل پیش‌فرض و allowlist را به همان ارائه‌دهنده پیش‌فیلتر می‌کند. برای Volcengine و BytePlus، این مورد گونه‌های coding-plan را نیز تطبیق می‌دهد (`volcengine-plan/*`، `byteplus-plan/*`).

اگر فیلتر ارائه‌دهندهٔ ترجیحی هنوز هیچ مدل بارگذاری‌شده‌ای ندهد، آنبوردینگ به‌جای خالی گذاشتن انتخاب‌گر، به catalog بدون فیلتر fallback می‌کند.

Web-search follow-ups

برخی ارائه‌دهنده‌های جست‌وجوی وب، اعلان‌های پیگیری مخصوص ارائه‌دهنده را فعال می‌کنند:

  * **Grok** می‌تواند راه‌اندازی اختیاری `x_search` را با همان `XAI_API_KEY` و یک انتخاب مدل `x_search` پیشنهاد کند.
  * **Kimi** می‌تواند منطقهٔ API Moonshot (`api.moonshot.ai` در برابر `api.moonshot.cn`) و مدل پیش‌فرض جست‌وجوی وب Kimi را بپرسد.

Other behaviors

  * رفتار محدودهٔ DM آنبوردینگ محلی: [مرجع راه‌اندازی CLI](</fa/start/wizard-cli-reference#outputs-and-internals>).
  * سریع‌ترین نخستین گفت‌وگو: `openclaw dashboard` (Control UI، بدون راه‌اندازی کانال).
  * ارائه‌دهندهٔ سفارشی: هر endpoint سازگار با OpenAI یا Anthropic را وصل کنید، از جمله ارائه‌دهنده‌های میزبانی‌شده‌ای که فهرست نشده‌اند. برای تشخیص خودکار از Unknown استفاده کنید.
  * اگر وضعیت Hermes تشخیص داده شود، آنبوردینگ یک جریان مهاجرت پیشنهاد می‌کند. برای طرح‌های dry-run، حالت overwrite، گزارش‌ها، و نگاشت‌های دقیق از [Migrate](</fa/cli/migrate>) استفاده کنید.


## فرمان‌های پیگیری رایج

bashCopy code
[code]
    openclaw channels addopenclaw configureopenclaw agents add <name>
[/code]

وقتی فقط به پیکربندی/فضای کاری پایه نیاز دارید، به‌جای آن از `openclaw setup` استفاده کنید. بعداً برای تغییرات هدفمند از `openclaw configure` و برای راه‌اندازی فقط کانال از `openclaw channels add` استفاده کنید.

Was this useful?YesNo