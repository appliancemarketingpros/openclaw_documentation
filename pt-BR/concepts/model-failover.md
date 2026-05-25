---
title: Alternância de modelo em caso de falha
source_url: https://docs.openclaw.ai/pt-BR/concepts/model-failover
scraped_at: 2026-05-25
---

O OpenClaw lida com falhas em dois estágios:

  1. **Rotação de perfil de autenticação** dentro do provedor atual.
  2. **Fallback de modelo** para o próximo modelo em `agents.defaults.model.fallbacks`.


Este documento explica as regras de runtime e os dados que dão suporte a elas.

## Fluxo de runtime

Para uma execução normal de texto, o OpenClaw avalia os candidatos nesta ordem:

* ### Resolver estado da sessão

Resolver o modelo da sessão ativa e a preferência de perfil de autenticação.

* ### Construir cadeia de candidatos

Construir a cadeia de candidatos de modelo a partir da seleção de modelo atual e da política de fallback para a origem dessa seleção. Padrões configurados, primários de jobs Cron e modelos de fallback selecionados automaticamente podem usar fallbacks configurados; seleções explícitas de sessão do usuário são estritas.

* ### Tentar o provedor atual

Tentar o provedor atual com regras de rotação/cooldown de perfil de autenticação.

* ### Avançar em erros que justificam failover

Se esse provedor for esgotado com um erro que justifique failover, passar para o próximo candidato de modelo.

* ### Persistir substituição de fallback

Persistir a substituição de fallback selecionada antes do início da nova tentativa para que outros leitores da sessão vejam o mesmo provedor/modelo que o executor está prestes a usar. A substituição de modelo persistida é marcada como `modelOverrideSource: "auto"`.

* ### Reverter de forma restrita em caso de falha

Se o candidato de fallback falhar, reverter somente os campos de substituição de sessão pertencentes ao fallback quando eles ainda corresponderem a esse candidato com falha.

* ### Lançar FallbackSummaryError se esgotado

Se todos os candidatos falharem, lançar um `FallbackSummaryError` com detalhes por tentativa e a expiração de cooldown mais próxima quando uma for conhecida.

Isso é intencionalmente mais restrito do que "salvar e restaurar a sessão inteira". O executor de resposta só persiste os campos de seleção de modelo que ele controla para fallback:

  * `providerOverride`
  * `modelOverride`
  * `modelOverrideSource`
  * `authProfileOverride`
  * `authProfileOverrideSource`
  * `authProfileOverrideCompactionCount`


Isso impede que uma nova tentativa de fallback com falha sobrescreva mutações de sessão mais recentes e não relacionadas, como alterações manuais de `/model` ou atualizações de rotação de sessão que aconteceram enquanto a tentativa estava em execução.

## Política de origem da seleção

O OpenClaw separa o provedor/modelo selecionado do motivo pelo qual ele foi selecionado. Essa origem controla se a cadeia de fallback é permitida:

  * **Padrão configurado** : `agents.defaults.model.primary` usa `agents.defaults.model.fallbacks`.
  * **Primário do agente** : `agents.list[].model` é estrito, a menos que esse objeto de modelo do agente inclua seus próprios `fallbacks`. Use `fallbacks: []` para tornar o comportamento estrito explícito, ou forneça uma lista não vazia para habilitar fallback de modelo para esse agente.
  * **Substituição de fallback automática** : um fallback de runtime grava `providerOverride`, `modelOverride`, `modelOverrideSource: "auto"` e o modelo de origem selecionado antes de tentar novamente. Essa substituição automática pode continuar percorrendo a cadeia de fallback configurada e é limpa por `/new`, `/reset` e `sessions.reset`. Execuções de Heartbeat sem um `heartbeat.model` explícito também limpam uma substituição automática direta quando sua origem não corresponde mais ao padrão configurado atual.
  * **Substituição de sessão do usuário** : `/model`, o seletor de modelo, `session_status(model=...)` e `sessions.patch` gravam `modelOverrideSource: "user"`. Essa é uma seleção exata de sessão. Se o provedor/modelo selecionado falhar antes de produzir uma resposta, o OpenClaw relata a falha em vez de responder a partir de um fallback configurado não relacionado.
  * **Substituição de sessão legada** : entradas de sessão mais antigas podem ter `modelOverride` sem `modelOverrideSource`. O OpenClaw trata essas entradas como substituições do usuário para que uma seleção antiga explícita não seja convertida silenciosamente em comportamento de fallback.
  * **Modelo de payload Cron** : um `payload.model` / `--model` de job Cron é um primário de job, não uma substituição de sessão do usuário. Ele usa fallbacks configurados, a menos que o job forneça `payload.fallbacks`; `payload.fallbacks: []` torna a execução Cron estrita.


