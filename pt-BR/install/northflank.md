---
title: Northflank
source_url: https://docs.openclaw.ai/pt-BR/install/northflank
scraped_at: 2026-05-25
---

# Northflank

Implante o OpenClaw no Northflank com um modelo de um clique e acesse-o pela Interface de controle web. Este é o caminho mais fácil de “sem terminal no servidor”: o Northflank executa o Gateway para você.

## Como começar

  1. Clique em [Deploy OpenClaw](<https://northflank.com/stacks/deploy-openclaw>) para abrir o modelo.
  2. Crie uma [conta no Northflank](<https://app.northflank.com/signup>) se ainda não tiver uma.
  3. Clique em **Deploy OpenClaw now**.
  4. Defina a variável de ambiente obrigatória: `OPENCLAW_GATEWAY_TOKEN` (use um valor aleatório forte).
  5. Clique em **Deploy stack** para compilar e executar o modelo OpenClaw.
  6. Aguarde a conclusão da implantação e clique em **View resources**.
  7. Abra o serviço OpenClaw.
  8. Abra a URL pública do OpenClaw em `/openclaw` e conecte-se usando o segredo compartilhado configurado. Este modelo usa `OPENCLAW_GATEWAY_TOKEN` por padrão; se você substituí-lo por autenticação por senha, use essa senha no lugar.


## O que você recebe

  * Gateway OpenClaw hospedado + Interface de controle
  * Armazenamento persistente via Volume do Northflank (`/data`) para que `openclaw.json`, `auth-profiles.json` por agente, estado de canal/provider, sessões e espaço de trabalho sobrevivam a reimplantações


## Conectar um canal

Use a Interface de controle em `/openclaw` ou execute `openclaw onboard` via SSH para obter instruções de configuração de canal:

  * [Telegram](</pt-BR/channels/telegram>) (mais rápido — apenas um token de bot)
  * [Discord](</pt-BR/channels/discord>)
  * [Todos os canais](</pt-BR/channels>)


## Próximos passos

  * Configure canais de mensagens: [Canais](</pt-BR/channels>)
  * Configure o Gateway: [Configuração do Gateway](</pt-BR/gateway/configuration>)
  * Mantenha o OpenClaw atualizado: [Atualização](</pt-BR/install/updating>)


Was this useful?YesNo