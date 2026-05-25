---
title: Внутрішні механізми інсталятора
source_url: https://docs.openclaw.ai/uk/install/installer
scraped_at: 2026-05-25
---

OpenClaw постачає три інсталяційні скрипти, які обслуговуються з `openclaw.ai`.

Скрипт | Платформа | Що він робить  
---|---|---  
`install.sh` | macOS / Linux / WSL | За потреби встановлює Node, встановлює OpenClaw через npm (типово) або git і може запустити onboarding.  
`install-cli.sh` | macOS / Linux / WSL | Встановлює Node + OpenClaw у локальний префікс (`~/.openclaw`) у режимах npm або git checkout. Root не потрібен.  
`install.ps1` | Windows (PowerShell) | За потреби встановлює Node, встановлює OpenClaw через npm (типово) або git і може запустити onboarding.  
  
## Швидкі команди

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

## [install.sh](<http://install.sh>)

### Процес ([install.sh](<http://install.sh>))

* ### Визначення ОС

Підтримує macOS і Linux (зокрема WSL). Якщо виявлено macOS, встановлює Homebrew, якщо його немає.

* ### Типово забезпечення Node.js 24

Перевіряє версію Node і за потреби встановлює Node 24 (Homebrew на macOS, скрипти налаштування NodeSource на Linux apt/dnf/yum). OpenClaw все ще підтримує Node 22 LTS, наразі `22.16+`, для сумісності.

* ### Забезпечення Git

Встановлює Git, якщо його немає.

* ### Встановлення OpenClaw

  * метод `npm` (типово): глобальне встановлення npm
  * метод `git`: клонує/оновлює репозиторій, встановлює залежності через pnpm, збирає, а потім встановлює обгортку в `~/.local/bin/openclaw`


* ### Завдання після встановлення

  * Оновлює завантажений сервіс gateway за найкращою спробою (`openclaw gateway install --force`, потім перезапуск)
  * Запускає `openclaw doctor --non-interactive` під час оновлень і git-встановлень (за найкращою спробою)
  * Намагається виконати onboarding, коли це доречно (TTY доступний, onboarding не вимкнено, а перевірки bootstrap/config проходять)
  * Типово встановлює `SHARP_IGNORE_GLOBAL_LIBVIPS=1`


### Виявлення checkout вихідного коду

Якщо запущено всередині checkout OpenClaw (`package.json` \+ `pnpm-workspace.yaml`), скрипт пропонує:

  * використати checkout (`git`), або
  * використати глобальне встановлення (`npm`)


Якщо TTY недоступний і метод встановлення не задано, типово використовується `npm` і виводиться попередження.

Скрипт завершується з кодом `2` у разі недійсного вибору методу або недійсних значень `--install-method`.

### Приклади ([install.sh](<http://install.sh>))

### Типово

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### Пропустити onboarding

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Git-встановлення

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --install-method git
[/code]

### GitHub main через npm

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --version main
[/code]

### Пробний запуск

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --dry-run
[/code]

Довідник прапорців Прапорець | Опис  
---|---  
`--install-method npm|git` | Вибрати метод встановлення (типово: `npm`). Псевдонім: `--method`  
`--npm` | Скорочення для методу npm  
`--git` | Скорочення для методу git. Псевдонім: `--github`  
`--version <version|dist-tag|spec>` | Версія npm, dist-tag або специфікація пакета (типово: `latest`)  
`--beta` | Використати beta dist-tag, якщо доступний, інакше fallback до `latest`  
`--git-dir <path>` | Каталог checkout (типово: `~/openclaw`). Псевдонім: `--dir`  
`--no-git-update` | Пропустити `git pull` для наявного checkout  
`--no-prompt` | Вимкнути підказки  
`--no-onboard` | Пропустити onboarding  
`--onboard` | Увімкнути onboarding  
`--dry-run` | Вивести дії без застосування змін  
`--verbose` | Увімкнути debug-вивід (`set -x`, журнали npm рівня notice)  
`--help` | Показати використання (`-h`)  
Довідник змінних середовища Змінна | Опис  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Метод встановлення  
`OPENCLAW_VERSION=latest|next|main|<semver>|<spec>` | Версія npm, dist-tag або специфікація пакета  
`OPENCLAW_BETA=0|1` | Використати beta, якщо доступна  
`OPENCLAW_GIT_DIR=<path>` | Каталог checkout  
`OPENCLAW_GIT_UPDATE=0|1` | Перемкнути оновлення git  
`OPENCLAW_NO_PROMPT=1` | Вимкнути підказки  
`OPENCLAW_NO_ONBOARD=1` | Пропустити onboarding  
`OPENCLAW_DRY_RUN=1` | Режим пробного запуску  
`OPENCLAW_VERBOSE=1` | Debug-режим  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | Рівень журналювання npm  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | Керування поведінкою sharp/libvips (типово: `1`)  
  
