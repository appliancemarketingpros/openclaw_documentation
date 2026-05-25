---
title: Alibaba Model Studio
source_url: https://docs.openclaw.ai/fa/providers/alibaba
scraped_at: 2026-05-25
---

OpenClaw یک Plugin داخلی `alibaba` را همراه خود ارائه می‌دهد که یک ارائه‌دهنده تولید ویدیو برای مدل‌های Wan روی Alibaba Model Studio (نام بین‌المللی DashScope) ثبت می‌کند. این Plugin به‌صورت پیش‌فرض فعال است؛ فقط باید یک کلید API تنظیم کنید.

ویژگی | مقدار  
---|---  
شناسه ارائه‌دهنده | `alibaba`  
Plugin | همراه، `enabledByDefault: true`  
متغیرهای محیطی احراز هویت | `MODELSTUDIO_API_KEY` → `DASHSCOPE_API_KEY` → `QWEN_API_KEY` (اولین مورد منطبق برنده است)  
پرچم راه‌اندازی اولیه | `--auth-choice alibaba-model-studio-api-key`  
پرچم مستقیم CLI | `--alibaba-model-studio-api-key <key>`  
مدل پیش‌فرض | `alibaba/wan2.6-t2v`  
URL پایه پیش‌فرض | `https://dashscope-intl.aliyuncs.com`  
  
## شروع به کار

* ### تنظیم یک کلید API

برای ذخیره کلید برای ارائه‌دهنده `alibaba` از راه‌اندازی اولیه استفاده کنید:

bashCopy code
[code]
    openclaw onboard --auth-choice alibaba-model-studio-api-key
[/code]

یا کلید را هنگام نصب/راه‌اندازی اولیه مستقیماً وارد کنید:

bashCopy code
[code]
    openclaw onboard --alibaba-model-studio-api-key <your-key>
[/code]

یا پیش از راه‌اندازی Gateway، هرکدام از متغیرهای محیطی پذیرفته‌شده را export کنید:

bashCopy code
[code]
    export MODELSTUDIO_API_KEY=sk-...# or DASHSCOPE_API_KEY=...# or QWEN_API_KEY=...
[/code]

* ### تنظیم یک مدل ویدیوی پیش‌فرض

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "alibaba/wan2.6-t2v",      },    },  },}
[/code]

* ### بررسی پیکربندی بودن ارائه‌دهنده

bashCopy code
[code]
    openclaw models list --provider alibaba
[/code]

فهرست باید شامل هر پنج مدل داخلی Wan باشد. اگر `MODELSTUDIO_API_KEY` قابل حل نباشد، `openclaw models status --json` اعتبارنامه گمشده را زیر `auth.unusableProfiles` گزارش می‌کند.

## مدل‌های داخلی Wan

ارجاع مدل | حالت  
---|---  
`alibaba/wan2.6-t2v` | متن به ویدیو (پیش‌فرض)  
`alibaba/wan2.6-i2v` | تصویر به ویدیو  
`alibaba/wan2.6-r2v` | مرجع به ویدیو  
`alibaba/wan2.6-r2v-flash` | مرجع به ویدیو (سریع)  
`alibaba/wan2.7-r2v` | مرجع به ویدیو  
  
## قابلیت‌ها و محدودیت‌ها

ارائه‌دهنده داخلی، سقف‌های API ویدیوی Wan در DashScope را بازتاب می‌دهد. هر سه حالت تعداد ویدیو در هر درخواست و سقف مدت یکسانی دارند؛ فقط شکل ورودی متفاوت است.

حالت | حداکثر ویدیوهای خروجی | حداکثر تصاویر ورودی | حداکثر ویدیوهای ورودی | حداکثر مدت | کنترل‌های پشتیبانی‌شده  
---|---|---|---|---|---  
متن به ویدیو | 1 | نامرتبط | نامرتبط | 10 ثانیه | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
تصویر به ویدیو | 1 | 1 | نامرتبط | 10 ثانیه | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
مرجع به ویدیو | 1 | نامرتبط | 4 | 10 ثانیه | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
  
وقتی درخواستی `durationSeconds` را حذف کند، ارائه‌دهنده مقدار پیش‌فرض پذیرفته‌شده DashScope یعنی **5 ثانیه** را می‌فرستد. برای افزایش تا 10 ثانیه، `durationSeconds` را صراحتاً روی [ابزار تولید ویدیو](</fa/tools/video-generation>) تنظیم کنید.

## پیکربندی پیشرفته

نادیده‌گرفتن URL پایه DashScope

ارائه‌دهنده به‌صورت پیش‌فرض از endpoint بین‌المللی DashScope استفاده می‌کند. برای هدف‌گیری endpoint منطقه چین، این مورد را تنظیم کنید:

json5Copy code
[code]
    {  models: {    providers: {      alibaba: {        baseUrl: "https://dashscope.aliyuncs.com",      },    },  },}
[/code]

ارائه‌دهنده پیش از ساخت URLهای وظیفه AIGC، اسلش‌های انتهایی را حذف می‌کند.

اولویت متغیر محیطی احراز هویت

OpenClaw کلید API مربوط به Alibaba را به این ترتیب از متغیرهای محیطی حل می‌کند و اولین مقدار غیرخالی را برمی‌دارد:

  1. `MODELSTUDIO_API_KEY`
  2. `DASHSCOPE_API_KEY`
  3. `QWEN_API_KEY`


ورودی‌های پیکربندی‌شده `auth.profiles` (که از طریق `openclaw models auth login` تنظیم می‌شوند) حل متغیر محیطی را نادیده می‌گیرند. برای چرخش پروفایل، cooldown و سازوکارهای نادیده‌گیری، [پروفایل‌های احراز هویت در پرسش‌های متداول مدل‌ها](</fa/help/faq-models#what-is-an-auth-profile>) را ببینید.

ارتباط با Plugin مربوط به Qwen

هر دو Plugin داخلی با DashScope ارتباط می‌گیرند و کلیدهای API هم‌پوشان را می‌پذیرند. استفاده کنید از:

  * شناسه‌های `alibaba/wan*.*` برای هدایت ارائه‌دهنده اختصاصی ویدیوی Wan که در این صفحه مستند شده است.
  * شناسه‌های `qwen/*` برای چت، embedding و درک رسانه Qwen ([Qwen](</fa/providers/qwen>) را ببینید).


تنظیم یک‌باره `MODELSTUDIO_API_KEY` هر دو Plugin را احراز هویت می‌کند، چون فهرست متغیرهای محیطی احراز هویت عمداً هم‌پوشانی دارد؛ لازم نیست هر Plugin را جداگانه راه‌اندازی اولیه کنید.

## مرتبط

[**تولید ویدیو** پارامترهای مشترک ابزار ویدیو و انتخاب ارائه‌دهنده. ](</fa/tools/video-generation>) [**Qwen** راه‌اندازی چت، embedding و درک رسانه Qwen روی همان احراز هویت DashScope. ](</fa/providers/qwen>) [**مرجع پیکربندی** پیش‌فرض‌های عامل و پیکربندی مدل. ](</fa/gateway/config-agents#agent-defaults>) [**پرسش‌های متداول مدل‌ها** پروفایل‌های احراز هویت، تعویض مدل‌ها، و حل خطاهای «بدون پروفایل». ](</fa/help/faq-models>)

Was this useful?YesNo