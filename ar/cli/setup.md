---
title: الإعداد
source_url: https://docs.openclaw.ai/ar/cli/setup
scraped_at: 2026-05-25
---

# `openclaw setup`

هيّئ التكوين الأساسي ومساحة عمل الوكيل. عند وجود أي علامة للتهيئة الأولية، يشغّل المعالج أيضًا.

## الخيارات

العلامة | الوصف  
---|---  
`--workspace <dir>` | دليل مساحة عمل الوكيل (الافتراضي `~/.openclaw/workspace`؛ يُخزّن باسم `agents.defaults.workspace`).  
`--wizard` | تشغيل التهيئة الأولية التفاعلية.  
`--non-interactive` | تشغيل التهيئة الأولية دون مطالبات.  
`--mode <mode>` | وضع التهيئة الأولية: `local` أو `remote`.  
`--import-from <provider>` | موفر الترحيل المراد تشغيله أثناء التهيئة الأولية.  
`--import-source <path>` | موطن وكيل المصدر لـ `--import-from`.  
`--import-secrets` | استيراد الأسرار المدعومة أثناء ترحيل التهيئة الأولية.  
`--remote-url <url>` | عنوان URL لـ WebSocket الخاص بـ Gateway البعيد.  
`--remote-token <token>` | رمز Gateway البعيد (اختياري).  
  
### التشغيل التلقائي للمعالج

يشغّل `openclaw setup` المعالج عند وجود أي من هذه العلامات صراحةً، حتى من دون `--wizard`:

`--wizard`, `--non-interactive`, `--mode`, `--import-from`, `--import-source`, `--import-secrets`, `--remote-url`, `--remote-token`.

## أمثلة

bashCopy code
[code]
    openclaw setupopenclaw setup --workspace ~/.openclaw/workspaceopenclaw setup --wizardopenclaw setup --wizard --import-from hermes --import-source ~/.hermesopenclaw setup --non-interactive --mode remote --remote-url wss://gateway-host:18789 --remote-token <token>
[/code]

## ملاحظات

  * يقوم `openclaw setup` العادي بتهيئة التكوين ومساحة العمل دون تشغيل مسار التهيئة الأولية الكامل.
  * بعد الإعداد العادي، شغّل `openclaw onboard` للرحلة الإرشادية الكاملة، أو `openclaw configure` للتغييرات المحددة، أو `openclaw channels add` لإضافة حسابات القنوات.
  * إذا اكتُشفت حالة Hermes، يمكن للتهيئة الأولية التفاعلية أن تعرض الترحيل تلقائيًا. يتطلب استيراد التهيئة الأولية إعدادًا جديدًا؛ استخدم [الترحيل](</ar/cli/migrate>) لخطط التشغيل التجريبي، والنسخ الاحتياطية، ووضع الاستبدال خارج التهيئة الأولية.


## ذو صلة

  * [مرجع CLI](</ar/cli>)
  * [التهيئة الأولية (CLI)](</ar/start/wizard>)
  * [بدء الاستخدام](</ar/start/getting-started>)
  * [نظرة عامة على التثبيت](</ar/install>)


Was this useful?YesNo