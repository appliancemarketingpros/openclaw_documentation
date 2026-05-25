---
title: Voltooiing
source_url: https://docs.openclaw.ai/nl/cli/completion
scraped_at: 2026-05-25
---

# `openclaw completion`

Genereer shellcompletion-scripts en installeer ze optioneel in je shellprofiel.

## Gebruik

bashCopy code
[code]
    openclaw completionopenclaw completion --shell zshopenclaw completion --installopenclaw completion --shell fish --installopenclaw completion --write-stateopenclaw completion --shell bash --write-state
[/code]

## Opties

  * `-s, --shell <shell>`: doel-shell (`zsh`, `bash`, `powershell`, `fish`; standaard: `zsh`)
  * `-i, --install`: installeer completion door een source-regel aan je shellprofiel toe te voegen
  * `--write-state`: schrijf completion-script(s) naar `$OPENCLAW_STATE_DIR/completions` zonder naar stdout te printen
  * `-y, --yes`: sla bevestigingsprompts voor installatie over


## Opmerkingen

  * `--install` schrijft een klein blok "OpenClaw Completion" naar je shellprofiel en laat het verwijzen naar het gecachete script.
  * Zonder `--install` of `--write-state` print de opdracht het script naar stdout.
  * Completion-generatie laadt opdrachtbomen meteen, zodat geneste subopdrachten worden meegenomen.


## Gerelateerd

  * [CLI-naslag](</nl/cli>)


Was this useful?YesNo