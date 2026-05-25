---
title: Primeros pasos
source_url: https://docs.openclaw.ai/es/start/getting-started
scraped_at: 2026-05-25
---

Instala OpenClaw, ejecuta la incorporación y chatea con tu asistente de IA, todo en unos 5 minutos. Al final tendrás un Gateway en ejecución, autenticación configurada y una sesión de chat funcionando.

## Lo que necesitas

  * **Node.js** — se recomienda Node 24 (también se admite Node 22.16+)
  * **Una clave de API** de un proveedor de modelos (Anthropic, OpenAI, Google, etc.) — la incorporación te la pedirá


## Configuración rápida

* ### Instalar OpenClaw

### macOS / Linux

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

![Proceso del script de instalación](/assets/install-script.svg)

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

* ### Ejecutar la incorporación

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

El asistente te guía para elegir un proveedor de modelos, configurar una clave de API y configurar el Gateway. Tarda unos 2 minutos.

Consulta [Incorporación (CLI)](</es/start/wizard>) para ver la referencia completa.

* ### Verificar que el Gateway esté en ejecución

bashCopy code
[code]
    openclaw gateway status
[/code]

Deberías ver que el Gateway escucha en el puerto 18789.

* ### Abrir el panel

bashCopy code
[code]
    openclaw dashboard
[/code]

Esto abre la interfaz de control en tu navegador. Si carga, todo funciona.

* ### Enviar tu primer mensaje

Escribe un mensaje en el chat de la interfaz de control y deberías recibir una respuesta de IA.

¿Quieres chatear desde tu teléfono en su lugar? El canal más rápido de configurar es [Telegram](</es/channels/telegram>) (solo un token de bot). Consulta [Canales](</es/channels>) para ver todas las opciones.

Avanzado: montar una compilación personalizada de la interfaz de control

Si mantienes una compilación localizada o personalizada del panel, apunta `gateway.controlUi.root` a un directorio que contenga tus recursos estáticos compilados y `index.html`.

bashCopy code
[code]
    mkdir -p "$HOME/.openclaw/control-ui-custom"# Copy your built static files into that directory.
[/code]

Luego configura:

jsonCopy code
[code]
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "$HOME/.openclaw/control-ui-custom"  }}}
[/code]

Reinicia el Gateway y vuelve a abrir el panel:

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## Qué hacer después

[**Conectar un canal** Discord, Feishu, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo y más. ](</es/channels>) [**Emparejamiento y seguridad** Controla quién puede enviar mensajes a tu agente. ](</es/channels/pairing>) [**Configurar el Gateway** Modelos, herramientas, sandbox y configuración avanzada. ](</es/gateway/configuration>) [**Explorar herramientas** Navegador, exec, búsqueda web, Skills y plugins. ](</es/tools>)

Avanzado: variables de entorno

Si ejecutas OpenClaw como una cuenta de servicio o quieres rutas personalizadas:

  * `OPENCLAW_HOME` — directorio de inicio para la resolución interna de rutas
  * `OPENCLAW_STATE_DIR` — sobrescribe el directorio de estado
  * `OPENCLAW_CONFIG_PATH` — sobrescribe la ruta del archivo de configuración


Referencia completa: [Variables de entorno](</es/help/environment>).

## Relacionado

  * [Resumen de instalación](</es/install>)
  * [Resumen de canales](</es/channels>)
  * [Configuración](</es/start/setup>)


Was this useful?YesNo