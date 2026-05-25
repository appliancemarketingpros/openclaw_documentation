---
title: پیکربندی
source_url: https://docs.openclaw.ai/fa/cli/config
scraped_at: 2026-05-25
---

راهنماهای پیکربندی برای ویرایش‌های غیرتعاملی در `openclaw.json`: دریافت/تنظیم/وصله‌کردن/حذف‌کردن/فایل/طرحواره/اعتبارسنجی مقادیر بر اساس مسیر و چاپ فایل پیکربندی فعال. بدون زیرفرمان اجرا کنید تا جادوگر پیکربندی باز شود (همانند `openclaw configure`).

## گزینه‌های ریشه

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tc2VjdGlvbiA8c2VjdGlvbg " type="string"> فیلتر بخش راه‌اندازی هدایت‌شده که قابل تکرار است، زمانی که `openclaw config` را بدون زیرفرمان اجرا می‌کنید.

بخش‌های هدایت‌شده پشتیبانی‌شده: `workspace`، `model`، `web`، `gateway`، `daemon`، `channels`، `plugins`، `skills`، `health`.

## نمونه‌ها

bashCopy code
[code]
    openclaw config fileopenclaw config --section modelopenclaw config --section gateway --section daemonopenclaw config schemaopenclaw config get browser.executablePathopenclaw config set browser.executablePath "/usr/bin/google-chrome"openclaw config set browser.profiles.work.executablePath "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"openclaw config set agents.defaults.heartbeat.every "2h"openclaw config set agents.list[0].tools.exec.node "node-id-or-name"openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKENopenclaw config set secrets.providers.vaultfile --provider-source file --provider-path /etc/openclaw/secrets.json --provider-mode jsonopenclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config unset plugins.entries.brave.config.webSearch.apiKeyopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKEN --dry-runopenclaw config validateopenclaw config validate --json
[/code]

### `config schema`

طرحواره JSON تولیدشده برای `openclaw.json` را به‌صورت JSON در stdout چاپ می‌کند.

What it includes

  * طرحواره پیکربندی ریشه فعلی، به‌همراه یک فیلد رشته‌ای ریشه `$schema` برای ابزارهای ویرایشگر.
  * فراداده مستندات `title` و `description` فیلد که توسط Control UI استفاده می‌شود.
  * گره‌های آبجکت تودرتو، wildcard (`*`) و آیتم آرایه (`[]`) وقتی مستندات فیلد متناظر وجود داشته باشد، همان فراداده `title` / `description` را به ارث می‌برند.
  * شاخه‌های `anyOf` / `oneOf` / `allOf` نیز وقتی مستندات فیلد متناظر وجود داشته باشد، همان فراداده مستندات را به ارث می‌برند.
  * فراداده طرحواره زنده Plugin + کانال به‌صورت best-effort، وقتی manifestهای runtime قابل بارگذاری باشند.
  * یک طرحواره جایگزین تمیز حتی وقتی پیکربندی فعلی نامعتبر باشد.

Related runtime RPC

`config.schema.lookup` یک مسیر پیکربندی نرمال‌شده را همراه با یک گره طرحواره کم‌عمق (`title`، `description`، `type`، `enum`، `const`، کران‌های رایج)، فراداده راهنمای UI متناظر، و خلاصه‌های فرزند بلافاصله برمی‌گرداند. از آن برای واکاوی محدود به مسیر در Control UI یا کلاینت‌های سفارشی استفاده کنید.

bashCopy code
[code]
    openclaw config schema
[/code]

وقتی می‌خواهید آن را با ابزارهای دیگر بررسی یا اعتبارسنجی کنید، آن را به یک فایل pipe کنید:

bashCopy code
[code]
    openclaw config schema > openclaw.schema.json
[/code]

### مسیرها

مسیرها از نشانه‌گذاری نقطه‌ای یا کروشه‌ای استفاده می‌کنند:

bashCopy code
[code]
    openclaw config get agents.defaults.workspaceopenclaw config get agents.list[0].id
