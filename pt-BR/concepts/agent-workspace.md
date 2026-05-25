---
title: Espaço de trabalho do agente
source_url: https://docs.openclaw.ai/pt-BR/concepts/agent-workspace
scraped_at: 2026-05-25
---

O workspace é a casa do agente. Ele é o único diretório de trabalho usado para ferramentas de arquivo e para o contexto do workspace. Mantenha-o privado e trate-o como memória.

Isso é separado de `~/.openclaw/`, que armazena configuração, credenciais e sessões.

## Local padrão

  * Padrão: `~/.openclaw/workspace`
  * Se `OPENCLAW_PROFILE` estiver definido e não for `"default"`, o padrão passa a ser `~/.openclaw/workspace-<profile>`.
  * Substitua em `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/.openclaw/workspace",    },  },}
[/code]

`openclaw onboard`, `openclaw configure` ou `openclaw setup` criarão o workspace e semearão os arquivos de bootstrap se eles estiverem ausentes.

Se você já gerencia os arquivos do workspace por conta própria, pode desativar a criação de arquivos de bootstrap:

json5Copy code
[code]
    { agents: { defaults: { skipBootstrap: true } } }
[/code]

## Pastas extras de workspace

Instalações mais antigas podem ter criado `~/openclaw`. Manter vários diretórios de workspace pode causar confusão de autenticação ou desvio de estado, porque apenas um workspace fica ativo por vez.

## Mapa de arquivos do workspace

Estes são os arquivos padrão que o OpenClaw espera dentro do workspace:

AGENTS.md - instruções operacionais

Instruções operacionais para o agente e como ele deve usar a memória. Carregadas no início de cada sessão. Bom lugar para regras, prioridades e detalhes de "como se comportar".

SOUL.md - persona e tom

Persona, tom e limites. Carregado em todas as sessões. Guia: [guia de personalidade SOUL.md](</pt-BR/concepts/soul>).

USER.md - quem é o usuário

Quem é o usuário e como se dirigir a ele. Carregado em todas as sessões.

IDENTITY.md - nome, vibe, emoji

O nome, a vibe e o emoji do agente. Criado/atualizado durante o ritual de bootstrap.

TOOLS.md - convenções de ferramentas locais

Observações sobre suas ferramentas locais e convenções. Não controla a disponibilidade de ferramentas; é apenas orientação.

HEARTBEAT.md - checklist de Heartbeat

Pequeno checklist opcional para execuções de Heartbeat. Mantenha-o curto para evitar gasto de tokens.

BOOT.md - checklist de inicialização

Checklist opcional de inicialização executado automaticamente no reinício do Gateway (quando [hooks internos](</pt-BR/automation/hooks>) estão ativados). Mantenha-o curto; use a ferramenta de mensagens para envios de saída.

BOOTSTRAP.md - ritual de primeira execução

Ritual único de primeira execução. Criado apenas para um workspace totalmente novo. Exclua-o depois que o ritual for concluído.

memory/YYYY-MM-DD.md - registro diário de memória

Registro diário de memória (um arquivo por dia). Recomendado ler hoje + ontem no início da sessão.

MEMORY.md - memória de longo prazo curada (opcional)

Memória de longo prazo curada: fatos duráveis, preferências, decisões e resumos curtos. Mantenha registros detalhados em `memory/YYYY-MM-DD.md` para que as ferramentas de memória possam recuperá-los sob demanda sem injetá-los em cada prompt. Carregue `MEMORY.md` apenas na sessão principal e privada (não em contextos compartilhados/de grupo). Consulte [Memória](</pt-BR/concepts/memory>) para o fluxo de trabalho e a descarga automática de memória.

skills/ - skills do workspace (opcional)

Skills específicas do workspace. Local de Skill com maior precedência para esse workspace. Substitui skills de agente do projeto, skills de agente pessoais, skills gerenciadas, skills incluídas e `skills.load.extraDirs` quando há colisão de nomes.

canvas/ - arquivos de UI do Canvas (opcional)

Arquivos de UI do Canvas para exibições de nós (por exemplo, `canvas/index.html`).

## O que NÃO fica no workspace

Estes ficam em `~/.openclaw/` e NÃO devem ser commitados no repositório do workspace:

  * `~/.openclaw/openclaw.json` (configuração)
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` (perfis de autenticação do modelo: OAuth + chaves de API)
  * `~/.openclaw/agents/<agentId>/agent/codex-home/` (conta de runtime Codex por agente, configuração, skills, plugins e estado nativo de threads)
  * `~/.openclaw/credentials/` (estado de canal/provedor mais dados legados de importação OAuth)
  * `~/.openclaw/agents/<agentId>/sessions/` (transcrições de sessão + metadados)
  * `~/.openclaw/skills/` (skills gerenciadas)


