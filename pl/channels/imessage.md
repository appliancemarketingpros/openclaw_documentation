---
title: iMessage
source_url: https://docs.openclaw.ai/pl/channels/imessage
scraped_at: 2026-05-25
---

Status: natywna integracja z zewnętrznym CLI. Gateway uruchamia `imsg rpc` i komunikuje się przez JSON-RPC na stdio (bez osobnego demona/portu). Zaawansowane akcje wymagają `imsg launch` oraz pomyślnej sondy prywatnego API.

**Akcje prywatnego API** Odpowiedzi, tapbacki, efekty, załączniki i zarządzanie grupami. [**Parowanie** Wiadomości prywatne iMessage domyślnie używają trybu parowania. ](</pl/channels/pairing>) **Zdalny Mac** Użyj wrappera SSH, gdy Gateway nie działa na Macu z Messages. [**Dokumentacja konfiguracji** Pełna dokumentacja pól iMessage. ](</pl/gateway/config-channels#imessage>)

## Szybka konfiguracja

### Lokalny Mac (szybka ścieżka)

* ### Zainstaluj i zweryfikuj imsg

bashCopy code
[code]
    brew install steipete/tap/imsgimsg rpc --helpimsg launchopenclaw channels status --probe
[/code]

* ### Skonfiguruj OpenClaw

json5Copy code
[code]
    {channels: {imessage: {enabled: true,cliPath: "/usr/local/bin/imsg",dbPath: "/Users/user/Library/Messages/chat.db",},},}
[/code]

* ### Uruchom gateway

bashCopy code
[code]
    openclaw gateway
[/code]

* ### Zatwierdź pierwsze parowanie wiadomości prywatnej (domyślne dmPolicy)

bashCopy code
[code]
    openclaw pairing list imessageopenclaw pairing approve imessage &lt;CODE&gt;
[/code]

Żądania parowania wygasają po 1 godzinie.

### Zdalny Mac przez SSH

OpenClaw wymaga tylko `cliPath` zgodnego ze stdio, więc możesz wskazać `cliPath` na skrypt wrappera, który łączy się przez SSH ze zdalnym Makiem i uruchamia `imsg`.

bashCopy code
[code]
    #!/usr/bin/env bashexec ssh -T gateway-host imsg "$@"
[/code]

Zalecana konfiguracja, gdy załączniki są włączone:

json5Copy code
[code]
    {channels: {imessage: {  enabled: true,  cliPath: "~/.openclaw/scripts/imsg-ssh",  remoteHost: "user@gateway-host", // used for SCP attachment fetches  includeAttachments: true,  // Optional: override allowed attachment roots.  // Defaults include /Users/*/Library/Messages/Attachments  attachmentRoots: ["/Users/*/Library/Messages/Attachments"],  remoteAttachmentRoots: ["/Users/*/Library/Messages/Attachments"],},},}
[/code]

Jeśli `remoteHost` nie jest ustawione, OpenClaw próbuje wykryć je automatycznie, analizując skrypt wrappera SSH. `remoteHost` musi mieć postać `host` albo `user@host` (bez spacji ani opcji SSH). OpenClaw używa ścisłego sprawdzania klucza hosta dla SCP, więc klucz hosta pośredniczącego musi już istnieć w `~/.ssh/known_hosts`. Ścieżki załączników są sprawdzane względem dozwolonych katalogów głównych (`attachmentRoots` / `remoteAttachmentRoots`).

## Wymagania i uprawnienia (macOS)

  * Messages musi być zalogowane na Macu uruchamiającym `imsg`.
  * Full Disk Access jest wymagany dla kontekstu procesu uruchamiającego OpenClaw/`imsg` (dostęp do bazy danych Messages).
  * Uprawnienie Automation jest wymagane do wysyłania wiadomości przez Messages.app.
  * W przypadku zaawansowanych akcji (reakcja / edycja / cofnięcie wysłania / odpowiedź w wątku / efekty / operacje na grupach) funkcja System Integrity Protection musi być wyłączona — zobacz poniżej Włączanie prywatnego API imsg. Podstawowe wysyłanie/odbieranie tekstu i multimediów działa bez tego.


## Włączanie prywatnego API imsg

`imsg` działa w dwóch trybach operacyjnych:

  * **Tryb podstawowy** (domyślny, bez zmian SIP): tekst i multimedia wychodzące przez `send`, obserwacja/historia przychodząca, lista czatów. To otrzymujesz od razu po świeżej instalacji `brew install steipete/tap/imsg` oraz przyznaniu standardowych uprawnień macOS opisanych wyżej.
  * **Tryb prywatnego API** : `imsg` wstrzykuje pomocniczą bibliotekę dylib do `Messages.app`, aby wywoływać wewnętrzne funkcje `IMCore`. To odblokowuje `react`, `edit`, `unsend`, `reply` (wątek), `sendWithEffect`, `renameGroup`, `setGroupIcon`, `addParticipant`, `removeParticipant`, `leaveGroup`, a także wskaźniki pisania i potwierdzenia odczytu.


Aby uzyskać dostęp do zaawansowanego obszaru akcji dokumentowanego na tej stronie kanału, potrzebujesz trybu prywatnego API. README `imsg` jasno wskazuje wymaganie:

> Zaawansowane funkcje, takie jak `read`, `typing`, `launch`, rozbudowane wysyłanie wspierane przez bridge, mutacja wiadomości i zarządzanie czatami, są opcjonalne. Wymagają wyłączenia SIP oraz wstrzyknięcia pomocniczej biblioteki dylib do `Messages.app`. `imsg launch` odmawia wstrzyknięcia, gdy SIP jest włączone.

Technika wstrzykiwania helpera używa własnej biblioteki dylib `imsg`, aby dotrzeć do prywatnych API Messages. W ścieżce OpenClaw iMessage nie ma serwera zewnętrznego ani środowiska uruchomieniowego BlueBubbles.

### Konfiguracja

  1. **Zainstaluj (lub zaktualizuj)`imsg`** na Macu, na którym działa Messages.app:

bashCopy code
[code]brew install steipete/tap/imsgimsg --versionimsg status --json
[/code]

Wynik `imsg status --json` raportuje `bridge_version`, `rpc_methods` oraz `selectors` dla poszczególnych metod, dzięki czemu możesz sprawdzić, co obsługuje bieżąca kompilacja, zanim zaczniesz.

  2. **Wyłącz System Integrity Protection.** Jest to zależne od wersji macOS, ponieważ podstawowe wymaganie Apple zależy od systemu operacyjnego i sprzętu:

     * **macOS 10.13–10.15 (Sierra–Catalina):** wyłącz Library Validation przez Terminal, uruchom ponownie w trybie Recovery Mode, uruchom `csrutil disable`, zrestartuj.
     * **macOS 11+ (Big Sur i nowsze), Intel:** Recovery Mode (albo Internet Recovery), `csrutil disable`, restart.
     * **macOS 11+, Apple Silicon:** sekwencja uruchamiania przyciskiem zasilania, aby wejść do Recovery; w nowszych wersjach macOS przytrzymaj klawisz **Left Shift** , gdy klikasz Continue, a następnie `csrutil disable`. Konfiguracje maszyn wirtualnych używają osobnej procedury — najpierw zrób snapshot VM.
     * **macOS 26 / Tahoe:** zasady library-validation i kontrole prywatnych uprawnień `imagent` zostały jeszcze bardziej zaostrzone; `imsg` może wymagać zaktualizowanej kompilacji, aby nadążyć. Jeśli po dużej aktualizacji macOS wstrzyknięcie `imsg launch` albo konkretne `selectors` zaczynają zwracać false, sprawdź informacje o wydaniu `imsg`, zanim uznasz, że krok SIP się powiódł.

Wykonaj procedurę Apple dla trybu Recovery odpowiednią dla Twojego Maca, aby wyłączyć SIP przed uruchomieniem `imsg launch`.

  3. **Wstrzyknij helper.** Przy wyłączonym SIP i zalogowanym Messages.app:

bashCopy code
[code]imsg launch
[/code]

`imsg launch` odmawia wstrzyknięcia, gdy SIP nadal jest włączone, więc działa to również jako potwierdzenie, że krok 2 został wykonany.

  4. **Zweryfikuj bridge z OpenClaw:**

bashCopy code
[code]openclaw channels status --probe
[/code]

Wpis iMessage powinien raportować `works`, a `imsg status --json | jq '.selectors'` powinien pokazywać `retractMessagePart: true` oraz wszystkie selektory edycji / pisania / odczytu ujawniane przez Twoją kompilację macOS. Bramkowanie poszczególnych metod Pluginu OpenClaw w `actions.ts` reklamuje tylko akcje, których bazowy selektor ma wartość `true`, więc obszar akcji widoczny na liście narzędzi agenta odzwierciedla to, co bridge może faktycznie zrobić na tym hoście.


Jeśli `openclaw channels status --probe` raportuje kanał jako `works`, ale konkretne akcje zgłaszają błąd „iMessage `<action>` requires the imsg private API bridge” w czasie wysyłania, uruchom ponownie `imsg launch` — helper może zniknąć (restart Messages.app, aktualizacja systemu itd.), a buforowany status `available: true` będzie nadal reklamować akcje do czasu, aż następna sonda go odświeży.

### Gdy nie możesz wyłączyć SIP

Jeśli wyłączenie SIP nie jest akceptowalne dla Twojego modelu zagrożeń:

  * `imsg` wraca do trybu podstawowego — tylko tekst + multimedia + odbiór.
  * Plugin OpenClaw nadal reklamuje wysyłanie tekstu/multimediów i monitorowanie przychodzące; po prostu ukrywa `react`, `edit`, `unsend`, `reply`, `sendWithEffect` oraz operacje na grupach z obszaru akcji (zgodnie z bramką możliwości dla poszczególnych metod).
  * Możesz uruchomić osobnego Maca bez Apple Silicon (albo dedykowanego Maca bota) z wyłączonym SIP dla obciążenia iMessage, pozostawiając SIP włączony na swoich głównych urządzeniach. Zobacz poniżej Dedykowany użytkownik macOS bota (osobna tożsamość iMessage).


## Kontrola dostępu i routing

### Polityka wiadomości prywatnych

`channels.imessage.dmPolicy` kontroluje wiadomości bezpośrednie:

  * `pairing` (domyślnie)
  * `allowlist`
  * `open` (wymaga, aby `allowFrom` zawierało `"*"`)
  * `disabled`


Pole listy dozwolonych: `channels.imessage.allowFrom`.

Wpisy listy dozwolonych muszą identyfikować nadawców: uchwyty albo statyczne grupy dostępu nadawców (`accessGroup:<name>`). Użyj `channels.imessage.groupAllowFrom` dla celów czatu, takich jak `chat_id:*`, `chat_guid:*` lub `chat_identifier:*`; użyj `channels.imessage.groups` dla numerycznych kluczy rejestru `chat_id`.

### Polityka grup + wzmianki

`channels.imessage.groupPolicy` kontroluje obsługę grup:

  * `allowlist` (domyślnie, gdy skonfigurowane)
  * `open`
  * `disabled`


Lista dozwolonych nadawców grupowych: `channels.imessage.groupAllowFrom`.

Wpisy `groupAllowFrom` mogą również odwoływać się do statycznych grup dostępu nadawców (`accessGroup:<name>`).

Zachowanie zapasowe w czasie działania: jeśli `groupAllowFrom` nie jest ustawione, kontrole nadawców grup iMessage używają `allowFrom`; ustaw `groupAllowFrom`, gdy przyjmowanie wiadomości prywatnych i grupowych powinno się różnić. Uwaga dotycząca działania: jeśli `channels.imessage` całkowicie brakuje, środowisko uruchomieniowe wraca do `groupPolicy="allowlist"` i zapisuje ostrzeżenie (nawet jeśli ustawiono `channels.defaults.groupPolicy`).

Bramkowanie wzmianek dla grup:

  * iMessage nie ma natywnych metadanych wzmianek
  * wykrywanie wzmianek używa wzorców regex (`agents.list[].groupChat.mentionPatterns`, awaryjnie `messages.groupChat.mentionPatterns`)
  * bez skonfigurowanych wzorców bramkowania wzmianek nie da się wymusić


Polecenia sterujące od autoryzowanych nadawców mogą omijać bramkowanie wzmianek w grupach.

`systemPrompt` dla grupy:

Każdy wpis pod `channels.imessage.groups.*` akceptuje opcjonalny ciąg `systemPrompt`. Wartość jest wstrzykiwana do promptu systemowego agenta przy każdym przebiegu obsługującym wiadomość w tej grupie. Rozwiązywanie odzwierciedla rozwiązywanie promptu dla grupy używane przez `channels.whatsapp.groups`:

  1. **Prompt systemowy konkretnej grupy** (`groups["<chat_id>"].systemPrompt`): używany, gdy konkretny wpis grupy istnieje w mapie **i** jego klucz `systemPrompt` jest zdefiniowany. Jeśli `systemPrompt` jest pustym ciągiem (`""`), symbol wieloznaczny jest tłumiony i do tej grupy nie jest stosowany żaden prompt systemowy.
  2. **Prompt systemowy symbolu wieloznacznego grupy** (`groups["*"].systemPrompt`): używany, gdy konkretny wpis grupy jest całkowicie nieobecny w mapie albo gdy istnieje, ale nie definiuje klucza `systemPrompt`.

json5Copy code
[code]
    {  channels: {    imessage: {      groupPolicy: "allowlist",      groupAllowFrom: ["+15555550123"],      groups: {        "*": { systemPrompt: "Use British spelling." },        "8421": {          requireMention: true,          systemPrompt: "This is the on-call rotation chat. Keep replies under 3 sentences.",        },        "9907": {          // explicit suppression: the wildcard "Use British spelling." does not apply here          systemPrompt: "",        },      },    },  },}
[/code]

Prompty dla grup dotyczą tylko wiadomości grupowych — wiadomości bezpośrednie w tym kanale pozostają bez zmian.

### Sesje i deterministyczne odpowiedzi

  * DM-y używają routingu bezpośredniego; grupy używają routingu grupowego.
  * Przy domyślnym `session.dmScope=main` DM-y iMessage zwijają się do głównej sesji agenta.
  * Sesje grupowe są izolowane (`agent:<agentId>:imessage:group:<chat_id>`).
  * Odpowiedzi są kierowane z powrotem do iMessage przy użyciu metadanych kanału/targetu pochodzenia.


Zachowanie wątków podobnych do grupowych:

Niektóre wieloosobowe wątki iMessage mogą przychodzić z `is_group=false`. Jeśli ten `chat_id` jest jawnie skonfigurowany pod `channels.imessage.groups`, OpenClaw traktuje go jako ruch grupowy (bramkowanie grupowe + izolacja sesji grupowej).

## Powiązania konwersacji ACP

Starsze czaty iMessage można także powiązać z sesjami ACP.

Szybki przepływ operatora:

  * Uruchom `/acp spawn codex --bind here` w DM-ie lub dozwolonym czacie grupowym.
  * Przyszłe wiadomości w tej samej konwersacji iMessage będą kierowane do utworzonej sesji ACP.
  * `/new` i `/reset` resetują tę samą powiązaną sesję ACP w miejscu.
  * `/acp close` zamyka sesję ACP i usuwa powiązanie.


Skonfigurowane trwałe powiązania są obsługiwane przez wpisy najwyższego poziomu `bindings[]` z `type: "acp"` i `match.channel: "imessage"`.

`match.peer.id` może używać:

  * znormalizowanego uchwytu DM, takiego jak `+15555550123` lub `user@example.com`
  * `chat_id:<id>` (zalecane dla stabilnych powiązań grupowych)
  * `chat_guid:<guid>`
  * `chat_identifier:<identifier>`


Przykład:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "codex",        runtime: {          type: "acp",          acp: { agent: "codex", backend: "acpx", mode: "persistent" },        },      },    ],  },  bindings: [    {      type: "acp",      agentId: "codex",      match: {        channel: "imessage",        accountId: "default",        peer: { kind: "group", id: "chat_id:123" },      },      acp: { label: "codex-group" },    },  ],}
[/code]

Zobacz [Agenci ACP](</pl/tools/acp-agents>), aby poznać wspólne zachowanie powiązań ACP.

## Wzorce wdrożenia

Dedykowany użytkownik bota macOS (osobna tożsamość iMessage)

Użyj dedykowanego Apple ID i użytkownika macOS, aby ruch bota był odizolowany od Twojego osobistego profilu Messages.

Typowy przepływ:

  1. Utwórz dedykowanego użytkownika macOS lub zaloguj się jako taki użytkownik.
  2. Zaloguj się w Messages przy użyciu Apple ID bota w ramach tego użytkownika.
  3. Zainstaluj `imsg` u tego użytkownika.
  4. Utwórz wrapper SSH, aby OpenClaw mógł uruchamiać `imsg` w kontekście tego użytkownika.
  5. Ustaw `channels.imessage.accounts.<id>.cliPath` i `.dbPath` na profil tego użytkownika.


Pierwsze uruchomienie może wymagać zatwierdzeń w GUI (Automation + Full Disk Access) w sesji tego użytkownika bota.

Zdalny Mac przez Tailscale (przykład)

Typowa topologia:

  * Gateway działa na Linux/VM
  * iMessage + `imsg` działa na Macu w Twoim tailnecie
  * wrapper `cliPath` używa SSH do uruchomienia `imsg`
  * `remoteHost` włącza pobieranie załączników przez SCP


Przykład:

json5Copy code
[code]
    {  channels: {    imessage: {      enabled: true,      cliPath: "~/.openclaw/scripts/imsg-ssh",      remoteHost: "bot@mac-mini.tailnet-1234.ts.net",      includeAttachments: true,      dbPath: "/Users/bot/Library/Messages/chat.db",    },  },}
[/code]

bashCopy code
[code]
    #!/usr/bin/env bashexec ssh -T bot@mac-mini.tailnet-1234.ts.net imsg "$@"
[/code]

Użyj kluczy SSH, aby zarówno SSH, jak i SCP były nieinteraktywne. Najpierw upewnij się, że klucz hosta jest zaufany (na przykład `ssh bot@mac-mini.tailnet-1234.ts.net`), aby `known_hosts` było wypełnione.

Wzorzec wielu kont

iMessage obsługuje konfigurację dla konta pod `channels.imessage.accounts`.

Każde konto może nadpisywać pola takie jak `cliPath`, `dbPath`, `allowFrom`, `groupPolicy`, `mediaMaxMb`, ustawienia historii i allowlisty katalogów głównych załączników.

## Multimedia, dzielenie i targety dostarczania

Załączniki i multimedia

  * przyjmowanie załączników przychodzących jest **domyślnie wyłączone** — ustaw `channels.imessage.includeAttachments: true`, aby przekazywać zdjęcia, notatki głosowe, wideo i inne załączniki do agenta. Gdy jest wyłączone, iMessage zawierające tylko załączniki są odrzucane przed dotarciem do agenta i mogą w ogóle nie wygenerować wiersza logu `Inbound message`.
  * zdalne ścieżki załączników można pobierać przez SCP, gdy ustawiono `remoteHost`
  * ścieżki załączników muszą pasować do dozwolonych katalogów głównych: 
    * `channels.imessage.attachmentRoots` (lokalne)
    * `channels.imessage.remoteAttachmentRoots` (tryb zdalnego SCP)
    * domyślny wzorzec katalogu głównego: `/Users/*/Library/Messages/Attachments`
  * SCP używa ścisłego sprawdzania klucza hosta (`StrictHostKeyChecking=yes`)
  * rozmiar multimediów wychodzących używa `channels.imessage.mediaMaxMb` (domyślnie 16 MB)

Dzielenie wiadomości wychodzących

  * limit fragmentu tekstu: `channels.imessage.textChunkLimit` (domyślnie 4000)
  * tryb dzielenia: `channels.imessage.chunkMode`
    * `length` (domyślnie)
    * `newline` (dzielenie najpierw według akapitów)

Formaty adresowania

Preferowane jawne targety:

  * `chat_id:123` (zalecane dla stabilnego routingu)
  * `chat_guid:...`
  * `chat_identifier:...`


Obsługiwane są także targety uchwytów:

  * `imessage:+1555...`
  * `sms:+1555...`
  * `user@example.com`

bashCopy code
[code]
    imsg chats --limit 20
[/code]

## Akcje prywatnego API

Gdy działa `imsg launch`, a `openclaw channels status --probe` zgłasza `privateApi.available: true`, narzędzie wiadomości może używać natywnych akcji iMessage oprócz zwykłych wysyłek tekstowych.

json5Copy code
[code]
    {  channels: {    imessage: {      actions: {        reactions: true,        edit: true,        unsend: true,        reply: true,        sendWithEffect: true,        sendAttachment: true,        renameGroup: true,        setGroupIcon: true,        addParticipant: true,        removeParticipant: true,        leaveGroup: true,      },    },  },}
[/code]

Dostępne akcje

  * **react** : Dodaj/usuń tapbacki iMessage (`messageId`, `emoji`, `remove`). Obsługiwane tapbacki mapują się na miłość, polubienie, niechęć, śmiech, podkreślenie i pytanie.
  * **reply** : Wyślij odpowiedź w wątku do istniejącej wiadomości (`messageId`, `text` lub `message`, plus `chatGuid`, `chatId`, `chatIdentifier` albo `to`).
  * **sendWithEffect** : Wyślij tekst z efektem iMessage (`text` lub `message`, `effect` lub `effectId`).
  * **edit** : Edytuj wysłaną wiadomość w obsługiwanych wersjach macOS/prywatnego API (`messageId`, `text` lub `newText`).
  * **unsend** : Cofnij wysłaną wiadomość w obsługiwanych wersjach macOS/prywatnego API (`messageId`).
  * **upload-file** : Wyślij multimedia/pliki (`buffer` jako base64 albo uwodnione `media`/`path`/`filePath`, `filename`, opcjonalnie `asVoice`). Starszy alias: `sendAttachment`.
  * **renameGroup** , **setGroupIcon** , **addParticipant** , **removeParticipant** , **leaveGroup** : Zarządzaj czatami grupowymi, gdy bieżący target jest konwersacją grupową.

Identyfikatory wiadomości

Kontekst przychodzącego iMessage zawiera zarówno krótkie wartości `MessageSid`, jak i pełne GUID-y wiadomości, gdy są dostępne. Krótkie identyfikatory są ograniczone do ostatniej pamięci podręcznej odpowiedzi w pamięci i przed użyciem są sprawdzane względem bieżącego czatu. Jeśli krótki identyfikator wygasł albo należy do innego czatu, spróbuj ponownie z pełnym `MessageSidFull`.

Wykrywanie możliwości

OpenClaw ukrywa akcje prywatnego API tylko wtedy, gdy status sondy z pamięci podręcznej mówi, że mostek jest niedostępny. Jeśli status jest nieznany, akcje pozostają widoczne i wysyłanie leniwie uruchamia sondy, aby pierwsza akcja mogła się powieść po `imsg launch` bez osobnego ręcznego odświeżenia statusu.

Potwierdzenia odczytu i pisanie

Gdy mostek prywatnego API działa, zaakceptowane czaty przychodzące są oznaczane jako przeczytane przed wysłaniem do obsługi, a nadawcy jest pokazywana chmurka pisania, gdy agent generuje odpowiedź. Wyłącz oznaczanie jako przeczytane za pomocą:

json5Copy code
[code]
    {  channels: {    imessage: {      sendReadReceipts: false,    },  },}
[/code]

Starsze kompilacje `imsg`, które poprzedzają listę możliwości dla metody, po cichu wyłączą pisanie/odczyt; OpenClaw zapisuje jednorazowe ostrzeżenie przy każdym restarcie, aby brakujące potwierdzenie dało się przypisać.

Przychodzące tapbacki

OpenClaw subskrybuje tapbacki iMessage i kieruje zaakceptowane reakcje jako zdarzenia systemowe zamiast zwykłego tekstu wiadomości, więc tapback użytkownika nie wyzwala zwykłej pętli odpowiedzi.

Tryb powiadomień jest kontrolowany przez `channels.imessage.reactionNotifications`:

  * `"own"` (domyślnie): powiadamiaj tylko wtedy, gdy użytkownicy reagują na wiadomości napisane przez bota.
  * `"all"`: powiadamiaj o wszystkich przychodzących tapbackach od autoryzowanych nadawców.
  * `"off"`: ignoruj przychodzące tapbacki.


Nadpisania dla konta używają `channels.imessage.accounts.<id>.reactionNotifications`.

## Zapisy konfiguracji

iMessage domyślnie zezwala na zapisy konfiguracji inicjowane przez kanał (dla `/config set|unset`, gdy `commands.config: true`).

Wyłącz:

json5Copy code
[code]
    {  channels: {    imessage: {      configWrites: false,    },  },}
[/code]

## Scalanie dzielonych wysyłek DM-ów (polecenie + URL w jednej kompozycji)

Gdy użytkownik wpisze razem polecenie i URL — np. `Dump https://example.com/article` — aplikacja Messages firmy Apple dzieli wysyłkę na **dwa osobne wiersze`chat.db`**:

  1. Wiadomość tekstową (`"Dump"`).
  2. Dymek podglądu URL (`"https://..."`) z obrazami podglądu OG jako załącznikami.


Dwa wiersze docierają do OpenClaw w odstępie około 0,8-2,0 s w większości konfiguracji. Bez scalania agent otrzymuje samo polecenie w turze 1, odpowiada (często „wyślij mi URL”) i widzi URL dopiero w turze 2 — wtedy kontekst polecenia jest już utracony. To wynika z potoku wysyłania Apple, a nie z czegokolwiek, co wprowadza OpenClaw lub `imsg`.

`channels.imessage.coalesceSameSenderDms` włącza dla DM scalanie kolejnych wierszy od tego samego nadawcy w jedną turę agenta. Czaty grupowe nadal są wysyłane osobno dla każdej wiadomości, aby zachować strukturę tur wielu użytkowników.

### When to enable

Włącz, gdy:

  * Dostarczasz Skills, które oczekują `command + payload` w jednej wiadomości (dump, paste, save, queue itd.).
  * Twoi użytkownicy wklejają URL-e, obrazy lub długą treść obok poleceń.
  * Możesz zaakceptować dodatkowe opóźnienie tury DM (zobacz niżej).


Pozostaw wyłączone, gdy:

  * Potrzebujesz minimalnego opóźnienia poleceń dla jednowyrazowych wyzwalaczy DM.
  * Wszystkie Twoje przepływy to jednorazowe polecenia bez dalszych payloadów.


### Enabling

json5Copy code
[code]
    {  channels: {    imessage: {      coalesceSameSenderDms: true, // opt in (default: false)    },  },}
[/code]

Przy włączonej fladze i bez jawnego `messages.inbound.byChannel.imessage` okno debounce rozszerza się do **2500 ms** (starsza wartość domyślna to 0 ms — bez debounce). Szersze okno jest wymagane, ponieważ rytm podzielonego wysyłania Apple wynoszący 0,8-2,0 s nie mieści się w węższej wartości domyślnej.

Aby samodzielnie dostroić okno:

json5Copy code
[code]
    {  messages: {    inbound: {      byChannel: {        // 2500 ms works for most setups; raise to 4000 ms if your Mac is        // slow or under memory pressure (observed gap can stretch past 2 s        // then).        imessage: 2500,      },    },  },}
[/code]

### Trade-offs

  * **Dodatkowe opóźnienie dla wiadomości DM.** Przy włączonej fladze każdy DM (w tym samodzielne polecenia sterujące i pojedyncze tekstowe kontynuacje) czeka maksymalnie do końca okna debounce przed wysłaniem, na wypadek nadejścia wiersza z payloadem. Wiadomości czatu grupowego zachowują natychmiastowe wysyłanie.
  * **Scalone wyjście jest ograniczone.** Scalony tekst ma limit 4000 znaków z jawnym znacznikiem `…[truncated]`; załączniki mają limit 20; wpisy źródeł mają limit 10 (po przekroczeniu zachowywany jest pierwszy i najnowsze). Każdy GUID źródła jest śledzony w `coalescedMessageGuids` dla dalszej telemetrii.
  * **Tylko DM.** Czaty grupowe przechodzą do wysyłania per wiadomość, aby bot pozostawał responsywny, gdy pisze wiele osób.
  * **Opt-in, per kanał.** Inne kanały (Telegram, WhatsApp, Slack, …) pozostają bez zmian. Starsze konfiguracje BlueBubbles, które ustawiają `channels.bluebubbles.coalesceSameSenderDms`, powinny przenieść tę wartość do `channels.imessage.coalesceSameSenderDms`.


### Scenariusze i to, co widzi agent

Użytkownik tworzy | `chat.db` generuje | Flaga wyłączona (domyślnie) | Flaga włączona + okno 2500 ms  
---|---|---|---  
`Dump https://example.com` (jedno wysłanie) | 2 wiersze ~1 s odstępu | Dwie tury agenta: samo „Dump”, potem URL | Jedna tura: scalony tekst `Dump https://example.com`  
`Save this 📎image.jpg caption` (załącznik + tekst) | 2 wiersze | Dwie tury (załącznik porzucony przy scalaniu) | Jedna tura: tekst + obraz zachowane  
`/status` (samodzielne polecenie) | 1 wiersz | Natychmiastowe wysłanie | **Czekaj maksymalnie do końca okna, potem wyślij**  
URL wklejony samodzielnie | 1 wiersz | Natychmiastowe wysłanie | Natychmiastowe wysłanie (tylko jeden wpis w kubełku)  
Tekst + URL wysłane jako dwie celowo oddzielne wiadomości, w odstępie minut | 2 wiersze poza oknem | Dwie tury | Dwie tury (okno wygasa między nimi)  
Szybka seria (>10 małych DM w oknie) | N wierszy | N tur | Jedna tura, ograniczone wyjście (pierwszy + najnowsze, zastosowane limity tekstu/załączników)  
Dwie osoby piszące w czacie grupowym | N wierszy od M nadawców | M+ tur (jedna na kubełek nadawcy) | M+ tur — czaty grupowe nie są scalane  
  
## Nadrabianie po przestoju Gateway

Gdy Gateway jest offline (awaria, restart, uśpienie Maca, wyłączona maszyna), `imsg watch` wznawia działanie od bieżącego stanu `chat.db`, gdy Gateway ponownie się uruchomi — wszystko, co dotarło podczas przerwy, domyślnie nigdy nie zostanie zobaczone. Nadrabianie odtwarza te wiadomości przy następnym uruchomieniu, aby agent nie pominął po cichu ruchu przychodzącego.

Nadrabianie jest **domyślnie wyłączone**. Włącz je per kanał:

tsCopy code
[code]
    channels: {  imessage: {    catchup: {      enabled: true,             // master switch (default: false)      maxAgeMinutes: 120,        // skip rows older than now - 2h (default: 120, clamp 1..720)      perRunLimit: 50,           // max rows replayed per startup (default: 50, clamp 1..500)      firstRunLookbackMinutes: 30, // first run with no cursor: look back 30 min (default: 30)      maxFailureRetries: 10,     // give up on a wedged guid after 10 dispatch failures (default: 10)    },  },}
[/code]

### Jak to działa

Jedno przejście na każde uruchomienie `monitorIMessageProvider`, w sekwencji: gotowe `imsg launch` → `watch.subscribe` → `performIMessageCatchup` → pętla wysyłania na żywo. Samo nadrabianie używa `chats.list` \+ per-czatowego `messages.history` wobec tego samego klienta JSON-RPC, którego używa `imsg watch`. Wszystko, co dotrze podczas przebiegu nadrabiania, normalnie przechodzi przez wysyłanie na żywo; istniejąca pamięć podręczna deduplikacji przychodzącej pochłania wszelkie nakładanie się z odtwarzanymi wierszami.

Każdy odtwarzany wiersz jest przekazywany przez ścieżkę wysyłania na żywo (`evaluateIMessageInbound` \+ `dispatchInboundMessage`), więc listy dozwolonych, zasady grup, debouncer, pamięć podręczna echa i potwierdzenia odczytu zachowują się identycznie dla wiadomości odtwarzanych i wiadomości na żywo.

### Semantyka kursora i ponawiania

Nadrabianie utrzymuje kursor per konto w `<openclawStateDir>/imessage/catchup/<account>__<hash>.json` (katalog stanu OpenClaw domyślnie to `~/.openclaw`, można go nadpisać przez `OPENCLAW_STATE_DIR`):

jsonCopy code
[code]
    {  "lastSeenMs": 1717900800000,  "lastSeenRowid": 482910,  "updatedAt": 1717900801234,  "failureRetries": { "<guid>": 1 }}
[/code]

  * Kursor przesuwa się po każdym udanym wysłaniu i jest zatrzymywany, gdy wysłanie wiersza rzuci błąd — następne uruchomienie ponawia ten sam wiersz od zatrzymanego kursora.
  * Po `maxFailureRetries` kolejnych rzutach błędu dla tego samego `guid` nadrabianie zapisuje `warn` i wymusza przesunięcie kursora poza zablokowaną wiadomość, aby kolejne uruchomienia mogły iść naprzód.
  * GUID-y, dla których już się poddano, są pomijane po wykryciu (bez próby wysłania) w późniejszych uruchomieniach i liczone pod `skippedGivenUp` w podsumowaniu przebiegu.


### Sygnały widoczne dla operatora

CodeCopy code
[code]
    imessage catchup: replayed=N skippedFromMe=… skippedGivenUp=… failed=… givenUp=… fetchedCount=…imessage catchup: giving up on guid=<guid> after &lt;N&gt; failures; advancing cursor past itimessage catchup: fetched &lt;X&gt; rows across chats, capped to perRunLimit=&lt;Y&gt;
[/code]

Wiersz `WARN ... capped to perRunLimit` oznacza, że pojedyncze uruchomienie nie opróżniło całego backlogu. Zwiększ `perRunLimit` (maks. 500), jeśli Twoje przerwy regularnie przekraczają domyślny przebieg 50 wierszy.

### Kiedy pozostawić wyłączone

  * Gateway działa ciągle z automatycznym restartem przez watchdog, a przerwy są zawsze krótsze niż kilka sekund — domyślne wyłączenie jest w porządku.
  * Wolumen DM jest niski, a pominięte wiadomości nie zmieniłyby zachowania agenta — początkowe okno `firstRunLookbackMinutes` może wysłać zaskakujący stary kontekst przy pierwszym włączeniu.


Gdy włączysz nadrabianie, pierwsze uruchomienie bez kursora patrzy wstecz tylko o `firstRunLookbackMinutes` (domyślnie 30 min), a nie o pełne okno `maxAgeMinutes` — zapobiega to odtwarzaniu długiej historii wiadomości sprzed włączenia.

## Rozwiązywanie problemów

imsg not found or RPC unsupported

Sprawdź binarkę i obsługę RPC:

bashCopy code
[code]
    imsg rpc --helpimsg status --jsonopenclaw channels status --probe
[/code]

Jeśli próba zgłasza brak obsługi RPC, zaktualizuj `imsg`. Jeśli akcje prywatnego API są niedostępne, uruchom `imsg launch` w zalogowanej sesji użytkownika macOS i wykonaj próbę ponownie. Jeśli Gateway nie działa na macOS, użyj opisanej wyżej konfiguracji zdalnego Maca przez SSH zamiast domyślnej lokalnej ścieżki `imsg`.

Gateway is not running on macOS

Domyślne `cliPath: "imsg"` musi działać na Macu zalogowanym do Wiadomości. W systemie Linux lub Windows ustaw `channels.imessage.cliPath` na skrypt opakowujący, który łączy się przez SSH z tym Makiem i uruchamia `imsg "$@"`.

bashCopy code
[code]
    #!/usr/bin/env bashexec ssh -T messages-mac imsg "$@"
[/code]

Następnie uruchom:

bashCopy code
[code]
    openclaw channels status --probe --channel imessage
[/code]

DMs are ignored

Sprawdź:

  * `channels.imessage.dmPolicy`
  * `channels.imessage.allowFrom`
  * zatwierdzenia parowania (`openclaw pairing list imessage`)

Group messages are ignored

Sprawdź:

  * `channels.imessage.groupPolicy`
  * `channels.imessage.groupAllowFrom`
  * zachowanie listy dozwolonych `channels.imessage.groups`
  * konfigurację wzorca wzmianki (`agents.list[].groupChat.mentionPatterns`)

Remote attachments fail

Sprawdź:

  * `channels.imessage.remoteHost`
  * `channels.imessage.remoteAttachmentRoots`
  * uwierzytelnianie kluczem SSH/SCP z hosta Gateway
  * czy klucz hosta istnieje w `~/.ssh/known_hosts` na hoście Gateway
  * czy zdalna ścieżka jest czytelna na Macu uruchamiającym Wiadomości

macOS permission prompts were missed

Uruchom ponownie w interaktywnym terminalu GUI w tym samym kontekście użytkownika/sesji i zatwierdź monity:

bashCopy code
[code]
    imsg chats --limit 1imsg send <handle> "test"
[/code]

Potwierdź, że pełny dostęp do dysku i automatyzacja są przyznane dla kontekstu procesu, który uruchamia OpenClaw/`imsg`.

## Wskaźniki referencji konfiguracji

  * [Referencja konfiguracji - iMessage](</pl/gateway/config-channels#imessage>)
  * [Konfiguracja Gateway](</pl/gateway/configuration>)
  * [Parowanie](</pl/channels/pairing>)


## Powiązane

  * [Przegląd kanałów](</pl/channels>) — wszystkie obsługiwane kanały
  * [Usunięcie BlueBubbles i ścieżka imsg iMessage](</pl/announcements/bluebubbles-imessage>) — ogłoszenie i podsumowanie migracji
  * [Przejście z BlueBubbles](</pl/channels/imessage-from-bluebubbles>) — tabela tłumaczenia konfiguracji i instrukcja przełączenia krok po kroku
  * [Parowanie](</pl/channels/pairing>) — uwierzytelnianie DM i przepływ parowania
  * [Grupy](</pl/channels/groups>) — zachowanie czatu grupowego i bramkowanie wzmianek
  * [Routing kanałów](</pl/channels/channel-routing>) — routing sesji dla wiadomości
  * [Bezpieczeństwo](</pl/gateway/security>) — model dostępu i utwardzanie


Was this useful?YesNo