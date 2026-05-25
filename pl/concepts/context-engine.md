---
title: Silnik kontekstu
source_url: https://docs.openclaw.ai/pl/concepts/context-engine
scraped_at: 2026-05-25
---

**silnik kontekstu** kontroluje, jak OpenClaw buduje kontekst modelu dla każdego uruchomienia: które komunikaty uwzględnić, jak podsumowywać starszą historię oraz jak zarządzać kontekstem między granicami subagentów.

OpenClaw zawiera wbudowany silnik `legacy` i domyślnie go używa - większość użytkowników nigdy nie musi tego zmieniać. Zainstaluj i wybierz silnik Plugin tylko wtedy, gdy chcesz uzyskać inne zachowanie składania, Compaction lub przywoływania między sesjami.

## Szybki start

* ### Check which engine is active

bashCopy code
[code]
    openclaw doctor# or inspect config directly:cat ~/.openclaw/openclaw.json | jq '.plugins.slots.contextEngine'
[/code]

* ### Install a plugin engine

Pluginy silnika kontekstu instaluje się tak samo jak każdy inny Plugin OpenClaw.

### From npm

bashCopy code
[code]
    openclaw plugins install @martian-engineering/lossless-claw
[/code]

### From a local path

bashCopy code
[code]
    openclaw plugins install -l ./my-context-engine
[/code]

* ### Enable and select the engine

json5Copy code
[code]
    // openclaw.json{  plugins: {    slots: {      contextEngine: "lossless-claw", // must match the plugin's registered engine id    },    entries: {      "lossless-claw": {        enabled: true,        // Plugin-specific config goes here (see the plugin's docs)      },    },  },}
[/code]

Po instalacji i konfiguracji uruchom ponownie Gateway.

* ### Switch back to legacy (optional)

Ustaw `contextEngine` na `"legacy"` (albo całkowicie usuń klucz - `"legacy"` jest wartością domyślną).

## Jak to działa

Za każdym razem, gdy OpenClaw uruchamia monit modelu, silnik kontekstu uczestniczy w czterech punktach cyklu życia:

1\. Ingest

Wywoływane, gdy do sesji dodawany jest nowy komunikat. Silnik może zapisać lub zindeksować komunikat we własnym magazynie danych.

2\. Assemble

Wywoływane przed każdym uruchomieniem modelu. Silnik zwraca uporządkowany zestaw komunikatów (oraz opcjonalny `systemPromptAddition`), które mieszczą się w budżecie tokenów.

3\. Compact

Wywoływane, gdy okno kontekstu jest pełne albo gdy użytkownik uruchamia `/compact`. Silnik podsumowuje starszą historię, aby zwolnić miejsce.

4\. After turn

Wywoływane po zakończeniu uruchomienia. Silnik może utrwalić stan, uruchomić Compaction w tle lub zaktualizować indeksy.

Dla dołączonego harnessu Codex innego niż ACP OpenClaw stosuje ten sam cykl życia, projektując złożony kontekst do instrukcji deweloperskich Codex oraz monitu bieżącej tury. Codex nadal zarządza własną natywną historią wątku i natywnym kompaktorem.

### Cykl życia subagenta (opcjonalnie)

OpenClaw wywołuje dwa opcjonalne haki cyklu życia subagenta:

Przygotowuje współdzielony stan kontekstu przed rozpoczęciem uruchomienia podrzędnego. Hak otrzymuje klucze sesji nadrzędnej/podrzędnej, `contextMode` (`isolated` lub `fork`), dostępne identyfikatory/pliki transkrypcji oraz opcjonalny TTL. Jeśli zwróci uchwyt wycofania, OpenClaw wywoła go, gdy utworzenie subagenta nie powiedzie się po pomyślnym przygotowaniu.

Czyści zasoby, gdy sesja subagenta zostanie zakończona lub usunięta.

### Dodatek do monitu systemowego

Metoda `assemble` może zwrócić ciąg `systemPromptAddition`. OpenClaw poprzedza nim monit systemowy dla uruchomienia. Dzięki temu silniki mogą wstrzykiwać dynamiczne wskazówki przywoływania, instrukcje pobierania lub podpowiedzi zależne od kontekstu bez wymagania statycznych plików obszaru roboczego.

## Silnik legacy

Wbudowany silnik `legacy` zachowuje pierwotne zachowanie OpenClaw:

  * **Pobieranie** : brak operacji (menedżer sesji bezpośrednio obsługuje utrwalanie komunikatów).
  * **Składanie** : przekazanie bez zmian (istniejący potok sanitize → validate → limit w środowisku uruchomieniowym obsługuje składanie kontekstu).
  * **Compaction** : deleguje do wbudowanej Compaction podsumowującej, która tworzy pojedyncze podsumowanie starszych komunikatów i zachowuje najnowsze komunikaty bez zmian.
  * **Po turze** : brak operacji.


