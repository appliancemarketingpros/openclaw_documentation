---
title: الترحيل من Hermes
source_url: https://docs.openclaw.ai/ar/install/migrating-hermes
scraped_at: 2026-05-25
---

تستورد OpenClaw حالة Hermes عبر مزوّد ترحيل مضمّن. يعاين المزوّد كل شيء قبل تغيير الحالة، وينقّح الأسرار في الخطط والتقارير، وينشئ نسخة احتياطية متحقَّقًا منها قبل التطبيق.

## طريقتان للاستيراد

### معالج الإعداد الأولي

المسار الأسرع. يكتشف المعالج Hermes في `~/.hermes` ويعرض معاينة قبل التطبيق.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

أو وجّهه إلى مصدر محدد:

bashCopy code
[code]
    openclaw onboard --import-from hermes --import-source ~/.hermes
[/code]

### CLI

استخدم `openclaw migrate` للتشغيلات النصية أو القابلة للتكرار. راجع [`openclaw migrate`](</ar/cli/migrate>) للمرجع الكامل.

bashCopy code
[code]
    openclaw migrate hermes --dry-run    # preview onlyopenclaw migrate apply hermes --yes  # apply with confirmation skipped
[/code]

أضف `--from <path>` عندما يكون Hermes خارج `~/.hermes`.

## ما يتم استيراده

إعداد النموذج

  * اختيار النموذج الافتراضي من `config.yaml` في Hermes.
  * مزوّدو النماذج المكوّنون ونقاط النهاية المخصصة المتوافقة مع OpenAI من `providers` و`custom_providers`.

خوادم MCP

تعريفات خوادم MCP من `mcp_servers` أو `mcp.servers`.

ملفات مساحة العمل

  * يتم نسخ `SOUL.md` و`AGENTS.md` إلى مساحة عمل وكيل OpenClaw.
  * يتم **إلحاق** `memories/MEMORY.md` و`memories/USER.md` بملفات ذاكرة OpenClaw المطابقة بدلًا من استبدالها.

إعداد الذاكرة

الإعدادات الافتراضية لتكوين الذاكرة لذاكرة ملفات OpenClaw. يتم تسجيل مزوّدي الذاكرة الخارجيين مثل Honcho كعناصر أرشيف أو مراجعة يدوية حتى تتمكن من نقلها بعناية.

Skills

يتم نسخ Skills التي تحتوي على ملف `SKILL.md` ضمن `skills/<name>/`، مع قيم الإعداد لكل Skill من `skills.config`.

مفاتيح API (اختياري)

عيّن `--include-secrets` لاستيراد مفاتيح `.env` المدعومة: `OPENAI_API_KEY`، `ANTHROPIC_API_KEY`، `OPENROUTER_API_KEY`، `GOOGLE_API_KEY`، `GEMINI_API_KEY`، `GROQ_API_KEY`، `XAI_API_KEY`، `MISTRAL_API_KEY`، `DEEPSEEK_API_KEY`. بدون هذا العلم، لا يتم نسخ الأسرار أبدًا.

## ما يبقى للأرشيف فقط

ينسخ المزوّد هذه العناصر إلى دليل تقرير الترحيل للمراجعة اليدوية، لكنه **لا** يحمّلها في إعدادات OpenClaw الحية أو بيانات الاعتماد:

  * `plugins/`
  * `sessions/`
  * `logs/`
  * `cron/`
  * `mcp-tokens/`
  * `auth.json`
  * `state.db`


ترفض OpenClaw تنفيذ هذه الحالة أو الوثوق بها تلقائيًا لأن التنسيقات وافتراضات الثقة يمكن أن تختلف بين الأنظمة. انقل ما تحتاج إليه يدويًا بعد مراجعة الأرشيف.

## التدفق الموصى به

* ### عاين الخطة

bashCopy code
[code]
    openclaw migrate hermes --dry-run
[/code]

تسرد الخطة كل ما سيتغير، بما في ذلك التعارضات والعناصر المتخطاة وأي عناصر حساسة. ينقّح إخراج الخطة المفاتيح المتداخلة التي تبدو كأسرار.

* ### طبّق مع نسخة احتياطية

bashCopy code
[code]
    openclaw migrate apply hermes --yes
