---
title: التقاط الصور بالكاميرا
source_url: https://docs.openclaw.ai/ar/nodes/camera
scraped_at: 2026-05-25
---

يدعم OpenClaw **التقاط الكاميرا** لتدفقات عمل الوكيل:

  * **عقدة iOS** (مقترنة عبر Gateway): التقاط **صورة** (`jpg`) أو **مقطع فيديو قصير** (`mp4`، مع صوت اختياري) عبر `node.invoke`.
  * **عقدة Android** (مقترنة عبر Gateway): التقاط **صورة** (`jpg`) أو **مقطع فيديو قصير** (`mp4`، مع صوت اختياري) عبر `node.invoke`.
  * **تطبيق macOS** (عقدة عبر Gateway): التقاط **صورة** (`jpg`) أو **مقطع فيديو قصير** (`mp4`، مع صوت اختياري) عبر `node.invoke`.


كل وصول إلى الكاميرا مقيّد خلف **إعدادات يتحكم بها المستخدم**.

## عقدة iOS

### إعداد المستخدم (مفعّل افتراضيًا)

  * تبويب إعدادات iOS → **الكاميرا** → **السماح بالكاميرا** (`camera.enabled`) 
    * الافتراضي: **مفعّل** (يُعامل المفتاح المفقود على أنه مفعّل).
    * عند التعطيل: تعيد أوامر `camera.*` القيمة `CAMERA_DISABLED`.


### الأوامر (عبر Gateway `node.invoke`)

  * `camera.list`

    * حمولة الاستجابة: 
      * `devices`: مصفوفة من `{ id, name, position, deviceType }`
  * `camera.snap`

    * المعاملات: 
      * `facing`: `front|back` (الافتراضي: `front`)
      * `maxWidth`: رقم (اختياري؛ الافتراضي `1600` على عقدة iOS)
      * `quality`: `0..1` (اختياري؛ الافتراضي `0.9`)
      * `format`: حاليًا `jpg`
      * `delayMs`: رقم (اختياري؛ الافتراضي `0`)
      * `deviceId`: سلسلة نصية (اختياري؛ من `camera.list`)
    * حمولة الاستجابة: 
      * `format: "jpg"`
      * `base64: "<...>"`
      * `width`, `height`
    * حارس الحمولة: يُعاد ضغط الصور لإبقاء حمولة base64 دون 5 ميجابايت.
  * `camera.clip`

    * المعاملات: 
      * `facing`: `front|back` (الافتراضي: `front`)
      * `durationMs`: رقم (الافتراضي `3000`، ومحدّد بحد أقصى `60000`)
      * `includeAudio`: قيمة منطقية (الافتراضي `true`)
      * `format`: حاليًا `mp4`
      * `deviceId`: سلسلة نصية (اختياري؛ من `camera.list`)
    * حمولة الاستجابة: 
      * `format: "mp4"`
      * `base64: "<...>"`
      * `durationMs`
      * `hasAudio`


### متطلب العمل في الواجهة

مثل `canvas.*`، تسمح عقدة iOS بأوامر `camera.*` فقط في **الواجهة**. تعيد الاستدعاءات في الخلفية `NODE_BACKGROUND_UNAVAILABLE`.

### مساعد CLI (ملفات مؤقتة + MEDIA)

أسهل طريقة للحصول على المرفقات هي عبر مساعد CLI، الذي يكتب الوسائط المفككة إلى ملف مؤقت ويطبع `MEDIA:<path>`.

أمثلة:

bashCopy code
[code]
    openclaw nodes camera snap --node <id>               # default: both front + back (2 MEDIA lines)openclaw nodes camera snap --node <id> --facing frontopenclaw nodes camera clip --node <id> --duration 3000openclaw nodes camera clip --node <id> --no-audio
[/code]

ملاحظات:

  * يكون `nodes camera snap` افتراضيًا على **كلتا** الجهتين لتزويد الوكيل بكلتا الرؤيتين.
  * تكون ملفات الإخراج مؤقتة (في دليل الملفات المؤقتة لنظام التشغيل) ما لم تُنشئ الغلاف الخاص بك.


## عقدة Android

