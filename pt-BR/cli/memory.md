---
title: Memória
source_url: https://docs.openclaw.ai/pt-BR/cli/memory
scraped_at: 2026-05-25
---

# `openclaw memory`

Gerencie a indexação e a busca de memória semântica. Fornecido pelo Plugin Active Memory (padrão: `memory-core`; defina `plugins.slots.memory = "none"` para desativar).

Relacionado:

  * Conceito de memória: [Memória](</pt-BR/concepts/memory>)
  * Wiki de memória: [Wiki de Memória](</pt-BR/plugins/memory-wiki>)
  * CLI da wiki: [wiki](</pt-BR/cli/wiki>)
  * Plugins: [Plugins](</pt-BR/tools/plugin>)


## Exemplos

bashCopy code
[code]
    openclaw memory statusopenclaw memory status --deepopenclaw memory status --fixopenclaw memory index --forceopenclaw memory search "meeting notes"openclaw memory search --query "deployment" --max-results 20openclaw memory promote --limit 10 --min-score 0.75openclaw memory promote --applyopenclaw memory promote --json --min-recall-count 0 --min-unique-queries 0openclaw memory promote-explain "router vlan"openclaw memory promote-explain "router vlan" --jsonopenclaw memory rem-harnessopenclaw memory rem-harness --jsonopenclaw memory status --jsonopenclaw memory status --deep --indexopenclaw memory status --deep --index --verboseopenclaw memory status --agent mainopenclaw memory index --agent main --verbose
[/code]

## Opções

`memory status` e `memory index`:

  * `--agent <id>`: limita o escopo a um único agente. Sem isso, esses comandos são executados para cada agente configurado; se nenhuma lista de agentes estiver configurada, eles usam o agente padrão.
  * `--verbose`: emite logs detalhados durante sondagens e indexação.


`memory status`:

  * `--deep`: sonda a prontidão do armazenamento vetorial local, a prontidão do provedor de embeddings e a prontidão da busca vetorial semântica. `memory status` simples permanece rápido e não executa trabalho ativo de embeddings nem descoberta de provedores; estado desconhecido de armazenamento vetorial ou vetor semântico significa que ele não foi sondado nesse comando. `searchMode: "search"` lexical de QMD ignora sondagens de vetores semânticos e manutenção de embeddings mesmo com `--deep`.
  * `--index`: executa uma reindexação se o armazenamento estiver sujo (implica `--deep`).
  * `--fix`: repara travas de recall obsoletas e normaliza metadados de promoção.
  * `--json`: imprime saída JSON.


