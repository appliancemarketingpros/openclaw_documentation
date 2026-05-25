---
title: Pakiety Plugin
source_url: https://docs.openclaw.ai/pl/plugins/bundles
scraped_at: 2026-05-25
---

OpenClaw może instalować pluginy z trzech zewnętrznych ekosystemów: **Codex** , **Claude** i **Cursor**. Nazywa się je **pakietami** — pakietami treści i metadanych, które OpenClaw mapuje na natywne funkcje, takie jak Skills, hooki i narzędzia MCP.

## Dlaczego istnieją pakiety

Wiele użytecznych pluginów jest publikowanych w formacie Codex, Claude lub Cursor. Zamiast wymagać od autorów przepisywania ich jako natywnych pluginów OpenClaw, OpenClaw wykrywa te formaty i mapuje ich obsługiwaną treść na natywny zestaw funkcji. Oznacza to, że możesz zainstalować pakiet poleceń Claude lub pakiet Skills Codex i używać go od razu.

## Instalowanie pakietu

* ### Zainstaluj z katalogu, archiwum lub marketplace

bashCopy code
[code]
    # Katalog lokalnyopenclaw plugins install ./my-bundle # Archiwumopenclaw plugins install ./my-bundle.tgz # Marketplace Claudeopenclaw plugins marketplace list <marketplace-name>openclaw plugins install <plugin-name>@<marketplace-name>
[/code]

* ### Zweryfikuj wykrywanie

bashCopy code
[code]
    openclaw plugins listopenclaw plugins inspect <id>
[/code]

Pakiety są wyświetlane jako `Format: bundle` z podtypem `codex`, `claude` lub `cursor`.

* ### Uruchom ponownie i używaj

bashCopy code
[code]
    openclaw gateway restart
[/code]

Zmapowane funkcje (Skills, hooki, narzędzia MCP, domyślne ustawienia LSP) są dostępne w następnej sesji.

## Co OpenClaw mapuje z pakietów

Nie każda funkcja pakietu działa dziś w OpenClaw. Oto co działa oraz co jest wykrywane, ale nie zostało jeszcze podłączone.

### Obsługiwane teraz

Funkcja | Jak jest mapowana | Dotyczy  
---|---|---  
Treść Skills | Korzenie Skills pakietu ładują się jak zwykłe Skills OpenClaw | Wszystkie formaty  
Polecenia | `commands/` i `.cursor/commands/` są traktowane jako korzenie Skills | Claude, Cursor  
Pakiety hooków | Układy w stylu OpenClaw: `HOOK.md` \+ `handler.ts` | Codex  
Narzędzia MCP | Konfiguracja MCP pakietu scalana z osadzonymi ustawieniami Pi; ładowane są obsługiwane serwery stdio i HTTP | Wszystkie formaty  
Serwery LSP | Claude `.lsp.json` i zadeklarowane w manifeście `lspServers` scalane z domyślnymi ustawieniami LSP osadzonego Pi | Claude  
Ustawienia | Claude `settings.json` importowany jako domyślne ustawienia osadzonego Pi | Claude  
  
#### Treść Skills

  * korzenie Skills pakietu ładują się jak zwykłe korzenie Skills OpenClaw
  * korzenie Claude `commands` są traktowane jako dodatkowe korzenie Skills
  * korzenie Cursor `.cursor/commands` są traktowane jako dodatkowe korzenie Skills


Oznacza to, że markdownowe pliki poleceń Claude działają przez zwykły loader Skills OpenClaw. Markdown poleceń Cursor działa tą samą ścieżką.

#### Pakiety hooków

  * korzenie hooków pakietu działają **tylko** wtedy, gdy używają zwykłego układu pakietu hooków OpenClaw. Dziś jest to przede wszystkim przypadek zgodny z Codex: 
    * `HOOK.md`
    * `handler.ts` lub `handler.js`


#### MCP dla Pi

  * włączone pakiety mogą dostarczać konfigurację serwerów MCP
  * OpenClaw scala konfigurację MCP pakietu z efektywnymi ustawieniami osadzonego Pi jako `mcpServers`
  * OpenClaw udostępnia obsługiwane narzędzia MCP pakietu podczas tur osadzonego agenta Pi przez uruchamianie serwerów stdio lub łączenie się z serwerami HTTP
  * profile narzędzi `coding` i `messaging` domyślnie obejmują narzędzia MCP pakietów; użyj `tools.deny: ["bundle-mcp"]`, aby zrezygnować dla agenta lub Gateway
  * lokalne ustawienia Pi projektu nadal obowiązują po domyślnych ustawieniach pakietu, więc ustawienia workspace mogą w razie potrzeby nadpisać wpisy MCP pakietu
  * katalogi narzędzi MCP pakietów są sortowane deterministycznie przed rejestracją, więc zmiany kolejności `listTools()` po stronie upstream nie powodują ciągłych zmian bloków narzędzi cache promptów


##### Transporty

Serwery MCP mogą używać transportu stdio lub HTTP:

**Stdio** uruchamia proces potomny:

jsonCopy code
[code]
    {  "mcp": {    "servers": {      "my-server": {        "command": "node",        "args": ["server.js"],        "env": { "PORT": "3000" }      }    }  }}
[/code]

**HTTP** domyślnie łączy się z działającym serwerem MCP przez `sse` albo przez `streamable-http`, gdy zostanie to zażądane:

jsonCopy code
[code]
    {  "mcp": {    "servers": {      "my-server": {        "url": "http://localhost:3100/mcp",        "transport": "streamable-http",        "headers": {          "Authorization": "Bearer ${MY_SECRET_TOKEN}"        },        "connectionTimeoutMs": 30000      }    }  }}
[/code]

  * `transport` może być ustawione na `"streamable-http"` lub `"sse"`; gdy zostanie pominięte, OpenClaw używa `sse`
  * `type: "http"` to natywny dla CLI kształt downstream; użyj `transport: "streamable-http"` w konfiguracji OpenClaw. `openclaw mcp set` i `openclaw doctor --fix` normalizują typowy alias.
  * dozwolone są tylko schematy URL `http:` i `https:`
  * wartości `headers` obsługują interpolację `${ENV_VAR}`
  * wpis serwera zawierający jednocześnie `command` i `url` jest odrzucany
  * dane uwierzytelniające URL (userinfo i parametry zapytania) są redagowane z opisów narzędzi i logów
  * `connectionTimeoutMs` nadpisuje domyślny 30-sekundowy limit czasu połączenia dla transportów stdio i HTTP


##### Nazewnictwo narzędzi

OpenClaw rejestruje narzędzia MCP pakietów z nazwami bezpiecznymi dla dostawcy w formie `serverName__toolName`. Na przykład serwer z kluczem `"vigil-harbor"` udostępniający narzędzie `memory_search` rejestruje się jako `vigil-harbor__memory_search`.

  * znaki spoza `A-Za-z0-9_-` są zastępowane znakiem `-`
  * fragmenty, które zaczynałyby się od znaku innego niż litera, dostają prefiks literowy, więc numeryczne klucze serwerów, takie jak `12306`, stają się bezpiecznymi dla dostawcy prefiksami narzędzi
  * prefiksy serwerów są ograniczone do 30 znaków
  * pełne nazwy narzędzi są ograniczone do 64 znaków
  * puste nazwy serwerów wracają do `mcp`
  * kolidujące nazwy po sanityzacji są rozróżniane sufiksami liczbowymi
  * ostateczna kolejność udostępnianych narzędzi jest deterministyczna według bezpiecznej nazwy, aby powtarzane tury Pi były stabilne dla cache
  * filtrowanie profili traktuje wszystkie narzędzia z jednego serwera MCP pakietu jako należące do pluginu `bundle-mcp`, więc allowlisty i listy odmów profilu mogą zawierać pojedyncze udostępnione nazwy narzędzi albo klucz pluginu `bundle-mcp`


#### Ustawienia osadzonego Pi

  * Claude `settings.json` jest importowany jako domyślne ustawienia osadzonego Pi, gdy pakiet jest włączony
  * OpenClaw sanityzuje klucze nadpisania shella przed ich zastosowaniem


Sanityzowane klucze:

  * `shellPath`
  * `shellCommandPrefix`


#### Osadzone LSP Pi

  * włączone pakiety Claude mogą dostarczać konfigurację serwerów LSP
  * OpenClaw ładuje `.lsp.json` oraz wszystkie ścieżki `lspServers` zadeklarowane w manifeście
  * konfiguracja LSP pakietu jest scalana z efektywnymi domyślnymi ustawieniami LSP osadzonego Pi
  * dziś uruchamialne są tylko obsługiwane serwery LSP oparte na stdio; nieobsługiwane transporty nadal pojawiają się w `openclaw plugins inspect <id>`


### Wykrywane, ale niewykonywane

Są rozpoznawane i pokazywane w diagnostyce, ale OpenClaw ich nie uruchamia:

  * Claude `agents`, automatyzacja `hooks.json`, `outputStyles`
  * Cursor `.cursor/agents`, `.cursor/hooks.json`, `.cursor/rules`
  * metadane inline/aplikacji Codex poza raportowaniem możliwości


## Formaty pakietów

Pakiety Codex

Znaczniki: `.codex-plugin/plugin.json`

Opcjonalna treść: `skills/`, `hooks/`, `.mcp.json`, `.app.json`

