---
title: Sandbox e strumenti multi-agente
source_url: https://docs.openclaw.ai/it/tools/multi-agent-sandbox-tools
scraped_at: 2026-05-25
---

Ogni agente in una configurazione multi-agente può sovrascrivere la sandbox globale e la policy degli strumenti. Questa pagina illustra la configurazione per agente, le regole di precedenza e alcuni esempi.

[**Sandboxing** Backend e modalità — riferimento completo della sandbox. ](</it/gateway/sandboxing>) [**Sandbox vs policy degli strumenti vs elevata** Debug di "perché è bloccato?" ](</it/gateway/sandbox-vs-tool-policy-vs-elevated>) [**Modalità elevata** Esecuzione elevata per mittenti attendibili. ](</it/tools/elevated>)

* * *

## Esempi di configurazione

Esempio 1: agente personale + agente famiglia con restrizioni jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "name": "Personal Assistant",        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      },      {        "id": "family",        "name": "Family Bot",        "workspace": "~/.openclaw/workspace-family",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read", "message"],          "deny": ["exec", "write", "edit", "apply_patch", "process", "browser"],          "message": {            "crossContext": {              "allowWithinProvider": false,              "allowAcrossProviders": false            }          }        }      }    ]  },  "bindings": [    {      "agentId": "family",      "match": {        "provider": "whatsapp",        "accountId": "*",        "peer": {          "kind": "group",          "id": "120363424282127706@g.us"        }      }    }  ]}
[/code]

**Risultato:**

  * agente `main`: viene eseguito sull'host, accesso completo agli strumenti.
  * agente `family`: viene eseguito in Docker (un contenitore per agente), solo `read` e invii di messaggi nella conversazione corrente.

Esempio 2: agente di lavoro con sandbox condivisa jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "personal",        "workspace": "~/.openclaw/workspace-personal",        "sandbox": { "mode": "off" }      },      {        "id": "work",        "workspace": "~/.openclaw/workspace-work",        "sandbox": {          "mode": "all",          "scope": "shared",          "workspaceRoot": "/tmp/work-sandboxes"        },        "tools": {          "allow": ["read", "write", "apply_patch", "exec"],          "deny": ["browser", "gateway", "discord"]        }      }    ]  }}
[/code]

Esempio 2b: profilo di codifica globale + agente solo messaggistica jsonCopy code
[code]
    {  "tools": { "profile": "coding" },  "agents": {    "list": [      {        "id": "support",        "tools": { "profile": "messaging", "allow": ["slack"] }      }    ]  }}
[/code]

**Risultato:**

  * gli agenti predefiniti ottengono gli strumenti di codifica.
  * l'agente `support` è solo messaggistica (+ strumento Slack).

Esempio 3: modalità sandbox diverse per agente jsonCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "non-main",        "scope": "session"      }    },    "list": [      {        "id": "main",        "workspace": "~/.openclaw/workspace",        "sandbox": {          "mode": "off"        }      },      {        "id": "public",        "workspace": "~/.openclaw/workspace-public",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read"],          "deny": ["exec", "write", "edit", "apply_patch"]        }      }    ]  }}
[/code]

* * *

## Precedenza della configurazione

Quando esistono sia configurazioni globali (`agents.defaults.*`) sia configurazioni specifiche dell'agente (`agents.list[].*`):

### Configurazione della sandbox

Le impostazioni specifiche dell'agente sovrascrivono quelle globali:

CodeCopy code
[code]
    agents.list[].sandbox.mode > agents.defaults.sandbox.modeagents.list[].sandbox.scope > agents.defaults.sandbox.scopeagents.list[].sandbox.workspaceRoot > agents.defaults.sandbox.workspaceRootagents.list[].sandbox.workspaceAccess > agents.defaults.sandbox.workspaceAccessagents.list[].sandbox.docker.* > agents.defaults.sandbox.docker.*agents.list[].sandbox.browser.* > agents.defaults.sandbox.browser.*agents.list[].sandbox.prune.* > agents.defaults.sandbox.prune.*
[/code]

### Restrizioni degli strumenti

L'ordine di filtraggio è:

* ### Profilo strumenti

`tools.profile` o `agents.list[].tools.profile`.

* ### Profilo strumenti del provider

`tools.byProvider[provider].profile` o `agents.list[].tools.byProvider[provider].profile`.

* ### Policy globale degli strumenti

`tools.allow` / `tools.deny`.

* ### Policy degli strumenti del provider

`tools.byProvider[provider].allow/deny`.

* ### Policy degli strumenti specifica dell'agente

`agents.list[].tools.allow/deny`.

* ### Policy del provider dell'agente

`agents.list[].tools.byProvider[provider].allow/deny`.

* ### Policy degli strumenti della sandbox

`tools.sandbox.tools` o `agents.list[].tools.sandbox.tools`.

* ### Policy degli strumenti dei sottoagenti

`tools.subagents.tools`, se applicabile.

Regole di precedenza

  * Ogni livello può restringere ulteriormente gli strumenti, ma non può concedere di nuovo strumenti negati dai livelli precedenti.
  * Se `agents.list[].tools.sandbox.tools` è impostato, sostituisce `tools.sandbox.tools` per quell'agente.
  * Se `agents.list[].tools.profile` è impostato, sovrascrive `tools.profile` per quell'agente.
  * Le chiavi degli strumenti del provider accettano `provider` (ad es. `google-antigravity`) oppure `provider/model` (ad es. `openai/gpt-5.4`).

Comportamento dell'allowlist vuota

Se una allowlist esplicita in quella catena lascia l'esecuzione senza strumenti invocabili, OpenClaw si arresta prima di inviare il prompt al modello. Questo è intenzionale: un agente configurato con uno strumento mancante come `agents.list[].tools.allow: ["query_db"]` deve fallire in modo evidente finché il plugin che registra `query_db` non viene abilitato, non continuare come agente solo testo.

Le policy degli strumenti supportano scorciatoie `group:*` che si espandono in più strumenti. Consulta [Gruppi di strumenti](</it/gateway/sandbox-vs-tool-policy-vs-elevated#tool-groups-shorthands>) per l'elenco completo.

Le sovrascritture elevate per agente (`agents.list[].tools.elevated`) possono restringere ulteriormente l'esecuzione elevata per agenti specifici. Consulta [Modalità elevata](</it/tools/elevated>) per i dettagli.

* * *

## Migrazione da agente singolo

### Prima (agente singolo)

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "workspace": "~/.openclaw/workspace",      "sandbox": {        "mode": "non-main"      }    }  },  "tools": {    "sandbox": {      "tools": {        "allow": ["read", "write", "apply_patch", "exec"],        "deny": []      }    }  }}
[/code]

