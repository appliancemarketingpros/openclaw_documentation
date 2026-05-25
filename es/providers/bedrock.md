---
title: Amazon Bedrock
source_url: https://docs.openclaw.ai/es/providers/bedrock
scraped_at: 2026-05-25
---

OpenClaw puede usar modelos de **Amazon Bedrock** mediante el proveedor de streaming **Bedrock Converse** de pi-ai. La autenticación de Bedrock usa la **cadena de credenciales predeterminada del AWS SDK** , no una clave de API.

Propiedad | Valor  
---|---  
Proveedor | `amazon-bedrock`  
API | `bedrock-converse-stream`  
Autenticación | Credenciales de AWS (variables de entorno, configuración compartida o rol de instancia)  
Región | `AWS_REGION` o `AWS_DEFAULT_REGION` (predeterminado: `us-east-1`)  
  
## Primeros pasos

Elige tu método de autenticación preferido y sigue los pasos de configuración.

### Claves de acceso / variables de entorno

**Recomendado para:** máquinas de desarrollo, CI o hosts donde administras las credenciales de AWS directamente.

* ### Configurar credenciales de AWS en el host del gateway

bashCopy code
[code]
    export AWS_ACCESS_KEY_ID="AKIA..."export AWS_SECRET_ACCESS_KEY="..."export AWS_REGION="us-east-1"# Optional:export AWS_SESSION_TOKEN="..."export AWS_PROFILE="your-profile"# Optional (Bedrock API key/bearer token):export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

* ### Agregar un proveedor y modelo de Bedrock a tu configuración

No se requiere `apiKey`. Configura el proveedor con `auth: "aws-sdk"`:

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock": {        baseUrl: "https://bedrock-runtime.us-east-1.amazonaws.com",        api: "bedrock-converse-stream",        auth: "aws-sdk",        models: [          {            id: "us.anthropic.claude-opus-4-6-v1:0",            name: "Claude Opus 4.6 (Bedrock)",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 200000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "amazon-bedrock/us.anthropic.claude-opus-4-6-v1:0" },    },  },}
[/code]

* ### Verificar que los modelos estén disponibles

bashCopy code
[code]
    openclaw models list
[/code]

### Roles de instancia de EC2 (IMDS)

**Recomendado para:** instancias EC2 con un rol de IAM adjunto que usan el servicio de metadatos de instancia para la autenticación.

* ### Habilitar el descubrimiento explícitamente

Al usar IMDS, OpenClaw no puede detectar la autenticación de AWS solo a partir de marcadores de entorno, así que debes activarlo:

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1
[/code]

* ### Opcionalmente, agregar un marcador de entorno para el modo automático

Si también quieres que funcione la ruta de detección automática mediante marcadores de entorno (por ejemplo, para superficies de `openclaw status`):

bashCopy code
[code]
    export AWS_PROFILE=defaultexport AWS_REGION=us-east-1
[/code]

**No** necesitas una clave de API falsa.

* ### Verificar que se descubran los modelos

bashCopy code
[code]
    openclaw models list
[/code]

## Descubrimiento automático de modelos

OpenClaw puede descubrir automáticamente modelos de Bedrock que admiten **streaming** y **salida de texto**. El descubrimiento usa `bedrock:ListFoundationModels` y `bedrock:ListInferenceProfiles`, y los resultados se almacenan en caché (predeterminado: 1 hora).

Cómo se habilita el proveedor implícito:

  * Si `plugins.entries.amazon-bedrock.config.discovery.enabled` es `true`, OpenClaw intentará el descubrimiento incluso cuando no haya ningún marcador de entorno de AWS presente.
  * Si `plugins.entries.amazon-bedrock.config.discovery.enabled` no está definido, OpenClaw solo agrega automáticamente el proveedor implícito de Bedrock cuando ve uno de estos marcadores de autenticación de AWS: `AWS_BEARER_TOKEN_BEDROCK`, `AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY` o `AWS_PROFILE`.
  * La ruta real de autenticación del runtime de Bedrock sigue usando la cadena predeterminada del AWS SDK, por lo que la configuración compartida, SSO y la autenticación mediante rol de instancia de IMDS pueden funcionar incluso cuando el descubrimiento necesitó `enabled: true` para activarse.


Opciones de configuración de descubrimiento

Las opciones de configuración se encuentran en `plugins.entries.amazon-bedrock.config.discovery`:

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          discovery: {            enabled: true,            region: "us-east-1",            providerFilter: ["anthropic", "amazon"],            refreshInterval: 3600,            defaultContextWindow: 32000,            defaultMaxTokens: 4096,          },        },      },    },  },}
[/code]

