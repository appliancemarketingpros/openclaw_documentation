---
title: Nodes
source_url: https://docs.openclaw.ai/pt-BR/cli/nodes
scraped_at: 2026-05-25
---

# `openclaw nodes`

Gerencie nós (dispositivos) pareados e invoque capacidades de nós.

Relacionado:

  * Visão geral dos nós: [Nós](</pt-BR/nodes>)
  * Câmera: [Nós de câmera](</pt-BR/nodes/camera>)
  * Imagens: [Nós de imagem](</pt-BR/nodes/images>)


Opções comuns:

  * `--url`, `--token`, `--timeout`, `--json`


## Comandos comuns

bashCopy code
[code]
    openclaw nodes listopenclaw nodes list --connectedopenclaw nodes list --last-connected 24hopenclaw nodes pendingopenclaw nodes approve <requestId>openclaw nodes reject <requestId>openclaw nodes remove --node <id|name|ip>openclaw nodes rename --node <id|name|ip> --name <displayName>openclaw nodes statusopenclaw nodes status --connectedopenclaw nodes status --last-connected 24h
[/code]

`nodes list` imprime tabelas de pendentes/pareados. As linhas pareadas incluem a idade da conexão mais recente (Última conexão). Use `--connected` para mostrar apenas nós conectados no momento. Use `--last-connected <duration>` para filtrar para nós que se conectaram dentro de uma duração (por exemplo, `24h`, `7d`). Use `nodes remove --node <id|name|ip>` para excluir um registro obsoleto de pareamento de nó pertencente ao Gateway.

Observação sobre aprovação:

  * `openclaw nodes pending` precisa apenas do escopo de pareamento.
  * `gateway.nodes.pairing.autoApproveCidrs` pode pular a etapa de pendência apenas para pareamento de dispositivo `role: node` explicitamente confiável e de primeira vez. Ele fica desativado por padrão e não aprova upgrades.
  * `openclaw nodes approve <requestId>` herda requisitos de escopo extras da solicitação pendente: 
    * solicitação sem comando: somente pareamento
    * comandos de nó sem exec: pareamento + escrita
    * `system.run` / `system.run.prepare` / `system.which`: pareamento + admin


## Invocar

bashCopy code
[code]
    openclaw nodes invoke --node <id|name|ip> --command <command> --params <json>
[/code]

Flags de invocação:

  * `--params <json>`: string de objeto JSON (padrão `{}`).
  * `--invoke-timeout <ms>`: tempo limite de invocação do nó (padrão `15000`).
  * `--idempotency-key <key>`: chave de idempotência opcional.
  * `system.run` e `system.run.prepare` são bloqueados aqui; use a ferramenta `exec` com `host=node` para execução no shell.


Para execução no shell em um nó, use a ferramenta `exec` com `host=node` em vez de `openclaw nodes run`. A CLI `nodes` agora é focada em capacidades: RPC direto via `nodes invoke`, além de pareamento, câmera, tela, localização, Canvas e notificações. Os comandos de Canvas são implementados pelo Plugin experimental Canvas incluído; o core mantém um gancho de compatibilidade para que eles permaneçam em `openclaw nodes canvas`.

## Relacionado

  * [Referência da CLI](</pt-BR/cli>)
  * [Nós](</pt-BR/nodes>)


Was this useful?YesNo