---
title: هوک‌ها
source_url: https://docs.openclaw.ai/fa/cli/hooks
scraped_at: 2026-05-25
---

# `openclaw hooks`

هوک‌های عامل را مدیریت کنید (اتوماسیون‌های رویدادمحور برای فرمان‌هایی مانند `/new`، `/reset`، و راه‌اندازی Gateway).

اجرای `openclaw hooks` بدون زیرفرمان، معادل `openclaw hooks list` است.

مرتبط:

  * هوک‌ها: [هوک‌ها](</fa/automation/hooks>)
  * هوک‌های Plugin: [هوک‌های Plugin](</fa/plugins/hooks>)


## فهرست همه هوک‌ها

bashCopy code
[code]
    openclaw hooks list
[/code]

همه هوک‌های کشف‌شده از مسیرهای workspace، managed، extra و bundled را فهرست می‌کند. راه‌اندازی Gateway تا زمانی که دست‌کم یک هوک داخلی پیکربندی نشده باشد، handlerهای هوک داخلی را بارگذاری نمی‌کند.

**گزینه‌ها:**

  * `--eligible`: فقط هوک‌های واجد شرایط را نشان بده (نیازمندی‌ها برآورده شده‌اند)
  * `--json`: خروجی به‌صورت JSON
  * `-v, --verbose`: نمایش اطلاعات تفصیلی، شامل نیازمندی‌های مفقود


**نمونه خروجی:**

CodeCopy code
[code]
    Hooks (4/4 ready) Ready:  🚀 boot-md ✓ - Run BOOT.md on gateway startup  📎 bootstrap-extra-files ✓ - Inject extra workspace bootstrap files during agent bootstrap  📝 command-logger ✓ - Log all command events to a centralized audit file  💾 session-memory ✓ - Save session context to memory when /new or /reset command is issued
[/code]

**نمونه (verbose):**

bashCopy code
[code]
    openclaw hooks list --verbose
[/code]

نیازمندی‌های مفقود برای هوک‌های فاقد شرایط را نشان می‌دهد.

**نمونه (JSON):**

bashCopy code
[code]
    openclaw hooks list --json
[/code]

JSON ساختاریافته را برای استفاده برنامه‌نویسی برمی‌گرداند.

## دریافت اطلاعات هوک

bashCopy code
[code]
    openclaw hooks info <name>
[/code]

اطلاعات تفصیلی درباره یک هوک مشخص را نشان می‌دهد.

**آرگومان‌ها:**

  * `<name>`: نام هوک یا کلید هوک (مثلاً `session-memory`)


**گزینه‌ها:**

  * `--json`: خروجی به‌صورت JSON


**نمونه:**

bashCopy code
[code]
    openclaw hooks info session-memory
[/code]

**خروجی:**

CodeCopy code
[code]
    💾 session-memory ✓ Ready Save session context to memory when /new or /reset command is issued Details:  Source: openclaw-bundled  Path: /path/to/openclaw/hooks/bundled/session-memory/HOOK.md  Handler: /path/to/openclaw/hooks/bundled/session-memory/handler.ts  Homepage: https://docs.openclaw.ai/automation/hooks#session-memory  Events: command:new, command:reset Requirements:  Config: ✓ workspace.dir
[/code]

## بررسی واجد شرایط بودن هوک‌ها

bashCopy code
[code]
    openclaw hooks check
[/code]

خلاصه‌ای از وضعیت واجد شرایط بودن هوک‌ها را نشان می‌دهد (چند مورد آماده‌اند و چند مورد آماده نیستند).

**گزینه‌ها:**

  * `--json`: خروجی به‌صورت JSON


**نمونه خروجی:**

CodeCopy code
[code]
    Hooks Status Total hooks: 4Ready: 4Not ready: 0
[/code]

## فعال‌سازی یک هوک

bashCopy code
[code]
    openclaw hooks enable <name>
[/code]

یک هوک مشخص را با افزودن آن به پیکربندی شما فعال می‌کند (`~/.openclaw/openclaw.json` به‌صورت پیش‌فرض).

