---
title: خادم Linux
source_url: https://docs.openclaw.ai/ar/vps
scraped_at: 2026-05-25
---

شغّل OpenClaw Gateway على أي خادم Linux أو VPS سحابي. تساعدك هذه الصفحة على اختيار مزوّد، وتشرح كيفية عمل عمليات النشر السحابية، وتغطي ضبط Linux العام الذي ينطبق في كل مكان.

## اختر مزوّدًا

[**Railway** [**Northflank** [**DigitalOcean** [**Oracle Cloud** [**Fly.io** [**Hetzner** [**Hostinger** [**GCP** [**Azure** [**exe.dev** [**Raspberry Pi** **AWS (EC2 / Lightsail / free tier)** يعمل جيدًا أيضًا. يتوفر شرح فيديو من المجتمع على [x.com/techfrenAJ/status/2014934471095812547](<https://x.com/techfrenAJ/status/2014934471095812547>) (مورد مجتمعي -- قد يصبح غير متاح). كيفية عمل الإعدادات السحابية

  * **يعمل Gateway على VPS** ويمتلك الحالة + مساحة العمل.
  * تتصل من حاسوبك المحمول أو هاتفك عبر **واجهة التحكم** أو **Tailscale/SSH**.
  * تعامل مع VPS باعتباره مصدر الحقيقة و**انسخ احتياطيًا** للحالة + مساحة العمل بانتظام.
  * الإعداد الافتراضي الآمن: أبقِ Gateway على loopback وادخل إليه عبر نفق SSH أو Tailscale Serve. إذا ربطته بـ `lan` أو `tailnet`، فاطلب `gateway.auth.token` أو `gateway.auth.password`.

صفحات ذات صلة: [الوصول البعيد إلى Gateway](</ar/gateway/remote>)، [مركز المنصات](</ar/platforms>). شدّد الوصول الإداري أولًا قبل تثبيت OpenClaw على VPS عام، قرر كيف تريد إدارة الجهاز نفسه.

  * إذا كنت تريد وصولًا إداريًا عبر Tailnet فقط، فثبّت Tailscale أولًا، وانضم بـ VPS إلى tailnet لديك، وتحقق من جلسة SSH ثانية عبر عنوان IP الخاص بـ Tailscale أو اسم MagicDNS، ثم قيّد SSH العام.
  * إذا لم تكن تستخدم Tailscale، فطبّق التشديد المكافئ لمسار SSH قبل كشف المزيد من الخدمات.
  * هذا منفصل عن الوصول إلى Gateway. لا يزال بإمكانك إبقاء OpenClaw مربوطًا بـ loopback واستخدام نفق SSH أو Tailscale Serve للوحة المعلومات.

توجد خيارات Gateway الخاصة بـ Tailscale في [Tailscale](</ar/gateway/tailscale>). وكيل شركة مشترك على VPS تشغيل وكيل واحد لفريق هو إعداد صالح عندما يكون كل المستخدمين ضمن حدود الثقة نفسها ويكون الوكيل مخصصًا للعمل فقط.

  * أبقه على بيئة تشغيل مخصصة (VPS/VM/حاوية + مستخدم/حسابات نظام تشغيل مخصصة).
  * لا تسجل دخول بيئة التشغيل تلك إلى حسابات Apple/Google شخصية أو ملفات تعريف متصفح/مدير كلمات مرور شخصية.
  * إذا كان المستخدمون خصومًا لبعضهم بعضًا، فافصل حسب Gateway/المضيف/مستخدم نظام التشغيل.

تفاصيل نموذج الأمان: [الأمان](</ar/gateway/security>). استخدام العُقد مع VPS يمكنك إبقاء Gateway في السحابة وإقران **العُقد** على أجهزتك المحلية (Mac/iOS/Android/بدون واجهة). توفر العُقد إمكانات الشاشة/الكاميرا/canvas المحلية و`system.run` بينما يبقى Gateway في السحابة. المستندات: [العُقد](</ar/nodes>)، [CLI العُقد](</ar/cli/nodes>). ضبط بدء التشغيل للأجهزة الافتراضية الصغيرة ومضيفي ARM إذا بدت أوامر CLI بطيئة على الأجهزة الافتراضية منخفضة الطاقة (أو مضيفي ARM)، ففعّل ذاكرة التخزين المؤقت لتجميع وحدات Node: bashCopy code
[code]
    grep -q 'NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache' ~/.bashrc || cat >> ~/.bashrc <<'EOF'export NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cachemkdir -p /var/tmp/openclaw-compile-cacheexport OPENCLAW_NO_RESPAWN=1EOFsource ~/.bashrc
[/code]

  * يحسّن `NODE_COMPILE_CACHE` أزمنة بدء الأوامر المتكررة.
  * يتجنب `OPENCLAW_NO_RESPAWN=1` حملًا إضافيًا عند بدء التشغيل من مسار إعادة تشغيل ذاتية.
  * أول تشغيل للأمر يهيئ ذاكرة التخزين المؤقت؛ تكون التشغيلات اللاحقة أسرع.
  * لتفاصيل Raspberry Pi، راجع [Raspberry Pi](</ar/install/raspberry-pi>).

قائمة تحقق ضبط systemd (اختياري) لمضيفي VM الذين يستخدمون `systemd`، ضع في اعتبارك:

  * أضف بيئة خدمة لمسار بدء تشغيل مستقر: 
    * `OPENCLAW_NO_RESPAWN=1`
    * `NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache`
  * اجعل سلوك إعادة التشغيل صريحًا: 
    * `Restart=always`
    * `RestartSec=2`
    * `TimeoutStartSec=90`
  * فضّل الأقراص المدعومة بـ SSD لمسارات الحالة/ذاكرة التخزين المؤقت لتقليل عقوبات البدء البارد الناتجة عن الإدخال/الإخراج العشوائي.

لمسار `openclaw onboard --install-daemon` القياسي، حرّر وحدة المستخدم: bashCopy code
[code]
    systemctl --user edit openclaw-gateway.service
[/code]

iniCopy code
[code]
    [Service]Environment=OPENCLAW_NO_RESPAWN=1Environment=NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cacheRestart=alwaysRestartSec=2TimeoutStartSec=90
[/code]

إذا كنت قد ثبّتّ وحدة نظام عن قصد بدلًا من ذلك، فحرّر `openclaw-gateway.service` عبر `sudo systemctl edit openclaw-gateway.service`. كيف تساعد سياسات `Restart=` في الاسترداد الآلي: [يمكن لـ systemd أتمتة استرداد الخدمة](<https://www.redhat.com/en/blog/systemd-automate-recovery>). لسلوك Linux عند نفاد الذاكرة، واختيار العملية الفرعية الضحية، وتشخيصات `exit 137`، راجع [ضغط الذاكرة في Linux وعمليات القتل بسبب نفاد الذاكرة](</ar/platforms/linux#memory-pressure-and-oom-kills>). ذو صلة

  * [نظرة عامة على التثبيت](</ar/install>)
  * [DigitalOcean](</ar/install/digitalocean>)
  * [Fly.io](</ar/install/fly>)
  * [Hetzner](</ar/install/hetzner>)

](</ar/install/raspberry-pi>) Was this useful?YesNo ](</ar/install/exe-dev>)](</ar/install/azure>)](</ar/install/gcp>)](</ar/install/hostinger>)](</ar/install/hetzner>)](</ar/install/fly>)](</ar/install/oracle>)](</ar/install/digitalocean>)](</ar/install/northflank>)](</ar/install/railway>)