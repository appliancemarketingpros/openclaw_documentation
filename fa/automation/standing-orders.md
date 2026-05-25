---
title: دستورهای ثابت
source_url: https://docs.openclaw.ai/fa/automation/standing-orders
scraped_at: 2026-05-25
---

دستورهای دائمی به عامل شما **اختیار عملیاتی دائمی** برای برنامه‌های تعریف‌شده می‌دهند. به‌جای اینکه هر بار دستورالعمل‌های جداگانه برای کارها بدهید، برنامه‌هایی با محدوده، محرک‌ها و قواعد ارجاع شفاف تعریف می‌کنید - و عامل به‌صورت خودکار در همان مرزها اجرا می‌کند.

این تفاوت میان این است که هر جمعه به دستیار خود بگویید «گزارش هفتگی را بفرست» یا اختیار دائمی بدهید: «گزارش هفتگی بر عهده توست. هر جمعه آن را تدوین و ارسال کن و فقط اگر چیزی نادرست به نظر رسید ارجاع بده.»

## چرا دستورهای دائمی

**بدون دستورهای دائمی:**

  * باید برای هر کار به عامل اعلان بدهید
  * عامل بین درخواست‌ها بیکار می‌ماند
  * کارهای روتین فراموش یا به تأخیر می‌افتند
  * شما به گلوگاه تبدیل می‌شوید


**با دستورهای دائمی:**

  * عامل در مرزهای تعریف‌شده به‌صورت خودکار اجرا می‌کند
  * کارهای روتین طبق زمان‌بندی و بدون اعلان انجام می‌شوند
  * شما فقط برای استثناها و تأییدها وارد می‌شوید
  * عامل زمان بیکاری را به‌شکل مفید پر می‌کند


## چگونه کار می‌کنند

دستورهای دائمی در فایل‌های [فضای کاری عامل](</fa/concepts/agent-workspace>) شما تعریف می‌شوند. رویکرد پیشنهادی این است که آن‌ها را مستقیماً در `AGENTS.md` قرار دهید (که در هر نشست به‌صورت خودکار تزریق می‌شود) تا عامل همیشه آن‌ها را در زمینه داشته باشد. برای پیکربندی‌های بزرگ‌تر، می‌توانید آن‌ها را در یک فایل اختصاصی مانند `standing-orders.md` نیز قرار دهید و از `AGENTS.md` به آن ارجاع دهید.

هر برنامه مشخص می‌کند:

  1. **محدوده** \- عامل مجاز به انجام چه کاری است
  2. **محرک‌ها** \- چه زمانی اجرا شود (زمان‌بندی، رویداد یا شرط)
  3. **گیت‌های تأیید** \- چه چیزی پیش از اقدام به تأیید انسانی نیاز دارد
  4. **قواعد ارجاع** \- چه زمانی متوقف شود و درخواست کمک کند


عامل این دستورالعمل‌ها را در هر نشست از طریق فایل‌های راه‌اندازی فضای کاری بارگذاری می‌کند (برای فهرست کامل فایل‌های تزریق‌شونده خودکار، [فضای کاری عامل](</fa/concepts/agent-workspace>) را ببینید) و همراه با [کارهای Cron](</fa/automation/cron-jobs>) برای اجرای زمان‌محور، بر اساس آن‌ها عمل می‌کند.

## ساختار یک دستور دائمی

markdownCopy code
[code]
    ## Program: Weekly Status Report **Authority:** Compile data, generate report, deliver to stakeholders**Trigger:** Every Friday at 4 PM (enforced via cron job)**Approval gate:** None for standard reports. Flag anomalies for human review.**Escalation:** If data source is unavailable or metrics look unusual (>2σ from norm) ### Execution steps 1. Pull metrics from configured sources2. Compare to prior week and targets3. Generate report in Reports/weekly/YYYY-MM-DD.md4. Deliver summary via configured channel5. Log completion to Agent/Logs/ ### What NOT to do - Do not send reports to external parties- Do not modify source data- Do not skip delivery if metrics look bad - report accurately
[/code]

