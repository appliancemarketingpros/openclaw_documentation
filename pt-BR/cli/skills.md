---
title: Skills
source_url: https://docs.openclaw.ai/pt-BR/cli/skills
scraped_at: 2026-05-25
---

# `openclaw skills`

Inspecione Skills locais e instale/atualize Skills a partir do ClawHub.

Relacionado:

  * Sistema de Skills: [Skills](</pt-BR/tools/skills>)
  * Configuração de Skills: [Configuração de Skills](</pt-BR/tools/skills-config>)
  * Instalações do ClawHub: [ClawHub](</pt-BR/clawhub/cli>)


## Comandos

bashCopy code
[code]
    openclaw skills search "calendar"openclaw skills search --limit 20 --jsonopenclaw skills install <slug>openclaw skills install <slug> --version <version>openclaw skills install <slug> --forceopenclaw skills install <slug> --agent <id>openclaw skills update <slug>openclaw skills update --allopenclaw skills update --all --agent <id>openclaw skills listopenclaw skills list --eligibleopenclaw skills list --jsonopenclaw skills list --verboseopenclaw skills list --agent <id>openclaw skills info <name>openclaw skills info <name> --jsonopenclaw skills info <name> --agent <id>openclaw skills checkopenclaw skills check --agent <id>openclaw skills check --json
[/code]

`search`/`install`/`update` usam o ClawHub diretamente e instalam no diretório `skills/` do workspace ativo. `list`/`info`/`check` ainda inspecionam as Skills locais visíveis para o workspace e a configuração atuais. Comandos com base em workspace resolvem o workspace de destino a partir de `--agent <id>`, depois do diretório de trabalho atual quando ele está dentro de um workspace de agente configurado e, por fim, do agente padrão.

Este comando `install` da CLI baixa pastas de Skills do ClawHub. Instalações de dependências de Skills com suporte do Gateway acionadas a partir do onboarding ou das configurações de Skills usam o caminho de solicitação `skills.install` separado.

Observações:

  * `search [query...]` aceita uma consulta opcional; omita-a para navegar pelo feed de busca padrão do ClawHub.
  * `search --limit <n>` limita os resultados retornados.
  * `install --force` sobrescreve uma pasta de Skills existente no workspace para o mesmo slug.
  * `--agent <id>` direciona para um workspace de agente configurado e substitui a inferência do diretório de trabalho atual.
  * `update --all` atualiza somente instalações rastreadas do ClawHub no workspace ativo.
  * `check --agent <id>` verifica o workspace do agente selecionado e informa quais Skills prontas estão realmente visíveis no prompt ou na superfície de comandos desse agente.
  * `list` é a ação padrão quando nenhum subcomando é fornecido.
  * `list`, `info` e `check` gravam sua saída renderizada em stdout. Com `--json`, isso significa que a carga útil legível por máquina permanece em stdout para pipes e scripts.


## Relacionado

  * [Referência da CLI](</pt-BR/cli>)
  * [Skills](</pt-BR/tools/skills>)


Was this useful?YesNo