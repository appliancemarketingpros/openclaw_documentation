---
title: Grupos de transmissão
source_url: https://docs.openclaw.ai/pt-BR/channels/broadcast-groups
scraped_at: 2026-05-25
---

## Visão geral

Broadcast Groups permitem que vários agentes processem e respondam à mesma mensagem simultaneamente. Isso permite criar equipes de agentes especializados que trabalham juntas em um único grupo ou DM do WhatsApp — tudo usando um único número de telefone.

Escopo atual: **somente WhatsApp** (canal web).

Broadcast groups são avaliados após allowlists de canais e regras de ativação de grupos. Em grupos do WhatsApp, isso significa que broadcasts acontecem quando o OpenClaw normalmente responderia (por exemplo: em uma menção, dependendo das configurações do seu grupo).

## Casos de uso

1\. Equipes de agentes especializados

Implante vários agentes com responsabilidades atômicas e focadas:

CodeCopy code
[code]
    Group: "Development Team"Agents:  - CodeReviewer (reviews code snippets)  - DocumentationBot (generates docs)  - SecurityAuditor (checks for vulnerabilities)  - TestGenerator (suggests test cases)
[/code]

Cada agente processa a mesma mensagem e fornece sua perspectiva especializada.

2\. Suporte multilíngue CodeCopy code
[code]
    Group: "International Support"Agents:  - Agent_EN (responds in English)  - Agent_DE (responds in German)  - Agent_ES (responds in Spanish)
[/code]

3\. Fluxos de trabalho de garantia de qualidade CodeCopy code
[code]
    Group: "Customer Support"Agents:  - SupportAgent (provides answer)  - QAAgent (reviews quality, only responds if issues found)
[/code]

4\. Automação de tarefas CodeCopy code
[code]
    Group: "Project Management"Agents:  - TaskTracker (updates task database)  - TimeLogger (logs time spent)  - ReportGenerator (creates summaries)
[/code]

## Configuração

### Configuração básica

Adicione uma seção `broadcast` de nível superior (ao lado de `bindings`). As chaves são ids de pares do WhatsApp:

  * conversas em grupo: JID do grupo (por exemplo, `120363403215116621@g.us`)
  * DMs: número de telefone E.164 (por exemplo, `+15551234567`)

jsonCopy code
[code]
    {  "broadcast": {    "120363403215116621@g.us": ["alfred", "baerbel", "assistant3"]  }}
[/code]

**Resultado:** Quando o OpenClaw responderia nesta conversa, ele executará todos os três agentes.

### Estratégia de processamento

Controle como os agentes processam mensagens:

### parallel (padrão)

Todos os agentes processam simultaneamente:

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### sequential

Os agentes processam em ordem (um espera o anterior terminar):

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### Exemplo completo

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "code-reviewer",        "name": "Code Reviewer",        "workspace": "/path/to/code-reviewer",        "sandbox": { "mode": "all" }      },      {        "id": "security-auditor",        "name": "Security Auditor",        "workspace": "/path/to/security-auditor",        "sandbox": { "mode": "all" }      },      {        "id": "docs-generator",        "name": "Documentation Generator",        "workspace": "/path/to/docs-generator",        "sandbox": { "mode": "all" }      }    ]  },  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["code-reviewer", "security-auditor", "docs-generator"],    "120363424282127706@g.us": ["support-en", "support-de"],    "+15555550123": ["assistant", "logger"]  }}
[/code]

## Como funciona

### Fluxo de mensagens

* ### Mensagem recebida chega

Uma mensagem de grupo ou DM do WhatsApp chega.

* ### Verificação de broadcast

O sistema verifica se o ID do par está em `broadcast`.

* ### Se estiver na lista de broadcast

  * Todos os agentes listados processam a mensagem.
  * Cada agente tem sua própria chave de sessão e contexto isolado.
  * Os agentes processam em paralelo (padrão) ou sequencialmente.


* ### Se não estiver na lista de broadcast

O roteamento normal se aplica (primeiro binding correspondente).

### Isolamento de sessão

