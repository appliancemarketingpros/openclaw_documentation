---
title: `openclaw tasks`
source_url: https://docs.openclaw.ai/pt-BR/cli/tasks
scraped_at: 2026-05-25
---

Inspecione tarefas duráveis em segundo plano e o estado do Task Flow. Sem subcomando, `openclaw tasks` é equivalente a `openclaw tasks list`.

Consulte [Tarefas em segundo plano](</pt-BR/automation/tasks>) para ver o ciclo de vida e o modelo de entrega.

## Uso

bashCopy code
[code]
    openclaw tasksopenclaw tasks listopenclaw tasks list --runtime acpopenclaw tasks list --status runningopenclaw tasks show <lookup>openclaw tasks notify <lookup> state_changesopenclaw tasks cancel <lookup>openclaw tasks auditopenclaw tasks maintenanceopenclaw tasks maintenance --applyopenclaw tasks flow listopenclaw tasks flow show <lookup>openclaw tasks flow cancel <lookup>
[/code]

## Opções raiz

  * `--json`: gera JSON.
  * `--runtime <name>`: filtra por tipo: `subagent`, `acp`, `cron` ou `cli`.
  * `--status <name>`: filtra por status: `queued`, `running`, `succeeded`, `failed`, `timed_out`, `cancelled` ou `lost`.


## Subcomandos

### `list`

bashCopy code
[code]
    openclaw tasks list [--runtime <name>] [--status <name>] [--json]
[/code]

Lista as tarefas em segundo plano rastreadas, da mais recente para a mais antiga.

### `show`

bashCopy code
[code]
    openclaw tasks show <lookup> [--json]
[/code]

Mostra uma tarefa por ID da tarefa, ID de execução ou chave de sessão.

### `notify`

bashCopy code
[code]
    openclaw tasks notify <lookup> <done_only|state_changes|silent>
[/code]

Altera a política de notificação de uma tarefa em execução.

### `cancel`

bashCopy code
[code]
    openclaw tasks cancel <lookup>
[/code]

Cancela uma tarefa em segundo plano em execução.

### `audit`

bashCopy code
[code]
    openclaw tasks audit [--severity <warn|error>] [--code <name>] [--limit <n>] [--json]
[/code]

Expõe registros de tarefas e de Task Flow obsoletos, perdidos, com falha de entrega ou inconsistentes de outra forma. Tarefas perdidas retidas até `cleanupAfter` são avisos; tarefas perdidas expiradas ou sem carimbo são erros.

### `maintenance`

bashCopy code
[code]
    openclaw tasks maintenance [--apply] [--json]
[/code]

Pré-visualiza ou aplica reconciliação de tarefas e de Task Flow, carimbo de limpeza, remoção, e limpeza de registro de sessões obsoletas de execuções Cron. Para tarefas Cron, a reconciliação usa logs de execução/estado de jobs persistidos antes de marcar uma tarefa ativa antiga como `lost`, para que execuções Cron concluídas não se tornem falsos erros de auditoria apenas porque o estado de runtime em memória do Gateway desapareceu. A auditoria offline da CLI não é autoritativa para o conjunto de jobs ativos de Cron local ao processo do Gateway. Tarefas da CLI com um ID de execução/ID de origem são marcadas como `lost` quando seu contexto de execução ativo do Gateway desaparece, mesmo que uma linha antiga de sessão filha permaneça. Quando aplicada, a manutenção também remove linhas do registro de sessões `cron:<jobId>:run:<uuid>` com mais de 7 dias, preservando jobs Cron em execução no momento e deixando linhas de sessão não Cron intocadas.

### `flow`

bashCopy code
[code]
    openclaw tasks flow list [--status <name>] [--json]openclaw tasks flow show <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Inspeciona ou cancela o estado durável de Task Flow sob o ledger de tarefas.

## Relacionados

  * [Referência da CLI](</pt-BR/cli>)
  * [Tarefas em segundo plano](</pt-BR/automation/tasks>)


Was this useful?YesNo