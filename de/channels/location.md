---
title: Kanal-Standort-Parsing
source_url: https://docs.openclaw.ai/de/channels/location
scraped_at: 2026-05-25
---

OpenClaw normalisiert geteilte Standorte aus Chat-Kanälen in:

  * knappen Koordinatentext, der an den eingehenden Body angehängt wird, und
  * strukturierte Felder in der Auto-Reply-Kontextnutzlast. Vom Kanal bereitgestellte Labels, Adressen und Bildunterschriften/Kommentare werden über den gemeinsamen JSON-Block für nicht vertrauenswürdige Metadaten in den Prompt gerendert, nicht inline im Benutzer-Body.


Derzeit unterstützt:

  * **Telegram** (Standort-Pins + Orte + Live-Standorte)
  * **WhatsApp** (`locationMessage` \+ `liveLocationMessage`)
  * **Matrix** (`m.location` mit `geo_uri`)


## Textformatierung

Standorte werden als benutzerfreundliche Zeilen ohne Klammern gerendert:

  * Pin: 
    * `📍 48.858844, 2.294351 ±12m`
  * Benannter Ort: 
    * `📍 48.858844, 2.294351 ±12m`
  * Live-Freigabe: 
    * `🛰 Live-Standort: 48.858844, 2.294351 ±12m`


Wenn der Kanal ein Label, eine Adresse oder eine Bildunterschrift/einen Kommentar enthält, bleibt dies in der Kontextnutzlast erhalten und erscheint im Prompt als eingerahmtes nicht vertrauenswürdiges JSON:

textCopy code
[code]
    Standort (nicht vertrauenswürdige Metadaten):```json{  "latitude": 48.858844,  "longitude": 2.294351,  "name": "Eiffel Tower",  "address": "Champ de Mars, Paris",  "caption": "Meet here"}```
[/code]

## Kontextfelder

Wenn ein Standort vorhanden ist, werden diese Felder zu `ctx` hinzugefügt:

  * `LocationLat` (Zahl)
  * `LocationLon` (Zahl)
  * `LocationAccuracy` (Zahl, Meter; optional)
  * `LocationName` (String; optional)
  * `LocationAddress` (String; optional)
  * `LocationSource` (`pin | place | live`)
  * `LocationIsLive` (Boolean)
  * `LocationCaption` (String; optional)


Der Prompt-Renderer behandelt `LocationName`, `LocationAddress` und `LocationCaption` als nicht vertrauenswürdige Metadaten und serialisiert sie über denselben begrenzten JSON-Pfad, der auch für anderen Kanal-Kontext verwendet wird.

## Kanalhinweise

  * **Telegram** : Orte werden `LocationName/LocationAddress` zugeordnet; Live-Standorte verwenden `live_period`.
  * **WhatsApp** : `locationMessage.comment` und `liveLocationMessage.caption` füllen `LocationCaption`.
  * **Matrix** : `geo_uri` wird als Pin-Standort geparst; die Höhe wird ignoriert und `LocationIsLive` ist immer false.


## Verwandt

  * [Standortbefehl (Nodes)](</de/nodes/location-command>)
  * [Kameraaufnahme](</de/nodes/camera>)
  * [Medienverständnis](</de/nodes/media-understanding>)


Was this useful?YesNo