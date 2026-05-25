---
title: WebChat (macOS)
source_url: https://docs.openclaw.ai/pt-BR/platforms/mac/webchat
scraped_at: 2026-05-25
---

O app da barra de menus do macOS incorpora a UI do WebChat como uma visualização SwiftUI nativa. Ele se conecta ao Gateway e usa como padrão a **sessão main** do agente selecionado (com um seletor de sessões para outras sessões).

  * **Modo local** : conecta-se diretamente ao WebSocket do Gateway local.
  * **Modo remoto** : encaminha a porta de controle do Gateway por SSH e usa esse túnel como plano de dados.


## Inicialização e depuração

  * Manual: menu Lobster → "Abrir Chat".

  * Abertura automática para testes:

bashCopy code
[code]dist/OpenClaw.app/Contents/MacOS/OpenClaw --webchat
[/code]

  * Logs: `./scripts/clawlog.sh` (subsistema `ai.openclaw`, categoria `WebChatSwiftUI`).


## Como ele é conectado

  * Plano de dados: métodos WS do Gateway `chat.history`, `chat.send`, `chat.abort`, `chat.inject` e eventos `chat`, `agent`, `presence`, `tick`, `health`.
  * `chat.history` retorna linhas de transcrição normalizadas para exibição: tags de diretivas inline são removidas do texto visível, cargas XML de chamadas de ferramentas em texto simples (incluindo `<tool_call>...</tool_call>`, `<function_call>...</function_call>`, `<tool_calls>...</tool_calls>`, `<function_calls>...</function_calls>` e blocos truncados de chamadas de ferramentas) e tokens de controle de modelo ASCII/largura total vazados são removidos, linhas puras de assistente com tokens silenciosos, como `NO_REPLY` / `no_reply` exatos, são omitidas, e linhas grandes demais podem ser substituídas por placeholders.
  * Sessão: usa como padrão a sessão primária (`main`, ou `global` quando o escopo é global). A UI pode alternar entre sessões.
  * A integração inicial usa uma sessão dedicada para manter a configuração da primeira execução separada.


## Superfície de segurança

  * O modo remoto encaminha apenas a porta de controle WebSocket do Gateway por SSH.


## Limitações conhecidas

  * A UI é otimizada para sessões de chat (não para uma sandbox completa de navegador).


## Relacionado

  * [WebChat](</pt-BR/web/webchat>)
  * [app macOS](</pt-BR/platforms/macos>)


Was this useful?YesNo