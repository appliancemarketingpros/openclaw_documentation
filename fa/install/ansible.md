---
title: Ansible
source_url: https://docs.openclaw.ai/fa/install/ansible
scraped_at: 2026-05-25
---

OpenClaw را با **[openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>)** روی سرورهای تولید مستقر کنید -- یک نصب‌کننده خودکار با معماری امنیت‌محور.

## پیش‌نیازها

نیازمندی | جزئیات  
---|---  
**سیستم‌عامل** | Debian 11+ یا Ubuntu 20.04+  
**دسترسی** | دسترسی root یا امتیازهای sudo  
**شبکه** | اتصال اینترنت برای نصب بسته‌ها  
**Ansible** | 2.14+ (به‌صورت خودکار توسط اسکریپت شروع سریع نصب می‌شود)  
  
## چه چیزی دریافت می‌کنید

  * **امنیت با اولویت فایروال** \-- UFW + ایزوله‌سازی Docker (فقط SSH + Tailscale در دسترس)
  * **Tailscale VPN** \-- دسترسی راه دور امن بدون عمومی‌کردن سرویس‌ها
  * **Docker** \-- کانتینرهای سندباکس ایزوله، اتصال‌های فقط localhost
  * **دفاع چندلایه** \-- معماری امنیتی ۴ لایه
  * **یکپارچه‌سازی با Systemd** \-- شروع خودکار هنگام راه‌اندازی با سخت‌سازی امنیتی
  * **راه‌اندازی با یک فرمان** \-- استقرار کامل در چند دقیقه


## شروع سریع

نصب با یک فرمان:

bashCopy code
[code]
    curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash
[/code]

## چه چیزهایی نصب می‌شود

پلی‌بوک Ansible این موارد را نصب و پیکربندی می‌کند:

  1. **Tailscale** \-- VPN مش برای دسترسی راه دور امن
  2. **فایروال UFW** \-- فقط پورت‌های SSH + Tailscale
  3. **Docker CE + Compose V2** \-- برای بک‌اند پیش‌فرض سندباکس عامل
  4. **Node.js 24 + pnpm** \-- وابستگی‌های زمان اجرا (Node 22 LTS، در حال حاضر `22.16+`، همچنان پشتیبانی می‌شود)
  5. **OpenClaw** \-- مبتنی بر میزبان، نه کانتینری‌شده
  6. **سرویس Systemd** \-- شروع خودکار با سخت‌سازی امنیتی


## راه‌اندازی پس از نصب

* ### به کاربر openclaw بروید

bashCopy code
[code]
    sudo -i -u openclaw
[/code]

* ### ویزارد آغاز به کار را اجرا کنید

اسکریپت پس از نصب شما را در پیکربندی تنظیمات OpenClaw راهنمایی می‌کند.

* ### ارائه‌دهندگان پیام‌رسانی را وصل کنید

به WhatsApp، Telegram، Discord یا Signal وارد شوید:

bashCopy code
[code]
    openclaw channels login
[/code]

* ### نصب را بررسی کنید

bashCopy code
[code]
    sudo systemctl status openclawsudo journalctl -u openclaw -f
[/code]

* ### به Tailscale وصل شوید

برای دسترسی راه دور امن، به مش VPN خود بپیوندید.

### فرمان‌های سریع

bashCopy code
[code]
    # Check service statussudo systemctl status openclaw # View live logssudo journalctl -u openclaw -f # Restart gatewaysudo systemctl restart openclaw # Provider login (run as openclaw user)sudo -i -u openclawopenclaw channels login
[/code]

## معماری امنیتی

استقرار از یک مدل دفاعی ۴ لایه استفاده می‌کند:

  1. **فایروال (UFW)** \-- فقط SSH (22) + Tailscale (41641/udp) به‌صورت عمومی در معرض دسترس است
  2. **VPN (Tailscale)** \-- Gateway فقط از طریق مش VPN در دسترس است
  3. **ایزوله‌سازی Docker** \-- زنجیره iptables با نام DOCKER-USER از در معرض قرار گرفتن پورت‌های خارجی جلوگیری می‌کند
  4. **سخت‌سازی Systemd** \-- NoNewPrivileges، PrivateTmp، کاربر بدون امتیاز


