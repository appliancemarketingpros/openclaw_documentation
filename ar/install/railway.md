---
title: Railway
source_url: https://docs.openclaw.ai/ar/install/railway
scraped_at: 2026-05-25
---

# Railway

انشر OpenClaw على Railway باستخدام قالب بنقرة واحدة وادخل إليه عبر Control UI على الويب. هذا هو أسهل مسار "من دون طرفية على الخادم": حيث يشغّل Railway الـ Gateway نيابةً عنك.

## قائمة تحقق سريعة (للمستخدمين الجدد)

  1. انقر **Deploy on Railway** (أدناه).
  2. أضف **Volume** مُثبتًا عند `/data`.
  3. اضبط **Variables** المطلوبة (على الأقل `OPENCLAW_GATEWAY_PORT` و`OPENCLAW_GATEWAY_TOKEN`).
  4. فعّل **HTTP Proxy** على المنفذ `8080`.
  5. افتح `https://<your-railway-domain>/openclaw` واتصل باستخدام السر المشترك المهيأ. يستخدم هذا القالب `OPENCLAW_GATEWAY_TOKEN` افتراضيًا؛ وإذا استبدلته بمصادقة كلمة مرور، فاستخدم كلمة المرور تلك بدلًا منه.


## نشر بنقرة واحدة

[ Deploy on Railway ](<https://railway.com/deploy/clawdbot-railway-template>)

بعد النشر، اعثر على عنوان URL العام الخاص بك في **Railway ← خدمتك ← Settings ← Domains**.

سيقوم Railway إما بما يلي:

  * يمنحك نطاقًا مُنشأً تلقائيًا (غالبًا `https://<something>.up.railway.app`)، أو
  * يستخدم نطاقك المخصص إذا قمت بإرفاق واحد.


ثم افتح:

  * `https://<your-railway-domain>/openclaw` — Control UI


## ما الذي تحصل عليه

  * OpenClaw Gateway + Control UI مستضافان
  * تخزين دائم عبر Railway Volume (`/data`) بحيث تستمر ملفات `openclaw.json`، وملفات `auth-profiles.json` لكل وكيل، وحالة القنوات/المزوّدين، والجلسات، ومساحة العمل بعد إعادة النشر


## إعدادات Railway المطلوبة

### الشبكات العامة

فعّل **HTTP Proxy** للخدمة.

  * المنفذ: `8080`


### Volume (مطلوب)

أرفق volume مثبّتًا عند:

  * `/data`


### Variables

اضبط هذه المتغيرات على الخدمة:

  * `OPENCLAW_GATEWAY_PORT=8080` (مطلوب — يجب أن يطابق المنفذ في Public Networking)
  * `OPENCLAW_GATEWAY_TOKEN` (مطلوب؛ تعامل معه كسر إداري)
  * `OPENCLAW_STATE_DIR=/data/.openclaw` (موصى به)
  * `OPENCLAW_WORKSPACE_DIR=/data/workspace` (موصى به)


## توصيل قناة

استخدم Control UI عند `/openclaw` أو شغّل `openclaw onboard` عبر shell الخاص بـ Railway للحصول على تعليمات إعداد القنوات:

  * [Telegram](</ar/channels/telegram>) (الأسرع — فقط رمز بوت)
  * [Discord](</ar/channels/discord>)
  * [كل القنوات](</ar/channels>)


## النسخ الاحتياطية والترحيل

صدّر الحالة والإعدادات وملفات تعريف المصادقة ومساحة العمل:

bashCopy code
[code]
    openclaw backup create
[/code]

يؤدي هذا إلى إنشاء أرشيف نسخ احتياطي قابل للنقل يحتوي على حالة OpenClaw بالإضافة إلى أي مساحة عمل مهيأة. راجع [Backup](</ar/cli/backup>) للتفاصيل.

## الخطوات التالية

  * اضبط قنوات المراسلة: [القنوات](</ar/channels>)
  * اضبط Gateway: [إعدادات Gateway](</ar/gateway/configuration>)
  * حافظ على تحديث OpenClaw: [التحديث](</ar/install/updating>)


Was this useful?YesNo