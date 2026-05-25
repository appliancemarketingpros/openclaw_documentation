---
title: Plugin pessoal do Zalo
source_url: https://docs.openclaw.ai/pt-BR/plugins/zalouser
scraped_at: 2026-05-25
---

Suporte ao Zalo Personal para OpenClaw por meio de um Plugin, usando `zca-js` nativo para automatizar uma conta normal de usuário do Zalo.

## Nomenclatura

O id do canal é `zalouser` para deixar explícito que isso automatiza uma **conta pessoal de usuário do Zalo** (não oficial). Mantemos `zalo` reservado para uma possível integração futura com a API oficial do Zalo.

## Onde ele é executado

Este Plugin é executado **dentro do processo do Gateway**.

Se você usa um Gateway remoto, instale/configure-o na **máquina que executa o Gateway** e, em seguida, reinicie o Gateway.

Nenhum binário externo de CLI `zca`/`openzca` é necessário.

## Instalação

### Opção A: instalar a partir do npm

bashCopy code
[code]
    openclaw plugins install @openclaw/zalouser
[/code]

Use o pacote sem especificar versão para acompanhar a tag de lançamento oficial atual. Fixe uma versão exata apenas quando precisar de uma instalação reproduzível.

Reinicie o Gateway depois disso.

### Opção B: instalar a partir de uma pasta local (dev)

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/zalouser-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

Reinicie o Gateway depois disso.

## Configuração

A configuração do canal fica em `channels.zalouser` (não em `plugins.entries.*`):

json5Copy code
[code]
    {  channels: {    zalouser: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

## CLI

bashCopy code
[code]
    openclaw channels login --channel zalouseropenclaw channels logout --channel zalouseropenclaw channels status --probeopenclaw message send --channel zalouser --target <threadId> --message "Hello from OpenClaw"openclaw directory peers list --channel zalouser --query "name"
[/code]

## Ferramenta do agente

Nome da ferramenta: `zalouser`

Ações: `send`, `image`, `link`, `friends`, `groups`, `me`, `status`

As ações de mensagem do canal também oferecem suporte a `react` para reações a mensagens.

## Relacionado

  * [Criando plugins](</pt-BR/plugins/building-plugins>)
  * [ClawHub](</pt-BR/clawhub>)


Was this useful?YesNo