---
title: Z.AI
source_url: https://docs.openclaw.ai/fa/providers/zai
scraped_at: 2026-05-25
---

[Z.AI](<http://Z.AI>) پلتفرم API برای مدل‌های **GLM** است. این پلتفرم APIهای REST را برای GLM فراهم می‌کند و برای احراز هویت از کلیدهای API استفاده می‌کند. کلید API خود را در کنسول [Z.AI](<http://Z.AI>) بسازید. OpenClaw از ارائه‌دهنده‌ی `zai` با یک کلید API مربوط به [Z.AI](<http://Z.AI>) استفاده می‌کند.

  * ارائه‌دهنده: `zai`
  * احراز هویت: `ZAI_API_KEY`
  * API: تکمیل‌های گفت‌وگوی [Z.AI](<http://Z.AI>) (احراز هویت Bearer)


## شروع به کار

### Auto-detect endpoint

**بهترین گزینه برای:** بیشتر کاربران. OpenClaw نقطه پایانی منطبق [Z.AI](<http://Z.AI>) را از روی کلید تشخیص می‌دهد و URL پایه‌ی درست را به‌صورت خودکار اعمال می‌کند.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice zai-api-key
[/code]

* ### Set a default model

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Verify the model is listed

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

### Explicit regional endpoint

**بهترین گزینه برای:** کاربرانی که می‌خواهند یک Coding Plan مشخص یا سطح عمومی API را اجباری کنند.

* ### Pick the right onboarding choice

bashCopy code
[code]
    # Coding Plan Global (recommended for Coding Plan users)openclaw onboard --auth-choice zai-coding-global # Coding Plan CN (China region)openclaw onboard --auth-choice zai-coding-cn # General APIopenclaw onboard --auth-choice zai-global # General API CN (China region)openclaw onboard --auth-choice zai-cn
[/code]

* ### Set a default model

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Verify the model is listed

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

## کاتالوگ داخلی

OpenClaw کاتالوگ ارائه‌دهنده‌ی همراه `zai` را در مانیفست Plugin ارائه می‌کند، بنابراین فهرست‌گیری فقط‌خواندنی می‌تواند ردیف‌های شناخته‌شده‌ی GLM را بدون بارگذاری runtime ارائه‌دهنده نشان دهد:

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

کاتالوگ مبتنی بر مانیفست در حال حاضر شامل این موارد است:

ارجاع مدل | یادداشت‌ها  
---|---  
`zai/glm-5.1` | مدل پیش‌فرض  
`zai/glm-5` |   
`zai/glm-5-turbo` |   
`zai/glm-5v-turbo` |   
`zai/glm-4.7` |   
`zai/glm-4.7-flash` |   
`zai/glm-4.7-flashx` |   
`zai/glm-4.6` |   
`zai/glm-4.6v` |   
`zai/glm-4.5` |   
`zai/glm-4.5-air` |   
`zai/glm-4.5-flash` |   
`zai/glm-4.5v` |   
  
## پیکربندی پیشرفته

Forward-resolving unknown GLM-5 models

شناسه‌های ناشناخته‌ی `glm-5*` همچنان در مسیر ارائه‌دهنده‌ی همراه، با ساخت فراداده‌ی متعلق به ارائه‌دهنده از الگوی `glm-4.7`، forward-resolve می‌شوند؛ البته زمانی که شناسه با شکل فعلی خانواده‌ی GLM-5 منطبق باشد.

Tool-call streaming

`tool_stream` به‌صورت پیش‌فرض برای پخش جریانی فراخوانی ابزار در [Z.AI](<http://Z.AI>) فعال است. برای غیرفعال‌کردن آن:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/<model>": {          params: { tool_stream: false },        },      },    },  },}
[/code]

Thinking and preserved thinking

تفکر [Z.AI](<http://Z.AI>) از کنترل‌های `/think` در OpenClaw پیروی می‌کند. وقتی تفکر خاموش باشد، OpenClaw مقدار `thinking: { type: "disabled" }` را ارسال می‌کند تا از پاسخ‌هایی جلوگیری کند که پیش از متن قابل مشاهده، بودجه‌ی خروجی را صرف `reasoning_content` می‌کنند.

تفکر حفظ‌شده اختیاری است، چون [Z.AI](<http://Z.AI>) نیاز دارد کل `reasoning_content` تاریخی دوباره پخش شود، که توکن‌های پرامپت را افزایش می‌دهد. آن را برای هر مدل فعال کنید:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/glm-5.1": {          params: { preserveThinking: true },        },      },    },  },}
[/code]

وقتی فعال باشد و تفکر روشن باشد، OpenClaw مقدار `thinking: { type: "enabled", clear_thinking: false }` را ارسال می‌کند و `reasoning_content` قبلی را برای همان متن گفت‌وگوی سازگار با OpenAI دوباره پخش می‌کند.

کاربران پیشرفته همچنان می‌توانند payload دقیق ارائه‌دهنده را با `params.extra_body.thinking` بازنویسی کنند.

Image understanding

Plugin همراه [Z.AI](<http://Z.AI>) فهم تصویر را ثبت می‌کند.

ویژگی | مقدار  
---|---  
مدل | `glm-4.6v`  
  
فهم تصویر به‌صورت خودکار از احراز هویت پیکربندی‌شده‌ی [Z.AI](<http://Z.AI>) resolve می‌شود؛ هیچ پیکربندی اضافه‌ای لازم نیست.

Auth details

  * [Z.AI](<http://Z.AI>) از احراز هویت Bearer با کلید API شما استفاده می‌کند.
  * گزینه‌ی onboarding با نام `zai-api-key` نقطه پایانی منطبق [Z.AI](<http://Z.AI>) را از روی پیشوند کلید به‌صورت خودکار تشخیص می‌دهد.
  * وقتی می‌خواهید یک سطح API مشخص را اجباری کنید، از گزینه‌های منطقه‌ای صریح (`zai-coding-global`، `zai-coding-cn`، `zai-global`، `zai-cn`) استفاده کنید.


## مرتبط

[**GLM model family** نمای کلی خانواده‌ی مدل‌های GLM. ](</fa/providers/glm>) [**Model selection** انتخاب ارائه‌دهندگان، ارجاع‌های مدل، و رفتار failover. ](</fa/concepts/model-providers>)

Was this useful?YesNo