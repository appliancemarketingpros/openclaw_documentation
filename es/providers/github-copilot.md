---
title: GitHub Copilot
source_url: https://docs.openclaw.ai/es/providers/github-copilot
scraped_at: 2026-05-25
---

GitHub Copilot es el asistente de codificación con IA de GitHub. Proporciona acceso a los modelos de Copilot para tu cuenta y plan de GitHub. OpenClaw puede usar Copilot como proveedor de modelos de dos formas distintas.

## Dos formas de usar Copilot en OpenClaw

### Proveedor integrado (github-copilot)

Usa el flujo nativo de inicio de sesión del dispositivo para obtener un token de GitHub y luego canjearlo por tokens de la API de Copilot cuando OpenClaw se ejecuta. Esta es la ruta **predeterminada** y más sencilla porque no requiere VS Code.

* ### Ejecuta el comando de inicio de sesión

bashCopy code
[code]
    openclaw models auth login-github-copilot
[/code]

Se te pedirá que visites una URL e introduzcas un código de un solo uso. Mantén la terminal abierta hasta que se complete.

* ### Establece un modelo predeterminado

bashCopy code
[code]
    openclaw models set github-copilot/claude-opus-4.7
[/code]

O en la configuración:

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "github-copilot/claude-opus-4.7" } },  },}
[/code]

### Plugin Copilot Proxy (copilot-proxy)

Usa la extensión de VS Code **Copilot Proxy** como puente local. OpenClaw se comunica con el endpoint `/v1` del proxy y usa la lista de modelos que configures allí.

## Flags opcionales

Flag | Descripción  
---|---  
`--yes` | Omite el prompt de confirmación  
`--set-default` | Aplica también el modelo predeterminado recomendado del proveedor  
bashCopy code
[code]
    # Skip confirmationopenclaw models auth login-github-copilot --yes # Login and set the default model in one stepopenclaw models auth login --provider github-copilot --method device --set-default
[/code]

## Incorporación no interactiva

Si ya tienes un token de acceso OAuth de GitHub para Copilot, impórtalo durante la configuración sin interfaz con `openclaw onboard --non-interactive`:

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --auth-choice github-copilot \  --github-copilot-token "$COPILOT_GITHUB_TOKEN" \  --skip-channels --skip-health
[/code]

También puedes omitir `--auth-choice`; pasar `--github-copilot-token` infiere la opción de autenticación del proveedor GitHub Copilot. Si se omite el flag, la incorporación recurre a `COPILOT_GITHUB_TOKEN`, `GH_TOKEN` y luego a `GITHUB_TOKEN`. Usa `--secret-input-mode ref` con `COPILOT_GITHUB_TOKEN` definido para almacenar un `tokenRef` respaldado por env en lugar de texto sin formato en `auth-profiles.json`.

Se requiere TTY interactiva

El flujo de inicio de sesión del dispositivo requiere una TTY interactiva. Ejecútalo directamente en una terminal, no en un script no interactivo ni en un pipeline de CI.

La disponibilidad de modelos depende de tu plan

La disponibilidad de los modelos de Copilot depende de tu plan de GitHub. Si se rechaza un modelo, prueba con otro ID (por ejemplo, `github-copilot/gpt-4.1`).

Actualización del catálogo en vivo desde la API de Copilot

Una vez que la ruta de autenticación de inicio de sesión del dispositivo (o variable de entorno) ha resuelto un token de GitHub, OpenClaw actualiza el catálogo de modelos bajo demanda desde `${baseUrl}/models` (el mismo endpoint que usa VS Code Copilot) para que el entorno de ejecución siga los derechos por cuenta y las ventanas de contexto precisas sin rotación de manifiestos. Los modelos de Copilot recién publicados se vuelven visibles sin una actualización de OpenClaw, y las ventanas de contexto reflejan los límites reales por modelo (p. ej., 400k para la serie gpt-5.x, 1M para las variantes internas `claude-opus-*-1m`).

