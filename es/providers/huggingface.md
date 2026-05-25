---
title: Hugging Face (inference)
source_url: https://docs.openclaw.ai/es/providers/huggingface
scraped_at: 2026-05-25
---

[Hugging Face Inference Providers](<https://huggingface.co/docs/inference-providers>) ofrecen chat completions compatibles con OpenAI a través de una única API de router. Obtienes acceso a muchos modelos (DeepSeek, Llama y más) con un solo token. OpenClaw usa el **endpoint compatible con OpenAI** (solo chat completions); para texto a imagen, embeddings o speech usa directamente los [clientes de inferencia de HF](<https://huggingface.co/docs/api-inference/quicktour>).

  * Proveedor: `huggingface`
  * Auth: `HUGGINGFACE_HUB_TOKEN` o `HF_TOKEN` (token de granularidad fina con **Make calls to Inference Providers**)
  * API: compatible con OpenAI (`https://router.huggingface.co/v1`)
  * Facturación: un único token de HF; el [precio](<https://huggingface.co/docs/inference-providers/pricing>) sigue las tarifas del proveedor con un nivel gratuito.


## Primeros pasos

* ### Crear un token de granularidad fina

Ve a [Hugging Face Settings Tokens](<https://huggingface.co/settings/tokens/new?ownUserPermissions=inference.serverless.write&tokenType=fineGrained>) y crea un nuevo token de granularidad fina.

* ### Ejecutar la incorporación

Elige **Hugging Face** en el desplegable de proveedores y luego introduce tu clave API cuando se te solicite:

bashCopy code
[code]
    openclaw onboard --auth-choice huggingface-api-key
[/code]

* ### Seleccionar un modelo predeterminado

En el desplegable **Default Hugging Face model** , elige el modelo que quieras. La lista se carga desde la API de Inference cuando tienes un token válido; de lo contrario se muestra una lista integrada. Tu elección se guarda como modelo predeterminado.

También puedes establecer o cambiar el modelo predeterminado más tarde en la configuración:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/deepseek-ai/DeepSeek-R1" },    },  },}
[/code]

* ### Verificar que el modelo está disponible

bashCopy code
[code]
    openclaw models list --provider huggingface
[/code]

### Configuración no interactiva

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice huggingface-api-key \  --huggingface-api-key "$HF_TOKEN"
[/code]

Esto establecerá `huggingface/deepseek-ai/DeepSeek-R1` como modelo predeterminado.

## IDs de modelo

Las referencias de modelo usan la forma `huggingface/<org>/<model>` (IDs estilo Hub). La lista de abajo proviene de **GET** `https://router.huggingface.co/v1/models`; tu catálogo puede incluir más.

Modelo | Ref (anteponer `huggingface/`)  
---|---  
DeepSeek R1 | `deepseek-ai/DeepSeek-R1`  
DeepSeek V3.2 | `deepseek-ai/DeepSeek-V3.2`  
Qwen3 8B | `Qwen/Qwen3-8B`  
Qwen2.5 7B Instruct | `Qwen/Qwen2.5-7B-Instruct`  
Qwen3 32B | `Qwen/Qwen3-32B`  
Llama 3.3 70B Instruct | `meta-llama/Llama-3.3-70B-Instruct`  
Llama 3.1 8B Instruct | `meta-llama/Llama-3.1-8B-Instruct`  
GPT-OSS 120B | `openai/gpt-oss-120b`  
GLM 4.7 | `zai-org/GLM-4.7`  
Kimi K2.5 | `moonshotai/Kimi-K2.5`  
  
## Configuración avanzada

Descubrimiento de modelos y desplegable de incorporación

OpenClaw descubre modelos llamando directamente al **endpoint de Inference** :

bashCopy code
[code]
    GET https://router.huggingface.co/v1/models
[/code]

(Opcional: envía `Authorization: Bearer $HUGGINGFACE_HUB_TOKEN` o `$HF_TOKEN` para la lista completa; algunos endpoints devuelven un subconjunto sin autenticación). La respuesta es de estilo OpenAI `{ "object": "list", "data": [ { "id": "Qwen/Qwen3-8B", "owned_by": "Qwen", ... }, ... ] }`.

Cuando configuras una clave API de Hugging Face (mediante incorporación, `HUGGINGFACE_HUB_TOKEN` o `HF_TOKEN`), OpenClaw usa este GET para descubrir modelos disponibles de chat completion. Durante la **configuración interactiva** , después de introducir tu token ves un desplegable **Default Hugging Face model** rellenado con esa lista (o con el catálogo integrado si la solicitud falla). En tiempo de ejecución (por ejemplo al iniciar el Gateway), cuando hay una clave presente, OpenClaw vuelve a llamar a **GET** `https://router.huggingface.co/v1/models` para actualizar el catálogo. La lista se fusiona con un catálogo integrado (para metadatos como ventana de contexto y coste). Si la solicitud falla o no se establece ninguna clave, solo se usa el catálogo integrado.

Nombres de modelo, aliases y sufijos de política

  * **Nombre desde API:** el nombre visible del modelo se **hidrata desde GET /v1/models** cuando la API devuelve `name`, `title` o `display_name`; en caso contrario se deriva del id del modelo (por ejemplo `deepseek-ai/DeepSeek-R1` pasa a ser "DeepSeek R1").
  * **Sobrescribir nombre visible:** puedes establecer una etiqueta personalizada por modelo en la configuración para que aparezca como quieras en la CLI y la IU:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1 (rápido)" },        "huggingface/deepseek-ai/DeepSeek-R1:cheapest": { alias: "DeepSeek R1 (barato)" },      },    },  },}
[/code]

  * **Sufijos de política:** la documentación y las ayudas integradas de Hugging Face en OpenClaw actualmente tratan estos dos sufijos como variantes integradas de política:

    * **`:fastest`** — mayor rendimiento.
    * **`:cheapest`** — menor coste por token de salida.

Puedes agregarlos como entradas separadas en `models.providers.huggingface.models` o establecer `model.primary` con el sufijo. También puedes definir tu orden predeterminado de proveedor en [Inference Provider settings](<https://hf.co/settings/inference-providers>) (sin sufijo = usar ese orden).

  * **Fusión de configuración:** las entradas existentes en `models.providers.huggingface.models` (por ejemplo en `models.json`) se conservan cuando se fusiona la configuración. Así que cualquier `name`, `alias` u opción de modelo personalizada que establezcas ahí se preserva.


Entorno y configuración del daemon

Si el Gateway se ejecuta como daemon (launchd/systemd), asegúrate de que `HUGGINGFACE_HUB_TOKEN` o `HF_TOKEN` esté disponible para ese proceso (por ejemplo, en `~/.openclaw/.env` o mediante `env.shellEnv`).

Configuración: DeepSeek R1 con fallback a Qwen json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-R1",        fallbacks: ["huggingface/Qwen/Qwen3-8B"],      },      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1" },        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },      },    },  },}
[/code]

