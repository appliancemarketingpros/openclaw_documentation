---
title: CLI نصوص المحادثات
source_url: https://docs.openclaw.ai/ar/cli/transcripts
scraped_at: 2026-06-29
---

Get started

# `openclaw transcripts`

افحص النصوص المكتوبة بواسطة أداة `transcripts` الأساسية في OpenClaw. هذا الـ CLI للقراءة فقط؛ فالالتقاط والاستيراد والتلخيص مملوكة لأداة الوكيل ومصادر البدء التلقائي المُكوّنة.

استخدم الـ CLI عندما تريد العثور على ملاحظات الأمس، أو فتح ملف Markdown في محرر، أو تمرير نص إلى أداة أخرى، أو تصحيح موضع استقرار جلسة على القرص. لا يبدأ الالتقاط ولا يوقفه.

توجد المخرجات ضمن دليل حالة OpenClaw:

textCopy code
[code]
    $OPENCLAW_STATE_DIR/transcripts/YYYY-MM-DD/<session>/  metadata.json  transcript.jsonl  summary.json  summary.md
[/code]

دليل الحالة الافتراضي هو `~/.openclaw`؛ عيّن `OPENCLAW_STATE_DIR` لاستخدام دليل مختلف. يأتي دليل التاريخ من وقت بدء الجلسة، ودليل الجلسة هو مقطع آمن لنظام الملفات مشتق من معرف الجلسة.

## الأوامر

bashCopy code
[code]
    openclaw transcripts listopenclaw transcripts show <session>openclaw transcripts show YYYY-MM-DD/<session>openclaw transcripts path <session>openclaw transcripts path YYYY-MM-DD/<session>openclaw transcripts path <session> --diropenclaw transcripts path <session> --metadataopenclaw transcripts path <session> --transcriptopenclaw transcripts list --jsonopenclaw transcripts show <session> --jsonopenclaw transcripts path <session> --json
[/code]

  * `list`: يسرد الجلسات المخزنة، والمحدد المؤهل بالتاريخ، ووقت البدء، والعنوان، ومسار `summary.md`.
  * `show <session>`: يطبع `summary.md` المخزن.
  * `path <session>`: يطبع مسار `summary.md`.
  * `path <session> --dir`: يطبع دليل الجلسة.
  * `path <session> --metadata`: يطبع `metadata.json`.
  * `path <session> --transcript`: يطبع `transcript.jsonl`.
  * `--json`: يطبع مخرجات قابلة للقراءة آليًا.


عندما يتكرر معرف جلسة بشري عبر أيام متعددة، استخدم المحدد المؤهل بالتاريخ من `list`، مثل `openclaw transcripts show 2026-05-22/standup`. تتضمن معرفات الجلسات الافتراضية طابعًا زمنيًا ولاحقة عشوائية؛ لا تكوّن معرفات جلسات ثابتة إلا عندما تكون فريدة ضمن اليوم.

## المخرجات

يطبع `list` جلسة واحدة في كل سطر:

textCopy code
[code]
    2026-05-22/standup  2026-05-22T09:00:00.000Z  Weekly standup  /Users/alex/.openclaw/transcripts/2026-05-22/standup/summary.md
[/code]

المخرجات مفصولة بعلامات تبويب. الأعمدة هي المحدد، ووقت البدء، والعنوان، ومسار الملخص. المحدد هو القيمة الأكثر أمانًا لتمريرها مرة أخرى إلى `show` أو `path`.

يطبع `list --json` كائنات تتضمن:

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


يعيد `show --json` بيانات تعريف الجلسة المخزنة، والمحدد، ودليل الجلسة، ومسار الملخص، ونص ملخص Markdown. يعيد `path --json` المسار المحدد وما إذا كان ذلك الملف موجودًا.

## اجتماعات كثيرة في اليوم

تجمع Transcripts الجلسات حسب التاريخ، ثم حسب معرف الجلسة. تصبح عشرة اجتماعات في يوم واحد عشرة مجلدات شقيقة:

textCopy code
[code]
    ~/.openclaw/transcripts/2026-05-22/  transcript-2026-05-22T09-00-00-000Z-a1b2c3d4/  transcript-2026-05-22T10-30-00-000Z-b2c3d4e5/  standup/
[/code]

استخدم المعرفات الافتراضية المولدة لمعظم الأتمتة. استخدم معرفًا ثابتًا مثل `standup` فقط عندما لن يُستخدم المعرف نفسه مرتين في التاريخ نفسه.

## الملخصات المفقودة

تكتب الجلسات الحية `summary.md` عند توقف الجلسة. تكتب النصوص المستوردة `summary.md` مباشرة بعد الاستيراد. قد تظل الجلسة تظهر في `list` بدون ملخص عندما يكون الالتقاط نشطًا، أو يفشل مزود أثناء الإيقاف، أو تُكتب بيانات التعريف قبل وصول أي أقوال.

استخدم `path <session> --transcript` لفحص النص الملحق فقط، واستخدم إجراء أداة `transcripts` المسمى `summarize` لإعادة إنشاء ملخص Markdown.

## التكوين

التقاط النصوص اختياري لأن المصادر الحية يمكنها الانضمام إلى صوت الاجتماع وتسجيله. فعّل الأداة باستخدام `transcripts.enabled` في المستوى الأعلى:

jsonCopy code
[code]
    {  "transcripts": {    "enabled": true,    "maxUtterances": 2000  }}
[/code]

كوّن مصادر البدء التلقائي باستخدام `transcripts.autoStart` في `openclaw.json`. يُفعّل كل إدخال بمجرد وجوده؛ احذف إدخالًا لتعطيل ذلك المصدر.

jsonCopy code
[code]
    {  "transcripts": {    "enabled": true,    "autoStart": [      {        "providerId": "discord-voice",        "guildId": "1234567890",        "channelId": "2345678901"      },      {        "providerId": "slack-huddle",        "accountId": "workspace",        "channelId": "C123"      }    ]  }}
[/code]

Was this useful?YesNo

Open issue