---
title: Fluxos (redirecionamento)
source_url: https://docs.openclaw.ai/pt-BR/cli/flows
scraped_at: 2026-05-25
---

# `openclaw tasks flow`

Não há comando de nível superior `openclaw flows`. A inspeção durável de TaskFlow fica em `openclaw tasks flow`.

## Subcomandos

bashCopy code
[code]
    openclaw tasks flow list   [--json] [--status <name>]openclaw tasks flow show   <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Subcomando | Descrição | Argumentos / opções  
---|---|---  
`list` | Lista TaskFlows rastreados. | Saída legível por máquina com `--json`; filtro `--status <name>` (veja os valores de status abaixo).  
`show` | Mostra um TaskFlow. | `<lookup>` ID do fluxo ou chave do proprietário; saída legível por máquina com `--json`.  
`cancel` | Cancela um TaskFlow em execução. | `<lookup>` ID do fluxo ou chave do proprietário.  
  
`<lookup>` aceita um ID de fluxo (retornado por `list` / `show`) ou a chave do proprietário do fluxo (o identificador estável que o subsistema responsável usa para rastrear o fluxo).

### Valores do filtro de status

`--status` em `list` aceita um de:

`queued`, `running`, `waiting`, `blocked`, `succeeded`, `failed`, `cancelled`, `lost`

## Exemplos

bashCopy code
[code]
    openclaw tasks flow listopenclaw tasks flow list --status runningopenclaw tasks flow list --jsonopenclaw tasks flow show flow_abc123openclaw tasks flow show flow_abc123 --jsonopenclaw tasks flow cancel flow_abc123
[/code]

Para ver os conceitos completos de TaskFlow e criação, consulte [TaskFlow](</pt-BR/automation/taskflow>). Para o comando pai `tasks`, consulte [referência da CLI de tasks](</pt-BR/cli/tasks>).

## Relacionados

  * [Referência da CLI](</pt-BR/cli>)
  * [Automação](</pt-BR/automation>)
  * [TaskFlow](</pt-BR/automation/taskflow>)


Was this useful?YesNo