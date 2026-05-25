---
title: Direcionar
source_url: https://docs.openclaw.ai/pt-BR/tools/steer
scraped_at: 2026-05-25
---

`/steer` envia orientação para uma execução já ativa. Ele é para momentos de "ajustar esta execução enquanto ela ainda está trabalhando", não para iniciar um novo turno.

## Sessão atual

Use `/steer` de nível superior para direcionar a execução ativa da sessão atual:

textCopy code
[code]
    /steer prefer the smaller patch and keep the tests focused/tell summarize before making the next tool call
[/code]

Comportamento:

  * Direciona somente a execução ativa da sessão atual.
  * Funciona independentemente do modo `/queue` da sessão.
  * Não inicia uma nova execução quando a sessão está ociosa.
  * Responde com um aviso quando não há execução ativa para direcionar.
  * Usa o caminho de direcionamento do runtime ativo, portanto o modelo vê a orientação no próximo limite de runtime compatível.


## Direcionar vs fila

`/queue steer` altera como mensagens de entrada normais se comportam quando chegam enquanto uma execução está ativa. `/steer <message>` é um comando explícito que tenta injetar a mensagem desse comando na execução ativa no próximo limite de runtime compatível, independentemente da configuração `/queue` armazenada.

Use:

  * `/steer <message>` quando quiser orientar a execução ativa agora.
  * `/queue steer` quando quiser que futuras mensagens normais direcionem execuções ativas por padrão.
  * `/queue collect` ou `/queue followup` quando novas mensagens devem aguardar um turno posterior em vez de direcionar a execução ativa.


Para modos de fila e comportamento de fallback, consulte [Fila de comandos](</pt-BR/concepts/queue>) e [Fila de direcionamento](</pt-BR/concepts/queue-steering>).

## Subagentes

Use `/subagents steer` quando o alvo for uma execução filha:

textCopy code
[code]
    /subagents steer 2 focus only on the API surface
[/code]

`/steer` de nível superior não seleciona um subagente por id ou índice de lista. Ele sempre direciona a execução ativa da sessão atual. Consulte [Subagentes](</pt-BR/tools/subagents>) para ids, rótulos e comandos de controle de subagentes.

## Sessões ACP

Use `/acp steer` quando o alvo for uma sessão de harness ACP:

textCopy code
[code]
    /acp steer --session agent:main:acp:codex tighten the repro
[/code]

Consulte [Agentes ACP](</pt-BR/tools/acp-agents>) para seleção de sessão ACP e comportamento de runtime.

## Relacionado

  * [Comandos de barra](</pt-BR/tools/slash-commands>)
  * [Fila de comandos](</pt-BR/concepts/queue>)
  * [Fila de direcionamento](</pt-BR/concepts/queue-steering>)
  * [Subagentes](</pt-BR/tools/subagents>)


Was this useful?YesNo