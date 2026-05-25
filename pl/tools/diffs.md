---
title: Różnice
source_url: https://docs.openclaw.ai/pl/tools/diffs
scraped_at: 2026-05-25
---

`diffs` to opcjonalne narzędzie Plugin z krótkimi wbudowanymi wskazówkami systemowymi i towarzyszącą mu umiejętnością, która przekształca treść zmian w artefakt diff tylko do odczytu dla agentów.

Przyjmuje albo:

  * tekst `before` i `after`
  * zunifikowany `patch`


Może zwrócić:

  * adres URL przeglądarki gateway do prezentacji na canvas
  * ścieżkę wyrenderowanego pliku (PNG lub PDF) do dostarczenia w wiadomości
  * oba wyniki w jednym wywołaniu


Po włączeniu Plugin dodaje zwięzłe wskazówki użycia do przestrzeni promptu systemowego, a także udostępnia szczegółową umiejętność dla przypadków, gdy agent potrzebuje pełniejszych instrukcji.

## Szybki start

* ### Zainstaluj Plugin

bashCopy code
[code]
    openclaw plugins install diffs
[/code]

* ### Włącz Plugin

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,      },    },  },}
[/code]

* ### Wybierz tryb

### view

Przepływy z canvas na pierwszym planie: agenci wywołują `diffs` z `mode: "view"` i otwierają `details.viewerUrl` za pomocą `canvas present`.

### file

Dostarczanie pliku na czacie: agenci wywołują `diffs` z `mode: "file"` i wysyłają `details.filePath` za pomocą `message`, używając `path` lub `filePath`.

### both

Tryb łączony: agenci wywołują `diffs` z `mode: "both"`, aby uzyskać oba artefakty w jednym wywołaniu.

## Wyłącz wbudowane wskazówki systemowe

Jeśli chcesz zachować włączone narzędzie `diffs`, ale wyłączyć jego wbudowane wskazówki promptu systemowego, ustaw `plugins.entries.diffs.hooks.allowPromptInjection` na `false`:

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        hooks: {          allowPromptInjection: false,        },      },    },  },}
[/code]

Blokuje to hook `before_prompt_build` pluginu diffs, pozostawiając dostępne Plugin, narzędzie i towarzyszącą umiejętność.

Jeśli chcesz wyłączyć zarówno wskazówki, jak i narzędzie, wyłącz zamiast tego Plugin.

## Typowy przepływ pracy agenta

* ### Wywołaj diffs

Agent wywołuje narzędzie `diffs` z danymi wejściowymi.

* ### Odczytaj details

Agent odczytuje pola `details` z odpowiedzi.

* ### Zaprezentuj

Agent otwiera `details.viewerUrl` za pomocą `canvas present`, wysyła `details.filePath` za pomocą `message`, używając `path` lub `filePath`, albo robi jedno i drugie.

## Przykłady danych wejściowych

### Przed i po

jsonCopy code
[code]
    {  "before": "# Hello\n\nOne",  "after": "# Hello\n\nTwo",  "path": "docs/example.md",  "mode": "view"}
[/code]

### Patch

jsonCopy code
[code]
    {  "patch": "diff --git a/src/example.ts b/src/example.ts\n--- a/src/example.ts\n+++ b/src/example.ts\n@@ -1 +1 @@\n-const x = 1;\n+const x = 2;\n",  "mode": "both"}
[/code]

## Referencja danych wejściowych narzędzia

Wszystkie pola są opcjonalne, chyba że zaznaczono inaczej.

Tekst oryginalny. Wymagany z `after`, gdy pominięto `patch`.

Zaktualizowany tekst. Wymagany z `before`, gdy pominięto `patch`.

Tekst zunifikowanego diff. Wzajemnie wyklucza się z `before` i `after`.

Wyświetlana nazwa pliku dla trybu przed i po.

Wskazówka nadpisania języka dla trybu przed i po. Nieznane wartości wracają do zwykłego tekstu.

Nadpisanie tytułu przeglądarki.

Tryb wyjścia. Domyślnie używa wartości domyślnej Plugin `defaults.mode`. Przestarzały alias: `"image"` działa jak `"file"` i nadal jest akceptowany dla zgodności wstecznej.

Motyw przeglądarki. Domyślnie używa wartości domyślnej Plugin `defaults.theme`.

Układ diff. Domyślnie używa wartości domyślnej Plugin `defaults.layout`.

Rozwiń niezmienione sekcje, gdy dostępny jest pełny kontekst. Tylko opcja dla pojedynczego wywołania (nie jest domyślnym kluczem Plugin).

