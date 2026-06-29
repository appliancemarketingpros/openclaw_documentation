---
title: Майстерня навичок
source_url: https://docs.openclaw.ai/uk/tools/skill-workshop
scraped_at: 2026-06-29
---

CapabilitiesSkills

Skill Workshop — це керований шлях OpenClaw для створення й оновлення Skills робочого простору.

Агенти й оператори не записують активні файли `SKILL.md` напряму через цей шлях. Спочатку вони створюють **пропозицію**. Пропозиція — це чернетка в очікуванні, що містить запропонований вміст skill, цільову прив’язку, стан сканера, хеші, метадані допоміжних файлів і метадані відкоту. Вона стає live skill лише після застосування.

Skill Workshop записує лише Skills робочого простору. Він не змінює bundled, plugin, ClawHub, extra-root, managed, personal-agent або system skills.

## Як це працює

  * **Спочатку пропозиція:** згенерований вміст skill зберігається як `PROPOSAL.md`, а не `SKILL.md`.
  * **Застосування — єдиний live-запис:** create, update і revise не змінюють активні Skills.
  * **У межах робочого простору:** створення націлені на корінь `skills/` робочого простору. Оновлення дозволені лише для доступних для запису Skills робочого простору.
  * **Без перезапису:** create завершується помилкою, якщо цільовий skill уже існує.
  * **Прив’язка до хешу:** update-пропозиції прив’язуються до поточного хешу цілі й стають застарілими, якщо live skill змінюється до застосування.
  * **Захист сканером:** apply повторно запускає сканування перед записом.
  * **Можливість відновлення:** apply записує метадані відкоту перед зміною live-файлів.
  * **Узгоджені поверхні:** чат, CLI і Gateway усі викликають той самий сервіс Skill Workshop.


## Життєвий цикл

textCopy code
[code]
    create/update -> pendingrevise        -> pendingapply         -> appliedreject        -> rejectedquarantine    -> quarantinedtarget change -> stale
[/code]

Лише пропозиції `pending` можна переглядати, застосовувати, відхиляти або поміщати в карантин.

## Чат

Попросіть агента про потрібний skill. Агент викликає `skill_workshop` і повертає ідентифікатор пропозиції.

Створення:

textCopy code
[code]
    Make a skill called morning-catchup that runs my Monday inbox routine.
[/code]

Оновлення наявного skill робочого простору:

textCopy code
[code]
    Update trip-planning to also check seat maps before booking.
[/code]

Ітерація над пропозицією в очікуванні:

textCopy code
[code]
    Show me the morning-catchup proposal.Revise it to also flag anything marked urgent.Apply the morning-catchup proposal.
[/code]

За замовчуванням ініційовані агентом `apply`, `reject` і `quarantine` показують запит на схвалення перед виконанням. Установіть `skills.workshop.approvalPolicy` на `"auto"`, щоб пропустити запит у довірених середовищах.

## CLI

Створити нову пропозицію skill:

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name morning-catchup \  --description "Daily inbox catch-up: triage, archive, surface, draft, plan" \  --proposal ./PROPOSAL.md
[/code]

Створити пропозицію оновлення для наявного skill робочого простору:

bashCopy code
[code]
    openclaw skills workshop propose-update trip-planning --proposal ./PROPOSAL.md
[/code]

Список і перегляд:

bashCopy code
[code]
    openclaw skills workshop listopenclaw skills workshop inspect <proposal-id>
[/code]

Переглянути перед схваленням:

bashCopy code
[code]
    openclaw skills workshop revise <proposal-id> --proposal ./PROPOSAL.md
[/code]

Закрити пропозицію:

bashCopy code
[code]
    openclaw skills workshop apply <proposal-id>openclaw skills workshop reject <proposal-id> --reason "Duplicate"openclaw skills workshop quarantine <proposal-id> --reason "Needs security review"
[/code]

## Вміст пропозиції

Поки пропозиція в очікуванні, вона зберігається як `PROPOSAL.md` з frontmatter лише для пропозиції:

markdownCopy code
[code]
    ---name: "morning-catchup"description: "Daily inbox catch-up: triage, archive, surface, draft, plan"status: proposalversion: "v1"date: "2026-05-30T00:00:00.000Z"---
[/code]

Під час застосування Skill Workshop записує активний `SKILL.md` і видаляє поля лише для пропозиції: `status`, proposal `version` і proposal `date`.

## Допоміжні файли

Використовуйте `--proposal-dir`, коли запропонованому skill потрібні файли поруч із `PROPOSAL.md`:

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name weekly-update \  --description "Friday wrap-up: stats, highlights, next week's top three" \  --proposal-dir ./weekly-update-proposal
[/code]

Каталог має містити `PROPOSAL.md`. Допоміжні файли мають бути в:

  * `assets/`
  * `examples/`
  * `references/`
  * `scripts/`
  * `templates/`


Skill Workshop сканує, хешує та зберігає допоміжні файли разом із пропозицією. Вони записуються поруч із live `SKILL.md` лише під час застосування.

