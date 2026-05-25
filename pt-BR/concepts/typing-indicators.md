---
title: Indicadores de digitação
source_url: https://docs.openclaw.ai/pt-BR/concepts/typing-indicators
scraped_at: 2026-05-25
---

Indicadores de digitação são enviados ao canal de chat enquanto uma execução está ativa. Use `agents.defaults.typingMode` para controlar **quando** a digitação começa e `typingIntervalSeconds` para controlar **com que frequência** ela é atualizada.

## Padrões

Quando `agents.defaults.typingMode` **não está definido** , o OpenClaw mantém o comportamento legado:

  * **Chats diretos** : a digitação começa imediatamente assim que o loop do modelo começa.
  * **Chats em grupo com uma menção** : a digitação começa imediatamente.
  * **Chats em grupo sem uma menção** : a digitação começa somente quando o texto da mensagem começa a ser transmitido.
  * **Execuções de Heartbeat** : a digitação começa quando a execução de Heartbeat começa se o destino de Heartbeat resolvido for um chat compatível com digitação e a digitação não estiver desabilitada.


## Modos

Defina `agents.defaults.typingMode` como um destes:

  * `never` \- nenhum indicador de digitação, nunca.
  * `instant` \- inicia a digitação **assim que o loop do modelo começa** , mesmo que a execução depois retorne apenas o token de resposta silenciosa.
  * `thinking` \- inicia a digitação no **primeiro delta de raciocínio** (requer `reasoningLevel: "stream"` para a execução).
  * `message` \- inicia a digitação no **primeiro delta de texto não silencioso** (ignora o token silencioso `NO_REPLY`).


Ordem de "quão cedo é acionado": `never` → `message` → `thinking` → `instant`

## Configuração

Defina o padrão no nível do agente:

json5Copy code
[code]
    {  agents: {    defaults: {      typingMode: "thinking",      typingIntervalSeconds: 6,    },  },}
[/code]

Substitua o modo ou a cadência por sessão:

json5Copy code
[code]
    {  session: {    typingMode: "message",    typingIntervalSeconds: 4,  },}
[/code]

## Observações

  * O modo `message` não mostra digitação para respostas somente silenciosas quando todo o payload é exatamente o token silencioso (por exemplo `NO_REPLY` / `no_reply`, correspondido sem diferenciar maiúsculas de minúsculas).
  * `thinking` só é acionado se a execução transmitir raciocínio (`reasoningLevel: "stream"`). Se o modelo não emitir deltas de raciocínio, a digitação não começará.
  * A digitação de Heartbeat é um sinal de vivacidade para o destino de entrega resolvido. Ela começa no início da execução de Heartbeat, em vez de seguir o tempo de stream de `message` ou `thinking`. Defina `typingMode: "never"` para desabilitá-la.
  * Heartbeats não mostram digitação quando `target: "none"`, quando o destino não pode ser resolvido, quando a entrega por chat está desabilitada para o Heartbeat ou quando o canal não oferece suporte a digitação.
  * `typingIntervalSeconds` controla a **cadência de atualização** , não o horário de início. O padrão é 6 segundos.


## Relacionados

[**Presence** Como o Gateway rastreia clientes conectados e os exibe na aba Instances do macOS. ](</pt-BR/concepts/presence>) [**Streaming and chunking** Comportamento de streaming de saída, limites de chunks e entrega específica por canal. ](</pt-BR/concepts/streaming>)

Was this useful?YesNo