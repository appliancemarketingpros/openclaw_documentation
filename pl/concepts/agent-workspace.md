---
title: Przestrzeń robocza agenta
source_url: https://docs.openclaw.ai/pl/concepts/agent-workspace
scraped_at: 2026-05-25
---

Obszar roboczy jest domem agenta. Jest jedynym katalogiem roboczym używanym przez narzędzia plikowe i kontekst obszaru roboczego. Zachowaj jego prywatność i traktuj go jak pamięć.

Jest to niezależne od `~/.openclaw/`, gdzie przechowywane są konfiguracja, poświadczenia i sesje.

## Domyślna lokalizacja

  * Domyślnie: `~/.openclaw/workspace`
  * Jeśli ustawiono `OPENCLAW_PROFILE` i nie ma wartości `"default"`, domyślna lokalizacja staje się `~/.openclaw/workspace-<profile>`.
  * Nadpisanie w `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/.openclaw/workspace",    },  },}
[/code]

`openclaw onboard`, `openclaw configure` lub `openclaw setup` utworzą obszar roboczy i dodadzą początkowe pliki bootstrap, jeśli ich brakuje.

Jeśli już samodzielnie zarządzasz plikami obszaru roboczego, możesz wyłączyć tworzenie plików bootstrap:

json5Copy code
[code]
    { agents: { defaults: { skipBootstrap: true } } }
[/code]

## Dodatkowe foldery obszaru roboczego

Starsze instalacje mogły utworzyć `~/openclaw`. Przechowywanie wielu katalogów obszaru roboczego może powodować mylące rozjazdy uwierzytelniania lub stanu, ponieważ w danym momencie aktywny jest tylko jeden obszar roboczy.

## Mapa plików obszaru roboczego

Oto standardowe pliki, których OpenClaw oczekuje w obszarze roboczym:

AGENTS.md - instrukcje operacyjne

Instrukcje operacyjne dla agenta oraz sposób używania pamięci. Ładowane na początku każdej sesji. Dobre miejsce na reguły, priorytety i szczegóły „jak się zachowywać”.

SOUL.md - persona i ton

Persona, ton i granice. Ładowane w każdej sesji. Przewodnik: [przewodnik osobowości SOUL.md](</pl/concepts/soul>).

USER.md - kim jest użytkownik

Kim jest użytkownik i jak się do niego zwracać. Ładowane w każdej sesji.

IDENTITY.md - imię, styl, emoji

Imię agenta, styl i emoji. Tworzone/aktualizowane podczas rytuału bootstrap.

TOOLS.md - lokalne konwencje narzędzi

Notatki o lokalnych narzędziach i konwencjach. Nie steruje dostępnością narzędzi; to tylko wskazówki.

HEARTBEAT.md - lista kontrolna heartbeat

Opcjonalna krótka lista kontrolna dla uruchomień Heartbeat. Zachowaj ją krótką, aby uniknąć zużycia tokenów.

BOOT.md - lista kontrolna startu

Opcjonalna lista kontrolna startu uruchamiana automatycznie przy restarcie Gateway (gdy włączone są [wewnętrzne hooki](</pl/automation/hooks>)). Zachowaj ją krótką; do wysyłek wychodzących używaj narzędzia wiadomości.

BOOTSTRAP.md - rytuał pierwszego uruchomienia

Jednorazowy rytuał pierwszego uruchomienia. Tworzony tylko dla zupełnie nowego obszaru roboczego. Usuń go po zakończeniu rytuału.

memory/YYYY-MM-DD.md - dzienny dziennik pamięci

Dzienny dziennik pamięci (jeden plik na dzień). Zalecane jest odczytanie dzisiejszego i wczorajszego dnia przy starcie sesji.

MEMORY.md - utrzymana pamięć długoterminowa (opcjonalnie)

Utrzymana pamięć długoterminowa: trwałe fakty, preferencje, decyzje i krótkie podsumowania. Szczegółowe logi trzymaj w `memory/YYYY-MM-DD.md`, aby narzędzia pamięci mogły pobierać je na żądanie bez wstrzykiwania ich do każdego promptu. Ładuj `MEMORY.md` tylko w głównej, prywatnej sesji (nie w kontekstach współdzielonych/grupowych). Zobacz [Pamięć](</pl/concepts/memory>), aby poznać workflow i automatyczne opróżnianie pamięci.

skills/ - Skills obszaru roboczego (opcjonalnie)

Skills specyficzne dla obszaru roboczego. Lokalizacja Skills o najwyższym priorytecie dla tego obszaru roboczego. Nadpisuje Skills agenta projektu, osobiste Skills agenta, zarządzane Skills, dołączone Skills oraz `skills.load.extraDirs`, gdy nazwy kolidują.

canvas/ - pliki interfejsu Canvas (opcjonalnie)

Pliki interfejsu Canvas dla wyświetlaczy węzłów (na przykład `canvas/index.html`).

## Czego NIE ma w obszarze roboczym

Te elementy znajdują się pod `~/.openclaw/` i NIE powinny być commitowane do repozytorium obszaru roboczego:

  * `~/.openclaw/openclaw.json` (konfiguracja)
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` (profile uwierzytelniania modelu: OAuth + klucze API)
  * `~/.openclaw/agents/<agentId>/agent/codex-home/` (konto runtime Codex dla agenta, konfiguracja, Skills, plugins i natywny stan wątku)
  * `~/.openclaw/credentials/` (stan kanału/providera oraz starsze dane importu OAuth)
  * `~/.openclaw/agents/<agentId>/sessions/` (transkrypty sesji + metadane)
  * `~/.openclaw/skills/` (zarządzane Skills)


