---
title: Conclusão
source_url: https://docs.openclaw.ai/pt-BR/cli/completion
scraped_at: 2026-05-25
---

# `openclaw completion`

Gere scripts de conclusão de shell e, opcionalmente, instale-os no perfil do seu shell.

## Uso

bashCopy code
[code]
    openclaw completionopenclaw completion --shell zshopenclaw completion --installopenclaw completion --shell fish --installopenclaw completion --write-stateopenclaw completion --shell bash --write-state
[/code]

## Opções

  * `-s, --shell <shell>`: shell de destino (`zsh`, `bash`, `powershell`, `fish`; padrão: `zsh`)
  * `-i, --install`: instala a conclusão adicionando uma linha de source ao perfil do seu shell
  * `--write-state`: grava o(s) script(s) de conclusão em `$OPENCLAW_STATE_DIR/completions` sem imprimir no stdout
  * `-y, --yes`: ignora prompts de confirmação de instalação


## Observações

  * `--install` grava um pequeno bloco "OpenClaw Completion" no perfil do seu shell e o aponta para o script em cache.
  * Sem `--install` ou `--write-state`, o comando imprime o script no stdout.
  * A geração de conclusão carrega antecipadamente as árvores de comandos para incluir subcomandos aninhados.


## Relacionado

  * [Referência de CLI](</pt-BR/cli>)


Was this useful?YesNo