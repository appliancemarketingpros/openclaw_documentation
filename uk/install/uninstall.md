---
title: Видалення OpenClaw
source_url: https://docs.openclaw.ai/uk/install/uninstall
scraped_at: 2026-05-25
---

Є два шляхи:

  * **Простий шлях** , якщо `openclaw` усе ще встановлено.
  * **Ручне видалення сервісу** , якщо CLI вже немає, але сервіс усе ще працює.


## Простий шлях (CLI усе ще встановлено)

Рекомендовано: скористайтеся вбудованим деінсталятором:

bashCopy code
[code]
    openclaw uninstall
[/code]

Неінтерактивний режим (автоматизація / npx):

bashCopy code
[code]
    openclaw uninstall --all --yes --non-interactivenpx -y openclaw uninstall --all --yes --non-interactive
[/code]

Ручні кроки (той самий результат):

  1. Зупиніть сервіс gateway:

bashCopy code
[code]
    openclaw gateway stop
[/code]

  2. Видаліть сервіс gateway (launchd/systemd/schtasks):

bashCopy code
[code]
    openclaw gateway uninstall
[/code]

  3. Видаліть стан і конфігурацію:

bashCopy code
[code]
    rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
[/code]

Якщо ви встановили `OPENCLAW_CONFIG_PATH` на власне розташування поза каталогом стану, видаліть і цей файл.

  4. Видаліть робочий простір (необов’язково, видаляє файли агента):

bashCopy code
[code]
    rm -rf ~/.openclaw/workspace
[/code]

  5. Видаліть встановлений CLI (виберіть той спосіб, який ви використовували):

bashCopy code
[code]
    npm rm -g openclawpnpm remove -g openclawbun remove -g openclaw
[/code]

  6. Якщо ви встановлювали застосунок macOS:

bashCopy code
[code]
    rm -rf /Applications/OpenClaw.app
[/code]

Примітки:

  * Якщо ви використовували профілі (`--profile` / `OPENCLAW_PROFILE`), повторіть крок 3 для кожного каталогу стану (типові значення — `~/.openclaw-<profile>`).
  * У віддаленому режимі каталог стану розташований на **хості gateway** , тож виконайте кроки 1–4 і там також.


## Ручне видалення сервісу (CLI не встановлено)

Використовуйте цей шлях, якщо сервіс gateway продовжує працювати, але `openclaw` відсутній.

### macOS (launchd)

Типова мітка — `ai.openclaw.gateway` (або `ai.openclaw.<profile>`; застарілі `com.openclaw.*` усе ще можуть існувати):

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.gatewayrm -f ~/Library/LaunchAgents/ai.openclaw.gateway.plist
[/code]

Якщо ви використовували профіль, замініть мітку та ім’я plist на `ai.openclaw.<profile>`. Якщо є, видаліть усі застарілі plist `com.openclaw.*`.

### Linux (користувацький unit systemd)

Типова назва unit — `openclaw-gateway.service` (або `openclaw-gateway-<profile>.service`):

bashCopy code
[code]
    systemctl --user disable --now openclaw-gateway.servicerm -f ~/.config/systemd/user/openclaw-gateway.servicesystemctl --user daemon-reload
[/code]

### Windows (Scheduled Task)

Типова назва завдання — `OpenClaw Gateway` (або `OpenClaw Gateway (<profile>)`). Скрипт завдання розташований у вашому каталозі стану.

powershellCopy code
[code]
    schtasks /Delete /F /TN "OpenClaw Gateway"Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd"
[/code]

Якщо ви використовували профіль, видаліть відповідну назву завдання та `~\.openclaw-<profile>\gateway.cmd`.

## Звичайне встановлення vs checkout з джерела

### Звичайне встановлення ([install.sh](<http://install.sh>) / npm / pnpm / bun)

Якщо ви використовували `https://openclaw.ai/install.sh` або `install.ps1`, CLI було встановлено через `npm install -g openclaw@latest`. Видаліть його за допомогою `npm rm -g openclaw` (або `pnpm remove -g` / `bun remove -g`, якщо встановлювали саме так).

### Checkout з джерела (git clone)

Якщо ви запускаєте з checkout репозиторію (`git clone` \+ `openclaw ...` / `bun run openclaw ...`):

  1. Видаліть сервіс gateway **перед** видаленням репозиторію (скористайтеся простим шляхом вище або ручним видаленням сервісу).
  2. Видаліть каталог репозиторію.
  3. Видаліть стан і робочий простір, як показано вище.


## Пов’язано

  * [Огляд встановлення](</uk/install>)
  * [Посібник з міграції](</uk/install/migrating>)


Was this useful?YesNo