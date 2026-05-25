---
title: CLI استنتاج
source_url: https://docs.openclaw.ai/fa/cli/infer
scraped_at: 2026-05-25
---

`openclaw infer` سطح headless متعارف برای جریان‌های کاری استنتاجِ متکی به provider است.

این دستور عمداً خانواده‌های capability را نمایش می‌دهد، نه نام‌های خام RPC مربوط به gateway و نه شناسه‌های خام ابزار agent.

## تبدیل infer به یک skill

این متن را در یک agent کپی و جای‌گذاری کنید:

textCopy code
[code]
    Read https://docs.openclaw.ai/cli/infer, then create a skill that routes my common workflows to `openclaw infer`.Focus on model runs, image generation, video generation, audio transcription, TTS, web search, and embeddings.
[/code]

یک skill خوب مبتنی بر infer باید:

  * نیت‌های رایج کاربر را به زیر‌دستور درست infer نگاشت کند
  * چند نمونه متعارف infer برای جریان‌های کاری‌ای که پوشش می‌دهد شامل شود
  * در نمونه‌ها و پیشنهادها `openclaw infer ...` را ترجیح دهد
  * از مستندسازی دوباره کل سطح infer در بدنه skill خودداری کند


پوشش معمول skill متمرکز بر infer:

  * `openclaw infer model run`
  * `openclaw infer image generate`
  * `openclaw infer audio transcribe`
  * `openclaw infer tts convert`
  * `openclaw infer web search`
  * `openclaw infer embedding create`


## چرا از infer استفاده کنیم

`openclaw infer` یک CLI یکپارچه برای وظایف استنتاجِ متکی به provider در OpenClaw فراهم می‌کند.

مزایا:

  * به‌جای اتصال wrapperهای موردی برای هر backend، از providerها و مدل‌هایی استفاده کنید که از قبل در OpenClaw پیکربندی شده‌اند.
  * جریان‌های کاری مدل، تصویر، رونویسی صوت، TTS، ویدئو، وب و embedding را زیر یک درخت دستور نگه دارید.
  * برای اسکریپت‌ها، خودکارسازی و جریان‌های کاری agentمحور از شکل خروجی پایدار `--json` استفاده کنید.
  * وقتی وظیفه اساساً «اجرای استنتاج» است، یک سطح رسمی OpenClaw را ترجیح دهید.
  * برای بیشتر دستورهای infer از مسیر محلی معمول استفاده کنید، بدون اینکه به gateway نیاز باشد.


برای بررسی‌های انتهابه‌انتهای provider، پس از سبز شدن تست‌های سطح پایین‌تر provider، `openclaw infer ...` را ترجیح دهید. این کار CLI منتشرشده، بارگذاری config، resolve کردن default-agent، فعال‌سازی Pluginهای bundled، و runtime مشترک capability را پیش از ارسال درخواست provider تمرین می‌دهد.

## درخت دستور

textCopy code
[code]
     openclaw infer  list  inspect   model    run    list    inspect    providers    auth login    auth logout    auth status   image    generate    edit    describe    describe-many    providers   audio    transcribe    providers   tts    convert    voices    providers    status    enable    disable    set-provider   video    generate    describe    providers   web    search    fetch    providers   embedding    create    providers
[/code]

## وظایف رایج

این جدول وظایف رایج استنتاج را به دستور infer متناظر نگاشت می‌کند.

وظیفه | دستور | نکات  
---|---|---  
اجرای یک prompt متنی/مدلی | `openclaw infer model run --prompt "..." --json` | به‌طور پیش‌فرض از مسیر محلی معمول استفاده می‌کند  
اجرای prompt مدل روی تصویرها | `openclaw infer model run --prompt "Describe this" --file ./image.png --model provider/model` | برای چند ورودی تصویر، `--file` را تکرار کنید  
تولید یک تصویر | `openclaw infer image generate --prompt "..." --json` | هنگام شروع از یک فایل موجود از `image edit` استفاده کنید  
توصیف یک فایل تصویر | `openclaw infer image describe --file ./image.png --prompt "..." --json` | `--model` باید یک `<provider/model>` دارای قابلیت تصویر باشد  
رونویسی صوت | `openclaw infer audio transcribe --file ./memo.m4a --json` | `--model` باید `<provider/model>` باشد  
سنتز گفتار | `openclaw infer tts convert --text "..." --output ./speech.mp3 --json` | `tts status` معطوف به gateway است  
تولید یک ویدئو | `openclaw infer video generate --prompt "..." --json` | از اشاره‌های provider مانند `--resolution` پشتیبانی می‌کند  
توصیف یک فایل ویدئو | `openclaw infer video describe --file ./clip.mp4 --json` | `--model` باید `<provider/model>` باشد  
جست‌وجوی وب | `openclaw infer web search --query "..." --json` |   
دریافت یک صفحه وب | `openclaw infer web fetch --url https://example.com --json` |   
ایجاد embeddingها | `openclaw infer embedding create --text "..." --json` |   
  
