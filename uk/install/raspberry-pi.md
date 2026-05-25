---
title: Raspberry Pi
source_url: https://docs.openclaw.ai/uk/install/raspberry-pi
scraped_at: 2026-05-25
---

Запустіть постійний, завжди активний OpenClaw Gateway на Raspberry Pi. Оскільки Pi є лише Gateway (моделі працюють у хмарі через API), навіть скромний Pi добре справляється з навантаженням — типова вартість обладнання становить **$35–80 одноразово** , без щомісячних платежів.

## Сумісність обладнання

Модель Pi | ОЗП | Працює? | Примітки  
---|---|---|---  
Pi 5 | 4/8 ГБ | Найкраще | Найшвидший, рекомендовано.  
Pi 4 | 4 ГБ | Добре | Оптимальний варіант для більшості користувачів.  
Pi 4 | 2 ГБ | OK | Додайте swap.  
Pi 4 | 1 ГБ | Обмежено | Можливо зі swap, мінімальна конфігурація.  
Pi 3B+ | 1 ГБ | Повільно | Працює, але мляво.  
Pi Zero 2 W | 512 МБ | Ні | Не рекомендовано.  
  
**Мінімум:** 1 ГБ ОЗП, 1 ядро, 500 МБ вільного диска, 64-бітна ОС. **Рекомендовано:** 2+ ГБ ОЗП, SD-карта 16+ ГБ (або USB SSD), Ethernet.

## Передумови

  * Raspberry Pi 4 або 5 з 2+ ГБ ОЗП (рекомендовано 4 ГБ)
  * Карта MicroSD (16+ ГБ) або USB SSD (краща продуктивність)
  * Офіційний блок живлення Pi
  * Підключення до мережі (Ethernet або WiFi)
  * 64-бітна Raspberry Pi OS (обов’язково -- не використовуйте 32-бітну)
  * Близько 30 хвилин


## Налаштування

* ### Flash the OS

Використовуйте **Raspberry Pi OS Lite (64-bit)** \-- для headless-сервера робочий стіл не потрібен.

  1. Завантажте [Raspberry Pi Imager](<https://www.raspberrypi.com/software/>).
  2. Виберіть ОС: **Raspberry Pi OS Lite (64-bit)**.
  3. У діалозі налаштувань попередньо задайте: 
     * Ім’я хоста: `gateway-host`
     * Увімкнути SSH
     * Задати ім’я користувача й пароль
     * Налаштувати WiFi (якщо не використовуєте Ethernet)
  4. Запишіть образ на SD-карту або USB-накопичувач, вставте його й завантажте Pi.


* ### Connect via SSH

bashCopy code
[code]
    ssh user@gateway-host
[/code]

* ### Update the system

bashCopy code
[code]
    sudo apt update && sudo apt upgrade -ysudo apt install -y git curl build-essential # Set timezone (important for cron and reminders)sudo timedatectl set-timezone America/Chicago
[/code]

* ### Install Node.js 24

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt install -y nodejsnode --version
[/code]

* ### Add swap (important for 2 GB or less)

bashCopy code
[code]
    sudo fallocate -l 2G /swapfilesudo chmod 600 /swapfilesudo mkswap /swapfilesudo swapon /swapfileecho '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab # Reduce swappiness for low-RAM devicesecho 'vm.swappiness=10' | sudo tee -a /etc/sysctl.confsudo sysctl -p
[/code]

* ### Install OpenClaw

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Дотримуйтеся вказівок майстра. Для headless-пристроїв рекомендовано API-ключі замість OAuth. Telegram — найпростіший канал для початку.

* ### Verify

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### Access the Control UI

На своєму комп’ютері отримайте URL панелі керування з Pi:

bashCopy code
[code]
    ssh user@gateway-host 'openclaw dashboard --no-open'
[/code]

Потім створіть SSH-тунель в іншому терміналі:

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 user@gateway-host
[/code]

Відкрийте надрукований URL у локальному браузері. Для постійного віддаленого доступу див. [інтеграцію Tailscale](</uk/gateway/tailscale>).

## Поради щодо продуктивності

**Використовуйте USB SSD** \-- SD-карти повільні й зношуються. USB SSD суттєво покращує продуктивність. Див. [посібник із USB-завантаження Pi](<https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#usb-mass-storage-boot>).

**Увімкніть кеш компіляції модулів** \-- пришвидшує повторні виклики CLI на малопотужних хостах Pi:

bashCopy code
[code]
    grep -q 'NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache' ~/.bashrc || cat >> ~/.bashrc <<'EOF' # pragma: allowlist secretexport NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cachemkdir -p /var/tmp/openclaw-compile-cacheexport OPENCLAW_NO_RESPAWN=1EOFsource ~/.bashrc
[/code]

**Зменште використання пам’яті** \-- для headless-налаштувань звільніть пам’ять GPU й вимкніть невикористовувані служби:

bashCopy code
[code]
    echo 'gpu_mem=16' | sudo tee -a /boot/config.txtsudo systemctl disable bluetooth
[/code]

**systemd drop-in для стабільних перезапусків** \-- якщо цей Pi здебільшого запускає OpenClaw, додайте service drop-in:

bashCopy code
[code]
    systemctl --user edit openclaw-gateway.service
[/code]

iniCopy code
[code]
    [Service]Environment=OPENCLAW_NO_RESPAWN=1Environment=NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cacheRestart=alwaysRestartSec=2TimeoutStartSec=90
[/code]

Потім `systemctl --user daemon-reload && systemctl --user restart openclaw-gateway.service`. На headless Pi також один раз увімкніть lingering, щоб користувацька служба працювала після виходу з системи: `sudo loginctl enable-linger "$(whoami)"`.

## Рекомендоване налаштування моделі

Оскільки Pi запускає лише Gateway, використовуйте API-моделі, розміщені в хмарі:

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "model": {        "primary": "anthropic/claude-sonnet-4-6",        "fallbacks": ["openai/gpt-5.4-mini"]      }    }  }}
[/code]

