---
title: LM Studio
source_url: https://docs.openclaw.ai/fa/providers/lmstudio
scraped_at: 2026-05-25
---

LM Studio برنامه‌ای دوستانه اما قدرتمند برای اجرای مدل‌های open-weight روی سخت‌افزار خودتان است. این برنامه به شما امکان می‌دهد مدل‌های llama.cpp (GGUF) یا MLX (Apple Silicon) را اجرا کنید. به‌صورت بسته GUI یا daemon بدون رابط (`llmster`) ارائه می‌شود. برای مستندات محصول و راه‌اندازی، [lmstudio.ai](<https://lmstudio.ai/>) را ببینید.

## شروع سریع

  1. LM Studio (دسکتاپ) یا `llmster` (بدون رابط) را نصب کنید، سپس سرور محلی را شروع کنید:

bashCopy code
[code]
    curl -fsSL https://lmstudio.ai/install.sh | bash
[/code]

  2. سرور را شروع کنید


مطمئن شوید که یا برنامه دسکتاپ را شروع کرده‌اید یا daemon را با دستور زیر اجرا می‌کنید:

bashCopy code
[code]
    lms daemon up
[/code]

bashCopy code
[code]
    lms server start --port 1234
[/code]

اگر از برنامه استفاده می‌کنید، مطمئن شوید JIT برای تجربه‌ای روان فعال است. در [راهنمای JIT و TTL در LM Studio](<https://lmstudio.ai/docs/developer/core/ttl-and-auto-evict>) بیشتر بدانید.

  3. اگر احراز هویت LM Studio فعال است، `LM_API_TOKEN` را تنظیم کنید:

bashCopy code
[code]
    export LM_API_TOKEN="your-lm-studio-api-token"
[/code]

اگر احراز هویت LM Studio غیرفعال است، می‌توانید کلید API را هنگام راه‌اندازی تعاملی OpenClaw خالی بگذارید.

برای جزئیات راه‌اندازی احراز هویت LM Studio، [احراز هویت LM Studio](<https://lmstudio.ai/docs/developer/core/authentication>) را ببینید.

  4. onboarding را اجرا کنید و `LM Studio` را انتخاب کنید:

bashCopy code
[code]
    openclaw onboard
[/code]

  5. در onboarding، از درخواست `Default model` برای انتخاب مدل LM Studio خود استفاده کنید.


همچنین می‌توانید آن را بعداً تنظیم یا تغییر دهید:

bashCopy code
[code]
    openclaw models set lmstudio/qwen/qwen3.5-9b
[/code]

کلیدهای مدل LM Studio از قالب `author/model-name` پیروی می‌کنند (مثلاً `qwen/qwen3.5-9b`). ارجاع‌های مدل OpenClaw نام provider را در ابتدا اضافه می‌کنند: `lmstudio/qwen/qwen3.5-9b`. می‌توانید کلید دقیق یک مدل را با اجرای `curl http://localhost:1234/api/v1/models` و نگاه کردن به فیلد `key` پیدا کنید.

## Onboarding غیرتعاملی

وقتی می‌خواهید راه‌اندازی را اسکریپت کنید (CI، provisioning، bootstrap راه دور)، از onboarding غیرتعاملی استفاده کنید:

bashCopy code
[code]
    openclaw onboard \  --non-interactive \  --accept-risk \  --auth-choice lmstudio
[/code]

یا URL پایه، مدل، و کلید API اختیاری را مشخص کنید:

bashCopy code
[code]
    openclaw onboard \  --non-interactive \  --accept-risk \  --auth-choice lmstudio \  --custom-base-url http://localhost:1234/v1 \  --lmstudio-api-key "$LM_API_TOKEN" \  --custom-model-id qwen/qwen3.5-9b
[/code]

`--custom-model-id` کلید مدل را همان‌طور که LM Studio برمی‌گرداند دریافت می‌کند (مثلاً `qwen/qwen3.5-9b`)، بدون پیشوند provider یعنی `lmstudio/`.

برای سرورهای LM Studio دارای احراز هویت، `--lmstudio-api-key` را پاس دهید یا `LM_API_TOKEN` را تنظیم کنید. برای سرورهای LM Studio بدون احراز هویت، کلید را حذف کنید؛ OpenClaw یک نشانگر محلی غیرمحرمانه ذخیره می‌کند.

`--custom-api-key` همچنان برای سازگاری پشتیبانی می‌شود، اما `--lmstudio-api-key` برای LM Studio ترجیح داده می‌شود.

این کار `models.providers.lmstudio` را می‌نویسد و مدل پیش‌فرض را روی `lmstudio/<custom-model-id>` تنظیم می‌کند. وقتی کلید API ارائه می‌کنید، راه‌اندازی همچنین پروفایل احراز هویت `lmstudio:default` را می‌نویسد.

راه‌اندازی تعاملی می‌تواند برای طول زمینه بارگذاری ترجیحی اختیاری درخواست دهد و آن را روی مدل‌های LM Studio کشف‌شده‌ای که در پیکربندی ذخیره می‌کند اعمال می‌کند. پیکربندی Plugin در LM Studio به endpoint پیکربندی‌شده LM Studio برای درخواست‌های مدل اعتماد می‌کند، از جمله loopback، LAN، و میزبان‌های tailnet. می‌توانید با تنظیم `models.providers.lmstudio.request.allowPrivateNetwork: false` از این رفتار خارج شوید.

## پیکربندی

### سازگاری مصرف در streaming

LM Studio با مصرف در streaming سازگار است. وقتی یک شیء `usage` با ساختار OpenAI منتشر نمی‌کند، OpenClaw به‌جای آن شمارش tokenها را از metadata به سبک llama.cpp یعنی `timings.prompt_n` / `timings.predicted_n` بازیابی می‌کند.

همین رفتار مصرف در streaming برای این backendهای محلی سازگار با OpenAI اعمال می‌شود:

  * vLLM
  * SGLang
  * llama.cpp
  * LocalAI
  * Jan
  * TabbyAPI
  * text-generation-webui


### سازگاری Thinking

وقتی کشف `/api/v1/models` در LM Studio گزینه‌های reasoning مختص مدل را گزارش می‌کند، OpenClaw مقادیر سازگار با OpenAI و متناظر `reasoning_effort` را در metadata سازگاری مدل نمایان می‌کند. buildهای فعلی LM Studio می‌توانند گزینه‌های دودویی UI مانند `allowed_options: ["off", "on"]` را اعلام کنند، در حالی که همان مقادیر را در `/v1/chat/completions` رد می‌کنند؛ OpenClaw این شکل کشف دودویی را پیش از ارسال درخواست‌ها به `none`، `minimal`، `low`، `medium`، `high`، و `xhigh` نرمال‌سازی می‌کند. پیکربندی ذخیره‌شده قدیمی‌تر LM Studio که شامل نگاشت‌های reasoning با `off`/`on` است نیز هنگام بارگذاری catalog به همین روش نرمال‌سازی می‌شود.

### پیکربندی صریح

json5Copy code
[code]
    {  models: {    providers: {      lmstudio: {        baseUrl: "http://localhost:1234/v1",        apiKey: "${LM_API_TOKEN}",        api: "openai-completions",        models: [          {            id: "qwen/qwen3-coder-next",            name: "Qwen 3 Coder Next",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## عیب‌یابی

### LM Studio شناسایی نشد

مطمئن شوید LM Studio در حال اجرا است. اگر احراز هویت فعال است، `LM_API_TOKEN` را نیز تنظیم کنید:

bashCopy code
[code]
    # Start via desktop app, or headless:lms server start --port 1234
[/code]

دسترسی‌پذیر بودن API را بررسی کنید:

bashCopy code
[code]
    curl http://localhost:1234/api/v1/models
[/code]

### خطاهای احراز هویت (HTTP 401)

اگر راه‌اندازی HTTP 401 گزارش می‌کند، کلید API خود را بررسی کنید:

  * بررسی کنید که `LM_API_TOKEN` با کلید پیکربندی‌شده در LM Studio مطابقت داشته باشد.
  * برای جزئیات راه‌اندازی احراز هویت LM Studio، [احراز هویت LM Studio](<https://lmstudio.ai/docs/developer/core/authentication>) را ببینید.
  * اگر سرور شما به احراز هویت نیاز ندارد، هنگام راه‌اندازی کلید را خالی بگذارید.


### بارگذاری just-in-time مدل

LM Studio از بارگذاری just-in-time (JIT) مدل پشتیبانی می‌کند، که در آن مدل‌ها هنگام نخستین درخواست بارگذاری می‌شوند. OpenClaw به‌طور پیش‌فرض مدل‌ها را از طریق endpoint بارگذاری بومی LM Studio از پیش بارگذاری می‌کند، که وقتی JIT غیرفعال است کمک می‌کند. برای اینکه JIT، idle TTL، و رفتار auto-evict در LM Studio مالک چرخه عمر مدل باشند، مرحله preload در OpenClaw را غیرفعال کنید:

json5Copy code
[code]
    {  models: {    providers: {      lmstudio: {        baseUrl: "http://localhost:1234/v1",        api: "openai-completions",        params: { preload: false },        models: [{ id: "qwen/qwen3.5-9b" }],      },    },  },}
[/code]

### میزبان LM Studio روی LAN یا tailnet

از نشانی قابل دسترس میزبان LM Studio استفاده کنید، `/v1` را نگه دارید، و مطمئن شوید LM Studio روی آن دستگاه فراتر از loopback bind شده است:

json5Copy code
[code]
    {  models: {    providers: {      lmstudio: {        baseUrl: "http://gpu-box.local:1234/v1",        apiKey: "lmstudio",        api: "openai-completions",        models: [{ id: "qwen/qwen3.5-9b" }],      },    },  },}
[/code]

برخلاف providerهای عمومی سازگار با OpenAI، `lmstudio` به‌طور خودکار به endpoint محلی/خصوصی پیکربندی‌شده خود برای درخواست‌های محافظت‌شده مدل اعتماد می‌کند. شناسه‌های provider سفارشی loopback مانند `localhost` یا `127.0.0.1` نیز به‌طور خودکار مورد اعتماد هستند؛ برای شناسه‌های provider سفارشی LAN، tailnet، یا DNS خصوصی، `models.providers.<id>.request.allowPrivateNetwork: true` را به‌صراحت تنظیم کنید.

## مرتبط

  * [انتخاب مدل](</fa/concepts/model-providers>)
  * [Ollama](</fa/providers/ollama>)
  * [مدل‌های محلی](</fa/gateway/local-models>)


Was this useful?YesNo