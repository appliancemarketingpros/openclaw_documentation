---
title: Gateway de IA de Vercel
source_url: https://docs.openclaw.ai/es/providers/vercel-ai-gateway
scraped_at: 2026-05-25
---

The [Vercel AI Gateway](<https://vercel.com/ai-gateway>) proporciona una API unificada para acceder a cientos de modelos mediante un único endpoint.

Propiedad | Valor  
---|---  
Proveedor | `vercel-ai-gateway`  
Auth | `AI_GATEWAY_API_KEY`  
API | compatible con Anthropic Messages  
Catálogo de modelos | Descubierto automáticamente mediante `/v1/models`  
  
## Primeros pasos

* ### Set the API key

Ejecuta la incorporación y elige la opción de autenticación de AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice ai-gateway-api-key
[/code]

* ### Set a default model

Añade el modelo a tu configuración de OpenClaw:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.6" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider vercel-ai-gateway
[/code]

## Ejemplo no interactivo

Para configuraciones con scripts o de CI, pasa todos los valores en la línea de comandos:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
[/code]

## Forma abreviada del ID de modelo

OpenClaw acepta referencias abreviadas de modelos Claude de Vercel y las normaliza en tiempo de ejecución:

Entrada abreviada | Referencia de modelo normalizada  
---|---  
`vercel-ai-gateway/claude-opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
`vercel-ai-gateway/opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4-6`  
  
## Configuración avanzada

Environment variable for daemon processes

Si el OpenClaw Gateway se ejecuta como daemon (launchd/systemd), asegúrate de que `AI_GATEWAY_API_KEY` esté disponible para ese proceso.

Provider routing

Vercel AI Gateway enruta las solicitudes al proveedor ascendente según el prefijo de la referencia de modelo. Por ejemplo, `vercel-ai-gateway/anthropic/claude-opus-4.6` se enruta mediante Anthropic, mientras que `vercel-ai-gateway/openai/gpt-5.5` se enruta mediante OpenAI y `vercel-ai-gateway/moonshotai/kimi-k2.6` se enruta mediante MoonshotAI. Tu única `AI_GATEWAY_API_KEY` gestiona la autenticación para todos los proveedores ascendentes.

Thinking levels

Las opciones de `/think` siguen prefijos de modelos ascendentes de confianza cuando OpenClaw conoce el contrato del proveedor ascendente. `vercel-ai-gateway/anthropic/...` usa el perfil de razonamiento de Claude, incluidos los valores predeterminados adaptativos para modelos Claude 4.6. `vercel-ai-gateway/openai/gpt-5.4`, `gpt-5.5` y las referencias de estilo Codex exponen `/think xhigh` igual que los proveedores directos OpenAI/OpenAI Codex. Otras referencias con espacio de nombres conservan los niveles normales de razonamiento, salvo que sus metadatos de catálogo declaren más.

## Relacionado

[**Model selection** Elegir proveedores, referencias de modelo y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Troubleshooting** Solución general de problemas y preguntas frecuentes. ](</es/help/troubleshooting>)

Was this useful?YesNo