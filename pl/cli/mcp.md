---
title: MCP
source_url: https://docs.openclaw.ai/pl/cli/mcp
scraped_at: 2026-05-25
---

`openclaw mcp` ma dwa zadania:

  * uruchamiać OpenClaw jako serwer MCP za pomocą `openclaw mcp serve`
  * zarządzać należącymi do OpenClaw definicjami wychodzących serwerów MCP za pomocą `list`, `show`, `set` i `unset`


Innymi słowy:

  * `serve` to OpenClaw działający jako serwer MCP
  * `list` / `show` / `set` / `unset` to OpenClaw działający jako rejestr po stronie klienta MCP dla innych serwerów MCP, z których jego runtime'y mogą korzystać później


Użyj [`openclaw acp`](</pl/cli/acp>), gdy OpenClaw ma sam hostować sesję uprzęży kodowania i kierować ten runtime przez ACP.

## OpenClaw jako serwer MCP

To jest ścieżka `openclaw mcp serve`.

### Kiedy używać `serve`

Użyj `openclaw mcp serve`, gdy:

  * Codex, Claude Code lub inny klient MCP ma komunikować się bezpośrednio z konwersacjami kanałów obsługiwanymi przez OpenClaw
  * masz już lokalny lub zdalny OpenClaw Gateway z routowanymi sesjami
  * chcesz jednego serwera MCP, który działa z backendami kanałów OpenClaw, zamiast uruchamiać osobne mosty dla każdego kanału


Użyj zamiast tego [`openclaw acp`](</pl/cli/acp>), gdy OpenClaw ma hostować sam runtime kodowania i utrzymywać sesję agenta wewnątrz OpenClaw.

### Jak to działa

`openclaw mcp serve` uruchamia serwer MCP stdio. Klient MCP jest właścicielem tego procesu. Dopóki klient utrzymuje otwartą sesję stdio, most łączy się z lokalnym lub zdalnym OpenClaw Gateway przez WebSocket i udostępnia routowane konwersacje kanałów przez MCP.

* ### Klient uruchamia most

Klient MCP uruchamia `openclaw mcp serve`.

* ### Most łączy się z Gateway

Most łączy się z OpenClaw Gateway przez WebSocket.

* ### Sesje stają się konwersacjami MCP

Routowane sesje stają się konwersacjami MCP oraz narzędziami transkrypcji/historii.

* ### Kolejka zdarzeń na żywo

Zdarzenia na żywo są kolejkowane w pamięci, gdy most jest połączony.

* ### Opcjonalne wypychanie Claude

Jeśli tryb kanału Claude jest włączony, ta sama sesja może też odbierać powiadomienia push specyficzne dla Claude.

Ważne zachowanie

  * stan kolejki na żywo zaczyna się, gdy most się łączy
  * starsza historia transkrypcji jest odczytywana za pomocą `messages_read`
  * powiadomienia push Claude istnieją tylko wtedy, gdy sesja MCP jest aktywna
  * gdy klient się rozłączy, most kończy działanie, a kolejka na żywo znika
  * jednorazowe punkty wejścia agenta, takie jak `openclaw agent` i `openclaw infer model run`, zamykają wszystkie dołączone runtime'y MCP, które otworzą, po ukończeniu odpowiedzi, więc powtarzane uruchomienia skryptowe nie gromadzą procesów potomnych stdio MCP
  * serwery MCP stdio uruchamiane przez OpenClaw (dołączone lub skonfigurowane przez użytkownika) są zamykane jako drzewo procesów przy wyłączaniu, więc podprocesy potomne uruchomione przez serwer nie przetrwają po zakończeniu nadrzędnego klienta stdio
  * usunięcie lub zresetowanie sesji usuwa klientów MCP tej sesji przez współdzieloną ścieżkę czyszczenia runtime'u, więc nie pozostają żadne wiszące połączenia stdio powiązane z usuniętą sesją


### Wybierz tryb klienta

Używaj tego samego mostu na dwa różne sposoby:

### Ogólni klienci MCP

