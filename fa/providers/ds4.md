---
title: ds4
source_url: https://docs.openclaw.ai/fa/providers/ds4
scraped_at: 2026-06-29
---

ModelsProviders

[ds4](<https://github.com/antirez/ds4>) مدل DeepSeek V4 Flash را از یک بک‌اند محلی Metal با API سازگار با OpenAI در مسیر `/v1` ارائه می‌کند. OpenClaw از طریق خانوادهٔ عمومی providerهای `openai-completions` به ds4 متصل می‌شود.

ds4 یک provider Plugin همراه OpenClaw نیست. آن را زیر `models.providers.ds4` پیکربندی کنید، سپس `ds4/deepseek-v4-flash` را انتخاب کنید.

  * شناسهٔ provider: `ds4`
  * Plugin: ندارد
  * API: Chat Completions سازگار با OpenAI (`openai-completions`)
  * نشانی پایهٔ پیشنهادی: `http://127.0.0.1:18000/v1`
  * شناسهٔ مدل: `deepseek-v4-flash`
  * فراخوانی ابزارها: از طریق `tools` و `tool_calls` به سبک OpenAI پشتیبانی می‌شود
  * استدلال: `thinking` و `reasoning_effort` به سبک DeepSeek


## نیازمندی‌ها

  * macOS با پشتیبانی Metal.
  * یک checkout فعال از ds4 همراه با `ds4-server` و فایل GGUF مدل DeepSeek V4 Flash.
  * حافظهٔ کافی برای context انتخابی شما. مقدارهای بزرگ‌تر `--ctx` هنگام شروع سرور حافظهٔ KV بیشتری اختصاص می‌دهند.


## شروع سریع

* ### Start ds4-server

`&lt;DS4_DIR&gt;` را با مسیر checkout مربوط به ds4 جایگزین کنید.

bashCopy code
[code]
    &lt;DS4_DIR&gt;/ds4-server \  --model &lt;DS4_DIR&gt;/ds4flash.gguf \  --host 127.0.0.1 \  --port 18000 \  --ctx 32768 \  --tokens 128
[/code]

* ### Verify the OpenAI-compatible endpoint

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

پاسخ باید شامل `deepseek-v4-flash` باشد.

* ### Add the OpenClaw provider config

پیکربندی بخش پیکربندی کامل را اضافه کنید، سپس یک بررسی یک‌بارهٔ مدل اجرا کنید:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

## پیکربندی کامل

وقتی ds4 از قبل روی `127.0.0.1:18000` در حال اجراست، از این پیکربندی استفاده کنید.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "ds4/deepseek-v4-flash" },      models: {        "ds4/deepseek-v4-flash": {          alias: "DS4 local",        },      },    },  },  models: {    mode: "merge",    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

`contextWindow` را با مقدار `ds4-server --ctx` هماهنگ نگه دارید. `maxTokens` را با `--tokens` هماهنگ نگه دارید، مگر اینکه عمداً بخواهید OpenClaw خروجی کمتری از پیش‌فرض سرور درخواست کند.

## راه‌اندازی در صورت نیاز

OpenClaw می‌تواند ds4 را فقط زمانی راه‌اندازی کند که یک مدل `ds4/...` انتخاب شده باشد. `localService` را به همان ورودی provider اضافه کنید:

json5Copy code
[code]
    {  models: {    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "&lt;DS4_DIR&gt;/ds4-server",          args: [            "--model",            "&lt;DS4_DIR&gt;/ds4flash.gguf",            "--host",            "127.0.0.1",            "--port",            "18000",            "--ctx",            "32768",            "--tokens",            "128",          ],          cwd: "&lt;DS4_DIR&gt;",          healthUrl: "http://127.0.0.1:18000/v1/models",          readyTimeoutMs: 300000,          idleStopMs: 0,        },        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

`command` باید یک مسیر اجرایی مطلق باشد. جست‌وجوی shell و گسترش `~` استفاده نمی‌شوند. برای همهٔ فیلدهای `localService`، [سرویس‌های مدل محلی](</fa/gateway/local-model-services>) را ببینید.

## Think Max

ds4 فقط زمانی Think Max را اعمال می‌کند که هر دو شرط برقرار باشند:

  * `ds4-server` با `--ctx 393216` یا بالاتر شروع شود.
  * درخواست از `reasoning_effort: "max"` یا فیلد effort معادل در ds4 استفاده کند.


اگر آن context بزرگ را اجرا می‌کنید، هم پرچم‌های سرور و هم فرادادهٔ مدل OpenClaw را به‌روزرسانی کنید:

json5Copy code
[code]
    {  contextWindow: 393216,  maxTokens: 384000,  compat: {    supportsUsageInStreaming: true,    supportsReasoningEffort: true,    maxTokensField: "max_tokens",    supportsStrictMode: false,    thinkingFormat: "deepseek",    supportedReasoningEfforts: ["low", "medium", "high", "xhigh", "max"],  },}
[/code]

## آزمون

با یک بررسی مستقیم HTTP شروع کنید:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"Reply with exactly: ds4-ok"}],"max_tokens":16,"stream":false,"thinking":{"type":"disabled"}}'
[/code]

