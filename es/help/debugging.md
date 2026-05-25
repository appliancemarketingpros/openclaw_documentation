---
title: Depuración
source_url: https://docs.openclaw.ai/es/help/debugging
scraped_at: 2026-05-25
---

Ayudantes de depuración para salida en streaming, especialmente cuando un proveedor mezcla razonamiento en texto normal.

## Anulaciones de depuración en tiempo de ejecución

Usa `/debug` en el chat para definir anulaciones de configuración **solo en tiempo de ejecución** (memoria, no disco). `/debug` está deshabilitado de forma predeterminada; habilítalo con `commands.debug: true`. Esto resulta práctico cuando necesitas alternar ajustes poco comunes sin editar `openclaw.json`.

Ejemplos:

CodeCopy code
[code]
    /debug show/debug set messages.responsePrefix="[openclaw]"/debug unset messages.responsePrefix/debug reset
[/code]

`/debug reset` borra todas las anulaciones y vuelve a la configuración en disco.

## Salida de traza de sesión

Usa `/trace` cuando quieras ver líneas de traza/depuración propiedad del Plugin en una sesión sin activar el modo detallado completo.

Ejemplos:

textCopy code
[code]
    /trace/trace on/trace off
[/code]

Usa `/trace` para diagnósticos de Plugin, como resúmenes de depuración de Active Memory. Sigue usando `/verbose` para la salida detallada normal de estado/herramientas, y sigue usando `/debug` para anulaciones de configuración solo en tiempo de ejecución.

## Traza del ciclo de vida del Plugin

Usa `OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1` cuando los comandos de ciclo de vida del Plugin se sientan lentos y necesites un desglose de fases integrado para metadatos de Plugin, descubrimiento, registro, espejo de tiempo de ejecución, mutación de configuración y trabajo de actualización. La traza es opcional y escribe en stderr, por lo que la salida JSON de los comandos sigue siendo analizable.

Ejemplo:

bashCopy code
[code]
    OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1 openclaw plugins install tokenjuice --force
[/code]

Salida de ejemplo:

textCopy code
[code]
    [plugins:lifecycle] phase="config read" ms=6.83 status=ok command="install"[plugins:lifecycle] phase="slot selection" ms=94.31 status=ok command="install" pluginId="tokenjuice"[plugins:lifecycle] phase="registry refresh" ms=51.56 status=ok command="install" reason="source-changed"
[/code]

Usa esto para investigar el ciclo de vida del Plugin antes de recurrir a un perfilador de CPU. Si el comando se ejecuta desde un checkout de código fuente, prefiere medir el runtime compilado con `node dist/entry.js ...` después de `pnpm build`; `pnpm openclaw ...` también mide la sobrecarga del ejecutor desde código fuente.

## Inicio de CLI y perfilado de comandos

Usa el benchmark de inicio incluido en el repositorio cuando un comando se sienta lento:

bashCopy code
[code]
    pnpm test:startup:bench:smokepnpm tsx scripts/bench-cli-startup.ts --preset real --case status --runs 3pnpm tsx scripts/bench-cli-startup.ts --preset real --cpu-prof-dir .artifacts/cli-cpu
[/code]

Para un perfilado puntual a través del ejecutor normal desde código fuente, define `OPENCLAW_RUN_NODE_CPU_PROF_DIR`:

bashCopy code
[code]
    OPENCLAW_RUN_NODE_CPU_PROF_DIR=.artifacts/cli-cpu pnpm openclaw status
[/code]

El ejecutor desde código fuente añade flags de perfil de CPU de Node y escribe un `.cpuprofile` para el comando. Usa esto antes de añadir instrumentación temporal al código de comandos.

Para bloqueos de inicio que parecen trabajo síncrono del sistema de archivos o del cargador de módulos, añade el flag de traza de E/S síncrona de Node a través del ejecutor desde código fuente:

bashCopy code
[code]
    OPENCLAW_TRACE_SYNC_IO=1 pnpm openclaw gateway --force
[/code]

