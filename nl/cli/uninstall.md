---
title: Verwijderen
source_url: https://docs.openclaw.ai/nl/cli/uninstall
scraped_at: 2026-05-25
---

# `openclaw uninstall`

Deïnstalleer de Gateway-service + lokale gegevens (CLI blijft behouden).

Opties:

  * `--service`: verwijder de Gateway-service
  * `--state`: verwijder status en configuratie
  * `--workspace`: verwijder werkruimtemappen
  * `--app`: verwijder de macOS-app
  * `--all`: verwijder service, status, werkruimte en app
  * `--yes`: sla bevestigingsprompts over
  * `--non-interactive`: schakel prompts uit; vereist `--yes`
  * `--dry-run`: druk acties af zonder bestanden te verwijderen


Voorbeelden:

bashCopy code
[code]
    openclaw backup createopenclaw uninstallopenclaw uninstall --service --yes --non-interactiveopenclaw uninstall --state --workspace --yes --non-interactiveopenclaw uninstall --all --yesopenclaw uninstall --dry-run
[/code]

Opmerkingen:

  * Voer eerst `openclaw backup create` uit als je een herstelbare momentopname wilt voordat je status of werkruimtes verwijdert.
  * `--all` is een verkorte schrijfwijze om service, status, werkruimte en app samen te verwijderen.
  * `--non-interactive` vereist `--yes`.


## Gerelateerd

  * [CLI-referentie](</nl/cli>)
  * [Deïnstalleren](</nl/install/uninstall>)


Was this useful?YesNo