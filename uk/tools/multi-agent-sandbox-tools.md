---
title: Багатоагентна пісочниця та інструменти
source_url: https://docs.openclaw.ai/uk/tools/multi-agent-sandbox-tools
scraped_at: 2026-05-25
---

Кожен агент у багатоагентному налаштуванні може перевизначати глобальні політики пісочниці та інструментів. На цій сторінці описано конфігурацію для окремих агентів, правила пріоритету та приклади.

[**Пісочниця** Бекенди та режими — повна довідка з пісочниці. ](</uk/gateway/sandboxing>) [**Пісочниця, політика інструментів і підвищений режим** Налагодження: «чому це заблоковано?» ](</uk/gateway/sandbox-vs-tool-policy-vs-elevated>) [**Підвищений режим** Підвищений exec для довірених відправників. ](</uk/tools/elevated>)

* * *

## Приклади конфігурації

Приклад 1: особистий агент + обмежений сімейний агент jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "name": "Personal Assistant",        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      },      {        "id": "family",        "name": "Family Bot",        "workspace": "~/.openclaw/workspace-family",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read", "message"],          "deny": ["exec", "write", "edit", "apply_patch", "process", "browser"],          "message": {            "crossContext": {              "allowWithinProvider": false,              "allowAcrossProviders": false            }          }        }      }    ]  },  "bindings": [    {      "agentId": "family",      "match": {        "provider": "whatsapp",        "accountId": "*",        "peer": {          "kind": "group",          "id": "120363424282127706@g.us"        }      }    }  ]}
[/code]

**Результат:**

  * агент `main`: працює на хості, повний доступ до інструментів.
  * агент `family`: працює в Docker (один контейнер на агента), лише `read` і надсилання повідомлень у поточній розмові.

Приклад 2: робочий агент зі спільною пісочницею jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "personal",        "workspace": "~/.openclaw/workspace-personal",        "sandbox": { "mode": "off" }      },      {        "id": "work",        "workspace": "~/.openclaw/workspace-work",        "sandbox": {          "mode": "all",          "scope": "shared",          "workspaceRoot": "/tmp/work-sandboxes"        },        "tools": {          "allow": ["read", "write", "apply_patch", "exec"],          "deny": ["browser", "gateway", "discord"]        }      }    ]  }}
[/code]

Приклад 2b: глобальний профіль кодування + агент лише для повідомлень jsonCopy code
[code]
    {  "tools": { "profile": "coding" },  "agents": {    "list": [      {        "id": "support",        "tools": { "profile": "messaging", "allow": ["slack"] }      }    ]  }}
[/code]

**Результат:**

  * типові агенти отримують інструменти для кодування.
  * агент `support` призначений лише для повідомлень (+ інструмент Slack).

Приклад 3: різні режими пісочниці для кожного агента jsonCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "non-main",        "scope": "session"      }    },    "list": [      {        "id": "main",        "workspace": "~/.openclaw/workspace",        "sandbox": {          "mode": "off"        }      },      {        "id": "public",        "workspace": "~/.openclaw/workspace-public",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read"],          "deny": ["exec", "write", "edit", "apply_patch"]        }      }    ]  }}
[/code]

* * *

## Пріоритет конфігурації

Коли існують і глобальні (`agents.defaults.*`), і специфічні для агента (`agents.list[].*`) конфігурації:

### Конфігурація пісочниці

Параметри конкретного агента перевизначають глобальні:

CodeCopy code
[code]
    agents.list[].sandbox.mode > agents.defaults.sandbox.modeagents.list[].sandbox.scope > agents.defaults.sandbox.scopeagents.list[].sandbox.workspaceRoot > agents.defaults.sandbox.workspaceRootagents.list[].sandbox.workspaceAccess > agents.defaults.sandbox.workspaceAccessagents.list[].sandbox.docker.* > agents.defaults.sandbox.docker.*agents.list[].sandbox.browser.* > agents.defaults.sandbox.browser.*agents.list[].sandbox.prune.* > agents.defaults.sandbox.prune.*
[/code]

### Обмеження інструментів

Порядок фільтрації такий:

* ### Профіль інструментів

`tools.profile` або `agents.list[].tools.profile`.

* ### Профіль інструментів провайдера

`tools.byProvider[provider].profile` або `agents.list[].tools.byProvider[provider].profile`.

* ### Глобальна політика інструментів

`tools.allow` / `tools.deny`.

* ### Політика інструментів провайдера

`tools.byProvider[provider].allow/deny`.

* ### Політика інструментів конкретного агента

`agents.list[].tools.allow/deny`.

* ### Політика провайдера агента

`agents.list[].tools.byProvider[provider].allow/deny`.

* ### Політика інструментів пісочниці

`tools.sandbox.tools` або `agents.list[].tools.sandbox.tools`.

* ### Політика інструментів субагента

`tools.subagents.tools`, якщо застосовно.

Правила пріоритету

  * Кожен рівень може додатково обмежувати інструменти, але не може знову дозволити інструменти, заборонені на попередніх рівнях.
  * Якщо задано `agents.list[].tools.sandbox.tools`, воно замінює `tools.sandbox.tools` для цього агента.
  * Якщо задано `agents.list[].tools.profile`, воно перевизначає `tools.profile` для цього агента.
  * Ключі інструментів провайдера приймають або `provider` (наприклад, `google-antigravity`), або `provider/model` (наприклад, `openai/gpt-5.4`).

Поведінка порожнього allowlist

Якщо будь-який явний allowlist у цьому ланцюжку залишає запуск без доступних для виклику інструментів, OpenClaw зупиняється до надсилання prompt до моделі. Це навмисно: агент, налаштований із відсутнім інструментом, як-от `agents.list[].tools.allow: ["query_db"]`, має явно завершитися помилкою, доки не буде ввімкнено Plugin, що реєструє `query_db`, а не продовжувати як агент лише для тексту.

Політики інструментів підтримують скорочення `group:*`, які розгортаються в кілька інструментів. Повний список див. у [Групи інструментів](</uk/gateway/sandbox-vs-tool-policy-vs-elevated#tool-groups-shorthands>).

Перевизначення підвищеного режиму для окремих агентів (`agents.list[].tools.elevated`) можуть додатково обмежувати підвищений exec для конкретних агентів. Докладніше див. у [Підвищений режим](</uk/tools/elevated>).

* * *

## Міграція з одного агента

### До (один агент)

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "workspace": "~/.openclaw/workspace",      "sandbox": {        "mode": "non-main"      }    }  },  "tools": {    "sandbox": {      "tools": {        "allow": ["read", "write", "apply_patch", "exec"],        "deny": []      }    }  }}
[/code]

