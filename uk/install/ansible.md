---
title: Ansible
source_url: https://docs.openclaw.ai/uk/install/ansible
scraped_at: 2026-05-25
---

Розгорніть OpenClaw на виробничих серверах за допомогою **[openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>)** \-- автоматизованого інсталятора з архітектурою, орієнтованою на безпеку.

## Передумови

Вимога | Подробиці  
---|---  
**OS** | Debian 11+ або Ubuntu 20.04+  
**Доступ** | Права root або sudo  
**Мережа** | Підключення до інтернету для встановлення пакетів  
**Ansible** | 2.14+ (встановлюється автоматично скриптом швидкого старту)  
  
## Що ви отримуєте

  * **Безпека з пріоритетом брандмауера** \-- UFW + ізоляція Docker (доступні лише SSH + Tailscale)
  * **Tailscale VPN** \-- безпечний віддалений доступ без публічного відкриття сервісів
  * **Docker** \-- ізольовані контейнери пісочниці, прив'язки лише до localhost
  * **Багаторівневий захист** \-- 4-рівнева архітектура безпеки
  * **Інтеграція з systemd** \-- автозапуск під час завантаження з посиленням безпеки
  * **Налаштування однією командою** \-- повне розгортання за лічені хвилини


## Швидкий старт

Встановлення однією командою:

bashCopy code
[code]
    curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash
[/code]

## Що встановлюється

Ansible playbook встановлює та налаштовує:

  1. **Tailscale** \-- mesh VPN для безпечного віддаленого доступу
  2. **Брандмауер UFW** \-- лише порти SSH + Tailscale
  3. **Docker CE + Compose V2** \-- для стандартного бекенда пісочниці агента
  4. **Node.js 24 + pnpm** \-- runtime-залежності (Node 22 LTS, зараз `22.16+`, залишається підтримуваним)
  5. **OpenClaw** \-- на основі хоста, без контейнеризації
  6. **Сервіс systemd** \-- автозапуск із посиленням безпеки


## Налаштування після встановлення

* ### Перемкніться на користувача openclaw

bashCopy code
[code]
    sudo -i -u openclaw
[/code]

* ### Запустіть майстер початкового налаштування

Скрипт після встановлення проведе вас через налаштування параметрів OpenClaw.

* ### Підключіть провайдерів повідомлень

Увійдіть у WhatsApp, Telegram, Discord або Signal:

bashCopy code
[code]
    openclaw channels login
[/code]

* ### Перевірте встановлення

bashCopy code
[code]
    sudo systemctl status openclawsudo journalctl -u openclaw -f
[/code]

* ### Підключіться до Tailscale

Приєднайтеся до своєї mesh VPN для безпечного віддаленого доступу.

### Швидкі команди

bashCopy code
[code]
    # Check service statussudo systemctl status openclaw # View live logssudo journalctl -u openclaw -f # Restart gatewaysudo systemctl restart openclaw # Provider login (run as openclaw user)sudo -i -u openclawopenclaw channels login
[/code]

## Архітектура безпеки

Розгортання використовує 4-рівневу модель захисту:

  1. **Брандмауер (UFW)** \-- публічно відкриті лише SSH (22) + Tailscale (41641/udp)
  2. **VPN (Tailscale)** \-- Gateway доступний лише через mesh VPN
  3. **Ізоляція Docker** \-- ланцюжок iptables DOCKER-USER запобігає зовнішньому відкриттю портів
  4. **Посилення systemd** \-- NoNewPrivileges, PrivateTmp, непривілейований користувач


Щоб перевірити зовнішню поверхню атаки:

bashCopy code
[code]
    nmap -p- YOUR_SERVER_IP
[/code]

Відкритим має бути лише порт 22 (SSH). Усі інші сервіси (Gateway, Docker) заблоковані.

Docker встановлюється для пісочниць агентів (ізольоване виконання інструментів), а не для запуску самого Gateway. Див. [Багатоагентна пісочниця та інструменти](</uk/tools/multi-agent-sandbox-tools>) для конфігурації пісочниці.

## Ручне встановлення

Якщо ви віддаєте перевагу ручному контролю над автоматизацією:

* ### Встановіть передумови

bashCopy code
[code]
    sudo apt update && sudo apt install -y ansible git
[/code]

* ### Клонуйте репозиторій

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw-ansible.gitcd openclaw-ansible
[/code]

* ### Встановіть колекції Ansible

bashCopy code
[code]
    ansible-galaxy collection install -r requirements.yml
[/code]

* ### Запустіть playbook

bashCopy code
[code]
    ./run-playbook.sh
[/code]

Або запустіть напряму, а потім вручну виконайте скрипт налаштування:

bashCopy code
[code]
    ansible-playbook playbook.yml --ask-become-pass# Then run: /tmp/openclaw-setup.sh
[/code]

## Оновлення

Інсталятор Ansible налаштовує OpenClaw для ручних оновлень. Див. [Оновлення](</uk/install/updating>) для стандартного процесу оновлення.

Щоб повторно запустити Ansible playbook (наприклад, для змін конфігурації):

bashCopy code
[code]
    cd openclaw-ansible./run-playbook.sh
[/code]

Це ідемпотентно й безпечно для багаторазового запуску.

## Усунення несправностей

Брандмауер блокує моє підключення

  * Спершу переконайтеся, що можете отримати доступ через Tailscale VPN
  * Доступ SSH (порт 22) завжди дозволений
  * Gateway за задумом доступний лише через Tailscale

Сервіс не запускається bashCopy code
[code]
    # Check logssudo journalctl -u openclaw -n 100 # Verify permissionssudo ls -la /opt/openclaw # Test manual startsudo -i -u openclawcd ~/openclawopenclaw gateway run
[/code]

Проблеми з пісочницею Docker bashCopy code
[code]
    # Verify Docker is runningsudo systemctl status docker # Check sandbox imagesudo docker images | grep openclaw-sandbox # Build sandbox image if missing (requires source checkout)cd /opt/openclaw/openclawsudo -u openclaw ./scripts/sandbox-setup.sh# For npm installs without a source checkout, see# https://docs.openclaw.ai/gateway/sandboxing#images-and-setup
[/code]

Вхід до провайдера не вдається

Переконайтеся, що ви працюєте як користувач `openclaw`:

bashCopy code
[code]
    sudo -i -u openclawopenclaw channels login
[/code]

## Розширена конфігурація

Для докладної архітектури безпеки та усунення несправностей див. репозиторій openclaw-ansible:

  * [Архітектура безпеки](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/security.md>)
  * [Технічні подробиці](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/architecture.md>)
  * [Посібник з усунення несправностей](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/troubleshooting.md>)


## Пов'язане

  * [openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>) \-- повний посібник із розгортання
  * [Docker](</uk/install/docker>) \-- налаштування контейнеризованого Gateway
  * [Ізоляція в пісочниці](</uk/gateway/sandboxing>) \-- конфігурація пісочниці агента
  * [Багатоагентна пісочниця та інструменти](</uk/tools/multi-agent-sandbox-tools>) \-- ізоляція для кожного агента


Was this useful?YesNo