Pakiety Codex najlepiej pasują do OpenClaw, gdy używają korzeni Skills i katalogów pakietów hooków w stylu OpenClaw (`HOOK.md` \+ `handler.ts`).

Pakiety Claude

Dwa tryby wykrywania:

  * **Oparte na manifeście:** `.claude-plugin/plugin.json`
  * **Bez manifestu:** domyślny układ Claude (`skills/`, `commands/`, `agents/`, `hooks/`, `.mcp.json`, `.lsp.json`, `settings.json`)


Zachowanie specyficzne dla Claude:

  * `commands/` jest traktowane jako treść Skills
  * `settings.json` jest importowany do ustawień osadzonego Pi (klucze nadpisania shella są sanityzowane)
  * `.mcp.json` udostępnia obsługiwane narzędzia stdio osadzonemu Pi
  * `.lsp.json` oraz ścieżki `lspServers` zadeklarowane w manifeście ładują się do domyślnych ustawień LSP osadzonego Pi
  * `hooks/hooks.json` jest wykrywane, ale niewykonywane
  * niestandardowe ścieżki komponentów w manifeście są addytywne (rozszerzają wartości domyślne, nie zastępują ich)

Pakiety Cursor

Znaczniki: `.cursor-plugin/plugin.json`

Opcjonalna treść: `skills/`, `.cursor/commands/`, `.cursor/agents/`, `.cursor/rules/`, `.cursor/hooks.json`, `.mcp.json`

  * `.cursor/commands/` jest traktowane jako treść Skills
  * `.cursor/rules/`, `.cursor/agents/` i `.cursor/hooks.json` są tylko wykrywane


## Pierwszeństwo wykrywania

OpenClaw najpierw sprawdza natywny format pluginu:

  1. `openclaw.plugin.json` lub prawidłowy `package.json` z `openclaw.extensions` — traktowane jako **natywny plugin**
  2. Znaczniki pakietu (`.codex-plugin/`, `.claude-plugin/` lub domyślny układ Claude/Cursor) — traktowane jako **pakiet**


Jeśli katalog zawiera oba, OpenClaw używa ścieżki natywnej. Zapobiega to częściowemu instalowaniu pakietów w podwójnym formacie jako pakietów.

## Zależności runtime i czyszczenie

  * Zgodne pakiety firm trzecich nie otrzymują naprawy startupowej `npm install`. Powinny być instalowane przez `openclaw plugins install` i dostarczać wszystko, czego potrzebują, w zainstalowanym katalogu pluginu.
  * Pakietowe pluginy należące do OpenClaw są albo dostarczane lekko w core, albo pobierane przez instalator pluginów. Startup Gateway nigdy nie uruchamia dla nich menedżera pakietów.
  * `openclaw doctor --fix` usuwa starsze katalogi staged dependency i może odzyskać pobieralne pluginy, których brakuje w lokalnym indeksie pluginów, gdy odwołuje się do nich konfiguracja.


## Bezpieczeństwo

Pakiety mają węższą granicę zaufania niż natywne pluginy:

  * OpenClaw **nie** ładuje dowolnych modułów runtime pakietu w procesie
  * ścieżki Skills i pakietów hooków muszą pozostawać wewnątrz katalogu głównego pluginu (sprawdzana jest granica)
  * pliki ustawień są czytane z tymi samymi kontrolami granicy
  * obsługiwane serwery MCP stdio mogą być uruchamiane jako podprocesy


Dzięki temu pakiety są domyślnie bezpieczniejsze, ale nadal należy traktować pakiety firm trzecich jako zaufaną treść dla funkcji, które udostępniają.

## Rozwiązywanie problemów

Pakiet jest wykrywany, ale możliwości nie działają

Uruchom `openclaw plugins inspect <id>`. Jeśli możliwość jest wymieniona, ale oznaczona jako niepodłączona, to ograniczenie produktu — nie uszkodzona instalacja.

Pliki poleceń Claude nie pojawiają się

Upewnij się, że pakiet jest włączony, a pliki markdown znajdują się w wykrytym korzeniu `commands/` lub `skills/`.

Ustawienia Claude nie są stosowane

Obsługiwane są tylko ustawienia osadzonego Pi z `settings.json`. OpenClaw nie traktuje ustawień pakietu jako surowych łatek konfiguracji.

Hooki Claude się nie wykonują

`hooks/hooks.json` jest tylko wykrywane. Jeśli potrzebujesz uruchamialnych hooków, użyj układu pakietu hooków OpenClaw albo dostarcz natywny plugin.

## Powiązane

  * [Instalowanie i konfigurowanie pluginów](</pl/tools/plugin>)
  * [Tworzenie pluginów](</pl/plugins/building-plugins>) — utwórz natywny plugin
  * [Manifest pluginu](</pl/plugins/manifest>) — natywny schemat manifestu


Was this useful?YesNo