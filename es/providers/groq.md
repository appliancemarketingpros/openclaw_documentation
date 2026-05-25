---
title: Groq
source_url: https://docs.openclaw.ai/es/providers/groq
scraped_at: 2026-05-25
---

[Groq](<https://groq.com>) proporciona inferencia ultrarrápida en modelos de pesos abiertos (Llama, Gemma, Kimi, Qwen, GPT OSS y más) mediante hardware LPU personalizado. OpenClaw incluye un Plugin de Groq integrado que registra tanto un proveedor de chat compatible con OpenAI como un proveedor de comprensión de medios de audio.

Propiedad | Valor  
---|---  
Id. de proveedor | `groq`  
Plugin | integrado, `enabledByDefault: true`  
Variable de entorno de autenticación | `GROQ_API_KEY`  
Indicador de incorporación | `--auth-choice groq-api-key`  
API | compatible con OpenAI (`openai-completions`)  
URL base | `https://api.groq.com/openai/v1`  
Transcripción de audio | `whisper-large-v3-turbo` (predeterminado)  
Valor predeterminado sugerido para chat | `groq/llama-3.3-70b-versatile`  
  
## Primeros pasos

* ### Obtén una clave de API

Crea una clave de API en [console.groq.com/keys](<https://console.groq.com/keys>).

* ### Configura la clave de API

IncorporaciónCopy code
[code]
    openclaw onboard --auth-choice groq-api-key
[/code]

Solo entornoCopy code
[code]
    export GROQ_API_KEY=gsk_...
[/code]

* ### Configura un modelo predeterminado

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

* ### Verifica que se pueda acceder al catálogo

bashCopy code
[code]
    openclaw models list --provider groq
[/code]

### Ejemplo de archivo de configuración

json5Copy code
[code]
    {  env: { GROQ_API_KEY: "gsk_..." },  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

## Catálogo integrado

OpenClaw incluye un catálogo de Groq respaldado por manifiesto con entradas tanto de razonamiento como sin razonamiento. Ejecuta `openclaw models list --provider groq` para ver las filas integradas de tu versión instalada, o consulta [console.groq.com/docs/models](<https://console.groq.com/docs/models>) para ver la lista oficial de Groq.

Ref. de modelo | Nombre | Razonamiento | Entrada | Contexto  
---|---|---|---|---  
`groq/llama-3.3-70b-versatile` | Llama 3.3 70B Versatile | no | texto | 131,072  
`groq/llama-3.1-8b-instant` | Llama 3.1 8B Instant | no | texto | 131,072  
`groq/meta-llama/llama-4-maverick-17b-128e-instruct` | Llama 4 Maverick 17B | no | texto + imagen | 131,072  
`groq/meta-llama/llama-4-scout-17b-16e-instruct` | Llama 4 Scout 17B | no | texto + imagen | 131,072  
`groq/llama3-70b-8192` | Llama 3 70B | no | texto | 8,192  
`groq/llama3-8b-8192` | Llama 3 8B | no | texto | 8,192  
`groq/gemma2-9b-it` | Gemma 2 9B | no | texto | 8,192  
`groq/mistral-saba-24b` | Mistral Saba 24B | no | texto | 32,768  
`groq/moonshotai/kimi-k2-instruct` | Kimi K2 Instruct | no | texto | 131,072  
`groq/moonshotai/kimi-k2-instruct-0905` | Kimi K2 Instruct 0905 | no | texto | 262,144  
`groq/openai/gpt-oss-120b` | GPT OSS 120B | sí | texto | 131,072  
`groq/openai/gpt-oss-20b` | GPT OSS 20B | sí | texto | 131,072  
`groq/openai/gpt-oss-safeguard-20b` | Safety GPT OSS 20B | sí | texto | 131,072  
`groq/qwen-qwq-32b` | Qwen QwQ 32B | sí | texto | 131,072  
`groq/qwen/qwen3-32b` | Qwen3 32B | sí | texto | 131,072  
`groq/deepseek-r1-distill-llama-70b` | DeepSeek R1 Distill Llama 70B | sí | texto | 131,072  
`groq/groq/compound` | Compound | sí | texto | 131,072  
`groq/groq/compound-mini` | Compound Mini | sí | texto | 131,072  
  
## Modelos de razonamiento

OpenClaw asigna sus niveles compartidos de `/think` a los valores `reasoning_effort` específicos del modelo de Groq:

  * Para `qwen/qwen3-32b`, el pensamiento desactivado envía `none` y el pensamiento activado envía `default`.
  * Para los modelos de razonamiento GPT OSS de Groq (`openai/gpt-oss-*`), OpenClaw envía `low`, `medium` o `high` según el nivel de `/think`. El pensamiento desactivado omite `reasoning_effort` porque esos modelos no admiten un valor desactivado.
  * DeepSeek R1 Distill, Qwen QwQ y Compound usan la superficie de razonamiento nativa de Groq; `/think` controla la visibilidad, pero el modelo siempre razona.


Consulta [Modos de pensamiento](</es/tools/thinking>) para conocer los niveles compartidos de `/think` y cómo OpenClaw los traduce por proveedor.

## Transcripción de audio

El Plugin integrado de Groq también registra un **proveedor de comprensión de medios de audio** para que los mensajes de voz se puedan transcribir mediante la superficie compartida `tools.media.audio`.

Propiedad | Valor  
---|---  
Ruta de configuración compartida | `tools.media.audio`  
URL base predeterminada | `https://api.groq.com/openai/v1`  
Modelo predeterminado | `whisper-large-v3-turbo`  
Prioridad automática | 20  
Endpoint de API | compatible con OpenAI `/audio/transcriptions`  
  
Para hacer que Groq sea el backend de audio predeterminado:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [{ provider: "groq" }],      },    },  },}
[/code]

Disponibilidad del entorno para el daemon

Si el Gateway se ejecuta como servicio administrado (launchd, systemd, Docker), `GROQ_API_KEY` debe ser visible para ese proceso, no solo para tu shell interactivo.

Ids. de modelo Groq personalizados

OpenClaw acepta cualquier id. de modelo de Groq en tiempo de ejecución. Usa el id. exacto que muestra Groq y antepónle el prefijo `groq/`. El catálogo integrado cubre los casos habituales; los ids. que no están en el catálogo pasan a la plantilla compatible con OpenAI predeterminada.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/<your-model-id>" },    },  },}
[/code]

## Relacionado

[**Proveedores de modelos** Elegir proveedores, refs. de modelos y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Modos de pensamiento** Niveles de esfuerzo de razonamiento e interacción con la política del proveedor. ](</es/tools/thinking>) [**Referencia de configuración** Esquema de configuración completo, incluidos los ajustes de proveedor y audio. ](</es/gateway/configuration-reference>) [**Consola de Groq** Panel de Groq, documentación de API y precios. ](<https://console.groq.com>)

Was this useful?YesNo