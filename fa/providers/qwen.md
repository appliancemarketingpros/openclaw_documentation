---
title: Qwen
source_url: https://docs.openclaw.ai/fa/providers/qwen
scraped_at: 2026-05-25
---

OpenClaw اکنون Qwen را به‌عنوان یک ارائه‌دهندهٔ همراهِ درجه‌یک با شناسهٔ canonical `qwen` در نظر می‌گیرد. ارائه‌دهندهٔ همراه، نقاط پایانی Qwen Cloud / Alibaba DashScope و Coding Plan را هدف می‌گیرد و شناسه‌های قدیمی `modelstudio` را به‌عنوان نام مستعار سازگاری فعال نگه می‌دارد.

  * ارائه‌دهنده: `qwen`
  * متغیر محیطی ترجیحی: `QWEN_API_KEY`
  * برای سازگاری نیز پذیرفته می‌شود: `MODELSTUDIO_API_KEY`, `DASHSCOPE_API_KEY`
  * سبک API: سازگار با OpenAI


## شروع به کار

نوع طرح خود را انتخاب کنید و مراحل راه‌اندازی را دنبال کنید.

### Coding Plan (subscription)

**بهترین برای:** دسترسی مبتنی بر اشتراک از طریق Qwen Coding Plan.

* ### Get your API key

یک کلید API را از [home.qwencloud.com/api-keys](<https://home.qwencloud.com/api-keys>) بسازید یا کپی کنید.

* ### Run onboarding

برای نقطهٔ پایانی **جهانی** :

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-api-key
[/code]

برای نقطهٔ پایانی **چین** :

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-api-key-cn
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "qwen/qwen3.5-plus" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider qwen
[/code]

### Standard (pay-as-you-go)

**بهترین برای:** دسترسی پرداخت به‌ازای مصرف از طریق نقطهٔ پایانی Standard Model Studio، شامل مدل‌هایی مانند `qwen3.6-plus` که ممکن است در Coding Plan در دسترس نباشند.

* ### Get your API key

یک کلید API را از [home.qwencloud.com/api-keys](<https://home.qwencloud.com/api-keys>) بسازید یا کپی کنید.

* ### Run onboarding

برای نقطهٔ پایانی **جهانی** :

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key
[/code]

برای نقطهٔ پایانی **چین** :

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key-cn
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "qwen/qwen3.5-plus" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider qwen
[/code]

## انواع طرح و نقاط پایانی

طرح | منطقه | گزینهٔ احراز هویت | نقطهٔ پایانی  
---|---|---|---  
استاندارد (پرداخت به‌ازای مصرف) | چین | `qwen-standard-api-key-cn` | `dashscope.aliyuncs.com/compatible-mode/v1`  
استاندارد (پرداخت به‌ازای مصرف) | جهانی | `qwen-standard-api-key` | `dashscope-intl.aliyuncs.com/compatible-mode/v1`  
Coding Plan (اشتراکی) | چین | `qwen-api-key-cn` | `coding.dashscope.aliyuncs.com/v1`  
Coding Plan (اشتراکی) | جهانی | `qwen-api-key` | `coding-intl.dashscope.aliyuncs.com/v1`  
  
ارائه‌دهنده بر اساس گزینهٔ احراز هویت شما نقطهٔ پایانی را به‌صورت خودکار انتخاب می‌کند. گزینه‌های canonical از خانوادهٔ `qwen-*` استفاده می‌کنند؛ `modelstudio-*` فقط برای سازگاری باقی مانده است. می‌توانید با یک `baseUrl` سفارشی در پیکربندی آن را override کنید.

## کاتالوگ داخلی

OpenClaw در حال حاضر این کاتالوگ همراه Qwen را ارائه می‌کند. کاتالوگ پیکربندی‌شده به نقطهٔ پایانی آگاه است: پیکربندی‌های Coding Plan مدل‌هایی را که فقط برای کار روی نقطهٔ پایانی استاندارد شناخته شده‌اند حذف می‌کنند.

ارجاع مدل | ورودی | زمینه | یادداشت‌ها  
---|---|---|---  
`qwen/qwen3.5-plus` | متن، تصویر | 1,000,000 | مدل پیش‌فرض  
`qwen/qwen3.6-plus` | متن، تصویر | 1,000,000 | وقتی به این مدل نیاز دارید، نقاط پایانی استاندارد را ترجیح دهید  
`qwen/qwen3-max-2026-01-23` | متن | 262,144 | خط Qwen Max  
`qwen/qwen3-coder-next` | متن | 262,144 | کدنویسی  
`qwen/qwen3-coder-plus` | متن | 1,000,000 | کدنویسی  
`qwen/MiniMax-M2.5` | متن | 1,000,000 | استدلال فعال  
`qwen/glm-5` | متن | 202,752 | GLM  
`qwen/glm-4.7` | متن | 202,752 | GLM  
`qwen/kimi-k2.5` | متن، تصویر | 262,144 | Moonshot AI از طریق Alibaba  
  
## کنترل‌های تفکر

برای مدل‌های Qwen Cloud با قابلیت استدلال، ارائه‌دهندهٔ همراه سطوح تفکر OpenClaw را به پرچم درخواست سطح‌بالای `enable_thinking` در DashScope نگاشت می‌کند. تفکر غیرفعال `enable_thinking: false` را می‌فرستد؛ سطوح دیگر تفکر `enable_thinking: true` را می‌فرستند.

## افزونه‌های چندوجهی

Plugin `qwen` همچنین قابلیت‌های چندوجهی را روی نقاط پایانی **استاندارد** DashScope ارائه می‌کند (نه نقاط پایانی Coding Plan):

  * **درک ویدئو** از طریق `qwen-vl-max-latest`
  * **تولید ویدئوی Wan** از طریق `wan2.6-t2v` (پیش‌فرض), `wan2.6-i2v`, `wan2.6-r2v`, `wan2.6-r2v-flash`, `wan2.7-r2v`


برای استفاده از Qwen به‌عنوان ارائه‌دهندهٔ پیش‌فرض ویدئو:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: { primary: "qwen/wan2.6-t2v" },    },  },}
[/code]

