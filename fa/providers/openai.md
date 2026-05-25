---
title: OpenAI
source_url: https://docs.openclaw.ai/fa/providers/openai
scraped_at: 2026-05-25
---

OpenAI APIهای توسعه‌دهنده را برای مدل‌های GPT فراهم می‌کند، و Codex نیز از طریق کلاینت‌های Codex شرکت OpenAI به‌عنوان یک عامل کدنویسی در طرح ChatGPT در دسترس است. OpenClaw این سطح‌ها را جدا نگه می‌دارد تا پیکربندی قابل پیش‌بینی بماند.

OpenClaw از `openai/*` به‌عنوان مسیر متعارف مدل OpenAI استفاده می‌کند. نوبت‌های عامل تعبیه‌شده روی مدل‌های OpenAI به‌طور پیش‌فرض از طریق زمان‌اجرای بومی app-server مربوط به Codex اجرا می‌شوند؛ احراز هویت مستقیم با کلید API برای سطح‌های غیرعاملی OpenAI مانند تصاویر، embeddingها، گفتار، و realtime همچنان در دسترس است.

  * **مدل‌های عامل** \- مدل‌های `openai/*` از طریق زمان‌اجرای Codex؛ برای استفاده از اشتراک ChatGPT/Codex با احراز هویت Codex وارد شوید، یا وقتی عمدا احراز هویت با کلید API را می‌خواهید، یک پشتیبان کلید API سازگار با Codex برای OpenAI پیکربندی کنید.
  * **APIهای غیرعاملی OpenAI** \- دسترسی مستقیم به OpenAI Platform با صورت‌حساب مبتنی بر مصرف از طریق `OPENAI_API_KEY` یا راه‌اندازی کلید API مربوط به OpenAI.
  * **پیکربندی قدیمی** \- ارجاع‌های مدل `openai-codex/*` توسط `openclaw doctor --fix` به `openai/*` به‌همراه زمان‌اجرای Codex تعمیر می‌شوند.


OpenAI صراحتا از استفاده OAuth اشتراکی در ابزارها و گردش‌کارهای بیرونی مانند OpenClaw پشتیبانی می‌کند.

ارائه‌دهنده، مدل، زمان‌اجرا، و کانال لایه‌های جداگانه‌اند. اگر این برچسب‌ها با هم قاطی می‌شوند، پیش از تغییر پیکربندی، [زمان‌اجراهای عامل](</fa/concepts/agent-runtimes>) را بخوانید.

## انتخاب سریع

هدف | استفاده کنید | یادداشت‌ها  
---|---|---  
اشتراک ChatGPT/Codex با زمان‌اجرای بومی Codex | `openai/gpt-5.5` | تنظیم پیش‌فرض عامل OpenAI. با احراز هویت Codex وارد شوید.  
صورت‌حساب مستقیم با کلید API برای مدل‌های عامل | `openai/gpt-5.5` به‌همراه یک نمایه کلید API سازگار با Codex | از `auth.order.openai` برای قرار دادن پشتیبان پس از احراز هویت اشتراکی استفاده کنید.  
صورت‌حساب مستقیم با کلید API از طریق PI صریح | `openai/gpt-5.5` به‌همراه زمان‌اجرای ارائه‌دهنده/مدل `pi` | یک نمایه کلید API معمولی `openai` انتخاب کنید.  
آخرین نام مستعار API مدل Instant در ChatGPT | `openai/chat-latest` | فقط کلید API مستقیم. نام مستعار متحرک برای آزمایش‌ها، نه پیش‌فرض.  
احراز هویت اشتراک ChatGPT/Codex از طریق PI صریح | `openai/gpt-5.5` به‌همراه زمان‌اجرای ارائه‌دهنده/مدل `pi` | برای مسیر سازگاری، یک نمایه احراز هویت `openai-codex` انتخاب کنید.  
تولید یا ویرایش تصویر | `openai/gpt-image-2` | با `OPENAI_API_KEY` یا OAuth مربوط به OpenAI Codex کار می‌کند.  
تصاویر با پس‌زمینه شفاف | `openai/gpt-image-1.5` | از `outputFormat=png` یا `webp` و `openai.background=transparent` استفاده کنید.  
  
## نقشه نام‌گذاری

نام‌ها مشابه‌اند اما قابل‌جایگزینی نیستند:

نامی که می‌بینید | لایه | معنی  
---|---|---  
`openai` | پیشوند ارائه‌دهنده | مسیر متعارف مدل OpenAI؛ نوبت‌های عامل از زمان‌اجرای Codex استفاده می‌کنند.  
`openai-codex` | پیشوند احراز هویت/نمایه قدیمی | فضای نام قدیمی‌تر نمایه OpenAI Codex OAuth/اشتراک. نمایه‌های موجود و `auth.order.openai-codex` همچنان کار می‌کنند.  
Plugin مربوط به `codex` | Plugin | Plugin همراه OpenClaw که زمان‌اجرای بومی app-server مربوط به Codex و کنترل‌های گفتگوی `/codex` را فراهم می‌کند.  
provider/model `agentRuntime.id: codex` | زمان‌اجرای عامل | harness بومی app-server مربوط به Codex را برای نوبت‌های تعبیه‌شده مطابق، اجبار می‌کند.  
`/codex ...` | مجموعه فرمان گفتگو | رشته‌های app-server مربوط به Codex را از یک گفتگو متصل/کنترل می‌کند.  
`runtime: "acp", agentId: "codex"` | مسیر نشست ACP | مسیر fallback صریحی که Codex را از طریق ACP/acpx اجرا می‌کند.  
  
