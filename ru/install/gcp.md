---
title: GCP
source_url: https://docs.openclaw.ai/ru/install/gcp
scraped_at: 2026-06-29
---

InstallHosting

Запустите постоянный OpenClaw Gateway на VM GCP Compute Engine с помощью Docker, с долговечным состоянием, встроенными бинарными файлами и безопасным поведением при перезапуске.

Если вам нужен «OpenClaw 24/7 примерно за $5-12/мес.», это надежная схема в Google Cloud. Цена зависит от типа машины и региона; выберите самую маленькую VM, подходящую для вашей нагрузки, и увеличьте ее, если столкнетесь с OOM.

## Что мы делаем (простыми словами)?

  * Создаем проект GCP и включаем биллинг
  * Создаем VM Compute Engine
  * Устанавливаем Docker (изолированная среда выполнения приложения)
  * Запускаем OpenClaw Gateway в Docker
  * Сохраняем `~/.openclaw` \+ `~/.openclaw/workspace` на хосте (переживает перезапуски/пересборки)
  * Получаем доступ к Control UI с ноутбука через SSH-туннель


Это смонтированное состояние `~/.openclaw` включает `openclaw.json`, поагентные `agents/<agentId>/agent/auth-profiles.json` и `.env`.

Доступ к Gateway можно получить через:

  * проброс SSH-порта с ноутбука
  * прямую публикацию порта, если вы самостоятельно управляете firewall и токенами


В этом руководстве используется Debian на GCP Compute Engine. Ubuntu также подходит; сопоставьте пакеты соответствующим образом. Общий процесс Docker см. в [Docker](</ru/install/docker>).

* * *

## Быстрый путь (для опытных операторов)

  1. Создайте проект GCP и включите Compute Engine API
  2. Создайте VM Compute Engine (`e2-small`, Debian 12, 20 ГБ)
  3. Подключитесь к VM по SSH
  4. Установите Docker
  5. Клонируйте репозиторий OpenClaw
  6. Создайте постоянные каталоги на хосте
  7. Настройте `.env` и `docker-compose.yml`
  8. Встройте необходимые бинарные файлы, соберите и запустите


* * *

## Что вам понадобится

  * Аккаунт GCP (e2-micro подходит для бесплатного уровня)
  * Установленный gcloud CLI (или Cloud Console)
  * SSH-доступ с вашего ноутбука
  * Базовое умение пользоваться SSH и копированием/вставкой
  * ~20-30 минут
  * Docker и Docker Compose
  * Учетные данные аутентификации модели
  * Необязательные учетные данные провайдеров 
    * QR WhatsApp
    * токен бота Telegram
    * Gmail OAuth


* * *

* ### Install gcloud CLI (or use Console)

**Вариант A: gcloud CLI** (рекомендуется для автоматизации)

Установите с <https://cloud.google.com/sdk/docs/install>

Инициализируйте и выполните аутентификацию:

bashCopy code
[code]
    gcloud initgcloud auth login
[/code]

**Вариант B: Cloud Console**

Все шаги можно выполнить через веб-интерфейс по адресу <https://console.cloud.google.com>

* ### Create a GCP project

**CLI:**

bashCopy code
[code]
    gcloud projects create my-openclaw-project --name="OpenClaw Gateway"gcloud config set project my-openclaw-project
[/code]

Включите биллинг на <https://console.cloud.google.com/billing> (требуется для Compute Engine).

Включите Compute Engine API:

bashCopy code
[code]
    gcloud services enable compute.googleapis.com
[/code]

**Console:**

  1. Перейдите в IAM & Admin > Create Project
  2. Назовите проект и создайте его
  3. Включите биллинг для проекта
  4. Перейдите в APIs & Services > Enable APIs > найдите "Compute Engine API" > Enable


* ### Create the VM

**Типы машин:**

Тип | Характеристики | Стоимость | Примечания  
---|---|---|---  
e2-medium | 2 vCPU, 4 ГБ RAM | ~$25/мес. | Самый надежный вариант для локальных сборок Docker  
e2-small | 2 vCPU, 2 ГБ RAM | ~$12/мес. | Минимально рекомендуется для сборки Docker  
e2-micro | 2 vCPU (общие), 1 ГБ RAM | Доступен в бесплатном уровне | Часто падает при сборке Docker из-за OOM (exit 137)  
  
**CLI:**

bashCopy code
[code]
    gcloud compute instances create openclaw-gateway \  --zone=us-central1-a \  --machine-type=e2-small \  --boot-disk-size=20GB \  --image-family=debian-12 \  --image-project=debian-cloud
[/code]

