---
title: Navegador
source_url: https://docs.openclaw.ai/es/cli/browser
scraped_at: 2026-05-25
---

# `openclaw browser`

Administra la superficie de control del navegador de OpenClaw y ejecuta acciones del navegador (ciclo de vida, perfiles, pestañas, instantáneas, capturas de pantalla, navegación, entrada, emulación de estado y depuración).

Relacionado:

  * Herramienta del navegador + API: [Herramienta del navegador](</es/tools/browser>)


## Marcas comunes

  * `--url <gatewayWsUrl>`: URL WebSocket del Gateway (usa la configuración por defecto).
  * `--token <token>`: token del Gateway (si se requiere).
  * `--timeout <ms>`: tiempo de espera de la solicitud (ms).
  * `--expect-final`: espera una respuesta final del Gateway.
  * `--browser-profile <name>`: elige un perfil de navegador (por defecto desde la configuración).
  * `--json`: salida legible por máquinas (donde sea compatible).


## Inicio rápido (local)

bashCopy code
[code]
    openclaw browser profilesopenclaw browser --browser-profile openclaw startopenclaw browser --browser-profile openclaw open https://example.comopenclaw browser --browser-profile openclaw snapshot
[/code]

Los agentes pueden ejecutar la misma comprobación de preparación con `browser({ action: "doctor" })`.

## Solución rápida de problemas

Si `start` falla con `not reachable after start`, primero soluciona la preparación de CDP. Si `start` y `tabs` funcionan pero `open` o `navigate` falla, el plano de control del navegador está en buen estado y el fallo suele ser la política SSRF de navegación.

Secuencia mínima:

bashCopy code
[code]
    openclaw browser --browser-profile openclaw doctoropenclaw browser --browser-profile openclaw startopenclaw browser --browser-profile openclaw tabsopenclaw browser --browser-profile openclaw open https://example.com
[/code]