Format wyrenderowanego pliku. Domyślnie używa wartości domyślnej Plugin `defaults.fileFormat`.

Preset jakości dla renderowania PNG lub PDF.

Nadpisanie skali urządzenia (`1`-`4`).

Maksymalna szerokość renderowania w pikselach CSS (`640`-`2400`).

TTL artefaktu w sekundach dla wyników przeglądarki i samodzielnego pliku. Maks. 21600.

Nadpisanie pochodzenia adresu URL przeglądarki. Nadpisuje `viewerBaseUrl` Plugin. Musi być `http` lub `https`, bez query/hash.

Starsze aliasy danych wejściowych

Nadal akceptowane dla zgodności wstecznej:

  * `format` -> `fileFormat`
  * `imageFormat` -> `fileFormat`
  * `imageQuality` -> `fileQuality`
  * `imageScale` -> `fileScale`
  * `imageMaxWidth` -> `fileMaxWidth`

Walidacja i limity

  * `before` i `after` mają maks. po 512 KiB.
  * `patch` maks. 2 MiB.
  * `path` maks. 2048 bajtów.
  * `lang` maks. 128 bajtów.
  * `title` maks. 1024 bajty.
  * Limit złożoności patcha: maks. 128 plików i 120000 łącznych wierszy.
  * `patch` razem z `before` lub `after` jest odrzucany.
  * Limity bezpieczeństwa wyrenderowanego pliku (dotyczą PNG i PDF): 
    * `fileQuality: "standard"`: maks. 8 MP (8 000 000 wyrenderowanych pikseli).
    * `fileQuality: "hq"`: maks. 14 MP (14 000 000 wyrenderowanych pikseli).
    * `fileQuality: "print"`: maks. 24 MP (24 000 000 wyrenderowanych pikseli).
    * PDF ma także maksimum 50 stron.


## Kontrakt szczegółów wyjściowych

Narzędzie zwraca ustrukturyzowane metadane w `details`.

Pola przeglądarki

Wspólne pola dla trybów, które tworzą przeglądarkę:

  * `artifactId`
  * `viewerUrl`
  * `viewerPath`
  * `title`
  * `expiresAt`
  * `inputKind`
  * `fileCount`
  * `mode`
  * `context` (`agentId`, `sessionId`, `messageChannel`, `agentAccountId`, gdy dostępne)

Pola pliku

Pola pliku, gdy renderowany jest PNG lub PDF:

  * `artifactId`
  * `expiresAt`
  * `filePath`
  * `path` (ta sama wartość co `filePath`, dla zgodności z narzędziem wiadomości)
  * `fileBytes`
  * `fileFormat`
  * `fileQuality`
  * `fileScale`
  * `fileMaxWidth`

Aliasy zgodności

Zwracane także dla istniejących wywołujących:

  * `format` (ta sama wartość co `fileFormat`)
  * `imagePath` (ta sama wartość co `filePath`)
  * `imageBytes` (ta sama wartość co `fileBytes`)
  * `imageQuality` (ta sama wartość co `fileQuality`)
  * `imageScale` (ta sama wartość co `fileScale`)
  * `imageMaxWidth` (ta sama wartość co `fileMaxWidth`)


Podsumowanie działania trybów:

Tryb | Co jest zwracane  
---|---  
`"view"` | Tylko pola przeglądarki.  
`"file"` | Tylko pola pliku, bez artefaktu przeglądarki.  
`"both"` | Pola przeglądarki plus pola pliku. Jeśli renderowanie pliku się nie powiedzie, przeglądarka nadal zwraca wynik z aliasem `fileError` i `imageError`.  
  
## Zwinięte niezmienione sekcje

  * Przeglądarka może pokazywać wiersze takie jak `N unmodified lines`.
  * Kontrolki rozwijania w tych wierszach są warunkowe i nie są gwarantowane dla każdego rodzaju danych wejściowych.
  * Kontrolki rozwijania pojawiają się, gdy wyrenderowany diff ma dane kontekstu możliwe do rozwinięcia, co jest typowe dla danych wejściowych przed i po.
  * Dla wielu zunifikowanych danych wejściowych patcha pominięte treści kontekstu nie są dostępne w sparsowanych hunkach patcha, więc wiersz może pojawić się bez kontrolek rozwijania. To oczekiwane zachowanie.
  * `expandUnchanged` ma zastosowanie tylko wtedy, gdy istnieje kontekst możliwy do rozwinięcia.


