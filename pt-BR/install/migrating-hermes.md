---
title: Migrando do Hermes
source_url: https://docs.openclaw.ai/pt-BR/install/migrating-hermes
scraped_at: 2026-05-25
---

OpenClaw importa o estado do Hermes por meio de um provedor de migração incluído. O provedor pré-visualiza tudo antes de alterar o estado, oculta segredos em planos e relatórios e cria um backup verificado antes da aplicação.

## Duas formas de importar

### Assistente de onboarding

O caminho mais rápido. O assistente detecta o Hermes em `~/.hermes` e mostra uma pré-visualização antes de aplicar.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

Ou aponte para uma origem específica:

bashCopy code
[code]
    openclaw onboard --import-from hermes --import-source ~/.hermes
[/code]

### CLI

Use `openclaw migrate` para execuções por script ou repetíveis. Consulte [`openclaw migrate`](</pt-BR/cli/migrate>) para a referência completa.

bashCopy code
[code]
    openclaw migrate hermes --dry-run    # somente pré-visualizaçãoopenclaw migrate apply hermes --yes  # aplica ignorando a confirmação
[/code]

Adicione `--from <path>` quando o Hermes estiver fora de `~/.hermes`.

## O que é importado

Configuração de modelo

  * Seleção de modelo padrão a partir de `config.yaml` do Hermes.
  * Provedores de modelo configurados e endpoints personalizados compatíveis com OpenAI a partir de `providers` e `custom_providers`.

Servidores MCP

Definições de servidores MCP de `mcp_servers` ou `mcp.servers`.

Arquivos do workspace

  * `SOUL.md` e `AGENTS.md` são copiados para o workspace do agente do OpenClaw.
  * `memories/MEMORY.md` e `memories/USER.md` são **anexados** aos arquivos de memória correspondentes do OpenClaw em vez de sobrescrevê-los.

Configuração de memória

Padrões de configuração de memória para a memória em arquivo do OpenClaw. Provedores de memória externos, como o Honcho, são registrados como itens de arquivo ou de revisão manual para que você possa movê-los deliberadamente.

Skills

Skills com um arquivo `SKILL.md` em `skills/<name>/` são copiadas, junto com valores de configuração por Skill de `skills.config`.

Chaves de API (opcional)

Defina `--include-secrets` para importar chaves `.env` compatíveis: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `OPENROUTER_API_KEY`, `GOOGLE_API_KEY`, `GEMINI_API_KEY`, `GROQ_API_KEY`, `XAI_API_KEY`, `MISTRAL_API_KEY`, `DEEPSEEK_API_KEY`. Sem a flag, segredos nunca são copiados.

## O que permanece somente em arquivo

O provedor copia estes itens para o diretório de relatório de migração para revisão manual, mas **não** os carrega na configuração ou nas credenciais ativas do OpenClaw:

  * `plugins/`
  * `sessions/`
  * `logs/`
  * `cron/`
  * `mcp-tokens/`
  * `auth.json`
  * `state.db`


O OpenClaw se recusa a executar ou confiar nesse estado automaticamente porque os formatos e pressupostos de confiança podem divergir entre sistemas. Mova manualmente o que você precisar depois de revisar o arquivo.

## Fluxo recomendado

* ### Pré-visualizar o plano

bashCopy code
[code]
    openclaw migrate hermes --dry-run
[/code]

O plano lista tudo que será alterado, incluindo conflitos, itens ignorados e quaisquer itens sensíveis. A saída do plano oculta chaves aninhadas que parecem conter segredos.

* ### Aplicar com backup

bashCopy code
[code]
    openclaw migrate apply hermes --yes
[/code]

O OpenClaw cria e verifica um backup antes de aplicar. Se você precisar importar chaves de API, adicione `--include-secrets`.

* ### Executar doctor

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</pt-BR/gateway/doctor>) reaplica quaisquer migrações de configuração pendentes e verifica problemas introduzidos durante a importação.

* ### Reiniciar e verificar

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

Confirme que o Gateway está saudável e que o modelo, a memória e as Skills importados foram carregados.

## Tratamento de conflitos

A aplicação se recusa a continuar quando o plano relata conflitos (um arquivo ou valor de configuração já existe no destino).

Para uma instalação nova do OpenClaw, conflitos são incomuns. Eles geralmente aparecem quando você executa novamente a importação em uma configuração que já tem edições do usuário.

Se um conflito surgir no meio da aplicação (por exemplo, uma disputa inesperada em um arquivo de configuração), o Hermes marca os itens de configuração dependentes restantes como `skipped` com o motivo `blocked by earlier apply conflict` em vez de gravá-los parcialmente. O relatório de migração registra cada item bloqueado para que você possa resolver o conflito original e executar a importação novamente.

## Segredos

Segredos nunca são importados por padrão.

  * Execute primeiro `openclaw migrate apply hermes --yes` para importar estado sem segredos.
  * Se você também quiser copiar chaves `.env` compatíveis, execute novamente com `--include-secrets`.
  * Para credenciais gerenciadas por SecretRef, configure a origem SecretRef depois que a importação for concluída.


## Saída JSON para automação

bashCopy code
[code]
    openclaw migrate hermes --dry-run --jsonopenclaw migrate apply hermes --json --yes
[/code]

Com `--json` e sem `--yes`, a aplicação imprime o plano e não altera o estado. Este é o modo mais seguro para CI e scripts compartilhados.

## Solução de problemas

A aplicação é recusada com conflitos

Inspecione a saída do plano. Cada conflito identifica o caminho de origem e o destino existente. Decida por item se deve ignorar, editar o destino ou executar novamente com `--overwrite`.

O Hermes está fora de ~/.hermes

Passe `--from /actual/path` (CLI) ou `--import-source /actual/path` (onboarding).

O onboarding se recusa a importar em uma configuração existente

Importações via onboarding exigem uma configuração nova. Redefina o estado e refaça o onboarding, ou use `openclaw migrate apply hermes` diretamente, que oferece suporte a `--overwrite` e controle explícito de backup.

As chaves de API não foram importadas

`--include-secrets` é obrigatório, e somente as chaves listadas acima são reconhecidas. Outras variáveis em `.env` são ignoradas.

## Relacionados

  * [`openclaw migrate`](</pt-BR/cli/migrate>): referência completa da CLI, contrato do Plugin e formatos JSON.
  * [Onboarding](</pt-BR/cli/onboard>): fluxo do assistente e flags não interativas.
  * [Migração](</pt-BR/install/migrating>): mova uma instalação do OpenClaw entre máquinas.
  * [Doctor](</pt-BR/gateway/doctor>): verificação de integridade pós-migração.
  * [Workspace do agente](</pt-BR/concepts/agent-workspace>): onde `SOUL.md`, `AGENTS.md` e os arquivos de memória ficam.


Was this useful?YesNo