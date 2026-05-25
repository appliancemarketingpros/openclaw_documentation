---
title: Standaard AGENTS.md
source_url: https://docs.openclaw.ai/nl/reference/AGENTS.default
scraped_at: 2026-05-25
---

## Eerste uitvoering (aanbevolen)

OpenClaw gebruikt een speciale werkruimtemap voor de agent. Standaard: `~/.openclaw/workspace` (configureerbaar via `agents.defaults.workspace`).

  1. Maak de werkruimte aan (als die nog niet bestaat):

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace
[/code]

  2. Kopieer de standaard werkruimtesjablonen naar de werkruimte:

bashCopy code
[code]
    cp docs/reference/templates/AGENTS.md ~/.openclaw/workspace/AGENTS.mdcp docs/reference/templates/SOUL.md ~/.openclaw/workspace/SOUL.mdcp docs/reference/templates/TOOLS.md ~/.openclaw/workspace/TOOLS.md
[/code]

  3. Optioneel: als je het Skills-overzicht voor de persoonlijke assistent wilt, vervang [AGENTS.md](<http://AGENTS.md>) dan door dit bestand:

bashCopy code
[code]
    cp docs/reference/AGENTS.default.md ~/.openclaw/workspace/AGENTS.md
[/code]

  4. Optioneel: kies een andere werkruimte door `agents.defaults.workspace` in te stellen (ondersteunt `~`):

json5Copy code
[code]
    {  agents: { defaults: { workspace: "~/.openclaw/workspace" } },}
[/code]

## Veiligheidsstandaarden

  * Dump geen mappen of geheimen in chat.
  * Voer geen destructieve opdrachten uit tenzij daar expliciet om is gevraagd.
  * Verstuur geen gedeeltelijke/streaming-antwoorden naar externe berichtoppervlakken (alleen definitieve antwoorden).


## Sessiestart (vereist)

  * Lees `SOUL.md`, `USER.md` en vandaag+gisteren in `memory/`.
  * Lees `MEMORY.md` wanneer aanwezig.
  * Doe dit voordat je antwoordt.


## Soul (vereist)

  * `SOUL.md` definieert identiteit, toon en grenzen. Houd het actueel.
  * Als je `SOUL.md` wijzigt, vertel het de gebruiker.
  * Je bent elke sessie een nieuw exemplaar; continuiteit leeft in deze bestanden.


## Gedeelde ruimtes (aanbevolen)

  * Je bent niet de stem van de gebruiker; wees voorzichtig in groepschats of openbare kanalen.
  * Deel geen privegegevens, contactgegevens of interne notities.


## Geheugensysteem (aanbevolen)

  * Dagelijks logboek: `memory/YYYY-MM-DD.md` (maak `memory/` aan indien nodig).
  * Langetermijngeheugen: `MEMORY.md` voor duurzame feiten, voorkeuren en beslissingen.
  * Kleine letters `memory.md` is alleen legacy-reparatie-invoer; bewaar niet bewust beide rootbestanden.
  * Lees bij sessiestart vandaag + gisteren + `MEMORY.md` wanneer aanwezig.
  * Leg vast: beslissingen, voorkeuren, beperkingen, openstaande lussen.
  * Vermijd geheimen tenzij expliciet gevraagd.


## Tools en Skills

  * Tools staan in Skills; volg de `SKILL.md` van elke Skill wanneer je die nodig hebt.
  * Bewaar omgevingsspecifieke notities in `TOOLS.md` (Notities voor Skills).


## Back-uptip (aanbevolen)

Als je deze werkruimte behandelt als Clawds "geheugen", maak er dan een git-repo van (bij voorkeur prive) zodat `AGENTS.md` en je geheugenbestanden worden geback-upt.

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.mdgit commit -m "Add Clawd workspace"# Optional: add a private remote + push
[/code]

## Wat OpenClaw doet

  * Draait WhatsApp Gateway + Pi-coderingsagent zodat de assistent chats kan lezen/schrijven, context kan ophalen en Skills kan uitvoeren via de host-Mac.
  * De macOS-app beheert machtigingen (schermopname, meldingen, microfoon) en stelt de `openclaw` CLI beschikbaar via de meegeleverde binary.
  * Directe chats worden standaard samengevoegd in de `main`-sessie van de agent; groepen blijven geisoleerd als `agent:<agentId>:<channel>:group:<id>` (ruimtes/kanalen: `agent:<agentId>:<channel>:channel:<id>`); Heartbeats houden achtergrondtaken actief.


## Kern-Skills (inschakelen in Instellingen → Skills)

  * **mcporter** \- Toolserver-runtime/CLI voor het beheren van externe Skill-backends.
  * **Peekaboo** \- Snelle macOS-screenshots met optionele AI-visieanalyse.
  * **camsnap** \- Frames, clips of bewegingsmeldingen vastleggen van RTSP/ONVIF-beveiligingscamera's.
  * **oracle** \- Agent-CLI geschikt voor OpenAI, met sessieherhaling en browserbesturing.
  * **eightctl** \- Beheer je slaap vanaf de terminal.
  * **imsg** \- iMessage en SMS verzenden, lezen en streamen.
  * **wacli** \- WhatsApp CLI: synchroniseren, zoeken, verzenden.
  * **discord** \- Discord-acties: reageren, stickers, polls. Gebruik `user:<id>`\- of `channel:<id>`-doelen (losse numerieke id's zijn ambigu).
  * **gog** \- Google Suite CLI: Gmail, Calendar, Drive, Contacts.
  * **spotify-player** \- Terminalclient voor Spotify om afspelen te zoeken/in de wachtrij te zetten/te bedienen.
  * **sag** \- ElevenLabs-spraak met mac-achtige say-UX; streamt standaard naar speakers.
  * **Sonos CLI** \- Bedien Sonos-speakers (ontdekken/status/afspelen/volume/groeperen) vanuit scripts.
  * **blucli** \- Speel BluOS-spelers af, groepeer ze en automatiseer ze vanuit scripts.
  * **OpenHue CLI** \- Philips Hue-lichtbediening voor scenes en automatiseringen.
  * **OpenAI Whisper** \- Lokale spraak-naar-tekst voor snelle dictatie en voicemailtranscripties.
  * **Gemini CLI** \- Google Gemini-modellen vanaf de terminal voor snelle vraag-en-antwoord.
  * **agent-tools** \- Hulppakket voor automatiseringen en helperscripts.


## Gebruiksnotities

  * Geef de voorkeur aan de `openclaw` CLI voor scripting; de Mac-app handelt machtigingen af.
  * Voer installaties uit vanaf het tabblad Skills; dit verbergt de knop als er al een binary aanwezig is.
  * Houd Heartbeats ingeschakeld zodat de assistent herinneringen kan plannen, inboxen kan monitoren en camera-opnames kan activeren.
  * Canvas-UI draait schermvullend met native overlays. Plaats geen kritieke bedieningselementen in de bovenlinker-/bovenrechter-/onderranden; voeg expliciete goten toe in de lay-out en vertrouw niet op safe-area-insets.
  * Gebruik voor browsergestuurde verificatie `openclaw browser` (tabs/status/screenshot) met het door OpenClaw beheerde Chrome-profiel.
  * Gebruik voor DOM-inspectie `openclaw browser eval|query|dom|snapshot` (en `--json`/`--out` wanneer je machine-uitvoer nodig hebt).
  * Gebruik voor interacties `openclaw browser click|type|hover|drag|select|upload|press|wait|navigate|back|evaluate|run` (click/type vereisen snapshot-verwijzingen; gebruik `evaluate` voor CSS-selectors).


## Gerelateerd

  * [Agentwerkruimte](</nl/concepts/agent-workspace>)
  * [Agentruntime](</nl/concepts/agent>)


Was this useful?YesNo