---
title: Kilo Gateway
source_url: https://docs.openclaw.ai/es/providers/kilocode
scraped_at: 2026-05-25
---

Kilo Gateway proporciona una **API unificada** que enruta solicitudes a muchos modelos detrás de un único endpoint y una clave de API. Es compatible con OpenAI, por lo que la mayoría de los SDK de OpenAI funcionan cambiando la URL base.

Propiedad | Valor  
---|---  
Proveedor | `kilocode`  
Autenticación | `KILOCODE_API_KEY`  
API | Compatible con OpenAI  
URL base | `https://api.kilo.ai/api/gateway/`  
  
## Primeros pasos

* ### Crear una cuenta

Ve a [app.kilo.ai](<https://app.kilo.ai>), inicia sesión o crea una cuenta, luego navega a API Keys y genera una clave nueva.

* ### Ejecutar la incorporación

bashCopy code
[code]
    openclaw onboard --auth-choice kilocode-api-key
[/code]

O configura directamente la variable de entorno:

bashCopy code
[code]
    export KILOCODE_API_KEY="<your-kilocode-api-key>" # pragma: allowlist secret
[/code]

* ### Verificar que el modelo esté disponible

bashCopy code
[code]
    openclaw models list --provider kilocode
[/code]

## Modelo predeterminado

El modelo predeterminado es `kilocode/kilo/auto`, un modelo de enrutamiento inteligente propiedad del proveedor y gestionado por Kilo Gateway.

## Catálogo integrado

OpenClaw descubre dinámicamente los modelos disponibles desde Kilo Gateway al iniciarse. Usa `/models kilocode` para ver la lista completa de modelos disponibles con tu cuenta.

Cualquier modelo disponible en el Gateway se puede usar con el prefijo `kilocode/`:

Referencia de modelo | Notas  
---|---  
`kilocode/kilo/auto` | Predeterminado — enrutamiento inteligente  
`kilocode/anthropic/claude-sonnet-4` | Anthropic mediante Kilo  
`kilocode/openai/gpt-5.5` | OpenAI mediante Kilo  
`kilocode/google/gemini-3.1-pro-preview` | Google mediante Kilo  
...y muchos más | Usa `/models kilocode` para listar todos  
  
## Ejemplo de configuración

json5Copy code
[code]
    {  env: { KILOCODE_API_KEY: "<your-kilocode-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "kilocode/kilo/auto" },    },  },}
[/code]

Transporte y compatibilidad

Kilo Gateway está documentado en el código fuente como compatible con OpenRouter, por lo que permanece en la ruta de estilo proxy compatible con OpenAI en lugar de usar el conformado nativo de solicitudes de OpenAI.

  * Las referencias de Kilo respaldadas por Gemini permanecen en la ruta proxy-Gemini, por lo que OpenClaw mantiene allí la depuración de firmas de pensamiento de Gemini sin habilitar la validación de reproducción nativa de Gemini ni las reescrituras de arranque.
  * Kilo Gateway usa internamente un token Bearer con tu clave de API.

Contenedor de stream y razonamiento

El contenedor de stream compartido de Kilo añade el encabezado de aplicación del proveedor y normaliza las cargas de razonamiento de proxy para las referencias de modelo concretas compatibles.

Solución de problemas

  * Si el descubrimiento de modelos falla al inicio, OpenClaw recurre al catálogo estático incluido que contiene `kilocode/kilo/auto`.
  * Confirma que tu clave de API sea válida y que tu cuenta de Kilo tenga habilitados los modelos deseados.
  * Cuando el Gateway se ejecuta como daemon, asegúrate de que `KILOCODE_API_KEY` esté disponible para ese proceso (por ejemplo, en `~/.openclaw/.env` o mediante `env.shellEnv`).


## Relacionado

[**Selección de modelos** Elección de proveedores, referencias de modelo y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Referencia de configuración** Referencia completa de configuración de OpenClaw. ](</es/gateway/configuration-reference>) [**Kilo Gateway** Panel de Kilo Gateway, claves de API y gestión de cuenta. ](<https://app.kilo.ai>)

Was this useful?YesNo