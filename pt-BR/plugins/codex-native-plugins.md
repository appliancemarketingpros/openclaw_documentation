---
title: Plugins nativos do Codex
source_url: https://docs.openclaw.ai/pt-BR/plugins/codex-native-plugins
scraped_at: 2026-05-25
---

O suporte nativo a plugins do Codex permite que um agente OpenClaw no modo Codex use os recursos próprios de app e plugin do app-server do Codex dentro da mesma thread do Codex que lida com o turno do OpenClaw.

O OpenClaw não traduz plugins do Codex em ferramentas dinâmicas sintéticas `codex_plugin_*` do OpenClaw. As chamadas de plugin permanecem na transcrição nativa do Codex, e o app-server do Codex é responsável pela execução MCP apoiada por app.

Use esta página depois que o [harness do Codex](</pt-BR/plugins/codex-harness>) base estiver funcionando.

## Requisitos

  * O runtime do agente OpenClaw selecionado deve ser o harness nativo do Codex.
  * `plugins.entries.codex.enabled` deve ser true.
  * `plugins.entries.codex.config.codexPlugins.enabled` deve ser true.
  * A V1 oferece suporte apenas a plugins `openai-curated` que a migração observou como instalados a partir da origem no diretório home do Codex de origem.
  * O app-server do Codex de destino deve conseguir ver o marketplace, o plugin e o inventário de apps esperados.


`codexPlugins` não tem efeito em execuções PI, execuções normais do provedor OpenAI, associações de conversa ACP ou outros harnesses, porque esses caminhos não criam threads do app-server do Codex com configuração nativa de `apps`.

## Início rápido

Pré-visualize a migração a partir do diretório home do Codex de origem:

bashCopy code
[code]
    openclaw migrate codex --dry-run
[/code]

Use a verificação estrita de apps de origem quando quiser que a migração verifique a acessibilidade dos apps de origem antes de planejar a ativação nativa de plugins:

bashCopy code
[code]
    openclaw migrate codex --dry-run --verify-plugin-apps
[/code]

Aplique a migração quando o plano parecer correto:

bashCopy code
[code]
    openclaw migrate apply codex --yes
[/code]

A migração grava entradas `codexPlugins` explícitas para plugins elegíveis e chama `plugin/install` do app-server do Codex para os plugins selecionados. Uma configuração migrada típica se parece com isto:

json5Copy code
[code]
    {  plugins: {    entries: {      codex: {        enabled: true,        config: {          codexPlugins: {            enabled: true,            allow_destructive_actions: true,            plugins: {              "google-calendar": {                enabled: true,                marketplaceName: "openai-curated",                pluginName: "google-calendar",              },            },          },        },      },    },  },}
[/code]

Depois de alterar `codexPlugins`, use `/new`, `/reset` ou reinicie o Gateway para que futuras sessões do harness do Codex sejam iniciadas com o conjunto de apps atualizado.

## Como a configuração nativa de plugins funciona

A integração tem três estados separados:

  * Instalado: o Codex tem o pacote local do plugin no runtime do app-server de destino.
  * Habilitado: a configuração do OpenClaw permite disponibilizar o plugin para turnos do harness do Codex.
  * Acessível: o app-server do Codex confirma que as entradas de app do plugin estão disponíveis para a conta ativa e podem ser mapeadas para a identidade de plugin migrada.


A migração é a etapa durável de instalação/elegibilidade. Durante o planejamento, o OpenClaw lê os detalhes de `plugin/read` do Codex de origem e verifica se a resposta da conta do app-server do Codex de origem é uma conta com assinatura do ChatGPT. Respostas de conta que não sejam do ChatGPT ou ausentes ignoram plugins apoiados por app com `codex_subscription_required`. Por padrão, a migração não chama `app/list` de origem; plugins de origem apoiados por app que passam pelo gate de conta são planejados sem verificação de acessibilidade dos apps de origem, e falhas de transporte na consulta da conta são ignoradas com `codex_account_unavailable`. Com `--verify-plugin-apps`, a migração obtém um snapshot novo de `app/list` de origem e exige que todos os apps pertencentes estejam presentes, habilitados e acessíveis antes de planejar a ativação nativa. Nesse modo, falhas de transporte na consulta da conta avançam para o gate de inventário de apps de origem. O inventário de apps em runtime é a verificação de acessibilidade da sessão de destino após a migração. Em seguida, a configuração de sessão do harness do Codex calcula uma configuração restritiva de apps da thread para os apps de plugins habilitados e acessíveis.