`pnpm gateway:watch` deja este flag deshabilitado de forma predeterminada para el hijo Gateway observado. Define `OPENCLAW_TRACE_SYNC_IO=1` cuando quieras explícitamente salida de traza de E/S síncrona de Node en modo observación.

## Modo observación del Gateway

Para iterar rápidamente, ejecuta el gateway bajo el observador de archivos:

bashCopy code
[code]
    pnpm gateway:watch
[/code]

De forma predeterminada, esto inicia o reinicia una sesión tmux llamada `openclaw-gateway-watch-main` (o una variante específica de perfil/puerto como `openclaw-gateway-watch-dev-19001`) y se adjunta automáticamente desde terminales interactivos. Shells no interactivos, CI y llamadas de ejecución de agentes permanecen separadas e imprimen instrucciones para adjuntarse. Adjunta manualmente cuando sea necesario:

bashCopy code
[code]
    tmux attach -t openclaw-gateway-watch-main
[/code]

El panel de tmux ejecuta el observador sin procesar:

bashCopy code
[code]
    node scripts/watch-node.mjs gateway --force
[/code]

Usa el modo en primer plano cuando no quieras tmux:

bashCopy code
[code]
    pnpm gateway:watch:raw# orOPENCLAW_GATEWAY_WATCH_TMUX=0 pnpm gateway:watch
[/code]

Deshabilita la adjunción automática manteniendo la gestión de tmux:

bashCopy code
[code]
    OPENCLAW_GATEWAY_WATCH_ATTACH=0 pnpm gateway:watch
[/code]

Perfila el tiempo de CPU del Gateway observado al depurar puntos críticos de inicio/runtime:

bashCopy code
[code]
    pnpm gateway:watch --benchmark
[/code]

El wrapper de observación consume `--benchmark` antes de invocar el Gateway y escribe un `.cpuprofile` de V8 por cada salida del hijo Gateway bajo `.artifacts/gateway-watch-profiles/`. Detén o reinicia el gateway observado para vaciar el perfil actual y luego ábrelo con Chrome DevTools o Speedscope:

