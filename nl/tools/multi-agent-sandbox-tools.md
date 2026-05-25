---
title: Sandboxomgeving en hulpmiddelen voor meerdere agenten
source_url: https://docs.openclaw.ai/nl/tools/multi-agent-sandbox-tools
scraped_at: 2026-05-25
---

Elke agent in een multi-agentconfiguratie kan de globale sandbox- en tool-policy overschrijven. Deze pagina behandelt configuratie per agent, prioriteitsregels en voorbeelden.

[**Sandboxing** Backends en modi — volledige sandboxreferentie. ](</nl/gateway/sandboxing>) [**Sandbox vs tool-policy vs verhoogd** Debuggen: "waarom wordt dit geblokkeerd?" ](</nl/gateway/sandbox-vs-tool-policy-vs-elevated>) [**Verhoogde modus** Verhoogde exec voor vertrouwde afzenders. ](</nl/tools/elevated>)

* * *

## Configuratievoorbeelden

Voorbeeld 1: Persoonlijke + beperkte familieagent jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "name": "Personal Assistant",        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      },      {        "id": "family",        "name": "Family Bot",        "workspace": "~/.openclaw/workspace-family",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read", "message"],          "deny": ["exec", "write", "edit", "apply_patch", "process", "browser"],          "message": {            "crossContext": {              "allowWithinProvider": false,              "allowAcrossProviders": false            }          }        }      }    ]  },  "bindings": [    {      "agentId": "family",      "match": {        "provider": "whatsapp",        "accountId": "*",        "peer": {          "kind": "group",          "id": "120363424282127706@g.us"        }      }    }  ]}
[/code]

**Resultaat:**

  * `main`-agent: draait op de host, volledige tooltoegang.
  * `family`-agent: draait in Docker (één container per agent), alleen `read` en berichten verzenden in het huidige gesprek.

Voorbeeld 2: Werkagent met gedeelde sandbox jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "personal",        "workspace": "~/.openclaw/workspace-personal",        "sandbox": { "mode": "off" }      },      {        "id": "work",        "workspace": "~/.openclaw/workspace-work",        "sandbox": {          "mode": "all",          "scope": "shared",          "workspaceRoot": "/tmp/work-sandboxes"        },        "tools": {          "allow": ["read", "write", "apply_patch", "exec"],          "deny": ["browser", "gateway", "discord"]        }      }    ]  }}
[/code]

Voorbeeld 2b: Globaal codeerprofiel + agent voor alleen berichten jsonCopy code
[code]
    {  "tools": { "profile": "coding" },  "agents": {    "list": [      {        "id": "support",        "tools": { "profile": "messaging", "allow": ["slack"] }      }    ]  }}
[/code]

**Resultaat:**

  * standaardagents krijgen codeertools.
  * `support`-agent is alleen voor berichten (+ Slack-tool).

Voorbeeld 3: Verschillende sandboxmodi per agent jsonCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "non-main",        "scope": "session"      }    },    "list": [      {        "id": "main",        "workspace": "~/.openclaw/workspace",        "sandbox": {          "mode": "off"        }      },      {        "id": "public",        "workspace": "~/.openclaw/workspace-public",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read"],          "deny": ["exec", "write", "edit", "apply_patch"]        }      }    ]  }}
[/code]

* * *

## Configuratieprioriteit

Wanneer zowel globale (`agents.defaults.*`) als agentspecifieke (`agents.list[].*`) configuraties bestaan:

### Sandboxconfiguratie

Agentspecifieke instellingen overschrijven globale instellingen:

CodeCopy code
[code]
    agents.list[].sandbox.mode > agents.defaults.sandbox.modeagents.list[].sandbox.scope > agents.defaults.sandbox.scopeagents.list[].sandbox.workspaceRoot > agents.defaults.sandbox.workspaceRootagents.list[].sandbox.workspaceAccess > agents.defaults.sandbox.workspaceAccessagents.list[].sandbox.docker.* > agents.defaults.sandbox.docker.*agents.list[].sandbox.browser.* > agents.defaults.sandbox.browser.*agents.list[].sandbox.prune.* > agents.defaults.sandbox.prune.*
[/code]

### Toolbeperkingen

De filtervolgorde is:

* ### Toolprofiel

`tools.profile` of `agents.list[].tools.profile`.

* ### Provider-toolprofiel

`tools.byProvider[provider].profile` of `agents.list[].tools.byProvider[provider].profile`.

* ### Globale tool-policy

`tools.allow` / `tools.deny`.

* ### Provider-tool-policy

`tools.byProvider[provider].allow/deny`.

* ### Agentspecifieke tool-policy

`agents.list[].tools.allow/deny`.

* ### Agent-provider-policy

`agents.list[].tools.byProvider[provider].allow/deny`.

* ### Sandbox-tool-policy

`tools.sandbox.tools` of `agents.list[].tools.sandbox.tools`.

* ### Subagent-tool-policy

`tools.subagents.tools`, indien van toepassing.

Prioriteitsregels

  * Elk niveau kan tools verder beperken, maar kan eerder geweigerde tools niet opnieuw toestaan.
  * Als `agents.list[].tools.sandbox.tools` is ingesteld, vervangt dit `tools.sandbox.tools` voor die agent.
  * Als `agents.list[].tools.profile` is ingesteld, overschrijft dit `tools.profile` voor die agent.
  * Provider-toolsleutels accepteren `provider` (bijv. `google-antigravity`) of `provider/model` (bijv. `openai/gpt-5.4`).

Gedrag bij lege allowlist

Als een expliciete allowlist in die keten ervoor zorgt dat de run geen aanroepbare tools meer heeft, stopt OpenClaw voordat de prompt naar het model wordt gestuurd. Dit is opzettelijk: een agent die is geconfigureerd met een ontbrekende tool zoals `agents.list[].tools.allow: ["query_db"]` moet duidelijk falen totdat de Plugin die `query_db` registreert is ingeschakeld, en niet doorgaan als tekst-only agent.

Tool-policies ondersteunen `group:*`-verkortingen die worden uitgebreid naar meerdere tools. Zie [Toolgroepen](</nl/gateway/sandbox-vs-tool-policy-vs-elevated#tool-groups-shorthands>) voor de volledige lijst.

Verhoogde overschrijvingen per agent (`agents.list[].tools.elevated`) kunnen verhoogde exec voor specifieke agents verder beperken. Zie [Verhoogde modus](</nl/tools/elevated>) voor details.

* * *

## Migratie van één agent

### Vóór (één agent)

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "workspace": "~/.openclaw/workspace",      "sandbox": {        "mode": "non-main"      }    }  },  "tools": {    "sandbox": {      "tools": {        "allow": ["read", "write", "apply_patch", "exec"],        "deny": []      }    }  }}
[/code]

