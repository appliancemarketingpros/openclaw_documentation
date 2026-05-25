---
title: Оновлення
source_url: https://docs.openclaw.ai/uk/install/updating
scraped_at: 2026-05-25
---

Підтримуйте OpenClaw в актуальному стані.

## Рекомендовано: `openclaw update`

Найшвидший спосіб оновлення. Він визначає тип вашого встановлення (npm або git), отримує найновішу версію, запускає `openclaw doctor` і перезапускає Gateway.

bashCopy code
[code]
    openclaw update
[/code]

Щоб перемкнути канали або вибрати конкретну версію:

bashCopy code
[code]
    openclaw update --channel betaopenclaw update --channel devopenclaw update --tag mainopenclaw update --dry-run   # preview without applying
[/code]

`openclaw update` не приймає `--verbose`. Для діагностики оновлення використовуйте `--dry-run`, щоб попередньо переглянути заплановані дії, `--json` для структурованих результатів або `openclaw update status --json`, щоб переглянути стан каналу й доступності. Інсталятор має власний прапорець `--verbose`, але цей прапорець не є частиною `openclaw update`.

`--channel beta` надає перевагу beta, але середовище виконання повертається до stable/latest, коли тег beta відсутній або старіший за найновіший стабільний випуск. Використовуйте `--tag beta`, якщо вам потрібен необроблений npm beta dist-tag для одноразового оновлення пакета.

Для керованих Plugin-ів резервний перехід beta-каналу є попередженням: оновлення ядра може все одно завершитися успішно, тоді як Plugin використовує свій записаний default/latest випуск, бо beta для Plugin недоступна.

Див. [Канали розробки](</uk/install/development-channels>), щоб дізнатися семантику каналів.

## Перемикання між встановленнями npm і git

Використовуйте канали, коли хочете змінити тип встановлення. Засіб оновлення зберігає ваш стан, конфігурацію, облікові дані та робочу область у `~/.openclaw`; він змінює лише те, яке встановлення коду OpenClaw використовують CLI і Gateway.

bashCopy code
[code]
    # npm package install -> editable git checkoutopenclaw update --channel dev # git checkout -> npm package installopenclaw update --channel stable
[/code]

Спершу запустіть із `--dry-run`, щоб попередньо переглянути точне перемикання режиму встановлення:

bashCopy code
[code]
    openclaw update --channel dev --dry-runopenclaw update --channel stable --dry-run
[/code]

Канал `dev` забезпечує git checkout, збирає його та встановлює глобальний CLI з цього checkout. Канали `stable` і `beta` використовують встановлення пакетів. Якщо Gateway уже встановлено, `openclaw update` оновлює метадані сервісу та перезапускає його, якщо ви не передали `--no-restart`.

## Альтернатива: повторно запустіть інсталятор

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

Додайте `--no-onboard`, щоб пропустити онбординг. Щоб примусово вибрати конкретний тип встановлення через інсталятор, передайте `--install-method git --no-onboard` або `--install-method npm --no-onboard`.

Якщо `openclaw update` завершується помилкою після етапу встановлення npm-пакета, повторно запустіть інсталятор. Інсталятор не викликає старий засіб оновлення; він запускає глобальне встановлення пакета напряму й може відновити частково оновлене npm-встановлення.

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --install-method npm
[/code]

Щоб закріпити відновлення за конкретною версією або dist-tag, додайте `--version`:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --install-method npm --version <version-or-dist-tag>
[/code]

## Альтернатива: ручне встановлення через npm, pnpm або bun

bashCopy code
[code]
    npm i -g openclaw@latest
[/code]

Надавайте перевагу `openclaw update` для контрольованих встановлень, бо він може узгодити заміну пакета із запущеним сервісом Gateway. Якщо ви оновлюєте вручну, поки керований Gateway працює, перезапустіть Gateway одразу після завершення роботи менеджера пакетів, щоб старий процес не продовжував обслуговування з уже замінених файлів пакета.

Коли `openclaw update` керує глобальним npm-встановленням, він спершу встановлює ціль у тимчасовий npm-префікс, перевіряє інвентар упакованого `dist`, а потім замінює чисте дерево пакета в реальному глобальному префіксі. Це запобігає накладанню npm нового пакета на застарілі файли зі старого пакета. Якщо команда встановлення завершується помилкою, OpenClaw повторює спробу один раз із `--omit=optional`. Ця повторна спроба допомагає хостам, де нативні необов’язкові залежності не можуть скомпілюватися, водночас залишаючи початкову помилку видимою, якщо резервний варіант також завершується невдачею.

bashCopy code
[code]
    pnpm add -g openclaw@latest
[/code]

bashCopy code
[code]
    bun add -g openclaw@latest
[/code]

### Розширені теми встановлення npm

Дерево пакетів лише для читання

