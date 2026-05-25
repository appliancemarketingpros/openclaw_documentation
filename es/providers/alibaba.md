---
title: Alibaba Model Studio
source_url: https://docs.openclaw.ai/es/providers/alibaba
scraped_at: 2026-05-25
---

OpenClaw incluye un Plugin `alibaba` integrado que registra un proveedor de generación de video para los modelos Wan en Alibaba Model Studio (el nombre internacional de DashScope). El Plugin está habilitado de forma predeterminada; solo necesitas configurar una clave de API.

Propiedad | Valor  
---|---  
Id. del proveedor | `alibaba`  
Plugin | integrado, `enabledByDefault: true`  
Vars. env. de auth | `MODELSTUDIO_API_KEY` → `DASHSCOPE_API_KEY` → `QWEN_API_KEY` (gana la primera coincidencia)  
Flag de onboarding | `--auth-choice alibaba-model-studio-api-key`  
Flag directa de CLI | `--alibaba-model-studio-api-key <key>`  
Modelo predeterminado | `alibaba/wan2.6-t2v`  
URL base predeterminada | `https://dashscope-intl.aliyuncs.com`  
  
## Primeros pasos

* ### Configura una clave de API

Usa el onboarding para almacenar la clave en el proveedor `alibaba`:

bashCopy code
[code]
    openclaw onboard --auth-choice alibaba-model-studio-api-key
[/code]

O pasa la clave directamente durante la instalación/onboarding:

bashCopy code
[code]
    openclaw onboard --alibaba-model-studio-api-key <your-key>
[/code]

O exporta cualquiera de las variables de entorno aceptadas antes de iniciar el Gateway:

bashCopy code
[code]
    export MODELSTUDIO_API_KEY=sk-...# or DASHSCOPE_API_KEY=...# or QWEN_API_KEY=...
[/code]

* ### Configura un modelo de video predeterminado

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "alibaba/wan2.6-t2v",      },    },  },}
[/code]

* ### Verifica que el proveedor esté configurado

bashCopy code
[code]
    openclaw models list --provider alibaba
[/code]

La lista debe incluir los cinco modelos Wan integrados. Si `MODELSTUDIO_API_KEY` no se resuelve, `openclaw models status --json` informa la credencial faltante en `auth.unusableProfiles`.

## Modelos Wan integrados

Ref. de modelo | Modo  
---|---  
`alibaba/wan2.6-t2v` | Texto a video (predeterminado)  
`alibaba/wan2.6-i2v` | Imagen a video  
`alibaba/wan2.6-r2v` | Referencia a video  
`alibaba/wan2.6-r2v-flash` | Referencia a video (rápido)  
`alibaba/wan2.7-r2v` | Referencia a video  
  
## Capacidades y límites

El proveedor integrado replica los límites de la API de video Wan de DashScope. Los tres modos comparten el mismo límite de videos por solicitud y de duración; solo difiere la forma de la entrada.

Modo | Videos de salida máx. | Imágenes de entrada máx. | Videos de entrada máx. | Duración máx. | Controles admitidos  
---|---|---|---|---|---  
Texto a video | 1 | n/a | n/a | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
Imagen a video | 1 | 1 | n/a | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
Referencia a video | 1 | n/a | 4 | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
  
Cuando una solicitud omite `durationSeconds`, el proveedor envía el valor predeterminado aceptado por DashScope de **5 segundos**. Configura `durationSeconds` explícitamente en la [herramienta de generación de video](</es/tools/video-generation>) para ampliarlo hasta 10 s.

## Configuración avanzada

Sobrescribir la URL base de DashScope

El proveedor usa de forma predeterminada el endpoint internacional de DashScope. Para apuntar al endpoint de la región de China, configura:

json5Copy code
[code]
    {  models: {    providers: {      alibaba: {        baseUrl: "https://dashscope.aliyuncs.com",      },    },  },}
[/code]

El proveedor elimina las barras finales antes de construir las URL de tareas AIGC.

Prioridad de vars. env. de auth

OpenClaw resuelve la clave de API de Alibaba desde variables de entorno en este orden, tomando el primer valor no vacío:

  1. `MODELSTUDIO_API_KEY`
  2. `DASHSCOPE_API_KEY`
  3. `QWEN_API_KEY`


Las entradas configuradas en `auth.profiles` (establecidas mediante `openclaw models auth login`) sobrescriben la resolución de variables de entorno. Consulta [perfiles de auth en la FAQ de modelos](</es/help/faq-models#what-is-an-auth-profile>) para conocer la rotación de perfiles, el periodo de enfriamiento y la mecánica de sobrescritura.

Relación con el Plugin de Qwen

Ambos Plugins integrados se comunican con DashScope y aceptan claves de API superpuestas. Usa:

  * Identificadores `alibaba/wan*.*` para controlar el proveedor dedicado de video Wan documentado en esta página.
  * Identificadores `qwen/*` para chat, embeddings y comprensión multimedia de Qwen (consulta [Qwen](</es/providers/qwen>)).


Configurar `MODELSTUDIO_API_KEY` una vez autentica ambos Plugins porque la lista de variables de entorno de auth se superpone intencionadamente; no necesitas ejecutar el onboarding de cada Plugin por separado.

## Relacionado

[**Generación de video** Parámetros compartidos de la herramienta de video y selección de proveedor. ](</es/tools/video-generation>) [**Qwen** Configuración de chat, embeddings y comprensión multimedia de Qwen con la misma auth de DashScope. ](</es/providers/qwen>) [**Referencia de configuración** Valores predeterminados de agentes y configuración de modelos. ](</es/gateway/config-agents#agent-defaults>) [**FAQ de modelos** Perfiles de auth, cambio de modelos y resolución de errores "no profile". ](</es/help/faq-models>)

Was this useful?YesNo