## Wartości domyślne Plugin

Ustaw wartości domyślne dla całego Plugin w `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          defaults: {            fontFamily: "Fira Code",            fontSize: 15,            lineSpacing: 1.6,            layout: "unified",            showLineNumbers: true,            diffIndicators: "bars",            wordWrap: true,            background: true,            theme: "dark",            fileFormat: "png",            fileQuality: "standard",            fileScale: 2,            fileMaxWidth: 960,            mode: "both",            ttlSeconds: 21600,          },        },      },    },  },}
[/code]

Obsługiwane wartości domyślne:

  * `fontFamily`
  * `fontSize`
  * `lineSpacing`
  * `layout`
  * `showLineNumbers`
  * `diffIndicators`
  * `wordWrap`
  * `background`
  * `theme`
  * `fileFormat`
  * `fileQuality`
  * `fileScale`
  * `fileMaxWidth`
  * `mode`
  * `ttlSeconds`


Jawne parametry narzędzia nadpisują te wartości domyślne.

### Trwała konfiguracja adresu URL przeglądarki

Rezerwowa wartość należąca do Plugin dla zwracanych linków przeglądarki, gdy wywołanie narzędzia nie przekazuje `baseUrl`. Musi być `http` lub `https`, bez query/hash.

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          viewerBaseUrl: "https://gateway.example.com/openclaw",        },      },    },  },}
[/code]

## Konfiguracja bezpieczeństwa

`false`: żądania inne niż loopback do tras przeglądarki są odrzucane. `true`: zdalne przeglądarki są dozwolone, jeśli tokenizowana ścieżka jest prawidłowa.

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          security: {            allowRemoteViewer: false,          },        },      },    },  },}
[/code]

## Cykl życia artefaktu i przechowywanie

  * Artefakty są przechowywane w podfolderze tymczasowym: `$TMPDIR/openclaw-diffs`.
  * Metadane artefaktu przeglądarki zawierają: 
    * losowy identyfikator artefaktu (20 znaków szesnastkowych)
    * losowy token (48 znaków szesnastkowych)
    * `createdAt` i `expiresAt`
    * zapisaną ścieżkę `viewer.html`
  * Domyślny TTL artefaktu wynosi 30 minut, gdy nie podano inaczej.
  * Maksymalny akceptowany TTL przeglądarki wynosi 6 godzin.
  * Czyszczenie uruchamia się oportunistycznie po utworzeniu artefaktu.
  * Wygasłe artefakty są usuwane.
  * Czyszczenie rezerwowe usuwa nieaktualne foldery starsze niż 24 godziny, gdy brakuje metadanych.


## Adres URL przeglądarki i zachowanie sieciowe

Trasa przeglądarki:

  * `/plugins/diffs/view/{artifactId}/{token}`


Zasoby przeglądarki:

  * `/plugins/diffs/assets/viewer.js`
  * `/plugins/diffs/assets/viewer-runtime.js`


Dokument przeglądarki rozwiązuje te zasoby względem adresu URL przeglądarki, więc opcjonalny prefiks ścieżki `baseUrl` jest zachowywany także dla obu żądań zasobów.

Zachowanie konstrukcji adresu URL:

  * Jeśli podano `baseUrl` wywołania narzędzia, jest używane po ścisłej walidacji.
  * W przeciwnym razie, jeśli skonfigurowano `viewerBaseUrl` Plugin, jest używane.
  * Bez żadnego z tych nadpisań adres URL przeglądarki domyślnie używa loopback `127.0.0.1`.
  * Jeśli tryb bindowania gateway to `custom` i ustawiono `gateway.customBindHost`, używany jest ten host.


Reguły `baseUrl`:

  * Musi być `http://` lub `https://`.
  * Query i hash są odrzucane.
  * Dozwolone jest pochodzenie plus opcjonalna ścieżka bazowa.


## Model bezpieczeństwa

Wzmocnienie bezpieczeństwa przeglądarki

  * Domyślnie tylko loopback.
  * Tokenizowane ścieżki przeglądarki ze ścisłą walidacją identyfikatora i tokenu.
  * CSP odpowiedzi przeglądarki: 
    * `default-src 'none'`
    * skrypty i zasoby tylko z tego samego źródła
    * brak wychodzącego `connect-src`
  * Ograniczanie zdalnych nietrafień, gdy dostęp zdalny jest włączony: 
    * 40 niepowodzeń na 60 sekund
    * 60-sekundowa blokada (`429 Too Many Requests`)

