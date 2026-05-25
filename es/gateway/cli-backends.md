---
title: Backends de la CLI
source_url: https://docs.openclaw.ai/es/gateway/cli-backends
scraped_at: 2026-05-25
---

OpenClaw puede ejecutar **CLI de IA locales** como **respaldo solo de texto** cuando los proveedores de API están caídos, limitados por tasa o se comportan mal temporalmente. Esto es intencionadamente conservador:

  * **Las herramientas de OpenClaw no se inyectan directamente** , pero los backends con `bundleMcp: true` pueden recibir herramientas del Gateway mediante un puente MCP de loopback.
  * **Streaming JSONL** para las CLI que lo admiten.
  * **Se admiten sesiones** (para que los turnos de seguimiento mantengan coherencia).
  * **Las imágenes pueden pasarse tal cual** si la CLI acepta rutas de imagen.


Esto está diseñado como una **red de seguridad** más que como una ruta principal. Úsalo cuando quieras respuestas de texto que "siempre funcionen" sin depender de API externas.

Si quieres un runtime de arnés completo con controles de sesión ACP, tareas en segundo plano, vinculación de hilos/conversaciones y sesiones externas de codificación persistentes, usa [Agentes ACP](</es/tools/acp-agents>) en su lugar. Los backends de CLI no son ACP.

## Inicio rápido para principiantes

Puedes usar Codex CLI **sin ninguna configuración** (el plugin de OpenAI incluido registra un backend predeterminado):

bashCopy code
[code]
    openclaw agent --message "hi" --model codex-cli/gpt-5.5
[/code]

Si tu Gateway se ejecuta bajo launchd/systemd y PATH es mínimo, añade solo la ruta del comando:

json5Copy code
[code]
    {  agents: {    defaults: {      cliBackends: {        "codex-cli": {          command: "/opt/homebrew/bin/codex",        },      },    },  },}
[/code]

Eso es todo. No se necesitan claves ni configuración de autenticación adicional más allá de la propia CLI.

Si usas un backend de CLI incluido como **proveedor de mensajes principal** en un host de Gateway, OpenClaw ahora carga automáticamente el plugin incluido propietario cuando tu configuración hace referencia explícita a ese backend en una referencia de modelo o bajo `agents.defaults.cliBackends`.

## Usarlo como respaldo

Añade un backend de CLI a tu lista de respaldos para que solo se ejecute cuando fallen los modelos principales:

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "anthropic/claude-opus-4-6",        fallbacks: ["codex-cli/gpt-5.5"],      },      models: {        "anthropic/claude-opus-4-6": { alias: "Opus" },        "codex-cli/gpt-5.5": {},      },    },  },}
[/code]

Notas:

  * Si usas `agents.defaults.models` (lista de permitidos), también debes incluir ahí tus modelos de backend de CLI.
  * Si el proveedor principal falla (autenticación, límites de tasa, tiempos de espera), OpenClaw probará después el backend de CLI.


## Resumen de configuración

Todos los backends de CLI viven bajo:

CodeCopy code
[code]
    agents.defaults.cliBackends
[/code]

Cada entrada se identifica por un **id de proveedor** (por ejemplo, `codex-cli`, `my-cli`). El id de proveedor se convierte en el lado izquierdo de tu referencia de modelo:

CodeCopy code
[code]
    <provider>/<model>
[/code]

### Configuración de ejemplo

