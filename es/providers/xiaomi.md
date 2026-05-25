---
title: Xiaomi MiMo
source_url: https://docs.openclaw.ai/es/providers/xiaomi
scraped_at: 2026-05-25
---

Xiaomi MiMo es la plataforma de API para los modelos **MiMo**. OpenClaw incluye un Plugin `xiaomi` incluido que registra tanto un proveedor de chat compatible con OpenAI como un proveedor de voz (TTS) con la misma `XIAOMI_API_KEY`.

Propiedad | Valor  
---|---  
Id. de proveedor | `xiaomi`  
Plugin | incluido, `enabledByDefault: true`  
Variable de entorno de autenticación | `XIAOMI_API_KEY`  
Indicador de incorporación | `--auth-choice xiaomi-api-key`  
Indicador directo de CLI | `--xiaomi-api-key <key>`  
Contratos | finalizaciones de chat + `speechProviders`  
API | compatible con OpenAI (`openai-completions`)  
URL base | `https://api.xiaomimimo.com/v1`  
Modelo predeterminado | `xiaomi/mimo-v2-flash`  
TTS predeterminado | `mimo-v2.5-tts`, voz `mimo_default`  
  
## Primeros pasos

* ### Get an API key

Crea una clave de API en la [consola de Xiaomi MiMo](<https://platform.xiaomimimo.com/#/console/api-keys>).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key
[/code]

O pasa la clave directamente:

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key --xiaomi-api-key "$XIAOMI_API_KEY"
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider xiaomi
[/code]

## Catálogo integrado

Referencia de modelo | Entrada | Contexto | Salida máxima | Razonamiento | Notas  
---|---|---|---|---|---  
`xiaomi/mimo-v2-flash` | texto | 262,144 | 8,192 | No | Modelo predeterminado  
`xiaomi/mimo-v2-pro` | texto | 1,048,576 | 32,000 | Sí | Contexto grande  
`xiaomi/mimo-v2-omni` | texto, imagen | 262,144 | 32,000 | Sí | Multimodal  
  
## Texto a voz

El Plugin `xiaomi` incluido también registra Xiaomi MiMo como proveedor de voz para `messages.tts`. Llama al contrato de TTS de finalizaciones de chat de Xiaomi con el texto como un mensaje `assistant` y una guía de estilo opcional como mensaje `user`.

Propiedad | Valor  
---|---  
Id. de TTS | `xiaomi` (alias `mimo`)  
Autenticación | `XIAOMI_API_KEY`  
API | `POST /v1/chat/completions` con `audio`  
Predeterminado | `mimo-v2.5-tts`, voz `mimo_default`  
Salida | MP3 de forma predeterminada; WAV cuando se configura  
json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "xiaomi",      providers: {        xiaomi: {          apiKey: "xiaomi_api_key",          model: "mimo-v2.5-tts",          voice: "mimo_default",          format: "mp3",          style: "Bright, natural, conversational tone.",        },      },    },  },}
[/code]

Las voces integradas compatibles incluyen `mimo_default`, `default_zh`, `default_en`, `Mia`, `Chloe`, `Milo` y `Dean`. `mimo-v2-tts` es compatible con cuentas TTS de MiMo anteriores; el valor predeterminado usa el modelo TTS actual MiMo-V2.5. Para destinos de notas de voz como Feishu y Telegram, OpenClaw transcodifica la salida de Xiaomi a Opus de 48 kHz con `ffmpeg` antes de la entrega.

## Ejemplo de configuración

json5Copy code
[code]
    {  env: { XIAOMI_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "xiaomi/mimo-v2-flash" } } },  models: {    mode: "merge",    providers: {      xiaomi: {        baseUrl: "https://api.xiaomimimo.com/v1",        api: "openai-completions",        apiKey: "XIAOMI_API_KEY",        models: [          {            id: "mimo-v2-flash",            name: "Xiaomi MiMo V2 Flash",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 8192,          },          {            id: "mimo-v2-pro",            name: "Xiaomi MiMo V2 Pro",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 1048576,            maxTokens: 32000,          },          {            id: "mimo-v2-omni",            name: "Xiaomi MiMo V2 Omni",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Auto-injection behavior

El proveedor `xiaomi` se inyecta automáticamente cuando `XIAOMI_API_KEY` está configurada en tu entorno o existe un perfil de autenticación. No necesitas configurar manualmente el proveedor salvo que quieras sobrescribir los metadatos del modelo o la URL base.

Model details

  * **mimo-v2-flash** — ligero y rápido, ideal para tareas de texto de propósito general. Sin compatibilidad con razonamiento.
  * **mimo-v2-pro** — admite razonamiento con una ventana de contexto de 1M de tokens para cargas de trabajo con documentos largos.
  * **mimo-v2-omni** — modelo multimodal con razonamiento habilitado que acepta entradas tanto de texto como de imagen.

Troubleshooting

  * Si los modelos no aparecen, confirma que `XIAOMI_API_KEY` esté configurada y sea válida.
  * Cuando el Gateway se ejecuta como demonio, asegúrate de que la clave esté disponible para ese proceso (por ejemplo en `~/.openclaw/.env` o mediante `env.shellEnv`).


## Relacionado

[**Model selection** Elegir proveedores, referencias de modelo y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Configuration reference** Referencia completa de configuración de OpenClaw. ](</es/gateway/configuration-reference>) [**Xiaomi MiMo console** Panel de Xiaomi MiMo y gestión de claves de API. ](<https://platform.xiaomimimo.com>)

Was this useful?YesNo