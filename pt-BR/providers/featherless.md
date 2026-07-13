---
title: Featherless AI
source_url: https://docs.openclaw.ai/pt-BR/providers/featherless
scraped_at: 2026-07-13
---

ModelsProviders

[Featherless AI](<https://featherless.ai>) disponibiliza modelos abertos por meio de uma API compatível com a OpenAI. O OpenClaw instala o Featherless como um Plugin oficial de provedor externo e mantém o catálogo integrado enxuto, ao mesmo tempo que aceita IDs exatos de modelos do Featherless em tempo de execução.

Propriedade | Valor  
---|---  
ID do provedor | `featherless`  
Pacote | `@openclaw/featherless-provider`  
Variável de ambiente de autenticação | `FEATHERLESS_API_KEY`  
Flag de integração inicial | `--auth-choice featherless-api-key`  
Flag direta da CLI | `--featherless-api-key <key>`  
API | Compatível com a OpenAI (`openai-completions`)  
URL base | `https://api.featherless.ai/v1`  
Modelo padrão | `featherless/Qwen/Qwen3-32B`  
  
## Configuração

Instale o Plugin e reinicie o Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/featherless-provideropenclaw gateway restart
[/code]

Execute a integração inicial:

bashCopy code
[code]
    openclaw onboard --auth-choice featherless-api-key
[/code]

Para uma configuração não interativa:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice featherless-api-key \  --featherless-api-key "$FEATHERLESS_API_KEY"
[/code]

Ou disponibilize a chave ao processo do Gateway:

bashCopy code
[code]
    export FEATHERLESS_API_KEY="<your-featherless-api-key>" # pragma: allowlist secret
[/code]

Verifique o provedor:

bashCopy code
[code]
    openclaw models list --provider featherless
[/code]

## Modelo padrão

O Plugin usa `Qwen/Qwen3-32B` como padrão de configuração porque o Featherless documenta chamadas nativas de ferramentas para a família Qwen 3. O OpenClaw configura sua janela de contexto de 32.768 tokens, um limite conservador de saída de 4.096 tokens e controles de raciocínio do modelo de chat do Qwen.

Os campos de custo do catálogo são zero porque o Featherless oferece vários modelos de cobrança, e o OpenClaw não incorpora taxas específicas do plano da conta nem preços por solicitação.

## Outros modelos do Featherless

Use o ID exato do modelo do Featherless após o prefixo de provedor `featherless/`:

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "featherless/moonshotai/Kimi-K2-Instruct",      },    },  },}
[/code]

O OpenClaw deliberadamente não copia o índice público completo de modelos do Featherless para o seletor. O índice é grande e não fornece metadados estruturados de recursos suficientes para classificar com segurança todos os modelos de texto, visão, embeddings e raciocínio. Portanto, IDs desconhecidos são resolvidos com padrões conservadores somente de texto e sem raciocínio: uma janela de contexto de 4.096 tokens e um limite de saída de 1.024 tokens.

Adicione uma entrada explícita de modelo do provedor quando um modelo precisar de metadados diferentes:

json5Copy code
[code]
    {  models: {    mode: "merge",    providers: {      featherless: {        baseUrl: "https://api.featherless.ai/v1",        apiKey: "${FEATHERLESS_API_KEY}",        api: "openai-completions",        models: [          {            id: "google/gemma-3-27b-it",            name: "Gemma 3 27B",            input: ["text", "image"],            reasoning: false,            contextWindow: 32768,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

Consulte o catálogo de modelos do Featherless para verificar a disponibilidade atual dos modelos e as etiquetas de recursos antes de adicionar metadados personalizados.

## Solução de problemas

  * `401` ou `403`: confirme se `FEATHERLESS_API_KEY` está visível para o processo do Gateway ou execute novamente a integração inicial.
  * Modelo desconhecido: use o ID exato, diferenciando maiúsculas de minúsculas, fornecido pelo Featherless após o prefixo `featherless/`.
  * Chamadas de ferramentas retornadas como texto: escolha uma família de modelos que o Featherless documente como compatível com chamadas nativas de funções, como a Qwen 3.
  * O Gateway gerenciado não consegue acessar a chave: coloque-a em `~/.openclaw/.env` ou em outra fonte de variáveis de ambiente carregada pelo serviço e reinicie o Gateway.


## Conteúdo relacionado

  * [Provedores de modelos](</pt-BR/concepts/model-providers>)
  * [Todos os provedores](</pt-BR/providers>)
  * [Modos de raciocínio](</pt-BR/tools/thinking>)


Was this useful?YesNo

Open issue