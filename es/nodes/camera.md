---
title: Captura de cámara
source_url: https://docs.openclaw.ai/es/nodes/camera
scraped_at: 2026-05-25
---

OpenClaw admite **captura con cámara** para flujos de trabajo de agentes:

  * **Node de iOS** (emparejado mediante Gateway): captura una **foto** (`jpg`) o un **clip de video corto** (`mp4`, con audio opcional) mediante `node.invoke`.
  * **Node de Android** (emparejado mediante Gateway): captura una **foto** (`jpg`) o un **clip de video corto** (`mp4`, con audio opcional) mediante `node.invoke`.
  * **app de macOS** (Node mediante Gateway): captura una **foto** (`jpg`) o un **clip de video corto** (`mp4`, con audio opcional) mediante `node.invoke`.


Todo acceso a la cámara está protegido por **ajustes controlados por el usuario**.

## Node de iOS

### Ajuste de usuario (activado de forma predeterminada)

  * Pestaña Ajustes de iOS → **Cámara** → **Permitir cámara** (`camera.enabled`) 
    * Predeterminado: **activado** (una clave ausente se trata como habilitada).
    * Cuando está desactivado: los comandos `camera.*` devuelven `CAMERA_DISABLED`.


### Comandos (mediante Gateway `node.invoke`)

  * `camera.list`

    * Carga útil de respuesta: 
      * `devices`: array de `{ id, name, position, deviceType }`
  * `camera.snap`

    * Parámetros: 
      * `facing`: `front|back` (predeterminado: `front`)
      * `maxWidth`: número (opcional; predeterminado `1600` en el Node de iOS)
      * `quality`: `0..1` (opcional; predeterminado `0.9`)
      * `format`: actualmente `jpg`
      * `delayMs`: número (opcional; predeterminado `0`)
      * `deviceId`: cadena (opcional; desde `camera.list`)
    * Carga útil de respuesta: 
      * `format: "jpg"`
      * `base64: "<...>"`
      * `width`, `height`
    * Protección de carga útil: las fotos se recomprimen para mantener la carga útil base64 por debajo de 5 MB.
  * `camera.clip`

    * Parámetros: 
      * `facing`: `front|back` (predeterminado: `front`)
      * `durationMs`: número (predeterminado `3000`, limitado a un máximo de `60000`)
      * `includeAudio`: booleano (predeterminado `true`)
      * `format`: actualmente `mp4`
      * `deviceId`: cadena (opcional; desde `camera.list`)
    * Carga útil de respuesta: 
      * `format: "mp4"`
      * `base64: "<...>"`
      * `durationMs`
      * `hasAudio`


### Requisito de primer plano

Al igual que `canvas.*`, el Node de iOS solo permite comandos `camera.*` en **primer plano**. Las invocaciones en segundo plano devuelven `NODE_BACKGROUND_UNAVAILABLE`.

### Ayudante de CLI (archivos temporales + MEDIA)

La forma más sencilla de obtener adjuntos es mediante el ayudante de CLI, que escribe los medios decodificados en un archivo temporal e imprime `MEDIA:<path>`.

Ejemplos:

bashCopy code
[code]
    openclaw nodes camera snap --node <id>               # default: both front + back (2 MEDIA lines)openclaw nodes camera snap --node <id> --facing frontopenclaw nodes camera clip --node <id> --duration 3000openclaw nodes camera clip --node <id> --no-audio
[/code]

Notas:

  * `nodes camera snap` usa de forma predeterminada **ambas** orientaciones para dar al agente ambas vistas.
  * Los archivos de salida son temporales (en el directorio temporal del SO) salvo que crees tu propio contenedor.


## Node de Android

### Ajuste de usuario de Android (activado de forma predeterminada)

  * Hoja de ajustes de Android → **Cámara** → **Permitir cámara** (`camera.enabled`) 
    * Predeterminado: **activado** (una clave ausente se trata como habilitada).
    * Cuando está desactivado: los comandos `camera.*` devuelven `CAMERA_DISABLED`.


### Permisos

  * Android requiere permisos en tiempo de ejecución: 
    * `CAMERA` para `camera.snap` y `camera.clip`.
    * `RECORD_AUDIO` para `camera.clip` cuando `includeAudio=true`.


Si faltan permisos, la app los solicitará cuando sea posible; si se deniegan, las solicitudes `camera.*` fallan con un error `*_PERMISSION_REQUIRED`.

### Requisito de primer plano en Android

Al igual que `canvas.*`, el Node de Android solo permite comandos `camera.*` en **primer plano**. Las invocaciones en segundo plano devuelven `NODE_BACKGROUND_UNAVAILABLE`.

### Comandos de Android (mediante Gateway `node.invoke`)

  * `camera.list`
    * Carga útil de respuesta: 
      * `devices`: array de `{ id, name, position, deviceType }`


### Protección de carga útil

Las fotos se recomprimen para mantener la carga útil base64 por debajo de 5 MB.

## app de macOS

### Ajuste de usuario (desactivado de forma predeterminada)

La app complementaria de macOS expone una casilla:

  * **Ajustes → General → Permitir cámara** (`openclaw.cameraEnabled`) 
    * Predeterminado: **desactivado**
    * Cuando está desactivado: las solicitudes de cámara devuelven "Cámara deshabilitada por el usuario".


### Ayudante de CLI (invocación de Node)

Usa la CLI principal `openclaw` para invocar comandos de cámara en el Node de macOS.

Ejemplos:

bashCopy code
[code]
    openclaw nodes camera list --node <id>            # list camera idsopenclaw nodes camera snap --node <id>            # prints MEDIA:<path>openclaw nodes camera snap --node <id> --max-width 1280openclaw nodes camera snap --node <id> --delay-ms 2000openclaw nodes camera snap --node <id> --device-id <id>openclaw nodes camera clip --node <id> --duration 10s          # prints MEDIA:<path>openclaw nodes camera clip --node <id> --duration-ms 3000      # prints MEDIA:<path> (legacy flag)openclaw nodes camera clip --node <id> --device-id <id>openclaw nodes camera clip --node <id> --no-audio
[/code]

Notas:

  * `openclaw nodes camera snap` usa `maxWidth=1600` de forma predeterminada salvo que se anule.
  * En macOS, `camera.snap` espera `delayMs` (predeterminado 2000ms) después del calentamiento/estabilización de exposición antes de capturar.
  * Las cargas útiles de fotos se recomprimen para mantener base64 por debajo de 5 MB.


## Seguridad + límites prácticos

  * El acceso a la cámara y al micrófono activa los avisos de permiso habituales del SO (y requiere cadenas de uso en Info.plist).
  * Los clips de video están limitados (actualmente `<= 60s`) para evitar cargas útiles de Node demasiado grandes (sobrecarga de base64 + límites de mensajes).


## Video de pantalla de macOS (nivel del SO)

Para video de _pantalla_ (no de cámara), usa la app complementaria de macOS:

bashCopy code
[code]
    openclaw nodes screen record --node <id> --duration 10s --fps 15   # prints MEDIA:<path>
[/code]

Notas:

  * Requiere el permiso **Grabación de pantalla** de macOS (TCC).


## Relacionado

  * [Compatibilidad con imágenes y medios](</es/nodes/images>)
  * [Comprensión de medios](</es/nodes/media-understanding>)
  * [Comando de ubicación](</es/nodes/location-command>)


Was this useful?YesNo