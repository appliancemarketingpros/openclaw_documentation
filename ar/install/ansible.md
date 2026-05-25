---
title: Ansible
source_url: https://docs.openclaw.ai/ar/install/ansible
scraped_at: 2026-05-25
---

انشر OpenClaw إلى خوادم الإنتاج باستخدام **[openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>)** \-- مثبّت آلي ببنية تركّز على الأمان أولاً.

## المتطلبات الأساسية

المتطلب | التفاصيل  
---|---  
**نظام التشغيل** | Debian 11+ أو Ubuntu 20.04+  
**الوصول** | صلاحيات Root أو sudo  
**الشبكة** | اتصال إنترنت لتثبيت الحزم  
**Ansible** | 2.14+ (يثبّته سكربت البدء السريع تلقائياً)  
  
## ما الذي ستحصل عليه

  * **أمان يبدأ بجدار الحماية** \-- عزل UFW + Docker (يمكن الوصول إلى SSH + Tailscale فقط)
  * **Tailscale VPN** \-- وصول آمن عن بُعد دون كشف الخدمات للعامة
  * **Docker** \-- حاويات عزل منفصلة، وروابط محصورة في localhost فقط
  * **دفاع متعدد الطبقات** \-- بنية أمان من 4 طبقات
  * **تكامل Systemd** \-- بدء تلقائي عند الإقلاع مع تقوية الأمان
  * **إعداد بأمر واحد** \-- نشر كامل خلال دقائق


## البدء السريع

تثبيت بأمر واحد:

bashCopy code
[code]
    curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash
[/code]

## ما الذي يتم تثبيته

يثبّت Ansible playbook ويضبط ما يلي:

  1. **Tailscale** \-- شبكة VPN متداخلة للوصول الآمن عن بُعد
  2. **جدار حماية UFW** \-- منافذ SSH + Tailscale فقط
  3. **Docker CE + Compose V2** \-- للواجهة الخلفية الافتراضية لبيئة عزل الوكيل
  4. **Node.js 24 + pnpm** \-- تبعيات وقت التشغيل (يبقى Node 22 LTS، حالياً `22.16+`، مدعوماً)
  5. **OpenClaw** \-- مستند إلى المضيف، وليس داخل حاوية
  6. **خدمة Systemd** \-- بدء تلقائي مع تقوية الأمان


## إعداد ما بعد التثبيت

* ### التبديل إلى مستخدم openclaw

bashCopy code
[code]
    sudo -i -u openclaw
[/code]

* ### تشغيل معالج التهيئة

يرشدك سكربت ما بعد التثبيت خلال ضبط إعدادات OpenClaw.

* ### ربط مزودي المراسلة

سجّل الدخول إلى WhatsApp أو Telegram أو Discord أو Signal:

bashCopy code
[code]
    openclaw channels login
[/code]

* ### التحقق من التثبيت

bashCopy code
[code]
    sudo systemctl status openclawsudo journalctl -u openclaw -f
[/code]

* ### الاتصال بـ Tailscale

انضم إلى شبكة VPN المتداخلة لديك للوصول الآمن عن بُعد.

### أوامر سريعة

bashCopy code
[code]
    # Check service statussudo systemctl status openclaw # View live logssudo journalctl -u openclaw -f # Restart gatewaysudo systemctl restart openclaw # Provider login (run as openclaw user)sudo -i -u openclawopenclaw channels login
[/code]

## بنية الأمان

يستخدم النشر نموذج دفاع من 4 طبقات:

  1. **جدار الحماية (UFW)** \-- لا تُكشف للعامة إلا منافذ SSH (22) + Tailscale (41641/udp)
  2. **VPN (Tailscale)** \-- لا يمكن الوصول إلى Gateway إلا عبر شبكة VPN المتداخلة
  3. **عزل Docker** \-- تمنع سلسلة iptables المسماة DOCKER-USER كشف المنافذ الخارجية
  4. **تقوية Systemd** \-- NoNewPrivileges، وPrivateTmp، ومستخدم غير مميز


