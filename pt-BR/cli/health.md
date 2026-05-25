---
title: Saúde
source_url: https://docs.openclaw.ai/pt-BR/cli/health
scraped_at: 2026-05-25
---

# `openclaw health`

Busca a integridade do Gateway em execução.

## Opções

Opção | Padrão | Descrição  
---|---|---  
`--json` | `false` | Imprime JSON legível por máquina em vez de texto.  
`--timeout <ms>` | `10000` | Tempo limite da conexão em milissegundos.  
`--verbose` | `false` | Registro detalhado. Força uma sondagem ativa e expande a saída por agente.  
`--debug` | `false` | Alias para `--verbose`.  
  
Exemplos:

bashCopy code
[code]
    openclaw healthopenclaw health --jsonopenclaw health --timeout 2500openclaw health --verboseopenclaw health --debug
[/code]

Observações:

  * Por padrão, `openclaw health` solicita ao Gateway em execução o instantâneo de integridade. Quando o Gateway já tem um instantâneo em cache recente, ele pode retornar essa carga útil em cache e atualizar em segundo plano.
  * `--verbose` força uma sondagem ativa, imprime os detalhes de conexão do Gateway e expande a saída legível por humanos em todas as contas e agentes configurados.
  * A saída inclui armazenamentos de sessão por agente quando vários agentes estão configurados.


## Relacionados

  * [Referência da CLI](</pt-BR/cli>)
  * [Integridade do Gateway](</pt-BR/gateway/health>)


Was this useful?YesNo