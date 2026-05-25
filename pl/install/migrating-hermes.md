---
title: Migracja z Hermes
source_url: https://docs.openclaw.ai/pl/install/migrating-hermes
scraped_at: 2026-05-25
---

OpenClaw importuje stan Hermes przez dołączonego dostawcę migracji. Dostawca wyświetla podgląd wszystkiego przed zmianą stanu, redaguje sekrety w planach i raportach oraz tworzy zweryfikowaną kopię zapasową przed zastosowaniem.

## Dwa sposoby importu

### Kreator wdrożenia

Najszybsza ścieżka. Kreator wykrywa Hermes w `~/.hermes` i pokazuje podgląd przed zastosowaniem.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

Albo wskaż konkretne źródło:

bashCopy code
[code]
    openclaw onboard --import-from hermes --import-source ~/.hermes
[/code]

### CLI

Użyj `openclaw migrate` do uruchomień skryptowych lub powtarzalnych. Pełną dokumentację znajdziesz w [`openclaw migrate`](</pl/cli/migrate>).

bashCopy code
[code]
    openclaw migrate hermes --dry-run    # preview onlyopenclaw migrate apply hermes --yes  # apply with confirmation skipped
[/code]

Dodaj `--from <path>`, gdy Hermes znajduje się poza `~/.hermes`.

## Co jest importowane

Konfiguracja modelu

  * Domyślny wybór modelu z Hermes `config.yaml`.
  * Skonfigurowani dostawcy modeli oraz niestandardowe punkty końcowe zgodne z OpenAI z `providers` i `custom_providers`.

Serwery MCP

Definicje serwerów MCP z `mcp_servers` lub `mcp.servers`.

Pliki obszaru roboczego

  * `SOUL.md` i `AGENTS.md` są kopiowane do obszaru roboczego agenta OpenClaw.
  * `memories/MEMORY.md` i `memories/USER.md` są **dopisywane** do odpowiadających im plików pamięci OpenClaw zamiast je nadpisywać.

Konfiguracja pamięci

Domyślne ustawienia konfiguracji pamięci dla pamięci plikowej OpenClaw. Zewnętrzni dostawcy pamięci, tacy jak Honcho, są zapisywani jako elementy archiwalne lub do ręcznego przeglądu, aby można było przenieść je świadomie.

Skills

Skills z plikiem `SKILL.md` w `skills/<name>/` są kopiowane wraz z wartościami konfiguracji poszczególnych Skills z `skills.config`.

Klucze API (opcjonalnie)

Ustaw `--include-secrets`, aby zaimportować obsługiwane klucze `.env`: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `OPENROUTER_API_KEY`, `GOOGLE_API_KEY`, `GEMINI_API_KEY`, `GROQ_API_KEY`, `XAI_API_KEY`, `MISTRAL_API_KEY`, `DEEPSEEK_API_KEY`. Bez tej flagi sekrety nigdy nie są kopiowane.

## Co pozostaje tylko w archiwum

Dostawca kopiuje te elementy do katalogu raportu migracji do ręcznego przeglądu, ale **nie** ładuje ich do aktywnej konfiguracji ani poświadczeń OpenClaw:

  * `plugins/`
  * `sessions/`
  * `logs/`
  * `cron/`
  * `mcp-tokens/`
  * `auth.json`
  * `state.db`


OpenClaw odmawia automatycznego wykonywania lub uznania tego stanu za zaufany, ponieważ formaty i założenia zaufania mogą różnić się między systemami. Po sprawdzeniu archiwum przenieś ręcznie to, czego potrzebujesz.

## Zalecany przepływ

* ### Wyświetl podgląd planu

bashCopy code
[code]
    openclaw migrate hermes --dry-run
[/code]

Plan zawiera wszystko, co zostanie zmienione, w tym konflikty, pominięte elementy i wszelkie elementy wrażliwe. Dane wyjściowe planu redagują zagnieżdżone klucze wyglądające jak sekrety.

* ### Zastosuj z kopią zapasową

