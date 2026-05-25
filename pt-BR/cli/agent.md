---
title: Agente
source_url: https://docs.openclaw.ai/pt-BR/cli/agent
scraped_at: 2026-05-25
---

# `openclaw agent`

Execute uma rodada de agente via Gateway (use `--local` para incorporado). Use `--agent <id>` para apontar diretamente para um agente configurado.

Passe pelo menos um seletor de sessão:

  * `--to <dest>`
  * `--session-id <id>`
  * `--agent <id>`


Relacionado:

  * Ferramenta de envio de agente: [Envio de agente](</pt-BR/tools/agent-send>)


## Opções

  * `-m, --message <text>`: corpo da mensagem obrigatório
  * `-t, --to <dest>`: destinatário usado para derivar a chave da sessão
  * `--session-id <id>`: id de sessão explícito
  * `--agent <id>`: id do agente; substitui associações de roteamento
  * `--model <id>`: substituição de modelo para esta execução (`provider/model` ou id do modelo)
  * `--thinking <level>`: nível de raciocínio do agente (`off`, `minimal`, `low`, `medium`, `high`, além de níveis personalizados compatíveis com o provedor, como `xhigh`, `adaptive` ou `max`)
  * `--verbose <on|off>`: persiste o nível verboso da sessão
  * `--channel <channel>`: canal de entrega; omita para usar o canal principal da sessão
  * `--reply-to <target>`: substituição do destino de entrega
  * `--reply-channel <channel>`: substituição do canal de entrega
  * `--reply-account <id>`: substituição da conta de entrega
  * `--local`: executa o agente incorporado diretamente (após pré-carregar o registro de plugins)
  * `--deliver`: envia a resposta de volta ao canal/destino selecionado
  * `--timeout <seconds>`: substitui o tempo limite do agente (padrão 600 ou valor de configuração)
  * `--json`: gera JSON


## Exemplos

bashCopy code
[code]
    openclaw agent --to +15555550123 --message "status update" --deliveropenclaw agent --agent ops --message "Summarize logs"openclaw agent --agent ops --model openai/gpt-5.4 --message "Summarize logs"openclaw agent --session-id 1234 --message "Summarize inbox" --thinking mediumopenclaw agent --to +15555550123 --message "Trace logs" --verbose on --jsonopenclaw agent --agent ops --message "Generate report" --deliver --reply-channel slack --reply-to "#reports"openclaw agent --agent ops --message "Run locally" --local
[/code]

## Observações

  * O modo Gateway recorre ao agente incorporado quando a solicitação ao Gateway falha. Use `--local` para forçar a execução incorporada desde o início.
  * `--local` ainda pré-carrega primeiro o registro de plugins, então provedores, ferramentas e canais fornecidos por plugins permanecem disponíveis durante execuções incorporadas.
  * Execuções com `--local` e fallback incorporado são tratadas como execuções únicas. Recursos de loopback MCP agrupados e sessões stdio Claude aquecidas abertas para esse processo local são descartados após a resposta, para que invocações por script não mantenham processos filhos locais ativos.
  * Execuções apoiadas pelo Gateway deixam recursos de loopback MCP pertencentes ao Gateway sob o processo Gateway em execução; clientes mais antigos ainda podem enviar a flag histórica de limpeza, mas o Gateway a aceita como um no-op de compatibilidade.
  * `--channel`, `--reply-channel` e `--reply-account` afetam a entrega da resposta, não o roteamento da sessão.
  * `--json` mantém stdout reservado para a resposta JSON. Diagnósticos do Gateway, de plugins e de fallback incorporado são roteados para stderr para que scripts possam analisar stdout diretamente.
  * O JSON de fallback incorporado inclui `meta.transport: "embedded"` e `meta.fallbackFrom: "gateway"` para que scripts possam distinguir execuções de fallback de execuções do Gateway.
  * Se o Gateway aceitar uma execução de agente, mas a CLI atingir tempo limite esperando pela resposta final, o fallback incorporado usa um novo id explícito de sessão/execução `gateway-fallback-*` e informa `meta.fallbackReason: "gateway_timeout"` mais os campos de sessão de fallback. Isso evita disputar o bloqueio da transcrição pertencente ao Gateway ou substituir silenciosamente a sessão de conversa roteada original.
  * Quando este comando aciona a regeneração de `models.json`, credenciais de provedores gerenciadas por SecretRef são persistidas como marcadores não secretos (por exemplo, nomes de variáveis de ambiente, `secretref-env:ENV_VAR_NAME` ou `secretref-managed`), não como texto puro de segredo resolvido.
  * Escritas de marcadores têm autoridade da fonte: o OpenClaw persiste marcadores do snapshot ativo da configuração de origem, não dos valores secretos resolvidos em runtime.


## Status de entrega JSON

Quando `--json --deliver` é usado, a resposta JSON da CLI pode incluir `deliveryStatus` de nível superior para que scripts possam distinguir envios entregues, suprimidos, parcialmente falhos e com falha:

jsonCopy code
[code]
    {  "payloads": [{ "text": "Report ready", "mediaUrl": null }],  "meta": { "durationMs": 1200 },  "deliveryStatus": {    "requested": true,    "attempted": true,    "status": "sent",    "succeeded": true,    "resultCount": 1  }}
[/code]

`deliveryStatus.status` é um de `sent`, `suppressed`, `partial_failed` ou `failed`. `suppressed` significa que a entrega intencionalmente não foi enviada, por exemplo, um hook de envio de mensagem a cancelou ou não havia resultado visível; ainda assim, é um desfecho terminal sem nova tentativa. `partial_failed` significa que pelo menos um payload foi enviado antes que um payload posterior falhasse. `failed` significa que nenhum envio durável foi concluído ou que a pré-validação de entrega falhou.

Respostas da CLI apoiadas pelo Gateway também preservam o formato bruto do resultado do Gateway, em que o mesmo objeto está disponível em `result.deliveryStatus`.

Campos comuns:

  * `requested`: sempre `true` quando o objeto está presente.
  * `attempted`: `true` depois que o caminho de envio durável foi executado; `false` para falhas de pré-validação ou ausência de payloads visíveis.
  * `succeeded`: `true`, `false` ou `"partial"`; `"partial"` acompanha `status: "partial_failed"`.
  * `reason`: um motivo em snake-case minúsculo vindo da entrega durável ou da validação de pré-validação. Motivos conhecidos incluem `cancelled_by_message_sending_hook`, `no_visible_payload`, `no_visible_result`, `channel_resolved_to_internal`, `unknown_channel`, `invalid_delivery_target` e `no_delivery_target`; envios duráveis com falha também podem informar o estágio que falhou. Trate valores desconhecidos como opacos porque o conjunto pode se expandir.
  * `resultCount`: número de resultados de envio do canal quando disponível.
  * `sentBeforeError`: `true` quando uma falha parcial enviou pelo menos um payload antes do erro.
  * `error`: booleano `true` para envios com falha ou parcialmente falhos.
  * `errorMessage`: incluído apenas quando uma mensagem de erro de entrega subjacente é capturada. Falhas de pré-validação carregam `error` e `reason`, mas não `errorMessage`.
  * `payloadOutcomes`: resultados opcionais por payload com `index`, `status`, `reason`, `resultCount`, `error`, `stage`, `sentBeforeError` ou metadados de hook quando disponíveis.


## Relacionado

  * [Referência da CLI](</pt-BR/cli>)
  * [Runtime do agente](</pt-BR/concepts/agent>)


Was this useful?YesNo