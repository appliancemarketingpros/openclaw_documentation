---
title: Plugin Google Meet
source_url: https://docs.openclaw.ai/uk/plugins/google-meet
scraped_at: 2026-05-25
---

Підтримка учасника Google Meet для OpenClaw — Plugin навмисно має явну поведінку:

  * Він приєднується лише до явної URL-адреси `https://meet.google.com/...`.
  * Він може створити новий простір Meet через Google Meet API, а потім приєднатися до поверненої URL-адреси.
  * `agent` — типовий режим зворотного мовлення: транскрибування в реальному часі слухає, налаштований агент OpenClaw відповідає, а звичайний OpenClaw TTS говорить у Meet.
  * `bidi` залишається доступним як резервний режим прямої голосової моделі в реальному часі.
  * Агенти вибирають поведінку приєднання за допомогою `mode`: використовуйте `agent` для живого прослуховування/зворотного мовлення, `bidi` для прямого резервного голосового режиму в реальному часі або `transcribe` для приєднання/керування браузером без моста зворотного мовлення.
  * Автентифікація починається як особистий Google OAuth або вже виконаний вхід у профіль Chrome.
  * Автоматичного оголошення згоди немає.
  * Типовий аудіобекенд Chrome — `BlackHole 2ch`.
  * Chrome може працювати локально або на спареному хості вузла.
  * Twilio приймає номер для дозвону плюс необов’язковий PIN або послідовність DTMF; він не може набирати URL-адресу Meet напряму.
  * Команда CLI — `googlemeet`; `meet` зарезервовано для ширших робочих процесів агентських телеконференцій.


## Швидкий старт

Встановіть локальні аудіозалежності та налаштуйте провайдера транскрибування в реальному часі плюс звичайний OpenClaw TTS. OpenAI є типовим провайдером транскрибування; Google Gemini Live також працює як окремий резервний голосовий режим `bidi` з `realtime.voiceProvider: "google"`:

bashCopy code
[code]
    brew install blackhole-2ch soxexport OPENAI_API_KEY=sk-...# only needed when realtime.voiceProvider is "google" for bidi modeexport GEMINI_API_KEY=...
[/code]

`blackhole-2ch` встановлює віртуальний аудіопристрій `BlackHole 2ch`. Інсталятор Homebrew потребує перезавантаження, перш ніж macOS покаже пристрій:

bashCopy code
[code]
    sudo reboot
[/code]

Після перезавантаження перевірте обидві частини:

bashCopy code
[code]
    system_profiler SPAudioDataType | grep -i BlackHolecommand -v sox
[/code]

Увімкніть Plugin:

json5Copy code
[code]
    {  plugins: {    entries: {      "google-meet": {        enabled: true,        config: {},      },    },  },}
[/code]

Перевірте налаштування:

bashCopy code
[code]
    openclaw googlemeet setup
[/code]

Вивід налаштування призначений для читання агентом і враховує режим. Він повідомляє про профіль Chrome, закріплення вузла, а для приєднань Chrome у реальному часі — про аудіоміст BlackHole/SoX і відкладені перевірки вступу в реальному часі. Для приєднань лише для спостереження перевірте той самий транспорт за допомогою `--mode transcribe`; цей режим пропускає аудіопередумови реального часу, оскільки не слухає й не говорить через міст:

bashCopy code
[code]
    openclaw googlemeet setup --transport chrome-node --mode transcribe
[/code]

Коли налаштовано делегування Twilio, налаштування також повідомляє, чи готові Plugin `voice-call`, облікові дані Twilio та публічна доступність Webhook. Сприймайте будь-яку перевірку `ok: false` як блокер для перевірених транспорту й режиму, перш ніж просити агента приєднатися. Використовуйте `openclaw googlemeet setup --json` для скриптів або машинозчитуваного виводу. Використовуйте `--transport chrome`, `--transport chrome-node` або `--transport twilio`, щоб попередньо перевірити конкретний транспорт до того, як агент спробує його використати.

Для Twilio завжди явно попередньо перевіряйте транспорт, коли типовим транспортом є Chrome:

bashCopy code
[code]
    openclaw googlemeet setup --transport twilio
[/code]

Це виявляє відсутню прив’язку `voice-call`, облікові дані Twilio або недосяжну доступність Webhook до того, як агент спробує набрати зустріч.

Приєднайтеся до зустрічі:

bashCopy code
[code]
    openclaw googlemeet join https://meet.google.com/abc-defg-hij
[/code]

Або дозвольте агенту приєднатися через інструмент `google_meet`:

jsonCopy code
[code]
    {  "action": "join",  "url": "https://meet.google.com/abc-defg-hij",  "transport": "chrome-node",  "mode": "agent"}
[/code]

Агентський інструмент `google_meet` залишається доступним на хостах не-macOS для артефактів, календаря, налаштування, транскрибування, Twilio та потоків `chrome-node`. Локальні дії зворотного мовлення Chrome там заблоковано, оскільки вбудований аудіошлях Chrome зараз залежить від macOS `BlackHole 2ch`. На Linux використовуйте `mode: "transcribe"`, дозвон Twilio або хост macOS `chrome-node` для участі Chrome зі зворотним мовленням.

Створіть нову зустріч і приєднайтеся до неї:

bashCopy code
[code]
    openclaw googlemeet create --transport chrome-node --mode agent
[/code]

Для кімнат, створених через API, використовуйте Google Meet `SpaceConfig.accessType`, коли хочете, щоб політика кімнати без стуку була явною, а не успадкованою з типових параметрів облікового запису Google:

bashCopy code
[code]
    openclaw googlemeet create --access-type OPEN --transport chrome-node --mode agent
[/code]

`OPEN` дозволяє будь-кому з URL-адресою Meet приєднатися без стуку. `TRUSTED` дозволяє довіреним користувачам організації хоста, запрошеним зовнішнім користувачам і користувачам дозвону приєднуватися без стуку. `RESTRICTED` обмежує вхід без стуку лише запрошеними. Ці налаштування застосовуються тільки до офіційного шляху створення Google Meet API, тому облікові дані OAuth мають бути налаштовані.

Якщо ви автентифікували Google Meet до появи цієї опції, повторно виконайте `openclaw googlemeet auth login --json` після додавання області `meetings.space.settings` на екран згоди Google OAuth.

Створіть лише URL-адресу без приєднання:

bashCopy code
[code]
    openclaw googlemeet create --no-join
[/code]

`googlemeet create` має два шляхи:

  * Створення через API: використовується, коли налаштовано облікові дані Google Meet OAuth. Це найдетермінованіший шлях, який не залежить від стану інтерфейсу браузера.
  * Резервний браузерний шлях: використовується, коли облікові дані OAuth відсутні. OpenClaw використовує закріплений вузол Chrome, відкриває `https://meet.google.com/new`, чекає, поки Google перенаправить на справжню URL-адресу з кодом зустрічі, а потім повертає цю URL-адресу. Цей шлях потребує, щоб профіль OpenClaw Chrome на вузлі вже був увійшов у Google. Автоматизація браузера обробляє власний запит Meet на мікрофон під час першого запуску; цей запит не вважається помилкою входу Google. Потоки приєднання та створення також намагаються повторно використати наявну вкладку Meet перед відкриттям нової. Зіставлення ігнорує нешкідливі рядки запиту URL, такі як `authuser`, тому повторна спроба агента має сфокусувати вже відкриту зустріч замість створення другої вкладки Chrome.


Вивід команди/інструмента містить поле `source` (`api` або `browser`), щоб агенти могли пояснити, який шлях було використано. `create` за замовчуванням приєднується до нової зустрічі й повертає `joined: true` плюс сесію приєднання. Щоб лише створити URL-адресу, використовуйте `create --no-join` у CLI або передайте `"join": false` інструменту.

Або скажіть агенту: "Створи Google Meet, приєднайся до нього в режимі агентського зворотного мовлення і надішли мені посилання." Агент має викликати `google_meet` з `action: "create"`, а потім поділитися поверненим `meetingUri`.

jsonCopy code
[code]
    {  "action": "create",  "transport": "chrome-node",  "mode": "agent"}
[/code]

Для приєднання лише для спостереження/керування браузером встановіть `"mode": "transcribe"`. Це не запускає дуплексний голосовий міст у реальному часі, не потребує BlackHole або SoX і не говоритиме назад у зустріч. Приєднання Chrome у цьому режимі також уникають надання дозволу OpenClaw на мікрофон/камеру й уникають шляху Meet **Use microphone**. Якщо Meet показує проміжний вибір аудіо, автоматизація намагається використати шлях без мікрофона, а інакше повідомляє про ручну дію замість відкриття локального мікрофона. У режимі транскрибування керовані транспорти Chrome також встановлюють caption observer Meet за принципом найкращих зусиль. `googlemeet status --json` і `googlemeet doctor` показують `captioning`, `captionsEnabledAttempted`, `transcriptLines`, `lastCaptionAt`, `lastCaptionSpeaker`, `lastCaptionText` і короткий хвіст `recentTranscript`, щоб оператори могли зрозуміти, чи браузер приєднався до дзвінка і чи субтитри Meet створюють текст. Використовуйте `openclaw googlemeet test-listen <meet-url> --transport chrome-node`, коли потрібна перевірка так/ні: він приєднується в режимі транскрибування, чекає на свіжий рух субтитрів або транскрипту й повертає `listenVerified`, `listenTimedOut`, поля ручної дії та останній стан субтитрів.