## دستورهای دائمی به‌همراه کارهای Cron

دستورهای دائمی تعریف می‌کنند عامل مجاز است **چه کاری** انجام دهد. [کارهای Cron](</fa/automation/cron-jobs>) تعریف می‌کنند این کار **چه زمانی** رخ دهد. آن‌ها با هم کار می‌کنند:

CodeCopy code
[code]
    Standing Order: "You own the daily inbox triage"    ↓Cron Job (8 AM daily): "Execute inbox triage per standing orders"    ↓Agent: Reads standing orders → executes steps → reports results
[/code]

اعلان کار Cron باید به‌جای تکرار دستور دائمی، به آن ارجاع دهد:

bashCopy code
[code]
    openclaw cron add \  --name daily-inbox-triage \  --cron "0 8 * * 1-5" \  --tz America/New_York \  --timeout-seconds 300 \  --announce \  --channel imessage \  --to "+1XXXXXXXXXX" \  --message "Execute daily inbox triage per standing orders. Check mail for new alerts. Parse, categorize, and persist each item. Report summary to owner. Escalate unknowns."
[/code]

## نمونه‌ها

### نمونه ۱: محتوا و شبکه‌های اجتماعی (چرخه هفتگی)

markdownCopy code
[code]
    ## Program: Content & Social Media **Authority:** Draft content, schedule posts, compile engagement reports**Approval gate:** All posts require owner review for first 30 days, then standing approval**Trigger:** Weekly cycle (Monday review → mid-week drafts → Friday brief) ### Weekly cycle - **Monday:** Review platform metrics and audience engagement- **Tuesday-Thursday:** Draft social posts, create blog content- **Friday:** Compile weekly marketing brief → deliver to owner ### Content rules - Voice must match the brand (see SOUL.md or brand voice guide)- Never identify as AI in public-facing content- Include metrics when available- Focus on value to audience, not self-promotion
[/code]

### نمونه ۲: عملیات مالی (محرک‌محور بر اساس رویداد)

markdownCopy code
[code]
    ## Program: Financial Processing **Authority:** Process transaction data, generate reports, send summaries**Approval gate:** None for analysis. Recommendations require owner approval.**Trigger:** New data file detected OR scheduled monthly cycle ### When new data arrives 1. Detect new file in designated input directory2. Parse and categorize all transactions3. Compare against budget targets4. Flag: unusual items, threshold breaches, new recurring charges5. Generate report in designated output directory6. Deliver summary to owner via configured channel ### Escalation rules - Single item > $500: immediate alert- Category > budget by 20%: flag in report- Unrecognizable transaction: ask owner for categorization- Failed processing after 2 retries: report failure, do not guess
[/code]

### نمونه ۳: پایش و هشدارها (پیوسته)

markdownCopy code
[code]
    ## Program: System Monitoring **Authority:** Check system health, restart services, send alerts**Approval gate:** Restart services automatically. Escalate if restart fails twice.**Trigger:** Every heartbeat cycle ### Checks - Service health endpoints responding- Disk space above threshold- Pending tasks not stale (>24 hours)- Delivery channels operational ### Response matrix | Condition        | Action                   | Escalate?                || ---------------- | ------------------------ | ------------------------ || Service down     | Restart automatically    | Only if restart fails 2x || Disk space < 10% | Alert owner              | Yes                      || Stale task > 24h | Remind owner             | No                       || Channel offline  | Log and retry next cycle | If offline > 2 hours     |
[/code]

## الگوی اجرا-راستی‌آزمایی-گزارش

دستورهای دائمی زمانی بهترین عملکرد را دارند که با انضباط سخت‌گیرانه در اجرا ترکیب شوند. هر کار در یک دستور دائمی باید این چرخه را دنبال کند:

  1. **اجرا** \- کار واقعی را انجام دهید (صرفاً دستور را تأیید نکنید)
  2. **راستی‌آزمایی** \- تأیید کنید نتیجه درست است (فایل وجود دارد، پیام تحویل داده شده، داده تجزیه شده است)
  3. **گزارش** \- به مالک بگویید چه کاری انجام شده و چه چیزی راستی‌آزمایی شده است

