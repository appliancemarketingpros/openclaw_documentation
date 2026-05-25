---
title: Generación de música
source_url: https://docs.openclaw.ai/es/tools/music-generation
scraped_at: 2026-05-25
---

La herramienta `music_generate` permite al agente crear música o audio mediante la capacidad compartida de generación de música con proveedores configurados: Google, MiniMax y ComfyUI configurado por workflow actualmente.

Para ejecuciones de agente respaldadas por sesión, OpenClaw inicia la generación de música como una tarea en segundo plano, la registra en el libro de tareas y luego vuelve a despertar al agente cuando la pista está lista para que el agente pueda avisar al usuario y adjuntar el audio terminado. En chats de grupo/canal que usan entrega visible solo mediante herramienta de mensajes, el agente transmite el resultado mediante la herramienta de mensajes. Si el agente de finalización escribe solo una respuesta final privada, OpenClaw recurre a un envío directo por el canal con los medios generados. El despertar de finalización advierte explícitamente al agente que las respuestas finales normales son privadas en esas rutas.

## Inicio rápido

### Respaldado por proveedor compartido

* ### Configurar autenticación

Define una clave de API para al menos un proveedor; por ejemplo, `GEMINI_API_KEY` o `MINIMAX_API_KEY`.

* ### Elegir un modelo predeterminado (opcional)

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

* ### Pedirle al agente

_"Genera una pista de synthpop animada sobre un recorrido nocturno por una ciudad de neón."_

El agente llama a `music_generate` automáticamente. No hace falta una lista de permisos de herramientas.

Para contextos sincrónicos directos sin una ejecución de agente respaldada por sesión, la herramienta integrada aún recurre a la generación en línea y devuelve la ruta final de los medios en el resultado de la herramienta.

### Workflow de ComfyUI

* ### Configurar el workflow

Configura `plugins.entries.comfy.config.music` con un JSON de workflow y nodos de prompt/salida.

* ### Autenticación en la nube (opcional)

Para Comfy Cloud, define `COMFY_API_KEY` o `COMFY_CLOUD_API_KEY`.

* ### Llamar a la herramienta

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

Prompts de ejemplo:

textCopy code
[code]
    Generate a cinematic piano track with soft strings and no vocals.
[/code]

textCopy code
[code]
    Generate an energetic chiptune loop about launching a rocket at sunrise.
[/code]

## Proveedores compatibles

Proveedor | Modelo predeterminado | Entradas de referencia | Controles compatibles | Autenticación  
---|---|---|---|---  
ComfyUI | `workflow` | Hasta 1 imagen | Música o audio definidos por el workflow | `COMFY_API_KEY`, `COMFY_CLOUD_API_KEY`  
Google | `lyria-3-clip-preview` | Hasta 10 imágenes | `lyrics`, `instrumental`, `format` | `GEMINI_API_KEY`, `GOOGLE_API_KEY`  
MiniMax | `music-2.6` | Ninguna | `lyrics`, `instrumental`, `durationSeconds`, `format=mp3` | `MINIMAX_API_KEY` o OAuth de MiniMax  
  
### Matriz de capacidades

El contrato de modo explícito usado por `music_generate`, las pruebas de contrato y el barrido live compartido:

Proveedor | `generate` | `edit` | Límite de edición | Carriles live compartidos  
---|---|---|---|---  
ComfyUI | ✓ | ✓ | 1 imagen | No está en el barrido compartido; cubierto por `extensions/comfy/comfy.live.test.ts`  
Google | ✓ | ✓ | 10 imágenes | `generate`, `edit`  
MiniMax | ✓ | — | Ninguno | `generate`  
  
Usa `action: "list"` para inspeccionar proveedores y modelos compartidos disponibles en tiempo de ejecución:

textCopy code
[code]
    /tool music_generate action=list
[/code]

Usa `action: "status"` para inspeccionar la tarea de música activa respaldada por sesión:

textCopy code
[code]
    /tool music_generate action=status