این یعنی یک پیکربندی می‌تواند عمدا ارجاع‌های مدل `openai/*` داشته باشد در حالی که نمایه‌های احراز هویت همچنان به اعتبارنامه‌های سازگار با Codex اشاره می‌کنند. برای پیکربندی جدید، `auth.order.openai` را ترجیح دهید؛ نمایه‌های موجود `openai-codex:*` و `auth.order.openai-codex` همچنان پشتیبانی می‌شوند. `openclaw doctor --fix` ارجاع‌های مدل قدیمی `openai-codex/*` را به مسیر متعارف مدل OpenAI بازنویسی می‌کند.

## پوشش قابلیت OpenClaw

قابلیت OpenAI | سطح OpenClaw | وضعیت  
---|---|---  
Chat / Responses | ارائه‌دهنده مدل `openai/<model>` | بله  
مدل‌های اشتراکی Codex | `openai/<model>` با OAuth مربوط به `openai-codex` | بله  
ارجاع‌های مدل قدیمی Codex | `openai-codex/<model>` | توسط doctor به `openai/<model>` تعمیر می‌شود  
harness مربوط به app-server در Codex | `openai/<model>` با زمان‌اجرای حذف‌شده یا `agentRuntime.id: codex` در ارائه‌دهنده/مدل | بله  
جستجوی وب سمت سرور | ابزار بومی OpenAI Responses | بله، وقتی جستجوی وب فعال باشد و هیچ ارائه‌دهنده‌ای pin نشده باشد  
تصاویر | `image_generate` | بله  
ویدیوها | `video_generate` | بله  
متن به گفتار | `messages.tts.provider: "openai"` / `tts` | بله  
گفتار به متن دسته‌ای | `tools.media.audio` / درک رسانه | بله  
گفتار به متن جریانی | Voice Call `streaming.provider: "openai"` | بله  
صدای realtime | Voice Call `realtime.provider: "openai"` / Control UI Talk | بله  
Embeddingها | ارائه‌دهنده embedding حافظه | بله  
  
## Embeddingهای حافظه

OpenClaw می‌تواند از OpenAI یا یک endpoint سازگار با OpenAI برای indexing در `memory_search` و embeddingهای query استفاده کند:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "openai",        model: "text-embedding-3-small",      },    },  },}
[/code]

برای endpointهای سازگار با OpenAI که به برچسب‌های embedding نامتقارن نیاز دارند، `queryInputType` و `documentInputType` را زیر `memorySearch` تنظیم کنید. OpenClaw این‌ها را به‌عنوان فیلدهای درخواست `input_type` ویژه ارائه‌دهنده ارسال می‌کند: embeddingهای query از `queryInputType` استفاده می‌کنند؛ قطعه‌های حافظه indexشده و indexing دسته‌ای از `documentInputType` استفاده می‌کنند. برای نمونه کامل، [مرجع پیکربندی حافظه](</fa/reference/memory-config#provider-specific-config>) را ببینید.

## شروع کار

روش احراز هویت ترجیحی خود را انتخاب کنید و مراحل راه‌اندازی را دنبال کنید.

### API key (OpenAI Platform)

**بهترین برای:** دسترسی مستقیم API و صورت‌حساب مبتنی بر مصرف.

* ### Get your API key

یک کلید API از [داشبورد OpenAI Platform](<https://platform.openai.com/api-keys>) بسازید یا کپی کنید.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice openai-api-key
[/code]

یا کلید را مستقیما پاس دهید:

bashCopy code
[code]
    openclaw onboard --openai-api-key "$OPENAI_API_KEY"
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider openai
[/code]

### خلاصه مسیر

ارجاع مدل | پیکربندی زمان‌اجرا | مسیر | احراز هویت  
---|---|---|---  
`openai/gpt-5.5` | حذف‌شده / provider/model `agentRuntime.id: "codex"` | harness مربوط به app-server در Codex | نمایه OpenAI سازگار با Codex  
`openai/gpt-5.4-mini` | حذف‌شده / provider/model `agentRuntime.id: "codex"` | harness مربوط به app-server در Codex | نمایه OpenAI سازگار با Codex  
`openai/gpt-5.5` | provider/model `agentRuntime.id: "pi"` | زمان‌اجرای تعبیه‌شده PI | نمایه `openai` یا نمایه انتخاب‌شده `openai-codex`  
  
### نمونه پیکربندی

json5Copy code
[code]
    {  env: { OPENAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "openai/gpt-5.5" } } },}
[/code]

برای امتحان کردن مدل Instant فعلی ChatGPT از API مربوط به OpenAI، مدل را به `openai/chat-latest` تنظیم کنید:

json5Copy code
[code]
    {  env: { OPENAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "openai/chat-latest" } } },}
[/code]

`chat-latest` یک نام مستعار متحرک است. OpenAI آن را به‌عنوان آخرین مدل Instant استفاده‌شده در ChatGPT مستند می‌کند و `gpt-5.5` را برای استفاده تولیدی API توصیه می‌کند، بنابراین مگر اینکه صراحتا رفتار آن نام مستعار را بخواهید، `openai/gpt-5.5` را به‌عنوان پیش‌فرض پایدار نگه دارید. این نام مستعار در حال حاضر فقط verbosity متن `medium` را می‌پذیرد، بنابراین OpenClaw overrideهای ناسازگار verbosity متن OpenAI را برای این مدل نرمال‌سازی می‌کند.

### اشتراک Codex

**مناسب برای:** استفاده از اشتراک ChatGPT/Codex شما با اجرای بومی app-server مربوط به Codex، به‌جای یک کلید API جداگانه. Codex ابری به ورود به ChatGPT نیاز دارد.

* ### اجرای OAuth مربوط به Codex

bashCopy code
[code]
    openclaw onboard --auth-choice openai-codex
[/code]

یا OAuth را مستقیما اجرا کنید:

bashCopy code
[code]
    openclaw models auth login --provider openai-codex
[/code]