**Console:**

  1. Перейдите в Compute Engine > VM instances > Create instance
  2. Имя: `openclaw-gateway`
  3. Регион: `us-central1`, зона: `us-central1-a`
  4. Тип машины: `e2-small`
  5. Загрузочный диск: Debian 12, 20 ГБ
  6. Создайте


* ### SSH into the VM

**CLI:**

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a
[/code]

**Console:**

Нажмите кнопку "SSH" рядом с вашей VM на панели Compute Engine.

Примечание: распространение SSH-ключа может занять 1-2 минуты после создания VM. Если соединение отклоняется, подождите и повторите попытку.

* ### Install Docker (on the VM)

bashCopy code
[code]
    sudo apt-get updatesudo apt-get install -y git curl ca-certificatescurl -fsSL https://get.docker.com | sudo shsudo usermod -aG docker $USER
[/code]

Выйдите и войдите снова, чтобы изменение группы вступило в силу:

bashCopy code
[code]
    exit
[/code]

Затем снова подключитесь по SSH:

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a
[/code]

Проверьте:

bashCopy code
[code]
    docker --versiondocker compose version
[/code]

* ### Clone the OpenClaw repository

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclaw
[/code]

Это руководство предполагает, что вы соберете пользовательский образ, чтобы гарантировать сохранность бинарных файлов.

* ### Create persistent host directories

Контейнеры Docker эфемерны. Все долгоживущее состояние должно находиться на хосте.

bashCopy code
[code]
    mkdir -p ~/.openclawmkdir -p ~/.openclaw/workspace
[/code]

* ### Configure environment variables

Создайте `.env` в корне репозитория.

bashCopy code
[code]
    OPENCLAW_IMAGE=openclaw:latestOPENCLAW_GATEWAY_TOKEN=OPENCLAW_GATEWAY_BIND=lanOPENCLAW_GATEWAY_PORT=18789 OPENCLAW_CONFIG_DIR=/home/$USER/.openclawOPENCLAW_WORKSPACE_DIR=/home/$USER/.openclaw/workspace GOG_KEYRING_PASSWORD=XDG_CONFIG_HOME=/home/node/.openclaw
[/code]

Задайте `OPENCLAW_GATEWAY_TOKEN`, если хотите управлять стабильным токеном Gateway через `.env`; иначе настройте `gateway.auth.token` перед тем, как полагаться на клиентов между перезапусками. Если ни один источник не существует, OpenClaw использует токен только для времени выполнения этого запуска. Сгенерируйте пароль keyring и вставьте его в `GOG_KEYRING_PASSWORD`:

bashCopy code
[code]
    openssl rand -hex 32
[/code]

**Не коммитьте этот файл.**

Этот файл `.env` предназначен для переменных окружения контейнера/среды выполнения, таких как `OPENCLAW_GATEWAY_TOKEN`. Сохраненная аутентификация OAuth/API-key для провайдеров находится в смонтированном `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`.

* ### Docker Compose configuration

Создайте или обновите `docker-compose.yml`.

yamlCopy code
[code]
    services:  openclaw-gateway:    image: ${OPENCLAW_IMAGE}    build: .    restart: unless-stopped    env_file:      - .env    environment:      - HOME=/home/node      - NODE_ENV=production      - TERM=xterm-256color      - OPENCLAW_GATEWAY_BIND=${OPENCLAW_GATEWAY_BIND}      - OPENCLAW_GATEWAY_PORT=${OPENCLAW_GATEWAY_PORT}      - OPENCLAW_GATEWAY_TOKEN=${OPENCLAW_GATEWAY_TOKEN}      - GOG_KEYRING_PASSWORD=${GOG_KEYRING_PASSWORD}      - XDG_CONFIG_HOME=${XDG_CONFIG_HOME}      - PATH=/home/linuxbrew/.linuxbrew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin    volumes:      - ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw      - ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace    ports:      # Recommended: keep the Gateway loopback-only on the VM; access via SSH tunnel.      # To expose it publicly, remove the `127.0.0.1:` prefix and firewall accordingly.      - "127.0.0.1:${OPENCLAW_GATEWAY_PORT}:18789"    command:      [        "node",        "dist/index.js",        "gateway",        "--bind",        "${OPENCLAW_GATEWAY_BIND}",        "--port",        "${OPENCLAW_GATEWAY_PORT}",        "--allow-unconfigured",      ]
[/code]

`--allow-unconfigured` предназначен только для удобства начальной настройки и не заменяет корректную конфигурацию Gateway. Все равно настройте аутентификацию (`gateway.auth.token` или пароль) и используйте безопасные настройки bind для вашего развертывания.

* ### Shared Docker VM runtime steps