### Dopo (multi-agente)

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      }    ]  }}
[/code]

* * *

## Esempi di restrizione degli strumenti

### Agente di sola lettura

jsonCopy code
[code]
    {  "tools": {    "allow": ["read"],    "deny": ["exec", "write", "edit", "apply_patch", "process"]  }}
[/code]

### Esecuzione shell con strumenti filesystem disabilitati

jsonCopy code
[code]
    {  "tools": {    "allow": ["read", "exec", "process"],    "deny": ["write", "edit", "apply_patch", "browser", "gateway"]  }}
[/code]

### Solo comunicazione

jsonCopy code
[code]
    {  "tools": {    "sessions": { "visibility": "tree" },    "allow": ["sessions_list", "sessions_send", "sessions_history", "session_status"],    "deny": ["exec", "write", "edit", "apply_patch", "read", "browser"]  }}
[/code]

`sessions_history` in questo profilo restituisce comunque una vista di richiamo limitata e sanificata, invece di un dump grezzo della trascrizione. Il richiamo dell'assistente rimuove i tag di ragionamento, l'impalcatura `<relevant-memories>`, i payload XML delle chiamate agli strumenti in testo semplice (inclusi `<tool_call>...</tool_call>`, `<function_call>...</function_call>`, `<tool_calls>...</tool_calls>`, `<function_calls>...</function_calls>` e i blocchi di chiamate agli strumenti troncati), l'impalcatura declassata delle chiamate agli strumenti, i token di controllo del modello ASCII/full-width trapelati e l'XML malformato delle chiamate agli strumenti MiniMax prima della redazione/troncatura.

* * *

## Errore comune: "non-main"

* * *

## Test

Dopo aver configurato sandbox e strumenti multi-agente:

* ### Controlla la risoluzione degli agenti

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

* ### Verifica i container sandbox

bashCopy code
[code]
    docker ps --filter "name=openclaw-sbx-"
[/code]

* ### Testa le restrizioni degli strumenti

  * Invia un messaggio che richieda strumenti con restrizioni.
  * Verifica che l'agente non possa usare gli strumenti negati.


* ### Monitora i log

bashCopy code
[code]
    tail -f "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/logs/gateway.log" | grep -E "routing|sandbox|tools"
[/code]

* * *

## Risoluzione dei problemi

Agente non in sandbox nonostante `mode: 'all'`

  * Controlla se esiste un `agents.defaults.sandbox.mode` globale che lo sovrascrive.
  * La configurazione specifica dell'agente ha la precedenza, quindi imposta `agents.list[].sandbox.mode: "all"`.

Strumenti ancora disponibili nonostante l'elenco deny

  * Controlla l'ordine di filtraggio degli strumenti: globale → agente → sandbox → subagente.
  * Ogni livello può solo restringere ulteriormente, non concedere di nuovo.
  * Verifica con i log: `[tools] filtering tools for agent:${agentId}`.

Container non isolato per agente

  * Imposta `scope: "agent"` nella configurazione sandbox specifica dell'agente.
  * Il valore predefinito è `"session"`, che crea un container per sessione.


* * *

## Correlati

  * [Modalità elevata](</it/tools/elevated>)
  * [Instradamento multi-agente](</it/concepts/multi-agent>)
  * [Configurazione della sandbox](</it/gateway/config-agents#agentsdefaultssandbox>)
  * [Sandbox vs criterio degli strumenti vs modalità elevata](</it/gateway/sandbox-vs-tool-policy-vs-elevated>) — debug di "perché è bloccato?"
  * [Sandboxing](</it/gateway/sandboxing>) — riferimento completo della sandbox (modalità, ambiti, backend, immagini)
  * [Gestione delle sessioni](</it/concepts/session>)


Was this useful?YesNo