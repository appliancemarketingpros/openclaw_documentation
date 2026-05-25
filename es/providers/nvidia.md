---
title: NVIDIA
source_url: https://docs.openclaw.ai/es/providers/nvidia
scraped_at: 2026-05-25
---

NVIDIA proporciona una API compatible con OpenAI en `https://integrate.api.nvidia.com/v1` para modelos abiertos de forma gratuita. Autentícate con una clave de API de [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

## Primeros pasos

* ### Obtén tu clave de API

Crea una clave de API en [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

* ### Exporta la clave y ejecuta la incorporación

bashCopy code
[code]
    export NVIDIA_API_KEY="nvapi-..."openclaw onboard --auth-choice nvidia-api-key
[/code]

* ### Configura un modelo de NVIDIA

bashCopy code
[code]
    openclaw models set nvidia/nvidia/nemotron-3-super-120b-a12b
[/code]

Para una configuración no interactiva, también puedes pasar la clave directamente:

bashCopy code
[code]
    openclaw onboard --auth-choice nvidia-api-key --nvidia-api-key "nvapi-..."
[/code]

## Ejemplo de configuración

json5Copy code
[code]
    {  env: { NVIDIA_API_KEY: "nvapi-..." },  models: {    providers: {      nvidia: {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",      },    },  },  agents: {    defaults: {      model: { primary: "nvidia/nvidia/nemotron-3-super-120b-a12b" },    },  },}
[/code]

## Catálogo integrado

Referencia de modelo | Nombre | Contexto | Salida máxima  
---|---|---|---  
`nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Nemotron 3 Super 120B | 262,144 | 8,192  
`nvidia/moonshotai/kimi-k2.5` | Kimi K2.5 | 262,144 | 8,192  
`nvidia/minimaxai/minimax-m2.5` | Minimax M2.5 | 196,608 | 8,192  
`nvidia/z-ai/glm5` | GLM 5 | 202,752 | 8,192  
  
## Configuración avanzada

Comportamiento de activación automática

El proveedor se activa automáticamente cuando la variable de entorno `NVIDIA_API_KEY` está configurada. No se requiere configuración explícita del proveedor más allá de la clave.

Catálogo y precios

El catálogo incluido es estático. Los costos se establecen de forma predeterminada en `0` en el código fuente, ya que NVIDIA actualmente ofrece acceso gratuito a la API para los modelos listados.

Endpoint compatible con OpenAI

NVIDIA usa el endpoint estándar de finalizaciones `/v1`. Cualquier herramienta compatible con OpenAI debería funcionar de inmediato con la URL base de NVIDIA.

Respuestas lentas de proveedores personalizados

Algunos modelos personalizados alojados por NVIDIA pueden tardar más que el watchdog de inactividad predeterminado del modelo antes de emitir el primer fragmento de respuesta. Para entradas personalizadas del proveedor NVIDIA, aumenta el tiempo de espera del proveedor en lugar de aumentar el tiempo de espera de ejecución de todo el agente:

json5Copy code
[code]
    {  models: {    providers: {      "custom-integrate-api-nvidia-com": {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",        apiKey: "NVIDIA_API_KEY",        timeoutSeconds: 300,      },    },  },  agents: {    defaults: {      models: {        "custom-integrate-api-nvidia-com/meta/llama-3.1-70b-instruct": {          params: { thinking: "off" },        },      },    },  },}
[/code]

## Relacionado

[**Selección de modelos** Elegir proveedores, referencias de modelo y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Referencia de configuración** Referencia completa de configuración para agentes, modelos y proveedores. ](</es/gateway/configuration-reference>)

Was this useful?YesNo