Configuración: Qwen con variantes cheapest y fastest json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen3-8B" },      models: {        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },        "huggingface/Qwen/Qwen3-8B:cheapest": { alias: "Qwen3 8B (más barato)" },        "huggingface/Qwen/Qwen3-8B:fastest": { alias: "Qwen3 8B (más rápido)" },      },    },  },}
[/code]

Configuración: DeepSeek + Llama + GPT-OSS con aliases json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-V3.2",        fallbacks: [          "huggingface/meta-llama/Llama-3.3-70B-Instruct",          "huggingface/openai/gpt-oss-120b",        ],      },      models: {        "huggingface/deepseek-ai/DeepSeek-V3.2": { alias: "DeepSeek V3.2" },        "huggingface/meta-llama/Llama-3.3-70B-Instruct": { alias: "Llama 3.3 70B" },        "huggingface/openai/gpt-oss-120b": { alias: "GPT-OSS 120B" },      },    },  },}
[/code]

Configuración: varios Qwen y DeepSeek con sufijos de política json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest" },      models: {        "huggingface/Qwen/Qwen2.5-7B-Instruct": { alias: "Qwen2.5 7B" },        "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest": { alias: "Qwen2.5 7B (barato)" },        "huggingface/deepseek-ai/DeepSeek-R1:fastest": { alias: "DeepSeek R1 (rápido)" },        "huggingface/meta-llama/Llama-3.1-8B-Instruct": { alias: "Llama 3.1 8B" },      },    },  },}
[/code]

## Relacionado

[**Selección de modelos** Resumen de todos los proveedores, referencias de modelo y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Selección de modelos** Cómo elegir y configurar modelos. ](</es/concepts/models>) [**Documentación de Inference Providers** Documentación oficial de Hugging Face Inference Providers. ](<https://huggingface.co/docs/inference-providers>) [**Configuración** Referencia completa de configuración. ](</es/gateway/configuration>)

Was this useful?YesNo