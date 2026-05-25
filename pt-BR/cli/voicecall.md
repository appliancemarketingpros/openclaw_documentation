---
title: Chamada de voz
source_url: https://docs.openclaw.ai/pt-BR/cli/voicecall
scraped_at: 2026-05-25
---

# `openclaw voicecall`

`voicecall` é um comando fornecido por Plugin. Ele aparece somente quando o Plugin voice-call está instalado e habilitado.

Quando o Gateway está em execução, os comandos operacionais (`call`, `start`, `continue`, `speak`, `dtmf`, `end`, `status`) são roteados para o runtime de chamada de voz desse Gateway. Se nenhum Gateway estiver acessível, eles recorrem a um runtime CLI independente.

## Subcomandos

bashCopy code
[code]
    openclaw voicecall setup    [--json]openclaw voicecall smoke    [-t <phone>] [--message <text>] [--mode <m>] [--yes] [--json]openclaw voicecall call     -m <text> [-t <phone>] [--mode <m>]openclaw voicecall start    --to <phone> [--message <text>] [--mode <m>]openclaw voicecall continue --call-id <id> --message <text>openclaw voicecall speak    --call-id <id> --message <text>openclaw voicecall dtmf     --call-id <id> --digits <digits>openclaw voicecall end      --call-id <id>openclaw voicecall status   [--call-id <id>] [--json]openclaw voicecall tail     [--file <path>] [--since <n>] [--poll <ms>]openclaw voicecall latency  [--file <path>] [--last <n>]openclaw voicecall expose   [--mode <m>] [--path <p>] [--port <port>] [--serve-path <p>]
[/code]

Subcomando | Descrição  
---|---  
`setup` | Mostra verificações de prontidão do provedor e do Webhook.  
`smoke` | Executa verificações de prontidão; faz uma chamada de teste real somente com `--yes`.  
`call` | Inicia uma chamada de voz de saída.  
`start` | Alias para `call` com `--to` obrigatório e `--message` opcional.  
`continue` | Fala uma mensagem e aguarda a próxima resposta.  
`speak` | Fala uma mensagem sem aguardar uma resposta.  
`dtmf` | Envia dígitos DTMF para uma chamada ativa.  
`end` | Desliga uma chamada ativa.  
`status` | Inspeciona chamadas ativas (ou uma por `--call-id`).  
`tail` | Acompanha `calls.jsonl` (útil durante testes de provedor).  
`latency` | Resume métricas de latência de turno de `calls.jsonl`.  
`expose` | Alterna Tailscale serve/funnel para o endpoint do Webhook.  
  
## Configuração e smoke

### `setup`

Imprime verificações de prontidão legíveis por humanos por padrão. Passe `--json` para scripts.

bashCopy code
[code]
    openclaw voicecall setupopenclaw voicecall setup --json
[/code]

### `smoke`

Executa as mesmas verificações de prontidão. Ele não fará uma chamada telefônica real a menos que `--to` e `--yes` estejam presentes.

Flag | Padrão | Descrição  
---|---|---  
`-t, --to <phone>` | (nenhum) | Número de telefone para ligar em um smoke real.  
`--message <text>` | `OpenClaw voice call smoke test.` | Mensagem a ser falada durante a chamada smoke.  
`--mode <mode>` | `notify` | Modo da chamada: `notify` ou `conversation`.  
`--yes` | `false` | Faz de fato a chamada de saída real.  
`--json` | `false` | Imprime JSON legível por máquina.  
bashCopy code
[code]
    openclaw voicecall smokeopenclaw voicecall smoke --to "+15555550123"        # dry runopenclaw voicecall smoke --to "+15555550123" --yes  # live notify call
[/code]

## Ciclo de vida da chamada

### `call`

Inicia uma chamada de voz de saída.

