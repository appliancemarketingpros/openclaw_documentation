---
title: Windows
source_url: https://docs.openclaw.ai/uk/platforms/windows
scraped_at: 2026-05-25
---

OpenClaw підтримує як **нативний Windows** , так і **WSL2**. WSL2 є стабільнішим шляхом і рекомендований для повного досвіду — CLI, Gateway і інструменти працюють усередині Linux із повною сумісністю. Нативний Windows підходить для базового використання CLI та Gateway, з деякими застереженнями, зазначеними нижче.

Супутні застосунки для нативного Windows заплановані.

## WSL2 (рекомендовано)

  * [Початок роботи](</uk/start/getting-started>) (використовуйте всередині WSL)
  * [Встановлення та оновлення](</uk/install/updating>)
  * Офіційний посібник WSL2 (Microsoft): <https://learn.microsoft.com/windows/wsl/install>


## Стан нативного Windows

Потоки CLI для нативного Windows покращуються, але WSL2 досі є рекомендованим шляхом.

Що добре працює на нативному Windows сьогодні:

  * встановлювач із вебсайту через `install.ps1`
  * локальне використання CLI, як-от `openclaw --version`, `openclaw doctor` і `openclaw plugins list --json`
  * вбудована димова перевірка локального агента/провайдера, наприклад:

powershellCopy code
[code]
    openclaw agent --local --agent main --thinking low -m "Reply with exactly WINDOWS-HATCH-OK."
[/code]

Поточні застереження:

  * `openclaw onboard --non-interactive` досі очікує доступний локальний Gateway, якщо не передати `--skip-health`
  * `openclaw onboard --non-interactive --install-daemon` і `openclaw gateway install` спершу пробують Windows Scheduled Tasks
  * якщо створення Scheduled Task заборонено, OpenClaw повертається до елемента входу в папці автозапуску поточного користувача та одразу запускає Gateway
  * якщо сам `schtasks` зависає або перестає відповідати, OpenClaw тепер швидко перериває цей шлях і переходить до резервного варіанту, замість того щоб зависати назавжди
  * Scheduled Tasks досі бажані, коли доступні, бо вони надають кращий статус супервізора


Якщо вам потрібен лише нативний CLI, без встановлення служби Gateway, використайте один із цих варіантів:

powershellCopy code
[code]
    openclaw onboard --non-interactive --skip-healthopenclaw gateway run
[/code]

Якщо ви хочете керований автозапуск у нативному Windows:

powershellCopy code
[code]
    openclaw gateway installopenclaw gateway status --json
[/code]

Якщо створення Scheduled Task заблоковано, резервний режим служби все одно автоматично запускається після входу через папку автозапуску поточного користувача.

## Gateway

  * [Операційний посібник Gateway](</uk/gateway>)
  * [Конфігурація](</uk/gateway/configuration>)


## Встановлення служби Gateway (CLI)

Усередині WSL2:

CodeCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Або:

CodeCopy code
[code]
    openclaw gateway install
[/code]

Або:

CodeCopy code
[code]
    openclaw configure
[/code]

Виберіть **службу Gateway** , коли з’явиться запит.

Відновлення/міграція:

CodeCopy code
[code]
    openclaw doctor
[/code]

## Автозапуск Gateway до входу в Windows

Для безголових налаштувань переконайтеся, що повний ланцюг завантаження працює навіть тоді, коли ніхто не входить у Windows.

### 1) Підтримуйте роботу користувацьких служб без входу

Усередині WSL:

bashCopy code
[code]
    sudo loginctl enable-linger "$(whoami)"
[/code]

### 2) Встановіть користувацьку службу OpenClaw gateway

Усередині WSL:

bashCopy code
[code]
    openclaw gateway install
[/code]

### 3) Автоматично запускайте WSL під час завантаження Windows

У PowerShell від імені адміністратора:

powershellCopy code
[code]
    schtasks /create /tn "WSL Boot" /tr "wsl.exe -d Ubuntu --exec /bin/true" /sc onstart /ru SYSTEM
[/code]

Замініть `Ubuntu` на назву вашого дистрибутива з:

powershellCopy code
[code]
    wsl --list --verbose
[/code]

### Перевірте ланцюг запуску

Після перезавантаження (до входу в Windows) перевірте з WSL:

bashCopy code
[code]
    systemctl --user is-enabled openclaw-gateway.servicesystemctl --user status openclaw-gateway.service --no-pager
[/code]

## Додатково: відкриття служб WSL у LAN (portproxy)

WSL має власну віртуальну мережу. Якщо іншій машині потрібно дістатися до служби, що працює **всередині WSL** (SSH, локальний TTS-сервер або Gateway), потрібно перенаправити порт Windows на поточну IP-адресу WSL. IP-адреса WSL змінюється після перезапусків, тому може знадобитися оновити правило перенаправлення.

