---
title: Reações
source_url: https://docs.openclaw.ai/pt-BR/tools/reactions
scraped_at: 2026-05-25
---

O agente pode adicionar e remover reações com emoji em mensagens usando a ferramenta `message` com a ação `react`. O comportamento das reações varia conforme o canal e o transporte.

## Como funciona

jsonCopy code
[code]
    {  "action": "react",  "messageId": "msg-123",  "emoji": "thumbsup"}
[/code]

  * `emoji` é obrigatório ao adicionar uma reação.
  * Defina `emoji` como uma string vazia (`""`) para remover a(s) reação(ões) do bot.
  * Defina `remove: true` para remover um emoji específico (requer `emoji` não vazio).
  * Em canais que oferecem suporte a reações de status, `trackToolCalls: true` em uma reação permite que o runtime use essa mensagem reagida para reações de progresso de ferramentas subsequentes durante o mesmo turno.


## Comportamento por canal

Discord e Slack

  * `emoji` vazio remove todas as reações do bot na mensagem.
  * `remove: true` remove apenas o emoji especificado.

Google Chat

  * `emoji` vazio remove as reações do app na mensagem.
  * `remove: true` remove apenas o emoji especificado.

Telegram

  * `emoji` vazio remove as reações do bot.
  * `remove: true` também remove reações, mas ainda requer um `emoji` não vazio para validação da ferramenta.

WhatsApp

  * `emoji` vazio remove a reação do bot.
  * `remove: true` é mapeado internamente para emoji vazio (ainda requer `emoji` na chamada da ferramenta).

Zalo Personal (zalouser)

  * Requer `emoji` não vazio.
  * `remove: true` remove essa reação de emoji específica.

Feishu/Lark

  * Use a ferramenta `feishu_reaction` com as ações `add`, `remove` e `list`.
  * Adicionar/remover requer `emoji_type`; remover também requer `reaction_id`.

Signal

  * As notificações de reação recebidas são controladas por `channels.signal.reactionNotifications`: `"off"` as desativa, `"own"` (padrão) emite eventos quando usuários reagem a mensagens do bot, e `"all"` emite eventos para todas as reações.

iMessage

  * Reações enviadas são tapbacks do iMessage (`love`, `like`, `dislike`, `laugh`, `emphasize` e `question`).
  * As notificações de tapback recebidas são controladas por `channels.imessage.reactionNotifications`: `"off"` as desativa, `"own"` (padrão) emite eventos quando usuários reagem a mensagens criadas pelo bot, e `"all"` emite eventos para todos os tapbacks de remetentes autorizados.


## Nível de reação

A configuração `reactionLevel` por canal controla quão amplamente o agente usa reações. Os valores normalmente são `off`, `ack`, `minimal` ou `extensive`.

  * [reactionLevel do Telegram](</pt-BR/channels/telegram#reaction-notifications>) — `channels.telegram.reactionLevel`
  * [reactionLevel do WhatsApp](</pt-BR/channels/whatsapp#reaction-level>) — `channels.whatsapp.reactionLevel`


Defina `reactionLevel` em canais individuais para ajustar com que atividade o agente reage a mensagens em cada plataforma.

## Relacionado

  * [Envio do agente](</pt-BR/tools/agent-send>) — a ferramenta `message` que inclui `react`
  * [Canais](</pt-BR/channels>) — configuração específica de canais


Was this useful?YesNo