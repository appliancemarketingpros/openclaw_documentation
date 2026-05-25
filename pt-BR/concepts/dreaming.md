---
title: Dreaming
source_url: https://docs.openclaw.ai/pt-BR/concepts/dreaming
scraped_at: 2026-05-25
---

Dreaming é o sistema de consolidação de memória em segundo plano no `memory-core`. Ele ajuda o OpenClaw a mover sinais fortes de curto prazo para a memória durável, mantendo o processo explicável e revisável.

## O que o dreaming grava

Dreaming mantém dois tipos de saída:

  * **Estado da máquina** em `memory/.dreams/` (armazenamento de recuperação, sinais de fase, checkpoints de ingestão, locks).
  * **Saída legível por humanos** em `DREAMS.md` (ou `dreams.md` existente) e arquivos opcionais de relatório de fase em `memory/dreaming/<phase>/YYYY-MM-DD.md`.


A promoção de longo prazo ainda grava apenas em `MEMORY.md`.

## Modelo de fases

Dreaming usa três fases cooperativas:

Fase | Propósito | Gravação durável  
---|---|---  
Leve | Classificar e preparar material recente de curto prazo | Não  
Profunda | Pontuar e promover candidatos duráveis | Sim (`MEMORY.md`)  
REM | Refletir sobre temas e ideias recorrentes | Não  
  
Essas fases são detalhes internos de implementação, não "modos" separados configurados pelo usuário.

Fase leve

A fase leve ingere sinais recentes de memória diária e rastros de recuperação, remove duplicatas e prepara linhas candidatas.

  * Lê do estado de recuperação de curto prazo, arquivos recentes de memória diária e transcrições de sessão redigidas quando disponíveis.
  * Grava um bloco `## Light Sleep` gerenciado quando o armazenamento inclui saída inline.
  * Registra sinais de reforço para ranqueamento profundo posterior.
  * Nunca grava em `MEMORY.md`.

Fase profunda

A fase profunda decide o que se torna memória de longo prazo.

  * Ranqueia candidatos usando pontuação ponderada e gates de limite.
  * Exige que `minScore`, `minRecallCount` e `minUniqueQueries` sejam aprovados.
  * Reidrata snippets de arquivos diários ativos antes de gravar, então snippets obsoletos/excluídos são ignorados.
  * Acrescenta entradas promovidas a `MEMORY.md`.
  * Grava um resumo `## Deep Sleep` em `DREAMS.md` e, opcionalmente, grava `memory/dreaming/deep/YYYY-MM-DD.md`.

Fase REM

A fase REM extrai padrões e sinais reflexivos.

  * Cria resumos de temas e reflexões a partir de rastros recentes de curto prazo.
  * Grava um bloco `## REM Sleep` gerenciado quando o armazenamento inclui saída inline.
  * Registra sinais de reforço REM usados pelo ranqueamento profundo.
  * Nunca grava em `MEMORY.md`.


## Ingestão de transcrições de sessão

Dreaming pode ingerir transcrições de sessão redigidas no corpus de dreaming. Quando as transcrições estão disponíveis, elas são enviadas para a fase leve junto com sinais de memória diária e rastros de recuperação. Conteúdo pessoal e sensível é redigido antes da ingestão.

## Dream Diary

Dreaming também mantém um **Dream Diary** narrativo em `DREAMS.md`. Depois que cada fase tem material suficiente, `memory-core` executa uma rodada de subagente em segundo plano em modo best-effort e acrescenta uma entrada curta de diário. Ele usa o modelo padrão de runtime, a menos que `dreaming.model` esteja configurado. Se o modelo configurado estiver indisponível, o Dream Diary tenta novamente uma vez com o modelo padrão da sessão.

Também há uma trilha de backfill histórico fundamentado para trabalho de revisão e recuperação:

Comandos de backfill

  * `memory rem-harness --path ... --grounded` pré-visualiza a saída de diário fundamentada a partir de notas históricas `YYYY-MM-DD.md`.
  * `memory rem-backfill --path ...` grava entradas reversíveis de diário fundamentado em `DREAMS.md`.
  * `memory rem-backfill --path ... --stage-short-term` prepara candidatos duráveis fundamentados no mesmo armazenamento de evidências de curto prazo que a fase profunda normal já usa.
  * `memory rem-backfill --rollback` e `--rollback-short-term` removem esses artefatos de backfill preparados sem tocar em entradas comuns de diário ou na recuperação ativa de curto prazo.


