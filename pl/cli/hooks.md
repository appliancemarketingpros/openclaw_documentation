---
title: Hooki
source_url: https://docs.openclaw.ai/pl/cli/hooks
scraped_at: 2026-05-25
---

# `openclaw hooks`

Zarządzaj hookami agentów (automatyzacjami sterowanymi zdarzeniami dla poleceń takich jak `/new`, `/reset` oraz uruchamianie gatewaya).

Uruchomienie `openclaw hooks` bez podpolecenia jest równoważne z `openclaw hooks list`.

Powiązane:

  * Hooki: [Hooki](</pl/automation/hooks>)
  * Hooki Pluginów: [Hooki Pluginów](</pl/plugins/hooks>)


## Wyświetl wszystkie hooki

bashCopy code
[code]
    openclaw hooks list
[/code]

Wyświetla wszystkie wykryte hooki z katalogów workspace, zarządzanych, dodatkowych i dołączonych. Uruchomienie Gateway nie ładuje wewnętrznych handlerów hooków, dopóki nie zostanie skonfigurowany co najmniej jeden wewnętrzny hook.

**Opcje:**

  * `--eligible`: Pokaż tylko kwalifikujące się hooki (spełnione wymagania)
  * `--json`: Wyjście jako JSON
  * `-v, --verbose`: Pokaż szczegółowe informacje, w tym brakujące wymagania


**Przykładowe wyjście:**

CodeCopy code
[code]
    Hooks (4/4 ready) Ready:  🚀 boot-md ✓ - Run BOOT.md on gateway startup  📎 bootstrap-extra-files ✓ - Inject extra workspace bootstrap files during agent bootstrap  📝 command-logger ✓ - Log all command events to a centralized audit file  💾 session-memory ✓ - Save session context to memory when /new or /reset command is issued
[/code]

**Przykład (szczegółowo):**

bashCopy code
[code]
    openclaw hooks list --verbose
[/code]

Pokazuje brakujące wymagania dla niekwalifikujących się hooków.

**Przykład (JSON):**

bashCopy code
[code]
    openclaw hooks list --json
[/code]

Zwraca strukturalny JSON do użycia programowego.

## Pobierz informacje o hooku

bashCopy code
[code]
    openclaw hooks info <name>
[/code]

Pokaż szczegółowe informacje o określonym hooku.

**Argumenty:**

  * `<name>`: Nazwa hooka lub klucz hooka (np. `session-memory`)


**Opcje:**

  * `--json`: Wyjście jako JSON


**Przykład:**

bashCopy code
[code]
    openclaw hooks info session-memory
[/code]

**Wyjście:**

CodeCopy code
[code]
    💾 session-memory ✓ Ready Save session context to memory when /new or /reset command is issued Details:  Source: openclaw-bundled  Path: /path/to/openclaw/hooks/bundled/session-memory/HOOK.md  Handler: /path/to/openclaw/hooks/bundled/session-memory/handler.ts  Homepage: https://docs.openclaw.ai/automation/hooks#session-memory  Events: command:new, command:reset Requirements:  Config: ✓ workspace.dir
[/code]

## Sprawdź kwalifikowalność hooków

bashCopy code
[code]
    openclaw hooks check
[/code]

Pokaż podsumowanie statusu kwalifikowalności hooków (ile jest gotowych, a ile niegotowych).

**Opcje:**

  * `--json`: Wyjście jako JSON


**Przykładowe wyjście:**

CodeCopy code
[code]
    Hooks Status Total hooks: 4Ready: 4Not ready: 0
[/code]

## Włącz hook

bashCopy code
[code]
    openclaw hooks enable <name>
[/code]

Włącz określony hook, dodając go do swojej konfiguracji (domyślnie `~/.openclaw/openclaw.json`).

**Uwaga:** Hooki workspace są domyślnie wyłączone, dopóki nie zostaną włączone tutaj albo w konfiguracji. Hooki zarządzane przez Pluginy pokazują `plugin:<id>` w `openclaw hooks list` i nie można ich tutaj włączać ani wyłączać. Zamiast tego włącz lub wyłącz Plugin.

**Argumenty:**

  * `<name>`: Nazwa hooka (np. `session-memory`)


**Przykład:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Wyjście:**

CodeCopy code
[code]
    ✓ Enabled hook: 💾 session-memory
[/code]

**Co to robi:**

  * Sprawdza, czy hook istnieje i czy jest kwalifikowalny
  * Aktualizuje `hooks.internal.entries.<name>.enabled = true` w Twojej konfiguracji
  * Zapisuje konfigurację na dysku


Jeśli hook pochodzi z `<workspace>/hooks/`, ten krok akceptacji jest wymagany, zanim Gateway go załaduje.

**Po włączeniu:**

  * Uruchom ponownie gateway, aby hooki zostały przeładowane (restart aplikacji paska menu w macOS albo restart procesu gatewaya w trybie deweloperskim).


## Wyłącz hook

bashCopy code
[code]
    openclaw hooks disable <name>
[/code]

Wyłącz określony hook, aktualizując swoją konfigurację.

**Argumenty:**

  * `<name>`: Nazwa hooka (np. `command-logger`)


**Przykład:**

bashCopy code
[code]
    openclaw hooks disable command-logger
[/code]

**Wyjście:**

CodeCopy code
[code]
    ⏸ Disabled hook: 📝 command-logger
[/code]

**Po wyłączeniu:**

  * Uruchom ponownie gateway, aby hooki zostały przeładowane


## Uwagi

  * `openclaw hooks list --json`, `info --json` oraz `check --json` zapisują strukturalny JSON bezpośrednio do stdout.
  * Hooków zarządzanych przez Pluginy nie można tutaj włączać ani wyłączać; zamiast tego włącz lub wyłącz właścicielski Plugin.


