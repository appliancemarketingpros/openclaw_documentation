---
title: CLI робочої дошки
source_url: https://docs.openclaw.ai/uk/cli/workboard
scraped_at: 2026-06-29
---

ReferenceCLI commands

`openclaw workboard` — це термінальна поверхня для вбудованого [Workboard Plugin](</uk/plugins/workboard>). Вона дає оператору змогу перелічувати картки, створювати картку, переглядати одну картку й просити запущений Gateway передати готову роботу в робочі запуски під¬агентів.

Увімкніть Plugin перед використанням команди:

bashCopy code
[code]
    openclaw plugins enable workboardopenclaw gateway restart
[/code]

## Використання

bashCopy code
[code]
    openclaw workboard list [--board <id>] [--status <status>] [--include-archived] [--json]openclaw workboard create <title...> [--notes <text>] [--status <status>] [--priority <priority>] [--agent <id>] [--board <id>] [--labels <items>] [--json]openclaw workboard show <id> [--json]openclaw workboard dispatch [--url <url>] [--token <token>] [--timeout <ms>] [--json]
[/code]

Команда читає й записує ту саму SQLite-базу даних, що належить Plugin і використовується панеллю керування та агентськими інструментами Workboard. Ідентифікатори карток можна передавати як повний id або як однозначний префікс, коли команда приймає id картки.

## `list`

bashCopy code
[code]
    openclaw workboard listopenclaw workboard list --board default --status readyopenclaw workboard list --json
[/code]

Текстовий вивід компактний:

textCopy code
[code]
    7f4a2c10  ready     high    default agent-a  Fix stale worker heartbeat
[/code]

Стовпці: префікс id, статус, пріоритет, id дошки, необов’язковий id агента та заголовок.

Прапорці:

Прапорець | Призначення  
---|---  
`--board <id>` | Обмежити результати одним простором імен дошки  
`--status <status>` | Обмежити результати одним статусом Workboard  
`--include-archived` | Додати архівовані картки до компактного текстового виводу  
`--json` | Надрукувати повний список карток як машинний JSON  
  
Компактний текстовий вивід типово приховує архівовані картки, щоб CLI відповідав команді `/workboard list`. Передайте `--include-archived`, щоб показати їх. Вивід JSON зберігає повний список карток, включно з архівованими картками, для наявної автоматизації.

## `create`

bashCopy code
[code]
    openclaw workboard create "Fix stale worker heartbeat" --priority high --labels bug,workboardopenclaw workboard create "Write Workboard docs" --status ready --agent docs-agent --board docs --notes "Cover CLI, slash command, dispatch, and SQLite state."
[/code]

Прапорці:

Прапорець | Призначення  
---|---  
`--notes <text>` | Початкові нотатки картки  
`--status <status>` | Початковий статус, типово `todo`  
`--priority <priority>` | Пріоритет, типово `normal`  
`--agent <id>` | Призначити картку агенту або id власника  
`--board <id>` | Зберегти картку в просторі імен дошки  
`--labels <items>` | Мітки, розділені комами  
`--json` | Надрукувати створену картку як машинний JSON  
  
`create` записує безпосередньо в SQLite-стан Workboard. Картка одразу видима у вкладці Workboard у Control UI та інструментам Workboard.

## `show`

bashCopy code
[code]
    openclaw workboard show 7f4a2c10openclaw workboard show 7f4a2c10 --json
[/code]

Текстовий вивід друкує компактний рядок картки та нотатки. Вивід JSON повертає повний запис картки, включно з метаданими виконання, спробами, коментарями, посиланнями, доказами, артефактами, журналами працівника, станом протоколу, діагностикою та метаданими автоматизації.

## `dispatch`

bashCopy code
[code]
    openclaw workboard dispatchopenclaw workboard dispatch --jsonopenclaw workboard dispatch --url http://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"
[/code]

`dispatch` спершу викликає метод RPC запущеного Gateway `workboard.cards.dispatch`. Цей шлях використовує той самий runtime під¬агента, що й дія dispatch у панелі керування, тож готові картки стають відстежуваними завданнями робочими запусками з пов’язаними ключами сеансів. Картки з призначеним агентом використовують ключі сеансів під¬агента, обмежені областю агента; непризначені картки зберігають ключ під¬агента без області, щоб зберігався налаштований типовий агент Gateway.

Цикл dispatch:

  1. Підвищує дочірні елементи з готовими залежностями до `ready`.
  2. Блокує протерміновані заявки або робочі запуски, що вичерпали час очікування.
  3. Записує метадані dispatch у готові картки.
  4. Вибирає невелику партію незаявлених готових карток.
  5. Заявляє кожну вибрану картку для диспетчера або призначеного агента.
  6. Запускає робочий запуск під¬агента з обмеженим контекстом картки та токеном заявки картки.
  7. Зберігає id робочого запуску, ключ сеансу, зв’язок із завданням, коли ledger завдань Gateway повідомляє його, статус виконання та журнал працівника в картці.


