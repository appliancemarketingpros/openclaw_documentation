---
title: Presentación de mensajes
source_url: https://docs.openclaw.ai/es/plugins/message-presentation
scraped_at: 2026-05-25
---

La presentación de mensajes es el contrato compartido de OpenClaw para una interfaz de chat saliente enriquecida. Permite que agentes, comandos de CLI, flujos de aprobación y plugins describan la intención del mensaje una sola vez, mientras cada Plugin de canal representa la mejor forma nativa que puede.

Use la presentación para una interfaz de mensaje portátil:

  * secciones de texto
  * texto pequeño de contexto/pie de página
  * divisores
  * botones
  * menús de selección
  * título y tono de tarjeta


No agregue nuevos campos nativos de proveedor, como `components` de Discord, `blocks` de Slack, `buttons` de Telegram, `card` de Teams o `card` de Feishu, a la herramienta de mensajes compartida. Esas son salidas de renderizador propiedad del Plugin de canal.

## Contrato

Los autores de plugins importan el contrato público desde:

tsCopy code
[code]
       MessagePresentation,  ReplyPayloadDelivery,} from "openclaw/plugin-sdk/interactive-runtime";
[/code]

Forma:

tsCopy code
[code]
    type MessagePresentation = {  title?: string;  tone?: "neutral" | "info" | "success" | "warning" | "danger";  blocks: MessagePresentationBlock[];}; type MessagePresentationBlock =  | { type: "text"; text: string }  | { type: "context"; text: string }  | { type: "divider" }  | { type: "buttons"; buttons: MessagePresentationButton[] }  | { type: "select"; placeholder?: string; options: MessagePresentationOption[] }; type MessagePresentationButton = {  label: string;  value?: string;  url?: string;  style?: "primary" | "secondary" | "success" | "danger";}; type MessagePresentationOption = {  label: string;  value: string;}; type ReplyPayloadDelivery = {  pin?:    | boolean    | {        enabled: boolean;        notify?: boolean;        required?: boolean;      };};
[/code]

Semántica de los botones:

  * `value` es un valor de acción de la aplicación que se enruta de vuelta por la ruta de interacción existente del canal cuando el canal admite controles clicables.
  * `url` es un botón de enlace. Puede existir sin `value`.
  * `label` es obligatorio y también se usa en el respaldo de texto.
  * `style` es orientativo. Los renderizadores deben asignar los estilos no admitidos a un valor predeterminado seguro, no hacer fallar el envío.


Semántica de selección:

  * `options[].value` es el valor de aplicación seleccionado.
  * `placeholder` es orientativo y puede ser ignorado por canales sin soporte nativo de selección.
  * Si un canal no admite selecciones, el texto de respaldo enumera las etiquetas.


## Ejemplos de productores

Tarjeta simple:

jsonCopy code
[code]
    {  "title": "Deploy approval",  "tone": "warning",  "blocks": [    { "type": "text", "text": "Canary is ready to promote." },    { "type": "context", "text": "Build 1234, staging passed." },    {      "type": "buttons",      "buttons": [        { "label": "Approve", "value": "deploy:approve", "style": "success" },        { "label": "Decline", "value": "deploy:decline", "style": "danger" }      ]    }  ]}
[/code]

Botón de enlace solo con URL:

jsonCopy code
[code]
    {  "blocks": [    { "type": "text", "text": "Release notes are ready." },    {      "type": "buttons",      "buttons": [{ "label": "Open notes", "url": "https://example.com/release" }]    }  ]}
[/code]

Menú de selección:

jsonCopy code
[code]
    {  "title": "Choose environment",  "blocks": [    {      "type": "select",      "placeholder": "Environment",      "options": [        { "label": "Canary", "value": "env:canary" },        { "label": "Production", "value": "env:prod" }      ]    }  ]}
[/code]

Envío de CLI:

bashCopy code
[code]
    openclaw message send --channel slack \  --target channel:C123 \  --message "Deploy approval" \  --presentation '{"title":"Deploy approval","tone":"warning","blocks":[{"type":"text","text":"Canary is ready."},{"type":"buttons","buttons":[{"label":"Approve","value":"deploy:approve","style":"success"},{"label":"Decline","value":"deploy:decline","style":"danger"}]}]}'
