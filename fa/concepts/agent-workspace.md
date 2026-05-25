---
title: فضای کاری عامل
source_url: https://docs.openclaw.ai/fa/concepts/agent-workspace
scraped_at: 2026-05-25
---

فضای کاری، خانهٔ عامل است. این تنها شاخهٔ کاری‌ای است که برای ابزارهای فایل و زمینهٔ فضای کاری استفاده می‌شود. آن را خصوصی نگه دارید و مانند حافظه با آن رفتار کنید.

این مورد جدا از `~/.openclaw/` است که پیکربندی، اعتبارنامه‌ها و نشست‌ها را ذخیره می‌کند.

## مکان پیش‌فرض

  * پیش‌فرض: `~/.openclaw/workspace`
  * اگر `OPENCLAW_PROFILE` تنظیم شده باشد و `"default"` نباشد، مقدار پیش‌فرض به `~/.openclaw/workspace-<profile>` تبدیل می‌شود.
  * بازنویسی در `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/.openclaw/workspace",    },  },}
[/code]

`openclaw onboard`، `openclaw configure`، یا `openclaw setup` فضای کاری را می‌سازد و اگر فایل‌های راه‌انداز وجود نداشته باشند، آن‌ها را seed می‌کند.

اگر خودتان فایل‌های فضای کاری را مدیریت می‌کنید، می‌توانید ساخت فایل‌های راه‌انداز را غیرفعال کنید:

json5Copy code
[code]
    { agents: { defaults: { skipBootstrap: true } } }
[/code]

## پوشه‌های اضافی فضای کاری

نصب‌های قدیمی‌تر ممکن است `~/openclaw` را ساخته باشند. نگه داشتن چند شاخهٔ فضای کاری می‌تواند باعث ابهام در auth یا drift در state شود، چون در هر زمان فقط یک فضای کاری فعال است.

## نقشهٔ فایل‌های فضای کاری

این‌ها فایل‌های استانداردی هستند که OpenClaw انتظار دارد داخل فضای کاری وجود داشته باشند:

AGENTS.md - دستورالعمل‌های عملیاتی

دستورالعمل‌های عملیاتی برای عامل و اینکه چگونه باید از حافظه استفاده کند. در شروع هر نشست بارگذاری می‌شود. جای مناسبی برای قوانین، اولویت‌ها و جزئیات «چگونه رفتار کردن» است.

SOUL.md - شخصیت و لحن

شخصیت، لحن و مرزها. در هر نشست بارگذاری می‌شود. راهنما: [راهنمای شخصیت SOUL.md](</fa/concepts/soul>).

USER.md - کاربر کیست

کاربر کیست و چگونه باید خطاب شود. در هر نشست بارگذاری می‌شود.

IDENTITY.md - نام، حال‌وهوا، ایموجی

نام، حال‌وهوا و ایموجی عامل. در طول آیین راه‌اندازی ساخته/به‌روزرسانی می‌شود.

TOOLS.md - قراردادهای ابزار محلی

یادداشت‌هایی دربارهٔ ابزارها و قراردادهای محلی شما. دسترس‌پذیری ابزارها را کنترل نمی‌کند؛ فقط راهنماست.

HEARTBEAT.md - چک‌لیست Heartbeat

چک‌لیست کوچک اختیاری برای اجراهای Heartbeat. آن را کوتاه نگه دارید تا از مصرف توکن جلوگیری شود.

BOOT.md - چک‌لیست شروع

چک‌لیست شروع اختیاری که هنگام restart شدن Gateway به‌صورت خودکار اجرا می‌شود (وقتی [hookهای داخلی](</fa/automation/hooks>) فعال باشند). آن را کوتاه نگه دارید؛ برای ارسال‌های خروجی از ابزار message استفاده کنید.

BOOTSTRAP.md - آیین اجرای نخست

آیین یک‌بارهٔ اجرای نخست. فقط برای یک فضای کاری کاملاً جدید ساخته می‌شود. پس از کامل شدن آیین، آن را حذف کنید.

memory/YYYY-MM-DD.md - لاگ روزانهٔ حافظه

لاگ روزانهٔ حافظه (یک فایل برای هر روز). توصیه می‌شود در شروع نشست، امروز + دیروز را بخوانید.

MEMORY.md - حافظهٔ بلندمدت گزینش‌شده (اختیاری)

حافظهٔ بلندمدت گزینش‌شده: واقعیت‌های پایدار، ترجیحات، تصمیم‌ها و خلاصه‌های کوتاه. لاگ‌های دقیق را در `memory/YYYY-MM-DD.md` نگه دارید تا ابزارهای حافظه بتوانند هنگام نیاز آن‌ها را بازیابی کنند بدون اینکه به هر prompt تزریق شوند. `MEMORY.md` را فقط در نشست اصلی و خصوصی بارگذاری کنید (نه زمینه‌های اشتراکی/گروهی). برای گردش‌کار و flush خودکار حافظه، [حافظه](</fa/concepts/memory>) را ببینید.

skills/ - Skills فضای کاری (اختیاری)

Skills مخصوص فضای کاری. مکان Skills با بالاترین اولویت برای آن فضای کاری. وقتی نام‌ها تداخل داشته باشند، Skills عامل پروژه، Skills عامل شخصی، Skills مدیریت‌شده، Skills باندل‌شده و `skills.load.extraDirs` را override می‌کند.

canvas/ - فایل‌های Canvas UI (اختیاری)

فایل‌های Canvas UI برای نمایش‌های node (برای مثال `canvas/index.html`).

## چه چیزهایی در فضای کاری نیستند

این موارد زیر `~/.openclaw/` قرار دارند و نباید به repo فضای کاری commit شوند:

  * `~/.openclaw/openclaw.json` (پیکربندی)
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` (پروفایل‌های auth مدل: OAuth + API keys)
  * `~/.openclaw/agents/<agentId>/agent/codex-home/` (حساب runtime، پیکربندی، Skills، plugins و state بومی thread برای هر عامل در Codex)
  * `~/.openclaw/credentials/` (state کانال/provider به‌علاوهٔ داده‌های import قدیمی OAuth)
  * `~/.openclaw/agents/<agentId>/sessions/` (رونوشت‌های نشست + metadata)
  * `~/.openclaw/skills/` (Skills مدیریت‌شده)


