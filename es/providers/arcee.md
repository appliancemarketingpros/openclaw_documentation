---
title: Arcee AI
source_url: https://docs.openclaw.ai/es/providers/arcee
scraped_at: 2026-05-25
---

[Arcee AI](<https://arcee.ai>) proporciona acceso a la familia Trinity de modelos de mezcla de expertos mediante una API compatible con OpenAI. Todos los modelos Trinity tienen licencia Apache 2.0.

Se puede acceder a los modelos de Arcee AI directamente mediante la plataforma Arcee o a través de [OpenRouter](</es/providers/openrouter>).

Propiedad | Valor  
---|---  
Proveedor | `arcee`  
Autenticación | `ARCEEAI_API_KEY` (directa) o `OPENROUTER_API_KEY` (mediante OpenRouter)  
API | Compatible con OpenAI  
URL base | `https://api.arcee.ai/api/v1` (directa) o `https://openrouter.ai/api/v1` (OpenRouter)  
  
## Primeros pasos

### Directo (plataforma Arcee)

* ### Obtén una clave de API

Crea una clave de API en [Arcee AI](<https://chat.arcee.ai/>).

* ### Ejecuta la incorporación

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-api-key
[/code]

* ### Define un modelo predeterminado

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

### Mediante OpenRouter

* ### Obtén una clave de API

Crea una clave de API en [OpenRouter](<https://openrouter.ai/keys>).

* ### Ejecuta la incorporación

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-openrouter
[/code]

* ### Define un modelo predeterminado

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

Las mismas referencias de modelo funcionan para configuraciones directas y con OpenRouter (por ejemplo, `arcee/trinity-large-thinking`).

## Configuración no interactiva

### Directo (plataforma Arcee)

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-api-key \  --arceeai-api-key "$ARCEEAI_API_KEY"
[/code]

### Mediante OpenRouter

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-openrouter \  --openrouter-api-key "$OPENROUTER_API_KEY"
[/code]

## Catálogo integrado

OpenClaw incluye actualmente este catálogo Arcee incluido:

Referencia de modelo | Nombre | Entrada | Contexto | Costo (entrada/salida por 1M) | Notas  
---|---|---|---|---|---  
`arcee/trinity-large-thinking` | Trinity Large Thinking | text | 256K | $0.25 / $0.90 | Modelo predeterminado; razonamiento activado  
`arcee/trinity-large-preview` | Trinity Large Preview | text | 128K | $0.25 / $1.00 | De propósito general; 400B parámetros, 13B activos  
`arcee/trinity-mini` | Trinity Mini 26B | text | 128K | $0.045 / $0.15 | Rápido y rentable; llamada a funciones  
  
## Funciones admitidas

Función | Admitida  
---|---  
Streaming | Sí  
Uso de herramientas / llamada a funciones | Sí (Trinity Mini, Trinity Large Preview)  
Salida estructurada (modo JSON y esquema JSON) | Sí  
Pensamiento extendido | Sí (Trinity Large Thinking; herramientas deshabilitadas)  
  
Nota sobre el entorno

Si el Gateway se ejecuta como daemon (launchd/systemd), asegúrate de que `ARCEEAI_API_KEY` (o `OPENROUTER_API_KEY`) esté disponible para ese proceso (por ejemplo, en `~/.openclaw/.env` o mediante `env.shellEnv`).

Enrutamiento de OpenRouter

Al usar modelos Arcee mediante OpenRouter, se aplican las mismas referencias de modelo `arcee/*`. OpenClaw gestiona el enrutamiento de forma transparente según tu opción de autenticación. Consulta la [documentación del proveedor OpenRouter](</es/providers/openrouter>) para ver detalles de configuración específicos de OpenRouter.

## Relacionado

[**OpenRouter** Accede a los modelos Arcee y a muchos otros mediante una sola clave de API. ](</es/providers/openrouter>) [**Selección de modelo** Elección de proveedores, referencias de modelo y comportamiento de conmutación por error. ](</es/concepts/model-providers>)

Was this useful?YesNo