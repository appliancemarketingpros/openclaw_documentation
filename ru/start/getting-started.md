---
title: Начало работы
source_url: https://docs.openclaw.ai/ru/start/getting-started
scraped_at: 2026-06-29
---

Get startedFirst steps

Установите OpenClaw, пройдите онбординг и общайтесь со своим ИИ-ассистентом — все это примерно за 5 минут. В итоге у вас будет запущенный Gateway, настроенная аутентификация и рабочий сеанс чата.

## Что вам понадобится

  * **Node.js** — рекомендуется Node 24 (Node 22.19+ также поддерживается)
  * **API-ключ** от поставщика моделей (Anthropic, OpenAI, Google и т. д.) — онбординг запросит его


## Быстрая настройка

* ### Установите OpenClaw

### macOS / Linux

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

![Процесс установочного скрипта](/assets/install-script.svg)

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

* ### Запустите онбординг

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Мастер проведет вас через выбор поставщика моделей, настройку API-ключа и конфигурацию Gateway. QuickStart обычно занимает всего несколько минут, но вход у поставщика, сопряжение канала, установка демона, сетевые загрузки, Skills или дополнительные плагины могут увеличить время полного онбординга. Необязательные шаги можно пропустить и вернуться к ним позже с помощью `openclaw configure`.

Полный справочник см. в [Онбординг (CLI)](</ru/start/wizard>).

* ### Проверьте, что Gateway запущен

bashCopy code
[code]
    openclaw gateway status
[/code]

Вы должны увидеть, что Gateway слушает порт 18789.

* ### Откройте панель управления

bashCopy code
[code]
    openclaw dashboard
[/code]

Это откроет Control UI в вашем браузере. Если он загрузился, все работает.

* ### Отправьте первое сообщение

Введите сообщение в чате Control UI, и вы должны получить ответ ИИ.

Хотите вместо этого общаться с телефона? Самый быстрый канал для настройки — [Telegram](</ru/channels/telegram>) (нужен только токен бота). Все варианты см. в [Каналы](</ru/channels>).

Дополнительно: подключение собственной сборки Control UI

Если вы поддерживаете локализованную или настроенную сборку панели управления, укажите в `gateway.controlUi.root` каталог, содержащий собранные статические ресурсы и `index.html`.

bashCopy code
[code]
    mkdir -p "$HOME/.openclaw/control-ui-custom"# Copy your built static files into that directory.
[/code]

Затем задайте:

jsonCopy code
[code]
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "$HOME/.openclaw/control-ui-custom"  }}}
[/code]

Перезапустите Gateway и снова откройте панель управления:

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## Что делать дальше

[**Подключить канал** Discord, Feishu, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo и другие. ](</ru/channels>) [**Сопряжение и безопасность** Управляйте тем, кто может отправлять сообщения вашему агенту. ](</ru/channels/pairing>) [**Настроить Gateway** Модели, инструменты, песочница и расширенные настройки. ](</ru/gateway/configuration>) [**Просмотреть инструменты** Браузер, exec, веб-поиск, Skills и плагины. ](</ru/tools>)

Дополнительно: переменные окружения

Если вы запускаете OpenClaw от имени сервисной учетной записи или хотите использовать собственные пути:

  * `OPENCLAW_HOME` — домашний каталог для разрешения внутренних путей
  * `OPENCLAW_STATE_DIR` — переопределяет каталог состояния
  * `OPENCLAW_CONFIG_PATH` — переопределяет путь к файлу конфигурации


Полный справочник: [Переменные окружения](</ru/help/environment>).

## Связанные материалы

  * [Обзор установки](</ru/install>)
  * [Обзор каналов](</ru/channels>)
  * [Настройка](</ru/start/setup>)


Was this useful?YesNo

Open issue