Tylko standardowe narzędzia MCP. Używaj `conversations_list`, `messages_read`, `events_poll`, `events_wait`, `messages_send` oraz narzędzi zatwierdzania.

### Claude Code

Standardowe narzędzia MCP plus adapter kanału specyficzny dla Claude. Włącz `--claude-channel-mode on` albo pozostaw domyślne `auto`.

### Co udostępnia `serve`

Most używa istniejących metadanych tras sesji Gateway, aby udostępniać konwersacje oparte na kanałach. Konwersacja pojawia się, gdy OpenClaw ma już stan sesji ze znaną trasą, taką jak:

  * `channel`
  * metadane odbiorcy lub miejsca docelowego
  * opcjonalne `accountId`
  * opcjonalne `threadId`


Daje to klientom MCP jedno miejsce do tego, aby:

  * wyświetlać ostatnie routowane konwersacje
  * odczytywać ostatnią historię transkrypcji
  * czekać na nowe zdarzenia przychodzące
  * wysyłać odpowiedź tą samą trasą
  * widzieć żądania zatwierdzenia, które docierają, gdy most jest połączony


### Użycie

### Lokalny Gateway

bashCopy code
[code]
    openclaw mcp serve
[/code]

### Zdalny Gateway (token)

bashCopy code
[code]
    openclaw mcp serve --url wss://gateway-host:18789 --token-file ~/.openclaw/gateway.token
[/code]

### Zdalny Gateway (hasło)

bashCopy code
[code]
    openclaw mcp serve --url wss://gateway-host:18789 --password-file ~/.openclaw/gateway.password
[/code]

### Szczegółowo / Claude wyłączony

bashCopy code
[code]
    openclaw mcp serve --verboseopenclaw mcp serve --claude-channel-mode off
[/code]

### Narzędzia mostu

Obecny most udostępnia te narzędzia MCP:

conversations_list

Wyświetla ostatnie konwersacje oparte na sesjach, które mają już metadane trasy w stanie sesji Gateway.

Przydatne filtry:

  * `limit`
  * `search`
  * `channel`
  * `includeDerivedTitles`
  * `includeLastMessage`

conversation_get

Zwraca jedną konwersację według `session_key` przy użyciu bezpośredniego wyszukiwania sesji Gateway.

messages_read

Odczytuje ostatnie wiadomości transkrypcji dla jednej konwersacji opartej na sesji.

attachments_fetch

Wyodrębnia nietekstowe bloki zawartości wiadomości z jednej wiadomości transkrypcji. To widok metadanych na zawartość transkrypcji, a nie samodzielny trwały magazyn blobów załączników.

events_poll

Odczytuje kolejkowane zdarzenia na żywo od kursora numerycznego.

events_wait

Używa długiego odpytywania, aż nadejdzie następne pasujące kolejkowane zdarzenie albo upłynie limit czasu.

Użyj tego, gdy ogólny klient MCP potrzebuje dostarczania prawie w czasie rzeczywistym bez protokołu push specyficznego dla Claude.

messages_send

Wysyła tekst z powrotem tą samą trasą, która jest już zapisana w sesji.

Obecne zachowanie:

  * wymaga istniejącej trasy konwersacji
  * używa kanału sesji, odbiorcy, identyfikatora konta i identyfikatora wątku
  * wysyła tylko tekst

permissions_list_open

Wyświetla oczekujące żądania zatwierdzenia exec/Plugin, które most zaobserwował od momentu połączenia z Gateway.

permissions_respond

Rozwiązuje jedno oczekujące żądanie zatwierdzenia exec/Plugin za pomocą:

  * `allow-once`
  * `allow-always`
  * `deny`


### Model zdarzeń

Most utrzymuje kolejkę zdarzeń w pamięci, gdy jest połączony.

Obecne typy zdarzeń:

  * `message`
  * `exec_approval_requested`
  * `exec_approval_resolved`
  * `plugin_approval_requested`
  * `plugin_approval_resolved`
  * `claude_permission_request`


### Powiadomienia kanału Claude