Відхилені шляхи допоміжних файлів включають абсолютні шляхи, приховані сегменти шляху, path traversal, шляхи, що перекриваються, виконувані файли з каталогів пропозицій, текст не у UTF-8, null-байти й файли поза стандартними папками допоміжних файлів.

## Інструмент агента

Модель використовує `skill_workshop`:

textCopy code
[code]
    action: create | update | revise | list | inspect | apply | reject | quarantine
[/code]

Агенти мають використовувати `skill_workshop` для згенерованої роботи зі Skills. Вони не повинні створювати або змінювати файли пропозицій через `write`, `edit`, `exec`, команди оболонки чи прямі операції з файловою системою.

## Схвалення й автономність

json5Copy code
[code]
    {  skills: {    workshop: {      autonomous: {        enabled: false,      },      allowSymlinkTargetWrites: false,      approvalPolicy: "pending",      maxPending: 50,      maxSkillBytes: 40000,    },  },}
[/code]

  * `autonomous.enabled`: дозволяє OpenClaw створювати пропозиції в очікуванні з durable signals розмови після успішних ходів. За замовчуванням: `false`.
  * `allowSymlinkTargetWrites`: дозволяє apply записувати через symlink Skills робочого простору, реальна ціль яких указана в `skills.load.allowSymlinkTargets`. За замовчуванням: `false`.
  * `approvalPolicy: "pending"`: вимагає запиту на схвалення перед ініційованими агентом `apply`, `reject` або `quarantine`.
  * `approvalPolicy: "auto"`: пропускає цей запит на схвалення. Агент усе одно має викликати дію.
  * `maxPending`: обмежує кількість пропозицій у стані pending і quarantined для кожного робочого простору.
  * `maxSkillBytes`: обмежує розмір тіла пропозиції. За замовчуванням: `40000`.


Описи пропозицій завжди обмежені 160 байтами.

## Методи Gateway

textCopy code
[code]
    skills.proposals.listskills.proposals.inspectskills.proposals.createskills.proposals.updateskills.proposals.reviseskills.proposals.applyskills.proposals.rejectskills.proposals.quarantine
[/code]

Методи лише для читання потребують `operator.read`. Методи, що змінюють дані, потребують `operator.admin`.

## Сховище

textCopy code
[code]
    &lt;OPENCLAW_STATE_DIR&gt;/skill-workshop/  proposals.json  proposals/<proposal-id>/    proposal.json    PROPOSAL.md    rollback.json    assets/    examples/    references/    scripts/    templates/
[/code]

Каталог стану за замовчуванням: `~/.openclaw`.

  * `proposal.json`: канонічний запис пропозиції.
  * `proposals.json`: швидкий індекс списку, який можна перебудувати з папок пропозицій.
  * `PROPOSAL.md`: пропозиція skill в очікуванні.
  * `rollback.json`: метадані відновлення, записані перед тим, як apply змінює live-файли.


## Обмеження

  * Опис: 160 байтів.
  * Тіло пропозиції: `skills.workshop.maxSkillBytes` (за замовчуванням 40 000).
  * Допоміжні файли: 64 на пропозицію.
  * Розмір допоміжного файлу: 256 КБ кожен, 2 МБ загалом.
  * Пропозиції в стані pending і quarantined: `skills.workshop.maxPending` на робочий простір (за замовчуванням 50).


## Усунення несправностей

Проблема | Рішення  
---|---  
`Skill proposal description is too large` | Скоротіть `description` до 160 байтів або менше.  
`Skill proposal content is too large` | Скоротіть тіло пропозиції або збільште `skills.workshop.maxSkillBytes`.  
`Target skill changed after proposal creation` | Перегляньте пропозицію відносно поточної цілі або створіть нову пропозицію.  
`Proposal scan failed` | Перевірте знахідки сканера, потім перегляньте або помістіть пропозицію в карантин.  
`untrusted symlink target` | Налаштуйте `skills.load.allowSymlinkTargets` і вмикайте `skills.workshop.allowSymlinkTargetWrites` лише для навмисно спільних коренів Skills.  
`Support file paths must be under one of...` | Перемістіть допоміжні файли в `assets/`, `examples/`, `references/`, `scripts/` або `templates/`.  
Пропозиція не відображається у списку | Перевірте вибраний робочий простір `--agent` і `OPENCLAW_STATE_DIR`.  
Агент не може викликати `skill_workshop` | Перевірте активну політику інструментів і режим запуску. `coding` включає інструмент; обмежувальні політики `tools.allow` мають явно його перелічувати, а sandboxed-запуски мають використовувати звичайну host-side сесію агента або CLI.  
  
## Пов’язане

  * [Skills](</uk/tools/skills>) для порядку завантаження, пріоритету та видимості
  * [Створення Skills](</uk/tools/creating-skills>) для основ рукописного `SKILL.md`
  * [Конфігурація Skills](</uk/tools/skills-config>) для повної схеми `skills.workshop`
  * [CLI Skills](</uk/cli/skills>) для команд `openclaw skills`


Was this useful?YesNo

Open issue