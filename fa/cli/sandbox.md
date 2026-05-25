---
title: CLI محیط ایزوله
source_url: https://docs.openclaw.ai/fa/cli/sandbox
scraped_at: 2026-05-25
---

مدیریت زمان‌اجراهای sandbox برای اجرای ایزولهٔ عامل.

## نمای کلی

OpenClaw می‌تواند برای امنیت، عامل‌ها را در زمان‌اجراهای sandbox ایزوله اجرا کند. دستورهای `sandbox` به شما کمک می‌کنند پس از به‌روزرسانی‌ها یا تغییرات پیکربندی، این زمان‌اجراها را بررسی و بازایجاد کنید.

امروز این معمولاً یعنی:

  * کانتینرهای sandbox در Docker
  * زمان‌اجراهای sandbox مبتنی بر SSH وقتی `agents.defaults.sandbox.backend = "ssh"`
  * زمان‌اجراهای sandbox مبتنی بر OpenShell وقتی `agents.defaults.sandbox.backend = "openshell"`


برای `ssh` و OpenShell `remote`، بازایجاد از Docker مهم‌تر است:

  * فضای کاری راه‌دور پس از seed اولیه، مرجع اصلی است
  * `openclaw sandbox recreate` آن فضای کاری راه‌دور مرجع را برای دامنهٔ انتخاب‌شده حذف می‌کند
  * استفادهٔ بعدی دوباره آن را از فضای کاری محلی فعلی seed می‌کند


## دستورها

### `openclaw sandbox explain`

حالت/دامنه/دسترسی فضای کاری **مؤثر** sandbox، سیاست ابزار sandbox، و دروازه‌های elevated را بررسی کنید (همراه با مسیرهای کلید پیکربندی برای رفع مشکل).

bashCopy code
[code]
    openclaw sandbox explainopenclaw sandbox explain --session agent:main:mainopenclaw sandbox explain --agent workopenclaw sandbox explain --json
[/code]

### `openclaw sandbox list`

همهٔ زمان‌اجراهای sandbox را همراه با وضعیت و پیکربندی آن‌ها فهرست کنید.

bashCopy code
[code]
    openclaw sandbox listopenclaw sandbox list --browser  # List only browser containersopenclaw sandbox list --json     # JSON output
[/code]

**خروجی شامل این موارد است:**

  * نام و وضعیت زمان‌اجرا
  * بک‌اند (`docker`، `openshell` و غیره)
  * برچسب پیکربندی و این‌که آیا با پیکربندی فعلی مطابقت دارد یا نه
  * سن (زمان سپری‌شده از ایجاد)
  * زمان بیکاری (زمان سپری‌شده از آخرین استفاده)
  * نشست/عامل مرتبط


### `openclaw sandbox recreate`

زمان‌اجراهای sandbox را حذف کنید تا با پیکربندی به‌روزشده دوباره ایجاد شوند.

bashCopy code
[code]
    openclaw sandbox recreate --all                # Recreate all containersopenclaw sandbox recreate --session main       # Specific sessionopenclaw sandbox recreate --agent mybot        # Specific agentopenclaw sandbox recreate --browser            # Only browser containersopenclaw sandbox recreate --all --force        # Skip confirmation
[/code]

**گزینه‌ها:**

  * `--all`: بازایجاد همهٔ کانتینرهای sandbox
  * `--session <key>`: بازایجاد کانتینر برای نشست مشخص
  * `--agent <id>`: بازایجاد کانتینرها برای عامل مشخص
  * `--browser`: فقط بازایجاد کانتینرهای مرورگر
  * `--force`: رد کردن درخواست تأیید


## موارد استفاده

### پس از به‌روزرسانی یک تصویر Docker

bashCopy code
[code]
    # Pull new imagedocker pull openclaw-sandbox:latestdocker tag openclaw-sandbox:latest openclaw-sandbox:bookworm-slim # Update config to use new image# Edit config: agents.defaults.sandbox.docker.image (or agents.list[].sandbox.docker.image) # Recreate containersopenclaw sandbox recreate --all
[/code]

### پس از تغییر پیکربندی sandbox

bashCopy code
[code]
    # Edit config: agents.defaults.sandbox.* (or agents.list[].sandbox.*) # Recreate to apply new configopenclaw sandbox recreate --all
