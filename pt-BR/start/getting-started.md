---
title: Primeiros passos
source_url: https://docs.openclaw.ai/pt-BR/start/getting-started
scraped_at: 2026-05-25
---

Instale o OpenClaw, execute a integração inicial e converse com seu assistente de IA — tudo em cerca de 5 minutos. Ao final, você terá um Gateway em execução, autenticação configurada e uma sessão de conversa funcional.

## O que você precisa

  * **Node.js** — Node 24 recomendado (Node 22.16+ também é compatível)
  * **Uma chave de API** de um provedor de modelo (Anthropic, OpenAI, Google, etc.) — a integração inicial solicitará isso


## Configuração rápida

* ### Instalar o OpenClaw

### macOS / Linux

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

![Processo do Script de Instalação](/assets/install-script.svg)

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

* ### Executar a integração inicial

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

O assistente guia você na escolha de um provedor de modelo, na definição de uma chave de API e na configuração do Gateway. Leva cerca de 2 minutos.

Consulte [Integração inicial (CLI)](</pt-BR/start/wizard>) para a referência completa.

* ### Verificar se o Gateway está em execução

bashCopy code
[code]
    openclaw gateway status
[/code]

Você deve ver o Gateway escutando na porta 18789.

* ### Abrir o painel

bashCopy code
[code]
    openclaw dashboard
[/code]

Isso abre a interface de controle no seu navegador. Se ela carregar, tudo está funcionando.

* ### Enviar sua primeira mensagem

Digite uma mensagem no chat da interface de controle e você deverá receber uma resposta da IA.

Quer conversar pelo telefone em vez disso? O canal mais rápido de configurar é o [Telegram](</pt-BR/channels/telegram>) (apenas um token de bot). Consulte [Canais](</pt-BR/channels>) para todas as opções.

Avançado: montar uma build personalizada da interface de controle

Se você mantém uma build localizada ou personalizada do painel, aponte `gateway.controlUi.root` para um diretório que contenha seus ativos estáticos gerados e `index.html`.

bashCopy code
[code]
    mkdir -p "$HOME/.openclaw/control-ui-custom"# Copy your built static files into that directory.
[/code]

Então defina:

jsonCopy code
[code]
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "$HOME/.openclaw/control-ui-custom"  }}}
[/code]

Reinicie o Gateway e reabra o painel:

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## O que fazer a seguir

[**Conectar um canal** Discord, Feishu, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo e mais. ](</pt-BR/channels>) [**Pareamento e segurança** Controle quem pode enviar mensagens ao seu agente. ](</pt-BR/channels/pairing>) [**Configurar o Gateway** Modelos, ferramentas, sandbox e configurações avançadas. ](</pt-BR/gateway/configuration>) [**Explorar ferramentas** Navegador, exec, busca na web, Skills e Plugins. ](</pt-BR/tools>)

Avançado: variáveis de ambiente

Se você executa o OpenClaw como uma conta de serviço ou deseja caminhos personalizados:

  * `OPENCLAW_HOME` — diretório inicial para resolução de caminhos internos
  * `OPENCLAW_STATE_DIR` — substitui o diretório de estado
  * `OPENCLAW_CONFIG_PATH` — substitui o caminho do arquivo de configuração


Referência completa: [Variáveis de ambiente](</pt-BR/help/environment>).

## Relacionados

  * [Visão geral da instalação](</pt-BR/install>)
  * [Visão geral dos canais](</pt-BR/channels>)
  * [Configuração](</pt-BR/start/setup>)


Was this useful?YesNo