A configuração de apps da thread é calculada quando o OpenClaw estabelece uma sessão do harness do Codex ou substitui uma associação obsoleta de thread do Codex. Ela não é recalculada a cada turno.

## Limite de suporte da V1

A V1 é intencionalmente restrita:

  * Apenas plugins `openai-curated` que já estavam instalados no inventário do app-server do Codex de origem são elegíveis para migração.
  * Plugins de origem apoiados por app devem passar pelo gate de assinatura no momento da migração. `--verify-plugin-apps` adiciona o gate de inventário de apps de origem. Contas barradas por assinatura e, no modo de verificação, apps de origem inacessíveis, desabilitados, ausentes ou falhas de atualização do inventário de apps de origem são relatados como itens manuais ignorados em vez de entradas de configuração habilitadas. Detalhes de plugin ilegíveis são ignorados antes do gate de inventário de apps de origem.
  * A migração grava identidades de plugin explícitas com `marketplaceName` e `pluginName`; ela não grava caminhos de cache locais `marketplacePath`.
  * `codexPlugins.enabled` é a chave global de habilitação.
  * Não há wildcard `plugins["*"]` nem chave de configuração que conceda autoridade de instalação arbitrária.
  * Marketplaces sem suporte, pacotes de plugin em cache, hooks e arquivos de configuração do Codex são preservados no relatório de migração para revisão manual.


## Inventário e propriedade de apps

O OpenClaw lê o inventário de apps do Codex por meio de `app/list` do app-server, armazena-o em cache por uma hora e atualiza entradas obsoletas ou ausentes de forma assíncrona. O cache fica apenas em memória; reiniciar a CLI ou o Gateway o descarta, e o OpenClaw o reconstrói a partir da próxima leitura de `app/list`.

Migração e runtime usam chaves de cache separadas:

  * A verificação da migração de origem usa o diretório home do Codex de origem e as opções de inicialização do app-server de origem. Isso é executado apenas quando `--verify-plugin-apps` está definido, e força uma nova travessia de `app/list` de origem para essa execução de planejamento.
  * A configuração de runtime de destino usa a identidade do app-server do Codex do agente de destino quando constrói a configuração de apps da thread do Codex. A ativação de plugin invalida essa chave de cache de destino e, em seguida, força sua atualização após `plugin/install`.


Um app de plugin é exposto apenas quando o OpenClaw consegue mapeá-lo de volta para o plugin migrado por meio de propriedade estável:

  * id exato do app a partir dos detalhes do plugin
  * nome conhecido do servidor MCP
  * metadados estáveis únicos


Propriedade apenas por nome de exibição ou ambígua é excluída até que a próxima atualização de inventário comprove a propriedade.

## Configuração de apps da thread

O OpenClaw injeta um patch restritivo de `config.apps` para a thread do Codex: `_default` é desabilitado e apenas apps pertencentes a plugins migrados habilitados são habilitados.

O OpenClaw define `destructive_enabled` em nível de app a partir da política efetiva global ou por plugin `allow_destructive_actions` e permite que o Codex aplique os metadados de ferramentas destrutivas a partir das anotações nativas de ferramentas de app. A configuração do app `_default` é desabilitada com `open_world_enabled: false`. Apps de plugin habilitados são emitidos com `open_world_enabled: true`; o OpenClaw não expõe um controle separado de política open-world de plugin e não mantém listas de negação de nomes de ferramentas destrutivas por plugin.

O modo de aprovação de ferramentas é automático por padrão para apps de plugin, para que ferramentas de leitura não destrutivas possam ser executadas sem uma interface de aprovação na mesma thread. Ferramentas destrutivas permanecem controladas pela política `destructive_enabled` de cada app.

