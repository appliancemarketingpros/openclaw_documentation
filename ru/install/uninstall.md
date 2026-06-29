---
title: Удаление
source_url: https://docs.openclaw.ai/ru/install/uninstall
scraped_at: 2026-06-29
---

InstallMaintenance

Два пути:

  * **Простой путь** , если `openclaw` все еще установлен.
  * **Ручное удаление службы** , если CLI удален, но служба все еще работает.


## Простой путь (CLI все еще установлен)

Рекомендуется: используйте встроенный деинсталлятор:

bashCopy code
[code]
    openclaw uninstall
[/code]

При использовании CLI удаление состояния сохраняет настроенные каталоги рабочих областей, если вы также не выберете `--workspace`.

Предварительно посмотреть, что будет удалено (безопасно):

bashCopy code
[code]
    openclaw uninstall --dry-run --all
[/code]

Неинтерактивно (автоматизация / npx). Используйте с осторожностью и только после подтверждения областей удаления:

bashCopy code
[code]
    openclaw uninstall --all --yes --non-interactivenpx -y openclaw uninstall --all --yes --non-interactive
[/code]

Ручные шаги (тот же результат):

  1. Остановите службу Gateway:

bashCopy code
[code]
    openclaw gateway stop
[/code]

  2. Удалите службу Gateway (launchd/systemd/schtasks):

bashCopy code
[code]
    openclaw gateway uninstall
[/code]

  3. Удалите состояние и конфигурацию:

bashCopy code
[code]
    rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
[/code]

Если вы задали `OPENCLAW_CONFIG_PATH` в пользовательском расположении вне каталога состояния, удалите и этот файл. Если вы хотите сохранить рабочую область внутри каталога состояния, например `~/.openclaw/workspace`, переместите ее в сторону перед запуском `rm -rf` или удалите содержимое состояния выборочно.

  4. Удалите рабочую область (необязательно, удаляет файлы агентов):

bashCopy code
[code]
    rm -rf ~/.openclaw/workspace
[/code]

  5. Удалите установленный CLI (выберите тот вариант, который использовали):

bashCopy code
[code]
    npm rm -g openclawpnpm remove -g openclawbun remove -g openclaw
[/code]

  6. Если вы установили приложение macOS:

bashCopy code
[code]
    rm -rf /Applications/OpenClaw.app
[/code]

Примечания:

  * Если вы использовали профили (`--profile` / `OPENCLAW_PROFILE`), повторите шаг 3 для каждого каталога состояния (по умолчанию это `~/.openclaw-<profile>`).
  * В удаленном режиме каталог состояния находится на **хосте Gateway** , поэтому выполните шаги 1-4 и там.


## Ручное удаление службы (CLI не установлен)

Используйте это, если служба Gateway продолжает работать, но `openclaw` отсутствует.

### macOS (launchd)

Метка по умолчанию: `ai.openclaw.gateway` (или `ai.openclaw.<profile>`; устаревшие `com.openclaw.*` могут все еще существовать):

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.gatewayrm -f ~/Library/LaunchAgents/ai.openclaw.gateway.plist
[/code]

Если вы использовали профиль, замените метку и имя plist на `ai.openclaw.<profile>`. Удалите все устаревшие plist `com.openclaw.*`, если они есть.

### Linux (пользовательский unit systemd)

Имя unit по умолчанию: `openclaw-gateway.service` (или `openclaw-gateway-<profile>.service`):

bashCopy code
[code]
    systemctl --user disable --now openclaw-gateway.servicerm -f ~/.config/systemd/user/openclaw-gateway.servicesystemctl --user daemon-reload
[/code]

### Windows (запланированная задача)

Имя задачи по умолчанию: `OpenClaw Gateway` (или `OpenClaw Gateway (<profile>)`). Скрипт задачи находится в каталоге состояния как `gateway.cmd`; текущие установки могут также создавать средство запуска `gateway.vbs` без окна, которое Планировщик заданий запускает вместо прямого открытия `gateway.cmd`.

powershellCopy code
[code]
    schtasks /Delete /F /TN "OpenClaw Gateway"Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd" -ErrorAction SilentlyContinueRemove-Item -Force "$env:USERPROFILE\.openclaw\gateway.vbs" -ErrorAction SilentlyContinue
[/code]

Если вы использовали профиль, удалите соответствующее имя задачи и файлы `gateway.cmd` / `gateway.vbs` в `~\.openclaw-<profile>`.

## Обычная установка и checkout исходного кода

### Обычная установка (install.sh / npm / pnpm / bun)

Если вы использовали `https://openclaw.ai/install.sh` или `install.ps1`, CLI был установлен через `npm install -g openclaw@latest`. Удалите его командой `npm rm -g openclaw` (или `pnpm remove -g` / `bun remove -g`, если вы устанавливали этим способом).

### Checkout исходного кода (git clone)

Если вы запускаете из checkout репозитория (`git clone` \+ `openclaw ...` / `bun run openclaw ...`):

  1. Удалите службу Gateway **до** удаления репозитория (используйте простой путь выше или ручное удаление службы).
  2. Удалите каталог репозитория.
  3. Удалите состояние и рабочую область, как показано выше.


## Связанное

  * [Обзор установки](</ru/install>)
  * [Руководство по миграции](</ru/install/migrating>)


Was this useful?YesNo

Open issue