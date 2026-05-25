---
title: Sessões
source_url: https://docs.openclaw.ai/pt-BR/cli/sessions
scraped_at: 2026-05-25
---

# `openclaw sessions`

Lista sessões de conversa armazenadas.

As listas de sessões não são verificações de disponibilidade de canais/provedores. Elas mostram linhas de conversa persistidas dos armazenamentos de sessão. Um Discord, Slack, Telegram ou outro canal silencioso pode se reconectar com sucesso sem criar uma nova linha de sessão até que uma mensagem seja processada. Use `openclaw channels status --probe`, `openclaw status --deep` ou `openclaw health --verbose` quando precisar de conectividade de canal ao vivo.

As respostas de `openclaw sessions` e `sessions.list` do Gateway são limitadas por padrão para que armazenamentos grandes e de longa duração não monopolizem o processo da CLI ou o loop de eventos do Gateway. A CLI retorna as 100 sessões mais recentes por padrão; passe `--limit <n>` para uma janela menor/maior ou `--limit all` quando você precisar intencionalmente do armazenamento completo. As respostas JSON incluem `totalCount`, `limitApplied` e `hasMore` quando os chamadores precisam mostrar que existem mais linhas.

Clientes RPC podem passar `configuredAgentsOnly: true` para manter a fonte ampla e combinada de descoberta, mas retornar apenas linhas de agentes atualmente presentes na configuração. A UI de controle usa esse modo por padrão para que armazenamentos de agentes excluídos ou apenas em disco não reapareçam na visualização Sessões.

bashCopy code
[code]
    openclaw sessionsopenclaw sessions --agent workopenclaw sessions --all-agentsopenclaw sessions --active 120openclaw sessions --limit 25openclaw sessions --verboseopenclaw sessions --json
[/code]

Seleção de escopo:

  * padrão: armazenamento do agente padrão configurado
  * `--verbose`: registro detalhado
  * `--agent <id>`: um armazenamento de agente configurado
  * `--all-agents`: agrega todos os armazenamentos de agentes configurados
  * `--store <path>`: caminho de armazenamento explícito (não pode ser combinado com `--agent` ou `--all-agents`)
  * `--limit <n|all>`: máximo de linhas a exibir (padrão `100`; `all` restaura a saída completa)


Exporte um pacote de trajetória para uma sessão armazenada:

bashCopy code
[code]
    openclaw sessions export-trajectory --session-key "agent:main:telegram:direct:123" --workspace .openclaw sessions export-trajectory --session-key "agent:main:telegram:direct:123" --output bug-123 --json
[/code]

Esse é o caminho de comando usado pelo comando de barra `/export-trajectory` depois que o proprietário aprova a solicitação de exec. O diretório de saída é sempre resolvido dentro de `.openclaw/trajectory-exports/` no workspace selecionado.

`openclaw sessions --all-agents` lê armazenamentos de agentes configurados. A descoberta de sessões do Gateway e do ACP é mais ampla: ela também inclui armazenamentos apenas em disco encontrados sob a raiz padrão `agents/` ou uma raiz `session.store` modelada. Esses armazenamentos descobertos precisam resolver para arquivos `sessions.json` regulares dentro da raiz do agente; symlinks e caminhos fora da raiz são ignorados.

Exemplos JSON:

`openclaw sessions --all-agents --json`:

jsonCopy code
[code]
    {  "path": null,  "stores": [    { "agentId": "main", "path": "/home/user/.openclaw/agents/main/sessions/sessions.json" },    { "agentId": "work", "path": "/home/user/.openclaw/agents/work/sessions/sessions.json" }  ],  "allAgents": true,  "count": 2,  "totalCount": 2,  "limitApplied": 100,  "hasMore": false,  "activeMinutes": null,  "sessions": [    { "agentId": "main", "key": "agent:main:main", "model": "gpt-5" },    { "agentId": "work", "key": "agent:work:main", "model": "claude-opus-4-6" }  ]}
[/code]

## Manutenção de limpeza

Execute a manutenção agora (em vez de esperar o próximo ciclo de escrita):