## Armazenamento de autenticação (chaves + OAuth)

O OpenClaw usa **perfis de autenticação** tanto para chaves de API quanto para tokens OAuth.

  * Segredos ficam em `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` (legado: `~/.openclaw/agent/auth-profiles.json`).
  * O estado de roteamento de autenticação em runtime fica em `~/.openclaw/agents/<agentId>/agent/auth-state.json`.
  * As configurações `auth.profiles` / `auth.order` são **somente metadados + roteamento** (sem segredos).
  * Arquivo OAuth legado somente para importação: `~/.openclaw/credentials/oauth.json` (importado para `auth-profiles.json` no primeiro uso).


Mais detalhes: [OAuth](</pt-BR/concepts/oauth>)

Tipos de credencial:

  * `type: "api_key"` → `{ provider, key }`
  * `type: "oauth"` → `{ provider, access, refresh, expires, email? }` (+ `projectId`/`enterpriseUrl` para alguns provedores)


## IDs de perfil

Logins OAuth criam perfis distintos para que várias contas possam coexistir.

  * Padrão: `provider:default` quando nenhum e-mail está disponível.
  * OAuth com e-mail: `provider:<email>` (por exemplo, `google-antigravity:user@gmail.com`).


Os perfis ficam em `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` em `profiles`.

## Ordem de rotação

Quando um provedor tem vários perfis, o OpenClaw escolhe uma ordem assim:

* ### Configuração explícita

`auth.order[provider]` (se definido).

* ### Perfis configurados

`auth.profiles` filtrado por provedor.

* ### Perfis armazenados

Entradas em `auth-profiles.json` para o provedor.

Se nenhuma ordem explícita for configurada, o OpenClaw usa uma ordem round-robin:

  * **Chave primária:** tipo de perfil (**OAuth antes de chaves de API**).
  * **Chave secundária:** `usageStats.lastUsed` (mais antigo primeiro, dentro de cada tipo).
  * **Perfis em cooldown/desabilitados** são movidos para o fim, ordenados pela expiração mais próxima.


### Afinidade de sessão (amigável ao cache)

OpenClaw **fixa o perfil de autenticação escolhido por sessão** para manter os caches do provedor aquecidos. Ele **não** alterna a cada solicitação. O perfil fixado é reutilizado até que:

  * a sessão seja redefinida (`/new` / `/reset`)
  * uma Compaction seja concluída (a contagem de Compaction incrementa)
  * o perfil esteja em período de espera/desabilitado


A seleção manual via `/model …@<profileId>` define uma **substituição do usuário** para essa sessão e não é alternada automaticamente até que uma nova sessão comece.

### Assinatura do OpenAI Codex mais backup por chave de API

Para modelos de agente da OpenAI, autenticação e ambiente de execução são separados. `openai/gpt-*` permanece no harness do Codex enquanto a autenticação pode alternar entre um perfil de assinatura do Codex e um backup por chave de API da OpenAI.

Use `auth.order.openai` para a ordem voltada ao usuário:

json5Copy code
[code]
    {  auth: {    order: {      openai: ["openai-codex:user@example.com", "openai:api-key-backup"],    },  },}