برای راه‌اندازی‌های بدون محیط گرافیکی یا ناسازگار با callback، `--device-code` را اضافه کنید تا به‌جای callback مرورگر localhost، با جریان کد دستگاه ChatGPT وارد شوید:

bashCopy code
[code]
    openclaw models auth login --provider openai-codex --device-code
[/code]

* ### استفاده از مسیر استاندارد مدل OpenAI

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary openai/gpt-5.5
[/code]

برای مسیر پیش‌فرض، هیچ پیکربندی runtime لازم نیست. نوبت‌های agent مربوط به OpenAI به‌طور خودکار runtime بومی app-server مربوط به Codex را انتخاب می‌کنند، و OpenClaw وقتی این مسیر انتخاب شود، Plugin بسته‌بندی‌شده Codex را نصب یا ترمیم می‌کند.

* ### بررسی دردسترس بودن احراز هویت Codex

bashCopy code
[code]
    openclaw models list --provider openai-codex
[/code]

پس از اجرای gateway، در چت `/codex status` یا `/codex models` را بفرستید تا runtime بومی app-server را بررسی کنید.

### خلاصه مسیر

مرجع مدل | پیکربندی runtime | مسیر | احراز هویت  
---|---|---|---  
`openai/gpt-5.5` | حذف‌شده / provider/model `agentRuntime.id: "codex"` | harness بومی app-server مربوط به Codex | ورود به Codex یا پروفایل احراز هویت مرتب‌شده `openai`  
`openai/gpt-5.5` | provider/model `agentRuntime.id: "pi"` | runtime تعبیه‌شده PI با انتقال داخلی احراز هویت Codex | پروفایل انتخاب‌شده `openai-codex`  
`openai-codex/gpt-5.5` | ترمیم‌شده توسط doctor | مسیر قدیمی بازنویسی‌شده به `openai/gpt-5.5` | پروفایل موجود `openai-codex`  
  
### نمونه پیکربندی

json5Copy code
[code]
    {  plugins: { entries: { codex: { enabled: true } } },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },    },  },}
[/code]

با یک پشتیبان کلید API، مدل را روی `openai/gpt-5.5` نگه دارید و ترتیب احراز هویت را زیر `openai` قرار دهید. OpenClaw ابتدا اشتراک را امتحان می‌کند، سپس کلید API را، درحالی‌که روی harness مربوط به Codex باقی می‌ماند:

json5Copy code
[code]
    {  plugins: { entries: { codex: { enabled: true } } },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },    },  },  auth: {    order: {      openai: [        "openai-codex:user@example.com",        "openai:api-key-backup",      ],    },  },}
[/code]

### بررسی و بازیابی مسیریابی OAuth مربوط به Codex

از این دستورها استفاده کنید تا ببینید agent پیش‌فرض شما از کدام مدل، runtime، و مسیر احراز هویت استفاده می‌کند:

bashCopy code
[code]
    openclaw models statusopenclaw models auth list --provider openai-codexopenclaw config get agents.defaults.model --jsonopenclaw config get models.providers.openai.agentRuntime --json
[/code]

برای یک agent مشخص، `--agent <id>` را اضافه کنید:

bashCopy code
[code]
    openclaw models status --agent <id>openclaw models auth list --agent <id> --provider openai-codex
[/code]

اگر یک پیکربندی قدیمی‌تر هنوز `openai-codex/gpt-*` یا یک pin نشست OpenAI PI کهنه بدون پیکربندی صریح runtime دارد، آن را ترمیم کنید:

bashCopy code
[code]
    openclaw doctor --fixopenclaw config validate
[/code]

اگر `models auth list --provider openai-codex` هیچ پروفایل قابل‌استفاده‌ای نشان نمی‌دهد، دوباره وارد شوید:

bashCopy code
[code]
    openclaw models auth login --provider openai-codexopenclaw models status --probe --probe-provider openai-codex
[/code]

`openai/*` مسیر مدل برای نوبت‌های agent مربوط به OpenAI از طریق Codex است. شناسه provider احراز هویت/پروفایل `openai-codex` همچنان برای پروفایل‌های موجود و فهرست‌کردن CLI پذیرفته می‌شود.

### نشانگر وضعیت

چت `/status` نشان می‌دهد کدام runtime مدل برای نشست فعلی فعال است. harness بسته‌بندی‌شده app-server مربوط به Codex برای نوبت‌های مدل agent مربوط به OpenAI به‌صورت `Runtime: OpenAI Codex` ظاهر می‌شود. pinهای کهنه نشست PI به Codex ترمیم می‌شوند، مگر اینکه پیکربندی به‌طور صریح PI را pin کرده باشد.

### هشدار Doctor

اگر مسیرهای `openai-codex/*` یا pinهای کهنه OpenAI PI در پیکربندی یا وضعیت نشست باقی مانده باشند، `openclaw doctor --fix` آن‌ها را به `openai/*` با runtime مربوط به Codex بازنویسی می‌کند، مگر اینکه PI به‌طور صریح پیکربندی شده باشد.

### سقف پنجره context

OpenClaw فراداده مدل و سقف context مربوط به runtime را به‌عنوان مقدارهای جداگانه در نظر می‌گیرد.

برای `openai/gpt-5.5` از طریق کاتالوگ OAuth مربوط به Codex:

  * `contextWindow` بومی: `1000000`
  * سقف پیش‌فرض runtime `contextTokens`: `272000`


سقف پیش‌فرض کوچک‌تر در عمل ویژگی‌های تاخیر و کیفیت بهتری دارد. آن را با `contextTokens` بازنویسی کنید:

json5Copy code
[code]
    {  models: {    providers: {      "openai-codex": {        models: [{ id: "gpt-5.5", contextTokens: 160000 }],      },    },  },}
[/code]

### بازیابی کاتالوگ

