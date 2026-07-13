---
title: LongCat
source_url: https://docs.openclaw.ai/es/providers/longcat
scraped_at: 2026-07-13
---

ModelsProviders

[LongCat](<https://longcat.ai>) proporciona una API alojada para LongCat-2.0, un modelo de razonamiento creado para cargas de trabajo de programación y de agentes. OpenClaw proporciona el Plugin oficial `longcat` para el endpoint de LongCat compatible con OpenAI.

Propiedad | Valor  
---|---  
Proveedor | `longcat`  
Autenticación | `LONGCAT_API_KEY`  
API | Chat Completions compatible con OpenAI  
URL base | `https://api.longcat.chat/openai`  
Modelo | `longcat/LongCat-2.0`  
Contexto | 1,048,576 tokens  
Salida máxima | 131,072 tokens  
Entrada | Texto  
  
## Instalar el Plugin

Instale el paquete oficial y, después, reinicie el Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/longcat-provideropenclaw gateway restart
[/code]

## Primeros pasos

* ### Create an API key

Inicie sesión en la [plataforma de la API de LongCat](<https://longcat.chat/platform/>) y cree una clave en la página [Claves de API](<https://longcat.chat/platform/api_keys>).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice longcat-api-key
[/code]

* ### Verify the model

bashCopy code
[code]
    openclaw models list --provider longcat
[/code]

La incorporación añade el catálogo alojado y selecciona `longcat/LongCat-2.0` cuando aún no se ha configurado un modelo principal.

### Configuración no interactiva

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice longcat-api-key \  --longcat-api-key "$LONGCAT_API_KEY"
[/code]

## Comportamiento del razonamiento

LongCat ofrece un control binario del razonamiento. OpenClaw asigna los niveles de razonamiento habilitados a `thinking: { type: "enabled" }` y `/think off` a `thinking: { type: "disabled" }`. Actualmente, LongCat no documenta `reasoning_effort`, por lo que OpenClaw no lo envía.

LongCat devuelve el razonamiento en `reasoning_content`. OpenClaw conserva ese campo al reproducir turnos de llamadas a herramientas del asistente, de modo que las sesiones de agente de varios turnos mantengan la estructura de mensajes esperada por el proveedor.

## Precios

El catálogo integrado utiliza los precios de lista de pago por uso de LongCat en USD por millón de tokens: 0,75 USD por entrada sin caché, 0,015 USD por entrada en caché y 2,95 USD por salida. LongCat puede ofrecer descuentos temporales; la [página de precios](<https://longcat.chat/platform/docs/Pricing/LongCat-2.0.html>) y sus registros de facturación son las fuentes autoritativas.

## LongCat-2.0 autoalojado

El proveedor `longcat` está destinado a la API alojada de LongCat. Para usar los pesos abiertos disponibles en [Hugging Face](<https://huggingface.co/meituan-longcat/LongCat-2.0>), sirva el modelo mediante un entorno de ejecución compatible con OpenAI y utilice en su lugar el proveedor existente de OpenClaw [vLLM](</es/providers/vllm>) o [SGLang](</es/providers/sglang>).

Conserve el identificador exacto del modelo del entorno de ejecución en el catálogo del proveedor autoalojado; no enrute una implementación local mediante `longcat/LongCat-2.0`.

## Solución de problemas

The key works in a shell but not in the Gateway

Los procesos del Gateway administrados por un daemon no heredan todas las variables del shell interactivo. Añada `LONGCAT_API_KEY` a `~/.openclaw/.env`, configúrela mediante la incorporación o utilice una referencia de secreto aprobada.

Requests fail with 402 or 429

`402` significa que la cuenta no tiene suficiente cuota de tokens. `429` significa que la clave de API alcanzó un límite de solicitudes. Consulte el [uso de LongCat](<https://longcat.chat/platform/usage>) y vuelva a intentar las solicitudes limitadas después del periodo de espera del proveedor.

The model does not appear

Ejecute `openclaw plugins list` y confirme que el Plugin `longcat` está habilitado; después, ejecute `openclaw models list --provider longcat`.

## Contenido relacionado

[**Model providers** Configuración de proveedores, referencias de modelos y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**LongCat API docs** Endpoints de la API alojada, autenticación, límites y ejemplos. ](<https://longcat.chat/platform/docs/>) [**LongCat-2.0 model card** Arquitectura, orientación para la implementación y detalles del modelo. ](<https://huggingface.co/meituan-longcat/LongCat-2.0>) [**Secrets** Almacene las credenciales del proveedor sin insertar texto sin formato en la configuración. ](</es/gateway/secrets>)

Was this useful?YesNo

Open issue