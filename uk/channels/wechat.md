---
title: WeChat
source_url: https://docs.openclaw.ai/uk/channels/wechat
scraped_at: 2026-05-25
---

OpenClaw підключається до WeChat через зовнішній канальний Plugin Tencent `@tencent-weixin/openclaw-weixin`.

Статус: зовнішній Plugin. Прямі чати й медіа підтримуються. Групові чати не заявлені поточними метаданими можливостей Plugin.

## Назви

  * **WeChat** — назва для користувачів у цій документації.
  * **Weixin** — назва, яку використовує пакет Tencent і id Plugin.
  * `openclaw-weixin` — id каналу OpenClaw.
  * `@tencent-weixin/openclaw-weixin` — npm-пакет.


Використовуйте `openclaw-weixin` у командах CLI і шляхах конфігурації.

## Як це працює

Код WeChat не міститься в основному репозиторії OpenClaw. OpenClaw надає загальний контракт канального Plugin, а зовнішній Plugin надає специфічне для WeChat середовище виконання:

  1. `openclaw plugins install` встановлює `@tencent-weixin/openclaw-weixin`.
  2. Gateway знаходить маніфест Plugin і завантажує точку входу Plugin.
  3. Plugin реєструє id каналу `openclaw-weixin`.
  4. `openclaw channels login --channel openclaw-weixin` запускає вхід за QR-кодом.
  5. Plugin зберігає облікові дані облікового запису в каталозі стану OpenClaw.
  6. Коли Gateway запускається, Plugin запускає свій монітор Weixin для кожного налаштованого облікового запису.
  7. Вхідні повідомлення WeChat нормалізуються через контракт каналу, спрямовуються до вибраного агента OpenClaw і надсилаються назад через вихідний шлях Plugin.


Це розділення важливе: ядро OpenClaw має залишатися незалежним від каналів. Вхід у WeChat, виклики Tencent iLink API, завантаження й отримання медіа, токени контексту та моніторинг облікових записів належать зовнішньому Plugin.

## Встановлення

Швидке встановлення:

bashCopy code
[code]
    npx -y @tencent-weixin/openclaw-weixin-cli install
[/code]

Ручне встановлення:

bashCopy code
[code]
    openclaw plugins install "@tencent-weixin/openclaw-weixin"openclaw config set plugins.entries.openclaw-weixin.enabled true
[/code]

Перезапустіть Gateway після встановлення:

bashCopy code
[code]
    openclaw gateway restart
[/code]

## Вхід

Запустіть вхід за QR-кодом на тій самій машині, де працює Gateway:

bashCopy code
[code]
    openclaw channels login --channel openclaw-weixin
[/code]

Відскануйте QR-код у WeChat на телефоні й підтвердьте вхід. Plugin зберігає токен облікового запису локально після успішного сканування.

Щоб додати інший обліковий запис WeChat, знову виконайте ту саму команду входу. Для кількох облікових записів ізолюйте сеанси прямих повідомлень за обліковим записом, каналом і відправником:

bashCopy code
[code]
    openclaw config set session.dmScope per-account-channel-peer
[/code]

## Керування доступом

Прямі повідомлення використовують звичайну модель сполучення OpenClaw і список дозволених для канальних Plugin.

Схваліть нових відправників:

bashCopy code
[code]
    openclaw pairing list openclaw-weixinopenclaw pairing approve openclaw-weixin &lt;CODE&gt;
[/code]

Повну модель керування доступом дивіться в розділі [Сполучення](</uk/channels/pairing>).

## Сумісність

Plugin перевіряє версію хоста OpenClaw під час запуску.

Лінія Plugin | Версія OpenClaw | npm-тег  
---|---|---  
`2.x` | `>=2026.3.22` | `latest`  
`1.x` | `>=2026.1.0 <2026.3.22` | `legacy`  
  
Якщо Plugin повідомляє, що ваша версія OpenClaw застаріла, оновіть OpenClaw або встановіть legacy-лінію Plugin:

bashCopy code
[code]
    openclaw plugins install @tencent-weixin/openclaw-weixin@legacy
[/code]

## Процес sidecar

Plugin WeChat може виконувати допоміжну роботу поруч із Gateway, поки моніторить Tencent iLink API. У issue #68451 цей допоміжний шлях виявив помилку в загальному очищенні застарілого Gateway в OpenClaw: дочірній процес міг спробувати очистити батьківський процес Gateway, спричиняючи цикли перезапуску під менеджерами процесів, такими як systemd.

Поточне очищення під час запуску OpenClaw виключає поточний процес і його предків, тому допоміжний процес каналу не повинен завершувати Gateway, який його запустив. Це виправлення загальне; це не специфічний для WeChat шлях у ядрі.

## Усунення несправностей

Перевірте встановлення і статус:

bashCopy code
[code]
    openclaw plugins listopenclaw channels status --probeopenclaw --version
[/code]

Якщо канал відображається як встановлений, але не підключається, підтвердьте, що Plugin увімкнено, і перезапустіть:

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-weixin.enabled trueopenclaw gateway restart
[/code]

Якщо Gateway багаторазово перезапускається після ввімкнення WeChat, оновіть і OpenClaw, і Plugin:

bashCopy code
[code]
    npm view @tencent-weixin/openclaw-weixin versionopenclaw plugins install "@tencent-weixin/openclaw-weixin" --forceopenclaw gateway restart
[/code]

Якщо під час запуску повідомляється, що встановлений пакет Plugin `requires compiled runtime output for TypeScript entry`, npm-пакет було опубліковано без скомпільованих файлів середовища виконання JavaScript, потрібних OpenClaw. Оновіть або перевстановіть після того, як видавець Plugin випустить виправлений пакет, або тимчасово вимкніть чи видаліть Plugin.

Тимчасове вимкнення:

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-weixin.enabled falseopenclaw gateway restart
[/code]

## Пов’язана документація

  * Огляд каналів: [Канали чатів](</uk/channels>)
  * Сполучення: [Сполучення](</uk/channels/pairing>)
  * Маршрутизація каналів: [Маршрутизація каналів](</uk/channels/channel-routing>)
  * Архітектура Plugin: [Архітектура Plugin](</uk/plugins/architecture>)
  * SDK канального Plugin: [SDK канального Plugin](</uk/plugins/sdk-channel-plugins>)
  * Зовнішній пакет: [@tencent-weixin/openclaw-weixin](<https://www.npmjs.com/package/@tencent-weixin/openclaw-weixin>)


Was this useful?YesNo