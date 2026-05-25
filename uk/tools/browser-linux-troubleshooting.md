---
title: Усунення несправностей браузера
source_url: https://docs.openclaw.ai/uk/tools/browser-linux-troubleshooting
scraped_at: 2026-05-25
---

## Проблема: "Failed to start Chrome CDP on port 18800"

Сервер керування браузером OpenClaw не може запустити Chrome/Brave/Edge/Chromium і показує помилку:

CodeCopy code
[code]
    {"error":"Error: Failed to start Chrome CDP on port 18800 for profile \"openclaw\"."}
[/code]

### Коренева причина

В Ubuntu (і багатьох дистрибутивах Linux) типовим встановленням Chromium є **snap-пакет**. Ізоляція AppArmor у snap заважає тому, як OpenClaw запускає та відстежує процес браузера.

Команда `apt install chromium` встановлює пакет-заглушку, який перенаправляє до snap:

CodeCopy code
[code]
    Note, selecting 'chromium-browser' instead of 'chromium'chromium-browser is already the newest version (2:1snap1-0ubuntu2).
[/code]

Це НЕ справжній браузер — це лише обгортка.

Інші поширені збої запуску в Linux:

  * `The profile appears to be in use by another Chromium process` означає, що Chrome знайшов застарілі lock-файли `Singleton*` у каталозі керованого профілю. OpenClaw видаляє ці блокування і повторює спробу один раз, якщо блокування вказує на мертвий процес або процес з іншого хоста.
  * `Missing X server or $DISPLAY` означає, що було явно запитано видимий браузер на хості без сесії робочого столу. За замовчуванням локальні керовані профілі в Linux тепер переходять у headless-режим, коли `DISPLAY` і `WAYLAND_DISPLAY` обидва не задані. Якщо ви встановили `OPENCLAW_BROWSER_HEADLESS=0`, `browser.headless: false` або `browser.profiles.<name>.headless: false`, приберіть це перевизначення headed-режиму, задайте `OPENCLAW_BROWSER_HEADLESS=1`, запустіть `Xvfb`, виконайте `openclaw browser start --headless` для одноразового керованого запуску або запускайте OpenClaw у справжній сесії робочого столу.


### Рішення 1: Встановіть Google Chrome (рекомендовано)

Встановіть офіційний `.deb`-пакет Google Chrome, який не ізольований через snap:

bashCopy code
[code]
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.debsudo dpkg -i google-chrome-stable_current_amd64.debsudo apt --fix-broken install -y  # if there are dependency errors
[/code]

Потім оновіть конфігурацію OpenClaw (`~/.openclaw/openclaw.json`):

jsonCopy code
[code]
    {  "browser": {    "enabled": true,    "executablePath": "/usr/bin/google-chrome-stable",    "headless": true,    "noSandbox": true  }}
[/code]

### Рішення 2: Використовуйте snap Chromium у режимі лише приєднання

Якщо вам обов’язково потрібен snap Chromium, налаштуйте OpenClaw на приєднання до браузера, запущеного вручну:

  1. Оновіть конфігурацію:

jsonCopy code
[code]
    {  "browser": {    "enabled": true,    "attachOnly": true,    "headless": true,    "noSandbox": true  }}
[/code]

  2. Запустіть Chromium вручну:

bashCopy code
[code]
    chromium-browser --headless --no-sandbox --disable-gpu \  --remote-debugging-port=18800 \  --user-data-dir=$HOME/.openclaw/browser/openclaw/user-data \  about:blank &
[/code]

  3. За бажанням створіть systemd user service для автоматичного запуску Chrome:

iniCopy code
[code]
    # ~/.config/systemd/user/openclaw-browser.service[Unit]Description=OpenClaw Browser (Chrome CDP)After=network.target [Service]ExecStart=/snap/bin/chromium --headless --no-sandbox --disable-gpu --remote-debugging-port=18800 --user-data-dir=%h/.openclaw/browser/openclaw/user-data about:blankRestart=on-failureRestartSec=5 [Install]WantedBy=default.target
