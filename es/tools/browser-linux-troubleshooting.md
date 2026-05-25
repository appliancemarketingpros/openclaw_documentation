---
title: Solución de problemas del navegador
source_url: https://docs.openclaw.ai/es/tools/browser-linux-troubleshooting
scraped_at: 2026-05-25
---

## Problema: "Error al iniciar Chrome CDP en el puerto 18800"

El servidor de control del navegador de OpenClaw no puede iniciar Chrome/Brave/Edge/Chromium con el error:

CodeCopy code
[code]
    {"error":"Error: Failed to start Chrome CDP on port 18800 for profile \"openclaw\"."}
[/code]

### Causa raíz

En Ubuntu (y muchas distribuciones Linux), la instalación predeterminada de Chromium es un **paquete snap**. El confinamiento AppArmor de Snap interfiere con la forma en que OpenClaw genera y supervisa el proceso del navegador.

El comando `apt install chromium` instala un paquete auxiliar que redirige a snap:

CodeCopy code
[code]
    Note, selecting 'chromium-browser' instead of 'chromium'chromium-browser is already the newest version (2:1snap1-0ubuntu2).
[/code]

Esto NO es un navegador real: es solo un wrapper.

Otros fallos de inicio comunes en Linux:

  * `The profile appears to be in use by another Chromium process` significa que Chrome encontró archivos de bloqueo `Singleton*` obsoletos en el directorio del perfil gestionado. OpenClaw elimina esos bloqueos y vuelve a intentarlo una vez cuando el bloqueo apunta a un proceso inactivo o de un host diferente.
  * `Missing X server or $DISPLAY` significa que se solicitó explícitamente un navegador visible en un host sin sesión de escritorio. De forma predeterminada, los perfiles gestionados locales ahora vuelven al modo headless en Linux cuando `DISPLAY` y `WAYLAND_DISPLAY` no están definidos. Si defines `OPENCLAW_BROWSER_HEADLESS=0`, `browser.headless: false` o `browser.profiles.<name>.headless: false`, elimina esa anulación con interfaz visible, define `OPENCLAW_BROWSER_HEADLESS=1`, inicia `Xvfb`, ejecuta `openclaw browser start --headless` para un inicio gestionado puntual, o ejecuta OpenClaw en una sesión de escritorio real.


### Solución 1: Instalar Google Chrome (recomendado)

Instala el paquete `.deb` oficial de Google Chrome, que no está aislado por snap:

bashCopy code
[code]
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.debsudo dpkg -i google-chrome-stable_current_amd64.debsudo apt --fix-broken install -y  # if there are dependency errors
[/code]

Luego actualiza tu configuración de OpenClaw (`~/.openclaw/openclaw.json`):

jsonCopy code
[code]
    {  "browser": {    "enabled": true,    "executablePath": "/usr/bin/google-chrome-stable",    "headless": true,    "noSandbox": true  }}
[/code]

### Solución 2: Usar Snap Chromium en modo solo adjuntar

Si debes usar snap Chromium, configura OpenClaw para adjuntarse a un navegador iniciado manualmente:

  1. Actualiza la configuración:

jsonCopy code
[code]
    {  "browser": {    "enabled": true,    "attachOnly": true,    "headless": true,    "noSandbox": true  }}
[/code]

  2. Inicia Chromium manualmente:

bashCopy code
[code]
    chromium-browser --headless --no-sandbox --disable-gpu \  --remote-debugging-port=18800 \  --user-data-dir=$HOME/.openclaw/browser/openclaw/user-data \  about:blank &
[/code]

  3. Opcionalmente, crea un servicio de usuario systemd para iniciar Chrome automáticamente:

iniCopy code
[code]
    # ~/.config/systemd/user/openclaw-browser.service[Unit]Description=OpenClaw Browser (Chrome CDP)After=network.target [Service]ExecStart=/snap/bin/chromium --headless --no-sandbox --disable-gpu --remote-debugging-port=18800 --user-data-dir=%h/.openclaw/browser/openclaw/user-data about:blankRestart=on-failureRestartSec=5 [Install]WantedBy=default.target
