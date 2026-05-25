---
title: GCP
source_url: https://docs.openclaw.ai/uk/install/gcp
scraped_at: 2026-05-25
---

Запустіть постійний OpenClaw Gateway на VM GCP Compute Engine за допомогою Docker, зі стійким станом, вбудованими бінарними файлами та безпечною поведінкою перезапуску.

Якщо вам потрібен "OpenClaw 24/7 за ~$5-12/міс.", це надійне налаштування в Google Cloud. Ціна залежить від типу машини та регіону; виберіть найменшу VM, яка відповідає вашому робочому навантаженню, і масштабуйте її вгору, якщо зіткнетеся з OOM.

## Що ми робимо (простими словами)?

  * Створюємо проєкт GCP і вмикаємо білінг
  * Створюємо VM Compute Engine
  * Встановлюємо Docker (ізольоване середовище виконання застосунку)
  * Запускаємо OpenClaw Gateway у Docker
  * Зберігаємо `~/.openclaw` \+ `~/.openclaw/workspace` на хості (переживає перезапуски/перебудови)
  * Доступаємося до Control UI з вашого ноутбука через SSH-тунель


Цей змонтований стан `~/.openclaw` містить `openclaw.json`, окремий для кожного агента `agents/<agentId>/agent/auth-profiles.json` і `.env`.

До Gateway можна отримати доступ через:

  * SSH-переадресацію портів з вашого ноутбука
  * Пряме відкриття порту, якщо ви самостійно керуєте firewall і токенами


У цьому посібнику використовується Debian на GCP Compute Engine. Ubuntu також працює; зіставте пакети відповідно. Для загального процесу Docker див. [Docker](</uk/install/docker>).

* * *

## Швидкий шлях (досвідчені оператори)

  1. Створіть проєкт GCP + увімкніть Compute Engine API
  2. Створіть VM Compute Engine (e2-small, Debian 12, 20GB)
  3. Увійдіть на VM через SSH
  4. Встановіть Docker
  5. Клонуйте репозиторій OpenClaw
  6. Створіть постійні каталоги хоста
  7. Налаштуйте `.env` і `docker-compose.yml`
  8. Вбудуйте потрібні бінарні файли, зберіть і запустіть


* * *

## Що вам потрібно

  * Обліковий запис GCP (підходить free tier для e2-micro)
  * Встановлений gcloud CLI (або використовуйте Cloud Console)
  * SSH-доступ з вашого ноутбука
  * Базова впевненість у роботі з SSH + копіюванням/вставленням
  * ~20-30 хвилин
  * Docker і Docker Compose
  * Облікові дані автентифікації моделі
  * Додаткові облікові дані провайдера 
    * WhatsApp QR
    * Токен бота Telegram
    * Gmail OAuth


* * *

* ### Встановіть gcloud CLI (або використовуйте Console)

**Варіант A: gcloud CLI** (рекомендовано для автоматизації)

Встановіть із <https://cloud.google.com/sdk/docs/install>

Ініціалізуйте й автентифікуйтеся:

bashCopy code
[code]
    gcloud initgcloud auth login
[/code]

**Варіант B: Cloud Console**

Усі кроки можна виконати через веб-UI на <https://console.cloud.google.com>

* ### Створіть проєкт GCP

**CLI:**

bashCopy code
[code]
    gcloud projects create my-openclaw-project --name="OpenClaw Gateway"gcloud config set project my-openclaw-project
[/code]

Увімкніть білінг на <https://console.cloud.google.com/billing> (потрібно для Compute Engine).

Увімкніть Compute Engine API:

bashCopy code
[code]
    gcloud services enable compute.googleapis.com
[/code]

**Console:**

  1. Перейдіть до IAM & Admin > Create Project
  2. Назвіть його та створіть
  3. Увімкніть білінг для проєкту
  4. Перейдіть до APIs & Services > Enable APIs > знайдіть "Compute Engine API" > Enable


* ### Створіть VM

**Типи машин:**

Тип | Характеристики | Вартість | Примітки  
---|---|---|---  
e2-medium | 2 vCPU, 4GB RAM | ~$25/міс. | Найнадійніший варіант для локальних збірок Docker  
e2-small | 2 vCPU, 2GB RAM | ~$12/міс. | Мінімально рекомендовано для збірки Docker  
e2-micro | 2 vCPU (shared), 1GB RAM | Підходить для free tier | Часто завершується помилкою OOM під час збірки Docker (exit 137)  
  
**CLI:**

bashCopy code
[code]
    gcloud compute instances create openclaw-gateway \  --zone=us-central1-a \  --machine-type=e2-small \  --boot-disk-size=20GB \  --image-family=debian-12 \  --image-project=debian-cloud
[/code]