## رفتار

  * `openclaw infer ...` سطح CLI اصلی برای این جریان‌های کاری است.
  * وقتی خروجی توسط دستور یا اسکریپت دیگری مصرف می‌شود از `--json` استفاده کنید.
  * وقتی به یک backend مشخص نیاز است از `--provider` یا `--model provider/model` استفاده کنید.
  * برای پاس دادن یک سطح یک‌باره thinking/reasoning (`off`، `minimal`، `low`، `medium`، `high`، `adaptive`، `xhigh`، یا `max`) و در عین حال خام نگه داشتن اجرا، از `model run --thinking <level>` استفاده کنید.
  * برای `image describe`، `audio transcribe` و `video describe`، `--model` باید از قالب `<provider/model>` استفاده کند.
  * برای `image describe`، یک `--model` صریح همان provider/model را مستقیماً اجرا می‌کند. مدل باید در model catalog یا config provider قابلیت تصویر داشته باشد. `codex/<model>` یک نوبت محدود درک تصویر در app-server مربوط به Codex اجرا می‌کند؛ `openai-codex/<model>` از مسیر provider مربوط به OpenAI Codex OAuth استفاده می‌کند.
  * دستورهای اجرای stateless به‌طور پیش‌فرض local هستند.
  * دستورهای state مدیریت‌شده توسط Gateway به‌طور پیش‌فرض gateway هستند.
  * مسیر محلی معمول نیاز ندارد gateway در حال اجرا باشد.
  * `model run` محلی یک completion سبک و یک‌باره provider است. مدل و auth پیکربندی‌شده agent را resolve می‌کند، اما نوبت chat-agent را شروع نمی‌کند، ابزارها را بارگذاری نمی‌کند، یا سرورهای bundled MCP را باز نمی‌کند.
  * `model run --file` فایل‌های تصویر را می‌پذیرد، نوع MIME آن‌ها را تشخیص می‌دهد، و آن‌ها را همراه با prompt ارائه‌شده به مدل انتخاب‌شده می‌فرستد. برای چند تصویر، `--file` را تکرار کنید.
  * `model run --file` ورودی‌های غیرتصویری را رد می‌کند. برای فایل‌های صوتی از `infer audio transcribe` و برای فایل‌های ویدئویی از `infer video describe` استفاده کنید.
  * `model run --gateway` مسیریابی Gateway، auth ذخیره‌شده، انتخاب provider، و runtime تعبیه‌شده را تمرین می‌دهد، اما همچنان به‌صورت یک probe خام مدل اجرا می‌شود: prompt ارائه‌شده و هر پیوست تصویر را بدون transcript قبلی session، زمینه bootstrap/AGENTS، مونتاژ context-engine، ابزارها، یا سرورهای bundled MCP ارسال می‌کند.
  * `model run --gateway --model <provider/model>` به یک credential مورد اعتماد operator gateway نیاز دارد، زیرا درخواست از Gateway می‌خواهد یک override موردی provider/model اجرا کند.
  * `model run --thinking` محلی از مسیر provider-completion سبک استفاده می‌کند؛ سطح‌های مخصوص provider مانند `adaptive` و `max` به نزدیک‌ترین سطح portable simple-completion نگاشت می‌شوند.


## مدل

برای استنتاج متنی متکی به provider و بازرسی model/provider از `model` استفاده کنید.

bashCopy code
[code]
    openclaw infer model run --prompt "Reply with exactly: smoke-ok" --jsonopenclaw infer model run --prompt "Summarize this changelog entry" --model openai/gpt-5.4 --jsonopenclaw infer model run --prompt "Describe this image in one sentence" --file ./photo.jpg --model google/gemini-2.5-flash --jsonopenclaw infer model run --prompt "Use more reasoning here" --thinking high --jsonopenclaw infer model providers --jsonopenclaw infer model inspect --name gpt-5.5 --json
[/code]

