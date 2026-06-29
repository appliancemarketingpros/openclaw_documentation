---
title: Устранение неполадок WSL2 + Windows + удаленного Chrome CDP
source_url: https://docs.openclaw.ai/ru/tools/browser-wsl2-windows-remote-cdp-troubleshooting
scraped_at: 2026-06-29
---

CapabilitiesTools

В распространенной схеме с разделенными хостами OpenClaw Gateway работает внутри WSL2, Chrome работает в Windows, а управление браузером должно пересекать границу между WSL2 и Windows. Многоуровневый паттерн сбоев из [issue #39369](<https://github.com/openclaw/openclaw/issues/39369>) означает, что несколько независимых проблем могут проявиться одновременно, из-за чего сначала кажется сломанным не тот уровень.

## Сначала выберите правильный режим браузера

Есть два допустимых паттерна:

### Вариант 1: Прямой удаленный CDP из WSL2 в Windows

Используйте удаленный профиль браузера, который указывает из WSL2 на CDP-эндпоинт Chrome в Windows.

Выбирайте это, когда:

  * Gateway остается внутри WSL2
  * Chrome работает в Windows
  * вам нужно, чтобы управление браузером пересекало границу WSL2/Windows


### Вариант 2: Локальный для хоста Chrome MCP

Используйте `existing-session` / `user` только когда сам Gateway работает на том же хосте, что и Chrome.

Выбирайте это, когда:

  * OpenClaw и Chrome находятся на одной машине
  * вам нужно локальное состояние браузера с выполненным входом
  * вам не нужен межхостовый транспорт браузера
  * вам не нужны расширенные маршруты, доступные только через управляемый/прямой CDP, такие как `responsebody`, экспорт PDF, перехват загрузок или пакетные действия


Для WSL2 Gateway + Windows Chrome предпочитайте прямой удаленный CDP. Chrome MCP локален для хоста, а не является мостом из WSL2 в Windows.

## Рабочая архитектура

Ориентировочная схема:

  * WSL2 запускает Gateway на `127.0.0.1:18789`
  * Windows открывает интерфейс управления в обычном браузере по адресу `http://127.0.0.1:18789/`
  * Windows Chrome предоставляет CDP-эндпоинт на порту `9222`
  * WSL2 может достучаться до этого CDP-эндпоинта Windows
  * OpenClaw указывает профиль браузера на адрес, доступный из WSL2


## Почему эта настройка сбивает с толку

Несколько сбоев могут накладываться друг на друга:

  * WSL2 не может достучаться до CDP-эндпоинта Windows
  * интерфейс управления открыт из небезопасного origin
  * `gateway.controlUi.allowedOrigins` не совпадает с origin страницы
  * отсутствует токен или pairing
  * профиль браузера указывает на неправильный адрес


Поэтому после исправления одного уровня все еще может быть видна другая ошибка.

## Критическое правило для интерфейса управления

Когда UI открыт из Windows, используйте Windows localhost, если у вас нет намеренно настроенного HTTPS.

Используйте:

`http://127.0.0.1:18789/`

Не используйте LAN IP по умолчанию для интерфейса управления. Обычный HTTP на LAN- или tailnet-адресе может вызвать поведение небезопасного origin/device-auth, не связанное с самим CDP. См. [интерфейс управления](</ru/web/control-ui>).

## Проверяйте по уровням

Идите сверху вниз. Не перепрыгивайте вперед.

### Уровень 1: Проверьте, что Chrome отдает CDP в Windows

Запустите Chrome в Windows с включенной удаленной отладкой:

powershellCopy code
[code]
    chrome.exe --remote-debugging-port=9222
[/code]

Из Windows сначала проверьте сам Chrome:

powershellCopy code
[code]
    curl http://127.0.0.1:9222/json/versioncurl http://127.0.0.1:9222/json/list
[/code]

Если это не работает в Windows, OpenClaw пока не является проблемой.

### Уровень 2: Проверьте, что WSL2 может достучаться до этого эндпоинта Windows

Из WSL2 проверьте точный адрес, который планируете использовать в `cdpUrl`:

bashCopy code
[code]
    curl http://WINDOWS_HOST_OR_IP:9222/json/versioncurl http://WINDOWS_HOST_OR_IP:9222/json/list
[/code]

Хороший результат:

  * `/json/version` возвращает JSON с метаданными Browser / Protocol-Version
  * `/json/list` возвращает JSON (пустой массив допустим, если страницы не открыты)


Если это не работает:

  * Windows еще не предоставляет порт для WSL2
  * адрес неверен для стороны WSL2
  * firewall / проброс порта / локальное проксирование все еще отсутствует


Исправьте это до изменения конфигурации OpenClaw.

### Уровень 3: Настройте правильный профиль браузера

Для прямого удаленного CDP укажите OpenClaw адрес, доступный из WSL2:

json5Copy code
[code]
    {  browser: {    enabled: true,    defaultProfile: "remote",    profiles: {      remote: {        cdpUrl: "http://WINDOWS_HOST_OR_IP:9222",        attachOnly: true,        color: "#00AA00",      },    },  },}
[/code]

Примечания:

  * используйте адрес, доступный из WSL2, а не тот, который работает только в Windows
  * оставьте `attachOnly: true` для внешне управляемых браузеров
  * `cdpUrl` может быть `http://`, `https://`, `ws://` или `wss://`
  * используйте HTTP(S), когда хотите, чтобы OpenClaw обнаруживал `/json/version`
  * используйте WS(S) только когда провайдер браузера дает прямой URL сокета DevTools
  * проверьте тот же URL через `curl`, прежде чем ожидать успешной работы OpenClaw


### Уровень 4: Отдельно проверьте уровень интерфейса управления

Откройте UI из Windows:

`http://127.0.0.1:18789/`

Затем проверьте:

  * origin страницы совпадает с тем, что ожидает `gateway.controlUi.allowedOrigins`
  * token auth или pairing настроены правильно
  * вы не отлаживаете проблему аутентификации интерфейса управления так, будто это проблема браузера


Полезная страница:

  * [Интерфейс управления](</ru/web/control-ui>)


### Уровень 5: Проверьте сквозное управление браузером

Из WSL2:

bashCopy code
[code]
    openclaw browser open https://example.com --browser-profile remoteopenclaw browser tabs --browser-profile remote
[/code]

Хороший результат:

  * вкладка открывается в Windows Chrome
  * `openclaw browser tabs` возвращает цель
  * последующие действия (`snapshot`, `screenshot`, `navigate`) работают из того же профиля


## Частые вводящие в заблуждение ошибки

Рассматривайте каждое сообщение как подсказку, относящуюся к конкретному уровню:

  * `control-ui-insecure-auth`
    * проблема origin UI / secure context, а не проблема транспорта CDP
  * `token_missing`
    * проблема конфигурации аутентификации
  * `pairing required`
    * проблема подтверждения устройства
  * `Remote CDP for profile "remote" is not reachable`
    * WSL2 не может достучаться до настроенного `cdpUrl`
  * `Browser attachOnly is enabled and CDP websocket for profile "remote" is not reachable`
    * HTTP-эндпоинт ответил, но WebSocket DevTools все равно не удалось открыть
  * устаревшие переопределения viewport / dark-mode / locale / offline после удаленной сессии 
    * выполните `openclaw browser stop --browser-profile remote`
    * это закрывает активную сессию управления и освобождает состояние эмуляции Playwright/CDP без перезапуска gateway или внешнего браузера
  * `gateway timeout after 1500ms`
    * часто это все еще доступность CDP или медленный/недоступный удаленный эндпоинт
  * `No Chrome tabs found for profile="user"`
    * выбран локальный профиль Chrome MCP, когда локальные для хоста вкладки недоступны


## Быстрый чеклист диагностики

  1. Windows: работает ли `curl http://127.0.0.1:9222/json/version`?
  2. WSL2: работает ли `curl http://WINDOWS_HOST_OR_IP:9222/json/version`?
  3. Конфигурация OpenClaw: использует ли `browser.profiles.<name>.cdpUrl` именно этот адрес, доступный из WSL2?
  4. Интерфейс управления: открываете ли вы `http://127.0.0.1:18789/` вместо LAN IP?
  5. Пытаетесь ли вы использовать `existing-session` через WSL2 и Windows вместо прямого удаленного CDP?


## Практический вывод

Такая настройка обычно жизнеспособна. Сложность в том, что транспорт браузера, безопасность origin интерфейса управления и token/pairing могут отказывать независимо, при этом выглядеть похоже со стороны пользователя.

Если сомневаетесь:

  * сначала проверьте эндпоинт Windows Chrome локально
  * затем проверьте тот же эндпоинт из WSL2
  * только после этого отлаживайте конфигурацию OpenClaw или аутентификацию интерфейса управления


## Связанные материалы

  * [Браузер](</ru/tools/browser>)
  * [Вход в браузер](</ru/tools/browser-login>)
  * [Диагностика браузера в Linux](</ru/tools/browser-linux-troubleshooting>)


Was this useful?YesNo

Open issue