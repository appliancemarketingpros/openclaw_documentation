---
title: Hetzner
source_url: https://docs.openclaw.ai/ar/install/hetzner
scraped_at: 2026-05-25
---

## الهدف

شغّل OpenClaw Gateway دائمًا على Hetzner VPS باستخدام Docker، مع حالة دائمة، وثنائيات مدمجة، وسلوك إعادة تشغيل آمن.

إذا كنت تريد "OpenClaw على مدار الساعة مقابل نحو 5 دولارات"، فهذا هو أبسط إعداد موثوق. تتغير أسعار Hetzner؛ اختر أصغر VPS يعمل بنظام Debian/Ubuntu وزد الموارد إذا واجهت نفادًا في الذاكرة.

تذكير بنموذج الأمان:

  * الوكلاء المشتركون على مستوى الشركة مناسبون عندما يكون الجميع ضمن حدود الثقة نفسها ويكون وقت التشغيل مخصصًا للأعمال فقط.
  * حافظ على فصل صارم: VPS/وقت تشغيل مخصص + حسابات مخصصة؛ لا تستخدم ملفات تعريف Apple/Google/المتصفح/مدير كلمات المرور الشخصية على ذلك المضيف.
  * إذا كان المستخدمون خصومًا لبعضهم، فافصلهم حسب Gateway/المضيف/مستخدم نظام التشغيل.


راجع [الأمان](</ar/gateway/security>) و[استضافة VPS](</ar/vps>).

## ماذا سنفعل (بعبارات بسيطة)؟

  * استئجار خادم Linux صغير (Hetzner VPS)
  * تثبيت Docker (وقت تشغيل تطبيق معزول)
  * بدء OpenClaw Gateway في Docker
  * حفظ `~/.openclaw` \+ `~/.openclaw/workspace` على المضيف بشكل دائم (يبقى بعد إعادة التشغيل/إعادة البناء)
  * الوصول إلى واجهة التحكم من حاسوبك المحمول عبر نفق SSH


تتضمن حالة `~/.openclaw` المثبتة هذه `openclaw.json`، وملف `agents/<agentId>/agent/auth-profiles.json` لكل وكيل، و`.env`.

يمكن الوصول إلى Gateway عبر:

  * إعادة توجيه منفذ SSH من حاسوبك المحمول
  * تعريض المنفذ مباشرة إذا كنت تدير الجدار الناري والرموز بنفسك


يفترض هذا الدليل استخدام Ubuntu أو Debian على Hetzner.  
إذا كنت تستخدم VPS آخر يعمل بنظام Linux، فطابق الحزم وفقًا لذلك. للتدفق العام مع Docker، راجع [Docker](</ar/install/docker>).

* * *

## المسار السريع (للمشغلين ذوي الخبرة)

  1. وفّر Hetzner VPS
  2. ثبّت Docker
  3. استنسخ مستودع OpenClaw
  4. أنشئ أدلة مضيف دائمة
  5. اضبط `.env` و`docker-compose.yml`
  6. ادمج الثنائيات المطلوبة في الصورة
  7. `docker compose up -d`
  8. تحقق من الاستمرارية والوصول إلى Gateway


* * *

## ما تحتاجه

  * Hetzner VPS مع وصول root
  * وصول SSH من حاسوبك المحمول
  * إلمام أساسي بـ SSH + النسخ/اللصق
  * نحو 20 دقيقة
  * Docker وDocker Compose
  * اعتمادات مصادقة النموذج
  * اعتمادات مزوّد اختيارية 
    * WhatsApp QR
    * رمز بوت Telegram
    * Gmail OAuth


* * *

* ### توفير VPS

أنشئ VPS يعمل بنظام Ubuntu أو Debian في Hetzner.

اتصل كمستخدم root:

bashCopy code
[code]
    ssh root@YOUR_VPS_IP
[/code]

