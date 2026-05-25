---
title: Ganchos
source_url: https://docs.openclaw.ai/pt-BR/cli/hooks
scraped_at: 2026-05-25
---

# `openclaw hooks`

Gerencie ganchos de agente (automações orientadas a eventos para comandos como `/new`, `/reset` e inicialização do Gateway).

Executar `openclaw hooks` sem subcomando é equivalente a `openclaw hooks list`.

Relacionado:

  * Ganchos: [Ganchos](</pt-BR/automation/hooks>)
  * Ganchos de Plugin: [Ganchos de Plugin](</pt-BR/plugins/hooks>)


## Listar todos os ganchos

bashCopy code
[code]
    openclaw hooks list
[/code]

Liste todos os ganchos descobertos nos diretórios de workspace, gerenciados, extras e incluídos. A inicialização do Gateway não carrega manipuladores internos de ganchos até que pelo menos um gancho interno esteja configurado.

**Opções:**

  * `--eligible`: Mostra apenas ganchos elegíveis (requisitos atendidos)
  * `--json`: Gera saída como JSON
  * `-v, --verbose`: Mostra informações detalhadas, incluindo requisitos ausentes


**Exemplo de saída:**

CodeCopy code
[code]
    Hooks (4/4 ready) Ready:  🚀 boot-md ✓ - Run BOOT.md on gateway startup  📎 bootstrap-extra-files ✓ - Inject extra workspace bootstrap files during agent bootstrap  📝 command-logger ✓ - Log all command events to a centralized audit file  💾 session-memory ✓ - Save session context to memory when /new or /reset command is issued
[/code]

**Exemplo (detalhado):**

bashCopy code
[code]
    openclaw hooks list --verbose
[/code]

Mostra requisitos ausentes para ganchos inelegíveis.

**Exemplo (JSON):**

bashCopy code
[code]
    openclaw hooks list --json
[/code]

Retorna JSON estruturado para uso programático.

## Obter informações do gancho

bashCopy code
[code]
    openclaw hooks info <name>
[/code]

Mostra informações detalhadas sobre um gancho específico.

**Argumentos:**

  * `<name>`: Nome do gancho ou chave do gancho (por exemplo, `session-memory`)


**Opções:**

  * `--json`: Gera saída como JSON


**Exemplo:**

bashCopy code
[code]
    openclaw hooks info session-memory
[/code]

**Saída:**

CodeCopy code
[code]
    💾 session-memory ✓ Ready Save session context to memory when /new or /reset command is issued Details:  Source: openclaw-bundled  Path: /path/to/openclaw/hooks/bundled/session-memory/HOOK.md  Handler: /path/to/openclaw/hooks/bundled/session-memory/handler.ts  Homepage: https://docs.openclaw.ai/automation/hooks#session-memory  Events: command:new, command:reset Requirements:  Config: ✓ workspace.dir
[/code]

## Verificar elegibilidade dos ganchos

bashCopy code
[code]
    openclaw hooks check
[/code]

Mostra um resumo do status de elegibilidade dos ganchos (quantos estão prontos em comparação aos não prontos).

**Opções:**

  * `--json`: Gera saída como JSON


**Exemplo de saída:**

CodeCopy code
[code]
    Hooks Status Total hooks: 4Ready: 4Not ready: 0
[/code]

## Habilitar um gancho

bashCopy code
[code]
    openclaw hooks enable <name>
[/code]

Habilita um gancho específico adicionando-o à sua configuração (`~/.openclaw/openclaw.json` por padrão).

**Observação:** Ganchos de workspace ficam desabilitados por padrão até serem habilitados aqui ou na configuração. Ganchos gerenciados por plugins mostram `plugin:<id>` em `openclaw hooks list` e não podem ser habilitados/desabilitados aqui. Em vez disso, habilite/desabilite o plugin.

**Argumentos:**

  * `<name>`: Nome do gancho (por exemplo, `session-memory`)


**Exemplo:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Saída:**

CodeCopy code
[code]
    ✓ Enabled hook: 💾 session-memory
[/code]

**O que ele faz:**

  * Verifica se o gancho existe e é elegível
  * Atualiza `hooks.internal.entries.<name>.enabled = true` na sua configuração
  * Salva a configuração no disco


Se o gancho veio de `<workspace>/hooks/`, esta etapa de adesão é obrigatória antes que o Gateway o carregue.

**Depois de habilitar:**

  * Reinicie o gateway para que os ganchos sejam recarregados (reinício do app da barra de menus no macOS ou reinicie seu processo do gateway em desenvolvimento).


## Desabilitar um gancho

bashCopy code
[code]
    openclaw hooks disable <name>
[/code]

Desabilita um gancho específico atualizando sua configuração.

**Argumentos:**

  * `<name>`: Nome do gancho (por exemplo, `command-logger`)


**Exemplo:**

bashCopy code
[code]
    openclaw hooks disable command-logger
[/code]

**Saída:**

CodeCopy code
[code]
    ⏸ Disabled hook: 📝 command-logger
[/code]

**Depois de desabilitar:**

  * Reinicie o gateway para que os ganchos sejam recarregados