[/code]

Habilítalo con: `systemctl --user enable --now openclaw-browser.service`

### Verificar que el navegador funciona

Comprueba el estado:

bashCopy code
[code]
    curl -s http://127.0.0.1:18791/ | jq '{running, pid, chosenBrowser}'
[/code]

Prueba la navegación:

bashCopy code
[code]
    curl -s -X POST http://127.0.0.1:18791/startcurl -s http://127.0.0.1:18791/tabs
[/code]

### Referencia de configuración

Opción | Descripción | Valor predeterminado  
---|---|---  
`browser.enabled` | Habilitar el control del navegador | `true`  
`browser.executablePath` | Ruta a un binario de navegador basado en Chromium (Chrome/Brave/Edge/Chromium) | detectado automáticamente (prefiere el navegador predeterminado cuando está basado en Chromium)  
`browser.headless` | Ejecutar sin GUI | `false`  
`OPENCLAW_BROWSER_HEADLESS` | Anulación por proceso para el modo headless del navegador gestionado local | sin definir  
`browser.noSandbox` | Añadir la marca `--no-sandbox` (necesaria para algunas configuraciones de Linux) | `false`  
`browser.attachOnly` | No iniciar el navegador; solo adjuntarse al existente | `false`  
`browser.cdpPort` | Puerto de Chrome DevTools Protocol | `18800`  
`browser.localLaunchTimeoutMs` | Tiempo de espera de descubrimiento de Chrome gestionado local | `15000`  
`browser.localCdpReadyTimeoutMs` | Tiempo de espera de disponibilidad de CDP tras el inicio gestionado local | `8000`  
  
En Raspberry Pi, hosts VPS antiguos o almacenamiento lento, aumenta `browser.localLaunchTimeoutMs` cuando Chrome necesita más tiempo para exponer su endpoint HTTP de CDP. Aumenta `browser.localCdpReadyTimeoutMs` cuando el inicio tiene éxito pero `openclaw browser start` aún informa `not reachable after start`. Los valores deben ser enteros positivos de hasta `120000` ms; los valores de configuración no válidos se rechazan.

### Problema: "No se encontraron pestañas de Chrome para profile="user""

Estás usando un perfil `existing-session` / Chrome MCP. OpenClaw puede ver Chrome local, pero no hay pestañas abiertas disponibles a las que adjuntarse.

Opciones de corrección:

  1. **Usa el navegador gestionado:** `openclaw browser start --browser-profile openclaw` (o define `browser.defaultProfile: "openclaw"`).
  2. **Usa Chrome MCP:** asegúrate de que Chrome local esté ejecutándose con al menos una pestaña abierta y luego vuelve a intentarlo con `--browser-profile user`.


Notas:

  * `user` es solo para el host. Para servidores Linux, contenedores o hosts remotos, prefiere perfiles CDP.
  * `user` / otros perfiles `existing-session` mantienen los límites actuales de Chrome MCP: acciones basadas en ref, hooks de carga de un archivo, sin anulaciones de tiempo de espera de diálogos, sin `wait --load networkidle`, y sin `responsebody`, exportación a PDF, interceptación de descargas ni acciones por lotes.
  * Los perfiles locales `openclaw` asignan automáticamente `cdpPort`/`cdpUrl`; define esos valores solo para CDP remoto.
  * Los perfiles CDP remotos aceptan `http://`, `https://`, `ws://` y `wss://`. Usa HTTP(S) para el descubrimiento de `/json/version`, o WS(S) cuando tu servicio de navegador te proporcione una URL directa de socket de DevTools.


## Relacionado

  * [Navegador](</es/tools/browser>)
  * [Inicio de sesión en el navegador](</es/tools/browser-login>)
  * [Solución de problemas de WSL2 del navegador](</es/tools/browser-wsl2-windows-remote-cdp-troubleshooting>)


Was this useful?YesNo