---
title: Northflank
source_url: https://docs.openclaw.ai/ar/install/northflank
scraped_at: 2026-05-25
---

# Northflank

انشر OpenClaw على Northflank باستخدام قالب بنقرة واحدة وادخل إليه عبر واجهة Control UI على الويب. هذا هو أسهل مسار "من دون طرفية على الخادم": إذ يقوم Northflank بتشغيل Gateway نيابةً عنك.

## كيفية البدء

  1. انقر [Deploy OpenClaw](<https://northflank.com/stacks/deploy-openclaw>) لفتح القالب.
  2. أنشئ [حسابًا على Northflank](<https://app.northflank.com/signup>) إذا لم يكن لديك حساب بالفعل.
  3. انقر **Deploy OpenClaw now**.
  4. اضبط متغير البيئة المطلوب: `OPENCLAW_GATEWAY_TOKEN` (استخدم قيمة عشوائية قوية).
  5. انقر **Deploy stack** لبناء قالب OpenClaw وتشغيله.
  6. انتظر حتى يكتمل النشر، ثم انقر **View resources**.
  7. افتح خدمة OpenClaw.
  8. افتح عنوان URL العام الخاص بـ OpenClaw عند المسار `/openclaw` واتصل باستخدام السر المشترك المضبوط. يستخدم هذا القالب القيمة `OPENCLAW_GATEWAY_TOKEN` افتراضيًا؛ وإذا استبدلتها بمصادقة كلمة المرور، فاستخدم كلمة المرور تلك بدلًا منها.


## ما الذي تحصل عليه

  * Gateway مستضاف لـ OpenClaw + Control UI
  * تخزين دائم عبر Northflank Volume ‏(`/data`) بحيث تبقى `openclaw.json`، و`auth-profiles.json` لكل وكيل، وحالة القنوات/المزوّدات، والجلسات، ومساحة العمل محفوظة عبر عمليات إعادة النشر


## توصيل قناة

استخدم Control UI عند `/openclaw` أو شغّل `openclaw onboard` عبر SSH للحصول على تعليمات إعداد القنوات:

  * [Telegram](</ar/channels/telegram>) (الأسرع — يحتاج فقط إلى رمز روبوت)
  * [Discord](</ar/channels/discord>)
  * [جميع القنوات](</ar/channels>)


## الخطوات التالية

  * إعداد قنوات المراسلة: [القنوات](</ar/channels>)
  * إعداد Gateway: [إعداد Gateway](</ar/gateway/configuration>)
  * إبقاء OpenClaw محدّثًا: [التحديث](</ar/install/updating>)


Was this useful?YesNo