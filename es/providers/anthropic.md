---
title: Anthropic
source_url: https://docs.openclaw.ai/es/providers/anthropic
scraped_at: 2026-05-25
---

Anthropic crea la familia de modelos **Claude**. OpenClaw admite dos rutas de autenticación:

  * **Clave de API** — acceso directo a la API de Anthropic con facturación basada en uso (modelos `anthropic/*`)
  * **Claude CLI** — reutiliza un inicio de sesión existente de Claude CLI en el mismo host


## Primeros pasos

### Clave de API

**Ideal para:** acceso estándar a la API y facturación basada en uso.

* ### Obtén tu clave de API

Crea una clave de API en la [Consola de Anthropic](<https://console.anthropic.com/>).

* ### Ejecuta la incorporación

bashCopy code
[code]
    openclaw onboard# choose: Anthropic API key
[/code]

O pasa la clave directamente:

bashCopy code
[code]
    openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
[/code]

* ### Verifica que el modelo esté disponible

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Ejemplo de configuración

json5Copy code
[code]
    {  env: { ANTHROPIC_API_KEY: "sk-ant-..." },  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

### Claude CLI

**Ideal para:** reutilizar un inicio de sesión existente de Claude CLI sin una clave de API separada.

* ### Asegúrate de que Claude CLI esté instalado y con sesión iniciada

Verifica con:

bashCopy code
[code]
    claude --version
[/code]

* ### Ejecuta la incorporación

bashCopy code
[code]
    openclaw onboard# choose: Claude CLI
[/code]

OpenClaw detecta y reutiliza las credenciales existentes de Claude CLI.

* ### Verifica que el modelo esté disponible

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Ejemplo de configuración

Prefiere la referencia canónica del modelo de Anthropic más una anulación de runtime de CLI:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-7" },      models: {        "anthropic/claude-opus-4-7": {          agentRuntime: { id: "claude-cli" },        },      },    },  },}
[/code]

Las referencias de modelo heredadas `claude-cli/claude-opus-4-7` siguen funcionando por compatibilidad, pero la configuración nueva debe mantener la selección de proveedor/modelo como `anthropic/*` y poner el backend de ejecución en la política de runtime del proveedor/modelo.

## Valores predeterminados de thinking (Claude 4.6)

Los modelos Claude 4.6 usan `adaptive` thinking de forma predeterminada en OpenClaw cuando no se establece ningún nivel de thinking explícito.

Anúlalo por mensaje con `/think:<level>` o en los parámetros del modelo:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { thinking: "adaptive" },        },      },    },  },}
[/code]

## Caché de prompts

OpenClaw admite la función de caché de prompts de Anthropic para autenticación con clave de API.

Valor | Duración de caché | Descripción  
---|---|---  
`"short"` (predeterminado) | 5 minutos | Se aplica automáticamente para autenticación con clave de API  
`"long"` | 1 hora | Caché extendida  
`"none"` | Sin caché | Desactiva la caché de prompts  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },  },}
[/code]

Anulaciones de caché por agente

Usa parámetros a nivel de modelo como base y luego anula agentes específicos mediante `agents.list[].params`:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-6" },      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },    list: [      { id: "research", default: true },      { id: "alerts", params: { cacheRetention: "none" } },    ],  },}
[/code]

Orden de combinación de configuración:

  1. `agents.defaults.models["provider/model"].params`
  2. `agents.list[].params` (coincidencia por `id`, anula por clave)


Esto permite que un agente conserve una caché de larga duración mientras otro agente en el mismo modelo desactiva la caché para tráfico por ráfagas o de baja reutilización.

Notas de Claude en Bedrock

  * Los modelos Anthropic Claude en Bedrock (`amazon-bedrock/*anthropic.claude*`) aceptan el paso directo de `cacheRetention` cuando se configura.
  * Los modelos de Bedrock que no son de Anthropic se fuerzan a `cacheRetention: "none"` en runtime.
  * Los valores predeterminados inteligentes de clave de API también inicializan `cacheRetention: "short"` para referencias de Claude en Bedrock cuando no se establece un valor explícito.


## Configuración avanzada

Modo rápido

El interruptor compartido `/fast` de OpenClaw admite tráfico directo de Anthropic (clave de API y OAuth a `api.anthropic.com`).

Comando | Se asigna a  
---|---  
`/fast on` | `service_tier: "auto"`  
`/fast off` | `service_tier: "standard_only"`  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-sonnet-4-6": {          params: { fastMode: true },        },      },    },  },}
[/code]

Comprensión multimedia (imagen y PDF)

El Plugin incluido de Anthropic registra comprensión de imágenes y PDF. OpenClaw resuelve automáticamente las capacidades multimedia desde la autenticación de Anthropic configurada; no se necesita configuración adicional.

Propiedad | Valor  
---|---  
Modelo predeterminado | `claude-opus-4-7`  
Entrada compatible | Imágenes, documentos PDF  
  
Cuando se adjunta una imagen o un PDF a una conversación, OpenClaw la enruta automáticamente mediante el proveedor de comprensión multimedia de Anthropic.

Ventana de contexto de 1M (beta)

La ventana de contexto de 1M de Anthropic está limitada por beta. Actívala por modelo:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { context1m: true },        },      },    },  },}
[/code]

OpenClaw asigna esto a `anthropic-beta: context-1m-2025-08-07` en las solicitudes.

`params.context1m: true` también se aplica al backend de Claude CLI (`claude-cli/*`) para modelos Opus y Sonnet aptos, lo que amplía la ventana de contexto en runtime para esas sesiones de CLI a fin de igualar el comportamiento de la API directa.

Contexto de 1M de Claude Opus 4.7

`anthropic/claude-opus-4.7` y su variante `claude-cli` tienen una ventana de contexto de 1M de forma predeterminada; no se necesita `params.context1m: true`.

## Solución de problemas

Errores 401 / token inválido de repente

La autenticación con token de Anthropic caduca y puede revocarse. Para nuevas configuraciones, usa una clave de API de Anthropic en su lugar.

No se encontró ninguna clave de API para el proveedor "anthropic"

La autenticación de Anthropic es **por agente** : los agentes nuevos no heredan las claves del agente principal. Vuelve a ejecutar la incorporación para ese agente (o configura una clave de API en el host de Gateway), luego verifica con `openclaw models status`.

No se encontraron credenciales para el perfil "anthropic:default"

Ejecuta `openclaw models status` para ver qué perfil de autenticación está activo. Vuelve a ejecutar la incorporación o configura una clave de API para esa ruta de perfil.

No hay perfil de autenticación disponible (todos en enfriamiento)

Revisa `openclaw models status --json` para `auth.unusableProfiles`. Los enfriamientos por límite de tasa de Anthropic pueden estar acotados por modelo, por lo que un modelo Anthropic hermano aún podría ser utilizable. Añade otro perfil de Anthropic o espera a que termine el enfriamiento.

## Relacionado

[**Selección de modelos** Elección de proveedores, referencias de modelo y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Backends de CLI** Detalles de configuración y runtime del backend de Claude CLI. ](</es/gateway/cli-backends>) [**Caché de prompts** Cómo funciona la caché de prompts entre proveedores. ](</es/reference/prompt-caching>) [**OAuth y autenticación** Detalles de autenticación y reglas de reutilización de credenciales. ](</es/gateway/authentication>)

Was this useful?YesNo