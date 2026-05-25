---
title: Migrando do Claude
source_url: https://docs.openclaw.ai/pt-BR/install/migrating-claude
scraped_at: 2026-05-25
---

O OpenClaw importa o estado local do Claude por meio do provedor de migração Claude incluído. O provedor pré-visualiza todos os itens antes de alterar o estado, redige segredos em planos e relatórios, e cria um backup verificado antes de aplicar.

## Duas formas de importar

### Onboarding wizard

O assistente oferece Claude quando detecta estado local do Claude.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

Ou aponte para uma origem específica:

bashCopy code
[code]
    openclaw onboard --import-from claude --import-source ~/.claude
[/code]

### CLI

Use `openclaw migrate` para execuções com script ou repetíveis. Consulte [`openclaw migrate`](</pt-BR/cli/migrate>) para a referência completa.

bashCopy code
[code]
    openclaw migrate claude --dry-runopenclaw migrate apply claude --yes
[/code]

Adicione `--from <path>` para importar um diretório home ou raiz de projeto específico do Claude Code.

## O que é importado

Instructions and memory

  * O conteúdo de `CLAUDE.md` e `.claude/CLAUDE.md` do projeto é copiado ou anexado ao `AGENTS.md` do workspace do agente OpenClaw.
  * O conteúdo de `~/.claude/CLAUDE.md` do usuário é anexado ao `USER.md` do workspace.

MCP servers

As definições de servidores MCP são importadas de `.mcp.json` do projeto, `~/.claude.json` do Claude Code e `claude_desktop_config.json` do Claude Desktop quando presentes.

Skills and commands

  * Skills do Claude com um arquivo `SKILL.md` são copiadas para o diretório de Skills do workspace do OpenClaw.
  * Arquivos Markdown de comandos do Claude em `.claude/commands/` ou `~/.claude/commands/` são convertidos em Skills do OpenClaw com `disable-model-invocation: true`.


## O que permanece apenas no arquivo

O provedor copia estes itens para o relatório de migração para revisão manual, mas **não** os carrega na configuração ativa do OpenClaw:

  * Hooks do Claude
  * Permissões do Claude e listas amplas de permissão de ferramentas
  * Padrões de ambiente do Claude
  * `CLAUDE.local.md`
  * `.claude/rules/`
  * Subagentes do Claude em `.claude/agents/` ou `~/.claude/agents/`
  * Caches, planos e diretórios de histórico de projetos do Claude Code
  * Extensões do Claude Desktop e credenciais armazenadas pelo SO


O OpenClaw se recusa a executar hooks, confiar em listas de permissão ou decodificar automaticamente estado opaco de credenciais OAuth e Desktop. Mova manualmente o que você precisar depois de revisar o arquivo.

## Seleção de origem

Sem `--from`, o OpenClaw inspeciona o diretório home padrão do Claude Code em `~/.claude`, o arquivo de estado amostrado `~/.claude.json` do Claude Code e a configuração MCP do Claude Desktop no macOS.

Quando `--from` aponta para uma raiz de projeto, o OpenClaw importa apenas os arquivos Claude desse projeto, como `CLAUDE.md`, `.claude/settings.json`, `.claude/commands/`, `.claude/skills/` e `.mcp.json`. Ele não lê seu diretório home global do Claude durante uma importação de raiz de projeto.

## Fluxo recomendado

* ### Preview the plan

bashCopy code
[code]
    openclaw migrate claude --dry-run
[/code]

O plano lista tudo que será alterado, incluindo conflitos, itens ignorados e valores sensíveis redigidos de campos MCP `env` ou `headers` aninhados.

* ### Apply with backup

bashCopy code
[code]
    openclaw migrate apply claude --yes
[/code]

O OpenClaw cria e verifica um backup antes de aplicar.

* ### Run doctor

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</pt-BR/gateway/doctor>) verifica problemas de configuração ou estado após a importação.

* ### Restart and verify

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

Confirme se o Gateway está saudável e se suas instruções, servidores MCP e Skills importados foram carregados.

## Tratamento de conflitos

A aplicação se recusa a continuar quando o plano relata conflitos (um arquivo ou valor de configuração já existe no destino).

Para uma instalação nova do OpenClaw, conflitos são incomuns. Eles normalmente aparecem quando você executa novamente a importação em uma configuração que já tem edições do usuário.

## Saída JSON para automação

bashCopy code
[code]
    openclaw migrate claude --dry-run --jsonopenclaw migrate apply claude --json --yes
[/code]

Com `--json` e sem `--yes`, a aplicação imprime o plano e não altera o estado. Esse é o modo mais seguro para CI e scripts compartilhados.

## Solução de problemas

Claude state lives outside ~/.claude

Passe `--from /actual/path` (CLI) ou `--import-source /actual/path` (integração).

Onboarding refuses to import on an existing setup

Importações de integração exigem uma configuração nova. Redefina o estado e refaça a integração, ou use `openclaw migrate apply claude` diretamente, que oferece suporte a `--overwrite` e controle explícito de backup.

MCP servers from Claude Desktop did not import

O Claude Desktop lê `claude_desktop_config.json` de um caminho específico da plataforma. Aponte `--from` para o diretório desse arquivo se o OpenClaw não o detectou automaticamente.

Claude commands became skills with model invocation disabled

Por design. Comandos do Claude são acionados pelo usuário, então o OpenClaw os importa como Skills com `disable-model-invocation: true`. Edite o frontmatter de cada Skill se quiser que o agente as invoque automaticamente.

## Relacionados

  * [`openclaw migrate`](</pt-BR/cli/migrate>): referência completa da CLI, contrato de Plugin e formatos JSON.
  * [Guia de migração](</pt-BR/install/migrating>): todos os caminhos de migração.
  * [Migrando do Hermes](</pt-BR/install/migrating-hermes>): o outro caminho de importação entre sistemas.
  * [Integração](</pt-BR/cli/onboard>): fluxo do assistente e flags não interativas.
  * [Doctor](</pt-BR/gateway/doctor>): verificação de integridade pós-migração.
  * [Workspace do agente](</pt-BR/concepts/agent-workspace>): onde ficam `AGENTS.md`, `USER.md` e Skills.


Was this useful?YesNo