---
title: Внутреннее устройство установщика
source_url: https://docs.openclaw.ai/ru/install/installer
scraped_at: 2026-06-29
---

InstallInstall overview

OpenClaw поставляется с тремя скриптами установки, доступными с `openclaw.ai`.

Скрипт | Платформа | Что он делает  
---|---|---  
`install.sh` | macOS / Linux / WSL | Устанавливает Node при необходимости, устанавливает OpenClaw через npm (по умолчанию) или git и может запустить онбординг.  
`install-cli.sh` | macOS / Linux / WSL | Устанавливает Node + OpenClaw в локальный префикс (`~/.openclaw`) в режимах npm или git checkout. Root не требуется.  
`install.ps1` | Windows (PowerShell) | Устанавливает Node при необходимости, устанавливает OpenClaw через npm (по умолчанию) или git и может запустить онбординг.  
  
## Быстрые команды

### install.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --help
[/code]

### install-cli.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --help
[/code]

### install.ps1

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag beta -NoOnboard -DryRun
[/code]

* * *

## install.sh

### Процесс (install.sh)

* ### Определение ОС

Поддерживает macOS и Linux (включая WSL).

* ### Обеспечение Node.js 24 по умолчанию

Проверяет версию Node и устанавливает Node 24 при необходимости (Homebrew на macOS, установочные скрипты NodeSource на Linux apt/dnf/yum). На macOS Homebrew устанавливается только тогда, когда он нужен установщику для Node или Git. OpenClaw по-прежнему поддерживает Node 22 LTS, сейчас `22.19+`, для совместимости. На Alpine/musl Linux установщик использует пакеты apk вместо NodeSource; настроенные репозитории Alpine должны предоставлять Node `22.19+` (Alpine 3.21 или новее на момент написания).

* ### Обеспечение Git

Устанавливает Git, если он отсутствует, с помощью обнаруженного менеджера пакетов, включая Homebrew на macOS и apk на Alpine.

* ### Установка OpenClaw

  * метод `npm` (по умолчанию): глобальная установка npm
  * метод `git`: клонирование/обновление репозитория, установка зависимостей через pnpm, сборка, затем установка обертки в `~/.local/bin/openclaw`


* ### Задачи после установки

  * По возможности обновляет загруженную службу Gateway (`openclaw gateway install --force`, затем перезапуск)
  * Запускает `openclaw doctor --non-interactive` при обновлениях и установках через git (по возможности)
  * Пытается выполнить онбординг, когда это уместно (доступен TTY, онбординг не отключен, проверки bootstrap/config пройдены)


### Обнаружение исходного checkout

Если скрипт запущен внутри checkout OpenClaw (`package.json` \+ `pnpm-workspace.yaml`), он предлагает:

  * использовать checkout (`git`) или
  * использовать глобальную установку (`npm`)


Если TTY недоступен и метод установки не задан, по умолчанию используется `npm` с предупреждением.

Скрипт завершается с кодом `2` при недопустимом выборе метода или недопустимых значениях `--install-method`.

### Примеры (install.sh)

### По умолчанию

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### Пропустить онбординг

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Установка Git

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --install-method git
[/code]

### Checkout GitHub main

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --install-method git --version main
[/code]

### Пробный запуск

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --dry-run
[/code]

Справочник флагов

Флаг | Описание  
---|---  
`--install-method npm|git` | Выбрать метод установки (по умолчанию: `npm`). Псевдоним: `--method`  
`--npm` | Сокращение для метода npm  
`--git` | Сокращение для метода git. Псевдоним: `--github`  
`--version <version|dist-tag|spec>` | Версия npm, dist-tag или спецификация пакета (по умолчанию: `latest`)  
`--beta` | Использовать beta dist-tag, если доступен, иначе откатиться к `latest`  
`--git-dir <path>` | Каталог checkout (по умолчанию: `~/openclaw`). Псевдоним: `--dir`  
`--no-git-update` | Пропустить `git pull` для существующего checkout  
`--no-prompt` | Отключить запросы  
`--no-onboard` | Пропустить онбординг  
`--onboard` | Включить онбординг  
`--dry-run` | Печатать действия без применения изменений  
`--verbose` | Включить отладочный вывод (`set -x`, журналы npm уровня notice)  
`--help` | Показать использование (`-h`)  
  
Справочник переменных окружения

