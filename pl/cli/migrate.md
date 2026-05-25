---
title: Migracja
source_url: https://docs.openclaw.ai/pl/cli/migrate
scraped_at: 2026-05-25
---

# `openclaw migrate`

Importuj stan z innego systemu agentów za pośrednictwem dostawcy migracji należącego do pluginu. Dostawcy dołączeni w pakiecie obejmują stan Codex CLI, [Claude](</pl/install/migrating-claude>) i [Hermes](</pl/install/migrating-hermes>); pluginy firm trzecich mogą rejestrować dodatkowych dostawców.

## Polecenia

bashCopy code
[code]
    openclaw migrate listopenclaw migrate claude --dry-runopenclaw migrate codex --dry-runopenclaw migrate codex --skill gog-vault77-google-workspaceopenclaw migrate codex --plugin google-calendar --dry-runopenclaw migrate codex --plugin google-calendar --verify-plugin-apps --dry-runopenclaw migrate hermes --dry-runopenclaw migrate hermesopenclaw migrate apply codex --yes --skill gog-vault77-google-workspaceopenclaw migrate apply codex --yes --plugin google-calendaropenclaw migrate apply codex --yesopenclaw migrate apply claude --yesopenclaw migrate apply hermes --yesopenclaw migrate apply hermes --include-secrets --yesopenclaw onboard --flow importopenclaw onboard --import-from claude --import-source ~/.claudeopenclaw onboard --import-from hermes --import-source ~/.hermes
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ijxwcm92aWRlcg " type="string"> Nazwa zarejestrowanego dostawcy migracji, na przykład `hermes`. Uruchom `openclaw migrate list`, aby zobaczyć zainstalowanych dostawców.

Zbuduj plan i zakończ bez zmieniania stanu.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tZnJvbSA8cGF0aA " type="string"> Zastąp katalog stanu źródłowego. Hermes domyślnie używa `~/.hermes`.

Importuj obsługiwane poświadczenia. Domyślnie wyłączone.

Zezwól operacji apply na zastępowanie istniejących celów, gdy plan zgłasza konflikty.

Pomiń monit o potwierdzenie. Wymagane w trybie nieinteraktywnym.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tcGx1Z2luIDxuYW1l " type="string"> Wybierz jeden element instalacji pluginu Codex według nazwy pluginu lub identyfikatora elementu. Powtórz flagę, aby migrować wiele pluginów Codex. Po pominięciu interaktywne migracje Codex pokazują natywny selektor pól wyboru pluginów Codex, a migracje nieinteraktywne zachowują wszystkie zaplanowane pluginy. Dotyczy to tylko zainstalowanych w źródle pluginów Codex `openai-curated` wykrytych przez inwentarz serwera aplikacji Codex.

Tylko Codex. Wymuś świeże przejście `app/list` źródłowego serwera aplikacji Codex przed zaplanowaniem natywnej aktywacji pluginów. Domyślnie wyłączone, aby planowanie migracji było szybkie.

Pomiń kopię zapasową przed zastosowaniem. Wymaga `--force`, gdy lokalny stan OpenClaw istnieje.

Wymagane razem z `--no-backup`, gdy operacja apply w przeciwnym razie odmówiłaby pominięcia kopii zapasowej.

Wypisz plan lub wynik apply jako JSON. Z `--json` i bez `--yes` operacja apply wypisuje plan i nie modyfikuje stanu.

## Model bezpieczeństwa

`openclaw migrate` najpierw pokazuje podgląd.

Podgląd przed zastosowaniem

Dostawca zwraca wyszczególniony plan przed jakimikolwiek zmianami, w tym konflikty, pominięte elementy i elementy wrażliwe. Plany JSON, dane wyjściowe apply i raporty migracji redagują zagnieżdżone klucze wyglądające na sekrety, takie jak klucze API, tokeny, nagłówki autoryzacji, pliki cookie i hasła.

`openclaw migrate apply <provider>` pokazuje podgląd planu i prosi o potwierdzenie przed zmianą stanu, chyba że ustawiono `--yes`. W trybie nieinteraktywnym operacja apply wymaga `--yes`.

Kopie zapasowe

Operacja apply tworzy i weryfikuje kopię zapasową OpenClaw przed zastosowaniem migracji. Jeśli lokalny stan OpenClaw jeszcze nie istnieje, krok kopii zapasowej jest pomijany, a migracja może kontynuować. Aby pominąć kopię zapasową, gdy stan istnieje, przekaż zarówno `--no-backup`, jak i `--force`.

Konflikty

