---
title: Configuración
source_url: https://docs.openclaw.ai/es/gateway/configuration
scraped_at: 2026-05-25
---

OpenClaw lee una configuración opcional **JSON5** desde `~/.openclaw/openclaw.json`. La ruta de configuración activa debe ser un archivo normal. Los diseños de `openclaw.json` con enlaces simbólicos no son compatibles con las escrituras propiedad de OpenClaw; una escritura atómica puede reemplazar la ruta en lugar de preservar el enlace simbólico. Si mantienes la configuración fuera del directorio de estado predeterminado, apunta `OPENCLAW_CONFIG_PATH` directamente al archivo real.

Si el archivo no existe, OpenClaw usa valores predeterminados seguros. Motivos habituales para añadir una configuración:

  * Conectar canales y controlar quién puede enviar mensajes al bot
  * Definir modelos, herramientas, aislamiento o automatización (cron, hooks)
  * Ajustar sesiones, medios, red o UI


Consulta la [referencia completa](</es/gateway/configuration-reference>) para ver todos los campos disponibles.

Los agentes y la automatización deben usar `config.schema.lookup` para obtener documentación exacta a nivel de campo antes de editar la configuración. Usa esta página como guía orientada a tareas y la [Referencia de configuración](</es/gateway/configuration-reference>) para el mapa de campos y valores predeterminados más amplio.

## Configuración mínima

json5Copy code
[code]
    // ~/.openclaw/openclaw.json{  agents: { defaults: { workspace: "~/.openclaw/workspace" } },  channels: { whatsapp: { allowFrom: ["+15555550123"] } },}
[/code]

## Editar la configuración

### Asistente interactivo

bashCopy code
[code]
    openclaw onboard       # full onboarding flowopenclaw configure     # config wizard
[/code]

### CLI (comandos de una línea)

bashCopy code
[code]
    openclaw config get agents.defaults.workspaceopenclaw config set agents.defaults.heartbeat.every "2h"openclaw config unset plugins.entries.brave.config.webSearch.apiKey
[/code]

### UI de control

Abre <http://127.0.0.1:18789> y usa la pestaña **Configuración**. La UI de control renderiza un formulario a partir del esquema de configuración en vivo, incluidos los metadatos de documentación de campos `title` / `description`, además de los esquemas de plugins y canales cuando están disponibles, con un editor **JSON sin procesar** como vía de escape. Para UI de exploración detallada y otras herramientas, el Gateway también expone `config.schema.lookup` para obtener un nodo de esquema acotado por ruta más resúmenes inmediatos de sus hijos.

### Edición directa

Edita `~/.openclaw/openclaw.json` directamente. El Gateway vigila el archivo y aplica los cambios automáticamente (consulta recarga en caliente).

## Validación estricta

`openclaw config schema` imprime el JSON Schema canónico usado por la UI de control y la validación. `config.schema.lookup` obtiene un único nodo acotado por ruta más resúmenes de hijos para herramientas de exploración detallada. Los metadatos de documentación de campos `title`/`description` se propagan a través de objetos anidados, comodines (`*`), elementos de array (`[]`) y ramas `anyOf`/ `oneOf`/`allOf`. Los esquemas de plugins y canales en tiempo de ejecución se fusionan cuando se carga el registro de manifiestos.

Cuando falla la validación:

  * El Gateway no arranca
  * Solo funcionan los comandos de diagnóstico (`openclaw doctor`, `openclaw logs`, `openclaw health`, `openclaw status`)
  * Ejecuta `openclaw doctor` para ver los problemas exactos
  * Ejecuta `openclaw doctor --fix` (o `--yes`) para aplicar reparaciones


El Gateway conserva una copia confiable de la última configuración válida después de cada inicio correcto, pero el inicio y la recarga en caliente no la restauran automáticamente. Si `openclaw.json` falla la validación (incluida la validación local del plugin), el inicio del Gateway falla o se omite la recarga y el runtime actual conserva la última configuración aceptada. Ejecuta `openclaw doctor --fix` (o `--yes`) para reparar configuraciones con prefijos/sobrescritas o restaurar la copia de última configuración válida. La promoción a última configuración válida se omite cuando un candidato contiene marcadores de secretos redactados como `***`.

## Tareas comunes

Configurar un canal (WhatsApp, Telegram, Discord, etc.)

