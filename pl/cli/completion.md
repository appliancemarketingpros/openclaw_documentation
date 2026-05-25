---
title: Autouzupełnianie
source_url: https://docs.openclaw.ai/pl/cli/completion
scraped_at: 2026-05-25
---

# `openclaw completion`

Generuj skrypty autouzupełniania powłoki i opcjonalnie instaluj je w profilu swojej powłoki.

## Użycie

bashCopy code
[code]
    openclaw completionopenclaw completion --shell zshopenclaw completion --installopenclaw completion --shell fish --installopenclaw completion --write-stateopenclaw completion --shell bash --write-state
[/code]

## Opcje

  * `-s, --shell <shell>`: docelowa powłoka (`zsh`, `bash`, `powershell`, `fish`; domyślnie: `zsh`)
  * `-i, --install`: instaluje autouzupełnianie przez dodanie linii source do profilu powłoki
  * `--write-state`: zapisuje skrypt(y) autouzupełniania do `$OPENCLAW_STATE_DIR/completions` bez wypisywania na stdout
  * `-y, --yes`: pomija monity o potwierdzenie instalacji


## Uwagi

  * `--install` zapisuje mały blok „OpenClaw Completion” do profilu powłoki i wskazuje go na skrypt z pamięci podręcznej.
  * Bez `--install` lub `--write-state` polecenie wypisuje skrypt na stdout.
  * Generowanie autouzupełniania ładuje drzewa poleceń z wyprzedzeniem, aby uwzględnić zagnieżdżone podpolecenia.


## Powiązane

  * [Dokumentacja CLI](</pl/cli>)


Was this useful?YesNo