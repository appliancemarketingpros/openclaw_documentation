---
title: Qwen
source_url: https://docs.openclaw.ai/es/providers/qwen
scraped_at: 2026-05-25
---

OpenClaw ahora trata a Qwen como un proveedor incluido de primera clase con el id canónico `qwen`. El proveedor incluido apunta a los endpoints de Qwen Cloud / Alibaba DashScope y Coding Plan, y mantiene los ids heredados de `modelstudio` funcionando como un alias de compatibilidad.

  * Proveedor: `qwen`
  * Variable de entorno preferida: `QWEN_API_KEY`
  * También aceptadas por compatibilidad: `MODELSTUDIO_API_KEY`, `DASHSCOPE_API_KEY`
  * Estilo de API: compatible con OpenAI


## Primeros pasos

Elige tu tipo de plan y sigue los pasos de configuración.

### Coding Plan (suscripción)

**Mejor para:** acceso basado en suscripción mediante el Qwen Coding Plan.

* ### Obtén tu clave de API

Crea o copia una clave de API desde [home.qwencloud.com/api-keys](<https://home.qwencloud.com/api-keys>).

* ### Ejecuta la incorporación

Para el endpoint **Global** :

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-api-key
[/code]

Para el endpoint **China** :

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-api-key-cn
[/code]

* ### Establece un modelo predeterminado

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "qwen/qwen3.5-plus" },    },  },}
[/code]

* ### Verifica que el modelo esté disponible

bashCopy code
[code]
    openclaw models list --provider qwen
[/code]

### Standard (pago por uso)

**Mejor para:** acceso de pago por uso mediante el endpoint Standard Model Studio, incluidos modelos como `qwen3.6-plus` que quizá no estén disponibles en el Coding Plan.

* ### Obtén tu clave de API

Crea o copia una clave de API desde [home.qwencloud.com/api-keys](<https://home.qwencloud.com/api-keys>).

* ### Ejecuta la incorporación

Para el endpoint **Global** :

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key
[/code]

Para el endpoint **China** :

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key-cn
[/code]

* ### Establece un modelo predeterminado

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "qwen/qwen3.5-plus" },    },  },}
[/code]

* ### Verifica que el modelo esté disponible

bashCopy code
[code]
    openclaw models list --provider qwen
[/code]

## Tipos de plan y endpoints

Plan | Región | Opción de autenticación | Endpoint  
---|---|---|---  
Standard (pago por uso) | China | `qwen-standard-api-key-cn` | `dashscope.aliyuncs.com/compatible-mode/v1`  
Standard (pago por uso) | Global | `qwen-standard-api-key` | `dashscope-intl.aliyuncs.com/compatible-mode/v1`  
Coding Plan (suscripción) | China | `qwen-api-key-cn` | `coding.dashscope.aliyuncs.com/v1`  
Coding Plan (suscripción) | Global | `qwen-api-key` | `coding-intl.dashscope.aliyuncs.com/v1`  
  
El proveedor selecciona automáticamente el endpoint según tu opción de autenticación. Las opciones canónicas usan la familia `qwen-*`; `modelstudio-*` queda solo para compatibilidad. Puedes sobrescribirlo con un `baseUrl` personalizado en la configuración.

## Catálogo integrado

OpenClaw actualmente incluye este catálogo Qwen incluido. El catálogo configurado es consciente del endpoint: las configuraciones de Coding Plan omiten modelos que solo se sabe que funcionan en el endpoint Standard.

Referencia de modelo | Entrada | Contexto | Notas  
---|---|---|---  
`qwen/qwen3.5-plus` | texto, imagen | 1,000,000 | Modelo predeterminado  
`qwen/qwen3.6-plus` | texto, imagen | 1,000,000 | Prefiere endpoints Standard cuando necesites este modelo  
`qwen/qwen3-max-2026-01-23` | texto | 262,144 | Línea Qwen Max  
`qwen/qwen3-coder-next` | texto | 262,144 | Coding  
`qwen/qwen3-coder-plus` | texto | 1,000,000 | Coding  
`qwen/MiniMax-M2.5` | texto | 1,000,000 | Razonamiento habilitado  
`qwen/glm-5` | texto | 202,752 | GLM  
`qwen/glm-4.7` | texto | 202,752 | GLM  
`qwen/kimi-k2.5` | texto, imagen | 262,144 | Moonshot AI mediante Alibaba  
  
## Controles de pensamiento

Para los modelos de Qwen Cloud con razonamiento habilitado, el proveedor incluido asigna los niveles de pensamiento de OpenClaw al indicador de solicitud de nivel superior `enable_thinking` de DashScope. El pensamiento deshabilitado envía `enable_thinking: false`; los demás niveles de pensamiento envían `enable_thinking: true`.

## Complementos multimodales

El Plugin `qwen` también expone capacidades multimodales en los endpoints DashScope **Standard** (no en los endpoints de Coding Plan):

  * **Comprensión de video** mediante `qwen-vl-max-latest`
  * **Generación de video Wan** mediante `wan2.6-t2v` (predeterminado), `wan2.6-i2v`, `wan2.6-r2v`, `wan2.6-r2v-flash`, `wan2.7-r2v`


