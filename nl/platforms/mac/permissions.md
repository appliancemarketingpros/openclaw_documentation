---
title: macOS-machtigingen
source_url: https://docs.openclaw.ai/nl/platforms/mac/permissions
scraped_at: 2026-05-25
---

macOS-toestemmingsverleningen zijn kwetsbaar. TCC koppelt een verleende toestemming aan de codehandtekening, bundel-ID en het pad op schijf van de app. Als een daarvan verandert, behandelt macOS de app als nieuw en kan het toestemmingsvragen verwijderen of verbergen.

## Vereisten voor stabiele toestemmingen

  * Zelfde pad: voer de app uit vanaf een vaste locatie (voor OpenClaw, `dist/OpenClaw.app`).
  * Zelfde bundel-ID: het wijzigen van de bundel-ID maakt een nieuwe toestemmingsidentiteit aan.
  * Ondertekende app: niet-ondertekende of ad-hoc ondertekende builds behouden toestemmingen niet.
  * Consistente handtekening: gebruik een echt Apple Development- of Developer ID-certificaat zodat de handtekening stabiel blijft tussen rebuilds.


Ad-hoc handtekeningen genereren bij elke build een nieuwe identiteit. macOS vergeet eerdere verleningen, en toestemmingsvragen kunnen volledig verdwijnen totdat de verouderde vermeldingen zijn gewist.

## Herstelchecklist wanneer toestemmingsvragen verdwijnen

  1. Sluit de app af.
  2. Verwijder de app-vermelding in Systeeminstellingen -> Privacy en beveiliging.
  3. Start de app opnieuw vanaf hetzelfde pad en verleen de toestemmingen opnieuw.
  4. Als de toestemmingsvraag nog steeds niet verschijnt, reset dan TCC-vermeldingen met `tccutil` en probeer het opnieuw.
  5. Sommige toestemmingen verschijnen pas opnieuw na een volledige macOS-herstart.


Voorbeeldresets (vervang de bundel-ID waar nodig):

bashCopy code
[code]
    sudo tccutil reset Accessibility ai.openclaw.macsudo tccutil reset ScreenCapture ai.openclaw.macsudo tccutil reset AppleEvents
[/code]

## Bestands- en maptoestemmingen (Bureaublad/Documenten/Downloads)

macOS kan ook Bureaublad, Documenten en Downloads afschermen voor terminal-/achtergrondprocessen. Als het lezen van bestanden of het weergeven van mappen blijft hangen, verleen dan toegang aan dezelfde procescontext die bestandsbewerkingen uitvoert (bijvoorbeeld Terminal/iTerm, een door LaunchAgent gestarte app of een SSH-proces).

Tijdelijke oplossing: verplaats bestanden naar de OpenClaw-werkruimte (`~/.openclaw/workspace`) als je toestemmingen per map wilt vermijden.

Als je toestemmingen test, onderteken dan altijd met een echt certificaat. Ad-hoc builds zijn alleen acceptabel voor snelle lokale runs waarbij toestemmingen er niet toe doen.

## Gerelateerd

  * [macOS-app](</nl/platforms/macos>)
  * [macOS-ondertekening](</nl/platforms/mac/signing>)


Was this useful?YesNo