---
title: CLI رونوشت‌ها
source_url: https://docs.openclaw.ai/fa/cli/transcripts
scraped_at: 2026-06-29
---

Get started

# `openclaw transcripts`

رونوشت‌هایی را که ابزار اصلی `transcripts` در OpenClaw نوشته است بررسی کنید. این CLI فقط خواندنی است؛ ضبط، وارد کردن و خلاصه‌سازی در اختیار ابزار عامل و منابع شروع خودکار پیکربندی‌شده هستند.

وقتی می‌خواهید یادداشت‌های دیروز را پیدا کنید، فایل Markdown را در یک ویرایشگر باز کنید، یک رونوشت را به ابزار دیگری بدهید، یا عیب‌یابی کنید که یک نشست در کجای دیسک ذخیره شده است، از CLI استفاده کنید. این ابزار ضبط را شروع یا متوقف نمی‌کند.

مصنوعات زیر دایرکتوری وضعیت OpenClaw قرار دارند:

textCopy code
[code]
    $OPENCLAW_STATE_DIR/transcripts/YYYY-MM-DD/<session>/  metadata.json  transcript.jsonl  summary.json  summary.md
[/code]

دایرکتوری وضعیت پیش‌فرض `~/.openclaw` است؛ برای استفاده از دایرکتوری دیگر، `OPENCLAW_STATE_DIR` را تنظیم کنید. دایرکتوری تاریخ از زمان شروع نشست می‌آید، و دایرکتوری نشست یک بخش امن برای سامانه فایل است که از شناسه نشست مشتق شده است.

## فرمان‌ها

bashCopy code
[code]
    openclaw transcripts listopenclaw transcripts show <session>openclaw transcripts show YYYY-MM-DD/<session>openclaw transcripts path <session>openclaw transcripts path YYYY-MM-DD/<session>openclaw transcripts path <session> --diropenclaw transcripts path <session> --metadataopenclaw transcripts path <session> --transcriptopenclaw transcripts list --jsonopenclaw transcripts show <session> --jsonopenclaw transcripts path <session> --json
[/code]

  * `list`: نشست‌های ذخیره‌شده، انتخابگر واجد تاریخ، زمان شروع، عنوان، و مسیر `summary.md` را فهرست می‌کند.
  * `show <session>`: `summary.md` ذخیره‌شده را چاپ می‌کند.
  * `path <session>`: مسیر `summary.md` را چاپ می‌کند.
  * `path <session> --dir`: دایرکتوری نشست را چاپ می‌کند.
  * `path <session> --metadata`: `metadata.json` را چاپ می‌کند.
  * `path <session> --transcript`: `transcript.jsonl` را چاپ می‌کند.
  * `--json`: خروجی قابل‌خواندن توسط ماشین را چاپ می‌کند.


وقتی یک شناسه نشست انسانی در چند روز تکرار می‌شود، از انتخابگر واجد تاریخ از `list` استفاده کنید، برای مثال `openclaw transcripts show 2026-05-22/standup`. شناسه‌های نشست پیش‌فرض شامل یک مهر زمانی و پسوند تصادفی هستند؛ شناسه‌های نشست ثابت را فقط زمانی پیکربندی کنید که در همان روز یکتا باشند.

## خروجی

`list` در هر خط یک نشست چاپ می‌کند:

textCopy code
[code]
    2026-05-22/standup  2026-05-22T09:00:00.000Z  Weekly standup  /Users/alex/.openclaw/transcripts/2026-05-22/standup/summary.md
[/code]

خروجی با تب جدا شده است. ستون‌ها عبارت‌اند از انتخابگر، زمان شروع، عنوان، و مسیر خلاصه. انتخابگر امن‌ترین مقداری است که می‌توان دوباره به `show` یا `path` داد.

`list --json` اشیائی با این موارد چاپ می‌کند:

  * `sessionId`
  * `selector`
  * `date`
  * `title`
  * `startedAt`
  * `stoppedAt`
  * `source`
  * `path`
  * `summaryPath`
  * `hasSummary`


`show --json` فراداده نشست ذخیره‌شده، انتخابگر، دایرکتوری نشست، مسیر خلاصه، و متن Markdown خلاصه را برمی‌گرداند. `path --json` مسیر انتخاب‌شده و اینکه آن فایل وجود دارد یا نه را برمی‌گرداند.

## نشست‌های زیاد در هر روز

Transcripts نشست‌ها را ابتدا بر اساس تاریخ و سپس بر اساس شناسه نشست گروه‌بندی می‌کند. ده جلسه در یک روز به ده پوشه هم‌سطح تبدیل می‌شوند:

textCopy code
[code]
    ~/.openclaw/transcripts/2026-05-22/  transcript-2026-05-22T09-00-00-000Z-a1b2c3d4/  transcript-2026-05-22T10-30-00-000Z-b2c3d4e5/  standup/
[/code]

برای بیشتر خودکارسازی‌ها از شناسه‌های تولیدشده پیش‌فرض استفاده کنید. از یک شناسه ثابت مانند `standup` فقط زمانی استفاده کنید که همان شناسه در همان تاریخ دو بار استفاده نخواهد شد.

## خلاصه‌های گمشده

نشست‌های زنده وقتی نشست متوقف می‌شود `summary.md` را می‌نویسند. رونوشت‌های واردشده بلافاصله پس از وارد کردن، `summary.md` را می‌نویسند. یک نشست همچنان می‌تواند بدون خلاصه در `list` ظاهر شود، وقتی ضبط فعال است، یک ارائه‌دهنده هنگام توقف شکست خورده است، یا فراداده پیش از رسیدن هر گفته‌ای نوشته شده است.

برای بررسی رونوشت فقط‌افزودنی از `path <session> --transcript` استفاده کنید، و برای بازتولید خلاصه Markdown از کنش `summarize` در ابزار `transcripts` استفاده کنید.

## پیکربندی

ضبط رونوشت اختیاری است، چون منابع زنده می‌توانند به صدای جلسه ملحق شوند و آن را ضبط کنند. ابزار را با `transcripts.enabled` در سطح بالا فعال کنید:

jsonCopy code
[code]
    {  "transcripts": {    "enabled": true,    "maxUtterances": 2000  }}
[/code]

منابع شروع خودکار را با `transcripts.autoStart` در `openclaw.json` پیکربندی کنید. هر ورودی با حضور داشتن فعال می‌شود؛ برای غیرفعال کردن آن منبع، ورودی را حذف کنید.

jsonCopy code
[code]
    {  "transcripts": {    "enabled": true,    "autoStart": [      {        "providerId": "discord-voice",        "guildId": "1234567890",        "channelId": "2345678901"      },      {        "providerId": "slack-huddle",        "accountId": "workspace",        "channelId": "C123"      }    ]  }}
[/code]

Was this useful?YesNo

Open issue