---
title: OpenProse
source_url: https://docs.openclaw.ai/pt-BR/prose
scraped_at: 2026-05-25
---

O OpenProse é um formato portátil de workflow, orientado a Markdown, para orquestrar sessões de IA. No OpenClaw, ele é distribuído como um plugin que instala um pacote de Skills do OpenProse junto com um comando de barra `/prose`. Os programas ficam em arquivos `.prose` e podem gerar vários subagentes com controle explícito de fluxo.

Site oficial: <https://www.prose.md>

## O que ele pode fazer

  * Pesquisa + síntese com vários agentes e paralelismo explícito.
  * Workflows repetíveis e seguros para aprovação (revisão de código, triagem de incidentes, pipelines de conteúdo).
  * Programas `.prose` reutilizáveis que você pode executar em runtimes de agente compatíveis.


## Instalar + habilitar

Plugins integrados são desabilitados por padrão. Habilite o OpenProse:

bashCopy code
[code]
    openclaw plugins enable open-prose
[/code]

Reinicie o Gateway após habilitar o plugin.

Checkout local/dev: `openclaw plugins install ./path/to/local/open-prose-plugin`

Documentação relacionada: [Plugins](</pt-BR/tools/plugin>), [Manifesto de Plugin](</pt-BR/plugins/manifest>), [Skills](</pt-BR/tools/skills>).

## Comando de barra

O OpenProse registra `/prose` como um comando de Skill invocável pelo usuário. Ele faz o roteamento para as instruções da VM OpenProse e usa tools do OpenClaw internamente.

Comandos comuns:

CodeCopy code
[code]
    /prose help/prose run <file.prose>/prose run <handle/slug>/prose run <https://example.com/file.prose>/prose compile <file.prose>/prose examples/prose update
[/code]

## Exemplo: um arquivo `.prose` simples

proseCopy code
[code]
    # Pesquisa + síntese com dois agentes executando em paralelo. input topic: "What should we research?" agent researcher:  model: sonnet  prompt: "You research thoroughly and cite sources." agent writer:  model: opus  prompt: "You write a concise summary." parallel:  findings = session: researcher    prompt: "Research {topic}."  draft = session: writer    prompt: "Summarize {topic}." session "Merge the findings + draft into a final answer."context: { findings, draft }
[/code]

## Locais de arquivo

O OpenProse mantém o estado em `.prose/` no seu workspace:

CodeCopy code
[code]
    .prose/├── .env├── runs/│   └── {YYYYMMDD}-{HHMMSS}-{random}/│       ├── program.prose│       ├── state.md│       ├── bindings/│       └── agents/└── agents/
[/code]

Agentes persistentes em nível de usuário ficam em:

CodeCopy code
[code]
    ~/.prose/agents/
[/code]

## Modos de estado

O OpenProse oferece suporte a vários backends de estado:

  * **filesystem** (padrão): `.prose/runs/...`
  * **in-context** : transitório, para programas pequenos
  * **sqlite** (experimental): requer binário `sqlite3`
  * **postgres** (experimental): requer `psql` e uma string de conexão


Observações:

  * sqlite/postgres são opt-in e experimentais.
  * Credenciais de postgres fluem para logs de subagente; use um banco de dados dedicado com privilégios mínimos.


## Programas remotos

`/prose run <handle/slug>` resolve para `https://p.prose.md/<handle>/<slug>`. URLs diretas são buscadas como estão. Isso usa a tool `web_fetch` (ou `exec` para POST).

## Mapeamento de runtime do OpenClaw

Programas OpenProse são mapeados para primitivas do OpenClaw:

Conceito do OpenProse | Tool do OpenClaw  
---|---  
Gerar sessão / Task tool | `sessions_spawn`  
Leitura/gravação de arquivo | `read` / `write`  
Busca web | `web_fetch`  
  
Se sua lista de permissões de tools bloquear essas tools, programas OpenProse falharão. Consulte [Configuração de Skills](</pt-BR/tools/skills-config>).

## Segurança + aprovações

Trate arquivos `.prose` como código. Revise antes de executar. Use listas de permissões de tools e gates de aprovação do OpenClaw para controlar efeitos colaterais.

Para workflows determinísticos com gate de aprovação, compare com [Lobster](</pt-BR/tools/lobster>).

## Relacionado

  * [Texto para fala](</pt-BR/tools/tts>)
  * [Formatação Markdown](</pt-BR/concepts/markdown-formatting>)


Was this useful?YesNo