برای smoke-test کردن یک provider مشخص بدون راه‌اندازی Gateway یا بارگذاری سطح کامل ابزار agent از refهای کامل `<provider/model>` استفاده کنید:

bashCopy code
[code]
    openclaw infer model run --local --model anthropic/claude-sonnet-4-6 --prompt "Reply with exactly: pong" --jsonopenclaw infer model run --local --model cerebras/zai-glm-4.7 --prompt "Reply with exactly: pong" --jsonopenclaw infer model run --local --model google/gemini-2.5-flash --prompt "Reply with exactly: pong" --jsonopenclaw infer model run --local --model groq/llama-3.1-8b-instant --prompt "Reply with exactly: pong" --jsonopenclaw infer model run --local --model mistral/mistral-medium-3-5 --prompt "Reply with exactly: pong" --jsonopenclaw infer model run --local --model mistral/mistral-small-latest --prompt "Reply with exactly: pong" --jsonopenclaw infer model run --local --model openai/gpt-4.1 --prompt "Reply with exactly: pong" --jsonopenclaw infer model run --local --model ollama/qwen2.5vl:7b --prompt "Describe this image." --file ./photo.jpg --json
[/code]

نکات:

  * `model run` محلی باریک‌ترین smoke در CLI برای سلامت provider/model/auth است، زیرا برای providerهای غیر Codex فقط prompt ارائه‌شده را به مدل انتخاب‌شده می‌فرستد.
  * `model run --model <provider/model>` محلی می‌تواند پیش از نوشته شدن آن provider در config، از ردیف‌های دقیق bundled static catalog از `models list --all` استفاده کند. auth مربوط به provider همچنان لازم است؛ credentialهای گمشده به‌صورت خطاهای auth شکست می‌خورند، نه `Unknown model`.
  * برای probeهای reasoning مربوط به Mistral Medium 3.5، temperature را تنظیم‌نشده/پیش‌فرض بگذارید. Mistral ترکیب `reasoning_effort="high"` با `temperature: 0` را رد می‌کند؛ از `mistral/mistral-medium-3-5` با temperature پیش‌فرض یا یک مقدار reasoning-mode غیرصفر مانند `0.7` استفاده کنید.
  * probeهای محلی `openai-codex/*` استثنای محدود هستند: OpenClaw یک system instruction حداقلی اضافه می‌کند تا transport مربوط به Codex Responses بتواند فیلد الزامی `instructions` خود را پر کند، بدون افزودن زمینه کامل agent، ابزارها، memory، یا transcript session.
  * `model run --file` محلی همان مسیر سبک را نگه می‌دارد و محتوای تصویر را مستقیماً به پیام واحد user پیوست می‌کند. فایل‌های تصویر رایج مانند PNG، JPEG و WebP وقتی نوع MIME آن‌ها به‌صورت `image/*` تشخیص داده شود کار می‌کنند؛ فایل‌های پشتیبانی‌نشده یا شناسایی‌نشده پیش از فراخوانی provider شکست می‌خورند.
  * `model run --file` زمانی بهترین گزینه است که می‌خواهید مدل متنی multimodal انتخاب‌شده را مستقیماً تست کنید. وقتی انتخاب provider درک تصویر OpenClaw و مسیریابی پیش‌فرض image-model را می‌خواهید، از `infer image describe` استفاده کنید.
  * مدل انتخاب‌شده باید از ورودی تصویر پشتیبانی کند؛ مدل‌های فقط‌متن ممکن است درخواست را در لایه provider رد کنند.
  * `model run --prompt` باید متن غیر whitespace داشته باشد؛ promptهای خالی پیش از فراخوانی providerهای محلی یا Gateway رد می‌شوند.
  * `model run` محلی وقتی provider هیچ خروجی متنی برنگرداند با کد غیرصفر خارج می‌شود، بنابراین providerهای محلی غیرقابل‌دسترسی و completionهای خالی شبیه probeهای موفق به نظر نمی‌رسند.
  * وقتی نیاز دارید مسیریابی Gateway، راه‌اندازی agent-runtime، یا state provider مدیریت‌شده توسط Gateway را در حالی تست کنید که ورودی مدل خام بماند، از `model run --gateway` استفاده کنید. وقتی زمینه کامل agent، ابزارها، memory و transcript session را می‌خواهید، از `openclaw agent` یا سطوح chat استفاده کنید.
  * `model auth login`، `model auth logout` و `model auth status` state ذخیره‌شده auth مربوط به provider را مدیریت می‌کنند.


