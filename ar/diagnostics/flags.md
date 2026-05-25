---
title: علامات التشخيص
source_url: https://docs.openclaw.ai/ar/diagnostics/flags
scraped_at: 2026-05-25
---

تتيح لك علامات التشخيص تمكين سجلات تصحيح أخطاء موجّهة دون تشغيل التسجيل المطوّل في كل مكان. العلامات اختيارية ولا يكون لها أي تأثير إلا إذا تحقّق منها نظام فرعي.

## كيفية العمل

  * العلامات سلاسل نصية (غير حساسة لحالة الأحرف).
  * يمكنك تمكين العلامات في التكوين أو عبر تجاوز متغير بيئة.
  * أحرف البدل مدعومة: 
    * `telegram.*` يطابق `telegram.http`
    * `*` يمكّن كل العلامات


## التمكين عبر التكوين

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http"]  }}
[/code]

علامات متعددة:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http", "brave.http", "gateway.*"]  }}
[/code]

أعد تشغيل Gateway بعد تغيير العلامات.

## تجاوز متغير البيئة (لمرة واحدة)

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=telegram.http,telegram.payload
[/code]

تعطيل كل العلامات:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=0
[/code]

## آثار المخطط الزمني

تكتب علامة `timeline` أحداث توقيت منظمة لبدء التشغيل ووقت التشغيل من أجل حزم اختبار QA الخارجية:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=timeline \OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=/tmp/openclaw-timeline.jsonl \openclaw gateway run
[/code]

يمكنك أيضًا تمكينها في التكوين:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["timeline"]  }}
[/code]

لا يزال مسار ملف المخطط الزمني يأتي من `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH`. عند تمكين `timeline` من التكوين فقط، لا تُصدر أقدم نطاقات تحميل التكوين لأن OpenClaw لم يكن قد قرأ التكوين بعد؛ وتستخدم نطاقات بدء التشغيل اللاحقة علامة التكوين.

تؤدي `OPENCLAW_DIAGNOSTICS=1` و`OPENCLAW_DIAGNOSTICS=all` و `OPENCLAW_DIAGNOSTICS=*` أيضًا إلى تمكين المخطط الزمني لأنها تمكّن كل علامات التشخيص. فضّل `timeline` عندما لا تريد إلا أثر توقيت JSONL.

تستخدم سجلات المخطط الزمني غلاف `openclaw.diagnostics.v1`. يمكن أن تتضمن الأحداث معرّفات العمليات، وأسماء المراحل، وأسماء النطاقات، والمدد، ومعرّفات plugins، وأعداد التبعيات، وعينات تأخير حلقة الأحداث، وأسماء عمليات المزوّدين، وحالة خروج العمليات الفرعية، وأسماء/رسائل أخطاء بدء التشغيل. تعامل مع ملفات المخطط الزمني باعتبارها آثار تشخيص محلية؛ راجعها قبل مشاركتها خارج جهازك.

## أين تذهب السجلات

تُصدر العلامات السجلات إلى ملف سجل التشخيص القياسي. افتراضيًا:

CodeCopy code
[code]
    /tmp/openclaw/openclaw-YYYY-MM-DD.log
[/code]

إذا عيّنت `logging.file`، فاستخدم ذلك المسار بدلًا من ذلك. السجلات بتنسيق JSONL (كائن JSON واحد في كل سطر). لا يزال التنقيح مطبّقًا بناءً على `logging.redactSensitive`.

## استخراج السجلات

اختر أحدث ملف سجل:

bashCopy code
[code]
    ls -t /tmp/openclaw/openclaw-*.log | head -n 1
[/code]

صفِّ تشخيصات HTTP الخاصة بـTelegram:

bashCopy code
[code]
    rg "telegram http error" /tmp/openclaw/openclaw-*.log
[/code]

صفِّ تشخيصات HTTP الخاصة بـBrave Search:

bashCopy code
[code]
    rg "brave http" /tmp/openclaw/openclaw-*.log
[/code]

أو تابع السجل أثناء إعادة الإنتاج:

bashCopy code
[code]
    tail -f /tmp/openclaw/openclaw-$(date +%F).log | rg "telegram http error"
[/code]

بالنسبة إلى حالات Gateway البعيدة، يمكنك أيضًا استخدام `openclaw logs --follow` (راجع [/cli/logs](</ar/cli/logs>)).

## ملاحظات

  * إذا كان `logging.level` مضبوطًا على مستوى أعلى من `warn`، فقد تُحجب هذه السجلات. القيمة الافتراضية `info` مناسبة.
  * تسجّل `brave.http` عناوين URL/معلمات الاستعلام لطلبات Brave Search، وحالة/توقيت الاستجابة، وأحداث إصابة/إخفاق/كتابة ذاكرة التخزين المؤقت. لا تسجّل مفاتيح API أو أجسام الاستجابات، لكن استعلامات البحث قد تكون حساسة.
  * من الآمن ترك العلامات ممكّنة؛ فهي تؤثر فقط في حجم السجلات للنظام الفرعي المحدد.
  * استخدم [/logging](</ar/logging>) لتغيير وجهات السجلات ومستوياتها والتنقيح.


## ذو صلة

  * [تشخيصات Gateway](</ar/gateway/diagnostics>)
  * [استكشاف أخطاء Gateway وإصلاحها](</ar/gateway/troubleshooting>)


Was this useful?YesNo