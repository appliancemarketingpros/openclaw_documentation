---
title: Domyślny AGENTS.md
source_url: https://docs.openclaw.ai/pl/reference/AGENTS.default
scraped_at: 2026-05-25
---

## Pierwsze uruchomienie (zalecane)

OpenClaw używa dedykowanego katalogu obszaru roboczego dla agenta. Domyślnie: `~/.openclaw/workspace` (konfigurowalne przez `agents.defaults.workspace`).

  1. Utwórz obszar roboczy (jeśli jeszcze nie istnieje):

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace
[/code]

  2. Skopiuj domyślne szablony obszaru roboczego do obszaru roboczego:

bashCopy code
[code]
    cp docs/reference/templates/AGENTS.md ~/.openclaw/workspace/AGENTS.mdcp docs/reference/templates/SOUL.md ~/.openclaw/workspace/SOUL.mdcp docs/reference/templates/TOOLS.md ~/.openclaw/workspace/TOOLS.md
[/code]

  3. Opcjonalnie: jeśli chcesz listę Skills osobistego asystenta, zastąp [AGENTS.md](<http://AGENTS.md>) tym plikiem:

bashCopy code
[code]
    cp docs/reference/AGENTS.default.md ~/.openclaw/workspace/AGENTS.md
[/code]

  4. Opcjonalnie: wybierz inny obszar roboczy, ustawiając `agents.defaults.workspace` (obsługuje `~`):

json5Copy code
[code]
    {  agents: { defaults: { workspace: "~/.openclaw/workspace" } },}
[/code]

## Domyślne ustawienia bezpieczeństwa

  * Nie zrzucaj katalogów ani sekretów na czat.
  * Nie uruchamiaj destrukcyjnych poleceń, chyba że wyraźnie o to poproszono.
  * Nie wysyłaj częściowych/strumieniowych odpowiedzi do zewnętrznych powierzchni komunikacji (tylko odpowiedzi końcowe).


## Start sesji (wymagane)

  * Przeczytaj `SOUL.md`, `USER.md` oraz dzisiejszy i wczorajszy wpis w `memory/`.
  * Przeczytaj `MEMORY.md`, gdy jest obecny.
  * Zrób to przed odpowiedzią.


## Dusza (wymagane)

  * `SOUL.md` definiuje tożsamość, ton i granice. Utrzymuj go w aktualnym stanie.
  * Jeśli zmienisz `SOUL.md`, poinformuj użytkownika.
  * W każdej sesji jesteś świeżą instancją; ciągłość znajduje się w tych plikach.


## Przestrzenie współdzielone (zalecane)

  * Nie jesteś głosem użytkownika; zachowaj ostrożność w czatach grupowych lub kanałach publicznych.
  * Nie udostępniaj prywatnych danych, danych kontaktowych ani wewnętrznych notatek.


## System pamięci (zalecane)

  * Dzienny dziennik: `memory/YYYY-MM-DD.md` (w razie potrzeby utwórz `memory/`).
  * Pamięć długoterminowa: `MEMORY.md` dla trwałych faktów, preferencji i decyzji.
  * Małe `memory.md` to tylko starsze wejście naprawcze; nie utrzymuj celowo obu plików głównych.
  * Przy starcie sesji przeczytaj dzisiejszy + wczorajszy wpis + `MEMORY.md`, gdy jest obecny.
  * Zapisuj: decyzje, preferencje, ograniczenia, otwarte wątki.
  * Unikaj sekretów, chyba że wyraźnie o to poproszono.


## Narzędzia i Skills

  * Narzędzia znajdują się w Skills; gdy ich potrzebujesz, postępuj zgodnie z `SKILL.md` każdej umiejętności.
  * Notatki specyficzne dla środowiska przechowuj w `TOOLS.md` (Notatki dla Skills).


## Wskazówka dotycząca kopii zapasowej (zalecane)

Jeśli traktujesz ten obszar roboczy jako „pamięć” Clawd, uczyń go repozytorium git (najlepiej prywatnym), aby `AGENTS.md` i pliki pamięci były zabezpieczone kopią zapasową.

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.mdgit commit -m "Add Clawd workspace"# Optional: add a private remote + push
[/code]

## Co robi OpenClaw

  * Uruchamia WhatsApp Gateway + agenta kodującego Pi, aby asystent mógł odczytywać/zapisywać czaty, pobierać kontekst i uruchamiać Skills przez hosta Mac.
  * Aplikacja macOS zarządza uprawnieniami (nagrywanie ekranu, powiadomienia, mikrofon) i udostępnia CLI `openclaw` przez dołączony plik binarny.
  * Czaty bezpośrednie domyślnie zwijają się do sesji `main` agenta; grupy pozostają izolowane jako `agent:<agentId>:<channel>:group:<id>` (pokoje/kanały: `agent:<agentId>:<channel>:channel:<id>`); sygnały Heartbeat utrzymują zadania w tle przy życiu.


## Podstawowe Skills (włącz w Ustawienia → Skills)

  * **mcporter** \- Środowisko uruchomieniowe/CLI serwera narzędzi do zarządzania zewnętrznymi backendami Skills.
  * **Peekaboo** \- Szybkie zrzuty ekranu macOS z opcjonalną analizą wizyjną AI.
  * **camsnap** \- Przechwytuj klatki, klipy lub alerty ruchu z kamer bezpieczeństwa RTSP/ONVIF.
  * **oracle** \- Gotowy na OpenAI agent CLI z odtwarzaniem sesji i sterowaniem przeglądarką.
  * **eightctl** \- Steruj swoim snem z terminala.
  * **imsg** \- Wysyłaj, czytaj i strumieniuj iMessage oraz SMS.
  * **wacli** \- WhatsApp CLI: synchronizacja, wyszukiwanie, wysyłanie.
  * **discord** \- Akcje Discord: reakcje, naklejki, ankiety. Używaj celów `user:<id>` lub `channel:<id>` (same identyfikatory numeryczne są niejednoznaczne).
  * **gog** \- Google Suite CLI: Gmail, Calendar, Drive, Contacts.
  * **spotify-player** \- Terminalowy klient Spotify do wyszukiwania/kolejkowania/sterowania odtwarzaniem.
  * **sag** \- Mowa ElevenLabs z UX w stylu macOS `say`; domyślnie strumieniuje do głośników.
  * **Sonos CLI** \- Steruj głośnikami Sonos (wykrywanie/status/odtwarzanie/głośność/grupowanie) ze skryptów.
  * **blucli** \- Odtwarzaj, grupuj i automatyzuj odtwarzacze BluOS ze skryptów.
  * **OpenHue CLI** \- Sterowanie oświetleniem Philips Hue dla scen i automatyzacji.
  * **OpenAI Whisper** \- Lokalne rozpoznawanie mowy na tekst do szybkiego dyktowania i transkrypcji poczty głosowej.
  * **Gemini CLI** \- Modele Google Gemini z terminala do szybkich pytań i odpowiedzi.
  * **agent-tools** \- Zestaw narzędzi pomocniczych do automatyzacji i skryptów pomocniczych.


## Uwagi dotyczące użycia

  * Do skryptów preferuj CLI `openclaw`; aplikacja Mac obsługuje uprawnienia.
  * Uruchamiaj instalacje z karty Skills; przycisk jest ukrywany, jeśli plik binarny jest już obecny.
  * Pozostaw Heartbeat włączone, aby asystent mógł planować przypomnienia, monitorować skrzynki odbiorcze i wyzwalać przechwytywanie obrazu z kamer.
  * Interfejs Canvas działa pełnoekranowo z natywnymi nakładkami. Unikaj umieszczania krytycznych kontrolek przy górnej lewej/górnej prawej/dolnych krawędziach; dodaj jawne marginesy w układzie i nie polegaj na wcięciach bezpiecznego obszaru.
  * Do weryfikacji sterowanej przeglądarką użyj `openclaw browser` (karty/status/zrzut ekranu) z profilem Chrome zarządzanym przez OpenClaw.
  * Do inspekcji DOM użyj `openclaw browser eval|query|dom|snapshot` (oraz `--json`/`--out`, gdy potrzebujesz wyjścia maszynowego).
  * Do interakcji użyj `openclaw browser click|type|hover|drag|select|upload|press|wait|navigate|back|evaluate|run` (click/type wymagają odwołań do snapshot; użyj `evaluate` dla selektorów CSS).


## Powiązane

  * [Obszar roboczy agenta](</pl/concepts/agent-workspace>)
  * [Środowisko uruchomieniowe agenta](</pl/concepts/agent>)


Was this useful?YesNo