Під час сесій у реальному часі статус `google_meet` містить стан браузера й аудіомоста, зокрема `inCall`, `manualActionRequired`, `providerConnected`, `realtimeReady`, `audioInputActive`, `audioOutputActive`, останні часові мітки вводу/виводу, лічильники байтів і стан закриття моста. Якщо з’являється безпечний запит сторінки Meet, автоматизація браузера обробляє його, коли може. Вхід, допуск хостом і запити дозволів браузера/ОС повідомляються як ручна дія з причиною й повідомленням, яке агент має передати. Керовані сесії Chrome надсилають вступ або тестову фразу лише після того, як стан браузера повідомить `inCall: true`; інакше статус повідомляє `speechReady: false`, а спроба мовлення блокується замість удавання, що агент говорив у зустріч.

Локальні приєднання Chrome відбуваються через профіль браузера OpenClaw із виконаним входом. Режим реального часу потребує `BlackHole 2ch` для шляху мікрофона/динаміка, який використовує OpenClaw. Для чистого дуплексного аудіо використовуйте окремі віртуальні пристрої або граф у стилі Loopback; одного пристрою BlackHole достатньо для першого smoke test, але він може давати відлуння.

### Локальний Gateway + Parallels Chrome

Вам **не** потрібен повний OpenClaw Gateway або ключ API моделі всередині macOS VM лише для того, щоб VM володіла Chrome. Запустіть Gateway і агента локально, а потім запустіть хост вузла у VM. Увімкніть вбудований Plugin на VM один раз, щоб вузол оголошував команду Chrome:

Що де працює:

  * Хост Gateway: OpenClaw Gateway, робоча область агента, ключі моделі/API, провайдер реального часу і конфігурація Google Meet Plugin.
  * Parallels macOS VM: OpenClaw CLI/хост вузла, Google Chrome, SoX, BlackHole 2ch і профіль Chrome із входом у Google.
  * Не потрібно у VM: сервіс Gateway, конфігурація агента, ключ OpenAI/GPT або налаштування провайдера моделі.


Встановіть залежності VM:

bashCopy code
[code]
    brew install blackhole-2ch sox
[/code]

Перезавантажте VM після встановлення BlackHole, щоб macOS показала `BlackHole 2ch`:

bashCopy code
[code]
    sudo reboot
[/code]

Після перезавантаження перевірте, що VM бачить аудіопристрій і команди SoX:

bashCopy code
[code]
    system_profiler SPAudioDataType | grep -i BlackHolecommand -v sox
[/code]

Встановіть або оновіть OpenClaw у VM, а потім увімкніть там вбудований Plugin:

bashCopy code
[code]
    openclaw plugins enable google-meet
[/code]

Запустіть хост вузла у VM:

bashCopy code
[code]
    openclaw node run --host <gateway-host> --port 18789 --display-name parallels-macos
[/code]

Якщо `<gateway-host>` — це LAN IP і ви не використовуєте TLS, вузол відхиляє plaintext WebSocket, якщо ви явно не дозволите його для цієї довіреної приватної мережі:

bashCopy code
[code]
    OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1 \  openclaw node run --host <gateway-lan-ip> --port 18789 --display-name parallels-macos
[/code]

Використовуйте ту саму змінну середовища під час встановлення вузла як LaunchAgent:

bashCopy code
[code]
    OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1 \  openclaw node install --host <gateway-lan-ip> --port 18789 --display-name parallels-macos --forceopenclaw node restart
[/code]

`OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` — це середовище процесу, а не налаштування `openclaw.json`. `openclaw node install` зберігає його в середовищі LaunchAgent, коли воно присутнє в команді встановлення.

Схваліть вузол із хоста Gateway:

bashCopy code
[code]
    openclaw devices listopenclaw devices approve <requestId>
[/code]

Підтвердьте, що Gateway бачить вузол і що він оголошує як `googlemeet.chrome`, так і можливість браузера/`browser.proxy`:

bashCopy code
[code]
    openclaw nodes status
[/code]

Спрямуйте Meet через цей вузол на хості Gateway:

json5Copy code
[code]
    {  gateway: {    nodes: {      allowCommands: ["googlemeet.chrome", "browser.proxy"],    },  },  plugins: {    entries: {      "google-meet": {        enabled: true,        config: {          defaultTransport: "chrome-node",          chrome: {            guestName: "OpenClaw Agent",            autoJoin: true,            reuseExistingTab: true,          },          chromeNode: {            node: "parallels-macos",          },        },      },    },  },}
[/code]

Тепер приєднуйтеся звичайно з хоста Gateway:

bashCopy code
[code]
    openclaw googlemeet join https://meet.google.com/abc-defg-hij
[/code]

або попросіть агента використати інструмент `google_meet` з `transport: "chrome-node"`.

Для smoke test однією командою, який створює або повторно використовує сесію, вимовляє відому фразу й друкує стан сесії:

bashCopy code
[code]
    openclaw googlemeet test-speech https://meet.google.com/abc-defg-hij
[/code]

Під час приєднання в режимі реального часу автоматизація браузера OpenClaw заповнює ім’я гостя, натискає Join/Ask to join і приймає перший вибір Meet "Use microphone", коли ця підказка з’являється. Під час приєднання лише для спостереження або створення зустрічі лише в браузері вона продовжує після тієї самої підказки без мікрофона, коли цей вибір доступний. Якщо профіль браузера не ввійшов в обліковий запис, Meet очікує допуску від організатора, Chrome потребує дозволу на мікрофон/камеру для приєднання в режимі реального часу або Meet застряг на підказці, яку автоматизація не змогла розв’язати, результат join/test-speech повідомляє `manualActionRequired: true` з `manualActionReason` і `manualActionMessage`. Агенти мають припинити повторні спроби приєднання, повідомити це точне повідомлення разом із поточними `browserUrl`/`browserTitle` і повторити спробу лише після завершення ручної дії в браузері.

Якщо `chromeNode.node` пропущено, OpenClaw автоматично вибирає лише тоді, коли рівно один підключений вузол оголошує і `googlemeet.chrome`, і керування браузером. Якщо підключено кілька придатних вузлів, задайте `chromeNode.node` як id вузла, відображуване ім’я або віддалену IP-адресу.

Поширені перевірки збоїв:

  * `Configured Google Meet node ... is not usable: offline`: закріплений вузол відомий Gateway, але недоступний. Агенти мають трактувати цей вузол як діагностичний стан, а не як придатний хост Chrome, і повідомляти блокер налаштування замість відкату на інший транспорт, якщо користувач цього не просив.
  * `No connected Google Meet-capable node`: запустіть `openclaw node run` у VM, схваліть сполучення і переконайтеся, що `openclaw plugins enable google-meet` і `openclaw plugins enable browser` були виконані у VM. Також підтвердьте, що хост Gateway дозволяє обидві команди вузла через `gateway.nodes.allowCommands: ["googlemeet.chrome", "browser.proxy"]`.
  * `BlackHole 2ch audio device not found`: встановіть `blackhole-2ch` на хості, який перевіряється, і перезавантажтеся перед використанням локального аудіо Chrome.
  * `BlackHole 2ch audio device not found on the node`: встановіть `blackhole-2ch` у VM і перезавантажте VM.
  * Chrome відкривається, але не може приєднатися: увійдіть у профіль браузера всередині VM або залиште `chrome.guestName` заданим для гостьового приєднання. Автоматичне гостьове приєднання використовує автоматизацію браузера OpenClaw через проксі браузера вузла; переконайтеся, що конфігурація браузера вузла вказує на потрібний профіль, наприклад `browser.defaultProfile: "user"` або іменований профіль наявного сеансу.
  * Дублікати вкладок Meet: залиште `chrome.reuseExistingTab: true` увімкненим. OpenClaw активує наявну вкладку для того самого URL Meet перед відкриттям нової, а створення зустрічі в браузері повторно використовує вкладку `https://meet.google.com/new` у процесі або вкладку підказки облікового запису Google перед відкриттям іншої.
  * Немає аудіо: у Meet спрямуйте аудіо мікрофона/динаміка через шлях віртуального аудіопристрою, який використовує OpenClaw; використовуйте окремі віртуальні пристрої або маршрутизацію у стилі Loopback для чистого двостороннього аудіо.


## Нотатки щодо встановлення

Стандартне зворотне мовлення Chrome використовує два зовнішні інструменти:

  * `sox`: аудіоутиліта командного рядка. Plugin використовує явні команди пристрою CoreAudio для стандартного аудіомоста PCM16 24 кГц.
  * `blackhole-2ch`: віртуальний аудіодрайвер macOS. Він створює аудіопристрій `BlackHole 2ch`, через який Chrome/Meet може маршрутизувати аудіо.


OpenClaw не пакує й не розповсюджує жоден із цих пакетів. Документація просить користувачів встановити їх як залежності хоста через Homebrew. SoX ліцензовано як `LGPL-2.0-only AND GPL-2.0-only`; BlackHole має GPL-3.0. Якщо ви створюєте інсталятор або appliance, який пакує BlackHole разом з OpenClaw, перегляньте умови ліцензування upstream BlackHole або отримайте окрему ліцензію від Existential Audio.

## Транспорти

### Chrome

Транспорт Chrome відкриває URL Meet через керування браузером OpenClaw і приєднується як профіль браузера OpenClaw, що ввійшов в обліковий запис. На macOS Plugin перевіряє наявність `BlackHole 2ch` перед запуском. Якщо налаштовано, він також виконує команду перевірки справності аудіомоста та команду запуску перед відкриттям Chrome. Використовуйте `chrome`, коли Chrome/аудіо працюють на хості Gateway; використовуйте `chrome-node`, коли Chrome/аудіо працюють на спареному вузлі, наприклад VM Parallels macOS. Для локального Chrome виберіть профіль через `browser.defaultProfile`; `chrome.browserProfile` передається хостам `chrome-node`.

