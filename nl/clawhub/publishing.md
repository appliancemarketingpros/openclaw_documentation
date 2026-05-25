---
title: Publiceren
source_url: https://docs.openclaw.ai/nl/clawhub/publishing
scraped_at: 2026-05-25
---

# Publiceren

Publiceren op ClawHub is eigenaarsgebonden: elke publicatie richt zich op een publisher, en de server bepaalt of de aangemelde gebruiker daar mag publiceren.

## Eigenaren

Een eigenaar is een ClawHub-publisherhandle, zoals `@alice` of `@openclaw`. Persoonlijke eigenaren worden voor gebruikers aangemaakt. Organisatie-eigenaren kunnen meerdere leden hebben.

Wanneer je publiceert, gebruik je je persoonlijke eigenaar of kies je een organisatie-eigenaar waarvoor je publishertoegang hebt.

## Skills

Skills worden gepubliceerd vanuit een skillmap. De openbare pagina is:

textCopy code
[code]
    https://clawhub.ai/<owner>/<slug>
[/code]

Voorbeeld:

textCopy code
[code]
    https://clawhub.ai/alice/review-helper
[/code]

De publicatieaanvraag bevat de geselecteerde eigenaar, slug, versie, changelog en bestanden. De server controleert of de actor als die eigenaar mag publiceren voordat de release wordt aangemaakt.

Als je een bestaande skill naar een andere eigenaar wilt verplaatsen terwijl je een nieuwe versie publiceert, kies je de nieuwe eigenaar en bevestig je de eigendomsoverdracht expliciet. Geef in de CLI/API de doeleigenaar plus de migratie-opt-in door:

shCopy code
[code]
    clawhub skill publish ./review-helper --owner openclaw --migrate-owner --version 1.2.0
[/code]

Migratie van een skill-eigenaar vereist beheerders- of eigenaarstoegang bij zowel de huidige eigenaar als de bestemmingseigenaar. De skill, versiegeschiedenis, statistieken, opmerkingen, forks, aliassen en audittrail blijven behouden; oude eigenaar-URL's blijven werken via het alias-/redirectpad.

## Plugins

Plugins gebruiken npm-achtige pakketnamen. Scoped pakketnamen bevatten de eigenaar in het eerste deel van de naam:

textCopy code
[code]
    @owner/package-name
[/code]

De scope moet overeenkomen met de geselecteerde publicatie-eigenaar. Als je pakket `@openclaw/dronzer` heet, kan het alleen als `@openclaw` worden gepubliceerd. Als je publiceert als `@vintageayu`, hernoem het pakket dan naar `@vintageayu/dronzer`.

Dit voorkomt dat een pakket een organisatienamespace claimt waarover de publisher geen controle heeft.

## Releaseproces

  1. De UI, CLI of GitHub-workflow verzamelt pakketmetadata en bestanden.
  2. De publicatieaanvraag wordt naar ClawHub verzonden met de geselecteerde eigenaar.
  3. De server valideert eigenaarsrechten, pakketscope, pakketnaam, versie, bestandslimieten en bronmetadata.
  4. ClawHub slaat de release op en start geautomatiseerde beveiligingscontroles.
  5. Nieuwe releases worden verborgen voor normale installatie-/downloadoppervlakken totdat beoordeling en verificatie zijn afgerond.


Als validatie mislukt, wordt de release niet aangemaakt.

## FAQ

### Pakketscope moet overeenkomen met geselecteerde eigenaar

Als de pakketscope en geselecteerde eigenaar niet overeenkomen, wijst ClawHub de publicatie af:

textCopy code
[code]
    Package scope "@openclaw" must match selected owner "@vintageayu".Publish as "@openclaw" or rename this package to "@vintageayu/dronzer".
[/code]

Om dit op te lossen, kies je de eigenaar die door de pakketscope wordt genoemd, of hernoem je het pakket zodat de scope overeenkomt met de eigenaar waaronder je mag publiceren.

Als de pakketnaam al de juiste scope heeft maar het pakket eigendom is van de verkeerde publisher, draag dan in plaats daarvan het eigendom over:

shCopy code
[code]
    clawhub package transfer @opik/opik-openclaw --to opik
[/code]

Gebruik pakket- of skilloverdracht alleen wanneer je beheerdersrechten hebt bij zowel de huidige eigenaar als de bestemmingspublisher. Met pakketoverdracht kun je niet publiceren in een scope die je niet kunt beheren.

Dit beschermt organisatienamespaces. Een pakket met de naam `@openclaw/dronzer` claimt de `@openclaw`-namespace, dus alleen publishers met toegang tot de `@openclaw`-eigenaar kunnen het publiceren.

Was this useful?YesNo