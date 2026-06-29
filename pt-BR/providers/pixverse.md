---
title: PixVerse
source_url: https://docs.openclaw.ai/pt-BR/providers/pixverse
scraped_at: 2026-06-29
---

ModelsProviders

O OpenClaw fornece `pixverse` como um Plugin externo oficial para geração de vídeo hospedada do PixVerse. O Plugin registra o provedor `pixverse` no contrato `videoGenerationProviders`.

Propriedade | Valor  
---|---  
ID do provedor | `pixverse`  
Pacote do Plugin | `@openclaw/pixverse-provider`  
Var. env. de auth | `PIXVERSE_API_KEY`  
Flag de onboarding | `--auth-choice pixverse-api-key`  
Flag direta da CLI | `--pixverse-api-key <key>`  
API | API PixVerse Platform v2 (envio de `video_id` mais polling de resultado)  
Modelo padrão | `pixverse/v6`  
Região padrão da API | Internacional  
  
## Primeiros passos

* ### Instale o Plugin

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/pixverse-provideropenclaw gateway restart
[/code]

* ### Defina a chave de API

bashCopy code
[code]
    openclaw onboard --auth-choice pixverse-api-key
[/code]

O assistente pergunta se deve usar o endpoint Internacional (`https://app-api.pixverse.ai/openapi/v2`) ou o endpoint CN (`https://app-api.pixverseai.cn/openapi/v2`) antes de gravar `region` e `baseUrl` na configuração do provedor.

* ### Defina o PixVerse como o provedor de vídeo padrão

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "pixverse/v6"
[/code]

* ### Gere um vídeo

Peça ao agente para gerar um vídeo. O PixVerse será usado automaticamente.

## Modos e modelos compatíveis

O provedor expõe modelos de geração do PixVerse por meio da ferramenta de vídeo compartilhada do OpenClaw.

Modo | Modelos | Entrada de referência  
---|---|---  
Texto para vídeo | `v6` (padrão), `c1` | Nenhuma  
Imagem para vídeo | `v6` (padrão), `c1` | 1 imagem local ou remota  
  
Referências de imagem locais são enviadas para o PixVerse antes da solicitação de imagem para vídeo. URLs de imagem remotas são repassadas pelo endpoint de upload de imagem do PixVerse como `image_url`.

Opção | Valores compatíveis  
---|---  
Duração | 1-15 segundos  
Resolução | `360P`, `540P`, `720P`, `1080P`  
Proporção | `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `2:3`, `3:2`, `21:9` para texto para vídeo  
Áudio gerado | `audio: true`  
  
## Opções do provedor

O provedor de vídeo aceita estas chaves opcionais específicas do provedor:

Opção | Tipo | Efeito  
---|---|---  
`seed` | number | Seed determinística quando compatível  
`negativePrompt` / `negative_prompt` | string | Prompt negativo  
`quality` | string | Qualidade do PixVerse, como `720p`  
`motionMode` / `motion_mode` | string | Modo de movimento de imagem para vídeo  
`cameraMovement` / `camera_movement` | string | Predefinição de movimento de câmera do PixVerse  
`templateId` / `template_id` | number | ID de template PixVerse ativado  
  
## Configuração

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "pixverse/v6",      },    },  },}
[/code]

## Configuração avançada

Região da API

O OpenClaw usa por padrão a API internacional do PixVerse. Defina `models.providers.pixverse.region` manualmente quando sua chave pertencer a uma região específica da plataforma PixVerse, ou use `openclaw onboard --auth-choice pixverse-api-key` para escolher uma no assistente de configuração:

Valor da região | URL base da API PixVerse  
---|---  
`international` | `https://app-api.pixverse.ai/openapi/v2`  
`cn` | `https://app-api.pixverseai.cn/openapi/v2`  
  
json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        region: "cn", // "international" or "cn"        baseUrl: "https://app-api.pixverseai.cn/openapi/v2",        models: [],      },    },  },}
[/code]

URL base personalizada

Defina `models.providers.pixverse.baseUrl` somente ao rotear por um proxy compatível confiável. `baseUrl` tem precedência sobre `region`.

json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        baseUrl: "https://app-api.pixverse.ai/openapi/v2",      },    },  },}
[/code]

Polling de tarefa

O PixVerse retorna um `video_id` da solicitação de geração. O OpenClaw faz polling de `/openapi/v2/video/result/{video_id}` até que a tarefa seja concluída com sucesso, falhe ou atinja o tempo limite.

## Relacionado

[**Geração de vídeo** Parâmetros da ferramenta compartilhada, seleção de provedor e comportamento assíncrono. ](</pt-BR/tools/video-generation>) [**Referência de configuração** Configurações padrão do agente, incluindo o modelo de geração de vídeo. ](</pt-BR/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue