---
title: حل وابستگی‌های Plugin
source_url: https://docs.openclaw.ai/fa/plugins/dependency-resolution
scraped_at: 2026-05-25
---

OpenClaw کار وابستگی‌های Plugin را در زمان نصب/به‌روزرسانی نگه می‌دارد. بارگذاری زمان اجرا package managerها را اجرا نمی‌کند، درخت‌های وابستگی را ترمیم نمی‌کند، یا دایرکتوری package OpenClaw را تغییر نمی‌دهد.

## تقسیم مسئولیت

packageهای Plugin مالک گراف وابستگی خود هستند:

  * وابستگی‌های زمان اجرا در `dependencies` یا `optionalDependencies` مربوط به package Plugin قرار دارند
  * importهای SDK/core به‌صورت peer یا importهای فراهم‌شده توسط OpenClaw هستند
  * Pluginهای توسعه محلی وابستگی‌های ازپیش‌نصب‌شده خودشان را همراه دارند
  * Pluginهای npm و git در ریشه‌های package تحت مالکیت OpenClaw نصب می‌شوند


OpenClaw فقط مالک چرخه عمر Plugin است:

  * کشف منبع Plugin
  * نصب یا به‌روزرسانی package وقتی به‌صراحت درخواست شده باشد
  * ثبت فراداده نصب
  * بارگذاری نقطه ورود Plugin
  * شکست با خطایی قابل اقدام وقتی وابستگی‌ها موجود نیستند


## ریشه‌های نصب

OpenClaw از ریشه‌های پایدار برای هر منبع استفاده می‌کند:

  * packageهای npm زیر `~/.openclaw/npm` نصب می‌شوند
  * packageهای git زیر `~/.openclaw/git` clone می‌شوند
  * نصب‌های local/path/archive بدون ترمیم وابستگی کپی یا ارجاع داده می‌شوند


نصب‌های npm در ریشه npm با این دستور اجرا می‌شوند:

bashCopy code
[code]
    cd ~/.openclaw/npmnpm install --omit=dev --omit=peer --legacy-peer-deps --ignore-scripts --no-audit --no-fund
[/code]

`openclaw plugins install npm-pack:<path.tgz>` برای یک tarball محلی npm-pack از همان ریشه npm مدیریت‌شده استفاده می‌کند. OpenClaw فراداده npm tarball را می‌خواند، آن را به ریشه مدیریت‌شده به‌عنوان یک وابستگی `file:` کپی‌شده اضافه می‌کند، نصب عادی npm را اجرا می‌کند، و سپس پیش از اعتماد به Plugin، فراداده lockfile نصب‌شده را راستی‌آزمایی می‌کند. این برای اثبات package-acceptance و release-candidate در نظر گرفته شده است، جایی که یک مصنوعه pack محلی باید مانند مصنوعه registry که شبیه‌سازی می‌کند رفتار کند.

npm ممکن است وابستگی‌های گذرای را کنار package Plugin در `~/.openclaw/npm/node_modules` hoist کند. OpenClaw پیش از اعتماد به نصب، ریشه npm مدیریت‌شده را اسکن می‌کند و برای حذف packageهای مدیریت‌شده توسط npm هنگام uninstall از npm استفاده می‌کند، بنابراین وابستگی‌های زمان اجرای hoistشده داخل مرز پاک‌سازی مدیریت‌شده می‌مانند.

Pluginهایی که `openclaw/plugin-sdk/*` را import می‌کنند، `openclaw` را به‌عنوان یک وابستگی peer اعلام می‌کنند. OpenClaw اجازه نمی‌دهد npm یک کپی registry جداگانه از package میزبان را در ریشه مدیریت‌شده نصب کند، چون packageهای میزبان کهنه می‌توانند روی حل peer در npm هنگام نصب‌های بعدی Plugin اثر بگذارند. نصب‌های npm مدیریت‌شده، حل/مادی‌سازی peer توسط npm را برای ریشه مشترک نادیده می‌گیرند و OpenClaw پس از install، update، یا uninstall برای packageهای نصب‌شده‌ای که peer میزبان را اعلام می‌کنند، پیوندهای `node_modules/openclaw` محلیِ Plugin را دوباره برقرار می‌کند.

نصب‌های git مخزن را clone یا refresh می‌کنند، سپس اجرا می‌کنند:

bashCopy code
[code]
    npm install --omit=dev --ignore-scripts --no-audit --no-fund
[/code]

سپس Plugin نصب‌شده از همان دایرکتوری package بارگذاری می‌شود، بنابراین حل `node_modules` محلیِ package و والد همان‌گونه کار می‌کند که برای یک package عادی Node کار می‌کند.

## Pluginهای محلی