[/code]

Увімкнення: `systemctl --user enable --now openclaw-browser.service`

### Перевірка, чи браузер працює

Перевірте стан:

bashCopy code
[code]
    curl -s http://127.0.0.1:18791/ | jq '{running, pid, chosenBrowser}'
[/code]

Протестуйте перегляд:

bashCopy code
[code]
    curl -s -X POST http://127.0.0.1:18791/startcurl -s http://127.0.0.1:18791/tabs
[/code]

### Довідник із конфігурації

Опція | Опис | Типове значення  
---|---|---  
`browser.enabled` | Увімкнути керування браузером | `true`  
`browser.executablePath` | Шлях до двійкового файла браузера на базі Chromium (Chrome/Brave/Edge/Chromium) | визначається автоматично (надає перевагу типовому браузеру, якщо він на базі Chromium)  
`browser.headless` | Запуск без GUI | `false`  
`OPENCLAW_BROWSER_HEADLESS` | Перевизначення на рівні процесу для headless-режиму локального керованого браузера | не задано  
`browser.noSandbox` | Додати прапорець `--no-sandbox` (потрібно для деяких конфігурацій Linux) | `false`  
`browser.attachOnly` | Не запускати браузер, лише приєднуватися до наявного | `false`  
`browser.cdpPort` | Порт Chrome DevTools Protocol | `18800`  
`browser.localLaunchTimeoutMs` | Тайм-аут виявлення локального керованого Chrome | `15000`  
`browser.localCdpReadyTimeoutMs` | Тайм-аут готовності CDP після запуску локального керованого браузера | `8000`  
  
На Raspberry Pi, старих VPS-хостах або повільних носіях збільшуйте `browser.localLaunchTimeoutMs`, коли Chrome потребує більше часу, щоб відкрити свій HTTP-ендпоїнт CDP. Збільшуйте `browser.localCdpReadyTimeoutMs`, коли запуск успішний, але `openclaw browser start` усе ще повідомляє `not reachable after start`. Значення мають бути додатними цілими числами до `120000` мс; некоректні значення конфігурації відхиляються.

### Проблема: "No Chrome tabs found for profile="user""

Ви використовуєте профіль `existing-session` / Chrome MCP. OpenClaw бачить локальний Chrome, але немає відкритих вкладок, до яких можна приєднатися.

Варіанти виправлення:

  1. **Використовуйте керований браузер:** `openclaw browser start --browser-profile openclaw` (або задайте `browser.defaultProfile: "openclaw"`).
  2. **Використовуйте Chrome MCP:** переконайтеся, що локальний Chrome запущений і має принаймні одну відкриту вкладку, а потім повторіть спробу з `--browser-profile user`.


Примітки:

  * `user` доступний лише на хості. Для серверів Linux, контейнерів або віддалених хостів надавайте перевагу профілям CDP.
  * `user` / інші профілі `existing-session` зберігають поточні обмеження Chrome MCP: дії на основі ref, хуки завантаження одного файла, без перевизначення тайм-аутів діалогів, без `wait --load networkidle`, а також без `responsebody`, експорту PDF, перехоплення завантажень чи пакетних дій.
  * Локальні профілі `openclaw` автоматично призначають `cdpPort`/`cdpUrl`; задавайте їх лише для віддаленого CDP.
  * Віддалені профілі CDP приймають `http://`, `https://`, `ws://` і `wss://`. Використовуйте HTTP(S) для виявлення через `/json/version`, або WS(S), коли ваш сервіс браузера надає прямий URL сокета DevTools.


## Пов’язані матеріали

  * [Browser](</uk/tools/browser>)
  * [Browser login](</uk/tools/browser-login>)
  * [Browser WSL2 troubleshooting](</uk/tools/browser-wsl2-windows-remote-cdp-troubleshooting>)


Was this useful?YesNo