Не запускайте локальні LLM на Pi — навіть малі моделі надто повільні, щоб бути корисними. Нехай Claude або GPT виконують роботу моделі.

## Примітки щодо бінарних файлів ARM

Більшість функцій OpenClaw працюють на ARM64 без змін (Node.js, Telegram, WhatsApp/Baileys, Chromium). Бінарні файли, для яких іноді немає ARM-збірок, зазвичай є необов’язковими CLI-інструментами Go/Rust, що постачаються Skills. Перевірте сторінку релізу відсутнього бінарного файла на наявність артефактів `linux-arm64` / `aarch64`, перш ніж переходити до збирання з вихідного коду.

## Постійність і резервні копії

Стан OpenClaw зберігається тут:

  * `~/.openclaw/` — `openclaw.json`, поагентні `auth-profiles.json`, стан каналів/провайдерів, сеанси.
  * `~/.openclaw/workspace/` — робочий простір агента ([SOUL.md](<http://SOUL.md>), пам’ять, артефакти).


Вони зберігаються після перезавантажень. Створіть переносний знімок за допомогою:

bashCopy code
[code]
    openclaw backup create
[/code]

Якщо тримати їх на SSD, продуктивність і довговічність будуть кращими, ніж на SD-карті.

## Усунення несправностей

**Бракує пам’яті** \-- Перевірте, що swap активний, за допомогою `free -h`. Вимкніть невикористовувані служби (`sudo systemctl disable cups bluetooth avahi-daemon`). Використовуйте лише моделі на основі API.

**Повільна продуктивність** \-- Використовуйте USB SSD замість SD-карти. Перевірте обмеження частоти CPU за допомогою `vcgencmd get_throttled` (має повернути `0x0`).

**Служба не запускається** \-- Перевірте журнали за допомогою `journalctl --user -u openclaw-gateway.service --no-pager -n 100` і запустіть `openclaw doctor --non-interactive`. Якщо це headless Pi, також перевірте, що lingering увімкнено: `sudo loginctl enable-linger "$(whoami)"`.

**Проблеми з бінарними файлами ARM** \-- Якщо skill завершується з помилкою "exec format error", перевірте, чи має бінарний файл ARM64-збірку. Перевірте архітектуру за допомогою `uname -m` (має показати `aarch64`).

**Розривається WiFi** \-- Вимкніть керування живленням WiFi: `sudo iwconfig wlan0 power off`.

## Наступні кроки

  * [Канали](</uk/channels>) \-- підключіть Telegram, WhatsApp, Discord та інші
  * [Конфігурація Gateway](</uk/gateway/configuration>) \-- усі параметри конфігурації
  * [Оновлення](</uk/install/updating>) \-- підтримуйте OpenClaw в актуальному стані


## Пов’язане

  * [Огляд встановлення](</uk/install>)
  * [Linux-сервер](</uk/vps>)
  * [Платформи](</uk/platforms>)


Was this useful?YesNo