[/code]

برای هدف‌گیری یک Agent مشخص، از اندیس فهرست Agent استفاده کنید:

bashCopy code
[code]
    openclaw config get agents.listopenclaw config set agents.list[1].tools.exec.node "node-id-or-name"
[/code]

## مقادیر

مقادیر در صورت امکان به‌عنوان JSON5 تجزیه می‌شوند؛ در غیر این صورت به‌عنوان رشته در نظر گرفته می‌شوند. برای الزام تجزیه JSON5 از `--strict-json` استفاده کنید. `--json` همچنان به‌عنوان نام مستعار قدیمی پشتیبانی می‌شود.

bashCopy code
[code]
    openclaw config set agents.defaults.heartbeat.every "0m"openclaw config set gateway.port 19001 --strict-jsonopenclaw config set channels.whatsapp.groups '["*"]' --strict-json
[/code]

`config get <path> --json` مقدار خام را به‌جای متن قالب‌بندی‌شده ترمینال، به‌صورت JSON چاپ می‌کند.

هنگام افزودن ورودی به این mapها از `--merge` استفاده کنید:

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set models.providers.ollama.models '[{"id":"llama3.2","name":"Llama 3.2"}]' --strict-json --merge
[/code]

فقط وقتی از `--replace` استفاده کنید که عمداً می‌خواهید مقدار ارائه‌شده به مقدار کامل هدف تبدیل شود.

## حالت‌های `config set`

`openclaw config set` از چهار سبک انتساب پشتیبانی می‌کند:

### Value mode

bashCopy code
[code]
    openclaw config set <path> <value>
[/code]

### SecretRef builder mode

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN
[/code]

### Provider builder mode

حالت سازنده Provider فقط مسیرهای `secrets.providers.<alias>` را هدف می‌گیرد:

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-timeout-ms 5000
[/code]

### Batch mode

bashCopy code
[code]
    openclaw config set --batch-json '[  {    "path": "secrets.providers.default",    "provider": { "source": "env" }  },  {    "path": "channels.discord.token",    "ref": { "source": "env", "provider": "default", "id": "DISCORD_BOT_TOKEN" }  }]'
[/code]

bashCopy code
[code]
    openclaw config set --batch-file ./config-set.batch.json --dry-run
[/code]

تجزیه دسته‌ای همیشه از payload دسته‌ای (`--batch-json`/`--batch-file`) به‌عنوان منبع حقیقت استفاده می‌کند. `--strict-json` / `--json` رفتار تجزیه دسته‌ای را تغییر نمی‌دهند.

## `config patch`

وقتی می‌خواهید به‌جای اجرای تعداد زیادی فرمان `config set` مبتنی بر مسیر، یک وصله به‌شکل پیکربندی را paste یا pipe کنید، از `config patch` استفاده کنید. ورودی یک آبجکت JSON5 است. آبجکت‌ها به‌صورت بازگشتی merge می‌شوند، آرایه‌ها و مقادیر scalar مقدار هدف را جایگزین می‌کنند، و `null` مسیر هدف را حذف می‌کند.

bashCopy code
[code]
    openclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config patch --file ./openclaw.patch.json5
[/code]

همچنین می‌توانید یک وصله را از طریق stdin pipe کنید، که برای اسکریپت‌های راه‌اندازی راه‌دور مفید است:

bashCopy code
[code]
    ssh openclaw-host 'openclaw config patch --stdin --dry-run' < ./openclaw.patch.json5ssh openclaw-host 'openclaw config patch --stdin' < ./openclaw.patch.json5
[/code]

نمونه وصله:

json5Copy code
[code]
    {  channels: {    slack: {      enabled: true,      mode: "socket",      botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },      appToken: { source: "env", provider: "default", id: "SLACK_APP_TOKEN" },      groupPolicy: "open",      requireMention: false,    },    discord: {      enabled: true,      token: { source: "env", provider: "default", id: "DISCORD_BOT_TOKEN" },      dmPolicy: "disabled",      dm: { enabled: false },      groupPolicy: "allowlist",    },  },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },      models: {        "openai/gpt-5.5": { params: { fastMode: true } },      },    },  },}
