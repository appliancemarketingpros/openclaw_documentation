---
title: Redefinir
source_url: https://docs.openclaw.ai/pt-BR/cli/reset
scraped_at: 2026-05-25
---

# `openclaw reset`

Redefine a configuração/estado local (mantém a CLI instalada).

Opções:

  * `--scope <scope>`: `config`, `config+creds+sessions` ou `full`
  * `--yes`: ignora prompts de confirmação
  * `--non-interactive`: desabilita prompts; exige `--scope` e `--yes`
  * `--dry-run`: imprime ações sem remover arquivos


Exemplos:

bashCopy code
[code]
    openclaw backup createopenclaw resetopenclaw reset --dry-runopenclaw reset --scope config --yes --non-interactiveopenclaw reset --scope config+creds+sessions --yes --non-interactiveopenclaw reset --scope full --yes --non-interactive
[/code]

Observações:

  * Execute `openclaw backup create` primeiro se quiser um snapshot restaurável antes de remover o estado local.
  * Se você omitir `--scope`, `openclaw reset` usa um prompt interativo para escolher o que remover.
  * `--non-interactive` só é válido quando `--scope` e `--yes` estão definidos.


## Relacionado

  * [Referência da CLI](</pt-BR/cli>)


Was this useful?YesNo