---
title: Alibaba Model Studio
source_url: https://docs.openclaw.ai/pt-BR/providers/alibaba
scraped_at: 2026-05-25
---

OpenClaw inclui um plugin `alibaba` integrado que registra um provedor de geração de vídeo para modelos Wan no Alibaba Model Studio (o nome internacional do DashScope). O plugin é habilitado por padrão; você só precisa definir uma chave de API.

Propriedade | Valor  
---|---  
ID do provedor | `alibaba`  
Plugin | integrado, `enabledByDefault: true`  
Vars env de auth | `MODELSTUDIO_API_KEY` → `DASHSCOPE_API_KEY` → `QWEN_API_KEY` (a primeira correspondência vence)  
Flag de onboarding | `--auth-choice alibaba-model-studio-api-key`  
Flag direta da CLI | `--alibaba-model-studio-api-key <key>`  
Modelo padrão | `alibaba/wan2.6-t2v`  
URL base padrão | `https://dashscope-intl.aliyuncs.com`  
  
## Primeiros passos

* ### Defina uma chave de API

Use o onboarding para armazenar a chave no provedor `alibaba`:

bashCopy code
[code]
    openclaw onboard --auth-choice alibaba-model-studio-api-key
[/code]

Ou passe a chave diretamente durante a instalação/onboarding:

bashCopy code
[code]
    openclaw onboard --alibaba-model-studio-api-key <your-key>
[/code]

Ou exporte qualquer uma das vars env aceitas antes de iniciar o Gateway:

bashCopy code
[code]
    export MODELSTUDIO_API_KEY=sk-...# or DASHSCOPE_API_KEY=...# or QWEN_API_KEY=...
[/code]

* ### Defina um modelo de vídeo padrão

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "alibaba/wan2.6-t2v",      },    },  },}
[/code]

* ### Verifique se o provedor está configurado

bashCopy code
[code]
    openclaw models list --provider alibaba
[/code]

A lista deve incluir todos os cinco modelos Wan integrados. Se `MODELSTUDIO_API_KEY` não for resolvida, `openclaw models status --json` relata a credencial ausente em `auth.unusableProfiles`.

## Modelos Wan integrados

Ref. do modelo | Modo  
---|---  
`alibaba/wan2.6-t2v` | Texto para vídeo (padrão)  
`alibaba/wan2.6-i2v` | Imagem para vídeo  
`alibaba/wan2.6-r2v` | Referência para vídeo  
`alibaba/wan2.6-r2v-flash` | Referência para vídeo (rápido)  
`alibaba/wan2.7-r2v` | Referência para vídeo  
  
## Capacidades e limites

O provedor integrado espelha os limites da API de vídeo Wan do DashScope. Todos os três modos compartilham a mesma contagem de vídeos por solicitação e o mesmo limite de duração; apenas o formato da entrada difere.

Modo | Máx. vídeos de saída | Máx. imagens de entrada | Máx. vídeos de entrada | Duração máx. | Controles compatíveis  
---|---|---|---|---|---  
Texto para vídeo | 1 | n/a | n/a | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
Imagem para vídeo | 1 | 1 | n/a | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
Referência para vídeo | 1 | n/a | 4 | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
  
Quando uma solicitação omite `durationSeconds`, o provedor envia o padrão aceito pelo DashScope de **5 segundos**. Defina `durationSeconds` explicitamente na [ferramenta de geração de vídeo](</pt-BR/tools/video-generation>) para estender até 10 s.

## Configuração avançada

Substituir a URL base do DashScope

O provedor usa por padrão o endpoint internacional do DashScope. Para apontar para o endpoint da região da China, defina:

json5Copy code
[code]
    {  models: {    providers: {      alibaba: {        baseUrl: "https://dashscope.aliyuncs.com",      },    },  },}
[/code]

O provedor remove barras finais antes de construir URLs de tarefa AIGC.

Prioridade das vars env de auth

O OpenClaw resolve a chave de API da Alibaba a partir de variáveis de ambiente nesta ordem, usando o primeiro valor não vazio:

  1. `MODELSTUDIO_API_KEY`
  2. `DASHSCOPE_API_KEY`
  3. `QWEN_API_KEY`


Entradas configuradas em `auth.profiles` (definidas via `openclaw models auth login`) substituem a resolução por vars env. Consulte [Perfis de auth no FAQ de modelos](</pt-BR/help/faq-models#what-is-an-auth-profile>) para rotação de perfis, cooldown e mecânica de substituição.

Relação com o plugin Qwen

Ambos os plugins integrados se comunicam com o DashScope e aceitam chaves de API sobrepostas. Use:

  * IDs `alibaba/wan*.*` para acionar o provedor dedicado de vídeo Wan documentado nesta página.
  * IDs `qwen/*` para chat, embedding e entendimento de mídia do Qwen (consulte [Qwen](</pt-BR/providers/qwen>)).


Definir `MODELSTUDIO_API_KEY` uma vez autentica ambos os plugins porque a lista de vars env de auth se sobrepõe intencionalmente; você não precisa fazer onboarding de cada plugin separadamente.

## Relacionados

[**Geração de vídeo** Parâmetros compartilhados da ferramenta de vídeo e seleção de provedor. ](</pt-BR/tools/video-generation>) [**Qwen** Configuração de chat, embedding e entendimento de mídia do Qwen na mesma auth do DashScope. ](</pt-BR/providers/qwen>) [**Referência de configuração** Padrões do agente e configuração de modelos. ](</pt-BR/gateway/config-agents#agent-defaults>) [**FAQ de modelos** Perfis de auth, troca de modelos e resolução de erros "no profile". ](</pt-BR/help/faq-models>)

Was this useful?YesNo