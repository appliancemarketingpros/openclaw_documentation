---
title: Vydra
source_url: https://docs.openclaw.ai/pt-BR/providers/vydra
scraped_at: 2026-05-25
---

O Plugin Vydra incluído adiciona:

  * Geração de imagens via `vydra/grok-imagine`
  * Geração de vídeos via `vydra/veo3` e `vydra/kling`
  * Síntese de fala via rota de TTS da Vydra baseada no ElevenLabs


OpenClaw usa a mesma `VYDRA_API_KEY` para as três capacidades.

Propriedade | Valor  
---|---  
ID do provedor | `vydra`  
Plugin | incluído, `enabledByDefault: true`  
Variável de ambiente de auth | `VYDRA_API_KEY`  
Flag de onboarding | `--auth-choice vydra-api-key`  
Flag direta da CLI | `--vydra-api-key <key>`  
Contratos | `imageGenerationProviders`, `videoGenerationProviders`, `speechProviders`  
URL base | `https://www.vydra.ai/api/v1` (use o host `www`)  
  
## Configuração

* ### Execute o onboarding interativo

bashCopy code
[code]
    openclaw onboard --auth-choice vydra-api-key
[/code]

Ou defina a variável de ambiente diretamente:

bashCopy code
[code]
    export VYDRA_API_KEY="vydra_live_..."
[/code]

* ### Escolha uma capacidade padrão

Escolha uma ou mais das capacidades abaixo (imagem, vídeo ou fala) e aplique a configuração correspondente.

## Capacidades

Geração de imagens

Modelo de imagem padrão:

  * `vydra/grok-imagine`


Defina-o como o provedor de imagem padrão:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "vydra/grok-imagine",      },    },  },}
[/code]

O suporte incluído atual é apenas de texto para imagem. As rotas de edição hospedadas da Vydra esperam URLs de imagem remotas, e o OpenClaw ainda não adiciona uma ponte de upload específica da Vydra no Plugin incluído.

Geração de vídeos

Modelos de vídeo registrados:

  * `vydra/veo3` para texto para vídeo
  * `vydra/kling` para imagem para vídeo


Defina a Vydra como o provedor de vídeo padrão:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "vydra/veo3",      },    },  },}
[/code]

Observações:

  * `vydra/veo3` é incluído apenas como texto para vídeo.
  * `vydra/kling` atualmente exige uma referência de URL de imagem remota. Uploads de arquivos locais são rejeitados de início.
  * A rota HTTP `kling` atual da Vydra tem sido inconsistente quanto a exigir `image_url` ou `video_url`; o provedor incluído mapeia a mesma URL de imagem remota para ambos os campos.
  * O Plugin incluído permanece conservador e não encaminha ajustes de estilo não documentados, como proporção, resolução, marca-d'água ou áudio gerado.

Testes live de vídeo

Cobertura live específica do provedor:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_VYDRA_VIDEO=1 \pnpm test:live -- extensions/vydra/vydra.live.test.ts
[/code]

O arquivo live da Vydra incluído agora cobre:

  * texto para vídeo com `vydra/veo3`
  * imagem para vídeo com `vydra/kling` usando uma URL de imagem remota


Substitua a fixture de imagem remota quando necessário:

bashCopy code
[code]
    export OPENCLAW_LIVE_VYDRA_KLING_IMAGE_URL="https://example.com/reference.png"
[/code]

Síntese de fala

Defina a Vydra como o provedor de fala:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "vydra",      providers: {        vydra: {          apiKey: "${VYDRA_API_KEY}",          voiceId: "21m00Tcm4TlvDq8ikWAM",        },      },    },  },}
[/code]

Padrões:

  * Modelo: `elevenlabs/tts`
  * ID da voz: `21m00Tcm4TlvDq8ikWAM`


O Plugin incluído atualmente expõe uma voz padrão comprovadamente funcional e retorna arquivos de áudio MP3.

## Relacionado

[**Diretório de provedores** Navegue por todos os provedores disponíveis. ](</pt-BR/providers>) [**Geração de imagens** Parâmetros compartilhados da ferramenta de imagem e seleção de provedor. ](</pt-BR/tools/image-generation>) [**Geração de vídeos** Parâmetros compartilhados da ferramenta de vídeo e seleção de provedor. ](</pt-BR/tools/video-generation>) [**Referência de configuração** Padrões de agentes e configuração de modelo. ](</pt-BR/gateway/config-agents#agent-defaults>)

Was this useful?YesNo