bashCopy code
[code]
    openclaw googlemeet join https://meet.google.com/abc-defg-hij --transport chromeopenclaw googlemeet join https://meet.google.com/abc-defg-hij --transport chrome-node
[/code]

Маршрутизуйте аудіо мікрофона та динаміка Chrome через локальний аудіоміст OpenClaw. Якщо `BlackHole 2ch` не встановлено, приєднання завершується помилкою налаштування замість тихого приєднання без аудіошляху.

### Twilio

Транспорт Twilio — це суворий план набору, делегований Plugin Voice Call. Він не аналізує сторінки Meet для пошуку телефонних номерів.

Використовуйте це, коли участь через Chrome недоступна або вам потрібен резервний телефонний набір. Google Meet має показувати номер телефонного підключення та PIN для зустрічі; OpenClaw не виявляє їх зі сторінки Meet.

Увімкніть Plugin Voice Call на хості Gateway, а не на вузлі Chrome:

json5Copy code
[code]
    {  plugins: {    allow: ["google-meet", "voice-call", "google"],    entries: {      "google-meet": {        enabled: true,        config: {          defaultTransport: "chrome-node",          // or set "twilio" if Twilio should be the default        },      },      "voice-call": {        enabled: true,        config: {          provider: "twilio",          inboundPolicy: "allowlist",          realtime: {            enabled: true,            provider: "google",            instructions: "Join this Google Meet as an OpenClaw agent. Be brief.",            toolPolicy: "safe-read-only",            providers: {              google: {                silenceDurationMs: 500,                startSensitivity: "high",              },            },          },        },      },      google: {        enabled: true,      },    },  },}
[/code]

Надайте облікові дані Twilio через середовище або конфігурацію. Середовище тримає секрети поза `openclaw.json`:

bashCopy code
[code]
    export TWILIO_ACCOUNT_SID=AC...export TWILIO_AUTH_TOKEN=...export TWILIO_FROM_NUMBER=+15550001234export GEMINI_API_KEY=...
[/code]

Натомість використовуйте `realtime.provider: "openai"` з Plugin постачальника OpenAI і `OPENAI_API_KEY`, якщо це ваш постачальник голосу в режимі реального часу.

Перезапустіть або перезавантажте Gateway після ввімкнення `voice-call`; зміни конфігурації Plugin не з’являються у вже запущеному процесі Gateway, доки він не перезавантажиться.

Потім перевірте:

bashCopy code
[code]
    openclaw config validateopenclaw plugins list | grep -E 'google-meet|voice-call'openclaw googlemeet setup
[/code]

Коли делегування Twilio підключено, `googlemeet setup` містить успішні перевірки `twilio-voice-call-plugin`, `twilio-voice-call-credentials` і `twilio-voice-call-webhook`.

bashCopy code
[code]
    openclaw googlemeet join https://meet.google.com/abc-defg-hij \  --transport twilio \  --dial-in-number +15551234567 \  --pin 123456
[/code]

Використовуйте `--dtmf-sequence`, коли зустріч потребує спеціальної послідовності:

bashCopy code
[code]
    openclaw googlemeet join https://meet.google.com/abc-defg-hij \  --transport twilio \  --dial-in-number +15551234567 \  --dtmf-sequence ww123456#
[/code]

## OAuth і попередня перевірка

OAuth є необов’язковим для створення посилання Meet, оскільки `googlemeet create` може відкотитися до автоматизації браузера. Налаштовуйте OAuth, коли потрібні офіційне створення через API, розв’язання простору або попередні перевірки Meet Media API.

Доступ до Google Meet API використовує користувацький OAuth: створіть OAuth-клієнт Google Cloud, запросіть потрібні scopes, авторизуйте обліковий запис Google, а потім збережіть отриманий refresh token у конфігурації Plugin Google Meet або надайте змінні середовища `OPENCLAW_GOOGLE_MEET_*`.

OAuth не замінює шлях приєднання Chrome. Транспорти Chrome і Chrome-node все одно приєднуються через профіль Chrome, що ввійшов в обліковий запис, BlackHole/SoX і підключений вузол, коли ви використовуєте участь через браузер. OAuth призначений лише для офіційного шляху Google Meet API: створювати простори зустрічей, розв’язувати простори і виконувати попередні перевірки Meet Media API.

### Створення облікових даних Google

У Google Cloud Console:

  1. Створіть або виберіть проєкт Google Cloud.

  2. Увімкніть **Google Meet REST API** для цього проєкту.

  3. Налаштуйте екран згоди OAuth.

     * **Internal** найпростіший для організації Google Workspace.
     * **External** працює для особистих/тестових налаштувань; поки застосунок перебуває в Testing, додайте кожен обліковий запис Google, який авторизуватиме застосунок, як тестового користувача.
  4. Додайте scopes, які запитує OpenClaw:

     * `https://www.googleapis.com/auth/meetings.space.created`
     * `https://www.googleapis.com/auth/meetings.space.readonly`
     * `https://www.googleapis.com/auth/meetings.space.settings`
     * `https://www.googleapis.com/auth/meetings.conference.media.readonly`
  5. Створіть OAuth client ID.

     * Тип застосунку: **Web application**.

     * Авторизований URI переспрямування:

textCopy code
[code]http://localhost:8085/oauth2callback
[/code]

  6. Скопіюйте client ID і client secret.


`meetings.space.created` потрібен Google Meet `spaces.create`. `meetings.space.readonly` дає OpenClaw змогу розв’язувати URL/коди Meet у простори. `meetings.space.settings` дає OpenClaw змогу передавати налаштування `SpaceConfig`, як-от `accessType`, під час створення кімнати через API. `meetings.conference.media.readonly` призначений для попередньої перевірки Meet Media API і медіа роботи; Google може вимагати участі в Developer Preview для фактичного використання Media API. Якщо вам потрібні лише приєднання Chrome на основі браузера, повністю пропустіть OAuth.

### Створення refresh token

Налаштуйте `oauth.clientId` і, за потреби, `oauth.clientSecret`, або передайте їх як змінні середовища, а потім виконайте:

bashCopy code
[code]
    openclaw googlemeet auth login --json
[/code]

Команда друкує конфігураційний блок `oauth` із refresh token. Вона використовує PKCE, localhost callback на `http://localhost:8085/oauth2callback` і ручний потік копіювання/вставлення з `--manual`.

Приклади:

bashCopy code
[code]
    OPENCLAW_GOOGLE_MEET_CLIENT_ID="your-client-id" \OPENCLAW_GOOGLE_MEET_CLIENT_SECRET="your-client-secret" \openclaw googlemeet auth login --json
[/code]

Використовуйте ручний режим, коли браузер не може досягти локального callback:

bashCopy code
[code]
    OPENCLAW_GOOGLE_MEET_CLIENT_ID="your-client-id" \OPENCLAW_GOOGLE_MEET_CLIENT_SECRET="your-client-secret" \openclaw googlemeet auth login --json --manual
[/code]

JSON-вивід містить:

jsonCopy code
[code]
    {  "oauth": {    "clientId": "your-client-id",    "clientSecret": "your-client-secret",    "refreshToken": "refresh-token",    "accessToken": "access-token",    "expiresAt": 1770000000000  },  "scope": "..."}
[/code]

Збережіть об’єкт `oauth` у конфігурації Plugin Google Meet:

json5Copy code
[code]
    {  plugins: {    entries: {      "google-meet": {        enabled: true,        config: {          oauth: {            clientId: "your-client-id",            clientSecret: "your-client-secret",            refreshToken: "refresh-token",          },        },      },    },  },}
[/code]

Надавайте перевагу змінним середовища, коли не хочете зберігати refresh token у конфігурації. Якщо присутні і значення конфігурації, і значення середовища, Plugin спершу розв’язує конфігурацію, а потім fallback середовища.

Згода OAuth включає створення простору Meet, доступ на читання простору Meet і доступ на читання медіа конференції Meet. Якщо ви автентифікувалися до появи підтримки створення зустрічей, повторно виконайте `openclaw googlemeet auth login --json`, щоб refresh token мав scope `meetings.space.created`.

### Перевірка OAuth через doctor

Запустіть OAuth doctor, коли потрібна швидка перевірка справності без секретів:

bashCopy code
[code]
    openclaw googlemeet doctor --oauth --json
[/code]

Це не завантажує runtime Chrome і не потребує підключеного вузла Chrome. Воно перевіряє, що конфігурація OAuth існує і що refresh token може створити access token. JSON-звіт містить лише поля статусу, як-от `ok`, `configured`, `tokenSource`, `expiresAt` і повідомлення перевірок; він не друкує access token, refresh token або client secret.

Поширені результати:

Перевірка | Значення  
---|---  
`oauth-config` | Наявний `oauth.clientId` разом із `oauth.refreshToken`, або кешований токен доступу.  
`oauth-token` | Кешований токен доступу ще чинний, або токен оновлення випустив новий токен доступу.  
`meet-spaces-get` | Необов’язкова перевірка `--meeting` розв’язала наявний простір Meet.  
`meet-spaces-create` | Необов’язкова перевірка `--create-space` створила новий простір Meet.  
  
Щоб також підтвердити ввімкнення Google Meet API і область доступу `spaces.create`, запустіть перевірку створення з побічним ефектом:

bashCopy code
[code]
    openclaw googlemeet doctor --oauth --create-space --jsonopenclaw googlemeet create --no-join --json
[/code]

`--create-space` створює одноразовий URL Meet. Використовуйте його, коли потрібно підтвердити, що в проєкті Google Cloud увімкнено Meet API і що авторизований обліковий запис має область доступу `meetings.space.created`.

Щоб підтвердити доступ для читання до наявного простору зустрічі:

bashCopy code
[code]
    openclaw googlemeet doctor --oauth --meeting https://meet.google.com/abc-defg-hij --jsonopenclaw googlemeet resolve-space --meeting https://meet.google.com/abc-defg-hij
[/code]

`doctor --oauth --meeting` і `resolve-space` підтверджують доступ для читання до наявного простору, до якого авторизований обліковий запис Google має доступ. `403` у цих перевірках зазвичай означає, що Google Meet REST API вимкнено, погоджений токен оновлення не має потрібної області доступу, або обліковий запис Google не може отримати доступ до цього простору Meet. Помилка токена оновлення означає, що потрібно повторно виконати `openclaw googlemeet auth login --json` і зберегти новий блок `oauth`.

Для резервного режиму браузера облікові дані OAuth не потрібні. У цьому режимі автентифікація Google надходить із профілю Chrome, у який виконано вхід на вибраному вузлі, а не з конфігурації OpenClaw.

Ці змінні середовища приймаються як резервні значення:

  * `OPENCLAW_GOOGLE_MEET_CLIENT_ID` або `GOOGLE_MEET_CLIENT_ID`
  * `OPENCLAW_GOOGLE_MEET_CLIENT_SECRET` або `GOOGLE_MEET_CLIENT_SECRET`
  * `OPENCLAW_GOOGLE_MEET_REFRESH_TOKEN` або `GOOGLE_MEET_REFRESH_TOKEN`
  * `OPENCLAW_GOOGLE_MEET_ACCESS_TOKEN` або `GOOGLE_MEET_ACCESS_TOKEN`
  * `OPENCLAW_GOOGLE_MEET_ACCESS_TOKEN_EXPIRES_AT` або `GOOGLE_MEET_ACCESS_TOKEN_EXPIRES_AT`
  * `OPENCLAW_GOOGLE_MEET_DEFAULT_MEETING` або `GOOGLE_MEET_DEFAULT_MEETING`
  * `OPENCLAW_GOOGLE_MEET_PREVIEW_ACK` або `GOOGLE_MEET_PREVIEW_ACK`


Розв’яжіть URL Meet, код або `spaces/{id}` через `spaces.get`:

bashCopy code
[code]
    openclaw googlemeet resolve-space --meeting https://meet.google.com/abc-defg-hij
[/code]

Запустіть попередню перевірку перед роботою з медіа:

bashCopy code
[code]
    openclaw googlemeet preflight --meeting https://meet.google.com/abc-defg-hij
[/code]

Виведіть список артефактів зустрічі та відвідуваність після того, як Meet створить записи конференції:

bashCopy code
[code]
    openclaw googlemeet artifacts --meeting https://meet.google.com/abc-defg-hijopenclaw googlemeet attendance --meeting https://meet.google.com/abc-defg-hijopenclaw googlemeet export --meeting https://meet.google.com/abc-defg-hij --output ./meet-export
[/code]

З `--meeting`, `artifacts` і `attendance` типово використовують найновіший запис конференції. Передайте `--all-conference-records`, коли потрібні всі збережені записи для цієї зустрічі.

Пошук у календарі може розв’язати URL зустрічі з Google Calendar перед читанням артефактів Meet:

bashCopy code
[code]
    openclaw googlemeet latest --todayopenclaw googlemeet calendar-events --today --jsonopenclaw googlemeet artifacts --event "Weekly sync"openclaw googlemeet attendance --today --format csv --output attendance.csv
[/code]

`--today` шукає в сьогоднішньому календарі `primary` подію Calendar з посиланням Google Meet. Використовуйте `--event <query>` для пошуку відповідного тексту події та `--calendar <id>` для неосновного календаря. Пошук у календарі потребує нового входу OAuth, який включає область доступу лише для читання подій Calendar. `calendar-events` попередньо показує відповідні події Meet і позначає подію, яку вибере `latest`, `artifacts`, `attendance` або `export`.

Якщо ви вже знаєте ідентифікатор запису конференції, зверніться до нього напряму:

bashCopy code
[code]
    openclaw googlemeet latest --meeting https://meet.google.com/abc-defg-hijopenclaw googlemeet artifacts --conference-record conferenceRecords/abc123 --jsonopenclaw googlemeet attendance --conference-record conferenceRecords/abc123 --json
[/code]

Завершіть активну конференцію для створеного через API простору, коли потрібно закрити кімнату після дзвінка:

bashCopy code
[code]
    openclaw googlemeet end-active-conference https://meet.google.com/abc-defg-hij
[/code]

Це викликає Google Meet `spaces.endActiveConference` і потребує OAuth з областю доступу `meetings.space.created` для простору, яким авторизований обліковий запис може керувати. OpenClaw приймає URL Meet, код зустрічі або вхід `spaces/{id}` і розв’язує його в ресурс простору API перед завершенням активної конференції. Це окремо від `googlemeet leave`: `leave` зупиняє локальну/сеансову участь OpenClaw, тоді як `end-active-conference` просить Google Meet завершити активну конференцію для простору.

Запишіть читабельний звіт:

bashCopy code
[code]
    openclaw googlemeet artifacts --conference-record conferenceRecords/abc123 \  --format markdown --output meet-artifacts.mdopenclaw googlemeet attendance --conference-record conferenceRecords/abc123 \  --format markdown --output meet-attendance.mdopenclaw googlemeet attendance --conference-record conferenceRecords/abc123 \  --format csv --output meet-attendance.csvopenclaw googlemeet export --conference-record conferenceRecords/abc123 \  --include-doc-bodies --zip --output meet-exportopenclaw googlemeet export --conference-record conferenceRecords/abc123 \  --include-doc-bodies --dry-run
[/code]

`artifacts` повертає метадані запису конференції, а також метадані ресурсів учасників, записів, транскрипту, структурованих записів транскрипту та розумних нотаток, коли Google надає їх для зустрічі. Використовуйте `--no-transcript-entries`, щоб пропустити пошук записів для великих зустрічей. `attendance` розгортає учасників у рядки сеансів учасників із часом першої/останньої появи, загальною тривалістю сеансу, прапорцями запізнення/раннього виходу та дубльованими ресурсами учасників, об’єднаними за користувачем із виконаним входом або відображуваним іменем. Передайте `--no-merge-duplicates`, щоб залишити необроблені ресурси учасників окремими, `--late-after-minutes`, щоб налаштувати виявлення запізнень, і `--early-before-minutes`, щоб налаштувати виявлення раннього виходу.

`export` записує папку, що містить `summary.md`, `attendance.csv`, `transcript.md`, `artifacts.json`, `attendance.json` і `manifest.json`. `manifest.json` фіксує вибраний вхід, параметри експорту, записи конференції, вихідні файли, лічильники, джерело токена, подію Calendar, якщо її було використано, та будь-які попередження про часткове отримання. Передайте `--zip`, щоб також записати переносний архів поруч із папкою. Передайте `--include-doc-bodies`, щоб експортувати текст пов’язаних транскриптів і розумних нотаток Google Docs через Google Drive `files.export`; для цього потрібен новий вхід OAuth, який включає область доступу лише для читання Drive Meet. Без `--include-doc-bodies` експорти містять лише метадані Meet і структуровані записи транскрипту. Якщо Google повертає часткову помилку артефакту, наприклад помилку списку розумних нотаток, запису транскрипту або тіла документа Drive, зведення та маніфест зберігають попередження замість того, щоб провалити весь експорт. Використовуйте `--dry-run`, щоб отримати ті самі дані артефактів/відвідуваності й надрукувати JSON маніфесту без створення папки або ZIP. Це корисно перед записом великого експорту або коли агенту потрібні лише лічильники, вибрані записи та попередження.

Агенти також можуть створити той самий пакет через інструмент `google_meet`:

jsonCopy code
[code]
    {  "action": "export",  "conferenceRecord": "conferenceRecords/abc123",  "includeDocumentBodies": true,  "outputDir": "meet-export",  "zip": true}
[/code]

Установіть `"dryRun": true`, щоб повернути лише маніфест експорту та пропустити запис файлів.

Агенти також можуть створити кімнату з підтримкою API з явною політикою доступу:

jsonCopy code
[code]
    {  "action": "create",  "transport": "chrome-node",  "mode": "agent",  "accessType": "OPEN"}
[/code]

І вони можуть завершити активну конференцію для відомої кімнати:

jsonCopy code
[code]
    {  "action": "end_active_conference",  "meeting": "https://meet.google.com/abc-defg-hij"}
[/code]

Для валідації спочатку з прослуховуванням агенти мають використовувати `test_listen`, перш ніж стверджувати, що зустріч корисна:

jsonCopy code
[code]
    {  "action": "test_listen",  "url": "https://meet.google.com/abc-defg-hij",  "transport": "chrome-node",  "timeoutMs": 30000}
[/code]

Запустіть захищений живий smoke-тест на реальній збереженій зустрічі:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 \OPENCLAW_GOOGLE_MEET_LIVE_MEETING=https://meet.google.com/abc-defg-hij \pnpm test:live -- extensions/google-meet/google-meet.live.test.ts
[/code]

Запустіть живу браузерну перевірку спочатку з прослуховуванням на зустрічі, де хтось буде говорити, а субтитри Meet доступні:

bashCopy code
[code]
    openclaw googlemeet setup --transport chrome-node --mode transcribeopenclaw googlemeet test-listen https://meet.google.com/abc-defg-hij --transport chrome-node --timeout-ms 30000
[/code]

Середовище живого smoke-тесту:

  * `OPENCLAW_LIVE_TEST=1` вмикає захищені живі тести.
  * `OPENCLAW_GOOGLE_MEET_LIVE_MEETING` вказує на збережений URL Meet, код або `spaces/{id}`.
  * `OPENCLAW_GOOGLE_MEET_CLIENT_ID` або `GOOGLE_MEET_CLIENT_ID` надає ідентифікатор клієнта OAuth.
  * `OPENCLAW_GOOGLE_MEET_REFRESH_TOKEN` або `GOOGLE_MEET_REFRESH_TOKEN` надає токен оновлення.
  * Необов’язково: `OPENCLAW_GOOGLE_MEET_CLIENT_SECRET`, `OPENCLAW_GOOGLE_MEET_ACCESS_TOKEN` і `OPENCLAW_GOOGLE_MEET_ACCESS_TOKEN_EXPIRES_AT` використовують ті самі резервні імена без префікса `OPENCLAW_`.


Базовий живий smoke-тест артефактів/відвідуваності потребує `https://www.googleapis.com/auth/meetings.space.readonly` і `https://www.googleapis.com/auth/meetings.conference.media.readonly`. Пошук у календарі потребує `https://www.googleapis.com/auth/calendar.events.readonly`. Експорт тіла документа Drive потребує `https://www.googleapis.com/auth/drive.meet.readonly`.

Створіть новий простір Meet:

bashCopy code
[code]
    openclaw googlemeet create
[/code]

Команда друкує новий `meeting uri`, джерело та сеанс приєднання. З обліковими даними OAuth вона використовує офіційний Google Meet API. Без облікових даних OAuth вона використовує профіль браузера з виконаним входом у закріпленому вузлі Chrome як резервний варіант. Агенти можуть використовувати інструмент `google_meet` з `action: "create"`, щоб створити зустріч і приєднатися за один крок. Для створення лише URL передайте `"join": false`.

Приклад JSON-виводу з резервного режиму браузера:

jsonCopy code
[code]
    {  "source": "browser",  "meetingUri": "https://meet.google.com/abc-defg-hij",  "joined": true,  "browser": {    "nodeId": "ba0f4e4bc...",    "targetId": "tab-1"  },  "join": {    "session": {      "id": "meet_...",      "url": "https://meet.google.com/abc-defg-hij"    }  }}
[/code]

Якщо резервний режим браузера натрапляє на вхід Google або блокер дозволів Meet до того, як може створити URL, метод Gateway повертає невдалу відповідь, а інструмент `google_meet` повертає структуровані подробиці замість простого рядка:

jsonCopy code
[code]
    {  "source": "browser",  "error": "google-login-required: Sign in to Google in the OpenClaw browser profile, then retry meeting creation.",  "manualActionRequired": true,  "manualActionReason": "google-login-required",  "manualActionMessage": "Sign in to Google in the OpenClaw browser profile, then retry meeting creation.",  "browser": {    "nodeId": "ba0f4e4bc...",    "targetId": "tab-1",    "browserUrl": "https://accounts.google.com/signin",    "browserTitle": "Sign in - Google Accounts"  }}
[/code]

Коли агент бачить `manualActionRequired: true`, він має повідомити `manualActionMessage` разом із контекстом вузла/вкладки браузера та припинити відкривати нові вкладки Meet, доки оператор не завершить крок у браузері.

Приклад JSON-виводу зі створення через API:

jsonCopy code
[code]
    {  "source": "api",  "meetingUri": "https://meet.google.com/abc-defg-hij",  "joined": true,  "space": {    "name": "spaces/abc-defg-hij",    "meetingCode": "abc-defg-hij",    "meetingUri": "https://meet.google.com/abc-defg-hij"  },  "join": {    "session": {      "id": "meet_...",      "url": "https://meet.google.com/abc-defg-hij"    }  }}
[/code]

Створення Meet типово приєднує до зустрічі. Транспорту Chrome або Chrome-node все ще потрібен профіль Google Chrome із виконаним входом, щоб приєднатися через браузер. Якщо з профілю виконано вихід, OpenClaw повідомляє `manualActionRequired: true` або помилку резервного браузерного варіанта й просить оператора завершити вхід у Google перед повторною спробою.

Установлюйте `preview.enrollmentAcknowledged: true` лише після підтвердження, що ваш Cloud-проєкт, OAuth principal і учасники зустрічі зареєстровані в Google Workspace Developer Preview Program для Meet media APIs.

## Конфігурація

Спільному шляху агента Chrome потрібні лише ввімкнений Plugin, BlackHole, SoX, ключ провайдера транскрипції в реальному часі та налаштований провайдер TTS OpenClaw. OpenAI є типовим провайдером транскрипції; задайте `realtime.voiceProvider` як `"google"` і `realtime.model`, щоб використовувати Google Gemini Live для режиму `bidi` без зміни типового провайдера транскрипції в режимі агента:

bashCopy code
[code]
    brew install blackhole-2ch soxexport OPENAI_API_KEY=sk-...# orexport GEMINI_API_KEY=...
[/code]

Задайте конфігурацію Plugin у `plugins.entries.google-meet.config`:

json5Copy code
[code]
    {  plugins: {    entries: {      "google-meet": {        enabled: true,        config: {},      },    },  },}
[/code]

Типові значення:

  * `defaultTransport: "chrome"`
  * `defaultMode: "agent"` (`"realtime"` приймається лише як застарілий псевдонім сумісності для `"agent"`; нові виклики інструментів мають указувати `"agent"`)
  * `chromeNode.node`: необов’язковий id/ім’я/IP вузла для `chrome-node`
  * `chrome.audioBackend: "blackhole-2ch"`
  * `chrome.guestName: "OpenClaw Agent"`: ім’я, що використовується на гостьовому екрані Meet без виконаного входу
  * `chrome.autoJoin: true`: best-effort заповнення імені гостя та натискання Join Now через браузерну автоматизацію OpenClaw на `chrome-node`
  * `chrome.reuseExistingTab: true`: активувати наявну вкладку Meet замість відкривання дублікатів
  * `chrome.waitForInCallMs: 20000`: чекати, доки вкладка Meet повідомить про перебування у виклику, перш ніж запуститься вступ talk-back
  * `chrome.audioFormat: "pcm16-24khz"`: аудіоформат пари команд. Використовуйте `"g711-ulaw-8khz"` лише для застарілих/кастомних пар команд, які досі видають телефонний аудіосигнал.
  * `chrome.audioBufferBytes: 4096`: буфер обробки SoX для згенерованих аудіокоманд пари команд Chrome. Це половина типового буфера SoX у 8192 байти, що зменшує типову затримку pipe, залишаючи можливість збільшити його на завантажених хостах. Значення нижче мінімуму SoX обмежуються до 17 байтів.
  * `chrome.audioInputCommand`: команда SoX, яка читає з CoreAudio `BlackHole 2ch` і записує аудіо у форматі `chrome.audioFormat`
  * `chrome.audioOutputCommand`: команда SoX, яка читає аудіо у форматі `chrome.audioFormat` і записує в CoreAudio `BlackHole 2ch`
  * `chrome.bargeInInputCommand`: необов’язкова команда локального мікрофона, яка записує signed 16-bit little-endian mono PCM для виявлення людського втручання, поки активне відтворення асистента. Наразі це застосовується до розміщеного на Gateway мосту пари команд `chrome`.
  * `chrome.bargeInRmsThreshold: 650`: рівень RMS, який рахується людським перериванням на `chrome.bargeInInputCommand`
  * `chrome.bargeInPeakThreshold: 2500`: піковий рівень, який рахується людським перериванням на `chrome.bargeInInputCommand`
  * `chrome.bargeInCooldownMs: 900`: мінімальна затримка між повторними очищеннями людського переривання
  * `mode: "agent"`: типовий режим talk-back. Мовлення учасників транскрибується налаштованим провайдером транскрипції в реальному часі, надсилається налаштованому агенту OpenClaw у сесії підагента для окремої зустрічі та озвучується назад через звичайний runtime TTS OpenClaw.
  * `mode: "bidi"`: резервний прямий двонапрямний режим моделі реального часу. Провайдер голосу реального часу відповідає безпосередньо на мовлення учасників і може викликати `openclaw_agent_consult` для глибших відповідей або відповідей із підтримкою інструментів.
  * `mode: "transcribe"`: режим лише спостереження без мосту talk-back.
  * `realtime.provider: "openai"`: резервний варіант сумісності, що використовується, коли наведені нижче scoped-поля провайдера не задані.
  * `realtime.transcriptionProvider: "openai"`: id провайдера, який режим `agent` використовує для транскрипції в реальному часі.
  * `realtime.voiceProvider`: id провайдера, який режим `bidi` використовує для прямого голосу в реальному часі. Задайте його як `"google"`, щоб використовувати Gemini Live, зберігаючи транскрипцію режиму агента на OpenAI.
  * `realtime.toolPolicy: "safe-read-only"`
  * `realtime.instructions`: короткі усні відповіді з `openclaw_agent_consult` для глибших відповідей
  * `realtime.introMessage`: коротка усна перевірка готовності, коли міст реального часу підключається; задайте `""`, щоб приєднатися беззвучно
  * `realtime.agentId`: необов’язковий id агента OpenClaw для `openclaw_agent_consult`; типово `main`


Необов’язкові перевизначення:

json5Copy code
[code]
    {  defaults: {    meeting: "https://meet.google.com/abc-defg-hij",  },  browser: {    defaultProfile: "openclaw",  },  chrome: {    guestName: "OpenClaw Agent",    waitForInCallMs: 30000,    bargeInInputCommand: [      "sox",      "-q",      "-t",      "coreaudio",      "External Microphone",      "-r",      "24000",      "-c",      "1",      "-b",      "16",      "-e",      "signed-integer",      "-t",      "raw",      "-",    ],  },  chromeNode: {    node: "parallels-macos",  },  defaultMode: "agent",  realtime: {    provider: "openai",    transcriptionProvider: "openai",    voiceProvider: "google",    model: "gemini-2.5-flash-native-audio-preview-12-2025",    agentId: "jay",    toolPolicy: "owner",    introMessage: "Say exactly: I'm here.",    providers: {      google: {        voice: "Kore",      },    },  },}
[/code]

ElevenLabs для прослуховування й озвучення в режимі агента:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "elevenlabs",      providers: {        elevenlabs: {          modelId: "eleven_v3",          voiceId: "pMsXgVXv3BLzUgSXRplE",        },      },    },  },  plugins: {    entries: {      "google-meet": {        config: {          realtime: {            transcriptionProvider: "elevenlabs",            providers: {              elevenlabs: {                modelId: "scribe_v2_realtime",                audioFormat: "ulaw_8000",                sampleRate: 8000,                commitStrategy: "vad",              },            },          },        },      },    },  },}
[/code]

Постійний голос Meet береться з `messages.tts.providers.elevenlabs.voiceId`. Відповіді агента також можуть використовувати директиви `[[tts:voiceId=... model=eleven_v3]]` для окремих відповідей, коли перевизначення моделі TTS увімкнено, але конфігурація є детермінованим типовим варіантом для зустрічей. Під час приєднання журнали мають показати `transcriptionProvider=elevenlabs`, а кожна озвучена відповідь має журналювати `provider=elevenlabs model=eleven_v3 voice=<voiceId>`.

Конфігурація лише для Twilio:

json5Copy code
[code]
    {  defaultTransport: "twilio",  twilio: {    defaultDialInNumber: "+15551234567",    defaultPin: "123456",  },  voiceCall: {    gatewayUrl: "ws://127.0.0.1:18789",  },}
[/code]

`voiceCall.enabled` типово має значення `true`; з транспортом Twilio він делегує фактичний PSTN-виклик, DTMF і вступне привітання Plugin Voice Call. Voice Call відтворює послідовність DTMF перед відкриттям медіапотоку реального часу, а потім використовує збережений вступний текст як початкове привітання реального часу. Якщо `voice-call` не ввімкнено, Google Meet усе ще може перевірити та записати план набору, але не може здійснити виклик Twilio.

## Інструмент

Агенти можуть використовувати інструмент `google_meet`:

jsonCopy code
[code]
    {  "action": "join",  "url": "https://meet.google.com/abc-defg-hij",  "transport": "chrome-node",  "mode": "agent"}
[/code]

Використовуйте `transport: "chrome"`, коли Chrome працює на хості Gateway. Використовуйте `transport: "chrome-node"`, коли Chrome працює на спареному вузлі, наприклад Parallels VM. В обох випадках провайдери моделей і `openclaw_agent_consult` працюють на хості Gateway, тому облікові дані моделей залишаються там. Із типовим `mode: "agent"` провайдер транскрипції в реальному часі обробляє прослуховування, налаштований агент OpenClaw створює відповідь, а звичайний TTS OpenClaw озвучує її в Meet. Використовуйте `mode: "bidi"`, коли хочете, щоб голосова модель реального часу відповідала безпосередньо. Сирий `mode: "realtime"` досі приймається як застарілий псевдонім сумісності для `mode: "agent"`, але більше не рекламується в схемі інструмента агента. Журнали режиму агента включають визначеного провайдера/модель транскрипції під час запуску мосту, а також провайдера TTS, модель, голос, формат виводу та частоту дискретизації після кожної синтезованої відповіді.

Використовуйте `action: "status"`, щоб перелічити активні сесії або переглянути id сесії. Використовуйте `action: "speak"` із `sessionId` і `message`, щоб змусити агента реального часу говорити негайно. Використовуйте `action: "test_speech"`, щоб створити або повторно використати сесію, запустити відому фразу та повернути стан `inCall`, коли хост Chrome може його повідомити. `test_speech` завжди примусово використовує `mode: "agent"` і завершується помилкою, якщо його просять працювати в `mode: "transcribe"`, оскільки сесії лише спостереження навмисно не можуть видавати мовлення. Його результат `speechOutputVerified` базується на збільшенні байтів аудіовиходу реального часу під час цього тестового виклику, тому повторно використана сесія зі старішим аудіо не рахується як свіжа успішна перевірка мовлення. Використовуйте `action: "leave"`, щоб позначити сесію завершеною.

`status` включає стан Chrome, коли доступно:

  * `inCall`: Chrome, схоже, перебуває всередині виклику Meet
  * `micMuted`: best-effort стан мікрофона Meet
  * `manualActionRequired` / `manualActionReason` / `manualActionMessage`: профілю браузера потрібні ручний вхід, допуск від хоста Meet, дозволи або ремонт керування браузером, перш ніж мовлення зможе працювати
  * `speechReady` / `speechBlockedReason` / `speechBlockedMessage`: чи дозволено кероване мовлення Chrome зараз. `speechReady: false` означає, що OpenClaw не надіслав вступну/тестову фразу в аудіоміст.
  * `providerConnected` / `realtimeReady`: стан голосового мосту реального часу
  * `lastInputAt` / `lastOutputAt`: останнє аудіо, побачене з мосту або надіслане до нього
  * `audioOutputRouted` / `audioOutputDeviceLabel`: чи медіавихід вкладки Meet активно маршрутизовано до пристрою BlackHole, який використовує міст
  * `lastSuppressedInputAt` / `suppressedInputBytes`: вхід local loopback, проігнорований, поки активне відтворення асистента

jsonCopy code
[code]
    {  "action": "speak",  "sessionId": "meet_...",  "message": "Say exactly: I'm here and listening."}
[/code]

## Режими agent і bidi

Режим Chrome `agent` оптимізовано для поведінки "мій агент на зустрічі". Провайдер транскрипції в реальному часі чує аудіо зустрічі, фінальні транскрипти учасників маршрутизуються через налаштованого агента OpenClaw, а відповідь озвучується через звичайний runtime TTS OpenClaw. Задайте `mode: "bidi"`, коли хочете, щоб голосова модель реального часу відповідала безпосередньо. Близькі фінальні фрагменти транскриптів об’єднуються перед consult, щоб один усний turn не створював кілька застарілих часткових відповідей. Вхід реального часу також приглушується, поки поставлене в чергу аудіо асистента ще відтворюється, а нещодавні схожі на асистента відлуння транскриптів ігноруються перед consult агента, щоб local loopback BlackHole не змушував агента відповідати на власне мовлення.

Режим | Хто визначає відповідь | Шлях мовленнєвого виводу | Коли використовувати  
---|---|---|---  
`agent` | Налаштований агент OpenClaw | Звичайний runtime TTS OpenClaw | Коли потрібна поведінка "мій агент на зустрічі"  
`bidi` | Голосова модель реального часу | Аудіовідповідь провайдера голосу реального часу | Коли потрібен голосовий цикл розмови з найменшою затримкою  
  
У режимі `bidi`, коли моделі реального часу потрібні глибше міркування, актуальна інформація або звичайні інструменти OpenClaw, вона може викликати `openclaw_agent_consult`.

Інструмент consult запускає звичайного агента OpenClaw у фоновому режимі з контекстом нещодавньої стенограми зустрічі та повертає стислу усну відповідь. У режимі `agent` OpenClaw надсилає цю відповідь безпосередньо в середовище виконання TTS; у режимі `bidi` модель голосу в реальному часі може озвучити результат consult назад у зустріч. Він використовує той самий спільний механізм consult, що й Voice Call.

За замовчуванням consult виконується для агента `main`. Установіть `realtime.agentId`, коли lane Meet має звертатися до окремого робочого простору агента OpenClaw, стандартних параметрів моделі, політики інструментів, пам’яті та історії сесій.

Consult у режимі агента використовує ключ сесії `agent:<id>:subagent:google-meet:<session>` для кожної зустрічі, щоб подальші запитання зберігали контекст зустрічі, успадковуючи звичайну політику агента від налаштованого агента.

`realtime.toolPolicy` керує виконанням consult:

  * `safe-read-only`: показати інструмент consult і обмежити звичайного агента до `read`, `web_search`, `web_fetch`, `x_search`, `memory_search` і `memory_get`.
  * `owner`: показати інструмент consult і дозволити звичайному агенту використовувати звичайну політику інструментів агента.
  * `none`: не показувати інструмент consult голосовій моделі в реальному часі.


Ключ сесії consult обмежений окремою сесією Meet, тому подальші виклики consult можуть повторно використовувати попередній контекст consult під час тієї самої зустрічі.

Щоб примусово виконати усну перевірку готовності після того, як Chrome повністю приєднався до виклику:

bashCopy code
[code]
    openclaw googlemeet speak meet_... "Say exactly: I'm here and listening."
[/code]

Для повної smoke-перевірки приєднання та озвучення:

bashCopy code
[code]
    openclaw googlemeet test-speech https://meet.google.com/abc-defg-hij \  --transport chrome-node \  --message "Say exactly: I'm here and listening."
[/code]

## Контрольний список live-тесту

Використовуйте цю послідовність перед передаванням зустрічі агенту без нагляду:

bashCopy code
[code]
    openclaw googlemeet setupopenclaw nodes statusopenclaw googlemeet test-speech https://meet.google.com/abc-defg-hij \  --transport chrome-node \  --message "Say exactly: Google Meet speech test complete."
[/code]

Очікуваний стан Chrome-node:

  * `googlemeet setup` повністю зелений.
  * `googlemeet setup` включає `chrome-node-connected`, коли Chrome-node є транспортом за замовчуванням або вузол закріплено.
  * `nodes status` показує, що вибраний вузол підключено.
  * Вибраний вузол оголошує і `googlemeet.chrome`, і `browser.proxy`.
  * Вкладка Meet приєднується до виклику, а `test-speech` повертає стан Chrome із `inCall: true`.


Для віддаленого хоста Chrome, наприклад Parallels macOS VM, це найкоротша безпечна перевірка після оновлення Gateway або VM:

bashCopy code
[code]
    openclaw googlemeet setupopenclaw nodes status --connectedopenclaw nodes invoke \  --node parallels-macos \  --command googlemeet.chrome \  --params '{"action":"setup"}'
[/code]

Це підтверджує, що Plugin Gateway завантажено, вузол VM підключено з поточним токеном, а аудіоміст Meet доступний до того, як агент відкриє реальну вкладку зустрічі.

Для smoke-перевірки Twilio використовуйте зустріч, яка надає дані телефонного дозвону:

bashCopy code
[code]
    openclaw googlemeet setupopenclaw googlemeet join https://meet.google.com/abc-defg-hij \  --transport twilio \  --dial-in-number +15551234567 \  --pin 123456
[/code]

Очікуваний стан Twilio:

  * `googlemeet setup` включає зелені перевірки `twilio-voice-call-plugin`, `twilio-voice-call-credentials` і `twilio-voice-call-webhook`.
  * `voicecall` доступний у CLI після перезавантаження Gateway.
  * Повернена сесія має `transport: "twilio"` і `twilio.voiceCallId`.
  * `openclaw logs --follow` показує, що DTMF TwiML віддано перед realtime TwiML, а потім міст реального часу з початковим привітанням у черзі.
  * `googlemeet leave <sessionId>` завершує делегований голосовий виклик.


## Усунення несправностей

### Агент не бачить інструмент Google Meet

Переконайтеся, що Plugin увімкнено в конфігурації Gateway, і перезавантажте Gateway:

bashCopy code
[code]
    openclaw plugins list | grep google-meetopenclaw googlemeet setup
[/code]

Якщо ви щойно редагували `plugins.entries.google-meet`, перезапустіть або перезавантажте Gateway. Запущений агент бачить лише інструменти Plugin, зареєстровані поточним процесом Gateway.

На хостах Gateway не з macOS інструмент `google_meet`, видимий агенту, залишається видимим, але локальні дії з відповіддю голосом через Chrome блокуються до потрапляння в аудіоміст. Локальний звук відповіді через Chrome зараз залежить від macOS `BlackHole 2ch`, тому Linux-агенти мають використовувати `mode: "transcribe"`, дозвін Twilio або хост macOS `chrome-node` замість стандартного локального шляху агента Chrome.

### Немає підключеного вузла з підтримкою Google Meet

На хості вузла виконайте:

bashCopy code
[code]
    openclaw plugins enable google-meetopenclaw plugins enable browserOPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1 \  openclaw node run --host <gateway-lan-ip> --port 18789 --display-name parallels-macos
[/code]

На хості Gateway затвердьте вузол і перевірте команди:

bashCopy code
[code]
    openclaw devices listopenclaw devices approve <requestId>openclaw nodes status
[/code]

Вузол має бути підключений і перелічувати `googlemeet.chrome` разом із `browser.proxy`. Конфігурація Gateway має дозволяти ці команди вузла:

json5Copy code
[code]
    {  gateway: {    nodes: {      allowCommands: ["browser.proxy", "googlemeet.chrome"],    },  },}
[/code]

Якщо `googlemeet setup` не проходить `chrome-node-connected` або журнал Gateway повідомляє `gateway token mismatch`, перевстановіть або перезапустіть вузол із поточним токеном Gateway. Для LAN Gateway це зазвичай означає:

bashCopy code
[code]
    OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1 \  openclaw node install \  --host <gateway-lan-ip> \  --port 18789 \  --display-name parallels-macos \  --force
[/code]

Потім перезавантажте сервіс вузла та повторно виконайте:

bashCopy code
[code]
    openclaw googlemeet setupopenclaw nodes status --connected
[/code]

### Браузер відкривається, але агент не може приєднатися

Виконайте `googlemeet test-listen` для приєднань лише для спостереження або `googlemeet test-speech` для приєднань у реальному часі, а потім перегляньте повернений стан Chrome. Якщо будь-яка перевірка повідомляє `manualActionRequired: true`, покажіть `manualActionMessage` оператору та припиніть повторні спроби, доки дія в браузері не буде завершена.

Поширені ручні дії:

  * Увійти в профіль Chrome.
  * Допустити гостя з облікового запису хоста Meet.
  * Надати Chrome дозволи на мікрофон/камеру, коли з’явиться нативний запит дозволу Chrome.
  * Закрити або виправити завислий діалог дозволів Meet.


Не повідомляйте "not signed in" лише тому, що Meet показує "Do you want people to hear you in the meeting?" Це проміжний екран вибору аудіо Meet; OpenClaw натискає **Use microphone** через автоматизацію браузера, коли доступно, і продовжує очікувати реального стану зустрічі. Для резервного створення лише через браузер OpenClaw може натиснути **Continue without microphone** , тому що створення URL не потребує аудіошляху в реальному часі.

### Не вдається створити зустріч

`googlemeet create` спочатку використовує endpoint Google Meet API `spaces.create`, коли облікові дані OAuth налаштовано. Без облікових даних OAuth він переходить до резервного браузера закріпленого вузла Chrome. Перевірте:

  * Для створення через API: налаштовано `oauth.clientId` і `oauth.refreshToken`, або наявні відповідні змінні середовища `OPENCLAW_GOOGLE_MEET_*`.
  * Для створення через API: refresh token було видано після додавання підтримки створення. Старіші токени можуть не мати scope `meetings.space.created`; повторно виконайте `openclaw googlemeet auth login --json` і оновіть конфігурацію Plugin.
  * Для резервного браузера: `defaultTransport: "chrome-node"` і `chromeNode.node` вказують на підключений вузол із `browser.proxy` і `googlemeet.chrome`.
  * Для резервного браузера: профіль OpenClaw Chrome на цьому вузлі увійшов у Google і може відкрити `https://meet.google.com/new`.
  * Для резервного браузера: повторні спроби повторно використовують наявну вкладку `https://meet.google.com/new` або вкладку запиту облікового запису Google перед відкриттям нової вкладки. Якщо час очікування агента спливає, повторіть виклик інструмента, а не відкривайте іншу вкладку Meet вручну.
  * Для резервного браузера: якщо інструмент повертає `manualActionRequired: true`, використовуйте повернені `browser.nodeId`, `browser.targetId`, `browserUrl` і `manualActionMessage`, щоб скерувати оператора. Не повторюйте спроби в циклі, доки ця дія не буде завершена.
  * Для резервного браузера: якщо Meet показує "Do you want people to hear you in the meeting?", залиште вкладку відкритою. OpenClaw має натиснути **Use microphone** або, для резервного створення лише через браузер, **Continue without microphone** через автоматизацію браузера й продовжити очікувати згенерований URL Meet. Якщо це неможливо, у помилці має згадуватися `meet-audio-choice-required`, а не `google-login-required`.


### Агент приєднується, але не говорить

Перевірте шлях реального часу:

bashCopy code
[code]
    openclaw googlemeet setupopenclaw googlemeet doctor
[/code]

Використовуйте `mode: "agent"` для звичайного шляху відповіді голосом STT -> агент OpenClaw -> TTS, або `mode: "bidi"` для прямого резервного голосу в реальному часі. `mode: "transcribe"` навмисно не запускає міст відповіді голосом. Для налагодження лише спостереження виконайте `openclaw googlemeet status --json <session-id>` після того, як учасники заговорять, і перевірте `captioning`, `transcriptLines` і `lastCaptionText`. Якщо `inCall` дорівнює true, але `transcriptLines` залишається `0`, субтитри Meet можуть бути вимкнені, ніхто не говорив після встановлення спостерігача, інтерфейс Meet змінився або live-субтитри недоступні для мови/облікового запису зустрічі.

`googlemeet test-speech` завжди перевіряє шлях реального часу й повідомляє, чи було помічено байти виходу мосту для цього виклику. Якщо `speechOutputVerified` дорівнює false і `speechOutputTimedOut` дорівнює true, провайдер реального часу міг прийняти висловлювання, але OpenClaw не побачив, щоб нові вихідні байти дійшли до аудіомосту Chrome.

Також перевірте:

  * Ключ провайдера реального часу доступний на хості Gateway, наприклад `OPENAI_API_KEY` або `GEMINI_API_KEY`.
  * `BlackHole 2ch` видимий на хості Chrome.
  * `sox` існує на хості Chrome.
  * Мікрофон і динамік Meet маршрутизовано через віртуальний аудіошлях, який використовує OpenClaw. `doctor` має показувати `meet output routed: yes` для локальних приєднань Chrome у реальному часі.


`googlemeet doctor [session-id]` друкує сесію, вузол, стан у виклику, причину ручної дії, підключення провайдера реального часу, `realtimeReady`, активність аудіовходу/аудіовиходу, останні часові мітки аудіо, лічильники байтів і URL браузера. Використовуйте `googlemeet status [session-id] --json`, коли потрібен сирий JSON. Використовуйте `googlemeet doctor --oauth`, коли потрібно перевірити оновлення Google Meet OAuth без розкриття токенів; додайте `--meeting` або `--create-space`, коли також потрібне підтвердження Google Meet API.

Якщо час очікування агента сплив і ви бачите вже відкриту вкладку Meet, огляньте цю вкладку без відкриття іншої:

bashCopy code
[code]
    openclaw googlemeet recover-tabopenclaw googlemeet recover-tab https://meet.google.com/abc-defg-hij
[/code]

Відповідна дія інструмента — `recover_current_tab`. Вона фокусує та оглядає наявну вкладку Meet для вибраного транспорту. З `chrome` вона використовує локальне керування браузером через Gateway; з `chrome-node` вона використовує налаштований вузол Chrome. Вона не відкриває нову вкладку й не створює нову сесію; вона повідомляє поточний блокер, наприклад вхід, допуск, дозволи або стан вибору аудіо. Команда CLI звертається до налаштованого Gateway, тому Gateway має бути запущений; `chrome-node` також потребує підключеного вузла Chrome.

### Перевірки налаштування Twilio не проходять

`twilio-voice-call-plugin` не проходить, коли `voice-call` не дозволено або не ввімкнено. Додайте його до `plugins.allow`, увімкніть `plugins.entries.voice-call` і перезавантажте Gateway.

`twilio-voice-call-credentials` не проходить, коли backend Twilio не має account SID, auth token або номера абонента. Установіть їх на хості Gateway:

bashCopy code
[code]
    export TWILIO_ACCOUNT_SID=AC...export TWILIO_AUTH_TOKEN=...export TWILIO_FROM_NUMBER=+15550001234
[/code]

`twilio-voice-call-webhook` не проходить, коли `voice-call` не має публічного Webhook доступу або коли `publicUrl` вказує на loopback чи простір приватної мережі. Установіть `plugins.entries.voice-call.config.publicUrl` на URL публічного провайдера або налаштуйте тунель/експозицію Tailscale для `voice-call`.

Loopback і приватні URL недійсні для callback операторів зв’язку. Не використовуйте `localhost`, `127.0.0.1`, `0.0.0.0`, `10.x`, `172.16.x`-`172.31.x`, `192.168.x`, `169.254.x`, `fc00::/7` або `fd00::/8` як `publicUrl`.

Для стабільного публічного URL:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          provider: "twilio",          fromNumber: "+15550001234",          publicUrl: "https://voice.example.com/voice/webhook",        },      },    },  },}
[/code]