bashCopy code
[code]
    npx speedscope .artifacts/gateway-watch-profiles/*.cpuprofile
[/code]

Usa `--benchmark-dir <path>` cuando quieras perfiles en otro lugar. Usa `--benchmark-no-force` cuando quieras que el hijo bajo benchmark omita la limpieza de puerto predeterminada con `--force` y falle rápido si el puerto del Gateway ya está en uso. El modo benchmark suprime de forma predeterminada el ruido de traza de E/S síncrona. Define `OPENCLAW_TRACE_SYNC_IO=1` con `--benchmark` cuando quieras explícitamente tanto perfiles de CPU como trazas de pila de E/S síncrona de Node. En modo benchmark esos bloques de traza se escriben en `gateway-watch-output.log` bajo el directorio de benchmark y se filtran del panel de terminal; los logs normales del Gateway siguen visibles.

El wrapper de tmux traslada al panel selectores comunes no secretos de runtime, como `OPENCLAW_PROFILE`, `OPENCLAW_CONFIG_PATH`, `OPENCLAW_STATE_DIR`, `OPENCLAW_GATEWAY_PORT` y `OPENCLAW_SKIP_CHANNELS`. Pon credenciales de proveedor en tu perfil/configuración normal, o usa el modo sin procesar en primer plano para secretos efímeros puntuales. Si el Gateway observado sale durante el inicio, el observador ejecuta `openclaw doctor --fix --non-interactive` una vez y reinicia el hijo Gateway. Usa `OPENCLAW_GATEWAY_WATCH_AUTO_DOCTOR=0` cuando quieras el fallo de inicio original sin el paso de reparación solo para desarrollo. El panel tmux gestionado también usa de forma predeterminada logs del Gateway con color para mejorar la legibilidad; define `FORCE_COLOR=0` al iniciar `pnpm gateway:watch` para deshabilitar la salida ANSI.

El observador reinicia ante archivos relevantes para la compilación bajo `src/`, archivos fuente de extensiones, `package.json` de extensiones y metadatos `openclaw.plugin.json`, `tsconfig.json`, `package.json` y `tsdown.config.ts`. Los cambios de metadatos de extensiones reinician el gateway sin forzar una recompilación de `tsdown`; los cambios de código fuente y configuración todavía recompilan `dist` primero.

Añade cualquier flag de CLI de gateway después de `gateway:watch` y se pasará en cada reinicio. Volver a ejecutar el mismo comando de observación vuelve a crear el panel tmux nombrado, y el observador sin procesar todavía mantiene su bloqueo de observador único para que los padres de observador duplicados se reemplacen en lugar de acumularse.

## Perfil de desarrollo + gateway de desarrollo (--dev)

Usa el perfil de desarrollo para aislar el estado y levantar una configuración segura y descartable para depuración. Hay **dos** flags `--dev`:

  * **`--dev` global (perfil):** aísla el estado bajo `~/.openclaw-dev` y establece por defecto el puerto del gateway en `19001` (los puertos derivados se desplazan con él).
  * **`gateway --dev`: indica al Gateway que cree automáticamente una configuración + workspace predeterminados** si faltan (y omita [BOOTSTRAP.md](<http://BOOTSTRAP.md>)).


Flujo recomendado (perfil de desarrollo + arranque de desarrollo):

bashCopy code
[code]
    pnpm gateway:devOPENCLAW_PROFILE=dev openclaw tui
[/code]

Si todavía no tienes una instalación global, ejecuta la CLI mediante `pnpm openclaw ...`.

Qué hace esto:

  1. **Aislamiento de perfil** (`--dev` global)

     * `OPENCLAW_PROFILE=dev`
     * `OPENCLAW_STATE_DIR=~/.openclaw-dev`
     * `OPENCLAW_CONFIG_PATH=~/.openclaw-dev/openclaw.json`
     * `OPENCLAW_GATEWAY_PORT=19001` (browser/canvas se desplazan en consecuencia)
  2. **Arranque de desarrollo** (`gateway --dev`)

     * Escribe una configuración mínima si falta (`gateway.mode=local`, bind loopback).
     * Establece `agent.workspace` en el workspace de desarrollo.
     * Establece `agent.skipBootstrap=true` (sin [BOOTSTRAP.md](<http://BOOTSTRAP.md>)).
     * Inicializa los archivos del workspace si faltan: `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, `HEARTBEAT.md`.
     * Identidad predeterminada: **C3-PO** (droide de protocolo).
     * Omite proveedores de canales en modo desarrollo (`OPENCLAW_SKIP_CHANNELS=1`).


Flujo de restablecimiento (inicio limpio):

bashCopy code
[code]
    pnpm gateway:dev:reset
[/code]

`--reset` borra configuración, credenciales, sesiones y el workspace de desarrollo (usando `trash`, no `rm`), y luego recrea la configuración de desarrollo predeterminada.

## Logging de stream sin procesar (OpenClaw)

OpenClaw puede registrar el **stream sin procesar del asistente** antes de cualquier filtrado/formateo. Esta es la mejor forma de ver si el razonamiento llega como deltas de texto plano (o como bloques de pensamiento separados).

Habilítalo mediante CLI:

bashCopy code
[code]
    pnpm gateway:watch --raw-stream
[/code]

Anulación de ruta opcional:

bashCopy code
[code]
    pnpm gateway:watch --raw-stream --raw-stream-path ~/.openclaw/logs/raw-stream.jsonl
[/code]

Variables de entorno equivalentes:

bashCopy code
[code]
    OPENCLAW_RAW_STREAM=1OPENCLAW_RAW_STREAM_PATH=~/.openclaw/logs/raw-stream.jsonl
[/code]

Archivo predeterminado:

`~/.openclaw/logs/raw-stream.jsonl`

## Logging de fragmentos sin procesar (pi-mono)

Para capturar **fragmentos sin procesar compatibles con OpenAI** antes de que se analicen en bloques, pi-mono expone un logger independiente:

bashCopy code
[code]
    PI_RAW_STREAM=1
[/code]

Ruta opcional:

bashCopy code
[code]
    PI_RAW_STREAM_PATH=~/.pi-mono/logs/raw-openai-completions.jsonl
[/code]

Archivo predeterminado:

`~/.pi-mono/logs/raw-openai-completions.jsonl`

> Nota: esto solo lo emiten procesos que usan el proveedor `openai-completions` de pi-mono.

## Notas de seguridad

  * Los logs de stream sin procesar pueden incluir prompts completos, salida de herramientas y datos de usuario.
  * Mantén los logs locales y elimínalos después de depurar.
  * Si compartes logs, elimina primero secretos e información personal identificable.


## Depuración en VSCode

Los mapas de código fuente son necesarios para habilitar la depuración en IDEs basados en VSCode porque muchos de los archivos generados terminan con nombres con hash como parte del proceso de compilación. Las configuraciones `launch.json` incluidas apuntan al servicio Gateway, pero se pueden adaptar rápidamente para otros fines:

  1. **Rebuild and Debug Gateway** \- Depura el servicio Gateway después de crear una nueva compilación
  2. **Debug Gateway** \- Depura el servicio Gateway de una compilación preexistente


### Configuración

La configuración predeterminada **Rebuild and Debug Gateway** viene lista para usar: eliminará automáticamente la carpeta `/dist` y recompilará el proyecto con la depuración habilitada:

  1. Abre el panel **Run and Debug** desde la barra de actividad o pulsa `Ctrl`+`Shift`+`D`
  2. En el IDE, asegúrate de que **Rebuild and Debug Gateway** esté seleccionada en el menú desplegable de configuración y luego pulsa el botón **Start Debugging**


Como alternativa, si prefieres gestionar manualmente los procesos de compilación y depuración:

  1. Abre una terminal y habilita los mapas de código fuente: 
     * **Linux/macOS** : `export OUTPUT_SOURCE_MAPS=1`
     * **Windows (PowerShell)** : `$env:OUTPUT_SOURCE_MAPS="1"`
     * **Windows (CMD)** : `set OUTPUT_SOURCE_MAPS=1`
  2. En la misma terminal, recompila el proyecto: `pnpm clean:dist && pnpm build`
  3. En el IDE, selecciona la opción **Debug Gateway** en el menú desplegable de configuración **Run and Debug** y luego pulsa el botón **Start Debugging**


Ahora puedes establecer puntos de interrupción en tus archivos fuente TypeScript (directorio `src/`) y el depurador asignará correctamente los puntos de interrupción al JavaScript compilado mediante mapas de código fuente. Podrás inspeccionar variables, avanzar paso a paso por el código y examinar pilas de llamadas como se espera.

### Notas

  * Si usas la opción **"Rebuild and Debug Gateway"** , cada vez que se inicie el depurador eliminará por completo la carpeta `/dist` y ejecutará un `pnpm build` completo con mapas de código fuente habilitados antes de iniciar el Gateway
  * Si usas la opción **"Debug Gateway"** , las sesiones de depuración pueden iniciarse y detenerse en cualquier momento sin afectar la carpeta `/dist`, pero debes usar un proceso de terminal separado tanto para habilitar la depuración como para gestionar el ciclo de compilación
  * Modifica la configuración `launch.json` de `args` para depurar otras secciones del proyecto
  * Si necesitas usar la CLI compilada de OpenClaw para otras tareas (por ejemplo, `dashboard --no-open` si tu sesión de depuración genera un nuevo token de autenticación), puedes ejecutarla en otra terminal como `node ./openclaw.mjs` o crear un alias de shell como `alias openclaw-build="node $(pwd)/openclaw.mjs"`


## Relacionado

  * [Solución de problemas](</es/help/troubleshooting>)
  * [Preguntas frecuentes](</es/help/faq>)


Was this useful?YesNo