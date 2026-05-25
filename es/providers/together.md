---
title: Together AI
source_url: https://docs.openclaw.ai/es/providers/together
scraped_at: 2026-05-25
---

[Together AI](<https://together.ai>) proporciona acceso a modelos líderes de código abierto, incluidos Llama, DeepSeek, Kimi y más, mediante una API unificada.

Propiedad | Valor  
---|---  
Proveedor | `together`  
Autenticación | `TOGETHER_API_KEY`  
API | compatible con OpenAI  
URL base | `https://api.together.xyz/v1`  
  
## Primeros pasos

* ### Obtén una clave de API

Crea una clave de API en [api.together.ai/settings/api-keys](<https://api.together.ai/settings/api-keys>).

* ### Ejecuta la incorporación

bashCopy code
[code]
    openclaw onboard --auth-choice together-api-key
[/code]

* ### Define un modelo predeterminado

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "together/moonshotai/Kimi-K2.5" },    },  },}
[/code]

### Ejemplo no interactivo

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice together-api-key \  --together-api-key "$TOGETHER_API_KEY"
[/code]

## Catálogo integrado

OpenClaw incluye este catálogo de Together integrado:

Referencia de modelo | Nombre | Entrada | Contexto | Notas  
---|---|---|---|---  
`together/moonshotai/Kimi-K2.5` | Kimi K2.5 | texto, imagen | 262,144 | Modelo predeterminado; razonamiento habilitado  
`together/zai-org/GLM-4.7` | GLM 4.7 Fp8 | texto | 202,752 | Modelo de texto de propósito general  
`together/meta-llama/Llama-3.3-70B-Instruct-Turbo` | Llama 3.3 70B Instruct Turbo | texto | 131,072 | Modelo de instrucciones rápido  
`together/meta-llama/Llama-4-Scout-17B-16E-Instruct` | Llama 4 Scout 17B 16E Instruct | texto, imagen | 10,000,000 | Multimodal  
`together/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | Llama 4 Maverick 17B 128E Instruct FP8 | texto, imagen | 20,000,000 | Multimodal  
`together/deepseek-ai/DeepSeek-V3.1` | DeepSeek V3.1 | texto | 131,072 | Modelo de texto general  
`together/deepseek-ai/DeepSeek-R1` | DeepSeek R1 | texto | 131,072 | Modelo de razonamiento  
`together/moonshotai/Kimi-K2-Instruct-0905` | Kimi K2-Instruct 0905 | texto | 262,144 | Modelo de texto Kimi secundario  
  
## Generación de video

El plugin `together` integrado también registra la generación de video mediante la herramienta compartida `video_generate`.

Propiedad | Valor  
---|---  
Modelo de video predeterminado | `together/Wan-AI/Wan2.2-T2V-A14B`  
Modos | texto a video, referencia de una sola imagen  
Parámetros admitidos | `aspectRatio`, `resolution`  
  
Para usar Together como proveedor de video predeterminado:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "together/Wan-AI/Wan2.2-T2V-A14B",      },    },  },}
[/code]

Nota sobre el entorno

Si el Gateway se ejecuta como daemon (launchd/systemd), asegúrate de que `TOGETHER_API_KEY` esté disponible para ese proceso (por ejemplo, en `~/.openclaw/.env` o mediante `env.shellEnv`).

Solución de problemas

  * Verifica que tu clave funcione: `openclaw models list --provider together`
  * Si los modelos no aparecen, confirma que la clave de API esté definida en el entorno correcto para tu proceso de Gateway.
  * Las referencias de modelo usan la forma `together/<model-id>`.


## Relacionado

[**Selección de modelo** Reglas de proveedor, referencias de modelo y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Generación de video** Parámetros de la herramienta compartida de generación de video y selección de proveedor. ](</es/tools/video-generation>) [**Referencia de configuración** Esquema de configuración completo, incluida la configuración de proveedores. ](</es/gateway/configuration-reference>) [**Together AI** Panel de Together AI, documentación de API y precios. ](<https://together.ai>)

Was this useful?YesNo