Для локальної розробки використовуйте тунель або доступ через Tailscale замість приватної URL-адреси хоста:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          tunnel: { provider: "ngrok" },          // or          tailscale: { mode: "funnel", path: "/voice/webhook" },        },      },    },  },}
[/code]

Потім перезапустіть або перезавантажте Gateway і виконайте:

bashCopy code
[code]
    openclaw googlemeet setup --transport twilioopenclaw voicecall setupopenclaw voicecall smoke
[/code]

`voicecall smoke` за замовчуванням лише перевіряє готовність. Щоб виконати пробний запуск для конкретного номера:

bashCopy code
[code]
    openclaw voicecall smoke --to "+15555550123"
[/code]

Додавайте `--yes` лише тоді, коли ви навмисно хочете здійснити живий вихідний сповіщувальний виклик:

bashCopy code
[code]
    openclaw voicecall smoke --to "+15555550123" --yes
[/code]

### Виклик Twilio починається, але ніколи не входить у зустріч

Підтвердьте, що подія Meet містить дані телефонного дозвону. Передайте точний номер дозвону та PIN або власну послідовність DTMF:

bashCopy code
[code]
    openclaw googlemeet join https://meet.google.com/abc-defg-hij \  --transport twilio \  --dial-in-number +15551234567 \  --dtmf-sequence ww123456#
