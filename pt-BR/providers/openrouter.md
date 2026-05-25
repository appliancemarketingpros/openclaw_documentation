---
title: OpenRouter
source_url: https://docs.openclaw.ai/pt-BR/providers/openrouter
scraped_at: 2026-05-25
---

OpenRouter fornece uma **API unificada** que roteia solicitações para muitos modelos por trás de um único endpoint e chave de API. Ela é compatível com OpenAI, então a maioria dos SDKs da OpenAI funciona alterando a URL base.

## Primeiros passos

* ### Obtenha sua chave de API

Crie uma chave de API em [openrouter.ai/keys](<https://openrouter.ai/keys>).

* ### Execute o onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice openrouter-api-key
[/code]

* ### (Opcional) Mude para um modelo específico

O onboarding usa `openrouter/auto` por padrão. Escolha um modelo concreto depois:

bashCopy code
[code]
    openclaw models set openrouter/<provider>/<model>
[/code]

## Exemplo de configuração

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      model: { primary: "openrouter/auto" },    },  },}
[/code]

## Referências de modelos

Exemplos de fallback incluídos:

Ref de modelo | Observações  
---|---  
`openrouter/auto` | Roteamento automático do OpenRouter  
`openrouter/moonshotai/kimi-k2.6` | Kimi K2.6 via MoonshotAI  
`openrouter/moonshotai/kimi-k2.5` | Kimi K2.5 via MoonshotAI  
  
## Geração de imagens

OpenRouter também pode servir como backend da ferramenta `image_generate`. Use um modelo de imagem do OpenRouter em `agents.defaults.imageGenerationModel`:

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      imageGenerationModel: {        primary: "openrouter/google/gemini-3.1-flash-image-preview",        timeoutMs: 180_000,      },    },  },}
[/code]

OpenClaw envia solicitações de imagem para a API de imagens de conclusões de chat do OpenRouter com `modalities: ["image", "text"]`. Modelos de imagem Gemini recebem dicas compatíveis de `aspectRatio` e `resolution` por meio do `image_config` do OpenRouter. Use `agents.defaults.imageGenerationModel.timeoutMs` para modelos de imagem mais lentos do OpenRouter; o parâmetro `timeoutMs` por chamada da ferramenta `image_generate` ainda tem prioridade.

## Geração de vídeo

OpenRouter também pode servir como backend da ferramenta `video_generate` por meio de sua API assíncrona `/videos`. Use um modelo de vídeo do OpenRouter em `agents.defaults.videoGenerationModel`:

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      videoGenerationModel: {        primary: "openrouter/google/veo-3.1-fast",      },    },  },}
[/code]

OpenClaw envia trabalhos de texto para vídeo e imagem para vídeo ao OpenRouter, consulta o `polling_url` retornado e baixa o vídeo concluído a partir dos `unsigned_urls` do OpenRouter ou do endpoint documentado de conteúdo do trabalho. Imagens de referência são enviadas como imagens de primeiro/último quadro por padrão; imagens marcadas com `reference_image` são enviadas como referências de entrada do OpenRouter. O padrão incluído `google/veo-3.1-fast` anuncia as durações atualmente compatíveis de 4/6/8 segundos, resoluções `720P`/`1080P` e proporções `16:9`/`9:16`. Vídeo para vídeo não é registrado para OpenRouter porque a API upstream de geração de vídeo atualmente aceita referências de texto e imagem.

## Texto para fala

OpenRouter também pode ser usado como provedor de TTS por meio de seu endpoint `/audio/speech` compatível com OpenAI.

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "openrouter",      providers: {        openrouter: {          model: "hexgrad/kokoro-82m",          voice: "af_alloy",          responseFormat: "mp3",        },      },    },  },}
[/code]

Se `messages.tts.providers.openrouter.apiKey` for omitido, o TTS reutiliza `models.providers.openrouter.apiKey` e depois `OPENROUTER_API_KEY`.

## Fala para texto (áudio de entrada)

OpenRouter pode transcrever anexos de voz/áudio de entrada por meio do caminho compartilhado `tools.media.audio` usando seu endpoint STT (`/audio/transcriptions`). Isso se aplica a qualquer Plugin de canal que encaminhe voz/áudio de entrada para o pré-processamento de entendimento de mídia.

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "openrouter", model: "openai/whisper-large-v3-turbo" }],      },    },  },}
[/code]