## Observações

  * `openclaw hooks list --json`, `info --json` e `check --json` gravam JSON estruturado diretamente em stdout.
  * Ganchos gerenciados por Plugin não podem ser habilitados nem desabilitados aqui; em vez disso, habilite ou desabilite o Plugin proprietário.


## Instalar pacotes de ganchos

bashCopy code
[code]
    openclaw plugins install <package>        # npm by defaultopenclaw plugins install npm:<package>    # npm onlyopenclaw plugins install <package> --pin  # pin versionopenclaw plugins install <path>           # local path
[/code]

Instale pacotes de ganchos pelo instalador unificado de plugins.

`openclaw hooks install` ainda funciona como um alias de compatibilidade, mas imprime um aviso de descontinuação e encaminha para `openclaw plugins install`.

Especificações npm são **somente de registro** (nome do pacote + **versão exata** opcional ou **dist-tag**). Especificações Git/URL/arquivo e intervalos semver são rejeitados. Instalações de dependências são executadas localmente no projeto com `--ignore-scripts` por segurança, mesmo quando seu shell tem configurações globais de instalação do npm.

Especificações simples e `@latest` permanecem na trilha estável. Se o npm resolver qualquer uma delas para uma pré-versão, o OpenClaw interrompe e pede que você aceite explicitamente com uma tag de pré-versão, como `@beta`/`@rc`, ou uma versão exata de pré-versão.

**O que ele faz:**

  * Copia o pacote de ganchos para `~/.openclaw/hooks/<id>`
  * Habilita os ganchos instalados em `hooks.internal.entries.*`
  * Registra a instalação em `hooks.internal.installs`


**Opções:**

  * `-l, --link`: Vincula um diretório local em vez de copiar (adiciona-o a `hooks.internal.load.extraDirs`)
  * `--pin`: Registra instalações npm como `name@version` resolvido exato em `hooks.internal.installs`


**Arquivos compactados compatíveis:** `.zip`, `.tgz`, `.tar.gz`, `.tar`

**Exemplos:**

bashCopy code
[code]
    # Local directoryopenclaw plugins install ./my-hook-pack # Local archiveopenclaw plugins install ./my-hook-pack.zip # NPM packageopenclaw plugins install @openclaw/my-hook-pack # Link a local directory without copyingopenclaw plugins install -l ./my-hook-pack
[/code]

Pacotes de ganchos vinculados são tratados como ganchos gerenciados de um diretório configurado pelo operador, não como ganchos de workspace.

## Atualizar pacotes de ganchos

bashCopy code
[code]
    openclaw plugins update <id>openclaw plugins update --all
[/code]

Atualize pacotes de ganchos baseados em npm rastreados pelo atualizador unificado de plugins.

`openclaw hooks update` ainda funciona como um alias de compatibilidade, mas imprime um aviso de descontinuação e encaminha para `openclaw plugins update`.

**Opções:**

  * `--all`: Atualiza todos os pacotes de ganchos rastreados
  * `--dry-run`: Mostra o que mudaria sem gravar


Quando um hash de integridade armazenado existe e o hash do artefato obtido muda, o OpenClaw imprime um aviso e pede confirmação antes de prosseguir. Use `--yes` global para ignorar prompts em execuções de CI/não interativas.

## Ganchos incluídos

### session-memory

Salva o contexto da sessão na memória quando você emite `/new` ou `/reset`.

**Habilitar:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Saída:** `~/.openclaw/workspace/memory/YYYY-MM-DD-HHMM.md` por padrão. Defina `hooks.internal.entries.session-memory.llmSlug: true` para slugs de nome de arquivo gerados pelo modelo.

**Veja:** [documentação de session-memory](</pt-BR/automation/hooks#session-memory>)

### bootstrap-extra-files

Injeta arquivos de bootstrap adicionais (por exemplo, `AGENTS.md` / `TOOLS.md` locais ao monorepo) durante `agent:bootstrap`.

**Habilitar:**

bashCopy code
[code]
    openclaw hooks enable bootstrap-extra-files
[/code]

**Veja:** [documentação de bootstrap-extra-files](</pt-BR/automation/hooks#bootstrap-extra-files>)

### command-logger

Registra todos os eventos de comando em um arquivo de auditoria centralizado.

**Habilitar:**

bashCopy code
[code]
    openclaw hooks enable command-logger
[/code]

**Saída:** `~/.openclaw/logs/commands.log`

**Ver logs:**

bashCopy code
[code]
    # Recent commandstail -n 20 ~/.openclaw/logs/commands.log # Pretty-printcat ~/.openclaw/logs/commands.log | jq . # Filter by actiongrep '"action":"new"' ~/.openclaw/logs/commands.log | jq .
[/code]

**Veja:** [documentação de command-logger](</pt-BR/automation/hooks#command-logger>)

### boot-md

Executa `BOOT.md` quando o gateway inicia (após os canais iniciarem).

**Eventos** : `gateway:startup`

**Habilitar** :

bashCopy code
[code]
    openclaw hooks enable boot-md
[/code]

**Veja:** [documentação de boot-md](</pt-BR/automation/hooks#boot-md>)

## Relacionado

  * [Referência da CLI](</pt-BR/cli>)
  * [Ganchos de automação](</pt-BR/automation/hooks>)


Was this useful?YesNo