[/code]

Perfis existentes de assinatura do Codex ainda podem usar o id de perfil legado `openai-codex:*`. O backup ordenado por chave de API pode ser um perfil normal de chave de API `openai:*`. Quando a assinatura atinge um limite de uso do Codex, o OpenClaw registra o horário exato de redefinição quando o Codex fornece um, tenta o próximo perfil de autenticação ordenado e mantém a execução dentro do harness do Codex. Depois que o horário de redefinição passa, o perfil da assinatura fica qualificado novamente e a próxima seleção automática pode retornar a ele.

Use um perfil fixado pelo usuário apenas quando quiser forçar uma conta/chave para essa sessão. Perfis fixados pelo usuário são intencionalmente estritos e não pulam silenciosamente para outro perfil.

## Períodos de espera

Quando um perfil falha devido a erros de autenticação/limite de taxa (ou um tempo limite que parece limitação de taxa), o OpenClaw o marca em período de espera e passa para o próximo perfil.

O que entra na categoria de limite de taxa / timeout

Essa categoria de limite de taxa é mais ampla do que um simples `429`: ela também inclui mensagens de provedores como `Too many concurrent requests`, `ThrottlingException`, `concurrency limit reached`, `workers_ai ... quota limit exceeded`, `throttled`, `resource exhausted` e limites periódicos de janelas de uso como `weekly/monthly limit reached`.

Erros de formato/solicitação inválida geralmente são terminais porque repetir a mesma carga útil falharia da mesma forma, então o OpenClaw os expõe em vez de alternar perfis de autenticação. Caminhos conhecidos de reparo por repetição podem aderir explicitamente: por exemplo, falhas de validação de ID de chamada de ferramenta do Cloud Code Assist são sanitizadas e repetidas uma vez por meio da política `allowFormatRetry`. Erros de motivo de parada compatíveis com OpenAI, como `Unhandled stop reason: error`, `stop reason: error` e `reason: error`, são classificados como sinais de timeout/failover.

Texto genérico de servidor também pode entrar nessa categoria de timeout quando a origem corresponde a um padrão transitório conhecido. Por exemplo, a mensagem simples do wrapper de stream do pi-ai `An unknown error occurred` é tratada como digna de failover para todos os provedores porque o pi-ai a emite quando streams de provedores terminam com `stopReason: "aborted"` ou `stopReason: "error"` sem detalhes específicos. Cargas úteis JSON `api_error` com texto transitório de servidor, como `internal server error`, `unknown error, 520`, `upstream error` ou `backend error`, também são tratadas como timeouts dignos de failover.

Texto genérico de upstream específico do OpenRouter, como o simples `Provider returned error`, é tratado como timeout somente quando o contexto do provedor é de fato o OpenRouter. Texto genérico de fallback interno, como `LLM request failed with an unknown error.`, permanece conservador e não aciona failover por si só.

Limites de retry-after do SDK

Alguns SDKs de provedores poderiam, caso contrário, aguardar uma janela longa de `Retry-After` antes de devolver o controle ao OpenClaw. Para SDKs baseados em Stainless, como Anthropic e OpenAI, o OpenClaw limita por padrão as esperas internas do SDK `retry-after-ms` / `retry-after` a 60 segundos e expõe respostas repetíveis mais longas imediatamente para que esse caminho de failover possa ser executado. Ajuste ou desative o limite com `OPENCLAW_SDK_RETRY_MAX_WAIT_SECONDS`; consulte [Comportamento de repetição](</pt-BR/concepts/retry>).

Cooldowns por modelo

Cooldowns de limite de taxa também podem ser por modelo:

  * O OpenClaw registra `cooldownModel` para falhas de limite de taxa quando o ID do modelo que falhou é conhecido.
  * Um modelo irmão no mesmo provedor ainda pode ser tentado quando o cooldown está restrito a outro modelo.
  * Janelas de cobrança/desativação ainda bloqueiam o perfil inteiro entre modelos.