يفترض هذا الدليل أن VPS يحفظ الحالة. لا تتعامل معه كبنية تحتية قابلة للاستبدال.

* ### تثبيت Docker (على VPS)

bashCopy code
[code]
    apt-get updateapt-get install -y git curl ca-certificatescurl -fsSL https://get.docker.com | sh
[/code]

تحقق:

bashCopy code
[code]
    docker --versiondocker compose version
[/code]

* ### استنساخ مستودع OpenClaw

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclaw
[/code]

يفترض هذا الدليل أنك ستبني صورة مخصصة لضمان استمرار الثنائيات.

* ### إنشاء أدلة مضيف دائمة

حاويات Docker مؤقتة. يجب أن تعيش كل الحالة طويلة الأمد على المضيف.

bashCopy code
[code]
    mkdir -p /root/.openclaw/workspace # Set ownership to the container user (uid 1000):chown -R 1000:1000 /root/.openclaw
[/code]

* ### ضبط متغيرات البيئة

أنشئ `.env` في جذر المستودع.

bashCopy code
[code]
    OPENCLAW_IMAGE=openclaw:latestOPENCLAW_GATEWAY_TOKEN=OPENCLAW_GATEWAY_BIND=lanOPENCLAW_GATEWAY_PORT=18789 OPENCLAW_CONFIG_DIR=/root/.openclawOPENCLAW_WORKSPACE_DIR=/root/.openclaw/workspace GOG_KEYRING_PASSWORD=XDG_CONFIG_HOME=/home/node/.openclaw
[/code]

اضبط `OPENCLAW_GATEWAY_TOKEN` عندما تريد إدارة رمز Gateway المستقر عبر `.env`؛ وإلا فاضبط `gateway.auth.token` قبل الاعتماد على العملاء عبر عمليات إعادة التشغيل. إذا لم يكن أي من المصدرين موجودًا، يستخدم OpenClaw رمزًا خاصًا بوقت التشغيل فقط لتلك البداية. أنشئ كلمة مرور لسلسلة المفاتيح والصقها في `GOG_KEYRING_PASSWORD`:

bashCopy code
[code]
    openssl rand -hex 32
[/code]

**لا تلتزم بهذا الملف في المستودع.**

ملف `.env` هذا مخصص لبيئة الحاوية/وقت التشغيل مثل `OPENCLAW_GATEWAY_TOKEN`. تعيش مصادقة OAuth/API-key المخزنة للمزوّد في `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` المثبت.

* ### إعداد Docker Compose

أنشئ أو حدّث `docker-compose.yml`.

yamlCopy code
[code]
    services:  openclaw-gateway:    image: ${OPENCLAW_IMAGE}    build: .    restart: unless-stopped    env_file:      - .env    environment:      - HOME=/home/node      - NODE_ENV=production      - TERM=xterm-256color      - OPENCLAW_GATEWAY_BIND=${OPENCLAW_GATEWAY_BIND}      - OPENCLAW_GATEWAY_PORT=${OPENCLAW_GATEWAY_PORT}      - OPENCLAW_GATEWAY_TOKEN=${OPENCLAW_GATEWAY_TOKEN}      - GOG_KEYRING_PASSWORD=${GOG_KEYRING_PASSWORD}      - XDG_CONFIG_HOME=${XDG_CONFIG_HOME}      - PATH=/home/linuxbrew/.linuxbrew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin    volumes:      - ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw      - ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace    ports:      # Recommended: keep the Gateway loopback-only on the VPS; access via SSH tunnel.      # To expose it publicly, remove the `127.0.0.1:` prefix and firewall accordingly.      - "127.0.0.1:${OPENCLAW_GATEWAY_PORT}:18789"    command:      [        "node",        "dist/index.js",        "gateway",        "--bind",        "${OPENCLAW_GATEWAY_BIND}",        "--port",        "${OPENCLAW_GATEWAY_PORT}",        "--allow-unconfigured",      ]
