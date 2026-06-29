---
title: Практикум по Skills
source_url: https://docs.openclaw.ai/ru/tools/skill-workshop
scraped_at: 2026-06-29
---

CapabilitiesSkills

Skill Workshop — это управляемый путь OpenClaw для создания и обновления навыков рабочей области.

Агенты и операторы не записывают активные файлы `SKILL.md` напрямую через этот путь. Сначала они создают **предложение**. Предложение — это ожидающий черновик, содержащий предлагаемое содержимое навыка, целевую привязку, состояние сканера, хэши, метаданные вспомогательных файлов и метаданные отката. Оно становится действующим навыком только после применения.

Skill Workshop записывает только навыки рабочей области. Он не изменяет встроенные, Plugin, ClawHub, дополнительные корневые, управляемые, личные агентские или системные навыки.

## Как это работает

  * **Сначала предложение:** сгенерированное содержимое навыка сохраняется как `PROPOSAL.md`, а не `SKILL.md`.
  * **Применение — единственная живая запись:** создание, обновление и доработка не изменяют активные навыки.
  * **Ограничено рабочей областью:** создание нацелено на корень `skills/` рабочей области. Обновления разрешены только для доступных на запись навыков рабочей области.
  * **Без перезаписи:** создание завершается ошибкой, если целевой навык уже существует.
  * **Привязано к хэшу:** предложения обновления привязываются к текущему целевому хэшу и становятся устаревшими, если действующий навык меняется до применения.
  * **Ограничено сканером:** перед записью применение повторно запускает сканирование.
  * **Восстановимо:** перед изменением действующих файлов применение записывает метаданные отката.
  * **Согласованные поверхности:** чат, CLI и Gateway вызывают один и тот же сервис Skill Workshop.


## Жизненный цикл

textCopy code
[code]
    create/update -> pendingrevise        -> pendingapply         -> appliedreject        -> rejectedquarantine    -> quarantinedtarget change -> stale
[/code]

Только предложения в статусе `pending` можно дорабатывать, применять, отклонять или помещать в карантин.

## Чат

Попросите агента создать нужный вам навык. Агент вызывает `skill_workshop` и возвращает идентификатор предложения.

Создание:

textCopy code
[code]
    Make a skill called morning-catchup that runs my Monday inbox routine.
[/code]

Обновление существующего навыка рабочей области:

textCopy code
[code]
    Update trip-planning to also check seat maps before booking.
[/code]

Итерация по ожидающему предложению:

textCopy code
[code]
    Show me the morning-catchup proposal.Revise it to also flag anything marked urgent.Apply the morning-catchup proposal.
[/code]

По умолчанию инициированные агентом `apply`, `reject` и `quarantine` показывают запрос подтверждения перед запуском. Установите `skills.workshop.approvalPolicy` в `"auto"`, чтобы пропускать запрос в доверенных средах.

## CLI

Создать новое предложение навыка:

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name morning-catchup \  --description "Daily inbox catch-up: triage, archive, surface, draft, plan" \  --proposal ./PROPOSAL.md
[/code]

Создать предложение обновления для существующего навыка рабочей области:

bashCopy code
[code]
    openclaw skills workshop propose-update trip-planning --proposal ./PROPOSAL.md
[/code]

Список и просмотр:

bashCopy code
[code]
    openclaw skills workshop listopenclaw skills workshop inspect <proposal-id>
[/code]

Доработка перед утверждением:

bashCopy code
[code]
    openclaw skills workshop revise <proposal-id> --proposal ./PROPOSAL.md
[/code]

Завершить работу с предложением:

bashCopy code
[code]
    openclaw skills workshop apply <proposal-id>openclaw skills workshop reject <proposal-id> --reason "Duplicate"openclaw skills workshop quarantine <proposal-id> --reason "Needs security review"
[/code]

## Содержимое предложения

Пока предложение ожидает обработки, оно хранится как `PROPOSAL.md` с frontmatter только для предложения:

markdownCopy code
[code]
    ---name: "morning-catchup"description: "Daily inbox catch-up: triage, archive, surface, draft, plan"status: proposalversion: "v1"date: "2026-05-30T00:00:00.000Z"---
[/code]

При применении Skill Workshop записывает активный `SKILL.md` и удаляет поля, относящиеся только к предложению: `status`, `version` предложения и `date` предложения.

## Вспомогательные файлы

Используйте `--proposal-dir`, когда предлагаемому навыку нужны файлы рядом с `PROPOSAL.md`:

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name weekly-update \  --description "Friday wrap-up: stats, highlights, next week's top three" \  --proposal-dir ./weekly-update-proposal
[/code]

Каталог должен содержать `PROPOSAL.md`. Вспомогательные файлы должны находиться в:

  * `assets/`
  * `examples/`
  * `references/`
  * `scripts/`
  * `templates/`


Skill Workshop сканирует, хэширует и сохраняет вспомогательные файлы вместе с предложением. Они записываются рядом с действующим `SKILL.md` только при применении.