OpenClaw وقتی فراداده کاتالوگ upstream مربوط به Codex برای `gpt-5.5` موجود باشد، از آن استفاده می‌کند. اگر کشف زنده Codex ردیف `gpt-5.5` را درحالی‌که حساب احراز هویت شده است حذف کند، OpenClaw آن ردیف مدل OAuth را می‌سازد تا اجراهای cron، sub-agent، و مدل پیش‌فرض پیکربندی‌شده با `Unknown model` شکست نخورند.

## احراز هویت app-server بومی Codex

harness بومی app-server مربوط به Codex از مرجع‌های مدل `openai/*` به‌همراه پیکربندی runtime حذف‌شده یا provider/model `agentRuntime.id: "codex"` استفاده می‌کند، اما احراز هویت آن همچنان مبتنی بر حساب است. OpenClaw احراز هویت را به این ترتیب انتخاب می‌کند:

  1. پروفایل‌های احراز هویت مرتب‌شده OpenAI برای agent، ترجیحا زیر `auth.order.openai`. پروفایل‌های موجود `openai-codex:*` و `auth.order.openai-codex` برای نصب‌های قدیمی‌تر همچنان معتبر می‌مانند.
  2. حساب موجود app-server، مانند ورود محلی Codex CLI به ChatGPT.
  3. فقط برای راه‌اندازی‌های app-server محلی stdio، `CODEX_API_KEY`، سپس `OPENAI_API_KEY`، وقتی app-server هیچ حسابی گزارش نمی‌کند و همچنان به احراز هویت OpenAI نیاز دارد.


این یعنی ورود محلی با اشتراک ChatGPT/Codex فقط به این دلیل جایگزین نمی‌شود که فرایند gateway همچنین برای مدل‌های مستقیم OpenAI یا embeddingها `OPENAI_API_KEY` دارد. fallback کلید API در env فقط مسیر محلی stdio بدون حساب است؛ به اتصال‌های app-server از نوع WebSocket فرستاده نمی‌شود. وقتی یک پروفایل Codex به سبک اشتراک انتخاب می‌شود، OpenClaw همچنین `CODEX_API_KEY` و `OPENAI_API_KEY` را از فرزند app-server راه‌اندازی‌شده stdio بیرون نگه می‌دارد و اعتبارنامه‌های انتخاب‌شده را از طریق RPC ورود app-server می‌فرستد. وقتی آن پروفایل اشتراک به‌دلیل محدودیت استفاده Codex مسدود شود، OpenClaw می‌تواند بدون تغییر مدل انتخاب‌شده یا خروج از harness مربوط به Codex، به پروفایل بعدی مرتب‌شده کلید API از نوع `openai:*` بچرخد. پس از گذشت زمان reset اشتراک، پروفایل اشتراک دوباره واجد شرایط می‌شود.

## تولید تصویر

Plugin بسته‌بندی‌شده `openai` تولید تصویر را از طریق ابزار `image_generate` ثبت می‌کند. این ابزار هم تولید تصویر با کلید API مربوط به OpenAI و هم تولید تصویر با OAuth مربوط به Codex را از طریق همان مرجع مدل `openai/gpt-image-2` پشتیبانی می‌کند.

قابلیت | کلید API مربوط به OpenAI | OAuth مربوط به Codex  
---|---|---  
مرجع مدل | `openai/gpt-image-2` | `openai/gpt-image-2`  
احراز هویت | `OPENAI_API_KEY` | ورود OAuth مربوط به OpenAI Codex  
انتقال | OpenAI Images API | backend مربوط به Codex Responses  
بیشینه تصاویر در هر درخواست | 4 | 4  
حالت ویرایش | فعال (تا 5 تصویر مرجع) | فعال (تا 5 تصویر مرجع)  
بازنویسی اندازه‌ها | پشتیبانی می‌شود، شامل اندازه‌های 2K/4K | پشتیبانی می‌شود، شامل اندازه‌های 2K/4K  
نسبت تصویر / وضوح | به OpenAI Images API ارسال نمی‌شود | وقتی امن باشد به یک اندازه پشتیبانی‌شده نگاشت می‌شود  
json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: { primary: "openai/gpt-image-2" },    },  },}
[/code]

`gpt-image-2` پیش‌فرض برای تولید متن‌به‌تصویر و ویرایش تصویر OpenAI است. `gpt-image-1.5`، `gpt-image-1`، و `gpt-image-1-mini` همچنان به‌عنوان بازنویسی‌های صریح مدل قابل استفاده می‌مانند. برای خروجی PNG/WebP با پس‌زمینه شفاف از `openai/gpt-image-1.5` استفاده کنید؛ API فعلی `gpt-image-2` `background: "transparent"` را رد می‌کند.

برای یک درخواست پس‌زمینه شفاف، agentها باید `image_generate` را با `model: "openai/gpt-image-1.5"`، `outputFormat: "png"` یا `"webp"`، و `background: "transparent"` فراخوانی کنند؛ گزینه قدیمی‌تر provider یعنی `openai.background` همچنان پذیرفته می‌شود. OpenClaw همچنین از مسیرهای عمومی OpenAI و OpenAI Codex OAuth با بازنویسی درخواست‌های شفاف پیش‌فرض `openai/gpt-image-2` به `gpt-image-1.5` محافظت می‌کند؛ endpointهای Azure و endpointهای سفارشی سازگار با OpenAI نام‌های deployment/model پیکربندی‌شده خود را نگه می‌دارند.

همان تنظیم برای اجراهای CLI بدون محیط گرافیکی نیز ارائه شده است:

bashCopy code
[code]
    openclaw infer image generate \  --model openai/gpt-image-1.5 \  --output-format png \  --background transparent \  --prompt "A simple red circle sticker on a transparent background" \  --json
[/code]

هنگام شروع از یک فایل ورودی، همان flagهای `--output-format` و `--background` را با `openclaw infer image edit` استفاده کنید. `--openai-background` همچنان به‌عنوان alias ویژه OpenAI دردسترس است.

