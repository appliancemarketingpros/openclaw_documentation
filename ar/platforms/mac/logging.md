---
title: تسجيل السجلات في macOS
source_url: https://docs.openclaw.ai/ar/platforms/mac/logging
scraped_at: 2026-05-25
---

# التسجيل (macOS)

## سجل ملف تشخيصات متناوب (لوحة التصحيح)

يوجّه OpenClaw سجلات تطبيق macOS عبر swift-log (التسجيل الموحّد افتراضيًا) ويمكنه كتابة سجل ملف محلي متناوب إلى القرص عندما تحتاج إلى التقاط دائم.

  * مستوى التفصيل: **لوحة التصحيح → السجلات → تسجيل التطبيق → مستوى التفصيل**
  * التفعيل: **لوحة التصحيح → السجلات → تسجيل التطبيق → "كتابة سجل تشخيصات متناوب (JSONL)"**
  * الموقع: `~/Library/Logs/OpenClaw/diagnostics.jsonl` (يتناوب تلقائيًا؛ تُضاف إلى الملفات القديمة لواحق مثل `.1` و`.2` و…)
  * المسح: **لوحة التصحيح → السجلات → تسجيل التطبيق → "مسح"**


ملاحظات:

  * هذا **معطّل افتراضيًا**. فعّله فقط أثناء التصحيح النشط.
  * تعامل مع الملف على أنه حساس؛ لا تشاركه دون مراجعته.


## البيانات الخاصة في التسجيل الموحّد على macOS

يحجب التسجيل الموحّد معظم الحمولات ما لم يختر نظام فرعي استخدام `privacy -off`. وفقًا لمقالة Peter عن [حيل خصوصية التسجيل](<https://steipete.me/posts/2025/logging-privacy-shenanigans>) في macOS (2025)، يتم التحكم في ذلك بواسطة plist في `/Library/Preferences/Logging/Subsystems/` keyed by the subsystem name. تلتقط إدخالات السجل الجديدة فقط العلامة، لذا فعّلها قبل إعادة إنتاج مشكلة.

## التفعيل لـ OpenClaw (`ai.openclaw`)

  * اكتب plist إلى ملف مؤقت أولًا، ثم ثبّته ذريًا كجذر:

bashCopy code
[code]
    cat <<'EOF' >/tmp/ai.openclaw.plist<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>    <key>DEFAULT-OPTIONS</key>    <dict>        <key>Enable-Private-Data</key>        <true/>    </dict></dict></plist>EOFsudo install -m 644 -o root -g wheel /tmp/ai.openclaw.plist /Library/Preferences/Logging/Subsystems/ai.openclaw.plist
[/code]

  * لا يلزم إعادة التشغيل؛ يلاحظ logd الملف بسرعة، لكن أسطر السجل الجديدة فقط ستتضمن الحمولات الخاصة.
  * اعرض المخرجات الأغنى باستخدام المساعد الموجود، مثل `./scripts/clawlog.sh --category WebChat --last 5m`.


## التعطيل بعد التصحيح

  * أزل التجاوز: `sudo rm /Library/Preferences/Logging/Subsystems/ai.openclaw.plist`.
  * اختياريًا، شغّل `sudo log config --reload` لإجبار logd على إسقاط التجاوز فورًا.
  * تذكّر أن هذا السطح يمكن أن يتضمن أرقام هواتف ومحتويات رسائل؛ أبقِ plist في مكانه فقط أثناء حاجتك النشطة إلى التفاصيل الإضافية.


## ذو صلة

  * [تطبيق macOS](</ar/platforms/macos>)
  * [تسجيل Gateway](</ar/gateway/logging>)


Was this useful?YesNo