El catálogo estático incluido permanece como respaldo visible cuando la detección está deshabilitada, el usuario no tiene perfil de autenticación de GitHub, el canje de tokens falla o la llamada HTTPS a `/models` devuelve un error. Para desactivar esta opción y depender por completo del catálogo de manifiesto estático (escenarios sin conexión o aislados):

json5Copy code
[code]
    {  plugins: {    entries: {      "github-copilot": {        config: { discovery: { enabled: false } },      },    },  },}
[/code]

Selección de transporte

Los ID de modelo de Claude usan automáticamente el transporte Anthropic Messages. Los modelos GPT, o-series y Gemini mantienen el transporte OpenAI Responses. OpenClaw selecciona el transporte correcto en función de la referencia del modelo.

Compatibilidad de solicitudes

OpenClaw envía encabezados de solicitud al estilo de IDE de Copilot en los transportes de Copilot, incluidos turnos de Compaction integrada, resultado de herramienta y seguimiento de imagen. No habilita la continuación de Responses a nivel de proveedor para Copilot a menos que ese comportamiento se haya verificado con la API de Copilot.

Orden de resolución de variables de entorno

OpenClaw resuelve la autenticación de Copilot desde variables de entorno en el siguiente orden de prioridad:

Prioridad | Variable | Notas  
---|---|---  
1 | `COPILOT_GITHUB_TOKEN` | Máxima prioridad, específica de Copilot  
2 | `GH_TOKEN` | Token de GitHub CLI (respaldo)  
3 | `GITHUB_TOKEN` | Token estándar de GitHub (la más baja)  
  
Cuando hay varias variables definidas, OpenClaw usa la de mayor prioridad. El flujo de inicio de sesión del dispositivo (`openclaw models auth login-github-copilot`) almacena su token en el almacén de perfiles de autenticación y tiene prioridad sobre todas las variables de entorno.

Almacenamiento de tokens

El inicio de sesión almacena un token de GitHub en el almacén de perfiles de autenticación y lo canjea por un token de la API de Copilot cuando OpenClaw se ejecuta. No necesitas gestionar el token manualmente.

## Embeddings de búsqueda de memoria

GitHub Copilot también puede servir como proveedor de embeddings para la [búsqueda de memoria](</es/concepts/memory-search>). Si tienes una suscripción a Copilot y has iniciado sesión, OpenClaw puede usarlo para embeddings sin una clave de API aparte.

### Detección automática

Cuando `memorySearch.provider` es `"auto"` (el valor predeterminado), GitHub Copilot se prueba con prioridad 15 -- después de los embeddings locales pero antes de OpenAI y otros proveedores de pago. Si hay un token de GitHub disponible, OpenClaw descubre los modelos de embeddings disponibles desde la API de Copilot y elige el mejor automáticamente.

### Configuración explícita

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "github-copilot",        // Optional: override the auto-discovered model        model: "text-embedding-3-small",      },    },  },}
[/code]

### Cómo funciona

  1. OpenClaw resuelve tu token de GitHub (desde variables de entorno o perfil de autenticación).
  2. Lo canjea por un token de la API de Copilot de corta duración.
  3. Consulta el endpoint `/models` de Copilot para descubrir los modelos de embeddings disponibles.
  4. Elige el mejor modelo (prefiere `text-embedding-3-small`).
  5. Envía solicitudes de embeddings al endpoint `/embeddings` de Copilot.


La disponibilidad de modelos depende de tu plan de GitHub. Si no hay modelos de embeddings disponibles, OpenClaw omite Copilot y prueba el siguiente proveedor.

## Relacionado

[**Selección de modelos** Elección de proveedores, referencias de modelo y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**OAuth y autenticación** Detalles de autenticación y reglas de reutilización de credenciales. ](</es/gateway/authentication>)

Was this useful?YesNo