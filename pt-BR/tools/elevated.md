---
title: Modo elevado
source_url: https://docs.openclaw.ai/pt-BR/tools/elevated
scraped_at: 2026-05-25
---

Quando um agente é executado dentro de um sandbox, seus comandos `exec` ficam confinados ao ambiente do sandbox. O **modo elevado** permite que o agente saia dele e execute comandos fora do sandbox, com portões de aprovação configuráveis.

## Diretivas

Controle o modo elevado por sessão com comandos de barra:

Diretiva | O que faz  
---|---  
`/elevated on` | Executa fora do sandbox no caminho de host configurado, mantém aprovações  
`/elevated ask` | Igual a `on` (alias)  
`/elevated full` | Executa fora do sandbox no caminho de host configurado e ignora aprovações  
`/elevated off` | Retorna à execução confinada ao sandbox  
  
Também disponível como `/elev on|off|ask|full`.

Envie `/elevated` sem argumento para ver o nível atual.

## Como funciona

* ### Check availability

O modo elevado deve estar habilitado na configuração e o remetente deve estar na lista de permissões:

json5Copy code
[code]
    {  tools: {    elevated: {      enabled: true,      allowFrom: {        discord: ["user-id-123"],        whatsapp: ["+15555550123"],      },    },  },}
[/code]

* ### Set the level

Envie uma mensagem contendo apenas a diretiva para definir o padrão da sessão:

CodeCopy code
[code]
    /elevated full
[/code]

Ou use-a em linha (aplica-se apenas a essa mensagem):

CodeCopy code
[code]
    /elevated on run the deployment script
[/code]

* ### Commands run outside the sandbox

Com o modo elevado ativo, chamadas `exec` saem do sandbox. O host efetivo é `gateway` por padrão, ou `node` quando o destino exec configurado/da sessão é `node`. No modo `full`, aprovações de exec são ignoradas. No modo `on`/`ask`, as regras de aprovação configuradas ainda se aplicam.

## Ordem de resolução

  1. **Diretiva em linha** na mensagem (aplica-se apenas a essa mensagem)
  2. **Substituição de sessão** (definida ao enviar uma mensagem contendo apenas a diretiva)
  3. **Padrão global** (`agents.defaults.elevatedDefault` na configuração)


## Disponibilidade e listas de permissões

  * **Portão global** : `tools.elevated.enabled` (deve ser `true`)
  * **Lista de permissões de remetentes** : `tools.elevated.allowFrom` com listas por canal
  * **Portão por agente** : `agents.list[].tools.elevated.enabled` (só pode restringir ainda mais)
  * **Lista de permissões por agente** : `agents.list[].tools.elevated.allowFrom` (o remetente deve corresponder à global e à por agente)
  * **Fallback do Discord** : se `tools.elevated.allowFrom.discord` for omitido, `channels.discord.allowFrom` será usado como fallback
  * **Todos os portões devem passar** ; caso contrário, o modo elevado é tratado como indisponível


Formatos de entradas da lista de permissões:

Prefixo | Corresponde a  
---|---  
(nenhum) | ID do remetente, E.164 ou campo From  
`name:` | Nome de exibição do remetente  
`username:` | Nome de usuário do remetente  
`tag:` | Tag do remetente  
`id:`, `from:`, `e164:` | Direcionamento explícito de identidade  
  
## O que o modo elevado não controla

  * **Política de ferramenta** : se `exec` for negado pela política de ferramenta, o modo elevado não pode substituir isso.
  * **Política de seleção de host** : o modo elevado não transforma `auto` em uma substituição livre entre hosts. Ele usa as regras de destino exec configuradas/da sessão, escolhendo `node` somente quando o destino já é `node`.
  * **Separado de`/exec`**: a diretiva `/exec` ajusta padrões exec por sessão para remetentes autorizados e não exige modo elevado.


## Relacionados

[**Exec tool** Execução de comandos shell a partir do agente. ](</pt-BR/tools/exec>) [**Exec approvals** Sistema de aprovação e lista de permissões para `exec`. ](</pt-BR/tools/exec-approvals>) [**Sandboxing** Configuração de sandbox no nível do Gateway. ](</pt-BR/gateway/sandboxing>) [**Sandbox vs Tool Policy vs Elevated** Como os três portões se compõem durante uma chamada de ferramenta. ](</pt-BR/gateway/sandbox-vs-tool-policy-vs-elevated>)

Was this useful?YesNo