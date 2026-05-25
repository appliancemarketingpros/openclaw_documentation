---
title: Camera-opname
source_url: https://docs.openclaw.ai/nl/nodes/camera
scraped_at: 2026-05-25
---

OpenClaw ondersteunt **camera-opname** voor agentworkflows:

  * **iOS-node** (gekoppeld via Gateway): maak een **foto** (`jpg`) of **korte videoclip** (`mp4`, met optionele audio) via `node.invoke`.
  * **Android-node** (gekoppeld via Gateway): maak een **foto** (`jpg`) of **korte videoclip** (`mp4`, met optionele audio) via `node.invoke`.
  * **macOS-app** (node via Gateway): maak een **foto** (`jpg`) of **korte videoclip** (`mp4`, met optionele audio) via `node.invoke`.


Alle cameratoegang wordt afgeschermd door **door de gebruiker beheerde instellingen**.

## iOS-node

### Gebruikersinstelling (standaard aan)

  * iOS-tabblad Instellingen → **Camera** → **Camera toestaan** (`camera.enabled`) 
    * Standaard: **aan** (ontbrekende sleutel wordt behandeld als ingeschakeld).
    * Wanneer uit: `camera.*`-opdrachten retourneren `CAMERA_DISABLED`.


### Opdrachten (via Gateway `node.invoke`)

  * `camera.list`

    * Antwoordpayload: 
      * `devices`: array van `{ id, name, position, deviceType }`
  * `camera.snap`

    * Parameters: 
      * `facing`: `front|back` (standaard: `front`)
      * `maxWidth`: getal (optioneel; standaard `1600` op de iOS-node)
      * `quality`: `0..1` (optioneel; standaard `0.9`)
      * `format`: momenteel `jpg`
      * `delayMs`: getal (optioneel; standaard `0`)
      * `deviceId`: string (optioneel; uit `camera.list`)
    * Antwoordpayload: 
      * `format: "jpg"`
      * `base64: "<...>"`
      * `width`, `height`
    * Payloadbeveiliging: foto's worden opnieuw gecomprimeerd om de base64-payload onder 5 MB te houden.
  * `camera.clip`

    * Parameters: 
      * `facing`: `front|back` (standaard: `front`)
      * `durationMs`: getal (standaard `3000`, begrensd op maximaal `60000`)
      * `includeAudio`: boolean (standaard `true`)
      * `format`: momenteel `mp4`
      * `deviceId`: string (optioneel; uit `camera.list`)
    * Antwoordpayload: 
      * `format: "mp4"`
      * `base64: "<...>"`
      * `durationMs`
      * `hasAudio`


### Vereiste voorgrond

Net als `canvas.*` staat de iOS-node `camera.*`-opdrachten alleen toe op de **voorgrond**. Aanroepen op de achtergrond retourneren `NODE_BACKGROUND_UNAVAILABLE`.

### CLI-helper (tijdelijke bestanden + MEDIA)

De eenvoudigste manier om bijlagen te krijgen is via de CLI-helper, die gedecodeerde media naar een tijdelijk bestand schrijft en `MEDIA:<path>` afdrukt.

Voorbeelden:

bashCopy code
[code]
    openclaw nodes camera snap --node <id>               # default: both front + back (2 MEDIA lines)openclaw nodes camera snap --node <id> --facing frontopenclaw nodes camera clip --node <id> --duration 3000openclaw nodes camera clip --node <id> --no-audio
[/code]

Opmerkingen:

  * `nodes camera snap` gebruikt standaard **beide** richtingen om de agent beide weergaven te geven.
  * Uitvoerbestanden zijn tijdelijk (in de tijdelijke map van het OS), tenzij je je eigen wrapper bouwt.


## Android-node

### Android-gebruikersinstelling (standaard aan)

  * Android-instellingenpaneel → **Camera** → **Camera toestaan** (`camera.enabled`) 
    * Standaard: **aan** (ontbrekende sleutel wordt behandeld als ingeschakeld).
    * Wanneer uit: `camera.*`-opdrachten retourneren `CAMERA_DISABLED`.


### Machtigingen

  * Android vereist runtime-machtigingen: 
    * `CAMERA` voor zowel `camera.snap` als `camera.clip`.
    * `RECORD_AUDIO` voor `camera.clip` wanneer `includeAudio=true`.


Als machtigingen ontbreken, vraagt de app er waar mogelijk om; als ze worden geweigerd, mislukken `camera.*`-aanvragen met een `*_PERMISSION_REQUIRED`-fout.

### Vereiste voorgrond op Android

Net als `canvas.*` staat de Android-node `camera.*`-opdrachten alleen toe op de **voorgrond**. Aanroepen op de achtergrond retourneren `NODE_BACKGROUND_UNAVAILABLE`.

### Android-opdrachten (via Gateway `node.invoke`)

  * `camera.list`
    * Antwoordpayload: 
      * `devices`: array van `{ id, name, position, deviceType }`


### Payloadbeveiliging

Foto's worden opnieuw gecomprimeerd om de base64-payload onder 5 MB te houden.

## macOS-app

### Gebruikersinstelling (standaard uit)

De macOS-begeleidende app toont een selectievakje:

  * **Instellingen → Algemeen → Camera toestaan** (`openclaw.cameraEnabled`) 
    * Standaard: **uit**
    * Wanneer uit: camera-aanvragen retourneren "Camera uitgeschakeld door gebruiker".


### CLI-helper (node-aanroep)

Gebruik de hoofd-CLI `openclaw` om cameraopdrachten op de macOS-node aan te roepen.

Voorbeelden:

bashCopy code
[code]
    openclaw nodes camera list --node <id>            # list camera idsopenclaw nodes camera snap --node <id>            # prints MEDIA:<path>openclaw nodes camera snap --node <id> --max-width 1280openclaw nodes camera snap --node <id> --delay-ms 2000openclaw nodes camera snap --node <id> --device-id <id>openclaw nodes camera clip --node <id> --duration 10s          # prints MEDIA:<path>openclaw nodes camera clip --node <id> --duration-ms 3000      # prints MEDIA:<path> (legacy flag)openclaw nodes camera clip --node <id> --device-id <id>openclaw nodes camera clip --node <id> --no-audio
[/code]

Opmerkingen:

  * `openclaw nodes camera snap` gebruikt standaard `maxWidth=1600`, tenzij overschreven.
  * Op macOS wacht `camera.snap` `delayMs` (standaard 2000 ms) na opwarming/belichtingsstabilisatie voordat er wordt vastgelegd.
  * Fotopayloads worden opnieuw gecomprimeerd om base64 onder 5 MB te houden.


## Veiligheid + praktische limieten

  * Camera- en microfoontoegang activeren de gebruikelijke toestemmingsprompts van het OS (en vereisen gebruiksstrings in Info.plist).
  * Videoclips zijn begrensd (momenteel `<= 60s`) om te grote node-payloads te voorkomen (base64-overhead + berichtlimieten).


## macOS-schermvideo (OS-niveau)

Gebruik voor _scherm_ -video (niet camera) de macOS-begeleidende app:

bashCopy code
[code]
    openclaw nodes screen record --node <id> --duration 10s --fps 15   # prints MEDIA:<path>
[/code]

Opmerkingen:

  * Vereist macOS-machtiging voor **Schermopname** (TCC).


## Gerelateerd

  * [Ondersteuning voor afbeeldingen en media](</nl/nodes/images>)
  * [Mediabegrip](</nl/nodes/media-understanding>)
  * [Locatieopdracht](</nl/nodes/location-command>)


Was this useful?YesNo