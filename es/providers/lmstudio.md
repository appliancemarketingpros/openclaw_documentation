---
title: LM Studio
source_url: https://docs.openclaw.ai/es/providers/lmstudio
scraped_at: 2026-05-25
---

LM Studio es una aplicación amigable pero potente para ejecutar modelos de peso abierto en tu propio hardware. Te permite ejecutar modelos llama.cpp (GGUF) o MLX (Apple Silicon). Viene en un paquete con GUI o como daemon sin interfaz (`llmster`). Para la documentación del producto y la configuración, consulta [lmstudio.ai](<https://lmstudio.ai/>).

## Inicio rápido

  1. Instala LM Studio (escritorio) o `llmster` (sin interfaz) y luego inicia el servidor local:

bashCopy code
[code]
    curl -fsSL https://lmstudio.ai/install.sh | bash
[/code]

  2. Inicia el servidor


Asegúrate de iniciar la aplicación de escritorio o ejecutar el daemon con el siguiente comando:

bashCopy code
[code]
    lms daemon up
[/code]

bashCopy code
[code]
    lms server start --port 1234
[/code]

Si estás usando la aplicación, asegúrate de tener JIT habilitado para una experiencia fluida. Obtén más información en la [guía de JIT y TTL de LM Studio](<https://lmstudio.ai/docs/developer/core/ttl-and-auto-evict>).

  3. Si la autenticación de LM Studio está habilitada, define `LM_API_TOKEN`:

bashCopy code
[code]
    export LM_API_TOKEN="your-lm-studio-api-token"
[/code]

Si la autenticación de LM Studio está deshabilitada, puedes dejar la clave de API en blanco durante la configuración interactiva de OpenClaw.

Para detalles de configuración de autenticación de LM Studio, consulta [Autenticación de LM Studio](<https://lmstudio.ai/docs/developer/core/authentication>).

  4. Ejecuta la incorporación y elige `LM Studio`:

bashCopy code
[code]
    openclaw onboard
[/code]

  5. En la incorporación, usa el aviso `Default model` para elegir tu modelo de LM Studio.


También puedes definirlo o cambiarlo más adelante:

bashCopy code
[code]
    openclaw models set lmstudio/qwen/qwen3.5-9b
[/code]

Las claves de modelos de LM Studio siguen un formato `author/model-name` (por ejemplo, `qwen/qwen3.5-9b`). Las referencias de modelos de OpenClaw anteponen el nombre del proveedor: `lmstudio/qwen/qwen3.5-9b`. Puedes encontrar la clave exacta de un modelo ejecutando `curl http://localhost:1234/api/v1/models` y mirando el campo `key`.

## Incorporación no interactiva

Usa la incorporación no interactiva cuando quieras automatizar la configuración mediante scripts (CI, aprovisionamiento, arranque remoto):

bashCopy code
[code]
    openclaw onboard \  --non-interactive \  --accept-risk \  --auth-choice lmstudio
[/code]

O especifica la URL base, el modelo y la clave de API opcional:

bashCopy code
[code]
    openclaw onboard \  --non-interactive \  --accept-risk \  --auth-choice lmstudio \  --custom-base-url http://localhost:1234/v1 \  --lmstudio-api-key "$LM_API_TOKEN" \  --custom-model-id qwen/qwen3.5-9b
[/code]

`--custom-model-id` toma la clave del modelo tal como la devuelve LM Studio (por ejemplo, `qwen/qwen3.5-9b`), sin el prefijo de proveedor `lmstudio/`.

Para servidores de LM Studio autenticados, pasa `--lmstudio-api-key` o define `LM_API_TOKEN`. Para servidores de LM Studio sin autenticación, omite la clave; OpenClaw almacena un marcador local no secreto.

`--custom-api-key` sigue siendo compatible por compatibilidad, pero se prefiere `--lmstudio-api-key` para LM Studio.

Esto escribe `models.providers.lmstudio` y establece el modelo predeterminado en `lmstudio/<custom-model-id>`. Cuando proporcionas una clave de API, la configuración también escribe el perfil de autenticación `lmstudio:default`.

La configuración interactiva puede solicitar una longitud de contexto de carga preferida opcional y la aplica en todos los modelos de LM Studio descubiertos que guarda en la configuración. La configuración del Plugin de LM Studio confía en el endpoint de LM Studio configurado para solicitudes de modelos, incluidos hosts loopback, LAN y tailnet. Puedes desactivarlo definiendo `models.providers.lmstudio.request.allowPrivateNetwork: false`.

## Configuración

### Compatibilidad con uso en streaming

LM Studio es compatible con uso en streaming. Cuando no emite un objeto `usage` con la forma de OpenAI, OpenClaw recupera los conteos de tokens desde metadatos de estilo llama.cpp `timings.prompt_n` / `timings.predicted_n`.

El mismo comportamiento de uso en streaming se aplica a estos backends locales compatibles con OpenAI:

  * vLLM
  * SGLang
  * llama.cpp
  * LocalAI
  * Jan
  * TabbyAPI
  * text-generation-webui


### Compatibilidad con razonamiento

Cuando el descubrimiento `/api/v1/models` de LM Studio informa opciones de razonamiento específicas del modelo, OpenClaw expone los valores `reasoning_effort` compatibles con OpenAI correspondientes en los metadatos de compatibilidad del modelo. Las compilaciones actuales de LM Studio pueden anunciar opciones binarias de interfaz como `allowed_options: ["off", "on"]` mientras rechazan esos valores en `/v1/chat/completions`; OpenClaw normaliza esa forma de descubrimiento binaria a `none`, `minimal`, `low`, `medium`, `high` y `xhigh` antes de enviar solicitudes. La configuración guardada antigua de LM Studio que contiene mapas de razonamiento `off`/`on` se normaliza del mismo modo cuando se carga el catálogo.

### Configuración explícita

json5Copy code
[code]
    {  models: {    providers: {      lmstudio: {        baseUrl: "http://localhost:1234/v1",        apiKey: "${LM_API_TOKEN}",        api: "openai-completions",        models: [          {            id: "qwen/qwen3-coder-next",            name: "Qwen 3 Coder Next",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## Solución de problemas

### LM Studio no detectado

Asegúrate de que LM Studio esté en ejecución. Si la autenticación está habilitada, define también `LM_API_TOKEN`:

bashCopy code
[code]
    # Start via desktop app, or headless:lms server start --port 1234
[/code]

Verifica que la API sea accesible:

bashCopy code
[code]
    curl http://localhost:1234/api/v1/models
[/code]

### Errores de autenticación (HTTP 401)

Si la configuración informa HTTP 401, verifica tu clave de API:

  * Comprueba que `LM_API_TOKEN` coincida con la clave configurada en LM Studio.
  * Para detalles de configuración de autenticación de LM Studio, consulta [Autenticación de LM Studio](<https://lmstudio.ai/docs/developer/core/authentication>).
  * Si tu servidor no requiere autenticación, deja la clave en blanco durante la configuración.


### Carga de modelos justo a tiempo

LM Studio admite la carga de modelos justo a tiempo (JIT), donde los modelos se cargan en la primera solicitud. OpenClaw precarga los modelos mediante el endpoint de carga nativo de LM Studio de forma predeterminada, lo que ayuda cuando JIT está deshabilitado. Para permitir que el JIT, el TTL de inactividad y el comportamiento de expulsión automática de LM Studio controlen el ciclo de vida del modelo, deshabilita el paso de precarga de OpenClaw:

json5Copy code
[code]
    {  models: {    providers: {      lmstudio: {        baseUrl: "http://localhost:1234/v1",        api: "openai-completions",        params: { preload: false },        models: [{ id: "qwen/qwen3.5-9b" }],      },    },  },}
[/code]

### Host de LM Studio en LAN o tailnet

Usa la dirección accesible del host de LM Studio, conserva `/v1` y asegúrate de que LM Studio esté enlazado más allá de loopback en esa máquina:

json5Copy code
[code]
    {  models: {    providers: {      lmstudio: {        baseUrl: "http://gpu-box.local:1234/v1",        apiKey: "lmstudio",        api: "openai-completions",        models: [{ id: "qwen/qwen3.5-9b" }],      },    },  },}
[/code]

A diferencia de los proveedores genéricos compatibles con OpenAI, `lmstudio` confía automáticamente en su endpoint local/privado configurado para solicitudes de modelos protegidas. Los ID de proveedor personalizados de loopback como `localhost` o `127.0.0.1` también se consideran de confianza automáticamente; para ID de proveedor personalizados de LAN, tailnet o DNS privado, define explícitamente `models.providers.<id>.request.allowPrivateNetwork: true`.

## Relacionado

  * [Selección de modelos](</es/concepts/model-providers>)
  * [Ollama](</es/providers/ollama>)
  * [Modelos locales](</es/gateway/local-models>)


Was this useful?YesNo