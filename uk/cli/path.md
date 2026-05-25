---
title: Шлях
source_url: https://docs.openclaw.ai/uk/cli/path
scraped_at: 2026-05-25
---

# `openclaw path`

Наданий Plugin доступ оболонки до адресної основи `oc://`: одна схема шляхів із диспетчеризацією за типом для інспектування та редагування адресованих файлів робочого простору (markdown, jsonc, jsonl). Ті, хто розгортає власний хостинг, автори Plugin та розширення редакторів використовують її, щоб читати, знаходити або оновлювати вузьку ділянку без саморобних парсерів для кожного файлу.

CLI віддзеркалює публічні дієслова цієї основи:

  * `resolve` є конкретним і повертає один збіг.
  * `find` є дієсловом для множинних збігів: шаблонів, об’єднань, предикатів і позиційного розгортання.
  * `set` приймає лише конкретні шляхи або маркери вставлення; шаблони з підстановками відхиляються до запису.


`path` надається вбудованим необов’язковим Plugin `oc-path`. Увімкніть його перед першим використанням:

bashCopy code
[code]
    openclaw plugins enable oc-path
[/code]

## Навіщо це використовувати

Стан OpenClaw розподілений між редагованим людьми markdown, коментованою конфігурацією JSONC та журналами JSONL лише з додаванням. Shell-скриптам, хукам і агентам часто потрібне одне невелике значення з цих файлів: ключ frontmatter, налаштування Plugin, поле запису журналу або пункт списку в іменованому розділі.

`openclaw path` дає таким викликам стабільну адресу замість одноразового grep, регулярного виразу чи парсера для кожного типу файлу. Один і той самий шлях `oc://` можна перевірити, розв’язати, знайти, прогнати в режимі пробного запуску та записати з термінала, що спрощує перегляд вузької автоматизації та робить її безпечнішою для повторного виконання. Це особливо корисно, коли ви хочете оновити один листовий елемент, зберігши решту коментарів файлу, закінчення рядків і навколишнє форматування.

Використовуйте це, коли потрібна сутність має логічну адресу, але фізична форма файлу різниться:

  * Хук хоче прочитати одне налаштування з коментованого JSONC, не втрачаючи коментарів під час запису значення назад.
  * Скрипт обслуговування хоче знайти кожне відповідне поле події в журналі JSONL, не завантажуючи весь журнал у спеціальний парсер.
  * Розширення редактора хоче перейти до розділу markdown або пункту списку за slug, а потім відрендерити точний рядок, до якого шлях розв’язався.
  * Агент хоче пробно виконати крихітне редагування робочого простору перед застосуванням, із видимими для перегляду зміненими байтами.


Ймовірно, вам не потрібен `openclaw path` для звичайних редагувань цілих файлів, складних міграцій конфігурації або записів, специфічних для пам’яті. Для цього слід використовувати команду або Plugin власника. `path` призначений для малих адресованих операцій із файлами, де повторювана термінальна команда зрозуміліша за ще один спеціальний парсер.

## Як це використовується

Прочитати одне значення з редагованого людьми конфігураційного файлу:

bashCopy code
[code]
    openclaw path resolve 'oc://config.jsonc/plugins/github/enabled'
[/code]

Попередньо переглянути запис без змін на диску:

bashCopy code
[code]
    openclaw path set 'oc://config.jsonc/plugins/github/enabled' 'true' --dry-run
[/code]

Знайти відповідні записи в журналі JSONL лише з додаванням:

bashCopy code
[code]
    openclaw path find 'oc://session.jsonl/[event=tool_call]/name'
[/code]

Адресувати інструкцію в markdown за розділом і пунктом замість номера рядка:

bashCopy code
[code]
    openclaw path resolve 'oc://AGENTS.md/runtime-safety/openclaw-gateway'
[/code]

Перевірити шлях у CI або preflight-скрипті перед тим, як скрипт читатиме або писатиме:

bashCopy code
[code]
    openclaw path validate 'oc://AGENTS.md/tools/$last/risk'
