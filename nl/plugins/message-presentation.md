---
title: Berichtweergave
source_url: https://docs.openclaw.ai/nl/plugins/message-presentation
scraped_at: 2026-05-25
---

Berichtpresentatie is OpenClaw's gedeelde contract voor rijke uitgaande chat-UI. Hiermee kunnen agents, CLI-opdrachten, goedkeuringsstromen en plugins de berichtintentie eenmaal beschrijven, terwijl elke kanaalplugin de best mogelijke native vorm rendert.

Gebruik presentatie voor draagbare bericht-UI:

  * tekstsecties
  * korte context-/voettekst
  * scheidingslijnen
  * knoppen
  * selectiemenu's
  * kaarttitel en toon


Voeg geen nieuwe provider-native velden zoals Discord `components`, Slack `blocks`, Telegram `buttons`, Teams `card` of Feishu `card` toe aan de gedeelde berichttool. Dat zijn rendereruitvoer die eigendom is van de kanaalplugin.

## Contract

Plugin-auteurs importeren het publieke contract uit:

tsCopy code
[code]
       MessagePresentation,  ReplyPayloadDelivery,} from "openclaw/plugin-sdk/interactive-runtime";
[/code]

Vorm:

tsCopy code
[code]
    type MessagePresentation = {  title?: string;  tone?: "neutral" | "info" | "success" | "warning" | "danger";  blocks: MessagePresentationBlock[];}; type MessagePresentationBlock =  | { type: "text"; text: string }  | { type: "context"; text: string }  | { type: "divider" }  | { type: "buttons"; buttons: MessagePresentationButton[] }  | { type: "select"; placeholder?: string; options: MessagePresentationOption[] }; type MessagePresentationButton = {  label: string;  value?: string;  url?: string;  style?: "primary" | "secondary" | "success" | "danger";}; type MessagePresentationOption = {  label: string;  value: string;}; type ReplyPayloadDelivery = {  pin?:    | boolean    | {        enabled: boolean;        notify?: boolean;        required?: boolean;      };};
[/code]

Knopsemantiek:

  * `value` is een toepassingsactiewaarde die wordt teruggerouteerd via het bestaande interactiepad van het kanaal wanneer het kanaal klikbare bedieningselementen ondersteunt.
  * `url` is een linkknop. Deze kan bestaan zonder `value`.
  * `label` is verplicht en wordt ook gebruikt in de tekstfallback.
  * `style` is adviserend. Renderers moeten niet-ondersteunde stijlen mappen naar een veilige standaard, en de verzending niet laten mislukken.


Selectiesemantiek:

  * `options[].value` is de geselecteerde toepassingswaarde.
  * `placeholder` is adviserend en kan worden genegeerd door kanalen zonder native selectieondersteuning.
  * Als een kanaal geen selecties ondersteunt, toont fallbacktekst de labels als lijst.


## Producer-voorbeelden

Eenvoudige kaart:

jsonCopy code
[code]
    {  "title": "Deploy approval",  "tone": "warning",  "blocks": [    { "type": "text", "text": "Canary is ready to promote." },    { "type": "context", "text": "Build 1234, staging passed." },    {      "type": "buttons",      "buttons": [        { "label": "Approve", "value": "deploy:approve", "style": "success" },        { "label": "Decline", "value": "deploy:decline", "style": "danger" }      ]    }  ]}
[/code]

Alleen-URL-linkknop:

jsonCopy code
[code]
    {  "blocks": [    { "type": "text", "text": "Release notes are ready." },    {      "type": "buttons",      "buttons": [{ "label": "Open notes", "url": "https://example.com/release" }]    }  ]}
[/code]

Selectiemenu:

jsonCopy code
[code]
    {  "title": "Choose environment",  "blocks": [    {      "type": "select",      "placeholder": "Environment",      "options": [        { "label": "Canary", "value": "env:canary" },        { "label": "Production", "value": "env:prod" }      ]    }  ]}
[/code]

CLI-verzending:

bashCopy code
[code]
    openclaw message send --channel slack \  --target channel:C123 \  --message "Deploy approval" \  --presentation '{"title":"Deploy approval","tone":"warning","blocks":[{"type":"text","text":"Canary is ready."},{"type":"buttons","buttons":[{"label":"Approve","value":"deploy:approve","style":"success"},{"label":"Decline","value":"deploy:decline","style":"danger"}]}]}'
