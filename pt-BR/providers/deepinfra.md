---
title: DeepInfra
source_url: https://docs.openclaw.ai/pt-BR/providers/deepinfra
scraped_at: 2026-05-25
---

DeepInfra fornece uma **API unificada** que encaminha solicitações para os modelos open source e de fronteira mais populares por trás de um único endpoint e chave de API. Ela é compatível com OpenAI, então a maioria dos SDKs da OpenAI funciona ao trocar a URL base.

## Como obter uma chave de API

  1. Acesse <https://deepinfra.com/>
  2. Faça login ou crie uma conta
  3. Navegue até Dashboard / Keys e gere uma nova chave de API ou use a criada automaticamente


## Configuração da CLI

bashCopy code
[code]
    openclaw onboard --deepinfra-api-key <key>
[/code]

Ou defina a variável de ambiente:

bashCopy code
[code]
    export DEEPINFRA_API_KEY="<your-deepinfra-api-key>" # pragma: allowlist secret
[/code]

## Trecho de configuração

json5Copy code
[code]
    {  env: { DEEPINFRA_API_KEY: "<your-deepinfra-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "deepinfra/deepseek-ai/DeepSeek-V3.2" },    },  },}
[/code]

## Superfícies do OpenClaw compatíveis

O Plugin incluído registra todas as superfícies DeepInfra que correspondem aos contratos atuais de provedores do OpenClaw:

Superfície | Modelo padrão | Configuração/ferramenta do OpenClaw  
---|---|---  
Chat / provedor de modelo | `deepseek-ai/DeepSeek-V3.2` | `agents.defaults.model`  
Geração/edição de imagens | `black-forest-labs/FLUX-1-schnell` | `image_generate`, `agents.defaults.imageGenerationModel`  
Compreensão de mídia | `moonshotai/Kimi-K2.5` para imagens | compreensão de imagens recebidas  
Fala para texto | `openai/whisper-large-v3-turbo` | transcrição de áudio recebido  
Texto para fala | `hexgrad/Kokoro-82M` | `messages.tts.provider: "deepinfra"`  
Geração de vídeo | `Pixverse/Pixverse-T2V` | `video_generate`, `agents.defaults.videoGenerationModel`  
Embeddings de memória | `BAAI/bge-m3` | `agents.defaults.memorySearch.provider: "deepinfra"`  
  
DeepInfra também expõe reclassificação, classificação, detecção de objetos e outros tipos de modelo nativos. Atualmente, o OpenClaw não tem contratos de provedor de primeira classe para essas categorias, então este Plugin ainda não as registra.

## Modelos disponíveis

O OpenClaw descobre dinamicamente os modelos DeepInfra disponíveis na inicialização. Use `/models deepinfra` para ver a lista completa de modelos disponíveis.

Qualquer modelo disponível em [DeepInfra.com](<https://deepinfra.com/>) pode ser usado com o prefixo `deepinfra/`:

CodeCopy code
[code]
    deepinfra/MiniMaxAI/MiniMax-M2.5deepinfra/deepseek-ai/DeepSeek-V3.2deepinfra/moonshotai/Kimi-K2.5deepinfra/zai-org/GLM-5.1...and many more
[/code]

## Observações

  * As referências de modelo são `deepinfra/<provider>/<model>` (por exemplo, `deepinfra/Qwen/Qwen3-Max`).
  * Modelo padrão: `deepinfra/deepseek-ai/DeepSeek-V3.2`
  * URL base: `https://api.deepinfra.com/v1/openai`
  * A geração de vídeo nativa usa `https://api.deepinfra.com/v1/inference/<model>`.


## Relacionado

  * [Provedores de modelo](</pt-BR/concepts/model-providers>)
  * [Todos os provedores](</pt-BR/providers>)


Was this useful?YesNo