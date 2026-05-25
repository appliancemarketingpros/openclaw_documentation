---
title: Sandbox e ferramentas multiagente
source_url: https://docs.openclaw.ai/pt-BR/tools/multi-agent-sandbox-tools
scraped_at: 2026-05-25
---

Cada agente em uma configuração multiagente pode substituir a sandbox global e a política de ferramentas. Esta página aborda a configuração por agente, as regras de precedência e exemplos.

[**Sandboxing** Backends e modos — referência completa de sandbox. ](</pt-BR/gateway/sandboxing>) [**Sandbox vs tool policy vs elevated** Depure "por que isto está bloqueado?" ](</pt-BR/gateway/sandbox-vs-tool-policy-vs-elevated>) [**Elevated mode** Execução elevada para remetentes confiáveis. ](</pt-BR/tools/elevated>)

* * *

## Exemplos de configuração

Example 1: Personal + restricted family agent jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "name": "Personal Assistant",        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      },      {        "id": "family",        "name": "Family Bot",        "workspace": "~/.openclaw/workspace-family",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read", "message"],          "deny": ["exec", "write", "edit", "apply_patch", "process", "browser"],          "message": {            "crossContext": {              "allowWithinProvider": false,              "allowAcrossProviders": false            }          }        }      }    ]  },  "bindings": [    {      "agentId": "family",      "match": {        "provider": "whatsapp",        "accountId": "*",        "peer": {          "kind": "group",          "id": "120363424282127706@g.us"        }      }    }  ]}
[/code]

**Resultado:**

  * agente `main`: executa no host, com acesso completo às ferramentas.
  * agente `family`: executa no Docker (um contêiner por agente), apenas `read` e envios de mensagem na conversa atual.

Example 2: Work agent with shared sandbox jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "personal",        "workspace": "~/.openclaw/workspace-personal",        "sandbox": { "mode": "off" }      },      {        "id": "work",        "workspace": "~/.openclaw/workspace-work",        "sandbox": {          "mode": "all",          "scope": "shared",          "workspaceRoot": "/tmp/work-sandboxes"        },        "tools": {          "allow": ["read", "write", "apply_patch", "exec"],          "deny": ["browser", "gateway", "discord"]        }      }    ]  }}
[/code]

Example 2b: Global coding profile + messaging-only agent jsonCopy code
[code]
    {  "tools": { "profile": "coding" },  "agents": {    "list": [      {        "id": "support",        "tools": { "profile": "messaging", "allow": ["slack"] }      }    ]  }}
[/code]

**Resultado:**

  * agentes padrão recebem ferramentas de programação.
  * o agente `support` é somente para mensagens (+ ferramenta Slack).

Example 3: Different sandbox modes per agent jsonCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "non-main",        "scope": "session"      }    },    "list": [      {        "id": "main",        "workspace": "~/.openclaw/workspace",        "sandbox": {          "mode": "off"        }      },      {        "id": "public",        "workspace": "~/.openclaw/workspace-public",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read"],          "deny": ["exec", "write", "edit", "apply_patch"]        }      }    ]  }}
[/code]

* * *

## Precedência da configuração

Quando existem configurações globais (`agents.defaults.*`) e específicas de agente (`agents.list[].*`):

### Configuração de sandbox

As configurações específicas de agente substituem as globais:

CodeCopy code
[code]
    agents.list[].sandbox.mode > agents.defaults.sandbox.modeagents.list[].sandbox.scope > agents.defaults.sandbox.scopeagents.list[].sandbox.workspaceRoot > agents.defaults.sandbox.workspaceRootagents.list[].sandbox.workspaceAccess > agents.defaults.sandbox.workspaceAccessagents.list[].sandbox.docker.* > agents.defaults.sandbox.docker.*agents.list[].sandbox.browser.* > agents.defaults.sandbox.browser.*agents.list[].sandbox.prune.* > agents.defaults.sandbox.prune.*
[/code]

### Restrições de ferramentas

A ordem de filtragem é:

* ### Tool profile

`tools.profile` ou `agents.list[].tools.profile`.

* ### Provider tool profile

`tools.byProvider[provider].profile` ou `agents.list[].tools.byProvider[provider].profile`.

* ### Global tool policy

`tools.allow` / `tools.deny`.

* ### Provider tool policy

`tools.byProvider[provider].allow/deny`.

* ### Agent-specific tool policy

`agents.list[].tools.allow/deny`.

* ### Agent provider policy

`agents.list[].tools.byProvider[provider].allow/deny`.

* ### Sandbox tool policy

`tools.sandbox.tools` ou `agents.list[].tools.sandbox.tools`.

* ### Subagent tool policy

`tools.subagents.tools`, se aplicável.

Precedence rules

  * Cada nível pode restringir ainda mais as ferramentas, mas não pode conceder novamente ferramentas negadas em níveis anteriores.
  * Se `agents.list[].tools.sandbox.tools` estiver definido, ele substitui `tools.sandbox.tools` para esse agente.
  * Se `agents.list[].tools.profile` estiver definido, ele substitui `tools.profile` para esse agente.
  * Chaves de ferramentas de provedor aceitam `provider` (por exemplo, `google-antigravity`) ou `provider/model` (por exemplo, `openai/gpt-5.4`).

Empty allowlist behavior

Se qualquer lista de permissões explícita nessa cadeia deixar a execução sem ferramentas chamáveis, o OpenClaw para antes de enviar o prompt ao modelo. Isso é intencional: um agente configurado com uma ferramenta ausente, como `agents.list[].tools.allow: ["query_db"]`, deve falhar de forma clara até que o plugin que registra `query_db` seja habilitado, em vez de continuar como um agente apenas de texto.

Políticas de ferramentas oferecem suporte a abreviações `group:*`, que se expandem para várias ferramentas. Consulte [Grupos de ferramentas](</pt-BR/gateway/sandbox-vs-tool-policy-vs-elevated#tool-groups-shorthands>) para ver a lista completa.

Substituições elevadas por agente (`agents.list[].tools.elevated`) podem restringir ainda mais a execução elevada para agentes específicos. Consulte [Modo elevado](</pt-BR/tools/elevated>) para obter detalhes.

* * *

## Migração de agente único

### Antes (agente único)

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "workspace": "~/.openclaw/workspace",      "sandbox": {        "mode": "non-main"      }    }  },  "tools": {    "sandbox": {      "tools": {        "allow": ["read", "write", "apply_patch", "exec"],        "deny": []      }    }  }}
[/code]

### Depois (multiagente)

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      }    ]  }}
[/code]

* * *

## Exemplos de restrição de ferramentas

### Agente somente leitura

jsonCopy code
[code]
    {  "tools": {    "allow": ["read"],    "deny": ["exec", "write", "edit", "apply_patch", "process"]  }}
[/code]

### Execução de shell com ferramentas do sistema de arquivos desabilitadas

jsonCopy code
[code]
    {  "tools": {    "allow": ["read", "exec", "process"],    "deny": ["write", "edit", "apply_patch", "browser", "gateway"]  }}
[/code]

### Somente comunicação

jsonCopy code
[code]
    {  "tools": {    "sessions": { "visibility": "tree" },    "allow": ["sessions_list", "sessions_send", "sessions_history", "session_status"],    "deny": ["exec", "write", "edit", "apply_patch", "read", "browser"]  }}
[/code]

`sessions_history` neste perfil ainda retorna uma visualização de recuperação limitada e sanitizada, em vez de um despejo bruto de transcrição. A recuperação do assistente remove tags de pensamento, estrutura `<relevant-memories>`, payloads XML de chamadas de ferramentas em texto simples (incluindo `<tool_call>...</tool_call>`, `<function_call>...</function_call>`, `<tool_calls>...</tool_calls>`, `<function_calls>...</function_calls>` e blocos truncados de chamadas de ferramentas), estrutura de chamadas de ferramentas rebaixada, tokens vazados de controle do modelo em ASCII/largura total e XML malformado de chamadas de ferramentas do MiniMax antes da redação/truncamento.

* * *

## Armadilha comum: "non-main"

* * *

## Testes

Depois de configurar sandbox e ferramentas multiagente:

* ### Verificar a resolução de agentes

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

* ### Verificar contêineres de sandbox

bashCopy code
[code]
    docker ps --filter "name=openclaw-sbx-"
[/code]

* ### Testar restrições de ferramentas

  * Envie uma mensagem que exija ferramentas restritas.
  * Verifique se o agente não consegue usar ferramentas negadas.


* ### Monitorar logs

bashCopy code
[code]
    tail -f "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/logs/gateway.log" | grep -E "routing|sandbox|tools"
[/code]

* * *

## Solução de problemas

Agente não está em sandbox apesar de `mode: 'all'`

  * Verifique se há um `agents.defaults.sandbox.mode` global que o substitui.
  * A configuração específica do agente tem precedência, portanto defina `agents.list[].sandbox.mode: "all"`.

Ferramentas ainda disponíveis apesar da lista de negação

  * Verifique a ordem de filtragem de ferramentas: global → agente → sandbox → subagente.
  * Cada nível só pode restringir ainda mais, não conceder de volta.
  * Verifique com os logs: `[tools] filtering tools for agent:${agentId}`.

Contêiner não isolado por agente

  * Defina `scope: "agent"` na configuração de sandbox específica do agente.
  * O padrão é `"session"`, que cria um contêiner por sessão.


* * *

## Relacionado

  * [Modo elevado](</pt-BR/tools/elevated>)
  * [Roteamento multiagente](</pt-BR/concepts/multi-agent>)
  * [Configuração de sandbox](</pt-BR/gateway/config-agents#agentsdefaultssandbox>)
  * [Sandbox vs política de ferramentas vs elevado](</pt-BR/gateway/sandbox-vs-tool-policy-vs-elevated>) — depuração de "por que isso está bloqueado?"
  * [Sandboxing](</pt-BR/gateway/sandboxing>) — referência completa de sandbox (modos, escopos, backends, imagens)
  * [Gerenciamento de sessão](</pt-BR/concepts/session>)


Was this useful?YesNo