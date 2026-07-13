---
title: Widget weergeven
source_url: https://docs.openclaw.ai/nl/tools/show-widget
scraped_at: 2026-07-13
---

CapabilitiesTools

`show_widget` rendert een zelfstandig SVG- of HTML-fragment inline in het chattranscript van de Control UI. De gebundelde Canvas-plugin beheert de tool en host elk resultaat als een Canvas-document met dezelfde origin.

De tool is alleen beschikbaar wanneer de oorspronkelijke Gateway-client de mogelijkheid `inline-widgets` declareert. De Control UI declareert deze mogelijkheid automatisch. Kanaaluitvoeringen zoals Telegram en WhatsApp krijgen geen toegang tot `show_widget`.

Het transport van mogelijkheden omvat ingebedde modelbackends, modelbackends met een Codex-appserver en modelbackends die door de CLI worden aangestuurd. Met een toekenning geauthenticeerde MCP-aanroepers en directe HTTP-aanroepers voor tooluitvoering blijven standaard geblokkeerd, omdat ze geen clientmogelijkheden declareren.

## De tool gebruiken

De agent levert twee verplichte tekenreeksen:

Korte titel die bij de inlinevoorvertoning en als titel van het gehoste document wordt weergegeven.

Zelfstandig SVG- of HTML-fragment. Invoer die na het verwijderen van witruimte met `<svg` begint, wordt in SVG-modus gerenderd; alle andere invoer wordt als een HTML-fragment behandeld. Maximale lengte: 262.144 tekens.

Het toolresultaat bevat een Canvas-voorvertoningsreferentie, zodat webchat de widget rechtstreeks vanuit de toolaanroep rendert en deze na het opnieuw laden van de geschiedenis herstelt. Transcripties die geen voorvertoningen renderen, tonen nog steeds het gehoste Canvas-pad.

## Beveiliging en opslag

Widgetdocumenten gebruiken een restrictief Content Security Policy-beleid: inline stijlen en scripts zijn toegestaan, afbeeldingen mogen `data:`-URL's gebruiken en externe ophaalacties en het laden van bronnen worden geblokkeerd. Bewaar alle opmaak, stijlen, scripts en afbeeldingsgegevens in `widget_code`.

Het iframe laat `allow-same-origin` altijd weg, zelfs wanneer de globale insluitmodus van de Control UI `trusted` is, zodat widgetscripts de origin van de bovenliggende toepassing niet kunnen lezen. De Canvas-host levert widgetdocumenten ook met de antwoordheader `Content-Security-Policy: sandbox allow-scripts`, zodat de widget bij het rechtstreeks openen van de gehoste URL nog steeds in een ondoorzichtige origin wordt uitgevoerd in plaats van in de origin van de Control UI. Browsersandboxing voorkomt niet dat een script zijn eigen iframe naar een andere locatie navigeert; render alleen widgetcode die u bereid bent in dat geïsoleerde frame uit te voeren.

Het iframe volgt ook [`gateway.controlUi.embedSandbox`](</nl/web/control-ui#hosted-embeds>). Het standaardniveau `scripts` ondersteunt interactieve widgets en behoudt tegelijkertijd de originisolatie.

Canvas bewaart maximaal 32 widgets per sessie (of per agent wanneer er geen sessie beschikbaar is). Wanneer een andere widget wordt gemaakt, wordt het oudste document binnen dat bereik verwijderd.

## Gerelateerd

  * [Gehoste insluitingen van de Control UI](</nl/web/control-ui#hosted-embeds>)
  * [Canvas-plugin](</nl/plugins/reference/canvas>)
  * [Clientmogelijkheden van het Gateway-protocol](</nl/gateway/protocol#client-capabilities>)


Was this useful?YesNo

Open issue