OpenClaw розглядає упаковані глобальні встановлення як доступні лише для читання під час виконання, навіть коли глобальний каталог пакета доступний для запису поточному користувачу. Встановлення пакетів Plugin-ів розміщуються у власних npm/git коренях OpenClaw у каталозі конфігурації користувача, а запуск Gateway не змінює дерево пакета OpenClaw.

Деякі Linux npm-конфігурації встановлюють глобальні пакети в каталоги, що належать root, наприклад `/usr/lib/node_modules/openclaw`. OpenClaw підтримує таке компонування, бо команди встановлення/оновлення Plugin-ів записують дані поза цим глобальним каталогом пакета.

Посилені systemd-одиниці

Надайте OpenClaw доступ на запис до його коренів конфігурації/стану, щоб явні встановлення Plugin-ів, оновлення Plugin-ів і очищення doctor могли зберігати свої зміни:

iniCopy code
[code]
    ReadWritePaths=/var/lib/openclaw /home/openclaw/.openclaw /tmp
[/code]

Попередня перевірка місця на диску

Перед оновленнями пакетів і явними встановленнями Plugin-ів OpenClaw намагається виконати приблизну перевірку місця на диску для цільового тому. Малий обсяг вільного місця створює попередження з перевіреним шляхом, але не блокує оновлення, бо квоти файлової системи, знімки й мережеві томи можуть змінитися після перевірки. Фактичне встановлення через менеджер пакетів і післяінсталяційна перевірка залишаються авторитетними.

## Автоматичний засіб оновлення

Автоматичний засіб оновлення вимкнений за замовчуванням. Увімкніть його в `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  update: {    channel: "stable",    auto: {      enabled: true,      stableDelayHours: 6,      stableJitterHours: 12,      betaCheckIntervalHours: 1,    },  },}
[/code]

Канал | Поведінка  
---|---  
`stable` | Чекає `stableDelayHours`, а потім застосовує з детермінованим джитером у межах `stableJitterHours` (поступове розгортання).  
`beta` | Перевіряє кожні `betaCheckIntervalHours` (за замовчуванням: щогодини) і застосовує негайно.  
`dev` | Без автоматичного застосування. Використовуйте `openclaw update` вручну.  
  
Gateway також записує підказку про оновлення під час запуску (вимкніть за допомогою `update.checkOnStart: false`). Для відкату або відновлення після інциденту встановіть `OPENCLAW_NO_AUTO_UPDATE=1` у середовищі Gateway, щоб заблокувати автоматичні застосування, навіть коли налаштовано `update.auto.enabled`. Підказки про оновлення під час запуску все ще можуть виконуватися, якщо `update.checkOnStart` також не вимкнено.

Оновлення менеджера пакетів, запитані через live-обробник площини керування Gateway, примусово виконують неперенесений перезапуск оновлення без періоду охолодження після заміни пакета. Це запобігає тому, щоб старий процес у пам’яті залишався достатньо довго, щоб ліниво завантажувати фрагменти з дерева пакета, яке вже було замінено. Shell `openclaw update` залишається пріоритетним шляхом для контрольованих встановлень, бо він може зупиняти й перезапускати сервіс навколо оновлення.

## Після оновлення

### Запустіть doctor

bashCopy code
[code]
    openclaw doctor
[/code]

Мігрує конфігурацію, перевіряє політики DM і перевіряє працездатність Gateway. Подробиці: [Doctor](</uk/gateway/doctor>)

### Перезапустіть Gateway

bashCopy code
[code]
    openclaw gateway restart
[/code]

### Перевірте

bashCopy code
[code]
    openclaw health
[/code]

## Відкат

### Закріплення версії (npm)

bashCopy code
[code]
    npm i -g openclaw@<version>openclaw doctoropenclaw gateway restart
[/code]

### Закріплення коміту (джерельний код)

bashCopy code
[code]
    git fetch origingit checkout "$(git rev-list -n 1 --before=\"2026-01-01\" origin/main)"pnpm install && pnpm buildopenclaw gateway restart
[/code]

Щоб повернутися до найновішої версії: `git checkout main && git pull`.

## Якщо ви застрягли

  * Запустіть `openclaw doctor` ще раз і уважно прочитайте вивід.
  * Для `openclaw update --channel dev` на checkout-ах із джерельного коду засіб оновлення автоматично ініціалізує `pnpm`, коли це потрібно. Якщо ви бачите помилку ініціалізації pnpm/corepack, встановіть `pnpm` вручну (або повторно увімкніть `corepack`) і повторно запустіть оновлення.
  * Перевірте: [Усунення несправностей](</uk/gateway/troubleshooting>)
  * Запитайте в Discord: <https://discord.gg/clawd>


## Пов’язане

  * [Огляд встановлення](</uk/install>): усі методи встановлення.
  * [Doctor](</uk/gateway/doctor>): перевірки працездатності після оновлень.
  * [Міграція](</uk/install/migrating>): посібники з міграції між основними версіями.


Was this useful?YesNo