Переменная | Описание  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Метод установки  
`OPENCLAW_VERSION=latest|next|<semver>|<spec>` | Версия npm, dist-tag или спецификация пакета  
`OPENCLAW_BETA=0|1` | Использовать beta, если доступна  
`OPENCLAW_HOME=<path>` | Базовый каталог для состояния OpenClaw и путей git/онбординга по умолчанию  
`OPENCLAW_GIT_DIR=<path>` | Каталог checkout  
`OPENCLAW_GIT_UPDATE=0|1` | Переключить обновления git  
`OPENCLAW_NO_PROMPT=1` | Отключить запросы  
`OPENCLAW_NO_ONBOARD=1` | Пропустить онбординг  
`OPENCLAW_DRY_RUN=1` | Режим пробного запуска  
`OPENCLAW_VERBOSE=1` | Режим отладки  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | Уровень журналирования npm  
  
* * *

## install-cli.sh

### Процесс (install-cli.sh)

* ### Установка локальной среды выполнения Node

Загружает закрепленный поддерживаемый tarball Node LTS (версия встроена в скрипт и обновляется независимо) в `<prefix>/tools/node-v<version>` и проверяет SHA-256. На Alpine/musl Linux, где Node не публикует совместимые tarball для закрепленной среды выполнения, устанавливает `nodejs` и `npm` через `apk` и связывает эту среду выполнения с путем обертки префикса. Репозитории Alpine должны предоставлять Node `22.19+`; используйте Alpine 3.21 или новее, если старые репозитории предоставляют только Node 20 или 21.

* ### Обеспечение Git

Если Git отсутствует, пытается установить его через apt/dnf/yum/apk на Linux или Homebrew на macOS.

* ### Установка OpenClaw под префиксом

  * метод `npm` (по умолчанию): устанавливает под префиксом с помощью npm, затем записывает обертку в `<prefix>/bin/openclaw`
  * метод `git`: клонирует/обновляет checkout (по умолчанию `~/openclaw`) и все равно записывает обертку в `<prefix>/bin/openclaw`


* ### Обновление загруженной службы Gateway

Если служба Gateway уже загружена из того же префикса, скрипт запускает `openclaw gateway install --force`, затем `openclaw gateway restart` и по возможности проверяет работоспособность Gateway.

### Примеры (install-cli.sh)

### По умолчанию

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

### Пользовательский префикс + версия

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --prefix /opt/openclaw --version latest
[/code]

### Установка Git

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --install-method git --git-dir ~/openclaw
[/code]

### JSON-вывод для автоматизации

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### Запустить онбординг

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --onboard
[/code]

Справочник флагов

Флаг | Описание  
---|---  
`--prefix <path>` | Префикс установки (по умолчанию: `~/.openclaw`)  
`--install-method npm|git` | Выбрать метод установки (по умолчанию: `npm`). Псевдоним: `--method`  
`--npm` | Сокращение для метода npm  
`--git`, `--github` | Сокращение для метода git  
`--git-dir <path>` | Каталог checkout Git (по умолчанию: `~/openclaw`). Псевдоним: `--dir`  
`--version <ver>` | Версия OpenClaw или dist-tag (по умолчанию: `latest`)  
`--node-version <ver>` | Версия Node (по умолчанию: `22.22.0`)  
`--json` | Выводить события NDJSON  
`--onboard` | Запустить `openclaw onboard` после установки  
`--no-onboard` | Пропустить онбординг (по умолчанию)  
`--set-npm-prefix` | В Linux принудительно задать префикс npm как `~/.npm-global`, если текущий префикс недоступен для записи  
`--help` | Показать использование (`-h`)  
  
Справочник переменных окружения

Переменная | Описание  
---|---  
`OPENCLAW_PREFIX=<path>` | Префикс установки  
`OPENCLAW_INSTALL_METHOD=git|npm` | Метод установки  
`OPENCLAW_VERSION=<ver>` | Версия OpenClaw или dist-tag  
`OPENCLAW_NODE_VERSION=<ver>` | Версия Node  
`OPENCLAW_HOME=<path>` | Базовый каталог для состояния OpenClaw и путей git/онбординга по умолчанию  
`OPENCLAW_GIT_DIR=<path>` | Каталог checkout Git для установок через git  
`OPENCLAW_GIT_UPDATE=0|1` | Включить или отключить обновления git для существующих checkout  
`OPENCLAW_NO_ONBOARD=1` | Пропустить онбординг  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | Уровень логирования npm  
  
* * *

## install.ps1

### Поток (install.ps1)

* ### Проверить окружение PowerShell + Windows

Требуется PowerShell 5+.

* ### Обеспечить Node.js 24 по умолчанию

Если отсутствует, выполняется попытка установки через winget, затем Chocolatey, затем Scoop. Если менеджер пакетов недоступен, скрипт загружает официальный Windows zip Node.js в `%LOCALAPPDATA%\OpenClaw\deps\portable-node` и добавляет его в PATH текущего процесса и пользователя. Node 22 LTS, сейчас `22.19+`, остается поддерживаемым для совместимости.