Se `memory status` mostrar `Dreaming status: blocked`, o cron gerenciado de Dreaming está ativado, mas o heartbeat que o aciona não está disparando para o agente padrão. Consulte [Dreaming nunca é executado](</pt-BR/concepts/dreaming#dreaming-never-runs-status-shows-blocked>) para as duas causas comuns.

`memory index`:

  * `--force`: força uma reindexação completa.


`memory search`:

  * Entrada de consulta: passe `[query]` posicional ou `--query <text>`.
  * Se ambos forem fornecidos, `--query` prevalece.
  * Se nenhum for fornecido, o comando sai com erro.
  * `--agent <id>`: limita o escopo a um único agente (padrão: o agente padrão).
  * `--max-results <n>`: limita o número de resultados retornados.
  * `--min-score <n>`: filtra correspondências com pontuação baixa.
  * `--json`: imprime resultados JSON.


`memory promote`:

Pré-visualize e aplique promoções de memória de curto prazo.

bashCopy code
[code]
    openclaw memory promote [--apply] [--limit <n>] [--include-promoted]
[/code]

  * `--apply` \-- grava promoções em `MEMORY.md` (padrão: apenas pré-visualização).
  * `--limit <n>` \-- limita o número de candidatos exibidos.
  * `--include-promoted` \-- inclui entradas já promovidas em ciclos anteriores.


Opções completas:

  * Classifica candidatos de curto prazo de `memory/YYYY-MM-DD.md` usando sinais de promoção ponderados (`frequency`, `relevance`, `query diversity`, `recency`, `consolidation`, `conceptual richness`).
  * Usa sinais de curto prazo tanto de recalls de memória quanto de passagens de ingestão diária, além de sinais de reforço das fases leve/REM.
  * Quando Dreaming está ativado, `memory-core` gerencia automaticamente um cron job que executa uma varredura completa (`light -> REM -> deep`) em segundo plano (nenhum `openclaw cron add` manual é necessário).
  * `--agent <id>`: limita o escopo a um único agente (padrão: o agente padrão).
  * `--limit <n>`: máximo de candidatos a retornar/aplicar.
  * `--min-score <n>`: pontuação mínima ponderada de promoção.
  * `--min-recall-count <n>`: contagem mínima de recall exigida para um candidato.
  * `--min-unique-queries <n>`: contagem mínima de consultas distintas exigida para um candidato.
  * `--apply`: anexa os candidatos selecionados a `MEMORY.md` e os marca como promovidos.
  * `--include-promoted`: inclui candidatos já promovidos na saída.
  * `--json`: imprime saída JSON.


`memory promote-explain`:

Explique um candidato específico à promoção e o detalhamento de sua pontuação.

bashCopy code
[code]
    openclaw memory promote-explain <selector> [--agent <id>] [--include-promoted] [--json]
[/code]

  * `<selector>`: chave do candidato, fragmento de caminho ou fragmento de trecho a procurar.
  * `--agent <id>`: limita o escopo a um único agente (padrão: o agente padrão).
  * `--include-promoted`: inclui candidatos já promovidos.
  * `--json`: imprime saída JSON.


`memory rem-harness`:

Pré-visualize reflexões REM, verdades candidatas e saída de promoção profunda sem gravar nada.

bashCopy code
[code]
    openclaw memory rem-harness [--agent <id>] [--include-promoted] [--json]
[/code]

  * `--agent <id>`: limita o escopo a um único agente (padrão: o agente padrão).
  * `--include-promoted`: inclui candidatos profundos já promovidos.
  * `--json`: imprime saída JSON.


## Dreaming

Dreaming é o sistema de consolidação de memória em segundo plano com três fases cooperativas: **leve** (organizar/preparar material de curto prazo), **profunda** (promover fatos duráveis para `MEMORY.md`) e **REM** (refletir e revelar temas).

  * Ative com `plugins.entries.memory-core.config.dreaming.enabled: true`.
  * Alterne pelo chat com `/dreaming on|off` (ou inspecione com `/dreaming status`).
  * Dreaming é executado em uma programação de varredura gerenciada (`dreaming.frequency`) e executa as fases em ordem: leve, REM, profunda.
  * Somente a fase profunda grava memória durável em `MEMORY.md`.
  * A saída legível por humanos das fases e as entradas de diário são gravadas em `DREAMS.md` (ou no `dreams.md` existente), com relatórios opcionais por fase em `memory/dreaming/<phase>/YYYY-MM-DD.md`.
  * A classificação usa sinais ponderados: frequência de recall, relevância da recuperação, diversidade de consultas, recência temporal, consolidação entre dias e riqueza conceitual derivada.
  * A promoção relê a nota diária ativa antes de gravar em `MEMORY.md`, de modo que trechos de curto prazo editados ou excluídos não sejam promovidos a partir de snapshots obsoletos do armazenamento de recall.
  * Execuções agendadas e manuais de `memory promote` compartilham os mesmos padrões da fase profunda, a menos que você passe substituições de limiar pela CLI.
  * Execuções automáticas se distribuem por workspaces de memória configurados.


Agendamento padrão:

  * **Cadência de varredura** : `dreaming.frequency = 0 3 * * *`
  * **Limiares profundos** : `minScore=0.8`, `minRecallCount=3`, `minUniqueQueries=3`, `recencyHalfLifeDays=14`, `maxAgeDays=30`


Exemplo:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "memory-core": {        "config": {          "dreaming": {            "enabled": true          }        }      }    }  }}
[/code]

Observações:

  * `memory index --verbose` imprime detalhes por fase (provedor, modelo, fontes, atividade em lote).
  * `memory status` inclui quaisquer caminhos extras configurados via `memorySearch.extraPaths`.
  * Se campos de chave de API remota de Active Memory efetivamente ativos estiverem configurados como SecretRefs, o comando resolve esses valores a partir do snapshot ativo do Gateway. Se o Gateway estiver indisponível, o comando falha rapidamente.
  * Observação sobre divergência de versão do Gateway: este caminho de comando exige um Gateway compatível com `secrets.resolve`; gateways mais antigos retornam um erro de método desconhecido.
  * Ajuste a cadência de varredura agendada com `dreaming.frequency`. A política de promoção profunda é interna no restante; use flags de CLI em `memory promote` quando precisar de substituições manuais pontuais.
  * `memory rem-harness --path <file-or-dir> --grounded` pré-visualiza `What Happened`, `Reflections` e `Possible Lasting Updates` fundamentados a partir de notas diárias históricas sem gravar nada.
  * `memory rem-backfill --path <file-or-dir>` grava entradas de diário fundamentadas reversíveis em `DREAMS.md` para revisão na UI.
  * `memory rem-backfill --path <file-or-dir> --stage-short-term` também semeia candidatos duráveis fundamentados no armazenamento ativo de promoção de curto prazo para que a fase profunda normal possa classificá-los.
  * `memory rem-backfill --rollback` remove entradas de diário fundamentadas gravadas anteriormente, e `memory rem-backfill --rollback-short-term` remove candidatos fundamentados de curto prazo preparados anteriormente.
  * Consulte [Dreaming](</pt-BR/concepts/dreaming>) para descrições completas das fases e referência de configuração.


## Relacionado

  * [Referência da CLI](</pt-BR/cli>)
  * [Visão geral de memória](</pt-BR/concepts/memory>)


Was this useful?YesNo