برای نصب‌های OAuth مربوط به Codex، همان مرجع `openai/gpt-image-2` را نگه دارید. وقتی یک پروفایل OAuth از نوع `openai-codex` پیکربندی شده باشد، OpenClaw آن توکن دسترسی OAuth ذخیره‌شده را resolve می‌کند و درخواست‌های تصویر را از طریق backend مربوط به Codex Responses می‌فرستد. این سیستم ابتدا `OPENAI_API_KEY` را امتحان نمی‌کند یا برای آن درخواست بی‌صدا به کلید API fallback نمی‌کند. وقتی مسیر مستقیم OpenAI Images API را می‌خواهید، `models.providers.openai` را به‌طور صریح با یک کلید API، URL پایه سفارشی، یا endpoint مربوط به Azure پیکربندی کنید. اگر آن endpoint تصویر سفارشی روی یک LAN/نشانی خصوصی مورد اعتماد است، همچنین `browser.ssrfPolicy.dangerouslyAllowPrivateNetwork: true` را تنظیم کنید؛ OpenClaw endpointهای تصویر خصوصی/داخلی سازگار با OpenAI را مسدود نگه می‌دارد مگر اینکه این opt-in وجود داشته باشد.

تولید:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-2 prompt="A polished launch poster for OpenClaw on macOS" size=3840x2160 count=1
[/code]

تولید یک PNG شفاف:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-1.5 prompt="A simple red circle sticker on a transparent background" outputFormat=png background=transparent
[/code]

ویرایش:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-2 prompt="Preserve the object shape, change the material to translucent glass" image=/path/to/reference.png size=1024x1536
[/code]

## تولید ویدیو

Plugin همراه `openai` تولید ویدئو را از طریق ابزار `video_generate` ثبت می‌کند.

قابلیت | مقدار  
---|---  
مدل پیش‌فرض | `openai/sora-2`  
حالت‌ها | متن به ویدئو، تصویر به ویدئو، ویرایش تک‌ویدئویی  
ورودی‌های مرجع | ۱ تصویر یا ۱ ویدئو  
بازنویسی‌های اندازه | پشتیبانی می‌شود  
بازنویسی‌های دیگر | `aspectRatio`، `resolution`، `audio`، `watermark` با هشدار ابزار نادیده گرفته می‌شوند  
json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: { primary: "openai/sora-2" },    },  },}
[/code]

## مشارکت پرامپت GPT-5

OpenClaw یک مشارکت پرامپت مشترک GPT-5 را برای اجراهای خانواده GPT-5 در میان ارائه‌دهندگان اضافه می‌کند. این بر اساس شناسه مدل اعمال می‌شود، بنابراین `openai/gpt-5.5`، ارجاع‌های قدیمی پیش از تعمیر مانند `openai-codex/gpt-5.5`، `openrouter/openai/gpt-5.5`، `opencode/gpt-5.5`، و دیگر ارجاع‌های سازگار GPT-5 همان هم‌پوشانی را دریافت می‌کنند. مدل‌های قدیمی‌تر GPT-4.x این هم‌پوشانی را دریافت نمی‌کنند.

مهار بومی Codex همراه، همان رفتار GPT-5 و هم‌پوشانی heartbeat را از طریق دستورالعمل‌های توسعه‌دهنده app-server در Codex استفاده می‌کند، بنابراین نشست‌های `openai/gpt-5.x` که از طریق Codex مسیریابی می‌شوند همان راهنمایی پیگیری و heartbeat پیش‌دستانه را حفظ می‌کنند، هرچند Codex مالک بقیه پرامپت مهار است.

مشارکت GPT-5 یک قرارداد رفتاری برچسب‌دار برای پایداری پرسونا، ایمنی اجرا، انضباط ابزار، شکل خروجی، بررسی‌های تکمیل، و راستی‌آزمایی اضافه می‌کند. رفتار پاسخ مخصوص کانال و پیام خاموش در پرامپت سیستم مشترک OpenClaw و سیاست تحویل خروجی باقی می‌ماند. راهنمایی GPT-5 برای مدل‌های منطبق همیشه فعال است. لایه سبک تعامل دوستانه جدا و قابل پیکربندی است.

مقدار | اثر  
---|---  
`"friendly"` (پیش‌فرض) | فعال‌سازی لایه سبک تعامل دوستانه  
`"on"` | نام مستعار برای `"friendly"`  
`"off"` | فقط لایه سبک دوستانه را غیرفعال می‌کند  
  
### پیکربندی

json5Copy code
[code]
    {  agents: {    defaults: {      promptOverlays: {        gpt5: { personality: "friendly" },      },    },  },}
[/code]

### CLI

bashCopy code
[code]
    openclaw config set agents.defaults.promptOverlays.gpt5.personality off
[/code]

## صدا و گفتار

سنتز گفتار (TTS)

Plugin همراه `openai` سنتز گفتار را برای سطح `messages.tts` ثبت می‌کند.

تنظیم | مسیر پیکربندی | پیش‌فرض  
---|---|---  
مدل | `messages.tts.providers.openai.model` | `gpt-4o-mini-tts`  
صدا | `messages.tts.providers.openai.voice` | `coral`  
سرعت | `messages.tts.providers.openai.speed` | (تنظیم‌نشده)  
دستورالعمل‌ها | `messages.tts.providers.openai.instructions` | (تنظیم‌نشده، فقط `gpt-4o-mini-tts`)  
قالب | `messages.tts.providers.openai.responseFormat` | `opus` برای یادداشت‌های صوتی، `mp3` برای فایل‌ها  
کلید API | `messages.tts.providers.openai.apiKey` | به `OPENAI_API_KEY` برمی‌گردد  
نشانی پایه | `messages.tts.providers.openai.baseUrl` | `https://api.openai.com/v1`  
بدنه اضافی | `messages.tts.providers.openai.extraBody` / `extra_body` | (تنظیم‌نشده)  
  