* ### Установить OpenClaw

  * Метод `npm` (по умолчанию): глобальная установка npm с выбранным `-Tag`, запускается из доступного для записи временного каталога установщика, поэтому оболочки, открытые в защищенных папках, таких как `C:\`, продолжают работать
  * Метод `git`: клонировать/обновить репозиторий, установить/собрать с pnpm и установить wrapper в `%USERPROFILE%\.local\bin\openclaw.cmd`. Если Git отсутствует, скрипт подготавливает user-local MinGit в `%LOCALAPPDATA%\OpenClaw\deps\portable-git` и добавляет его в PATH текущего процесса и пользователя.


* ### Задачи после установки

  * По возможности добавляет нужный каталог bin в PATH пользователя
  * По мере возможности обновляет загруженную службу Gateway (`openclaw gateway install --force`, затем перезапуск)
  * Запускает `openclaw doctor --non-interactive` при обновлениях и установках через git (по мере возможности)


* ### Обработать сбои

Установки через `iwr ... | iex` и scriptblock сообщают о завершающей ошибке, не закрывая текущий сеанс PowerShell. Прямые установки через `powershell -File` / `pwsh -File` по-прежнему завершаются с ненулевым кодом для автоматизации.

### Примеры (install.ps1)

### По умолчанию

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

### Установка через Git

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git
[/code]

### Checkout GitHub main

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git -Tag main
[/code]

### Пользовательский каталог git

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git -GitDir "C:\openclaw"
[/code]

### Пробный запуск

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -DryRun
[/code]

### Трассировка отладки

powershellCopy code
[code]
    # install.ps1 has no dedicated -Verbose flag yet.Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

Справочник флагов

Флаг | Описание  
---|---  
`-InstallMethod npm|git` | Метод установки (по умолчанию: `npm`)  
`-Tag <tag|version|spec>` | npm dist-tag, версия или спецификация пакета (по умолчанию: `latest`)  
`-GitDir <path>` | Каталог checkout (по умолчанию: `%USERPROFILE%\openclaw`)  
`-NoOnboard` | Пропустить онбординг  
`-NoGitUpdate` | Пропустить `git pull`  
`-DryRun` | Только вывести действия  
  
Справочник переменных окружения

Переменная | Описание  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Метод установки  
`OPENCLAW_GIT_DIR=<path>` | Каталог checkout  
`OPENCLAW_NO_ONBOARD=1` | Пропустить онбординг  
`OPENCLAW_GIT_UPDATE=0` | Отключить git pull  
`OPENCLAW_DRY_RUN=1` | Режим пробного запуска  
  
* * *

## CI и автоматизация

Используйте неинтерактивные флаги/переменные окружения для предсказуемых запусков.

### install.sh (неинтерактивный npm)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-prompt --no-onboard
[/code]

### install.sh (неинтерактивный git)

bashCopy code
[code]
    OPENCLAW_INSTALL_METHOD=git OPENCLAW_NO_PROMPT=1 \  curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### install-cli.sh (JSON)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### install.ps1 (пропуск онбординга)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

* * *

## Устранение неполадок

Почему требуется Git?

Git требуется для метода установки `git`. Для установок через `npm` Git все равно проверяется/устанавливается, чтобы избежать сбоев `spawn git ENOENT`, когда зависимости используют URL git.

Почему npm получает EACCES в Linux?

Некоторые конфигурации Linux указывают глобальный префикс npm на пути, принадлежащие root. `install.sh` может переключить префикс на `~/.npm-global` и добавить экспорты PATH в rc-файлы оболочки (если эти файлы существуют).

Windows: "npm error spawn git / ENOENT"

Повторно запустите установщик, чтобы он мог подготовить user-local MinGit, или установите Git for Windows и заново откройте PowerShell.

Windows: "openclaw is not recognized"

Выполните `npm config get prefix` и добавьте этот каталог в пользовательский PATH (суффикс `\bin` в Windows не нужен), затем заново откройте PowerShell.

Windows: как получить подробный вывод установщика

`install.ps1` сейчас не предоставляет переключатель `-Verbose`. Используйте трассировку PowerShell для диагностики на уровне скрипта:

powershellCopy code
[code]
    Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

openclaw не найден после установки

Обычно это проблема PATH. См. [устранение неполадок Node.js](</ru/install/node#troubleshooting>).

## Связанное

  * [Обзор установки](</ru/install>)
  * [Обновление](</ru/install/updating>)
  * [Удаление](</ru/install/uninstall>)


Was this useful?YesNo

Open issue