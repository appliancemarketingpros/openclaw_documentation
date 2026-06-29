---
title: Многоагентная песочница и инструменты
source_url: https://docs.openclaw.ai/ru/tools/multi-agent-sandbox-tools
scraped_at: 2026-06-29
---

CapabilitiesAgent coordination

Каждый агент в многоагентной конфигурации может переопределять глобальную политику песочницы и инструментов. На этой странице описаны настройки для отдельных агентов, правила приоритета и примеры.

[**Песочница** Бэкенды и режимы — полный справочник по песочнице. ](</ru/gateway/sandboxing>) [**Песочница, политика инструментов и повышенный режим** Отладка вопроса «почему это заблокировано?» ](</ru/gateway/sandbox-vs-tool-policy-vs-elevated>) [**Повышенный режим** Повышенный exec для доверенных отправителей. ](</ru/tools/elevated>)

* * *

## Примеры конфигурации

Пример 1: личный агент + ограниченный семейный агент jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "name": "Personal Assistant",        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      },      {        "id": "family",        "name": "Family Bot",        "workspace": "~/.openclaw/workspace-family",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read", "message"],          "deny": ["exec", "write", "edit", "apply_patch", "process", "browser"],          "message": {            "crossContext": {              "allowWithinProvider": false,              "allowAcrossProviders": false            }          }        }      }    ]  },  "bindings": [    {      "agentId": "family",      "match": {        "provider": "whatsapp",        "accountId": "*",        "peer": {          "kind": "group",          "id": "120363424282127706@g.us"        }      }    }  ]}
[/code]

**Результат:**

  * агент `main`: работает на хосте, полный доступ к инструментам.
  * агент `family`: работает в Docker (один контейнер на агента), доступны только `read` и отправка сообщений в текущей беседе.

Пример 2: рабочий агент с общей песочницей jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "personal",        "workspace": "~/.openclaw/workspace-personal",        "sandbox": { "mode": "off" }      },      {        "id": "work",        "workspace": "~/.openclaw/workspace-work",        "sandbox": {          "mode": "all",          "scope": "shared",          "workspaceRoot": "/tmp/work-sandboxes"        },        "tools": {          "allow": ["read", "write", "apply_patch", "exec"],          "deny": ["browser", "gateway", "discord"]        }      }    ]  }}
[/code]

Пример 2b: глобальный профиль программирования + агент только для сообщений jsonCopy code
[code]
    {  "tools": { "profile": "coding" },  "agents": {    "list": [      {        "id": "support",        "tools": { "profile": "messaging", "allow": ["slack"] }      }    ]  }}
[/code]

**Результат:**

  * агенты по умолчанию получают инструменты для программирования.
  * агент `support` работает только с сообщениями (+ инструмент Slack).

Пример 3: разные режимы песочницы для разных агентов jsonCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "non-main",        "scope": "session"      }    },    "list": [      {        "id": "main",        "workspace": "~/.openclaw/workspace",        "sandbox": {          "mode": "off"        }      },      {        "id": "public",        "workspace": "~/.openclaw/workspace-public",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read"],          "deny": ["exec", "write", "edit", "apply_patch"]        }      }    ]  }}
[/code]

* * *

## Приоритет конфигурации

Когда существуют и глобальные (`agents.defaults.*`), и агентские (`agents.list[].*`) конфигурации:

### Конфигурация песочницы

Настройки конкретного агента переопределяют глобальные:

CodeCopy code
[code]
    agents.list[].sandbox.mode > agents.defaults.sandbox.modeagents.list[].sandbox.scope > agents.defaults.sandbox.scopeagents.list[].sandbox.workspaceRoot > agents.defaults.sandbox.workspaceRootagents.list[].sandbox.workspaceAccess > agents.defaults.sandbox.workspaceAccessagents.list[].sandbox.docker.* > agents.defaults.sandbox.docker.*agents.list[].sandbox.browser.* > agents.defaults.sandbox.browser.*agents.list[].sandbox.prune.* > agents.defaults.sandbox.prune.*
[/code]

### Ограничения инструментов

Порядок фильтрации:

* ### Профиль инструментов

`tools.profile` или `agents.list[].tools.profile`.

* ### Профиль инструментов провайдера

`tools.byProvider[provider].profile` или `agents.list[].tools.byProvider[provider].profile`.

* ### Глобальная политика инструментов

`tools.allow` / `tools.deny`.

* ### Политика инструментов провайдера

`tools.byProvider[provider].allow/deny`.

* ### Политика инструментов конкретного агента

`agents.list[].tools.allow/deny`.

* ### Политика провайдера агента

`agents.list[].tools.byProvider[provider].allow/deny`.

* ### Политика инструментов песочницы

`tools.sandbox.tools` или `agents.list[].tools.sandbox.tools`.

* ### Политика инструментов субагента

`tools.subagents.tools`, если применимо.

Правила приоритета

  * Каждый уровень может дополнительно ограничивать инструменты, но не может снова разрешить инструменты, запрещенные на предыдущих уровнях.
  * Если задано `agents.list[].tools.sandbox.tools`, оно заменяет `tools.sandbox.tools` для этого агента.
  * Если задано `agents.list[].tools.profile`, оно переопределяет `tools.profile` для этого агента.
  * Ключи инструментов провайдера принимают либо `provider` (например, `google-antigravity`), либо `provider/model` (например, `openai/gpt-5.4`).

Поведение пустого списка разрешений

Если любой явный список разрешений в этой цепочке оставляет запуск без доступных для вызова инструментов, OpenClaw останавливается до отправки промпта модели. Это сделано намеренно: агент, настроенный с отсутствующим инструментом, например `agents.list[].tools.allow: ["query_db"]`, должен явно завершаться ошибкой, пока не будет включен Plugin, регистрирующий `query_db`, а не продолжать работу как агент только с текстом.

Политики инструментов поддерживают сокращения `group:*`, которые раскрываются в несколько инструментов. Полный список см. в разделе [Группы инструментов](</ru/gateway/sandbox-vs-tool-policy-vs-elevated#tool-groups-shorthands>).

Переопределения повышенного режима для отдельных агентов (`agents.list[].tools.elevated`) могут дополнительно ограничивать повышенный exec для конкретных агентов. Подробнее см. в разделе [Повышенный режим](</ru/tools/elevated>).

* * *

## Миграция с одного агента

### До (один агент)

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "workspace": "~/.openclaw/workspace",      "sandbox": {        "mode": "non-main"      }    }  },  "tools": {    "sandbox": {      "tools": {        "allow": ["read", "write", "apply_patch", "exec"],        "deny": []      }    }  }}
[/code]