json5Copy code
[code]
    {  agents: {    defaults: {      cliBackends: {        "codex-cli": {          command: "/opt/homebrew/bin/codex",        },        "my-cli": {          command: "my-cli",          args: ["--json"],          output: "json",          input: "arg",          modelArg: "--model",          modelAliases: {            "claude-opus-4-6": "opus",            "claude-sonnet-4-6": "sonnet",          },          sessionArg: "--session",          sessionMode: "existing",          sessionIdFields: ["session_id", "conversation_id"],          systemPromptArg: "--system",          // For CLIs with a dedicated prompt-file flag:          // systemPromptFileArg: "--system-file",          // Codex-style CLIs can point at a prompt file instead:          // systemPromptFileConfigArg: "-c",          // systemPromptFileConfigKey: "model_instructions_file",          systemPromptWhen: "first",          imageArg: "--image",          imageMode: "repeat",          // Opt in only if this backend may reseed safe invalidated sessions          // from bounded raw OpenClaw transcript history before compaction.          reseedFromRawTranscriptWhenUncompacted: true,          serialize: true,        },      },    },  },}
[/code]

## Cómo funciona

  1. **Selecciona un backend** según el prefijo de proveedor (`codex-cli/...`).
  2. **Construye un prompt de sistema** usando el mismo prompt de OpenClaw + contexto del workspace.
  3. **Ejecuta la CLI** con un id de sesión (si se admite) para que el historial se mantenga consistente. El backend `claude-cli` incluido mantiene activo un proceso stdio de Claude por cada sesión de OpenClaw y envía los turnos de seguimiento por stdin stream-json.
  4. **Analiza la salida** (JSON o texto sin formato) y devuelve el texto final.
  5. **Persiste los ids de sesión** por backend, para que los seguimientos reutilicen la misma sesión de CLI.


El backend `codex-cli` de OpenAI incluido pasa el prompt de sistema de OpenClaw mediante la anulación de configuración `model_instructions_file` de Codex (`-c model_instructions_file="..."`). Codex no expone una bandera al estilo de Claude `--append-system-prompt`, así que OpenClaw escribe el prompt ensamblado en un archivo temporal para cada nueva sesión de Codex CLI.

El backend `claude-cli` de Anthropic incluido recibe la instantánea de Skills de OpenClaw de dos maneras: el catálogo compacto de Skills de OpenClaw en el prompt de sistema anexado, y un plugin temporal de Claude Code pasado con `--plugin-dir`. El plugin contiene solo las Skills elegibles para ese agente/sesión, por lo que el resolutor nativo de skills de Claude Code ve el mismo conjunto filtrado que OpenClaw anunciaría de otro modo en el prompt. OpenClaw sigue aplicando las anulaciones de entorno/API key de Skill al entorno del proceso hijo para la ejecución.

Claude CLI también tiene su propio modo de permisos no interactivo. OpenClaw lo asigna a la política de ejecución existente en vez de añadir configuración específica de Claude: cuando la política de ejecución efectiva solicitada es YOLO (`tools.exec.security: "full"` y `tools.exec.ask: "off"`), OpenClaw añade `--permission-mode bypassPermissions`. Los ajustes por agente `agents.list[].tools.exec` anulan `tools.exec` global para ese agente. Para forzar un modo de Claude diferente, define argumentos raw explícitos del backend como `--permission-mode default` o `--permission-mode acceptEdits` bajo `agents.defaults.cliBackends.claude-cli.args` y `resumeArgs` coincidentes.

El backend `claude-cli` de Anthropic incluido también asigna los niveles `/think` de OpenClaw a la bandera nativa `--effort` de Claude Code para niveles distintos de off. `minimal` y `low` se asignan a `low`, `adaptive` y `medium` se asignan a `medium`, y `high`, `xhigh` y `max` se asignan directamente. Otros backends de CLI necesitan que su plugin propietario declare un asignador argv equivalente antes de que `/think` pueda afectar a la CLI generada.

Antes de que OpenClaw pueda usar el backend `claude-cli` incluido, Claude Code ya debe haber iniciado sesión en el mismo host:

bashCopy code
[code]
    claude auth loginclaude auth status --textopenclaw models auth login --provider anthropic --method cli --set-default
[/code]

Usa `agents.defaults.cliBackends.claude-cli.command` solo cuando el binario `claude` no esté ya en `PATH`.

## Sesiones

  * Si la CLI admite sesiones, define `sessionArg` (por ejemplo, `--session-id`) o `sessionArgs` (marcador de posición `{sessionId}`) cuando el ID deba insertarse en varias banderas.
  * Si la CLI usa un **subcomando resume** con banderas diferentes, define `resumeArgs` (reemplaza `args` al reanudar) y opcionalmente `resumeOutput` (para reanudaciones no JSON).
  * `sessionMode`: 
    * `always`: siempre envía un id de sesión (UUID nuevo si no hay ninguno almacenado).
    * `existing`: envía un id de sesión solo si ya se había almacenado uno.
    * `none`: nunca envía un id de sesión.
  * `claude-cli` usa por defecto `liveSession: "claude-stdio"`, `output: "jsonl"`, e `input: "stdin"` para que los turnos de seguimiento reutilicen el proceso Claude activo mientras esté activo. Stdio cálido es ahora el valor predeterminado, incluso para configuraciones personalizadas que omiten campos de transporte. Si el Gateway se reinicia o el proceso inactivo sale, OpenClaw reanuda desde el id de sesión de Claude almacenado. Los ids de sesión almacenados se verifican contra una transcripción de proyecto existente y legible antes de reanudar, por lo que las vinculaciones fantasma se limpian con `reason=transcript-missing` en lugar de iniciar silenciosamente una nueva sesión de Claude CLI bajo `--resume`.
  * Las sesiones en vivo de Claude mantienen protecciones acotadas de salida JSONL. Los valores predeterminados permiten hasta 8 MiB y 20.000 líneas JSONL raw por turno. Los turnos de Claude con muchas herramientas pueden aumentarlas por backend con `agents.defaults.cliBackends.claude-cli.reliability.outputLimits.maxTurnRawChars` y `maxTurnLines`; OpenClaw limita esos ajustes a 64 MiB y 100.000 líneas.
  * Las sesiones de CLI almacenadas son continuidad propiedad del proveedor. El restablecimiento diario implícito de sesión no las corta; `/reset` y las políticas explícitas `session.reset` sí lo hacen.
  * Las sesiones nuevas de CLI normalmente reseembran solo desde el resumen de Compaction de OpenClaw más la cola posterior a la Compaction. Para recuperar sesiones cortas que se invalidan antes de la Compaction, un backend puede optar por `reseedFromRawTranscriptWhenUncompacted: true`. OpenClaw aún mantiene la reseembra de transcripción raw acotada y la limita a invalidaciones seguras como transcripciones de CLI ausentes, cambios de prompt de sistema/MCP o reintento por sesión expirada; los cambios de perfil de autenticación o de época de credenciales nunca reseembran historial de transcripción raw.


Notas de serialización:

  * `serialize: true` mantiene ordenadas las ejecuciones del mismo carril.
  * La mayoría de las CLI serializan en un carril de proveedor.
  * OpenClaw descarta la reutilización de sesiones de CLI almacenadas cuando cambia la identidad de autenticación seleccionada, incluido un id de perfil de autenticación cambiado, API key estática, token estático o identidad de cuenta OAuth cuando la CLI expone una. La rotación de tokens de acceso y actualización OAuth no corta la sesión de CLI almacenada. Si una CLI no expone un id de cuenta OAuth estable, OpenClaw deja que esa CLI aplique los permisos de reanudación.


## Preludio de respaldo desde sesiones claude-cli

Cuando un intento de `claude-cli` falla y pasa a un candidato que no es CLI en [`agents.defaults.model.fallbacks`](</es/concepts/model-failover>), OpenClaw siembra el siguiente intento con un preludio de contexto recopilado de la transcripción JSONL local de Claude Code en `~/.claude/projects/`. Sin esta siembra, el proveedor de respaldo empezaría en frío porque la propia transcripción de sesión de OpenClaw está vacía para ejecuciones de `claude-cli`.

  * El preludio prefiere el resumen `/compact` más reciente o el marcador `compact_boundary`, y luego anexa los turnos posteriores al límite más recientes hasta un presupuesto de caracteres. Los turnos previos al límite se descartan porque el resumen ya los representa.
  * Los bloques de herramientas se consolidan en pistas compactas `(tool call: name)` y `(tool result: …)` para mantener honesto el presupuesto del prompt. El resumen se etiqueta como `(truncated)` si se desborda.
  * Los respaldos del mismo proveedor de `claude-cli` a `claude-cli` dependen del propio `--resume` de Claude y omiten el preludio.
  * La siembra reutiliza la validación existente de rutas de archivo de sesión de Claude, por lo que no se pueden leer rutas arbitrarias.


## Imágenes (paso directo)

Si tu CLI acepta rutas de imagen, define `imageArg`:

json5Copy code
[code]
    imageArg: "--image",imageMode: "repeat"
[/code]

OpenClaw escribirá imágenes base64 en archivos temporales. Si `imageArg` está definido, esas rutas se pasan como argumentos de CLI. Si falta `imageArg`, OpenClaw anexa las rutas de archivo al prompt (inyección de rutas), lo cual basta para las CLI que cargan automáticamente archivos locales desde rutas sin formato.

## Entradas / salidas

  * `output: "json"` (predeterminado) intenta analizar JSON y extraer texto + id de sesión.
  * Para la salida JSON de Gemini CLI, OpenClaw lee el texto de respuesta desde `response` y el uso desde `stats` cuando `usage` falta o está vacío.
  * `output: "jsonl"` analiza streams JSONL (por ejemplo, Codex CLI `--json`) y extrae el mensaje final del agente más los identificadores de sesión cuando están presentes.
  * `output: "text"` trata stdout como la respuesta final.


Modos de entrada:

  * `input: "arg"` (predeterminado) pasa el prompt como el último argumento de CLI.
  * `input: "stdin"` envía el prompt por stdin.
  * Si el prompt es muy largo y `maxPromptArgChars` está definido, se usa stdin.


## Valores predeterminados (propiedad del plugin)

El plugin de OpenAI incluido también registra un valor predeterminado para `codex-cli`:

  * `command: "codex"`
  * `args: ["exec","--json","--color","never","--sandbox","workspace-write","--skip-git-repo-check"]`
  * `resumeArgs: ["exec","resume","{sessionId}","-c","sandbox_mode=\"workspace-write\"","--skip-git-repo-check"]`
  * `output: "jsonl"`
  * `resumeOutput: "text"`
  * `modelArg: "--model"`
  * `imageArg: "--image"`
  * `sessionMode: "existing"`


El Plugin de Google incluido también registra un valor predeterminado para `google-gemini-cli`:

  * `command: "gemini"`
  * `args: ["--output-format", "json", "--prompt", "{prompt}"]`
  * `resumeArgs: ["--resume", "{sessionId}", "--output-format", "json", "--prompt", "{prompt}"]`
  * `imageArg: "@"`
  * `imagePathScope: "workspace"`
  * `modelArg: "--model"`
  * `sessionMode: "existing"`
  * `sessionIdFields: ["session_id", "sessionId"]`


Requisito previo: la CLI local de Gemini debe estar instalada y disponible como `gemini` en `PATH` (`brew install gemini-cli` o `npm install -g @google/gemini-cli`).

Notas sobre JSON de Gemini CLI:

  * El texto de la respuesta se lee del campo JSON `response`.
  * El uso recurre a `stats` cuando `usage` no existe o está vacío.
  * `stats.cached` se normaliza como `cacheRead` de OpenClaw.
  * Si falta `stats.input`, OpenClaw deriva los tokens de entrada de `stats.input_tokens - stats.cached`.


Sobrescribe solo si es necesario (común: ruta absoluta de `command`).

## Valores predeterminados propios del Plugin

Los valores predeterminados del backend CLI ahora forman parte de la superficie del Plugin:

  * Los Plugins los registran con `api.registerCliBackend(...)`.
  * El `id` del backend se convierte en el prefijo del proveedor en las referencias de modelo.
  * La configuración de usuario en `agents.defaults.cliBackends.<id>` sigue sobrescribiendo el valor predeterminado del Plugin.
  * La limpieza de configuración específica del backend sigue siendo propiedad del Plugin mediante el hook opcional `normalizeConfig`.


Los Plugins que necesitan pequeños adaptadores de compatibilidad de prompts/mensajes pueden declarar transformaciones de texto bidireccionales sin reemplazar un proveedor ni un backend CLI:

typescriptCopy code
[code]
    api.registerTextTransforms({  input: [    { from: /red basket/g, to: "blue basket" },    { from: /paper ticket/g, to: "digital ticket" },    { from: /left shelf/g, to: "right shelf" },  ],  output: [    { from: /blue basket/g, to: "red basket" },    { from: /digital ticket/g, to: "paper ticket" },    { from: /right shelf/g, to: "left shelf" },  ],});
[/code]

`input` reescribe el prompt del sistema y el prompt del usuario que se pasan a la CLI. `output` reescribe los deltas transmitidos del asistente y el texto final analizado antes de que OpenClaw procese sus propios marcadores de control y la entrega del canal.

Para las CLI que emiten JSONL compatible con `stream-json` de Claude Code, establece `jsonlDialect: "claude-stream-json"` en la configuración de ese backend.

## Superposiciones de MCP incluido

Los backends CLI **no** reciben llamadas a herramientas de OpenClaw directamente, pero un backend puede habilitar una superposición generada de configuración MCP con `bundleMcp: true`.

Comportamiento incluido actual:

  * `claude-cli`: archivo de configuración MCP estricto generado
  * `codex-cli`: sobrescrituras de configuración en línea para `mcp_servers`; el servidor local loopback generado de OpenClaw se marca con el modo de aprobación de herramientas por servidor de Codex para que las llamadas MCP no puedan quedar bloqueadas por solicitudes locales de aprobación
  * `google-gemini-cli`: archivo de configuración del sistema de Gemini generado


Cuando MCP incluido está habilitado, OpenClaw:

  * inicia un servidor MCP HTTP de loopback que expone herramientas del Gateway al proceso CLI
  * autentica el puente con un token por sesión (`OPENCLAW_MCP_TOKEN`)
  * delimita el acceso a herramientas al contexto de la sesión, la cuenta y el canal actuales
  * carga los servidores bundle-MCP habilitados para el espacio de trabajo actual
  * los fusiona con cualquier forma existente de configuración/ajustes MCP del backend
  * reescribe la configuración de inicio usando el modo de integración propio del backend de la extensión propietaria


Si no hay servidores MCP habilitados, OpenClaw aún inyecta una configuración estricta cuando un backend habilita MCP incluido para que las ejecuciones en segundo plano permanezcan aisladas.

Los runtimes MCP incluidos con alcance de sesión se almacenan en caché para reutilizarse dentro de una sesión y luego se eliminan tras `mcp.sessionIdleTtlMs` milisegundos de inactividad (valor predeterminado: 10 minutos; establece `0` para deshabilitarlo). Las ejecuciones incrustadas de una sola vez, como pruebas de autenticación, generación de slugs y recuperación de active-memory, solicitan la limpieza al finalizar la ejecución para que los procesos secundarios stdio y los flujos HTTP/SSE Streamable no sobrevivan a la ejecución.

## Limitaciones

  * **Sin llamadas directas a herramientas de OpenClaw.** OpenClaw no inyecta llamadas a herramientas en el protocolo del backend CLI. Los backends solo ven herramientas del Gateway cuando habilitan `bundleMcp: true`.
  * **El streaming depende del backend.** Algunos backends transmiten JSONL; otros almacenan en búfer hasta salir.
  * **Las salidas estructuradas** dependen del formato JSON de la CLI.
  * **Las sesiones de Codex CLI** se reanudan mediante salida de texto (sin JSONL), que es menos estructurada que la ejecución inicial con `--json`. Las sesiones de OpenClaw siguen funcionando normalmente.


## Solución de problemas

  * **No se encuentra la CLI** : establece `command` en una ruta completa.
  * **Nombre de modelo incorrecto** : usa `modelAliases` para asignar `provider/model` → modelo de CLI.
  * **Sin continuidad de sesión** : asegúrate de que `sessionArg` esté establecido y de que `sessionMode` no sea `none` (Codex CLI actualmente no puede reanudarse con salida JSON).
  * **Imágenes ignoradas** : establece `imageArg` (y verifica que la CLI admita rutas de archivo).


## Relacionado

  * [Runbook del Gateway](</es/gateway>)
  * [Modelos locales](</es/gateway/local-models>)


Was this useful?YesNo