## تصویر

برای تولید، ویرایش و توصیف از `image` استفاده کنید.

bashCopy code
[code]
    openclaw infer image generate --prompt "friendly lobster illustration" --jsonopenclaw infer image generate --prompt "cinematic product photo of headphones" --jsonopenclaw infer image generate --model openai/gpt-image-1.5 --output-format png --background transparent --prompt "simple red circle sticker on a transparent background" --jsonopenclaw infer image generate --prompt "slow image backend" --timeout-ms 180000 --jsonopenclaw infer image edit --file ./logo.png --model openai/gpt-image-1.5 --output-format png --background transparent --prompt "keep the logo, remove the background" --jsonopenclaw infer image edit --file ./poster.png --prompt "make this a vertical story ad" --size 2160x3840 --aspect-ratio 9:16 --resolution 4K --jsonopenclaw infer image describe --file ./photo.jpg --jsonopenclaw infer image describe --file ./receipt.jpg --prompt "Extract the merchant, date, and total" --jsonopenclaw infer image describe-many --file ./before.png --file ./after.png --prompt "Compare the screenshots and list visible UI changes" --jsonopenclaw infer image describe --file ./ui-screenshot.png --model openai/gpt-4.1-mini --jsonopenclaw infer image describe --file ./photo.jpg --model ollama/qwen2.5vl:7b --prompt "Describe the image in one sentence" --timeout-ms 300000 --json
[/code]

یادداشت‌ها:

  * هنگام شروع از فایل‌های ورودی موجود، از `image edit` استفاده کنید.

  * برای providerها/مدل‌هایی که از راهنمایی‌های هندسی در ویرایش‌های تصویر مرجع پشتیبانی می‌کنند، از `--size`، `--aspect-ratio`، یا `--resolution` همراه با `image edit` استفاده کنید.

  * برای خروجی PNG با پس‌زمینه شفاف OpenAI، از `--output-format png --background transparent` همراه با `--model openai/gpt-image-1.5` استفاده کنید؛ `--openai-background` همچنان به‌عنوان نام مستعار اختصاصی OpenAI در دسترس است. providerهایی که پشتیبانی از پس‌زمینه را اعلام نمی‌کنند، این راهنما را به‌عنوان یک بازنویسی نادیده‌گرفته‌شده گزارش می‌کنند.

  * برای بررسی اینکه کدام providerهای تصویرِ همراه قابل کشف، پیکربندی‌شده، انتخاب‌شده هستند و هر provider کدام قابلیت‌های تولید/ویرایش را ارائه می‌کند، از `image providers --json` استفاده کنید.

  * از `image generate --model <provider/model> --json` به‌عنوان محدودترین smoke زنده CLI برای تغییرات تولید تصویر استفاده کنید. مثال:

bashCopy code
[code]openclaw infer image providers --jsonopenclaw infer image generate \  --model google/gemini-3.1-flash-image-preview \  --prompt "Minimal flat test image: one blue square on a white background, no text." \  --output ./openclaw-infer-image-smoke.png \  --json
[/code]