[/code]

Використовуйте початкові `w` або коми в `--dtmf-sequence`, якщо провайдеру потрібна пауза перед введенням PIN.

Якщо телефонний виклик створено, але в списку учасників Meet так і не з’являється учасник, що приєднався телефоном:

  * Виконайте `openclaw googlemeet doctor <session-id>`, щоб підтвердити делегований ID виклику Twilio, чи було поставлено DTMF у чергу та чи було запитано вступне привітання.
  * Виконайте `openclaw voicecall status --call-id <id>` і підтвердьте, що виклик усе ще активний.
  * Виконайте `openclaw voicecall tail` і перевірте, що Webhook-и Twilio надходять до Gateway.
  * Виконайте `openclaw logs --follow` і знайдіть послідовність Twilio Meet: Google Meet делегує приєднання, Voice Call зберігає й обслуговує DTMF TwiML до з’єднання, Voice Call обслуговує realtime TwiML для виклику Twilio, а потім Google Meet запитує вступне мовлення через `voicecall.speak`.
  * Повторно виконайте `openclaw googlemeet setup --transport twilio`; успішна перевірка налаштування потрібна, але вона не доводить, що послідовність PIN для зустрічі правильна.
  * Підтвердьте, що номер дозвону належить до того самого запрошення Meet і регіону, що й PIN.
  * Збільште `voiceCall.dtmfDelayMs` від стандартних 12 секунд, якщо Meet відповідає повільно або транскрипт виклику все ще містить запит на введення PIN після надсилання DTMF до з’єднання.
  * Якщо учасник приєднується, але ви не чуєте привітання, перевірте `openclaw logs --follow` на наявність запиту `voicecall.speak` після DTMF і відтворення TTS через медіапотік або резервний варіант Twilio `OPENCLAW_DOCS_MARKER:calloutOpen:U2F5`. Якщо транскрипт виклику все ще містить "enter the meeting PIN", телефонна гілка ще не приєдналася до кімнати Meet, тому учасники зустрічі не почують мовлення.


