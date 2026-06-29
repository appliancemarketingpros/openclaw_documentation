---
title: Конфигурация Skills
source_url: https://docs.openclaw.ai/ru/tools/skills-config
scraped_at: 2026-06-29
---

CapabilitiesSkills

Большая часть конфигурации Skills находится в разделе `skills` в `~/.openclaw/openclaw.json`. Видимость для конкретного агента находится в `agents.defaults.skills` и `agents.list[].skills`.

json5Copy code
[code]
    {  skills: {    allowBundled: ["gemini", "peekaboo"],    load: {      extraDirs: ["~/Projects/agent-scripts/skills"],      allowSymlinkTargets: ["~/Projects/manager/skills"],      watch: true,      watchDebounceMs: 250,    },    install: {      preferBrew: true,      nodeManager: "npm",      allowUploadedArchives: false,    },    workshop: {      autonomous: { enabled: false },      allowSymlinkTargetWrites: false,      approvalPolicy: "pending",      maxPending: 50,      maxSkillBytes: 40000,    },    entries: {      "image-lab": {        enabled: true,        apiKey: { source: "env", provider: "default", id: "GEMINI_API_KEY" },        env: { GEMINI_API_KEY: "GEMINI_KEY_HERE" },      },      peekaboo: { enabled: true },      sag: { enabled: false },    },  },}
[/code]

## Загрузка (`skills.load`)

Дополнительные каталоги Skills для сканирования с самым низким приоритетом (после встроенных и Plugin Skills). Пути раскрываются с поддержкой `~`.

Доверенные реальные целевые каталоги, в которые могут указывать символьные ссылки папок Skills, даже если символьная ссылка находится вне настроенного корня. Используйте это для намеренных схем с соседними репозиториями, например `<workspace>/skills/manager -> ~/Projects/manager/skills`. Держите этот список узким — не указывайте широкие корни вроде `~` или `~/Projects`.

Отслеживать папки Skills и обновлять снимок Skills при изменении файлов `SKILL.md`. Покрывает вложенные файлы под сгруппированными корнями Skills.

Окно debounce для событий наблюдателя Skills в миллисекундах.

## Установка (`skills.install`)

Предпочитать установщики Homebrew, когда доступен `brew`.

Предпочитаемый менеджер пакетов Node для установок Skills. Это влияет только на установки Skills — среда выполнения Gateway всё равно должна использовать Node (Bun не рекомендуется для WhatsApp/Telegram). Используйте `openclaw setup --node-manager` для npm, pnpm или bun; задайте `"yarn"` вручную для установок Skills на базе Yarn.

Разрешить доверенным клиентам Gateway `operator.admin` устанавливать приватные zip-архивы, подготовленные через `skills.upload.*`. Обычным установкам ClawHub этот параметр не нужен.

## Политика установки оператора (`security.installPolicy`)

Используйте `security.installPolicy`, когда операторам нужна доверенная локальная команда для разрешения или блокировки установок Skills и plugins с политикой, специфичной для хоста. Политика выполняется после того, как OpenClaw подготовил исходные материалы, и до продолжения установки или обновления. Она применяется к ClawHub Skills, загруженным Skills, Git/локальным Skills, установщикам зависимостей Skills и источникам установки/обновления plugins.