Приклад (PowerShell **від імені адміністратора**):

powershellCopy code
[code]
    $Distro = "Ubuntu-24.04"$ListenPort = 2222$TargetPort = 22 $WslIp = (wsl -d $Distro -- hostname -I).Trim().Split(" ")[0]if (-not $WslIp) { throw "WSL IP not found." } netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=$ListenPort `  connectaddress=$WslIp connectport=$TargetPort
[/code]

Дозвольте порт у Windows Firewall (одноразово):

powershellCopy code
[code]
    New-NetFirewallRule -DisplayName "WSL SSH $ListenPort" -Direction Inbound `  -Protocol TCP -LocalPort $ListenPort -Action Allow
[/code]

Оновіть portproxy після перезапуску WSL:

powershellCopy code
[code]
    netsh interface portproxy delete v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 | Out-Nullnetsh interface portproxy add v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 `  connectaddress=$WslIp connectport=$TargetPort | Out-Null
[/code]

Примітки:

  * SSH з іншої машини націлюється на **IP-адресу хоста Windows** (приклад: `ssh user@windows-host -p 2222`).
  * Віддалені вузли мають вказувати на **доступну** URL-адресу Gateway (не `127.0.0.1`); використовуйте `openclaw status --all` для підтвердження.
  * Використовуйте `listenaddress=0.0.0.0` для доступу з LAN; `127.0.0.1` залишає його лише локальним.
  * Якщо хочете автоматизувати це, зареєструйте Scheduled Task для запуску кроку оновлення під час входу.


## Покрокове встановлення WSL2

### 1) Встановіть WSL2 + Ubuntu

Відкрийте PowerShell (адміністратор):

powershellCopy code
[code]
    wsl --install# Or pick a distro explicitly:wsl --list --onlinewsl --install -d Ubuntu-24.04
[/code]

Перезавантажтеся, якщо Windows попросить.

### 2) Увімкніть systemd (потрібно для встановлення Gateway)

У вашому терміналі WSL:

bashCopy code
[code]
    sudo tee /etc/wsl.conf >/dev/null <<'EOF'[boot]systemd=trueEOF
[/code]

Потім з PowerShell:

powershellCopy code
[code]
    wsl --shutdown
[/code]

Знову відкрийте Ubuntu, потім перевірте:

bashCopy code
[code]
    systemctl --user status
[/code]

### 3) Встановіть OpenClaw (усередині WSL)

Для звичайного першого налаштування всередині WSL дотримуйтеся Linux-потоку початку роботи:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm installpnpm buildpnpm ui:buildpnpm openclaw onboard --install-daemon
[/code]

Якщо ви розробляєте з вихідного коду, а не виконуєте перше онбординг-налаштування, використовуйте цикл розробки з вихідного коду з [Налаштування](</uk/start/setup>):

bashCopy code
[code]
    pnpm install# First run only (or after resetting local OpenClaw config/workspace)pnpm openclaw setuppnpm gateway:watch
[/code]

Повний посібник: [Початок роботи](</uk/start/getting-started>)

## Супутній застосунок Windows

У нас ще немає супутнього застосунку Windows. Внески вітаються, якщо ви хочете допомогти це реалізувати.

## Підключення Git і GitHub (контриб’ютори)

Деякі мережі блокують або обмежують HTTPS до GitHub. Якщо `git clone` завершується невдало через тайм-аути або скидання з’єднання, спробуйте іншу мережу, VPN або HTTP/HTTPS-проксі, який надає ваша організація.

Якщо `gh auth login` завершується невдало під час браузерного потоку пристрою (наприклад, тайм-аут підключення до `github.com:443`), автентифікуйтеся натомість за допомогою персонального токена доступу:

  1. Створіть токен принаймні з областю `repo` (класичний PAT) або еквівалентним детальним доступом.
  2. У PowerShell для поточного сеансу:

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token>"gh auth statusgh auth setup-git
[/code]

  3. Якщо `gh auth status` попереджає про відсутній `read:org`, створіть токен, який включає цю область, і повторно призначте змінну:

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token-with-repo-and-read:org>"gh auth status
[/code]

`gh auth refresh -s read:org` застосовується лише тоді, коли ви автентифікувалися через `gh auth login` і маєте збережені облікові дані для оновлення (не під час використання `GH_TOKEN`).

Ніколи не комітьте токени й не вставляйте їх в issue або pull request.

## Пов’язане

  * [Огляд встановлення](</uk/install>)
  * [Платформи](</uk/platforms>)


Was this useful?YesNo