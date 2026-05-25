---
title: Desinstalar
source_url: https://docs.openclaw.ai/pt-BR/cli/uninstall
scraped_at: 2026-05-25
---

# `openclaw uninstall`

Desinstala o serviço do gateway + dados locais (a CLI permanece).

Opções:

  * `--service`: remove o serviço do gateway
  * `--state`: remove o estado e a configuração
  * `--workspace`: remove diretórios de workspace
  * `--app`: remove o app do macOS
  * `--all`: remove serviço, estado, workspace e app
  * `--yes`: ignora prompts de confirmação
  * `--non-interactive`: desabilita prompts; requer `--yes`
  * `--dry-run`: imprime as ações sem remover arquivos


Exemplos:

bashCopy code
[code]
    openclaw backup createopenclaw uninstallopenclaw uninstall --service --yes --non-interactiveopenclaw uninstall --state --workspace --yes --non-interactiveopenclaw uninstall --all --yesopenclaw uninstall --dry-run
[/code]

Observações:

  * Execute `openclaw backup create` primeiro se quiser um snapshot restaurável antes de remover o estado ou workspaces.
  * `--all` é um atalho para remover serviço, estado, workspace e app juntos.
  * `--non-interactive` requer `--yes`.


## Relacionado

  * [Referência da CLI](</pt-BR/cli>)
  * [Desinstalar](</pt-BR/install/uninstall>)


Was this useful?YesNo