Se você precisar migrar sessões ou configuração, copie-as separadamente e mantenha-as fora do controle de versão.

## Backup em Git (recomendado, privado)

Trate o workspace como memória privada. Coloque-o em um repositório git **privado** para que ele tenha backup e possa ser recuperado.

Execute estas etapas na máquina onde o Gateway roda (é onde o workspace fica).

* ### Inicialize o repositório

Se o git estiver instalado, workspaces totalmente novos serão inicializados automaticamente. Se este workspace ainda não for um repositório, execute:

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.md SOUL.md TOOLS.md IDENTITY.md USER.md HEARTBEAT.md memory/git commit -m "Add agent workspace"
[/code]

* ### Adicione um remote privado

### UI web do GitHub

  1. Crie um novo repositório **privado** no GitHub.
  2. Não inicialize com um README (evita conflitos de merge).
  3. Copie a URL remota HTTPS.
  4. Adicione o remote e faça push:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

### GitHub CLI (gh)

bashCopy code
[code]
    gh auth logingh repo create openclaw-workspace --private --source . --remote origin --push
[/code]

### UI web do GitLab

  1. Crie um novo repositório **privado** no GitLab.
  2. Não inicialize com um README (evita conflitos de merge).
  3. Copie a URL remota HTTPS.
  4. Adicione o remote e faça push:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

* ### Atualizações contínuas

bashCopy code
[code]
    git statusgit add .git commit -m "Update memory"git push
[/code]

## Não commite segredos

Modelo inicial sugerido de `.gitignore`:

gitignoreCopy code
[code]
    .DS_Store.env**/*.key**/*.pem**/secrets*
[/code]

## Movendo o workspace para uma nova máquina

* ### Clone o repositório

Clone o repositório para o caminho desejado (padrão `~/.openclaw/workspace`).

* ### Atualize a configuração

Defina `agents.defaults.workspace` para esse caminho em `~/.openclaw/openclaw.json`.

* ### Semeie arquivos ausentes

Execute `openclaw setup --workspace <path>` para semear quaisquer arquivos ausentes.

* ### Copie sessões (opcional)

Se você precisar das sessões, copie `~/.openclaw/agents/<agentId>/sessions/` da máquina antiga separadamente.

## Observações avançadas

  * O roteamento multiagente pode usar workspaces diferentes por agente. Consulte [Roteamento de canais](</pt-BR/channels/channel-routing>) para a configuração de roteamento.
  * Se `agents.defaults.sandbox` estiver ativado, sessões não principais podem usar workspaces de sandbox por sessão em `agents.defaults.sandbox.workspaceRoot`.


## Relacionados

  * [Heartbeat](</pt-BR/gateway/heartbeat>) \- arquivo de workspace [HEARTBEAT.md](<http://HEARTBEAT.md>)
  * [Sandboxing](</pt-BR/gateway/sandboxing>) \- acesso ao workspace em ambientes com sandbox
  * [Sessão](</pt-BR/concepts/session>) \- caminhos de armazenamento de sessão
  * [Ordens permanentes](</pt-BR/automation/standing-orders>) \- instruções persistentes em arquivos do workspace


Was this useful?YesNo