markdownCopy code
[code]
    ### Execution rules - Every task follows Execute-Verify-Report. No exceptions.- "I'll do that" is not execution. Do it, then report.- "Done" without verification is not acceptable. Prove it.- If execution fails: retry once with adjusted approach.- If still fails: report failure with diagnosis. Never silently fail.- Never retry indefinitely - 3 attempts max, then escalate.
[/code]

این الگو از رایج‌ترین حالت شکست عامل جلوگیری می‌کند: تأیید یک کار بدون کامل‌کردن آن.

## معماری چندبرنامه‌ای

برای عامل‌هایی که چندین حوزه را مدیریت می‌کنند، دستورهای دائمی را به‌صورت برنامه‌های جداگانه با مرزهای شفاف سازمان‌دهی کنید:

markdownCopy code
[code]
    ## Program 1: [Domain A] (Weekly) ... ## Program 2: [Domain B] (Monthly + On-Demand) ... ## Program 3: [Domain C] (As-Needed) ... ## Escalation Rules (All Programs) - [Common escalation criteria]- [Approval gates that apply across programs]
[/code]

هر برنامه باید داشته باشد:

  * **تناوب محرک** مخصوص خود (هفتگی، ماهانه، رویدادمحور، پیوسته)
  * **گیت‌های تأیید** مخصوص خود (برخی برنامه‌ها به نظارت بیشتری نسبت به دیگران نیاز دارند)
  * **مرزهای** شفاف (عامل باید بداند یک برنامه کجا تمام می‌شود و برنامه دیگر کجا آغاز می‌شود)


## بهترین رویه‌ها

### انجام دهید

  * با اختیار محدود شروع کنید و هم‌زمان با شکل‌گیری اعتماد آن را گسترش دهید
  * برای اقدامات پرریسک گیت‌های تأیید صریح تعریف کنید
  * بخش‌های «چه کاری انجام نشود» را اضافه کنید - مرزها به‌اندازه مجوزها اهمیت دارند
  * برای اجرای زمان‌محور قابل اتکا، با کارهای Cron ترکیب کنید
  * گزارش‌های عامل را هفتگی بررسی کنید تا مطمئن شوید دستورهای دائمی دنبال می‌شوند
  * با تغییر نیازهایتان، دستورهای دائمی را به‌روزرسانی کنید - آن‌ها اسناد زنده هستند


### پرهیز کنید

  * در روز اول اختیار گسترده بدهید («هر کاری فکر می‌کنی بهتر است انجام بده»)
  * قواعد ارجاع را حذف کنید - هر برنامه به بند «چه زمانی متوقف شود و بپرسد» نیاز دارد
  * فرض کنید عامل دستورهای شفاهی را به خاطر می‌سپارد - همه‌چیز را در فایل قرار دهید
  * دغدغه‌ها را در یک برنامه واحد مخلوط کنید - برای حوزه‌های جداگانه برنامه‌های جداگانه داشته باشید
  * فراموش کنید با کارهای Cron آن‌ها را الزام‌آور کنید - دستورهای دائمی بدون محرک به پیشنهاد تبدیل می‌شوند


## مرتبط

  * [اتوماسیون](</fa/automation>): همه سازوکارهای اتوماسیون در یک نگاه.
  * [کارهای Cron](</fa/automation/cron-jobs>): اجرای زمان‌بندی برای دستورهای دائمی.
  * [Hookها](</fa/automation/hooks>): اسکریپت‌های رویدادمحور برای رویدادهای چرخه عمر عامل.
  * [Webhookها](</fa/automation/cron-jobs#webhooks>): محرک‌های رویداد HTTP ورودی.
  * [فضای کاری عامل](</fa/concepts/agent-workspace>): محل قرارگیری دستورهای دائمی، شامل فهرست کامل فایل‌های راه‌اندازی تزریق‌شونده خودکار (`AGENTS.md`، `SOUL.md` و غیره).


Was this useful?YesNo