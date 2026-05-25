---
title: Flags de diagnóstico
source_url: https://docs.openclaw.ai/pt-BR/diagnostics/flags
scraped_at: 2026-05-25
---

Os sinalizadores de diagnóstico permitem ativar logs de depuração direcionados sem habilitar logs detalhados em todos os lugares. Os sinalizadores são opcionais e não têm efeito a menos que um subsistema os verifique.

## Como funciona

  * Os sinalizadores são strings (sem diferenciar maiúsculas de minúsculas).
  * Você pode ativar sinalizadores na configuração ou por meio de uma substituição de env.
  * Curingas são compatíveis: 
    * `telegram.*` corresponde a `telegram.http`
    * `*` ativa todos os sinalizadores


## Ativar via configuração

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http"]  }}
[/code]

Vários sinalizadores:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http", "brave.http", "gateway.*"]  }}
[/code]

Reinicie o gateway após alterar os sinalizadores.

## Substituição por env (uso único)

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=telegram.http,telegram.payload
[/code]

Desativar todos os sinalizadores:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=0
[/code]

## Artefatos de linha do tempo

O sinalizador `timeline` grava eventos estruturados de temporização de inicialização e execução para estruturas externas de QA:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=timeline \OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=/tmp/openclaw-timeline.jsonl \openclaw gateway run
[/code]

Você também pode ativá-lo na configuração:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["timeline"]  }}
[/code]

O caminho do arquivo de linha do tempo ainda vem de `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH`. Quando `timeline` é ativado apenas pela configuração, os primeiros intervalos de carregamento da configuração não são emitidos porque o OpenClaw ainda não leu a configuração; os intervalos subsequentes de inicialização usam o sinalizador da configuração.

`OPENCLAW_DIAGNOSTICS=1`, `OPENCLAW_DIAGNOSTICS=all` e `OPENCLAW_DIAGNOSTICS=*` também ativam a linha do tempo porque ativam todos os sinalizadores de diagnóstico. Prefira `timeline` quando você quiser apenas o artefato de temporização JSONL.

Os registros de linha do tempo usam o envelope `openclaw.diagnostics.v1`. Eventos podem incluir ids de processo, nomes de fase, nomes de intervalo, durações, ids de plugin, contagens de dependências, amostras de atraso do loop de eventos, nomes de operações de provedores, estado de saída de processos filhos e nomes/mensagens de erros de inicialização. Trate os arquivos de linha do tempo como artefatos de diagnóstico locais; revise-os antes de compartilhá-los fora da sua máquina.

## Para onde vão os logs

Os sinalizadores emitem logs no arquivo de log de diagnóstico padrão. Por padrão:

CodeCopy code
[code]
    /tmp/openclaw/openclaw-YYYY-MM-DD.log
[/code]

Se você definir `logging.file`, use esse caminho em vez disso. Os logs são JSONL (um objeto JSON por linha). A redação ainda se aplica com base em `logging.redactSensitive`.

## Extrair logs

Escolha o arquivo de log mais recente:

bashCopy code
[code]
    ls -t /tmp/openclaw/openclaw-*.log | head -n 1
[/code]

Filtre diagnósticos HTTP do Telegram:

bashCopy code
[code]
    rg "telegram http error" /tmp/openclaw/openclaw-*.log
[/code]

Filtre diagnósticos HTTP do Brave Search:

bashCopy code
[code]
    rg "brave http" /tmp/openclaw/openclaw-*.log
[/code]

Ou acompanhe enquanto reproduz:

bashCopy code
[code]
    tail -f /tmp/openclaw/openclaw-$(date +%F).log | rg "telegram http error"
[/code]

Para gateways remotos, você também pode usar `openclaw logs --follow` (consulte [/cli/logs](</pt-BR/cli/logs>)).

## Observações

  * Se `logging.level` estiver definido acima de `warn`, esses logs poderão ser suprimidos. O padrão `info` é adequado.
  * `brave.http` registra URLs/parâmetros de consulta de solicitações do Brave Search, status/tempo de resposta e eventos de acerto/erro/gravação de cache. Ele não registra chaves de API nem corpos de resposta, mas consultas de busca podem ser sensíveis.
  * É seguro deixar os sinalizadores ativados; eles afetam apenas o volume de logs do subsistema específico.
  * Use [/logging](</pt-BR/logging>) para alterar destinos, níveis e redação de logs.


## Relacionado

  * [Diagnóstico do Gateway](</pt-BR/gateway/diagnostics>)
  * [Solução de problemas do Gateway](</pt-BR/gateway/troubleshooting>)


Was this useful?YesNo