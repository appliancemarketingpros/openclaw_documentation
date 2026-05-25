---
title: عامل‌ها
source_url: https://docs.openclaw.ai/fa/cli/agents
scraped_at: 2026-05-25
---

# `openclaw agents`

عامل‌های ایزوله را مدیریت کنید (فضاهای کاری + احراز هویت + مسیریابی).

مرتبط:

  * [مسیریابی چندعاملی](</fa/concepts/multi-agent>)
  * [فضای کاری عامل](</fa/concepts/agent-workspace>)
  * [پیکربندی Skills](</fa/tools/skills-config>): پیکربندی نمایانی مهارت‌ها.


## نمونه‌ها

bashCopy code
[code]
    openclaw agents listopenclaw agents list --bindingsopenclaw agents add work --workspace ~/.openclaw/workspace-workopenclaw agents add ops --workspace ~/.openclaw/workspace-ops --bind telegram:ops --non-interactiveopenclaw agents bindingsopenclaw agents bind --agent work --bind telegram:opsopenclaw agents unbind --agent work --bind telegram:opsopenclaw agents set-identity --workspace ~/.openclaw/workspace --from-identityopenclaw agents set-identity --agent main --avatar avatars/openclaw.pngopenclaw agents delete work
[/code]

## اتصال‌های مسیریابی

از اتصال‌های مسیریابی برای ثابت‌کردن ترافیک ورودی کانال به یک عامل مشخص استفاده کنید.

