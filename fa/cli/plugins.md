---
title: Plugins
source_url: https://docs.openclaw.ai/fa/cli/plugins
scraped_at: 2026-05-25
---

مدیریت Pluginهای Gateway، بسته‌های hook، و bundleهای سازگار.

[**Plugin system** راهنمای کاربر نهایی برای نصب، فعال‌سازی، و عیب‌یابی pluginها. ](</fa/tools/plugin>) [**Manage plugins** نمونه‌های سریع برای نصب، فهرست‌کردن، به‌روزرسانی، حذف نصب، و انتشار. ](</fa/plugins/manage-plugins>) [**Plugin bundles** مدل سازگاری bundle. ](</fa/plugins/bundles>) [**Plugin manifest** فیلدهای manifest و schema پیکربندی. ](</fa/plugins/manifest>) [**Security** سخت‌سازی امنیتی برای نصب pluginها. ](</fa/gateway/security>)

## فرمان‌ها

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --jsonopenclaw plugins search <query>openclaw plugins search <query> --limit 20openclaw plugins search <query> --jsonopenclaw plugins install <path-or-spec>openclaw plugins inspect <id>openclaw plugins inspect <id> --runtimeopenclaw plugins inspect <id> --jsonopenclaw plugins inspect --allopenclaw plugins info <id>openclaw plugins enable <id>openclaw plugins disable <id>openclaw plugins registryopenclaw plugins registry --refreshopenclaw plugins uninstall <id>openclaw plugins doctoropenclaw plugins update <id-or-npm-spec>openclaw plugins update --allopenclaw plugins marketplace list <marketplace>openclaw plugins marketplace list <marketplace> --json
[/code]