[/code]

`--allow-unconfigured` مخصص فقط لراحة التمهيد، وليس بديلًا عن إعداد Gateway مناسب. مع ذلك اضبط المصادقة (`gateway.auth.token` أو كلمة مرور) واستخدم إعدادات ربط آمنة لنشرك.

* ### خطوات وقت تشغيل Docker VM المشتركة

استخدم دليل وقت التشغيل المشترك لتدفق مضيف Docker الشائع:

  * [دمج الثنائيات المطلوبة في الصورة](</ar/install/docker-vm-runtime#bake-required-binaries-into-the-image>)
  * [البناء والتشغيل](</ar/install/docker-vm-runtime#build-and-launch>)
  * [ما الذي يستمر وأين](</ar/install/docker-vm-runtime#what-persists-where>)
  * [التحديثات](</ar/install/docker-vm-runtime#updates>)


* ### وصول خاص بـ Hetzner

بعد خطوات البناء والتشغيل المشتركة، أكمل الإعداد التالي لفتح النفق:

**المتطلب السابق:** تأكد من أن إعداد sshd في VPS يسمح بإعادة توجيه TCP. إذا كنت قد شددت إعداد SSH لديك، فتحقق من `/etc/ssh/sshd_config` واضبط:

CodeCopy code
[code]
    AllowTcpForwarding local
[/code]

يسمح `local` بعمليات إعادة التوجيه المحلية `ssh -L` من حاسوبك المحمول مع حظر عمليات إعادة التوجيه البعيدة من الخادم. سيؤدي ضبطه على `no` إلى فشل النفق مع: `channel 3: open failed: administratively prohibited: open failed`

بعد تأكيد تمكين إعادة توجيه TCP، أعد تشغيل خدمة SSH (`systemctl restart ssh`) وشغّل النفق من حاسوبك المحمول:

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 root@YOUR_VPS_IP
[/code]

افتح:

`http://127.0.0.1:18789/`

الصق السر المشترك المضبوط. يستخدم هذا الدليل رمز Gateway افتراضيًا؛ إذا انتقلت إلى مصادقة كلمة المرور، فاستخدم تلك كلمة المرور بدلًا من ذلك.

توجد خريطة الاستمرارية المشتركة في [وقت تشغيل Docker VM](</ar/install/docker-vm-runtime#what-persists-where>).

## البنية التحتية ككود (Terraform)

للفرق التي تفضّل تدفقات عمل البنية التحتية ككود، يوفر إعداد Terraform المُدار من المجتمع:

  * إعداد Terraform معياري مع إدارة حالة بعيدة
  * توفيرًا آليًا عبر cloud-init
  * نصوص نشر برمجية (تمهيد، نشر، نسخ احتياطي/استعادة)
  * تعزيزًا أمنيًا (جدار ناري، UFW، وصول SSH فقط)
  * إعداد نفق SSH للوصول إلى Gateway


**المستودعات:**

  * البنية التحتية: [openclaw-terraform-hetzner](<https://github.com/andreesg/openclaw-terraform-hetzner>)
  * إعداد Docker: [openclaw-docker-config](<https://github.com/andreesg/openclaw-docker-config>)


يكمل هذا النهج إعداد Docker أعلاه بعمليات نشر قابلة للتكرار، وبنية تحتية مضبوطة بالإصدارات، واستعادة آلية عند الكوارث.

## الخطوات التالية

  * إعداد قنوات المراسلة: [القنوات](</ar/channels>)
  * ضبط Gateway: [إعداد Gateway](</ar/gateway/configuration>)
  * إبقاء OpenClaw محدّثًا: [التحديث](</ar/install/updating>)


## ذات صلة

  * [نظرة عامة على التثبيت](</ar/install>)
  * [Fly.io](</ar/install/fly>)
  * [Docker](</ar/install/docker>)
  * [استضافة VPS](</ar/vps>)


Was this useful?YesNo