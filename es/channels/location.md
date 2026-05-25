---
title: Análisis de ubicación del canal
source_url: https://docs.openclaw.ai/es/channels/location
scraped_at: 2026-05-25
---

OpenClaw normaliza las ubicaciones compartidas desde canales de chat en:

  * texto breve de coordenadas agregado al cuerpo entrante, y
  * campos estructurados en la carga de contexto de respuesta automática. Las etiquetas, direcciones y leyendas/comentarios proporcionados por el canal se representan en el prompt mediante el bloque JSON compartido de metadatos no confiables, no en línea dentro del cuerpo del usuario.


Actualmente compatible con:

  * **Telegram** (pines de ubicación + lugares + ubicaciones en tiempo real)
  * **WhatsApp** (`locationMessage` \+ `liveLocationMessage`)
  * **Matrix** (`m.location` con `geo_uri`)


## Formato del texto

Las ubicaciones se representan como líneas legibles sin corchetes:

  * Pin: 
    * `📍 48.858844, 2.294351 ±12m`
  * Lugar con nombre: 
    * `📍 48.858844, 2.294351 ±12m`
  * Compartir en vivo: 
    * `🛰 Live location: 48.858844, 2.294351 ±12m`


Si el canal incluye una etiqueta, dirección o leyenda/comentario, se conserva en la carga de contexto y aparece en el prompt como JSON no confiable delimitado:

textCopy code
[code]
    Location (untrusted metadata):```json{  "latitude": 48.858844,  "longitude": 2.294351,  "name": "Eiffel Tower",  "address": "Champ de Mars, Paris",  "caption": "Meet here"}```
[/code]

## Campos de contexto

Cuando hay una ubicación presente, estos campos se agregan a `ctx`:

  * `LocationLat` (número)
  * `LocationLon` (número)
  * `LocationAccuracy` (número, metros; opcional)
  * `LocationName` (cadena; opcional)
  * `LocationAddress` (cadena; opcional)
  * `LocationSource` (`pin | place | live`)
  * `LocationIsLive` (booleano)
  * `LocationCaption` (cadena; opcional)


El renderizador de prompts trata `LocationName`, `LocationAddress` y `LocationCaption` como metadatos no confiables y los serializa a través de la misma ruta JSON acotada utilizada para otro contexto del canal.

## Notas del canal

  * **Telegram** : los lugares se asignan a `LocationName/LocationAddress`; las ubicaciones en tiempo real usan `live_period`.
  * **WhatsApp** : `locationMessage.comment` y `liveLocationMessage.caption` rellenan `LocationCaption`.
  * **Matrix** : `geo_uri` se analiza como una ubicación de pin; la altitud se ignora y `LocationIsLive` siempre es false.


## Relacionado

  * [Comando de ubicación (nodes)](</es/nodes/location-command>)
  * [Captura de cámara](</es/nodes/camera>)
  * [Comprensión de medios](</es/nodes/media-understanding>)


Was this useful?YesNo