Most może też udostępniać powiadomienia kanału specyficzne dla Claude. To odpowiednik adaptera kanału Claude Code w OpenClaw: standardowe narzędzia MCP pozostają dostępne, ale wiadomości przychodzące na żywo mogą też przychodzić jako powiadomienia MCP specyficzne dla Claude.

### off

`--claude-channel-mode off`: tylko standardowe narzędzia MCP.

### on

`--claude-channel-mode on`: włącza powiadomienia kanału Claude.

### auto (domyślnie)

`--claude-channel-mode auto`: obecna wartość domyślna; takie samo zachowanie mostu jak `on`.

Gdy tryb kanału Claude jest włączony, serwer ogłasza eksperymentalne możliwości Claude i może emitować:

  * `notifications/claude/channel`
  * `notifications/claude/channel/permission`


Obecne zachowanie mostu:

  * przychodzące wiadomości transkrypcji `user` są przekazywane jako `notifications/claude/channel`
  * żądania uprawnień Claude odebrane przez MCP są śledzone w pamięci
  * jeśli powiązana konwersacja wyśle później `yes abcde` lub `no abcde`, most konwertuje to na `notifications/claude/channel/permission`
  * te powiadomienia istnieją tylko w sesji na żywo; jeśli klient MCP się rozłączy, nie ma celu push


Jest to celowo specyficzne dla klienta. Ogólni klienci MCP powinni polegać na standardowych narzędziach odpytywania.

### Konfiguracja klienta MCP

Przykładowa konfiguracja klienta stdio:

jsonCopy code
[code]
    {  "mcpServers": {    "openclaw": {      "command": "openclaw",      "args": [        "mcp",        "serve",        "--url",        "wss://gateway-host:18789",        "--token-file",        "/path/to/gateway.token"      ]    }  }}
[/code]

W przypadku większości ogólnych klientów MCP zacznij od standardowej powierzchni narzędzi i ignoruj tryb Claude. Włącz tryb Claude tylko dla klientów, którzy faktycznie rozumieją metody powiadomień specyficzne dla Claude.

### Opcje

`openclaw mcp serve` obsługuje:

URL WebSocket Gateway.

Token Gateway.

Odczytaj token z pliku.

Hasło Gateway.

Odczytaj hasło z pliku.

Tryb powiadomień Claude.

Szczegółowe logi na stderr.

### Bezpieczeństwo i granica zaufania

Most nie wymyśla routingu. Udostępnia tylko konwersacje, które Gateway już umie routować.

Oznacza to, że:

  * listy dozwolonych nadawców, parowanie i zaufanie na poziomie kanału nadal należą do bazowej konfiguracji kanału OpenClaw
  * `messages_send` może odpowiadać tylko przez istniejącą zapisaną trasę
  * stan zatwierdzeń jest tylko na żywo/w pamięci dla bieżącej sesji mostu
  * uwierzytelnianie mostu powinno używać tych samych mechanizmów tokenu lub hasła Gateway, którym ufałbyś w przypadku każdego innego zdalnego klienta Gateway


Jeśli konwersacji brakuje w `conversations_list`, zwykłą przyczyną nie jest konfiguracja MCP. Są nią brakujące lub niepełne metadane trasy w bazowej sesji Gateway.

### Testowanie

OpenClaw dostarcza deterministyczny smoke test Docker dla tego mostu:

bashCopy code
[code]
    pnpm test:docker:mcp-channels
[/code]

Ten smoke test:

  * uruchamia wstępnie zasilony kontener Gateway
  * uruchamia drugi kontener, który startuje `openclaw mcp serve`
  * weryfikuje wykrywanie konwersacji, odczyty transkrypcji, odczyty metadanych załączników, zachowanie kolejki zdarzeń na żywo i routing wysyłania wychodzącego
  * waliduje powiadomienia kanału i uprawnień w stylu Claude przez rzeczywisty most MCP stdio


To najszybszy sposób, aby udowodnić, że most działa bez podłączania prawdziwego konta Telegram, Discord ani iMessage do przebiegu testowego.

Szerszy kontekst testowania znajdziesz w [Testowanie](</pl/help/testing>).

### Rozwiązywanie problemów

