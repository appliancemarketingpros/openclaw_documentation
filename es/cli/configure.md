---
title: Configurar
source_url: https://docs.openclaw.ai/es/cli/configure
scraped_at: 2026-05-25
---

# `openclaw configure`

Asistente interactivo para cambios específicos en una configuración existente: credenciales, dispositivos, valores predeterminados de agentes, Gateway, canales, plugins, skills y comprobaciones de estado.

Usa `openclaw onboard` para el recorrido guiado completo de primera ejecución, `openclaw setup` solo para la configuración base y el espacio de trabajo, y `openclaw channels add` cuando solo necesites configurar una cuenta de canal.

Cuando configure se inicia desde una opción de autenticación de proveedor, los selectores de modelo predeterminado y lista de permitidos prefieren automáticamente ese proveedor. Para proveedores emparejados como Volcengine y BytePlus, la misma preferencia también coincide con sus variantes de plan de codificación (`volcengine-plan/*`, `byteplus-plan/*`). Si el filtro de proveedor preferido produjera una lista vacía, configure vuelve al catálogo sin filtrar en lugar de mostrar un selector en blanco.

Para la búsqueda web, `openclaw configure --section web` te permite elegir un proveedor y configurar sus credenciales. Algunos proveedores también muestran indicaciones de seguimiento específicas del proveedor:

  * **Grok** puede ofrecer configuración opcional de `x_search` con la misma `XAI_API_KEY` y permitirte elegir un modelo de `x_search`.
  * **Kimi** puede pedir la región de la API de Moonshot (`api.moonshot.ai` frente a `api.moonshot.cn`) y el modelo predeterminado de búsqueda web de Kimi.


Relacionado:

  * Referencia de configuración del Gateway: [Configuración](</es/gateway/configuration>)
  * CLI de configuración: [Config](</es/cli/config>)


## Opciones

  * `--section <section>`: filtro de sección repetible


Secciones disponibles:

  * `workspace`
  * `model`
  * `web`
  * `gateway`
  * `daemon`
  * `channels`
  * `plugins`
  * `skills`
  * `health`


Notas:

  * Elegir dónde se ejecuta el Gateway siempre actualiza `gateway.mode`. Puedes seleccionar "Continuar" sin otras secciones si eso es todo lo que necesitas.
  * Después de escribir la configuración local, configure instala los plugins descargables seleccionados cuando la ruta de configuración elegida los requiere. La configuración de Gateway remoto no instala paquetes de plugins locales.
  * Los servicios orientados a canales (Slack/Discord/Matrix/Microsoft Teams) solicitan listas de permitidos de canales/salas durante la configuración. Puedes introducir nombres o IDs; el asistente resuelve nombres a IDs cuando es posible.
  * Si ejecutas el paso de instalación del daemon, la autenticación con token requiere un token, y `gateway.auth.token` está gestionado por SecretRef, configure valida el SecretRef pero no persiste valores de token en texto plano resueltos en los metadatos de entorno del servicio supervisor.
  * Si la autenticación con token requiere un token y el SecretRef de token configurado no está resuelto, configure bloquea la instalación del daemon con orientación de corrección accionable.
  * Si tanto `gateway.auth.token` como `gateway.auth.password` están configurados y `gateway.auth.mode` no está establecido, configure bloquea la instalación del daemon hasta que el modo se establezca explícitamente.


## Ejemplos

bashCopy code
[code]
    openclaw configureopenclaw configure --section webopenclaw configure --section model --section channelsopenclaw configure --section gateway --section daemon
[/code]

## Relacionado

  * [Referencia de CLI](</es/cli>)
  * [Configuración](</es/gateway/configuration>)


Was this useful?YesNo