Вибір навмисно консервативний. Один dispatch типово запускає щонайбільше трьох працівників, пропускає архівовані або вже заявлені картки та запускає лише одну картку на власника або агента за один прохід. Картки, які вже належать активній запущеній роботі або роботі на перегляді, залишаються для пізнішого dispatch.

Якщо запуск працівника завершується помилкою після того, як картку заявлено, Workboard блокує цю картку, очищає заявку та записує помилку в метадані виконання картки й журналу працівника. Це робить невдалі запуски видимими замість тихого повернення картки до черги.

Якщо явну ціль Gateway не надано, а локальний Gateway недоступний або ще не надає метод dispatch Workboard, CLI відступає до dispatch лише за даними для локального стану Workboard. Dispatch лише за даними все ще може просувати залежності, очищати застарілі заявки та блокувати запуски, що вичерпали час очікування, але він не запускає працівників. Помилки автентифікації, дозволів, валідації та помилки для явної цілі `--url` або `--token` повідомляються напряму.

Текстовий вивід повідомляє про запуски працівників:

textCopy code
[code]
    dispatch complete: started=2 failures=0
[/code]

Вивід fallback явний:

textCopy code
[code]
    gateway unavailable; data dispatch only: promoted=1 blocked=0
[/code]

Вивід JSON містить результат dispatch. Dispatch через Gateway може містити `started` і `startFailures`; fallback лише за даними містить `gatewayUnavailable: true`. Токени заявок редагуються з JSON-виводу карток.

У панелі керування той самий результат dispatch показується як короткий підсумок, щоб оператор міг бачити, скільки карток запущено, просунуто, заблоковано, повторно заявлено або завершено з помилкою, не відкриваючи деталі картки.

## Паритет слеш-команд

Канали з підтримкою команд можуть використовувати відповідну слеш-команду:

textCopy code
[code]
    /workboard list/workboard show 7f4a2c10/workboard create Fix stale worker heartbeat/workboard dispatch
[/code]

Dispatch через слеш-команду також використовує runtime під¬агента Gateway, тож він дотримується тієї самої поведінки заявок, запуску працівників і помилок, що й шлях Gateway у панелі керування та CLI.

`/workboard list` і `/workboard show` — це команди читання для авторизованих відправників команд. `/workboard create` і `/workboard dispatch` змінюють стан дошки та потребують статусу власника на чат-поверхнях або клієнта Gateway з `operator.write` або `operator.admin`.

## Дозволи

Шлях dispatch у CLI викликає RPC Gateway з областями `operator.read` і `operator.write`. Токен Gateway лише для читання може переглядати дані Workboard через методи читання, але не може створювати картки або запускати dispatch працівників.

Локальні команди `list`, `create` і `show` працюють із локальним каталогом стану OpenClaw, який використовується поточним профілем. Використовуйте `--dev` або `--profile <name>` у команді верхнього рівня `openclaw`, коли потрібен інший корінь стану.

## Усунення несправностей

### Картки не з’являються

Підтвердьте, що Plugin увімкнено для того самого профілю та кореня стану:

bashCopy code
[code]
    openclaw plugins inspect workboard --runtime --json
[/code]

Якщо панель керування показує картки, а CLI ні, перевірте, що обидві команди використовують те саме налаштування `--dev` або `--profile`.

### Dispatch повідомляє про режим лише за даними

Запустіть або перезапустіть Gateway:

bashCopy code
[code]
    openclaw gateway restartopenclaw gateway status --deep
[/code]

Потім повторіть `openclaw workboard dispatch`. Fallback лише за даними корисний для локального очищення стану, але робочим запускам потрібен живий Gateway.

### Dispatch нічого не запускає

Перевірте наявність принаймні однієї картки `ready` без активної заявки:

bashCopy code
[code]
    openclaw workboard list --status ready
[/code]

Картки також можуть пропускатися, коли той самий власник уже має запущену роботу або роботу на перегляді. Перемістіть завершену роботу в `done`, звільніть застарілі заявки через інструменти Workboard або запустіть dispatch знову після завершення активного працівника.

## Пов’язане

  * [Workboard Plugin](</uk/plugins/workboard>)
  * [Довідник CLI](</uk/cli>)
  * [Слеш-команди](</uk/tools/slash-commands>)
  * [Control UI](</uk/web/control-ui>)


Was this useful?YesNo

Open issue