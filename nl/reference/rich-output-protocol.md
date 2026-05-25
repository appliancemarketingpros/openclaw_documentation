---
title: Protocol voor rijke uitvoer
source_url: https://docs.openclaw.ai/nl/reference/rich-output-protocol
scraped_at: 2026-05-25
---

Assistant-uitvoer kan een kleine set leverings-/renderdirectieven bevatten:

  * `MEDIA:` voor levering van bijlagen
  * `[[audio_as_voice]]` voor audiopresentatiehints
  * `[[reply_to_current]]` / `[[reply_to:<id>]]` voor antwoordmetadata
  * `[embed ...]` voor rijke rendering in de Control UI


Externe `MEDIA:`-bijlagen moeten openbare `https:`-URL's zijn. Platte `http:`, loopback, link-local, privé- en interne hostnamen worden genegeerd als bijlage- directieven; server-side media-fetchers handhaven nog steeds hun eigen netwerkbeveiligingen.

Lokale `MEDIA:`-bijlagen kunnen absolute paden, workspace-relatieve paden of home-relatieve `~/`-paden gebruiken. Ze gaan nog steeds door het beleid voor bestandslezen van de agent en controles op mediatypen voordat ze worden geleverd.

Gewone Markdown-afbeeldingssyntaxis blijft standaard tekst. Kanalen die bewust Markdown-afbeeldingsantwoorden naar mediabijlagen omzetten, schakelen dit in in hun uitgaande adapter; Telegram doet dit zodat `![alt](url)` nog steeds een media-antwoord kan worden.

Deze directieven staan los van elkaar. `MEDIA:` en antwoord-/spraak-tags blijven leveringsmetadata; `[embed ...]` is het web-only pad voor rijke rendering. Vertrouwde tool-resultaatmedia gebruiken dezelfde `MEDIA:` / `[[audio_as_voice]]`-parser vóór levering, zodat tekstuitvoer van tools nog steeds een audiobijlage als spraakbericht kan markeren.

Wanneer block streaming is ingeschakeld, blijft `MEDIA:` metadata voor eenmalige levering voor een turn. Als dezelfde media-URL in een gestreamd blok wordt verzonden en herhaald in de uiteindelijke assistant-payload, levert OpenClaw de bijlage één keer en verwijdert het duplicaat uit de uiteindelijke payload.

## `[embed ...]`

`[embed ...]` is de enige agent-gerichte syntaxis voor rijke rendering voor de Control UI.

Zelfsluitend voorbeeld:

textCopy code
[code]
    [embed ref="cv_123" title="Status" /]
[/code]

Regels:

  * `[view ...]` is niet langer geldig voor nieuwe uitvoer.
  * Embed-shortcodes renderen alleen in het berichtoppervlak van de assistant.
  * Alleen embeds met een URL-backend worden gerenderd. Gebruik `ref="..."` of `url="..."`.
  * Inline HTML-embed-shortcodes in blokvorm worden niet gerenderd.
  * De web-UI verwijdert de shortcode uit zichtbare tekst en rendert de embed inline.
  * `MEDIA:` is geen embed-alias en mag niet worden gebruikt voor rijke embed-rendering.


## Opgeslagen renderingsvorm

Het genormaliseerde/opgeslagen inhoudsblok van de assistant is een gestructureerd `canvas`-item:

jsonCopy code
[code]
    {  "type": "canvas",  "preview": {    "kind": "canvas",    "surface": "assistant_message",    "render": "url",    "viewId": "cv_123",    "url": "/__openclaw__/canvas/documents/cv_123/index.html",    "title": "Status",    "preferredHeight": 320  }}
[/code]

Opgeslagen/gerenderde rijke blokken gebruiken deze `canvas`-vorm direct. `present_view` wordt niet herkend.

## Gerelateerd

  * [RPC-adapters](</nl/reference/rpc>)
  * [Typebox](</nl/concepts/typebox>)


Was this useful?YesNo