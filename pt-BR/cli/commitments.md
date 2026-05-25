---
title: `openclaw commitments`
source_url: https://docs.openclaw.ai/pt-BR/cli/commitments
scraped_at: 2026-05-25
---

Liste e gerencie compromissos de acompanhamento inferidos.

Compromissos são memórias de acompanhamento opcionais e de curta duração criadas a partir do contexto da conversa. Consulte [Compromissos inferidos](</pt-BR/concepts/commitments>) para o guia conceitual.

Sem subcomando, `openclaw commitments` lista os compromissos pendentes.

## Uso

bashCopy code
[code]
    openclaw commitments [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments list [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments dismiss <id...> [--json]
[/code]

## Opções

  * `--all`: mostra todos os status em vez de apenas os compromissos pendentes.
  * `--agent <id>`: filtra para um id de agente.
  * `--status <status>`: filtra por status. Valores: `pending`, `sent`, `dismissed`, `snoozed` ou `expired`.
  * `--json`: gera JSON legível por máquina.


## Exemplos

Listar compromissos pendentes:

bashCopy code
[code]
    openclaw commitments
[/code]

Listar todos os compromissos armazenados:

bashCopy code
[code]
    openclaw commitments --all
[/code]

Filtrar para um agente:

bashCopy code
[code]
    openclaw commitments --agent main
[/code]

Encontrar compromissos adiados:

bashCopy code
[code]
    openclaw commitments --status snoozed
[/code]

Dispensar um ou mais compromissos:

bashCopy code
[code]
    openclaw commitments dismiss cm_abc123 cm_def456
[/code]

Exportar como JSON:

bashCopy code
[code]
    openclaw commitments --all --json
[/code]

## Saída

A saída em texto inclui:

  * id do compromisso
  * status
  * tipo
  * horário de vencimento mais cedo
  * escopo
  * texto de check-in sugerido


A saída JSON também inclui o caminho do armazenamento de compromissos e os registros armazenados completos.

## Relacionado

  * [Compromissos inferidos](</pt-BR/concepts/commitments>)
  * [Visão geral da memória](</pt-BR/concepts/memory>)
  * [Heartbeat](</pt-BR/gateway/heartbeat>)
  * [Tarefas agendadas](</pt-BR/automation/cron-jobs>)


Was this useful?YesNo