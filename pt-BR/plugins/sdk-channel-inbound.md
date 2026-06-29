---
title: API de entrada de canais
source_url: https://docs.openclaw.ai/pt-BR/plugins/sdk-channel-inbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

Plugins de canal devem modelar caminhos de recebimento com substantivos inbound e message:

textCopy code
[code]
    platform event -> inbound facts/context -> agent reply -> message delivery
[/code]

Use `openclaw/plugin-sdk/channel-inbound` para normalização de eventos inbound, formatação, roots e orquestração. Use `openclaw/plugin-sdk/channel-outbound` para comportamento de envio nativo, recibo, entrega durável e pré-visualização ao vivo.

## Auxiliares principais

tsCopy code
[code]
       buildChannelInboundEventContext,  runChannelInboundEvent,  dispatchChannelInboundReply,} from "openclaw/plugin-sdk/channel-inbound";
[/code]

  * `buildChannelInboundEventContext(...)`: projeta fatos normalizados do canal no contexto de prompt/sessão. Use `channelContext` para repassar metadados de remetente/chat pertencentes ao canal para o hook de Plugin `ctx.channelContext`; amplie `PluginHookChannelSenderContext` ou `PluginHookChannelChatContext` deste subcaminho para campos específicos do canal.
  * `runChannelInboundEvent(...)`: executa ingestão, classificação, preflight, resolução, registro, despacho e finalização para um evento inbound da plataforma.
  * `dispatchChannelInboundReply(...)`: registra e despacha uma resposta inbound já montada com um adaptador de entrega.


O runtime de Plugin injetado expõe os mesmos auxiliares de alto nível em `runtime.channel.inbound.*` para canais integrados/nativos que já recebem o objeto de runtime.

tsCopy code
[code]
    await runtime.channel.inbound.run({  channel: "demo",  accountId,  raw: platformEvent,  adapter: {    ingest: normalizePlatformEvent,    resolveTurn: resolveInboundReply,  },});
[/code]

Dispatchers de compatibilidade devem montar as entradas de `dispatchChannelInboundReply(...)` e manter a entrega da plataforma no adaptador de entrega. Novos caminhos de envio devem preferir adaptadores de mensagem e auxiliares de mensagem durável.

## Migração

Os aliases antigos de runtime `runtime.channel.turn.*` foram removidos. Use:

  * `runtime.channel.inbound.run(...)` para eventos inbound brutos.
  * `runtime.channel.inbound.dispatchReply(...)` para contextos de resposta montados.
  * `runtime.channel.inbound.buildContext(...)` para payloads de contexto inbound.
  * `runtime.channel.inbound.runPreparedReply(...)` apenas para caminhos de despacho preparado pertencentes ao canal que já montam seu próprio closure de despacho.


Novo código de Plugin não deve introduzir APIs de canal nomeadas com `turn`. Mantenha o vocabulário de turn de modelo ou agente dentro do código de agente/provedor; Plugins de canal usam termos inbound, message, delivery e reply.

Was this useful?YesNo

Open issue