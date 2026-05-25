---
title: GCP
source_url: https://docs.openclaw.ai/ar/install/gcp
scraped_at: 2026-05-25
---

شغّل OpenClaw Gateway دائمًا على VM في GCP Compute Engine باستخدام Docker، مع حالة دائمة وثنائيات مضمّنة وسلوك إعادة تشغيل آمن.

إذا كنت تريد "OpenClaw 24/7 مقابل حوالي 5-12 دولارًا/شهرًا"، فهذا إعداد موثوق على Google Cloud. تختلف الأسعار حسب نوع الجهاز والمنطقة؛ اختر أصغر VM تناسب حمل عملك، ثم وسّعها إذا واجهت حالات نفاد ذاكرة (OOM).

## ماذا نفعل (بعبارات بسيطة)؟

  * إنشاء مشروع GCP وتفعيل الفوترة
  * إنشاء VM في Compute Engine
  * تثبيت Docker (بيئة تشغيل تطبيق معزولة)
  * تشغيل OpenClaw Gateway في Docker
  * إبقاء `~/.openclaw` \+ `~/.openclaw/workspace` دائمين على المضيف (يبقيان بعد إعادة التشغيل/إعادة البناء)
  * الوصول إلى واجهة التحكم من حاسوبك المحمول عبر نفق SSH


تتضمن حالة `~/.openclaw` المثبتة هذه `openclaw.json` وملف `agents/<agentId>/agent/auth-profiles.json` الخاص بكل وكيل و`.env`.

يمكن الوصول إلى Gateway عبر:

  * تمرير منفذ SSH من حاسوبك المحمول
  * تعريض المنفذ مباشرة إذا كنت تدير الجدار الناري والرموز المميزة بنفسك


يستخدم هذا الدليل Debian على GCP Compute Engine. يعمل Ubuntu أيضًا؛ طابِق الحزم وفقًا لذلك. للمسار العام الخاص بـ Docker، راجع [Docker](</ar/install/docker>).

* * *

## المسار السريع (للمشغلين ذوي الخبرة)

  1. أنشئ مشروع GCP + فعّل Compute Engine API
  2. أنشئ VM في Compute Engine (e2-small، Debian 12، 20GB)
  3. ادخل إلى VM عبر SSH
  4. ثبّت Docker
  5. استنسخ مستودع OpenClaw
  6. أنشئ أدلة مضيف دائمة
  7. اضبط `.env` و`docker-compose.yml`
  8. ضمّن الثنائيات المطلوبة، وابنِ، وشغّل


* * *

## ما تحتاج إليه

  * حساب GCP (مؤهل للطبقة المجانية لـ e2-micro)
  * gcloud CLI مثبتة (أو استخدم Cloud Console)
  * وصول SSH من حاسوبك المحمول
  * إلمام أساسي بـ SSH + النسخ/اللصق
  * ~20-30 دقيقة
  * Docker وDocker Compose
  * بيانات اعتماد مصادقة النموذج
  * بيانات اعتماد مزود اختيارية 
    * WhatsApp QR
    * رمز بوت Telegram
    * Gmail OAuth


* * *

* ### تثبيت gcloud CLI (أو استخدام وحدة التحكم)

**الخيار أ: gcloud CLI** (موصى به للأتمتة)

ثبّت من <https://cloud.google.com/sdk/docs/install>

هيّئ وسجّل الدخول:

bashCopy code
[code]
    gcloud initgcloud auth login
[/code]

**الخيار ب: Cloud Console**

يمكن تنفيذ جميع الخطوات عبر واجهة الويب في <https://console.cloud.google.com>

* ### إنشاء مشروع GCP

**CLI:**

bashCopy code
[code]
    gcloud projects create my-openclaw-project --name="OpenClaw Gateway"gcloud config set project my-openclaw-project
[/code]

فعّل الفوترة في <https://console.cloud.google.com/billing> (مطلوبة لـ Compute Engine).

فعّل Compute Engine API:

