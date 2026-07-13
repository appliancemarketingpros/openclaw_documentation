---
title: Extensão do Chrome
source_url: https://docs.openclaw.ai/pt-BR/tools/chrome-extension
scraped_at: 2026-07-13
---

CapabilitiesTools

# Extensão do Chrome

A extensão do OpenClaw para Chrome permite que um agente controle suas **abas do Chrome com sessão iniciada** sem abrir um navegador gerenciado separado e **sem** a solicitação bloqueante "Allow remote debugging?" do Chrome.

Isso é importante quando você controla o OpenClaw por um telefone (Telegram, WhatsApp etc.): o [perfil `user`](</pt-BR/tools/browser#profiles-openclaw-user-chrome>) se conecta pela porta de depuração remota do Chrome, o que abre uma caixa de diálogo de consentimento no computador na qual ninguém pode clicar quando você está longe. Em vez disso, a extensão usa a API `chrome.debugger`, portanto, o único aviso na página é a faixa dispensável "OpenClaw started debugging this browser" do Chrome.

Essa é a mesma abordagem usada pelas extensões do Chrome do Claude, da Anthropic, e do Codex, da OpenAI.

## Como funciona

Três partes:

  * **Serviço de controle do navegador** (Gateway ou host do Node): a API chamada pela ferramenta `browser`.
  * **Relay da extensão** (WebSocket de local loopback): um pequeno servidor que o serviço de controle inicia em `127.0.0.1`. Ele apresenta um endpoint do Chrome DevTools Protocol ao OpenClaw e se comunica com a extensão. Ambos os lados se autenticam com um token local do host (veja abaixo).
  * **Extensão do OpenClaw para Chrome** (MV3): conecta-se às abas com `chrome.debugger`, encaminha o tráfego CDP e gerencia o **grupo de abas do OpenClaw**.


O OpenClaw só vê e controla as abas que estão no **grupo de abas do OpenClaw**. O grupo é o limite de consentimento: arraste uma aba para dentro dele para compartilhá-la e arraste-a para fora (ou clique no botão da barra de ferramentas) para revogar o acesso imediatamente.

## Instalação e pareamento

  1. Exiba o caminho da extensão descompactada:

bashCopy code
[code]openclaw browser extension path
[/code]

  2. Abra `chrome://extensions`, ative **Developer mode** , clique em **Load unpacked** e selecione o diretório exibido.

  3. Exiba a string de pareamento:

bashCopy code
[code]openclaw browser extension pair
[/code]

  4. Clique no ícone do OpenClaw na barra de ferramentas e cole a string de pareamento na janela pop-up. O indicador muda para **ON** quando a extensão se conecta ao relay.


O token de pareamento é um **segredo local do host** , criado no primeiro uso e armazenado em `credentials/` no diretório de estado (modo `0600`). Cada máquina que executa um navegador — o host do Gateway e cada host de Node do navegador — possui seu próprio token, portanto nenhuma credencial precisa ser transferida entre máquinas. Para substituí-lo, exclua o arquivo `browser-extension-relay.secret` e faça o pareamento novamente.

## Como usar

Selecione o perfil integrado `chrome` em uma chamada da ferramenta `browser` ou defina-o como padrão:

bashCopy code
[code]
    openclaw config set browser.defaultProfile chrome
[/code]

json5Copy code
[code]
    {  browser: {    profiles: {      chrome: { driver: "extension", color: "#FF4500" },    },  },}
[/code]

  * Compartilhe uma aba: clique no botão do OpenClaw na barra de ferramentas dessa aba (ela entrará no grupo de abas do OpenClaw) ou arraste qualquer aba para o grupo.
  * O agente também pode abrir novas abas; elas entram automaticamente no grupo.
  * Revogue o acesso: clique novamente no botão, arraste a aba para fora do grupo ou dispense a faixa de depuração do Chrome. O agente perde imediatamente o acesso a essa aba.


## Remoto/entre máquinas

O Chrome não precisa ser executado no host do Gateway. Há três topologias compatíveis:

  * **Mesmo host** (Gateway + Chrome em uma máquina): faça o pareamento nessa máquina com `openclaw browser extension pair`. O relay aceita apenas conexões de local loopback.
  * **Diretamente com um Gateway remoto** (Chrome no seu laptop, Gateway em um VPS e **nada mais no laptop**): no Gateway, execute `openclaw browser extension pair --gateway-url wss://your-gateway.example.com`. Ele exibe uma string `wss://…/browser/extension#<secret>`; carregue e faça o pareamento da extensão no laptop. A extensão se conecta **diretamente ao Gateway** por `wss://` — sem instalação do OpenClaw, Node, CLI ou porta de entrada aberta no laptop. Esse é o caminho para hospedagem gerenciada.
  * **Por meio de um host de Node do navegador** (Chrome em uma máquina que já executa um Node do OpenClaw): execute `pair` no Node e faça o pareamento localmente; o Gateway encaminha as ações do navegador para o Node por meio do vínculo autenticado existente com o Node.


O segredo de pareamento é específico de cada host (do Gateway, no caso direto) e validado pela rota `/browser/extension` do Gateway. Para o caminho direto, disponibilize o Gateway por TLS (`wss://`) para que o segredo de pareamento e o tráfego CDP sejam criptografados. O segredo permanece no fragmento de URL da string de pareamento e é apresentado durante o handshake do WebSocket como uma credencial de subprotocolo; portanto, os logs de acesso normais do proxy não o recebem na URL da solicitação. Certifique-se de que qualquer proxy reverso preserve o cabeçalho padrão `Sec-WebSocket-Protocol`.

## Diagnóstico

bashCopy code
[code]
    openclaw browser status --browser-profile chromeopenclaw browser doctor --browser-profile chrome
[/code]

O `doctor` informa que a verificação do **relay da extensão do Chrome** está falhando até que a janela pop-up da extensão mostre **Connected**.

## Modelo de segurança

  * O relay aceita apenas conexões de local loopback; ambos os lados do WebSocket são autenticados com o token derivado, e a origem do lado da extensão é verificada como `chrome-extension://`.
  * O pareamento direto com o Gateway não aceita o token do relay na URL da solicitação; em vez disso, a extensão incluída o transporta na lista de subprotocolos do WebSocket.
  * O agente só pode ver e controlar as abas no **grupo de abas do OpenClaw**. Suas outras abas permanecem privadas.
  * Em comparação com o perfil `user` (Chrome MCP), que expõe todo o navegador com sessão iniciada depois que você aprova a solicitação de depuração remota, a extensão mantém a superfície compartilhada restrita a um grupo de abas que você controla facilmente.


Veja também: [Navegador](</pt-BR/tools/browser>) para conhecer o modelo completo de perfis e os perfis gerenciados `openclaw` e `user` do Chrome MCP.

Was this useful?YesNo

Open issue