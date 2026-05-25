---
title: Migracja z Claude
source_url: https://docs.openclaw.ai/pl/install/migrating-claude
scraped_at: 2026-05-25
---

OpenClaw importuje lokalny stan Claude przez dołączonego dostawcę migracji Claude. Dostawca pokazuje podgląd każdego elementu przed zmianą stanu, redaguje sekrety w planach i raportach oraz tworzy zweryfikowaną kopię zapasową przed zastosowaniem zmian.

## Dwa sposoby importu

### Kreator wdrażania

Kreator proponuje Claude, gdy wykryje lokalny stan Claude.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

Albo wskaż konkretne źródło:

bashCopy code
[code]
    openclaw onboard --import-from claude --import-source ~/.claude
[/code]

### CLI

Użyj `openclaw migrate` do uruchomień skryptowych lub powtarzalnych. Pełny opis znajdziesz w [`openclaw migrate`](</pl/cli/migrate>).

bashCopy code
[code]
    openclaw migrate claude --dry-runopenclaw migrate apply claude --yes
[/code]

Dodaj `--from <path>`, aby zaimportować konkretny katalog domowy Claude Code lub katalog główny projektu.

## Co jest importowane

Instrukcje i pamięć

  * Zawartość projektu `CLAUDE.md` i `.claude/CLAUDE.md` jest kopiowana lub dołączana do `AGENTS.md` w przestrzeni roboczej agenta OpenClaw.
  * Zawartość użytkownika `~/.claude/CLAUDE.md` jest dołączana do `USER.md` w przestrzeni roboczej.

Serwery MCP

Definicje serwerów MCP są importowane z projektu `.mcp.json`, Claude Code `~/.claude.json` oraz Claude Desktop `claude_desktop_config.json`, gdy są obecne.

Skills i polecenia

  * Claude Skills z plikiem `SKILL.md` są kopiowane do katalogu Skills przestrzeni roboczej OpenClaw.
  * Pliki Markdown poleceń Claude w `.claude/commands/` lub `~/.claude/commands/` są konwertowane na OpenClaw Skills z `disable-model-invocation: true`.


## Co pozostaje tylko w archiwum

Dostawca kopiuje te elementy do raportu migracji do ręcznego przeglądu, ale **nie** ładuje ich do aktywnej konfiguracji OpenClaw:

  * hooki Claude
  * uprawnienia Claude i szerokie listy dozwolonych narzędzi
  * domyślne wartości środowiska Claude
  * `CLAUDE.local.md`
  * `.claude/rules/`
  * podagenci Claude w `.claude/agents/` lub `~/.claude/agents/`
  * katalogi pamięci podręcznej, planów i historii projektu Claude Code
  * rozszerzenia Claude Desktop i poświadczenia przechowywane przez system operacyjny


OpenClaw odmawia automatycznego wykonywania hooków, ufania listom dozwolonych uprawnień albo dekodowania nieprzezroczystego stanu poświadczeń OAuth i Desktop. Przenieś potrzebne elementy ręcznie po sprawdzeniu archiwum.

## Wybór źródła

Bez `--from` OpenClaw sprawdza domyślny katalog domowy Claude Code w `~/.claude`, przykładowy plik stanu Claude Code `~/.claude.json` oraz konfigurację MCP Claude Desktop na macOS.

Gdy `--from` wskazuje katalog główny projektu, OpenClaw importuje tylko pliki Claude tego projektu, takie jak `CLAUDE.md`, `.claude/settings.json`, `.claude/commands/`, `.claude/skills/` i `.mcp.json`. Podczas importu z katalogu głównego projektu nie odczytuje globalnego katalogu domowego Claude.

## Zalecany przepływ

* ### Podejrzyj plan

bashCopy code
[code]
    openclaw migrate claude --dry-run
[/code]

Plan wymienia wszystko, co zostanie zmienione, w tym konflikty, pominięte elementy i wartości wrażliwe zredagowane z zagnieżdżonych pól MCP `env` lub `headers`.

* ### Zastosuj z kopią zapasową

bashCopy code
[code]
    openclaw migrate apply claude --yes
[/code]

OpenClaw tworzy i weryfikuje kopię zapasową przed zastosowaniem zmian.

* ### Uruchom doctor

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</pl/gateway/doctor>) sprawdza problemy z konfiguracją lub stanem po imporcie.

* ### Uruchom ponownie i zweryfikuj

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

Potwierdź, że gateway działa poprawnie, a zaimportowane instrukcje, serwery MCP i Skills są załadowane.

## Obsługa konfliktów

Zastosowanie zmian odmawia kontynuowania, gdy plan zgłasza konflikty (plik lub wartość konfiguracji już istnieje w miejscu docelowym).

W świeżej instalacji OpenClaw konflikty są nietypowe. Zwykle pojawiają się, gdy ponownie uruchamiasz import w konfiguracji, która ma już edycje użytkownika.

## Wynik JSON do automatyzacji

bashCopy code
[code]
    openclaw migrate claude --dry-run --jsonopenclaw migrate apply claude --json --yes
[/code]

Z `--json` i bez `--yes` zastosowanie zmian wypisuje plan i nie modyfikuje stanu. To najbezpieczniejszy tryb dla CI i współdzielonych skryptów.

## Rozwiązywanie problemów

Stan Claude znajduje się poza ~/.claude

Przekaż `--from /actual/path` (CLI) albo `--import-source /actual/path` (wdrażanie).

Wdrażanie odmawia importu w istniejącej konfiguracji

Importy podczas wdrażania wymagają świeżej konfiguracji. Zresetuj stan i ponownie przejdź wdrażanie albo użyj bezpośrednio `openclaw migrate apply claude`, które obsługuje `--overwrite` i jawną kontrolę kopii zapasowej.

Serwery MCP z Claude Desktop nie zostały zaimportowane

Claude Desktop odczytuje `claude_desktop_config.json` ze ścieżki specyficznej dla platformy. Wskaż `--from` na katalog tego pliku, jeśli OpenClaw nie wykrył go automatycznie.

Polecenia Claude stały się Skills z wyłączonym wywoływaniem modelu

Zgodnie z projektem. Polecenia Claude są uruchamiane przez użytkownika, więc OpenClaw importuje je jako Skills z `disable-model-invocation: true`. Edytuj frontmatter każdego Skill, jeśli chcesz, aby agent wywoływał je automatycznie.

## Powiązane

  * [`openclaw migrate`](</pl/cli/migrate>): pełny opis CLI, kontrakt Plugin i kształty JSON.
  * [Przewodnik po migracji](</pl/install/migrating>): wszystkie ścieżki migracji.
  * [Migracja z Hermes](</pl/install/migrating-hermes>): druga ścieżka importu między systemami.
  * [Wdrażanie](</pl/cli/onboard>): przepływ kreatora i flagi nieinteraktywne.
  * [Doctor](</pl/gateway/doctor>): kontrola kondycji po migracji.
  * [Przestrzeń robocza agenta](</pl/concepts/agent-workspace>): gdzie znajdują się `AGENTS.md`, `USER.md` i Skills.


Was this useful?YesNo