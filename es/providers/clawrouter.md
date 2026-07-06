---
title: ClawRouter
source_url: https://docs.openclaw.ai/es/providers/clawrouter
scraped_at: 2026-07-06
---

ModelsProviders

ClawRouter proporciona a OpenClaw una clave con ámbito de política para varios proveedores de modelos upstream. El plugin `clawrouter` incluido descubre solo los modelos permitidos para esa clave, enruta cada modelo mediante su protocolo declarado e informa el presupuesto de la clave y el uso agregado en las superficies de uso de OpenClaw.

Las credenciales upstream y el reenvío específico de cada proveedor permanecen en ClawRouter, por lo que nunca instalas ni autenticas cada plugin de proveedor upstream en el host de OpenClaw. El plugin se entrega incluido con OpenClaw (`enabledByDefault: true`); solo necesitas una credencial emitida de ClawRouter.

Propiedad | Valor  
---|---  
Proveedor | `clawrouter`  
Plugin | incluido (incluido en OpenClaw)  
Auth | `CLAWROUTER_API_KEY`  
URL predeterminada | `https://clawrouter.openclaw.ai`  
Catálogo de modelos | Con ámbito de credencial mediante `/v1/catalog`  
Cuotas | Presupuesto mensual y uso mediante `/v1/usage`  
  
## Primeros pasos

* ### Obtén una credencial con ámbito

Pide a tu administrador de ClawRouter una credencial cuya política incluya los proveedores, modelos y presupuesto mensual que debes usar. Las credenciales se muestran una sola vez cuando se emiten.

* ### Configura OpenClaw

bashCopy code
[code]
    export CLAWROUTER_API_KEY="..."openclaw onboard --auth-choice clawrouter-api-keyopenclaw plugins enable clawrouter
[/code]

`clawrouter` está incluido y habilitado de forma predeterminada. Si tu configuración define `plugins.allow`, añade `clawrouter` a esa lista antes de habilitarlo. Para una implementación personalizada, define `models.providers.clawrouter.baseUrl` como el origen de ClawRouter; el valor predeterminado es `https://clawrouter.openclaw.ai`.

* ### Lista los modelos concedidos

bashCopy code
[code]
    openclaw models list --all --provider clawrouter
[/code]

Usa las referencias de modelo devueltas exactamente como se muestran. Conservan el espacio de nombres upstream, como `clawrouter/openai/gpt-5.5`, `clawrouter/anthropic/claude-sonnet-4-6` o `clawrouter/google/gemini-3.5-flash`. Si `agents.defaults.models` es una lista de permitidos en tu configuración, añade cada referencia seleccionada de ClawRouter.

* ### Selecciona un modelo

bashCopy code
[code]
    openclaw models set clawrouter/<provider>/<model>
[/code]

También puedes seleccionar un modelo devuelto para una ejecución con `openclaw agent --model clawrouter/<provider>/<model> --message "..."`.

## Descubrimiento de modelos

`GET /v1/catalog` devuelve `{ providers: [...] }`, donde cada entrada de proveedor lista sus propios `models[]` (con id upstream, capacidades y precios) y sus rutas de solicitud admitidas. OpenClaw no entrega una segunda lista fija de modelos de ClawRouter. Un modelo del catálogo se anuncia como modelo de OpenClaw cuando:

  * la política de la credencial concede su proveedor;
  * el modelo del catálogo anuncia una capacidad LLM admitida (`llm.responses`, `llm.chat`, `llm.messages` o `llm.stream` con una ruta de streaming coincidente); y
  * el proveedor expone una ruta coincidente para uno de los transportes siguientes.


Añadir un modelo a un proveedor de ClawRouter admitido no necesita una versión nueva de OpenClaw: la siguiente actualización del catálogo (almacenada en caché 60 segundos por ámbito de credencial) lo descubre. Un modelo que necesita un nuevo protocolo de cable requiere primero soporte del plugin.

## Protocolo y plugins de proveedor