Cooldowns usam backoff exponencial:

  * 1 minuto
  * 5 minutos
  * 25 minutos
  * 1 hora (limite)


O estado é armazenado em `auth-state.json` dentro de `usageStats`:

jsonCopy code
[code]
    {  "usageStats": {    "provider:profile": {      "lastUsed": 1736160000000,      "cooldownUntil": 1736160600000,      "errorCount": 2    }  }}
[/code]

## Desativações por cobrança

Falhas de cobrança/crédito (por exemplo, "créditos insuficientes" / "saldo de crédito muito baixo") são tratadas como dignas de failover, mas geralmente não são transitórias. Em vez de um cooldown curto, o OpenClaw marca o perfil como **desativado** (com um backoff mais longo) e alterna para o próximo perfil/provedor.

O estado é armazenado em `auth-state.json`:

jsonCopy code
[code]
    {  "usageStats": {    "provider:profile": {      "disabledUntil": 1736178000000,      "disabledReason": "billing"    }  }}
[/code]

Padrões:

  * O recuo de cobrança começa em **5 horas** , dobra a cada falha de cobrança e tem limite máximo de **24 horas**.
  * Os contadores de recuo são redefinidos se o perfil não falhar por **24 horas** (configurável).
  * Novas tentativas por sobrecarga permitem **1 rotação de perfil do mesmo provedor** antes do fallback de modelo.
  * Novas tentativas por sobrecarga usam **0 ms de recuo** por padrão.


## Fallback de modelo

Se todos os perfis de um provedor falharem, o OpenClaw passa para o próximo modelo em `agents.defaults.model.fallbacks`. Isso se aplica a falhas de autenticação, limites de taxa e tempos limite que esgotaram a rotação de perfis (outros erros não avançam o fallback). Erros de provedor que não expõem detalhes suficientes ainda são rotulados com precisão no estado de fallback: `empty_response` significa que o provedor não retornou nenhuma mensagem ou status utilizável, `no_error_details` significa que o provedor retornou explicitamente `Unknown error (no error details in response)`, e `unclassified` significa que o OpenClaw preservou a prévia bruta, mas nenhum classificador ainda correspondeu a ela.

Erros de sobrecarga e limite de taxa são tratados de forma mais agressiva que cooldowns de cobrança. Por padrão, o OpenClaw permite uma nova tentativa com perfil de autenticação do mesmo provedor e, em seguida, muda para o próximo fallback de modelo configurado sem esperar. Sinais de provedor ocupado, como `ModelNotReadyException`, entram nesse bucket de sobrecarga. Ajuste isso com `auth.cooldowns.overloadedProfileRotations`, `auth.cooldowns.overloadedBackoffMs` e `auth.cooldowns.rateLimitedProfileRotations`.

Quando uma execução começa pelo primário padrão configurado, por um primário de job cron, por um primário de agente com fallbacks explícitos ou por uma substituição de fallback selecionada automaticamente, o OpenClaw pode percorrer a cadeia de fallback configurada correspondente. Primários de agente sem fallbacks explícitos e seleções explícitas do usuário (por exemplo, `/model ollama/qwen3.5:27b`, o seletor de modelo, `sessions.patch` ou substituições pontuais de provedor/modelo pela CLI) são estritos: se esse provedor/modelo estiver inacessível ou falhar antes de produzir uma resposta, o OpenClaw relata a falha em vez de responder a partir de um fallback não relacionado.

### Regras da cadeia de candidatos

O OpenClaw cria a lista de candidatos a partir do `provider/model` solicitado no momento mais os fallbacks configurados.

