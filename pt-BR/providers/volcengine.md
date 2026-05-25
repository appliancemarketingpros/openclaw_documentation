---
title: Volcengine (Doubao)
source_url: https://docs.openclaw.ai/pt-BR/providers/volcengine
scraped_at: 2026-05-25
---

O provedor Volcengine dá acesso aos modelos Doubao e a modelos de terceiros hospedados no Volcano Engine, com endpoints separados para cargas de trabalho gerais e de programação. O mesmo Plugin incluído também pode registrar o Volcengine Speech como provedor de TTS.

Detalhe | Valor  
---|---  
Provedores | `volcengine` (geral + TTS) + `volcengine-plan` (programação)  
Autenticação do modelo | `VOLCANO_ENGINE_API_KEY`  
Autenticação de TTS | `VOLCENGINE_TTS_API_KEY` ou `BYTEPLUS_SEED_SPEECH_API_KEY`  
API | Modelos compatíveis com OpenAI, BytePlus Seed Speech TTS  
  
## Primeiros passos

* ### Defina a chave de API

Execute a configuração interativa:

bashCopy code
[code]
    openclaw onboard --auth-choice volcengine-api-key
[/code]

Isso registra os provedores geral (`volcengine`) e de programação (`volcengine-plan`) a partir de uma única chave de API.

* ### Defina um modelo padrão

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "volcengine-plan/ark-code-latest" },    },  },}
[/code]

* ### Verifique se o modelo está disponível

bashCopy code
[code]
    openclaw models list --provider volcengineopenclaw models list --provider volcengine-plan
[/code]

## Provedores e endpoints

Provedor | Endpoint | Caso de uso  
---|---|---  
`volcengine` | `ark.cn-beijing.volces.com/api/v3` | Modelos gerais  
`volcengine-plan` | `ark.cn-beijing.volces.com/api/coding/v3` | Modelos de programação  
  
## Catálogo integrado

### Geral (volcengine)

Ref. do modelo | Nome | Entrada | Contexto  
---|---|---|---  
`volcengine/doubao-seed-1-8-251228` | Doubao Seed 1.8 | texto, imagem | 256.000  
`volcengine/doubao-seed-code-preview-251028` | doubao-seed-code-preview-251028 | texto, imagem | 256.000  
`volcengine/kimi-k2-5-260127` | Kimi K2.5 | texto, imagem | 256.000  
`volcengine/glm-4-7-251222` | GLM 4.7 | texto, imagem | 200.000  
`volcengine/deepseek-v3-2-251201` | DeepSeek V3.2 | texto, imagem | 128.000  
  
### Programação (volcengine-plan)

Ref. do modelo | Nome | Entrada | Contexto  
---|---|---|---  
`volcengine-plan/ark-code-latest` | Ark Coding Plan | texto | 256.000  
`volcengine-plan/doubao-seed-code` | Doubao Seed Code | texto | 256.000  
`volcengine-plan/glm-4.7` | GLM 4.7 Coding | texto | 200.000  
`volcengine-plan/kimi-k2-thinking` | Kimi K2 Thinking | texto | 256.000  
`volcengine-plan/kimi-k2.5` | Kimi K2.5 Coding | texto | 256.000  
`volcengine-plan/doubao-seed-code-preview-251028` | Doubao Seed Code Preview | texto | 256.000  
  
## Conversão de texto em fala

O TTS do Volcengine usa a API HTTP BytePlus Seed Speech e é configurado separadamente da chave de API do modelo Doubao compatível com OpenAI. No console do BytePlus, abra Seed Speech > Settings > API Keys e copie a chave de API; em seguida, defina:

bashCopy code
[code]
    export VOLCENGINE_TTS_API_KEY="byteplus_seed_speech_api_key"export VOLCENGINE_TTS_RESOURCE_ID="seed-tts-1.0"
[/code]

Em seguida, habilite-o em `openclaw.json`:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "volcengine",      providers: {        volcengine: {          apiKey: "byteplus_seed_speech_api_key",          voice: "en_female_anna_mars_bigtts",          speedRatio: 1.0,        },      },    },  },}
[/code]

Para destinos de nota de voz, o OpenClaw solicita ao Volcengine o formato nativo do provedor `ogg_opus`. Para anexos de áudio normais, solicita `mp3`. Os aliases de provedor `bytedance` e `doubao` também resolvem para o mesmo provedor de fala.

O resource id padrão é `seed-tts-1.0` porque é isso que o BytePlus concede a chaves de API Seed Speech recém-criadas no projeto padrão. Se o seu projeto tiver direito ao TTS 2.0, defina `VOLCENGINE_TTS_RESOURCE_ID=seed-tts-2.0`.

A autenticação legada com AppID/token continua com suporte para aplicações mais antigas do Speech Console:

bashCopy code
[code]
    export VOLCENGINE_TTS_APPID="speech_app_id"export VOLCENGINE_TTS_TOKEN="speech_access_token"export VOLCENGINE_TTS_CLUSTER="volcano_tts"
[/code]

## Configuração avançada

Modelo padrão após a configuração inicial

`openclaw onboard --auth-choice volcengine-api-key` atualmente define `volcengine-plan/ark-code-latest` como o modelo padrão, enquanto também registra o catálogo geral `volcengine`.

Comportamento de fallback do seletor de modelo

Durante a configuração inicial/configuração da seleção de modelo, a opção de autenticação do Volcengine prioriza linhas `volcengine/*` e `volcengine-plan/*`. Se esses modelos ainda não tiverem sido carregados, o OpenClaw recorre ao catálogo sem filtro em vez de mostrar um seletor restrito ao provedor vazio.

Variáveis de ambiente para processos daemon

Se o Gateway for executado como daemon (launchd/systemd), certifique-se de que as variáveis de ambiente do modelo e do TTS, como `VOLCANO_ENGINE_API_KEY`, `VOLCENGINE_TTS_API_KEY`, `BYTEPLUS_SEED_SPEECH_API_KEY`, `VOLCENGINE_TTS_APPID` e `VOLCENGINE_TTS_TOKEN`, estejam disponíveis para esse processo (por exemplo, em `~/.openclaw/.env` ou via `env.shellEnv`).

## Relacionado

[**Seleção de modelo** Escolha de provedores, refs. de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Configuração** Referência completa de configuração para agentes, modelos e provedores. ](</pt-BR/gateway/configuration>) [**Solução de problemas** Problemas comuns e etapas de depuração. ](</pt-BR/help/troubleshooting>) [**FAQ** Perguntas frequentes sobre a configuração do OpenClaw. ](</pt-BR/help/faq>)

Was this useful?YesNo