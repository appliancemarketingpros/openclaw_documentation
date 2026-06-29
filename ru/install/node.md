---
title: Node.js
source_url: https://docs.openclaw.ai/ru/install/node
scraped_at: 2026-06-29
---

InstallInstall overview

OpenClaw требует **Node 22.19 или новее**. **Node 24 — среда выполнения по умолчанию и рекомендуемая среда** для установок, CI и рабочих процессов выпуска. Node 22 остается поддерживаемым через активную ветку LTS. [Скрипт установки](</ru/install#alternative-install-methods>) автоматически обнаружит и установит Node — эта страница предназначена для случаев, когда вы хотите настроить Node самостоятельно и убедиться, что все подключено правильно (версии, PATH, глобальные установки).

## Проверьте свою версию

bashCopy code
[code]
    node -v
[/code]

Если команда выводит `v24.x.x` или выше, вы используете рекомендуемую версию по умолчанию. Если она выводит `v22.19.x` или выше, вы используете поддерживаемый путь Node 22 LTS, но мы все равно рекомендуем перейти на Node 24, когда это будет удобно. Если Node не установлен или версия слишком старая, выберите способ установки ниже.

## Установите Node

### macOS

**Homebrew** (рекомендуется):

bashCopy code
[code]
    brew install node
[/code]

Или скачайте установщик для macOS с [nodejs.org](<https://nodejs.org/>).

### Linux

**Ubuntu / Debian:**

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt-get install -y nodejs
[/code]

**Fedora / RHEL:**

bashCopy code
[code]
    sudo dnf install nodejs
[/code]

Или используйте менеджер версий (см. ниже).

### Windows

**winget** (рекомендуется):

powershellCopy code
[code]
    winget install OpenJS.NodeJS.LTS
[/code]

**Chocolatey:**

powershellCopy code
[code]
    choco install nodejs-lts
[/code]

Или скачайте установщик для Windows с [nodejs.org](<https://nodejs.org/>).

Using a version manager (nvm, fnm, mise, asdf)

Менеджеры версий позволяют легко переключаться между версиями Node. Популярные варианты:

  * [**fnm**](<https://github.com/Schniz/fnm>) — быстрый, кроссплатформенный
  * [**nvm**](<https://github.com/nvm-sh/nvm>) — широко используется в macOS/Linux
  * [**mise**](<https://mise.jdx.dev/>) — многоязычный (Node, Python, Ruby и т. д.)


Пример с fnm:

bashCopy code
[code]
    fnm install 24fnm use 24
[/code]

## Устранение неполадок

### `openclaw: command not found`

Это почти всегда означает, что глобальный каталог bin npm не находится в вашем PATH.

* ### Find your global npm prefix

bashCopy code
[code]
    npm prefix -g
[/code]

* ### Check if it's on your PATH

bashCopy code
[code]
    echo "$PATH"
[/code]

Найдите в выводе `<npm-prefix>/bin` (macOS/Linux) или `<npm-prefix>` (Windows).

* ### Add it to your shell startup file

### macOS / Linux

Добавьте в `~/.zshrc` или `~/.bashrc`:

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Затем откройте новый терминал (или выполните `rehash` в zsh / `hash -r` в bash).

### Windows

Добавьте вывод `npm prefix -g` в системный PATH через Settings → System → Environment Variables.

### Ошибки разрешений при `npm install -g` (Linux)

Если вы видите ошибки `EACCES`, переключите глобальный префикс npm на каталог, доступный пользователю для записи:

bashCopy code
[code]
    mkdir -p "$HOME/.npm-global"npm config set prefix "$HOME/.npm-global"export PATH="$HOME/.npm-global/bin:$PATH"
[/code]

Добавьте строку `export PATH=...` в `~/.bashrc` или `~/.zshrc`, чтобы сделать изменение постоянным.

## Связанные материалы

  * [Обзор установки](</ru/install>) — все способы установки
  * [Обновление](</ru/install/updating>) — поддержание OpenClaw в актуальном состоянии
  * [Начало работы](</ru/start/getting-started>) — первые шаги после установки


Was this useful?YesNo

Open issue