---
title: vLLM
source_url: https://docs.openclaw.ai/fa/providers/vllm
scraped_at: 2026-05-25
---

vLLM می‌تواند مدل‌های متن‌باز (و برخی مدل‌های سفارشی) را از طریق یک API HTTP **سازگار با OpenAI** ارائه کند. OpenClaw با استفاده از API‏ `openai-completions` به vLLM متصل می‌شود.

OpenClaw همچنین می‌تواند وقتی با `VLLM_API_KEY` آن را فعال می‌کنید، مدل‌های در دسترس را از vLLM **به‌صورت خودکار کشف کند** (اگر سرور شما احراز هویت را اعمال نمی‌کند، هر مقداری کار می‌کند). وقتی یک URL پایهٔ سفارشی برای vLLM نیز پیکربندی می‌کنید، از `vllm/*` در `agents.defaults.models` استفاده کنید تا کشف مدل پویا بماند.

OpenClaw‏ `vllm` را به‌عنوان یک ارائه‌دهندهٔ محلی سازگار با OpenAI در نظر می‌گیرد که از حسابداری مصرف در جریان پخش پشتیبانی می‌کند، بنابراین شمارش توکن‌های وضعیت/زمینه می‌تواند از پاسخ‌های `stream_options.include_usage` به‌روزرسانی شود.

ویژگی | مقدار  
---|---  
شناسهٔ ارائه‌دهنده | `vllm`  
API | `openai-completions` (سازگار با OpenAI)  
احراز هویت | متغیر محیطی `VLLM_API_KEY`  
URL پایهٔ پیش‌فرض | `http://127.0.0.1:8000/v1`  
  
## شروع کار

* ### شروع vLLM با یک سرور سازگار با OpenAI

URL پایهٔ شما باید نقاط پایانی `/v1` را ارائه کند (مثلاً `/v1/models`، `/v1/chat/completions`). vLLM معمولاً روی این نشانی اجرا می‌شود:

CodeCopy code
[code]
    http://127.0.0.1:8000/v1
[/code]

* ### تنظیم متغیر محیطی کلید API

اگر سرور شما احراز هویت را اعمال نمی‌کند، هر مقداری کار می‌کند:

bashCopy code
[code]
    export VLLM_API_KEY="vllm-local"
[/code]

* ### انتخاب یک مدل

با یکی از شناسه‌های مدل vLLM خود جایگزین کنید:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vllm/your-model-id" },    },  },}
[/code]

* ### بررسی در دسترس بودن مدل

bashCopy code
[code]
    openclaw models list --provider vllm
[/code]

## کشف مدل (ارائه‌دهندهٔ ضمنی)

وقتی `VLLM_API_KEY` تنظیم شده باشد (یا یک نمایهٔ احراز هویت وجود داشته باشد) و شما `models.providers.vllm` را تعریف **نکرده باشید** ، OpenClaw این نشانی را پرس‌وجو می‌کند:

CodeCopy code
[code]
    GET http://127.0.0.1:8000/v1/models
[/code]

و شناسه‌های برگشتی را به ورودی‌های مدل تبدیل می‌کند.

## پیکربندی صریح (مدل‌های دستی)

از پیکربندی صریح استفاده کنید وقتی:

  * vLLM روی میزبان یا درگاه متفاوتی اجرا می‌شود
  * می‌خواهید مقادیر `contextWindow` یا `maxTokens` را ثابت کنید
  * سرور شما به یک کلید API واقعی نیاز دارد (یا می‌خواهید سرآیندها را کنترل کنید)
  * به یک نقطهٔ پایانی بازگشتی، LAN، یا Tailscale قابل اعتماد برای vLLM متصل می‌شوید

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://127.0.0.1:8000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300, // Optional: extend connect/header/body/request timeout for slow local models        models: [          {            id: "your-model-id",            name: "Local vLLM Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