للتحقق من سطح الهجوم الخارجي لديك:

bashCopy code
[code]
    nmap -p- YOUR_SERVER_IP
[/code]

يجب أن يكون المنفذ 22 (SSH) وحده مفتوحاً. كل الخدمات الأخرى (Gateway، Docker) مقفلة.

يُثبّت Docker لبيئات عزل الوكلاء (تنفيذ الأدوات المعزول)، وليس لتشغيل Gateway نفسه. راجع [بيئة عزل متعددة الوكلاء والأدوات](</ar/tools/multi-agent-sandbox-tools>) لضبط العزل.

## التثبيت اليدوي

إذا كنت تفضّل التحكم اليدوي بدلاً من الأتمتة:

* ### تثبيت المتطلبات الأساسية

bashCopy code
[code]
    sudo apt update && sudo apt install -y ansible git
[/code]

* ### استنساخ المستودع

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw-ansible.gitcd openclaw-ansible
[/code]

* ### تثبيت مجموعات Ansible

bashCopy code
[code]
    ansible-galaxy collection install -r requirements.yml
[/code]

* ### تشغيل playbook

bashCopy code
[code]
    ./run-playbook.sh
[/code]

بدلاً من ذلك، شغّله مباشرة ثم نفّذ سكربت الإعداد يدوياً بعد ذلك:

bashCopy code
[code]
    ansible-playbook playbook.yml --ask-become-pass# Then run: /tmp/openclaw-setup.sh
[/code]

## التحديث

يضبط مثبّت Ansible OpenClaw للتحديثات اليدوية. راجع [التحديث](</ar/install/updating>) لتدفق التحديث القياسي.

لإعادة تشغيل Ansible playbook (على سبيل المثال، لتغييرات الضبط):

bashCopy code
[code]
    cd openclaw-ansible./run-playbook.sh
[/code]

هذا الإجراء idempotent وآمن للتشغيل عدة مرات.

## استكشاف الأخطاء وإصلاحها

جدار الحماية يحظر اتصالي

  * تأكد أولاً من إمكانية الوصول عبر Tailscale VPN
  * الوصول عبر SSH (المنفذ 22) مسموح دائماً
  * لا يمكن الوصول إلى Gateway إلا عبر Tailscale بحسب التصميم

الخدمة لا تبدأ bashCopy code
[code]
    # Check logssudo journalctl -u openclaw -n 100 # Verify permissionssudo ls -la /opt/openclaw # Test manual startsudo -i -u openclawcd ~/openclawopenclaw gateway run
[/code]

مشكلات بيئة عزل Docker bashCopy code
[code]
    # Verify Docker is runningsudo systemctl status docker # Check sandbox imagesudo docker images | grep openclaw-sandbox # Build sandbox image if missing (requires source checkout)cd /opt/openclaw/openclawsudo -u openclaw ./scripts/sandbox-setup.sh# For npm installs without a source checkout, see# https://docs.openclaw.ai/gateway/sandboxing#images-and-setup
[/code]

فشل تسجيل الدخول إلى المزود

تأكد من أنك تعمل كمستخدم `openclaw`:

bashCopy code
[code]
    sudo -i -u openclawopenclaw channels login
[/code]

## الضبط المتقدم

للاطلاع على بنية الأمان التفصيلية واستكشاف الأخطاء وإصلاحها، راجع مستودع openclaw-ansible:

  * [بنية الأمان](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/security.md>)
  * [التفاصيل التقنية](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/architecture.md>)
  * [دليل استكشاف الأخطاء وإصلاحها](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/troubleshooting.md>)


## ذو صلة

  * [openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>) \-- دليل النشر الكامل
  * [Docker](</ar/install/docker>) \-- إعداد Gateway داخل حاوية
  * [العزل](</ar/gateway/sandboxing>) \-- ضبط بيئة عزل الوكيل
  * [بيئة عزل متعددة الوكلاء والأدوات](</ar/tools/multi-agent-sandbox-tools>) \-- عزل لكل وكيل


Was this useful?YesNo