Operacja apply odmawia kontynuowania, gdy plan ma konflikty. Przejrzyj plan, a następnie uruchom ponownie z `--overwrite`, jeśli zastąpienie istniejących celów jest zamierzone. Dostawcy nadal mogą zapisywać kopie zapasowe na poziomie elementów dla nadpisanych plików w katalogu raportu migracji.

Sekrety

Sekrety nigdy nie są importowane domyślnie. Użyj `--include-secrets`, aby importować obsługiwane poświadczenia.

## Dostawca Claude

Dołączony dostawca Claude domyślnie wykrywa stan Claude Code w `~/.claude`. Użyj `--from <path>`, aby importować konkretny katalog domowy lub katalog główny projektu Claude Code.

### Co importuje Claude

  * Projektowe `CLAUDE.md` i `.claude/CLAUDE.md` do przestrzeni roboczej agenta OpenClaw.
  * Użytkownika `~/.claude/CLAUDE.md` dołączone do `USER.md` przestrzeni roboczej.
  * Definicje serwerów MCP z projektowego `.mcp.json`, Claude Code `~/.claude.json` i Claude Desktop `claude_desktop_config.json`.
  * Katalogi Skills Claude, które zawierają `SKILL.md`.
  * Pliki Markdown poleceń Claude przekonwertowane na Skills OpenClaw wyłącznie z ręcznym wywołaniem.


### Stan archiwum i ręcznego przeglądu

Hooki Claude, uprawnienia, domyślne ustawienia środowiska, pamięć lokalna, reguły ograniczone ścieżką, subagenci, pamięci podręczne, plany i historia projektu są zachowywane w raporcie migracji albo zgłaszane jako elementy do ręcznego przeglądu. OpenClaw nie wykonuje hooków, nie kopiuje szerokich list dozwolonych ani nie importuje automatycznie stanu poświadczeń OAuth/Desktop.

## Dostawca Codex

Dołączony dostawca Codex domyślnie wykrywa stan Codex CLI w `~/.codex` albo w `CODEX_HOME`, gdy ta zmienna środowiskowa jest ustawiona. Użyj `--from <path>`, aby zinwentaryzować konkretny katalog domowy Codex.

Użyj tego dostawcy podczas przechodzenia na uprząż OpenClaw Codex, gdy chcesz świadomie wypromować przydatne osobiste zasoby Codex CLI. Lokalne uruchomienia serwera aplikacji Codex używają katalogów `CODEX_HOME` i `HOME` przypisanych do agenta, więc domyślnie nie czytają osobistego stanu Codex CLI.

Uruchomienie `openclaw migrate codex` w terminalu interaktywnym pokazuje podgląd pełnego planu, a następnie otwiera selektory pól wyboru przed ostatecznym potwierdzeniem apply. Elementy kopiowania Skills są monitowane jako pierwsze. Użyj `Toggle all on` lub `Toggle all off` do masowego wyboru. Naciśnij spację, aby przełączać wiersze, albo Enter, aby aktywować podświetlony wiersz i kontynuować. Zaplanowane Skills zaczynają jako zaznaczone, Skills z konfliktem zaczynają jako niezaznaczone, a `Skip for now` pomija kopiowanie Skills w tym uruchomieniu, nadal przechodząc do wyboru pluginów. Gdy zainstalowane w źródle kuratorowane pluginy Codex można migrować i nie podano `--plugin`, migracja następnie monituje o natywną aktywację pluginów Codex według nazwy pluginu. Elementy pluginów zaczynają jako zaznaczone, chyba że docelowa konfiguracja pluginu OpenClaw Codex już ma ten plugin. Istniejące pluginy docelowe zaczynają jako niezaznaczone i pokazują wskazówkę konfliktu, taką jak `conflict: plugin exists`; wybierz `Toggle all off`, aby nie migrować żadnych natywnych pluginów Codex w tym uruchomieniu, albo `Skip for now`, aby zatrzymać się przed zastosowaniem. Dla uruchomień skryptowych lub dokładnych przekaż `--skill <name>` raz dla każdego Skills, na przykład:

bashCopy code
[code]
    openclaw migrate codex --dry-run --skill gog-vault77-google-workspaceopenclaw migrate apply codex --yes --skill gog-vault77-google-workspace
[/code]

Użyj `--plugin <name>`, aby nieinteraktywnie ograniczyć migrację natywnych pluginów Codex do jednego lub większej liczby zainstalowanych w źródle kuratorowanych pluginów:

bashCopy code
[code]
    openclaw migrate codex --dry-run --plugin google-calendaropenclaw migrate apply codex --yes --plugin google-calendar
[/code]

