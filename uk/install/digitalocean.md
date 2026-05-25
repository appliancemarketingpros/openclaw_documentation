---
title: DigitalOcean
source_url: https://docs.openclaw.ai/uk/install/digitalocean
scraped_at: 2026-05-25
---

Запустіть постійний OpenClaw Gateway на DigitalOcean Droplet (~$6/місяць за план Basic на 1 GB).

DigitalOcean — найпростіший платний шлях із VPS. Якщо ви віддаєте перевагу дешевшим або безкоштовним варіантам:

  * [Hetzner](</uk/install/hetzner>) — €3.79/міс., більше ядер/RAM за ті самі гроші.
  * [Oracle Cloud](</uk/install/oracle>) — Always Free ARM (до 4 OCPU, 24 GB RAM), але реєстрація може бути примхливою, і доступний лише ARM.


## Передумови

  * Обліковий запис DigitalOcean ([реєстрація](<https://cloud.digitalocean.com/registrations/new>))
  * Пара SSH-ключів (або готовність використовувати автентифікацію паролем)
  * Близько 20 хвилин


## Налаштування

* ### Створіть Droplet

  1. Увійдіть у [DigitalOcean](<https://cloud.digitalocean.com/>).
  2. Натисніть **Create > Droplets**.
  3. Виберіть: 
     * **Регіон:** найближчий до вас
     * **Образ:** Ubuntu 24.04 LTS
     * **Розмір:** Basic, Regular, 1 vCPU / 1 GB RAM / 25 GB SSD
     * **Автентифікація:** SSH-ключ (рекомендовано) або пароль
  4. Натисніть **Create Droplet** і запишіть IP-адресу.


* ### Підключіться та встановіть

bashCopy code
[code]
    ssh root@YOUR_DROPLET_IP apt update && apt upgrade -y # Install Node.js 24curl -fsSL https://deb.nodesource.com/setup_24.x | bash -apt install -y nodejs # Install OpenClawcurl -fsSL https://openclaw.ai/install.sh | bash # Create the non-root user that will own OpenClaw state and services.adduser openclawusermod -aG sudo openclawloginctl enable-linger openclaw su - openclawopenclaw --version
[/code]

Використовуйте root-оболонку лише для системного початкового налаштування. Запускайте команди OpenClaw від імені користувача `openclaw` без прав root, щоб стан зберігався в `/home/openclaw/.openclaw/`, а Gateway встановлювався як systemd-сервіс цього користувача.

* ### Запустіть onboarding

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Майстер проведе вас через автентифікацію моделі, налаштування каналу, генерацію токена Gateway і встановлення демона (systemd).

* ### Додайте swap (рекомендовано для Droplet на 1 GB)

bashCopy code
[code]
    fallocate -l 2G /swapfilechmod 600 /swapfilemkswap /swapfileswapon /swapfileecho '/swapfile none swap sw 0 0' >> /etc/fstab
[/code]

* ### Перевірте Gateway

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### Отримайте доступ до Control UI

Gateway типово прив’язується до loopback. Виберіть один із цих варіантів.

**Варіант A: SSH-тунель (найпростіший)**

bashCopy code
[code]
    # From your local machinessh -L 18789:localhost:18789 root@YOUR_DROPLET_IP
[/code]

Потім відкрийте `http://localhost:18789`.

**Варіант B: Tailscale Serve**

bashCopy code
[code]
    curl -fsSL https://tailscale.com/install.sh | sudo shsudo tailscale upopenclaw config set gateway.tailscale.mode serveopenclaw gateway restart
[/code]

Потім відкрийте `https://<magicdns>/` з будь-якого пристрою у вашому tailnet.

Tailscale Serve автентифікує трафік Control UI та WebSocket через заголовки ідентичності tailnet, що передбачає довіру до самого хоста Gateway. Кінцеві точки HTTP API все одно дотримуються звичайного режиму автентифікації Gateway (токен/пароль). Щоб вимагати явні облікові дані зі спільним секретом через Serve, задайте `gateway.auth.allowTailscale: false` і використовуйте `gateway.auth.mode: "token"` або `"password"`.

**Варіант C: прив’язка tailnet (без Serve)**

bashCopy code
[code]
    openclaw config set gateway.bind tailnetopenclaw gateway restart
[/code]

Потім відкрийте `http://<tailscale-ip>:18789` (потрібен токен).

## Постійність і резервні копії

Стан OpenClaw зберігається в:

  * `~/.openclaw/` — `openclaw.json`, окремі для агентів `auth-profiles.json`, стан каналів/провайдерів і дані сесій.
  * `~/.openclaw/workspace/` — робоча область агента ([SOUL.md](<http://SOUL.md>), пам’ять, артефакти).


Вони зберігаються після перезавантажень Droplet. Щоб створити переносний знімок:

bashCopy code
[code]
    openclaw backup create
[/code]

Знімки DigitalOcean створюють резервну копію всього Droplet; `openclaw backup create` переноситься між хостами.

## Поради для 1 GB RAM

Droplet за $6 має лише 1 GB RAM. Щоб усе працювало плавно:

  * Переконайтеся, що крок зі swap вище є в `/etc/fstab`, щоб він зберігався після перезавантажень.
  * Віддавайте перевагу моделям на основі API (Claude, GPT), а не локальним — локальний LLM inference не поміщається в 1 GB.
  * Задайте `agents.defaults.model.primary` на меншу модель, якщо натрапляєте на OOM на великих промптах.
  * Моніторте через `free -h` і `htop`.


## Усунення несправностей

**Gateway не запускається** \-- Запустіть `openclaw doctor --non-interactive` і перевірте журнали через `journalctl --user -u openclaw-gateway.service -n 50`.

**Порт уже використовується** \-- Запустіть `lsof -i :18789`, щоб знайти процес, а потім зупиніть його.

**Бракує пам’яті** \-- Перевірте, що swap активний, через `free -h`. Якщо OOM все ще трапляється, використовуйте моделі на основі API (Claude, GPT), а не локальні моделі, або перейдіть на Droplet із 2 GB.

## Наступні кроки

  * [Канали](</uk/channels>) \-- підключіть Telegram, WhatsApp, Discord та інші
  * [Конфігурація Gateway](</uk/gateway/configuration>) \-- усі параметри конфігурації
  * [Оновлення](</uk/install/updating>) \-- підтримуйте OpenClaw в актуальному стані


## Пов’язане

  * [Огляд встановлення](</uk/install>)
  * [Fly.io](</uk/install/fly>)
  * [Hetzner](</uk/install/hetzner>)
  * [Хостинг VPS](</uk/vps>)


Was this useful?YesNo