اگر همچنین می‌خواهید Skills قابل مشاهده برای هر عامل متفاوت باشد، `agents.defaults.skills` و `agents.list[].skills` را در `openclaw.json` پیکربندی کنید. [پیکربندی Skills](</fa/tools/skills-config>) و [مرجع پیکربندی](</fa/gateway/config-agents#agents-defaults-skills>) را ببینید.

فهرست اتصال‌ها:

bashCopy code
[code]
    openclaw agents bindingsopenclaw agents bindings --agent workopenclaw agents bindings --json
[/code]

افزودن اتصال‌ها:

bashCopy code
[code]
    openclaw agents bind --agent work --bind telegram:ops --bind discord:guild-a
[/code]

اگر `accountId` را حذف کنید (`--bind <channel>`)، OpenClaw در صورت دسترس‌بودن، آن را از پیش‌فرض‌های کانال و قلاب‌های راه‌اندازی Plugin حل می‌کند.

اگر برای `bind` یا `unbind` گزینه `--agent` را حذف کنید، OpenClaw عامل پیش‌فرض فعلی را هدف می‌گیرد.

### رفتار دامنه اتصال

  * اتصال بدون `accountId` فقط با حساب پیش‌فرض کانال مطابقت دارد.
  * `accountId: "*"` جایگزین سراسری کانال است (همه حساب‌ها) و از اتصال حساب صریح اختصاصی‌تر نیست.
  * اگر همان عامل از قبل یک اتصال کانال مطابق بدون `accountId` داشته باشد و بعداً با یک `accountId` صریح یا حل‌شده اتصال ایجاد کنید، OpenClaw همان اتصال موجود را درجا ارتقا می‌دهد، به‌جای اینکه یک مورد تکراری اضافه کند.


نمونه:

bashCopy code
[code]
    # initial channel-only bindingopenclaw agents bind --agent work --bind telegram # later upgrade to account-scoped bindingopenclaw agents bind --agent work --bind telegram:ops
[/code]

پس از ارتقا، مسیریابی برای آن اتصال به `telegram:ops` محدود می‌شود. اگر مسیریابی حساب پیش‌فرض را هم می‌خواهید، آن را صریح اضافه کنید (برای نمونه `--bind telegram:default`).

حذف اتصال‌ها:

bashCopy code
[code]
    openclaw agents unbind --agent work --bind telegram:opsopenclaw agents unbind --agent work --all
[/code]

`unbind` یا `--all` را می‌پذیرد یا یک یا چند مقدار `--bind` را، نه هر دو را.

## سطح فرمان

### `agents`

اجرای `openclaw agents` بدون زیرفرمان معادل `openclaw agents list` است.

### `agents list`

گزینه‌ها:

  * `--json`
  * `--bindings`: قواعد کامل مسیریابی را شامل شود، نه فقط شمارش‌ها/خلاصه‌های هر عامل


### `agents add [name]`

گزینه‌ها:

  * `--workspace <dir>`
  * `--model <id>`
  * `--agent-dir <dir>`
  * `--bind <channel[:accountId]>` (قابل تکرار)
  * `--non-interactive`
  * `--json`


نکته‌ها:

  * ارسال هر پرچم افزودن صریح، فرمان را به مسیر غیرتعاملی می‌برد.
  * حالت غیرتعاملی هم به نام عامل و هم به `--workspace` نیاز دارد.
  * `main` رزرو شده است و نمی‌تواند به‌عنوان شناسه عامل جدید استفاده شود.
  * در حالت تعاملی، بذرگذاری احراز هویت فقط پروفایل‌های ایستای قابل حمل را کپی می‌کند (`api_key` و `token` ایستا به‌طور پیش‌فرض). پروفایل‌های OAuth دارای refresh-token فقط از طریق وراثت خواندنی از ذخیره‌گاه واقعی عامل `main` در دسترس می‌مانند. اگر عامل پیش‌فرض پیکربندی‌شده `main` نیست، برای پروفایل‌های OAuth در عامل جدید جداگانه وارد شوید.


### `agents bindings`

گزینه‌ها:

  * `--agent <id>`
  * `--json`


### `agents bind`

گزینه‌ها:

  * `--agent <id>` (به‌طور پیش‌فرض عامل پیش‌فرض فعلی)
  * `--bind <channel[:accountId]>` (قابل تکرار)
  * `--json`


### `agents unbind`

گزینه‌ها:

  * `--agent <id>` (به‌طور پیش‌فرض عامل پیش‌فرض فعلی)
  * `--bind <channel[:accountId]>` (قابل تکرار)
  * `--all`
  * `--json`


### `agents delete <id>`

گزینه‌ها:

  * `--force`
  * `--json`


نکته‌ها:

  * `main` قابل حذف نیست.
  * بدون `--force`، تأیید تعاملی لازم است.
  * فهرست‌های فضای کاری، وضعیت عامل، و رونوشت نشست به Trash منتقل می‌شوند، نه اینکه برای همیشه حذف شوند.
  * وقتی Gateway در دسترس باشد، حذف از طریق Gateway ارسال می‌شود تا پاک‌سازی پیکربندی و ذخیره‌گاه نشست از همان نویسنده ترافیک زمان اجرا استفاده کنند. اگر Gateway در دسترس نباشد، CLI به مسیر محلی آفلاین برمی‌گردد.
  * اگر فضای کاری عامل دیگری همان مسیر باشد، داخل این فضای کاری باشد، یا این فضای کاری را دربر بگیرد، فضای کاری حفظ می‌شود و `--json` موارد `workspaceRetained`، `workspaceRetainedReason`، و `workspaceSharedWith` را گزارش می‌کند.


## فایل‌های هویت

هر فضای کاری عامل می‌تواند در ریشه فضای کاری یک `IDENTITY.md` داشته باشد:

  * مسیر نمونه: `~/.openclaw/workspace/IDENTITY.md`
  * `set-identity --from-identity` از ریشه فضای کاری می‌خواند (یا از یک `--identity-file` صریح)


مسیرهای آواتار نسبت به ریشه فضای کاری حل می‌شوند.

## تنظیم هویت

`set-identity` فیلدها را در `agents.list[].identity` می‌نویسد:

  * `name`
  * `theme`
  * `emoji`
  * `avatar` (مسیر نسبی به فضای کاری، URL با http(s)، یا URI داده)


گزینه‌ها:

  * `--agent <id>`
  * `--workspace <dir>`
  * `--identity-file <path>`
  * `--from-identity`
  * `--name <name>`
  * `--theme <theme>`
  * `--emoji <emoji>`
  * `--avatar <value>`
  * `--json`


نکته‌ها:

  * برای انتخاب عامل هدف می‌توان از `--agent` یا `--workspace` استفاده کرد.
  * اگر به `--workspace` تکیه کنید و چند عامل آن فضای کاری را مشترکاً استفاده کنند، فرمان شکست می‌خورد و از شما می‌خواهد `--agent` را ارسال کنید.
  * وقتی هیچ فیلد هویت صریحی ارائه نشده باشد، فرمان داده‌های هویت را از `IDENTITY.md` می‌خواند.


بارگذاری از `IDENTITY.md`:

bashCopy code
[code]
    openclaw agents set-identity --workspace ~/.openclaw/workspace --from-identity
[/code]

بازنویسی صریح فیلدها:

bashCopy code
[code]
    openclaw agents set-identity --agent main --name "OpenClaw" --emoji "🦞" --avatar avatars/openclaw.png
[/code]

نمونه پیکربندی:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "main",        identity: {          name: "OpenClaw",          theme: "space lobster",          emoji: "🦞",          avatar: "avatars/openclaw.png",        },      },    ],  },}
[/code]

## مرتبط

  * [مرجع CLI](</fa/cli>)
  * [مسیریابی چندعاملی](</fa/concepts/multi-agent>)
  * [فضای کاری عامل](</fa/concepts/agent-workspace>)


Was this useful?YesNo