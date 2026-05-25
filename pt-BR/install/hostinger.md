---
title: Hostinger
source_url: https://docs.openclaw.ai/pt-BR/install/hostinger
scraped_at: 2026-05-25
---

Execute um Gateway OpenClaw persistente na [Hostinger](<https://www.hostinger.com/openclaw>) por meio de uma implantação gerenciada **1-Click** ou de uma instalação em **VPS**.

## Pré-requisitos

  * Conta na Hostinger ([cadastro](<https://www.hostinger.com/openclaw>))
  * Cerca de 5 a 10 minutos


## Opção A: OpenClaw 1-Click

A forma mais rápida de começar. A Hostinger cuida da infraestrutura, do Docker e das atualizações automáticas.

* ### Purchase and launch

  1. Na [página do OpenClaw da Hostinger](<https://www.hostinger.com/openclaw>), escolha um plano Managed OpenClaw e conclua a compra.


* ### Select a messaging channel

Escolha um ou mais canais para conectar:

  * **WhatsApp** — escaneie o código QR mostrado no assistente de configuração.
  * **Telegram** — cole o token do bot do [BotFather](<https://t.me/BotFather>).


* ### Complete installation

Clique em **Finish** para implantar a instância. Quando estiver pronta, acesse o dashboard do OpenClaw em **OpenClaw Overview** no hPanel.

## Opção B: OpenClaw em VPS

Mais controle sobre o servidor. A Hostinger implanta o OpenClaw via Docker na sua VPS, e você o gerencia pelo **Docker Manager** no hPanel.

* ### Purchase a VPS

  1. Na [página do OpenClaw da Hostinger](<https://www.hostinger.com/openclaw>), escolha um plano OpenClaw on VPS e conclua a compra.


* ### Configure OpenClaw

Quando a VPS estiver provisionada, preencha os campos de configuração:

  * **Gateway token** — gerado automaticamente; salve-o para usar depois.
  * **WhatsApp number** — seu número com código do país (opcional).
  * **Telegram bot token** — do [BotFather](<https://t.me/BotFather>) (opcional).
  * **API keys** — necessárias apenas se você não selecionou créditos de Ready-to-Use AI durante a compra.


* ### Start OpenClaw

Clique em **Deploy**. Quando estiver em execução, abra o dashboard do OpenClaw no hPanel clicando em **Open**.

Logs, reinicializações e atualizações são gerenciados diretamente pela interface do Docker Manager no hPanel. Para atualizar, clique em **Update** no Docker Manager, e isso fará o pull da imagem mais recente.

## Verifique sua configuração

Envie "Hi" para seu assistente no canal que você conectou. O OpenClaw responderá e orientará você pelas preferências iniciais.

## Solução de problemas

**Dashboard não carrega** — Aguarde alguns minutos para o container terminar o provisionamento. Verifique os logs do Docker Manager no hPanel.

**O container Docker continua reiniciando** — Abra os logs do Docker Manager e procure erros de configuração (tokens ausentes, chaves de API inválidas).

**O bot do Telegram não responde** — Envie sua mensagem com o código de pairing pelo Telegram diretamente como mensagem dentro do seu chat do OpenClaw para concluir a conexão.

## Próximos passos

  * [Channels](</pt-BR/channels>) — conecte Telegram, WhatsApp, Discord e mais
  * [Gateway configuration](</pt-BR/gateway/configuration>) — todas as opções de configuração


## Relacionado

  * [Visão geral de instalação](</pt-BR/install>)
  * [Hospedagem em VPS](</pt-BR/vps>)
  * [DigitalOcean](</pt-BR/install/digitalocean>)


Was this useful?YesNo