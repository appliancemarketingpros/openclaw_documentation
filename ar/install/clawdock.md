---
title: ClawDock
source_url: https://docs.openclaw.ai/ar/install/clawdock
scraped_at: 2026-05-25
---

ClawDock هي طبقة صغيرة من مساعدات الصدفة لتثبيتات OpenClaw المعتمدة على Docker.

تمنحك أوامر قصيرة مثل `clawdock-start` و`clawdock-dashboard` و`clawdock-fix-token` بدلاً من استدعاءات أطول مثل `docker compose ...`.

إذا لم تكن قد أعددت Docker بعد، فابدأ بـ [Docker](</ar/install/docker>).

## التثبيت

استخدم مسار المساعد القياسي:

bashCopy code
[code]
    mkdir -p ~/.clawdock && curl -sL https://raw.githubusercontent.com/openclaw/openclaw/main/scripts/clawdock/clawdock-helpers.sh -o ~/.clawdock/clawdock-helpers.shecho 'source ~/.clawdock/clawdock-helpers.sh' >> ~/.zshrc && source ~/.zshrc
[/code]

إذا كنت قد ثبّت ClawDock سابقًا من `scripts/shell-helpers/clawdock-helpers.sh`، فأعد التثبيت من المسار الجديد `scripts/clawdock/clawdock-helpers.sh`. تمت إزالة مسار GitHub الخام القديم.

## ما تحصل عليه

### العمليات الأساسية

الأمر | الوصف  
---|---  
`clawdock-start` | بدء تشغيل Gateway  
`clawdock-stop` | إيقاف Gateway  
`clawdock-restart` | إعادة تشغيل Gateway  
`clawdock-status` | التحقق من حالة الحاوية  
`clawdock-logs` | متابعة سجلات Gateway  
  
### الوصول إلى الحاوية

الأمر | الوصف  
---|---  
`clawdock-shell` | فتح صدفة داخل حاوية Gateway  
`clawdock-cli <command>` | تشغيل أوامر OpenClaw CLI في Docker  
`clawdock-exec <command>` | تنفيذ أمر عشوائي داخل الحاوية  
  
### واجهة الويب والاقتران

الأمر | الوصف  
---|---  
`clawdock-dashboard` | فتح عنوان URL لواجهة التحكم  
`clawdock-devices` | عرض اقترانات الأجهزة المعلقة  
`clawdock-approve <id>` | الموافقة على طلب اقتران  
  
### الإعداد والصيانة

الأمر | الوصف  
---|---  
`clawdock-fix-token` | تكوين رمز Gateway داخل الحاوية  
`clawdock-update` | السحب، وإعادة البناء، وإعادة التشغيل  
`clawdock-rebuild` | إعادة بناء صورة Docker فقط  
`clawdock-clean` | إزالة الحاويات ووحدات التخزين  
  
### الأدوات المساعدة

الأمر | الوصف  
---|---  
`clawdock-health` | تشغيل فحص سلامة Gateway  
`clawdock-token` | طباعة رمز Gateway  
`clawdock-cd` | الانتقال إلى دليل مشروع OpenClaw  
`clawdock-config` | فتح `~/.openclaw`  
`clawdock-show-config` | طباعة ملفات التكوين مع حجب القيم الحساسة  
`clawdock-workspace` | فتح دليل مساحة العمل  
  
## تدفق الاستخدام لأول مرة

bashCopy code
[code]
    clawdock-startclawdock-fix-tokenclawdock-dashboard
[/code]

إذا قال المتصفح إن الاقتران مطلوب:

bashCopy code
[code]
    clawdock-devicesclawdock-approve <request-id>
[/code]

## التكوين والأسرار

يعمل ClawDock مع التقسيم نفسه لتكوين Docker الموضح في [Docker](</ar/install/docker>):

  * `<project>/.env` للقيم الخاصة بـ Docker مثل اسم الصورة والمنافذ ورمز Gateway
  * `~/.openclaw/.env` لمفاتيح المزوّدين المدعومة بمتغيرات البيئة ورموز البوتات
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` لمصادقة OAuth/API-key الخاصة بالمزوّدين والمخزنة
  * `~/.openclaw/openclaw.json` لتكوين السلوك


استخدم `clawdock-show-config` عندما تريد فحص ملفات `.env` و`openclaw.json` بسرعة. يحجب قيم `.env` في المخرجات المطبوعة.

## ذو صلة

[**Docker** تثبيت Docker القياسي لـ OpenClaw. ](</ar/install/docker>) [**وقت تشغيل Docker VM** وقت تشغيل VM مُدار بواسطة Docker لعزل معزز. ](</ar/install/docker-vm-runtime>) [**التحديث** تحديث حزمة OpenClaw والخدمات المُدارة. ](</ar/install/updating>)

Was this useful?YesNo