Regras

  * O modelo solicitado sempre vem primeiro.
  * Fallbacks configurados explícitos são deduplicados, mas não filtrados pela lista de modelos permitidos. Eles são tratados como intenção explícita do operador.
  * Se a execução atual já estiver em um fallback configurado na mesma família de provedores, o OpenClaw continua usando a cadeia configurada completa.
  * Quando nenhuma substituição explícita de fallback é fornecida, os fallbacks configurados são tentados antes do primário configurado, mesmo que o modelo solicitado use um provedor diferente.
  * Quando nenhuma substituição explícita de fallback é fornecida ao executor de fallback, o primário configurado é anexado ao final para que a cadeia possa voltar ao padrão normal depois que os candidatos anteriores forem esgotados.
  * Quando um chamador fornece `fallbacksOverride`, o executor usa exatamente o modelo solicitado mais essa lista de substituição. Uma lista vazia desativa o fallback de modelo e impede que o primário configurado seja anexado como um alvo de nova tentativa oculto.


### Quais erros avançam o fallback

### Continua em

  * falhas de autenticação
  * limites de taxa e esgotamento de cooldown
  * erros de sobrecarga/provedor ocupado
  * erros de failover com formato de tempo limite
  * desativações por cobrança
  * `LiveSessionModelSwitchError`, que é normalizado em um caminho de failover para que um modelo persistido obsoleto não crie um loop externo de nova tentativa
  * outros erros não reconhecidos quando ainda há candidatos restantes


### Não continua em

  * abortos explícitos que não tenham formato de tempo limite/failover
  * erros de estouro de contexto que devem permanecer dentro da lógica de Compaction/nova tentativa (por exemplo, `request_too_large`, `INVALID_ARGUMENT: input exceeds the maximum number of tokens`, `input token count exceeds the maximum number of input tokens`, `The input is too long for the model` ou `ollama error: context length exceeded`)
  * um erro desconhecido final quando não há candidatos restantes


### Comportamento de pular cooldown versus sondar

Quando todos os perfis de autenticação de um provedor já estão em cooldown, o OpenClaw não pula automaticamente esse provedor para sempre. Ele toma uma decisão por candidato:

Decisões por candidato

  * Falhas persistentes de autenticação pulam o provedor inteiro imediatamente.
  * Desativações por cobrança geralmente são puladas, mas o candidato primário ainda pode ser sondado com limitação para possibilitar a recuperação sem reiniciar.
  * O candidato primário pode ser sondado perto do fim do cooldown, com uma limitação por provedor.
  * Irmãos de fallback do mesmo provedor podem ser tentados apesar do cooldown quando a falha parece transitória (`rate_limit`, `overloaded` ou desconhecida). Isso é especialmente relevante quando um limite de taxa tem escopo de modelo e um modelo irmão ainda pode se recuperar imediatamente.
  * Sondas de cooldown transitório são limitadas a uma por provedor por execução de fallback para que um único provedor não bloqueie o fallback entre provedores.


## Substituições de sessão e troca de modelo ao vivo

Alterações de modelo da sessão são estado compartilhado. O executor ativo, o comando `/model`, atualizações de Compaction/sessão e reconciliação de sessão ao vivo leem ou escrevem partes da mesma entrada de sessão.

Isso significa que novas tentativas de fallback precisam se coordenar com a troca de modelo ao vivo:

  * Somente alterações de modelo explícitas acionadas pelo usuário marcam uma troca ao vivo pendente. Isso inclui `/model`, `session_status(model=...)` e `sessions.patch`.
  * Alterações de modelo acionadas pelo sistema, como rotação de fallback, substituições de Heartbeat ou Compaction, nunca marcam sozinhas uma troca ao vivo pendente.
  * Substituições de modelo acionadas pelo usuário são tratadas como seleções exatas para a política de fallback; portanto, um provedor selecionado inacessível aparece como uma falha em vez de ser mascarado por `agents.defaults.model.fallbacks`.
  * Antes de uma nova tentativa de fallback começar, o executor de resposta persiste os campos de substituição de fallback selecionados na entrada da sessão.
  * Substituições automáticas de fallback permanecem selecionadas em turnos subsequentes para que o OpenClaw não sonde um primário sabidamente problemático a cada mensagem. `/new`, `/reset` e `sessions.reset` limpam substituições de origem automática e retornam a sessão ao padrão configurado.
  * `/status` mostra o modelo selecionado e, quando o estado de fallback difere, o modelo de fallback ativo e o motivo.
  * A reconciliação de sessão ao vivo prefere substituições de sessão persistidas em vez de campos de modelo de runtime obsoletos.
  * Se um erro de troca ao vivo apontar para um candidato posterior na cadeia de fallback ativa, o OpenClaw pula diretamente para esse modelo selecionado em vez de percorrer candidatos não relacionados primeiro.
  * Se a tentativa de fallback falhar, o executor reverte apenas os campos de substituição que escreveu, e somente se eles ainda corresponderem ao candidato que falhou.