[/code]

Ці команди розраховані на копіювання в shell-скрипти. Використовуйте `--json`, коли виклику потрібен структурований вивід, і `--human`, коли результат переглядає людина.

## Як це працює

`openclaw path` виконує чотири дії:

  1. Розбирає адресу `oc://` на слоти: файл, розділ, пункт, поле та необов’язкову сесію.
  2. Вибирає адаптер типу файлу за цільовим розширенням (`.md`, `.jsonc`, `.jsonl` та пов’язані псевдоніми).
  3. Розв’язує слоти відносно AST цього типу файлу: заголовків/пунктів markdown, ключів об’єктів/індексів масивів JSONC або рядкових записів JSONL.
  4. Для `set` випускає відредаговані байти через той самий адаптер, щоб незмінені частини файлу зберігали свої коментарі, закінчення рядків і близьке форматування там, де це підтримує тип файлу.


`resolve` і `set` потребують однієї конкретної цілі. `find` є дослідницьким дієсловом: воно розгортає підстановки, об’єднання, предикати й порядкові номери в конкретні збіги, які можна переглянути перед вибором одного для запису.

## Підкоманди

Підкоманда | Призначення  
---|---  
`resolve <oc-path>` | Надрукувати конкретний збіг за шляхом (або "not found").  
`find <pattern>` | Перелічити збіги для шляху з підстановкою / об’єднанням / предикатом.  
`set <oc-path> <value>` | Записати листовий елемент або ціль вставлення за конкретним шляхом. Підтримує `--dry-run`.  
`validate <oc-path>` | Лише розбір; надрукувати структурний поділ (файл / розділ / пункт / поле).  
`emit <file>` | Провести файл через `parseXxx` \+ `emitXxx` туди й назад (діагностика байтової точності).  
  
## Глобальні прапорці

Прапорець | Призначення  
---|---  
`--cwd <dir>` | Розв’язати слот файлу відносно цього каталогу (типово: `process.cwd()`).  
`--file <path>` | Перевизначити розв’язаний шлях слота файлу (абсолютний доступ).  
`--json` | Примусово виводити JSON (типово, коли stdout не є TTY).  
`--human` | Примусово виводити для людини (типово, коли stdout є TTY).  
`--dry-run` | (лише для `set`) надрукувати байти, які були б записані, без запису.  
  
## Синтаксис `oc://`

CodeCopy code
[code]
    oc://FILE/SECTION/ITEM/FIELD?session=SCOPE
[/code]

Правила слотів: `field` потребує `item`, а `item` потребує `section`. Для всіх чотирьох слотів:

  * **Цитовані сегменти** — `"a/b.c"` зберігає розділювачі `/` і `.`. Вміст є байт-літеральним; `"` і `\` не дозволені всередині лапок. Слот файлу також враховує лапки: `oc://"skills/email-drafter"/Tools/$last` трактує `skills/email-drafter` як один шлях файлу.
  * **Предикати** — `[k=v]`, `[k!=v]`, `[k<v]`, `[k<=v]`, `[k>v]`, `[k>=v]`. Числові оператори потребують, щоб обидві сторони приводилися до скінченних чисел.
  * **Об’єднання** — `{a,b,c}` збігається з будь-якою з альтернатив.
  * **Підстановки** — `*` (один підсегмент) і `**` (нуль або більше, рекурсивно). `find` приймає їх; `resolve` і `set` відхиляють їх як неоднозначні.
  * **Позиційний** — `$last` розв’язується в останній індекс / останній оголошений ключ.
  * **Порядковий** — `#N` для N-го збігу в порядку документа.
  * **Маркери вставлення** — `+`, `+key`, `+nnn` для вставлення за ключем / індексом (використовуйте з `set`).
  * **Область сесії** — `?session=cron-daily` тощо. Ортогональна до вкладеності слотів. Значення сесії є сирими, не декодуються з percent-encoding; вони не можуть містити керівні символи або зарезервовані розділювачі запиту (`?`, `&`, `%`).


