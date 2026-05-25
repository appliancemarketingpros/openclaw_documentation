---
title: Tencent Cloud (TokenHub)
source_url: https://docs.openclaw.ai/fa/providers/tencent
scraped_at: 2026-05-25
---

Tencent Cloud به‌صورت یک Plugin ارائه‌دهندهٔ همراه در OpenClaw عرضه می‌شود. این قابلیت از طریق نقطهٔ پایانی TokenHub (`tencent-tokenhub`) و با استفاده از یک API سازگار با OpenAI، دسترسی به پیش‌نمایش Tencent Hy3 را فراهم می‌کند.

ویژگی | مقدار  
---|---  
شناسهٔ ارائه‌دهنده | `tencent-tokenhub`  
Plugin | همراه، `enabledByDefault: true`  
متغیر محیطی احراز هویت | `TOKENHUB_API_KEY`  
پرچم راه‌اندازی اولیه | `--auth-choice tokenhub-api-key`  
پرچم مستقیم CLI | `--tokenhub-api-key <key>`  
API | سازگار با OpenAI (`openai-completions`)  
URL پایهٔ پیش‌فرض | `https://tokenhub.tencentmaas.com/v1`  
URL پایهٔ جهانی | `https://tokenhub-intl.tencentmaas.com/v1` (بازنویسی)  
مدل پیش‌فرض | `tencent-tokenhub/hy3-preview`  
  
## شروع سریع

* ### یک کلید API برای TokenHub ایجاد کنید

در Tencent Cloud TokenHub یک کلید API ایجاد کنید. اگر برای کلید دامنهٔ دسترسی محدودی انتخاب می‌کنید، **Hy3 preview** را در مدل‌های مجاز بگنجانید.

* ### راه‌اندازی اولیه را اجرا کنید

OnboardingCopy code
[code]
    openclaw onboard --auth-choice tokenhub-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice tokenhub-api-key \--tokenhub-api-key "$TOKENHUB_API_KEY"
[/code]

Env onlyCopy code
[code]
    export TOKENHUB_API_KEY=...
[/code]

* ### مدل را تأیید کنید

bashCopy code
[code]
    openclaw models list --provider tencent-tokenhub
[/code]

## راه‌اندازی غیرتعاملی

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice tokenhub-api-key \  --tokenhub-api-key "$TOKENHUB_API_KEY" \  --skip-health \  --accept-risk
[/code]

## کاتالوگ داخلی

ارجاع مدل | نام | ورودی | زمینه | حداکثر خروجی | یادداشت‌ها  
---|---|---|---|---|---  
`tencent-tokenhub/hy3-preview` | Hy3 preview (TokenHub) | متن | 256,000 | 64,000 | پیش‌فرض؛ دارای قابلیت استدلال  
  
Hy3 preview مدل زبانی بزرگ MoE متعلق به Tencent Hunyuan برای استدلال، پیروی از دستورالعمل‌ها با زمینهٔ طولانی، کدنویسی و گردش‌کارهای عامل است. نمونه‌های سازگار با OpenAI از Tencent از `hy3-preview` به‌عنوان شناسهٔ مدل استفاده می‌کنند و علاوه بر فراخوانی ابزار استاندارد chat-completions، از `reasoning_effort` نیز پشتیبانی می‌کنند.

## قیمت‌گذاری پلکانی

کاتالوگ همراه، فرادادهٔ هزینهٔ پلکانی را ارائه می‌کند که بر اساس طول پنجرهٔ ورودی مقیاس می‌شود؛ بنابراین برآوردهای هزینه بدون بازنویسی دستی پر می‌شوند.

محدودهٔ توکن‌های ورودی | نرخ ورودی | نرخ خروجی | خواندن از کش  
---|---|---|---  
0 - 16,000 | 0.176 | 0.587 | 0.059  
16,000 - 32,000 | 0.235 | 0.939 | 0.088  
32,000+ | 0.293 | 1.173 | 0.117  
  
نرخ‌ها به‌ازای هر یک میلیون توکن و به دلار آمریکا هستند، همان‌گونه که Tencent اعلام کرده است. قیمت‌گذاری را فقط زمانی زیر `models.providers.tencent-tokenhub` بازنویسی کنید که به سطح متفاوتی نیاز دارید.

## پیکربندی پیشرفته

بازنویسی نقطهٔ پایانی

OpenClaw به‌طور پیش‌فرض از نقطهٔ پایانی `https://tokenhub.tencentmaas.com/v1` متعلق به Tencent Cloud استفاده می‌کند. Tencent همچنین یک نقطهٔ پایانی بین‌المللی برای TokenHub مستند کرده است:

bashCopy code
[code]
    openclaw config set models.providers.tencent-tokenhub.baseUrl "https://tokenhub-intl.tencentmaas.com/v1"
[/code]

نقطهٔ پایانی را فقط زمانی بازنویسی کنید که حساب یا منطقهٔ TokenHub شما به آن نیاز داشته باشد.

در دسترس بودن محیط برای daemon

اگر Gateway به‌صورت یک سرویس مدیریت‌شده اجرا می‌شود (launchd، systemd، Docker)، `TOKENHUB_API_KEY` باید برای آن فرایند قابل مشاهده باشد. آن را در `~/.openclaw/.env` یا از طریق `env.shellEnv` تنظیم کنید تا محیط‌های launchd، systemd یا Docker exec بتوانند آن را بخوانند.

## مرتبط

[**ارائه‌دهندگان مدل** انتخاب ارائه‌دهندگان، ارجاع‌های مدل و رفتار failover. ](</fa/concepts/model-providers>) [**مرجع پیکربندی** طرح‌وارهٔ کامل پیکربندی، شامل تنظیمات ارائه‌دهنده. ](</fa/gateway/configuration>) [**Tencent TokenHub** صفحهٔ محصول TokenHub متعلق به Tencent Cloud. ](<https://cloud.tencent.com/product/tokenhub>) [**کارت مدل Hy3 preview** جزئیات و بنچمارک‌های Tencent Hunyuan Hy3 preview. ](<https://huggingface.co/tencent/Hy3-preview>)

Was this useful?YesNo