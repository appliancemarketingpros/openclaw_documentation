---
title: بوم
source_url: https://docs.openclaw.ai/fa/platforms/mac/canvas
scraped_at: 2026-05-25
---

برنامه macOS یک **پنل Canvas** کنترل‌شده توسط عامل را با استفاده از `WKWebView` در خود جای می‌دهد. این پنل یک فضای کاری بصری سبک برای HTML/CSS/JS، A2UI و سطح‌های کوچک UI تعاملی است.

## محل قرارگیری Canvas

وضعیت Canvas در Application Support ذخیره می‌شود:

  * `~/Library/Application Support/OpenClaw/canvas/<session>/...`


پنل Canvas این فایل‌ها را از طریق یک **شِمای URL سفارشی** ارائه می‌کند:

  * `openclaw-canvas://<session>/<path>`


مثال‌ها:

  * `openclaw-canvas://main/` → `<canvasRoot>/main/index.html`
  * `openclaw-canvas://main/assets/app.css` → `<canvasRoot>/main/assets/app.css`
  * `openclaw-canvas://main/widgets/todo/` → `<canvasRoot>/main/widgets/todo/index.html`


اگر در ریشه هیچ `index.html` وجود نداشته باشد، برنامه یک **صفحه داربست داخلی** را نشان می‌دهد.

## رفتار پنل

  * پنلی بدون حاشیه و قابل تغییر اندازه که نزدیک نوار منو (یا نشانگر ماوس) لنگر می‌شود.
  * اندازه/موقعیت را برای هر نشست به خاطر می‌سپارد.
  * هنگام تغییر فایل‌های Canvas محلی، به‌طور خودکار بازبارگذاری می‌شود.
  * در هر زمان فقط یک پنل Canvas قابل مشاهده است (نشست در صورت نیاز عوض می‌شود).


Canvas را می‌توان از Settings → **Allow Canvas** غیرفعال کرد. هنگام غیرفعال بودن، فرمان‌های Node مربوط به canvas مقدار `CANVAS_DISABLED` را برمی‌گردانند.

## سطح API عامل

Canvas از طریق **Gateway WebSocket** در دسترس قرار می‌گیرد، بنابراین عامل می‌تواند:

  * پنل را نمایش/مخفی کند
  * به یک مسیر یا URL ناوبری کند
  * JavaScript را ارزیابی کند
  * یک تصویر snapshot بگیرد


مثال‌های CLI:

bashCopy code
[code]
    openclaw nodes canvas present --node <id>openclaw nodes canvas navigate --node <id> --url "/"openclaw nodes canvas eval --node <id> --js "document.title"openclaw nodes canvas snapshot --node <id>
[/code]

نکات:

  * `canvas.navigate` **مسیرهای Canvas محلی** ، URLهای `http(s)` و URLهای `file://` را می‌پذیرد.
  * اگر `"/"` را ارسال کنید، Canvas داربست محلی یا `index.html` را نشان می‌دهد.


## A2UI در Canvas

A2UI توسط میزبان Canvas در Gateway میزبانی می‌شود و داخل پنل Canvas رندر می‌شود. هنگامی که Gateway یک میزبان Canvas را اعلام می‌کند، برنامه macOS در اولین باز شدن به‌طور خودکار به صفحه میزبان A2UI ناوبری می‌کند.

URL پیش‌فرض میزبان A2UI:

CodeCopy code
[code]
    http://<gateway-host>:18789/__openclaw__/a2ui/
[/code]

### فرمان‌های A2UI (v0.8)

Canvas در حال حاضر پیام‌های **A2UI v0.8** سرور→کلاینت را می‌پذیرد:

  * `beginRendering`
  * `surfaceUpdate`
  * `dataModelUpdate`
  * `deleteSurface`


`createSurface` (v0.9) پشتیبانی نمی‌شود.

مثال CLI:

bashCopy code
[code]
    cat > /tmp/a2ui-v0.8.jsonl <<'EOFA2'{"surfaceUpdate":{"surfaceId":"main","components":[{"id":"root","component":{"Column":{"children":{"explicitList":["title","content"]}}}},{"id":"title","component":{"Text":{"text":{"literalString":"Canvas (A2UI v0.8)"},"usageHint":"h1"}}},{"id":"content","component":{"Text":{"text":{"literalString":"If you can read this, A2UI push works."},"usageHint":"body"}}}]}}{"beginRendering":{"surfaceId":"main","root":"root"}}EOFA2 openclaw nodes canvas a2ui push --jsonl /tmp/a2ui-v0.8.jsonl --node <id>
[/code]

smoke سریع:

bashCopy code
[code]
    openclaw nodes canvas a2ui push --node <id> --text "Hello from A2UI"
[/code]

## راه‌اندازی اجرای عامل از Canvas

Canvas می‌تواند اجرای جدید عامل را از طریق deep linkها راه‌اندازی کند:

  * `openclaw://agent?...`


مثال (در JS):

jsCopy code
[code]
    window.location.href = "openclaw://agent?message=Review%20this%20design";
[/code]

برنامه درخواست تأیید می‌کند، مگر اینکه یک کلید معتبر ارائه شده باشد.

## نکات امنیتی

  * شِمای Canvas پیمایش دایرکتوری را مسدود می‌کند؛ فایل‌ها باید زیر ریشه نشست قرار داشته باشند.
  * محتوای Canvas محلی از یک شِمای سفارشی استفاده می‌کند (به سرور local loopback نیازی نیست).
  * URLهای خارجی `http(s)` فقط زمانی مجاز هستند که صراحتاً به آن‌ها ناوبری شده باشد.


## مرتبط

  * [برنامه macOS](</fa/platforms/macos>)
  * [WebChat](</fa/web/webchat>)


Was this useful?YesNo