[/code]

Entrega fijada:

bashCopy code
[code]
    openclaw message send --channel telegram \  --target -1001234567890 \  --message "Topic opened" \  --pin
[/code]

Entrega fijada con JSON explícito:

jsonCopy code
[code]
    {  "pin": {    "enabled": true,    "notify": true,    "required": false  }}
[/code]

## Contrato del renderizador

Los plugins de canal declaran el soporte de renderizado en su adaptador saliente:

tsCopy code
[code]
    const adapter: ChannelOutboundAdapter = {  deliveryMode: "direct",  presentationCapabilities: {    supported: true,    buttons: true,    selects: true,    context: true,    divider: true,  },  deliveryCapabilities: {    pin: true,  },  renderPresentation({ payload, presentation, ctx }) {    return renderNativePayload(payload, presentation, ctx);  },  async pinDeliveredMessage({ target, messageId, pin }) {    await pinNativeMessage(target, messageId, { notify: pin.notify === true });  },};
[/code]

Los campos de capacidad son booleanos intencionalmente simples. Describen lo que el renderizador puede hacer interactivo, no todos los límites de la plataforma nativa. Los renderizadores siguen siendo responsables de los límites específicos de la plataforma, como el número máximo de botones, el número de bloques y el tamaño de tarjeta.

## Flujo de renderizado central

Cuando un `ReplyPayload` o una acción de mensaje incluye `presentation`, el núcleo:

  1. Normaliza la carga útil de presentación.
  2. Resuelve el adaptador saliente del canal de destino.
  3. Lee `presentationCapabilities`.
  4. Llama a `renderPresentation` cuando el adaptador puede renderizar la carga útil.
  5. Recurre a texto conservador cuando el adaptador no existe o no puede renderizar.
  6. Envía la carga útil resultante por la ruta normal de entrega del canal.
  7. Aplica metadatos de entrega, como `delivery.pin`, después del primer mensaje enviado correctamente.


El núcleo es responsable del comportamiento de respaldo para que los productores puedan permanecer independientes del canal. Los plugins de canal son responsables del renderizado nativo y del manejo de interacciones.

## Reglas de degradación

La presentación debe ser segura de enviar en canales limitados.

El texto de respaldo incluye:

  * `title` como primera línea
  * bloques `text` como párrafos normales
  * bloques `context` como líneas de contexto compactas
  * bloques `divider` como separador visual
  * etiquetas de botones, incluidas las URL para botones de enlace
  * etiquetas de opciones de selección


Los controles nativos no admitidos deben degradarse en lugar de hacer fallar todo el envío. Ejemplos:

  * Telegram con botones en línea deshabilitados envía texto de respaldo.
  * Un canal sin soporte de selección enumera las opciones de selección como texto.
  * Un botón solo con URL se convierte en un botón de enlace nativo o en una línea de URL de respaldo.
  * Los errores opcionales al fijar no hacen fallar el mensaje entregado.


La principal excepción es `delivery.pin.required: true`; si se solicita fijar como obligatorio y el canal no puede fijar el mensaje enviado, la entrega informa un error.

## Asignación de proveedores

Renderizadores integrados actuales:

Canal | Destino de renderizado nativo | Notas  
---|---|---  
Discord | Componentes y contenedores de componentes | Preserva `channelData.discord.components` heredado para los productores de cargas útiles nativas de proveedor existentes, pero los nuevos envíos compartidos deben usar `presentation`.  
Slack | Block Kit | Preserva `channelData.slack.blocks` heredado para los productores de cargas útiles nativas de proveedor existentes, pero los nuevos envíos compartidos deben usar `presentation`.  
Telegram | Texto más teclados en línea | Los botones/selecciones requieren capacidad de botones en línea para la superficie de destino; de lo contrario, se usa texto de respaldo.  
Mattermost | Texto más props interactivas | Otros bloques se degradan a texto.  
Microsoft Teams | Adaptive Cards | El texto `message` simple se incluye con la tarjeta cuando se proporcionan ambos.  
Feishu | Tarjetas interactivas | El encabezado de la tarjeta puede usar `title`; el cuerpo evita duplicar ese título.  
Canales simples | Respaldo de texto | Los canales sin renderizador siguen obteniendo una salida legible.  
  
