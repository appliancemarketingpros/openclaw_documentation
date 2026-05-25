---
title: Servicios de modelos locales
source_url: https://docs.openclaw.ai/es/gateway/local-model-services
scraped_at: 2026-05-25
---

`models.providers.<id>.localService` permite que OpenClaw inicie bajo demanda un servidor de modelos local propiedad del proveedor. Es configuración a nivel de proveedor: cuando el modelo seleccionado pertenece a ese proveedor, OpenClaw sondea el servicio, inicia el proceso si el endpoint está inactivo, espera a que esté listo y luego envía la solicitud del modelo.

Úsalo para servidores locales que sean costosos de mantener ejecutándose todo el día, o para configuraciones manuales donde la selección del modelo debería bastar para levantar el backend.

## Cómo funciona

  1. Una solicitud de modelo se resuelve en un proveedor configurado.
  2. Si ese proveedor tiene `localService`, OpenClaw sondea `healthUrl`.
  3. Si el sondeo se realiza correctamente, OpenClaw usa el servidor existente.
  4. Si el sondeo falla, OpenClaw inicia `command` con `args`.
  5. OpenClaw sondea la disponibilidad hasta que vence `readyTimeoutMs`.
  6. La solicitud del modelo se envía a través del transporte normal del proveedor.
  7. Si OpenClaw inició el proceso y `idleStopMs` es positivo, el proceso se detiene después de que la última solicitud en curso haya estado inactiva durante ese tiempo.


OpenClaw no instala launchd, systemd, Docker ni un daemon para esto. El servidor es un proceso hijo del proceso de OpenClaw que lo necesitó primero.

## Estructura de configuración

json5Copy code
[code]
    {  models: {    providers: {      local: {        baseUrl: "http://127.0.0.1:8000/v1",        apiKey: "local-model",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/absolute/path/to/server",          args: ["--host", "127.0.0.1", "--port", "8000"],          cwd: "/absolute/path/to/working-dir",          env: { LOCAL_MODEL_CACHE: "/absolute/path/to/cache" },          healthUrl: "http://127.0.0.1:8000/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "my-local-model",            name: "My Local Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## Campos

  * `command`: ruta absoluta del ejecutable. No se usa la búsqueda del shell.
  * `args`: argumentos del proceso. No se aplican expansión del shell, tuberías, globbing ni reglas de entrecomillado.
  * `cwd`: directorio de trabajo opcional para el proceso.
  * `env`: variables de entorno opcionales combinadas sobre el entorno del proceso de OpenClaw.
  * `healthUrl`: URL de disponibilidad. Si se omite, OpenClaw añade `/models` a `baseUrl`, por lo que `http://127.0.0.1:8000/v1` pasa a ser `http://127.0.0.1:8000/v1/models`.
  * `readyTimeoutMs`: plazo límite de disponibilidad al iniciar. Predeterminado: `120000`.
  * `idleStopMs`: retardo de apagado por inactividad para procesos iniciados por OpenClaw. `0` u omitido mantiene el proceso activo hasta que OpenClaw salga.


## Ejemplo de Inferrs

Inferrs es un backend `/v1` personalizado compatible con OpenAI, por lo que la misma API de servicio local funciona con la entrada del proveedor `inferrs`.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "inferrs/google/gemma-4-E2B-it" },    },  },  models: {    mode: "merge",    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/opt/homebrew/bin/inferrs",          args: [            "serve",            "google/gemma-4-E2B-it",            "--host",            "127.0.0.1",            "--port",            "8080",            "--device",            "metal",          ],          healthUrl: "http://127.0.0.1:8080/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

Sustituye `command` por el resultado de `which inferrs` en la máquina que ejecuta OpenClaw.

## Ejemplo de ds4

json5Copy code
[code]
    {  models: {    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/Users/you/Projects/oss/ds4/ds4-server",          args: [            "--model",            "/Users/you/Projects/oss/ds4/ds4flash.gguf",            "--host",            "127.0.0.1",            "--port",            "18000",            "--ctx",            "393216",          ],          cwd: "/Users/you/Projects/oss/ds4",          healthUrl: "http://127.0.0.1:18000/v1/models",          readyTimeoutMs: 300000,          idleStopMs: 0,        },        models: [],      },    },  },}
[/code]

## Notas operativas

  * Un proceso de OpenClaw administra el hijo que inició. Otro proceso de OpenClaw que vea que la misma URL de estado ya está activa la reutilizará sin adoptarla.
  * El inicio se serializa por comando de proveedor y conjunto de argumentos, por lo que las solicitudes concurrentes no generan servidores duplicados para la misma configuración.
  * Las respuestas de streaming activas mantienen una concesión; el apagado por inactividad espera hasta que se complete el manejo del cuerpo de la respuesta.
  * Usa `timeoutSeconds` en proveedores locales lentos para que los arranques en frío y las generaciones largas no alcancen el tiempo de espera predeterminado de solicitud de modelo.
  * Usa un `healthUrl` explícito si tu servidor expone la disponibilidad en un lugar distinto de `/v1/models`.


## Relacionado

[**Local models** Configuración de modelos locales, opciones de proveedor y guía de seguridad. ](</es/gateway/local-models>) [**Inferrs** Ejecuta OpenClaw a través del servidor local compatible con OpenAI de inferrs. ](</es/providers/inferrs>)

Was this useful?YesNo