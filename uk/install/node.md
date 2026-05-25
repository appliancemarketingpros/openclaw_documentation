---
title: Node.js
source_url: https://docs.openclaw.ai/uk/install/node
scraped_at: 2026-05-25
---

OpenClaw вимагає **Node 22.16 або новішої версії**. **Node 24 є стандартним і рекомендованим середовищем виконання** для інсталяцій, CI та робочих процесів випуску. Node 22 залишається підтримуваним через активну гілку LTS. [Скрипт інсталятора](</uk/install#alternative-install-methods>) автоматично виявить і встановить Node - ця сторінка призначена для випадків, коли ви хочете налаштувати Node самостійно й переконатися, що все під'єднано правильно (версії, PATH, глобальні інсталяції).

## Перевірте свою версію

bashCopy code
[code]
    node -v
[/code]

Якщо команда виводить `v24.x.x` або вище, ви використовуєте рекомендовану стандартну версію. Якщо вона виводить `v22.16.x` або вище, ви використовуєте підтримуваний шлях Node 22 LTS, але ми все одно рекомендуємо перейти на Node 24, коли буде зручно. Якщо Node не встановлено або версія занадто стара, виберіть спосіб інсталяції нижче.

## Встановіть Node

### macOS

**Homebrew** (рекомендовано):

bashCopy code
[code]
    brew install node
[/code]

Або завантажте інсталятор macOS з [nodejs.org](<https://nodejs.org/>).

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

Або скористайтеся менеджером версій (див. нижче).

### Windows

**winget** (рекомендовано):

powershellCopy code
[code]
    winget install OpenJS.NodeJS.LTS
[/code]

**Chocolatey:**

powershellCopy code
[code]
    choco install nodejs-lts
[/code]

Або завантажте інсталятор Windows з [nodejs.org](<https://nodejs.org/>).

Використання менеджера версій (nvm, fnm, mise, asdf)

Менеджери версій дають змогу легко перемикатися між версіями Node. Популярні варіанти:

  * [**fnm**](<https://github.com/Schniz/fnm>) \- швидкий, кросплатформний
  * [**nvm**](<https://github.com/nvm-sh/nvm>) \- широко використовується на macOS/Linux
  * [**mise**](<https://mise.jdx.dev/>) \- поліглотний (Node, Python, Ruby тощо)


Приклад із fnm:

bashCopy code
[code]
    fnm install 24fnm use 24
[/code]

## Усунення несправностей

### `openclaw: command not found`

Це майже завжди означає, що глобальний bin-каталог npm не додано до вашого PATH.

* ### Знайдіть свій глобальний префікс npm

bashCopy code
[code]
    npm prefix -g
[/code]

* ### Перевірте, чи він є у вашому PATH

bashCopy code
[code]
    echo "$PATH"
[/code]

Знайдіть `<npm-prefix>/bin` (macOS/Linux) або `<npm-prefix>` (Windows) у виводі.

* ### Додайте його до файлу запуску оболонки

### macOS / Linux

Додайте до `~/.zshrc` або `~/.bashrc`:

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Потім відкрийте новий термінал (або виконайте `rehash` у zsh / `hash -r` у bash).

### Windows

Додайте результат `npm prefix -g` до системного PATH через Settings → System → Environment Variables.

### Помилки дозволів під час `npm install -g` (Linux)

Якщо ви бачите помилки `EACCES`, змініть глобальний префікс npm на каталог, доступний користувачу для запису:

bashCopy code
[code]
    mkdir -p "$HOME/.npm-global"npm config set prefix "$HOME/.npm-global"export PATH="$HOME/.npm-global/bin:$PATH"
[/code]

Додайте рядок `export PATH=...` до свого `~/.bashrc` або `~/.zshrc`, щоб зробити це постійним.

## Пов'язане

  * [Огляд інсталяції](</uk/install>) \- усі способи інсталяції
  * [Оновлення](</uk/install/updating>) \- підтримання OpenClaw в актуальному стані
  * [Початок роботи](</uk/start/getting-started>) \- перші кроки після інсталяції


Was this useful?YesNo