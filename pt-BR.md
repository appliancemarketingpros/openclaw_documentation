---
title: OpenClaw
source_url: https://docs.openclaw.ai/pt-BR
scraped_at: 2026-05-25
---

# OpenClaw 🦞

![OpenClaw](/assets/openclaw-logo-text-dark.png) ![OpenClaw](/assets/openclaw-logo-text.png)

> _"ESFOLIE! ESFOLIE!"_ — Uma lagosta espacial, provavelmente

**Gateway para qualquer sistema operacional para agentes de IA no Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo e mais.**

Envie uma mensagem e receba uma resposta do agente direto do seu bolso. Execute um Gateway em canais integrados, plugins de canal incluídos, WebChat e nodes móveis.

[**Comece** Instale o OpenClaw e coloque o Gateway no ar em minutos. ](</pt-BR/start/getting-started>) [**Execute o onboarding** Configuração guiada com `openclaw onboard` e fluxos de pareamento. ](</pt-BR/start/wizard>) [**Abra a Control UI** Inicie o painel do navegador para chat, configuração e sessões. ](</pt-BR/web/control-ui>)

## O que é o OpenClaw?

OpenClaw é um **gateway auto-hospedado** que conecta seus aplicativos de chat e superfícies de canal favoritos — canais integrados mais plugins de canal incluídos ou externos, como Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo e mais — a agentes de programação de IA como Pi. Você executa um único processo Gateway na sua própria máquina (ou em um servidor), e ele se torna a ponte entre seus aplicativos de mensagens e um assistente de IA sempre disponível.

**Para quem é?** Desenvolvedores e usuários avançados que querem um assistente de IA pessoal com o qual possam trocar mensagens de qualquer lugar — sem abrir mão do controle sobre seus dados nem depender de um serviço hospedado.

**O que o torna diferente?**

  * **Auto-hospedado** : roda no seu hardware, sob suas regras
  * **Multicanal** : um Gateway atende simultaneamente canais integrados e plugins de canal incluídos ou externos
  * **Nativo para agentes** : criado para agentes de programação com uso de ferramentas, sessões, memória e roteamento multiagente
  * **Código aberto** : licenciado sob MIT e impulsionado pela comunidade


**Do que você precisa?** Node 24 (recomendado), ou Node 22 LTS (`22.16+`) para compatibilidade, uma chave de API do provedor escolhido e 5 minutos. Para obter a melhor qualidade e segurança, use o modelo de geração mais recente mais forte disponível.

## Como funciona
[code] 
    flowchart LR
      A["Chat apps + plugins"] --> B["Gateway"]
      B --> C["Pi agent"]
      B --> D["CLI"]
      B --> E["Web Control UI"]
      B --> F["macOS app"]
      B --> G["iOS and Android nodes"]
[/code]

O Gateway é a única fonte da verdade para sessões, roteamento e conexões de canal.

## Principais recursos

[**Gateway multicanal** Discord, iMessage, Signal, Slack, Telegram, WhatsApp, WebChat e mais com um único processo Gateway. ](</pt-BR/channels>) [**Canais Plugin** Plugins incluídos adicionam Matrix, Nostr, Twitch, Zalo e mais nas versões atuais normais. ](</pt-BR/tools/plugin>) [**Roteamento multiagente** Sessões isoladas por agente, workspace ou remetente. ](</pt-BR/concepts/multi-agent>) [**Suporte a mídia** Envie e receba imagens, áudio e documentos. ](</pt-BR/nodes/images>) [**Web Control UI** Painel do navegador para chat, configuração, sessões e nodes. ](</pt-BR/web/control-ui>) [**Nodes móveis** Pareie nodes iOS e Android para fluxos de trabalho com Canvas, câmera e voz. ](</pt-BR/nodes>)

## Início rápido

* ### Instale o OpenClaw

bashCopy code
[code]
    npm install -g openclaw@latest
[/code]

* ### Faça o onboarding e instale o serviço

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

* ### Chat

Abra a Control UI no navegador e envie uma mensagem:

bashCopy code
[code]
    openclaw dashboard
[/code]

Ou conecte um canal ([Telegram](</pt-BR/channels/telegram>) é o mais rápido) e converse pelo celular.

Precisa da instalação completa e da configuração de desenvolvimento? Consulte [Primeiros passos](</pt-BR/start/getting-started>).

## Painel

Abra a Control UI do navegador depois que o Gateway iniciar.

  * Padrão local: <http://127.0.0.1:18789/>
  * Acesso remoto: [Superfícies web](</pt-BR/web>) e [Tailscale](</pt-BR/gateway/tailscale>)


![OpenClaw](/whatsapp-openclaw.jpg)

## Configuração (opcional)

A configuração fica em `~/.openclaw/openclaw.json`.

  * Se você **não fizer nada** , o OpenClaw usa o binário Pi incluído no modo RPC com sessões por remetente.
  * Se quiser restringir o acesso, comece por `channels.whatsapp.allowFrom` e (para grupos) regras de menção.


Exemplo:

json5Copy code
[code]
    {  channels: {    whatsapp: {      allowFrom: ["+15555550123"],      groups: { "*": { requireMention: true } },    },  },  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },}
[/code]

## Comece aqui

[**Centros de documentação** Toda a documentação e guias, organizados por caso de uso. ](</pt-BR/start/hubs>) [**Configuração** Configurações centrais do Gateway, tokens e configuração de provedor. ](</pt-BR/gateway/configuration>) [**Acesso remoto** Padrões de acesso por SSH e tailnet. ](</pt-BR/gateway/remote>) [**Canais** Configuração específica de canal para Feishu, Microsoft Teams, WhatsApp, Telegram, Discord e mais. ](</pt-BR/channels/telegram>) [**Nodes** Nodes iOS e Android com pareamento, Canvas, câmera e ações do dispositivo. ](</pt-BR/nodes>) [**Ajuda** Correções comuns e ponto de entrada para solução de problemas. ](</pt-BR/help>)

## Saiba mais

[**Lista completa de recursos** Recursos completos de canal, roteamento e mídia. ](</pt-BR/concepts/features>) [**Roteamento multiagente** Isolamento de workspace e sessões por agente. ](</pt-BR/concepts/multi-agent>) [**Segurança** Tokens, listas de permissões e controles de segurança. ](</pt-BR/gateway/security>) [**Solução de problemas** Diagnósticos do Gateway e erros comuns. ](</pt-BR/gateway/troubleshooting>) [**Sobre e créditos** Origens do projeto, colaboradores e licença. ](</pt-BR/reference/credits>)

Was this useful?YesNo