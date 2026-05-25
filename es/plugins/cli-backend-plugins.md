---
title: Creación de plugins de backend de CLI
source_url: https://docs.openclaw.ai/es/plugins/cli-backend-plugins
scraped_at: 2026-05-25
---

Los plugins de backend CLI permiten que OpenClaw llame a una CLI de IA local como backend de inferencia de texto. El backend aparece como un prefijo de proveedor en las refs de modelo:

textCopy code
[code]
    acme-cli/acme-large
[/code]

Usa un backend CLI cuando la integración ascendente ya esté expuesta como un comando local, cuando la CLI controle el estado de inicio de sesión local, o cuando la CLI sea una alternativa útil si los proveedores de API no están disponibles.

## Qué controla el plugin

Un plugin de backend CLI tiene tres contratos:

Contrato | Archivo | Propósito  
---|---|---  
Entrada de paquete | `package.json` | Apunta OpenClaw al módulo de runtime del plugin  
Propiedad de manifiesto | `openclaw.plugin.json` | Declara el id del backend antes de cargar el runtime  
Registro de runtime | `index.ts` | Llama a `api.registerCliBackend(...)` con valores predeterminados del comando  
  
El manifiesto es metadatos de descubrimiento. No ejecuta la CLI y no registra comportamiento de runtime. El comportamiento de runtime empieza cuando la entrada del plugin llama a `api.registerCliBackend(...)`.

## Plugin de backend mínimo

* ### Crear metadatos del paquete

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-acme-cli",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./index.ts"],    "compat": {      "pluginApi": ">=2026.3.24-beta.2",      "minGatewayVersion": "2026.3.24-beta.2"    },    "build": {      "openclawVersion": "2026.3.24-beta.2",      "pluginSdkVersion": "2026.3.24-beta.2"    }  },  "dependencies": {    "openclaw": "^2026.3.24"  },  "devDependencies": {    "typescript": "^5.9.0"  }}
[/code]

Los paquetes publicados deben incluir archivos JavaScript de runtime compilados. Si tu entrada de origen es `./src/index.ts`, agrega `openclaw.runtimeExtensions` que apunte al par JavaScript compilado. Consulta [Puntos de entrada](</es/plugins/sdk-entrypoints>).

* ### Declarar la propiedad del backend

openclaw.plugin.jsonCopy code
[code]
    {  "id": "acme-cli",  "name": "Acme CLI",  "description": "Run Acme's local AI CLI through OpenClaw",  "cliBackends": ["acme-cli"],  "setup": {    "cliBackends": ["acme-cli"],    "requiresRuntime": false  },  "activation": {    "onStartup": false  },  "configSchema": {    "type": "object",    "additionalProperties": false  }}
[/code]

`cliBackends` es la lista de propiedad de runtime. Permite que OpenClaw cargue automáticamente el plugin cuando la configuración o la selección de modelo mencione `acme-cli/...`.

`setup.cliBackends` es la superficie de configuración basada primero en descriptores. Agrégala cuando el descubrimiento de modelos, la incorporación o el estado deban reconocer el backend sin cargar el runtime del plugin. Usa `requiresRuntime: false` solo cuando esos descriptores estáticos basten para la configuración.

* ### Registrar el backend

index.tsCopy code
[code]
    import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";import {  CLI_FRESH_WATCHDOG_DEFAULTS,  CLI_RESUME_WATCHDOG_DEFAULTS,  type CliBackendPlugin,} from "openclaw/plugin-sdk/cli-backend"; function buildAcmeCliBackend(): CliBackendPlugin {  return {    id: "acme-cli",    liveTest: {      defaultModelRef: "acme-cli/acme-large",      defaultImageProbe: false,      defaultMcpProbe: false,      docker: {        npmPackage: "@acme/acme-cli",        binaryName: "acme",      },    },    config: {      command: "acme",      args: ["chat", "--json"],      output: "json",      input: "stdin",      modelArg: "--model",      sessionArg: "--session",      sessionMode: "existing",      sessionIdFields: ["session_id", "conversation_id"],      systemPromptFileArg: "--system-file",      systemPromptWhen: "first",      imageArg: "--image",      imageMode: "repeat",      reliability: {        watchdog: {          fresh: { ...CLI_FRESH_WATCHDOG_DEFAULTS },          resume: { ...CLI_RESUME_WATCHDOG_DEFAULTS },        },      },      serialize: true,    },  };} export default definePluginEntry({  id: "acme-cli",  name: "Acme CLI",  description: "Run Acme's local AI CLI through OpenClaw",  register(api) {    api.registerCliBackend(buildAcmeCliBackend());  },});
[/code]

El id del backend debe coincidir con la entrada `cliBackends` del manifiesto. La `config` registrada es solo el valor predeterminado; la configuración de usuario en `agents.defaults.cliBackends.acme-cli` se fusiona sobre ella en runtime.

## Forma de la configuración

`CliBackendConfig` describe cómo OpenClaw debe iniciar y analizar la CLI:

Campo | Uso  
---|---  
`command` | Nombre del binario o ruta absoluta del comando  
`args` | argv base para ejecuciones nuevas  
`resumeArgs` | argv alternativo para sesiones reanudadas; admite `{sessionId}`  
`output` / `resumeOutput` | Analizador: `json`, `jsonl` o `text`  
`input` | Transporte del prompt: `arg` o `stdin`  
`modelArg` | Marca usada antes del id del modelo  
`modelAliases` | Asigna ids de modelo de OpenClaw a ids nativos de la CLI  
`sessionArg` / `sessionArgs` | Cómo pasar un id de sesión  
`sessionMode` | `always`, `existing` o `none`  
`sessionIdFields` | Campos JSON que OpenClaw lee de la salida de la CLI  
`systemPromptArg` / `systemPromptFileArg` | Transporte del prompt del sistema  
`systemPromptWhen` | `first`, `always` o `never`  
`imageArg` / `imageMode` | Compatibilidad con rutas de imagen  
`serialize` | Mantiene ordenadas las ejecuciones del mismo backend  
`reliability.watchdog` | Ajuste de tiempo de espera sin salida  
  
Prefiere la configuración estática más pequeña que coincida con la CLI. Agrega callbacks del plugin solo para comportamientos que realmente pertenezcan al backend.

## Hooks avanzados de backend

`CliBackendPlugin` también puede definir:

Hook | Uso  
---|---  
`normalizeConfig(config, context)` | Reescribe configuración de usuario heredada tras la fusión  
`resolveExecutionArgs(ctx)` | Agrega marcas con alcance de solicitud, como esfuerzo de razonamiento  
`prepareExecution(ctx)` | Crea puentes temporales de autenticación o configuración antes del inicio  
`transformSystemPrompt(ctx)` | Aplica una transformación final del prompt del sistema específica de la CLI  
`textTransforms` | Reemplazos bidireccionales de prompt/salida  
`defaultAuthProfileId` | Prefiere un perfil de autenticación específico de OpenClaw  
`authEpochMode` | Decide cómo los cambios de autenticación invalidan sesiones CLI almacenadas  
`nativeToolMode` | Declara si la CLI tiene herramientas nativas siempre activas  
`bundleMcp` / `bundleMcpMode` | Opta por el puente de herramientas MCP de loopback de OpenClaw  
  
Mantén estos hooks bajo propiedad del proveedor. No agregues ramas específicas de CLI al núcleo cuando un hook de backend pueda expresar el comportamiento.

## Puente de herramientas MCP

Los backends CLI no reciben herramientas de OpenClaw de forma predeterminada. Si la CLI puede consumir una configuración MCP, opta por ella explícitamente:

typescriptCopy code
[code]
    return {  id: "acme-cli",  bundleMcp: true,  bundleMcpMode: "codex-config-overrides",  config: {    command: "acme",    args: ["chat", "--json"],    output: "json",  },};
[/code]

Los modos de puente compatibles son:

Modo | Uso  
---|---  
`claude-config-file` | CLI que aceptan un archivo de configuración MCP  
`codex-config-overrides` | CLI que aceptan sobrescrituras de configuración en argv  
`gemini-system-settings` | CLI que leen configuración MCP desde su directorio de configuración del sistema  
  
Activa el puente solo cuando la CLI pueda consumirlo realmente. Si la CLI tiene su propia capa de herramientas integrada que no puede desactivarse, define `nativeToolMode: "always-on"` para que OpenClaw pueda fallar en modo cerrado cuando un llamador requiera no usar herramientas nativas.

## Configuración de usuario

Los usuarios pueden sobrescribir cualquier valor predeterminado del backend:

json5Copy code
[code]
    {  agents: {    defaults: {      cliBackends: {        "acme-cli": {          command: "/opt/acme/bin/acme",          args: ["chat", "--json", "--profile", "work"],          modelAliases: {            large: "acme-large-2026",          },        },      },      model: {        primary: "openai/gpt-5.5",        fallbacks: ["acme-cli/large"],      },    },  },}
[/code]

Documenta la sobrescritura mínima que los usuarios probablemente necesiten. Normalmente es solo `command` cuando el binario está fuera de `PATH`.

## Verificación

Para plugins incluidos, agrega una prueba enfocada alrededor del constructor y el registro de configuración, y luego ejecuta el carril de pruebas dirigido del plugin:

bashCopy code
[code]
    pnpm test extensions/acme-cli
[/code]

Para plugins locales o instalados, verifica el descubrimiento y una ejecución real de modelo:

bashCopy code
[code]
    openclaw plugins inspect acme-cli --runtime --jsonopenclaw agent --message "reply exactly: backend ok" --model acme-cli/acme-large
[/code]

Si el backend admite imágenes o MCP, agrega una prueba smoke en vivo que demuestre esas rutas con la CLI real. No dependas de la inspección estática para el comportamiento de prompts, imágenes, MCP o reanudación de sesiones.

## Lista de verificación

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `package.json` tiene `openclaw.extensions` y entradas de runtime compiladas para paquetes publicados OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `openclaw.plugin.json` declara `cliBackends` y `activation.onStartup` intencional OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `setup.cliBackends` está presente cuando la configuración o el descubrimiento de modelos debe ver el backend en frío OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `api.registerCliBackend(...)` usa el mismo id de backend que el manifiesto OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Las sobrescrituras de usuario en `agents.defaults.cliBackends.<id>` siguen teniendo prioridad OPENCLAW_DOCS_MARKER:calloutClose:

Was this useful?YesNo