bashCopy code
[code]
    gcloud services enable compute.googleapis.com
[/code]

**وحدة التحكم:**

  1. انتقل إلى IAM والمسؤول > إنشاء مشروع
  2. سمّه وأنشئه
  3. فعّل الفوترة للمشروع
  4. انتقل إلى واجهات API والخدمات > تفعيل واجهات API > ابحث عن "Compute Engine API" > تفعيل


* ### إنشاء VM

**أنواع الأجهزة:**

النوع | المواصفات | التكلفة | ملاحظات  
---|---|---|---  
e2-medium | 2 vCPU، 4GB RAM | ~$25/mo | الأكثر موثوقية لعمليات بناء Docker المحلية  
e2-small | 2 vCPU، 2GB RAM | ~$12/mo | الحد الأدنى الموصى به لبناء Docker  
e2-micro | 2 vCPU (مشتركة)، 1GB RAM | مؤهل للطبقة المجانية | غالبًا يفشل عند بناء Docker بسبب نفاد الذاكرة (رمز الخروج 137)  
  
**CLI:**

bashCopy code
[code]
    gcloud compute instances create openclaw-gateway \  --zone=us-central1-a \  --machine-type=e2-small \  --boot-disk-size=20GB \  --image-family=debian-12 \  --image-project=debian-cloud
[/code]

**وحدة التحكم:**

  1. انتقل إلى Compute Engine > مثيلات VM > إنشاء مثيل
  2. الاسم: `openclaw-gateway`
  3. المنطقة: `us-central1`، النطاق: `us-central1-a`
  4. نوع الجهاز: `e2-small`
  5. قرص الإقلاع: Debian 12، 20GB
  6. أنشئ


* ### الدخول إلى VM عبر SSH

**CLI:**

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a
[/code]

**وحدة التحكم:**

انقر زر "SSH" بجوار VM الخاصة بك في لوحة معلومات Compute Engine.

ملاحظة: قد يستغرق نشر مفتاح SSH مدة 1-2 دقيقة بعد إنشاء VM. إذا رُفض الاتصال، انتظر ثم أعد المحاولة.

* ### تثبيت Docker (على VM)

bashCopy code
[code]
    sudo apt-get updatesudo apt-get install -y git curl ca-certificatescurl -fsSL https://get.docker.com | sudo shsudo usermod -aG docker $USER
[/code]

سجّل الخروج ثم ادخل مجددًا لتطبيق تغيير المجموعة:

bashCopy code
[code]
    exit
[/code]

ثم ادخل مرة أخرى عبر SSH:

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a
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

يفترض هذا الدليل أنك ستبني صورة مخصصة لضمان استمرارية الثنائيات.

* ### إنشاء أدلة مضيف دائمة

حاويات Docker مؤقتة. يجب أن تكون كل الحالة طويلة العمر على المضيف.

bashCopy code
[code]
    mkdir -p ~/.openclawmkdir -p ~/.openclaw/workspace
[/code]

* ### ضبط متغيرات البيئة

أنشئ `.env` في جذر المستودع.

bashCopy code
[code]
    OPENCLAW_IMAGE=openclaw:latestOPENCLAW_GATEWAY_TOKEN=OPENCLAW_GATEWAY_BIND=lanOPENCLAW_GATEWAY_PORT=18789 OPENCLAW_CONFIG_DIR=/home/$USER/.openclawOPENCLAW_WORKSPACE_DIR=/home/$USER/.openclaw/workspace GOG_KEYRING_PASSWORD=XDG_CONFIG_HOME=/home/node/.openclaw
[/code]

عيّن `OPENCLAW_GATEWAY_TOKEN` عندما تريد إدارة رمز Gateway المميز المستقر من خلال `.env`؛ وإلا فاضبط `gateway.auth.token` قبل الاعتماد على العملاء عبر عمليات إعادة التشغيل. إذا لم يكن أي من المصدرين موجودًا، يستخدم OpenClaw رمزًا مميزًا مخصصًا لوقت التشغيل فقط لذلك التشغيل. أنشئ كلمة مرور لسلسلة المفاتيح والصقها في `GOG_KEYRING_PASSWORD`:

