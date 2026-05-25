---
title: GitHub Copilot
source_url: https://docs.openclaw.ai/pt-BR/providers/github-copilot
scraped_at: 2026-05-25
---

GitHub Copilot é o assistente de programação por IA do GitHub. Ele fornece acesso aos modelos do Copilot para sua conta e seu plano do GitHub. O OpenClaw pode usar o Copilot como provedor de modelos de duas maneiras diferentes.

## Duas maneiras de usar o Copilot no OpenClaw

### Built-in provider (github-copilot)

Use o fluxo nativo de login por dispositivo para obter um token do GitHub e, em seguida, trocá-lo por tokens da API do Copilot quando o OpenClaw for executado. Este é o caminho **padrão** e mais simples porque não requer o VS Code.

* ### Run the login command

bashCopy code
[code]
    openclaw models auth login-github-copilot
[/code]

Você será solicitado a acessar uma URL e inserir um código de uso único. Mantenha o terminal aberto até que ele seja concluído.

* ### Set a default model

bashCopy code
[code]
    openclaw models set github-copilot/claude-opus-4.7
[/code]

Ou na configuração:

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "github-copilot/claude-opus-4.7" } },  },}
[/code]

### Copilot Proxy plugin (copilot-proxy)

Use a extensão **Copilot Proxy** do VS Code como uma ponte local. O OpenClaw se comunica com o endpoint `/v1` do proxy e usa a lista de modelos que você configura ali.

## Flags opcionais

Flag | Descrição  
---|---  
`--yes` | Pula o prompt de confirmação  
`--set-default` | Também aplica o modelo padrão recomendado pelo provedor  
bashCopy code
[code]
    # Skip confirmationopenclaw models auth login-github-copilot --yes # Login and set the default model in one stepopenclaw models auth login --provider github-copilot --method device --set-default
[/code]

## Integração não interativa

Se você já tem um token de acesso OAuth do GitHub para o Copilot, importe-o durante a configuração sem interface com `openclaw onboard --non-interactive`:

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --auth-choice github-copilot \  --github-copilot-token "$COPILOT_GITHUB_TOKEN" \  --skip-channels --skip-health
[/code]

Você também pode omitir `--auth-choice`; passar `--github-copilot-token` infere a opção de autenticação do provedor GitHub Copilot. Se a flag for omitida, a integração recorre a `COPILOT_GITHUB_TOKEN`, `GH_TOKEN` e depois `GITHUB_TOKEN`. Use `--secret-input-mode ref` com `COPILOT_GITHUB_TOKEN` definido para armazenar um `tokenRef` respaldado por env em vez de texto simples em `auth-profiles.json`.

Interactive TTY required

O fluxo de login por dispositivo requer uma TTY interativa. Execute-o diretamente em um terminal, não em um script não interativo ou pipeline de CI.

Model availability depends on your plan

A disponibilidade de modelos do Copilot depende do seu plano do GitHub. Se um modelo for rejeitado, tente outro ID (por exemplo, `github-copilot/gpt-4.1`).

Live catalog refresh from the Copilot API

Depois que o caminho de autenticação por login de dispositivo (ou env-var) resolver um token do GitHub, o OpenClaw atualiza o catálogo de modelos sob demanda a partir de `${baseUrl}/models` (o mesmo endpoint que o VS Code Copilot usa), de modo que o runtime acompanhe a autorização por conta e janelas de contexto precisas sem rotatividade de manifesto. Modelos Copilot recém-publicados ficam visíveis sem uma atualização do OpenClaw, e as janelas de contexto refletem os limites reais por modelo (por exemplo, 400k para a série gpt-5.x, 1M para as variantes internas `claude-opus-*-1m`).

O catálogo estático incluído permanece como fallback visível quando a descoberta está desabilitada, o usuário não tem perfil de autenticação do GitHub, a troca de token falha ou a chamada HTTPS para `/models` gera erro. Para desativar e depender inteiramente do catálogo de manifesto estático (cenários offline / isolados da rede):

json5Copy code
[code]
    {  plugins: {    entries: {      "github-copilot": {        config: { discovery: { enabled: false } },      },    },  },}
[/code]

Transport selection

IDs de modelo Claude usam automaticamente o transporte Anthropic Messages. Modelos GPT, o-series e Gemini mantêm o transporte OpenAI Responses. O OpenClaw seleciona o transporte correto com base na ref do modelo.

Request compatibility

O OpenClaw envia cabeçalhos de solicitação no estilo da IDE do Copilot nos transportes do Copilot, incluindo turnos integrados de Compaction, resultado de ferramenta e acompanhamento de imagem. Ele não habilita continuação de Responses no nível do provedor para o Copilot, a menos que esse comportamento tenha sido verificado com a API do Copilot.

Environment variable resolution order

O OpenClaw resolve a autenticação do Copilot a partir de variáveis de ambiente na seguinte ordem de prioridade:

Prioridade | Variável | Observações  
---|---|---  
1 | `COPILOT_GITHUB_TOKEN` | Maior prioridade, específica do Copilot  
2 | `GH_TOKEN` | Token da GitHub CLI (fallback)  
3 | `GITHUB_TOKEN` | Token padrão do GitHub (menor prioridade)  
  
Quando várias variáveis estão definidas, o OpenClaw usa a de maior prioridade. O fluxo de login por dispositivo (`openclaw models auth login-github-copilot`) armazena seu token no armazenamento de perfis de autenticação e tem precedência sobre todas as variáveis de ambiente.

Token storage

O login armazena um token do GitHub no armazenamento de perfis de autenticação e o troca por um token da API do Copilot quando o OpenClaw é executado. Você não precisa gerenciar o token manualmente.

## Embeddings de busca de memória

O GitHub Copilot também pode servir como provedor de embeddings para [busca de memória](</pt-BR/concepts/memory-search>). Se você tem uma assinatura do Copilot e fez login, o OpenClaw pode usá-lo para embeddings sem uma chave de API separada.

### Detecção automática

Quando `memorySearch.provider` é `"auto"` (o padrão), o GitHub Copilot é tentado na prioridade 15 -- após embeddings locais, mas antes da OpenAI e outros provedores pagos. Se um token do GitHub estiver disponível, o OpenClaw descobre modelos de embeddings disponíveis a partir da API do Copilot e escolhe automaticamente o melhor.

### Configuração explícita

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "github-copilot",        // Optional: override the auto-discovered model        model: "text-embedding-3-small",      },    },  },}
[/code]

### Como funciona

  1. O OpenClaw resolve seu token do GitHub (a partir de env vars ou do perfil de autenticação).
  2. Troca-o por um token de API do Copilot de curta duração.
  3. Consulta o endpoint `/models` do Copilot para descobrir modelos de embeddings disponíveis.
  4. Escolhe o melhor modelo (prefere `text-embedding-3-small`).
  5. Envia solicitações de embedding para o endpoint `/embeddings` do Copilot.


A disponibilidade de modelos depende do seu plano do GitHub. Se nenhum modelo de embedding estiver disponível, o OpenClaw ignora o Copilot e tenta o próximo provedor.

## Relacionados

[**Model selection** Escolher provedores, refs de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**OAuth and auth** Detalhes de autenticação e regras de reutilização de credenciais. ](</pt-BR/gateway/authentication>)

Was this useful?YesNo