**نکته:** هوک‌های workspace به‌صورت پیش‌فرض غیرفعال‌اند تا زمانی که اینجا یا در پیکربندی فعال شوند. هوک‌های مدیریت‌شده توسط Pluginها در `openclaw hooks list` مقدار `plugin:<id>` را نشان می‌دهند و اینجا قابل فعال/غیرفعال شدن نیستند. به‌جای آن خود Plugin را فعال/غیرفعال کنید.

**آرگومان‌ها:**

  * `<name>`: نام هوک (مثلاً `session-memory`)


**نمونه:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**خروجی:**

CodeCopy code
[code]
    ✓ Enabled hook: 💾 session-memory
[/code]

**کاری که انجام می‌دهد:**

  * بررسی می‌کند هوک وجود دارد و واجد شرایط است
  * مقدار `hooks.internal.entries.<name>.enabled = true` را در پیکربندی شما به‌روزرسانی می‌کند
  * پیکربندی را روی دیسک ذخیره می‌کند


اگر هوک از `<workspace>/hooks/` آمده باشد، این مرحله opt-in پیش از آن‌که Gateway آن را بارگذاری کند الزامی است.

**پس از فعال‌سازی:**

  * Gateway را بازراه‌اندازی کنید تا هوک‌ها دوباره بارگذاری شوند (بازراه‌اندازی برنامه menu bar در macOS، یا بازراه‌اندازی فرایند Gateway در dev).


## غیرفعال‌سازی یک هوک

bashCopy code
[code]
    openclaw hooks disable <name>
[/code]

یک هوک مشخص را با به‌روزرسانی پیکربندی شما غیرفعال می‌کند.

**آرگومان‌ها:**

  * `<name>`: نام هوک (مثلاً `command-logger`)


**نمونه:**

bashCopy code
[code]
    openclaw hooks disable command-logger
[/code]

**خروجی:**

CodeCopy code
[code]
    ⏸ Disabled hook: 📝 command-logger
[/code]

**پس از غیرفعال‌سازی:**

  * Gateway را بازراه‌اندازی کنید تا هوک‌ها دوباره بارگذاری شوند


## نکته‌ها

  * `openclaw hooks list --json`، `info --json`، و `check --json`، JSON ساختاریافته را مستقیم در stdout می‌نویسند.
  * هوک‌های مدیریت‌شده توسط Pluginها اینجا قابل فعال یا غیرفعال شدن نیستند؛ به‌جای آن Plugin مالک را فعال یا غیرفعال کنید.


## نصب بسته‌های هوک

bashCopy code
[code]
    openclaw plugins install <package>        # npm by defaultopenclaw plugins install npm:<package>    # npm onlyopenclaw plugins install <package> --pin  # pin versionopenclaw plugins install <path>           # local path
[/code]

بسته‌های هوک را از طریق نصب‌کننده یکپارچه Pluginها نصب کنید.

`openclaw hooks install` همچنان به‌عنوان alias سازگاری کار می‌کند، اما یک هشدار deprecation چاپ می‌کند و به `openclaw plugins install` ارسال می‌شود.

مشخصات Npm **فقط registry** هستند (نام بسته + **نسخه دقیق** اختیاری یا **dist-tag**). مشخصات Git/URL/file و بازه‌های semver رد می‌شوند. نصب وابستگی‌ها برای ایمنی به‌صورت project-local و با `--ignore-scripts` اجرا می‌شود، حتی وقتی shell شما تنظیمات نصب npm سراسری داشته باشد.

مشخصات بدون پیشوند و `@latest` روی مسیر stable باقی می‌مانند. اگر npm هرکدام از آن‌ها را به prerelease resolve کند، OpenClaw متوقف می‌شود و از شما می‌خواهد با یک برچسب prerelease مانند `@beta`/`@rc` یا یک نسخه prerelease دقیق، صریحاً opt in کنید.

**کاری که انجام می‌دهد:**

  * بسته هوک را در `~/.openclaw/hooks/<id>` کپی می‌کند
  * هوک‌های نصب‌شده را در `hooks.internal.entries.*` فعال می‌کند
  * نصب را زیر `hooks.internal.installs` ثبت می‌کند


**گزینه‌ها:**

  * `-l, --link`: به‌جای کپی کردن، یک دایرکتوری محلی را link می‌کند (آن را به `hooks.internal.load.extraDirs` اضافه می‌کند)
  * `--pin`: نصب‌های npm را به‌صورت `name@version` دقیق resolve‌شده در `hooks.internal.installs` ثبت می‌کند


