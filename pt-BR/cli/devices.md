---
title: Dispositivos
source_url: https://docs.openclaw.ai/pt-BR/cli/devices
scraped_at: 2026-05-25
---

# `openclaw devices`

Gerencie solicitações de pareamento de dispositivos e tokens com escopo de dispositivo.

## Comandos

### `openclaw devices list`

Liste solicitações de pareamento pendentes e dispositivos pareados.

CodeCopy code
[code]
    openclaw devices listopenclaw devices list --json
[/code]

A saída de solicitação pendente mostra o acesso solicitado ao lado do acesso atualmente aprovado do dispositivo quando ele já está pareado. Isso torna upgrades de escopo/função explícitos, em vez de parecer que o pareamento foi perdido.

### `openclaw devices remove <deviceId>`

Remova uma entrada de dispositivo pareado.

Quando você está autenticado com um token de dispositivo pareado, chamadores que não são administradores podem remover apenas a entrada de dispositivo **deles mesmos**. Remover outro dispositivo exige `operator.admin`.

CodeCopy code
[code]
    openclaw devices remove <deviceId>openclaw devices remove <deviceId> --json
[/code]

### `openclaw devices clear --yes [--pending]`

Limpe dispositivos pareados em massa.

CodeCopy code
[code]
    openclaw devices clear --yesopenclaw devices clear --yes --pendingopenclaw devices clear --yes --pending --json
[/code]

### `openclaw devices approve [requestId] [--latest]`

Aprove uma solicitação pendente de pareamento de dispositivo pelo `requestId` exato. Se `requestId` for omitido ou `--latest` for passado, o OpenClaw apenas imprime a solicitação pendente selecionada e sai; execute a aprovação novamente com o ID exato da solicitação depois de verificar os detalhes.

Se o dispositivo já estiver pareado e pedir escopos mais amplos ou uma função mais ampla, o OpenClaw mantém a aprovação existente e cria uma nova solicitação pendente de upgrade. Revise as colunas `Requested` vs `Approved` em `openclaw devices list` ou use `openclaw devices approve --latest` para pré-visualizar o upgrade exato antes de aprová-lo.

Se o Gateway estiver configurado explicitamente com `gateway.nodes.pairing.autoApproveCidrs`, solicitações iniciais de `role: node` de IPs de cliente correspondentes podem ser aprovadas antes de aparecerem nesta lista. Essa política fica desativada por padrão e nunca se aplica a clientes operador/navegador ou a solicitações de upgrade.

CodeCopy code
[code]
    openclaw devices approveopenclaw devices approve <requestId>openclaw devices approve --latest
[/code]

### `openclaw devices reject <requestId>`

Rejeite uma solicitação pendente de pareamento de dispositivo.

CodeCopy code
[code]
    openclaw devices reject <requestId>
[/code]

### `openclaw devices rotate --device <id> --role <role> [--scope <scope...>]`

Rotacione um token de dispositivo para uma função específica (opcionalmente atualizando escopos). A função de destino já deve existir no contrato de pareamento aprovado desse dispositivo; a rotação não pode emitir uma nova função não aprovada. Se você omitir `--scope`, reconexões posteriores com o token rotacionado armazenado reutilizam os escopos aprovados em cache desse token. Se você passar valores explícitos de `--scope`, eles se tornam o conjunto de escopos armazenado para futuras reconexões com token em cache. Chamadores com dispositivo pareado que não são administradores podem rotacionar apenas o token de dispositivo **deles mesmos**. O conjunto de escopos do token de destino deve permanecer dentro dos escopos de operador da própria sessão do chamador; a rotação não pode emitir nem preservar um token de operador mais amplo do que o chamador já possui.

CodeCopy code
[code]
    openclaw devices rotate --device <deviceId> --role operator --scope operator.read --scope operator.write
[/code]

Retorna metadados de rotação como JSON. Se o chamador estiver rotacionando o próprio token enquanto estiver autenticado com esse token de dispositivo, a resposta também inclui o token substituto para que o cliente possa persistí-lo antes de reconectar. Rotações compartilhadas/administrativas não ecoam o token bearer.

### `openclaw devices revoke --device <id> --role <role>`

Revogue um token de dispositivo para uma função específica.

Chamadores com dispositivo pareado que não são administradores podem revogar apenas o token de dispositivo **deles mesmos**. Revogar o token de outro dispositivo exige `operator.admin`. O conjunto de escopos do token de destino também deve caber dentro dos escopos de operador da própria sessão do chamador; chamadores apenas de pareamento não podem revogar tokens de operador admin/write.

