---
title: WeChat
source_url: https://docs.openclaw.ai/es/channels/wechat
scraped_at: 2026-05-25
---

OpenClaw se conecta a WeChat mediante el plugin de canal externo `@tencent-weixin/openclaw-weixin` de Tencent.

Estado: plugin externo. Los chats directos y los medios son compatibles. Los chats grupales no están anunciados por los metadatos de capacidades del plugin actual.

## Nomenclatura

  * **WeChat** es el nombre visible para el usuario en esta documentación.
  * **Weixin** es el nombre usado por el paquete de Tencent y por el id del plugin.
  * `openclaw-weixin` es el id de canal de OpenClaw.
  * `@tencent-weixin/openclaw-weixin` es el paquete npm.


Usa `openclaw-weixin` en comandos de CLI y rutas de configuración.

## Cómo funciona

El código de WeChat no vive en el repositorio principal de OpenClaw. OpenClaw proporciona el contrato genérico de plugin de canal, y el plugin externo proporciona el entorno de ejecución específico de WeChat:

  1. `openclaw plugins install` instala `@tencent-weixin/openclaw-weixin`.
  2. El Gateway descubre el manifiesto del plugin y carga el punto de entrada del plugin.
  3. El plugin registra el id de canal `openclaw-weixin`.
  4. `openclaw channels login --channel openclaw-weixin` inicia el inicio de sesión por QR.
  5. El plugin almacena las credenciales de la cuenta en el directorio de estado de OpenClaw.
  6. Cuando se inicia el Gateway, el plugin inicia su monitor de Weixin para cada cuenta configurada.
  7. Los mensajes entrantes de WeChat se normalizan mediante el contrato de canal, se enrutan al agente de OpenClaw seleccionado y se devuelven mediante la ruta saliente del plugin.


Esa separación importa: el núcleo de OpenClaw debe seguir siendo independiente de los canales. El inicio de sesión de WeChat, las llamadas a la API iLink de Tencent, la carga/descarga de medios, los tokens de contexto y la supervisión de cuentas pertenecen al plugin externo.

## Instalación

Instalación rápida:

bashCopy code
[code]
    npx -y @tencent-weixin/openclaw-weixin-cli install
[/code]

Instalación manual:

bashCopy code
[code]
    openclaw plugins install "@tencent-weixin/openclaw-weixin"openclaw config set plugins.entries.openclaw-weixin.enabled true
[/code]

Reinicia el Gateway después de la instalación:

bashCopy code
[code]
    openclaw gateway restart
[/code]

## Inicio de sesión

Ejecuta el inicio de sesión por QR en la misma máquina que ejecuta el Gateway:

bashCopy code
[code]
    openclaw channels login --channel openclaw-weixin
[/code]

Escanea el código QR con WeChat en tu teléfono y confirma el inicio de sesión. El plugin guarda el token de la cuenta localmente tras un escaneo correcto.

Para agregar otra cuenta de WeChat, ejecuta de nuevo el mismo comando de inicio de sesión. Para varias cuentas, aísla las sesiones de mensaje directo por cuenta, canal y remitente:

bashCopy code
[code]
    openclaw config set session.dmScope per-account-channel-peer
[/code]

## Control de acceso

Los mensajes directos usan el modelo normal de emparejamiento y lista de permitidos de OpenClaw para plugins de canal.

Aprueba nuevos remitentes:

bashCopy code
[code]
    openclaw pairing list openclaw-weixinopenclaw pairing approve openclaw-weixin &lt;CODE&gt;
[/code]

Para ver el modelo completo de control de acceso, consulta [Emparejamiento](</es/channels/pairing>).

## Compatibilidad

El plugin comprueba la versión del host de OpenClaw al iniciarse.

Línea del plugin | Versión de OpenClaw | Etiqueta npm  
---|---|---  
`2.x` | `>=2026.3.22` | `latest`  
`1.x` | `>=2026.1.0 <2026.3.22` | `legacy`  
  
Si el plugin informa que tu versión de OpenClaw es demasiado antigua, actualiza OpenClaw o instala la línea legacy del plugin:

bashCopy code
[code]
    openclaw plugins install @tencent-weixin/openclaw-weixin@legacy
[/code]

## Proceso sidecar

El plugin de WeChat puede ejecutar trabajo auxiliar junto al Gateway mientras supervisa la API iLink de Tencent. En el issue #68451, esa ruta auxiliar expuso un error en la limpieza genérica de Gateway obsoleto de OpenClaw: un proceso hijo podía intentar limpiar el proceso Gateway padre, lo que causaba bucles de reinicio bajo gestores de procesos como systemd.

La limpieza actual de inicio de OpenClaw excluye el proceso actual y sus ancestros, por lo que un auxiliar de canal no debe matar el Gateway que lo inició. Esta corrección es genérica; no es una ruta específica de WeChat en el núcleo.

## Solución de problemas

Comprueba la instalación y el estado:

bashCopy code
[code]
    openclaw plugins listopenclaw channels status --probeopenclaw --version
[/code]

Si el canal aparece como instalado pero no se conecta, confirma que el plugin está habilitado y reinicia:

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-weixin.enabled trueopenclaw gateway restart
[/code]

Si el Gateway se reinicia repetidamente después de habilitar WeChat, actualiza tanto OpenClaw como el plugin:

bashCopy code
[code]
    npm view @tencent-weixin/openclaw-weixin versionopenclaw plugins install "@tencent-weixin/openclaw-weixin" --forceopenclaw gateway restart
[/code]

Si el inicio informa que el paquete de plugin instalado `requires compiled runtime output for TypeScript entry`, el paquete npm se publicó sin los archivos de entorno de ejecución JavaScript compilados que OpenClaw necesita. Actualiza/reinstala después de que el publicador del plugin publique un paquete corregido, o deshabilita/desinstala temporalmente el plugin.

Deshabilitación temporal:

bashCopy code
[code]
    openclaw config set plugins.entries.openclaw-weixin.enabled falseopenclaw gateway restart
[/code]

## Documentación relacionada

  * Resumen de canales: [Canales de chat](</es/channels>)
  * Emparejamiento: [Emparejamiento](</es/channels/pairing>)
  * Enrutamiento de canales: [Enrutamiento de canales](</es/channels/channel-routing>)
  * Arquitectura de plugins: [Arquitectura de Plugin](</es/plugins/architecture>)
  * SDK de plugin de canal: [SDK de Plugin de canal](</es/plugins/sdk-channel-plugins>)
  * Paquete externo: [@tencent-weixin/openclaw-weixin](<https://www.npmjs.com/package/@tencent-weixin/openclaw-weixin>)


Was this useful?YesNo