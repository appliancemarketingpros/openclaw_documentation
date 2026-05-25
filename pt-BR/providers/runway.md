---
title: Pista
source_url: https://docs.openclaw.ai/pt-BR/providers/runway
scraped_at: 2026-05-25
---

OpenClaw inclui um provedor `runway` agrupado para geração de vídeo hospedada. O Plugin é habilitado por padrão e registra o provedor `runway` no contrato `videoGenerationProviders`.

Propriedade | Valor  
---|---  
ID do provedor | `runway`  
Plugin | agrupado, `enabledByDefault: true`  
Variáveis de ambiente auth | `RUNWAYML_API_SECRET` (canônica) ou `RUNWAY_API_KEY`  
Flag de onboarding | `--auth-choice runway-api-key`  
Flag direta da CLI | `--runway-api-key <key>`  
API | geração de vídeo baseada em tarefas da Runway (polling de `GET /v1/tasks/{id}`)  
Modelo padrão | `runway/gen4.5`  
  
## Primeiros passos

* ### Defina a chave da API

bashCopy code
[code]
    openclaw onboard --auth-choice runway-api-key
[/code]

* ### Defina Runway como o provedor de vídeo padrão

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "runway/gen4.5"
[/code]

* ### Gere um vídeo

Peça ao agente para gerar um vídeo. Runway será usado automaticamente.

## Modos e modelos compatíveis

O provedor expõe sete modelos da Runway divididos em três modos. O mesmo ID de modelo pode atender a mais de um modo (por exemplo, `gen4.5` funciona tanto para texto para vídeo quanto para imagem para vídeo).

Modo | Modelos | Entrada de referência  
---|---|---  
Texto para vídeo | `gen4.5` (padrão), `veo3.1`, `veo3.1_fast`, `veo3` | Nenhuma  
Imagem para vídeo | `gen4.5`, `gen4_turbo`, `gen3a_turbo`, `veo3.1`, `veo3.1_fast`, `veo3` | 1 imagem local ou remota  
Vídeo para vídeo | `gen4_aleph` | 1 vídeo local ou remoto  
  
Referências locais de imagem e vídeo são compatíveis via URIs de dados.

Proporções de tela | Valores permitidos  
---|---  
Texto para vídeo | `16:9`, `9:16`  
Edições de imagem e vídeo | `1:1`, `16:9`, `9:16`, `3:4`, `4:3`, `21:9`  
  
## Configuração

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "runway/gen4.5",      },    },  },}
[/code]

## Configuração avançada

Aliases de variáveis de ambiente

OpenClaw reconhece tanto `RUNWAYML_API_SECRET` (canônica) quanto `RUNWAY_API_KEY`. Qualquer uma das variáveis autenticará o provedor Runway.

Polling de tarefas

Runway usa uma API baseada em tarefas. Depois de enviar uma solicitação de geração, OpenClaw faz polling de `GET /v1/tasks/{id}` até que o vídeo esteja pronto. Nenhuma configuração adicional é necessária para o comportamento de polling.

## Relacionado

[**Geração de vídeo** Parâmetros de ferramenta compartilhados, seleção de provedor e comportamento assíncrono. ](</pt-BR/tools/video-generation>) [**Referência de configuração** Configurações padrão do agente, incluindo o modelo de geração de vídeo. ](</pt-BR/gateway/config-agents#agent-defaults>)

Was this useful?YesNo