bashCopy code
[code]
    openssl rand -hex 32
[/code]

**لا تودع هذا الملف في Git.**

ملف `.env` هذا مخصص لبيئة الحاوية/وقت التشغيل مثل `OPENCLAW_GATEWAY_TOKEN`. توجد مصادقة مزود OAuth/مفاتيح API المخزنة في المسار المثبت `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`.

* ### تكوين Docker Compose

أنشئ أو حدّث `docker-compose.yml`.

yamlCopy code
[code]
    services:  openclaw-gateway:    image: ${OPENCLAW_IMAGE}    build: .    restart: unless-stopped    env_file:      - .env    environment:      - HOME=/home/node      - NODE_ENV=production      - TERM=xterm-256color      - OPENCLAW_GATEWAY_BIND=${OPENCLAW_GATEWAY_BIND}      - OPENCLAW_GATEWAY_PORT=${OPENCLAW_GATEWAY_PORT}      - OPENCLAW_GATEWAY_TOKEN=${OPENCLAW_GATEWAY_TOKEN}      - GOG_KEYRING_PASSWORD=${GOG_KEYRING_PASSWORD}      - XDG_CONFIG_HOME=${XDG_CONFIG_HOME}      - PATH=/home/linuxbrew/.linuxbrew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin    volumes:      - ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw      - ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace    ports:      # Recommended: keep the Gateway loopback-only on the VM; access via SSH tunnel.      # To expose it publicly, remove the `127.0.0.1:` prefix and firewall accordingly.      - "127.0.0.1:${OPENCLAW_GATEWAY_PORT}:18789"    command:      [        "node",        "dist/index.js",        "gateway",        "--bind",        "${OPENCLAW_GATEWAY_BIND}",        "--port",        "${OPENCLAW_GATEWAY_PORT}",        "--allow-unconfigured",      ]
[/code]

`--allow-unconfigured` مخصص فقط لتسهيل التمهيد، وليس بديلًا عن تكوين Gateway صحيح. مع ذلك، اضبط المصادقة (`gateway.auth.token` أو كلمة مرور) واستخدم إعدادات ربط آمنة لنشرك.

* ### خطوات وقت تشغيل Docker VM المشتركة