## پیکربندی پیشرفته

Image and video understanding

Plugin همراه Qwen درک رسانه را برای تصاویر و ویدئو روی نقاط پایانی **استاندارد** DashScope ثبت می‌کند (نه نقاط پایانی Coding Plan).

ویژگی | مقدار  
---|---  
مدل | `qwen-vl-max-latest`  
ورودی پشتیبانی‌شده | تصاویر، ویدئو  
  
درک رسانه از احراز هویت پیکربندی‌شدهٔ Qwen به‌صورت خودکار تعیین می‌شود؛ هیچ پیکربندی اضافی لازم نیست. مطمئن شوید برای پشتیبانی از درک رسانه از یک نقطهٔ پایانی استاندارد (پرداخت به‌ازای مصرف) استفاده می‌کنید.

Qwen 3.6 Plus availability

`qwen3.6-plus` روی نقاط پایانی Standard (pay-as-you-go) Model Studio در دسترس است:

  * چین: `dashscope.aliyuncs.com/compatible-mode/v1`
  * جهانی: `dashscope-intl.aliyuncs.com/compatible-mode/v1`


اگر نقاط پایانی Coding Plan برای `qwen3.6-plus` خطای "unsupported model" برگردانند، به‌جای جفت نقطهٔ پایانی/کلید Coding Plan به استاندارد (پرداخت به‌ازای مصرف) تغییر دهید.

کاتالوگ همراه Qwen در OpenClaw، `qwen3.6-plus` را روی نقاط پایانی Coding Plan تبلیغ نمی‌کند، اما ورودی‌های `qwen/qwen3.6-plus` که به‌صراحت زیر `models.providers.qwen.models` پیکربندی شده‌اند روی baseUrlهای Coding Plan رعایت می‌شوند تا اگر Aliyun آن مدل را روی اشتراک شما فعال کرد، بتوانید آن را فعال کنید. API بالادستی همچنان تعیین می‌کند که فراخوانی موفق شود یا نه.

Capability plan

Plugin `qwen` در جایگاه خانهٔ فروشنده برای سطح کامل قابلیت‌های Qwen Cloud قرار می‌گیرد، نه فقط مدل‌های کدنویسی/متنی.

  * **مدل‌های متن/چت:** اکنون همراه است
  * **فراخوانی ابزار، خروجی ساختاریافته، تفکر:** از انتقال سازگار با OpenAI به ارث می‌رسد
  * **تولید تصویر:** در لایهٔ provider-Plugin برنامه‌ریزی شده است
  * **درک تصویر/ویدئو:** اکنون روی نقطهٔ پایانی استاندارد همراه است
  * **گفتار/صدا:** در لایهٔ provider-Plugin برنامه‌ریزی شده است
  * **جاسازی‌های حافظه/بازرتبه‌بندی:** از طریق سطح آداپتور embedding برنامه‌ریزی شده است
  * **تولید ویدئو:** اکنون از طریق قابلیت مشترک تولید ویدئو همراه است

