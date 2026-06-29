---
title: Среда выполнения Docker VM
source_url: https://docs.openclaw.ai/ru/install/docker-vm-runtime
scraped_at: 2026-06-29
---

InstallHosting

Общие шаги среды выполнения для Docker-установок на базе VM, таких как GCP, Hetzner и похожие VPS-провайдеры.

## Встройте обязательные бинарные файлы в образ

Установка бинарных файлов внутри запущенного контейнера — ловушка. Все, что устанавливается во время выполнения, будет потеряно при перезапуске.

Все внешние бинарные файлы, требуемые навыками, должны быть установлены во время сборки образа.

Примеры ниже показывают только три распространенных бинарных файла:

  * `gog` (из `gogcli`) для доступа к Gmail
  * `goplaces` для Google Places
  * `wacli` для WhatsApp


Это примеры, а не полный список. Вы можете установить столько бинарных файлов, сколько нужно, используя тот же шаблон.

Если позже вы добавите новые навыки, зависящие от дополнительных бинарных файлов, необходимо:

  1. Обновить Dockerfile
  2. Пересобрать образ
  3. Перезапустить контейнеры


**Пример Dockerfile**

dockerfileCopy code
[code]
    FROM node:24-bookworm RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/* # Example binary 1: Gmail CLI (gogcli — installs as `gog`)# Copy the current Linux asset URL from https://github.com/steipete/gogcli/releasesRUN curl -L https://github.com/steipete/gogcli/releases/latest/download/gogcli_linux_amd64.tar.gz \  | tar -xzO gog > /usr/local/bin/gog; \  chmod +x /usr/local/bin/gog # Example binary 2: Google Places CLI# Copy the current Linux asset URL from https://github.com/steipete/goplaces/releasesRUN curl -L https://github.com/steipete/goplaces/releases/latest/download/goplaces_linux_amd64.tar.gz \  | tar -xzO goplaces > /usr/local/bin/goplaces; \  chmod +x /usr/local/bin/goplaces # Example binary 3: WhatsApp CLI# Copy the current Linux asset URL from https://github.com/steipete/wacli/releasesRUN curl -L https://github.com/steipete/wacli/releases/latest/download/wacli-linux-amd64.tar.gz \  | tar -xzO wacli > /usr/local/bin/wacli; \  chmod +x /usr/local/bin/wacli # Add more binaries below using the same pattern WORKDIR /appCOPY package.json pnpm-lock.yaml pnpm-workspace.yaml .npmrc ./COPY ui/package.json ./ui/package.jsonCOPY scripts ./scripts RUN corepack enableRUN pnpm install --frozen-lockfile COPY . .RUN pnpm buildRUN pnpm ui:installRUN pnpm ui:build ENV NODE_ENV=production CMD ["node","dist/index.js"]
[/code]

## Сборка и запуск

bashCopy code
[code]
    docker compose builddocker compose up -d openclaw-gateway
[/code]

Если сборка завершается ошибкой `Killed` или `exit code 137` во время `pnpm install --frozen-lockfile`, на VM не хватает памяти. Перед повторной попыткой используйте класс машины большего размера.

Проверьте бинарные файлы:

bashCopy code
[code]
    docker compose exec openclaw-gateway which gogdocker compose exec openclaw-gateway which goplacesdocker compose exec openclaw-gateway which wacli
[/code]

Ожидаемый вывод:

CodeCopy code
[code]
    /usr/local/bin/gog/usr/local/bin/goplaces/usr/local/bin/wacli
[/code]

Проверьте Gateway:

bashCopy code
[code]
    docker compose logs -f openclaw-gateway
[/code]

Ожидаемый вывод:

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:18789
[/code]

## Что где сохраняется

OpenClaw работает в Docker, но Docker не является источником истины. Все долговременное состояние должно переживать перезапуски, пересборки и перезагрузки.

Компонент | Расположение | Механизм сохранения | Примечания  
---|---|---|---  
Конфигурация Gateway | `/home/node/.openclaw/` | Монтирование тома хоста | Включает `openclaw.json`, `.env`  
Профили авторизации моделей | `/home/node/.openclaw/agents/` | Монтирование тома хоста | `agents/<agentId>/agent/auth-profiles.json` (OAuth, API-ключи)  
Ключ профиля авторизации | `/home/node/.config/openclaw/` | Монтирование тома хоста | Локальный ключ шифрования для токенов профиля авторизации OAuth  
Конфигурации навыков | `/home/node/.openclaw/skills/` | Монтирование тома хоста | Состояние уровня навыка  
Рабочая область агента | `/home/node/.openclaw/workspace/` | Монтирование тома хоста | Код и артефакты агента  
Сессия WhatsApp | `/home/node/.openclaw/` | Монтирование тома хоста | Сохраняет вход по QR-коду  
Хранилище ключей Gmail | `/home/node/.openclaw/` | Том хоста + пароль | Требует `GOG_KEYRING_PASSWORD`  
Пакеты Plugin | `/home/node/.openclaw/npm`, `/home/node/.openclaw/git` | Монтирование тома хоста | Корневые каталоги загружаемых пакетов Plugin  
Внешние бинарные файлы | `/usr/local/bin/` | Образ Docker | Должны быть встроены во время сборки  
Среда выполнения Node | Файловая система контейнера | Образ Docker | Пересобирается при каждой сборке образа  
Пакеты ОС | Файловая система контейнера | Образ Docker | Не устанавливайте во время выполнения  
Контейнер Docker | Эфемерный | Перезапускаемый | Можно безопасно удалить  
  
## Обновления

Чтобы обновить OpenClaw на VM:

bashCopy code
[code]
    git pulldocker compose builddocker compose up -d
[/code]

## Связанные материалы

  * [Docker](</ru/install/docker>)
  * [Podman](</ru/install/podman>)
  * [ClawDock](</ru/install/clawdock>)


Was this useful?YesNo

Open issue