استخدم دليل وقت التشغيل المشترك لتدفق مضيف Docker العام:

  * [تضمين الثنائيات المطلوبة في الصورة](</ar/install/docker-vm-runtime#bake-required-binaries-into-the-image>)
  * [البناء والتشغيل](</ar/install/docker-vm-runtime#build-and-launch>)
  * [ما الذي يستمر وأين](</ar/install/docker-vm-runtime#what-persists-where>)
  * [التحديثات](</ar/install/docker-vm-runtime#updates>)


* ### ملاحظات تشغيل خاصة بـ GCP

على GCP، إذا فشل البناء مع `Killed` أو `exit code 137` أثناء `pnpm install --frozen-lockfile`، فهذا يعني أن ذاكرة VM نفدت. استخدم `e2-small` كحد أدنى، أو `e2-medium` لعمليات بناء أولى أكثر موثوقية.

عند الربط بالشبكة المحلية (LAN) (`OPENCLAW_GATEWAY_BIND=lan`)، اضبط أصل متصفح موثوقًا قبل المتابعة:

bashCopy code
[code]
    docker compose run --rm openclaw-cli config set gateway.controlUi.allowedOrigins '["http://127.0.0.1:18789"]' --strict-json
[/code]

إذا غيّرت منفذ Gateway، فاستبدل `18789` بالمنفذ الذي ضبطته.

* ### الوصول من حاسوبك المحمول

أنشئ نفق SSH لتمرير منفذ Gateway:

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a -- -L 18789:127.0.0.1:18789
[/code]

افتح في متصفحك:

`http://127.0.0.1:18789/`

أعد طباعة رابط نظيف للوحة المعلومات:

bashCopy code
[code]
    docker compose run --rm openclaw-cli dashboard --no-open
[/code]

إذا طالبت واجهة المستخدم بمصادقة سر مشترك، فالصق الرمز المميز أو كلمة المرور المضبوطة في إعدادات واجهة التحكم. يكتب مسار Docker هذا رمزًا مميزًا افتراضيًا؛ إذا بدّلت تكوين الحاوية إلى مصادقة بكلمة مرور، فاستخدم تلك الكلمة بدلًا من ذلك.

إذا عرضت واجهة التحكم `unauthorized` أو `disconnected (1008): pairing required`، فوافق على جهاز المتصفح:

bashCopy code
[code]
    docker compose run --rm openclaw-cli devices listdocker compose run --rm openclaw-cli devices approve <requestId>
[/code]

هل تحتاج مرة أخرى إلى مرجع الاستمرارية والتحديثات المشترك؟ راجع [وقت تشغيل Docker VM](</ar/install/docker-vm-runtime#what-persists-where>) و[تحديثات وقت تشغيل Docker VM](</ar/install/docker-vm-runtime#updates>).

* * *

## استكشاف الأخطاء وإصلاحها

**رُفض اتصال SSH**

قد يستغرق نشر مفتاح SSH مدة 1-2 دقيقة بعد إنشاء VM. انتظر ثم أعد المحاولة.

**مشكلات OS Login**

تحقق من ملف تعريف OS Login لديك:

bashCopy code
[code]
    gcloud compute os-login describe-profile
[/code]

تأكد من أن حسابك لديه أذونات IAM المطلوبة (Compute OS Login أو Compute OS Admin Login).

**نفاد الذاكرة (OOM)**

إذا فشل بناء Docker مع `Killed` و`exit code 137`، فقد أُوقفت VM بسبب نفاد الذاكرة. انتقل إلى e2-small (الحد الأدنى) أو e2-medium (الموصى به لعمليات البناء المحلية الموثوقة):

bashCopy code
[code]
    # Stop the VM firstgcloud compute instances stop openclaw-gateway --zone=us-central1-a # Change machine typegcloud compute instances set-machine-type openclaw-gateway \  --zone=us-central1-a \  --machine-type=e2-small # Start the VMgcloud compute instances start openclaw-gateway --zone=us-central1-a
[/code]

* * *

## حسابات الخدمة (أفضل ممارسة أمنية)

للاستخدام الشخصي، يكفي حساب المستخدم الافتراضي لديك.

لأغراض الأتمتة أو مسارات CI/CD، أنشئ حساب خدمة مخصصًا بأقل قدر من الأذونات:

  1. أنشئ حساب خدمة:

bashCopy code
[code]gcloud iam service-accounts create openclaw-deploy \  --display-name="OpenClaw Deployment"
[/code]

  2. امنح دور Compute Instance Admin (أو دورًا مخصصًا أضيق):

bashCopy code
[code]gcloud projects add-iam-policy-binding my-openclaw-project \  --member="serviceAccount:openclaw-deploy@my-openclaw-project.iam.gserviceaccount.com" \  --role="roles/compute.instanceAdmin.v1"
[/code]


تجنب استخدام دور Owner للأتمتة. استخدم مبدأ أقل الامتيازات.

راجع <https://cloud.google.com/iam/docs/understanding-roles> للاطلاع على تفاصيل أدوار IAM.

* * *

## الخطوات التالية

  * إعداد قنوات المراسلة: [القنوات](</ar/channels>)
  * إقران الأجهزة المحلية كـ Nodes: [Nodes](</ar/nodes>)
  * تكوين Gateway: [تكوين Gateway](</ar/gateway/configuration>)


## ذات صلة

  * [نظرة عامة على التثبيت](</ar/install>)
  * [Azure](</ar/install/azure>)
  * [استضافة VPS](</ar/vps>)


Was this useful?YesNo