---
title: ابزار apply_patch
source_url: https://docs.openclaw.ai/fa/tools/apply-patch
scraped_at: 2026-05-25
---

تغییرات فایل را با استفاده از قالب patch ساختاریافته اعمال کنید. این روش برای ویرایش‌های چندفایلی یا چندبخشی مناسب است، جایی که یک فراخوانی `edit` شکننده خواهد بود.

این ابزار یک رشته‌ی `input` می‌پذیرد که یک یا چند عملیات فایل را در بر می‌گیرد:

CodeCopy code
[code]
    *** Begin Patch*** Add File: path/to/file.txt+line 1+line 2*** Update File: src/app.ts@@-old line+new line*** Delete File: obsolete.txt*** End Patch
[/code]

## پارامترها

  * `input` (الزامی): محتوای کامل patch شامل `*** Begin Patch` و `*** End Patch`.


## نکته‌ها

  * مسیرهای patch از مسیرهای نسبی (از دایرکتوری workspace) و مسیرهای مطلق پشتیبانی می‌کنند.
  * مقدار پیش‌فرض `tools.exec.applyPatch.workspaceOnly` برابر `true` است (محدود به workspace). فقط زمانی آن را روی `false` تنظیم کنید که عمداً می‌خواهید `apply_patch` بیرون از دایرکتوری workspace بنویسد/حذف کند.
  * برای تغییر نام فایل‌ها، از `*** Move to:` داخل یک بخش `*** Update File:` استفاده کنید.
  * `*** End of File` در صورت نیاز درج فقط-EOF را مشخص می‌کند.
  * به‌طور پیش‌فرض برای مدل‌های OpenAI و OpenAI Codex در دسترس است. برای غیرفعال‌کردن آن، `tools.exec.applyPatch.enabled: false` را تنظیم کنید.
  * در صورت نیاز، از طریق `tools.exec.applyPatch.allowModels` بر اساس مدل محدودسازی کنید.
  * پیکربندی فقط زیر `tools.exec` قرار دارد.


## مثال

jsonCopy code
[code]
    {  "tool": "apply_patch",  "input": "*** Begin Patch\n*** Update File: src/index.ts\n@@\n-const foo = 1\n+const foo = 2\n*** End Patch"}
[/code]

## مرتبط

[**Diffs** نمایشگر diff فقط‌خواندنی برای ارائه‌ی تغییرات. ](</fa/tools/diffs>) [**Exec tool** اجرای فرمان shell از سوی agent. ](</fa/tools/exec>) [**Code execution** تحلیل Python راه‌دور sandbox‌شده با xAI. ](</fa/tools/code-execution>)

Was this useful?YesNo