Зарезервовані символи (`?`, `&`, `%`) поза цитованими сегментами, предикатами або об’єднаннями відхиляються. Керівні символи (U+0000-U+001F, U+007F) відхиляються всюди, включно зі значенням запиту `session`.

`formatOcPath(parseOcPath(path)) === path` гарантовано для канонічних шляхів. Неканонічні параметри запиту ігноруються, окрім першого непорожнього значення `session=`.

## Адресація за типом файлу

Тип | Модель адресації  
---|---  
Markdown | Розділи H2 за slug, пункти списку за slug або `#N`, frontmatter через `[frontmatter]`.  
JSONC/JSON | Ключі об’єктів та індекси масивів; крапки ділять вкладені підсегменти, якщо їх не взято в лапки.  
JSONL | Адреси рядків верхнього рівня (`L1`, `L2`, `$last`), потім спуск у стилі JSONC усередині рядка.  
  
`resolve` повертає структурований збіг: `root`, `node`, `leaf` або `insertion-point`, із номером рядка з основою 1. Листові значення подаються як текст плюс `leafType`, щоб автори Plugin могли рендерити попередні перегляди, не залежачи від форми AST конкретного типу.

## Контракт мутації

`set` записує одну конкретну ціль:

  * Значення markdown frontmatter і поля пунктів `- key: value` є рядковими листовими елементами. Вставлення в markdown додають розділи, ключі frontmatter або пункти розділів і рендерять канонічну форму markdown для зміненого файлу.
  * Записи листових елементів JSONC приводять рядкове значення до наявного типу листка (`string`, скінченний `number`, `true`/`false` або `null`). Вставлення об’єктів і масивів JSONC розбирають `<value>` як JSON і використовують шлях редагування `jsonc-parser` для звичайних записів листків, зберігаючи коментарі та близьке форматування.
  * Записи листових елементів JSONL приводяться як JSONC усередині рядка. Заміна цілого рядка й додавання розбирають `<value>` як JSON. Відрендерений JSONL зберігає домінантну для файлу конвенцію закінчень рядків LF/CRLF.


Використовуйте `--dry-run` перед записами, видимими користувачу, коли точні байти мають значення. Основа зберігає байтово ідентичний вивід для проходів parse/emit туди й назад, але мутація може канонізувати відредаговану ділянку або файл залежно від типу.

## Приклади

bashCopy code
[code]
    # Validate a path (no filesystem access)openclaw path validate 'oc://AGENTS.md/Tools/$last/risk' # Read a leafopenclaw path resolve 'oc://gateway.jsonc/version' # Wildcard searchopenclaw path find 'oc://session.jsonl/*/event' --file ./logs/session.jsonl # Dry-run a writeopenclaw path set 'oc://gateway.jsonc/version' '2.0' --dry-run # Apply the writeopenclaw path set 'oc://gateway.jsonc/version' '2.0' # Byte-fidelity round-trip (diagnostic)openclaw path emit ./AGENTS.md
[/code]

Більше прикладів граматики:

bashCopy code
[code]
    # Quote keys containing / or .openclaw path resolve 'oc://config.jsonc/agents.defaults.models/"anthropic/claude-opus-4-7"/alias' # Predicate search over JSONC childrenopenclaw path find 'oc://config.jsonc/plugins/[enabled=true]/id' # Insert into a JSONC arrayopenclaw path set 'oc://config.jsonc/items/+1' '{"id":"new","enabled":true}' --dry-run # Insert a JSONC object keyopenclaw path set 'oc://config.jsonc/plugins/+github' '{"enabled":true}' --dry-run # Append a JSONL eventopenclaw path set 'oc://session.jsonl/+' '{"event":"checkpoint","ok":true}' --file ./logs/session.jsonl # Resolve the last JSONL value lineopenclaw path resolve 'oc://session.jsonl/$last/event' --file ./logs/session.jsonl # Address markdown frontmatteropenclaw path resolve 'oc://AGENTS.md/[frontmatter]/name' # Insert markdown frontmatteropenclaw path set 'oc://AGENTS.md/[frontmatter]/+description' 'Agent instructions' --dry-run # Find markdown item fieldsopenclaw path find 'oc://SKILL.md/Tools/*/send_email' # Validate a session-scoped pathopenclaw path validate 'oc://AGENTS.md/Tools/$last/risk?session=cron-daily'
