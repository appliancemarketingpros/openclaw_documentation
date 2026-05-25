---
title: ComfyUI
source_url: https://docs.openclaw.ai/es/providers/comfy
scraped_at: 2026-05-25
---

OpenClaw incluye un plugin `comfy` integrado para ejecuciones de ComfyUI basadas en workflows. El plugin está completamente impulsado por workflows, por lo que OpenClaw no intenta mapear controles genéricos como `size`, `aspectRatio`, `resolution`, `durationSeconds` o controles de estilo TTS sobre tu grafo.

Propiedad | Detalle  
---|---  
Proveedor | `comfy`  
Modelos | `comfy/workflow`  
Superficies compartidas | `image_generate`, `video_generate`, `music_generate`  
Autenticación | Ninguna para ComfyUI local; `COMFY_API_KEY` o `COMFY_CLOUD_API_KEY` para Comfy Cloud  
API | ComfyUI `/prompt` / `/history` / `/view` y Comfy Cloud `/api/*`  
  
## Qué admite

  * Generación de imágenes a partir de un JSON de workflow
  * Edición de imágenes con 1 imagen de referencia subida
  * Generación de video a partir de un JSON de workflow
  * Generación de video con 1 imagen de referencia subida
  * Generación de música o audio mediante la herramienta compartida `music_generate`
  * Descarga de salida desde un nodo configurado o desde todos los nodos de salida coincidentes


## Primeros pasos

Elige entre ejecutar ComfyUI en tu propia máquina o usar Comfy Cloud.

### Local

**Ideal para:** ejecutar tu propia instancia de ComfyUI en tu máquina o red LAN.

* ### Inicia ComfyUI localmente

Asegúrate de que tu instancia local de ComfyUI esté en ejecución (usa `http://127.0.0.1:8188` por defecto).

* ### Prepara tu JSON de workflow

Exporta o crea un archivo JSON de workflow de ComfyUI. Toma nota de los ID de nodo del nodo de entrada del prompt y del nodo de salida del que quieres que OpenClaw lea.

* ### Configura el proveedor

Establece `mode: "local"` y apunta a tu archivo de workflow. Aquí tienes un ejemplo mínimo de imagen:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Establece el modelo predeterminado

Apunta OpenClaw al modelo `comfy/workflow` para la capacidad que configuraste:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Verifica

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

### Comfy Cloud

**Ideal para:** ejecutar workflows en Comfy Cloud sin administrar recursos locales de GPU.

* ### Obtén una API key

Regístrate en [comfy.org](<https://comfy.org>) y genera una API key desde el panel de tu cuenta.

* ### Establece la API key

Proporciona tu clave mediante uno de estos métodos:

bashCopy code
[code]
    # Variable de entorno (preferida)export COMFY_API_KEY="your-key" # Variable de entorno alternativaexport COMFY_CLOUD_API_KEY="your-key" # O en línea dentro de la configuraciónopenclaw config set plugins.entries.comfy.config.apiKey "your-key"
[/code]

* ### Prepara tu JSON de workflow

Exporta o crea un archivo JSON de workflow de ComfyUI. Toma nota de los ID de nodo del nodo de entrada del prompt y del nodo de salida.

* ### Configura el proveedor

Establece `mode: "cloud"` y apunta a tu archivo de workflow:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "cloud",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Establece el modelo predeterminado

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Verifica

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

## Configuración

Comfy admite ajustes compartidos de conexión de nivel superior además de secciones de workflow por capacidad (`image`, `video`, `music`):

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },          video: {            workflowPath: "./workflows/video-api.json",            promptNodeId: "12",            outputNodeId: "21",          },          music: {            workflowPath: "./workflows/music-api.json",            promptNodeId: "3",            outputNodeId: "18",          },        },      },    },  },}
[/code]

### Claves compartidas