[/code]

وقتی یک آبجکت یا آرایه باید به‌جای وصله بازگشتی، دقیقاً به مقدار ارائه‌شده تبدیل شود، از `--replace-path <path>` استفاده کنید:

bashCopy code
[code]
    openclaw config patch --file ./discord.patch.json5 --replace-path 'channels.discord.guilds["123"].channels'
[/code]

`--dry-run` بررسی‌های طرحواره و قابلیت resolve شدن SecretRef را بدون نوشتن اجرا می‌کند. SecretRefهای مبتنی بر exec هنگام dry-run به‌صورت پیش‌فرض نادیده گرفته می‌شوند؛ وقتی عمداً می‌خواهید dry-run فرمان‌های provider را اجرا کند، `--allow-exec` را اضافه کنید.

حالت مسیر/مقدار JSON همچنان هم برای SecretRefها و هم providerها پشتیبانی می‌شود:

bashCopy code
[code]
    openclaw config set channels.discord.token \  '{"source":"env","provider":"default","id":"DISCORD_BOT_TOKEN"}' \  --strict-json openclaw config set secrets.providers.vaultfile \  '{"source":"file","path":"/etc/openclaw/secrets.json","mode":"json"}' \  --strict-json
[/code]

## پرچم‌های سازنده Provider

هدف‌های سازنده Provider باید از `secrets.providers.<alias>` به‌عنوان مسیر استفاده کنند.

Common flags

  * `--provider-source <env|file|exec>`
  * `--provider-timeout-ms <ms>` (`file`, `exec`)

Env provider (--provider-source env)

  * `--provider-allowlist &lt;ENV_VAR&gt;` (قابل تکرار)

File provider (--provider-source file)

  * `--provider-path <path>` (الزامی)
  * `--provider-mode <singleValue|json>`
  * `--provider-max-bytes <bytes>`
  * `--provider-allow-insecure-path`

Exec provider (--provider-source exec)

  * `--provider-command <path>` (الزامی)
  * `--provider-arg <arg>` (قابل تکرار)
  * `--provider-no-output-timeout-ms <ms>`
  * `--provider-max-output-bytes <bytes>`
  * `--provider-json-only`
  * `--provider-env &lt;KEY=VALUE&gt;` (قابل تکرار)
  * `--provider-pass-env &lt;ENV_VAR&gt;` (قابل تکرار)
  * `--provider-trusted-dir <path>` (قابل تکرار)
  * `--provider-allow-insecure-path`
  * `--provider-allow-symlink-command`


نمونه provider سخت‌سازی‌شده مبتنی بر exec:

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-json-only \  --provider-pass-env VAULT_TOKEN \  --provider-trusted-dir /usr/local/bin \  --provider-timeout-ms 5000
[/code]

## Dry run

برای اعتبارسنجی تغییرات بدون نوشتن در `openclaw.json` از `--dry-run` استفاده کنید.

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run \  --json openclaw config set channels.discord.token \  --ref-provider vault \  --ref-source exec \  --ref-id discord/token \  --dry-run \  --allow-exec
[/code]

Dry-run behavior

  * حالت سازنده: بررسی‌های قابلیت resolve شدن SecretRef را برای refs/providers تغییریافته اجرا می‌کند.
  * حالت JSON (`--strict-json`، `--json`، یا حالت دسته‌ای): اعتبارسنجی طرحواره به‌همراه بررسی‌های قابلیت resolve شدن SecretRef را اجرا می‌کند.
  * اعتبارسنجی policy نیز برای سطوح هدف SecretRef شناخته‌شده و پشتیبانی‌نشده اجرا می‌شود.
  * بررسی‌های policy کل پیکربندی پس از تغییر را ارزیابی می‌کنند، بنابراین نوشتن آبجکت والد (برای مثال تنظیم `hooks` به‌عنوان یک آبجکت) نمی‌تواند اعتبارسنجی سطح پشتیبانی‌نشده را دور بزند.
  * بررسی‌های SecretRef مبتنی بر exec هنگام dry-run به‌صورت پیش‌فرض نادیده گرفته می‌شوند تا از اثرات جانبی فرمان جلوگیری شود.
  * برای opt in به بررسی‌های SecretRef مبتنی بر exec از `--allow-exec` همراه با `--dry-run` استفاده کنید (این ممکن است فرمان‌های provider را اجرا کند).
  * `--allow-exec` فقط برای dry-run است و اگر بدون `--dry-run` استفاده شود خطا می‌دهد.