مدل‌های موجود: `gpt-4o-mini-tts`، `tts-1`، `tts-1-hd`. صداهای موجود: `alloy`، `ash`، `ballad`، `cedar`، `coral`، `echo`، `fable`، `juniper`، `marin`، `onyx`، `nova`، `sage`، `shimmer`، `verse`.

`extraBody` پس از فیلدهای تولیدشده OpenClaw در JSON درخواست `/audio/speech` ادغام می‌شود، بنابراین از آن برای endpointهای سازگار با OpenAI که به کلیدهای اضافی مانند `lang` نیاز دارند استفاده کنید. کلیدهای پروتوتایپ نادیده گرفته می‌شوند.

json5Copy code
[code]
    {  messages: {    tts: {      providers: {        openai: { model: "gpt-4o-mini-tts", voice: "coral" },      },    },  },}
[/code]

گفتار به متن

Plugin همراه `openai` گفتار به متن دسته‌ای را از طریق سطح رونویسی درک رسانه OpenClaw ثبت می‌کند.

  * مدل پیش‌فرض: `gpt-4o-transcribe`
  * Endpoint: OpenAI REST `/v1/audio/transcriptions`
  * مسیر ورودی: بارگذاری فایل صوتی چندبخشی
  * پشتیبانی‌شده توسط OpenClaw در هر جایی که رونویسی صوت ورودی از `tools.media.audio` استفاده می‌کند، از جمله بخش‌های کانال صوتی Discord و پیوست‌های صوتی کانال


برای اجبار OpenAI برای رونویسی صوت ورودی:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [          {            type: "provider",            provider: "openai",            model: "gpt-4o-transcribe",          },        ],      },    },  },}
[/code]

راهنمایی‌های زبان و پرامپت زمانی که توسط پیکربندی رسانه صوتی مشترک یا درخواست رونویسی هر فراخوانی ارائه شوند، به OpenAI ارسال می‌شوند.

Realtime transcription

Plugin همراه `openai` رونویسی بلادرنگ را برای Plugin تماس صوتی ثبت می‌کند.

تنظیم | مسیر پیکربندی | پیش‌فرض  
---|---|---  
مدل | `plugins.entries.voice-call.config.streaming.providers.openai.model` | `gpt-4o-transcribe`  
زبان | `...openai.language` | (تنظیم‌نشده)  
پرامپت | `...openai.prompt` | (تنظیم‌نشده)  
مدت سکوت | `...openai.silenceDurationMs` | `800`  
آستانه VAD | `...openai.vadThreshold` | `0.5`  
احراز هویت | `...openai.apiKey`، `OPENAI_API_KEY`، یا OAuth مربوط به `openai-codex` | کلیدهای API مستقیم متصل می‌شوند؛ OAuth یک راز کلاینت رونویسی Realtime صادر می‌کند  
Realtime voice

Plugin همراه `openai` صدای بلادرنگ را برای Plugin تماس صوتی ثبت می‌کند.

تنظیم | مسیر پیکربندی | پیش‌فرض  
---|---|---  
مدل | `plugins.entries.voice-call.config.realtime.providers.openai.model` | `gpt-realtime-2`  
صدا | `...openai.voice` | `alloy`  
دما (پل استقرار Azure) | `...openai.temperature` | `0.8`  
آستانه VAD | `...openai.vadThreshold` | `0.5`  
مدت سکوت | `...openai.silenceDurationMs` | `500`  
فاصله‌گذاری پیشوند | `...openai.prefixPaddingMs` | `300`  
تلاش استدلال | `...openai.reasoningEffort` | (تنظیم‌نشده)  
احراز هویت | `...openai.apiKey`، `OPENAI_API_KEY`، یا OAuth مربوط به `openai-codex` | پل‌های Browser Talk و بک‌اند غیر Azure می‌توانند از OAuth مربوط به Codex استفاده کنند  
  
صداهای داخلی Realtime موجود برای `gpt-realtime-2`: `alloy`، `ash`، `ballad`، `coral`، `echo`، `sage`، `shimmer`، `verse`، `marin`، `cedar`. OpenAI برای بهترین کیفیت Realtime، `marin` و `cedar` را توصیه می‌کند. این مجموعه‌ای جدا از صداهای تبدیل متن به گفتار بالاست؛ فرض نکنید یک صدای TTS مانند `fable`، `nova`، یا `onyx` برای نشست‌های Realtime معتبر است.

## نقطه‌های پایانی Azure OpenAI

ارائه‌دهنده همراه `openai` می‌تواند با بازنویسی URL پایه، یک منبع Azure OpenAI را برای تولید تصویر هدف بگیرد. در مسیر تولید تصویر، OpenClaw نام‌های میزبان Azure را در `models.providers.openai.baseUrl` تشخیص می‌دهد و به‌صورت خودکار به شکل درخواست Azure تغییر می‌کند.

از Azure OpenAI استفاده کنید وقتی:

  * از قبل اشتراک، سهمیه، یا قرارداد سازمانی Azure OpenAI دارید
  * به اقامت منطقه‌ای داده یا کنترل‌های انطباقی که Azure فراهم می‌کند نیاز دارید
  * می‌خواهید ترافیک را داخل یک tenancy موجود Azure نگه دارید


### پیکربندی

برای تولید تصویر Azure از طریق ارائه‌دهنده همراه `openai`، `models.providers.openai.baseUrl` را به منبع Azure خود اشاره دهید و `apiKey` را روی کلید Azure OpenAI تنظیم کنید (نه کلید OpenAI Platform):

json5Copy code
[code]
    {  models: {    providers: {      openai: {        baseUrl: "https://<your-resource>.openai.azure.com",        apiKey: "<azure-openai-api-key>",      },    },  },}
