---
title: Plugin de reuniones de Microsoft Teams
source_url: https://docs.openclaw.ai/es/plugins/teams-meetings
scraped_at: 2026-07-20
---

CapabilitiesPlugin guides

El plugin `teams-meetings` se une como invitado a enlaces de Microsoft Teams en el perfil de Chrome de OpenClaw. Acepta enlaces de trabajo bajo `teams.microsoft.com/l/meetup-join/...` y enlaces de consumidores bajo `teams.live.com/meet/...`. No crea reuniones, no se conecta por teléfono, no llama a Microsoft Graph ni graba reuniones.

## Configuración

La respuesta por voz utiliza los mismos requisitos previos de audio local que el [plugin de Google Meet](</es/plugins/google-meet>): macOS, el dispositivo de audio virtual `BlackHole 2ch` y SoX.

bashCopy code
[code]
    brew install blackhole-2ch soxsudo rebootsystem_profiler SPAudioDataType | grep -i BlackHolecommand -v sox
[/code]

Habilite el plugin y, a continuación, compruebe la configuración:

json5Copy code
[code]
    {  plugins: {    entries: {      "teams-meetings": {        enabled: true,        config: {          defaultMode: "agent",          chrome: { guestName: "OpenClaw Agent" },        },      },    },  },}
[/code]

bashCopy code
[code]
    openclaw teamsmeetings setupopenclaw teamsmeetings join 'https://teams.microsoft.com/l/meetup-join/...'
[/code]

Use `chromeNode.node` para ejecutar Chrome, BlackHole y SoX en un nodo macOS emparejado. El nodo debe permitir `teamsmeetings.chrome` y `browser.proxy`.

## Modos

Modo | Comportamiento  
---|---  
`agent` | La transcripción en tiempo real consulta al agente de OpenClaw configurado; las respuestas se generan mediante TTS.  
`bidi` | Un modelo de voz en tiempo real escucha y responde directamente.  
`transcribe` | Se une solo como observador y obtiene instantáneas de la transcripción de subtítulos en directo.  
  
El modo de transcripción habilita los subtítulos en directo de Teams tras la admisión y captura las filas de subtítulos atribuidas a cada participante. La acción `transcript` devuelve el búfer acotado de subtítulos de la sesión de reunión activa de OpenClaw.

## Limitaciones de la unión como invitado

El adaptador del navegador cierra la pantalla intermedia de la aplicación, rellena el nombre del invitado, apaga la cámara, configura el micrófono para el modo seleccionado y hace clic en el botón para unirse. El estado durante la llamada utiliza el control para colgar; los estados de sala de espera, inicio de sesión del inquilino y permisos del dispositivo devuelven motivos explícitos que requieren una acción manual. Se admiten las redirecciones del iniciador de reuniones para consumidores y las etiquetas `BlackHole 2ch (Virtual)` que muestra Chrome.

La política del inquilino de Teams puede exigir el inicio de sesión, la verificación por correo electrónico o la admisión por parte del organizador. Complete ese paso en el perfil de Chrome de OpenClaw y, a continuación, vuelva a intentar consultar el estado o usar la voz. El plugin no elude la política del inquilino.

El cliente web de Teams para consumidores se ha validado en un entorno real para la pantalla intermedia de la aplicación, la introducción del nombre del invitado, los controles previos a la unión del micrófono y la cámara, la unión, la admisión desde la sala de espera, los permisos multimedia, la detección de llamadas en curso, los subtítulos en directo, el enrutamiento de entrada y salida de BlackHole, la salida y la detección posterior a la llamada. Los inquilinos de trabajo pueden imponer políticas diferentes de inicio de sesión, verificación por correo electrónico, admisión y confirmación de salida; complete cualquier acción manual indicada en el perfil de Chrome de OpenClaw.

## Superficie de herramientas y del Gateway

La herramienta de agente `teams_meetings` admite `join`, `leave`, `status`, `transcript` y `speak`. Los métodos del Gateway utilizan el prefijo `teamsmeetings.*`. El comando del nodo es `teamsmeetings.chrome`.

## Contenido relacionado

  * [Descripción general de los plugins de reuniones](</es/plugins/meeting-plugins>)
  * [Canal de Microsoft Teams](</es/channels/msteams>)


Was this useful?YesNo

Open issue