[/code]

Ejemplo de generación directa:

textCopy code
[code]
    /tool music_generate prompt="Dreamy lo-fi hip hop with vinyl texture and gentle rain" instrumental=true
[/code]

## Parámetros de la herramienta

Prompt de generación de música. Requerido para `action: "generate"`.

`"status"` devuelve la tarea de sesión actual; `"list"` inspecciona proveedores.

Anulación de proveedor/modelo (por ejemplo, `google/lyria-3-pro-preview`, `comfy/workflow`).

Letra opcional cuando el proveedor admite entrada explícita de letra.

Solicita una salida solo instrumental cuando el proveedor lo admite.

Ruta o URL de una sola imagen de referencia.

Varias imágenes de referencia (hasta 10 en proveedores compatibles).

Duración objetivo en segundos cuando el proveedor admite indicaciones de duración.

Indicación de formato de salida cuando el proveedor lo admite.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Tiempo de espera opcional de la solicitud al proveedor en milisegundos. Cuando se omite, OpenClaw usa `agents.defaults.musicGenerationModel.timeoutMs` si está configurado. Los valores inferiores a 10000ms se elevan a 10000ms y se informan en el resultado de la herramienta. OPENCLAW_DOCS_MARKER:paramClose:

## Comportamiento asíncrono

La generación de música respaldada por sesión se ejecuta como una tarea en segundo plano:

  * **Tarea en segundo plano:** `music_generate` crea una tarea en segundo plano, devuelve inmediatamente una respuesta iniciada/de tarea y publica la pista terminada más tarde en un mensaje de seguimiento del agente.
  * **Prevención de duplicados:** mientras una tarea está `queued` o `running`, las llamadas posteriores a `music_generate` en la misma sesión devuelven el estado de la tarea en lugar de iniciar otra generación. Usa `action: "status"` para comprobarlo explícitamente.
  * **Consulta de estado:** `openclaw tasks list` u `openclaw tasks show <taskId>` inspecciona estados en cola, en ejecución y terminales.
  * **Despertar de finalización:** OpenClaw inyecta un evento interno de finalización de vuelta en la misma sesión para que el modelo pueda escribir por sí mismo el seguimiento visible para el usuario.
  * **Indicación de prompt:** los turnos posteriores de usuario/manual en la misma sesión reciben una pequeña indicación en tiempo de ejecución cuando una tarea de música ya está en curso, para que el modelo no llame a `music_generate` a ciegas de nuevo.
  * **Reserva sin sesión:** los contextos directos/locales sin una sesión real de agente se ejecutan en línea y devuelven el resultado de audio final en el mismo turno.


### Ciclo de vida de la tarea

Estado | Significado  
---|---  
`queued` | Tarea creada, esperando a que el proveedor la acepte.  
`running` | El proveedor está procesando (normalmente de 30 segundos a 3 minutos según proveedor y duración).  
`succeeded` | Pista lista; el agente se despierta y la publica en la conversación.  
`failed` | Error del proveedor o tiempo de espera agotado; el agente se despierta con detalles del error.  
  
Comprueba el estado desde la CLI:

bashCopy code
[code]
    openclaw tasks listopenclaw tasks show <taskId>openclaw tasks cancel <taskId>
[/code]

## Configuración

### Selección de modelo

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",        fallbacks: ["minimax/music-2.6"],      },    },  },}
[/code]

### Orden de selección de proveedor

OpenClaw prueba proveedores en este orden:

  1. Parámetro `model` de la llamada de herramienta (si el agente especifica uno).
  2. `musicGenerationModel.primary` de la configuración.
  3. `musicGenerationModel.fallbacks` en orden.
  4. Detección automática usando solo valores predeterminados de proveedor respaldados por autenticación: 
     * primero el proveedor predeterminado actual;
     * los proveedores de generación de música registrados restantes en orden de identificador de proveedor.


Si un proveedor falla, se prueba automáticamente el siguiente candidato. Si todos fallan, el error incluye detalles de cada intento.

