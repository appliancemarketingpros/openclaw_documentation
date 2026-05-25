---
title: Кілька Gateway
source_url: https://docs.openclaw.ai/uk/gateway/multiple-gateways
scraped_at: 2026-05-25
---

Більшість конфігурацій мають використовувати один Gateway, оскільки один Gateway може обслуговувати кілька підключень до месенджерів і агентів. Якщо вам потрібна сильніша ізоляція або резервування (наприклад, rescue bot), запускайте окремі Gateway з ізольованими профілями/портами.

## Найкраща рекомендована конфігурація

Для більшості користувачів найпростішою конфігурацією rescue bot є:

  * залишити основного бота на профілі за замовчуванням
  * запускати rescue bot з `--profile rescue`
  * використовувати повністю окремого Telegram-бота для облікового запису rescue
  * тримати rescue bot на іншому базовому порту, наприклад `19789`


Це ізолює rescue bot від основного бота, тож він може налагоджувати або застосовувати зміни конфігурації, якщо основний бот недоступний. Залишайте щонайменше 20 портів між базовими портами, щоб похідні порти browser/canvas/CDP ніколи не конфліктували.

## Швидкий старт для rescue bot

Використовуйте це як типовий шлях, якщо у вас немає вагомої причини робити інакше:

bashCopy code
[code]
    # Rescue bot (окремий Telegram-бот, окремий профіль, порт 19789)openclaw --profile rescue onboardopenclaw --profile rescue gateway install --port 19789
[/code]

Якщо ваш основний бот уже працює, зазвичай цього достатньо.

Під час `openclaw --profile rescue onboard`:

  * використовуйте окремий токен Telegram-бота
  * залиште профіль `rescue`
  * використовуйте базовий порт принаймні на 20 вищий, ніж у основного бота
  * прийміть робочу область rescue за замовчуванням, якщо ви вже не керуєте власною


Якщо onboarding уже встановив для вас сервіс rescue, фінальна команда `gateway install` не потрібна.

## Чому це працює

Rescue bot залишається незалежним, тому що має власні:

  * профіль/конфігурацію
  * каталог стану
  * робочу область
  * базовий порт (плюс похідні порти)
  * токен Telegram-бота


Для більшості конфігурацій використовуйте повністю окремого Telegram-бота для профілю rescue:

  * легко обмежити лише операторами
  * окремий токен бота та ідентичність
  * незалежність від встановлення каналу/застосунку основного бота
  * простий шлях відновлення через DM, коли основний бот зламаний


## Що змінює `--profile rescue onboard`

`openclaw --profile rescue onboard` використовує звичайний процес onboarding, але записує все в окремий профіль.

На практиці це означає, що rescue bot отримує власні:

  * файл конфігурації
  * каталог стану
  * робочу область (за замовчуванням `~/.openclaw/workspace-rescue`)
  * ім’я керованого сервісу


В іншому запити такі самі, як і під час звичайного onboarding.

## Загальна конфігурація з кількома Gateway

Описана вище схема rescue bot — найпростіший типовий варіант, але той самий шаблон ізоляції працює для будь-якої пари або групи Gateway на одному хості.

Для більш загальної конфігурації дайте кожному додатковому Gateway власний іменований профіль і власний базовий порт:

bashCopy code
[code]
    # main (профіль за замовчуванням)openclaw setupopenclaw gateway --port 18789 # додатковий gatewayopenclaw --profile ops setupopenclaw --profile ops gateway --port 19789
[/code]

Якщо ви хочете, щоб обидва Gateway використовували іменовані профілі, це теж працює:

bashCopy code
[code]
    openclaw --profile main setupopenclaw --profile main gateway --port 18789 openclaw --profile ops setupopenclaw --profile ops gateway --port 19789
[/code]

Сервіси дотримуються того самого шаблону:

bashCopy code
[code]
    openclaw gateway installopenclaw --profile ops gateway install --port 19789
[/code]

Використовуйте швидкий старт для rescue bot, коли вам потрібен резервний операторський шлях. Використовуйте загальний шаблон профілів, коли вам потрібно кілька довготривалих Gateway для різних каналів, орендарів, робочих областей або операційних ролей.

## Контрольний список ізоляції

Зробіть унікальними для кожного екземпляра Gateway:

  * `OPENCLAW_CONFIG_PATH` — окремий файл конфігурації для кожного екземпляра
  * `OPENCLAW_STATE_DIR` — окремі сесії, облікові дані, кеші для кожного екземпляра
  * `agents.defaults.workspace` — окремий корінь робочої області для кожного екземпляра
  * `gateway.port` (або `--port`) — унікальний для кожного екземпляра
  * похідні порти browser/canvas/CDP


Якщо вони спільні, ви зіткнетеся з гонками конфігурації та конфліктами портів.

## Відображення портів (похідні)

Базовий порт = `gateway.port` (або `OPENCLAW_GATEWAY_PORT` / `--port`).

  * порт сервісу керування browser = базовий + 2 (лише local loopback)
  * canvas host обслуговується HTTP-сервером Gateway (той самий порт, що й `gateway.port`)
  * порти CDP профілю Browser автоматично виділяються з діапазону `browser.controlPort + 9 .. + 108`


Якщо ви перевизначаєте будь-що з цього в конфігурації або env, ви повинні зберігати унікальність для кожного екземпляра.

## Нотатки щодо Browser/CDP (типова пастка)

  * **Не** фіксуйте `browser.cdpUrl` на однакові значення для кількох екземплярів.
  * Кожному екземпляру потрібен власний порт керування browser і власний діапазон CDP (похідний від його порту gateway).
  * Якщо вам потрібні явні порти CDP, задайте `browser.profiles.<name>.cdpPort` для кожного екземпляра.
  * Віддалений Chrome: використовуйте `browser.profiles.<name>.cdpUrl` (для кожного профілю, для кожного екземпляра).


## Приклад ручного env

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=~/.openclaw/main.json \OPENCLAW_STATE_DIR=~/.openclaw \openclaw gateway --port 18789 OPENCLAW_CONFIG_PATH=~/.openclaw/rescue.json \OPENCLAW_STATE_DIR=~/.openclaw-rescue \openclaw gateway --port 19789
[/code]

## Швидкі перевірки

bashCopy code
[code]
    openclaw gateway status --deepopenclaw --profile rescue gateway status --deepopenclaw --profile rescue gateway probeopenclaw statusopenclaw --profile rescue statusopenclaw --profile rescue browser status
[/code]

Тлумачення:

  * `gateway status --deep` допомагає виявити застарілі сервіси launchd/systemd/schtasks від старіших інсталяцій.
  * Попереджувальний текст `gateway probe`, наприклад `multiple reachable gateways detected`, є очікуваним лише тоді, коли ви навмисно запускаєте більше ніж один ізольований gateway.


## Пов’язане

  * [Інструкція з Gateway](</uk/gateway>)
  * [Блокування Gateway](</uk/gateway/gateway-lock>)
  * [Конфігурація](</uk/gateway/configuration>)


Was this useful?YesNo