[/code]

OpenClaw این پسوندهای میزبان Azure را برای مسیر تولید تصویر Azure تشخیص می‌دهد:

  * `*.openai.azure.com`
  * `*.services.ai.azure.com`
  * `*.cognitiveservices.azure.com`


برای درخواست‌های تولید تصویر روی یک میزبان Azure شناخته‌شده، OpenClaw:

  * هدر `api-key` را به‌جای `Authorization: Bearer` ارسال می‌کند
  * از مسیرهای محدوده‌بندی‌شده به استقرار استفاده می‌کند (`/openai/deployments/{deployment}/...`)
  * به هر درخواست `?api-version=...` اضافه می‌کند
  * از زمان‌انتظار پیش‌فرض 600 ثانیه برای فراخوانی‌های تولید تصویر Azure استفاده می‌کند. مقادیر `timeoutMs` در هر فراخوانی همچنان این پیش‌فرض را بازنویسی می‌کنند.


URLهای پایه دیگر (OpenAI عمومی، پراکسی‌های سازگار با OpenAI) شکل استاندارد درخواست تصویر OpenAI را حفظ می‌کنند.

### نسخه API

`AZURE_OPENAI_API_VERSION` را تنظیم کنید تا یک نسخه پیش‌نمایش یا GA خاص Azure برای مسیر تولید تصویر Azure ثابت شود:

bashCopy code
[code]
    export AZURE_OPENAI_API_VERSION="2024-12-01-preview"
[/code]

وقتی این متغیر تنظیم نشده باشد، مقدار پیش‌فرض `2024-12-01-preview` است.

### نام‌های مدل، نام‌های استقرار هستند

Azure OpenAI مدل‌ها را به استقرارها متصل می‌کند. برای درخواست‌های تولید تصویر Azure که از طریق ارائه‌دهنده همراه `openai` مسیریابی می‌شوند، فیلد `model` در OpenClaw باید **نام استقرار Azure** باشد که در پورتال Azure پیکربندی کرده‌اید، نه شناسه عمومی مدل OpenAI.

اگر یک استقرار با نام `gpt-image-2-prod` بسازید که `gpt-image-2` را ارائه می‌کند:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-2-prod prompt="A clean poster" size=1024x1024 count=1
[/code]

همین قاعده نام استقرار برای فراخوانی‌های تولید تصویر که از طریق ارائه‌دهنده همراه `openai` مسیریابی می‌شوند نیز اعمال می‌شود.

### دسترس‌پذیری منطقه‌ای

تولید تصویر Azure در حال حاضر فقط در زیرمجموعه‌ای از مناطق در دسترس است (برای مثال `eastus2`، `swedencentral`، `polandcentral`، `westus3`، `uaenorth`). پیش از ساخت یک استقرار، فهرست فعلی مناطق Microsoft را بررسی کنید و تأیید کنید که مدل مشخص در منطقه شما ارائه می‌شود.

### تفاوت‌های پارامترها

Azure OpenAI و OpenAI عمومی همیشه پارامترهای تصویر یکسانی را نمی‌پذیرند. Azure ممکن است گزینه‌هایی را که OpenAI عمومی اجازه می‌دهد رد کند (برای مثال برخی مقادیر `background` روی `gpt-image-2`) یا آن‌ها را فقط روی نسخه‌های مشخص مدل در دسترس قرار دهد. این تفاوت‌ها از Azure و مدل زیربنایی می‌آیند، نه از OpenClaw. اگر یک درخواست Azure با خطای اعتبارسنجی شکست خورد، مجموعه پارامترهای پشتیبانی‌شده توسط استقرار و نسخه API مشخص خود را در پورتال Azure بررسی کنید.

## پیکربندی پیشرفته

انتقال (WebSocket در برابر SSE)

OpenClaw برای `openai/*` ابتدا از WebSocket استفاده می‌کند و در صورت نیاز به SSE برمی‌گردد (`"auto"`).

در حالت `"auto"`، OpenClaw:

  * پیش از بازگشت به SSE، یک شکست زودهنگام WebSocket را یک بار دوباره تلاش می‌کند
  * پس از یک شکست، WebSocket را برای حدود ۶۰ ثانیه به‌عنوان تنزل‌یافته علامت‌گذاری می‌کند و در زمان خنک‌سازی از SSE استفاده می‌کند
  * سرآیندهای پایدار هویت نشست و نوبت را برای تلاش‌های دوباره و اتصال‌های مجدد پیوست می‌کند
  * شمارنده‌های مصرف (`input_tokens` / `prompt_tokens`) را میان گونه‌های انتقال نرمال‌سازی می‌کند

مقدار | رفتار  
---|---  
`"auto"` (پیش‌فرض) | ابتدا WebSocket، بازگشت به SSE  
`"sse"` | فقط SSE را اجباری کن  
`"websocket"` | فقط WebSocket را اجباری کن  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          params: { transport: "auto" },        },      },    },  },}
[/code]