ClawRouter posee las credenciales upstream; su catálogo indica a OpenClaw qué transporte usar, por lo que nunca instalas el plugin de autenticación de cada empresa upstream.

Capacidad/ruta del catálogo | Transporte de OpenClaw  
---|---  
`llm.responses` (proveedor compatible con OpenAI) | `openai-responses`  
`llm.chat` (proveedor compatible con OpenAI) | `openai-completions`  
`llm.messages` \+ ruta `anthropic.messages` | `anthropic-messages`  
`llm.stream` \+ ruta de streaming `google.generate_content` | `google-generative-ai`  
  
El plugin también aplica las políticas coincidentes de replay y esquema de herramientas para esas familias (compatibilidad de esquema de herramientas de OpenAI/DeepSeek/Gemini; políticas nativas de replay de Anthropic y Google Gemini). Un proveedor del catálogo que expone solo un formato de solicitud no admitido no se anuncia intencionalmente como modelo de texto de OpenClaw. Normaliza esos proveedores a uno de los contratos admitidos en ClawRouter en lugar de enviar una carga incompatible.

## Cuotas y uso

La respuesta `/v1/usage` de ClawRouter alimenta las superficies normales de uso de proveedor de OpenClaw: totales de solicitudes, tokens y gasto, además de una ventana de presupuesto mensual cuando la clave tiene un límite. Las claves sin medición siguen mostrando el uso agregado sin una ventana porcentual.

La búsqueda de cuota usa la misma clave con ámbito que el descubrimiento de modelos. Un fallo en la búsqueda de cuota no bloquea la ejecución del modelo.

Consulta la instantánea en vivo con:

bashCopy code
[code]
    openclaw status --usageopenclaw models status
[/code]

La misma instantánea del proveedor está disponible para `/status` en el chat y en la IU de uso de OpenClaw. El presupuesto es para toda la política, por lo que las solicitudes realizadas por otro cliente usando la misma política de ClawRouter pueden cambiar el porcentaje restante.

## Solución de problemas

Síntoma | Comprobación  
---|---  
No hay modelos de ClawRouter | Confirma que el plugin está habilitado y permitido por `plugins.allow`, y luego comprueba que la credencial esté activa y conceda al menos un proveedor listo.  
Falta un modelo de ClawRouter configurado | Inspecciona su capacidad y compatibilidad de rutas de `/v1/catalog`. Los contratos de transporte no admitidos se filtran intencionalmente.  
`Unknown model: clawrouter/...` | Añade la referencia exacta del catálogo a `agents.defaults.models` cuando ese mapa de configuración se use como lista de permitidos.  
`401` o `403` desde el catálogo o uso | Reemite o vuelve a definir el ámbito de la credencial de ClawRouter; OpenClaw no recurre a claves de proveedor upstream.  
La llamada al modelo falla después del descubrimiento | Comprueba la conexión del proveedor y el estado del upstream en ClawRouter, y vuelve a intentarlo después de que se recupere su estado de disponibilidad.  
El uso tiene totales pero no porcentaje | La política no tiene medición; añade un presupuesto mensual en ClawRouter para exponer una ventana porcentual.  
  
## Comportamiento de seguridad

  * El descubrimiento del catálogo está limitado a la clave proxy configurada y se almacena en caché por ámbito de credencial (directorio del agente, directorio del workspace, id de perfil de autenticación y URL base).
  * La clave proxy se adjunta solo al despachar solicitudes; no se almacena en los metadatos del modelo.
  * Los ids de modelos nativos de Anthropic y Gemini se reescriben a sus ids upstream solo al despachar.
  * Las filas de catálogo no admitidas o no concedidas fallan de forma cerrada y no son seleccionables.


## Relacionado

[**Proveedores de modelos** Configuración de proveedores y selección de modelos. ](</es/concepts/model-providers>) [**Seguimiento de uso** Superficies de uso y estado de OpenClaw. ](</es/concepts/usage-tracking>)

Was this useful?YesNo

Open issue