---
title: Resetten
source_url: https://docs.openclaw.ai/nl/cli/reset
scraped_at: 2026-05-25
---

# `openclaw reset`

Lokale configuratie/status resetten (laat de CLI geïnstalleerd).

Opties:

  * `--scope <scope>`: `config`, `config+creds+sessions`, of `full`
  * `--yes`: bevestigingsprompts overslaan
  * `--non-interactive`: prompts uitschakelen; vereist `--scope` en `--yes`
  * `--dry-run`: acties weergeven zonder bestanden te verwijderen


Voorbeelden:

bashCopy code
[code]
    openclaw backup createopenclaw resetopenclaw reset --dry-runopenclaw reset --scope config --yes --non-interactiveopenclaw reset --scope config+creds+sessions --yes --non-interactiveopenclaw reset --scope full --yes --non-interactive
[/code]

Opmerkingen:

  * Voer eerst `openclaw backup create` uit als je een herstelbare momentopname wilt voordat je de lokale status verwijdert.
  * Als je `--scope` weglaat, gebruikt `openclaw reset` een interactieve prompt om te kiezen wat er wordt verwijderd.
  * `--non-interactive` is alleen geldig wanneer zowel `--scope` als `--yes` zijn ingesteld.


## Gerelateerd

  * [CLI-referentie](</nl/cli>)


Was this useful?YesNo