json5Copy code
[code]
    {  security: {    installPolicy: {      enabled: true,      // Omit targets to cover every supported target.      targets: ["skill", "plugin"],      exec: {        source: "exec",        command: "/usr/local/bin/openclaw-install-policy",        args: ["--json"],        timeoutMs: 10000,        noOutputTimeoutMs: 10000,        maxOutputBytes: 1048576,        passEnv: ["OPENCLAW_STATE_DIR", "PATH"],        env: { POLICY_MODE: "strict" },        trustedDirs: ["/usr/local/bin"],      },    },  },}
[/code]

Включает политику установки, принадлежащую оператору. Если она включена без допустимой команды `exec`, установки завершаются закрытым отказом.

Необязательный фильтр целей. Если он опущен, политика применяется ко всем поддерживаемым целям, чтобы новые установки неожиданно не становились открытыми при сбое.

Абсолютный путь к доверенному исполняемому файлу политики. OpenClaw запускает его без shell и проверяет путь перед использованием.

Статические аргументы, передаваемые после `command`.

Максимальное реальное время выполнения для одного решения политики.

Максимальное время без вывода stdout или stderr, после которого политика завершается закрытым отказом.

Максимальное суммарное число байтов stdout и stderr, принимаемых от процесса политики.

Имена переменных окружения, копируемых из процесса OpenClaw в процесс политики. Передаются только именованные переменные.

Необязательный allowlist каталогов, которые могут содержать исполняемый файл политики.

Обходит проверки владельца и разрешений пути команды. Используйте только когда путь защищён другим механизмом.

Разрешает настроенному пути команды быть символьной ссылкой. Разрешённая цель всё равно должна проходить остальные проверки пути. Аргументы скрипта интерпретатора должны быть прямыми обычными файлами, а не символьными ссылками.

Политика получает один JSON-объект на stdin с `protocolVersion: 1`, `openclawVersion`, `targetType`, `targetName`, `sourcePath`, `sourcePathKind`, необязательным структурированным `source`, структурированными `origin` и `request`. Она должна записать один JSON-объект в stdout: `{ "protocolVersion": 1, "decision": "allow" }` или `{ "protocolVersion": 1, "decision": "block", "reason": "..." }`. Ненулевой код выхода, timeout, некорректный JSON, отсутствующие поля или неподдерживаемые версии протокола завершаются закрытым отказом.

OpenClaw не выполняет политику установки во время обычного запуска Gateway. Установки и обновления завершаются закрытым отказом, когда политика включена, но недоступна. `openclaw doctor` выполняет статическую проверку, а `openclaw doctor --deep` запускает синтетическую проверку установки для настроенной команды.

Массовые обновления применяют политику к каждой цели: заблокированное обновление Skills или plugin завершает эту цель с ошибкой, не отключая политику и не пропуская последующие цели в пакете.

Пример stdin:

jsonCopy code
[code]
    {  "protocolVersion": 1,  "openclawVersion": "2026.6.1",  "targetType": "skill",  "targetName": "weather",  "sourcePath": "/var/folders/.../openclaw-skill-clawhub/root",  "sourcePathKind": "directory",  "source": {    "kind": "clawhub",    "authority": "openclaw",    "mutable": false,    "network": true  },  "origin": {    "type": "clawhub",    "registry": "https://clawhub.openclaw.ai",    "slug": "weather",    "version": "1.0.0"  },  "request": {    "kind": "skill-install",    "mode": "install",    "requestedSpecifier": "clawhub:weather@1.0.0"  },  "skill": {    "installId": "clawhub"  }}
[/code]

Минимальная команда политики:

jsCopy code
[code]
    #!/usr/bin/env node let input = "";process.stdin.setEncoding("utf8");process.stdin.on("data", (chunk) => {  input += chunk;});process.stdin.on("end", () => {  const request = JSON.parse(input);  if (request.targetType === "plugin" && request.source?.kind === "local-path") {    process.stdout.write(      JSON.stringify({        protocolVersion: 1,        decision: "block",        reason: "local plugin paths are not approved on this host",      }),    );    return;  }  process.stdout.write(JSON.stringify({ protocolVersion: 1, decision: "allow" }));});
[/code]

## Allowlist встроенных Skills

Необязательный allowlist только для **встроенных** Skills. Если задан, доступны только встроенные Skills из списка. Управляемые Skills, Skills уровня агента и рабочей области не затрагиваются.

## Записи отдельных Skills (`skills.entries`)

Ключи в `entries` по умолчанию соответствуют `name` Skills. Если Skills задаёт `metadata.openclaw.skillKey`, используйте этот ключ вместо него. Имена с дефисами берутся в кавычки (JSON5 допускает ключи в кавычках).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNraWxscy5lbnRyaWVzLjxrZXk .enabled" type="boolean"> `false` отключает Skills, даже если он встроен или установлен. Встроенный Skills `coding-agent` является opt-in — задайте для него `true` и убедитесь, что один из `claude`, `codex`, `opencode` или другой поддерживаемый CLI установлен и аутентифицирован.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNraWxscy5lbnRyaWVzLjxrZXk .apiKey" type='string | { source, provider, id }'> Удобное поле для Skills, которые объявляют `metadata.openclaw.primaryEnv`. Поддерживает строку в открытом виде или SecretRef: `{ source: "env", provider: "default", id: "VAR_NAME" }`.

## Agent allowlists (`agents`)

Используйте конфигурацию агента, когда нужны одни и те же корни Skills для машины/рабочей области, но разный видимый набор Skills для каждого агента.

json5Copy code
[code]
    {  agents: {    defaults: {      skills: ["github", "weather"], // shared baseline    },    list: [      { id: "writer" }, // inherits github, weather      { id: "docs", skills: ["docs-search"] }, // replaces defaults entirely      { id: "locked-down", skills: [] }, // no skills    ],  },}
[/code]

Общий базовый allowlist, наследуемый агентами, у которых отсутствует `agents.list[].skills`. Полностью опустите, чтобы Skills по умолчанию оставались неограниченными.

Явный итоговый набор Skills для этого агента. Явные списки **заменяют** наследуемые значения по умолчанию — они не объединяются. Задайте `[]`, чтобы не показывать Skills этому агенту.

## Workshop (`skills.workshop`)

Когда `true`, агенты могут создавать ожидающие предложения из долговечных сигналов беседы после успешных ходов. Создание Skills по запросу пользователя всегда проходит через Skill Workshop независимо от этого параметра.

`pending` требует одобрения оператора перед инициированными агентом apply, reject или quarantine. `auto` разрешает эти действия без одобрения.

Разрешить Skill Workshop apply выполнять запись через символьные ссылки Skills рабочей области, реальная цель которых уже доверена через `skills.load.allowSymlinkTargets`. Оставляйте это отключённым, если применение сгенерированного предложения не должно изменять этот общий корень Skills.

Максимальное число ожидающих и помещенных в карантин предложений, сохраняемых для каждой рабочей области.

Максимальный размер тела предложения в байтах. Описания предложений жестко ограничены 160 байтами, потому что они отображаются в выводе обнаружения и списка.

## Корни навыков с символьными ссылками

По умолчанию корни навыков рабочей области, проектного агента, дополнительных каталогов и встроенных навыков являются границами изоляции. Папка навыка с символьной ссылкой внутри `<workspace>/skills`, которая разрешается за пределы корня, пропускается с сообщением в журнале.

Чтобы разрешить намеренную схему с символьными ссылками, объявите доверенную цель:

json5Copy code
[code]
    {  skills: {    load: {      extraDirs: ["~/Projects/manager/skills"],      allowSymlinkTargets: ["~/Projects/manager/skills"],    },  },}
[/code]

С этой конфигурацией `<workspace>/skills/manager -> ~/Projects/manager/skills` принимается после разрешения realpath. `extraDirs` сканирует соседний репозиторий напрямую; `allowSymlinkTargets` сохраняет путь с символьной ссылкой для существующих схем.

Применение Skill Workshop по умолчанию не записывает через эти символьные ссылки. Чтобы разрешить Workshop apply изменять навыки в уже доверенных целях символьных ссылок, включите это отдельно:

json5Copy code
[code]
    {  skills: {    load: {      allowSymlinkTargets: ["~/Projects/manager/skills"],    },    workshop: {      allowSymlinkTargetWrites: true,    },  },}
[/code]

Управляемые каталоги `~/.openclaw/skills` и личные каталоги `~/.agents/skills` уже принимают символьные ссылки на каталоги навыков (изоляция per-skill `SKILL.md` по-прежнему применяется).

## Навыки в песочнице и переменные окружения

Передайте секреты в песочницу Docker с помощью:

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        docker: {          env: { GEMINI_API_KEY: "your-key-here" },        },      },    },  },}
[/code]

## Напоминание о порядке загрузки

textCopy code
[code]
    workspace/skills      (highest)workspace/.agents/skills~/.agents/skills~/.openclaw/skillsbundled skillsskills.load.extraDirs (lowest)
[/code]

Изменения навыков и конфигурации вступают в силу в следующем новом сеансе, если наблюдатель включен, или на следующем ходе агента, когда наблюдатель обнаружит изменение.

## Связанные материалы

[**Skills reference** Что такое навыки, порядок загрузки, ограничения доступа и формат SKILL.md. ](</ru/tools/skills>) [**Creating skills** Создание пользовательских навыков рабочей области. ](</ru/tools/creating-skills>) [**Skill Workshop** Очередь предложений для навыков, подготовленных агентом. ](</ru/tools/skill-workshop>) [**Slash commands** Нативный каталог слеш-команд и директивы чата. ](</ru/tools/slash-commands>)

Was this useful?YesNo

Open issue