برای بررسی نصب، inspect، حذف نصب، یا تازه‌سازی registry که کند است، فرمان را با `OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1` اجرا کنید. trace زمان‌بندی فازها را در stderr می‌نویسد و خروجی JSON را قابل parse نگه می‌دارد. [اشکال‌زدایی](</fa/help/debugging#plugin-lifecycle-trace>) را ببینید.

### نصب

bashCopy code
[code]
    openclaw plugins search "calendar"                   # search ClawHub pluginsopenclaw plugins install <package>                      # npm by defaultopenclaw plugins install clawhub:<package>              # ClawHub onlyopenclaw plugins install npm:<package>                  # npm onlyopenclaw plugins install npm-pack:<path.tgz>            # local npm pack through npm install semanticsopenclaw plugins install git:github.com/<owner>/<repo>  # git repoopenclaw plugins install git:github.com/<owner>/<repo>@<ref>openclaw plugins install <package> --force              # overwrite existing installopenclaw plugins install <package> --pin                # pin versionopenclaw plugins install <package> --dangerously-force-unsafe-installopenclaw plugins install <path>                         # local pathopenclaw plugins install <plugin>@<marketplace>         # marketplaceopenclaw plugins install <plugin> --marketplace <name>  # marketplace (explicit)openclaw plugins install <plugin> --marketplace https://github.com/<owner>/<repo>
[/code]

نگه‌دارندگان هنگام آزمودن نصب‌های زمان setup می‌توانند منابع نصب خودکار plugin را با متغیرهای محیطی محافظت‌شده override کنند. [Overrideهای نصب Plugin](</fa/plugins/install-overrides>) را ببینید.

`plugins search` در ClawHub برای بسته‌های plugin قابل نصب query می‌زند و نام‌های بسته‌ی آماده‌ی نصب را چاپ می‌کند. این فرمان بسته‌های code-plugin و bundle-plugin را جست‌وجو می‌کند، نه Skills را. برای Skills در ClawHub از `openclaw skills search` استفاده کنید.

Config includes and invalid-config repair

اگر بخش `plugins` شما با یک `$include` تک‌فایلی پشتیبانی می‌شود، `plugins install/update/enable/disable/uninstall` در همان فایل include‌شده می‌نویسند و `openclaw.json` را دست‌نخورده می‌گذارند. Includeهای root، آرایه‌های include، و includeهایی با overrideهای هم‌سطح به‌جای flatten شدن، بسته و ناموفق می‌شوند. برای شکل‌های پشتیبانی‌شده، [includeهای پیکربندی](</fa/gateway/configuration>) را ببینید.

اگر پیکربندی هنگام نصب نامعتبر باشد، `plugins install` معمولاً بسته و ناموفق می‌شود و به شما می‌گوید ابتدا `openclaw doctor --fix` را اجرا کنید. هنگام راه‌اندازی Gateway و hot reload، پیکربندی نامعتبر plugin مثل هر پیکربندی نامعتبر دیگری بسته و ناموفق می‌شود؛ `openclaw doctor --fix` می‌تواند entry نامعتبر plugin را قرنطینه کند. تنها استثنای مستندشده در زمان نصب، مسیر بازیابی محدود برای plugin همراه است، برای pluginهایی که به‌صراحت در `openclaw.install.allowInvalidConfigRecovery` opt in می‌کنند.

\--force and reinstall vs update

`--force` هدف نصب موجود را دوباره استفاده می‌کند و plugin یا بسته‌ی hook ازقبل‌نصب‌شده را در جای خودش بازنویسی می‌کند. وقتی آگاهانه همان id را از یک مسیر محلی، archive، بسته‌ی ClawHub، یا artifact npm جدید دوباره نصب می‌کنید از آن استفاده کنید. برای ارتقاهای معمول یک plugin npm که از قبل track شده است، `openclaw plugins update <id-or-npm-spec>` را ترجیح دهید.

اگر `plugins install` را برای id مربوط به pluginی اجرا کنید که از قبل نصب شده است، OpenClaw متوقف می‌شود و برای ارتقای معمول شما را به `plugins update <id-or-npm-spec>` راهنمایی می‌کند، یا وقتی واقعاً می‌خواهید نصب فعلی را از منبع دیگری بازنویسی کنید به `plugins install <package> --force`.

\--pin scope

`--pin` فقط روی نصب‌های npm اعمال می‌شود. با نصب‌های `git:` پشتیبانی نمی‌شود؛ وقتی منبع pin‌شده می‌خواهید، از یک git ref صریح مثل `git:github.com/acme/plugin@v1.2.3` استفاده کنید. با `--marketplace` پشتیبانی نمی‌شود، چون نصب‌های marketplace به‌جای npm spec، metadata منبع marketplace را ماندگار می‌کنند.

\--dangerously-force-unsafe-install

`--dangerously-force-unsafe-install` گزینه‌ای اضطراری برای مثبت‌های کاذب در اسکنر داخلی کد خطرناک است. این گزینه اجازه می‌دهد نصب حتی وقتی اسکنر داخلی یافته‌های `critical` گزارش می‌کند ادامه پیدا کند، اما blockهای policy مربوط به hookهای `before_install` در plugin را دور نمی‌زند و failureهای scan را دور نمی‌زند.

این CLI flag روی جریان‌های نصب/به‌روزرسانی plugin اعمال می‌شود. نصب‌های dependency مربوط به skill که با Gateway پشتیبانی می‌شوند از override درخواست متناظر `dangerouslyForceUnsafeInstall` استفاده می‌کنند، درحالی‌که `openclaw skills install` همچنان جریان جداگانه‌ی دانلود/نصب skill از ClawHub است.

اگر pluginی که در ClawHub منتشر کرده‌اید با scan در registry مسدود شده است، از مراحل ناشر در [ClawHub](</fa/clawhub/security>) استفاده کنید.

Hook packs and npm specs

`plugins install` همچنین سطح نصب برای بسته‌های hook است که `openclaw.hooks` را در `package.json` expose می‌کنند. برای visibility فیلترشده‌ی hook و فعال‌سازی هر hook، نه نصب package، از `openclaw hooks` استفاده کنید.

specهای npm **فقط registry** هستند (نام package + **نسخه‌ی دقیق** اختیاری یا **dist-tag**). specهای Git/URL/file و بازه‌های semver رد می‌شوند. نصب‌های dependency برای ایمنی به‌صورت project-local با `--ignore-scripts` اجرا می‌شوند، حتی وقتی shell شما تنظیمات سراسری نصب npm دارد. ریشه‌های npm مدیریت‌شده‌ی plugin، `overrides` سطح package متعلق به OpenClaw را به ارث می‌برند، بنابراین pinهای امنیتی host روی dependencyهای hoist‌شده‌ی plugin هم اعمال می‌شوند.

وقتی می‌خواهید resolution npm را صریح کنید، از `npm:<package>` استفاده کنید. specهای ساده‌ی package هم در دوره‌ی جابه‌جایی انتشار مستقیماً از npm نصب می‌شوند.

specهای ساده و `@latest` روی track پایدار می‌مانند. نسخه‌های اصلاحی تاریخ‌دار OpenClaw مثل `2026.5.3-1` برای این check، releaseهای پایدار هستند. اگر npm هرکدام از آن‌ها را به یک prerelease resolve کند، OpenClaw متوقف می‌شود و از شما می‌خواهد با یک tag prerelease مثل `@beta`/`@rc` یا یک نسخه‌ی دقیق prerelease مثل `@1.2.3-beta.4` صریحاً opt in کنید.

اگر یک install spec ساده با id رسمی plugin مطابقت داشته باشد (برای مثال `diffs`)، OpenClaw مستقیماً entry کاتالوگ را نصب می‌کند. برای نصب یک package npm با همان نام، از یک spec scoped صریح استفاده کنید (برای مثال `@scope/diffs`).

Git repositories

برای نصب مستقیم از یک repository در git، از `git:<repo>` استفاده کنید. شکل‌های پشتیبانی‌شده شامل clone URLهای `git:github.com/owner/repo`، `git:owner/repo`، `https://` کامل، `ssh://`، `git://`، `file://`، و `git@host:owner/repo.git` هستند. برای checkout کردن یک branch، tag، یا commit پیش از نصب، `@<ref>` یا `#<ref>` را اضافه کنید.

نصب‌های Git در یک directory موقت clone می‌کنند، وقتی ref درخواست‌شده وجود داشته باشد آن را check out می‌کنند، سپس از installer عادی directory plugin استفاده می‌کنند. یعنی اعتبارسنجی manifest، اسکن کد خطرناک، کار نصب package-manager، و recordهای نصب مثل نصب‌های npm رفتار می‌کنند. نصب‌های git ثبت‌شده شامل URL/ref منبع به‌همراه commit resolve‌شده هستند تا `openclaw plugins update` بتواند بعداً منبع را دوباره resolve کند.

بعد از نصب از git، از `openclaw plugins inspect <id> --runtime --json` برای تأیید registrationهای runtime مثل متدهای gateway و فرمان‌های CLI استفاده کنید. اگر plugin با `api.registerCli` یک CLI root ثبت کرده است، آن فرمان را مستقیماً از طریق CLI root متعلق به OpenClaw اجرا کنید، برای مثال `openclaw demo-plugin ping`.

Archives

Archiveهای پشتیبانی‌شده: `.zip`، `.tgz`، `.tar.gz`، `.tar`. Archiveهای plugin بومی OpenClaw باید در root استخراج‌شده‌ی plugin یک `openclaw.plugin.json` معتبر داشته باشند؛ archiveهایی که فقط `package.json` دارند پیش از اینکه OpenClaw recordهای نصب را بنویسد رد می‌شوند.

وقتی فایل یک tarball از npm-pack است و می‌خواهید همان مسیر نصب npm-root مدیریت‌شده را که نصب‌های registry استفاده می‌کنند تست کنید، از `npm-pack:<path.tgz>` استفاده کنید، شامل تأیید `package-lock.json`، اسکن dependencyهای hoist‌شده، و recordهای نصب npm. مسیرهای archive ساده همچنان به‌عنوان archive محلی زیر root مربوط به extensions plugin نصب می‌شوند.

نصب‌های marketplace مربوط به Claude هم پشتیبانی می‌شوند.

نصب‌های ClawHub از locator صریح `clawhub:<package>` استفاده می‌کنند:

bashCopy code
[code]
    openclaw plugins install clawhub:openclaw-codex-app-serveropenclaw plugins install clawhub:openclaw-codex-app-server@1.2.3
[/code]

specهای plugin ساده و ایمن برای npm در دوره‌ی جابه‌جایی انتشار به‌صورت پیش‌فرض از npm نصب می‌شوند:

bashCopy code
[code]
    openclaw plugins install openclaw-codex-app-server
[/code]

برای صریح‌کردن resolution فقط-npm از `npm:` استفاده کنید:

bashCopy code
[code]
    openclaw plugins install npm:openclaw-codex-app-serveropenclaw plugins install npm:@scope/plugin-name@1.0.1
[/code]

OpenClaw پیش از نصب، سازگاری API تبلیغ‌شدهٔ Plugin / حداقل سازگاری Gateway را بررسی می‌کند. وقتی نسخهٔ انتخاب‌شدهٔ ClawHub یک آرتیفکت ClawPack منتشر می‌کند، OpenClaw بستهٔ npm-pack نسخه‌دار `.tgz` را دانلود می‌کند، سرآیند digest در ClawHub و digest آرتیفکت را تأیید می‌کند، سپس آن را از مسیر معمول آرشیو نصب می‌کند. نسخه‌های قدیمی‌تر ClawHub بدون فرادادهٔ ClawPack همچنان از مسیر قدیمی تأیید آرشیو بسته نصب می‌شوند. نصب‌های ثبت‌شده، فرادادهٔ منبع ClawHub، نوع آرتیفکت، یکپارچگی npm، shasum در npm، نام tarball، و واقعیت‌های digest در ClawPack را برای به‌روزرسانی‌های بعدی نگه می‌دارند. نصب‌های ClawHub بدون نسخه، یک مشخصهٔ ثبت‌شدهٔ بدون نسخه نگه می‌دارند تا `openclaw plugins update` بتواند انتشارهای جدیدتر ClawHub را دنبال کند؛ انتخابگرهای نسخه یا برچسب صریح مانند `clawhub:pkg@1.2.3` و `clawhub:pkg@beta` همچنان به همان انتخابگر سنجاق می‌مانند.

#### کوتاه‌نویسی بازار

وقتی نام بازار در کش رجیستری محلی Claude در `~/.claude/plugins/known_marketplaces.json` وجود دارد، از کوتاه‌نویسی `plugin@marketplace` استفاده کنید:

bashCopy code
[code]
    openclaw plugins marketplace list <marketplace-name>openclaw plugins install <plugin-name>@<marketplace-name>
[/code]

وقتی می‌خواهید منبع بازار را صریحاً ارسال کنید، از `--marketplace` استفاده کنید:

bashCopy code
[code]
    openclaw plugins install <plugin-name> --marketplace <marketplace-name>openclaw plugins install <plugin-name> --marketplace <owner/repo>openclaw plugins install <plugin-name> --marketplace https://github.com/<owner>/<repo>openclaw plugins install <plugin-name> --marketplace ./my-marketplace
[/code]

### منابع بازار

  * یک نام بازار شناخته‌شدهٔ Claude از `~/.claude/plugins/known_marketplaces.json`
  * ریشهٔ بازار محلی یا مسیر `marketplace.json`
  * کوتاه‌نویسی مخزن GitHub مانند `owner/repo`
  * URL مخزن GitHub مانند `https://github.com/owner/repo`
  * یک URL مربوط به git


### قواعد بازار راه دور

برای بازارهای راه دور که از GitHub یا git بارگذاری می‌شوند، ورودی‌های Plugin باید داخل مخزن بازار cloneشده باقی بمانند. OpenClaw منابع مسیر نسبی را از همان مخزن می‌پذیرد و منابع Plugin از نوع HTTP(S)، مسیر مطلق، git، GitHub، و دیگر منابع غیرمسیر را از manifestهای راه دور رد می‌کند.

برای مسیرها و آرشیوهای محلی، OpenClaw به‌صورت خودکار تشخیص می‌دهد:

  * Pluginهای بومی OpenClaw (`openclaw.plugin.json`)
  * بسته‌های سازگار با Codex (`.codex-plugin/plugin.json`)
  * بسته‌های سازگار با Claude (`.claude-plugin/plugin.json` یا چیدمان پیش‌فرض مؤلفهٔ Claude)
  * بسته‌های سازگار با Cursor (`.cursor-plugin/plugin.json`)


### فهرست

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --jsonopenclaw plugins search <query>openclaw plugins search <query> --limit 20openclaw plugins search <query> --json
[/code]

فقط Pluginهای فعال را نشان بده.

از نمای جدولی به خط‌های جزئیات هر Plugin با فرادادهٔ منبع/خاستگاه/نسخه/فعال‌سازی جابه‌جا شو.

موجودی قابل‌خواندن توسط ماشین به‌همراه diagnostics رجیستری و وضعیت نصب وابستگی‌های بسته.

`plugins search` یک جست‌وجوی کاتالوگ راه دور ClawHub است. وضعیت محلی را بررسی نمی‌کند، config را تغییر نمی‌دهد، بسته نصب نمی‌کند، و کد زمان اجرای Plugin را بارگذاری نمی‌کند. نتایج جست‌وجو شامل نام بستهٔ ClawHub، خانواده، کانال، نسخه، خلاصه، و راهنمای نصبی مانند `openclaw plugins install clawhub:<package>` هستند.

برای کار روی Pluginهای همراه داخل یک image بسته‌بندی‌شدهٔ Docker، دایرکتوری منبع Plugin را روی مسیر منبع بسته‌بندی‌شدهٔ متناظر bind-mount کنید، مانند `/app/extensions/synology-chat`. OpenClaw آن overlay منبع mountشده را پیش از `/app/dist/extensions/synology-chat` کشف می‌کند؛ یک دایرکتوری منبع صرفاً کپی‌شده بی‌اثر می‌ماند تا نصب‌های بسته‌بندی‌شدهٔ معمول همچنان از dist کامپایل‌شده استفاده کنند.

برای اشکال‌زدایی hook زمان اجرا:

  * `openclaw plugins inspect <id> --runtime --json` hookهای ثبت‌شده و diagnostics را از یک گذر inspection با module-loaded نشان می‌دهد. inspection زمان اجرا هرگز وابستگی‌ها را نصب نمی‌کند؛ از `openclaw doctor --fix` برای پاک‌سازی وضعیت وابستگی قدیمی یا بازیابی Pluginهای دانلودشدنی گمشده که در config ارجاع شده‌اند استفاده کنید.
  * `openclaw gateway status --deep --require-rpc` Gateway قابل‌دسترسی، راهنماهای سرویس/فرایند، مسیر config، و سلامت RPC را تأیید می‌کند.
  * hookهای گفت‌وگوی غیرهمراه (`llm_input`, `llm_output`, `before_model_resolve`, `before_agent_reply`, `before_agent_run`, `before_agent_finalize`, `agent_end`) به `plugins.entries.<id>.hooks.allowConversationAccess=true` نیاز دارند.


برای جلوگیری از کپی‌کردن یک دایرکتوری محلی از `--link` استفاده کنید (به `plugins.load.paths` اضافه می‌کند):

bashCopy code
[code]
    openclaw plugins install -l ./my-plugin
[/code]

### index مربوط به Plugin

فرادادهٔ نصب Plugin وضعیتی مدیریت‌شده توسط ماشین است، نه config کاربر. نصب‌ها و به‌روزرسانی‌ها آن را در `plugins/installs.json` زیر دایرکتوری وضعیت فعال OpenClaw می‌نویسند. map سطح بالای `installRecords` منبع پایدار فرادادهٔ نصب است، از جمله رکوردهای manifestهای خراب یا گمشدهٔ Plugin. آرایهٔ `plugins` کش رجیستری سرد مشتق‌شده از manifest است. این فایل شامل هشدار ویرایش‌نکنید است و توسط `openclaw plugins update`، حذف نصب، diagnostics، و رجیستری سرد Plugin استفاده می‌شود.

وقتی OpenClaw رکوردهای قدیمی عرضه‌شدهٔ `plugins.installs` را در config می‌بیند، خواندن‌های زمان اجرا با آن‌ها به‌عنوان ورودی سازگاری رفتار می‌کنند، بدون اینکه `openclaw.json` را بازنویسی کنند. نوشتن‌های صریح Plugin و `openclaw doctor --fix` آن رکوردها را به index مربوط به Plugin منتقل می‌کنند و وقتی نوشتن config مجاز باشد کلید config را حذف می‌کنند؛ اگر هرکدام از نوشتن‌ها شکست بخورد، رکوردهای config نگه داشته می‌شوند تا فرادادهٔ نصب از دست نرود.

### حذف نصب

bashCopy code
[code]
    openclaw plugins uninstall <id>openclaw plugins uninstall <id> --dry-runopenclaw plugins uninstall <id> --keep-files
[/code]

`uninstall` رکوردهای Plugin را از `plugins.entries`، index پایدارشدهٔ Plugin، ورودی‌های فهرست allow/deny مربوط به Plugin، و در صورت کاربرد ورودی‌های پیوندی `plugins.load.paths` حذف می‌کند. مگر اینکه `--keep-files` تنظیم شده باشد، حذف نصب همچنین دایرکتوری نصب مدیریت‌شدهٔ ردیابی‌شده را وقتی داخل ریشهٔ extensions مربوط به Pluginهای OpenClaw باشد حذف می‌کند. برای Pluginهای active memory، slot حافظه به `memory-core` بازنشانی می‌شود.

### به‌روزرسانی

bashCopy code
[code]
    openclaw plugins update <id-or-npm-spec>openclaw plugins update --allopenclaw plugins update <id-or-npm-spec> --dry-runopenclaw plugins update @openclaw/voice-callopenclaw plugins update openclaw-codex-app-server --dangerously-force-unsafe-install
[/code]

به‌روزرسانی‌ها روی نصب‌های ردیابی‌شدهٔ Plugin در index مدیریت‌شدهٔ Plugin و نصب‌های ردیابی‌شدهٔ hook-pack در `hooks.internal.installs` اعمال می‌شوند.

resolve کردن شناسهٔ Plugin در برابر مشخصهٔ npm

وقتی یک شناسهٔ Plugin ارسال می‌کنید، OpenClaw مشخصهٔ نصب ثبت‌شده برای آن Plugin را بازاستفاده می‌کند. یعنی dist-tagهای قبلاً ذخیره‌شده مانند `@beta` و نسخه‌های دقیق pinشده در اجرای بعدی `update <id>` همچنان استفاده می‌شوند.

برای نصب‌های npm، همچنین می‌توانید یک مشخصهٔ صریح بستهٔ npm با dist-tag یا نسخهٔ دقیق ارسال کنید. OpenClaw آن نام بسته را به رکورد Plugin ردیابی‌شده resolve می‌کند، آن Plugin نصب‌شده را به‌روزرسانی می‌کند، و مشخصهٔ جدید npm را برای به‌روزرسانی‌های آینده بر پایهٔ شناسه ثبت می‌کند.

ارسال نام بستهٔ npm بدون نسخه یا برچسب نیز به رکورد Plugin ردیابی‌شده resolve می‌شود. وقتی یک Plugin به نسخه‌ای دقیق pin شده و می‌خواهید آن را به خط انتشار پیش‌فرض رجیستری برگردانید، از این استفاده کنید.

به‌روزرسانی‌های کانال beta

`openclaw plugins update` مشخصهٔ Plugin ردیابی‌شده را بازاستفاده می‌کند مگر اینکه مشخصهٔ جدیدی ارسال کنید. `openclaw update` علاوه بر آن کانال به‌روزرسانی فعال OpenClaw را می‌شناسد: در کانال beta، رکوردهای Plugin مربوط به npm و ClawHub در خط پیش‌فرض ابتدا `@beta` را امتحان می‌کنند، سپس اگر انتشار beta برای Plugin وجود نداشته باشد به مشخصهٔ پیش‌فرض/آخرین ثبت‌شده fallback می‌کنند. این fallback به‌عنوان هشدار گزارش می‌شود و باعث شکست به‌روزرسانی هسته نمی‌شود. نسخه‌های دقیق و برچسب‌های صریح به همان انتخابگر pin می‌مانند.

بررسی‌های نسخه و drift یکپارچگی

پیش از یک به‌روزرسانی زندهٔ npm، OpenClaw نسخهٔ بستهٔ نصب‌شده را با فرادادهٔ رجیستری npm بررسی می‌کند. اگر نسخهٔ نصب‌شده و هویت آرتیفکت ثبت‌شده از قبل با هدف resolveشده مطابقت داشته باشند، به‌روزرسانی بدون دانلود، نصب دوباره، یا بازنویسی `openclaw.json` رد می‌شود.

وقتی hash یکپارچگی ذخیره‌شده وجود داشته باشد و hash آرتیفکت fetchشده تغییر کند، OpenClaw با آن به‌عنوان drift آرتیفکت npm رفتار می‌کند. دستور تعاملی `openclaw plugins update` hashهای مورد انتظار و واقعی را چاپ می‌کند و پیش از ادامه تأیید می‌خواهد. helperهای به‌روزرسانی غیرتعاملی به‌صورت fail-closed شکست می‌خورند مگر اینکه caller یک سیاست ادامهٔ صریح فراهم کند.

\--dangerously-force-unsafe-install در به‌روزرسانی

`--dangerously-force-unsafe-install` همچنین در `plugins update` به‌عنوان override اضطراری برای false positiveهای scan کد خطرناک داخلی هنگام به‌روزرسانی Pluginها در دسترس است. این گزینه همچنان blockهای سیاست `before_install` مربوط به Plugin یا block ناشی از شکست scan را دور نمی‌زند، و فقط برای به‌روزرسانی‌های Plugin اعمال می‌شود، نه به‌روزرسانی‌های hook-pack.

### بازرسی

bashCopy code
[code]
    openclaw plugins inspect <id>openclaw plugins inspect <id> --runtimeopenclaw plugins inspect <id> --json
[/code]

Inspect هویت، وضعیت بارگذاری، منبع، قابلیت‌های manifest، پرچم‌های سیاست، diagnostics، فرادادهٔ نصب، قابلیت‌های بسته، و هرگونه پشتیبانی شناسایی‌شده از سرور MCP یا LSP را به‌صورت پیش‌فرض بدون import کردن زمان اجرای Plugin نشان می‌دهد. `--runtime` را اضافه کنید تا ماژول Plugin بارگذاری شود و hookها، ابزارها، commandها، سرویس‌ها، متدهای Gateway، و routeهای HTTP ثبت‌شده را شامل شود. inspection زمان اجرا وابستگی‌های گمشدهٔ Plugin را مستقیماً گزارش می‌کند؛ نصب‌ها و repairها در `openclaw plugins install`، `openclaw plugins update`، و `openclaw doctor --fix` باقی می‌مانند.

commandهای CLI تحت مالکیت Plugin معمولاً به‌عنوان گروه‌های command ریشهٔ `openclaw` نصب می‌شوند، اما Pluginها ممکن است commandهای تودرتو را نیز زیر یک والد هسته مانند `openclaw nodes` ثبت کنند. پس از اینکه `inspect --runtime` یک command را زیر `cliCommands` نشان داد، آن را در مسیر فهرست‌شده اجرا کنید؛ برای مثال یک Plugin که `demo-git` را ثبت می‌کند می‌تواند با `openclaw demo-git ping` تأیید شود.

هر Plugin بر اساس آنچه واقعاً در زمان اجرا ثبت می‌کند طبقه‌بندی می‌شود:

  * **plain-capability** — یک نوع قابلیت (مثلاً یک Plugin که فقط ارائه‌دهنده است)
  * **hybrid-capability** — چند نوع قابلیت (مثلاً متن + گفتار + تصویر)
  * **hook-only** — فقط هوک‌ها، بدون قابلیت یا سطح
  * **non-capability** — ابزارها/فرمان‌ها/سرویس‌ها اما بدون قابلیت


برای اطلاعات بیشتر درباره مدل قابلیت، [شکل‌های Plugin](</fa/plugins/architecture#plugin-shapes>) را ببینید.

### Doctor

bashCopy code
[code]
    openclaw plugins doctor
[/code]

`doctor` خطاهای بارگذاری Plugin، عیب‌یابی‌های manifest/discovery، و اعلان‌های سازگاری را گزارش می‌کند. وقتی همه‌چیز پاک باشد، `No plugin issues detected.` را چاپ می‌کند.

اگر یک Plugin پیکربندی‌شده روی دیسک وجود داشته باشد اما توسط بررسی‌های ایمنی مسیرِ بارگذار مسدود شده باشد، اعتبارسنجی پیکربندی ورودی Plugin را نگه می‌دارد و آن را به‌صورت `present but blocked` گزارش می‌کند. به‌جای حذف پیکربندی `plugins.entries.<id>` یا `plugins.allow`، عیب‌یابی قبلی مربوط به Plugin مسدودشده، مانند مالکیت مسیر یا مجوزهای قابل‌نوشتن برای همه، را رفع کنید.

برای شکست‌های مربوط به شکل ماژول، مانند نبود exportهای `register`/`activate`، با `OPENCLAW_PLUGIN_LOAD_DEBUG=1` دوباره اجرا کنید تا خلاصه‌ای فشرده از شکل exportها در خروجی عیب‌یابی گنجانده شود.

### رجیستری

bashCopy code
[code]
    openclaw plugins registryopenclaw plugins registry --refreshopenclaw plugins registry --json
[/code]

رجیستری محلی Plugin، مدل خواندن سرد و پایدار OpenClaw برای هویت Plugin نصب‌شده، فعال‌بودن، فراداده منبع، و مالکیت مشارکت‌ها است. راه‌اندازی عادی، جست‌وجوی مالک ارائه‌دهنده، طبقه‌بندی راه‌اندازی کانال، و موجودی Plugin می‌توانند آن را بدون import کردن ماژول‌های runtime Plugin بخوانند.

از `plugins registry` برای بررسی اینکه رجیستری پایدار وجود دارد، به‌روز است، یا منسوخ شده استفاده کنید. از `--refresh` برای بازسازی آن از ایندکس پایدار Plugin، سیاست پیکربندی، و فراداده manifest/package استفاده کنید. این مسیر تعمیر است، نه مسیر فعال‌سازی runtime.

`openclaw doctor --fix` همچنین ناهماهنگی npm مدیریت‌شده در مجاورت رجیستری را تعمیر می‌کند: اگر یک بسته یتیم یا بازیابی‌شده `@openclaw/*` زیر ریشه npm مربوط به Plugin مدیریت‌شده، یک Plugin باندل‌شده را تحت‌الشعاع قرار دهد، doctor آن بسته منسوخ را حذف می‌کند و رجیستری را بازسازی می‌کند تا راه‌اندازی در برابر manifest باندل‌شده اعتبارسنجی شود. Doctor همچنین بسته میزبان `openclaw` را به Pluginهای npm مدیریت‌شده‌ای که `peerDependencies.openclaw` را اعلام می‌کنند، دوباره لینک می‌کند تا importهای runtime محلی بسته مانند `openclaw/plugin-sdk/*` پس از به‌روزرسانی‌ها یا تعمیرهای npm resolve شوند.

### Marketplace

bashCopy code
[code]
    openclaw plugins marketplace list <source>openclaw plugins marketplace list <source> --json
[/code]

فهرست Marketplace یک مسیر محلی Marketplace، مسیر `marketplace.json`، shorthand گیت‌هاب مانند `owner/repo`، URL مخزن گیت‌هاب، یا URL گیت را می‌پذیرد. `--json` برچسب منبع resolve‌شده را همراه با manifest تجزیه‌شده Marketplace و ورودی‌های Plugin چاپ می‌کند.

## مرتبط

  * [ساخت Pluginها](</fa/plugins/building-plugins>)
  * [مرجع CLI](</fa/cli>)
  * [ClawHub](</fa/clawhub>)


Was this useful?YesNo