برای پویا نگه داشتن این ارائه‌دهنده بدون فهرست کردن دستی همهٔ مدل‌ها، یک نویسهٔ عام ارائه‌دهنده به فهرست نمایان مدل اضافه کنید:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/*": {},      },    },  },}
[/code]

## پیکربندی پیشرفته

رفتار سبک پراکسی

vLLM به‌عنوان یک پشتانهٔ `/v1` سبک پراکسی و سازگار با OpenAI در نظر گرفته می‌شود، نه یک نقطهٔ پایانی بومی OpenAI. یعنی:

رفتار | اعمال می‌شود؟  
---|---  
شکل‌دهی درخواست بومی OpenAI | خیر  
`service_tier` | ارسال نمی‌شود  
`store` پاسخ‌ها | ارسال نمی‌شود  
راهنماهای کش اعلان | ارسال نمی‌شود  
شکل‌دهی بار دادهٔ سازگار با استدلال OpenAI | اعمال نمی‌شود  
سرآیندهای انتساب پنهان OpenClaw | روی URLهای پایهٔ سفارشی تزریق نمی‌شود  
کنترل‌های تفکر Qwen

برای مدل‌های Qwen که از طریق vLLM ارائه می‌شوند، وقتی سرور انتظار kwargs قالب گفت‌وگوی Qwen را دارد، `params.qwenThinkingFormat: "chat-template"` را روی ورودی مدل تنظیم کنید. OpenClaw‏ `/think off` را به این تبدیل می‌کند:

jsonCopy code
[code]
    {  "chat_template_kwargs": {    "enable_thinking": false,    "preserve_thinking": true  }}
[/code]

سطح‌های تفکر غیر از `off` مقدار `enable_thinking: true` را ارسال می‌کنند. اگر نقطهٔ پایانی شما در عوض انتظار پرچم‌های سطح‌بالای سبک DashScope را دارد، از `params.qwenThinkingFormat: "top-level"` استفاده کنید تا `enable_thinking` در ریشهٔ درخواست ارسال شود. حالت snake-case یعنی `params.qwen_thinking_format` نیز پذیرفته می‌شود.

کنترل‌های تفکر Nemotron 3

vLLM/Nemotron 3 می‌تواند از kwargs قالب گفت‌وگو برای کنترل این‌که استدلال به‌صورت استدلال پنهان یا متن پاسخ نمایان برگردانده شود استفاده کند. وقتی یک نشست OpenClaw از `vllm/nemotron-3-*` با تفکر خاموش استفاده می‌کند، Plugin همراه vLLM این را ارسال می‌کند:

jsonCopy code
[code]
    {  "chat_template_kwargs": {    "enable_thinking": false,    "force_nonempty_content": true  }}
[/code]

برای سفارشی‌سازی این مقادیر، `chat_template_kwargs` را زیر پارامترهای مدل تنظیم کنید. اگر `params.extra_body.chat_template_kwargs` را نیز تنظیم کنید، آن مقدار تقدم نهایی را دارد، چون `extra_body` آخرین بازنویسی بدنهٔ درخواست است.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/nemotron-3-super": {          params: {            chat_template_kwargs: {              enable_thinking: false,              force_nonempty_content: true,            },          },        },      },    },  },}
[/code]

فراخوانی‌های ابزار Qwen به‌صورت متن ظاهر می‌شوند

ابتدا مطمئن شوید vLLM با تجزیه‌گر فراخوانی ابزار و قالب گفت‌وگوی درست برای مدل شروع شده است. برای مثال، مستندات vLLM‏ `hermes` را برای مدل‌های Qwen2.5 و `qwen3_xml` را برای مدل‌های Qwen3-Coder ذکر می‌کند.

نشانه‌ها:

  * Skills یا ابزارها هرگز اجرا نمی‌شوند
  * دستیار JSON/XML خامی مانند `{"name":"read","arguments":...}` چاپ می‌کند
  * وقتی OpenClaw مقدار `tool_choice: "auto"` را ارسال می‌کند، vLLM یک آرایهٔ `tool_calls` خالی برمی‌گرداند


برخی ترکیب‌های Qwen/vLLM فقط زمانی فراخوانی‌های ابزار ساختاریافته برمی‌گردانند که درخواست از `tool_choice: "required"` استفاده کند. برای آن ورودی‌های مدل، فیلد درخواست سازگار با OpenAI را با `params.extra_body` اجباری کنید:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/Qwen-Qwen2.5-Coder-32B-Instruct": {          params: {            extra_body: {              tool_choice: "required",            },          },        },      },    },  },}
[/code]

`Qwen-Qwen2.5-Coder-32B-Instruct` را با شناسهٔ دقیقی که این دستور برمی‌گرداند جایگزین کنید:

bashCopy code
[code]
    openclaw models list --provider vllm
[/code]

می‌توانید همین بازنویسی را از CLI اعمال کنید:

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"vllm/Qwen-Qwen2.5-Coder-32B-Instruct":{"params":{"extra_body":{"tool_choice":"required"}}}}' --strict-json --merge
[/code]

این یک راهکار سازگاری اختیاری است. باعث می‌شود هر نوبت مدل با ابزارها به یک فراخوانی ابزار نیاز داشته باشد، بنابراین فقط برای یک ورودی مدل محلی اختصاصی که این رفتار در آن پذیرفتنی است از آن استفاده کنید. آن را به‌عنوان پیش‌فرض سراسری برای همهٔ مدل‌های vLLM به کار نبرید، و از پراکسی‌ای استفاده نکنید که کورکورانه متن دلخواه دستیار را به فراخوانی‌های ابزار اجرایی تبدیل می‌کند.

URL پایهٔ سفارشی

اگر سرور vLLM شما روی میزبان یا درگاه غیرپیش‌فرض اجرا می‌شود، `baseUrl` را در پیکربندی صریح ارائه‌دهنده تنظیم کنید:

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://192.168.1.50:9000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300,        models: [          {            id: "my-custom-model",            name: "Remote vLLM Model",            reasoning: false,            input: ["text"],            contextWindow: 64000,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

## عیب‌یابی

کندی نخستین پاسخ یا پایان مهلت سرور دوردست

برای مدل‌های محلی بزرگ، میزبان‌های دوردست LAN، یا اتصال‌های Tailscale، یک مهلت درخواست در محدودهٔ ارائه‌دهنده تنظیم کنید:

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://192.168.1.50:8000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300,        models: [{ id: "your-model-id", name: "Local vLLM Model" }],      },    },  },}
[/code]

`timeoutSeconds` فقط برای درخواست‌های HTTP مدل vLLM اعمال می‌شود، از جمله برقراری اتصال، سرآیندهای پاسخ، پخش بدنه، و لغو کلی guarded-fetch. پیش از افزایش `agents.defaults.timeoutSeconds` که کل اجرای عامل را کنترل می‌کند، این گزینه را ترجیح دهید.

سرور قابل دسترسی نیست

بررسی کنید که سرور vLLM در حال اجرا و قابل دسترسی باشد:

bashCopy code
[code]
    curl http://127.0.0.1:8000/v1/models
[/code]

اگر خطای اتصال می‌بینید، میزبان، درگاه، و این‌که vLLM با حالت سرور سازگار با OpenAI شروع شده است را بررسی کنید. برای نقاط پایانی صریح بازگشتی، LAN، یا Tailscale، همچنین `models.providers.vllm.request.allowPrivateNetwork: true` را تنظیم کنید؛ درخواست‌های ارائه‌دهنده به‌طور پیش‌فرض URLهای شبکهٔ خصوصی را مسدود می‌کنند، مگر این‌که ارائه‌دهنده صریحاً قابل اعتماد اعلام شده باشد.

خطاهای احراز هویت در درخواست‌ها

اگر درخواست‌ها با خطاهای احراز هویت شکست می‌خورند، یک `VLLM_API_KEY` واقعی تنظیم کنید که با پیکربندی سرور شما مطابقت داشته باشد، یا ارائه‌دهنده را صریحاً زیر `models.providers.vllm` پیکربندی کنید.

هیچ مدلی کشف نشد

کشف خودکار نیاز دارد `VLLM_API_KEY` تنظیم شده باشد. اگر `models.providers.vllm` را تعریف کرده باشید، OpenClaw فقط از مدل‌های اعلام‌شدهٔ شما استفاده می‌کند، مگر این‌که `agents.defaults.models` شامل `"vllm/*": {}` باشد.

ابزارها به‌صورت متن خام نمایش داده می‌شوند

اگر یک مدل Qwen به‌جای اجرای Skills، نحو ابزار JSON/XML را چاپ می‌کند، راهنمای Qwen در بخش پیکربندی پیشرفتهٔ بالا را بررسی کنید. راه‌حل معمول این است:

  * vLLM را با تجزیه‌گر/قالب درست برای آن مدل شروع کنید
  * شناسهٔ دقیق مدل را با `openclaw models list --provider vllm` تأیید کنید
  * فقط اگر `tool_choice: "auto"` همچنان فراخوانی‌های ابزار خالی یا صرفاً متنی برمی‌گرداند، یک بازنویسی اختصاصی برای هر مدل با `params.extra_body.tool_choice: "required"` اضافه کنید


## مرتبط

[**انتخاب مدل** انتخاب ارائه‌دهندگان، ارجاع‌های مدل، و رفتار جایگزینی هنگام خرابی. ](</fa/concepts/model-providers>) [**OpenAI** ارائه‌دهندهٔ بومی OpenAI و رفتار مسیر سازگار با OpenAI. ](</fa/providers/openai>) [**OAuth و احراز هویت** جزئیات احراز هویت و قواعد استفادهٔ دوباره از اعتبارنامه‌ها. ](</fa/gateway/authentication>) [**عیب‌یابی** مشکلات رایج و روش رفع آن‌ها. ](</fa/help/troubleshooting>)

Was this useful?YesNo