La compatibilidad con cargas útiles nativas de proveedor es una facilidad de transición para productores de respuestas existentes. No es una razón para agregar nuevos campos nativos compartidos.

## Presentación frente a InteractiveReply

`InteractiveReply` es el subconjunto interno más antiguo usado por los ayudantes de aprobación e interacción. Admite:

  * texto
  * botones
  * selecciones


`MessagePresentation` es el contrato canónico de envío compartido. Agrega:

  * título
  * tono
  * contexto
  * divisor
  * botones solo con URL
  * metadatos de entrega genéricos mediante `ReplyPayload.delivery`


Use ayudantes de `openclaw/plugin-sdk/interactive-runtime` al adaptar código anterior:

tsCopy code
[code]
       interactiveReplyToPresentation,  normalizeMessagePresentation,  presentationToInteractiveControlsReply,  presentationToInteractiveReply,  renderMessagePresentationFallbackText,} from "openclaw/plugin-sdk/interactive-runtime";
[/code]

El código nuevo debe aceptar o producir `MessagePresentation` directamente.

`presentationToInteractiveReply(...)` preserva el texto visible de presentación al asignar el título, texto, contexto, botones y selecciones a la forma anterior de `InteractiveReply`. Los renderizadores de componentes que ya dibujan de forma nativa bloques de título, texto, contexto y divisor deben usar `presentationToInteractiveControlsReply(...)` en su lugar, y luego anexar solo los controles de botón y selección.

`renderMessagePresentationFallbackText(...)` devuelve una cadena vacía para bloques de presentación que no tienen respaldo de texto, como una presentación que solo contiene divisores. Los transportes que requieren un cuerpo de envío no vacío pueden pasar `emptyFallback` para optar por un cuerpo mínimo sin cambiar el contrato predeterminado de respaldo.

## Fijación de entrega

Fijar es un comportamiento de entrega, no de presentación. Use `delivery.pin` en lugar de campos nativos de proveedor como `channelData.telegram.pin`.

Semántica:

  * `pin: true` fija el primer mensaje entregado correctamente.
  * `pin.notify` toma `false` como valor predeterminado.
  * `pin.required` toma `false` como valor predeterminado.
  * Los errores opcionales al fijar se degradan y dejan intacto el mensaje enviado.
  * Los errores obligatorios al fijar hacen fallar la entrega.
  * Los mensajes fragmentados fijan el primer fragmento entregado, no el fragmento final.


Las acciones manuales de mensaje `pin`, `unpin` y `pins` siguen existiendo para mensajes existentes cuando el proveedor admite esas operaciones.

## Lista de comprobación para autores de plugins

  * Declare `presentation` desde `describeMessageTool(...)` cuando el canal pueda renderizar o degradar de forma segura la presentación semántica.
  * Agregue `presentationCapabilities` al adaptador saliente de tiempo de ejecución.
  * Implemente `renderPresentation` en código de tiempo de ejecución, no en código de configuración de Plugin del plano de control.
  * Mantenga las bibliotecas de UI nativa fuera de las rutas calientes de configuración/catálogo.
  * Preserve los límites de la plataforma en el renderizador y las pruebas.
  * Agregue pruebas de respaldo para botones no admitidos, selecciones, botones de URL, duplicación de título/texto y envíos mixtos de `message` más `presentation`.
  * Agregue soporte para fijación de entrega mediante `deliveryCapabilities.pin` y `pinDeliveredMessage` solo cuando el proveedor pueda fijar el id del mensaje enviado.
  * No exponga nuevos campos nativos de proveedor de tarjeta/bloque/componente/botón mediante el esquema de acción de mensaje compartido.


## Documentación relacionada

  * [CLI de mensajes](</es/cli/message>)
  * [Descripción general del SDK de Plugin](</es/plugins/sdk-overview>)
  * [Arquitectura de Plugin](</es/plugins/architecture-internals#message-tool-schemas>)
  * [Plan de refactorización de presentación de canales](</es/plan/ui-channels>)


Was this useful?YesNo