مستندات مرتبط OpenAI:

  * [Realtime API با WebSocket](<https://platform.openai.com/docs/guides/realtime-websocket>)
  * [پاسخ‌های Streaming API (SSE)](<https://platform.openai.com/docs/guides/streaming-responses>)

حالت سریع

OpenClaw یک کلید مشترک حالت سریع برای `openai/*` ارائه می‌کند:

  * **Chat/UI:** `/fast status|on|off`
  * **پیکربندی:** `agents.defaults.models["<provider>/<model>"].params.fastMode`


وقتی فعال باشد، OpenClaw حالت سریع را به پردازش اولویت‌دار OpenAI نگاشت می‌کند (`service_tier = "priority"`). مقادیر موجود `service_tier` حفظ می‌شوند و حالت سریع `reasoning` یا `text.verbosity` را بازنویسی نمی‌کند.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": { params: { fastMode: true } },      },    },  },}
[/code]

پردازش اولویت‌دار (service_tier)

API متعلق به OpenAI پردازش اولویت‌دار را از طریق `service_tier` ارائه می‌کند. آن را برای هر مدل در OpenClaw تنظیم کنید:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": { params: { serviceTier: "priority" } },      },    },  },}
[/code]

مقادیر پشتیبانی‌شده: `auto`، `default`، `flex`، `priority`.

Compaction سمت سرور (Responses API)

برای مدل‌های مستقیم OpenAI Responses (`openai/*` روی `api.openai.com`)، پوشش‌دهنده جریان Pi-harness متعلق به Plugin OpenAI به‌طور خودکار Compaction سمت سرور را فعال می‌کند:

  * `store: true` را اجباری می‌کند (مگر اینکه سازگاری مدل `supportsStore: false` را تنظیم کند)
  * `context_management: [{ type: "compaction", compact_threshold: ... }]` را تزریق می‌کند
  * مقدار پیش‌فرض `compact_threshold`: برابر با ۷۰٪ از `contextWindow` (یا در صورت نبود آن `80000`)


این مورد بر مسیر Pi harness داخلی و hookهای ارائه‌دهنده OpenAI که توسط اجراهای تعبیه‌شده استفاده می‌شوند اعمال می‌شود. harness بومی app-server متعلق به Codex زمینه خود را از طریق Codex مدیریت می‌کند و توسط مسیر عامل پیش‌فرض OpenAI یا سیاست runtime ارائه‌دهنده/مدل پیکربندی می‌شود.

### فعال‌سازی صریح

برای نقاط پایانی سازگار مانند Azure OpenAI Responses مفید است:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "azure-openai-responses/gpt-5.5": {          params: { responsesServerCompaction: true },        },      },    },  },}
[/code]

### آستانه سفارشی

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          params: {            responsesServerCompaction: true,            responsesCompactThreshold: 120000,          },        },      },    },  },}
[/code]

### غیرفعال‌سازی

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          params: { responsesServerCompaction: false },        },      },    },  },}
[/code]

حالت GPT عاملانه سخت‌گیرانه

برای اجراهای خانواده GPT-5 روی `openai/*`، OpenClaw می‌تواند از یک قرارداد اجرای تعبیه‌شده سخت‌گیرانه‌تر استفاده کند:

json5Copy code
[code]
    {  agents: {    defaults: {      embeddedPi: { executionContract: "strict-agentic" },    },  },}
[/code]

با `strict-agentic`، OpenClaw:

  * دیگر نوبتی را که فقط شامل برنامه است، وقتی یک اقدام ابزاری در دسترس باشد، پیشرفت موفق محسوب نمی‌کند
  * نوبت را با هدایت «اکنون اقدام کن» دوباره تلاش می‌کند
  * برای کارهای قابل‌توجه `update_plan` را به‌طور خودکار فعال می‌کند
  * اگر مدل بدون اقدام کردن به برنامه‌ریزی ادامه دهد، یک وضعیت مسدودشده صریح نشان می‌دهد

مسیرهای بومی در برابر مسیرهای سازگار با OpenAI

OpenClaw با نقاط پایانی مستقیم OpenAI، Codex و Azure OpenAI متفاوت از پراکسی‌های عمومی سازگار با OpenAI در `/v1` رفتار می‌کند:

**مسیرهای بومی** (`openai/*`، Azure OpenAI):

  * `reasoning: { effort: "none" }` را فقط برای مدل‌هایی نگه می‌دارد که از effort مقدار `none` متعلق به OpenAI پشتیبانی می‌کنند
  * استدلال غیرفعال‌شده را برای مدل‌ها یا پراکسی‌هایی که `reasoning.effort: "none"` را رد می‌کنند حذف می‌کند
  * طرح‌واره‌های ابزار را به‌طور پیش‌فرض در حالت سخت‌گیرانه قرار می‌دهد
  * سرآیندهای انتساب پنهان را فقط روی میزبان‌های بومی تأییدشده پیوست می‌کند
  * شکل‌دهی درخواست مخصوص OpenAI را نگه می‌دارد (`service_tier`، `store`، سازگاری reasoning، اشاره‌های prompt-cache)


**مسیرهای پراکسی/سازگار:**

  * از رفتار سازگاری سهل‌گیرانه‌تر استفاده می‌کنند
  * مقدار `store` مربوط به Completions را از payloadهای غیر بومی `openai-completions` حذف می‌کنند
  * JSON عبوری پیشرفته `params.extra_body`/`params.extraBody` را برای پراکسی‌های Completions سازگار با OpenAI می‌پذیرند
  * `params.chat_template_kwargs` را برای پراکسی‌های Completions سازگار با OpenAI مانند vLLM می‌پذیرند
  * طرح‌واره‌های سخت‌گیرانه ابزار یا سرآیندهای فقط بومی را اجباری نمی‌کنند


Azure OpenAI از انتقال بومی و رفتار سازگاری استفاده می‌کند اما سرآیندهای انتساب پنهان را دریافت نمی‌کند.

## مرتبط

[**انتخاب مدل** انتخاب ارائه‌دهندگان، ارجاع‌های مدل، و رفتار failover. ](</fa/concepts/model-providers>) [**تولید تصویر** پارامترهای مشترک ابزار تصویر و انتخاب ارائه‌دهنده. ](</fa/tools/image-generation>) [**تولید ویدئو** پارامترهای مشترک ابزار ویدئو و انتخاب ارائه‌دهنده. ](</fa/tools/video-generation>) [**OAuth و احراز هویت** جزئیات احراز هویت و قواعد استفاده دوباره از اعتبارنامه‌ها. ](</fa/gateway/authentication>)

Was this useful?YesNo