Якщо Webhook-и не надходять, спочатку налагодьте Plugin Voice Call: провайдер має досягати `plugins.entries.voice-call.config.publicUrl` або налаштованого тунелю. Див. [Усунення несправностей голосового виклику](</uk/plugins/voice-call#troubleshooting>).

## Примітки

Офіційний медіа-API Google Meet орієнтований на отримання, тому для мовлення в дзвінку Meet усе ще потрібен шлях учасника. Цей Plugin залишає цю межу видимою: Chrome обробляє участь через браузер і локальну маршрутизацію аудіо; Twilio обробляє участь через телефонний дозвін.

Режими зворотного мовлення Chrome потребують `BlackHole 2ch` і одного з таких варіантів:

  * `chrome.audioInputCommand` плюс `chrome.audioOutputCommand`: OpenClaw володіє мостом і передає аудіо у форматі `chrome.audioFormat` між цими командами та вибраним провайдером. Режим агента використовує realtime-транскрипцію плюс звичайний TTS; bidi-режим використовує realtime голосового провайдера. Стандартний шлях Chrome - 24 кГц PCM16 із `chrome.audioBufferBytes: 4096`; 8 кГц G.711 mu-law залишається доступним для застарілих пар команд.
  * `chrome.audioBridgeCommand`: зовнішня команда моста володіє всім локальним аудіошляхом і має завершитися після запуску або перевірки свого демона. Це допустимо лише для `bidi`, тому що режиму `agent` потрібен прямий доступ до пари команд для TTS.


Коли агент викликає інструмент `google_meet` у режимі агента, сесія консультанта зустрічі розгалужує поточний транскрипт викликача перед відповіддю на мовлення учасника. Сесія Meet усе одно залишається окремою (`agent:<agentId>:subagent:google-meet:<sessionId>`), тож подальші дії в зустрічі не змінюють транскрипт викликача напряму.

Для чистого дуплексного аудіо маршрутизуйте вихід Meet і мікрофон Meet через окремі віртуальні пристрої або граф віртуальних пристроїв у стилі Loopback. Один спільний пристрій BlackHole може відлунювати інших учасників назад у виклик.

З командною парою моста Chrome `chrome.bargeInInputCommand` може слухати окремий локальний мікрофон і очищати відтворення асистента, коли людина починає говорити. Це залишає людське мовлення попереду виводу асистента, навіть коли спільний вхід local loopback BlackHole тимчасово приглушено під час відтворення асистента. Як і `chrome.audioInputCommand` та `chrome.audioOutputCommand`, це локальна команда, налаштована оператором. Використовуйте явний довірений шлях команди або список аргументів і не спрямовуйте її на скрипти з недовірених розташувань.

`googlemeet speak` запускає активний аудіоміст зворотного мовлення для сесії Chrome. `googlemeet leave` зупиняє цей міст. Для сесій Twilio, делегованих через Plugin Voice Call, `leave` також завершує базовий голосовий виклик. Використовуйте `googlemeet end-active-conference`, коли також хочете закрити активну конференцію Google Meet для простору, керованого API.

## Пов’язане

  * [Plugin голосового виклику](</uk/plugins/voice-call>)
  * [Режим розмови](</uk/nodes/talk>)
  * [Створення plugins](</uk/plugins/building-plugins>)


Was this useful?YesNo