### Після (multi-agent)

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      }    ]  }}
[/code]

* * *

## Приклади обмеження інструментів

### Агент лише для читання

jsonCopy code
[code]
    {  "tools": {    "allow": ["read"],    "deny": ["exec", "write", "edit", "apply_patch", "process"]  }}
[/code]

### Виконання оболонки з вимкненими інструментами файлової системи

jsonCopy code
[code]
    {  "tools": {    "allow": ["read", "exec", "process"],    "deny": ["write", "edit", "apply_patch", "browser", "gateway"]  }}
[/code]

### Лише комунікація

jsonCopy code
[code]
    {  "tools": {    "sessions": { "visibility": "tree" },    "allow": ["sessions_list", "sessions_send", "sessions_history", "session_status"],    "deny": ["exec", "write", "edit", "apply_patch", "read", "browser"]  }}
[/code]

`sessions_history` у цьому профілі все одно повертає обмежений, очищений вигляд пригадування, а не необроблений дамп транскрипту. Пригадування асистента видаляє теги мислення, каркас `<relevant-memories>`, XML-навантаження викликів інструментів у звичайному тексті (зокрема `<tool_call>...</tool_call>`, `<function_call>...</function_call>`, `<tool_calls>...</tool_calls>`, `<function_calls>...</function_calls>` і обрізані блоки викликів інструментів), понижений каркас викликів інструментів, витеклі ASCII/повноширинні керівні токени моделі та некоректний XML викликів інструментів MiniMax перед редагуванням/обрізанням.

* * *

## Поширена помилка: "non-main"

* * *

## Тестування

Після налаштування пісочниці та інструментів для multi-agent:

* ### Перевірте визначення агента

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

* ### Перевірте контейнери пісочниці

bashCopy code
[code]
    docker ps --filter "name=openclaw-sbx-"
[/code]

* ### Протестуйте обмеження інструментів

  * Надішліть повідомлення, яке потребує обмежених інструментів.
  * Переконайтеся, що агент не може використовувати заборонені інструменти.


* ### Відстежуйте журнали

bashCopy code
[code]
    tail -f "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/logs/gateway.log" | grep -E "routing|sandbox|tools"
[/code]

* * *

## Усунення несправностей

Агент не ізольований у пісочниці попри `mode: 'all'`

  * Перевірте, чи немає глобального `agents.defaults.sandbox.mode`, який його перевизначає.
  * Конфігурація конкретного агента має пріоритет, тому задайте `agents.list[].sandbox.mode: "all"`.

Інструменти все ще доступні попри список заборон

  * Перевірте порядок фільтрації інструментів: глобальний → агент → пісочниця → підагент.
  * Кожен рівень може лише додатково обмежувати, а не повертати дозволи.
  * Перевірте за журналами: `[tools] filtering tools for agent:${agentId}`.

Контейнер не ізольований для кожного агента

  * Задайте `scope: "agent"` у конфігурації пісочниці конкретного агента.
  * Типове значення — `"session"`, що створює один контейнер на сесію.


* * *

## Пов’язане

  * [Підвищений режим](</uk/tools/elevated>)
  * [Маршрутизація між агентами](</uk/concepts/multi-agent>)
  * [Конфігурація пісочниці](</uk/gateway/config-agents#agentsdefaultssandbox>)
  * [Пісочниця порівняно з політикою інструментів і підвищеним режимом](</uk/gateway/sandbox-vs-tool-policy-vs-elevated>) — налагодження «чому це заблоковано?»
  * [Ізоляція в пісочниці](</uk/gateway/sandboxing>) — повний довідник пісочниці (режими, області, бекенди, образи)
  * [Керування сеансами](</uk/concepts/session>)


Was this useful?YesNo