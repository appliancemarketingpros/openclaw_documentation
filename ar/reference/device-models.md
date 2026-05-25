---
title: قاعدة بيانات طرازات الأجهزة
source_url: https://docs.openclaw.ai/ar/reference/device-models
scraped_at: 2026-05-25
---

يعرض التطبيق المساعد على macOS أسماءً ودية لطرازات أجهزة Apple في واجهة مستخدم **Instances** من خلال تعيين معرّفات طرازات Apple (مثل `iPad16,6` و`Mac16,6`) إلى أسماء مقروءة للبشر.

يتم تضمين هذا التعيين كبنية JSON ضمن:

  * `apps/macos/Sources/OpenClaw/Resources/DeviceModels/`


## مصدر البيانات

نقوم حاليًا بتضمين التعيين من المستودع المرخّص بترخيص MIT التالي:

  * `kyle-seongwoo-jun/apple-device-identifiers`


وللحفاظ على حتمية الإصدارات، يتم تثبيت ملفات JSON على عمليات التزام upstream محددة (مُسجّلة في `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`).

## تحديث قاعدة البيانات

  1. اختر عمليات التزام upstream التي تريد تثبيتها (واحدة لـ iOS وواحدة لـ macOS).
  2. حدّث تجزئات عمليات الالتزام في `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`.
  3. أعد تنزيل ملفات JSON مع تثبيتها على تلك العمليات:

bashCopy code
[code]
    IOS_COMMIT="<commit sha for ios-device-identifiers.json>"MAC_COMMIT="<commit sha for mac-device-identifiers.json>" curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${IOS_COMMIT}/ios-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/ios-device-identifiers.json curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${MAC_COMMIT}/mac-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/mac-device-identifiers.json
[/code]

  4. تأكد من أن `apps/macos/Sources/OpenClaw/Resources/DeviceModels/LICENSE.apple-device-identifiers.txt` لا يزال مطابقًا لـ upstream (واستبدله إذا تغيّر ترخيص upstream).
  5. تحقّق من أن تطبيق macOS يُبنى بشكل نظيف (من دون تحذيرات):

bashCopy code
[code]
    swift build --package-path apps/macos
[/code]

## ذو صلة

  * [Nodes](</ar/nodes>)
  * [استكشاف أخطاء Node وإصلاحها](</ar/nodes/troubleshooting>)


Was this useful?YesNo