---
title: بستهٔ @openclaw/ai
source_url: https://docs.openclaw.ai/fa/reference/openclaw-ai
scraped_at: 2026-07-13
---

ReferenceTechnical reference

`@openclaw/ai` شکل کتابخانه‌ای قابل‌انتشارِ لایه اجرای مدل OpenClaw است: قراردادهای مستقل از ارائه‌دهنده برای پیام، ابزار و جریان؛ اعتبارسنجی، عیب‌یابی، جریان‌های رویداد، یک رجیستری زمان‌اجرای ایزوله و آداپتورهای با بارگذاری تنبل برای هشت خانواده API داخلی (Anthropic Messages، OpenAI Completions، OpenAI Responses، Azure OpenAI Responses، ChatGPT/Codex Responses، Google Generative AI، Google Vertex، Mistral Conversations).

این کتابخانه در هر انتشار، همراه با بسته اصلی `openclaw` و با همان نسخه ثابت‌شده منتشر می‌شود و `npm-shrinkwrap.json` مختص خود را دارد تا درخت وابستگی‌های انتقالی آن هنگام نصب قفل شود. نصب `openclaw` نسخه منطبق `@openclaw/ai` را به‌طور خودکار نصب می‌کند؛ مصرف‌کنندگان کتابخانه نیز می‌توانند بدون هیچ‌گونه کد برنامه OpenClaw مستقیماً به آن وابسته باشند.

## شروع سریع

jsCopy code
[code]
      const runtime = createLlmRuntime();registerBuiltInApiProviders(runtime.registry); const stream = runtime.streamSimple(model, { messages }, { apiKey });for await (const event of stream) {  if (event.type === "text_delta") process.stdout.write(event.delta);}const result = await stream.result();
[/code]

نسخه‌ای قابل‌اجرا در مسیر `examples/ai-chat` مخزن قرار دارد.

## قرارداد طراحی

  * **به‌طور پیش‌فرض محدود به نمونه است.** واردکردن بسته هیچ چیزی را به‌صورت سراسری ثبت نمی‌کند. `createApiRegistry()` / `createLlmRuntime()` نمونه‌های ایزوله برمی‌گردانند؛ `registerBuiltInApiProviders(registry)` ترابری‌های داخلی را برای یک رجیستری فعال می‌کند. ماژول‌های SDK ارائه‌دهندگان در نخستین استفاده به‌صورت تنبل بارگذاری می‌شوند.
  * **سیاست میزبان تزریق می‌شود، نه اینکه در بسته گنجانده شود.** محافظت از واکشی درخواست‌ها (برای مثال، سیاست SSRF)، حذف اسرار از متن بازپخش نتیجه ابزار، پیش‌فرض‌های ابزار سخت‌گیرانه OpenAI و ثبت گزارش‌های عیب‌یابی، درگاه‌های `AiTransportHost` هستند که با `configureAiTransportHost` پیکربندی می‌شوند. پیش‌فرض‌های کتابخانه غیرفعال‌اند؛ OpenClaw پیاده‌سازی‌های واقعی خود را در نمای جریان نصب می‌کند.
  * **یک هویت واحد برای جریان رویداد.** `@openclaw/ai/event-stream` سازنده معیار `EventStream` است که میان هسته OpenClaw، agent-core و مصرف‌کنندگان خارجی به‌اشتراک گذاشته می‌شود.
  * **زیرمسیرهای`internal/*` جزو API نیستند.** این زیرمسیرها برای خود برنامه OpenClaw وجود دارند و هیچ تضمین semver ندارند.
  * شناسه‌های ارائه‌دهنده، اطلاعات احراز هویت، کاتالوگ‌های مدل، تلاش‌های مجدد و جایگزینی پس از خرابی همچنان دغدغه‌های برنامه هستند. OpenClaw این لایه‌ها را پیرامون این بسته قرار می‌دهد؛ مصرف‌کننده کتابخانه یک شیء `Model` و گزینه‌ها را مستقیماً ارائه می‌کند.


## خروجی‌های زیرمسیر

زیرمسیر | محتوا  
---|---  
`.` | قراردادها، `createApiRegistry`، `createLlmRuntime`، `configureAiTransportHost`  
`./providers` | `registerBuiltInApiProviders`، `resetApiProviders`  
`./types` | انواع مدل، پیام، ابزار و جریان  
`./validation` | اعتبارسنجی آرگومان‌های ابزار  
`./diagnostics` | قراردادهای عیب‌یابی  
`./event-stream` | پیاده‌سازی مشترک `EventStream`  
`./internal/*` | داخلی OpenClaw، بدون تضمین semver  
  
Was this useful?YesNo

Open issue