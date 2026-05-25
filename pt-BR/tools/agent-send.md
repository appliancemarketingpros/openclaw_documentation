---
title: Envio do agente
source_url: https://docs.openclaw.ai/pt-BR/tools/agent-send
scraped_at: 2026-05-25
---

`openclaw agent` executa um único turno de agente pela linha de comando sem precisar de uma mensagem de chat recebida. Use-o para fluxos de trabalho com scripts, testes e entrega programática.

## Início rápido

* ### Executar um turno de agente simples

bashCopy code
[code]
    openclaw agent --message "What is the weather today?"
[/code]

Isso envia a mensagem pelo Gateway e imprime a resposta.

* ### Direcionar para um agente ou sessão específica

bashCopy code
[code]
    # Target a specific agentopenclaw agent --agent ops --message "Summarize logs" # Target a phone number (derives session key)openclaw agent --to +15555550123 --message "Status update" # Reuse an existing sessionopenclaw agent --session-id abc123 --message "Continue the task"
[/code]

* ### Entregar a resposta a um canal

bashCopy code
[code]
    # Deliver to WhatsApp (default channel)openclaw agent --to +15555550123 --message "Report ready" --deliver # Deliver to Slackopenclaw agent --agent ops --message "Generate report" \  --deliver --reply-channel slack --reply-to "#reports"
[/code]

## Opções

Opção | Descrição  
---|---  
`--message \<text\>` | Mensagem a enviar (obrigatório)  
`--to \<dest\>` | Deriva a chave de sessão de um destino (telefone, id do chat)  
`--agent \<id\>` | Direciona para um agente configurado (usa sua sessão `main`)  
`--session-id \<id\>` | Reutiliza uma sessão existente pelo id  
`--local` | Força o runtime incorporado local (ignora o Gateway)  
`--deliver` | Envia a resposta para um canal de chat  
`--channel \<name\>` | Canal de entrega (whatsapp, telegram, discord, slack etc.)  
`--reply-to \<target\>` | Sobrescrita do destino de entrega  
`--reply-channel \<name\>` | Sobrescrita do canal de entrega  
`--reply-account \<id\>` | Sobrescrita do id da conta de entrega  
`--thinking \<level\>` | Define o nível de raciocínio para o perfil de modelo selecionado  
`--verbose \<on|full|off\>` | Define o nível de verbosidade  
`--timeout \<seconds\>` | Sobrescreve o tempo limite do agente  
`--json` | Gera JSON estruturado  
  
## Comportamento

  * Por padrão, a CLI passa **pelo Gateway**. Adicione `--local` para forçar o runtime incorporado na máquina atual.
  * Se o Gateway estiver inacessível, a CLI **recorre** à execução incorporada local.
  * Seleção de sessão: `--to` deriva a chave de sessão (destinos de grupo/canal preservam o isolamento; chats diretos se reduzem a `main`).
  * As opções de raciocínio e verbosidade persistem no armazenamento da sessão.
  * Saída: texto simples por padrão, ou `--json` para payload estruturado + metadados.
  * Com `--json --deliver`, o JSON inclui o status de entrega para envios enviados, suprimidos, parciais e com falha. Consulte [status de entrega JSON](</pt-BR/cli/agent#json-delivery-status>).


## Exemplos

bashCopy code
[code]
    # Simple turn with JSON outputopenclaw agent --to +15555550123 --message "Trace logs" --verbose on --json # Turn with thinking levelopenclaw agent --session-id 1234 --message "Summarize inbox" --thinking medium # Deliver to a different channel than the sessionopenclaw agent --agent ops --message "Alert" --deliver --reply-channel telegram --reply-to "@admin"
[/code]

## Relacionado

[**Referência da CLI de agente** Referência completa de opções e flags de `openclaw agent`. ](</pt-BR/cli/agent>) [**Subagentes** Geração de subagentes em segundo plano. ](</pt-BR/tools/subagents>) [**Sessões** Como as chaves de sessão funcionam e como `--to`, `--agent` e `--session-id` as resolvem. ](</pt-BR/concepts/session>) [**Comandos de barra** Catálogo de comandos nativos usado dentro de sessões de agente. ](</pt-BR/tools/slash-commands>)

Was this useful?YesNo