### Na (multi-agent)

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      }    ]  }}
[/code]

* * *

## Voorbeelden van toolbeperkingen

### Alleen-lezen-agent

jsonCopy code
[code]
    {  "tools": {    "allow": ["read"],    "deny": ["exec", "write", "edit", "apply_patch", "process"]  }}
[/code]

### Shelluitvoering met bestandssysteemtools uitgeschakeld

jsonCopy code
[code]
    {  "tools": {    "allow": ["read", "exec", "process"],    "deny": ["write", "edit", "apply_patch", "browser", "gateway"]  }}
[/code]

### Alleen communicatie

jsonCopy code
[code]
    {  "tools": {    "sessions": { "visibility": "tree" },    "allow": ["sessions_list", "sessions_send", "sessions_history", "session_status"],    "deny": ["exec", "write", "edit", "apply_patch", "read", "browser"]  }}
[/code]

`sessions_history` in dit profiel retourneert nog steeds een begrensde, opgeschoonde recall-weergave in plaats van een ruwe transcriptdump. Assistant-recall verwijdert denktags, `<relevant-memories>`-scaffolding, tool-call-XML-payloads in platte tekst (inclusief `<tool_call>...</tool_call>`, `<function_call>...</function_call>`, `<tool_calls>...</tool_calls>`, `<function_calls>...</function_calls>` en afgekorte tool-call-blokken), gedegradeerde tool-call-scaffolding, gelekte ASCII-/full-width-modelcontroletokens en misvormde MiniMax-tool-call-XML vóór redactie/afkapping.

* * *

## Veelvoorkomende valkuil: "non-main"

* * *

## Testen

Na het configureren van multi-agent-sandbox en tools:

* ### Agentresolutie controleren

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

* ### Sandboxcontainers verifiëren

bashCopy code
[code]
    docker ps --filter "name=openclaw-sbx-"
[/code]

* ### Toolbeperkingen testen

  * Stuur een bericht waarvoor beperkte tools nodig zijn.
  * Controleer of de agent geweigerde tools niet kan gebruiken.


* ### Logs monitoren

bashCopy code
[code]
    tail -f "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/logs/gateway.log" | grep -E "routing|sandbox|tools"
[/code]

* * *

## Problemen oplossen

Agent niet gesandboxed ondanks `mode: 'all'`

  * Controleer of er een globale `agents.defaults.sandbox.mode` is die dit overschrijft.
  * Agentspecifieke configuratie heeft voorrang, dus stel `agents.list[].sandbox.mode: "all"` in.

Tools nog steeds beschikbaar ondanks deny-lijst

  * Controleer de volgorde van toolfiltering: globaal → agent → sandbox → subagent.
  * Elk niveau kan alleen verder beperken, niet opnieuw toestaan.
  * Verifieer met logs: `[tools] filtering tools for agent:${agentId}`.

Container niet per agent geïsoleerd

  * Stel `scope: "agent"` in in agentspecifieke sandboxconfiguratie.
  * De standaard is `"session"`, waarmee één container per sessie wordt gemaakt.


* * *

## Gerelateerd

  * [Verhoogde modus](</nl/tools/elevated>)
  * [Routering met meerdere agents](</nl/concepts/multi-agent>)
  * [Sandboxconfiguratie](</nl/gateway/config-agents#agentsdefaultssandbox>)
  * [Sandbox versus toolbeleid versus verhoogd](</nl/gateway/sandbox-vs-tool-policy-vs-elevated>) — foutopsporing voor "waarom is dit geblokkeerd?"
  * [Sandboxing](</nl/gateway/sandboxing>) — volledige sandboxreferentie (modi, bereiken, backends, containerimages)
  * [Sessiebeheer](</nl/concepts/session>)


Was this useful?YesNo