Opción | Predeterminado | Descripción  
---|---|---  
`enabled` | auto | En modo automático, OpenClaw solo habilita el proveedor implícito de Bedrock cuando ve un marcador de entorno de AWS compatible. Establece `true` para forzar el descubrimiento.  
`region` | `AWS_REGION` / `AWS_DEFAULT_REGION` / `us-east-1` | Región de AWS usada para las llamadas a la API de descubrimiento.  
`providerFilter` | (todos) | Coincide con nombres de proveedores de Bedrock (por ejemplo, `anthropic`, `amazon`).  
`refreshInterval` | `3600` | Duración de la caché en segundos. Establece `0` para deshabilitar el almacenamiento en caché.  
`defaultContextWindow` | `32000` | Ventana de contexto usada para modelos descubiertos (sobrescríbela si conoces los límites de tu modelo).  
`defaultMaxTokens` | `4096` | Tokens máximos de salida usados para modelos descubiertos (sobrescríbelos si conoces los límites de tu modelo).  
  
## Configuración rápida (ruta de AWS)

Este recorrido crea un rol de IAM, adjunta permisos de Bedrock, asocia el perfil de instancia y habilita el descubrimiento de OpenClaw en el host EC2.

bashCopy code
[code]
    # 1. Create IAM role and instance profileaws iam create-role --role-name EC2-Bedrock-Access \  --assume-role-policy-document '{    "Version": "2012-10-17",    "Statement": [{      "Effect": "Allow",      "Principal": {"Service": "ec2.amazonaws.com"},      "Action": "sts:AssumeRole"    }]  }' aws iam attach-role-policy --role-name EC2-Bedrock-Access \  --policy-arn arn:aws:iam::aws:policy/AmazonBedrockFullAccess aws iam create-instance-profile --instance-profile-name EC2-Bedrock-Accessaws iam add-role-to-instance-profile \  --instance-profile-name EC2-Bedrock-Access \  --role-name EC2-Bedrock-Access # 2. Attach to your EC2 instanceaws ec2 associate-iam-instance-profile \  --instance-id i-xxxxx \  --iam-instance-profile Name=EC2-Bedrock-Access # 3. On the EC2 instance, enable discovery explicitlyopenclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1 # 4. Optional: add an env marker if you want auto mode without explicit enableecho 'export AWS_PROFILE=default' >> ~/.bashrcecho 'export AWS_REGION=us-east-1' >> ~/.bashrcsource ~/.bashrc # 5. Verify models are discoveredopenclaw models list
[/code]

## Configuración avanzada

Perfiles de inferencia

OpenClaw descubre **perfiles de inferencia regionales y globales** junto con modelos base. Cuando un perfil se asigna a un modelo base conocido, el perfil hereda las capacidades de ese modelo (ventana de contexto, tokens máximos, razonamiento, visión) y la región de solicitud correcta de Bedrock se inyecta automáticamente. Esto significa que los perfiles de Claude entre regiones funcionan sin sobrescrituras manuales del proveedor.

Los ID de perfil de inferencia se ven como `us.anthropic.claude-opus-4-6-v1:0` (regional) o `anthropic.claude-opus-4-6-v1:0` (global). Si el modelo subyacente ya está en los resultados de descubrimiento, el perfil hereda todo su conjunto de capacidades; de lo contrario, se aplican valores predeterminados seguros.

No se necesita configuración adicional. Siempre que el descubrimiento esté habilitado y la entidad principal de IAM tenga `bedrock:ListInferenceProfiles`, los perfiles aparecen junto a los modelos base en `openclaw models list`.

Nivel de servicio

Algunos modelos de Bedrock admiten un parámetro `service_tier` para optimizar por costo o latencia. Los siguientes niveles están disponibles:

Nivel | Descripción  
---|---  
`default` | Nivel estándar de Bedrock  
`flex` | Procesamiento con descuento para cargas de trabajo que pueden tolerar mayor latencia  
`priority` | Procesamiento priorizado para cargas de trabajo sensibles a la latencia  
`reserved` | Capacidad reservada para cargas de trabajo de estado estable  
  
Establece `serviceTier` (o `service_tier`) mediante `agents.defaults.params` para solicitudes de modelos de Bedrock, o por modelo en `agents.defaults.models["<model-key>"].params`:

