---
title: Встановлення
source_url: https://docs.openclaw.ai/uk/install
scraped_at: 2026-05-25
---

## Системні вимоги

  * **Node 24** (рекомендовано) або Node 22.16+ - скрипт інсталятора обробляє це автоматично
  * **macOS, Linux або Windows** \- підтримуються як нативний Windows, так і WSL2; WSL2 стабільніший. Див. [Windows](</uk/platforms/windows>).
  * `pnpm` потрібен лише якщо ви збираєте з вихідного коду


## Рекомендовано: скрипт інсталятора

Найшвидший спосіб інсталяції. Він визначає вашу ОС, інсталює Node за потреби, інсталює OpenClaw і запускає onboarding.

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

Щоб інсталювати без запуску onboarding:

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

Усі прапорці та параметри CI/автоматизації див. у [внутрішніх механізмах інсталятора](</uk/install/installer>).

## Альтернативні способи інсталяції

### Інсталятор із локальним префіксом (`install-cli.sh`)

Використовуйте це, коли хочете тримати OpenClaw і Node у локальному префіксі, такому як `~/.openclaw`, без залежності від системної інсталяції Node:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
[/code]

За замовчуванням він підтримує інсталяції через npm, а також інсталяції з git-checkout у межах того самого потоку з префіксом. Повна довідка: [внутрішні механізми інсталятора](</uk/install/installer#install-clish>).

Уже інстальовано? Перемикайтеся між пакетною та git-інсталяцією за допомогою `openclaw update --channel dev` і `openclaw update --channel stable`. Див. [Оновлення](</uk/install/updating#switch-between-npm-and-git-installs>).

### npm, pnpm або bun

Якщо ви вже самостійно керуєте Node:

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

Усунення несправностей: помилки збірки sharp (npm)

Якщо `sharp` дає збій через глобально інстальований libvips:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw@latest
[/code]

### З вихідного коду

Для контриб’юторів або всіх, хто хоче запускати з локального checkout:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm install && pnpm build && pnpm ui:buildpnpm link --globalopenclaw onboard --install-daemon
[/code]

Або пропустіть link і використовуйте `pnpm openclaw ...` зсередини репозиторію. Повні робочі процеси розробки див. у [Налаштуванні](</uk/start/setup>).

### Інсталяція з GitHub main

bashCopy code
[code]
    npm install -g github:openclaw/openclaw#main
[/code]

### Контейнери та менеджери пакетів

[**Docker** Контейнеризовані або headless-розгортання. ](</uk/install/docker>) [**Podman** Rootless контейнерна альтернатива Docker. ](</uk/install/podman>) [**Nix** Декларативна інсталяція через Nix flake. ](</uk/install/nix>) [**Ansible** Автоматизоване підготовлення fleet. ](</uk/install/ansible>) [**Bun** Використання лише CLI через середовище виконання Bun. ](</uk/install/bun>)

## Перевірка інсталяції

bashCopy code
[code]
    openclaw --version      # confirm the CLI is availableopenclaw doctor         # check for config issuesopenclaw gateway status # verify the Gateway is running
[/code]

Якщо після інсталяції вам потрібен керований запуск:

  * macOS: LaunchAgent через `openclaw onboard --install-daemon` або `openclaw gateway install`
  * Linux/WSL2: користувацька служба systemd через ті самі команди
  * Нативний Windows: спочатку Scheduled Task, із резервним login item у теці Startup для конкретного користувача, якщо створення завдання відхилено


## Хостинг і розгортання

Розгорніть OpenClaw на хмарному сервері або VPS:

[**VPS** [**Docker VM** [**Kubernetes** OPENCLAW_DOCS_MARKER:cardOpen:IHRpdGxlPSJGbHkuaW8iIGhyZWY9Ii91ay9pbnN0YWxsL2ZseSI [Fly.io](<http://Fly.io>) OPENCLAW_DOCS_MARKER:cardClose: [**Hetzner** [**GCP** [**Azure** [**Railway** [**Render** [**Northflank** Оновлення, міграція або деінсталяція [**Оновлення** Підтримуйте OpenClaw в актуальному стані. ](</uk/install/updating>) [**Міграція** Перенесіть на нову машину. ](</uk/install/migrating>) [**Деінсталяція** Повністю видаліть OpenClaw. ](</uk/install/uninstall>) Усунення несправностей: `openclaw` не знайдено Якщо інсталяція успішна, але `openclaw` не знайдено у вашому терміналі: bashCopy code
[code]
    node -v           # Node installed?npm prefix -g     # Where are global packages?echo "$PATH"      # Is the global bin dir in PATH?
[/code]

Якщо `$(npm prefix -g)/bin` немає у вашому `$PATH`, додайте його до startup-файлу вашої shell (`~/.zshrc` або `~/.bashrc`): bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Потім відкрийте новий термінал. Докладніше див. у [Налаштуванні Node](</uk/install/node>). ](</uk/install/northflank>) Was this useful?YesNo ](</uk/install/render>)](</uk/install/railway>)](</uk/install/azure>)](</uk/install/gcp>)](</uk/install/hetzner>)](</uk/install/kubernetes>)](</uk/install/docker-vm-runtime>)](</uk/vps>)