Wzmocnienie bezpieczeństwa renderowania plików

  * Trasowanie żądań przeglądarki zrzutów ekranu domyślnie odmawia dostępu.
  * Dozwolone są tylko lokalne zasoby przeglądarki z `http://127.0.0.1/plugins/diffs/assets/*`.
  * Zewnętrzne żądania sieciowe są blokowane.


## Wymagania przeglądarki dla trybu pliku

`mode: "file"` i `mode: "both"` wymagają przeglądarki zgodnej z Chromium.

Kolejność rozwiązywania:

* ### Konfiguracja

`browser.executablePath` w konfiguracji OpenClaw.

* ### Zmienne środowiskowe

  * `OPENCLAW_BROWSER_EXECUTABLE_PATH`
  * `BROWSER_EXECUTABLE_PATH`
  * `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH`


* ### Zapasowy mechanizm platformy

Zapasowe wykrywanie polecenia/ścieżki platformy.

Typowy tekst błędu:

  * `Diff PNG/PDF rendering requires a Chromium-compatible browser...`


Napraw to, instalując Chrome, Chromium, Edge lub Brave albo ustawiając jedną z powyższych opcji ścieżki do pliku wykonywalnego.

## Rozwiązywanie problemów

Błędy walidacji danych wejściowych

  * `Provide patch or both before and after text.` — podaj zarówno `before`, jak i `after`, albo podaj `patch`.
  * `Provide either patch or before/after input, not both.` — nie mieszaj trybów wejścia.
  * `Invalid baseUrl: ...` — użyj źródła `http(s)` z opcjonalną ścieżką, bez zapytania/fragmentu.
  * `{field} exceeds maximum size (...)` — zmniejsz rozmiar ładunku.
  * Odrzucenie dużej poprawki — zmniejsz liczbę plików poprawki lub łączną liczbę wierszy.

Dostępność przeglądarki

  * URL przeglądarki domyślnie rozwiązuje się do `127.0.0.1`.
  * W scenariuszach dostępu zdalnego: 
    * ustaw `viewerBaseUrl` pluginu, albo
    * przekaż `baseUrl` dla każdego wywołania narzędzia, albo
    * użyj `gateway.bind=custom` i `gateway.customBindHost`
  * Jeśli `gateway.trustedProxies` obejmuje loopback dla proxy na tym samym hoście (na przykład Tailscale Serve), surowe żądania przeglądarki przez loopback bez przekazanych nagłówków IP klienta są z założenia zamykane niepowodzeniem.
  * Dla tej topologii proxy: 
    * preferuj `mode: "file"` albo `mode: "both"`, gdy potrzebujesz tylko załącznika, albo
    * celowo włącz `security.allowRemoteViewer` i ustaw `viewerBaseUrl` pluginu albo przekaż proxy/publiczne `baseUrl`, gdy potrzebujesz udostępnialnego URL-a przeglądarki
  * Włącz `security.allowRemoteViewer` tylko wtedy, gdy zamierzasz udostępnić zewnętrzny dostęp do przeglądarki.

Wiersz niezmodyfikowanych linii nie ma przycisku rozwijania

Może się to zdarzyć dla wejścia poprawki, gdy poprawka nie zawiera rozwijalnego kontekstu. Jest to oczekiwane i nie oznacza awarii przeglądarki.

Nie znaleziono artefaktu

  * Artefakt wygasł z powodu TTL.
  * Token lub ścieżka się zmieniły.
  * Czyszczenie usunęło nieaktualne dane.


## Wskazówki operacyjne

  * Preferuj `mode: "view"` do lokalnych interaktywnych przeglądów w kanwie.
  * Preferuj `mode: "file"` dla wychodzących kanałów czatu, które potrzebują załącznika.
  * Pozostaw `allowRemoteViewer` wyłączone, chyba że Twoje wdrożenie wymaga zdalnych URL-i przeglądarki.
  * Ustaw jawne krótkie `ttlSeconds` dla wrażliwych różnic.
  * Unikaj wysyłania sekretów w wejściu różnic, gdy nie jest to wymagane.
  * Jeśli Twój kanał agresywnie kompresuje obrazy (na przykład Telegram lub WhatsApp), preferuj wyjście PDF (`fileFormat: "pdf"`).


## Powiązane

  * [Przeglądarka](</pl/tools/browser>)
  * [Pluginy](</pl/tools/plugin>)
  * [Przegląd narzędzi](</pl/tools>)


Was this useful?YesNo