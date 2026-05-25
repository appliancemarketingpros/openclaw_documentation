---
title: Anthropic
source_url: https://docs.openclaw.ai/pt-BR/providers/anthropic
scraped_at: 2026-05-25
---

A Anthropic cria a família de modelos **Claude**. O OpenClaw oferece suporte a duas rotas de autenticação:

  * **Chave de API** — acesso direto à API da Anthropic com cobrança baseada em uso (modelos `anthropic/*`)
  * **Claude CLI** — reutilize um login existente do Claude CLI no mesmo host


## Introdução

### API key

**Ideal para:** acesso padrão à API e cobrança baseada em uso.

* ### Get your API key

Crie uma chave de API no [Console da Anthropic](<https://console.anthropic.com/>).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard# choose: Anthropic API key
[/code]

Ou passe a chave diretamente:

bashCopy code
[code]
    openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Exemplo de configuração

json5Copy code
[code]
    {  env: { ANTHROPIC_API_KEY: "sk-ant-..." },  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

### Claude CLI

**Ideal para:** reutilizar um login existente do Claude CLI sem uma chave de API separada.

* ### Ensure Claude CLI is installed and logged in

Verifique com:

bashCopy code
[code]
    claude --version
[/code]

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard# choose: Claude CLI
[/code]

O OpenClaw detecta e reutiliza as credenciais existentes do Claude CLI.

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Exemplo de configuração

Prefira a referência canônica de modelo da Anthropic mais uma substituição de runtime de CLI:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-7" },      models: {        "anthropic/claude-opus-4-7": {          agentRuntime: { id: "claude-cli" },        },      },    },  },}
[/code]

Referências legadas de modelo `claude-cli/claude-opus-4-7` ainda funcionam por compatibilidade, mas novas configurações devem manter a seleção de provedor/modelo como `anthropic/*` e colocar o backend de execução na política de runtime de provedor/modelo.

## Padrões de raciocínio (Claude 4.6)

Modelos Claude 4.6 usam `adaptive` thinking por padrão no OpenClaw quando nenhum nível explícito de thinking é definido.

Substitua por mensagem com `/think:<level>` ou nos parâmetros do modelo:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { thinking: "adaptive" },        },      },    },  },}
[/code]

## Cache de prompt

O OpenClaw oferece suporte ao recurso de cache de prompt da Anthropic para autenticação por chave de API.

Valor | Duração do cache | Descrição  
---|---|---  
`"short"` (padrão) | 5 minutos | Aplicado automaticamente para autenticação por chave de API  
`"long"` | 1 hora | Cache estendido  
`"none"` | Sem cache | Desabilita o cache de prompt  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },  },}
[/code]

Per-agent cache overrides

Use parâmetros no nível do modelo como base e depois substitua agentes específicos via `agents.list[].params`:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-6" },      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },    list: [      { id: "research", default: true },      { id: "alerts", params: { cacheRetention: "none" } },    ],  },}
[/code]

Ordem de mesclagem da configuração:

  1. `agents.defaults.models["provider/model"].params`
  2. `agents.list[].params` (correspondente ao `id`, substitui por chave)


Isso permite que um agente mantenha um cache de longa duração enquanto outro agente no mesmo modelo desabilita o cache para tráfego em rajadas/de baixa reutilização.

Bedrock Claude notes

  * Modelos Anthropic Claude no Bedrock (`amazon-bedrock/*anthropic.claude*`) aceitam repasse de `cacheRetention` quando configurado.
  * Modelos Bedrock que não são da Anthropic são forçados para `cacheRetention: "none"` em runtime.
  * Padrões inteligentes de chave de API também semeiam `cacheRetention: "short"` para referências Claude no Bedrock quando nenhum valor explícito é definido.


## Configuração avançada

Fast mode

O alternador compartilhado `/fast` do OpenClaw oferece suporte a tráfego direto da Anthropic (chave de API e OAuth para `api.anthropic.com`).

Comando | Mapeia para  
---|---  
`/fast on` | `service_tier: "auto"`  
`/fast off` | `service_tier: "standard_only"`  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-sonnet-4-6": {          params: { fastMode: true },        },      },    },  },}
[/code]

Media understanding (image and PDF)

O Plugin Anthropic incluído registra compreensão de imagem e PDF. O OpenClaw resolve automaticamente as capacidades de mídia a partir da autenticação Anthropic configurada — nenhuma configuração adicional é necessária.

Propriedade | Valor  
---|---  
Modelo padrão | `claude-opus-4-7`  
Entrada compatível | Imagens, documentos PDF  
  
Quando uma imagem ou PDF é anexado a uma conversa, o OpenClaw automaticamente o roteia pelo provedor de compreensão de mídia da Anthropic.

1M context window (beta)

A janela de contexto de 1M da Anthropic é controlada por beta. Habilite por modelo:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { context1m: true },        },      },    },  },}
[/code]

O OpenClaw mapeia isso para `anthropic-beta: context-1m-2025-08-07` nas solicitações.

`params.context1m: true` também se aplica ao backend Claude CLI (`claude-cli/*`) para modelos Opus e Sonnet elegíveis, expandindo a janela de contexto de runtime dessas sessões de CLI para corresponder ao comportamento da API direta.

Claude Opus 4.7 1M context

`anthropic/claude-opus-4.7` e sua variante `claude-cli` têm uma janela de contexto de 1M por padrão — sem necessidade de `params.context1m: true`.

## Solução de problemas

401 errors / token suddenly invalid

A autenticação por token da Anthropic expira e pode ser revogada. Para novas configurações, use uma chave de API da Anthropic.

No API key found for provider "anthropic"

A autenticação Anthropic é **por agente** — novos agentes não herdam as chaves do agente principal. Execute o onboarding novamente para esse agente (ou configure uma chave de API no host do Gateway) e depois verifique com `openclaw models status`.

No credentials found for profile "anthropic:default"

Execute `openclaw models status` para ver qual perfil de autenticação está ativo. Execute o onboarding novamente ou configure uma chave de API para esse caminho de perfil.

No available auth profile (all in cooldown)

Verifique `openclaw models status --json` para `auth.unusableProfiles`. Cooldowns de limite de taxa da Anthropic podem ter escopo por modelo, então um modelo Anthropic irmão ainda pode ser utilizável. Adicione outro perfil Anthropic ou aguarde o cooldown.

## Relacionado

[**Model selection** Escolha de provedores, referências de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**CLI backends** Configuração do backend Claude CLI e detalhes de runtime. ](</pt-BR/gateway/cli-backends>) [**Prompt caching** Como o cache de prompt funciona entre provedores. ](</pt-BR/reference/prompt-caching>) [**OAuth and auth** Detalhes de autenticação e regras de reutilização de credenciais. ](</pt-BR/gateway/authentication>)

Was this useful?YesNo