Isso evita a corrida clássica:

* ### Primário falha

O modelo primário selecionado falha.

* ### Fallback escolhido na memória

O candidato de fallback é escolhido na memória.

* ### Armazenamento da sessão ainda indica o primário antigo

O armazenamento da sessão ainda reflete o primário antigo.

* ### Reconciliação ao vivo lê estado obsoleto

A reconciliação de sessão ao vivo lê o estado obsoleto da sessão.

* ### Nova tentativa volta ao anterior

A nova tentativa é levada de volta ao modelo antigo antes de a tentativa de fallback começar.

A substituição de fallback persistida fecha essa janela, e a reversão estreita mantém intactas as alterações manuais ou de sessão de runtime mais recentes.

## Observabilidade e resumos de falha

`runWithModelFallback(...)` registra detalhes por tentativa que alimentam logs e mensagens de cooldown voltadas ao usuário:

  * provedor/modelo tentado
  * motivo (`rate_limit`, `overloaded`, `billing`, `auth`, `model_not_found` e motivos de failover semelhantes)
  * status/código opcional
  * resumo de erro legível por humanos


Logs estruturados `model_fallback_decision` também incluem campos planos `fallbackStep*` quando um candidato falha, é pulado ou um fallback posterior tem sucesso. Esses campos tornam explícita a transição tentada (`fallbackStepFromModel`, `fallbackStepToModel`, `fallbackStepFromFailureReason`, `fallbackStepFromFailureDetail`, `fallbackStepFinalOutcome`) para que logs e exportadores de diagnóstico possam reconstruir a falha primária mesmo quando o fallback terminal também falhar.

Quando todos os candidatos falham, o OpenClaw lança `FallbackSummaryError`. O executor externo de resposta pode usar isso para criar uma mensagem mais específica, como "todos os modelos estão temporariamente limitados por taxa", e incluir a expiração de cooldown mais próxima quando ela for conhecida.

Esse resumo de cooldown considera o modelo:

  * limites de taxa com escopo de modelo não relacionados são ignorados para a cadeia de provedor/modelo tentada
  * se o bloqueio restante for um limite de taxa com escopo de modelo correspondente, o OpenClaw relata a última expiração correspondente que ainda bloqueia esse modelo


## Configuração relacionada

Veja [Configuração do Gateway](</pt-BR/gateway/configuration>) para:

  * `auth.profiles` / `auth.order`
  * `auth.cooldowns.billingBackoffHours` / `auth.cooldowns.billingBackoffHoursByProvider`
  * `auth.cooldowns.billingMaxHours` / `auth.cooldowns.failureWindowHours`
  * `auth.cooldowns.overloadedProfileRotations` / `auth.cooldowns.overloadedBackoffMs`
  * `auth.cooldowns.rateLimitedProfileRotations`
  * `agents.defaults.model.primary` / `agents.defaults.model.fallbacks`
  * roteamento de `agents.defaults.imageModel`


Veja [Modelos](</pt-BR/concepts/models>) para a visão geral mais ampla de seleção de modelos e fallback.

Was this useful?YesNo