---
title: Установка
source_url: https://docs.openclaw.ai/ru/install
scraped_at: 2026-06-29
---

InstallInstall overview

## Системные требования

  * **Node 24** (рекомендуется) или Node 22.19+ - установочный скрипт обрабатывает это автоматически
  * **macOS, Linux или Windows** \- пользователи Windows могут начать с нативного приложения Windows Hub, установщика CLI для PowerShell или WSL2 Gateway. См. [Windows](</ru/platforms/windows>).
  * `pnpm` нужен только при сборке из исходного кода


## Рекомендуется: установочный скрипт

Самый быстрый способ установки. Он определяет вашу ОС, при необходимости устанавливает Node, устанавливает OpenClaw и запускает первичную настройку.

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

Чтобы установить без запуска первичной настройки:

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

Все флаги и параметры CI/автоматизации см. в разделе [Внутреннее устройство установщика](</ru/install/installer>).

## Альтернативные способы установки

### Установщик с локальным префиксом (`install-cli.sh`)

Используйте этот вариант, если хотите держать OpenClaw и Node в локальном префиксе, например `~/.openclaw`, без зависимости от общесистемной установки Node:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
[/code]

По умолчанию он поддерживает установку через npm, а также установку из git checkout в рамках того же потока с префиксом. Полная справка: [Внутреннее устройство установщика](</ru/install/installer#install-clish>).

Уже установлено? Переключайтесь между установками из пакета и из git с помощью `openclaw update --channel dev` и `openclaw update --channel stable`. См. [Обновление](</ru/install/updating#switch-between-npm-and-git-installs>).

### npm, pnpm или bun

Если вы уже управляете Node самостоятельно:

### npm

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

### pnpm

bashCopy code
[code]
    pnpm add -g openclaw@latestpnpm approve-builds -gopenclaw onboard --install-daemon
[/code]

### bun

bashCopy code
[code]
    bun add -g openclaw@latestopenclaw onboard --install-daemon
[/code]

### Из исходного кода

Для участников разработки или всех, кто хочет запускать из локального checkout:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm install && pnpm build && pnpm ui:buildpnpm link --globalopenclaw onboard --install-daemon
[/code]

Или пропустите связывание и используйте `pnpm openclaw ...` внутри репозитория. Полные рабочие процессы разработки см. в разделе [Настройка](</ru/start/setup>).

### Установка из checkout основной ветки GitHub

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --install-method git --version main
[/code]

### Контейнеры и менеджеры пакетов

[**Docker** Контейнеризованные или безголовые развертывания. ](</ru/install/docker>) [**Podman** Rootless-альтернатива Docker для контейнеров. ](</ru/install/podman>) [**Nix** Декларативная установка через Nix flake. ](</ru/install/nix>) [**Ansible** Автоматизированная подготовка парка машин. ](</ru/install/ansible>) [**Bun** Использование только CLI через среду выполнения Bun. ](</ru/install/bun>)

## Проверка установки

bashCopy code
[code]
    openclaw --version      # confirm the CLI is availableopenclaw doctor         # check for config issuesopenclaw gateway status # verify the Gateway is running
[/code]

Если после установки нужен управляемый запуск:

  * macOS: LaunchAgent через `openclaw onboard --install-daemon` или `openclaw gateway install`
  * Linux/WSL2: пользовательская служба systemd через те же команды
  * Нативная Windows: сначала Scheduled Task, с резервным элементом входа в пользовательской папке Startup, если создание задачи запрещено


## Хостинг и развертывание

Разверните OpenClaw на облачном сервере или VPS:

[**VPS** Любой Linux VPS. ](</ru/vps>) [**Docker VM** Общие шаги для Docker. ](</ru/install/docker-vm-runtime>) [**Kubernetes** Развертывание K8s. ](</ru/install/kubernetes>) [**Fly.io** Развертывание на Fly.io. ](</ru/install/fly>) [**Hetzner** Развертывание в Hetzner. ](</ru/install/hetzner>) [**GCP** Развертывание в Google Cloud. ](</ru/install/gcp>) [**Azure** Развертывание в Azure. ](</ru/install/azure>) [**Railway** Развертывание в Railway. ](</ru/install/railway>) [**Render** Развертывание в Render. ](</ru/install/render>) [**Northflank** Развертывание в Northflank. ](</ru/install/northflank>)

## Обновление, миграция или удаление

[**Обновление** Поддерживайте OpenClaw в актуальном состоянии. ](</ru/install/updating>) [**Миграция** Перенос на новую машину. ](</ru/install/migrating>) [**Удаление** Полностью удалите OpenClaw. ](</ru/install/uninstall>)

## Устранение неполадок: `openclaw` не найден

Если установка прошла успешно, но `openclaw` не найден в вашем терминале:

bashCopy code
[code]
    node -v           # Node installed?npm prefix -g     # Where are global packages?echo "$PATH"      # Is the global bin dir in PATH?
[/code]

Если `$(npm prefix -g)/bin` отсутствует в вашем `$PATH`, добавьте его в файл запуска вашей оболочки (`~/.zshrc` или `~/.bashrc`):

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Затем откройте новый терминал. Подробнее см. в разделе [Настройка Node](</ru/install/node>).

Was this useful?YesNo

Open issue