[/code]

### پس از تغییر مقصد SSH یا مواد احراز هویت SSH

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - agents.defaults.sandbox.ssh.target# - agents.defaults.sandbox.ssh.workspaceRoot# - agents.defaults.sandbox.ssh.identityFile / certificateFile / knownHostsFile# - agents.defaults.sandbox.ssh.identityData / certificateData / knownHostsData openclaw sandbox recreate --all
[/code]

برای بک‌اند اصلی `ssh`، بازایجاد ریشهٔ فضای کاری راه‌دور مختص هر دامنه را روی مقصد SSH حذف می‌کند. اجرای بعدی دوباره آن را از فضای کاری محلی seed می‌کند.

### پس از تغییر منبع، سیاست، یا حالت OpenShell

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - plugins.entries.openshell.config.from# - plugins.entries.openshell.config.mode# - plugins.entries.openshell.config.policy openclaw sandbox recreate --all
[/code]

برای حالت OpenShell `remote`، بازایجاد فضای کاری راه‌دور مرجع را برای آن دامنه حذف می‌کند. اجرای بعدی دوباره آن را از فضای کاری محلی seed می‌کند.

### پس از تغییر setupCommand

bashCopy code
[code]
    openclaw sandbox recreate --all# or just one agent:openclaw sandbox recreate --agent family
[/code]

### فقط برای یک عامل مشخص

bashCopy code
[code]
    # Update only one agent's containersopenclaw sandbox recreate --agent alfred
[/code]

## چرا این لازم است

وقتی پیکربندی sandbox را به‌روزرسانی می‌کنید:

  * زمان‌اجراهای موجود با تنظیمات قدیمی به کار ادامه می‌دهند.
  * زمان‌اجراها فقط پس از ۲۴ ساعت بی‌استفاده بودن پاک‌سازی می‌شوند.
  * عامل‌هایی که مرتب استفاده می‌شوند، زمان‌اجراهای قدیمی را برای مدت نامحدود زنده نگه می‌دارند.


از `openclaw sandbox recreate` استفاده کنید تا حذف زمان‌اجراهای قدیمی را اجبار کنید. آن‌ها در زمان نیاز بعدی، به‌صورت خودکار با تنظیمات فعلی بازایجاد می‌شوند.

## مهاجرت رجیستری

OpenClaw فرادادهٔ زمان‌اجرای sandbox را به‌صورت یک shard JSON برای هر ورودی کانتینر/مرورگر، زیر دایرکتوری وضعیت sandbox ذخیره می‌کند. نصب‌های قدیمی‌تر ممکن است هنوز فایل‌های قدیمی یکپارچه داشته باشند:

  * `~/.openclaw/sandbox/containers.json`
  * `~/.openclaw/sandbox/browsers.json`


خواندن‌های معمول زمان‌اجرای sandbox این فایل‌ها را بازنویسی نمی‌کنند. برای مهاجرت ورودی‌های قدیمی معتبر به دایرکتوری‌های رجیستری shardشده، `openclaw doctor --fix` را اجرا کنید. فایل‌های قدیمی نامعتبر قرنطینه می‌شوند تا یک رجیستری قدیمی خراب نتواند ورودی‌های زمان‌اجرای فعلی را پنهان کند.

## پیکربندی

تنظیمات sandbox در `~/.openclaw/openclaw.json` زیر `agents.defaults.sandbox` قرار دارند (بازنویسی‌های مختص هر عامل در `agents.list[].sandbox` قرار می‌گیرند):

jsoncCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "all", // off, non-main, all        "backend": "docker", // docker, ssh, openshell        "scope": "agent", // session, agent, shared        "docker": {          "image": "openclaw-sandbox:bookworm-slim",          "containerPrefix": "openclaw-sbx-",          // ... more Docker options        },        "prune": {          "idleHours": 24, // Auto-prune after 24h idle          "maxAgeDays": 7, // Auto-prune after 7 days        },      },    },  },}
[/code]

## مرتبط

  * [مرجع CLI](</fa/cli>)
  * [sandboxing](</fa/gateway/sandboxing>)
  * [فضای کاری عامل](</fa/concepts/agent-workspace>)
  * [Doctor](</fa/gateway/doctor>): راه‌اندازی sandbox را بررسی می‌کند.


Was this useful?YesNo