---
title: Plugin voor Zoom-vergaderingen
source_url: https://docs.openclaw.ai/nl/plugins/zoom-meetings
scraped_at: 2026-10-12
---

CapabilitiesPlugin guides

De plugin `zoom-meetings` neemt als gast deel via Zoom-vergaderlinks met de Zoom Web App in het OpenClaw Chrome-profiel. De plugin accepteert vergaderlinks onder `zoom.us/j/...` en accountsubdomeinen zoals `example.zoom.us/j/...`. De plugin maakt geen vergaderingen aan, belt niet in, gebruikt de Zoom Meeting SDK niet en legt geen audio- of video-opnamen vast.

## Installatie

Terugspreken gebruikt dezelfde lokale audiovereisten als de [Google Meet-plugin](</nl/plugins/google-meet>): macOS, het virtuele audioapparaat `BlackHole 2ch` en SoX.

bashCopy code
[code]
    brew install blackhole-2ch soxsudo rebootsystem_profiler SPAudioDataType | grep -i BlackHolecommand -v sox
[/code]

De plugin is inbegrepen en standaard ingeschakeld. Voeg alleen een vermelding toe om de plugin aan te passen en controleer daarna de installatie:

json5Copy code
[code]
    {  plugins: {    entries: {      "zoom-meetings": {        config: {          defaultMode: "agent",          chrome: { guestName: "OpenClaw Agent" },        },      },    },  },}
[/code]

Voer `openclaw plugins disable zoom-meetings` uit als je de plugin niet actief wilt hebben.

bashCopy code
[code]
    openclaw zoommeetings setupopenclaw zoommeetings join 'https://zoom.us/j/1234567890'
[/code]

Gebruik `chromeNode.node` om Chrome, BlackHole en SoX op een gekoppelde macOS-Node uit te voeren. De Node moet `zoommeetings.chrome` en `browser.proxy` toestaan.

## Modi

Modus | Gedrag  
---|---  
`agent` | Realtime transcriptie raadpleegt de geconfigureerde OpenClaw-agent; TTS antwoordt.  
`bidi` | Een realtime spraakmodel luistert en antwoordt rechtstreeks.  
`transcribe` | Alleen observeren met momentopnamen van het live-ondertitelingstranscript.  
  
Live-ondertiteling van Zoom wordt na toelating in elke modus ingeschakeld, zodat OpenClaw vergadernotities kan bewaren. De actie `transcript` retourneert nog steeds alleen de begrensde livebuffer voor `transcribe`-sessies. Bij het verlaten slaat OpenClaw het duurzame transcript en de afgeleide samenvatting op in de gedeelde statusdatabase; bekijk of exporteer deze met [`openclaw transcripts`](</nl/cli/transcripts>).

Automatische notities zijn standaard ingeschakeld. Stel `transcripts.enabled: false` in om duurzame notities globaal uit te schakelen; de expliciete modus `transcribe` stelt nog steeds alleen het begrensde live-einde beschikbaar.

## Beperkingen voor deelname als gast

De browseradapter kiest **Join from browser** , vult de gastnaam in, schakelt de camera uit, configureert de microfoon voor de geselecteerde modus en klikt op **Join**. Zoom Web App wordt uitgevoerd onder `app.zoom.us`; de plugin verleent die oorsprong vóór de navigatie machtigingen voor de microfoon en luidsprekerselectie. De status tijdens het gesprek gebruikt de Leave-bediening van Zoom. Wachtruimte-, aanmeldings-, toegangscode-, CAPTCHA- en apparaatmachtigingsstatussen retourneren expliciete redenen waarom handmatige actie nodig is.

Het beleid van de Zoom-host en het account kan deelname via de browser uitschakelen, authenticatie of e-mailverificatie vereisen, een CAPTCHA tonen of toelating door de host vereisen. Voltooi die stap in het OpenClaw Chrome-profiel en probeer daarna de status of spraak opnieuw. De plugin omzeilt het Zoom-beleid niet.

De Zoom Web App is live gevalideerd met een officiële Zoom-testvergadering voor het tussenscherm van de app, het invoeren van de gastnaam in een iframe, microfoon- en camerabediening vóór deelname, deelname, mediarechten van de browser en macOS, detectie tijdens het gesprek, inschakeling van live-ondertiteling en detectie van beëindiging door de host. Wachtruimte- en authenticatiestatussen zijn afhankelijk van het hostbeleid en behouden tekstuele terugvalopties wanneer geen stabiele DOM-id beschikbaar is.

## Tool- en Gateway-oppervlak

De agenttool `zoom_meetings` ondersteunt `join`, `leave`, `status`, `transcript` en `speak`. Gateway-methoden gebruiken het voorvoegsel `zoommeetings.*`. De Node-opdracht is `zoommeetings.chrome`.

## Gerelateerd

  * [Overzicht van vergaderplugins](</nl/plugins/meeting-plugins>)


Was this useful?YesNo

Open issue