---
title: Создание Skills
source_url: https://docs.openclaw.ai/ru/tools/creating-skills
scraped_at: 2026-06-29
---

CapabilitiesSkills

Skills учат агента, как и когда использовать инструменты. Каждый Skill — это каталог, содержащий файл `SKILL.md` с YAML frontmatter и инструкциями в markdown. OpenClaw загружает Skills из нескольких корней в заданном [порядке приоритета](</ru/tools/skills#loading-order>).

## Создайте свой первый Skill

* ### Создайте каталог Skill

Skills находятся в папке `skills/` вашего рабочего пространства. Создайте каталог для нового Skill:

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace/skills/hello-world
[/code]

Для организации можно группировать Skills в подпапках — имя Skill всё равно задаётся frontmatter в `SKILL.md`, а не путём к папке:

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace/skills/personal/hello-world# skill name is still "hello-world", invoked as /hello-world
[/code]

* ### Напишите SKILL.md

Создайте `SKILL.md` внутри каталога. Frontmatter определяет метаданные; тело содержит инструкции для агента.

markdownCopy code
[code]
    ---name: hello-worlddescription: A simple skill that prints a greeting.--- # Hello World When the user asks for a greeting, use the `exec` tool to run: ```bashecho "Hello from your custom skill!"
[/code]

CodeCopy code
[code]
     Правила именования:- Используйте строчные буквы, цифры и дефисы для `name`.- Синхронизируйте имя каталога и `name` во frontmatter.- `description` показывается агенту и в обнаружении slash-команд —  оставляйте его в одну строку и короче 160 символов.  OPENCLAW_DOCS_MARKER:stepClose:   OPENCLAW_DOCS_MARKER:stepOpen:IHRpdGxlPSLQn9GA0L7QstC10YDRjNGC0LUsINGH0YLQviBTa2lsbCDQt9Cw0LPRgNGD0LbQtdC9Ig ```bashopenclaw skills list
[/code]

По умолчанию OpenClaw отслеживает файлы `SKILL.md` в корнях Skills. Если наблюдатель отключён или вы продолжаете существующую сессию, запустите новую, чтобы агент получил обновлённый список:

bashCopy code
[code]
    # From chat — archive current session and start fresh/new # Or restart the gatewayopenclaw gateway restart
[/code]

* ### Протестируйте его

Отправьте сообщение, которое должно активировать Skill:

bashCopy code
[code]
    openclaw agent --message "give me a greeting"
[/code]

Или откройте чат и спросите агента напрямую. Используйте `/skill hello-world`, чтобы вызвать его явно по имени.

## Справочник SKILL.md

### Обязательные поля

Поле | Описание  
---|---  
`name` | Уникальный slug из строчных букв, цифр и дефисов  
`description` | Однострочное описание, показываемое агенту и в выводе обнаружения  
  
### Необязательные ключи frontmatter

Поле | По умолчанию | Описание  
---|---|---  
`user-invocable` | `true` | Показывает Skill как пользовательскую slash-команду  
`disable-model-invocation` | `false` | Исключает Skill из системного prompt агента (он всё ещё запускается через `/skill`)  
`command-dispatch` | — | Установите `tool`, чтобы направить slash-команду напрямую в инструмент, обходя модель  
`command-tool` | — | Имя инструмента для вызова, когда задано `command-dispatch: tool`  
`command-arg-mode` | `raw` | Для диспетчеризации инструмента передаёт в инструмент необработанную строку аргументов  
`homepage` | — | URL, показываемый как "Website" в macOS UI Skills  
  
Поля ограничений (`requires.bins`, `requires.env` и т. д.) см. в [Skills — Ограничения](</ru/tools/skills#gating>).

### Использование `{baseDir}`

Используйте `{baseDir}` в теле Skill, чтобы ссылаться на файлы внутри каталога Skill без жёстко заданных путей:

markdownCopy code
[code]
    Run the helper script at `{baseDir}/scripts/run.sh`.
[/code]

## Добавление условной активации

Ограничьте Skill так, чтобы он загружался только при доступности его зависимостей:

markdownCopy code
[code]
    ---name: gemini-searchdescription: Search using Gemini CLI.metadata: { "openclaw": { "requires": { "bins": ["gemini"] }, "primaryEnv": "GEMINI_API_KEY" } }---
[/code]

Параметры ограничений

Ключ | Описание  
---|---  
`requires.bins` | Все бинарные файлы должны существовать в `PATH`  
`requires.anyBins` | Хотя бы один бинарный файл должен существовать в `PATH`  
`requires.env` | Каждая переменная env должна существовать в процессе или конфигурации  
`requires.config` | Каждый путь `openclaw.json` должен иметь truthy-значение  
`os` | Фильтр платформы: `["darwin"]`, `["linux"]`, `["win32"]`  
`always` | Установите `true`, чтобы пропустить все ограничения и всегда включать Skill  
  
Полный справочник: [Skills — Ограничения](</ru/tools/skills#gating>).

Переменные окружения и API-ключи

Привяжите API-ключ к записи Skill в `openclaw.json`:

json5Copy code
[code]
    {  skills: {    entries: {      "gemini-search": {        enabled: true,        apiKey: { source: "env", provider: "default", id: "GEMINI_API_KEY" },      },    },  },}
[/code]

Ключ внедряется в процесс хоста только на этот ход агента. Он не попадает в песочницу — см. [переменные env в песочнице](</ru/tools/skills-config#sandboxed-skills-and-env-vars>).

## Предложение через Skill Workshop

Для Skills, подготовленных агентом, или когда перед запуском Skill в работу нужен операторский review, используйте предложения [Skill Workshop](</ru/tools/skill-workshop>) вместо прямой записи `SKILL.md`.

bashCopy code
[code]
    # Propose a brand-new skillopenclaw skills workshop propose-create \  --name "hello-world" \  --description "A simple skill that prints a greeting." \  --proposal ./PROPOSAL.md # Propose an update to an existing skillopenclaw skills workshop propose-update hello-world \  --proposal ./PROPOSAL.md \  --description "Updated greeting skill"
[/code]

Используйте `--proposal-dir`, когда предложение включает вспомогательные файлы:

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name "hello-world" \  --description "A simple skill that prints a greeting." \  --proposal-dir ./hello-world-proposal/
[/code]

Каталог должен содержать `PROPOSAL.md`. Вспомогательные файлы можно размещать в `assets/`, `examples/`, `references/`, `scripts/` или `templates/`.

После review:

bashCopy code
[code]
    openclaw skills workshop inspect <proposal-id>openclaw skills workshop apply <proposal-id>
[/code]

Полный жизненный цикл предложения см. в [Skill Workshop](</ru/tools/skill-workshop>).

## Публикация в ClawHub

* ### Убедитесь, что ваш SKILL.md заполнен полностью

Убедитесь, что заданы `name`, `description` и все поля ограничений `metadata.openclaw`. Добавьте URL `homepage`, если у вас есть страница проекта.

* ### Установите Skill ClawHub

Skill ClawHub документирует текущую форму команды публикации и обязательные метаданные:

bashCopy code
[code]
    openclaw skills install @openclaw/clawhub-publish
[/code]

* ### Опубликуйте

bashCopy code
[code]
    clawhub publish
[/code]

Полный процесс см. в [ClawHub — Публикация](</ru/clawhub/publishing>).

## Рекомендации

## См. также

[**Справочник Skills** Порядок загрузки, ограничения, allowlists и формат SKILL.md. ](</ru/tools/skills>) [**Skill Workshop** Очередь предложений для Skills, подготовленных агентом. ](</ru/tools/skill-workshop>) [**Конфигурация Skills** Полная схема конфигурации `skills.*`. ](</ru/tools/skills-config>) [**ClawHub** Просматривайте и публикуйте Skills в публичном registry. ](</ru/clawhub>) [**Создание Plugins** Plugins могут поставлять Skills вместе с инструментами, которые они документируют. ](</ru/plugins/building-plugins>)

Was this useful?YesNo

Open issue