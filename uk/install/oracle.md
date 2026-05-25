---
title: Oracle Cloud
source_url: https://docs.openclaw.ai/uk/install/oracle
scraped_at: 2026-05-25
---

Запустіть постійний OpenClaw Gateway на ARM-рівні **Always Free** Oracle Cloud (до 4 OCPU, 24 ГБ RAM, 200 ГБ сховища) безплатно.

## Передумови

  * Обліковий запис Oracle Cloud ([реєстрація](<https://www.oracle.com/cloud/free/>)) -- див. [посібник спільноти з реєстрації](<https://gist.github.com/rssnyder/51e3cfedd730e7dd5f4a816143b25dbd>), якщо виникнуть проблеми
  * Обліковий запис Tailscale (безплатно на [tailscale.com](<https://tailscale.com>))
  * Пара SSH-ключів
  * Приблизно 30 хвилин


## Налаштування

* ### Створіть інстанс OCI

  1. Увійдіть до [Oracle Cloud Console](<https://cloud.oracle.com/>).
  2. Перейдіть до **Compute > Instances > Create Instance**.
  3. Налаштуйте: 
     * **Назва:** `openclaw`
     * **Образ:** Ubuntu 24.04 (aarch64)
     * **Форма:** `VM.Standard.A1.Flex` (Ampere ARM)
     * **OCPU:** 2 (або до 4)
     * **Пам'ять:** 12 ГБ (або до 24 ГБ)
     * **Завантажувальний том:** 50 ГБ (до 200 ГБ безплатно)
     * **SSH-ключ:** додайте свій публічний ключ
  4. Натисніть **Create** і занотуйте публічну IP-адресу.


* ### Підключіться й оновіть систему

bashCopy code
[code]
    ssh ubuntu@YOUR_PUBLIC_IP sudo apt update && sudo apt upgrade -ysudo apt install -y build-essential
[/code]

`build-essential` потрібен для ARM-компіляції деяких залежностей.

* ### Налаштуйте користувача та ім'я хоста

bashCopy code
[code]
    sudo hostnamectl set-hostname openclawsudo passwd ubuntusudo loginctl enable-linger ubuntu
[/code]

Увімкнення linger зберігає роботу користувацьких служб після виходу із системи.

* ### Встановіть Tailscale

bashCopy code
[code]
    curl -fsSL https://tailscale.com/install.sh | shsudo tailscale up --ssh --hostname=openclaw
[/code]

Відтепер підключайтеся через Tailscale: `ssh ubuntu@openclaw`.

* ### Встановіть OpenClaw

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bashsource ~/.bashrc
[/code]

Коли з'явиться запит "How do you want to hatch your bot?", виберіть **Do this later**.

* ### Налаштуйте Gateway

Використовуйте автентифікацію за токеном із Tailscale Serve для безпечного віддаленого доступу.

bashCopy code
[code]
    openclaw config set gateway.bind loopbackopenclaw config set gateway.auth.mode tokenopenclaw doctor --generate-gateway-tokenopenclaw config set gateway.tailscale.mode serveopenclaw config set gateway.trustedProxies '["127.0.0.1"]' systemctl --user restart openclaw-gateway.service
[/code]

`gateway.trustedProxies=["127.0.0.1"]` тут призначено лише для обробки forwarded-IP/local-client локального проксі Tailscale Serve. Це **не** `gateway.auth.mode: "trusted-proxy"`. Маршрути переглядача diff у цьому налаштуванні зберігають fail-closed поведінку: необроблені запити переглядача `127.0.0.1` без заголовків проксі переспрямування можуть повертати `Diff not found`. Використовуйте `mode=file` / `mode=both` для вкладень або навмисно ввімкніть віддалені переглядачі й задайте `plugins.entries.diffs.config.viewerBaseUrl` (або передайте проксі `baseUrl`), якщо потрібні посилання переглядача, якими можна ділитися.

* ### Заблокуйте безпеку VCN

Заблокуйте весь трафік, крім Tailscale, на мережевому периметрі:

  1. Перейдіть до **Networking > Virtual Cloud Networks** у OCI Console.
  2. Натисніть свою VCN, потім **Security Lists > Default Security List**.
  3. **Видаліть** усі правила входу, крім `0.0.0.0/0 UDP 41641` (Tailscale).
  4. Залиште стандартні правила виходу (дозволити весь вихідний трафік).


Це блокує SSH на порту 22, HTTP, HTTPS і все інше на мережевому периметрі. З цього моменту підключатися можна лише через Tailscale.

* ### Перевірте

bashCopy code
[code]
    openclaw --versionsystemctl --user status openclaw-gateway.servicetailscale serve statuscurl http://localhost:18789
[/code]

Отримайте доступ до Control UI з будь-якого пристрою у вашій tailnet:

CodeCopy code
[code]
    https://openclaw.<tailnet-name>.ts.net/
[/code]

Замініть `<tailnet-name>` на назву вашої tailnet (видно в `tailscale status`).

## Перевірте стан безпеки

Коли VCN заблоковано (відкритий лише UDP 41641), а Gateway прив'язано до loopback, публічний трафік блокується на мережевому периметрі, а адміністративний доступ доступний лише з tailnet. Це усуває потребу в кількох традиційних кроках посилення безпеки VPS:

Традиційний крок | Потрібен? | Чому  
---|---|---  
Брандмауер UFW | Ні | VCN блокує трафік до того, як він досягне інстанса.  
fail2ban | Ні | Порт 22 заблоковано на рівні VCN; поверхні для brute-force немає.  
Посилення sshd | Ні | Tailscale SSH не використовує sshd.  
Вимкнення входу root | Ні | Tailscale автентифікує за ідентичністю tailnet, а не системними користувачами.  
Автентифікація лише ключем SSH | Ні | Те саме — ідентичність tailnet замінює системні SSH-ключі.  
Посилення IPv6 | Зазвичай ні | Залежить від налаштувань VCN/підмережі; перевірте, що фактично призначено/відкрито.  
  
Усе ще рекомендовано:

  * `chmod 700 ~/.openclaw`, щоб обмежити дозволи файлів облікових даних.
  * `openclaw security audit` для перевірки стану безпеки, специфічної для OpenClaw.
  * Регулярно виконувати `sudo apt update && sudo apt upgrade` для патчів ОС.
  * Періодично переглядати пристрої в [адміністративній консолі Tailscale](<https://login.tailscale.com/admin>).


Швидкі команди перевірки:

bashCopy code
[code]
    # Confirm no public ports are listeningsudo ss -tlnp | grep -v '127.0.0.1\|::1' # Verify Tailscale SSH is activetailscale status | grep -q 'offers: ssh' && echo "Tailscale SSH active" # Optional: disable sshd entirely once Tailscale SSH is confirmed workingsudo systemctl disable --now ssh
[/code]

## Примітки щодо ARM

Рівень Always Free працює на ARM (`aarch64`). Більшість функцій OpenClaw працюють нормально; невелика кількість нативних бінарних файлів потребує ARM-збірок:

  * Node.js, Telegram, WhatsApp (Baileys): чистий JavaScript, без проблем.
  * Більшість npm-пакетів із нативним кодом: доступні попередньо зібрані артефакти `linux-arm64`.
  * Необов'язкові CLI-помічники (наприклад, Go/Rust-бінарники, що постачаються Skills): перед встановленням перевірте наявність релізу `aarch64` / `linux-arm64`.


Перевірте архітектуру за допомогою `uname -m` (має вивести `aarch64`). Для бінарних файлів без ARM-збірки встановіть із вихідного коду або пропустіть їх.

## Постійність і резервні копії

Стан OpenClaw зберігається в:

  * `~/.openclaw/` — `openclaw.json`, поагентні `auth-profiles.json`, стан каналів/провайдерів і дані сесій.
  * `~/.openclaw/workspace/` — робочий простір агента ([SOUL.md](<http://SOUL.md>), пам'ять, артефакти).


Вони зберігаються після перезавантажень. Щоб створити переносний знімок:

bashCopy code
[code]
    openclaw backup create
[/code]

## Резервний варіант: SSH-тунель

Якщо Tailscale Serve не працює, використайте SSH-тунель зі своєї локальної машини:

bashCopy code
[code]
    ssh -L 18789:127.0.0.1:18789 ubuntu@openclaw
[/code]

Потім відкрийте `http://localhost:18789`.

## Усунення несправностей

**Створення інстанса завершується помилкою ("Out of capacity")** \-- ARM-інстанси безплатного рівня популярні. Спробуйте інший домен доступності або повторіть у години меншого навантаження.

**Tailscale не підключається** \-- Виконайте `sudo tailscale up --ssh --hostname=openclaw --reset`, щоб повторно автентифікуватися.

**Gateway не запускається** \-- Виконайте `openclaw doctor --non-interactive` і перевірте журнали командою `journalctl --user -u openclaw-gateway.service -n 50`.

**Проблеми з ARM-бінарниками** \-- Більшість npm-пакетів працюють на ARM64. Для нативних бінарних файлів шукайте релізи `linux-arm64` або `aarch64`. Перевірте архітектуру за допомогою `uname -m`.

## Наступні кроки

  * [Канали](</uk/channels>) \-- підключіть Telegram, WhatsApp, Discord та інші
  * [Конфігурація Gateway](</uk/gateway/configuration>) \-- усі параметри конфігурації
  * [Оновлення](</uk/install/updating>) \-- підтримуйте OpenClaw в актуальному стані


## Пов'язане

  * [Огляд встановлення](</uk/install>)
  * [GCP](</uk/install/gcp>)
  * [Хостинг VPS](</uk/vps>)


Was this useful?YesNo