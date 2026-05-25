---
title: CLI de Modelos
source_url: https://docs.openclaw.ai/pt-BR/concepts/models
scraped_at: 2026-05-25
---

[**Failover de modelo** Rotação de perfil de autenticação, cooldowns e como isso interage com fallbacks. ](</pt-BR/concepts/model-failover>) [**Provedores de modelo** Visão geral rápida dos provedores e exemplos. ](</pt-BR/concepts/model-providers>) [**Runtimes de agente** PI, Codex e outros runtimes de loop de agente. ](</pt-BR/concepts/agent-runtimes>) [**Referência de configuração** Chaves de configuração de modelo. ](</pt-BR/gateway/config-agents#agent-defaults>)

As refs de modelo escolhem um provedor e um modelo. Elas normalmente não escolhem o runtime de agente de baixo nível. As refs de agente OpenAI são a principal exceção: `openai/gpt-5.5` é executado pelo runtime de servidor de app do Codex por padrão no provedor oficial OpenAI. Substituições explícitas de runtime pertencem à política de provedor/modelo, não ao agente ou à sessão inteira. No modo de runtime Codex, a ref `openai/gpt-*` não implica cobrança por chave de API; a autenticação pode vir de uma conta Codex ou de um perfil de autenticação `openai-codex`. Consulte [Runtimes de agente](</pt-BR/concepts/agent-runtimes>).

## Como a seleção de modelo funciona

O OpenClaw seleciona modelos nesta ordem:

* ### Modelo principal

`agents.defaults.model.primary` (ou `agents.defaults.model`).

* ### Fallbacks

`agents.defaults.model.fallbacks` (em ordem).

* ### Failover de autenticação do provedor

O failover de autenticação acontece dentro de um provedor antes de passar para o próximo modelo.

Superfícies de modelo relacionadas

  * `agents.defaults.models` é a lista de permissões/catálogo de modelos que o OpenClaw pode usar (mais aliases). Use entradas `provider/*` para limitar os provedores visíveis mantendo a descoberta de provedores dinâmica.
  * `agents.defaults.imageModel` é usado **somente quando** o modelo principal não aceita imagens.
  * `agents.defaults.pdfModel` é usado pela ferramenta `pdf`. Se omitido, a ferramenta recorre a `agents.defaults.imageModel` e depois ao modelo resolvido da sessão/padrão.
  * `agents.defaults.imageGenerationModel` é usado pela capacidade compartilhada de geração de imagens. Se omitido, `image_generate` ainda pode inferir um padrão de provedor com autenticação. Ele tenta primeiro o provedor padrão atual e depois os demais provedores registrados de geração de imagens em ordem de ID de provedor. Se você definir um provedor/modelo específico, configure também a autenticação/chave de API desse provedor.
  * `agents.defaults.musicGenerationModel` é usado pela capacidade compartilhada de geração de música. Se omitido, `music_generate` ainda pode inferir um padrão de provedor com autenticação. Ele tenta primeiro o provedor padrão atual e depois os demais provedores registrados de geração de música em ordem de ID de provedor. Se você definir um provedor/modelo específico, configure também a autenticação/chave de API desse provedor.
  * `agents.defaults.videoGenerationModel` é usado pela capacidade compartilhada de geração de vídeo. Se omitido, `video_generate` ainda pode inferir um padrão de provedor com autenticação. Ele tenta primeiro o provedor padrão atual e depois os demais provedores registrados de geração de vídeo em ordem de ID de provedor. Se você definir um provedor/modelo específico, configure também a autenticação/chave de API desse provedor.
  * Padrões por agente podem substituir `agents.defaults.model` via `agents.list[].model` mais vínculos (consulte [Roteamento multiagente](</pt-BR/concepts/multi-agent>)).


## Fonte da seleção e comportamento de fallback

O mesmo `provider/model` pode significar coisas diferentes dependendo de onde veio:

  * Padrões configurados (`agents.defaults.model.primary` e modelos principais específicos de agente) são o ponto de partida normal e usam `agents.defaults.model.fallbacks`.
  * Seleções automáticas de fallback são estado temporário de recuperação. Elas são armazenadas com `modelOverrideSource: "auto"` para que turnos posteriores possam continuar usando a cadeia de fallback sem sondar primeiro um modelo principal sabidamente ruim.
  * Seleções de sessão do usuário são exatas. `/model`, o seletor de modelo, `session_status(model=...)` e `sessions.patch` armazenam `modelOverrideSource: "user"`; se esse provedor/modelo selecionado estiver inacessível, o OpenClaw falha de forma visível em vez de seguir para outro modelo configurado.
  * Cron `--model` / payload `model` é um modelo principal por job. Ele ainda usa os fallbacks configurados, a menos que o job forneça `fallbacks` explícitos no payload (use `fallbacks: []` para uma execução cron estrita).
  * Seletores de modelo padrão e lista de permissões da CLI respeitam `models.mode: "replace"` listando `models.providers.*.models` explícitos em vez de carregar todo o catálogo integrado.
  * O seletor de modelo da UI de Controle solicita ao Gateway sua visão de modelos configurada: `agents.defaults.models` quando presente, incluindo entradas `provider/*` para provedores inteiros; caso contrário, `models.providers.*.models` explícitos mais provedores com autenticação utilizável. O catálogo integrado completo é reservado para visualizações explícitas de navegação, como `models.list` com `view: "all"` ou `openclaw models list --all`.


## Política rápida de modelos

  * Defina seu principal como o modelo mais forte de geração mais recente disponível para você.
  * Use fallbacks para tarefas sensíveis a custo/latência e chats de menor risco.
  * Para agentes com ferramentas habilitadas ou entradas não confiáveis, evite camadas de modelo mais antigas/fracas.


## Onboarding (recomendado)

Se você não quiser editar a configuração manualmente, execute o onboarding:

bashCopy code
[code]
    openclaw onboard
[/code]

Ele pode configurar modelo + autenticação para provedores comuns, incluindo **assinatura OpenAI Code (Codex)** (OAuth) e **Anthropic** (chave de API ou Claude CLI).

## Chaves de configuração (visão geral)

  * `agents.defaults.model.primary` e `agents.defaults.model.fallbacks`
  * `agents.defaults.imageModel.primary` e `agents.defaults.imageModel.fallbacks`
  * `agents.defaults.pdfModel.primary` e `agents.defaults.pdfModel.fallbacks`
  * `agents.defaults.imageGenerationModel.primary` e `agents.defaults.imageGenerationModel.fallbacks`
  * `agents.defaults.videoGenerationModel.primary` e `agents.defaults.videoGenerationModel.fallbacks`
  * `agents.defaults.models` (lista de permissões + aliases + parâmetros de provedor + entradas dinâmicas de provedor `provider/*`)
  * `models.providers` (provedores personalizados gravados em `models.json`)


### Edições seguras na lista de permissões

Use gravações aditivas ao atualizar `agents.defaults.models` manualmente:

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --merge
[/code]

Regras de proteção contra sobrescrita

`openclaw config set` protege mapas de modelos/provedores contra sobrescritas acidentais. Uma atribuição de objeto simples a `agents.defaults.models`, `models.providers` ou `models.providers.<id>.models` é rejeitada quando removeria entradas existentes. Use `--merge` para alterações aditivas; use `--replace` somente quando o valor fornecido deve se tornar o valor-alvo completo.

A configuração interativa de provedor e `openclaw configure --section model` também mesclam seleções com escopo de provedor na lista de permissões existente, portanto adicionar Codex, Ollama ou outro provedor não remove entradas de modelo não relacionadas. A configuração preserva um `agents.defaults.model.primary` existente quando a autenticação do provedor é reaplicada. Comandos explícitos de definição de padrão, como `openclaw models auth login --provider <id> --set-default` e `openclaw models set <model>`, ainda substituem `agents.defaults.model.primary`.

## "Modelo não permitido" (e por que as respostas param)

Se `agents.defaults.models` estiver definido, ele se torna a **lista de permissões** para `/model` e para substituições de sessão. Quando um usuário seleciona um modelo que não está nessa lista de permissões, o OpenClaw retorna:

CodeCopy code
[code]
    Model "provider/model" is not allowed. Use /models to list providers, or /models <provider> to list models.Add it with: openclaw config set agents.defaults.models '{"provider/model":{}}' --strict-json --merge
[/code]

Quando o comando rejeitado incluía uma substituição de runtime, como `/model openai/gpt-5.5 --runtime codex`, corrija primeiro a lista de permissões e depois tente novamente o mesmo comando `/model ... --runtime ...`. Para execução nativa do Codex, o modelo selecionado ainda é `openai/gpt-5.5`; o runtime `codex` seleciona o harness e usa a autenticação Codex separadamente.

Para modelos locais/GGUF, armazene a ref completa prefixada pelo provedor na lista de permissões, por exemplo `ollama/gemma4:26b`, `lmstudio/Gemma4-26b-a4-it-gguf` ou o provedor/modelo exato mostrado por `openclaw models list --provider <provider>`. Nomes de arquivo locais simples ou nomes de exibição não bastam quando a lista de permissões está ativa.

Se você quiser limitar provedores sem listar manualmente todos os modelos, adicione entradas `provider/*` a `agents.defaults.models`:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai-codex/*": {},        "vllm/*": {},      },    },  },}
[/code]

Com essa política, `/model`, `/models` e seletores de modelo mostram o catálogo descoberto somente para esses provedores. Novos modelos dos provedores selecionados podem aparecer sem editar a lista de permissões. Entradas exatas `provider/model` podem ser combinadas com entradas `provider/*` quando você precisar de um modelo específico de outro provedor.

Exemplo de configuração de lista de permissões:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-sonnet-4-6" },      models: {        "anthropic/claude-sonnet-4-6": { alias: "Sonnet" },        "anthropic/claude-opus-4-6": { alias: "Opus" },      },    },  },}
[/code]

## Troca de modelos no chat (`/model`)

Você pode trocar os modelos da sessão atual sem reiniciar:

CodeCopy code
[code]
    /model/model list/model 3/model openai/gpt-5.4/model status
[/code]

Comportamento do seletor

  * `/model` (e `/model list`) é um seletor compacto e numerado (família do modelo + provedores disponíveis).
  * No Discord, `/model` e `/models` abrem um seletor interativo com menus suspensos de provedor e modelo, além de uma etapa de Enviar.
  * No Telegram, as seleções do seletor `/models` têm escopo de sessão; elas não alteram o padrão persistente do agente em `openclaw.json`.
  * `/models add` está obsoleto e agora retorna uma mensagem de descontinuação em vez de registrar modelos pelo chat.
  * `/model <#>` seleciona a partir desse seletor.

Persistência e troca ao vivo

  * `/model` persiste imediatamente a nova seleção da sessão.
  * Se o agente estiver ocioso, a próxima execução usa o novo modelo imediatamente.
  * Se uma execução já estiver ativa, o OpenClaw marca uma troca ao vivo como pendente e só reinicia no novo modelo em um ponto de nova tentativa limpo.
  * Se a atividade de ferramentas ou a saída da resposta já tiver começado, a troca pendente pode ficar na fila até uma oportunidade posterior de nova tentativa ou até o próximo turno do usuário.
  * Uma ref `/model` selecionada pelo usuário é estrita para essa sessão: se o provedor/modelo selecionado estiver inacessível, a resposta falha de forma visível em vez de responder silenciosamente a partir de `agents.defaults.model.fallbacks`. Isso difere dos padrões configurados e dos modelos principais de jobs cron, que ainda podem usar cadeias de fallback.
  * `/model status` é a visão detalhada (candidatos de autenticação e, quando configurado, `baseUrl` do endpoint do provedor + modo `api`).

Análise de referências

  * Referências de modelo são analisadas dividindo na **primeira** `/`. Use `provider/model` ao digitar `/model <ref>`.
  * Se o ID do modelo em si contiver `/` (estilo OpenRouter), você deve incluir o prefixo do provedor (exemplo: `/model openrouter/moonshotai/kimi-k2`).
  * Se você omitir o provedor, o OpenClaw resolve a entrada nesta ordem: 
    1. correspondência de alias
    2. correspondência única de provedor configurado para esse ID de modelo exato sem prefixo
    3. fallback obsoleto para o provedor padrão configurado — se esse provedor não expuser mais o modelo padrão configurado, o OpenClaw usará como fallback o primeiro provedor/modelo configurado para evitar exibir um padrão obsoleto de provedor removido.


Comportamento/configuração completa do comando: [Comandos de barra](</pt-BR/tools/slash-commands>).

## Comandos da CLI

bashCopy code
[code]
    openclaw models listopenclaw models statusopenclaw models set <provider/model>openclaw models set-image <provider/model> openclaw models aliases listopenclaw models aliases add <alias> <provider/model>openclaw models aliases remove <alias> openclaw models fallbacks listopenclaw models fallbacks add <provider/model>openclaw models fallbacks remove <provider/model>openclaw models fallbacks clear openclaw models image-fallbacks listopenclaw models image-fallbacks add <provider/model>openclaw models image-fallbacks remove <provider/model>openclaw models image-fallbacks clear
[/code]

`openclaw models` (sem subcomando) é um atalho para `models status`.

### `models list`

Mostra modelos configurados/disponíveis para autenticação por padrão. Flags úteis:

Catálogo completo. Inclui linhas de catálogo estático pertencentes ao provedor e empacotadas antes que a autenticação seja configurada, para que visualizações apenas de descoberta possam mostrar modelos indisponíveis até você adicionar credenciais correspondentes do provedor.

Apenas provedores locais.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tcHJvdmlkZXIgPGlk " type="string"> Filtra por ID do provedor, por exemplo `moonshot`. Rótulos exibidos em seletores interativos não são aceitos.

Um modelo por linha.

Saída legível por máquina.

### `models status`

Mostra o modelo primário resolvido, fallbacks, modelo de imagem e uma visão geral de autenticação dos provedores configurados. Também exibe o status de expiração de OAuth para perfis encontrados no armazenamento de autenticação (avisa dentro de 24h por padrão). `--plain` imprime apenas o modelo primário resolvido.

Comportamento de autenticação e sondagem

  * O status de OAuth é sempre mostrado (e incluído na saída `--json`). Se um provedor configurado não tiver credenciais, `models status` imprime uma seção **Autenticação ausente**.
  * JSON inclui `auth.oauth` (janela de aviso + perfis) e `auth.providers` (autenticação efetiva por provedor, incluindo credenciais baseadas em env). `auth.oauth` é apenas a integridade de perfis do armazenamento de autenticação; provedores somente por env não aparecem ali.
  * Use `--check` para automação (sai com `1` quando ausente/expirado, `2` quando estiver expirando).
  * Use `--probe` para verificações de autenticação ao vivo; linhas de sondagem podem vir de perfis de autenticação, credenciais de env ou `models.json`.
  * Se `auth.order.<provider>` explícito omitir um perfil armazenado, a sondagem relata `excluded_by_auth_order` em vez de tentar usá-lo. Se a autenticação existir, mas nenhum modelo sondável puder ser resolvido para esse provedor, a sondagem relata `status: no_model`.


Exemplo (CLI do Claude):

bashCopy code
[code]
    claude auth loginopenclaw models status
[/code]

## Varredura (modelos gratuitos do OpenRouter)

`openclaw models scan` inspeciona o **catálogo de modelos gratuitos** do OpenRouter e pode, opcionalmente, sondar modelos para suporte a ferramentas e imagens.

Pula sondagens ao vivo (apenas metadados).

Define `agents.defaults.model.primary` como a primeira seleção.

Define `agents.defaults.imageModel.primary` como a primeira seleção de imagem.

Os resultados da varredura são classificados por:

  1. Suporte a imagem
  2. Latência de ferramentas
  3. Tamanho de contexto
  4. Contagem de parâmetros


Entrada:

  * Lista `/models` do OpenRouter (filtro `:free`)
  * Sondagens ao vivo exigem uma chave de API do OpenRouter de perfis de autenticação ou `OPENROUTER_API_KEY` (veja [Variáveis de ambiente](</pt-BR/help/environment>))
  * Filtros opcionais: `--max-age-days`, `--min-params`, `--provider`, `--max-candidates`
  * Controles de solicitação/sondagem: `--timeout`, `--concurrency`


Quando sondagens ao vivo são executadas em um TTY, você pode selecionar fallbacks interativamente. No modo não interativo, passe `--yes` para aceitar os padrões. Resultados apenas de metadados são informativos; `--set-default` e `--set-image` exigem sondagens ao vivo para que o OpenClaw não configure um modelo OpenRouter sem chave e inutilizável.

## Registro de modelos (`models.json`)

Provedores personalizados em `models.providers` são gravados em `models.json` no diretório do agente (padrão `~/.openclaw/agents/<agentId>/agent/models.json`). Esse arquivo é mesclado por padrão, a menos que `models.mode` esteja definido como `replace`.

Precedência do modo de mesclagem

Precedência do modo de mesclagem para IDs de provedor correspondentes:

  * `baseUrl` não vazio já presente no `models.json` do agente vence.
  * `apiKey` não vazio no `models.json` do agente vence somente quando esse provedor não é gerenciado por SecretRef no contexto atual de configuração/perfil de autenticação.
  * Valores de `apiKey` de provedor gerenciados por SecretRef são atualizados a partir de marcadores de origem (`ENV_VAR_NAME` para refs de env, `secretref-managed` para refs de arquivo/exec) em vez de persistir segredos resolvidos.
  * Valores de cabeçalho de provedor gerenciados por SecretRef são atualizados a partir de marcadores de origem (`secretref-env:ENV_VAR_NAME` para refs de env, `secretref-managed` para refs de arquivo/exec).
  * `apiKey`/`baseUrl` do agente vazios ou ausentes voltam para `models.providers` da configuração.
  * Outros campos do provedor são atualizados a partir da configuração e de dados de catálogo normalizados.


## Relacionados

  * [Runtimes de agente](</pt-BR/concepts/agent-runtimes>) — PI, Codex e outros runtimes de loop de agente
  * [Referência de configuração](</pt-BR/gateway/config-agents#agent-defaults>) — chaves de configuração de modelo
  * [Geração de imagens](</pt-BR/tools/image-generation>) — configuração de modelo de imagem
  * [Failover de modelo](</pt-BR/concepts/model-failover>) — cadeias de fallback
  * [Provedores de modelo](</pt-BR/concepts/model-providers>) — roteamento e autenticação de provedor
  * [Geração de música](</pt-BR/tools/music-generation>) — configuração de modelo de música
  * [Geração de vídeo](</pt-BR/tools/video-generation>) — configuração de modelo de vídeo


Was this useful?YesNo