Cada canal tiene su propia sección de configuración bajo `channels.<provider>`. Consulta la página dedicada del canal para ver los pasos de configuración:

  * [WhatsApp](</es/channels/whatsapp>) \- `channels.whatsapp`
  * [Telegram](</es/channels/telegram>) \- `channels.telegram`
  * [Discord](</es/channels/discord>) \- `channels.discord`
  * [Feishu](</es/channels/feishu>) \- `channels.feishu`
  * [Google Chat](</es/channels/googlechat>) \- `channels.googlechat`
  * [Microsoft Teams](</es/channels/msteams>) \- `channels.msteams`
  * [Slack](</es/channels/slack>) \- `channels.slack`
  * [Signal](</es/channels/signal>) \- `channels.signal`
  * [iMessage](</es/channels/imessage>) \- `channels.imessage`
  * [Mattermost](</es/channels/mattermost>) \- `channels.mattermost`


Todos los canales comparten el mismo patrón de política de DM:

json5Copy code
[code]
    {  channels: {    telegram: {      enabled: true,      botToken: "123:abc",      dmPolicy: "pairing",   // pairing | allowlist | open | disabled      allowFrom: ["tg:123"], // only for allowlist/open    },  },}
[/code]

Elegir y configurar modelos

Define el modelo principal y los fallbacks opcionales:

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "anthropic/claude-sonnet-4-6",        fallbacks: ["openai/gpt-5.4"],      },      models: {        "anthropic/claude-sonnet-4-6": { alias: "Sonnet" },        "openai/gpt-5.4": { alias: "GPT" },      },    },  },}
[/code]

  * `agents.defaults.models` define el catálogo de modelos y actúa como allowlist para `/model`; las entradas `provider/*` filtran `/model`, `/models` y los selectores de modelos a los proveedores seleccionados mientras siguen usando descubrimiento dinámico de modelos.
  * Usa `openclaw config set agents.defaults.models '<json>' --strict-json --merge` para añadir entradas a la allowlist sin eliminar modelos existentes. Los reemplazos planos que eliminarían entradas se rechazan a menos que pases `--replace`.
  * Las referencias de modelo usan el formato `provider/model` (por ejemplo, `anthropic/claude-opus-4-6`).
  * `agents.defaults.imageMaxDimensionPx` controla la reducción de escala de imágenes de transcripción/herramientas (valor predeterminado `1200`); valores más bajos suelen reducir el uso de tokens de visión en ejecuciones con muchas capturas de pantalla.
  * Consulta [CLI de modelos](</es/concepts/models>) para cambiar modelos en el chat y [Conmutación por error de modelos](</es/concepts/model-failover>) para la rotación de autenticación y el comportamiento de fallback.
  * Para proveedores personalizados/autohospedados, consulta [Proveedores personalizados](</es/gateway/config-tools#custom-providers-and-base-urls>) en la referencia.

Controlar quién puede enviar mensajes al bot

El acceso por DM se controla por canal mediante `dmPolicy`:

  * `"pairing"` (predeterminado): los remitentes desconocidos reciben un código de vinculación de un solo uso para aprobación
  * `"allowlist"`: solo remitentes en `allowFrom` (o en el almacén de permisos vinculados)
  * `"open"`: permite todos los DM entrantes (requiere `allowFrom: ["*"]`)
  * `"disabled"`: ignora todos los DM


Para grupos, usa `groupPolicy` \+ `groupAllowFrom` o allowlists específicas del canal.

Consulta la [referencia completa](</es/gateway/config-channels#dm-and-group-access>) para ver detalles por canal.

Configurar el control de menciones en chats grupales

Los mensajes grupales requieren **mención** de forma predeterminada. Configura patrones de activación por agente y mantén las respuestas visibles de sala en la ruta predeterminada de herramienta de mensajes, a menos que quieras intencionalmente respuestas finales automáticas heredadas:

json5Copy code
[code]
    {  messages: {    visibleReplies: "automatic", // set "message_tool" to require message-tool sends everywhere    groupChat: {      visibleReplies: "message_tool", // default; use "automatic" for legacy room replies    },  },  agents: {    list: [      {        id: "main",        groupChat: {          mentionPatterns: ["@openclaw", "openclaw"],        },      },    ],  },  channels: {    whatsapp: {      groups: { "*": { requireMention: true } },    },  },}
[/code]

  * **Menciones de metadatos** : @-menciones nativas (mencionar tocando en WhatsApp, @bot de Telegram, etc.)
  * **Patrones de texto** : patrones regex seguros en `mentionPatterns`
  * **Respuestas visibles** : `messages.visibleReplies` puede requerir envíos mediante herramienta de mensajes globalmente; `messages.groupChat.visibleReplies` lo sobrescribe para grupos/canales.
  * Consulta la [referencia completa](</es/gateway/config-channels#group-chat-mention-gating>) para los modos de respuesta visible, las sobrescrituras por canal y el modo de chat consigo mismo.

Restringir Skills por agente

Usa `agents.defaults.skills` para una base compartida y luego sobrescribe agentes específicos con `agents.list[].skills`:

json5Copy code
[code]
    {  agents: {    defaults: {      skills: ["github", "weather"],    },    list: [      { id: "writer" }, // inherits github, weather      { id: "docs", skills: ["docs-search"] }, // replaces defaults      { id: "locked-down", skills: [] }, // no skills    ],  },}
[/code]

  * Omite `agents.defaults.skills` para permitir Skills sin restricciones de forma predeterminada.
  * Omite `agents.list[].skills` para heredar los valores predeterminados.
  * Define `agents.list[].skills: []` para no permitir Skills.
  * Consulta [Skills](</es/tools/skills>), [Configuración de Skills](</es/tools/skills-config>) y la [Referencia de configuración](</es/gateway/config-agents#agents-defaults-skills>).

Ajustar la supervisión de estado de canales del Gateway

Controla con qué agresividad el Gateway reinicia canales que parecen obsoletos:

json5Copy code
[code]
    {  gateway: {    channelHealthCheckMinutes: 5,    channelStaleEventThresholdMinutes: 30,    channelMaxRestartsPerHour: 10,  },  channels: {    telegram: {      healthMonitor: { enabled: false },      accounts: {        alerts: {          healthMonitor: { enabled: true },        },      },    },  },}
[/code]

  * Define `gateway.channelHealthCheckMinutes: 0` para desactivar globalmente los reinicios del monitor de estado.
  * `channelStaleEventThresholdMinutes` debe ser mayor o igual que el intervalo de comprobación.
  * Usa `channels.<provider>.healthMonitor.enabled` o `channels.<provider>.accounts.<id>.healthMonitor.enabled` para desactivar los reinicios automáticos de un canal o cuenta sin desactivar el monitor global.
  * Consulta [Comprobaciones de estado](</es/gateway/health>) para depuración operativa y la [referencia completa](</es/gateway/configuration-reference#gateway>) para todos los campos.

Ajustar el timeout del handshake WebSocket del Gateway

Da más tiempo a los clientes locales para completar el handshake WebSocket previo a la autenticación en hosts cargados o de baja potencia:

json5Copy code
[code]
    {  gateway: {    handshakeTimeoutMs: 30000,  },}
[/code]

  * El valor predeterminado es `15000` milisegundos.
  * `OPENCLAW_HANDSHAKE_TIMEOUT_MS` sigue teniendo prioridad para sobrescrituras puntuales de servicio o shell.
  * Prefiere corregir primero los bloqueos de inicio/bucle de eventos; este ajuste es para hosts que están sanos pero son lentos durante el calentamiento.

Configurar sesiones y restablecimientos

Las sesiones controlan la continuidad y el aislamiento de las conversaciones:

json5Copy code
[code]
    {  session: {    dmScope: "per-channel-peer",  // recommended for multi-user    threadBindings: {      enabled: true,      idleHours: 24,      maxAgeHours: 0,    },    reset: {      mode: "daily",      atHour: 4,      idleMinutes: 120,    },  },}
[/code]

  * `dmScope`: `main` (compartido) | `per-peer` | `per-channel-peer` | `per-account-channel-peer`
  * `threadBindings`: valores predeterminados globales para el enrutamiento de sesiones vinculadas a hilos (Discord admite `/focus`, `/unfocus`, `/agents`, `/session idle` y `/session max-age`).
  * Consulta [Gestión de sesiones](</es/concepts/session>) para el alcance, los enlaces de identidad y la política de envío.
  * Consulta la [referencia completa](</es/gateway/config-agents#session>) para ver todos los campos.

Habilitar el aislamiento

Ejecuta sesiones de agente en runtimes de aislamiento aislados:

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "non-main",  // off | non-main | all        scope: "agent",    // session | agent | shared      },    },  },}
[/code]

Compila primero la imagen: desde un checkout de código fuente ejecuta `scripts/sandbox-setup.sh`, o desde una instalación de npm consulta el comando `docker build` en línea en [Aislamiento § Imágenes y configuración](</es/gateway/sandboxing#images-and-setup>).

Consulta [Aislamiento](</es/gateway/sandboxing>) para ver la guía completa y la [referencia completa](</es/gateway/config-agents#agentsdefaultssandbox>) para ver todas las opciones.

Habilitar push respaldado por relay para compilaciones oficiales de iOS

El push respaldado por relay se configura en `openclaw.json`.

Define esto en la configuración del Gateway:

json5Copy code
[code]
    {  gateway: {    push: {      apns: {        relay: {          baseUrl: "https://relay.example.com",          // Optional. Default: 10000          timeoutMs: 10000,        },      },    },  },}
[/code]

Equivalente en CLI:

bashCopy code
[code]
    openclaw config set gateway.push.apns.relay.baseUrl https://relay.example.com
[/code]

Qué hace esto:

  * Permite que el Gateway envíe `push.test`, avisos de activación y activaciones de reconexión a través del relay externo.
  * Usa una concesión de envío con alcance de registro reenviada por la app de iOS emparejada. El Gateway no necesita un token de relay para todo el despliegue.
  * Vincula cada registro respaldado por relay con la identidad del Gateway con la que se emparejó la app de iOS, por lo que otro Gateway no puede reutilizar el registro almacenado.
  * Mantiene las compilaciones locales/manuales de iOS en APNs directas. Los envíos respaldados por relay se aplican solo a las compilaciones distribuidas oficiales que se registraron a través del relay.
  * Debe coincidir con la URL base del relay integrada en la compilación oficial/TestFlight de iOS, para que el tráfico de registro y envío llegue al mismo despliegue del relay.


Flujo de extremo a extremo:

  1. Instala una compilación oficial/TestFlight de iOS compilada con la misma URL base del relay.
  2. Configura `gateway.push.apns.relay.baseUrl` en el Gateway.
  3. Empareja la app de iOS con el Gateway y deja que se conecten tanto las sesiones del nodo como las del operador.
  4. La app de iOS obtiene la identidad del Gateway, se registra con el relay usando App Attest más el recibo de la app y luego publica la carga útil `push.apns.register` respaldada por relay en el Gateway emparejado.
  5. El Gateway almacena el identificador del relay y la concesión de envío, y luego los usa para `push.test`, avisos de activación y activaciones de reconexión.


Notas operativas:

  * Si cambias la app de iOS a un Gateway diferente, vuelve a conectar la app para que pueda publicar un nuevo registro de relay vinculado a ese Gateway.
  * Si publicas una nueva compilación de iOS que apunta a un despliegue de relay diferente, la app actualiza su registro de relay en caché en lugar de reutilizar el origen de relay anterior.


Nota de compatibilidad:

  * `OPENCLAW_APNS_RELAY_BASE_URL` y `OPENCLAW_APNS_RELAY_TIMEOUT_MS` siguen funcionando como sobrescrituras temporales de entorno.
  * `OPENCLAW_APNS_RELAY_ALLOW_HTTP=true` sigue siendo una vía de escape de desarrollo solo para local loopback; no persistas URLs de relay HTTP en la configuración.


Consulta [App de iOS](</es/platforms/ios#relay-backed-push-for-official-builds>) para ver el flujo de extremo a extremo y [Flujo de autenticación y confianza](</es/platforms/ios#authentication-and-trust-flow>) para ver el modelo de seguridad del relay.

Configurar Heartbeat (comprobaciones periódicas) json5Copy code
[code]
    {  agents: {    defaults: {      heartbeat: {        every: "30m",        target: "last",      },    },  },}
[/code]

  * `every`: cadena de duración (`30m`, `2h`). Define `0m` para deshabilitar.
  * `target`: `last` | `none` | `<channel-id>` (por ejemplo `discord`, `matrix`, `telegram` o `whatsapp`)
  * `directPolicy`: `allow` (predeterminado) o `block` para destinos de Heartbeat de estilo DM
  * Consulta [Heartbeat](</es/gateway/heartbeat>) para ver la guía completa.

Configurar trabajos de Cron json5Copy code
[code]
    {  cron: {    enabled: true,    maxConcurrentRuns: 2, // cron dispatch + isolated cron agent-turn execution    sessionRetention: "24h",    runLog: {      maxBytes: "2mb",      keepLines: 2000,    },  },}
[/code]

  * `sessionRetention`: elimina sesiones de ejecución aisladas completadas de `sessions.json` (predeterminado `24h`; define `false` para deshabilitar).
  * `runLog`: recorta `cron/runs/<jobId>.jsonl` por tamaño y líneas conservadas.
  * Consulta [Trabajos de Cron](</es/automation/cron-jobs>) para ver una descripción general de la función y ejemplos de CLI.

Configurar webhooks (hooks)

Habilita endpoints HTTP de Webhook en el Gateway:

json5Copy code
[code]
    {  hooks: {    enabled: true,    token: "shared-secret",    path: "/hooks",    defaultSessionKey: "hook:ingress",    allowRequestSessionKey: false,    allowedSessionKeyPrefixes: ["hook:"],    mappings: [      {        match: { path: "gmail" },        action: "agent",        agentId: "main",        deliver: true,      },    ],  },}
[/code]

Nota de seguridad:

  * Trata todo el contenido de las cargas útiles de hook/Webhook como entrada no confiable.
  * Usa un `hooks.token` dedicado; no reutilices el token compartido del Gateway.
  * La autenticación de hook es solo por encabezado (`Authorization: Bearer ...` o `x-openclaw-token`); los tokens en la cadena de consulta se rechazan.
  * `hooks.path` no puede ser `/`; mantén el ingreso de Webhook en una subruta dedicada, como `/hooks`.
  * Mantén deshabilitadas las marcas de omisión de contenido no seguro (`hooks.gmail.allowUnsafeExternalContent`, `hooks.mappings[].allowUnsafeExternalContent`) salvo para depuración con alcance muy limitado.
  * Si habilitas `hooks.allowRequestSessionKey`, define también `hooks.allowedSessionKeyPrefixes` para acotar las claves de sesión elegidas por el llamador.
  * Para agentes impulsados por hooks, prefiere niveles de modelo modernos y sólidos y una política de herramientas estricta (por ejemplo, solo mensajería más aislamiento cuando sea posible).


Consulta la [referencia completa](</es/gateway/configuration-reference#hooks>) para ver todas las opciones de asignación y la integración con Gmail.

Configurar enrutamiento multiagente

Ejecuta varios agentes aislados con espacios de trabajo y sesiones separados:

json5Copy code
[code]
    {  agents: {    list: [      { id: "home", default: true, workspace: "~/.openclaw/workspace-home" },      { id: "work", workspace: "~/.openclaw/workspace-work" },    ],  },  bindings: [    { agentId: "home", match: { channel: "whatsapp", accountId: "personal" } },    { agentId: "work", match: { channel: "whatsapp", accountId: "biz" } },  ],}
[/code]

Consulta [Multiagente](</es/concepts/multi-agent>) y la [referencia completa](</es/gateway/config-agents#multi-agent-routing>) para ver las reglas de vinculación y los perfiles de acceso por agente.

Dividir la configuración en varios archivos ($include)

Usa `$include` para organizar configuraciones grandes:

json5Copy code
[code]
    // ~/.openclaw/openclaw.json{  gateway: { port: 18789 },  agents: { $include: "./agents.json5" },  broadcast: {    $include: ["./clients/a.json5", "./clients/b.json5"],  },}
[/code]

  * **Archivo único** : reemplaza el objeto contenedor
  * **Matriz de archivos** : se fusiona en profundidad en orden (gana el posterior)
  * **Claves hermanas** : se fusionan después de los includes (sobrescriben los valores incluidos)
  * **Includes anidados** : admitidos hasta 10 niveles de profundidad
  * **Rutas relativas** : se resuelven en relación con el archivo que incluye
  * **Escrituras propiedad de OpenClaw** : cuando una escritura cambia solo una sección de nivel superior respaldada por un include de archivo único como `plugins: { $include: "./plugins.json5" }`, OpenClaw actualiza ese archivo incluido y deja `openclaw.json` intacto
  * **Write-through no admitido** : los includes raíz, las matrices de includes y los includes con sobrescrituras hermanas fallan de forma cerrada para escrituras propiedad de OpenClaw en lugar de aplanar la configuración
  * **Confinamiento** : las rutas de `$include` deben resolverse bajo el directorio que contiene `openclaw.json`. Para compartir un árbol entre máquinas o usuarios, define `OPENCLAW_INCLUDE_ROOTS` como una lista de rutas (`:` en POSIX, `;` en Windows) de directorios adicionales que los includes pueden referenciar. Los enlaces simbólicos se resuelven y se vuelven a comprobar, por lo que una ruta que léxicamente vive en un directorio de configuración pero cuyo destino real escapa de todas las raíces permitidas también se rechaza.
  * **Gestión de errores** : errores claros para archivos faltantes, errores de análisis e includes circulares


## Recarga en caliente de la configuración

El Gateway observa `~/.openclaw/openclaw.json` y aplica los cambios automáticamente; no se necesita reinicio manual para la mayoría de los ajustes.

Las ediciones directas de archivos se tratan como no confiables hasta que se validan. El observador espera a que se estabilice la actividad de escrituras temporales/renombrados del editor, lee el archivo final y rechaza las ediciones externas no válidas sin reescribir `openclaw.json`. Las escrituras de configuración propiedad de OpenClaw usan la misma puerta de esquema antes de escribir; las sobrescrituras destructivas como eliminar `gateway.mode` o reducir el archivo a menos de la mitad se rechazan y se guardan como `.rejected.*` para inspección.

Si ves `config reload skipped (invalid config)` o el arranque informa `Invalid config`, inspecciona la configuración, ejecuta `openclaw config validate` y luego ejecuta `openclaw doctor --fix` para reparar. Consulta [Solución de problemas del Gateway](</es/gateway/troubleshooting#gateway-rejected-invalid-config>) para ver la lista de comprobación.

### Modos de recarga

Modo | Comportamiento  
---|---  
**`hybrid`** (predeterminado) | Aplica en caliente los cambios seguros al instante. Reinicia automáticamente para los críticos.  
**`hot`** | Aplica en caliente solo los cambios seguros. Registra una advertencia cuando se necesita reiniciar; tú te encargas.  
**`restart`** | Reinicia el Gateway ante cualquier cambio de configuración, sea seguro o no.  
**`off`** | Deshabilita la observación de archivos. Los cambios surten efecto en el siguiente reinicio manual.  
json5Copy code
[code]
    {  gateway: {    reload: { mode: "hybrid", debounceMs: 300 },  },}
[/code]

### Qué se aplica en caliente y qué necesita un reinicio

La mayoría de los campos se aplican en caliente sin tiempo de inactividad. En modo `hybrid`, los cambios que requieren reinicio se gestionan automáticamente.

Categoría | Campos | ¿Requiere reinicio?  
---|---|---  
Canales | `channels.*`, `web` (WhatsApp): todos los canales integrados y de Plugin | No  
Agente y modelos | `agent`, `agents`, `models`, `routing` | No  
Automatización | `hooks`, `cron`, `agent.heartbeat` | No  
Sesiones y mensajes | `session`, `messages` | No  
Herramientas y medios | `tools`, `browser`, `skills`, `mcp`, `audio`, `talk` | No  
IU y varios | `ui`, `logging`, `identity`, `bindings` | No  
Servidor Gateway | `gateway.*` (puerto, enlace, autenticación, tailscale, TLS, HTTP) | **Sí**  
Infraestructura | `discovery`, `plugins` | **Sí**  
  
### Planificación de recarga

Cuando editas un archivo fuente referenciado mediante `$include`, OpenClaw planifica la recarga desde el diseño definido en la fuente, no desde la vista aplanada en memoria. Esto mantiene predecibles las decisiones de recarga en caliente (aplicación en caliente frente a reinicio), incluso cuando una única sección de nivel superior vive en su propio archivo incluido, como `plugins: { $include: "./plugins.json5" }`. La planificación de recarga falla de forma cerrada si el diseño de origen es ambiguo.

## RPC de configuración (actualizaciones programáticas)

Para herramientas que escriben configuración mediante la API de Gateway, prefiere este flujo:

  * `config.schema.lookup` para inspeccionar un subárbol (nodo de esquema superficial + resúmenes de hijos)
  * `config.get` para obtener la instantánea actual más `hash`
  * `config.patch` para actualizaciones parciales (parche de fusión JSON: los objetos se fusionan, `null` elimina, los arreglos reemplazan)
  * `config.apply` solo cuando pretendas reemplazar toda la configuración
  * `update.run` para una autoactualización explícita más reinicio; incluye `continuationMessage` cuando la sesión posterior al reinicio deba ejecutar un turno de seguimiento
  * `update.status` para inspeccionar el centinela de reinicio de la actualización más reciente y verificar la versión en ejecución después de un reinicio


Los agentes deben tratar `config.schema.lookup` como el primer punto de consulta para obtener documentación y restricciones exactas a nivel de campo. Usa [Referencia de configuración](</es/gateway/configuration-reference>) cuando necesiten el mapa de configuración más amplio, los valores predeterminados o enlaces a referencias dedicadas de subsistemas.

Ejemplo de parche parcial:

bashCopy code
[code]
    openclaw gateway call config.get --params '{}'  # capture payload.hashopenclaw gateway call config.patch --params '{  "raw": "{ channels: { telegram: { groups: { \"*\": { requireMention: false } } } } }",  "baseHash": "<hash>"}'
[/code]

Tanto `config.apply` como `config.patch` aceptan `raw`, `baseHash`, `sessionKey`, `note` y `restartDelayMs`. `baseHash` es obligatorio para ambos métodos cuando ya existe una configuración.

## Variables de entorno

OpenClaw lee variables de entorno del proceso padre, además de:

  * `.env` desde el directorio de trabajo actual (si está presente)
  * `~/.openclaw/.env` (respaldo global)


Ninguno de los archivos sobrescribe variables de entorno existentes. También puedes definir variables de entorno en línea en la configuración:

json5Copy code
[code]
    {  env: {    OPENROUTER_API_KEY: "sk-or-...",    vars: { GROQ_API_KEY: "gsk-..." },  },}
[/code]

Importación de entorno de shell (opcional)

Si está habilitada y las claves esperadas no están definidas, OpenClaw ejecuta tu shell de inicio de sesión e importa solo las claves faltantes:

json5Copy code
[code]
    {env: {  shellEnv: { enabled: true, timeoutMs: 15000 },},}
[/code]

Variable de entorno equivalente: `OPENCLAW_LOAD_SHELL_ENV=1`

Sustitución de variables de entorno en valores de configuración

Referencia variables de entorno en cualquier valor de cadena de configuración con `${VAR_NAME}`:

json5Copy code
[code]
    {gateway: { auth: { token: "${OPENCLAW_GATEWAY_TOKEN}" } },models: { providers: { custom: { apiKey: "${CUSTOM_API_KEY}" } } },}
[/code]

Reglas:

  * Solo coinciden nombres en mayúsculas: `[A-Z_][A-Z0-9_]*`
  * Las variables faltantes/vacías generan un error en el momento de carga
  * Escapa con `$${VAR}` para salida literal
  * Funciona dentro de archivos `$include`
  * Sustitución en línea: `"${BASE}/v1"` → `"https://api.example.com/v1"`

Referencias secretas (env, archivo, exec)

Para campos que admiten objetos SecretRef, puedes usar:

json5Copy code
[code]
    {models: {  providers: {    openai: { apiKey: { source: "env", provider: "default", id: "OPENAI_API_KEY" } },  },},skills: {  entries: {    "image-lab": {      apiKey: {        source: "file",        provider: "filemain",        id: "/skills/entries/image-lab/apiKey",      },    },  },},channels: {  googlechat: {    serviceAccountRef: {      source: "exec",      provider: "vault",      id: "channels/googlechat/serviceAccount",    },  },},}
[/code]

Los detalles de SecretRef (incluido `secrets.providers` para `env`/`file`/`exec`) están en [Gestión de secretos](</es/gateway/secrets>). Las rutas de credenciales compatibles se enumeran en [Superficie de credenciales de SecretRef](</es/reference/secretref-credential-surface>).

Consulta [Entorno](</es/help/environment>) para ver la precedencia y las fuentes completas.

## Referencia completa

Para la referencia completa campo por campo, consulta **[Referencia de configuración](</es/gateway/configuration-reference>)**.

* * *

_Relacionado:[Ejemplos de configuración](</es/gateway/configuration-examples>) · [Referencia de configuración](</es/gateway/configuration-reference>) · [Doctor](</es/gateway/doctor>)_

## Relacionado

  * [Referencia de configuración](</es/gateway/configuration-reference>)
  * [Ejemplos de configuración](</es/gateway/configuration-examples>)
  * [Manual operativo de Gateway](</es/gateway>)


Was this useful?YesNo