**Console:**

  1. Перейдіть до Compute Engine > VM instances > Create instance
  2. Name: `openclaw-gateway`
  3. Region: `us-central1`, Zone: `us-central1-a`
  4. Machine type: `e2-small`
  5. Boot disk: Debian 12, 20GB
  6. Створіть


* ### Увійдіть на VM через SSH

**CLI:**

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a
[/code]

**Console:**

Натисніть кнопку "SSH" поруч із вашою VM на панелі Compute Engine.

Примітка: поширення SSH-ключа може тривати 1-2 хвилини після створення VM. Якщо з’єднання відхилено, зачекайте й повторіть спробу.

* ### Встановіть Docker (на VM)

bashCopy code
[code]
    sudo apt-get updatesudo apt-get install -y git curl ca-certificatescurl -fsSL https://get.docker.com | sudo shsudo usermod -aG docker $USER
[/code]

Вийдіть і зайдіть знову, щоб зміна групи набула чинності:

bashCopy code
[code]
    exit
[/code]

Потім знову підключіться через SSH:

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a
[/code]

Перевірте:

bashCopy code
[code]
    docker --versiondocker compose version
[/code]

* ### Клонуйте репозиторій OpenClaw

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclaw
[/code]

Цей посібник припускає, що ви збиратимете власний образ, щоб гарантувати збереження бінарних файлів.

* ### Створіть постійні каталоги хоста

Контейнери Docker є ефемерними. Увесь довгоживучий стан має зберігатися на хості.

bashCopy code
[code]
    mkdir -p ~/.openclawmkdir -p ~/.openclaw/workspace
[/code]

* ### Налаштуйте змінні середовища

Створіть `.env` у корені репозиторію.

bashCopy code
[code]
    OPENCLAW_IMAGE=openclaw:latestOPENCLAW_GATEWAY_TOKEN=OPENCLAW_GATEWAY_BIND=lanOPENCLAW_GATEWAY_PORT=18789 OPENCLAW_CONFIG_DIR=/home/$USER/.openclawOPENCLAW_WORKSPACE_DIR=/home/$USER/.openclaw/workspace GOG_KEYRING_PASSWORD=XDG_CONFIG_HOME=/home/node/.openclaw
[/code]

Задайте `OPENCLAW_GATEWAY_TOKEN`, якщо хочете керувати стабільним токеном Gateway через `.env`; інакше налаштуйте `gateway.auth.token`, перш ніж покладатися на клієнтів між перезапусками. Якщо жодного джерела немає, OpenClaw використовує токен лише для часу виконання для цього запуску. Згенеруйте пароль keyring і вставте його в `GOG_KEYRING_PASSWORD`:

bashCopy code
[code]
    openssl rand -hex 32
[/code]

**Не комітьте цей файл.**

Цей файл `.env` призначений для env контейнера/середовища виконання, як-от `OPENCLAW_GATEWAY_TOKEN`. Збережена автентифікація OAuth/API-key провайдерів міститься у змонтованому `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`.

* ### Конфігурація Docker Compose

Створіть або оновіть `docker-compose.yml`.

yamlCopy code
[code]
    services:  openclaw-gateway:    image: ${OPENCLAW_IMAGE}    build: .    restart: unless-stopped    env_file:      - .env    environment:      - HOME=/home/node      - NODE_ENV=production      - TERM=xterm-256color      - OPENCLAW_GATEWAY_BIND=${OPENCLAW_GATEWAY_BIND}      - OPENCLAW_GATEWAY_PORT=${OPENCLAW_GATEWAY_PORT}      - OPENCLAW_GATEWAY_TOKEN=${OPENCLAW_GATEWAY_TOKEN}      - GOG_KEYRING_PASSWORD=${GOG_KEYRING_PASSWORD}      - XDG_CONFIG_HOME=${XDG_CONFIG_HOME}      - PATH=/home/linuxbrew/.linuxbrew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin    volumes:      - ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw      - ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace    ports:      # Recommended: keep the Gateway loopback-only on the VM; access via SSH tunnel.      # To expose it publicly, remove the `127.0.0.1:` prefix and firewall accordingly.      - "127.0.0.1:${OPENCLAW_GATEWAY_PORT}:18789"    command:      [        "node",        "dist/index.js",        "gateway",        "--bind",        "${OPENCLAW_GATEWAY_BIND}",        "--port",        "${OPENCLAW_GATEWAY_PORT}",        "--allow-unconfigured",      ]
[/code]

`--allow-unconfigured` призначений лише для зручності початкового налаштування, це не заміна належної конфігурації Gateway. Усе одно налаштуйте автентифікацію (`gateway.auth.token` або пароль) і використовуйте безпечні параметри прив’язки для вашого розгортання.

* ### Спільні кроки середовища виконання Docker VM

