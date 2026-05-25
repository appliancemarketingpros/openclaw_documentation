---
title: ClawDock
source_url: https://docs.openclaw.ai/uk/install/clawdock
scraped_at: 2026-05-25
---

ClawDock — це невеликий шар shell-помічників для встановлень OpenClaw на основі Docker.

Він дає короткі команди на кшталт `clawdock-start`, `clawdock-dashboard` і `clawdock-fix-token` замість довших викликів `docker compose ...`.

Якщо ви ще не налаштували Docker, почніть із [Docker](</uk/install/docker>).

## Встановлення

Використовуйте канонічний шлях помічника:

bashCopy code
[code]
    mkdir -p ~/.clawdock && curl -sL https://raw.githubusercontent.com/openclaw/openclaw/main/scripts/clawdock/clawdock-helpers.sh -o ~/.clawdock/clawdock-helpers.shecho 'source ~/.clawdock/clawdock-helpers.sh' >> ~/.zshrc && source ~/.zshrc
[/code]

Якщо раніше ви встановили ClawDock із `scripts/shell-helpers/clawdock-helpers.sh`, перевстановіть його з нового шляху `scripts/clawdock/clawdock-helpers.sh`. Старий raw-шлях GitHub було вилучено.

## Що ви отримуєте

### Базові операції

Команда | Опис  
---|---  
`clawdock-start` | Запустити Gateway  
`clawdock-stop` | Зупинити Gateway  
`clawdock-restart` | Перезапустити Gateway  
`clawdock-status` | Перевірити стан контейнера  
`clawdock-logs` | Стежити за журналами Gateway  
  
### Доступ до контейнера

Команда | Опис  
---|---  
`clawdock-shell` | Відкрити оболонку всередині контейнера Gateway  
`clawdock-cli <command>` | Запускати команди OpenClaw CLI в Docker  
`clawdock-exec <command>` | Виконати довільну команду в контейнері  
  
### Веб-інтерфейс і сполучення

Команда | Опис  
---|---  
`clawdock-dashboard` | Відкрити URL Control UI  
`clawdock-devices` | Показати список очікуваних сполучень пристроїв  
`clawdock-approve <id>` | Схвалити запит на сполучення  
  
### Налаштування й обслуговування

Команда | Опис  
---|---  
`clawdock-fix-token` | Налаштувати токен Gateway усередині контейнера  
`clawdock-update` | Завантажити, перебудувати й перезапустити  
`clawdock-rebuild` | Лише перебудувати образ Docker  
`clawdock-clean` | Видалити контейнери й томи  
  
### Утиліти

Команда | Опис  
---|---  
`clawdock-health` | Запустити перевірку стану Gateway  
`clawdock-token` | Вивести токен Gateway  
`clawdock-cd` | Перейти до каталогу проєкту OpenClaw  
`clawdock-config` | Відкрити `~/.openclaw`  
`clawdock-show-config` | Вивести файли конфігурації з редагованими значеннями  
`clawdock-workspace` | Відкрити каталог робочого простору  
  
## Потік першого запуску

bashCopy code
[code]
    clawdock-startclawdock-fix-tokenclawdock-dashboard
[/code]

Якщо браузер повідомляє, що потрібне сполучення:

bashCopy code
[code]
    clawdock-devicesclawdock-approve <request-id>
[/code]

## Конфігурація та секрети

ClawDock працює з тим самим поділом конфігурації Docker, описаним у [Docker](</uk/install/docker>):

  * `<project>/.env` для специфічних для Docker значень, як-от назва образу, порти й токен Gateway
  * `~/.openclaw/.env` для ключів провайдерів і токенів ботів, що надходять з env
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` для збереженої OAuth/API-key автентифікації провайдерів
  * `~/.openclaw/openclaw.json` для конфігурації поведінки


Використовуйте `clawdock-show-config`, коли хочете швидко переглянути файли `.env` і `openclaw.json`. У виведеному тексті він редагує значення `.env`.

## Пов’язане

[**Docker** Канонічне встановлення Docker для OpenClaw. ](</uk/install/docker>) [**Середовище виконання Docker VM** Кероване Docker середовище виконання VM для посиленої ізоляції. ](</uk/install/docker-vm-runtime>) [**Оновлення** Оновлення пакета OpenClaw і керованих служб. ](</uk/install/updating>)

Was this useful?YesNo