A Control UI expõe o mesmo fluxo de backfill/reset de diário para que você possa inspecionar os resultados na cena Dreams antes de decidir se os candidatos fundamentados merecem promoção. A Scene também mostra uma trilha fundamentada distinta para que você possa ver quais entradas de curto prazo preparadas vieram de replay histórico, quais itens promovidos foram conduzidos por fundamentação, e limpar apenas entradas preparadas exclusivamente fundamentadas sem tocar no estado ativo comum de curto prazo.

## Sinais de ranqueamento profundo

O ranqueamento profundo usa seis sinais base ponderados mais reforço de fase:

Sinal | Peso | Descrição  
---|---|---  
Frequência | 0.24 | Quantos sinais de curto prazo a entrada acumulou  
Relevância | 0.30 | Qualidade média de recuperação da entrada  
Diversidade de consulta | 0.15 | Contextos distintos de consulta/dia que a revelaram  
Recência | 0.15 | Pontuação de atualidade com decaimento temporal  
Consolidação | 0.10 | Força de recorrência em vários dias  
Riqueza conceitual | 0.06 | Densidade de tags conceituais do snippet/caminho  
  
Acertos das fases leve e REM adicionam um pequeno boost com decaimento por recência a partir de `memory/.dreams/phase-signals.json`.

## Agendamento

Quando habilitado, `memory-core` gerencia automaticamente um job cron para uma varredura completa de dreaming. Cada varredura executa as fases em ordem: leve → REM → profunda.

A varredura inclui o workspace principal de runtime e quaisquer workspaces de agentes configurados, sem duplicatas por caminho, para que o fan-out de workspace de subagentes não exclua o `DREAMS.md` e o estado de memória do agente principal.

Comportamento de cadência padrão:

Configuração | Padrão  
---|---  
`dreaming.frequency` | `0 3 * * *`  
`dreaming.model` | modelo padrão  
  
## Início rápido

### Habilitar dreaming

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "memory-core": {        "config": {          "dreaming": {            "enabled": true          }        }      }    }  }}
[/code]

### Cadência personalizada de varredura

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "memory-core": {        "config": {          "dreaming": {            "enabled": true,            "timezone": "America/Los_Angeles",            "frequency": "0 */6 * * *"          }        }      }    }  }}
[/code]

## Comando slash

CodeCopy code
[code]
    /dreaming status/dreaming on/dreaming off/dreaming help
[/code]

## Fluxo de trabalho da CLI

### Prévia / aplicação de promoção

bashCopy code
[code]
    openclaw memory promoteopenclaw memory promote --applyopenclaw memory promote --limit 5openclaw memory status --deep
[/code]

O `memory promote` manual usa os limites da fase profunda por padrão, a menos que sejam sobrescritos com flags da CLI.

### Explicar promoção

Explique por que um candidato específico seria ou não promovido:

bashCopy code
[code]
    openclaw memory promote-explain "router vlan"openclaw memory promote-explain "router vlan" --json
[/code]

### Prévia do harness REM

Pré-visualize reflexões REM, verdades candidatas e saída de promoção profunda sem gravar nada:

bashCopy code
[code]
    openclaw memory rem-harnessopenclaw memory rem-harness --json
[/code]

## Principais padrões

Todas as configurações ficam em `plugins.entries.memory-core.config.dreaming`.

Habilite ou desabilite a varredura de dreaming.

Cadência Cron para a varredura completa de dreaming.

Sobrescrita opcional de modelo de subagente do Dream Diary. Use um valor canônico `provider/model` ao também definir uma allowlist `allowedModels` de subagente.

## UI Dreams

Quando habilitada, a aba **Dreams** do Gateway mostra:

  * estado atual de dreaming habilitado
  * status em nível de fase e presença de varredura gerenciada
  * contagens de curto prazo, fundamentadas, de sinais e promovidas hoje
  * horário da próxima execução agendada
  * uma trilha Scene fundamentada distinta para entradas preparadas de replay histórico
  * um leitor expansível do Dream Diary apoiado por `doctor.memory.dreamDiary`


## Dreaming nunca executa: o status mostra bloqueado

Se `openclaw memory status` relatar `Dreaming status: blocked`, o cron gerenciado existe, mas o Heartbeat do agente padrão não está disparando. Verifique se o Heartbeat está habilitado para o agente padrão e se o destino dele não é `none`; depois execute `openclaw memory status --deep` novamente após o próximo intervalo de Heartbeat.

## Relacionado

  * [Memória](</pt-BR/concepts/memory>)
  * [CLI de memória](</pt-BR/cli/memory>)
  * [Referência de configuração de memória](</pt-BR/reference/memory-config>)
  * [Busca de memória](</pt-BR/concepts/memory-search>)


Was this useful?YesNo