## Zainstaluj pakiety hooków

bashCopy code
[code]
    openclaw plugins install <package>        # npm domyślnieopenclaw plugins install npm:<package>    # tylko npmopenclaw plugins install <package> --pin  # przypnij wersjęopenclaw plugins install <path>           # ścieżka lokalna
[/code]

Instaluj pakiety hooków przez ujednolicony instalator Pluginów.

`openclaw hooks install` nadal działa jako alias zgodności, ale wypisuje ostrzeżenie o wycofaniu i przekazuje dalej do `openclaw plugins install`.

Specyfikacje npm są **tylko z rejestru** (nazwa pakietu + opcjonalna **dokładna wersja** lub **dist-tag**). Specyfikacje Git/URL/plik i zakresy semver są odrzucane. Instalacje zależności działają lokalnie dla projektu z `--ignore-scripts` ze względów bezpieczeństwa, nawet gdy Twoja powłoka ma globalne ustawienia instalacji npm.

Gołe specyfikacje i `@latest` pozostają na stabilnej ścieżce. Jeśli npm rozwiąże którąkolwiek z nich do wersji przedpremierowej, OpenClaw zatrzyma się i poprosi o jednoznaczną akceptację za pomocą tagu przedpremierowego, takiego jak `@beta`/`@rc`, albo dokładnej wersji przedpremierowej.

**Co to robi:**

  * Kopiuje pakiet hooków do `~/.openclaw/hooks/<id>`
  * Włącza zainstalowane hooki w `hooks.internal.entries.*`
  * Rejestruje instalację w `hooks.internal.installs`


**Opcje:**

  * `-l, --link`: Połącz katalog lokalny zamiast go kopiować (dodaje go do `hooks.internal.load.extraDirs`)
  * `--pin`: Zapisz instalacje npm jako dokładnie rozwiązane `name@version` w `hooks.internal.installs`


**Obsługiwane archiwa:** `.zip`, `.tgz`, `.tar.gz`, `.tar`

**Przykłady:**

bashCopy code
[code]
    # Katalog lokalnyopenclaw plugins install ./my-hook-pack # Archiwum lokalneopenclaw plugins install ./my-hook-pack.zip # Pakiet NPMopenclaw plugins install @openclaw/my-hook-pack # Połącz katalog lokalny bez kopiowaniaopenclaw plugins install -l ./my-hook-pack
[/code]

Połączone pakiety hooków są traktowane jako zarządzane hooki z katalogu skonfigurowanego przez operatora, a nie jako hooki workspace.

## Aktualizuj pakiety hooków

bashCopy code
[code]
    openclaw plugins update <id>openclaw plugins update --all
[/code]

Aktualizuj śledzone pakiety hooków oparte na npm przez ujednolicony aktualizator Pluginów.

`openclaw hooks update` nadal działa jako alias zgodności, ale wypisuje ostrzeżenie o wycofaniu i przekazuje dalej do `openclaw plugins update`.

**Opcje:**

  * `--all`: Aktualizuj wszystkie śledzone pakiety hooków
  * `--dry-run`: Pokaż, co by się zmieniło, bez zapisywania


Gdy istnieje zapisany hash integralności i hash pobranego artefaktu się zmieni, OpenClaw wypisuje ostrzeżenie i prosi o potwierdzenie przed kontynuowaniem. Użyj globalnego `--yes`, aby pominąć monity w CI/uruchomieniach nieinteraktywnych.

## Dołączone hooki

### session-memory

Zapisuje kontekst sesji do pamięci, gdy wydasz `/new` lub `/reset`.

**Włącz:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Wyjście:** domyślnie `~/.openclaw/workspace/memory/YYYY-MM-DD-HHMM.md`. Ustaw `hooks.internal.entries.session-memory.llmSlug: true`, aby używać slugów nazw plików generowanych przez model.

**Zobacz:** [dokumentacja session-memory](</pl/automation/hooks#session-memory>)

### bootstrap-extra-files

Wstrzykuje dodatkowe pliki bootstrapu (na przykład lokalne dla monorepo `AGENTS.md` / `TOOLS.md`) podczas `agent:bootstrap`.

**Włącz:**

bashCopy code
[code]
    openclaw hooks enable bootstrap-extra-files
[/code]

**Zobacz:** [dokumentacja bootstrap-extra-files](</pl/automation/hooks#bootstrap-extra-files>)

### command-logger

Rejestruje wszystkie zdarzenia poleceń w scentralizowanym pliku audytu.

**Włącz:**

bashCopy code
[code]
    openclaw hooks enable command-logger
[/code]

**Wyjście:** `~/.openclaw/logs/commands.log`

**Wyświetl logi:**

bashCopy code
[code]
    # Ostatnie poleceniatail -n 20 ~/.openclaw/logs/commands.log # Ładne formatowaniecat ~/.openclaw/logs/commands.log | jq . # Filtruj według akcjigrep '"action":"new"' ~/.openclaw/logs/commands.log | jq .
[/code]

**Zobacz:** [dokumentacja command-logger](</pl/automation/hooks#command-logger>)

### boot-md

Uruchamia `BOOT.md`, gdy gateway startuje (po uruchomieniu kanałów).

**Zdarzenia** : `gateway:startup`

**Włącz** :

bashCopy code
[code]
    openclaw hooks enable boot-md
[/code]

**Zobacz:** [dokumentacja boot-md](</pl/automation/hooks#boot-md>)

## Powiązane

  * [Dokumentacja CLI](</pl/cli>)
  * [Hooki automatyzacji](</pl/automation/hooks>)


Was this useful?YesNo