\--dry-run --json fields

`--dry-run --json` یک گزارش قابل خواندن توسط ماشین چاپ می‌کند:

  * `ok`: اینکه اجرای آزمایشی موفق بوده است یا نه
  * `operations`: تعداد انتساب‌های ارزیابی‌شده
  * `checks`: اینکه بررسی‌های schema/resolvability اجرا شده‌اند یا نه
  * `checks.resolvabilityComplete`: اینکه بررسی‌های resolvability تا پایان اجرا شده‌اند یا نه (وقتی ارجاع‌های exec نادیده گرفته می‌شوند false است)
  * `refsChecked`: تعداد ارجاع‌هایی که واقعا در طول اجرای آزمایشی resolve شده‌اند
  * `skippedExecRefs`: تعداد ارجاع‌های exec که چون `--allow-exec` تنظیم نشده بود نادیده گرفته شدند
  * `errors`: خطاهای ساختاریافته schema/resolvability وقتی `ok=false`


### شکل خروجی JSON

json5Copy code
[code]
    {  ok: boolean,  operations: number,  configPath: string,  inputModes: ["value" | "json" | "builder", ...],  checks: {    schema: boolean,    resolvability: boolean,    resolvabilityComplete: boolean,  },  refsChecked: number,  skippedExecRefs: number,  errors?: [    {      kind: "schema" | "resolvability",      message: string,      ref?: string, // present for resolvability errors    },  ],}
[/code]

### Success example

jsonCopy code
[code]
    {  "ok": true,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0}
[/code]

### Failure example

jsonCopy code
[code]
    {  "ok": false,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0,  "errors": [    {      "kind": "resolvability",      "message": "Error: Environment variable \"MISSING_TEST_SECRET\" is not set.",      "ref": "env:default:MISSING_TEST_SECRET"    }  ]}
[/code]

If dry-run fails

  * `config schema validation failed`: شکل پیکربندی پس از تغییر نامعتبر است؛ مسیر/مقدار یا شکل شیء provider/ref را اصلاح کنید.
  * `Config policy validation failed: unsupported SecretRef usage`: آن اعتبارنامه را دوباره به ورودی plaintext/string منتقل کنید و SecretRefها را فقط روی سطح‌های پشتیبانی‌شده نگه دارید.
  * `SecretRef assignment(s) could not be resolved`: provider/ref ارجاع‌شده در حال حاضر نمی‌تواند resolve شود (متغیر محیطی جاافتاده، اشاره‌گر فایل نامعتبر، خرابی provider اجرایی، یا ناهماهنگی provider/source).
  * `Dry run note: skipped <n> exec SecretRef resolvability check(s)`: اجرای آزمایشی ارجاع‌های exec را نادیده گرفت؛ اگر به اعتبارسنجی resolvability برای exec نیاز دارید، دوباره با `--allow-exec` اجرا کنید.
  * برای حالت batch، ورودی‌های ناموفق را اصلاح کنید و پیش از نوشتن، `--dry-run` را دوباره اجرا کنید.


## ایمنی نوشتن

`openclaw config set` و دیگر نویسنده‌های پیکربندی متعلق به OpenClaw، پیش از ثبت کردن پیکربندی روی دیسک، کل پیکربندی پس از تغییر را اعتبارسنجی می‌کنند. اگر payload جدید در اعتبارسنجی schema ناموفق شود یا شبیه clobber مخرب به نظر برسد، پیکربندی فعال دست‌نخورده می‌ماند و payload ردشده در کنار آن با نام `openclaw.json.rejected.*` ذخیره می‌شود.

برای ویرایش‌های کوچک، نوشتن با CLI را ترجیح دهید:

bashCopy code
[code]
    openclaw config set gateway.reload.mode hybrid --dry-runopenclaw config set gateway.reload.mode hybridopenclaw config validate
[/code]

اگر نوشتن رد شد، payload ذخیره‌شده را بررسی کنید و شکل کامل پیکربندی را اصلاح کنید:

bashCopy code
[code]
    CONFIG="$(openclaw config file)"ls -lt "$CONFIG".rejected.* 2>/dev/null | headopenclaw config validate
[/code]

نوشتن مستقیم با ویرایشگر همچنان مجاز است، اما Gateway در حال اجرا تا زمان اعتبارسنجی، آن‌ها را نامطمئن تلقی می‌کند. ویرایش‌های مستقیم نامعتبر باعث شکست راه‌اندازی می‌شوند یا در hot reload نادیده گرفته می‌شوند؛ Gateway فایل `openclaw.json` را بازنویسی نمی‌کند. برای ترمیم پیکربندی دارای پیشوند/خراب‌شده یا بازیابی آخرین نسخه سالم شناخته‌شده، `openclaw doctor --fix` را اجرا کنید. [عیب‌یابی Gateway](</fa/gateway/troubleshooting#gateway-rejected-invalid-config>) را ببینید.

بازیابی کل فایل فقط برای ترمیم با doctor محفوظ است. تغییرات schema مربوط به Plugin یا skew در `minHostVersion` پرصدا می‌مانند، به‌جای اینکه تنظیمات نامرتبط کاربر مانند مدل‌ها، providerها، نمایه‌های احراز هویت، کانال‌ها، exposure در Gateway، ابزارها، حافظه، مرورگر یا پیکربندی cron را برگردانند.

## زیر‌فرمان‌ها

  * `config file`: مسیر فایل پیکربندی فعال را چاپ می‌کند (از `OPENCLAW_CONFIG_PATH` یا مکان پیش‌فرض resolve شده است). مسیر باید نام یک فایل عادی باشد، نه symlink.


پس از ویرایش‌ها Gateway را restart کنید.

## اعتبارسنجی

پیکربندی فعلی را بدون شروع Gateway، در برابر schema فعال اعتبارسنجی کنید.

bashCopy code
[code]
    openclaw config validateopenclaw config validate --json
[/code]

پس از اینکه `openclaw config validate` موفق شد، می‌توانید از TUI محلی استفاده کنید تا یک عامل embedded پیکربندی فعال را با مستندات مقایسه کند، در حالی که هر تغییر را از همان ترمینال اعتبارسنجی می‌کنید:

bashCopy code
[code]
    openclaw chat
[/code]

سپس داخل TUI:

textCopy code
[code]
    !openclaw config file!openclaw docs gateway auth token secretref!openclaw config validate!openclaw doctor
[/code]

چرخه معمول ترمیم:

* ### Compare with docs

از عامل بخواهید پیکربندی فعلی شما را با صفحه مرتبط مستندات مقایسه کند و کوچک‌ترین اصلاح را پیشنهاد دهد.

* ### Apply targeted edits

ویرایش‌های هدفمند را با `openclaw config set` یا `openclaw configure` اعمال کنید.

* ### Re-validate

پس از هر تغییر، `openclaw config validate` را دوباره اجرا کنید.

* ### Doctor for runtime issues

اگر اعتبارسنجی موفق است اما runtime هنوز ناسالم است، برای کمک به migration و ترمیم، `openclaw doctor` یا `openclaw doctor --fix` را اجرا کنید.

## مرتبط

  * [مرجع CLI](</fa/cli>)
  * [پیکربندی](</fa/gateway/configuration>)


Was this useful?YesNo