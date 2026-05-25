---
title: Xiaomi MiMo
source_url: https://docs.openclaw.ai/pt-BR/providers/xiaomi
scraped_at: 2026-05-25
---

Xiaomi MiMo é a plataforma de API para os modelos **MiMo**. O OpenClaw inclui um Plugin `xiaomi` integrado que registra tanto um provedor de chat compatível com OpenAI quanto um provedor de fala (TTS) usando a mesma `XIAOMI_API_KEY`.

Propriedade | Valor  
---|---  
ID do provedor | `xiaomi`  
Plugin | integrado, `enabledByDefault: true`  
Variável de ambiente de autenticação | `XIAOMI_API_KEY`  
Flag de onboarding | `--auth-choice xiaomi-api-key`  
Flag direta da CLI | `--xiaomi-api-key <key>`  
Contratos | conclusões de chat + `speechProviders`  
API | compatível com OpenAI (`openai-completions`)  
URL base | `https://api.xiaomimimo.com/v1`  
Modelo padrão | `xiaomi/mimo-v2-flash`  
Padrão de TTS | `mimo-v2.5-tts`, voz `mimo_default`  
  
## Primeiros passos

* ### Obtenha uma chave de API

Crie uma chave de API no [console do Xiaomi MiMo](<https://platform.xiaomimimo.com/#/console/api-keys>).

* ### Execute o onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key
[/code]

Ou passe a chave diretamente:

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key --xiaomi-api-key "$XIAOMI_API_KEY"
[/code]

* ### Verifique se o modelo está disponível

bashCopy code
[code]
    openclaw models list --provider xiaomi
[/code]

## Catálogo integrado

Referência do modelo | Entrada | Contexto | Saída máxima | Raciocínio | Observações  
---|---|---|---|---|---  
`xiaomi/mimo-v2-flash` | texto | 262,144 | 8,192 | Não | Modelo padrão  
`xiaomi/mimo-v2-pro` | texto | 1,048,576 | 32,000 | Sim | Contexto grande  
`xiaomi/mimo-v2-omni` | texto, imagem | 262,144 | 32,000 | Sim | Multimodal  
  
## Texto para fala

O Plugin `xiaomi` integrado também registra o Xiaomi MiMo como provedor de fala para `messages.tts`. Ele chama o contrato TTS de conclusões de chat da Xiaomi com o texto como uma mensagem `assistant` e orientações de estilo opcionais como uma mensagem `user`.

Propriedade | Valor  
---|---  
ID de TTS | `xiaomi` (alias `mimo`)  
Autenticação | `XIAOMI_API_KEY`  
API | `POST /v1/chat/completions` com `audio`  
Padrão | `mimo-v2.5-tts`, voz `mimo_default`  
Saída | MP3 por padrão; WAV quando configurado  
json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "xiaomi",      providers: {        xiaomi: {          apiKey: "xiaomi_api_key",          model: "mimo-v2.5-tts",          voice: "mimo_default",          format: "mp3",          style: "Bright, natural, conversational tone.",        },      },    },  },}
[/code]

As vozes integradas compatíveis incluem `mimo_default`, `default_zh`, `default_en`, `Mia`, `Chloe`, `Milo` e `Dean`. `mimo-v2-tts` é compatível com contas TTS mais antigas do MiMo; o padrão usa o modelo TTS MiMo-V2.5 atual. Para destinos de notas de voz como Feishu e Telegram, o OpenClaw transcodifica a saída da Xiaomi para Opus a 48 kHz com `ffmpeg` antes da entrega.

## Exemplo de configuração

json5Copy code
[code]
    {  env: { XIAOMI_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "xiaomi/mimo-v2-flash" } } },  models: {    mode: "merge",    providers: {      xiaomi: {        baseUrl: "https://api.xiaomimimo.com/v1",        api: "openai-completions",        apiKey: "XIAOMI_API_KEY",        models: [          {            id: "mimo-v2-flash",            name: "Xiaomi MiMo V2 Flash",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 8192,          },          {            id: "mimo-v2-pro",            name: "Xiaomi MiMo V2 Pro",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 1048576,            maxTokens: 32000,          },          {            id: "mimo-v2-omni",            name: "Xiaomi MiMo V2 Omni",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Comportamento de injeção automática

O provedor `xiaomi` é injetado automaticamente quando `XIAOMI_API_KEY` está definida no seu ambiente ou quando existe um perfil de autenticação. Você não precisa configurar manualmente o provedor, a menos que queira substituir metadados de modelo ou a URL base.

Detalhes do modelo

  * **mimo-v2-flash** — leve e rápido, ideal para tarefas de texto de uso geral. Sem suporte a raciocínio.
  * **mimo-v2-pro** — oferece suporte a raciocínio com uma janela de contexto de 1M tokens para cargas de trabalho com documentos longos.
  * **mimo-v2-omni** — modelo multimodal com raciocínio habilitado que aceita entradas de texto e imagem.

Solução de problemas

  * Se os modelos não aparecerem, confirme que `XIAOMI_API_KEY` está definida e é válida.
  * Quando o Gateway é executado como daemon, garanta que a chave esteja disponível para esse processo (por exemplo, em `~/.openclaw/.env` ou via `env.shellEnv`).


## Relacionados

[**Seleção de modelo** Escolha de provedores, referências de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Referência de configuração** Referência completa de configuração do OpenClaw. ](</pt-BR/gateway/configuration-reference>) [**Console do Xiaomi MiMo** Painel do Xiaomi MiMo e gerenciamento de chaves de API. ](<https://platform.xiaomimimo.com>)

Was this useful?YesNo