Використовуйте спільний посібник із середовища виконання для типового процесу хоста Docker:

  * [Вбудуйте потрібні бінарні файли в образ](</uk/install/docker-vm-runtime#bake-required-binaries-into-the-image>)
  * [Зберіть і запустіть](</uk/install/docker-vm-runtime#build-and-launch>)
  * [Що де зберігається](</uk/install/docker-vm-runtime#what-persists-where>)
  * [Оновлення](</uk/install/docker-vm-runtime#updates>)


* ### Примітки щодо запуску, специфічні для GCP

У GCP, якщо збірка завершується помилкою `Killed` або `exit code 137` під час `pnpm install --frozen-lockfile`, VM не вистачає пам’яті. Використовуйте щонайменше `e2-small` або `e2-medium` для надійніших перших збірок.

Під час прив’язки до LAN (`OPENCLAW_GATEWAY_BIND=lan`) налаштуйте довірене джерело браузера, перш ніж продовжувати:

bashCopy code
[code]
    docker compose run --rm openclaw-cli config set gateway.controlUi.allowedOrigins '["http://127.0.0.1:18789"]' --strict-json
[/code]

Якщо ви змінили порт Gateway, замініть `18789` на налаштований порт.

* ### Доступ із вашого ноутбука

Створіть SSH-тунель для переадресації порту Gateway:

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a -- -L 18789:127.0.0.1:18789
[/code]

Відкрийте у браузері:

`http://127.0.0.1:18789/`

Повторно виведіть чисте посилання на панель керування:

bashCopy code
[code]
    docker compose run --rm openclaw-cli dashboard --no-open
[/code]

Якщо UI запитує автентифікацію shared-secret, вставте налаштований токен або пароль у налаштування Control UI. Цей процес Docker за замовчуванням записує токен; якщо ви перемкнете конфігурацію контейнера на автентифікацію паролем, використовуйте натомість цей пароль.

Якщо Control UI показує `unauthorized` або `disconnected (1008): pairing required`, схваліть пристрій браузера:

bashCopy code
[code]
    docker compose run --rm openclaw-cli devices listdocker compose run --rm openclaw-cli devices approve <requestId>
[/code]

Знову потрібна довідка щодо спільної стійкості та оновлень? Див. [Середовище виконання Docker VM](</uk/install/docker-vm-runtime#what-persists-where>) і [оновлення середовища виконання Docker VM](</uk/install/docker-vm-runtime#updates>).

* * *

## Усунення несправностей

**SSH-з’єднання відхилено**

Поширення SSH-ключа може тривати 1-2 хвилини після створення VM. Зачекайте й повторіть спробу.

**Проблеми OS Login**

Перевірте свій профіль OS Login:

bashCopy code
[code]
    gcloud compute os-login describe-profile
[/code]

Переконайтеся, що ваш обліковий запис має потрібні дозволи IAM (Compute OS Login або Compute OS Admin Login).

**Брак пам’яті (OOM)**

Якщо збірка Docker завершується помилкою `Killed` і `exit code 137`, VM було завершено через OOM. Оновіть до e2-small (мінімум) або e2-medium (рекомендовано для надійних локальних збірок):

bashCopy code
[code]
    # Stop the VM firstgcloud compute instances stop openclaw-gateway --zone=us-central1-a # Change machine typegcloud compute instances set-machine-type openclaw-gateway \  --zone=us-central1-a \  --machine-type=e2-small # Start the VMgcloud compute instances start openclaw-gateway --zone=us-central1-a
[/code]

* * *

## Сервісні облікові записи (найкраща практика безпеки)

Для особистого використання ваш стандартний обліковий запис користувача підходить добре.

Для автоматизації або CI/CD-конвеєрів створіть окремий сервісний обліковий запис із мінімальними дозволами:

  1. Створіть сервісний обліковий запис:

bashCopy code
[code]gcloud iam service-accounts create openclaw-deploy \  --display-name="OpenClaw Deployment"
[/code]

  2. Надайте роль Compute Instance Admin (або вужчу власну роль):

bashCopy code
[code]gcloud projects add-iam-policy-binding my-openclaw-project \  --member="serviceAccount:openclaw-deploy@my-openclaw-project.iam.gserviceaccount.com" \  --role="roles/compute.instanceAdmin.v1"
[/code]


Уникайте використання ролі Owner для автоматизації. Дотримуйтеся принципу найменших привілеїв.

Деталі ролей IAM див. на <https://cloud.google.com/iam/docs/understanding-roles>.

* * *

## Наступні кроки

  * Налаштуйте канали обміну повідомленнями: [Канали](</uk/channels>)
  * Спарте локальні пристрої як вузли: [Вузли](</uk/nodes>)
  * Налаштуйте Gateway: [Конфігурація Gateway](</uk/gateway/configuration>)


## Пов’язане

  * [Огляд встановлення](</uk/install>)
  * [Azure](</uk/install/azure>)
  * [VPS-хостинг](</uk/vps>)


Was this useful?YesNo