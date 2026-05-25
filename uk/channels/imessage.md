---
title: iMessage
source_url: https://docs.openclaw.ai/uk/channels/imessage
scraped_at: 2026-05-25
---

Стан: нативна інтеграція із зовнішнім CLI. Gateway запускає `imsg rpc` і взаємодіє через JSON-RPC у stdio (без окремого демона/порту). Розширені дії потребують `imsg launch` і успішної перевірки приватного API.

**Дії приватного API** Відповіді, tapback-реакції, ефекти, вкладення та керування групами. [**Сполучення** Особисті повідомлення iMessage типово використовують режим сполучення. ](</uk/channels/pairing>) **Віддалений Mac** Використовуйте SSH-обгортку, коли Gateway не запущено на Mac із Messages. [**Довідник конфігурації** Повний довідник полів iMessage. ](</uk/gateway/config-channels#imessage>)

## Швидке налаштування

### Локальний Mac (швидкий шлях)

* ### Установіть і перевірте imsg

bashCopy code
[code]
    brew install steipete/tap/imsgimsg rpc --helpimsg launchopenclaw channels status --probe
[/code]

* ### Налаштуйте OpenClaw

json5Copy code
[code]
    {channels: {imessage: {enabled: true,cliPath: "/usr/local/bin/imsg",dbPath: "/Users/user/Library/Messages/chat.db",},},}
[/code]

* ### Запустіть gateway

bashCopy code
[code]
    openclaw gateway
[/code]

* ### Підтвердьте перше сполучення DM (типовий dmPolicy)

bashCopy code
[code]
    openclaw pairing list imessageopenclaw pairing approve imessage &lt;CODE&gt;
[/code]

Запити на сполучення спливають через 1 годину.

### Віддалений Mac через SSH

OpenClaw потребує лише сумісного зі stdio `cliPath`, тож можна вказати `cliPath` на скрипт-обгортку, який підключається SSH до віддаленого Mac і запускає `imsg`.

bashCopy code
[code]
    #!/usr/bin/env bashexec ssh -T gateway-host imsg "$@"
[/code]

Рекомендована конфігурація, коли вкладення ввімкнено:

json5Copy code
[code]
    {channels: {imessage: {  enabled: true,  cliPath: "~/.openclaw/scripts/imsg-ssh",  remoteHost: "user@gateway-host", // used for SCP attachment fetches  includeAttachments: true,  // Optional: override allowed attachment roots.  // Defaults include /Users/*/Library/Messages/Attachments  attachmentRoots: ["/Users/*/Library/Messages/Attachments"],  remoteAttachmentRoots: ["/Users/*/Library/Messages/Attachments"],},},}
[/code]

Якщо `remoteHost` не задано, OpenClaw намагається автоматично визначити його, розбираючи SSH-скрипт-обгортку. `remoteHost` має бути `host` або `user@host` (без пробілів чи SSH-параметрів). OpenClaw використовує сувору перевірку ключа хоста для SCP, тому ключ хоста ретранслятора вже має існувати в `~/.ssh/known_hosts`. Шляхи вкладень перевіряються відносно дозволених коренів (`attachmentRoots` / `remoteAttachmentRoots`).

## Вимоги та дозволи (macOS)

  * На Mac, де запускається `imsg`, має бути виконано вхід у Messages.
  * Для контексту процесу, що запускає OpenClaw/`imsg`, потрібен повний доступ до диска (доступ до БД Messages).
  * Для надсилання повідомлень через Messages.app потрібен дозвіл на автоматизацію.
  * Для розширених дій (реакція / редагування / скасування надсилання / відповідь у треді / ефекти / групові операції) потрібно вимкнути System Integrity Protection — див. Увімкнення приватного API imsg нижче. Базове надсилання й отримання тексту та медіа працює без цього.


## Увімкнення приватного API imsg

`imsg` постачається у двох робочих режимах:

  * **Базовий режим** (типовий, зміни SIP не потрібні): вихідні текст і медіа через `send`, вхідне спостереження/історія, список чатів. Це те, що ви отримуєте одразу після свіжого `brew install steipete/tap/imsg` плюс стандартні дозволи macOS, наведені вище.
  * **Режим приватного API** : `imsg` інжектує допоміжну dylib у `Messages.app`, щоб викликати внутрішні функції `IMCore`. Саме це розблоковує `react`, `edit`, `unsend`, `reply` (у треді), `sendWithEffect`, `renameGroup`, `setGroupIcon`, `addParticipant`, `removeParticipant`, `leaveGroup`, а також індикатори введення та сповіщення про прочитання.


Щоб отримати поверхню розширених дій, описану на цій сторінці каналу, потрібен режим приватного API. README `imsg` прямо вказує на цю вимогу:

> Розширені можливості, як-от `read`, `typing`, `launch`, розширене надсилання через міст, зміна повідомлень і керування чатами, вмикаються явно. Вони потребують вимкненого SIP і допоміжної dylib, інжектованої в `Messages.app`. `imsg launch` відмовляється виконувати інжекцію, коли SIP увімкнено.

Техніка інжекції helper використовує власну dylib `imsg`, щоб отримати доступ до приватних API Messages. У шляху OpenClaw iMessage немає стороннього сервера чи середовища виконання BlueBubbles.

### Налаштування

  1. **Установіть (або оновіть)`imsg`** на Mac, де працює Messages.app:

bashCopy code
[code]brew install steipete/tap/imsgimsg --versionimsg status --json
[/code]

Вивід `imsg status --json` повідомляє `bridge_version`, `rpc_methods` і `selectors` для кожного методу, щоб ви могли побачити, що підтримує поточна збірка, перш ніж почати.

  2. **Вимкніть System Integrity Protection.** Це залежить від версії macOS, бо базова вимога Apple залежить від ОС і обладнання:

     * **macOS 10.13–10.15 (Sierra–Catalina):** вимкніть Library Validation через Terminal, перезавантажтеся в Recovery Mode, виконайте `csrutil disable`, перезапустіть.
     * **macOS 11+ (Big Sur і новіші), Intel:** Recovery Mode (або Internet Recovery), `csrutil disable`, перезапустіть.
     * **macOS 11+, Apple Silicon:** послідовність запуску з кнопкою живлення для входу в Recovery; у новіших версіях macOS утримуйте клавішу **Left Shift** , коли натискаєте Continue, потім `csrutil disable`. Налаштування віртуальних машин мають окремий процес — спочатку зробіть знімок VM.
     * **macOS 26 / Tahoe:** політики library-validation і перевірки приватних entitlement для `imagent` стали ще суворішими; `imsg` може потребувати оновленої збірки, щоб не відставати. Якщо інжекція `imsg launch` або конкретні `selectors` починають повертати false після великого оновлення macOS, перевірте примітки до випуску `imsg`, перш ніж вважати, що крок SIP успішно виконано.

Дотримуйтеся процесу Apple Recovery-mode для вашого Mac, щоб вимкнути SIP перед запуском `imsg launch`.

  3. **Інжектуйте helper.** Коли SIP вимкнено і в Messages.app виконано вхід:

bashCopy code
[code]imsg launch
[/code]

`imsg launch` відмовляється виконувати інжекцію, коли SIP досі увімкнено, тож це також слугує підтвердженням, що крок 2 спрацював.

  4. **Перевірте міст з OpenClaw:**

bashCopy code
[code]openclaw channels status --probe
[/code]

Запис iMessage має повідомляти `works`, а `imsg status --json | jq '.selectors'` має показувати `retractMessagePart: true` плюс ті селектори редагування / введення / прочитання, які надає ваша збірка macOS. Поштучне gating методів у Plugin OpenClaw в `actions.ts` рекламує лише дії, базовий селектор яких дорівнює `true`, тож поверхня дій, яку ви бачите в списку інструментів агента, відображає те, що міст реально може виконати на цьому хості.


Якщо `openclaw channels status --probe` повідомляє, що канал має стан `works`, але конкретні дії під час dispatch викидають "iMessage `<action>` requires the imsg private API bridge", запустіть `imsg launch` ще раз — helper може зникнути (перезапуск Messages.app, оновлення ОС тощо), а кешований статус `available: true` продовжуватиме рекламувати дії до наступного оновлення probe.

### Коли ви не можете вимкнути SIP

Якщо вимкнений SIP неприйнятний для вашої моделі загроз:

  * `imsg` повертається до базового режиму — лише текст + медіа + отримання.
  * Plugin OpenClaw усе ще рекламує надсилання тексту/медіа та моніторинг вхідних повідомлень; він просто приховує `react`, `edit`, `unsend`, `reply`, `sendWithEffect` і групові операції з поверхні дій (відповідно до gate можливостей для кожного методу).
  * Ви можете запустити окремий Mac без Apple Silicon (або виділений bot Mac) з вимкненим SIP для навантаження iMessage, залишивши SIP увімкненим на основних пристроях. Див. Виділений користувач macOS для бота (окрема ідентичність iMessage) нижче.


## Контроль доступу та маршрутизація

### Політика DM

`channels.imessage.dmPolicy` керує особистими повідомленнями:

  * `pairing` (типово)
  * `allowlist`
  * `open` (потребує, щоб `allowFrom` містив `"*"`)
  * `disabled`


Поле списку дозволених: `channels.imessage.allowFrom`.

Записи списку дозволених мають ідентифікувати відправників: handles або статичні групи доступу відправників (`accessGroup:<name>`). Використовуйте `channels.imessage.groupAllowFrom` для цілей чату, як-от `chat_id:*`, `chat_guid:*` або `chat_identifier:*`; використовуйте `channels.imessage.groups` для числових ключів реєстру `chat_id`.

### Групова політика + згадки

`channels.imessage.groupPolicy` керує обробкою груп:

  * `allowlist` (типово, коли налаштовано)
  * `open`
  * `disabled`


Список дозволених відправників групи: `channels.imessage.groupAllowFrom`.

Записи `groupAllowFrom` також можуть посилатися на статичні групи доступу відправників (`accessGroup:<name>`).

Резервний варіант під час виконання: якщо `groupAllowFrom` не задано, перевірки відправників груп iMessage використовують `allowFrom`; задайте `groupAllowFrom`, коли правила допуску для DM і груп мають відрізнятися. Примітка щодо виконання: якщо `channels.imessage` повністю відсутній, runtime повертається до `groupPolicy="allowlist"` і записує попередження в журнал (навіть якщо `channels.defaults.groupPolicy` задано).

Обмеження згадками для груп:

  * iMessage не має власних метаданих згадок
  * виявлення згадок використовує regex-шаблони (`agents.list[].groupChat.mentionPatterns`, резервний варіант `messages.groupChat.mentionPatterns`)
  * без налаштованих шаблонів обмеження згадками неможливо примусово застосувати


Керівні команди від авторизованих відправників можуть обходити обмеження згадками в групах.

`systemPrompt` для окремої групи:

Кожен запис у `channels.imessage.groups.*` приймає необов’язковий рядок `systemPrompt`. Значення вставляється в системний промпт агента на кожному ході, який обробляє повідомлення в цій групі. Визначення повторює визначення промпта для окремої групи, яке використовує `channels.whatsapp.groups`:

  1. **Системний промпт конкретної групи** (`groups["<chat_id>"].systemPrompt`): використовується, коли конкретний запис групи існує в мапі **і** його ключ `systemPrompt` визначено. Якщо `systemPrompt` є порожнім рядком (`""`), wildcard пригнічується, і до цієї групи не застосовується жоден системний промпт.
  2. **Wildcard системного промпта групи** (`groups["*"].systemPrompt`): використовується, коли конкретного запису групи взагалі немає в мапі або коли він існує, але не визначає ключ `systemPrompt`.

json5Copy code
[code]
    {  channels: {    imessage: {      groupPolicy: "allowlist",      groupAllowFrom: ["+15555550123"],      groups: {        "*": { systemPrompt: "Use British spelling." },        "8421": {          requireMention: true,          systemPrompt: "This is the on-call rotation chat. Keep replies under 3 sentences.",        },        "9907": {          // explicit suppression: the wildcard "Use British spelling." does not apply here          systemPrompt: "",        },      },    },  },}
[/code]

Промпти для окремих груп застосовуються лише до групових повідомлень — прямі повідомлення в цьому каналі не змінюються.

### Сесії та детерміновані відповіді

  * DM використовують пряме маршрутизування; групи використовують групове маршрутизування.
  * Із типовим `session.dmScope=main` DM iMessage згортаються в основну сесію агента.
  * Групові сесії ізольовані (`agent:<agentId>:imessage:group:<chat_id>`).
  * Відповіді маршрутизуються назад до iMessage за допомогою метаданих початкового каналу/цілі.


Поведінка потоків, схожих на групові:

Деякі потоки iMessage з кількома учасниками можуть надходити з `is_group=false`. Якщо цей `chat_id` явно налаштовано в `channels.imessage.groups`, OpenClaw обробляє його як груповий трафік (групові обмеження + ізоляція групової сесії).

## Прив’язки розмов ACP

Застарілі чати iMessage також можна прив’язувати до сесій ACP.

Швидкий операторський процес:

  * Запустіть `/acp spawn codex --bind here` у DM або дозволеному груповому чаті.
  * Майбутні повідомлення в тій самій розмові iMessage маршрутизуватимуться до створеної сесії ACP.
  * `/new` і `/reset` скидають ту саму прив’язану сесію ACP на місці.
  * `/acp close` закриває сесію ACP і видаляє прив’язку.


Налаштовані постійні прив’язки підтримуються через записи верхнього рівня `bindings[]` з `type: "acp"` і `match.channel: "imessage"`.

`match.peer.id` може використовувати:

  * нормалізований ідентифікатор DM, наприклад `+15555550123` або `user@example.com`
  * `chat_id:<id>` (рекомендовано для стабільних групових прив’язок)
  * `chat_guid:<guid>`
  * `chat_identifier:<identifier>`


Приклад:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "codex",        runtime: {          type: "acp",          acp: { agent: "codex", backend: "acpx", mode: "persistent" },        },      },    ],  },  bindings: [    {      type: "acp",      agentId: "codex",      match: {        channel: "imessage",        accountId: "default",        peer: { kind: "group", id: "chat_id:123" },      },      acp: { label: "codex-group" },    },  ],}
[/code]

Див. [Агенти ACP](</uk/tools/acp-agents>) щодо спільної поведінки прив’язок ACP.

## Шаблони розгортання

Виділений користувач macOS для бота (окрема ідентичність iMessage)

Використовуйте виділений Apple ID і користувача macOS, щоб трафік бота був ізольований від вашого особистого профілю Messages.

Типовий процес:

  1. Створіть/увійдіть у виділеного користувача macOS.
  2. Увійдіть у Messages з Apple ID бота в цьому користувачі.
  3. Установіть `imsg` у цьому користувачі.
  4. Створіть SSH-обгортку, щоб OpenClaw міг запускати `imsg` у контексті цього користувача.
  5. Спрямуйте `channels.imessage.accounts.<id>.cliPath` і `.dbPath` на профіль цього користувача.


Перший запуск може вимагати схвалень у GUI (Automation + Full Disk Access) у сесії цього користувача бота.

Віддалений Mac через Tailscale (приклад)

Поширена топологія:

  * gateway працює на Linux/VM
  * iMessage + `imsg` працює на Mac у вашій tailnet
  * обгортка `cliPath` використовує SSH для запуску `imsg`
  * `remoteHost` вмикає отримання вкладень через SCP


Приклад:

json5Copy code
[code]
    {  channels: {    imessage: {      enabled: true,      cliPath: "~/.openclaw/scripts/imsg-ssh",      remoteHost: "bot@mac-mini.tailnet-1234.ts.net",      includeAttachments: true,      dbPath: "/Users/bot/Library/Messages/chat.db",    },  },}
[/code]

bashCopy code
[code]
    #!/usr/bin/env bashexec ssh -T bot@mac-mini.tailnet-1234.ts.net imsg "$@"
[/code]

Використовуйте SSH-ключі, щоб і SSH, і SCP були неінтерактивними. Спочатку переконайтеся, що ключ хоста довірений (наприклад, `ssh bot@mac-mini.tailnet-1234.ts.net`), щоб `known_hosts` було заповнено.

Шаблон з кількома обліковими записами

iMessage підтримує налаштування для окремих облікових записів у `channels.imessage.accounts`.

Кожен обліковий запис може перевизначати поля, як-от `cliPath`, `dbPath`, `allowFrom`, `groupPolicy`, `mediaMaxMb`, налаштування історії та allowlist коренів вкладень.

## Медіа, розбиття на частини та цілі доставлення

Вкладення та медіа

  * приймання вхідних вкладень **вимкнене за замовчуванням** — задайте `channels.imessage.includeAttachments: true`, щоб пересилати фото, голосові нотатки, відео та інші вкладення агенту. Коли це вимкнено, iMessage лише з вкладеннями відкидаються до потрапляння до агента й можуть узагалі не створювати рядок журналу `Inbound message`.
  * віддалені шляхи вкладень можна отримувати через SCP, коли встановлено `remoteHost`
  * шляхи вкладень мають відповідати дозволеним кореням: 
    * `channels.imessage.attachmentRoots` (локально)
    * `channels.imessage.remoteAttachmentRoots` (режим віддаленого SCP)
    * типовий шаблон кореня: `/Users/*/Library/Messages/Attachments`
  * SCP використовує сувору перевірку ключа хоста (`StrictHostKeyChecking=yes`)
  * розмір вихідних медіа використовує `channels.imessage.mediaMaxMb` (типово 16 MB)

Розбиття вихідних повідомлень на частини

  * ліміт частини тексту: `channels.imessage.textChunkLimit` (типово 4000)
  * режим розбиття: `channels.imessage.chunkMode`
    * `length` (типово)
    * `newline` (розділення спочатку за абзацами)

Формати адресування

Бажані явні цілі:

  * `chat_id:123` (рекомендовано для стабільного маршрутизування)
  * `chat_guid:...`
  * `chat_identifier:...`


Цілі-ідентифікатори також підтримуються:

  * `imessage:+1555...`
  * `sms:+1555...`
  * `user@example.com`

bashCopy code
[code]
    imsg chats --limit 20
[/code]

## Дії Private API

Коли `imsg launch` запущено, а `openclaw channels status --probe` повідомляє `privateApi.available: true`, інструмент повідомлень може використовувати нативні для iMessage дії на додачу до звичайного надсилання тексту.

json5Copy code
[code]
    {  channels: {    imessage: {      actions: {        reactions: true,        edit: true,        unsend: true,        reply: true,        sendWithEffect: true,        sendAttachment: true,        renameGroup: true,        setGroupIcon: true,        addParticipant: true,        removeParticipant: true,        leaveGroup: true,      },    },  },}
[/code]

Доступні дії

  * **react** : додати/видалити tapback iMessage (`messageId`, `emoji`, `remove`). Підтримувані tapback відповідають love, like, dislike, laugh, emphasize і question.
  * **reply** : надіслати відповідь у потоці на наявне повідомлення (`messageId`, `text` або `message`, плюс `chatGuid`, `chatId`, `chatIdentifier` або `to`).
  * **sendWithEffect** : надіслати текст з ефектом iMessage (`text` або `message`, `effect` або `effectId`).
  * **edit** : редагувати надіслане повідомлення на підтримуваних версіях macOS/Private API (`messageId`, `text` або `newText`).
  * **unsend** : відкликати надіслане повідомлення на підтримуваних версіях macOS/Private API (`messageId`).
  * **upload-file** : надіслати медіа/файли (`buffer` як base64 або гідратований `media`/`path`/`filePath`, `filename`, необов’язково `asVoice`). Застарілий псевдонім: `sendAttachment`.
  * **renameGroup** , **setGroupIcon** , **addParticipant** , **removeParticipant** , **leaveGroup** : керувати груповими чатами, коли поточна ціль є груповою розмовою.

ID повідомлень

Контекст вхідного iMessage містить і короткі значення `MessageSid`, і повні GUID повідомлень, коли вони доступні. Короткі ID обмежені нещодавнім кешем відповідей у пам’яті та перевіряються щодо поточного чату перед використанням. Якщо короткий ID застарів або належить іншому чату, повторіть спробу з повним `MessageSidFull`.

Виявлення можливостей

OpenClaw приховує дії Private API лише тоді, коли кешований стан перевірки вказує, що міст недоступний. Якщо стан невідомий, дії залишаються видимими, а dispatch запускає перевірки ліниво, щоб перша дія могла успішно виконатися після `imsg launch` без окремого ручного оновлення стану.

Сповіщення про прочитання та індикатор набору

Коли міст Private API працює, прийняті вхідні чати позначаються прочитаними перед dispatch, а відправнику показується індикатор набору, поки агент генерує відповідь. Вимкніть позначення прочитання за допомогою:

json5Copy code
[code]
    {  channels: {    imessage: {      sendReadReceipts: false,    },  },}
[/code]

Старіші збірки `imsg`, які передують списку можливостей для окремих методів, тихо вимикатимуть індикатор набору/прочитання; OpenClaw записує одноразове попередження за перезапуск, щоб відсутність підтвердження прочитання можна було пояснити.

Вхідні tapback

OpenClaw підписується на tapback iMessage і маршрутизує прийняті реакції як системні події замість звичайного тексту повідомлення, тому tapback користувача не запускає звичайний цикл відповідей.

Режим сповіщень контролюється `channels.imessage.reactionNotifications`:

  * `"own"` (типово): сповіщати лише коли користувачі реагують на повідомлення, створені ботом.
  * `"all"`: сповіщати про всі вхідні tapback від авторизованих відправників.
  * `"off"`: ігнорувати вхідні tapback.


Перевизначення для окремих облікових записів використовують `channels.imessage.accounts.<id>.reactionNotifications`.

## Записи конфігурації

iMessage за замовчуванням дозволяє ініційовані каналом записи конфігурації (для `/config set|unset`, коли `commands.config: true`).

Вимкнути:

json5Copy code
[code]
    {  channels: {    imessage: {      configWrites: false,    },  },}
[/code]

## Об’єднання розділених DM (команда + URL в одній композиції)

Коли користувач вводить команду й URL разом — наприклад, `Dump https://example.com/article` — застосунок Messages від Apple розділяє надсилання на **два окремі рядки`chat.db`**:

  1. Текстове повідомлення (`"Dump"`).
  2. Кулька попереднього перегляду URL (`"https://..."`) із зображеннями OG-preview як вкладеннями.


Два рядки надходять до OpenClaw з інтервалом приблизно 0,8-2,0 с у більшості налаштувань. Без об’єднання агент отримує саму команду на кроці 1, відповідає (часто «надішліть мені URL») і бачить URL лише на кроці 2 — коли контекст команди вже втрачено. Це конвеєр надсилання Apple, а не щось, що додають OpenClaw або `imsg`.

`channels.imessage.coalesceSameSenderDms` вмикає для DM об’єднання послідовних рядків від того самого відправника в один крок агента. Групові чати й далі надсилаються повідомлення за повідомленням, щоб зберегти структуру кроків із кількома користувачами.

### When to enable

Увімкніть, коли:

  * Ви постачаєте Skills, які очікують `command + payload` в одному повідомленні (dump, paste, save, queue тощо).
  * Ваші користувачі вставляють URL, зображення або довгий вміст разом із командами.
  * Ви можете прийняти додану затримку кроку DM (див. нижче).


Залиште вимкненим, коли:

  * Вам потрібна мінімальна затримка команди для однословних тригерів DM.
  * Усі ваші потоки — це одноразові команди без подальших payload.


### Enabling

json5Copy code
[code]
    {  channels: {    imessage: {      coalesceSameSenderDms: true, // opt in (default: false)    },  },}
[/code]

Коли прапорець увімкнено і немає явного `messages.inbound.byChannel.imessage`, вікно debounce розширюється до **2500 мс** (застаріле значення за замовчуванням — 0 мс, тобто без debouncing). Ширше вікно потрібне, бо ритм розділеного надсилання Apple у 0,8-2,0 с не вкладається в тісніше значення за замовчуванням.

Щоб налаштувати вікно самостійно:

json5Copy code
[code]
    {  messages: {    inbound: {      byChannel: {        // 2500 ms works for most setups; raise to 4000 ms if your Mac is        // slow or under memory pressure (observed gap can stretch past 2 s        // then).        imessage: 2500,      },    },  },}
[/code]

### Trade-offs

  * **Додана затримка для повідомлень DM.** Коли прапорець увімкнено, кожне DM (включно з окремими керівними командами й одиничними текстовими продовженнями) очікує до завершення вікна debounce перед надсиланням, на випадок якщо надходить рядок payload. Повідомлення групових чатів зберігають миттєве надсилання.
  * **Об’єднаний вивід має межі.** Об’єднаний текст обмежується 4000 символами з явним маркером `…[truncated]`; вкладення обмежені 20; записи джерел — 10 (після цього зберігаються перший і найновіші). Кожен GUID джерела відстежується в `coalescedMessageGuids` для подальшої телеметрії.
  * **Лише DM.** Групові чати проходять до надсилання повідомлення за повідомленням, щоб бот залишався чутливим, коли кілька людей друкують одночасно.
  * **Опційно, для окремого каналу.** Інші канали (Telegram, WhatsApp, Slack, …) не зачіпаються. Застарілі конфігурації BlueBubbles, які встановлюють `channels.bluebubbles.coalesceSameSenderDms`, мають перенести це значення до `channels.imessage.coalesceSameSenderDms`.


### Сценарії та що бачить агент

Користувач створює | `chat.db` створює | Прапорець вимкнено (за замовчуванням) | Прапорець увімкнено + вікно 2500 мс  
---|---|---|---  
`Dump https://example.com` (одне надсилання) | 2 рядки з інтервалом ~1 с | Два кроки агента: лише "Dump", потім URL | Один крок: об’єднаний текст `Dump https://example.com`  
`Save this 📎image.jpg caption` (вкладення + текст) | 2 рядки | Два кроки (вкладення скинуто під час об’єднання) | Один крок: текст + зображення збережено  
`/status` (окрема команда) | 1 рядок | Миттєве надсилання | **Очікування до завершення вікна, потім надсилання**  
URL вставлено окремо | 1 рядок | Миттєве надсилання | Миттєве надсилання (лише один запис у bucket)  
Текст + URL надіслано як два навмисно окремі повідомлення з різницею в хвилини | 2 рядки поза вікном | Два кроки | Два кроки (вікно спливає між ними)  
Швидкий потік (>10 малих DM у межах вікна) | N рядків | N кроків | Один крок, обмежений вивід (перший + найновіші, застосовано обмеження тексту/вкладень)  
Двоє людей друкують у груповому чаті | N рядків від M відправників | M+ кроків (по одному на bucket відправника) | M+ кроків — групові чати не об’єднуються  
  
## Надолуження після простою Gateway

Коли Gateway офлайн (збій, перезапуск, сон Mac, вимкнена машина), `imsg watch` після повернення Gateway відновлюється з поточного стану `chat.db` — усе, що надійшло під час прогалини, за замовчуванням ніколи не буде побачено. Catchup відтворює ці повідомлення під час наступного запуску, щоб агент не пропускав вхідний трафік мовчки.

Catchup **вимкнено за замовчуванням**. Увімкніть його для окремого каналу:

tsCopy code
[code]
    channels: {  imessage: {    catchup: {      enabled: true,             // master switch (default: false)      maxAgeMinutes: 120,        // skip rows older than now - 2h (default: 120, clamp 1..720)      perRunLimit: 50,           // max rows replayed per startup (default: 50, clamp 1..500)      firstRunLookbackMinutes: 30, // first run with no cursor: look back 30 min (default: 30)      maxFailureRetries: 10,     // give up on a wedged guid after 10 dispatch failures (default: 10)    },  },}
[/code]

### Як це виконується

Один прохід на кожен запуск `monitorIMessageProvider`, послідовність така: готовність `imsg launch` → `watch.subscribe` → `performIMessageCatchup` → цикл live-надсилання. Сам Catchup використовує `chats.list` \+ `messages.history` для кожного чату через той самий JSON-RPC-клієнт, який використовує `imsg watch`. Усе, що надходить під час проходу Catchup, проходить через live-надсилання у звичайному режимі; наявний кеш inbound-dedupe поглинає будь-яке перекриття з відтвореними рядками.

Кожен відтворений рядок подається через live-шлях надсилання (`evaluateIMessageInbound` \+ `dispatchInboundMessage`), тож allowlist, політика груп, debouncer, echo cache і сповіщення про прочитання поводяться однаково для відтворених і live-повідомлень.

### Семантика курсора й повторів

Catchup зберігає курсор для кожного облікового запису в `<openclawStateDir>/imessage/catchup/<account>__<hash>.json` (каталог стану OpenClaw за замовчуванням — `~/.openclaw`, можна перевизначити через `OPENCLAW_STATE_DIR`):

jsonCopy code
[code]
    {  "lastSeenMs": 1717900800000,  "lastSeenRowid": 482910,  "updatedAt": 1717900801234,  "failureRetries": { "<guid>": 1 }}
[/code]

  * Курсор просувається після кожного успішного надсилання й утримується, коли надсилання рядка кидає помилку — наступний запуск повторює той самий рядок із утриманого курсора.
  * Після `maxFailureRetries` послідовних помилок для того самого `guid`, Catchup записує `warn` і примусово просуває курсор повз застрягле повідомлення, щоб подальші запуски могли рухатися далі.
  * GUID, щодо яких уже відмовилися, пропускаються відразу (без спроби надсилання) у подальших запусках і враховуються в `skippedGivenUp` у підсумку запуску.


### Сигнали, видимі оператору

CodeCopy code
[code]
    imessage catchup: replayed=N skippedFromMe=… skippedGivenUp=… failed=… givenUp=… fetchedCount=…imessage catchup: giving up on guid=<guid> after &lt;N&gt; failures; advancing cursor past itimessage catchup: fetched &lt;X&gt; rows across chats, capped to perRunLimit=&lt;Y&gt;
[/code]

Рядок `WARN ... capped to perRunLimit` означає, що один запуск не вичерпав увесь backlog. Збільште `perRunLimit` (макс. 500), якщо ваші прогалини регулярно перевищують стандартний прохід у 50 рядків.

### Коли залишити вимкненим

  * Gateway працює безперервно з автоматичним перезапуском через watchdog, а прогалини завжди < кількох секунд — стандартне вимкнене значення підходить.
  * Обсяг DM низький, і пропущені повідомлення не змінять поведінку агента — початкове вікно `firstRunLookbackMinutes` може надіслати неочікуваний старий контекст під час першого ввімкнення.


Коли ви вмикаєте Catchup, перший запуск без курсора дивиться назад лише на `firstRunLookbackMinutes` (30 хв за замовчуванням), а не на повне вікно `maxAgeMinutes` — це запобігає відтворенню довгої історії повідомлень, що передували ввімкненню.

## Усунення несправностей

imsg not found or RPC unsupported

Перевірте бінарний файл і підтримку RPC:

bashCopy code
[code]
    imsg rpc --helpimsg status --jsonopenclaw channels status --probe
[/code]

Якщо probe повідомляє, що RPC не підтримується, оновіть `imsg`. Якщо дії приватного API недоступні, запустіть `imsg launch` у сеансі користувача macOS, який увійшов у систему, і знову виконайте probe. Якщо Gateway не працює на macOS, використайте налаштування віддаленого Mac через SSH вище замість стандартного локального шляху `imsg`.

Gateway is not running on macOS

Стандартний `cliPath: "imsg"` має виконуватися на Mac, який увійшов у Messages. На Linux або Windows встановіть `channels.imessage.cliPath` на wrapper-скрипт, який підключається до цього Mac через SSH і запускає `imsg "$@"`.

bashCopy code
[code]
    #!/usr/bin/env bashexec ssh -T messages-mac imsg "$@"
[/code]

Потім виконайте:

bashCopy code
[code]
    openclaw channels status --probe --channel imessage
[/code]

DMs are ignored

Перевірте:

  * `channels.imessage.dmPolicy`
  * `channels.imessage.allowFrom`
  * схвалення pairing (`openclaw pairing list imessage`)

Group messages are ignored

Перевірте:

  * `channels.imessage.groupPolicy`
  * `channels.imessage.groupAllowFrom`
  * поведінку allowlist `channels.imessage.groups`
  * конфігурацію шаблонів згадок (`agents.list[].groupChat.mentionPatterns`)

Remote attachments fail

Перевірте:

  * `channels.imessage.remoteHost`
  * `channels.imessage.remoteAttachmentRoots`
  * автентифікацію SSH/SCP-ключем із хоста Gateway
  * наявність ключа хоста в `~/.ssh/known_hosts` на хості Gateway
  * доступність віддаленого шляху для читання на Mac, де працює Messages

macOS permission prompts were missed

Повторно запустіть в інтерактивному GUI-терміналі в тому самому контексті користувача/сеансу й підтвердьте запити:

bashCopy code
[code]
    imsg chats --limit 1imsg send <handle> "test"
[/code]

Підтвердьте, що Full Disk Access + Automation надано для контексту процесу, який запускає OpenClaw/`imsg`.

## Вказівники довідника конфігурації

  * [Довідник конфігурації - iMessage](</uk/gateway/config-channels#imessage>)
  * [Конфігурація Gateway](</uk/gateway/configuration>)
  * [Pairing](</uk/channels/pairing>)


## Пов’язане

  * [Огляд каналів](</uk/channels>) — усі підтримувані канали
  * [Вилучення BlueBubbles і шлях imsg iMessage](</uk/announcements/bluebubbles-imessage>) — оголошення й підсумок міграції
  * [Перехід із BlueBubbles](</uk/channels/imessage-from-bluebubbles>) — таблиця перекладу конфігурації та покрокове перемикання
  * [Pairing](</uk/channels/pairing>) — автентифікація DM і потік pairing
  * [Групи](</uk/channels/groups>) — поведінка групових чатів і gating згадок
  * [Маршрутизація каналів](</uk/channels/channel-routing>) — маршрутизація сеансів для повідомлень
  * [Безпека](</uk/gateway/security>) — модель доступу й зміцнення


Was this useful?YesNo