Define `agents.defaults.mediaGenerationAutoProviderFallback: false` para usar solo entradas explícitas de `model`, `primary` y `fallbacks`.

## Notas de proveedores

ComfyUI

Controlado por workflow y depende del grafo configurado más la asignación de nodos para campos de prompt/salida. El Plugin `comfy` incluido se conecta a la herramienta compartida `music_generate` mediante el registro de proveedores de generación de música.

Google (Lyria 3)

Usa generación por lotes de Lyria 3. El flujo integrado actual admite prompt, texto opcional de letra e imágenes de referencia opcionales.

MiniMax

Usa el endpoint por lotes `music_generation`. Admite prompt, letra opcional, modo instrumental, dirección de duración y salida mp3 mediante autenticación con clave de API `minimax` u OAuth de `minimax-portal`.

## Elegir la ruta adecuada

  * **Respaldado por proveedor compartido** cuando quieres selección de modelo, conmutación por error de proveedor y el flujo asíncrono integrado de tarea/estado.
  * **Ruta de Plugin (ComfyUI)** cuando necesitas un grafo de workflow personalizado o un proveedor que no forma parte de la capacidad musical compartida incluida.


Si estás depurando comportamiento específico de ComfyUI, consulta [ComfyUI](</es/providers/comfy>). Si estás depurando comportamiento de proveedor compartido, empieza con [Google (Gemini)](</es/providers/google>) o [MiniMax](</es/providers/minimax>).

## Modos de capacidad de proveedor

El contrato compartido de generación de música admite declaraciones explícitas de modo:

  * `generate` para generación solo con prompt.
  * `edit` cuando la solicitud incluye una o más imágenes de referencia.


Las nuevas implementaciones de proveedores deben preferir bloques de modo explícitos:

typescriptCopy code
[code]
    capabilities: {  generate: {    maxTracks: 1,    supportsLyrics: true,    supportsFormat: true,  },  edit: {    enabled: true,    maxTracks: 1,    maxInputImages: 1,    supportsFormat: true,  },}
[/code]

Los campos planos heredados como `maxInputImages`, `supportsLyrics` y `supportsFormat` **no** bastan para anunciar compatibilidad con edición. Los proveedores deben declarar `generate` y `edit` explícitamente para que las pruebas live, las pruebas de contrato y la herramienta compartida `music_generate` puedan validar la compatibilidad de modo de forma determinista.

## Pruebas live

Cobertura live con suscripción explícita para los proveedores integrados compartidos:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test:live -- extensions/music-generation-providers.live.test.ts
[/code]

Wrapper del repo:

bashCopy code
[code]
    pnpm test:live:media music
[/code]

Este archivo live carga las variables de entorno de proveedor que faltan desde `~/.profile`, prefiere las claves de API de live/env antes que los perfiles de autenticación almacenados de forma predeterminada y ejecuta tanto la cobertura de `generate` como la de `edit` declarada cuando el proveedor habilita el modo `edit`. Cobertura actual:

  * `google`: `generate` más `edit`
  * `minimax`: solo `generate`
  * `comfy`: cobertura live separada de Comfy, no el barrido compartido de proveedores


Cobertura live opcional para la ruta de música de ComfyUI incluida:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

El archivo live de Comfy también cubre flujos de trabajo de imagen y video de comfy cuando esas secciones están configuradas.

## Relacionado

  * [Tareas en segundo plano](</es/automation/tasks>) — seguimiento de tareas para ejecuciones desvinculadas de `music_generate`
  * [ComfyUI](</es/providers/comfy>)
  * [Referencia de configuración](</es/gateway/config-agents#agent-defaults>) — configuración de `musicGenerationModel`
  * [Google (Gemini)](</es/providers/google>)
  * [MiniMax](</es/providers/minimax>)
  * [Modelos](</es/concepts/models>) — configuración de modelos y conmutación por error
  * [Resumen de herramientas](</es/tools>)


Was this useful?YesNo