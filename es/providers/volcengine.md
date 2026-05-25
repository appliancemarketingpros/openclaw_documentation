---
title: Volcengine (Doubao)
source_url: https://docs.openclaw.ai/es/providers/volcengine
scraped_at: 2026-05-25
---

El proveedor de Volcengine da acceso a modelos Doubao y a modelos de terceros alojados en Volcano Engine, con endpoints separados para cargas de trabajo generales y de programación. El mismo Plugin integrado también puede registrar Volcengine Speech como proveedor de TTS.

Detalle | Valor  
---|---  
Proveedores | `volcengine` (general + TTS) + `volcengine-plan` (programación)  
Autenticación del modelo | `VOLCANO_ENGINE_API_KEY`  
Autenticación de TTS | `VOLCENGINE_TTS_API_KEY` o `BYTEPLUS_SEED_SPEECH_API_KEY`  
API | Modelos compatibles con OpenAI, TTS de BytePlus Seed Speech  
  
## Primeros pasos

* ### Configura la clave de API

Ejecuta la incorporación interactiva:

bashCopy code
[code]
    openclaw onboard --auth-choice volcengine-api-key
[/code]

Esto registra los proveedores general (`volcengine`) y de programación (`volcengine-plan`) a partir de una sola clave de API.

* ### Configura un modelo predeterminado

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "volcengine-plan/ark-code-latest" },    },  },}
[/code]

* ### Verifica que el modelo esté disponible

bashCopy code
[code]
    openclaw models list --provider volcengineopenclaw models list --provider volcengine-plan
[/code]

## Proveedores y endpoints

Proveedor | Endpoint | Caso de uso  
---|---|---  
`volcengine` | `ark.cn-beijing.volces.com/api/v3` | Modelos generales  
`volcengine-plan` | `ark.cn-beijing.volces.com/api/coding/v3` | Modelos de programación  
  
## Catálogo integrado

### General (volcengine)

Referencia del modelo | Nombre | Entrada | Contexto  
---|---|---|---  
`volcengine/doubao-seed-1-8-251228` | Doubao Seed 1.8 | texto, imagen | 256,000  
`volcengine/doubao-seed-code-preview-251028` | doubao-seed-code-preview-251028 | texto, imagen | 256,000  
`volcengine/kimi-k2-5-260127` | Kimi K2.5 | texto, imagen | 256,000  
`volcengine/glm-4-7-251222` | GLM 4.7 | texto, imagen | 200,000  
`volcengine/deepseek-v3-2-251201` | DeepSeek V3.2 | texto, imagen | 128,000  
  
### Programación (volcengine-plan)

Referencia del modelo | Nombre | Entrada | Contexto  
---|---|---|---  
`volcengine-plan/ark-code-latest` | Ark Coding Plan | texto | 256,000  
`volcengine-plan/doubao-seed-code` | Doubao Seed Code | texto | 256,000  
`volcengine-plan/glm-4.7` | GLM 4.7 Coding | texto | 200,000  
`volcengine-plan/kimi-k2-thinking` | Kimi K2 Thinking | texto | 256,000  
`volcengine-plan/kimi-k2.5` | Kimi K2.5 Coding | texto | 256,000  
`volcengine-plan/doubao-seed-code-preview-251028` | Doubao Seed Code Preview | texto | 256,000  
  
## Conversión de texto a voz

Volcengine TTS usa la API HTTP de BytePlus Seed Speech y se configura por separado de la clave de API del modelo Doubao compatible con OpenAI. En la consola de BytePlus, abre Seed Speech > Settings > API Keys y copia la clave de API; luego configura:

bashCopy code
[code]
    export VOLCENGINE_TTS_API_KEY="byteplus_seed_speech_api_key"export VOLCENGINE_TTS_RESOURCE_ID="seed-tts-1.0"
[/code]

Luego actívalo en `openclaw.json`:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "volcengine",      providers: {        volcengine: {          apiKey: "byteplus_seed_speech_api_key",          voice: "en_female_anna_mars_bigtts",          speedRatio: 1.0,        },      },    },  },}
[/code]

Para destinos de notas de voz, OpenClaw solicita a Volcengine el formato nativo del proveedor `ogg_opus`. Para adjuntos de audio normales, solicita `mp3`. Los alias del proveedor `bytedance` y `doubao` también se resuelven al mismo proveedor de voz.

El id de recurso predeterminado es `seed-tts-1.0` porque eso es lo que BytePlus concede a las claves de API de Seed Speech recién creadas en el proyecto predeterminado. Si tu proyecto tiene habilitación de TTS 2.0, configura `VOLCENGINE_TTS_RESOURCE_ID=seed-tts-2.0`.

La autenticación heredada con AppID/token sigue siendo compatible para aplicaciones antiguas de la consola Speech:

bashCopy code
[code]
    export VOLCENGINE_TTS_APPID="speech_app_id"export VOLCENGINE_TTS_TOKEN="speech_access_token"export VOLCENGINE_TTS_CLUSTER="volcano_tts"
[/code]

## Configuración avanzada

Modelo predeterminado después de la incorporación

`openclaw onboard --auth-choice volcengine-api-key` actualmente configura `volcengine-plan/ark-code-latest` como modelo predeterminado mientras también registra el catálogo general `volcengine`.

Comportamiento de respaldo del selector de modelos

Durante la incorporación o la selección de modelos en la configuración, la opción de autenticación de Volcengine prioriza tanto las filas `volcengine/*` como `volcengine-plan/*`. Si esos modelos todavía no se han cargado, OpenClaw vuelve al catálogo sin filtrar en lugar de mostrar un selector vacío limitado al proveedor.

Variables de entorno para procesos daemon

Si el Gateway se ejecuta como daemon (launchd/systemd), asegúrate de que las variables de entorno del modelo y TTS, como `VOLCANO_ENGINE_API_KEY`, `VOLCENGINE_TTS_API_KEY`, `BYTEPLUS_SEED_SPEECH_API_KEY`, `VOLCENGINE_TTS_APPID` y `VOLCENGINE_TTS_TOKEN`, estén disponibles para ese proceso (por ejemplo, en `~/.openclaw/.env` o mediante `env.shellEnv`).

## Relacionado

[**Selección de modelos** Elegir proveedores, referencias de modelos y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Configuración** Referencia completa de configuración para agentes, modelos y proveedores. ](</es/gateway/configuration>) [**Solución de problemas** Problemas comunes y pasos de depuración. ](</es/help/troubleshooting>) [**Preguntas frecuentes** Preguntas frecuentes sobre la configuración de OpenClaw. ](</es/help/faq>)

Was this useful?YesNo