[/code]

## Рецепти за типом файлу

Ті самі п’ять дієслів працюють для всіх типів; схема адресації диспетчеризує за розширенням файлу. Наведені нижче приклади використовують фікстури з опису PR.

### Markdown

textCopy code
[code]
    <!-- frontmatter.md -->---name: drafterdescription: email drafting agenttier: core---## Tools- gh: GitHub CLI- curl: HTTP client- send_email: enabled
[/code]

bashCopy code
[code]
    $ openclaw path resolve 'oc://x.md/[frontmatter]/tier' --file frontmatter.md --humanleaf @ L4: "core" (string) $ openclaw path resolve 'oc://x.md/tools/gh/gh' --file frontmatter.md --humanleaf @ L9: "GitHub CLI" (string) $ openclaw path find 'oc://x.md/tools/*' --file frontmatter.md --human3 matches for oc://x.md/tools/*:  oc://x.md/tools/gh           →  node @ L9 [md-item]  oc://x.md/tools/curl         →  node @ L10 [md-item]  oc://x.md/tools/send-email   →  node @ L11 [md-item]
[/code]

Предикат `[frontmatter]` адресує YAML-блок frontmatter; `tools` збігається із заголовком `## Tools` через slug, а листки пунктів зберігають свою slug-форму навіть коли джерело використовує підкреслення (`send_email` → `send-email`).

### JSONC

textCopy code
[code]
    // config.jsonc{  "plugins": {    "github": {"enabled": true, "role": "vcs"},    "slack":  {"enabled": false, "role": "chat"}  }}
[/code]

bashCopy code
[code]
    $ openclaw path resolve 'oc://config.jsonc/plugins/github/enabled' --file config.jsonc --humanleaf @ L4: "true" (boolean) $ openclaw path set 'oc://config.jsonc/plugins/slack/enabled' 'true' --file config.jsonc --dry-run--dry-run: would write 142 bytes to /…/config.jsonc{  "plugins": {    "github": {"enabled": true, "role": "vcs"},    "slack":  {"enabled": true, "role": "chat"}  }}
[/code]

Редагування JSONC проходять через `jsonc-parser`, тому коментарі й пробіли зберігаються після `set`. Спершу запустіть із `--dry-run`, щоб переглянути байти перед фіксацією змін.

### JSONL

textCopy code
[code]
    {"event":"start","userId":"u1","ts":1}{"event":"action","userId":"u1","ts":2}{"event":"end","userId":"u1","ts":3}
[/code]

bashCopy code
[code]
    $ openclaw path find 'oc://session.jsonl/[event=action]/userId' --file session.jsonl --human1 match for oc://session.jsonl/[event=action]/userId:  oc://session.jsonl/L2/userId  →  leaf @ L2: "u1" (string) $ openclaw path resolve 'oc://session.jsonl/L2/ts' --file session.jsonl --humanleaf @ L2: "2" (number)
[/code]

Кожен рядок є записом. Звертайтеся за предикатом (`[event=action]`), коли ви не знаєте номер рядка, або за канонічним сегментом `LN`, коли знаєте.

## Довідник підкоманд

### `resolve <oc-path>`

Зчитує один листок або вузол. Символи-замінники відхиляються — використовуйте для них `find`. Завершується з кодом `0` за збігу, `1` за коректної відсутності збігу, `2` у разі помилки розбору або відхиленого шаблону.

bashCopy code
[code]
    openclaw path resolve 'oc://AGENTS.md/tools/gh/risk' --humanopenclaw path resolve 'oc://gateway.jsonc/server/port' --json