[/code]

تنشئ OpenClaw نسخة احتياطية وتتحقق منها قبل التطبيق. إذا كنت تحتاج إلى استيراد مفاتيح API، فأضف `--include-secrets`.

* ### شغّل Doctor

bashCopy code
[code]
    openclaw doctor
[/code]

يعيد [Doctor](</ar/gateway/doctor>) تطبيق أي عمليات ترحيل إعدادات معلقة ويفحص المشكلات التي أُدخلت أثناء الاستيراد.

* ### أعد التشغيل وتحقق

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

تأكد من أن Gateway سليم وأن النموذج والذاكرة وSkills المستوردة قد تم تحميلها.

## معالجة التعارضات

يرفض التطبيق المتابعة عندما تبلغ الخطة عن تعارضات (ملف أو قيمة إعدادات موجودة بالفعل في الهدف).

في تثبيت OpenClaw جديد، تكون التعارضات غير معتادة. تظهر عادةً عندما تعيد تشغيل الاستيراد على إعداد يحتوي بالفعل على تعديلات من المستخدم.

إذا ظهر تعارض أثناء التطبيق (على سبيل المثال، تسابق غير متوقع على ملف إعدادات)، يضع Hermes علامة `skipped` على عناصر الإعدادات التابعة المتبقية مع السبب `blocked by earlier apply conflict` بدلًا من كتابتها جزئيًا. يسجل تقرير الترحيل كل عنصر محظور حتى تتمكن من حل التعارض الأصلي وإعادة تشغيل الاستيراد.

## الأسرار

لا يتم استيراد الأسرار افتراضيًا أبدًا.

  * شغّل `openclaw migrate apply hermes --yes` أولًا لاستيراد الحالة غير السرية.
  * إذا كنت تريد أيضًا نسخ مفاتيح `.env` المدعومة، فأعد التشغيل مع `--include-secrets`.
  * بالنسبة إلى بيانات الاعتماد المُدارة عبر SecretRef، كوّن مصدر SecretRef بعد اكتمال الاستيراد.


## إخراج JSON للأتمتة

bashCopy code
[code]
    openclaw migrate hermes --dry-run --jsonopenclaw migrate apply hermes --json --yes
[/code]

مع `--json` وبدون `--yes`، يطبع التطبيق الخطة ولا يغيّر الحالة. هذا هو الوضع الأكثر أمانًا لـ CI والنصوص المشتركة.

## استكشاف الأخطاء وإصلاحها

يرفض التطبيق بسبب تعارضات

افحص إخراج الخطة. يحدد كل تعارض مسار المصدر والهدف الحالي. قرر لكل عنصر ما إذا كنت ستتخطاه، أو تعدّل الهدف، أو تعيد التشغيل مع `--overwrite`.

يوجد Hermes خارج ~/.hermes

مرّر `--from /actual/path` ‏(CLI) أو `--import-source /actual/path` (الإعداد الأولي).

يرفض الإعداد الأولي الاستيراد على إعداد موجود

تتطلب عمليات استيراد الإعداد الأولي إعدادًا جديدًا. إما أن تعيد ضبط الحالة وتعيد الإعداد الأولي، أو تستخدم `openclaw migrate apply hermes` مباشرةً، فهو يدعم `--overwrite` والتحكم الصريح في النسخ الاحتياطي.

لم يتم استيراد مفاتيح API

`--include-secrets` مطلوب، ولا يتم التعرف إلا على المفاتيح المذكورة أعلاه. يتم تجاهل المتغيرات الأخرى في `.env`.

## ذو صلة

  * [`openclaw migrate`](</ar/cli/migrate>): مرجع CLI الكامل، وعقد Plugin، وأشكال JSON.
  * [الإعداد الأولي](</ar/cli/onboard>): تدفق المعالج والأعلام غير التفاعلية.
  * [الترحيل](</ar/install/migrating>): نقل تثبيت OpenClaw بين الأجهزة.
  * [Doctor](</ar/gateway/doctor>): فحص السلامة بعد الترحيل.
  * [مساحة عمل الوكيل](</ar/concepts/agent-workspace>): مكان وجود `SOUL.md` و`AGENTS.md` وملفات الذاكرة.


Was this useful?YesNo