Jeśli musisz migrować sesje lub konfigurację, skopiuj je oddzielnie i trzymaj poza kontrolą wersji.

## Kopia zapasowa w Git (zalecana, prywatna)

Traktuj obszar roboczy jak prywatną pamięć. Umieść go w **prywatnym** repozytorium git, aby był objęty kopią zapasową i możliwy do odzyskania.

Uruchom te kroki na maszynie, na której działa Gateway (tam znajduje się obszar roboczy).

* ### Zainicjalizuj repozytorium

Jeśli git jest zainstalowany, zupełnie nowe obszary robocze są inicjalizowane automatycznie. Jeśli ten obszar roboczy nie jest jeszcze repozytorium, uruchom:

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.md SOUL.md TOOLS.md IDENTITY.md USER.md HEARTBEAT.md memory/git commit -m "Add agent workspace"
[/code]

* ### Dodaj prywatny remote

### Interfejs webowy GitHub

  1. Utwórz nowe **prywatne** repozytorium na GitHub.
  2. Nie inicjalizuj go plikiem README (pozwala to uniknąć konfliktów scalania).
  3. Skopiuj zdalny URL HTTPS.
  4. Dodaj remote i wypchnij:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

### GitHub CLI (gh)

bashCopy code
[code]
    gh auth logingh repo create openclaw-workspace --private --source . --remote origin --push
[/code]

### Interfejs webowy GitLab

  1. Utwórz nowe **prywatne** repozytorium na GitLab.
  2. Nie inicjalizuj go plikiem README (pozwala to uniknąć konfliktów scalania).
  3. Skopiuj zdalny URL HTTPS.
  4. Dodaj remote i wypchnij:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

* ### Bieżące aktualizacje

bashCopy code
[code]
    git statusgit add .git commit -m "Update memory"git push
[/code]

## Nie commituj sekretów

Sugerowany starter `.gitignore`:

gitignoreCopy code
[code]
    .DS_Store.env**/*.key**/*.pem**/secrets*
[/code]

## Przenoszenie obszaru roboczego na nową maszynę

* ### Sklonuj repozytorium

Sklonuj repozytorium do wybranej ścieżki (domyślnie `~/.openclaw/workspace`).

* ### Zaktualizuj konfigurację

Ustaw `agents.defaults.workspace` na tę ścieżkę w `~/.openclaw/openclaw.json`.

* ### Uzupełnij brakujące pliki

Uruchom `openclaw setup --workspace <path>`, aby dodać brakujące pliki.

* ### Skopiuj sesje (opcjonalnie)

Jeśli potrzebujesz sesji, skopiuj oddzielnie `~/.openclaw/agents/<agentId>/sessions/` ze starej maszyny.

## Uwagi zaawansowane

  * Routing wielu agentów może używać różnych obszarów roboczych dla poszczególnych agentów. Zobacz [routing kanałów](</pl/channels/channel-routing>), aby poznać konfigurację routingu.
  * Jeśli `agents.defaults.sandbox` jest włączone, sesje inne niż główna mogą używać obszarów roboczych piaskownicy dla sesji pod `agents.defaults.sandbox.workspaceRoot`.


## Powiązane

  * [Heartbeat](</pl/gateway/heartbeat>) \- plik obszaru roboczego [HEARTBEAT.md](<http://HEARTBEAT.md>)
  * [Piaskownica](</pl/gateway/sandboxing>) \- dostęp do obszaru roboczego w środowiskach piaskownicy
  * [Sesja](</pl/concepts/session>) \- ścieżki przechowywania sesji
  * [Stałe polecenia](</pl/automation/standing-orders>) \- trwałe instrukcje w plikach obszaru roboczego


Was this useful?YesNo