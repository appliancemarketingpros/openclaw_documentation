---
title: ارسال عامل
source_url: https://docs.openclaw.ai/fa/tools/agent-send
scraped_at: 2026-05-25
---

`openclaw agent` یک نوبت عامل را از خط فرمان اجرا می‌کند، بدون اینکه به پیام چت ورودی نیاز داشته باشد. از آن برای جریان‌های کاری اسکریپتی، آزمایش و تحویل برنامه‌نویسی‌شده استفاده کنید.

## شروع سریع

* ### اجرای یک نوبت ساده عامل

bashCopy code
[code]
    openclaw agent --message "What is the weather today?"
[/code]

این پیام را از طریق Gateway ارسال می‌کند و پاسخ را چاپ می‌کند.

* ### هدف‌گیری یک عامل یا نشست مشخص

bashCopy code
[code]
    # Target a specific agentopenclaw agent --agent ops --message "Summarize logs" # Target a phone number (derives session key)openclaw agent --to +15555550123 --message "Status update" # Reuse an existing sessionopenclaw agent --session-id abc123 --message "Continue the task"
[/code]

* ### تحویل پاسخ به یک کانال

bashCopy code
[code]
    # Deliver to WhatsApp (default channel)openclaw agent --to +15555550123 --message "Report ready" --deliver # Deliver to Slackopenclaw agent --agent ops --message "Generate report" \  --deliver --reply-channel slack --reply-to "#reports"
[/code]

## پرچم‌ها

پرچم | توضیح  
---|---  
`--message \<text\>` | پیام برای ارسال (الزامی)  
`--to \<dest\>` | مشتق‌کردن کلید نشست از یک مقصد (تلفن، شناسه چت)  
`--agent \<id\>` | هدف‌گیری یک عامل پیکربندی‌شده (از نشست `main` آن استفاده می‌کند)  
`--session-id \<id\>` | استفاده دوباره از یک نشست موجود بر اساس شناسه  
`--local` | اجبار به زمان اجرای تعبیه‌شده محلی (ردکردن Gateway)  
`--deliver` | ارسال پاسخ به یک کانال چت  
`--channel \<name\>` | کانال تحویل (whatsapp، telegram، discord، slack و غیره)  
`--reply-to \<target\>` | بازنویسی مقصد تحویل  
`--reply-channel \<name\>` | بازنویسی کانال تحویل  
`--reply-account \<id\>` | بازنویسی شناسه حساب تحویل  
`--thinking \<level\>` | تنظیم سطح تفکر برای پروفایل مدل انتخاب‌شده  
`--verbose \<on|full|off\>` | تنظیم سطح پرگویی  
`--timeout \<seconds\>` | بازنویسی مهلت زمانی عامل  
`--json` | خروجی JSON ساخت‌یافته  
  
## رفتار

  * به‌صورت پیش‌فرض، CLI **از طریق Gateway** عبور می‌کند. برای اجبار به زمان اجرای تعبیه‌شده روی ماشین فعلی، `--local` را اضافه کنید.
  * اگر Gateway در دسترس نباشد، CLI **به اجرای تعبیه‌شده محلی بازمی‌گردد**.
  * انتخاب نشست: `--to` کلید نشست را مشتق می‌کند (هدف‌های گروه/کانال جداسازی را حفظ می‌کنند؛ چت‌های مستقیم به `main` فروکاسته می‌شوند).
  * پرچم‌های تفکر و پرگویی در ذخیره‌گاه نشست ماندگار می‌شوند.
  * خروجی: به‌صورت پیش‌فرض متن ساده، یا `--json` برای محموله ساخت‌یافته همراه با فراداده.
  * با `--json --deliver`، JSON شامل وضعیت تحویل برای ارسال‌های ارسال‌شده، سرکوب‌شده، جزئی و ناموفق است. به [وضعیت تحویل JSON](</fa/cli/agent#json-delivery-status>) مراجعه کنید.


## نمونه‌ها

bashCopy code
[code]
    # Simple turn with JSON outputopenclaw agent --to +15555550123 --message "Trace logs" --verbose on --json # Turn with thinking levelopenclaw agent --session-id 1234 --message "Summarize inbox" --thinking medium # Deliver to a different channel than the sessionopenclaw agent --agent ops --message "Alert" --deliver --reply-channel telegram --reply-to "@admin"
[/code]

## مرتبط

[**مرجع CLI عامل** مرجع کامل پرچم‌ها و گزینه‌های `openclaw agent`. ](</fa/cli/agent>) [**زیرعامل‌ها** ایجاد زیرعامل در پس‌زمینه. ](</fa/tools/subagents>) [**نشست‌ها** کلیدهای نشست چگونه کار می‌کنند و `--to`، `--agent` و `--session-id` چگونه آن‌ها را حل می‌کنند. ](</fa/concepts/session>) [**دستورهای اسلش** کاتالوگ دستورهای بومی که داخل نشست‌های عامل استفاده می‌شود. ](</fa/tools/slash-commands>)

Was this useful?YesNo