### После (мультиагентный режим)

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      }    ]  }}
[/code]

* * *

## Примеры ограничений инструментов

### Агент только для чтения

jsonCopy code
[code]
    {  "tools": {    "allow": ["read"],    "deny": ["exec", "write", "edit", "apply_patch", "process"]  }}
[/code]

### Выполнение shell с отключенными файловыми инструментами

jsonCopy code
[code]
    {  "tools": {    "allow": ["read", "exec", "process"],    "deny": ["write", "edit", "apply_patch", "browser", "gateway"]  }}
[/code]

### Только коммуникация

jsonCopy code
[code]
    {  "tools": {    "sessions": { "visibility": "tree" },    "allow": ["sessions_list", "sessions_send", "sessions_history", "session_status"],    "deny": ["exec", "write", "edit", "apply_patch", "read", "browser"]  }}
[/code]

`sessions_history` в этом профиле все равно возвращает ограниченное, очищенное представление извлеченного контекста, а не необработанный дамп транскрипта. Извлечение контекста ассистента удаляет теги размышлений, каркас `<relevant-memories>`, текстовые XML-пейлоады вызовов инструментов (включая `<tool_call>...</tool_call>`, `<function_call>...</function_call>`, `<tool_calls>...</tool_calls>`, `<function_calls>...</function_calls>` и усеченные блоки вызовов инструментов), пониженный каркас вызовов инструментов, утекшие ASCII/полноширинные управляющие токены модели и некорректный XML вызовов инструментов MiniMax перед редактированием/усечением.

* * *

## Распространенная ошибка: "non-main"

* * *

## Тестирование

После настройки мультиагентной песочницы и инструментов:

* ### Проверьте разрешение агента

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

* ### Проверьте контейнеры песочницы

bashCopy code
[code]
    docker ps --filter "name=openclaw-sbx-"
[/code]

* ### Проверьте ограничения инструментов

  * Отправьте сообщение, требующее ограниченных инструментов.
  * Убедитесь, что агент не может использовать запрещенные инструменты.


* ### Отслеживайте журналы

bashCopy code
[code]
    tail -f "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/logs/gateway.log" | grep -E "routing|sandbox|tools"
[/code]

* * *

## Устранение неполадок

Агент не запускается в песочнице, несмотря на `mode: 'all'`

  * Проверьте, есть ли глобальный `agents.defaults.sandbox.mode`, который переопределяет это значение.
  * Конфигурация конкретного агента имеет приоритет, поэтому задайте `agents.list[].sandbox.mode: "all"`.

Инструменты все еще доступны, несмотря на список запретов

  * Проверьте порядок фильтрации инструментов: глобальный → агент → песочница → субагент.
  * Каждый уровень может только дополнительно ограничивать, а не возвращать доступ.
  * Проверьте по журналам: `[tools] filtering tools for agent:${agentId}`.

Контейнер не изолирован для каждого агента

  * Задайте `scope: "agent"` в конфигурации песочницы конкретного агента.
  * Значение по умолчанию — `"session"`, при котором создается один контейнер на сеанс.


* * *

## Связанные материалы

  * [Повышенный режим](</ru/tools/elevated>)
  * [Маршрутизация между несколькими агентами](</ru/concepts/multi-agent>)
  * [Конфигурация песочницы](</ru/gateway/config-agents#agentsdefaultssandbox>)
  * [Песочница, политика инструментов и повышенный режим](</ru/gateway/sandbox-vs-tool-policy-vs-elevated>) — отладка «почему это заблокировано?»
  * [Песочница](</ru/gateway/sandboxing>) — полный справочник по песочнице (режимы, области, бэкенды, образы)
  * [Управление сеансами](</ru/concepts/session>)


Was this useful?YesNo

Open issue