Clave | Tipo | Descripción  
---|---|---  
`mode` | `"local"` o `"cloud"` | Modo de conexión.  
`baseUrl` | string | Usa `http://127.0.0.1:8188` por defecto para local o `https://cloud.comfy.org` para cloud.  
`apiKey` | string | Clave en línea opcional, alternativa a las variables de entorno `COMFY_API_KEY` / `COMFY_CLOUD_API_KEY`.  
`allowPrivateNetwork` | boolean | Permite un `baseUrl` privado/LAN en modo cloud.  
  
### Claves por capacidad

Estas claves se aplican dentro de las secciones `image`, `video` o `music`:

Clave | Obligatoria | Predeterminado | Descripción  
---|---|---|---  
`workflow` o `workflowPath` | Sí | \-- | Ruta al archivo JSON del workflow de ComfyUI.  
`promptNodeId` | Sí | \-- | ID del nodo que recibe el prompt de texto.  
`promptInputName` | No | `"text"` | Nombre de entrada en el nodo del prompt.  
`outputNodeId` | No | \-- | ID del nodo del que leer la salida. Si se omite, se usan todos los nodos de salida coincidentes.  
`pollIntervalMs` | No | \-- | Intervalo de sondeo en milisegundos para la finalización del trabajo.  
`timeoutMs` | No | \-- | Tiempo de espera en milisegundos para la ejecución del workflow.  
  
Las secciones `image` y `video` también admiten:

Clave | Obligatoria | Predeterminado | Descripción  
---|---|---|---  
`inputImageNodeId` | Sí (cuando se pasa una imagen de referencia) | \-- | ID del nodo que recibe la imagen de referencia subida.  
`inputImageInputName` | No | `"image"` | Nombre de entrada en el nodo de imagen.  
  
## Detalles del workflow

Workflows de imagen

Establece el modelo de imagen predeterminado en `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

**Ejemplo de edición con imagen de referencia:**

Para habilitar la edición de imágenes con una imagen de referencia subida, añade `inputImageNodeId` a tu configuración de imagen:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          image: {            workflowPath: "./workflows/edit-api.json",            promptNodeId: "6",            inputImageNodeId: "7",            inputImageInputName: "image",            outputNodeId: "9",          },        },      },    },  },}
[/code]

Workflows de video

Establece el modelo de video predeterminado en `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

Los workflows de video de Comfy admiten texto a video e imagen a video mediante el grafo configurado.

Workflows de música

El plugin integrado registra un proveedor de generación de música para salidas de audio o música definidas por workflow, expuesto a través de la herramienta compartida `music_generate`:

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

Usa la sección de configuración `music` para apuntar al JSON de tu workflow de audio y al nodo de salida.

Compatibilidad con versiones anteriores

La configuración de imagen existente de nivel superior (sin la sección `image` anidada) sigue funcionando:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          workflowPath: "./workflows/flux-api.json",          promptNodeId: "6",          outputNodeId: "9",        },      },    },  },}
[/code]

OpenClaw trata esa estructura heredada como la configuración del workflow de imagen. No necesitas migrar de inmediato, pero se recomiendan las secciones anidadas `image` / `video` / `music` para configuraciones nuevas.

Pruebas en vivo

Existe cobertura en vivo opcional para el plugin integrado:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

La prueba en vivo omite casos individuales de imagen, video o música a menos que la sección correspondiente del workflow de Comfy esté configurada.

## Relacionado

[**Generación de imágenes** Configuración y uso de la herramienta de generación de imágenes. ](</es/tools/image-generation>) [**Generación de video** Configuración y uso de la herramienta de generación de video. ](</es/tools/video-generation>) [**Generación de música** Configuración de la herramienta de generación de música y audio. ](</es/tools/music-generation>) [**Directorio de proveedores** Resumen de todos los proveedores y referencias de modelos. ](</es/providers>) [**Referencia de configuración** Referencia completa de configuración, incluidos los valores predeterminados del agente. ](</es/gateway/config-agents#agent-defaults>)

Was this useful?YesNo