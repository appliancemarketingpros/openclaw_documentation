---
title: Agenci
source_url: https://docs.openclaw.ai/pl/cli/agents
scraped_at: 2026-05-25
---

# `openclaw agents`

Zarządzaj izolowanymi agentami (obszary robocze + uwierzytelnianie + routing).

Powiązane:

  * [Routing wieloagentowy](</pl/concepts/multi-agent>)
  * [Obszar roboczy agenta](</pl/concepts/agent-workspace>)
  * [Konfiguracja Skills](</pl/tools/skills-config>): konfiguracja widoczności skills.


## Przykłady

bashCopy code
[code]
    openclaw agents listopenclaw agents list --bindingsopenclaw agents add work --workspace ~/.openclaw/workspace-workopenclaw agents add ops --workspace ~/.openclaw/workspace-ops --bind telegram:ops --non-interactiveopenclaw agents bindingsopenclaw agents bind --agent work --bind telegram:opsopenclaw agents unbind --agent work --bind telegram:opsopenclaw agents set-identity --workspace ~/.openclaw/workspace --from-identityopenclaw agents set-identity --agent main --avatar avatars/openclaw.pngopenclaw agents delete work
[/code]

## Powiązania routingu

Użyj powiązań routingu, aby przypiąć przychodzący ruch z kanału do konkretnego agenta.