[/code]

Vastgezette levering:

bashCopy code
[code]
    openclaw message send --channel telegram \  --target -1001234567890 \  --message "Topic opened" \  --pin
[/code]

Vastgezette levering met expliciete JSON:

jsonCopy code
[code]
    {  "pin": {    "enabled": true,    "notify": true,    "required": false  }}
[/code]

## Renderercontract

Kanaalplugins declareren renderondersteuning op hun uitgaande adapter:

tsCopy code
[code]
    const adapter: ChannelOutboundAdapter = {  deliveryMode: "direct",  presentationCapabilities: {    supported: true,    buttons: true,    selects: true,    context: true,    divider: true,  },  deliveryCapabilities: {    pin: true,  },  renderPresentation({ payload, presentation, ctx }) {    return renderNativePayload(payload, presentation, ctx);  },  async pinDeliveredMessage({ target, messageId, pin }) {    await pinNativeMessage(target, messageId, { notify: pin.notify === true });  },};
[/code]

Capability-velden zijn bewust eenvoudige booleans. Ze beschrijven wat de renderer interactief kan maken, niet elke native platformlimiet. Renderers blijven eigenaar van platformspecifieke limieten zoals het maximumaantal knoppen, het aantal blokken en de kaartgrootte.

## Kernrenderstroom

Wanneer een `ReplyPayload` of berichtactie `presentation` bevat, doet de kern het volgende:

  1. Normaliseert de presentatiepayload.
  2. Lost de uitgaande adapter van het doelkanaal op.
  3. Leest `presentationCapabilities`.
  4. Roept `renderPresentation` aan wanneer de adapter de payload kan renderen.
  5. Valt terug op conservatieve tekst wanneer de adapter ontbreekt of niet kan renderen.
  6. Verzendt de resulterende payload via het normale kanaalleveringspad.
  7. Past leveringsmetadata zoals `delivery.pin` toe na het eerste succesvol verzonden bericht.


De kern is eigenaar van fallbackgedrag zodat producers kanaalagnostisch kunnen blijven. Kanaalplugins zijn eigenaar van native rendering en interactieafhandeling.

## Degradatieregels

Presentatie moet veilig te verzenden zijn op beperkte kanalen.

Fallbacktekst bevat:

  * `title` als de eerste regel
  * `text`-blokken als normale alinea's
  * `context`-blokken als compacte contextregels
  * `divider`-blokken als visuele scheiding
  * knoplabels, inclusief URL's voor linkknoppen
  * labels van selectieopties


Niet-ondersteunde native bedieningselementen moeten degraderen in plaats van de hele verzending te laten mislukken. Voorbeelden:

  * Telegram met inline knoppen uitgeschakeld verzendt tekstfallback.
  * Een kanaal zonder selectieondersteuning toont selectieopties als tekst.
  * Een alleen-URL-knop wordt een native linkknop of een fallback-URL-regel.
  * Optionele pinfouten laten het geleverde bericht niet mislukken.


De belangrijkste uitzondering is `delivery.pin.required: true`; als vastzetten als verplicht is aangevraagd en het kanaal het verzonden bericht niet kan vastzetten, rapporteert levering een fout.

## Providermapping

Huidige gebundelde renderers:

Kanaal | Native renderdoel | Opmerkingen  
---|---|---  
Discord | Componenten en componentcontainers | Behoudt legacy `channelData.discord.components` voor bestaande provider-native payload-producers, maar nieuwe gedeelde verzendingen moeten `presentation` gebruiken.  
Slack | Block Kit | Behoudt legacy `channelData.slack.blocks` voor bestaande provider-native payload-producers, maar nieuwe gedeelde verzendingen moeten `presentation` gebruiken.  
Telegram | Tekst plus inline toetsenborden | Knoppen/selecties vereisen inline-knopcapaciteit voor het doeloppervlak; anders wordt tekstfallback gebruikt.  
Mattermost | Tekst plus interactieve props | Andere blokken degraderen naar tekst.  
Microsoft Teams | Adaptive Cards | Platte `message`-tekst wordt bij de kaart opgenomen wanneer beide worden opgegeven.  
Feishu | Interactieve kaarten | Kaartkop kan `title` gebruiken; body voorkomt duplicatie van die titel.  
Platte kanalen | Tekstfallback | Kanalen zonder renderer krijgen nog steeds leesbare uitvoer.  
  