### Co importuje Codex

  * Katalogi Skills Codex CLI w `$CODEX_HOME/skills`, z wyłączeniem pamięci podręcznej `.system` Codex.
  * Osobiste AgentSkills w `$HOME/.agents/skills`, kopiowane do bieżącej przestrzeni roboczej agenta OpenClaw, gdy chcesz własności przypisanej do agenta.
  * Zainstalowane w źródle pluginy Codex `openai-curated` wykryte przez `plugin/list` serwera aplikacji Codex. Planowanie odczytuje `plugin/read` dla każdego włączonego zainstalowanego pluginu. Pluginy oparte na aplikacjach wymagają, aby odpowiedź konta źródłowego serwera aplikacji Codex była kontem subskrypcji ChatGPT; odpowiedzi spoza ChatGPT lub brakujące odpowiedzi konta są pomijane z `codex_subscription_required`. Domyślnie migracja nie wywołuje źródłowego `app/list`, więc pluginy oparte na aplikacjach, które przejdą bramkę konta, są planowane bez weryfikacji dostępności aplikacji źródłowej, a awarie transportu wyszukiwania konta są pomijane z `codex_account_unavailable`. Przekaż `--verify-plugin-apps`, gdy chcesz, aby migracja wymusiła świeżą migawkę źródłowego `app/list` i wymagała, by każda posiadana aplikacja była obecna, włączona i dostępna przed zaplanowaniem natywnej aktywacji. W tym trybie awarie transportu wyszukiwania konta przechodzą do weryfikacji inwentarza aplikacji źródłowych. Migawka inwentarza aplikacji źródłowych jest przechowywana w pamięci dla bieżącego procesu; nie jest zapisywana w danych wyjściowych migracji ani w konfiguracji docelowej. Wyłączone pluginy, nieczytelne szczegóły pluginów, konta źródłowe ograniczone subskrypcją oraz, gdy zażądano weryfikacji, brakujące aplikacje, wyłączone aplikacje, niedostępne aplikacje lub awarie inwentarza aplikacji źródłowych stają się ręcznie pominiętymi elementami z typowanymi powodami zamiast wpisów konfiguracji docelowej. Operacja apply wywołuje `plugin/install` serwera aplikacji dla każdego wybranego kwalifikującego się pluginu, nawet jeśli docelowy serwer aplikacji już zgłasza ten plugin jako zainstalowany i włączony. Zmigrowane pluginy Codex są użyteczne tylko w sesjach, które wybierają natywną uprząż Codex; nie są udostępniane Pi, zwykłym uruchomieniom dostawcy OpenAI, powiązaniom konwersacji ACP ani innym uprzężom.


### Stan Codex do ręcznego przeglądu

Codex `config.toml`, natywne `hooks/hooks.json`, niekuratorowane marketplace'y, buforowane pakiety pluginów, które nie są zainstalowanymi w źródle kuratorowanymi pluginami, oraz zainstalowane w źródle pluginy, które nie przejdą źródłowej bramki subskrypcji, nie są aktywowane automatycznie. Gdy ustawiono `--verify-plugin-apps`, pluginy, które nie przejdą bramki inwentarza aplikacji źródłowych, również są pomijane. Są kopiowane albo zgłaszane w raporcie migracji do ręcznego przeglądu.

Dla zmigrowanych zainstalowanych w źródle kuratorowanych pluginów operacja apply zapisuje:

  * `plugins.entries.codex.enabled: true`
  * `plugins.entries.codex.config.codexPlugins.enabled: true`
  * `plugins.entries.codex.config.codexPlugins.allow_destructive_actions: true`
  * jeden jawny wpis pluginu z `marketplaceName: "openai-curated"` i `pluginName` dla każdego wybranego pluginu


Migracja nigdy nie zapisuje `plugins["*"]` i nigdy nie przechowuje lokalnych ścieżek pamięci podręcznej marketplace'u. Awarie subskrypcji po stronie źródła są zgłaszane przy elementach ręcznych z typowanymi powodami, takimi jak `codex_subscription_required`, `codex_account_unavailable`, `plugin_disabled` lub `plugin_read_unavailable`. Z `--verify-plugin-apps` awarie inwentarza aplikacji źródłowych mogą również pojawić się jako `app_inaccessible`, `app_disabled`, `app_missing` lub `app_inventory_unavailable`. Pominięte pluginy nie są zapisywane w konfiguracji docelowej. Instalacje wymagające autoryzacji po stronie docelowej są zgłaszane przy dotkniętym elemencie pluginu z `status: "skipped"`, `reason: "auth_required"` i oczyszczonymi identyfikatorami aplikacji. Ich jawne wpisy konfiguracji są zapisywane jako wyłączone do czasu ponownej autoryzacji i włączenia ich. Inne awarie instalacji są wynikami `error` ograniczonymi do elementu.