**آرشیوهای پشتیبانی‌شده:** `.zip`، `.tgz`، `.tar.gz`، `.tar`

**نمونه‌ها:**

bashCopy code
[code]
    # Local directoryopenclaw plugins install ./my-hook-pack # Local archiveopenclaw plugins install ./my-hook-pack.zip # NPM packageopenclaw plugins install @openclaw/my-hook-pack # Link a local directory without copyingopenclaw plugins install -l ./my-hook-pack
[/code]

بسته‌های هوک link‌شده به‌عنوان هوک‌های managed از یک دایرکتوری پیکربندی‌شده توسط operator در نظر گرفته می‌شوند، نه به‌عنوان هوک‌های workspace.

## به‌روزرسانی بسته‌های هوک

bashCopy code
[code]
    openclaw plugins update <id>openclaw plugins update --all
[/code]

بسته‌های هوک مبتنی بر npm و ردیابی‌شده را از طریق به‌روزرسان یکپارچه Pluginها به‌روزرسانی کنید.

`openclaw hooks update` همچنان به‌عنوان alias سازگاری کار می‌کند، اما یک هشدار deprecation چاپ می‌کند و به `openclaw plugins update` ارسال می‌شود.

**گزینه‌ها:**

  * `--all`: همه بسته‌های هوک ردیابی‌شده را به‌روزرسانی کن
  * `--dry-run`: بدون نوشتن، نشان بده چه چیزی تغییر می‌کند


وقتی hash یکپارچگی ذخیره‌شده وجود داشته باشد و hash artifact دریافت‌شده تغییر کند، OpenClaw یک هشدار چاپ می‌کند و پیش از ادامه تأیید می‌خواهد. برای دور زدن promptها در اجراهای CI/غیرتعاملی از `--yes` سراسری استفاده کنید.

## هوک‌های bundled

### session-memory

وقتی `/new` یا `/reset` را صادر می‌کنید، زمینه session را در memory ذخیره می‌کند.

**فعال‌سازی:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**خروجی:** به‌صورت پیش‌فرض `~/.openclaw/workspace/memory/YYYY-MM-DD-HHMM.md`. برای slugهای نام فایل تولیدشده توسط مدل، `hooks.internal.entries.session-memory.llmSlug: true` را تنظیم کنید.

**ببینید:** [مستندات session-memory](</fa/automation/hooks#session-memory>)

### bootstrap-extra-files

فایل‌های bootstrap اضافی (برای مثال `AGENTS.md` / `TOOLS.md` محلیِ monorepo) را هنگام `agent:bootstrap` تزریق می‌کند.

**فعال‌سازی:**

bashCopy code
[code]
    openclaw hooks enable bootstrap-extra-files
[/code]

**ببینید:** [مستندات bootstrap-extra-files](</fa/automation/hooks#bootstrap-extra-files>)

### command-logger

همه رویدادهای فرمان را در یک فایل audit متمرکز ثبت می‌کند.

**فعال‌سازی:**

bashCopy code
[code]
    openclaw hooks enable command-logger
[/code]

**خروجی:** `~/.openclaw/logs/commands.log`

**مشاهده logها:**

bashCopy code
[code]
    # Recent commandstail -n 20 ~/.openclaw/logs/commands.log # Pretty-printcat ~/.openclaw/logs/commands.log | jq . # Filter by actiongrep '"action":"new"' ~/.openclaw/logs/commands.log | jq .
[/code]

**ببینید:** [مستندات command-logger](</fa/automation/hooks#command-logger>)

### boot-md

وقتی Gateway شروع به کار می‌کند، `BOOT.md` را اجرا می‌کند (پس از شروع channels).

**رویدادها** : `gateway:startup`

**فعال‌سازی** :

bashCopy code
[code]
    openclaw hooks enable boot-md
[/code]

**ببینید:** [مستندات boot-md](</fa/automation/hooks#boot-md>)

## مرتبط

  * [مرجع CLI](</fa/cli>)
  * [هوک‌های اتوماسیون](</fa/automation/hooks>)


Was this useful?YesNo