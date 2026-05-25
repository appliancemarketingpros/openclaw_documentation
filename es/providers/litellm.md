---
title: LiteLLM
source_url: https://docs.openclaw.ai/es/providers/litellm
scraped_at: 2026-05-25
---

[LiteLLM](<https://litellm.ai>) es un Gateway LLM de código abierto que proporciona una API unificada para más de 100 proveedores de modelos. Enruta OpenClaw a través de LiteLLM para obtener seguimiento centralizado de costos, registros y la flexibilidad de cambiar de backends sin modificar tu configuración de OpenClaw.

## Inicio rápido

### Incorporación (recomendado)

**Ideal para:** la ruta más rápida hacia una configuración funcional de LiteLLM.

* ### Ejecutar la incorporación

bashCopy code
[code]
    openclaw onboard --auth-choice litellm-api-key
[/code]

Para una configuración no interactiva contra un proxy remoto, pasa explícitamente la URL del proxy:

bashCopy code
[code]
    openclaw onboard --non-interactive --auth-choice litellm-api-key --litellm-api-key "$LITELLM_API_KEY" --custom-base-url "https://litellm.example/v1"
[/code]

### Configuración manual

**Ideal para:** control total sobre la instalación y la configuración.

* ### Iniciar el proxy de LiteLLM

bashCopy code
[code]
    pip install 'litellm[proxy]'litellm --model claude-opus-4-6
[/code]

* ### Apuntar OpenClaw a LiteLLM

bashCopy code
[code]
    export LITELLM_API_KEY="your-litellm-key" openclaw
[/code]

Eso es todo. OpenClaw ahora se enruta a través de LiteLLM.

## Configuración

### Variables de entorno

bashCopy code
[code]
    export LITELLM_API_KEY="sk-litellm-key"
[/code]

### Archivo de configuración

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",        api: "openai-completions",        models: [          {            id: "claude-opus-4-6",            name: "Claude Opus 4.6",            reasoning: true,            input: ["text", "image"],            contextWindow: 200000,            maxTokens: 64000,          },          {            id: "gpt-4o",            name: "GPT-4o",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "litellm/claude-opus-4-6" },    },  },}
[/code]

## Configuración avanzada

### Generación de imágenes

LiteLLM también puede respaldar la herramienta `image_generate` mediante rutas compatibles con OpenAI `/images/generations` y `/images/edits`. Configura un modelo de imagen de LiteLLM en `agents.defaults.imageGenerationModel`:

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",      },    },  },  agents: {    defaults: {      imageGenerationModel: {        primary: "litellm/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

Las URL de LiteLLM de local loopback como `http://localhost:4000` funcionan sin una anulación global de red privada. Para un proxy alojado en LAN, establece `models.providers.litellm.request.allowPrivateNetwork: true` porque la clave de API se enviará al host de proxy configurado.

Claves virtuales

Crea una clave dedicada para OpenClaw con límites de gasto:

bashCopy code
[code]
    curl -X POST "http://localhost:4000/key/generate" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \  -H "Content-Type: application/json" \  -d '{    "key_alias": "openclaw",    "max_budget": 50.00,    "budget_duration": "monthly"  }'
[/code]

Usa la clave generada como `LITELLM_API_KEY`.

Enrutamiento de modelos

LiteLLM puede enrutar solicitudes de modelos a distintos backends. Configúralo en tu `config.yaml` de LiteLLM:

yamlCopy code
[code]
    model_list:  - model_name: claude-opus-4-6    litellm_params:      model: claude-opus-4-6      api_key: os.environ/ANTHROPIC_API_KEY   - model_name: gpt-4o    litellm_params:      model: gpt-4o      api_key: os.environ/OPENAI_API_KEY
[/code]

OpenClaw sigue solicitando `claude-opus-4-6`; LiteLLM se encarga del enrutamiento.

Ver uso

Consulta el panel o la API de LiteLLM:

bashCopy code
[code]
    # Key infocurl "http://localhost:4000/key/info" \  -H "Authorization: Bearer sk-litellm-key" # Spend logscurl "http://localhost:4000/spend/logs" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY"
[/code]

Notas sobre el comportamiento del proxy

  * LiteLLM se ejecuta en `http://localhost:4000` de forma predeterminada
  * OpenClaw se conecta a través del endpoint `/v1` compatible con OpenAI de estilo proxy de LiteLLM
  * La conformación de solicitudes exclusiva de OpenAI nativa no se aplica a través de LiteLLM: sin `service_tier`, sin `store` de Responses, sin indicaciones de caché de prompts y sin conformación de payload de compatibilidad con razonamiento de OpenAI
  * Los encabezados de atribución ocultos de OpenClaw (`originator`, `version`, `User-Agent`) no se inyectan en URL base personalizadas de LiteLLM


## Relacionado

[**Documentación de LiteLLM** Documentación oficial y referencia de API de LiteLLM. ](<https://docs.litellm.ai>) [**Selección de modelos** Resumen de todos los proveedores, referencias de modelos y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Configuración** Referencia completa de configuración. ](</es/gateway/configuration>) [**Selección de modelos** Cómo elegir y configurar modelos. ](</es/concepts/models>)

Was this useful?YesNo