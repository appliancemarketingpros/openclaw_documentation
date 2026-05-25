---
title: Kanały wydań
source_url: https://docs.openclaw.ai/pl/install/development-channels
scraped_at: 2026-05-25
---

OpenClaw udostępnia trzy kanały aktualizacji:

  * **stable** : npm dist-tag `latest`. Zalecany dla większości użytkowników.
  * **beta** : npm dist-tag `beta`, gdy jest aktualny; jeśli beta jest niedostępna lub starsza niż najnowsze wydanie stable, przepływ aktualizacji wraca do `latest`.
  * **dev** : ruchoma głowica gałęzi `main` (git). npm dist-tag: `dev` (gdy opublikowany). Gałąź `main` służy do eksperymentów i aktywnego rozwoju. Może zawierać nieukończone funkcje lub zmiany niezgodne wstecz. Nie używaj jej dla bram produkcyjnych.


Zazwyczaj najpierw publikujemy kompilacje stable do **beta** , testujemy je tam, a następnie uruchamiamy jawny krok promocji, który przenosi zweryfikowaną kompilację do `latest` bez zmiany numeru wersji. Maintainerzy mogą też w razie potrzeby opublikować wydanie stable bezpośrednio do `latest`. Dist-tagi są źródłem prawdy dla instalacji npm.

## Przełączanie kanałów

bashCopy code
[code]
    openclaw update --channel stableopenclaw update --channel betaopenclaw update --channel dev
[/code]

`--channel` zapisuje wybrany kanał w konfiguracji (`update.channel`) i dopasowuje metodę instalacji:

  * **`stable`** (instalacje pakietowe): aktualizuje przez npm dist-tag `latest`.
  * **`beta`** (instalacje pakietowe): preferuje npm dist-tag `beta`, ale wraca do `latest`, gdy `beta` jest niedostępny lub starszy niż bieżący tag stable.
  * **`stable`** (instalacje git): pobiera najnowszy tag git stable.
  * **`beta`** (instalacje git): preferuje najnowszy tag git beta, ale wraca do najnowszego taga git stable, gdy beta jest niedostępna lub starsza.
  * **`dev`** : zapewnia checkout git (domyślnie `~/openclaw`, można nadpisać przez `OPENCLAW_GIT_DIR`), przełącza na `main`, wykonuje rebase względem upstream, buduje i instaluje globalny CLI z tego checkoutu.


## Jednorazowe wskazanie wersji lub taga

Użyj `--tag`, aby wskazać konkretny dist-tag, wersję lub specyfikację pakietu dla pojedynczej aktualizacji **bez** zmieniania zapisanego kanału:

bashCopy code
[code]
    # Install a specific versionopenclaw update --tag 2026.4.1-beta.1 # Install from the beta dist-tag (one-off, does not persist)openclaw update --tag beta # Install from GitHub main branch (npm tarball)openclaw update --tag main # Install a specific npm package specopenclaw update --tag openclaw@2026.4.1-beta.1
[/code]

Uwagi:

  * `--tag` dotyczy **wyłącznie instalacji pakietowych (npm)**. Instalacje git go ignorują.
  * Tag nie jest zapisywany. Następne `openclaw update` użyje jak zwykle skonfigurowanego kanału.
  * Ochrona przed obniżeniem wersji: jeśli wersja docelowa jest starsza niż bieżąca wersja, OpenClaw poprosi o potwierdzenie (pomiń przez `--yes`).
  * `--channel beta` różni się od `--tag beta`: przepływ kanału może wrócić do stable/latest, gdy beta jest niedostępna lub starsza, natomiast `--tag beta` wskazuje surowy dist-tag `beta` tylko dla tego jednego uruchomienia.


## Próba bez zmian

Podejrzyj, co zrobiłoby `openclaw update`, bez wprowadzania zmian:

bashCopy code
[code]
    openclaw update --dry-runopenclaw update --channel beta --dry-runopenclaw update --tag 2026.4.1-beta.1 --dry-runopenclaw update --dry-run --json
[/code]

Próba bez zmian pokazuje efektywny kanał, wersję docelową, planowane działania oraz czy wymagane byłoby potwierdzenie obniżenia wersji.

## Pluginy i kanały

Gdy przełączasz kanały za pomocą `openclaw update`, OpenClaw synchronizuje także źródła Pluginów:

  * `dev` preferuje dołączone Pluginy z checkoutu git.
  * `stable` i `beta` przywracają pakiety Pluginów zainstalowane przez npm.
  * Pluginy zainstalowane przez npm są aktualizowane po zakończeniu aktualizacji rdzenia.


## Sprawdzanie bieżącego stanu

bashCopy code
[code]
    openclaw update status
[/code]

Pokazuje aktywny kanał, rodzaj instalacji (git lub pakiet), bieżącą wersję oraz źródło (konfiguracja, tag git, gałąź git lub wartość domyślna).

## Najlepsze praktyki tagowania

  * Oznaczaj tagami wydania, na których mają lądować checkouty git (`vYYYY.M.D` dla stable, `vYYYY.M.D-beta.N` dla beta).
  * `vYYYY.M.D.beta.N` jest również rozpoznawany ze względu na zgodność, ale preferuj `-beta.N`.
  * Starsze tagi `vYYYY.M.D-<patch>` są nadal rozpoznawane jako stable (nie beta).
  * Utrzymuj tagi jako niezmienne: nigdy nie przenoś ani nie używaj ponownie taga.
  * npm dist-tagi pozostają źródłem prawdy dla instalacji npm: 
    * `latest` -> stable
    * `beta` -> kompilacja kandydująca lub kompilacja stable publikowana najpierw do beta
    * `dev` -> migawka main (opcjonalnie)


## Dostępność aplikacji macOS

Kompilacje beta i dev mogą **nie** zawierać wydania aplikacji macOS. To jest w porządku:

  * Tag git i npm dist-tag nadal mogą zostać opublikowane.
  * W informacjach o wydaniu lub changelogu zaznacz „brak kompilacji macOS dla tej bety”.


## Powiązane

  * [Aktualizowanie](</pl/install/updating>)
  * [Wewnętrzne mechanizmy instalatora](</pl/install/installer>)


Was this useful?YesNo