Video generation details

برای تولید ویدئو، OpenClaw قبل از ارسال کار، منطقهٔ Qwen پیکربندی‌شده را به میزبان AIGC متناظر DashScope نگاشت می‌کند:

  * جهانی/بین‌المللی: `https://dashscope-intl.aliyuncs.com`
  * چین: `https://dashscope.aliyuncs.com`


یعنی یک `models.providers.qwen.baseUrl` معمولی که به میزبان‌های Coding Plan یا Standard Qwen اشاره می‌کند همچنان تولید ویدئو را روی نقطهٔ پایانی ویدئوی DashScope منطقه‌ای درست نگه می‌دارد.

محدودیت‌های فعلی تولید ویدئوی Qwen همراه:

  * حداکثر **1** ویدئوی خروجی در هر درخواست
  * حداکثر **1** تصویر ورودی
  * حداکثر **4** ویدئوی ورودی
  * حداکثر **10 ثانیه** مدت‌زمان
  * از `size`, `aspectRatio`, `resolution`, `audio` و `watermark` پشتیبانی می‌کند
  * حالت تصویر/ویدئوی مرجع در حال حاضر به **URLهای دوردست http(s)** نیاز دارد. مسیرهای فایل محلی از ابتدا رد می‌شوند، چون نقطهٔ پایانی ویدئوی DashScope بافرهای محلی آپلودشده را برای آن ارجاع‌ها نمی‌پذیرد.

Streaming usage compatibility

نقاط پایانی بومی Model Studio سازگاری مصرف در جریان‌سازی را روی انتقال مشترک `openai-completions` اعلام می‌کنند. OpenClaw اکنون این را بر اساس قابلیت‌های نقطهٔ پایانی تعیین می‌کند، بنابراین شناسه‌های ارائه‌دهندهٔ سفارشی سازگار با DashScope که همان میزبان‌های بومی را هدف می‌گیرند همان رفتار مصرف در جریان‌سازی را به ارث می‌برند، بدون اینکه به‌طور خاص به شناسهٔ ارائه‌دهندهٔ داخلی `qwen` نیاز داشته باشند.

سازگاری مصرف در جریان‌سازی بومی هم برای میزبان‌های Coding Plan و هم برای میزبان‌های Standard سازگار با DashScope اعمال می‌شود:

  * `https://coding.dashscope.aliyuncs.com/v1`
  * `https://coding-intl.dashscope.aliyuncs.com/v1`
  * `https://dashscope.aliyuncs.com/compatible-mode/v1`
  * `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`

Multimodal endpoint regions

سطح‌های چندوجهی (درک ویدئو و تولید ویدئوی Wan) از نقاط پایانی **استاندارد** DashScope استفاده می‌کنند، نه نقاط پایانی Coding Plan:

  * URL پایهٔ استاندارد جهانی/بین‌المللی: `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`
  * URL پایهٔ استاندارد چین: `https://dashscope.aliyuncs.com/compatible-mode/v1`

راه‌اندازی محیط و daemon

اگر Gateway به‌صورت daemon (`launchd`/`systemd`) اجرا می‌شود، مطمئن شوید `QWEN_API_KEY` برای آن فرایند در دسترس است (برای مثال، در `~/.openclaw/.env` یا از طریق `env.shellEnv`).

## مرتبط

[**انتخاب مدل** انتخاب ارائه‌دهندگان، ارجاع‌های مدل، و رفتار failover. ](</fa/concepts/model-providers>) [**تولید ویدئو** پارامترهای مشترک ابزار ویدئو و انتخاب ارائه‌دهنده. ](</fa/tools/video-generation>) [**Alibaba (ModelStudio)** ارائه‌دهنده قدیمی ModelStudio و یادداشت‌های مهاجرت. ](</fa/providers/alibaba>) [**عیب‌یابی** عیب‌یابی عمومی و پرسش‌های متداول. ](</fa/help/troubleshooting>)

Was this useful?YesNo