Jeśli chcesz także ustawić różne widoczne skills dla poszczególnych agentów, skonfiguruj `agents.defaults.skills` i `agents.list[].skills` w `openclaw.json`. Zobacz [Konfiguracja Skills](</pl/tools/skills-config>) i [Dokumentacja konfiguracji](</pl/gateway/config-agents#agents-defaults-skills>).

Wyświetlanie powiązań:

bashCopy code
[code]
    openclaw agents bindingsopenclaw agents bindings --agent workopenclaw agents bindings --json
[/code]

Dodawanie powiązań:

bashCopy code
[code]
    openclaw agents bind --agent work --bind telegram:ops --bind discord:guild-a
[/code]

Jeśli pominiesz `accountId` (`--bind <channel>`), OpenClaw rozwiąże je z domyślnych ustawień kanału i haków konfiguracji Plugin, gdy są dostępne.

Jeśli pominiesz `--agent` dla `bind` lub `unbind`, OpenClaw wybierze bieżącego domyślnego agenta.

### Zachowanie zakresu powiązań

  * Powiązanie bez `accountId` pasuje tylko do domyślnego konta kanału.
  * `accountId: "*"` to kanałowa wartość rezerwowa (wszystkie konta) i jest mniej szczegółowa niż jawne powiązanie konta.
  * Jeśli ten sam agent ma już pasujące powiązanie kanału bez `accountId`, a później dodasz powiązanie z jawnym lub rozwiązanym `accountId`, OpenClaw zaktualizuje istniejące powiązanie w miejscu zamiast dodawać duplikat.


Przykład:

bashCopy code
[code]
    # initial channel-only bindingopenclaw agents bind --agent work --bind telegram # later upgrade to account-scoped bindingopenclaw agents bind --agent work --bind telegram:ops
[/code]

Po aktualizacji routing dla tego powiązania jest ograniczony do `telegram:ops`. Jeśli chcesz także routing dla konta domyślnego, dodaj go jawnie (na przykład `--bind telegram:default`).

Usuwanie powiązań:

bashCopy code
[code]
    openclaw agents unbind --agent work --bind telegram:opsopenclaw agents unbind --agent work --all
[/code]

`unbind` akceptuje albo `--all`, albo jedną lub więcej wartości `--bind`, ale nie oba naraz.

## Powierzchnia poleceń

### `agents`

Uruchomienie `openclaw agents` bez podpolecenia jest równoważne z `openclaw agents list`.

### `agents list`

Opcje:

  * `--json`
  * `--bindings`: uwzględnia pełne reguły routingu, nie tylko liczby/podsumowania dla poszczególnych agentów


### `agents add [name]`

Opcje:

  * `--workspace <dir>`
  * `--model <id>`
  * `--agent-dir <dir>`
  * `--bind <channel[:accountId]>` (można powtarzać)
  * `--non-interactive`
  * `--json`


Uwagi:

  * Przekazanie dowolnych jawnych flag dodawania przełącza polecenie na ścieżkę nieinteraktywną.
  * Tryb nieinteraktywny wymaga zarówno nazwy agenta, jak i `--workspace`.
  * `main` jest zarezerwowane i nie może zostać użyte jako identyfikator nowego agenta.
  * W trybie interaktywnym zasiewanie uwierzytelniania kopiuje tylko przenośne profile statyczne (`api_key` i statyczny `token` domyślnie). Profile OAuth z tokenem odświeżania pozostają dostępne tylko przez dziedziczenie z odczytem z rzeczywistego magazynu agenta `main`. Jeśli skonfigurowany domyślny agent nie jest `main`, zaloguj się osobno dla profili OAuth na nowym agencie.


### `agents bindings`

Opcje:

  * `--agent <id>`
  * `--json`


### `agents bind`

Opcje:

  * `--agent <id>` (domyślnie bieżący domyślny agent)
  * `--bind <channel[:accountId]>` (można powtarzać)
  * `--json`


### `agents unbind`

Opcje:

  * `--agent <id>` (domyślnie bieżący domyślny agent)
  * `--bind <channel[:accountId]>` (można powtarzać)
  * `--all`
  * `--json`


### `agents delete <id>`

Opcje:

  * `--force`
  * `--json`


Uwagi:

  * `main` nie może zostać usunięte.
  * Bez `--force` wymagane jest interaktywne potwierdzenie.
  * Katalogi obszaru roboczego, stanu agenta i transkryptów sesji są przenoszone do Kosza, a nie trwale usuwane.
  * Gdy Gateway jest osiągalny, usunięcie jest wysyłane przez Gateway, aby czyszczenie konfiguracji i magazynu sesji współdzieliło ten sam mechanizm zapisu co ruch runtime. Jeśli Gateway jest nieosiągalny, CLI wraca do ścieżki lokalnej offline.
  * Jeśli obszar roboczy innego agenta jest tą samą ścieżką, znajduje się wewnątrz tego obszaru roboczego albo zawiera ten obszar roboczy, obszar roboczy jest zachowywany, a `--json` raportuje `workspaceRetained`, `workspaceRetainedReason` i `workspaceSharedWith`.


## Pliki tożsamości

Każdy obszar roboczy agenta może zawierać `IDENTITY.md` w katalogu głównym obszaru roboczego:

  * Przykładowa ścieżka: `~/.openclaw/workspace/IDENTITY.md`
  * `set-identity --from-identity` odczytuje z katalogu głównego obszaru roboczego (lub z jawnego `--identity-file`)


Ścieżki awatarów są rozwiązywane względem katalogu głównego obszaru roboczego.

## Ustawianie tożsamości

`set-identity` zapisuje pola w `agents.list[].identity`:

  * `name`
  * `theme`
  * `emoji`
  * `avatar` (ścieżka względna wobec obszaru roboczego, URL http(s) albo identyfikator URI danych)


Opcje:

  * `--agent <id>`
  * `--workspace <dir>`
  * `--identity-file <path>`
  * `--from-identity`
  * `--name <name>`
  * `--theme <theme>`
  * `--emoji <emoji>`
  * `--avatar <value>`
  * `--json`


Uwagi:

  * `--agent` lub `--workspace` można użyć do wybrania docelowego agenta.
  * Jeśli polegasz na `--workspace`, a wielu agentów współdzieli ten obszar roboczy, polecenie kończy się niepowodzeniem i prosi o przekazanie `--agent`.
  * Gdy nie podano jawnych pól tożsamości, polecenie odczytuje dane tożsamości z `IDENTITY.md`.


Wczytywanie z `IDENTITY.md`:

bashCopy code
[code]
    openclaw agents set-identity --workspace ~/.openclaw/workspace --from-identity
[/code]

Jawne nadpisanie pól:

bashCopy code
[code]
    openclaw agents set-identity --agent main --name "OpenClaw" --emoji "🦞" --avatar avatars/openclaw.png
[/code]

Przykład konfiguracji:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "main",        identity: {          name: "OpenClaw",          theme: "space lobster",          emoji: "🦞",          avatar: "avatars/openclaw.png",        },      },    ],  },}
[/code]

## Powiązane

  * [Dokumentacja CLI](</pl/cli>)
  * [Routing wieloagentowy](</pl/concepts/multi-agent>)
  * [Obszar roboczy agenta](</pl/concepts/agent-workspace>)


Was this useful?YesNo