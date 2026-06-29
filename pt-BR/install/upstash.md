---
title: Caixa Upstash
source_url: https://docs.openclaw.ai/pt-BR/install/upstash
scraped_at: 2026-06-29
---

InstallHosting

Execute um Gateway persistente do OpenClaw no Upstash Box, um ambiente Linux gerenciado com suporte ao ciclo de vida keep-alive.

Use um túnel SSH para acessar o dashboard. Não exponha a porta do Gateway diretamente à internet pública.

## Pré-requisitos

  * Conta Upstash
  * Upstash Box com keep-alive
  * Cliente SSH na sua máquina local


## Criar uma Box

Crie uma Box com keep-alive no Upstash Console. Anote o ID da Box, como `right-flamingo-14486`, e sua chave de API da Box.

A Upstash mantém seu passo a passo atual da Box para OpenClaw em [Configuração do OpenClaw](<https://upstash.com/docs/box/guides/openclaw-setup>).

## Conectar com um túnel SSH

Encaminhe a porta do dashboard do OpenClaw para sua máquina local. Use sua chave de API da Box como senha SSH quando solicitado:

bashCopy code
[code]
    ssh -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

As opções de keepalive reduzem quedas do túnel por inatividade durante a integração inicial.

## Instalar o OpenClaw

Dentro da Box:

bashCopy code
[code]
    sudo npm install -g openclaw
[/code]

## Executar a integração inicial

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Siga as instruções. Copie a URL e o token do dashboard quando a integração inicial terminar.

## Iniciar o Gateway

Configure o Gateway para a rede da Box e inicie-o em segundo plano:

bashCopy code
[code]
    openclaw config set gateway.bind lannohup openclaw gateway > gateway.log 2>&1 &
[/code]

Com o túnel SSH ativo, abra a URL do dashboard localmente:

textCopy code
[code]
    http://127.0.0.1:18789/#token=<your-token>
[/code]

## Reinício automático

Defina este comando como o script de inicialização da Box para que o Gateway reinicie quando a Box iniciar:

bashCopy code
[code]
    nohup openclaw gateway > gateway.log 2>&1 &
[/code]

## Solução de problemas

Se o SSH travar durante a integração inicial, reconecte com uma configuração SSH limpa e keepalives:

bashCopy code
[code]
    ssh -F /dev/null -o ControlMaster=no -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

Isso ignora configurações locais obsoletas em `~/.ssh/config` e mantém o túnel ativo durante períodos de inatividade da rede.

## Relacionados

  * [Acesso remoto](</pt-BR/gateway/remote>)
  * [Segurança do Gateway](</pt-BR/gateway/security>)
  * [Atualizar o OpenClaw](</pt-BR/install/updating>)


Was this useful?YesNo

Open issue