* * *

## [install-cli.sh](<http://install-cli.sh>)

### Процес ([install-cli.sh](<http://install-cli.sh>))

* ### Встановлення локального runtime Node

Завантажує закріплений підтримуваний tarball Node LTS (версія вбудована в скрипт і оновлюється незалежно) до `<prefix>/tools/node-v<version>` і перевіряє SHA-256.

* ### Забезпечення Git

Якщо Git відсутній, намагається встановити через apt/dnf/yum на Linux або Homebrew на macOS.

* ### Встановлення OpenClaw під префіксом

  * метод `npm` (типово): встановлює під префіксом через npm, потім записує обгортку в `<prefix>/bin/openclaw`
  * метод `git`: клонує/оновлює checkout (типово `~/openclaw`) і все одно записує обгортку в `<prefix>/bin/openclaw`


* ### Оновлення завантаженого сервісу gateway

Якщо сервіс gateway уже завантажено з того самого префікса, скрипт запускає `openclaw gateway install --force`, потім `openclaw gateway restart`, і перевіряє працездатність gateway за найкращою спробою.

### Приклади ([install-cli.sh](<http://install-cli.sh>))

### Типово

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

### Власний префікс + версія

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --prefix /opt/openclaw --version latest
[/code]

### Git-встановлення

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --install-method git --git-dir ~/openclaw
[/code]

### JSON-вивід для автоматизації

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### Запустити onboarding

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --onboard
[/code]

Довідник прапорців Прапорець | Опис  
---|---  
`--prefix <path>` | Префікс встановлення (типово: `~/.openclaw`)  
`--install-method npm|git` | Вибрати метод встановлення (типово: `npm`). Псевдонім: `--method`  
`--npm` | Скорочення для методу npm  
`--git`, `--github` | Скорочення для методу git  
`--git-dir <path>` | Каталог git checkout (типово: `~/openclaw`). Псевдонім: `--dir`  
`--version <ver>` | Версія OpenClaw або dist-tag (типово: `latest`)  
`--node-version <ver>` | Версія Node (типово: `22.22.0`)  
`--json` | Виводити події NDJSON  
`--onboard` | Запустити `openclaw onboard` після встановлення  
`--no-onboard` | Пропустити onboarding (типово)  
`--set-npm-prefix` | На Linux примусово задати префікс npm як `~/.npm-global`, якщо поточний префікс недоступний для запису  
`--help` | Показати використання (`-h`)  
Довідник змінних середовища Змінна | Опис  
---|---  
`OPENCLAW_PREFIX=<path>` | Префікс встановлення  
`OPENCLAW_INSTALL_METHOD=git|npm` | Метод встановлення  
`OPENCLAW_VERSION=<ver>` | Версія OpenClaw або dist-tag  
`OPENCLAW_NODE_VERSION=<ver>` | Версія Node  
`OPENCLAW_GIT_DIR=<path>` | Каталог робочої копії Git для git-встановлень  
`OPENCLAW_GIT_UPDATE=0|1` | Перемкнути git-оновлення для наявних робочих копій  
`OPENCLAW_NO_ONBOARD=1` | Пропустити початкове налаштування  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | Рівень журналювання npm  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | Керувати поведінкою sharp/libvips (типово: `1`)  
  
* * *

## install.ps1

### Потік (install.ps1)

* ### Перевірити середовище PowerShell + Windows

Потрібен PowerShell 5+.

* ### Типово забезпечити Node.js 24

Якщо відсутній, намагається встановити через winget, потім Chocolatey, потім Scoop. Node 22 LTS, наразі `22.16+`, залишається підтримуваним для сумісності.