Flag | Obrigatório | Padrão | Descrição  
---|---|---|---  
`-m, --message <text>` | sim | (nenhum) | Mensagem a ser falada quando a chamada conectar.  
`-t, --to <phone>` | não | config `toNumber` | Número de telefone E.164 para ligar.  
`--mode <mode>` | não | `conversation` | Modo da chamada: `notify` (desliga após a mensagem) ou `conversation` (permanece aberta).  
bashCopy code
[code]
    openclaw voicecall call --to "+15555550123" --message "Hello"openclaw voicecall call -m "Heads up" --mode notify
[/code]

### `start`

Alias para `call` com um formato de flags padrão diferente.

Flag | Obrigatório | Padrão | Descrição  
---|---|---|---  
`--to <phone>` | sim | (nenhum) | Número de telefone para ligar.  
`--message <text>` | não | (nenhum) | Mensagem a ser falada quando a chamada conectar.  
`--mode <mode>` | não | `conversation` | Modo da chamada: `notify` ou `conversation`.  
  
### `continue`

Fala uma mensagem e aguarda uma resposta.

Flag | Obrigatório | Descrição  
---|---|---  
`--call-id <id>` | sim | ID da chamada.  
`--message <text>` | sim | Mensagem a ser falada.  
  
### `speak`

Fala uma mensagem sem aguardar uma resposta.

Flag | Obrigatório | Descrição  
---|---|---  
`--call-id <id>` | sim | ID da chamada.  
`--message <text>` | sim | Mensagem a ser falada.  
  
### `dtmf`

Envia dígitos DTMF para uma chamada ativa.

Flag | Obrigatório | Descrição  
---|---|---  
`--call-id <id>` | sim | ID da chamada.  
`--digits <digits>` | sim | Dígitos DTMF (por exemplo, `ww123456#` para esperas).  
  
### `end`

Desliga uma chamada ativa.

Flag | Obrigatório | Descrição  
---|---|---  
`--call-id <id>` | sim | ID da chamada.  
  
### `status`

Inspeciona chamadas ativas.

Flag | Padrão | Descrição  
---|---|---  
`--call-id <id>` | (nenhum) | Restringe a saída a uma chamada.  
`--json` | `false` | Imprime JSON legível por máquina.  
bashCopy code
[code]
    openclaw voicecall statusopenclaw voicecall status --jsonopenclaw voicecall status --call-id <id>
[/code]

## Logs e métricas

### `tail`

Acompanha o log JSONL de chamadas de voz. Imprime as últimas `--since` linhas ao iniciar e, em seguida, transmite novas linhas conforme são gravadas.

Flag | Padrão | Descrição  
---|---|---  
`--file <path>` | resolvido pelo store do Plugin | Caminho para `calls.jsonl`.  
`--since <n>` | `25` | Linhas a imprimir antes de acompanhar.  
`--poll <ms>` | `250` (mínimo 50) | Intervalo de sondagem em milissegundos.  
  
### `latency`

Resume métricas de latência de turno e espera de escuta de `calls.jsonl`. A saída é JSON com resumos de `recordsScanned`, `turnLatency` e `listenWait`.

Flag | Padrão | Descrição  
---|---|---  
`--file <path>` | resolvido pelo store do Plugin | Caminho para `calls.jsonl`.  
`--last <n>` | `200` (mínimo 1) | Número de registros recentes a analisar.  
  
## Expondo Webhooks

### `expose`

Habilita, desabilita ou altera a configuração de Tailscale serve/funnel para o Webhook de voz.

Flag | Padrão | Descrição  
---|---|---  
`--mode <mode>` | `funnel` | `off`, `serve` (tailnet) ou `funnel` (público).  
`--path <path>` | config `tailscale.path` ou `--serve-path` | Caminho Tailscale a expor.  
`--port <port>` | config `serve.port` ou `3334` | Porta local do Webhook.  
`--serve-path <path>` | config `serve.path` ou `/voice/webhook` | Caminho local do Webhook.  
bashCopy code
[code]
    openclaw voicecall expose --mode serveopenclaw voicecall expose --mode funnelopenclaw voicecall expose --mode off
[/code]

## Relacionado

  * [Referência da CLI](</pt-BR/cli>)
  * [Plugin de chamada de voz](</pt-BR/plugins/voice-call>)


Was this useful?YesNo