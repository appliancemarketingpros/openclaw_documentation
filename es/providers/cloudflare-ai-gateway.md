---
title: Gateway de IA de Cloudflare
source_url: https://docs.openclaw.ai/es/providers/cloudflare-ai-gateway
scraped_at: 2026-05-25
---

Cloudflare AI Gateway se sitúa delante de las API de proveedores y te permite añadir análisis, almacenamiento en caché y controles. Para Anthropic, OpenClaw usa la Anthropic Messages API a través de tu endpoint de Gateway.

Propiedad | Valor  
---|---  
Proveedor | `cloudflare-ai-gateway`  
URL base | `https://gateway.ai.cloudflare.com/v1/<account_id>/<gateway_id>/anthropic`  
Modelo predeterminado | `cloudflare-ai-gateway/claude-sonnet-4-6`  
Clave de API | `CLOUDFLARE_AI_GATEWAY_API_KEY` (tu clave de API de proveedor para solicitudes a través del Gateway)  
  
Cuando el razonamiento está habilitado para los modelos Anthropic Messages, OpenClaw elimina los turnos finales de prellenado del asistente antes de enviar la carga útil a través de Cloudflare AI Gateway. Anthropic rechaza el prellenado de respuestas con razonamiento extendido, mientras que el prellenado ordinario sin razonamiento sigue estando disponible.

## Primeros pasos

* ### Configurar la clave de API del proveedor y los detalles del Gateway

Ejecuta la incorporación y elige la opción de autenticación de Cloudflare AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice cloudflare-ai-gateway-api-key
[/code]

Esto solicita tu ID de cuenta, ID de Gateway y clave de API.

* ### Configurar un modelo predeterminado

Añade el modelo a tu configuración de OpenClaw:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cloudflare-ai-gateway/claude-sonnet-4-6" },    },  },}
[/code]

* ### Verificar que el modelo está disponible

bashCopy code
[code]
    openclaw models list --provider cloudflare-ai-gateway
[/code]

## Ejemplo no interactivo

Para configuraciones con scripts o de CI, pasa todos los valores en la línea de comandos:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY"
[/code]

## Configuración avanzada

Gateways autenticados

Si habilitaste la autenticación de Gateway en Cloudflare, añade el encabezado `cf-aig-authorization`. Esto es **además de** tu clave de API del proveedor.

json5Copy code
[code]
    {  models: {    providers: {      "cloudflare-ai-gateway": {        headers: {          "cf-aig-authorization": "Bearer <cloudflare-ai-gateway-token>",        },      },    },  },}
[/code]

Nota sobre el entorno

Si el Gateway se ejecuta como un demonio (launchd/systemd), asegúrate de que `CLOUDFLARE_AI_GATEWAY_API_KEY` esté disponible para ese proceso.

## Relacionado

[**Selección de modelo** Elección de proveedores, referencias de modelos y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Solución de problemas** Solución general de problemas y preguntas frecuentes. ](</es/help/troubleshooting>)

Was this useful?YesNo