Отклоняемые пути вспомогательных файлов включают абсолютные пути, скрытые сегменты пути, обход каталогов, пересекающиеся пути, исполняемые файлы из каталогов предложений, текст не в UTF-8, нулевые байты и файлы вне стандартных вспомогательных папок.

## Инструмент агента

Модель использует `skill_workshop`:

textCopy code
[code]
    action: create | update | revise | list | inspect | apply | reject | quarantine
[/code]

Агенты должны использовать `skill_workshop` для сгенерированной работы с навыками. Они не должны создавать или изменять файлы предложений через `write`, `edit`, `exec`, команды shell или прямые операции файловой системы.

## Утверждение и автономность

json5Copy code
[code]
    {  skills: {    workshop: {      autonomous: {        enabled: false,      },      allowSymlinkTargetWrites: false,      approvalPolicy: "pending",      maxPending: 50,      maxSkillBytes: 40000,    },  },}
[/code]

  * `autonomous.enabled`: позволяет OpenClaw создавать ожидающие предложения из устойчивых сигналов разговора после успешных ходов. По умолчанию: `false`.
  * `allowSymlinkTargetWrites`: позволяет применению записывать через symlink навыков рабочей области, реальная цель которых указана в `skills.load.allowSymlinkTargets`. По умолчанию: `false`.
  * `approvalPolicy: "pending"`: требует запроса подтверждения перед инициированными агентом `apply`, `reject` или `quarantine`.
  * `approvalPolicy: "auto"`: пропускает этот запрос подтверждения. Агент все равно должен вызвать действие.
  * `maxPending`: ограничивает ожидающие и помещенные в карантин предложения на рабочую область.
  * `maxSkillBytes`: ограничивает размер тела предложения. По умолчанию: `40000`.


Описания предложений всегда ограничены 160 байтами.

## Методы Gateway

textCopy code
[code]
    skills.proposals.listskills.proposals.inspectskills.proposals.createskills.proposals.updateskills.proposals.reviseskills.proposals.applyskills.proposals.rejectskills.proposals.quarantine
[/code]

Методы только для чтения требуют `operator.read`. Изменяющие методы требуют `operator.admin`.

## Хранилище

textCopy code
[code]
    &lt;OPENCLAW_STATE_DIR&gt;/skill-workshop/  proposals.json  proposals/<proposal-id>/    proposal.json    PROPOSAL.md    rollback.json    assets/    examples/    references/    scripts/    templates/
[/code]

Каталог состояния по умолчанию: `~/.openclaw`.

  * `proposal.json`: каноническая запись предложения.
  * `proposals.json`: быстрый индекс списка, восстанавливаемый из папок предложений.
  * `PROPOSAL.md`: ожидающее предложение навыка.
  * `rollback.json`: метаданные восстановления, записываемые перед тем, как применение изменит действующие файлы.


## Ограничения

  * Описание: 160 байт.
  * Тело предложения: `skills.workshop.maxSkillBytes` (по умолчанию 40 000).
  * Вспомогательные файлы: 64 на предложение.
  * Размер вспомогательного файла: 256 КБ каждый, всего 2 МБ.
  * Ожидающие и помещенные в карантин предложения: `skills.workshop.maxPending` на рабочую область (по умолчанию 50).


## Устранение неполадок

Проблема | Решение  
---|---  
`Skill proposal description is too large` | Сократите `description` до 160 байт или меньше.  
`Skill proposal content is too large` | Сократите тело предложения или увеличьте `skills.workshop.maxSkillBytes`.  
`Target skill changed after proposal creation` | Доработайте предложение относительно текущей цели или создайте новое предложение.  
`Proposal scan failed` | Изучите результаты сканера, затем доработайте предложение или поместите его в карантин.  
`untrusted symlink target` | Настраивайте `skills.load.allowSymlinkTargets` и включайте `skills.workshop.allowSymlinkTargetWrites` только для намеренно используемых общих корней навыков.  
`Support file paths must be under one of...` | Переместите вспомогательные файлы в `assets/`, `examples/`, `references/`, `scripts/` или `templates/`.  
Предложение не отображается в списке | Проверьте выбранную рабочую область `--agent` и `OPENCLAW_STATE_DIR`.  
Агент не может вызвать `skill_workshop` | Проверьте активную политику инструментов и режим запуска. `coding` включает инструмент; ограничительные политики `tools.allow` должны явно перечислять его, а запуски в sandbox должны использовать обычную хостовую сессию агента или CLI.  
  
## Связанные материалы

  * [Skills](</ru/tools/skills>) для порядка загрузки, приоритета и видимости
  * [Создание навыков](</ru/tools/creating-skills>) для основ написанного вручную `SKILL.md`
  * [Конфигурация Skills](</ru/tools/skills-config>) для полной схемы `skills.workshop`
  * [CLI Skills](</ru/cli/skills>) для команд `openclaw skills`


Was this useful?YesNo

Open issue