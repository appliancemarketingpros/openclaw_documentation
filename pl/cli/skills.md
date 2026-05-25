---
title: Skills
source_url: https://docs.openclaw.ai/pl/cli/skills
scraped_at: 2026-05-25
---

# `openclaw skills`

Sprawdzaj lokalne Skills oraz instaluj/aktualizuj Skills z ClawHub.

Powiązane:

  * System Skills: [Skills](</pl/tools/skills>)
  * Konfiguracja Skills: [Konfiguracja Skills](</pl/tools/skills-config>)
  * Instalacje ClawHub: [ClawHub](</pl/clawhub/cli>)


## Polecenia

bashCopy code
[code]
    openclaw skills search "calendar"openclaw skills search --limit 20 --jsonopenclaw skills install <slug>openclaw skills install <slug> --version <version>openclaw skills install <slug> --forceopenclaw skills install <slug> --agent <id>openclaw skills update <slug>openclaw skills update --allopenclaw skills update --all --agent <id>openclaw skills listopenclaw skills list --eligibleopenclaw skills list --jsonopenclaw skills list --verboseopenclaw skills list --agent <id>openclaw skills info <name>openclaw skills info <name> --jsonopenclaw skills info <name> --agent <id>openclaw skills checkopenclaw skills check --agent <id>openclaw skills check --json
[/code]

`search`/`install`/`update` używają bezpośrednio ClawHub i instalują w katalogu `skills/` aktywnej przestrzeni roboczej. `list`/`info`/`check` nadal sprawdzają lokalne Skills widoczne dla bieżącej przestrzeni roboczej i konfiguracji. Polecenia oparte na przestrzeni roboczej ustalają docelową przestrzeń roboczą na podstawie `--agent <id>`, następnie bieżącego katalogu roboczego, gdy znajduje się on w skonfigurowanej przestrzeni roboczej agenta, a następnie domyślnego agenta.

To polecenie CLI `install` pobiera foldery Skills z ClawHub. Instalacje zależności Skills oparte na Gateway, wyzwalane z wdrażania lub ustawień Skills, używają zamiast tego oddzielnej ścieżki żądania `skills.install`.

Uwagi:

  * `search [query...]` akceptuje opcjonalne zapytanie; pomiń je, aby przeglądać domyślny kanał wyszukiwania ClawHub.
  * `search --limit <n>` ogranicza liczbę zwracanych wyników.
  * `install --force` nadpisuje istniejący folder Skills w przestrzeni roboczej dla tego samego sluga.
  * `--agent <id>` wskazuje jedną skonfigurowaną przestrzeń roboczą agenta i zastępuje wnioskowanie na podstawie bieżącego katalogu roboczego.
  * `update --all` aktualizuje tylko śledzone instalacje ClawHub w aktywnej przestrzeni roboczej.
  * `check --agent <id>` sprawdza przestrzeń roboczą wybranego agenta i raportuje, które gotowe Skills są faktycznie widoczne w prompcie tego agenta lub na powierzchni poleceń.
  * `list` jest domyślną akcją, gdy nie podano podpolecenia.
  * `list`, `info` i `check` zapisują renderowane dane wyjściowe do stdout. Z `--json` oznacza to, że ładunek czytelny maszynowo pozostaje na stdout dla potoków i skryptów.


## Powiązane

  * [Dokumentacja CLI](</pl/cli>)
  * [Skills](</pl/tools/skills>)


Was this useful?YesNo