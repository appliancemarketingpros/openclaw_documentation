---
title: Verificações de integridade (macOS)
source_url: https://docs.openclaw.ai/pt-BR/platforms/mac/health
scraped_at: 2026-05-25
---

# Verificações de integridade no macOS

Como ver se o canal vinculado está saudável a partir do app da barra de menus.

## Barra de menus

  * O ponto de status agora reflete a integridade do Baileys: 
    * Verde: vinculado + socket aberto recentemente.
    * Laranja: conectando/repetindo tentativas.
    * Vermelho: sessão encerrada ou probe falhou.
  * A linha secundária mostra "linked · auth 12m" ou exibe o motivo da falha.
  * O item de menu "Run Health Check" aciona um probe sob demanda.


## Configurações

  * A aba General ganha um cartão Health mostrando: idade da autenticação vinculada, caminho/contagem do armazenamento de sessão, hora da última verificação, último erro/código de status e botões para Run Health Check / Reveal Logs.
  * Usa um snapshot em cache para que a interface carregue instantaneamente e recue de forma elegante quando offline.
  * A aba **Channels** exibe status de canal + controles para WhatsApp/Telegram (QR de login, logout, probe, último disconnect/error).


## Como o probe funciona

  * O app executa `openclaw health --json` via `ShellExecutor` a cada ~60s e sob demanda. O probe carrega credenciais e relata o status sem enviar mensagens.
  * Faça cache do último snapshot válido e do último erro separadamente para evitar cintilação; mostre o timestamp de cada um.


## Em caso de dúvida

  * Você ainda pode usar o fluxo de CLI em [Integridade do Gateway](</pt-BR/gateway/health>) (`openclaw status`, `openclaw status --deep`, `openclaw health --json`) e acompanhar `/tmp/openclaw/openclaw-*.log` para `web-heartbeat` / `web-reconnect`.


## Relacionado

  * [Integridade do Gateway](</pt-BR/gateway/health>)
  * [App do macOS](</pt-BR/platforms/macos>)


Was this useful?YesNo