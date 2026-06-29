---
title: API de saída do canal
source_url: https://docs.openclaw.ai/pt-BR/plugins/sdk-channel-outbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

Plugins de canal devem expor o comportamento de mensagens de saída a partir de `openclaw/plugin-sdk/channel-outbound`. Use `openclaw/plugin-sdk/channel-inbound` para orquestração de recebimento/contexto/despacho.

O core é responsável por enfileiramento, durabilidade, política genérica de repetição, hooks, recibos e a ferramenta `message` compartilhada. O Plugin é responsável por chamadas nativas de enviar/editar/excluir, normalização de destino, encadeamento da plataforma, citações selecionadas, sinalizadores de notificação, estado da conta e efeitos colaterais específicos da plataforma.

## Adaptador

A maioria dos Plugins define um adaptador `message`:

tsCopy code
[code]
       defineChannelMessageAdapter,  createMessageReceiptFromOutboundResults,} from "openclaw/plugin-sdk/channel-outbound"; export const demoMessageAdapter = defineChannelMessageAdapter({  id: "demo",  durableFinal: {    capabilities: {      text: true,      replyTo: true,      thread: true,      messageSendingHooks: true,    },  },  send: {    text: async ({ cfg, to, text, accountId, replyToId, threadId, signal }) => {      const sent = await sendDemoMessage({        cfg,        to,        text,        accountId: accountId ?? undefined,        replyToId: replyToId ?? undefined,        threadId: threadId == null ? undefined : String(threadId),        signal,      });       return {        receipt: createMessageReceiptFromOutboundResults({          results: [{ channel: "demo", messageId: sent.id, conversationId: to }],          kind: "text",          threadId: threadId == null ? undefined : String(threadId),          replyToId: replyToId ?? undefined,        }),      };    },  },});
[/code]

Declare apenas capacidades que o transporte nativo realmente preserva. Cubra cada capacidade declarada de envio, recibo, pré-visualização ao vivo e confirmação de recebimento com os helpers de contrato exportados deste subcaminho.

## Adaptadores de saída existentes

Se o canal já tiver um adaptador `outbound` compatível, derive o adaptador de mensagem em vez de duplicar o código de envio:

tsCopy code
[code]
     export const messageAdapter = createChannelMessageAdapterFromOutbound({  id: "demo",  outbound,  durableFinal: {    capabilities: {      text: true,      media: true,    },  },});
[/code]

## Envios duráveis

Helpers de envio em tempo de execução também ficam em `channel-outbound`:

  * `sendDurableMessageBatch(...)`
  * `withDurableMessageSendContext(...)`
  * `deliverInboundReplyWithMessageSendContext(...)`
  * helpers de streaming/progresso de rascunho, como `resolveChannelDraftStreamingChunking(...)`


`sendDurableMessageBatch(...)` retorna um resultado explícito:

  * `sent`: pelo menos uma mensagem visível da plataforma foi entregue.
  * `suppressed`: nenhuma mensagem da plataforma deve ser tratada como ausente.
  * `partial_failed`: pelo menos uma mensagem da plataforma foi entregue antes que um payload ou efeito colateral posterior falhasse.
  * `failed`: nenhum recibo da plataforma foi produzido.


Use `payloadOutcomes` quando um lote mistura payloads enviados, suprimidos e com falha. Não infira cancelamento de hook a partir de um resultado vazio de entrega direta legada.

## Despacho de compatibilidade

O despacho de resposta de entrada deve ser montado por meio de `dispatchChannelInboundReply(...)` de `channel-inbound`. Mantenha a entrega da plataforma no adaptador de entrega; use `channel-outbound` para adaptadores de mensagem, envios duráveis, recibos, pré-visualização ao vivo e opções do pipeline de resposta.

Was this useful?YesNo

Open issue