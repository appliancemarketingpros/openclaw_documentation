---
title: Volcengine (Doubao)
source_url: https://docs.openclaw.ai/fa/providers/volcengine
scraped_at: 2026-05-25
---

ارائه‌دهنده Volcengine دسترسی به مدل‌های Doubao و مدل‌های شخص ثالث میزبانی‌شده روی Volcano Engine را، با نقاط پایانی جداگانه برای بارهای کاری عمومی و کدنویسی، فراهم می‌کند. همین Plugin همراه می‌تواند Volcengine Speech را نیز به‌عنوان یک ارائه‌دهنده TTS ثبت کند.

جزئیات | مقدار  
---|---  
ارائه‌دهندگان | `volcengine` (عمومی + TTS) + `volcengine-plan` (کدنویسی)  
احراز هویت مدل | `VOLCANO_ENGINE_API_KEY`  
احراز هویت TTS | `VOLCENGINE_TTS_API_KEY` یا `BYTEPLUS_SEED_SPEECH_API_KEY`  
API | مدل‌های سازگار با OpenAI، BytePlus Seed Speech TTS  
  
## شروع به کار

* ### تنظیم کلید API

راه‌اندازی تعاملی را اجرا کنید:

bashCopy code
[code]
    openclaw onboard --auth-choice volcengine-api-key
[/code]

این کار هر دو ارائه‌دهنده عمومی (`volcengine`) و کدنویسی (`volcengine-plan`) را از یک کلید API واحد ثبت می‌کند.

* ### تنظیم یک مدل پیش‌فرض

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "volcengine-plan/ark-code-latest" },    },  },}
[/code]

* ### بررسی در دسترس بودن مدل

bashCopy code
[code]
    openclaw models list --provider volcengineopenclaw models list --provider volcengine-plan
[/code]

## ارائه‌دهندگان و نقاط پایانی

ارائه‌دهنده | نقطه پایانی | مورد استفاده  
---|---|---  
`volcengine` | `ark.cn-beijing.volces.com/api/v3` | مدل‌های عمومی  
`volcengine-plan` | `ark.cn-beijing.volces.com/api/coding/v3` | مدل‌های کدنویسی  
  
## کاتالوگ داخلی

### عمومی (volcengine)

ارجاع مدل | نام | ورودی | زمینه  
---|---|---|---  
`volcengine/doubao-seed-1-8-251228` | Doubao Seed 1.8 | متن، تصویر | 256,000  
`volcengine/doubao-seed-code-preview-251028` | doubao-seed-code-preview-251028 | متن، تصویر | 256,000  
`volcengine/kimi-k2-5-260127` | Kimi K2.5 | متن، تصویر | 256,000  
`volcengine/glm-4-7-251222` | GLM 4.7 | متن، تصویر | 200,000  
`volcengine/deepseek-v3-2-251201` | DeepSeek V3.2 | متن، تصویر | 128,000  
  
### کدنویسی (volcengine-plan)

ارجاع مدل | نام | ورودی | زمینه  
---|---|---|---  
`volcengine-plan/ark-code-latest` | Ark Coding Plan | متن | 256,000  
`volcengine-plan/doubao-seed-code` | Doubao Seed Code | متن | 256,000  
`volcengine-plan/glm-4.7` | GLM 4.7 Coding | متن | 200,000  
`volcengine-plan/kimi-k2-thinking` | Kimi K2 Thinking | متن | 256,000  
`volcengine-plan/kimi-k2.5` | Kimi K2.5 Coding | متن | 256,000  
`volcengine-plan/doubao-seed-code-preview-251028` | Doubao Seed Code Preview | متن | 256,000  
  
## تبدیل متن به گفتار

Volcengine TTS از BytePlus Seed Speech HTTP API استفاده می‌کند و جدا از کلید API مدل Doubao سازگار با OpenAI پیکربندی می‌شود. در کنسول BytePlus، Seed Speech > Settings > API Keys را باز کنید و کلید API را کپی کنید، سپس تنظیم کنید:

