---
title: Plugin do WhatsApp
source_url: https://docs.openclaw.ai/pt-BR/plugins/reference/whatsapp
scraped_at: 2026-05-25
---

# Plugin do WhatsApp

Adiciona a superfície de canal do WhatsApp para enviar e receber mensagens do OpenClaw.

## Distribuição

  * Pacote: `@openclaw/whatsapp`
  * Rota de instalação: npm; ClawHub


## Superfície

channels: whatsapp

## Observação de instalação no Windows

No Windows, o Plugin do WhatsApp precisa do Git no `PATH` durante a instalação via npm porque uma de suas dependências Baileys/libsignal é obtida de uma URL git. Instale o Git para Windows, reinicie o shell e execute novamente a instalação:

powershellCopy code
[code]
    winget install --id Git.Git -e
[/code]

O Git portátil também funciona se seu diretório `bin` estiver no `PATH`.

## Documentação relacionada

  * [whatsapp](</pt-BR/channels/whatsapp>)


Was this useful?YesNo