### إعداد مستخدم Android (مفعّل افتراضيًا)

  * ورقة إعدادات Android → **الكاميرا** → **السماح بالكاميرا** (`camera.enabled`) 
    * الافتراضي: **مفعّل** (يُعامل المفتاح المفقود على أنه مفعّل).
    * عند التعطيل: تعيد أوامر `camera.*` القيمة `CAMERA_DISABLED`.


### الأذونات

  * يتطلب Android أذونات وقت التشغيل: 
    * `CAMERA` لكل من `camera.snap` و`camera.clip`.
    * `RECORD_AUDIO` لـ `camera.clip` عندما تكون `includeAudio=true`.


إذا كانت الأذونات مفقودة، فسيعرض التطبيق مطالبة عندما يكون ذلك ممكنًا؛ وإذا رُفضت، تفشل طلبات `camera.*` بخطأ `*_PERMISSION_REQUIRED`.

### متطلب العمل في واجهة Android

مثل `canvas.*`، تسمح عقدة Android بأوامر `camera.*` فقط في **الواجهة**. تعيد الاستدعاءات في الخلفية `NODE_BACKGROUND_UNAVAILABLE`.

### أوامر Android (عبر Gateway `node.invoke`)

  * `camera.list`
    * حمولة الاستجابة: 
      * `devices`: مصفوفة من `{ id, name, position, deviceType }`


### حارس الحمولة

يُعاد ضغط الصور لإبقاء حمولة base64 دون 5 ميجابايت.

## تطبيق macOS

### إعداد المستخدم (معطّل افتراضيًا)

يعرض تطبيق macOS المرافق مربع اختيار:

  * **الإعدادات → عام → السماح بالكاميرا** (`openclaw.cameraEnabled`) 
    * الافتراضي: **معطّل**
    * عند التعطيل: تعيد طلبات الكاميرا "عطّل المستخدم الكاميرا".


### مساعد CLI (استدعاء العقدة)

استخدم CLI الرئيسي لـ `openclaw` لاستدعاء أوامر الكاميرا على عقدة macOS.

أمثلة:

bashCopy code
[code]
    openclaw nodes camera list --node <id>            # list camera idsopenclaw nodes camera snap --node <id>            # prints MEDIA:<path>openclaw nodes camera snap --node <id> --max-width 1280openclaw nodes camera snap --node <id> --delay-ms 2000openclaw nodes camera snap --node <id> --device-id <id>openclaw nodes camera clip --node <id> --duration 10s          # prints MEDIA:<path>openclaw nodes camera clip --node <id> --duration-ms 3000      # prints MEDIA:<path> (legacy flag)openclaw nodes camera clip --node <id> --device-id <id>openclaw nodes camera clip --node <id> --no-audio
[/code]

ملاحظات:

  * يكون `openclaw nodes camera snap` افتراضيًا على `maxWidth=1600` ما لم يتم تجاوزه.
  * على macOS، ينتظر `camera.snap` مدة `delayMs` (الافتراضي 2000ms) بعد الاستعداد واستقرار التعريض قبل الالتقاط.
  * يُعاد ضغط حمولات الصور لإبقاء base64 دون 5 ميجابايت.


## السلامة + الحدود العملية

  * يؤدي الوصول إلى الكاميرا والميكروفون إلى ظهور مطالبات أذونات نظام التشغيل المعتادة (ويتطلب سلاسل استخدام في Info.plist).
  * تُحدَّد مقاطع الفيديو بحد أقصى (حاليًا `<= 60s`) لتجنب حمولات العقدة كبيرة الحجم (زيادة base64 + حدود الرسائل).


## فيديو شاشة macOS (على مستوى نظام التشغيل)

لفيديو _الشاشة_ (وليس الكاميرا)، استخدم تطبيق macOS المرافق:

bashCopy code
[code]
    openclaw nodes screen record --node <id> --duration 10s --fps 15   # prints MEDIA:<path>
[/code]

ملاحظات:

  * يتطلب إذن **تسجيل الشاشة** في macOS (TCC).


## ذو صلة

  * [دعم الصور والوسائط](</ar/nodes/images>)
  * [فهم الوسائط](</ar/nodes/media-understanding>)
  * [أمر الموقع](</ar/nodes/location-command>)


Was this useful?YesNo