سپس مسیریابی مدل OpenClaw را آزمون کنید:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

برای یک smoke کامل مربوط به agent و فراخوانی ابزار، از context دست‌کم 32768 استفاده کنید:

bashCopy code
[code]
    openclaw agent \  --local \  --session-id ds4-tool-smoke \  --model ds4/deepseek-v4-flash \  --thinking off \  --message "Use the shell command pwd once, then reply exactly: tool-ok <output>" \  --json \  --timeout 240
[/code]

نتیجهٔ مورد انتظار:

  * `executionTrace.winnerProvider` برابر `ds4` است
  * `executionTrace.winnerModel` برابر `deepseek-v4-flash` است
  * `toolSummary.calls` دست‌کم `1` است
  * `finalAssistantVisibleText` با `tool-ok` شروع می‌شود


## عیب‌یابی

curl /v1/models cannot connect

ds4 اجرا نشده یا به host و port موجود در `baseUrl` متصل نشده است. `ds4-server` را شروع کنید، سپس دوباره تلاش کنید:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

500 prompt exceeds context

مقدار پیکربندی‌شدهٔ `--ctx` برای نوبت OpenClaw بیش از حد کوچک است. `ds4-server --ctx` را افزایش دهید، سپس `models.providers.ds4.models[].contextWindow` را برای تطابق به‌روزرسانی کنید. نوبت‌های کامل agent همراه با ابزارها به context بسیار بیشتری نسبت به یک درخواست مستقیم curl تک‌پیامی نیاز دارند.

Think Max does not activate

ds4 فقط زمانی از Think Max استفاده می‌کند که `--ctx` دست‌کم `393216` باشد و درخواست `reasoning_effort: "max"` را بخواهد. contextهای کوچک‌تر به استدلال high برمی‌گردند.

The first request is slow

ds4 یک مرحلهٔ cold residency در Metal و گرم‌سازی مدل دارد. وقتی OpenClaw سرور را در صورت نیاز شروع می‌کند، از `localService.readyTimeoutMs: 300000` استفاده کنید.

## مرتبط

[**Local model services** سرورهای مدل محلی را پیش از درخواست‌های مدل، در صورت نیاز شروع کنید. ](</fa/gateway/local-model-services>) [**Local models** بک‌اندهای مدل محلی را انتخاب و اجرا کنید. ](</fa/gateway/local-models>) [**Model providers** ارجاع‌های provider، احراز هویت، و failover را پیکربندی کنید. ](</fa/concepts/model-providers>) [**DeepSeek** رفتار provider بومی DeepSeek و کنترل‌های thinking. ](</fa/providers/deepseek>)

Was this useful?YesNo

Open issue