---
title: Infiere
source_url: https://docs.openclaw.ai/es/providers/inferrs
scraped_at: 2026-05-25
---

[inferrs](<https://github.com/ericcurtin/inferrs>) puede servir modelos locales detrás de una API `/v1` compatible con OpenAI. OpenClaw funciona con `inferrs` mediante la ruta genérica `openai-completions`.

Propiedad | Valor  
---|---  
ID de proveedor | `inferrs` (personalizado; configurar en `models.providers.inferrs`)  
Plugin | ninguno — `inferrs` no es un Plugin de proveedor incluido con OpenClaw  
Variable de entorno de autenticación | Opcional. Cualquier valor funciona si tu servidor inferrs no tiene autenticación  
API | Compatible con OpenAI (`openai-completions`)  
URL base sugerida | `http://127.0.0.1:8080/v1` (o donde se ejecute tu servidor inferrs)  
  
## Primeros pasos

* ### Iniciar inferrs con un modelo

bashCopy code
[code]
    inferrs serve google/gemma-4-E2B-it \  --host 127.0.0.1 \  --port 8080 \  --device metal
[/code]

* ### Verificar que el servidor sea accesible

bashCopy code
[code]
    curl http://127.0.0.1:8080/healthcurl http://127.0.0.1:8080/v1/models
[/code]

* ### Añadir una entrada de proveedor de OpenClaw

Añade una entrada de proveedor explícita y apunta tu modelo predeterminado a ella. Consulta el ejemplo completo de configuración a continuación.

## Ejemplo de configuración completo

Este ejemplo usa Gemma 4 en un servidor local `inferrs`.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "inferrs/google/gemma-4-E2B-it" },      models: {        "inferrs/google/gemma-4-E2B-it": {          alias: "Gemma 4 (inferrs)",        },      },    },  },  models: {    mode: "merge",    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

## Inicio bajo demanda

OpenClaw también puede iniciar Inferrs solo cuando se selecciona un modelo `inferrs/...`. Añade `localService` a la misma entrada de proveedor:

json5Copy code
[code]
    {  models: {    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/opt/homebrew/bin/inferrs",          args: [            "serve",            "google/gemma-4-E2B-it",            "--host",            "127.0.0.1",            "--port",            "8080",            "--device",            "metal",          ],          healthUrl: "http://127.0.0.1:8080/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

`command` debe ser absoluto. Usa `which inferrs` en el host del Gateway y coloca esa ruta en la configuración. Para la referencia completa de campos, consulta [Servicios de modelos locales](</es/gateway/local-model-services>).

## Configuración avanzada

Por qué requiresStringContent importa

Algunas rutas de Chat Completions de `inferrs` solo aceptan `messages[].content` como cadena, no matrices estructuradas de partes de contenido.

json5Copy code
[code]
    compat: {  requiresStringContent: true}
[/code]

OpenClaw convertirá las partes de contenido de texto puro en cadenas simples antes de enviar la solicitud.

Advertencia sobre Gemma y el esquema de herramientas

Algunas combinaciones actuales de `inferrs` \+ Gemma aceptan solicitudes directas pequeñas a `/v1/chat/completions`, pero aun así fallan en turnos completos del entorno de ejecución de agentes de OpenClaw.

Si eso ocurre, prueba esto primero:

json5Copy code
[code]
    compat: {  requiresStringContent: true,  supportsTools: false}
[/code]

Eso desactiva la superficie de esquema de herramientas de OpenClaw para el modelo y puede reducir la presión del prompt en backends locales más estrictos.

Si las solicitudes directas mínimas aún funcionan, pero los turnos normales de agentes de OpenClaw siguen fallando dentro de `inferrs`, el problema restante suele ser comportamiento ascendente del modelo o servidor, no la capa de transporte de OpenClaw.

Prueba de humo manual

Una vez configurado, prueba ambas capas:

bashCopy code
[code]
    curl http://127.0.0.1:8080/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"google/gemma-4-E2B-it","messages":[{"role":"user","content":"What is 2 + 2?"}],"stream":false}'
[/code]

bashCopy code
[code]
    openclaw infer model run \  --model inferrs/google/gemma-4-E2B-it \  --prompt "What is 2 + 2? Reply with one short sentence." \  --json
[/code]

Si el primer comando funciona pero el segundo falla, revisa la sección de solución de problemas a continuación.

Comportamiento de estilo proxy

`inferrs` se trata como un backend `/v1` de estilo proxy compatible con OpenAI, no como un endpoint nativo de OpenAI.

  * La adaptación de solicitudes exclusiva de OpenAI nativo no se aplica aquí
  * Sin `service_tier`, sin Responses `store`, sin indicaciones de caché de prompts y sin adaptación de carga útil de compatibilidad de razonamiento de OpenAI
  * Los encabezados ocultos de atribución de OpenClaw (`originator`, `version`, `User-Agent`) no se inyectan en URL base personalizadas de `inferrs`


## Solución de problemas

curl /v1/models falla

`inferrs` no se está ejecutando, no es accesible o no está enlazado al host/puerto esperado. Asegúrate de que el servidor esté iniciado y escuchando en la dirección que configuraste.

messages[].content esperaba una cadena

Define `compat.requiresStringContent: true` en la entrada del modelo. Consulta la sección `requiresStringContent` anterior para obtener detalles.

Las llamadas directas a /v1/chat/completions pasan, pero openclaw infer model run falla

Prueba definir `compat.supportsTools: false` para desactivar la superficie de esquema de herramientas. Consulta la advertencia sobre el esquema de herramientas de Gemma anterior.

inferrs sigue fallando en turnos de agente más grandes

Si OpenClaw ya no recibe errores de esquema, pero `inferrs` sigue fallando en turnos de agente más grandes, trátalo como una limitación ascendente de `inferrs` o del modelo. Reduce la presión del prompt o cambia a otro backend o modelo local.

## Relacionado

[**Modelos locales** Ejecutar OpenClaw contra servidores de modelos locales. ](</es/gateway/local-models>) [**Servicios de modelos locales** Iniciar servidores de modelos locales bajo demanda para proveedores configurados. ](</es/gateway/local-model-services>) [**Solución de problemas del Gateway** Depurar backends locales compatibles con OpenAI que pasan las pruebas, pero fallan en ejecuciones de agentes. ](</es/gateway/troubleshooting#local-openai-compatible-backend-passes-direct-probes-but-agent-runs-fail>) [**Selección de modelos** Resumen de todos los proveedores, referencias de modelo y comportamiento de conmutación por error. ](</es/concepts/model-providers>)

Was this useful?YesNo