Cada agente em um broadcast group mantém completamente separados:

  * **Chaves de sessão** (`agent:alfred:whatsapp:group:120363...` vs `agent:baerbel:whatsapp:group:120363...`)
  * **Histórico de conversa** (o agente não vê as mensagens dos outros agentes)
  * **Workspace** (sandboxes separados, se configurados)
  * **Acesso a ferramentas** (listas de permissão/negação diferentes)
  * **Memória/contexto** ([IDENTITY.md](<http://IDENTITY.md>), [SOUL.md](<http://SOUL.md>), etc. separados)
  * **Buffer de contexto do grupo** (mensagens recentes do grupo usadas como contexto) é compartilhado por par, então todos os agentes de broadcast veem o mesmo contexto quando acionados


Isso permite que cada agente tenha:

  * Personalidades diferentes
  * Acesso a ferramentas diferente (por exemplo, somente leitura vs. leitura e escrita)
  * Modelos diferentes (por exemplo, opus vs. sonnet)
  * Skills diferentes instaladas


### Exemplo: sessões isoladas

No grupo `120363403215116621@g.us` com agentes `["alfred", "baerbel"]`:

### Contexto do Alfred

CodeCopy code
[code]
    Session: agent:alfred:whatsapp:group:120363403215116621@g.usHistory: [user message, alfred's previous responses]Workspace: /Users/user/openclaw-alfred/Tools: read, write, exec
[/code]

### Contexto da Bärbel

CodeCopy code
[code]
    Session: agent:baerbel:whatsapp:group:120363403215116621@g.usHistory: [user message, baerbel's previous responses]Workspace: /Users/user/openclaw-baerbel/Tools: read only
[/code]

## Práticas recomendadas

1\. Mantenha os agentes focados

Projete cada agente com uma responsabilidade única e clara:

jsonCopy code
[code]
    {  "broadcast": {    "DEV_GROUP": ["formatter", "linter", "tester"]  }}
[/code]

✅ **Bom:** Cada agente tem uma função. ❌ **Ruim:** Um agente genérico "dev-helper".

2\. Use nomes descritivos

Deixe claro o que cada agente faz:

jsonCopy code
[code]
    {  "agents": {    "security-scanner": { "name": "Security Scanner" },    "code-formatter": { "name": "Code Formatter" },    "test-generator": { "name": "Test Generator" }  }}
[/code]

3\. Configure acessos diferentes a ferramentas

Dê aos agentes apenas as ferramentas de que precisam:

jsonCopy code
[code]
    {  "agents": {    "reviewer": {      "tools": { "allow": ["read", "exec"] }    },    "fixer": {      "tools": { "allow": ["read", "write", "edit", "exec"] }    }  }}
[/code]

`reviewer` é somente leitura. `fixer` pode ler e escrever.

4\. Monitore o desempenho

Com muitos agentes, considere:

  * Usar `"strategy": "parallel"` (padrão) para velocidade
  * Limitar broadcast groups a 5-10 agentes
  * Usar modelos mais rápidos para agentes mais simples

5\. Lide com falhas com elegância

Agentes falham de forma independente. O erro de um agente não bloqueia os outros:

CodeCopy code
[code]
    Message → [Agent A ✓, Agent B ✗ error, Agent C ✓]Result: Agent A and C respond, Agent B logs error
[/code]

## Compatibilidade

### Providers

Broadcast groups atualmente funcionam com:

  * ✅ WhatsApp (implementado)
  * 🚧 Telegram (planejado)
  * 🚧 Discord (planejado)
  * 🚧 Slack (planejado)


### Roteamento

Broadcast groups funcionam junto com o roteamento existente:

jsonCopy code
[code]
    {  "bindings": [    {      "match": { "channel": "whatsapp", "peer": { "kind": "group", "id": "GROUP_A" } },      "agentId": "alfred"    }  ],  "broadcast": {    "GROUP_B": ["agent1", "agent2"]  }}
[/code]

  * `GROUP_A`: Somente alfred responde (roteamento normal).
  * `GROUP_B`: agent1 E agent2 respondem (broadcast).


## Solução de problemas

Agentes não respondem

**Verifique:**

  1. Os IDs dos agentes existem em `agents.list`.
  2. O formato do ID do par está correto (por exemplo, `120363403215116621@g.us`).
  3. Os agentes não estão em listas de negação.


**Depuração:**

bashCopy code
[code]
    tail -f ~/.openclaw/logs/gateway.log | grep broadcast
[/code]

Apenas um agente responde

**Causa:** O ID do par pode estar em `bindings`, mas não em `broadcast`.

**Correção:** Adicione à configuração de broadcast ou remova de bindings.

Problemas de desempenho

Se ficar lento com muitos agentes:

  * Reduza o número de agentes por grupo.
  * Use modelos mais leves (sonnet em vez de opus).
  * Verifique o tempo de inicialização do sandbox.


## Exemplos

Exemplo 1: Equipe de revisão de código jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": [      "code-formatter",      "security-scanner",      "test-coverage",      "docs-checker"    ]  },  "agents": {    "list": [      {        "id": "code-formatter",        "workspace": "~/agents/formatter",        "tools": { "allow": ["read", "write"] }      },      {        "id": "security-scanner",        "workspace": "~/agents/security",        "tools": { "allow": ["read", "exec"] }      },      {        "id": "test-coverage",        "workspace": "~/agents/testing",        "tools": { "allow": ["read", "exec"] }      },      { "id": "docs-checker", "workspace": "~/agents/docs", "tools": { "allow": ["read"] } }    ]  }}
[/code]

**Usuário envia:** Trecho de código.

**Respostas:**

  * code-formatter: "Corrigi a indentação e adicionei dicas de tipo"
  * security-scanner: "⚠️ Vulnerabilidade de injeção de SQL na linha 12"
  * test-coverage: "A cobertura é de 45%, faltam testes para casos de erro"
  * docs-checker: "Docstring ausente para a função `process_data`"

Exemplo 2: Suporte multilíngue jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "+15555550123": ["detect-language", "translator-en", "translator-de"]  },  "agents": {    "list": [      { "id": "detect-language", "workspace": "~/agents/lang-detect" },      { "id": "translator-en", "workspace": "~/agents/translate-en" },      { "id": "translator-de", "workspace": "~/agents/translate-de" }    ]  }}
[/code]

## Referência da API

### Esquema de configuração

typescriptCopy code
[code]
    interface OpenClawConfig {  broadcast?: {    strategy?: "parallel" | "sequential";    [peerId: string]: string[];  };}
[/code]

### Campos

Como processar agentes. `parallel` executa todos os agentes simultaneamente; `sequential` os executa na ordem do array.

JID de grupo do WhatsApp, número E.164 ou outro ID de par. O valor é o array de IDs de agentes que devem processar mensagens.

## Limitações

  1. **Máximo de agentes:** Sem limite rígido, mas 10+ agentes podem ser lentos.
  2. **Contexto compartilhado:** Os agentes não veem as respostas uns dos outros (por design).
  3. **Ordem das mensagens:** Respostas paralelas podem chegar em qualquer ordem.
  4. **Limites de taxa:** Todos os agentes contam para os limites de taxa do WhatsApp.


## Melhorias futuras

Recursos planejados:

  * [ ] Modo de contexto compartilhado (agentes veem as respostas uns dos outros)
  * [ ] Coordenação de agentes (agentes podem sinalizar uns aos outros)
  * [ ] Seleção dinâmica de agentes (escolher agentes com base no conteúdo da mensagem)
  * [ ] Prioridades de agentes (alguns agentes respondem antes de outros)


## Relacionado

  * [Roteamento de canais](</pt-BR/channels/channel-routing>)
  * [Grupos](</pt-BR/channels/groups>)
  * [Ferramentas de sandbox multiagente](</pt-BR/tools/multi-agent-sandbox-tools>)
  * [Emparelhamento](</pt-BR/channels/pairing>)
  * [Gerenciamento de sessões](</pt-BR/concepts/session>)


Was this useful?YesNo