Guía detallada: [Solución de problemas del navegador](</es/tools/browser#cdp-startup-failure-vs-navigation-ssrf-block>)

## Ciclo de vida

bashCopy code
[code]
    openclaw browser statusopenclaw browser doctoropenclaw browser doctor --deepopenclaw browser startopenclaw browser start --headlessopenclaw browser stopopenclaw browser --browser-profile openclaw reset-profile
[/code]

Notas:

  * `doctor --deep` agrega una prueba de instantánea en vivo. Es útil cuando la preparación básica de CDP está en verde, pero quieres una prueba de que la pestaña actual se puede inspeccionar.
  * Para perfiles `attachOnly` y CDP remotos, `openclaw browser stop` cierra la sesión de control activa y borra las anulaciones temporales de emulación incluso cuando OpenClaw no inició el proceso del navegador.
  * Para perfiles locales administrados, `openclaw browser stop` detiene el proceso de navegador generado.
  * `openclaw browser start --headless` se aplica solo a esa solicitud de inicio y solo cuando OpenClaw inicia un navegador local administrado. No reescribe `browser.headless` ni la configuración del perfil, y no tiene efecto en un navegador que ya está en ejecución.
  * En hosts Linux sin `DISPLAY` ni `WAYLAND_DISPLAY`, los perfiles locales administrados se ejecutan automáticamente sin interfaz gráfica a menos que `OPENCLAW_BROWSER_HEADLESS=0`, `browser.headless=false` o `browser.profiles.<name>.headless=false` soliciten explícitamente un navegador visible.


## Si falta el comando

Si `openclaw browser` es un comando desconocido, revisa `plugins.allow` en `~/.openclaw/openclaw.json`.

Cuando `plugins.allow` esté presente, lista explícitamente el Plugin de navegador incluido a menos que la configuración ya tenga un bloque raíz `browser`:

json5Copy code
[code]
    {  plugins: {    allow: ["telegram", "browser"],  },}
[/code]

Un bloque raíz explícito `browser`, por ejemplo `browser.enabled=true` o `browser.profiles.<name>`, también activa el Plugin de navegador incluido bajo una lista de Plugins permitidos restrictiva.

Relacionado: [Herramienta del navegador](</es/tools/browser#missing-browser-command-or-tool>)

## Perfiles

Los perfiles son configuraciones con nombre para el enrutamiento del navegador. En la práctica:

  * `openclaw`: inicia o se adjunta a una instancia dedicada de Chrome administrada por OpenClaw (directorio de datos de usuario aislado).
  * `user`: controla tu sesión existente de Chrome con sesión iniciada mediante Chrome DevTools MCP.
  * perfiles CDP personalizados: apuntan a un endpoint CDP local o remoto.

bashCopy code
[code]
    openclaw browser profilesopenclaw browser create-profile --name work --color "#FF5A36"openclaw browser create-profile --name chrome-live --driver existing-sessionopenclaw browser create-profile --name remote --cdp-url https://browser-host.example.comopenclaw browser delete-profile --name work
[/code]

Usa un perfil específico:

bashCopy code
[code]
    openclaw browser --browser-profile work tabs
[/code]

## Pestañas

bashCopy code
[code]
    openclaw browser tabsopenclaw browser tab new --label docsopenclaw browser tab label t1 docsopenclaw browser tab select 2openclaw browser tab close 2openclaw browser open https://docs.openclaw.ai --label docsopenclaw browser focus docsopenclaw browser close t1
[/code]

`tabs` devuelve primero `suggestedTargetId`, luego el `tabId` estable, como `t1`, la etiqueta opcional y el `targetId` sin procesar. Los agentes deben pasar `suggestedTargetId` de vuelta a `focus`, `close`, instantáneas y acciones. Puedes asignar una etiqueta con `open --label`, `tab new --label` o `tab label`; se aceptan etiquetas, ids de pestaña, ids de destino sin procesar y prefijos únicos de id de destino. Cuando Chromium reemplaza el destino sin procesar subyacente durante una navegación o envío de formulario, OpenClaw mantiene el `tabId`/la etiqueta estable asociado a la pestaña de reemplazo cuando puede demostrar la coincidencia. Los ids de destino sin procesar siguen siendo volátiles; prefiere `suggestedTargetId`.

## Instantánea / captura de pantalla / acciones

Instantánea:

bashCopy code
[code]
    openclaw browser snapshotopenclaw browser snapshot --urls
[/code]

Captura de pantalla:

bashCopy code
[code]
    openclaw browser screenshotopenclaw browser screenshot --full-pageopenclaw browser screenshot --ref e12openclaw browser screenshot --labels
[/code]

Notas:

  * `--full-page` es solo para capturas de página; no se puede combinar con `--ref` ni `--element`.
  * Los perfiles `existing-session` / `user` admiten capturas de pantalla de página y capturas `--ref` desde la salida de instantánea, pero no capturas CSS `--element`.
  * `--labels` superpone las referencias de instantánea actuales sobre la captura de pantalla.
  * `snapshot --urls` agrega los destinos de enlaces descubiertos a las instantáneas de IA para que los agentes puedan elegir destinos de navegación directos en lugar de adivinar solo a partir del texto del enlace.


Navegar/hacer clic/escribir (automatización de UI basada en referencias):

bashCopy code
[code]
    openclaw browser navigate https://example.comopenclaw browser click <ref>openclaw browser click-coords 120 340openclaw browser type <ref> "hello"openclaw browser press Enteropenclaw browser hover <ref>openclaw browser scrollintoview <ref>openclaw browser drag <startRef> <endRef>openclaw browser select <ref> OptionA OptionBopenclaw browser fill --fields '[{"ref":"1","value":"Ada"}]'openclaw browser wait --text "Done"openclaw browser evaluate --fn '(el) => el.textContent' --ref <ref>
[/code]

Las respuestas de acciones devuelven el `targetId` sin procesar actual después de un reemplazo de página activado por la acción cuando OpenClaw puede demostrar la pestaña de reemplazo. Aun así, los scripts deben almacenar y pasar `suggestedTargetId`/etiquetas para flujos de trabajo de larga duración.

Ayudantes de archivos + diálogos:

bashCopy code
[code]
    openclaw browser upload /tmp/openclaw/uploads/file.pdf --ref <ref>openclaw browser waitfordownloadopenclaw browser download <ref> report.pdfopenclaw browser dialog --accept
[/code]

Los perfiles de Chrome administrados guardan las descargas ordinarias activadas por clic en el directorio de descargas de OpenClaw (`/tmp/openclaw/downloads` por defecto, o la raíz temporal configurada). Usa `waitfordownload` o `download` cuando el agente necesite esperar un archivo específico y devolver su ruta; esos esperadores explícitos son dueños de la siguiente descarga.

## Estado y almacenamiento

Vista + emulación:

bashCopy code
[code]
    openclaw browser resize 1280 720openclaw browser set viewport 1280 720openclaw browser set offline onopenclaw browser set media darkopenclaw browser set timezone Europe/Londonopenclaw browser set locale en-GBopenclaw browser set geo 51.5074 -0.1278 --accuracy 25openclaw browser set device "iPhone 14"openclaw browser set headers '{"x-test":"1"}'openclaw browser set credentials myuser mypass
[/code]

Cookies + almacenamiento:

bashCopy code
[code]
    openclaw browser cookiesopenclaw browser cookies set session abc123 --url https://example.comopenclaw browser cookies clearopenclaw browser storage local getopenclaw browser storage local set token abc123openclaw browser storage session clear
[/code]

## Depuración

bashCopy code
[code]
    openclaw browser console --level erroropenclaw browser pdfopenclaw browser responsebody "**/api"openclaw browser highlight <ref>openclaw browser errors --clearopenclaw browser requests --filter apiopenclaw browser trace startopenclaw browser trace stop --out trace.zip
[/code]

## Chrome existente mediante MCP

Usa el perfil integrado `user` o crea tu propio perfil `existing-session`:

bashCopy code
[code]
    openclaw browser --browser-profile user tabsopenclaw browser create-profile --name chrome-live --driver existing-sessionopenclaw browser create-profile --name brave-live --driver existing-session --user-data-dir "~/Library/Application Support/BraveSoftware/Brave-Browser"openclaw browser --browser-profile chrome-live tabs
[/code]

Esta ruta es solo para host. Para Docker, servidores sin interfaz gráfica, Browserless u otras configuraciones remotas, usa un perfil CDP en su lugar.

Límites actuales de existing-session:

  * las acciones impulsadas por instantáneas usan referencias, no selectores CSS
  * `browser.actionTimeoutMs` establece por defecto las solicitudes `act` compatibles en 60000 ms cuando los llamadores omiten `timeoutMs`; `timeoutMs` por llamada sigue prevaleciendo.
  * `click` es solo clic izquierdo
  * `type` no admite `slowly=true`
  * `press` no admite `delayMs`
  * `hover`, `scrollintoview`, `drag`, `select`, `fill` y `evaluate` rechazan anulaciones de tiempo de espera por llamada
  * `select` admite solo un valor
  * `wait --load networkidle` no es compatible
  * las cargas de archivos requieren `--ref` / `--input-ref`, no admiten CSS `--element` y actualmente admiten un archivo a la vez
  * los hooks de diálogo no admiten `--timeout`
  * las capturas de pantalla admiten capturas de página y `--ref`, pero no CSS `--element`
  * `responsebody`, la intercepción de descargas, la exportación PDF y las acciones por lotes todavía requieren un navegador administrado o un perfil CDP sin procesar


## Control remoto del navegador (proxy de host de nodo)

Si el Gateway se ejecuta en una máquina distinta a la del navegador, ejecuta un **host de nodo** en la máquina que tiene Chrome/Brave/Edge/Chromium. El Gateway enviará por proxy las acciones del navegador a ese nodo (no se requiere un servidor de control del navegador separado).

Usa `gateway.nodes.browser.mode` para controlar el enrutamiento automático y `gateway.nodes.browser.node` para fijar un nodo específico si hay varios conectados.

Seguridad + configuración remota: [Herramienta del navegador](</es/tools/browser>), [Acceso remoto](</es/gateway/remote>), [Tailscale](</es/gateway/tailscale>), [Seguridad](</es/gateway/security>)

## Relacionado

  * [Referencia de CLI](</es/cli>)
  * [Navegador](</es/tools/browser>)


Was this useful?YesNo