Nie zwrócono żadnych konwersacji

Zwykle oznacza to, że sesja Gateway nie jest jeszcze routowalna. Potwierdź, że bazowa sesja ma zapisane metadane trasy kanału/dostawcy, odbiorcy oraz opcjonalnie konta/wątku.

events_poll lub events_wait pomija starsze wiadomości

Oczekiwane. Kolejka na żywo zaczyna się, gdy most się łączy. Odczytaj starszą historię transkrypcji za pomocą `messages_read`.

Powiadomienia Claude się nie pojawiają

Sprawdź wszystkie poniższe elementy:

  * klient utrzymał otwartą sesję MCP stdio
  * `--claude-channel-mode` ma wartość `on` lub `auto`
  * klient faktycznie rozumie metody powiadomień specyficzne dla Claude
  * wiadomość przychodząca nastąpiła po połączeniu mostu

Brakuje zatwierdzeń

`permissions_list_open` pokazuje tylko żądania zatwierdzenia zaobserwowane, gdy most był połączony. Nie jest to API trwałej historii zatwierdzeń.

## OpenClaw jako rejestr klientów MCP

To jest ścieżka `openclaw mcp list`, `show`, `set` i `unset`.

Te polecenia nie udostępniają OpenClaw przez MCP. Zarządzają definicjami serwerów MCP należącymi do OpenClaw w `mcp.servers` w konfiguracji OpenClaw.

Te zapisane definicje są przeznaczone dla środowisk uruchomieniowych, które OpenClaw uruchamia lub konfiguruje później, takich jak osadzony Pi i inne adaptery środowisk uruchomieniowych. OpenClaw przechowuje definicje centralnie, aby te środowiska uruchomieniowe nie musiały utrzymywać własnych zduplikowanych list serwerów MCP.

Ważne zachowanie

  * te polecenia tylko odczytują lub zapisują konfigurację OpenClaw
  * nie łączą się z docelowym serwerem MCP
  * nie sprawdzają, czy polecenie, URL lub zdalny transport jest w tej chwili osiągalny
  * adaptery środowiska uruchomieniowego decydują w czasie wykonania, które kształty transportu faktycznie obsługują
  * osadzony Pi udostępnia skonfigurowane narzędzia MCP w zwykłych profilach narzędzi `coding` i `messaging`; `minimal` nadal je ukrywa, a `tools.deny: ["bundle-mcp"]` jawnie je wyłącza
  * pakietowe środowiska uruchomieniowe MCP o zakresie sesji są usuwane po `mcp.sessionIdleTtlMs` milisekundach bezczynności (domyślnie 10 minut; ustaw `0`, aby wyłączyć), a jednorazowe osadzone uruchomienia czyszczą je po zakończeniu działania


Adaptery środowiska uruchomieniowego mogą normalizować ten współdzielony rejestr do kształtu oczekiwanego przez ich klienta podrzędnego. Na przykład osadzony Pi używa wartości `transport` OpenClaw bezpośrednio, podczas gdy Claude Code i Gemini otrzymują natywne dla CLI wartości `type`, takie jak `http`, `sse` lub `stdio`.

### Zapisane definicje serwerów MCP

OpenClaw przechowuje też lekki rejestr serwerów MCP w konfiguracji dla powierzchni, które chcą definicji MCP zarządzanych przez OpenClaw.

Polecenia:

  * `openclaw mcp list`
  * `openclaw mcp show [name]`
  * `openclaw mcp set <name> <json>`
  * `openclaw mcp unset <name>`


Uwagi:

  * `list` sortuje nazwy serwerów.
  * `show` bez nazwy wypisuje pełny skonfigurowany obiekt serwera MCP.
  * `set` oczekuje jednej wartości obiektu JSON w wierszu poleceń.
  * Użyj `transport: "streamable-http"` dla serwerów MCP Streamable HTTP. `openclaw mcp set` normalizuje też natywne dla CLI `type: "http"` do tego samego kanonicznego kształtu konfiguracji w celu zgodności.
  * `unset` kończy się niepowodzeniem, jeśli nazwany serwer nie istnieje.