Compatibiliteit met provider-native payloads is een overgangsvoorziening voor bestaande antwoordproducers. Het is geen reden om nieuwe gedeelde native velden toe te voegen.

## Presentation versus InteractiveReply

`InteractiveReply` is de oudere interne subset die wordt gebruikt door goedkeurings- en interactiehelpers. Deze ondersteunt:

  * tekst
  * knoppen
  * selecties


`MessagePresentation` is het canonieke gedeelde verzendcontract. Het voegt toe:

  * titel
  * toon
  * context
  * scheidingslijn
  * alleen-URL-knoppen
  * generieke leveringsmetadata via `ReplyPayload.delivery`


Gebruik helpers uit `openclaw/plugin-sdk/interactive-runtime` bij het overbruggen van oudere code:

tsCopy code
[code]
       interactiveReplyToPresentation,  normalizeMessagePresentation,  presentationToInteractiveControlsReply,  presentationToInteractiveReply,  renderMessagePresentationFallbackText,} from "openclaw/plugin-sdk/interactive-runtime";
[/code]

Nieuwe code moet `MessagePresentation` rechtstreeks accepteren of produceren.

`presentationToInteractiveReply(...)` behoudt zichtbare presentatietekst door de titel, tekst, context, knoppen en selecties naar de oudere `InteractiveReply`-vorm te mappen. Componentrenderers die titel, tekst, context en scheidingsblokken al native tekenen, moeten in plaats daarvan `presentationToInteractiveControlsReply(...)` gebruiken en daarna alleen de knop- en selectiebedieningselementen toevoegen.

`renderMessagePresentationFallbackText(...)` retourneert een lege tekenreeks voor presentatieblokken die geen tekstfallback hebben, zoals een presentatie met alleen een scheidingslijn. Transports die een niet-lege verzendbody vereisen, kunnen `emptyFallback` doorgeven om voor een minimale body te kiezen zonder het standaard fallbackcontract te wijzigen.

## Leveringspin

Vastzetten is leveringsgedrag, geen presentatie. Gebruik `delivery.pin` in plaats van provider-native velden zoals `channelData.telegram.pin`.

Semantiek:

  * `pin: true` zet het eerste succesvol geleverde bericht vast.
  * `pin.notify` staat standaard op `false`.
  * `pin.required` staat standaard op `false`.
  * Optionele pinfouten degraderen en laten het verzonden bericht intact.
  * Vereiste pinfouten laten levering mislukken.
  * Opgesplitste berichten zetten het eerste geleverde deel vast, niet het laatste deel.


Handmatige `pin`-, `unpin`\- en `pins`-berichtacties bestaan nog steeds voor bestaande berichten waarbij de provider die bewerkingen ondersteunt.

## Checklist voor Plugin-auteurs

  * Declareer `presentation` vanuit `describeMessageTool(...)` wanneer het kanaal semantische presentatie kan renderen of veilig kan degraderen.
  * Voeg `presentationCapabilities` toe aan de uitgaande runtimeadapter.
  * Implementeer `renderPresentation` in runtimecode, niet in control-plane Plugin- setupcode.
  * Houd native UI-bibliotheken uit hete setup-/cataloguspaden.
  * Behoud platformlimieten in de renderer en tests.
  * Voeg fallbacktests toe voor niet-ondersteunde knoppen, selecties, URL-knoppen, duplicatie van titel/tekst en gemengde verzendingen met `message` plus `presentation`.
  * Voeg leveringspinondersteuning toe via `deliveryCapabilities.pin` en `pinDeliveredMessage` alleen wanneer de provider de verzonden bericht-id kan vastzetten.
  * Stel geen nieuwe provider-native kaart-/blok-/component-/knopvelden beschikbaar via het gedeelde berichtactieschema.


## Gerelateerde docs

  * [Bericht-CLI](</nl/cli/message>)
  * [Overzicht van Plugin SDK](</nl/plugins/sdk-overview>)
  * [Pluginarchitectuur](</nl/plugins/architecture-internals#message-tool-schemas>)
  * [Refactorplan voor kanaalpresentatie](</nl/plan/ui-channels>)


Was this useful?YesNo