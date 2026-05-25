---
title: Piaskownica i narzędzia dla wielu agentów
source_url: https://docs.openclaw.ai/pl/tools/multi-agent-sandbox-tools
scraped_at: 2026-05-25
---

Każdy agent w konfiguracji wieloagentowej może nadpisać globalne zasady sandboxa i narzędzi. Ta strona omawia konfigurację per agent, reguły pierwszeństwa oraz przykłady.

[**Sandboxing** Backendy i tryby — pełna dokumentacja sandboxa. ](</pl/gateway/sandboxing>) [**Sandbox a zasady narzędzi a elevated** Debugowanie: „dlaczego to jest zablokowane?” ](</pl/gateway/sandbox-vs-tool-policy-vs-elevated>) [**Tryb elevated** Podniesione uprawnienia exec dla zaufanych nadawców. ](</pl/tools/elevated>)

* * *

## Przykłady konfiguracji

Przykład 1: Agent osobisty + ograniczony agent rodzinny jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "name": "Personal Assistant",        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      },      {        "id": "family",        "name": "Family Bot",        "workspace": "~/.openclaw/workspace-family",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read", "message"],          "deny": ["exec", "write", "edit", "apply_patch", "process", "browser"],          "message": {            "crossContext": {              "allowWithinProvider": false,              "allowAcrossProviders": false            }          }        }      }    ]  },  "bindings": [    {      "agentId": "family",      "match": {        "provider": "whatsapp",        "accountId": "*",        "peer": {          "kind": "group",          "id": "120363424282127706@g.us"        }      }    }  ]}
[/code]

**Wynik:**

  * agent `main`: działa na hoście, pełny dostęp do narzędzi.
  * agent `family`: działa w Dockerze (jeden kontener na agenta), tylko `read` i wysyłanie wiadomości w bieżącej konwersacji.

Przykład 2: Agent roboczy ze współdzielonym sandboxem jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "personal",        "workspace": "~/.openclaw/workspace-personal",        "sandbox": { "mode": "off" }      },      {        "id": "work",        "workspace": "~/.openclaw/workspace-work",        "sandbox": {          "mode": "all",          "scope": "shared",          "workspaceRoot": "/tmp/work-sandboxes"        },        "tools": {          "allow": ["read", "write", "apply_patch", "exec"],          "deny": ["browser", "gateway", "discord"]        }      }    ]  }}
[/code]

Przykład 2b: Globalny profil kodowania + agent tylko do wiadomości jsonCopy code
[code]
    {  "tools": { "profile": "coding" },  "agents": {    "list": [      {        "id": "support",        "tools": { "profile": "messaging", "allow": ["slack"] }      }    ]  }}
[/code]

**Wynik:**

  * agenci domyślni otrzymują narzędzia do kodowania.
  * agent `support` służy tylko do wiadomości (+ narzędzie Slack).

Przykład 3: Różne tryby sandboxa per agent jsonCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "non-main",        "scope": "session"      }    },    "list": [      {        "id": "main",        "workspace": "~/.openclaw/workspace",        "sandbox": {          "mode": "off"        }      },      {        "id": "public",        "workspace": "~/.openclaw/workspace-public",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read"],          "deny": ["exec", "write", "edit", "apply_patch"]        }      }    ]  }}
[/code]

* * *

## Pierwszeństwo konfiguracji

Gdy istnieją zarówno konfiguracje globalne (`agents.defaults.*`), jak i specyficzne dla agenta (`agents.list[].*`):

### Konfiguracja sandboxa

Ustawienia specyficzne dla agenta nadpisują globalne:

CodeCopy code
[code]
    agents.list[].sandbox.mode > agents.defaults.sandbox.modeagents.list[].sandbox.scope > agents.defaults.sandbox.scopeagents.list[].sandbox.workspaceRoot > agents.defaults.sandbox.workspaceRootagents.list[].sandbox.workspaceAccess > agents.defaults.sandbox.workspaceAccessagents.list[].sandbox.docker.* > agents.defaults.sandbox.docker.*agents.list[].sandbox.browser.* > agents.defaults.sandbox.browser.*agents.list[].sandbox.prune.* > agents.defaults.sandbox.prune.*
[/code]

### Ograniczenia narzędzi

Kolejność filtrowania jest następująca:

* ### Profil narzędzi

`tools.profile` lub `agents.list[].tools.profile`.

* ### Profil narzędzi dostawcy

`tools.byProvider[provider].profile` lub `agents.list[].tools.byProvider[provider].profile`.

* ### Globalna polityka narzędzi

`tools.allow` / `tools.deny`.

* ### Polityka narzędzi dostawcy

`tools.byProvider[provider].allow/deny`.

* ### Polityka narzędzi specyficzna dla agenta

`agents.list[].tools.allow/deny`.

* ### Polityka dostawcy agenta

`agents.list[].tools.byProvider[provider].allow/deny`.

* ### Polityka narzędzi sandboxa

`tools.sandbox.tools` lub `agents.list[].tools.sandbox.tools`.

* ### Polityka narzędzi subagenta

`tools.subagents.tools`, jeśli ma zastosowanie.

Reguły pierwszeństwa

  * Każdy poziom może dalej ograniczać narzędzia, ale nie może ponownie przyznać narzędzi zabronionych na wcześniejszych poziomach.
  * Jeśli ustawiono `agents.list[].tools.sandbox.tools`, zastępuje ono `tools.sandbox.tools` dla tego agenta.
  * Jeśli ustawiono `agents.list[].tools.profile`, nadpisuje ono `tools.profile` dla tego agenta.
  * Klucze narzędzi dostawcy akceptują `provider` (np. `google-antigravity`) albo `provider/model` (np. `openai/gpt-5.4`).

Zachowanie pustej listy dozwolonych

Jeśli dowolna jawna lista dozwolonych w tym łańcuchu pozostawi uruchomienie bez wywoływalnych narzędzi, OpenClaw zatrzyma się przed wysłaniem promptu do modelu. Jest to celowe: agent skonfigurowany z brakującym narzędziem, takim jak `agents.list[].tools.allow: ["query_db"]`, powinien zakończyć się głośnym błędem, dopóki Plugin rejestrujący `query_db` nie zostanie włączony, zamiast kontynuować jako agent tylko tekstowy.

Polityki narzędzi obsługują skróty `group:*`, które rozwijają się do wielu narzędzi. Pełną listę znajdziesz w [Grupach narzędzi](</pl/gateway/sandbox-vs-tool-policy-vs-elevated#tool-groups-shorthands>).

Nadpisania elevated per agent (`agents.list[].tools.elevated`) mogą dodatkowo ograniczać podniesione uprawnienia exec dla konkretnych agentów. Szczegóły znajdziesz w [Trybie elevated](</pl/tools/elevated>).

* * *

## Migracja z pojedynczego agenta

### Przed (pojedynczy agent)

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "workspace": "~/.openclaw/workspace",      "sandbox": {        "mode": "non-main"      }    }  },  "tools": {    "sandbox": {      "tools": {        "allow": ["read", "write", "apply_patch", "exec"],        "deny": []      }    }  }}
[/code]