Para usar Qwen como proveedor de video predeterminado:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: { primary: "qwen/wan2.6-t2v" },    },  },}
[/code]

## Configuración avanzada

Comprensión de imágenes y video

El Plugin Qwen incluido registra comprensión multimedia para imágenes y video en los endpoints DashScope **Standard** (no en los endpoints de Coding Plan).

Propiedad | Valor  
---|---  
Modelo | `qwen-vl-max-latest`  
Entrada compatible | Imágenes, video  
  
La comprensión multimedia se resuelve automáticamente desde la autenticación de Qwen configurada; no se necesita configuración adicional. Asegúrate de usar un endpoint Standard (pago por uso) para el soporte de comprensión multimedia.

Disponibilidad de Qwen 3.6 Plus

`qwen3.6-plus` está disponible en los endpoints Standard (pago por uso) de Model Studio:

  * China: `dashscope.aliyuncs.com/compatible-mode/v1`
  * Global: `dashscope-intl.aliyuncs.com/compatible-mode/v1`


Si los endpoints de Coding Plan devuelven un error de "modelo no compatible" para `qwen3.6-plus`, cambia a Standard (pago por uso) en lugar del par endpoint/clave de Coding Plan.

El catálogo Qwen incluido de OpenClaw no anuncia `qwen3.6-plus` en endpoints de Coding Plan, pero las entradas `qwen/qwen3.6-plus` configuradas explícitamente bajo `models.providers.qwen.models` se respetan en baseUrls de Coding Plan para que puedas habilitar ese modelo si Aliyun lo activa en tu suscripción. La API upstream sigue decidiendo si la llamada se realiza correctamente.

Plan de capacidades

El Plugin `qwen` se está posicionando como el hogar del proveedor para toda la superficie de Qwen Cloud, no solo para modelos de codificación/texto.

  * **Modelos de texto/chat:** incluidos ahora
  * **Llamadas a herramientas, salida estructurada, pensamiento:** heredados del transporte compatible con OpenAI
  * **Generación de imágenes:** planificada en la capa de Plugin de proveedor
  * **Comprensión de imágenes/video:** incluida ahora en el endpoint Standard
  * **Voz/audio:** planificada en la capa de Plugin de proveedor
  * **Embeddings/reordenamiento de memoria:** planificado mediante la superficie del adaptador de embeddings
  * **Generación de video:** incluida ahora mediante la capacidad compartida de generación de video

Detalles de generación de video

Para la generación de video, OpenClaw asigna la región Qwen configurada al host AIGC de DashScope correspondiente antes de enviar el trabajo:

  * Global/Intl: `https://dashscope-intl.aliyuncs.com`
  * China: `https://dashscope.aliyuncs.com`


Eso significa que un `models.providers.qwen.baseUrl` normal que apunte a los hosts Qwen de Coding Plan o Standard todavía mantiene la generación de video en el endpoint de video regional correcto de DashScope.

Límites actuales incluidos para generación de video con Qwen:

  * Hasta **1** video de salida por solicitud
  * Hasta **1** imagen de entrada
  * Hasta **4** videos de entrada
  * Hasta **10 segundos** de duración
  * Admite `size`, `aspectRatio`, `resolution`, `audio` y `watermark`
  * El modo de imagen/video de referencia actualmente requiere **URL http(s) remotas**. Las rutas de archivos locales se rechazan de entrada porque el endpoint de video de DashScope no acepta búferes locales subidos para esas referencias.

Compatibilidad de uso en streaming

Los endpoints nativos de Model Studio anuncian compatibilidad de uso en streaming en el transporte compartido `openai-completions`. OpenClaw ahora se basa en las capacidades del endpoint, por lo que los ids de proveedor personalizados compatibles con DashScope que apunten a los mismos hosts nativos heredan el mismo comportamiento de uso en streaming en lugar de requerir específicamente el id del proveedor integrado `qwen`.

La compatibilidad de uso con streaming nativo se aplica tanto a los hosts de Coding Plan como a los hosts compatibles con Standard DashScope:

  * `https://coding.dashscope.aliyuncs.com/v1`
  * `https://coding-intl.dashscope.aliyuncs.com/v1`
  * `https://dashscope.aliyuncs.com/compatible-mode/v1`
  * `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`

Regiones de endpoints multimodales

Las superficies multimodales (comprensión de video y generación de video Wan) usan los endpoints DashScope **Standard** , no los endpoints de Coding Plan:

  * URL base Global/Intl Standard: `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`
  * URL base China Standard: `https://dashscope.aliyuncs.com/compatible-mode/v1`

Configuración del entorno y del daemon

Si el Gateway se ejecuta como daemon (launchd/systemd), asegúrate de que `QWEN_API_KEY` esté disponible para ese proceso (por ejemplo, en `~/.openclaw/.env` o mediante `env.shellEnv`).

## Relacionado

[**Selección de modelos** Elección de proveedores, referencias de modelos y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Generación de video** Parámetros compartidos de la herramienta de video y selección de proveedores. ](</es/tools/video-generation>) [**Alibaba (ModelStudio)** Proveedor heredado de ModelStudio y notas de migración. ](</es/providers/alibaba>) [**Solución de problemas** Solución general de problemas y preguntas frecuentes. ](</es/help/troubleshooting>)

Was this useful?YesNo