## Política de ação destrutiva

Solicitações destrutivas de plugins são permitidas por padrão para plugins do Codex migrados, enquanto schemas inseguros e propriedade ambígua ainda falham fechados:

  * `allow_destructive_actions` global usa `true` como padrão.
  * `allow_destructive_actions` por plugin substitui a política global para esse plugin.
  * Quando a política é `false`, o OpenClaw retorna uma recusa determinística.
  * Quando a política é `true`, o OpenClaw aceita automaticamente apenas schemas seguros que consegue mapear para uma resposta de aprovação, como um campo booleano de aprovação.
  * Identidade de plugin ausente, propriedade ambígua, id de turno ausente, id de turno incorreto ou schema de solicitação inseguro recusam em vez de solicitar confirmação.


## Solução de problemas

**`auth_required`:** a migração instalou o plugin, mas um de seus apps ainda precisa de autenticação. A entrada explícita do plugin é gravada desabilitada até que você reautorize e habilite-a.

**`app_inaccessible`, `app_disabled` ou `app_missing`:** a migração não instalou o plugin porque o inventário de apps do Codex de origem não mostrou todos os apps pertencentes como presentes, habilitados e acessíveis enquanto `--verify-plugin-apps` estava definido. Reautorize ou habilite o app no Codex e execute a migração novamente com `--verify-plugin-apps`.

**`app_inventory_unavailable`:** a migração não instalou o plugin porque a verificação estrita de apps de origem foi solicitada e a atualização do inventário de apps do Codex de origem falhou. Corrija o acesso ao app-server do Codex de origem ou tente novamente sem `--verify-plugin-apps` se aceitar o plano mais rápido baseado no gate de conta.

**`codex_subscription_required`:** a migração não instalou o plugin apoiado por app porque a conta do app-server do Codex de origem não estava conectada com uma conta de assinatura do ChatGPT. Entre no app Codex com autenticação de assinatura e execute a migração novamente.

**`codex_account_unavailable`:** a migração não instalou o plugin apoiado por app porque a conta do app-server do Codex de origem não pôde ser lida. Corrija a autenticação do app-server do Codex de origem ou execute novamente com `--verify-plugin-apps` se quiser que o inventário de apps de origem decida a elegibilidade quando a consulta da conta falhar.

**`marketplace_missing` ou `plugin_missing`:** o app-server do Codex de destino não consegue ver o marketplace ou plugin `openai-curated` esperado. Execute a migração novamente contra o runtime de destino ou inspecione o status de plugins do app-server do Codex.

**`app_inventory_missing` ou `app_inventory_stale`:** a prontidão do app veio de um cache vazio ou obsoleto. O OpenClaw agenda uma atualização assíncrona e exclui apps de plugin até que a propriedade e a prontidão sejam conhecidas.

**`app_ownership_ambiguous`:** o inventário de apps só correspondeu pelo nome de exibição, então o app não é exposto à thread do Codex.

**A configuração mudou, mas o agente não consegue ver o plugin:** use `/new`, `/reset` ou reinicie o Gateway. Associações existentes de thread do Codex mantêm a configuração de apps com que foram iniciadas até que o OpenClaw estabeleça uma nova sessão de harness ou substitua uma associação obsoleta.

**A ação destrutiva é recusada:** verifique os valores globais e por plugin de `allow_destructive_actions`. Mesmo quando a política é true, schemas de solicitação inseguros e identidade de plugin ambígua ainda falham fechados.

## Relacionados

  * [harness do Codex](</pt-BR/plugins/codex-harness>)
  * [referência do harness do Codex](</pt-BR/plugins/codex-harness-reference>)
  * [runtime do harness do Codex](</pt-BR/plugins/codex-harness-runtime>)
  * [Referência de configuração](</pt-BR/gateway/configuration-reference#codex-harness-plugin-config>)
  * [CLI de migração](</pt-BR/cli/migrate>)


Was this useful?YesNo