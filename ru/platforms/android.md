---
title: Приложение для Android
source_url: https://docs.openclaw.ai/ru/platforms/android
scraped_at: 2026-06-29
---

PlatformsPlatforms overview

## Краткая сводка поддержки

  * Роль: приложение сопутствующего узла (Android не размещает Gateway).
  * Требуется Gateway: да (запустите его на macOS, Linux или Windows через WSL2).
  * Установка: [Google Play](<https://play.google.com/store/apps/details?id=ai.openclaw.app&hl=en_IN>) для приложения, [Начало работы](</ru/start/getting-started>) для Gateway, затем [Сопряжение](</ru/channels/pairing>).
  * Gateway: [Runbook](</ru/gateway>) \+ [Конфигурация](</ru/gateway/configuration>). 
    * Протоколы: [протокол Gateway](</ru/gateway/protocol>) (узлы + плоскость управления).


## Управление системой

Управление системой (launchd/systemd) находится на хосте Gateway. См. [Gateway](</ru/gateway>).

## Runbook подключения

Приложение узла Android ⇄ (mDNS/NSD + WebSocket) ⇄ **Gateway**

Android подключается напрямую к WebSocket Gateway и использует сопряжение устройства (`role: node`).

Для Tailscale или публичных хостов Android требует защищенную конечную точку:

  * Предпочтительно: Tailscale Serve / Funnel с `https://<magicdns>` / `wss://<magicdns>`
  * Также поддерживается: любой другой URL Gateway `wss://` с настоящей TLS-конечной точкой
  * Незашифрованный `ws://` остается поддерживаемым для частных LAN-адресов / хостов `.local`, а также `localhost`, `127.0.0.1` и моста эмулятора Android (`10.0.2.2`)


### Предварительные требования

  * Вы можете запустить Gateway на «главной» машине.
  * Устройство/эмулятор Android может достичь WebSocket шлюза: 
    * В той же LAN с mDNS/NSD, **или**
    * В той же tailnet Tailscale с использованием Wide-Area Bonjour / unicast DNS-SD (см. ниже), **или**
    * Хост/порт шлюза вручную (резервный вариант)
  * Сопряжение мобильного устройства через tailnet/публичную сеть **не** использует raw tailnet IP-конечные точки `ws://`. Вместо этого используйте Tailscale Serve или другой URL `wss://`.
  * Вы можете запустить CLI (`openclaw`) на машине шлюза (или через SSH).


### 1) Запустите Gateway

bashCopy code
[code]
    openclaw gateway --port 18789 --verbose
[/code]

Убедитесь, что в логах есть что-то вроде:

  * `listening on ws://0.0.0.0:18789`


Для удаленного доступа Android через Tailscale предпочитайте Serve/Funnel вместо raw tailnet bind:

bashCopy code
[code]
    openclaw gateway --tailscale serve
[/code]

Это дает Android защищенную конечную точку `wss://` / `https://`. Обычной настройки `gateway.bind: "tailnet"` недостаточно для первичного удаленного сопряжения Android, если вы также отдельно не терминируете TLS.

### 2) Проверьте обнаружение (необязательно)

С машины шлюза:

bashCopy code
[code]
    dns-sd -B _openclaw-gw._tcp local.
[/code]

Дополнительные заметки по отладке: [Bonjour](</ru/gateway/bonjour>).

Если вы также настроили домен обнаружения wide-area, сравните с:

bashCopy code
[code]
    openclaw gateway discover --json
[/code]

Он показывает `local.` плюс настроенный wide-area домен за один проход и использует разрешенную конечную точку сервиса вместо подсказок только из TXT.

#### Обнаружение в tailnet (Вена ⇄ Лондон) через unicast DNS-SD

Обнаружение Android NSD/mDNS не проходит между сетями. Если ваш узел Android и шлюз находятся в разных сетях, но подключены через Tailscale, используйте вместо этого Wide-Area Bonjour / unicast DNS-SD.

Одного обнаружения недостаточно для сопряжения Android через tailnet/публичную сеть. Обнаруженному маршруту все равно нужна защищенная конечная точка (`wss://` или Tailscale Serve):

  1. Настройте зону DNS-SD (пример `openclaw.internal.`) на хосте шлюза и опубликуйте записи `_openclaw-gw._tcp`.
  2. Настройте split DNS Tailscale для выбранного домена, указав этот DNS-сервер.


Подробности и пример конфигурации CoreDNS: [Bonjour](</ru/gateway/bonjour>).

### 3) Подключитесь с Android

В приложении Android:

  * Приложение поддерживает соединение со шлюзом через **foreground service** (постоянное уведомление).
  * Откройте вкладку **Подключение**.
  * Используйте режим **Код настройки** или **Вручную**.
  * Если обнаружение заблокировано, используйте ручной хост/порт в **Расширенных элементах управления**. Для частных LAN-хостов `ws://` по-прежнему работает. Для Tailscale/публичных хостов включите TLS и используйте конечную точку `wss://` / Tailscale Serve.


После первого успешного сопряжения Android автоматически переподключается при запуске:

  * Ручная конечная точка (если включена), иначе
  * Последний обнаруженный шлюз (по мере возможности).


### Presence alive beacons

После подключения аутентифицированной сессии узла, а также когда приложение переходит в фон, пока foreground service все еще подключен, Android вызывает `node.event` с `event: "node.presence.alive"`. Шлюз записывает это как `lastSeenAtMs`/`lastSeenReason` в метаданные сопряженного узла/устройства только после того, как известна идентичность аутентифицированного устройства узла.

Приложение считает маяк успешно записанным только тогда, когда ответ шлюза включает `handled: true`. Более старые шлюзы могут подтверждать `node.event` с `{ "ok": true }`; такой ответ совместим, но не считается долговременным обновлением last-seen.

### 4) Одобрите сопряжение (CLI)

На машине шлюза:

bashCopy code
[code]
    openclaw devices listopenclaw devices approve <requestId>openclaw devices reject <requestId>
[/code]

Подробности сопряжения: [Сопряжение](</ru/channels/pairing>).

Необязательно: если узел Android всегда подключается из строго контролируемой подсети, вы можете явно включить автоматическое одобрение узла при первом сопряжении с помощью CIDR или точных IP:

json5Copy code
[code]
    {  gateway: {    nodes: {      pairing: {        autoApproveCidrs: ["192.168.1.0/24"],      },    },  },}
[/code]

По умолчанию это отключено. Это применяется только к новому сопряжению `role: node` без запрошенных областей доступа. Сопряжение оператора/браузера и любое изменение роли, области доступа, метаданных или публичного ключа по-прежнему требуют ручного одобрения.

### 5) Проверьте, что узел подключен

  * Через статус узлов:

bashCopy code
[code]openclaw nodes status
[/code]

  * Через Gateway:

bashCopy code
[code]openclaw gateway call node.list --params "{}"
[/code]


### 6) Чат + история

Вкладка Chat в Android поддерживает выбор сессии (по умолчанию `main`, а также другие существующие сессии):

  * История: `chat.history` (нормализованная для отображения; встроенные теги директив удаляются из видимого текста, plain-text XML-полезные нагрузки вызовов инструментов (включая `<tool_call>...</tool_call>`, `<function_call>...</function_call>`, `<tool_calls>...</tool_calls>`, `<function_calls>...</function_calls>` и усеченные блоки вызовов инструментов) и просочившиеся ASCII/full-width токены управления модели удаляются, строки ассистента только с silent-token, такие как точные `NO_REPLY` / `no_reply`, опускаются, а слишком большие строки могут быть заменены placeholders)
  * Отправка: `chat.send`
  * Push-обновления (по мере возможности): `chat.subscribe` → `event:"chat"`


### 7) Canvas + камера

#### Хост Gateway Canvas (рекомендуется для веб-контента)

Если вы хотите, чтобы узел показывал настоящий HTML/CSS/JS, который агент может редактировать на диске, укажите узлу хост canvas Gateway.

  1. Создайте `~/.openclaw/workspace/canvas/index.html` на хосте шлюза.

  2. Перейдите узлом к нему (LAN):


bashCopy code
[code]
    openclaw nodes invoke --node "&lt;Android Node&gt;" --command canvas.navigate --params '{"url":"http://<gateway-hostname>.local:18789/__openclaw__/canvas/"}'
[/code]

Tailnet (необязательно): если оба устройства находятся в Tailscale, используйте имя MagicDNS или tailnet IP вместо `.local`, например `http://<gateway-magicdns>:18789/__openclaw__/canvas/`.

Этот сервер внедряет клиент live-reload в HTML и перезагружает страницу при изменениях файлов. Gateway также обслуживает `/__openclaw__/a2ui/`, но приложение Android рассматривает удаленные страницы A2UI как доступные только для рендеринга. Команды A2UI с поддержкой действий используют встроенную страницу A2UI, принадлежащую приложению, перед применением сообщений.

Команды Canvas (только на переднем плане):

  * `canvas.eval`, `canvas.snapshot`, `canvas.navigate` (используйте `{"url":""}` или `{"url":"/"}`, чтобы вернуться к стандартному scaffold). `canvas.snapshot` возвращает `{ format, base64 }` (по умолчанию `format="jpeg"`).
  * A2UI: `canvas.a2ui.push`, `canvas.a2ui.reset` (устаревший alias `canvas.a2ui.pushJSONL`). Эти команды используют встроенную страницу A2UI, принадлежащую приложению, для рендеринга с поддержкой действий.


Команды камеры (только на переднем плане; ограничены разрешениями):

  * `camera.snap` (jpg)
  * `camera.clip` (mp4)


Параметры и вспомогательные команды CLI см. в [узле камеры](</ru/nodes/camera>).

### 8) Голос + расширенная поверхность команд Android

  * Вкладка Voice: Android имеет два явных режима захвата. **Mic** — это ручная сессия на вкладке Voice, которая отправляет каждую паузу как ход чата и останавливается, когда приложение покидает передний план или пользователь уходит со вкладки Voice. **Talk** — это непрерывный режим Talk Mode, который продолжает слушать, пока его не отключат или пока узел не отключится.
  * Talk Mode повышает существующий foreground service с `connectedDevice` до `connectedDevice|microphone` перед началом захвата, затем понижает его, когда Talk Mode останавливается. Сервис узла объявляет `FOREGROUND_SERVICE_CONNECTED_DEVICE` с `CHANGE_NETWORK_STATE`; Android 14+ также требует объявление `FOREGROUND_SERVICE_MICROPHONE`, runtime-разрешение `RECORD_AUDIO` и тип сервиса microphone во время выполнения.
  * По умолчанию Android Talk использует нативное распознавание речи, чат Gateway и `talk.speak` через настроенного провайдера Talk шлюза. Локальный системный TTS используется только когда `talk.speak` недоступен.
  * Android Talk использует realtime relay Gateway только когда `talk.realtime.mode` равно `realtime`, а `talk.realtime.transport` равно `gateway-relay`.
  * Voice wake остается отключенным в UX/runtime Android.
  * Дополнительные семейства команд Android (доступность зависит от устройства, разрешений и пользовательских настроек): 
    * `device.status`, `device.info`, `device.permissions`, `device.health`
    * `device.apps` только когда включено **Settings > Phone Capabilities > Installed Apps**; по умолчанию выводит приложения, видимые в launcher.
    * `notifications.list`, `notifications.actions` (см. пересылку уведомлений ниже)
    * `photos.latest`
    * `contacts.search`, `contacts.add`
    * `calendar.events`, `calendar.add`
    * `callLog.search`
    * `sms.search`
    * `motion.activity`, `motion.pedometer`


## Точки входа ассистента

Android поддерживает запуск OpenClaw через системный триггер ассистента (Google Assistant). Если настроено, удержание кнопки Home или фраза «Hey Google, ask OpenClaw...» открывает приложение и передает prompt в композер чата.

Это использует метаданные Android **App Actions** , объявленные в манифесте приложения. На стороне шлюза дополнительная конфигурация не нужна -- intent ассистента полностью обрабатывается приложением Android и пересылается как обычное сообщение чата.

## Пересылка уведомлений

Android может пересылать уведомления устройства на шлюз как события. Несколько элементов управления позволяют ограничить, какие уведомления пересылаются и когда.

Ключ | Тип | Описание  
---|---|---  
`notifications.allowPackages` | string[] | Пересылать уведомления только от этих имен пакетов. Если задано, все остальные пакеты игнорируются.  
`notifications.denyPackages` | string[] | Никогда не пересылать уведомления от этих имен пакетов. Применяется после `allowPackages`.  
`notifications.quietHours.start` | string (HH:mm) | Начало окна тихих часов (локальное время устройства). Уведомления подавляются в течение этого окна.  
`notifications.quietHours.end` | string (HH:mm) | Конец окна тихих часов.  
`notifications.rateLimit` | number | Максимум пересылаемых уведомлений на пакет в минуту. Лишние уведомления отбрасываются.  
  
Пикер уведомлений также использует более безопасное поведение для пересылаемых событий уведомлений, предотвращая случайную пересылку конфиденциальных системных уведомлений.

Пример конфигурации:

json5Copy code
[code]
    {  notifications: {    allowPackages: ["com.slack", "com.whatsapp"],    denyPackages: ["com.android.systemui"],    quietHours: {      start: "22:00",      end: "07:00",    },    rateLimit: 5,  },}
[/code]

## Связанные материалы

  * [приложение iOS](</ru/platforms/ios>)
  * [Узлы](</ru/nodes>)
  * [Устранение неполадок узла Android](</ru/nodes/troubleshooting>)


Was this useful?YesNo

Open issue