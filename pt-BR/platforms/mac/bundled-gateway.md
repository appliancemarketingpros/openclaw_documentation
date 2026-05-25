---
title: Gateway no macOS
source_url: https://docs.openclaw.ai/pt-BR/platforms/mac/bundled-gateway
scraped_at: 2026-05-25
---

OpenClaw.app não inclui mais Node/Bun nem o runtime do Gateway. O app macOS espera uma instalação **externa** da CLI `openclaw`, não inicia o Gateway como um processo filho e gerencia um serviço launchd por usuário para manter o Gateway em execução (ou se conecta a um Gateway local existente se já houver um em execução).

## Instale a CLI (obrigatório para o modo local)

Node 24 é o runtime padrão no Mac. Node 22 LTS, atualmente `22.16+`, ainda funciona por compatibilidade. Em seguida, instale `openclaw` globalmente:

bashCopy code
[code]
    npm install -g openclaw@<version>
[/code]

O botão **Instalar CLI** do app macOS executa o mesmo fluxo de instalação global que o app usa internamente: ele prefere npm primeiro, depois pnpm, depois bun se esse for o único gerenciador de pacotes detectado. Node continua sendo o runtime recomendado para o Gateway.

## Launchd (Gateway como LaunchAgent)

Rótulo:

  * `ai.openclaw.gateway` (ou `ai.openclaw.<profile>`; o legado `com.openclaw.*` pode permanecer)


Localização do plist (por usuário):

  * `~/Library/LaunchAgents/ai.openclaw.gateway.plist` (ou `~/Library/LaunchAgents/ai.openclaw.<profile>.plist`)


Gerenciador:

  * O app macOS é responsável por instalar/atualizar o LaunchAgent no modo Local.
  * A CLI também pode instalá-lo: `openclaw gateway install`.


Comportamento:

  * "OpenClaw Ativo" ativa/desativa o LaunchAgent.
  * Sair do app **não** interrompe o gateway (o launchd o mantém ativo).
  * Se um Gateway já estiver em execução na porta configurada, o app se conecta a ele em vez de iniciar um novo.


Logs:

  * stdout/err do launchd: `/tmp/openclaw/openclaw-gateway.log`


## Compatibilidade de versões

O app macOS verifica a versão do gateway em relação à sua própria versão. Se elas forem incompatíveis, atualize a CLI global para corresponder à versão do app.

## Verificação smoke

bashCopy code
[code]
    openclaw --version OPENCLAW_SKIP_CHANNELS=1 \OPENCLAW_SKIP_CANVAS_HOST=1 \openclaw gateway --port 18999 --bind loopback
[/code]

Em seguida:

bashCopy code
[code]
    openclaw gateway call health --url ws://127.0.0.1:18999 --timeout 3000
[/code]

## Relacionado

  * [app macOS](</pt-BR/platforms/macos>)
  * [Runbook do Gateway](</pt-BR/gateway>)


Was this useful?YesNo