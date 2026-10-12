---
title: Scherm
source_url: https://docs.openclaw.ai/nl/tools/screen
scraped_at: 2026-10-12
---

CapabilitiesTools

Met de tool `screen` kan een agent de browsergebaseerde Control UI indelen. Het is een getypeerd oppervlak voor indeling en navigatie, niet voor het vastleggen van schermafbeeldingen of browserautomatisering.

De tool is alleen beschikbaar wanneer de oorspronkelijke client de mogelijkheid `ui-commands` aankondigt. Er moet nog ten minste één geschikte Control UI verbonden zijn wanneer de tool wordt uitgevoerd; anders retourneert de Gateway `UNAVAILABLE`.

## Acties

Actie | Effect | Optionele invoer  
---|---|---  
`split_right` | Splits het doelvenster van de sessie naar rechts | `sessionKey` (standaard de huidige sessie)  
`split_down` | Splits het doelvenster van de sessie naar beneden | `sessionKey` (standaard de huidige sessie)  
`close_pane` | Sluit het doelvenster van de sessie | `sessionKey` (standaard de huidige sessie)  
`focus` | Stel het doelvenster van de sessie scherp | `sessionKey` (standaard de huidige sessie)  
`navigate` | Open de doelsessie | `sessionKey` (standaard de huidige sessie)  
`sidebar_show` / `sidebar_hide` | Toon of verberg de hoofdzijbalk | -  
`terminal_show` / `terminal_hide` | Toon of verberg het terminalpaneel voor de operator | `dock` (`bottom` of `right`) bij het tonen  
`browser_show` / `browser_hide` | Toon of verberg het browserpaneel | `dock` (`bottom` of `right`) bij het tonen  
  
Een geslaagde opdracht retourneert `{ "ok": true }` nadat de Gateway de getypeerde gebeurtenis `ui.command` heeft uitgezonden.

## Routering en beveiliging

Protocol v1 stuurt de opdracht opzettelijk naar elke verbonden Control UI die `ui-commands` aankondigt; de opdracht is niet gericht op één browsertabblad. Dit is van belang wanneer dezelfde operator meerdere dashboards heeft geopend.

De Gateway-RPC vereist `operator.write`. De tool kan alleen de presentatiestatus wijzigen: de tool kan geen pixels lezen, schermafbeeldingen maken, op willekeurige pagina-inhoud klikken of de machtigingen van de geselecteerde sessie- en operatorpanelen omzeilen.

## Gerelateerd

  * [Control UI](</web/control-ui>)
  * [Gateway-protocol](</nl/gateway/protocol#method-families>)
  * [Browsertool](</nl/tools/browser>)


Was this useful?YesNo

Open issue