Przykłady:

bashCopy code
[code]
    openclaw mcp listopenclaw mcp show context7 --jsonopenclaw mcp set context7 '{"command":"uvx","args":["context7-mcp"]}'openclaw mcp set docs '{"url":"https://mcp.example.com","transport":"streamable-http"}'openclaw mcp unset context7
[/code]

Przykładowy kształt konfiguracji:

jsonCopy code
[code]
    {  "mcp": {    "servers": {      "context7": {        "command": "uvx",        "args": ["context7-mcp"]      },      "docs": {        "url": "https://mcp.example.com",        "transport": "streamable-http"      }    }  }}
[/code]

### Transport stdio

Uruchamia lokalny proces potomny i komunikuje się przez stdin/stdout.

Pole | Opis  
---|---  
`command` | Plik wykonywalny do uruchomienia (wymagane)  
`args` | Tablica argumentów wiersza poleceń  
`env` | Dodatkowe zmienne środowiskowe  
`cwd` / `workingDirectory` | Katalog roboczy procesu  
  
### Transport SSE / HTTP

Łączy się ze zdalnym serwerem MCP przez HTTP Server-Sent Events.

Pole | Opis  
---|---  
`url` | URL HTTP lub HTTPS zdalnego serwera (wymagane)  
`headers` | Opcjonalna mapa klucz-wartość nagłówków HTTP (na przykład tokeny uwierzytelniania)  
`connectionTimeoutMs` | Limit czasu połączenia dla serwera w ms (opcjonalne)  
  
Przykład:

jsonCopy code
[code]
    {  "mcp": {    "servers": {      "remote-tools": {        "url": "https://mcp.example.com",        "headers": {          "Authorization": "Bearer <token>"        }      }    }  }}
[/code]

Wartości wrażliwe w `url` (userinfo) i `headers` są redagowane w logach i danych statusu.

### Transport Streamable HTTP

`streamable-http` to dodatkowa opcja transportu obok `sse` i `stdio`. Używa strumieniowania HTTP do dwukierunkowej komunikacji ze zdalnymi serwerami MCP.

Pole | Opis  
---|---  
`url` | URL HTTP lub HTTPS zdalnego serwera (wymagane)  
`transport` | Ustaw na `"streamable-http"`, aby wybrać ten transport; gdy pominięte, OpenClaw używa `sse`  
`headers` | Opcjonalna mapa klucz-wartość nagłówków HTTP (na przykład tokeny uwierzytelniania)  
`connectionTimeoutMs` | Limit czasu połączenia dla serwera w ms (opcjonalne)  
  
Konfiguracja OpenClaw używa `transport: "streamable-http"` jako kanonicznej pisowni. Natywne dla CLI wartości MCP `type: "http"` są akceptowane przy zapisie przez `openclaw mcp set` i naprawiane przez `openclaw doctor --fix` w istniejącej konfiguracji, ale `transport` jest tym, czego osadzony Pi używa bezpośrednio.

Przykład:

jsonCopy code
[code]
    {  "mcp": {    "servers": {      "streaming-tools": {        "url": "https://mcp.example.com/stream",        "transport": "streamable-http",        "connectionTimeoutMs": 10000,        "headers": {          "Authorization": "Bearer <token>"        }      }    }  }}
[/code]

## Obecne ograniczenia

Ta strona dokumentuje most w postaci dostarczanej obecnie.

Obecne ograniczenia:

  * odnajdywanie konwersacji zależy od istniejących metadanych trasy sesji Gateway
  * brak ogólnego protokołu push poza adapterem specyficznym dla Claude
  * nie ma jeszcze narzędzi edycji wiadomości ani reakcji
  * transport HTTP/SSE/streamable-http łączy się z jednym zdalnym serwerem; nie ma jeszcze multipleksowanego upstreamu
  * `permissions_list_open` obejmuje tylko zatwierdzenia zaobserwowane, gdy most jest połączony


## Powiązane

  * [Dokumentacja CLI](</pl/cli>)
  * [Plugins](</pl/cli/plugins>)


Was this useful?YesNo