bashCopy code
[code]
    export VOLCENGINE_TTS_API_KEY="byteplus_seed_speech_api_key"export VOLCENGINE_TTS_RESOURCE_ID="seed-tts-1.0"
[/code]

سپس آن را در `openclaw.json` فعال کنید:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "volcengine",      providers: {        volcengine: {          apiKey: "byteplus_seed_speech_api_key",          voice: "en_female_anna_mars_bigtts",          speedRatio: 1.0,        },      },    },  },}
[/code]

برای مقصدهای یادداشت صوتی، OpenClaw از Volcengine فرمت بومی ارائه‌دهنده `ogg_opus` را درخواست می‌کند. برای پیوست‌های صوتی عادی، `mp3` را درخواست می‌کند. نام‌های مستعار ارائه‌دهنده `bytedance` و `doubao` نیز به همان ارائه‌دهنده گفتار ارجاع می‌شوند.

شناسه منبع پیش‌فرض `seed-tts-1.0` است، چون BytePlus همین مورد را به کلیدهای API تازه‌ساخته Seed Speech در پروژه پیش‌فرض اعطا می‌کند. اگر پروژه شما مجوز TTS 2.0 دارد، `VOLCENGINE_TTS_RESOURCE_ID=seed-tts-2.0` را تنظیم کنید.

احراز هویت AppID/token قدیمی همچنان برای برنامه‌های قدیمی‌تر Speech Console پشتیبانی می‌شود:

bashCopy code
[code]
    export VOLCENGINE_TTS_APPID="speech_app_id"export VOLCENGINE_TTS_TOKEN="speech_access_token"export VOLCENGINE_TTS_CLUSTER="volcano_tts"
[/code]

## پیکربندی پیشرفته

مدل پیش‌فرض پس از راه‌اندازی

`openclaw onboard --auth-choice volcengine-api-key` در حال حاضر `volcengine-plan/ark-code-latest` را به‌عنوان مدل پیش‌فرض تنظیم می‌کند و هم‌زمان کاتالوگ عمومی `volcengine` را نیز ثبت می‌کند.

رفتار جایگزین انتخابگر مدل

هنگام انتخاب مدل در راه‌اندازی/پیکربندی، گزینه احراز هویت Volcengine ردیف‌های `volcengine/*` و `volcengine-plan/*` را ترجیح می‌دهد. اگر آن مدل‌ها هنوز بارگذاری نشده باشند، OpenClaw به‌جای نمایش یک انتخابگر خالی محدودشده به ارائه‌دهنده، به کاتالوگ فیلترنشده برمی‌گردد.

متغیرهای محیطی برای فرایندهای daemon

اگر Gateway به‌صورت daemon اجرا می‌شود (launchd/systemd)، مطمئن شوید متغیرهای محیطی مدل و TTS مانند `VOLCANO_ENGINE_API_KEY`، `VOLCENGINE_TTS_API_KEY`، `BYTEPLUS_SEED_SPEECH_API_KEY`، `VOLCENGINE_TTS_APPID` و `VOLCENGINE_TTS_TOKEN` برای آن فرایند در دسترس هستند (برای مثال، در `~/.openclaw/.env` یا از طریق `env.shellEnv`).

## مرتبط

[**انتخاب مدل** انتخاب ارائه‌دهندگان، ارجاع‌های مدل و رفتار failover. ](</fa/concepts/model-providers>) [**پیکربندی** مرجع کامل پیکربندی برای عامل‌ها، مدل‌ها و ارائه‌دهندگان. ](</fa/gateway/configuration>) [**عیب‌یابی** مشکلات رایج و مراحل اشکال‌زدایی. ](</fa/help/troubleshooting>) [**پرسش‌های متداول** پرسش‌های متداول درباره راه‌اندازی OpenClaw. ](</fa/help/faq>)

Was this useful?YesNo