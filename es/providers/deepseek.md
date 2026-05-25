---
title: DeepSeek
source_url: https://docs.openclaw.ai/es/providers/deepseek
scraped_at: 2026-05-25
---

[DeepSeek](<https://www.deepseek.com>) proporciona potentes modelos de IA con una API compatible con OpenAI.

Propiedad | Valor  
---|---  
Proveedor | `deepseek`  
Autenticación | `DEEPSEEK_API_KEY`  
API | compatible con OpenAI  
URL base | `https://api.deepseek.com`  
  
## Primeros pasos

* ### Get your API key

Crea una clave de API en [platform.deepseek.com](<https://platform.deepseek.com/api_keys>).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice deepseek-api-key
[/code]

Esto solicitará tu clave de API y establecerá `deepseek/deepseek-v4-flash` como modelo predeterminado.

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider deepseek
[/code]

Para inspeccionar el catálogo estático incluido sin requerir un Gateway en ejecución, usa:

bashCopy code
[code]
    openclaw models list --all --provider deepseek
[/code]

Non-interactive setup

Para instalaciones con scripts o sin interfaz, pasa todas las marcas directamente:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice deepseek-api-key \  --deepseek-api-key "$DEEPSEEK_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Catálogo integrado

Referencia de modelo | Nombre | Entrada | Contexto | Salida máxima | Notas  
---|---|---|---|---|---  
`deepseek/deepseek-v4-flash` | DeepSeek V4 Flash | texto | 1,000,000 | 384,000 | Modelo predeterminado; superficie V4 con capacidad de pensamiento  
`deepseek/deepseek-v4-pro` | DeepSeek V4 Pro | texto | 1,000,000 | 384,000 | Superficie V4 con capacidad de pensamiento  
`deepseek/deepseek-chat` | DeepSeek Chat | texto | 131,072 | 8,192 | Superficie DeepSeek V3.2 sin pensamiento  
`deepseek/deepseek-reasoner` | DeepSeek Reasoner | texto | 131,072 | 65,536 | Superficie V3.2 con razonamiento habilitado  
  
## Pensamiento y herramientas

Las sesiones de pensamiento de DeepSeek V4 tienen un contrato de reproducción más estricto que la mayoría de los proveedores compatibles con OpenAI: después de que un turno con pensamiento habilitado usa herramientas, DeepSeek espera que los mensajes del asistente reproducidos de ese turno incluyan `reasoning_content` en las solicitudes de seguimiento. OpenClaw maneja esto dentro del Plugin de DeepSeek, por lo que el uso normal de herramientas de varios turnos funciona con `deepseek/deepseek-v4-flash` y `deepseek/deepseek-v4-pro`.

Si cambias una sesión existente de otro proveedor compatible con OpenAI a un modelo DeepSeek V4, es posible que los turnos anteriores de llamadas a herramientas del asistente no tengan `reasoning_content` nativo de DeepSeek. OpenClaw completa ese campo faltante en los mensajes del asistente reproducidos para solicitudes de pensamiento de DeepSeek V4, de modo que el proveedor pueda aceptar el historial sin requerir `/new`.

Cuando el pensamiento está deshabilitado en OpenClaw (incluida la selección **None** en la interfaz), OpenClaw envía a DeepSeek `thinking: { type: "disabled" }` y elimina el `reasoning_content` reproducido del historial saliente. Esto mantiene las sesiones con pensamiento deshabilitado en la ruta sin pensamiento de DeepSeek.

Usa `deepseek/deepseek-v4-flash` para la ruta rápida predeterminada. Usa `deepseek/deepseek-v4-pro` cuando quieras el modelo V4 más potente y puedas aceptar mayor costo o latencia.

## Pruebas en vivo

La suite directa de modelos en vivo incluye DeepSeek V4 en el conjunto de modelos moderno. Para ejecutar solo las comprobaciones de modelos directos de DeepSeek V4:

bashCopy code
[code]
    OPENCLAW_LIVE_PROVIDERS=deepseek \OPENCLAW_LIVE_MODELS="deepseek/deepseek-v4-flash,deepseek/deepseek-v4-pro" \pnpm test:live src/agents/models.profiles.live.test.ts
[/code]

Esa comprobación en vivo verifica que ambos modelos V4 puedan completar solicitudes y que los turnos de seguimiento de pensamiento/herramientas conserven la carga de reproducción que DeepSeek requiere.

## Ejemplo de configuración

json5Copy code
[code]
    {  env: { DEEPSEEK_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "deepseek/deepseek-v4-flash" },    },  },}
[/code]

## Relacionado

[**Model selection** Elección de proveedores, referencias de modelos y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Configuration reference** Referencia completa de configuración para agentes, modelos y proveedores. ](</es/gateway/configuration-reference>)

Was this useful?YesNo