[/code]

### `find <pattern>`

Перелічує всі збіги для шаблону із символом-замінником / предикатом / об’єднанням. Завершується з кодом `0`, якщо є принаймні один збіг, і `1`, якщо збігів немає. Символи-замінники в слоті файлу відхиляються з `OC_PATH_FILE_WILDCARD_UNSUPPORTED` — передайте конкретний файл (пошук за шаблонами в кількох файлах є майбутньою функцією).

bashCopy code
[code]
    openclaw path find 'oc://AGENTS.md/tools/**/risk'openclaw path find 'oc://session.jsonl/[event=action]/userId'openclaw path find 'oc://config.jsonc/plugins/{github,slack}/enabled'
[/code]

### `set <oc-path> <value>`

Записує листок. Поєднуйте з `--dry-run`, щоб попередньо переглянути байти, які було б записано без зміни файлу. Завершується з кодом `0` після успішного запису, `1`, якщо субстрат відмовляє (наприклад, спрацював захисний sentinel), `2` у разі помилок розбору.

bashCopy code
[code]
    openclaw path set 'oc://gateway.jsonc/version' '2.0' --dry-runopenclaw path set 'oc://gateway.jsonc/version' '2.0'openclaw path set 'oc://AGENTS.md/Tools/+gh/risk' 'low'
[/code]

Маркер вставлення `+key` створює іменований дочірній елемент, якщо він ще не існує; `+nnn` і голий `+` працюють для індексованого вставлення та вставлення в кінець відповідно.

### `validate <oc-path>`

Перевірка лише розбору. Без доступу до файлової системи. Корисно, коли потрібно підтвердити, що шаблонний шлях має правильну форму перед підставлянням змінних, або коли потрібен структурний розбір для налагодження:

bashCopy code
[code]
    $ openclaw path validate 'oc://AGENTS.md/tools/gh' --humanvalid: oc://AGENTS.md/tools/gh  file:    AGENTS.md  section: tools  item:    gh
[/code]

Завершується з кодом `0`, коли шлях дійсний, `1`, коли недійсний (зі структурованими `code` і `message`), `2` у разі помилок аргументів.

### `emit <file>`

Пропускає файл туди й назад через парсер і емітер для відповідного типу. Вивід має бути побайтово ідентичним до вводу для справного файлу — розбіжність указує на помилку парсера або спрацювання sentinel. Корисно для налагодження поведінки субстрату на реальних вхідних даних.

bashCopy code
[code]
    openclaw path emit ./AGENTS.mdopenclaw path emit ./gateway.jsonc --json
[/code]

## Коди виходу

Код | Значення  
---|---  
`0` | Успіх. (`resolve` / `find`: принаймні один збіг. `set`: запис виконано.)  
`1` | Немає збігу, або `set` відхилено субстратом (без помилки системного рівня).  
`2` | Помилка аргументів або розбору.  
  
## Режим виводу

`openclaw path` враховує TTY: людиночитний вивід у терміналі, JSON, коли stdout передається через pipe або перенаправляється. `--json` і `--human` перевизначають автовизначення.

## Нотатки

  * `set` записує байти через шлях emit субстрату, який автоматично застосовує захист redaction-sentinel. Листок, що містить `__OPENCLAW_REDACTED__` (дослівно або як підрядок), відхиляється під час запису.
  * Розбір JSONC і редагування листків використовують локальну для plugin залежність `jsonc-parser`, тому коментарі та форматування зберігаються під час звичайних записів листків, а не проходять через самописний шлях парсера/повторного рендерингу.
  * `path` не знає про LKG. Якщо файл відстежується LKG, наступний виклик observe вирішує, чи виконувати promote / recover. `set --batch` для атомарного multi-set через життєвий цикл promote/recover LKG заплановано разом із субстратом LKG-recovery.


## Пов’язане

  * [Довідник CLI](</uk/cli>)


Was this useful?YesNo