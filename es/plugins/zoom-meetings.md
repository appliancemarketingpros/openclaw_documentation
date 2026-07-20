---
title: Plugin de reuniones de Zoom
source_url: https://docs.openclaw.ai/es/plugins/zoom-meetings
scraped_at: 2026-07-20
---

CapabilitiesPlugin guides

El plugin `zoom-meetings` se une como invitado a enlaces de reuniones de Zoom mediante la aplicación web de Zoom en el perfil de Chrome de OpenClaw. Acepta enlaces de reuniones bajo `zoom.us/j/...` y subdominios de cuentas como `example.zoom.us/j/...`. No crea reuniones, no se conecta por teléfono, no utiliza el SDK de reuniones de Zoom ni graba reuniones.

## Configuración

Las respuestas de voz utilizan los mismos requisitos locales de audio que el [plugin de Google Meet](</es/plugins/google-meet>): macOS, el dispositivo de audio virtual `BlackHole 2ch` y SoX.

bashCopy code
[code]
    brew install blackhole-2ch soxsudo rebootsystem_profiler SPAudioDataType | grep -i BlackHolecommand -v sox
[/code]

Habilite el plugin y, a continuación, compruebe la configuración:

json5Copy code
[code]
    {  plugins: {    entries: {      "zoom-meetings": {        enabled: true,        config: {          defaultMode: "agent",          chrome: { guestName: "OpenClaw Agent" },        },      },    },  },}
[/code]

bashCopy code
[code]
    openclaw zoommeetings setupopenclaw zoommeetings join 'https://zoom.us/j/1234567890'
[/code]

Utilice `chromeNode.node` para ejecutar Chrome, BlackHole y SoX en un nodo macOS emparejado. El nodo debe permitir `zoommeetings.chrome` y `browser.proxy`.

## Modos

Modo | Comportamiento  
---|---  
`agent` | La transcripción en tiempo real consulta al agente de OpenClaw configurado; TTS responde.  
`bidi` | Un modelo de voz en tiempo real escucha y responde directamente.  
`transcribe` | Conexión solo de observación con capturas de la transcripción de subtítulos en directo.  
  
El modo de transcripción habilita los subtítulos en directo de Zoom después de la admisión y captura la visualización acotada de subtítulos. La acción `transcript` devuelve el búfer de subtítulos de la sesión de reunión activa de OpenClaw.

## Limitaciones de la conexión como invitado

El adaptador del navegador selecciona **Join from browser** , completa el nombre del invitado, apaga la cámara, configura el micrófono para el modo seleccionado y hace clic en **Join**. La aplicación web de Zoom se ejecuta bajo `app.zoom.us`; el plugin concede a ese origen permisos de micrófono y selección de altavoz antes de la navegación. El estado durante la llamada utiliza el control Leave de Zoom. Los estados de sala de espera, inicio de sesión, código de acceso, CAPTCHA y permisos del dispositivo devuelven motivos explícitos que requieren intervención manual.

Las políticas del anfitrión y de la cuenta de Zoom pueden deshabilitar la conexión desde el navegador, exigir autenticación o verificación por correo electrónico, mostrar un CAPTCHA o requerir la admisión del anfitrión. Complete ese paso en el perfil de Chrome de OpenClaw y, a continuación, vuelva a consultar el estado o a intentar la intervención de voz. El plugin no elude las políticas de Zoom.

La aplicación web de Zoom se ha validado en directo con una reunión de prueba oficial de Zoom para comprobar la pantalla intermedia de la aplicación, la introducción del nombre del invitado en un iframe, los controles del micrófono y la cámara previos a la conexión, la conexión, los permisos multimedia del navegador y macOS, la detección durante la llamada, la habilitación de subtítulos en directo y la detección de la finalización por parte del anfitrión. Los estados de sala de espera y autenticación dependen de la política del anfitrión y conservan alternativas basadas en texto cuando no hay disponible un identificador DOM estable.

## Superficie de herramientas y del Gateway

La herramienta del agente `zoom_meetings` admite `join`, `leave`, `status`, `transcript` y `speak`. Los métodos del Gateway utilizan el prefijo `zoommeetings.*`. El comando del nodo es `zoommeetings.chrome`.

## Relacionado

  * [Descripción general de los plugins de reuniones](</es/plugins/meeting-plugins>)


Was this useful?YesNo

Open issue