Pluginهای محلی به‌عنوان دایرکتوری‌های تحت کنترل توسعه‌دهنده در نظر گرفته می‌شوند. OpenClaw برای آن‌ها `npm install`، `pnpm install`، یا ترمیم وابستگی اجرا نمی‌کند. اگر یک Plugin محلی وابستگی دارد، پیش از بارگذاری آن، وابستگی‌ها را در همان Plugin نصب کنید.

Pluginهای محلی TypeScript شخص ثالث می‌توانند از مسیر اضطراری Jiti استفاده کنند. Pluginهای JavaScript بسته‌بندی‌شده و Pluginهای داخلی bundled به‌جای Jiti از طریق import/require بومی بارگذاری می‌شوند.

## راه‌اندازی و بارگذاری مجدد

راه‌اندازی Gateway و بارگذاری مجدد config هرگز وابستگی‌های Plugin را نصب نمی‌کنند. آن‌ها رکوردهای نصب Plugin را می‌خوانند، نقطه ورود را محاسبه می‌کنند، و آن را بارگذاری می‌کنند.

اگر وابستگی‌ای در زمان اجرا موجود نباشد، Plugin بارگذاری نمی‌شود و خطا باید operator را به یک رفع صریح هدایت کند:

bashCopy code
[code]
    openclaw plugins update <id>openclaw plugins install <source>openclaw doctor --fix
[/code]

`doctor --fix` می‌تواند وضعیت وابستگی قدیمی تولیدشده توسط OpenClaw را پاک کند و Pluginهای قابل دانلودی را که هنگام ارجاع config به آن‌ها از رکوردهای نصب محلی غایب هستند بازیابی کند. Doctor وابستگی‌های یک Plugin محلی ازپیش‌نصب‌شده را ترمیم نمی‌کند.

## Pluginهای bundled

Pluginهای bundled سبک و حیاتی برای core به‌عنوان بخشی از OpenClaw عرضه می‌شوند. آن‌ها باید یا درخت وابستگی زمان اجرای سنگینی نداشته باشند یا به یک package قابل دانلود در ClawHub/npm منتقل شوند.

برای فهرست تولیدشده فعلی از Pluginهایی که در package core عرضه می‌شوند، بیرونی نصب می‌شوند، یا فقط source-only می‌مانند، [فهرست موجودی Plugin](</fa/plugins/plugin-inventory>) را ببینید.

manifestهای Plugin bundled نباید staging وابستگی درخواست کنند. قابلیت‌های بزرگ یا اختیاری Plugin باید به‌عنوان یک Plugin عادی بسته‌بندی شوند و از طریق همان مسیر npm/git/ClawHub مانند Pluginهای شخص ثالث نصب شوند.

در checkoutهای source، OpenClaw مخزن را به‌عنوان یک monorepo مبتنی بر pnpm در نظر می‌گیرد. پس از `pnpm install`، Pluginهای bundled از `extensions/<id>` بارگذاری می‌شوند تا وابستگی‌های workspace محلیِ package در دسترس باشند و ویرایش‌ها مستقیم اعمال شوند. توسعه checkoutهای source فقط با pnpm پشتیبانی می‌شود؛ اجرای ساده `npm install` در ریشه مخزن روش پشتیبانی‌شده‌ای برای آماده‌سازی وابستگی‌های Plugin bundled نیست.

شکل نصب | محل Plugin bundled | مالک وابستگی  
---|---|---  
`npm install -g openclaw` | درخت زمان اجرای ساخته‌شده داخل package | package OpenClaw و جریان‌های صریح install/update/doctor برای Plugin  
Git checkout به‌همراه `pnpm install` | packageهای workspace در `extensions/<id>` | workspace pnpm، شامل وابستگی‌های خود هر package Plugin  
`openclaw plugins install ...` | ریشه Plugin مدیریت‌شده npm/git/ClawHub | جریان install/update مربوط به Plugin  
  
## پاک‌سازی میراثی

نسخه‌های قدیمی‌تر OpenClaw ریشه‌های وابستگی Pluginهای bundled را هنگام راه‌اندازی یا در طول ترمیم doctor تولید می‌کردند. پاک‌سازی doctor فعلی وقتی `--fix` استفاده شود، آن دایرکتوری‌ها و symlinkهای کهنه را حذف می‌کند، شامل ریشه‌های قدیمی `plugin-runtime-deps`، symlinkهای package با prefix سراسری Node که به هدف‌های حذف‌شده `plugin-runtime-deps` اشاره می‌کنند، manifestهای `.openclaw-runtime-deps*`، `node_modules` تولیدشده Plugin، دایرکتوری‌های مرحله نصب، و storeهای pnpm محلیِ package. postinstall بسته‌بندی‌شده نیز آن symlinkهای سراسری را پیش از حذف ریشه‌های هدف legacy حذف می‌کند تا upgradeها importهای package مربوط به ESM را به‌صورت dangling باقی نگذارند.

این مسیرها فقط بقایای legacy هستند. نصب‌های جدید نباید آن‌ها را ایجاد کنند.

Was this useful?YesNo