CodeCopy code
[code]
    openclaw devices revoke --device <deviceId> --role node
[/code]

Retorna o resultado da revogação como JSON.

## Opções comuns

  * `--url <url>`: URL WebSocket do Gateway (usa `gateway.remote.url` por padrão quando configurado).
  * `--token <token>`: Token do Gateway (se necessário).
  * `--password <password>`: Senha do Gateway (autenticação por senha).
  * `--timeout <ms>`: Tempo limite de RPC.
  * `--json`: Saída JSON (recomendado para scripts).


## Observações

  * A rotação de token retorna um novo token (sensível). Trate-o como um segredo.
  * Estes comandos exigem o escopo `operator.pairing` (ou `operator.admin`). Algumas aprovações também exigem que o chamador tenha os escopos de operador que o dispositivo de destino emitiria ou herdaria; consulte [Escopos de operador](</pt-BR/gateway/operator-scopes>).
  * `gateway.nodes.pairing.autoApproveCidrs` é uma política opcional do Gateway apenas para pareamento inicial de dispositivo node; ela não altera a autoridade de aprovação da CLI.
  * A rotação e a revogação de tokens permanecem dentro do conjunto de funções de pareamento aprovado e da linha de base de escopos aprovada para esse dispositivo. Uma entrada de token em cache perdida não concede um alvo de gerenciamento de token.
  * Para sessões de token de dispositivo pareado, o gerenciamento entre dispositivos é apenas para admin: `remove`, `rotate` e `revoke` são apenas para o próprio dispositivo, a menos que o chamador tenha `operator.admin`.
  * A mutação de token também fica contida no escopo do chamador: uma sessão apenas de pareamento não pode rotacionar ou revogar um token que atualmente carrega `operator.admin` ou `operator.write`.
  * `devices clear` é intencionalmente protegido por `--yes`.
  * Se o escopo de pareamento estiver indisponível em local loopback (e nenhum `--url` explícito for passado), list/approve pode usar um fallback de pareamento local.
  * `devices approve` exige um ID de solicitação explícito antes de emitir tokens; omitir `requestId` ou passar `--latest` apenas pré-visualiza a solicitação pendente mais recente.


## Lista de verificação para recuperação de desvio de token

Use isto quando a Control UI ou outros clientes continuarem falhando com `AUTH_TOKEN_MISMATCH`, `AUTH_DEVICE_TOKEN_MISMATCH` ou `AUTH_SCOPE_MISMATCH`.

  1. Confirme a origem atual do token do gateway:

bashCopy code
[code]
    openclaw config get gateway.auth.token
[/code]

  2. Liste dispositivos pareados e identifique o id do dispositivo afetado:

bashCopy code
[code]
    openclaw devices list
[/code]

  3. Rotacione o token de operador para o dispositivo afetado:

bashCopy code
[code]
    openclaw devices rotate --device <deviceId> --role operator
[/code]

  4. Se a rotação não for suficiente, remova o pareamento obsoleto e aprove novamente:

bashCopy code
[code]
    openclaw devices remove <deviceId>openclaw devices listopenclaw devices approve <requestId>
[/code]

  5. Tente novamente a conexão do cliente com o token/senha compartilhado atual.


Observações:

  * A precedência normal de autenticação na reconexão é primeiro token/senha compartilhado explícito, depois `deviceToken` explícito, depois token de dispositivo armazenado e, por fim, token de bootstrap.
  * A recuperação confiável de `AUTH_TOKEN_MISMATCH` pode enviar temporariamente tanto o token compartilhado quanto o token de dispositivo armazenado juntos na única nova tentativa limitada.
  * `AUTH_SCOPE_MISMATCH` significa que o token de dispositivo foi reconhecido, mas não carrega o conjunto de escopos solicitado; corrija o contrato de aprovação de pareamento/escopo antes de alterar a autenticação compartilhada do gateway.


Relacionado:

  * [Solução de problemas de autenticação do dashboard](</pt-BR/web/dashboard#if-you-see-unauthorized-1008>)
  * [Solução de problemas do Gateway](</pt-BR/gateway/troubleshooting#dashboard-control-ui-connectivity>)


## Relacionado

  * [Referência da CLI](</pt-BR/cli>)
  * [Nodes](</pt-BR/nodes>)


Was this useful?YesNo