bashCopy code
[code]
    openclaw migrate apply hermes --yes
[/code]

OpenClaw tworzy i weryfikuje kopię zapasową przed zastosowaniem. Jeśli potrzebujesz zaimportować klucze API, dodaj `--include-secrets`.

* ### Uruchom doctor

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</pl/gateway/doctor>) ponownie stosuje wszystkie oczekujące migracje konfiguracji i sprawdza problemy wprowadzone podczas importu.

* ### Uruchom ponownie i zweryfikuj

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

Potwierdź, że Gateway działa poprawnie, a zaimportowany model, pamięć i Skills są załadowane.

## Obsługa konfliktów

Zastosowanie odmawia kontynuowania, gdy plan zgłasza konflikty (plik lub wartość konfiguracji już istnieje w miejscu docelowym).

W świeżej instalacji OpenClaw konflikty są nietypowe. Zazwyczaj pojawiają się po ponownym uruchomieniu importu w konfiguracji, która ma już zmiany użytkownika.

Jeśli konflikt pojawi się w trakcie zastosowania (na przykład nieoczekiwany wyścig na pliku konfiguracji), Hermes oznacza pozostałe zależne elementy konfiguracji jako `skipped` z powodem `blocked by earlier apply conflict` zamiast zapisywać je częściowo. Raport migracji zapisuje każdy zablokowany element, aby można było rozwiązać pierwotny konflikt i ponownie uruchomić import.

## Sekrety

Sekrety nigdy nie są importowane domyślnie.

  * Najpierw uruchom `openclaw migrate apply hermes --yes`, aby zaimportować stan bez sekretów.
  * Jeśli chcesz też skopiować obsługiwane klucze `.env`, uruchom ponownie z `--include-secrets`.
  * W przypadku poświadczeń zarządzanych przez SecretRef skonfiguruj źródło SecretRef po zakończeniu importu.


## Dane wyjściowe JSON do automatyzacji

bashCopy code
[code]
    openclaw migrate hermes --dry-run --jsonopenclaw migrate apply hermes --json --yes
[/code]

Z `--json` i bez `--yes` zastosowanie wypisuje plan i nie modyfikuje stanu. To najbezpieczniejszy tryb dla CI i współdzielonych skryptów.

## Rozwiązywanie problemów

Zastosowanie odmawia z powodu konfliktów

Sprawdź dane wyjściowe planu. Każdy konflikt wskazuje ścieżkę źródłową i istniejące miejsce docelowe. Zdecyduj dla każdego elementu, czy go pominąć, edytować miejsce docelowe, czy uruchomić ponownie z `--overwrite`.

Hermes znajduje się poza ~/.hermes

Przekaż `--from /actual/path` (CLI) albo `--import-source /actual/path` (wdrożenie).

Wdrożenie odmawia importu w istniejącej konfiguracji

Importy wdrożeniowe wymagają świeżej konfiguracji. Zresetuj stan i uruchom wdrożenie ponownie albo użyj bezpośrednio `openclaw migrate apply hermes`, które obsługuje `--overwrite` i jawną kontrolę kopii zapasowej.

Klucze API nie zostały zaimportowane

Wymagane jest `--include-secrets`, a rozpoznawane są tylko klucze wymienione powyżej. Inne zmienne w `.env` są ignorowane.

## Powiązane

  * [`openclaw migrate`](</pl/cli/migrate>): pełna dokumentacja CLI, kontrakt Plugin i kształty JSON.
  * [Wdrożenie](</pl/cli/onboard>): przepływ kreatora i flagi nieinteraktywne.
  * [Migracja](</pl/install/migrating>): przenoszenie instalacji OpenClaw między maszynami.
  * [Doctor](</pl/gateway/doctor>): kontrola kondycji po migracji.
  * [Obszar roboczy agenta](</pl/concepts/agent-workspace>): miejsce, w którym znajdują się `SOUL.md`, `AGENTS.md` i pliki pamięci.


Was this useful?YesNo