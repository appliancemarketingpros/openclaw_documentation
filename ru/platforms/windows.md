---
title: Windows
source_url: https://docs.openclaw.ai/ru/platforms/windows
scraped_at: 2026-06-29
---

PlatformsPlatforms overview

OpenClaw поставляется с нативным сопутствующим приложением **Windows Hub** и поддержкой Windows CLI. Используйте Windows Hub, если вам нужно настольное приложение с настройкой, статусом в трее, чатом, диагностикой Командного центра и возможностями узла Windows. Используйте установщик PowerShell, если вам нужен CLI/Gateway напрямую. Используйте WSL2, если вам нужна среда выполнения Gateway с максимальной совместимостью с Linux.

## Рекомендуется: Windows Hub

Windows Hub — это нативное сопутствующее приложение WinUI для Windows 10 20H2+ и Windows 11. Оно устанавливается без прав администратора и публикуется с подписанными установщиками x64 и ARM64 в релизах OpenClaw.

Загрузите последнюю стабильную версию установщика со [страницы релизов OpenClaw](<https://github.com/openclaw/openclaw/releases>):

  * [OpenClawCompanion-Setup-x64.exe](<https://github.com/openclaw/openclaw/releases/download/v2026.6.5/OpenClawCompanion-Setup-x64.exe>)
  * [OpenClawCompanion-Setup-arm64.exe](<https://github.com/openclaw/openclaw/releases/download/v2026.6.5/OpenClawCompanion-Setup-arm64.exe>)
  * [Контрольные суммы](<https://github.com/openclaw/openclaw/releases/download/v2026.6.5/OpenClawCompanion-SHA256SUMS.txt>)


Если ссылка для загрузки выше возвращает 404, откройте [страницу релизов](<https://github.com/openclaw/openclaw/releases>) и найдите ресурсы `OpenClawCompanion-Setup-*` в последнем релизе.

После установки запустите **OpenClaw Companion** из меню «Пуск» или системного трея. Установщик также добавляет ярлыки для настройки Gateway, чата, настроек, проверки обновлений и удаления.

### Что включает Windows Hub

  * статус в системном трее и запуск при входе в систему
  * первичная настройка локального WSL Gateway, принадлежащего приложению
  * настройки подключения для локальных, удаленных и SSH-туннелированных Gateway
  * нативное окно чата и доступ к браузерному интерфейсу управления
  * диагностика Командного центра для сеансов, использования, каналов, узлов, сопряжения и команд восстановления
  * режим узла Windows для управляемого агентом холста, экрана, камеры, уведомлений, состояния устройства, преобразования текста в речь, распознавания речи и контролируемого `system.run`
  * режим локального MCP-сервера для MCP-клиентов, таких как Claude Desktop, Claude Code и Cursor


### Первый запуск

При первом запуске Windows Hub открывает настройку, если нет пригодного сохраненного Gateway. Самый быстрый путь — **Настроить локально** : он подготавливает принадлежащий приложению WSL-дистрибутив `OpenClawGateway`, устанавливает в него Gateway и сопрягает приложение. Это не экспортирует и не изменяет ваш существующий дистрибутив Ubuntu.

Выберите **Расширенная настройка** или откройте вкладку «Подключения», если у вас уже есть Gateway. Вы можете подключиться к:

  * локальному Gateway на этом ПК
  * WSL Gateway на этом ПК
  * удаленному Gateway по URL и токену или коду настройки
  * Gateway, доступному через SSH-туннель


Когда настройка завершится, значок в трее станет зеленым. Откройте **Командный центр** из трея, чтобы подтвердить подключение, сопряжение, состояние узла и работоспособность канала.

## Режим узла Windows

Windows Hub может регистрироваться как полноценный узел OpenClaw. После этого агент может использовать объявленные нативные возможности Windows через Gateway.

Распространенные команды:

  * `canvas.present`, `canvas.hide`, `canvas.navigate`, `canvas.eval`, `canvas.snapshot`
  * `screen.snapshot` и, при явном согласии, `screen.record`
  * `camera.list` и, при явном согласии, `camera.snap`, `camera.clip`
  * `system.notify`, `system.run`, `system.run.prepare`, `system.which`
  * `location.get`, `device.info`, `device.status`
  * `stt.transcribe`, `tts.speak`


Для режима узла требуется сопряжение с Gateway. Если приложение показывает запрос на сопряжение, одобрите его на хосте Gateway:

powershellCopy code
[code]
    openclaw devices listopenclaw devices approve <request-id>openclaw nodes status
[/code]

Gateway пересылает только те команды, которые объявляет узел и разрешает политика сервера. Команды, чувствительные к приватности, такие как `screen.record`, `camera.snap` и `camera.clip`, требуют явного включения через `gateway.nodes.allowCommands`.

## Режим локального MCP

Windows Hub может предоставить тот же реестр нативных возможностей Windows как локальный MCP-сервер на loopback. Это полезно, когда вы хотите, чтобы локальные MCP-клиенты управляли возможностями Windows без запущенного OpenClaw Gateway.

Включите его в настройках Windows Hub в разделе для разработчиков/расширенных настроек. После включения сервера приложение показывает loopback-конечную точку и bearer token.

Матрица режимов:

Режим узла | MCP-сервер | Поведение  
---|---|---  
выкл | выкл | Настольное приложение только для оператора  
вкл | выкл | Узел Windows, подключенный к Gateway  
выкл | вкл | Только локальный MCP-сервер  
вкл | вкл | Узел Gateway плюс локальный MCP-сервер  
  
## Нативные Windows CLI и Gateway

Для использования в первую очередь из терминала установите OpenClaw из PowerShell:

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

Проверьте:

powershellCopy code
[code]
    openclaw --versionopenclaw doctoropenclaw gateway status --json
[/code]

Нативные сценарии Windows CLI и Gateway поддерживаются и продолжают улучшаться. Управляемый запуск использует запланированные задачи Windows, когда они доступны. Задача сохраняет читаемый скрипт `gateway.cmd` в каталоге состояния OpenClaw, но запускает его через сгенерированную обертку WScript `gateway.vbs`, чтобы фоновый Gateway не открывал видимое окно консоли. Если создание задачи запрещено, OpenClaw откатывается к элементу входа в папке автозагрузки пользователя.

Чтобы установить службу Gateway:

powershellCopy code
[code]
    openclaw gateway installopenclaw gateway status --json
[/code]

Если вам нужен только CLI без управляемой службы Gateway:

powershellCopy code
[code]
    openclaw onboard --non-interactive --skip-healthopenclaw gateway run
[/code]

## WSL2 Gateway

WSL2 остается средой выполнения Gateway на Windows с максимальной совместимостью с Linux. Windows Hub может настроить для вас WSL Gateway, принадлежащий приложению, или вы можете установить его вручную внутри собственного дистрибутива.

Ручная настройка:

powershellCopy code
[code]
    wsl --install# Or pick a distro explicitly:wsl --list --onlinewsl --install -d Ubuntu-24.04
[/code]

Включите systemd внутри WSL:

bashCopy code
[code]
    sudo tee /etc/wsl.conf >/dev/null <<'EOF'[boot]systemd=trueEOF
[/code]

Перезапустите WSL из PowerShell:

powershellCopy code
[code]
    wsl --shutdown
[/code]

Затем установите OpenClaw внутри WSL, используя краткое руководство для Linux:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bashopenclaw gateway status
[/code]

## Автозапуск Gateway до входа в Windows

Для headless-настроек WSL убедитесь, что вся цепочка загрузки выполняется даже тогда, когда никто не входит в Windows.

Внутри WSL:

bashCopy code
[code]
    sudo apt-get install -y dbus-x11sudo loginctl enable-linger "$(whoami)"openclaw gateway install
[/code]

В PowerShell от имени администратора:

powershellCopy code
[code]
    schtasks /create /tn "WSL Boot" /tr "wsl.exe -d Ubuntu --exec dbus-launch true" /sc onstart /ru "$env:USERNAME"
[/code]

Замените `Ubuntu` именем вашего дистрибутива из:

powershellCopy code
[code]
    wsl --list --verbose
[/code]

> **Примечание:** Два изменения по сравнению со старыми рецептами:
> 
>   * **`dbus-launch true` вместо `/bin/true`** — в WSL ≥ 2.6.1.0 регрессия ([microsoft/WSL #13416](<https://github.com/microsoft/WSL/issues/13416>)) приводит к тому, что дистрибутив завершает работу из-за простоя через 15–20 секунд после выхода последнего клиента, даже при включенном linger. `dbus-launch true` оставляет дочерний процесс init активным как обходной путь ([обсуждение сообщества, microsoft/WSL #9245](<https://github.com/microsoft/WSL/discussions/9245>)).
>   * **`/ru "$env:USERNAME"` вместо `/ru SYSTEM`** — пользовательские WSL-дистрибутивы (настройка по умолчанию) не видны учетной записи SYSTEM; задача выглядит запущенной, но дистрибутив так и не стартует. Запуск от вашей учетной записи позволяет избежать этого. Windows запросит ваш пароль при создании задачи.
> 


После перезагрузки проверьте из WSL:

bashCopy code
[code]
    systemctl --user is-enabled openclaw-gateway.servicesystemctl --user status openclaw-gateway.service --no-pager
[/code]

## Открытие WSL-сервисов в LAN

У WSL есть собственная виртуальная сеть. Если другой машине нужно обратиться к сервису внутри WSL, перенаправьте порт Windows на текущий IP WSL. IP WSL может меняться после перезапусков, поэтому при необходимости обновляйте правило перенаправления.

Пример в PowerShell от имени администратора:

powershellCopy code
[code]
    $Distro = "Ubuntu-24.04"$ListenPort = 2222$TargetPort = 22 $WslIp = (wsl -d $Distro -- hostname -I).Trim().Split(" ")[0]if (-not $WslIp) { throw "WSL IP not found." } netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=$ListenPort `  connectaddress=$WslIp connectport=$TargetPort New-NetFirewallRule -DisplayName "WSL SSH $ListenPort" -Direction Inbound `  -Protocol TCP -LocalPort $ListenPort -Action Allow
[/code]

Примечания:

  * SSH с другой машины должен обращаться к IP хоста Windows, например `ssh user@windows-host -p 2222`.
  * Удаленные узлы должны указывать на доступный URL Gateway, а не на `127.0.0.1`.
  * Используйте `listenaddress=0.0.0.0` для доступа из LAN. Используйте `127.0.0.1` для доступа только локально.


## Устранение неполадок

### Значок в трее не появляется

Проверьте в Диспетчере задач `OpenClaw.Tray.WinUI.exe`. Если он запущен, откройте область скрытых значков трея и закрепите его. Если он не запущен, запустите **OpenClaw Companion** из меню «Пуск».

### Локальная настройка завершается ошибкой

Откройте журнал настройки из Windows Hub или проверьте:

powershellCopy code
[code]
    notepad "$env:LOCALAPPDATA\OpenClawTray\Logs\Setup\easy-setup-latest.txt"
[/code]

Распространенные причины: отключенный WSL, заблокированная виртуализация, устаревшее состояние WSL, принадлежащее приложению, или сбой сети во время установки пакета Gateway.

### Приложение сообщает, что требуется сопряжение

Одобрите запрос оператора или узла из Gateway:

powershellCopy code
[code]
    openclaw devices listopenclaw devices approve <request-id>
[/code]

Если у устройства уже был токен, повторно подключитесь на вкладке «Подключения» после одобрения.

### Веб-чат не может подключиться к удаленному Gateway

Удаленному веб-чату требуется HTTPS или localhost. Для самоподписанных сертификатов доверьте сертификат в Windows или используйте SSH-туннель к localhost URL.

### Команды `screen.snapshot`, камеры или аудио завершаются ошибкой

Проверьте разрешения Windows для камеры, микрофона, захвата экрана и уведомлений. Пакетные установки объявляют защищенные возможности, но Windows все равно может запросить разрешение при первом использовании команды.

### Не удается подключиться к Git или GitHub

Некоторые сети блокируют или ограничивают HTTPS к GitHub. Если `git clone` или `gh auth login` завершается ошибкой, попробуйте другую сеть, VPN или HTTP/HTTPS-прокси.

Для аутентификации `gh` по токену в текущем сеансе:

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token>"gh auth statusgh auth setup-git
[/code]

Никогда не коммитьте токены и не вставляйте их в issues или pull requests.

## Связанные материалы

  * [Обзор установки](</ru/install>)
  * [Настройка Node.js](</ru/install/node>)
  * [Узлы](</ru/nodes>)
  * [Интерфейс управления](</ru/web/control-ui>)
  * [Конфигурация Gateway](</ru/gateway/configuration>)


Was this useful?YesNo

Open issue