json5Copy code
[code]
    {  agents: {    defaults: {      params: {        serviceTier: "flex", // applies to all models      },      models: {        "amazon-bedrock/mistral.mistral-large-3-675b-instruct": {          params: {            serviceTier: "priority", // per-model override          },        },      },    },  },}
[/code]

Los valores válidos son `default`, `flex`, `priority` y `reserved`. No todos los modelos admiten todos los niveles; si se solicita un nivel no compatible, Bedrock devolverá un error de validación. Nota: el mensaje de error es algo engañoso; puede decir "The provided model identifier is invalid" en lugar de indicar un nivel de servicio no compatible. Si ves este error, verifica si el modelo admite el nivel solicitado.

Temperatura de Claude Opus 4.7

Bedrock rechaza el parámetro `temperature` para Claude Opus 4.7. OpenClaw omite `temperature` automáticamente para cualquier referencia de Bedrock a Opus 4.7, incluidos ID de modelos base, perfiles de inferencia con nombre, perfiles de inferencia de aplicación cuyo modelo subyacente se resuelve como Opus 4.7 mediante `bedrock:GetInferenceProfile` y variantes punteadas de `opus-4.7` con prefijos de región opcionales (`us.`, `eu.`, `ap.`, `apac.`, `au.`, `jp.`, `global.`). No se requiere ningún control de configuración, y la omisión se aplica tanto al objeto de opciones de solicitud como al campo de carga útil `inferenceConfig`.

Mecanismos de protección

Puedes aplicar [Amazon Bedrock Guardrails](<https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>) a todas las invocaciones de modelos de Bedrock añadiendo un objeto `guardrail` a la configuración del plugin `amazon-bedrock`. Los mecanismos de protección te permiten aplicar filtrado de contenido, denegación de temas, filtros de palabras, filtros de información confidencial y comprobaciones de fundamentación contextual.

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          guardrail: {            guardrailIdentifier: "abc123", // guardrail ID or full ARN            guardrailVersion: "1", // version number or "DRAFT"            streamProcessingMode: "sync", // optional: "sync" or "async"            trace: "enabled", // optional: "enabled", "disabled", or "enabled_full"          },        },      },    },  },}
[/code]

Opción | Obligatorio | Descripción  
---|---|---  
`guardrailIdentifier` | Sí | ID del mecanismo de protección (p. ej., `abc123`) o ARN completo (p. ej., `arn:aws:bedrock:us-east-1:123456789012:guardrail/abc123`).  
`guardrailVersion` | Sí | Número de versión publicado, o `"DRAFT"` para el borrador de trabajo.  
`streamProcessingMode` | No | `"sync"` o `"async"` para la evaluación del mecanismo de protección durante el streaming. Si se omite, Bedrock usa su valor predeterminado.  
`trace` | No | `"enabled"` o `"enabled_full"` para depuración; omítelo o configúralo como `"disabled"` para producción.  
Embeddings para búsqueda en memoria

Bedrock también puede servir como proveedor de embeddings para la [búsqueda en memoria](</es/concepts/memory-search>). Esto se configura por separado del proveedor de inferencia: establece `agents.defaults.memorySearch.provider` en `"bedrock"`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "bedrock",        model: "amazon.titan-embed-text-v2:0", // default      },    },  },}
[/code]

Los embeddings de Bedrock usan la misma cadena de credenciales del SDK de AWS que la inferencia (roles de instancia, SSO, claves de acceso, configuración compartida e identidad web). No se necesita ninguna clave de API. Cuando `provider` es `"auto"`, Bedrock se detecta automáticamente si esa cadena de credenciales se resuelve correctamente.

Los modelos de embedding compatibles incluyen Amazon Titan Embed (v1, v2), Amazon Nova Embed, Cohere Embed (v3, v4) y TwelveLabs Marengo. Consulta la [referencia de configuración de memoria: Bedrock](</es/reference/memory-config#bedrock-embedding-config>) para ver la lista completa de modelos y las opciones de dimensión.

Notas y advertencias

  * Bedrock requiere **acceso al modelo** habilitado en tu cuenta/región de AWS.
  * La detección automática necesita los permisos `bedrock:ListFoundationModels` y `bedrock:ListInferenceProfiles`.
  * Si dependes del modo automático, configura uno de los marcadores de entorno de autenticación de AWS compatibles en el host del Gateway. Si prefieres autenticación IMDS/configuración compartida sin marcadores de entorno, configura `plugins.entries.amazon-bedrock.config.discovery.enabled: true`.
  * OpenClaw muestra la fuente de credenciales en este orden: `AWS_BEARER_TOKEN_BEDROCK`, luego `AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`, luego `AWS_PROFILE` y, después, la cadena predeterminada del SDK de AWS.
  * La compatibilidad con razonamiento depende del modelo; consulta la ficha del modelo de Bedrock para ver las capacidades actuales.
  * Si prefieres un flujo de claves gestionado, también puedes colocar un proxy compatible con OpenAI delante de Bedrock y configurarlo como proveedor de OpenAI en su lugar.


## Relacionado

[**Selección de modelos** Elegir proveedores, referencias de modelo y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Búsqueda en memoria** Embeddings de Bedrock para la configuración de búsqueda en memoria. ](</es/concepts/memory-search>) [**Referencia de configuración de memoria** Lista completa de modelos de embedding de Bedrock y opciones de dimensión. ](</es/reference/memory-config#bedrock-embedding-config>) [**Solución de problemas** Solución general de problemas y preguntas frecuentes. ](</es/help/troubleshooting>)

Was this useful?YesNo