Jeśli inwentarz pluginów serwera aplikacji Codex jest niedostępny podczas planowania, migracja cofa się do doradczych elementów buforowanych pakietów zamiast kończyć całą migrację niepowodzeniem.

## Dostawca Hermes

Dołączony dostawca Hermes domyślnie wykrywa stan w `~/.hermes`. Użyj `--from <path>`, gdy Hermes znajduje się gdzie indziej.

### Co importuje Hermes

  * Domyślna konfiguracja modelu z `config.yaml`.
  * Skonfigurowani dostawcy modeli i niestandardowe punkty końcowe zgodne z OpenAI z `providers` oraz `custom_providers`.
  * Definicje serwerów MCP z `mcp_servers` lub `mcp.servers`.
  * `SOUL.md` i `AGENTS.md` do obszaru roboczego agenta OpenClaw.
  * `memories/MEMORY.md` i `memories/USER.md` dołączone do plików pamięci obszaru roboczego.
  * Domyślne ustawienia konfiguracji pamięci plikowej OpenClaw oraz elementy archiwalne lub do ręcznego przeglądu dla zewnętrznych dostawców pamięci, takich jak Honcho.
  * Skills, które zawierają plik `SKILL.md` w `skills/<name>/`.
  * Wartości konfiguracji poszczególnych Skills z `skills.config`.
  * Obsługiwane klucze API z `.env`, tylko z `--include-secrets`.


### Obsługiwane klucze `.env`

`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `OPENROUTER_API_KEY`, `GOOGLE_API_KEY`, `GEMINI_API_KEY`, `GROQ_API_KEY`, `XAI_API_KEY`, `MISTRAL_API_KEY`, `DEEPSEEK_API_KEY`.

### Stan wyłącznie archiwalny

Stan Hermes, którego OpenClaw nie może bezpiecznie zinterpretować, jest kopiowany do raportu migracji do ręcznego przeglądu, ale nie jest ładowany do aktywnej konfiguracji ani poświadczeń OpenClaw. Zachowuje to nieprzezroczysty lub niebezpieczny stan bez udawania, że OpenClaw może go automatycznie wykonać lub mu zaufać:

  * `plugins/`
  * `sessions/`
  * `logs/`
  * `cron/`
  * `mcp-tokens/`
  * `auth.json`
  * `state.db`


### Po zastosowaniu

bashCopy code
[code]
    openclaw doctor
[/code]

## Kontrakt Plugin

Źródła migracji są Plugin. Plugin deklaruje swoje identyfikatory dostawców w `openclaw.plugin.json`:

jsonCopy code
[code]
    {  "contracts": {    "migrationProviders": ["hermes"]  }}
[/code]

W czasie działania Plugin wywołuje `api.registerMigrationProvider(...)`. Dostawca implementuje `detect`, `plan` i `apply`. Core odpowiada za orkiestrację CLI, zasady tworzenia kopii zapasowych, monity, dane wyjściowe JSON i wstępną kontrolę konfliktów. Core przekazuje sprawdzony plan do `apply(ctx, plan)`, a dostawcy mogą przebudować plan tylko wtedy, gdy ten argument jest nieobecny ze względów kompatybilności.

Plugin dostawcy mogą używać `openclaw/plugin-sdk/migration` do tworzenia elementów i zliczania podsumowań oraz `openclaw/plugin-sdk/migration-runtime` do świadomego konfliktów kopiowania plików, kopiowania raportów wyłącznie do archiwum, buforowanych wrapperów środowiska uruchomieniowego konfiguracji i raportów migracji.

## Integracja z onboardingiem

Onboarding może zaoferować migrację, gdy dostawca wykryje znane źródło. Zarówno `openclaw onboard --flow import`, jak i `openclaw setup --wizard --import-from hermes` używają tego samego dostawcy migracji Plugin i nadal pokazują podgląd przed zastosowaniem.

## Powiązane

  * [Migracja z Hermes](</pl/install/migrating-hermes>): przewodnik dla użytkownika.
  * [Migracja z Claude](</pl/install/migrating-claude>): przewodnik dla użytkownika.
  * [Migracja](</pl/install/migrating>): przeniesienie OpenClaw na nową maszynę.
  * [Doctor](</pl/gateway/doctor>): kontrola kondycji po zastosowaniu migracji.
  * [Plugins](</pl/tools/plugin>): instalacja i rejestracja Plugin.


Was this useful?YesNo