---
title: Pareamento
source_url: https://docs.openclaw.ai/pt-BR/cli/pairing
scraped_at: 2026-05-25
---

# `openclaw pairing`

Aprove ou inspecione solicitações de pareamento por DM (para canais compatíveis com pareamento).

Relacionado:

  * Fluxo de pareamento: [Pareamento](</pt-BR/channels/pairing>)


## Comandos

bashCopy code
[code]
    openclaw pairing list telegramopenclaw pairing list --channel telegram --account workopenclaw pairing list telegram --json openclaw pairing approve <code>openclaw pairing approve telegram <code>openclaw pairing approve --channel telegram --account work <code> --notify
[/code]

## `pairing list`

Liste solicitações de pareamento pendentes para um canal.

Opções:

  * `[channel]`: ID de canal posicional
  * `--channel <channel>`: ID de canal explícito
  * `--account <accountId>`: ID da conta para canais com várias contas
  * `--json`: saída legível por máquina


Observações:

  * Se vários canais compatíveis com pareamento estiverem configurados, você deve fornecer um canal posicionalmente ou com `--channel`.
  * Canais de Plugin são permitidos desde que o ID do canal seja válido.


## `pairing approve`

Aprove um código de pareamento pendente e permita esse remetente.

Uso:

  * `openclaw pairing approve <channel> <code>`
  * `openclaw pairing approve --channel <channel> <code>`
  * `openclaw pairing approve <code>` quando exatamente um canal compatível com pareamento estiver configurado


Opções:

  * `--channel <channel>`: ID de canal explícito
  * `--account <accountId>`: ID da conta para canais com várias contas
  * `--notify`: envia uma confirmação de volta ao solicitante no mesmo canal


Inicialização do proprietário:

  * Se `commands.ownerAllowFrom` estiver vazio quando você aprovar um código de pareamento, o OpenClaw também registra o remetente aprovado como proprietário dos comandos, usando uma entrada com escopo de canal, como `telegram:123456789`.
  * Isso inicializa apenas o primeiro proprietário. Aprovações de pareamento posteriores não substituem nem expandem `commands.ownerAllowFrom`.
  * O proprietário dos comandos é a conta do operador humano autorizada a executar comandos exclusivos do proprietário e aprovar ações perigosas, como `/diagnostics`, `/export-trajectory`, `/config` e aprovações de exec.


## Observações

  * Entrada de canal: passe-a posicionalmente (`pairing list telegram`) ou com `--channel <channel>`.
  * `pairing list` aceita `--account <accountId>` para canais com várias contas.
  * `pairing approve` aceita `--account <accountId>` e `--notify`.
  * Se apenas um canal compatível com pareamento estiver configurado, `pairing approve <code>` é permitido.
  * Se você aprovou um remetente antes de essa inicialização existir, execute `openclaw doctor`; ele avisa quando nenhum proprietário de comandos está configurado e mostra o comando `openclaw config set commands.ownerAllowFrom ...` para corrigir isso.


## Relacionado

  * [Referência da CLI](</pt-BR/cli>)
  * [Pareamento de canais](</pt-BR/channels/pairing>)


Was this useful?YesNo