### Po (wielu agentów)

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      }    ]  }}
[/code]

* * *

## Przykłady ograniczeń narzędzi

### Agent tylko do odczytu

jsonCopy code
[code]
    {  "tools": {    "allow": ["read"],    "deny": ["exec", "write", "edit", "apply_patch", "process"]  }}
[/code]

### Wykonywanie poleceń powłoki z wyłączonymi narzędziami systemu plików

jsonCopy code
[code]
    {  "tools": {    "allow": ["read", "exec", "process"],    "deny": ["write", "edit", "apply_patch", "browser", "gateway"]  }}
[/code]

### Tylko komunikacja

jsonCopy code
[code]
    {  "tools": {    "sessions": { "visibility": "tree" },    "allow": ["sessions_list", "sessions_send", "sessions_history", "session_status"],    "deny": ["exec", "write", "edit", "apply_patch", "read", "browser"]  }}
[/code]

`sessions_history` w tym profilu nadal zwraca ograniczony, oczyszczony widok przypominania, a nie surowy zrzut transkrypcji. Przypominanie asystenta usuwa tagi rozumowania, struktury pomocnicze `<relevant-memories>`, ładunki XML wywołań narzędzi w postaci zwykłego tekstu (w tym `<tool_call>...</tool_call>`, `<function_call>...</function_call>`, `<tool_calls>...</tool_calls>`, `<function_calls>...</function_calls>` oraz ucięte bloki wywołań narzędzi), zdegradowane struktury pomocnicze wywołań narzędzi, ujawnione tokeny kontrolne modelu ASCII/pełnej szerokości oraz nieprawidłowy XML wywołań narzędzi MiniMax przed redakcją/ucięciem.

* * *

## Typowa pułapka: „non-main”

* * *

## Testowanie

Po skonfigurowaniu sandboxa i narzędzi dla wielu agentów:

* ### Sprawdź rozstrzyganie agenta

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

* ### Zweryfikuj kontenery sandboxa

bashCopy code
[code]
    docker ps --filter "name=openclaw-sbx-"
[/code]

* ### Przetestuj ograniczenia narzędzi

  * Wyślij wiadomość wymagającą ograniczonych narzędzi.
  * Sprawdź, czy agent nie może używać narzędzi, którym odmówiono dostępu.


* ### Monitoruj logi

bashCopy code
[code]
    tail -f "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/logs/gateway.log" | grep -E "routing|sandbox|tools"
[/code]

* * *

## Rozwiązywanie problemów

Agent nie jest objęty sandboxem mimo `mode: 'all'`

  * Sprawdź, czy istnieje globalne `agents.defaults.sandbox.mode`, które je zastępuje.
  * Konfiguracja specyficzna dla agenta ma pierwszeństwo, więc ustaw `agents.list[].sandbox.mode: "all"`.

Narzędzia nadal dostępne mimo listy odmów

  * Sprawdź kolejność filtrowania narzędzi: globalne → agent → sandbox → podagent.
  * Każdy poziom może tylko dalej ograniczać, nie ponownie przyznawać dostęp.
  * Zweryfikuj w logach: `[tools] filtering tools for agent:${agentId}`.

Kontener nie jest izolowany na agenta

  * Ustaw `scope: "agent"` w konfiguracji sandboxa specyficznej dla agenta.
  * Wartością domyślną jest `"session"`, co tworzy jeden kontener na sesję.


* * *

## Powiązane

  * [Tryb podwyższonych uprawnień](</pl/tools/elevated>)
  * [Routing wieloagentowy](</pl/concepts/multi-agent>)
  * [Konfiguracja piaskownicy](</pl/gateway/config-agents#agentsdefaultssandbox>)
  * [Piaskownica kontra polityka narzędzi kontra tryb podwyższonych uprawnień](</pl/gateway/sandbox-vs-tool-policy-vs-elevated>) — debugowanie „dlaczego to jest blokowane?”
  * [Izolacja w piaskownicy](</pl/gateway/sandboxing>) — pełna dokumentacja referencyjna piaskownicy (tryby, zakresy, backendy, obrazy)
  * [Zarządzanie sesją](</pl/concepts/session>)


Was this useful?YesNo