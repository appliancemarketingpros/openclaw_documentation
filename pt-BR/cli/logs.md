---
title: Registros
source_url: https://docs.openclaw.ai/pt-BR/cli/logs
scraped_at: 2026-05-25
---

# `openclaw logs`

Acompanhe logs de arquivo do Gateway via RPC (funciona em modo remoto).

Relacionado:

  * Visão geral de logging: [Logging](</pt-BR/logging>)
  * CLI do Gateway: [gateway](</pt-BR/cli/gateway>)


## Opções

  * `--limit <n>`: número máximo de linhas de log a retornar (padrão `200`)
  * `--max-bytes <n>`: número máximo de bytes a ler do arquivo de log (padrão `250000`)
  * `--follow`: acompanhar o fluxo de logs
  * `--interval <ms>`: intervalo de polling durante o acompanhamento (padrão `1000`)
  * `--json`: emitir eventos JSON delimitados por linha
  * `--plain`: saída em texto simples sem formatação estilizada
  * `--no-color`: desabilitar cores ANSI
  * `--local-time`: renderizar timestamps no seu fuso horário local


## Opções RPC compartilhadas do Gateway

`openclaw logs` também aceita as flags padrão do cliente Gateway:

  * `--url <url>`: URL WebSocket do Gateway
  * `--token <token>`: token do Gateway
  * `--timeout <ms>`: timeout em ms (padrão `30000`)
  * `--expect-final`: aguardar uma resposta final quando a chamada ao Gateway for apoiada por agente


Quando você passa `--url`, a CLI não aplica automaticamente configuração nem credenciais de ambiente. Inclua `--token` explicitamente se o Gateway de destino exigir autenticação.

## Exemplos

bashCopy code
[code]
    openclaw logsopenclaw logs --followopenclaw logs --follow --interval 2000openclaw logs --limit 500 --max-bytes 500000openclaw logs --jsonopenclaw logs --plainopenclaw logs --no-coloropenclaw logs --limit 500openclaw logs --local-timeopenclaw logs --follow --local-timeopenclaw logs --url ws://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"
[/code]

## Observações

  * Use `--local-time` para renderizar timestamps no seu fuso horário local.
  * Se o Gateway local loopback implícito solicitar pareamento, fechar durante a conexão ou atingir timeout antes que `logs.tail` responda, `openclaw logs` recorre automaticamente ao arquivo de log configurado do Gateway. Destinos explícitos com `--url` não usam esse fallback.
  * Ao usar `--follow`, desconexões transitórias do Gateway (fechamento do WebSocket, timeout, queda de conexão) acionam reconexão automática com recuo exponencial (até 8 tentativas, limitado a 30 s entre tentativas). Um aviso é impresso em stderr a cada nova tentativa, e um aviso `[logs] gateway reconnected` é impresso quando um polling é bem-sucedido. No modo `--json`, tanto o aviso de nova tentativa quanto a transição de reconexão são emitidos como registros `{"type":"notice"}` em stderr. Erros não recuperáveis (falha de autenticação, configuração incorreta) ainda encerram imediatamente.


## Relacionado

  * [Referência da CLI](</pt-BR/cli>)
  * [Logging do Gateway](</pt-BR/gateway/logging>)


Was this useful?YesNo