Silnik legacy nie rejestruje narzędzi ani nie udostępnia `systemPromptAddition`.

Gdy `plugins.slots.contextEngine` nie jest ustawione (albo jest ustawione na `"legacy"`), ten silnik jest używany automatycznie.

## Silniki Plugin

Plugin może zarejestrować silnik kontekstu za pomocą API Plugin:

tsCopy code
[code]
     export default function register(api) {  api.registerContextEngine("my-engine", (ctx) => ({    info: {      id: "my-engine",      name: "My Context Engine",      ownsCompaction: true,    },     async ingest({ sessionId, message, isHeartbeat }) {      // Store the message in your data store      return { ingested: true };    },     async assemble({ sessionId, messages, tokenBudget, availableTools, citationsMode }) {      // Return messages that fit the budget      return {        messages: buildContext(messages, tokenBudget),        estimatedTokens: countTokens(messages),        systemPromptAddition: buildMemorySystemPromptAddition({          availableTools: availableTools ?? new Set(),          citationsMode,        }),      };    },     async compact({ sessionId, force }) {      // Summarize older context      return { ok: true, compacted: true };    },  }));}
[/code]

Fabryka `ctx` zawiera opcjonalne wartości `config`, `agentDir` i `workspaceDir`, aby Pluginy mogły zainicjalizować stan dla agenta lub obszaru roboczego przed uruchomieniem pierwszego haka cyklu życia.

Następnie włącz go w konfiguracji:

json5Copy code
[code]
    {  plugins: {    slots: {      contextEngine: "my-engine",    },    entries: {      "my-engine": {        enabled: true,      },    },  },}
[/code]

### Interfejs ContextEngine

Wymagane elementy:

Element | Rodzaj | Cel  
---|---|---  
`info` | Właściwość | Identyfikator silnika, nazwa, wersja i czy posiada Compaction  
`ingest(params)` | Metoda | Zapisuje pojedynczy komunikat  
`assemble(params)` | Metoda | Buduje kontekst dla uruchomienia modelu (zwraca `AssembleResult`)  
`compact(params)` | Metoda | Podsumowuje/redukuje kontekst  
  
`assemble` zwraca `AssembleResult` z:

Uporządkowane komunikaty do wysłania do modelu.

Szacunek silnika dotyczący łącznej liczby tokenów w złożonym kontekście. OpenClaw używa go do decyzji o progach Compaction i raportowania diagnostycznego.

Dodawane na początku monitu systemowego.

Kontroluje, którego szacunku tokenów runner używa do wyprzedzających kontroli przepełnienia. Domyślnie `"assembled"`, co oznacza, że sprawdzany jest tylko szacunek złożonego monitu - odpowiednie dla silników zwracających okienkowany, samowystarczalny kontekst. Ustaw `"preassembly_may_overflow"` tylko wtedy, gdy złożony widok może ukrywać ryzyko przepełnienia w bazowej transkrypcji; wtedy runner bierze maksimum z oszacowania złożonego oraz oszacowania historii sesji sprzed składania (bez okienkowania), gdy decyduje, czy wyprzedzająco wykonać Compaction. W obu przypadkach model nadal widzi komunikaty, które zwrócisz - `promptAuthority` wpływa tylko na kontrolę wstępną.

`compact` zwraca `CompactResult`. Gdy Compaction rotuje aktywną transkrypcję, `result.sessionId` i `result.sessionFile` identyfikują następną sesję, której musi użyć kolejna próba lub tura.

Opcjonalne elementy:

Element | Rodzaj | Cel  
---|---|---  
`bootstrap(params)` | Metoda | Inicjalizuje stan silnika dla sesji. Wywoływane raz, gdy silnik po raz pierwszy widzi sesję (np. import historii).  
`ingestBatch(params)` | Metoda | Pobiera ukończoną turę jako partię. Wywoływane po zakończeniu uruchomienia, ze wszystkimi komunikatami z tej tury naraz.  
`afterTurn(params)` | Metoda | Prace cyklu życia po uruchomieniu (utrwalenie stanu, uruchomienie Compaction w tle).  
`prepareSubagentSpawn(params)` | Metoda | Konfiguruje współdzielony stan dla sesji podrzędnej przed jej rozpoczęciem.  
`onSubagentEnded(params)` | Metoda | Czyści po zakończeniu subagenta.  
`dispose()` | Metoda | Zwalnia zasoby. Wywoływane podczas zamykania Gateway lub ponownego ładowania Plugin - nie dla każdej sesji.  
  
### ownsCompaction

`ownsCompaction` kontroluje, czy wbudowana w Pi automatyczna Compaction w ramach próby pozostaje włączona dla uruchomienia:

ownsCompaction: true

Silnik posiada zachowanie Compaction. OpenClaw wyłącza wbudowaną automatyczną Compaction Pi dla tego uruchomienia, a implementacja `compact()` silnika odpowiada za `/compact`, Compaction odzyskiwania po przepełnieniu oraz wszelką proaktywną Compaction, którą chce wykonać w `afterTurn()`. OpenClaw może nadal uruchomić zabezpieczenie przed przepełnieniem przed monitem; gdy przewidzi, że pełna transkrypcja się przepełni, ścieżka odzyskiwania wywołuje `compact()` aktywnego silnika przed przesłaniem kolejnego monitu.

ownsCompaction: false or unset

Wbudowana automatyczna Compaction Pi może nadal działać podczas wykonywania monitu, ale metoda `compact()` aktywnego silnika jest nadal wywoływana dla `/compact` i odzyskiwania po przepełnieniu.

Oznacza to, że istnieją dwa poprawne wzorce Plugin:

### Owning mode

Zaimplementuj własny algorytm Compaction i ustaw `ownsCompaction: true`.

### Delegating mode

Ustaw `ownsCompaction: false` i spraw, aby `compact()` wywoływało `delegateCompactionToRuntime(...)` z `openclaw/plugin-sdk/core`, aby użyć wbudowanego zachowania Compaction OpenClaw.

Puste `compact()` jest niebezpieczne dla aktywnego silnika nieposiadającego Compaction, ponieważ wyłącza normalną ścieżkę Compaction `/compact` i odzyskiwania po przepełnieniu dla tego slotu silnika.

## Odniesienie do konfiguracji

json5Copy code
[code]
    {  plugins: {    slots: {      // Select the active context engine. Default: "legacy".      // Set to a plugin id to use a plugin engine.      contextEngine: "legacy",    },  },}
[/code]

## Relacja z Compaction i pamięcią

Compaction

Compaction to jedna z odpowiedzialności silnika kontekstu. Starszy silnik deleguje to do wbudowanego podsumowywania OpenClaw. Silniki Plugin mogą implementować dowolną strategię kompaktowania (podsumowania DAG, pobieranie wektorowe itd.).

Pluginy pamięci

Pluginy pamięci (`plugins.slots.memory`) są oddzielone od silników kontekstu. Pluginy pamięci zapewniają wyszukiwanie/pobieranie; silniki kontekstu kontrolują, co widzi model. Mogą działać razem - silnik kontekstu może używać danych pluginu pamięci podczas składania. Silniki Plugin, które chcą używać ścieżki promptu aktywnej pamięci, powinny preferować `buildMemorySystemPromptAddition(...)` z `openclaw/plugin-sdk/core`, która konwertuje sekcje promptu aktywnej pamięci na gotowy do poprzedzenia `systemPromptAddition`. Jeśli silnik potrzebuje kontroli niższego poziomu, nadal może pobrać surowe wiersze z `openclaw/plugin-sdk/memory-host-core` za pomocą `buildActiveMemoryPromptSection(...)`.

Przycinanie sesji

Przycinanie starych wyników narzędzi w pamięci nadal działa niezależnie od tego, który silnik kontekstu jest aktywny.

## Wskazówki

  * Użyj `openclaw doctor`, aby zweryfikować, że silnik ładuje się poprawnie.
  * Jeśli przełączasz silniki, istniejące sesje kontynuują pracę z bieżącą historią. Nowy silnik przejmuje obsługę przyszłych uruchomień.
  * Błędy silnika są rejestrowane i pokazywane w diagnostyce. Jeśli silnik Plugin nie zarejestruje się albo nie da się rozwiązać identyfikatora wybranego silnika, OpenClaw nie przełączy się automatycznie na rozwiązanie zapasowe; uruchomienia będą kończyć się niepowodzeniem, dopóki nie naprawisz pluginu albo nie przełączysz `plugins.slots.contextEngine` z powrotem na `"legacy"`.
  * Podczas developmentu użyj `openclaw plugins install -l ./my-engine`, aby połączyć lokalny katalog pluginu bez kopiowania.


## Powiązane

  * [Compaction](</pl/concepts/compaction>) \- podsumowywanie długich rozmów
  * [Kontekst](</pl/concepts/context>) \- jak kontekst jest budowany dla tur agenta
  * [Architektura Plugin](</pl/plugins/architecture>) \- rejestrowanie pluginów silnika kontekstu
  * [Manifest Plugin](</pl/plugins/manifest>) \- pola manifestu pluginu
  * [Pluginy](</pl/tools/plugin>) \- omówienie pluginów


Was this useful?YesNo