---
title: LiteLLM
source_url: https://docs.openclaw.ai/fa/providers/litellm
scraped_at: 2026-05-25
---

[LiteLLM](<https://litellm.ai>) یک Gateway متن‌باز برای LLM است که یک API یکپارچه برای بیش از ۱۰۰ ارائه‌دهندهٔ مدل فراهم می‌کند. OpenClaw را از طریق LiteLLM مسیریابی کنید تا ردیابی هزینهٔ متمرکز، ثبت گزارش، و انعطاف‌پذیری برای جابه‌جایی backendها بدون تغییر config OpenClaw را داشته باشید.

## شروع سریع

### Onboarding (recommended)

**بهترین برای:** سریع‌ترین مسیر برای راه‌اندازی عملی LiteLLM.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice litellm-api-key
[/code]

برای راه‌اندازی غیرتعاملی در برابر یک proxy راه‌دور، URL مربوط به proxy را صریحاً پاس دهید:

bashCopy code
[code]
    openclaw onboard --non-interactive --auth-choice litellm-api-key --litellm-api-key "$LITELLM_API_KEY" --custom-base-url "https://litellm.example/v1"
[/code]

### Manual setup

**بهترین برای:** کنترل کامل روی نصب و config.

* ### Start LiteLLM Proxy

bashCopy code
[code]
    pip install 'litellm[proxy]'litellm --model claude-opus-4-6
[/code]

* ### Point OpenClaw to LiteLLM

bashCopy code
[code]
    export LITELLM_API_KEY="your-litellm-key" openclaw
[/code]

همین است. OpenClaw اکنون از طریق LiteLLM مسیریابی می‌شود.

## پیکربندی

### متغیرهای محیطی

bashCopy code
[code]
    export LITELLM_API_KEY="sk-litellm-key"
[/code]

### فایل config

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",        api: "openai-completions",        models: [          {            id: "claude-opus-4-6",            name: "Claude Opus 4.6",            reasoning: true,            input: ["text", "image"],            contextWindow: 200000,            maxTokens: 64000,          },          {            id: "gpt-4o",            name: "GPT-4o",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "litellm/claude-opus-4-6" },    },  },}
[/code]

## پیکربندی پیشرفته

### تولید تصویر

LiteLLM می‌تواند از ابزار `image_generate` نیز از طریق مسیرهای سازگار با OpenAI یعنی `/images/generations` و `/images/edits` پشتیبانی کند. یک مدل تصویر LiteLLM را زیر `agents.defaults.imageGenerationModel` پیکربندی کنید:

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",      },    },  },  agents: {    defaults: {      imageGenerationModel: {        primary: "litellm/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

URLهای LiteLLM از نوع loopback مانند `http://localhost:4000` بدون override سراسری شبکهٔ خصوصی کار می‌کنند. برای proxy میزبانی‌شده روی LAN، `models.providers.litellm.request.allowPrivateNetwork: true` را تنظیم کنید، چون API key به میزبان proxy پیکربندی‌شده ارسال خواهد شد.

Virtual keys

برای OpenClaw یک کلید اختصاصی با سقف هزینه بسازید:

bashCopy code
[code]
    curl -X POST "http://localhost:4000/key/generate" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \  -H "Content-Type: application/json" \  -d '{    "key_alias": "openclaw",    "max_budget": 50.00,    "budget_duration": "monthly"  }'
[/code]

از کلید تولیدشده به‌عنوان `LITELLM_API_KEY` استفاده کنید.

Model routing

LiteLLM می‌تواند درخواست‌های مدل را به backendهای مختلف مسیریابی کند. در `config.yaml` مربوط به LiteLLM پیکربندی کنید:

yamlCopy code
[code]
    model_list:  - model_name: claude-opus-4-6    litellm_params:      model: claude-opus-4-6      api_key: os.environ/ANTHROPIC_API_KEY   - model_name: gpt-4o    litellm_params:      model: gpt-4o      api_key: os.environ/OPENAI_API_KEY
[/code]

OpenClaw همچنان `claude-opus-4-6` را درخواست می‌کند — LiteLLM مسیریابی را انجام می‌دهد.

Viewing usage

داشبورد یا API مربوط به LiteLLM را بررسی کنید:

bashCopy code
[code]
    # Key infocurl "http://localhost:4000/key/info" \  -H "Authorization: Bearer sk-litellm-key" # Spend logscurl "http://localhost:4000/spend/logs" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY"
[/code]

Proxy behavior notes

  * LiteLLM به‌طور پیش‌فرض روی `http://localhost:4000` اجرا می‌شود
  * OpenClaw از طریق endpoint سازگار با OpenAI و proxy-style مربوط به LiteLLM یعنی `/v1` وصل می‌شود
  * شکل‌دهی درخواست مخصوص OpenAI بومی از طریق LiteLLM اعمال نمی‌شود: نه `service_tier`، نه Responses `store`، نه راهنمایی‌های prompt-cache، و نه شکل‌دهی payload سازگاری reasoning مربوط به OpenAI
  * هدرهای attribution پنهان OpenClaw (`originator`، `version`، `User-Agent`) روی URLهای پایهٔ سفارشی LiteLLM تزریق نمی‌شوند


## مرتبط

[**LiteLLM Docs** مستندات رسمی LiteLLM و مرجع API. ](<https://docs.litellm.ai>) [**Model selection** نمای کلی همهٔ ارائه‌دهندگان، ارجاع‌های مدل، و رفتار failover. ](</fa/concepts/model-providers>) [**Configuration** مرجع کامل config. ](</fa/gateway/configuration>) [**Model selection** نحوهٔ انتخاب و پیکربندی مدل‌ها. ](</fa/concepts/models>)

Was this useful?YesNo