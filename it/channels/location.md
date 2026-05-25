---
title: Analisi della posizione del canale
source_url: https://docs.openclaw.ai/it/channels/location
scraped_at: 2026-05-25
---

OpenClaw normalizza le posizioni condivise dai canali di chat in:

  * testo conciso con coordinate aggiunto al corpo in ingresso, e
  * campi strutturati nel payload di contesto della risposta automatica. Le etichette, gli indirizzi e le didascalie/commenti forniti dal canale vengono resi nel prompt tramite il blocco JSON condiviso di metadati non attendibili, non inline nel corpo dell'utente.


Attualmente supportato:

  * **Telegram** (pin di posizione + luoghi + posizioni in tempo reale)
  * **WhatsApp** (`locationMessage` \+ `liveLocationMessage`)
  * **Matrix** (`m.location` con `geo_uri`)


## Formattazione del testo

Le posizioni vengono visualizzate come righe leggibili senza parentesi:

  * Pin: 
    * `📍 48.858844, 2.294351 ±12m`
  * Luogo con nome: 
    * `📍 48.858844, 2.294351 ±12m`
  * Condivisione in tempo reale: 
    * `🛰 Posizione in tempo reale: 48.858844, 2.294351 ±12m`


Se il canale include un'etichetta, un indirizzo o una didascalia/commento, questi vengono mantenuti nel payload di contesto e compaiono nel prompt come JSON non attendibile delimitato:

textCopy code
[code]
    Posizione (metadati non attendibili):```json{  "latitude": 48.858844,  "longitude": 2.294351,  "name": "Torre Eiffel",  "address": "Champ de Mars, Parigi",  "caption": "Incontriamoci qui"}```
[/code]

## Campi di contesto

Quando è presente una posizione, questi campi vengono aggiunti a `ctx`:

  * `LocationLat` (number)
  * `LocationLon` (number)
  * `LocationAccuracy` (number, metri; facoltativo)
  * `LocationName` (string; facoltativo)
  * `LocationAddress` (string; facoltativo)
  * `LocationSource` (`pin | place | live`)
  * `LocationIsLive` (boolean)
  * `LocationCaption` (string; facoltativo)


Il renderer del prompt tratta `LocationName`, `LocationAddress` e `LocationCaption` come metadati non attendibili e li serializza tramite lo stesso percorso JSON delimitato usato per gli altri contesti di canale.

## Note sui canali

  * **Telegram** : i luoghi vengono mappati a `LocationName/LocationAddress`; le posizioni in tempo reale usano `live_period`.
  * **WhatsApp** : `locationMessage.comment` e `liveLocationMessage.caption` popolano `LocationCaption`.
  * **Matrix** : `geo_uri` viene analizzato come posizione pin; l'altitudine viene ignorata e `LocationIsLive` è sempre false.


## Correlati

  * [Comando di posizione (Node)](</it/nodes/location-command>)
  * [Acquisizione fotocamera](</it/nodes/camera>)
  * [Comprensione dei media](</it/nodes/media-understanding>)


Was this useful?YesNo