برای بررسی سطح حمله خارجی خود:

bashCopy code
[code]
    nmap -p- YOUR_SERVER_IP
[/code]

فقط پورت 22 (SSH) باید باز باشد. همه سرویس‌های دیگر (Gateway، Docker) قفل شده‌اند.

Docker برای سندباکس‌های عامل نصب می‌شود (اجرای ایزوله ابزار)، نه برای اجرای خود Gateway. برای پیکربندی سندباکس، [سندباکس و ابزارهای چندعاملی](</fa/tools/multi-agent-sandbox-tools>) را ببینید.

## نصب دستی

اگر کنترل دستی را به خودکارسازی ترجیح می‌دهید:

* ### پیش‌نیازها را نصب کنید

bashCopy code
[code]
    sudo apt update && sudo apt install -y ansible git
[/code]

* ### مخزن را کلون کنید

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw-ansible.gitcd openclaw-ansible
[/code]

* ### کالکشن‌های Ansible را نصب کنید

bashCopy code
[code]
    ansible-galaxy collection install -r requirements.yml
[/code]

* ### پلی‌بوک را اجرا کنید

bashCopy code
[code]
    ./run-playbook.sh
[/code]

در روش دیگر، مستقیما اجرا کنید و سپس اسکریپت راه‌اندازی را بعدا به‌صورت دستی اجرا کنید:

bashCopy code
[code]
    ansible-playbook playbook.yml --ask-become-pass# Then run: /tmp/openclaw-setup.sh
[/code]

## به‌روزرسانی

نصب‌کننده Ansible، OpenClaw را برای به‌روزرسانی‌های دستی آماده می‌کند. برای جریان استاندارد به‌روزرسانی، [به‌روزرسانی](</fa/install/updating>) را ببینید.

برای اجرای دوباره پلی‌بوک Ansible (برای مثال، برای تغییرات پیکربندی):

bashCopy code
[code]
    cd openclaw-ansible./run-playbook.sh
[/code]

این فرایند idempotent است و اجرای چندباره آن امن است.

## عیب‌یابی

فایروال اتصال من را مسدود می‌کند

  * مطمئن شوید ابتدا می‌توانید از طریق Tailscale VPN دسترسی داشته باشید
  * دسترسی SSH (پورت 22) همیشه مجاز است
  * Gateway طبق طراحی فقط از طریق Tailscale در دسترس است

سرویس شروع نمی‌شود bashCopy code
[code]
    # Check logssudo journalctl -u openclaw -n 100 # Verify permissionssudo ls -la /opt/openclaw # Test manual startsudo -i -u openclawcd ~/openclawopenclaw gateway run
[/code]

مشکلات سندباکس Docker bashCopy code
[code]
    # Verify Docker is runningsudo systemctl status docker # Check sandbox imagesudo docker images | grep openclaw-sandbox # Build sandbox image if missing (requires source checkout)cd /opt/openclaw/openclawsudo -u openclaw ./scripts/sandbox-setup.sh# For npm installs without a source checkout, see# https://docs.openclaw.ai/gateway/sandboxing#images-and-setup
[/code]

ورود ارائه‌دهنده ناموفق است

مطمئن شوید به‌عنوان کاربر `openclaw` اجرا می‌کنید:

bashCopy code
[code]
    sudo -i -u openclawopenclaw channels login
[/code]

## پیکربندی پیشرفته

برای معماری امنیتی دقیق و عیب‌یابی، مخزن openclaw-ansible را ببینید:

  * [معماری امنیتی](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/security.md>)
  * [جزئیات فنی](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/architecture.md>)
  * [راهنمای عیب‌یابی](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/troubleshooting.md>)


## مرتبط

  * [openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>) \-- راهنمای کامل استقرار
  * [Docker](</fa/install/docker>) \-- راه‌اندازی Gateway کانتینری‌شده
  * [سندباکس‌کردن](</fa/gateway/sandboxing>) \-- پیکربندی سندباکس عامل
  * [سندباکس و ابزارهای چندعاملی](</fa/tools/multi-agent-sandbox-tools>) \-- ایزوله‌سازی برای هر عامل


Was this useful?YesNo