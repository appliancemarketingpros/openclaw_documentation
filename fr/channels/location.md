---
title: Analyse de l’emplacement des canaux
source_url: https://docs.openclaw.ai/fr/channels/location
scraped_at: 2026-05-25
---

OpenClaw normalise les emplacements partagés provenant des canaux de discussion en :

  * un texte de coordonnées concis ajouté au corps entrant, et
  * des champs structurés dans la charge utile de contexte de réponse automatique. Les libellés, adresses et légendes/commentaires fournis par le canal sont rendus dans le prompt via le bloc JSON partagé de métadonnées non fiables, et non inline dans le corps utilisateur.


Actuellement pris en charge :

  * **Telegram** (épingles de position + lieux + positions en direct)
  * **WhatsApp** (`locationMessage` \+ `liveLocationMessage`)
  * **Matrix** (`m.location` avec `geo_uri`)


## Formatage du texte

Les emplacements sont rendus sous forme de lignes lisibles sans crochets :

  * Épingle : 
    * `📍 48.858844, 2.294351 ±12m`
  * Lieu nommé : 
    * `📍 48.858844, 2.294351 ±12m`
  * Partage en direct : 
    * `🛰 Position en direct : 48.858844, 2.294351 ±12m`


Si le canal inclut un libellé, une adresse ou une légende/commentaire, cet élément est conservé dans la charge utile de contexte et apparaît dans le prompt sous forme de JSON non fiable délimité :

textCopy code
[code]
    Emplacement (métadonnées non fiables) :```json{  "latitude": 48.858844,  "longitude": 2.294351,  "name": "Tour Eiffel",  "address": "Champ de Mars, Paris",  "caption": "Retrouvons-nous ici"}```
[/code]

## Champs de contexte

Lorsqu’un emplacement est présent, ces champs sont ajoutés à `ctx` :

  * `LocationLat` (nombre)
  * `LocationLon` (nombre)
  * `LocationAccuracy` (nombre, mètres ; facultatif)
  * `LocationName` (chaîne ; facultatif)
  * `LocationAddress` (chaîne ; facultatif)
  * `LocationSource` (`pin | place | live`)
  * `LocationIsLive` (booléen)
  * `LocationCaption` (chaîne ; facultatif)


Le moteur de rendu du prompt traite `LocationName`, `LocationAddress` et `LocationCaption` comme des métadonnées non fiables et les sérialise via le même chemin JSON borné utilisé pour les autres contextes de canal.

## Remarques sur les canaux

  * **Telegram** : les lieux sont mappés vers `LocationName/LocationAddress` ; les positions en direct utilisent `live_period`.
  * **WhatsApp** : `locationMessage.comment` et `liveLocationMessage.caption` remplissent `LocationCaption`.
  * **Matrix** : `geo_uri` est analysé comme une position épinglée ; l’altitude est ignorée et `LocationIsLive` est toujours faux.


## Lié

  * [Commande de localisation (nodes)](</fr/nodes/location-command>)
  * [Capture caméra](</fr/nodes/camera>)
  * [Compréhension des médias](</fr/nodes/media-understanding>)


Was this useful?YesNo