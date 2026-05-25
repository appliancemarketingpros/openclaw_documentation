---
title: إلغاء التثبيت
source_url: https://docs.openclaw.ai/ar/install/uninstall
scraped_at: 2026-05-25
---

هناك مساران:

  * **المسار السهل** إذا كان `openclaw` لا يزال مثبتًا.
  * **إزالة الخدمة يدويًا** إذا كان CLI غير موجود لكن الخدمة لا تزال تعمل.


## المسار السهل (لا يزال CLI مثبتًا)

الموصى به: استخدم أداة إلغاء التثبيت المضمنة:

bashCopy code
[code]
    openclaw uninstall
[/code]

وضع غير تفاعلي (للأتمتة / ‏npx):

bashCopy code
[code]
    openclaw uninstall --all --yes --non-interactivenpx -y openclaw uninstall --all --yes --non-interactive
[/code]

الخطوات اليدوية (النتيجة نفسها):

  1. أوقف خدمة gateway:

bashCopy code
[code]
    openclaw gateway stop
[/code]

  2. أزل خدمة gateway ‏(launchd/systemd/schtasks):

bashCopy code
[code]
    openclaw gateway uninstall
[/code]

  3. احذف الحالة + الإعدادات:

bashCopy code
[code]
    rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
[/code]

إذا كنت قد ضبطت `OPENCLAW_CONFIG_PATH` على موقع مخصص خارج دليل الحالة، فاحذف ذلك الملف أيضًا.

  4. احذف مساحة عملك (اختياري، يزيل ملفات الوكيل):

bashCopy code
[code]
    rm -rf ~/.openclaw/workspace
[/code]

  5. أزل تثبيت CLI ‏(اختر الطريقة التي استخدمتها):

bashCopy code
[code]
    npm rm -g openclawpnpm remove -g openclawbun remove -g openclaw
[/code]

  6. إذا كنت قد ثبّت تطبيق macOS:

bashCopy code
[code]
    rm -rf /Applications/OpenClaw.app
[/code]

ملاحظات:

  * إذا كنت قد استخدمت ملفات شخصية (`--profile` / `OPENCLAW_PROFILE`)، فكرّر الخطوة 3 لكل دليل حالة (القيم الافتراضية هي `~/.openclaw-<profile>`).
  * في الوضع البعيد، يوجد دليل الحالة على **مضيف gateway** ، لذا شغّل الخطوات 1-4 هناك أيضًا.


## إزالة الخدمة يدويًا (CLI غير مثبت)

استخدم هذا إذا استمرت خدمة gateway في العمل لكن `openclaw` غير موجود.

### macOS ‏(launchd)

الوسم الافتراضي هو `ai.openclaw.gateway` ‏(أو `ai.openclaw.<profile>`؛ وقد تظل وسوم `com.openclaw.*` القديمة موجودة):

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.gatewayrm -f ~/Library/LaunchAgents/ai.openclaw.gateway.plist
[/code]

إذا كنت قد استخدمت ملفًا شخصيًا، فاستبدل الوسم واسم ملف plist بـ `ai.openclaw.<profile>`. وأزل أي ملفات plist قديمة من نوع `com.openclaw.*` إن وُجدت.

### Linux ‏(وحدة systemd للمستخدم)

اسم الوحدة الافتراضي هو `openclaw-gateway.service` ‏(أو `openclaw-gateway-<profile>.service`):

bashCopy code
[code]
    systemctl --user disable --now openclaw-gateway.servicerm -f ~/.config/systemd/user/openclaw-gateway.servicesystemctl --user daemon-reload
[/code]

### Windows ‏(Scheduled Task)

اسم المهمة الافتراضي هو `OpenClaw Gateway` ‏(أو `OpenClaw Gateway (<profile>)`). يوجد سكربت المهمة تحت دليل الحالة الخاص بك.

powershellCopy code
[code]
    schtasks /Delete /F /TN "OpenClaw Gateway"Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd"
[/code]

إذا كنت قد استخدمت ملفًا شخصيًا، فاحذف اسم المهمة المطابق و`~\.openclaw-<profile>\gateway.cmd`.

## التثبيت العادي مقابل نسخة المصدر

### التثبيت العادي (`install.sh` / `npm` / `pnpm` / `bun`)

إذا كنت قد استخدمت `https://openclaw.ai/install.sh` أو `install.ps1`، فقد تم تثبيت CLI باستخدام `npm install -g openclaw@latest`. أزله باستخدام `npm rm -g openclaw` (أو `pnpm remove -g` / `bun remove -g` إذا كنت قد ثبّتّه بهذه الطريقة).

### نسخة المصدر (`git clone`)

إذا كنت تشغّل من نسخة مستودع (`git clone` \+ `openclaw ...` / `bun run openclaw ...`):

  1. أزل تثبيت خدمة gateway **قبل** حذف المستودع (استخدم المسار السهل أعلاه أو إزالة الخدمة يدويًا).
  2. احذف دليل المستودع.
  3. أزل الحالة + مساحة العمل كما هو موضح أعلاه.


## ذو صلة

  * [نظرة عامة على التثبيت](</ar/install>)
  * [دليل الترحيل](</ar/install/migrating>)


Was this useful?YesNo