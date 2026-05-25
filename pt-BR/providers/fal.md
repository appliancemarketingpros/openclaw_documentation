---
title: Fal
source_url: https://docs.openclaw.ai/pt-BR/providers/fal
scraped_at: 2026-05-25
---

OpenClaw inclui um provedor `fal` integrado para geração hospedada de imagens e vídeos.

Propriedade | Valor  
---|---  
Provedor | `fal`  
Autenticação | `FAL_KEY` (canônico; `FAL_API_KEY` também funciona como alternativa)  
API | endpoints de modelo fal  
  
## Primeiros passos

* ### Defina a chave de API

bashCopy code
[code]
    openclaw onboard --auth-choice fal-api-key
[/code]

* ### Defina um modelo de imagem padrão

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Geração de imagens

O provedor de geração de imagens `fal` integrado usa como padrão `fal/fal-ai/flux/dev`.

Capacidade | Valor  
---|---  
Máximo de imagens | 4 por solicitação  
Modo de edição | Flux: 1 imagem de referência; GPT Image 2: 10; Nano Banana 2: 14  
Substituições de tamanho | Compatível  
Proporção | Compatível para geração e edição com GPT Image 2/Nano Banana 2  
Resolução | Compatível  
Formato de saída | `png` ou `jpeg`  
  
Use `outputFormat: "png"` quando quiser saída em PNG. A fal não declara um controle explícito de fundo transparente no OpenClaw, portanto `background: "transparent"` é relatado como uma substituição ignorada para modelos fal.

Para usar a fal como provedora de imagens padrão:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Geração de vídeos

O provedor de geração de vídeos `fal` integrado usa como padrão `fal/fal-ai/minimax/video-01-live`.

Capacidade | Valor  
---|---  
Modos | Texto para vídeo, referência de imagem única, referência para vídeo Seedance  
Runtime | Fluxo de envio/status/resultado baseado em fila para trabalhos de longa duração  
  
Modelos de vídeo disponíveis

**HeyGen video-agent:**

  * `fal/fal-ai/heygen/v2/video-agent`


**Seedance 2.0:**

  * `fal/bytedance/seedance-2.0/fast/text-to-video`
  * `fal/bytedance/seedance-2.0/fast/image-to-video`
  * `fal/bytedance/seedance-2.0/fast/reference-to-video`
  * `fal/bytedance/seedance-2.0/text-to-video`
  * `fal/bytedance/seedance-2.0/image-to-video`
  * `fal/bytedance/seedance-2.0/reference-to-video`

Exemplo de configuração do Seedance 2.0 json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/text-to-video",      },    },  },}
[/code]

Exemplo de configuração de referência para vídeo do Seedance 2.0 json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/reference-to-video",      },    },  },}
[/code]

Referência para vídeo aceita até 9 imagens, 3 vídeos e 3 referências de áudio por meio dos parâmetros compartilhados `video_generate` `images`, `videos` e `audioRefs`, com no máximo 12 arquivos de referência no total.

Exemplo de configuração do HeyGen video-agent json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/fal-ai/heygen/v2/video-agent",      },    },  },}
[/code]

## Relacionados

[**Geração de imagens** Parâmetros compartilhados da ferramenta de imagem e seleção de provedor. ](</pt-BR/tools/image-generation>) [**Geração de vídeos** Parâmetros compartilhados da ferramenta de vídeo e seleção de provedor. ](</pt-BR/tools/video-generation>) [**Referência de configuração** Padrões do agente, incluindo seleção de modelos de imagem e vídeo. ](</pt-BR/gateway/config-agents#agent-defaults>)

Was this useful?YesNo