---
title: Amazon Bedrock Mantle
source_url: https://docs.openclaw.ai/es/providers/bedrock-mantle
scraped_at: 2026-05-25
---

OpenClaw incluye un proveedor **Amazon Bedrock Mantle** incluido que se conecta al endpoint compatible con OpenAI de Mantle. Mantle aloja modelos de código abierto y de terceros (GPT-OSS, Qwen, Kimi, GLM y similares) mediante una superficie estándar `/v1/chat/completions` respaldada por la infraestructura de Bedrock.

Propiedad | Valor  
---|---  
ID del proveedor | `amazon-bedrock-mantle`  
API | `openai-completions` (compatible con OpenAI) o `anthropic-messages` (ruta Anthropic Messages)  
Autenticación | `AWS_BEARER_TOKEN_BEDROCK` explícito o generación de token portador mediante la cadena de credenciales IAM  
Región predeterminada | `us-east-1` (sobrescribir con `AWS_REGION` o `AWS_DEFAULT_REGION`)  
  
## Primeros pasos

Elige tu método de autenticación preferido y sigue los pasos de configuración.

### Token portador explícito

**Recomendado para:** entornos donde ya tienes un token portador de Mantle.

* ### Configurar el token portador en el host del Gateway

bashCopy code
[code]
    export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

Opcionalmente, configura una región (el valor predeterminado es `us-east-1`):

bashCopy code
[code]
    export AWS_REGION="us-west-2"
[/code]

* ### Verificar que se descubren modelos

bashCopy code
[code]
    openclaw models list
[/code]

Los modelos descubiertos aparecen bajo el proveedor `amazon-bedrock-mantle`. No se requiere configuración adicional salvo que quieras sobrescribir los valores predeterminados.

### Credenciales IAM

**Recomendado para:** usar credenciales compatibles con AWS SDK (configuración compartida, SSO, identidad web, roles de instancia o de tarea).

* ### Configurar credenciales de AWS en el host del Gateway

Funciona cualquier origen de autenticación compatible con AWS SDK:

bashCopy code
[code]
    export AWS_PROFILE="default"export AWS_REGION="us-west-2"
[/code]

* ### Verificar que se descubren modelos

bashCopy code
[code]
    openclaw models list
[/code]

OpenClaw genera automáticamente un token portador de Mantle a partir de la cadena de credenciales.

## Descubrimiento automático de modelos

Cuando `AWS_BEARER_TOKEN_BEDROCK` está configurado, OpenClaw lo usa directamente. De lo contrario, OpenClaw intenta generar un token portador de Mantle a partir de la cadena de credenciales predeterminada de AWS. Luego descubre los modelos de Mantle disponibles consultando el endpoint `/v1/models` de la región.

Comportamiento | Detalle  
---|---  
Caché de descubrimiento | Resultados almacenados en caché durante 1 hora  
Actualización de token IAM | Cada hora  
  
Para mantener habilitado el plugin Mantle pero suprimir el descubrimiento automático y la generación de tokens portadores IAM, deshabilita el interruptor de descubrimiento propiedad del plugin:

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock-mantle.config.discovery.enabled false
[/code]

### Regiones compatibles

`us-east-1`, `us-east-2`, `us-west-2`, `ap-northeast-1`, `ap-south-1`, `ap-southeast-3`, `eu-central-1`, `eu-west-1`, `eu-west-2`, `eu-south-1`, `eu-north-1`, `sa-east-1`.

## Configuración manual

Si prefieres configuración explícita en lugar de descubrimiento automático:

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        baseUrl: "https://bedrock-mantle.us-east-1.api.aws/v1",        api: "openai-completions",        auth: "api-key",        apiKey: "env:AWS_BEARER_TOKEN_BEDROCK",        models: [          {            id: "gpt-oss-120b",            name: "GPT-OSS 120B",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32000,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

## Configuración avanzada

Soporte de razonamiento

El soporte de razonamiento se infiere a partir de IDs de modelo que contienen patrones como `thinking`, `reasoner` o `gpt-oss-120b`. OpenClaw establece `reasoning: true` automáticamente para los modelos coincidentes durante el descubrimiento.

Endpoint no disponible

Si el endpoint de Mantle no está disponible o no devuelve modelos, el proveedor se omite silenciosamente. OpenClaw no genera un error; otros proveedores configurados siguen funcionando con normalidad.

Claude Opus 4.7 mediante la ruta Anthropic Messages

Mantle también expone una ruta Anthropic Messages que transporta modelos Claude por la misma ruta de streaming autenticada con token portador. Claude Opus 4.7 (`amazon-bedrock-mantle/claude-opus-4.7`) se puede invocar mediante esta ruta con streaming propiedad del proveedor, por lo que los tokens portadores de AWS no se tratan como claves de API de Anthropic.

Cuando fijas un modelo Anthropic Messages en el proveedor Mantle, OpenClaw usa la superficie de API `anthropic-messages` en lugar de `openai-completions` para ese modelo. La autenticación sigue viniendo de `AWS_BEARER_TOKEN_BEDROCK` (o del token portador IAM emitido).

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        models: [          {            id: "claude-opus-4.7",            name: "Claude Opus 4.7",            api: "anthropic-messages",            reasoning: true,            input: ["text", "image"],            contextWindow: 1000000,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Relación con el proveedor Amazon Bedrock

Bedrock Mantle es un proveedor separado del proveedor estándar [Amazon Bedrock](</es/providers/bedrock>). Mantle usa una superficie `/v1` compatible con OpenAI, mientras que el proveedor estándar de Bedrock usa la API nativa de Bedrock.

Ambos proveedores comparten la misma credencial `AWS_BEARER_TOKEN_BEDROCK` cuando está presente.

## Relacionado

[**Amazon Bedrock** Proveedor nativo de Bedrock para Anthropic Claude, Titan y otros modelos. ](</es/providers/bedrock>) [**Selección de modelo** Elección de proveedores, refs de modelo y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**OAuth y autenticación** Detalles de autenticación y reglas de reutilización de credenciales. ](</es/gateway/authentication>) [**Solución de problemas** Problemas comunes y cómo resolverlos. ](</es/help/troubleshooting>)

Was this useful?YesNo