اگر باید نشست‌ها یا پیکربندی را migrate کنید، آن‌ها را جداگانه کپی کنید و بیرون از version control نگه دارید.

## پشتیبان‌گیری Git (توصیه‌شده، خصوصی)

با فضای کاری مانند حافظهٔ خصوصی رفتار کنید. آن را در یک repo **خصوصی** git قرار دهید تا پشتیبان‌گیری شود و قابل بازیابی باشد.

این مراحل را روی دستگاهی اجرا کنید که Gateway روی آن اجرا می‌شود (همان‌جایی که فضای کاری قرار دارد).

* ### مقداردهی اولیهٔ repo

اگر git نصب شده باشد، فضای کاری‌های کاملاً جدید به‌صورت خودکار مقداردهی اولیه می‌شوند. اگر این فضای کاری هنوز repo نیست، اجرا کنید:

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.md SOUL.md TOOLS.md IDENTITY.md USER.md HEARTBEAT.md memory/git commit -m "Add agent workspace"
[/code]

* ### افزودن remote خصوصی

### GitHub web UI

  1. یک repository **خصوصی** جدید روی GitHub بسازید.
  2. آن را با README مقداردهی اولیه نکنید (از merge conflict جلوگیری می‌کند).
  3. URL مربوط به HTTPS remote را کپی کنید.
  4. remote را اضافه کنید و push کنید:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

### GitHub CLI (gh)

bashCopy code
[code]
    gh auth logingh repo create openclaw-workspace --private --source . --remote origin --push
[/code]

### GitLab web UI

  1. یک repository **خصوصی** جدید روی GitLab بسازید.
  2. آن را با README مقداردهی اولیه نکنید (از merge conflict جلوگیری می‌کند).
  3. URL مربوط به HTTPS remote را کپی کنید.
  4. remote را اضافه کنید و push کنید:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

* ### به‌روزرسانی‌های مداوم

bashCopy code
[code]
    git statusgit add .git commit -m "Update memory"git push
[/code]

## secrets را commit نکنید

شروع پیشنهادی برای `.gitignore`:

gitignoreCopy code
[code]
    .DS_Store.env**/*.key**/*.pem**/secrets*
[/code]

## انتقال فضای کاری به دستگاه جدید

* ### Clone کردن repo

repo را به مسیر موردنظر clone کنید (پیش‌فرض `~/.openclaw/workspace`).

* ### به‌روزرسانی پیکربندی

`agents.defaults.workspace` را در `~/.openclaw/openclaw.json` روی آن مسیر تنظیم کنید.

* ### Seed کردن فایل‌های گم‌شده

برای seed کردن هر فایل گم‌شده‌ای، `openclaw setup --workspace <path>` را اجرا کنید.

* ### کپی نشست‌ها (اختیاری)

اگر به نشست‌ها نیاز دارید، `~/.openclaw/agents/<agentId>/sessions/` را جداگانه از دستگاه قدیمی کپی کنید.

## یادداشت‌های پیشرفته

  * routing چندعاملی می‌تواند برای هر عامل از فضای کاری‌های متفاوت استفاده کند. برای پیکربندی routing، [Channel routing](</fa/channels/channel-routing>) را ببینید.
  * اگر `agents.defaults.sandbox` فعال باشد، نشست‌های غیر اصلی می‌توانند از فضای کاری‌های sandbox مخصوص هر نشست زیر `agents.defaults.sandbox.workspaceRoot` استفاده کنند.


## مرتبط

  * [Heartbeat](</fa/gateway/heartbeat>) \- فایل فضای کاری [HEARTBEAT.md](<http://HEARTBEAT.md>)
  * [Sandboxing](</fa/gateway/sandboxing>) \- دسترسی به فضای کاری در محیط‌های sandboxشده
  * [نشست](</fa/concepts/session>) \- مسیرهای ذخیره‌سازی نشست
  * [دستورهای پایدار](</fa/automation/standing-orders>) \- دستورالعمل‌های پایدار در فایل‌های فضای کاری


Was this useful?YesNo