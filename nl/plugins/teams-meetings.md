---
title: Microsoft Teams-vergaderingenplugin
source_url: https://docs.openclaw.ai/nl/plugins/teams-meetings
scraped_at: 2026-10-12
---

CapabilitiesPlugin guides

De `teams-meetings`-plugin neemt als gast deel via Microsoft Teams-links in het OpenClaw Chrome-profiel. De plugin accepteert werklinks onder `teams.microsoft.com/l/meetup-join/...` en consumentenlinks onder `teams.live.com/meet/...`. De plugin maakt geen vergaderingen aan, belt niet in, roept Microsoft Graph niet aan en legt geen audio- of video-opnamen vast.

## Installatie

Terugspreken gebruikt dezelfde lokale audiovereisten als de [Google Meet-plugin](</nl/plugins/google-meet>): macOS, het virtuele audioapparaat `BlackHole 2ch` en SoX.

bashCopy code
[code]
    brew install blackhole-2ch soxsudo rebootsystem_profiler SPAudioDataType | grep -i BlackHolecommand -v sox
[/code]

De plugin is standaard inbegrepen en ingeschakeld. Voeg alleen een vermelding toe om de plugin aan te passen en controleer daarna de installatie:

json5Copy code
[code]
    {  plugins: {    entries: {      "teams-meetings": {        config: {          defaultMode: "agent",          chrome: { guestName: "OpenClaw Agent" },        },      },    },  },}
[/code]

Voer `openclaw plugins disable teams-meetings` uit als je de plugin niet actief wilt hebben.

bashCopy code
[code]
    openclaw teamsmeetings setupopenclaw teamsmeetings join 'https://teams.microsoft.com/l/meetup-join/...'
[/code]

Gebruik `chromeNode.node` om Chrome, BlackHole en SoX op een gekoppelde macOS-node uit te voeren. De node moet `teamsmeetings.chrome` en `browser.proxy` toestaan.

## Modi

Modus | Gedrag  
---|---  
`agent` | Realtime transcriptie raadpleegt de geconfigureerde OpenClaw-agent; TTS antwoordt.  
`bidi` | Een realtime spraakmodel luistert en antwoordt rechtstreeks.  
`transcribe` | Alleen observerend deelnemen met momentopnamen van het live-ondertitelingstranscript.  
  
Liveondertiteling van Teams wordt na toelating in elke modus ingeschakeld, zodat OpenClaw notities met sprekerstoewijzing kan bewaren. De actie `transcript` retourneert nog steeds alleen de begrensde livebuffer voor `transcribe`-sessies. Bij het verlaten slaat OpenClaw het duurzame transcript en de afgeleide samenvatting op in de gedeelde statusdatabase; geef ze weer of exporteer ze met [`openclaw transcripts`](</nl/cli/transcripts>).

Automatische notities zijn standaard ingeschakeld. Stel `transcripts.enabled: false` in om duurzame notities globaal uit te schakelen; de expliciete modus `transcribe` stelt nog steeds alleen het begrensde live-uiteinde beschikbaar.

## Beperkingen voor deelname als gast

De browseradapter sluit het tussenscherm van de app, vult de gastnaam in, schakelt de camera uit, configureert de microfoon voor de geselecteerde modus en klikt op de knop om deel te nemen. Tijdens een gesprek wordt het besturingselement voor ophangen gebruikt; statussen voor de lobby, aanmelding bij de tenant en apparaatmachtigingen retourneren expliciete redenen voor handmatige actie. Omleidingen van de consumentenlauncher voor vergaderingen en de door Chrome weergegeven `BlackHole 2ch (Virtual)`-labels worden ondersteund.

Teams-tenantbeleid kan aanmelding, e-mailverificatie of toelating door de organisator vereisen. Voltooi die stap in het OpenClaw Chrome-profiel en probeer daarna opnieuw de status op te vragen of spraak te gebruiken. De plugin omzeilt het tenantbeleid niet.

De Teams-webclient voor consumenten is live gevalideerd voor het tussenscherm van de app, invoer van de gastnaam, microfoon-/cameraschakelaars vóór deelname, deelname, toelating vanuit de lobby, mediamachtigingen, detectie van een actief gesprek, liveondertiteling, routering van BlackHole-invoer/-uitvoer, verlaten en detectie na het gesprek. Werktenants kunnen ander beleid opleggen voor aanmelding, e-mailverificatie, toelating en bevestiging bij het verlaten; voltooi elke gemelde handmatige actie in het OpenClaw Chrome-profiel.

## Tool- en Gateway-oppervlak

De agenttool `teams_meetings` ondersteunt `join`, `leave`, `status`, `transcript` en `speak`. Gateway-methoden gebruiken het voorvoegsel `teamsmeetings.*`. De nodeopdracht is `teamsmeetings.chrome`.

## Gerelateerd

  * [Overzicht van vergaderplugins](</nl/plugins/meeting-plugins>)
  * [Microsoft Teams-kanaal](</nl/channels/msteams>)


Was this useful?YesNo

Open issue