Используйте общее руководство по среде выполнения для стандартного процесса на хосте Docker:

  * [Встроить необходимые бинарные файлы в образ](</ru/install/docker-vm-runtime#bake-required-binaries-into-the-image>)
  * [Собрать и запустить](</ru/install/docker-vm-runtime#build-and-launch>)
  * [Что и где сохраняется](</ru/install/docker-vm-runtime#what-persists-where>)
  * [Обновления](</ru/install/docker-vm-runtime#updates>)


* ### GCP-specific launch notes

В GCP, если сборка падает с `Killed` или `exit code 137` во время `pnpm install --frozen-lockfile`, VM не хватает памяти. Используйте минимум `e2-small` или `e2-medium` для более надежных первых сборок.

При bind к LAN (`OPENCLAW_GATEWAY_BIND=lan`) настройте доверенный источник браузера перед продолжением:

bashCopy code
[code]
    docker compose run --rm openclaw-cli config set gateway.controlUi.allowedOrigins '["http://127.0.0.1:18789"]' --strict-json
[/code]

Если вы изменили порт Gateway, замените `18789` на настроенный порт.

* ### Access from your laptop

Создайте SSH-туннель для проброса порта Gateway:

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a -- -L 18789:127.0.0.1:18789
[/code]

Откройте в браузере:

`http://127.0.0.1:18789/`

Повторно выведите чистую ссылку на панель:

bashCopy code
[code]
    docker compose run --rm openclaw-cli dashboard --no-open
[/code]

Если UI запрашивает аутентификацию shared-secret, вставьте настроенный токен или пароль в настройки Control UI. Этот процесс Docker по умолчанию записывает токен; если вы переключите конфигурацию контейнера на аутентификацию паролем, используйте этот пароль вместо токена.

Если Control UI показывает `unauthorized` или `disconnected (1008): pairing required`, одобрите устройство браузера:

bashCopy code
[code]
    docker compose run --rm openclaw-cli devices listdocker compose run --rm openclaw-cli devices approve <requestId>
[/code]

Снова нужна справка по общей постоянной сохранности и обновлениям? См. [Docker VM Runtime](</ru/install/docker-vm-runtime#what-persists-where>) и [обновления Docker VM Runtime](</ru/install/docker-vm-runtime#updates>).

* * *

## Устранение неполадок

**SSH-соединение отклонено**

Распространение SSH-ключа может занять 1-2 минуты после создания VM. Подождите и повторите попытку.

**Проблемы с OS Login**

Проверьте свой профиль OS Login:

bashCopy code
[code]
    gcloud compute os-login describe-profile
[/code]

Убедитесь, что у вашего аккаунта есть необходимые разрешения IAM (Compute OS Login или Compute OS Admin Login).

**Недостаточно памяти (OOM)**

Если сборка Docker падает с `Killed` и `exit code 137`, VM была завершена из-за OOM. Перейдите на e2-small (минимум) или e2-medium (рекомендуется для надежных локальных сборок):

bashCopy code
[code]
    # Stop the VM firstgcloud compute instances stop openclaw-gateway --zone=us-central1-a # Change machine typegcloud compute instances set-machine-type openclaw-gateway \  --zone=us-central1-a \  --machine-type=e2-small # Start the VMgcloud compute instances start openclaw-gateway --zone=us-central1-a
[/code]

* * *

## Сервисные аккаунты (лучшая практика безопасности)

Для личного использования ваш стандартный пользовательский аккаунт подходит.

Для автоматизации или CI/CD-пайплайнов создайте отдельный сервисный аккаунт с минимальными разрешениями:

  1. Создайте сервисный аккаунт:

bashCopy code
[code]gcloud iam service-accounts create openclaw-deploy \  --display-name="OpenClaw Deployment"
[/code]

  2. Выдайте роль Compute Instance Admin (или более узкую пользовательскую роль):

bashCopy code
[code]gcloud projects add-iam-policy-binding my-openclaw-project \  --member="serviceAccount:openclaw-deploy@my-openclaw-project.iam.gserviceaccount.com" \  --role="roles/compute.instanceAdmin.v1"
[/code]


Не используйте роль Owner для автоматизации. Применяйте принцип наименьших привилегий.

Подробности о ролях IAM см. на <https://cloud.google.com/iam/docs/understanding-roles>.

* * *

## Следующие шаги

  * Настройте каналы обмена сообщениями: [Каналы](</ru/channels>)
  * Сопрягите локальные устройства как узлы: [Узлы](</ru/nodes>)
  * Настройте Gateway: [Конфигурация Gateway](</ru/gateway/configuration>)


## Связанные материалы

  * [Обзор установки](</ru/install>)
  * [Azure](</ru/install/azure>)
  * [Хостинг VPS](</ru/vps>)


Was this useful?YesNo

Open issue