OpenClaw envia solicitações STT do OpenRouter como JSON com áudio em base64 em `input_audio` (contrato STT do OpenRouter), não como uploads multipart de formulário OpenAI.

## Autenticação e cabeçalhos

OpenRouter usa internamente um token Bearer com sua chave de API.

Em solicitações reais ao OpenRouter (`https://openrouter.ai/api/v1`), o OpenClaw também adiciona os cabeçalhos documentados de atribuição de aplicativo do OpenRouter:

Cabeçalho | Valor  
---|---  
`HTTP-Referer` | `https://openclaw.ai`  
`X-OpenRouter-Title` | `OpenClaw`  
`X-OpenRouter-Categories` | `cli-agent,cloud-agent,programming-app,creative-writing,writing-assistant,general-chat,personal-agent`  
  
## Configuração avançada

Cache de respostas

O cache de respostas do OpenRouter é opcional. Habilite-o por modelo OpenRouter com parâmetros de modelo:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openrouter/auto": {          params: {            responseCache: true,            responseCacheTtlSeconds: 300,          },        },      },    },  },}
[/code]

OpenClaw envia `X-OpenRouter-Cache: true` e, quando configurado, `X-OpenRouter-Cache-TTL`. `responseCacheClear: true` força uma atualização para a solicitação atual e armazena a resposta substituta. Aliases em snake_case (`response_cache`, `response_cache_ttl_seconds` e `response_cache_clear`) também são aceitos.

Isso é separado do cache de prompt do provedor e dos marcadores `cache_control` da Anthropic do OpenRouter. Ele é aplicado apenas em rotas `openrouter.ai` verificadas, não em URLs base de proxy personalizadas.

Marcadores de cache da Anthropic

Em rotas verificadas do OpenRouter, refs de modelos Anthropic mantêm os marcadores `cache_control` específicos da Anthropic do OpenRouter que o OpenClaw usa para melhor reutilização do cache de prompt em blocos de prompt de sistema/desenvolvedor.

Preenchimento prévio de reasoning da Anthropic

Em rotas verificadas do OpenRouter, refs de modelos Anthropic com reasoning habilitado removem turnos finais de preenchimento prévio do assistente antes que a solicitação chegue ao OpenRouter, correspondendo à exigência da Anthropic de que conversas com reasoning terminem com um turno de usuário.

Injeção de thinking / reasoning

Em rotas compatíveis que não sejam `auto`, o OpenClaw mapeia o nível de thinking selecionado para payloads de reasoning do proxy OpenRouter. Dicas de modelo sem suporte e `openrouter/auto` pulam essa injeção de reasoning. Hunter Alpha também pula reasoning de proxy para refs de modelo configuradas obsoletas porque o OpenRouter poderia retornar texto de resposta final em campos de reasoning para essa rota desativada.

Reprodução de reasoning do DeepSeek V4

Em rotas verificadas do OpenRouter, `openrouter/deepseek/deepseek-v4-flash` e `openrouter/deepseek/deepseek-v4-pro` preenchem `reasoning_content` ausente em turnos de assistente reproduzidos para que conversas com thinking/ferramentas mantenham o formato de acompanhamento exigido pelo DeepSeek V4. OpenClaw envia valores de `reasoning_effort` compatíveis com OpenRouter para essas rotas; `xhigh` é o nível mais alto anunciado, e substituições obsoletas de `max` são mapeadas para `xhigh`.

Formatação de solicitações somente OpenAI

OpenRouter ainda passa pelo caminho compatível com OpenAI em estilo proxy, então formatações de solicitação nativas apenas da OpenAI, como `serviceTier`, `store` de Responses, payloads de compatibilidade de reasoning da OpenAI e dicas de cache de prompt não são encaminhadas.

Rotas com backend Gemini

Refs OpenRouter com backend Gemini permanecem no caminho proxy-Gemini: o OpenClaw mantém a sanitização de assinatura de pensamento do Gemini ali, mas não habilita validação nativa de reprodução do Gemini nem reescritas de bootstrap.

Metadados de roteamento de provedor

Se você passar roteamento de provedor do OpenRouter em parâmetros de modelo, o OpenClaw o encaminha como metadados de roteamento do OpenRouter antes que os wrappers de stream compartilhados sejam executados.

## Relacionado

[**Seleção de modelo** Escolha de provedores, refs de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Referência de configuração** Referência completa de configuração para agentes, modelos e provedores. ](</pt-BR/gateway/configuration-reference>)

Was this useful?YesNo