bashCopy code
[code]
    openclaw sessions cleanup --dry-runopenclaw sessions cleanup --agent work --dry-runopenclaw sessions cleanup --all-agents --dry-runopenclaw sessions cleanup --enforceopenclaw sessions cleanup --enforce --active-key "agent:main:telegram:direct:123"openclaw sessions cleanup --dry-run --fix-dm-scopeopenclaw sessions cleanup --json
[/code]

`openclaw sessions cleanup` usa as configurações de `session.maintenance` da configuração:

  * Observação de escopo: `openclaw sessions cleanup` mantém armazenamentos de sessão, transcrições e arquivos auxiliares de trajetória. Ele não remove logs de execuções de Cron (`cron/runs/<jobId>.jsonl`), que são gerenciados por `cron.runLog.maxBytes` e `cron.runLog.keepLines` em [configuração de Cron](</pt-BR/automation/cron-jobs#configuration>) e explicados em [manutenção de Cron](</pt-BR/automation/cron-jobs#maintenance>).

  * A limpeza também remove transcrições primárias não referenciadas, pontos de verificação de Compaction e arquivos auxiliares de trajetória mais antigos que `session.maintenance.pruneAfter`; arquivos ainda referenciados por `sessions.json` são preservados.

  * `--dry-run`: pré-visualiza quantas entradas seriam removidas/limitadas sem escrever.

    * Em modo texto, a simulação imprime uma tabela de ações por sessão (`Action`, `Key`, `Age`, `Model`, `Flags`) para que você possa ver o que seria mantido versus removido.
  * `--enforce`: aplica a manutenção mesmo quando `session.maintenance.mode` é `warn`.

  * `--fix-missing`: remove entradas cujos arquivos de transcrição estão ausentes, mesmo que elas ainda normalmente não fossem removidas por idade/contagem.

  * `--fix-dm-scope`: quando `session.dmScope` é `main`, aposenta linhas antigas de DM direto com chave por par deixadas por roteamentos anteriores `per-peer`, `per-channel-peer` ou `per-account-channel-peer`. Use `--dry-run` primeiro; aplicar a limpeza remove essas linhas de `sessions.json` e preserva suas transcrições como arquivos excluídos.

  * `--active-key <key>`: protege uma chave ativa específica contra despejo por orçamento de disco. Ponteiros duráveis de conversas externas, como sessões de grupo e sessões de chat com escopo de thread, também são mantidos pela manutenção por idade/contagem/orçamento de disco.

  * `--agent <id>`: executa a limpeza para um armazenamento de agente configurado.

  * `--all-agents`: executa a limpeza para todos os armazenamentos de agentes configurados.

  * `--store <path>`: executa contra um arquivo `sessions.json` específico.

  * `--json`: imprime um resumo JSON. Com `--all-agents`, a saída inclui um resumo por armazenamento.


Quando um Gateway está acessível, a limpeza que não é simulação para armazenamentos de agentes configurados é enviada pelo Gateway para compartilhar o mesmo gravador de armazenamento de sessão do tráfego em tempo de execução. Use `--store <path>` para o reparo offline explícito de um arquivo de armazenamento.

`openclaw sessions cleanup --all-agents --dry-run --json`:

jsonCopy code
[code]
    {  "allAgents": true,  "mode": "warn",  "dryRun": true,  "stores": [    {      "agentId": "main",      "storePath": "/home/user/.openclaw/agents/main/sessions/sessions.json",      "beforeCount": 120,      "afterCount": 80,      "missing": 0,      "dmScopeRetired": 0,      "pruned": 40,      "capped": 0    },    {      "agentId": "work",      "storePath": "/home/user/.openclaw/agents/work/sessions/sessions.json",      "beforeCount": 18,      "afterCount": 18,      "missing": 0,      "dmScopeRetired": 0,      "pruned": 0,      "capped": 0    }  ]}
[/code]

Relacionado:

  * Configuração de sessão: [Referência de configuração](</pt-BR/gateway/config-agents#session>)


## Relacionado

  * [Referência da CLI](</pt-BR/cli>)
  * [Gerenciamento de sessões](</pt-BR/concepts/session>)


Was this useful?YesNo