پاسخ JSON، `ok`،‏ `provider`،‏ `model`،‏ `attempts` و مسیرهای خروجی نوشته‌شده را گزارش می‌کند. وقتی `--output` تنظیم شده باشد، پسوند نهایی ممکن است از نوع MIME بازگردانده‌شده توسط provider پیروی کند.

  * برای `image describe` و `image describe-many`، از `--prompt` استفاده کنید تا به مدل بینایی یک دستور ویژه‌ی کار بدهید، مانند OCR، مقایسه، بررسی UI، یا کپشن‌نویسی کوتاه.

  * از `--timeout-ms` برای مدل‌های بینایی محلی کند یا شروع‌های سرد Ollama استفاده کنید.

  * برای `image describe`،‏ `--model` باید یک `<provider/model>` دارای قابلیت تصویر باشد.

  * برای مدل‌های بینایی محلی Ollama، ابتدا مدل را pull کنید و `OLLAMA_API_KEY` را روی هر مقدار جای‌نگهدار تنظیم کنید، برای مثال `ollama-local`. [Ollama](</fa/providers/ollama#vision-and-image-description>) را ببینید.


## صوت

از `audio` برای رونویسی فایل استفاده کنید.

bashCopy code
[code]
    openclaw infer audio transcribe --file ./memo.m4a --jsonopenclaw infer audio transcribe --file ./team-sync.m4a --language en --prompt "Focus on names and action items" --jsonopenclaw infer audio transcribe --file ./memo.m4a --model openai/whisper-1 --json
[/code]

یادداشت‌ها:

  * `audio transcribe` برای رونویسی فایل است، نه مدیریت نشست بلادرنگ.
  * `--model` باید `<provider/model>` باشد.


## TTS

از `tts` برای سنتز گفتار و وضعیت providerهای TTS استفاده کنید.

bashCopy code
[code]
    openclaw infer tts convert --text "hello from openclaw" --output ./hello.mp3 --jsonopenclaw infer tts convert --text "Your build is complete" --output ./build-complete.mp3 --jsonopenclaw infer tts providers --jsonopenclaw infer tts status --json
[/code]

یادداشت‌ها:

  * `tts status` به‌طور پیش‌فرض روی Gateway است، زیرا وضعیت TTS مدیریت‌شده توسط Gateway را بازتاب می‌دهد.
  * برای بررسی و پیکربندی رفتار TTS، از `tts providers`،‏ `tts voices` و `tts set-provider` استفاده کنید.


## ویدئو

از `video` برای تولید و توصیف استفاده کنید.

bashCopy code
[code]
    openclaw infer video generate --prompt "cinematic sunset over the ocean" --jsonopenclaw infer video generate --prompt "slow drone shot over a forest lake" --resolution 768P --duration 6 --jsonopenclaw infer video describe --file ./clip.mp4 --jsonopenclaw infer video describe --file ./clip.mp4 --model openai/gpt-4.1-mini --json
[/code]

یادداشت‌ها:

  * `video generate` گزینه‌های `--size`،‏ `--aspect-ratio`،‏ `--resolution`،‏ `--duration`،‏ `--audio`،‏ `--watermark` و `--timeout-ms` را می‌پذیرد و آن‌ها را به runtime تولید ویدئو ارسال می‌کند.
  * برای `video describe`،‏ `--model` باید `<provider/model>` باشد.


## وب

از `web` برای گردش‌کارهای جست‌وجو و واکشی استفاده کنید.

bashCopy code
[code]
    openclaw infer web search --query "OpenClaw docs" --jsonopenclaw infer web search --query "OpenClaw infer web providers" --jsonopenclaw infer web fetch --url https://docs.openclaw.ai/cli/infer --jsonopenclaw infer web providers --json
[/code]

یادداشت‌ها:

  * برای بررسی providerهای موجود، پیکربندی‌شده و انتخاب‌شده، از `web providers` استفاده کنید.


## embedding

از `embedding` برای ساخت بردار و بررسی providerهای embedding استفاده کنید.

bashCopy code
[code]
    openclaw infer embedding create --text "friendly lobster" --jsonopenclaw infer embedding create --text "customer support ticket: delayed shipment" --model openai/text-embedding-3-large --jsonopenclaw infer embedding providers --json
[/code]

## خروجی JSON

دستورهای infer خروجی JSON را زیر یک envelope مشترک نرمال‌سازی می‌کنند:

jsonCopy code
[code]
    {  "ok": true,  "capability": "image.generate",  "transport": "local",  "provider": "openai",  "model": "gpt-image-2",  "attempts": [],  "outputs": []}
[/code]

فیلدهای سطح بالا پایدار هستند:

  * `ok`
  * `capability`
  * `transport`
  * `provider`
  * `model`
  * `attempts`
  * `outputs`
  * `error`


برای دستورهای رسانه تولیدشده، `outputs` شامل فایل‌هایی است که OpenClaw نوشته است. برای خودکارسازی، به‌جای parse کردن stdout خوانا برای انسان، از `path`،‏ `mimeType`،‏ `size` و هر ابعاد ویژه‌ی رسانه در آن آرایه استفاده کنید.

## خطاهای رایج

bashCopy code
[code]
    # Badopenclaw infer media image generate --prompt "friendly lobster" # Goodopenclaw infer image generate --prompt "friendly lobster"
[/code]

bashCopy code
[code]
    # Badopenclaw infer audio transcribe --file ./memo.m4a --model whisper-1 --json # Goodopenclaw infer audio transcribe --file ./memo.m4a --model openai/whisper-1 --json
[/code]

## یادداشت‌ها

  * `openclaw capability ...` نام مستعار `openclaw infer ...` است.


## مرتبط

  * [مرجع CLI](</fa/cli>)
  * [مدل‌ها](</fa/concepts/models>)


Was this useful?YesNo