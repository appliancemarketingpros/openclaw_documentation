---
title: Linux-сервер
source_url: https://docs.openclaw.ai/uk/vps
scraped_at: 2026-05-25
---

Запустіть OpenClaw Gateway на будь-якому Linux-сервері або хмарному VPS. Ця сторінка допоможе вам вибрати провайдера, пояснює, як працюють хмарні розгортання, і описує загальне налаштування Linux, яке застосовується всюди.

## Виберіть провайдера

[**Railway** [**Northflank** [**DigitalOcean** [**Oracle Cloud** [**Fly.io** [**Hetzner** [**Hostinger** [**GCP** [**Azure** [**exe.dev** [**Raspberry Pi** **AWS (EC2 / Lightsail / free tier)** також добре працює. Покрокове відео від спільноти доступне за адресою [x.com/techfrenAJ/status/2014934471095812547](<https://x.com/techfrenAJ/status/2014934471095812547>) (ресурс спільноти -- може стати недоступним). Як працюють хмарні налаштування

  * **Gateway працює на VPS** і володіє станом + робочим простором.
  * Ви підключаєтеся з ноутбука або телефона через **інтерфейс керування** або **Tailscale/SSH**.
  * Вважайте VPS джерелом істини та регулярно **створюйте резервні копії** стану + робочого простору.
  * Безпечний типовий варіант: залишайте Gateway на loopback і отримуйте доступ через SSH-тунель або Tailscale Serve. Якщо ви прив’язуєтеся до `lan` або `tailnet`, вимагайте `gateway.auth.token` або `gateway.auth.password`.

Пов’язані сторінки: [Віддалений доступ до Gateway](</uk/gateway/remote>), [Центр платформ](</uk/platforms>). Спочатку захистіть адміністративний доступ Перш ніж установлювати OpenClaw на публічний VPS, вирішіть, як ви хочете адмініструвати сам сервер.

  * Якщо вам потрібен адміністративний доступ лише через Tailnet, спочатку встановіть Tailscale, приєднайте VPS до вашого tailnet, перевірте другий SSH-сеанс через IP-адресу Tailscale або ім’я MagicDNS, а потім обмежте публічний SSH.
  * Якщо ви не використовуєте Tailscale, застосуйте еквівалентне посилення захисту для вашого SSH шляху, перш ніж відкривати додаткові сервіси.
  * Це окремо від доступу до Gateway. Ви все ще можете залишити OpenClaw прив’язаним до loopback і використовувати SSH-тунель або Tailscale Serve для панелі керування.

Параметри Gateway, специфічні для Tailscale, описані в [Tailscale](</uk/gateway/tailscale>). Спільний агент компанії на VPS Запуск одного агента для команди є допустимим налаштуванням, коли всі користувачі перебувають в одній зоні довіри, а агент призначений лише для бізнесу.

  * Тримайте його в окремому середовищі виконання (VPS/VM/контейнер + окремий користувач ОС/облікові записи).
  * Не входьте з цього середовища виконання в особисті облікові записи Apple/Google або особисті профілі браузера/менеджера паролів.
  * Якщо користувачі можуть діяти один проти одного, розділіть їх за gateway/хостом/користувачем ОС.

Докладніше про модель безпеки: [Безпека](</uk/gateway/security>). Використання вузлів із VPS Ви можете тримати Gateway у хмарі та спарювати **вузли** на своїх локальних пристроях (Mac/iOS/Android/headless). Вузли надають локальні можливості екрана/камери/canvas і `system.run`, поки Gateway залишається в хмарі. Документація: [Вузли](</uk/nodes>), [CLI вузлів](</uk/cli/nodes>). Налаштування запуску для малих VM і ARM-хостів Якщо CLI-команди виконуються повільно на малопотужних VM (або ARM-хостах), увімкніть кеш компіляції модулів Node: bashCopy code
[code]
    grep -q 'NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache' ~/.bashrc || cat >> ~/.bashrc <<'EOF'export NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cachemkdir -p /var/tmp/openclaw-compile-cacheexport OPENCLAW_NO_RESPAWN=1EOFsource ~/.bashrc
[/code]

  * `NODE_COMPILE_CACHE` покращує час запуску повторних команд.
  * `OPENCLAW_NO_RESPAWN=1` уникає додаткових накладних витрат запуску від шляху самоперезапуску.
  * Перший запуск команди прогріває кеш; наступні запуски швидші.
  * Для особливостей Raspberry Pi див. [Raspberry Pi](</uk/install/raspberry-pi>).

Контрольний список налаштування systemd (необов’язково) Для VM-хостів, які використовують `systemd`, розгляньте:

  * Додайте змінні середовища сервісу для стабільного шляху запуску: 
    * `OPENCLAW_NO_RESPAWN=1`
    * `NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache`
  * Зробіть поведінку перезапуску явною: 
    * `Restart=always`
    * `RestartSec=2`
    * `TimeoutStartSec=90`
  * Надавайте перевагу дискам на SSD для шляхів стану/кешу, щоб зменшити штрафи холодного запуску через випадковий I/O.

Для стандартного шляху `openclaw onboard --install-daemon` відредагуйте користувацький unit: bashCopy code
[code]
    systemctl --user edit openclaw-gateway.service
[/code]

iniCopy code
[code]
    [Service]Environment=OPENCLAW_NO_RESPAWN=1Environment=NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cacheRestart=alwaysRestartSec=2TimeoutStartSec=90
[/code]

Якщо ви навмисно встановили system unit, відредагуйте `openclaw-gateway.service` через `sudo systemctl edit openclaw-gateway.service`. Як політики `Restart=` допомагають автоматизованому відновленню: [systemd може автоматизувати відновлення сервісів](<https://www.redhat.com/en/blog/systemd-automate-recovery>). Про поведінку Linux OOM, вибір дочірнього процесу як жертви та діагностику `exit 137` див. [Тиск пам’яті Linux і OOM-завершення](</uk/platforms/linux#memory-pressure-and-oom-kills>). Пов’язане

  * [Огляд встановлення](</uk/install>)
  * [DigitalOcean](</uk/install/digitalocean>)
  * [Fly.io](</uk/install/fly>)
  * [Hetzner](</uk/install/hetzner>)

](</uk/install/raspberry-pi>) Was this useful?YesNo ](</uk/install/exe-dev>)](</uk/install/azure>)](</uk/install/gcp>)](</uk/install/hostinger>)](</uk/install/hetzner>)](</uk/install/fly>)](</uk/install/oracle>)](</uk/install/digitalocean>)](</uk/install/northflank>)](</uk/install/railway>)