* ### Встановити OpenClaw

  * Метод `npm` (типово): глобальне встановлення npm із вибраним `-Tag`, запущене з доступного для запису тимчасового каталогу інсталятора, тож оболонки, відкриті в захищених папках, як-от `C:\`, усе одно працюють
  * Метод `git`: клонувати/оновити репозиторій, встановити/зібрати за допомогою pnpm і встановити обгортку в `%USERPROFILE%\.local\bin\openclaw.cmd`


* ### Завдання після встановлення

  * Додає потрібний bin-каталог до користувацького PATH, коли це можливо
  * За можливості оновлює завантажений сервіс Gateway (`openclaw gateway install --force`, потім перезапуск)
  * Запускає `openclaw doctor --non-interactive` під час оновлень і git-встановлень (за можливості)


* ### Обробити збої

Встановлення через `iwr ... | iex` і scriptblock повідомляють про завершальну помилку, не закриваючи поточний сеанс PowerShell. Прямі встановлення через `powershell -File` / `pwsh -File` усе ще завершуються з ненульовим кодом для автоматизації.

### Приклади (install.ps1)

### Типово

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

### Git-встановлення

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git
[/code]

### GitHub main через npm

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag main
[/code]

### Власний git-каталог

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git -GitDir "C:\openclaw"
[/code]

### Пробний запуск

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -DryRun
[/code]

### Трасування для налагодження

powershellCopy code
[code]
    # install.ps1 has no dedicated -Verbose flag yet.Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

Довідник прапорців Прапорець | Опис  
---|---  
`-InstallMethod npm|git` | Метод встановлення (типово: `npm`)  
`-Tag <tag|version|spec>` | npm dist-tag, версія або специфікація пакета (типово: `latest`)  
`-GitDir <path>` | Каталог робочої копії (типово: `%USERPROFILE%\openclaw`)  
`-NoOnboard` | Пропустити початкове налаштування  
`-NoGitUpdate` | Пропустити `git pull`  
`-DryRun` | Лише вивести дії  
Довідник змінних середовища Змінна | Опис  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Метод встановлення  
`OPENCLAW_GIT_DIR=<path>` | Каталог робочої копії  
`OPENCLAW_NO_ONBOARD=1` | Пропустити початкове налаштування  
`OPENCLAW_GIT_UPDATE=0` | Вимкнути git pull  
`OPENCLAW_DRY_RUN=1` | Режим пробного запуску  
  
* * *

## CI та автоматизація

Використовуйте неінтерактивні прапорці/змінні середовища для передбачуваних запусків.

### install.sh (неінтерактивний npm)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-prompt --no-onboard
[/code]

### install.sh (неінтерактивний git)

bashCopy code
[code]
    OPENCLAW_INSTALL_METHOD=git OPENCLAW_NO_PROMPT=1 \  curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### install-cli.sh (JSON)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### install.ps1 (пропустити початкове налаштування)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

* * *

## Усунення несправностей

Чому потрібен Git?

Git потрібен для методу встановлення `git`. Для встановлень через `npm` Git усе одно перевіряється/встановлюється, щоб уникнути збоїв `spawn git ENOENT`, коли залежності використовують git URL.

Чому npm отримує EACCES у Linux?

Деякі конфігурації Linux спрямовують глобальний префікс npm на шляхи, що належать root. `install.sh` може перемкнути префікс на `~/.npm-global` і додати експорти PATH до shell rc-файлів (коли ці файли існують).

Проблеми sharp/libvips

Скрипти типово задають `SHARP_IGNORE_GLOBAL_LIBVIPS=1`, щоб уникнути збирання sharp із системним libvips. Щоб перевизначити:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=0 curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

Windows: "npm error spawn git / ENOENT"

Встановіть Git for Windows, знову відкрийте PowerShell і повторно запустіть інсталятор.

Windows: "openclaw is not recognized"

Запустіть `npm config get prefix` і додайте цей каталог до свого користувацького PATH (у Windows суфікс `\bin` не потрібен), потім знову відкрийте PowerShell.

Windows: як отримати докладний вивід інсталятора

`install.ps1` наразі не надає перемикач `-Verbose`. Використовуйте трасування PowerShell для діагностики на рівні скрипта:

powershellCopy code
[code]
    Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

openclaw не знайдено після встановлення

Зазвичай це проблема PATH. Див. [усунення несправностей Node.js](</uk/install/node#troubleshooting>).

## Пов’язане

  * [Огляд встановлення](</uk/install>)
  * [Оновлення](</uk/install/updating>)
  * [Видалення](</uk/install/uninstall>)


Was this useful?YesNo