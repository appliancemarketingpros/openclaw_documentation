---
title: Zaplanowane zadania
source_url: https://docs.openclaw.ai/pl/automation/cron-jobs
scraped_at: 2026-05-25
---

Cron to wbudowany harmonogram Gateway. Utrwala zadania, wybudza agenta we właściwym czasie i może dostarczać wynik z powrotem do kanału czatu lub punktu końcowego Webhook.

## Szybki start

* ### Add a one-shot reminder

bashCopy code
[code]
    openclaw cron add \  --name "Reminder" \  --at "2026-02-01T16:00:00Z" \  --session main \  --system-event "Reminder: check the cron docs draft" \  --wake now \  --delete-after-run
[/code]

* ### Check your jobs

bashCopy code
[code]
    openclaw cron listopenclaw cron get <job-id>openclaw cron show <job-id>
[/code]

* ### See run history

bashCopy code
[code]
    openclaw cron runs --id <job-id>
[/code]

## Jak działa cron

  * Cron działa **wewnątrz procesu Gateway** (nie wewnątrz modelu).
  * Definicje zadań są utrwalane w `~/.openclaw/cron/jobs.json`, więc ponowne uruchomienia nie powodują utraty harmonogramów.
  * Stan wykonania w czasie działania jest utrwalany obok, w `~/.openclaw/cron/jobs-state.json`. Jeśli śledzisz definicje cron w git, śledź `jobs.json` i dodaj `jobs-state.json` do gitignore.
  * Po rozdzieleniu starsze wersje OpenClaw mogą odczytać `jobs.json`, ale mogą traktować zadania jako nowe, ponieważ pola czasu działania znajdują się teraz w `jobs-state.json`.
  * Gdy `jobs.json` zostanie edytowany podczas działania lub zatrzymania Gateway, OpenClaw porównuje zmienione pola harmonogramu z oczekującymi metadanymi slotu czasu działania i czyści nieaktualne wartości `nextRunAtMs`. Przepisania obejmujące wyłącznie formatowanie lub kolejność kluczy zachowują oczekujący slot.
  * Wszystkie wykonania cron tworzą rekordy [zadania w tle](</pl/automation/tasks>).
  * Przy uruchomieniu Gateway zaległe izolowane zadania tury agenta są planowane ponownie poza oknem łączenia kanałów, zamiast odtwarzać się natychmiast, dzięki czemu uruchamianie Discord/Telegram i konfiguracja poleceń natywnych pozostają responsywne po restartach.
  * Zadania jednorazowe (`--at`) domyślnie usuwają się automatycznie po sukcesie.
  * Izolowane uruchomienia cron w trybie najlepszych starań zamykają śledzone karty/procesy przeglądarki dla swojej sesji `cron:<jobId>` po zakończeniu uruchomienia, aby odłączona automatyzacja przeglądarki nie zostawiała osieroconych procesów.
  * Izolowane uruchomienia cron, które otrzymują wąskie uprawnienie samooczyszczania cron, nadal mogą odczytać status harmonogramu, samofiltrowaną listę swojego bieżącego zadania oraz historię uruchomień tego zadania, dzięki czemu kontrole statusu/Heartbeat mogą sprawdzać własny harmonogram bez uzyskiwania szerszego dostępu do mutowania cron.
  * Izolowane uruchomienia cron chronią też przed nieaktualnymi odpowiedziami potwierdzającymi. Jeśli pierwszy wynik jest tylko tymczasową aktualizacją statusu (`on it`, `pulling everything together` i podobne wskazówki), a żadne podrzędne uruchomienie subagenta nie odpowiada już za finalną odpowiedź, OpenClaw ponawia prompt raz, aby uzyskać rzeczywisty wynik przed dostarczeniem.
  * Izolowane uruchomienia cron preferują ustrukturyzowane metadane odmowy wykonania z osadzonego uruchomienia, a następnie wracają do znanych znaczników finalnego podsumowania/wyjścia, takich jak `SYSTEM_RUN_DENIED` i `INVALID_REQUEST`, aby zablokowane polecenie nie zostało zgłoszone jako udane uruchomienie.
  * Izolowane uruchomienia cron traktują też błędy agenta na poziomie uruchomienia jako błędy zadania, nawet gdy nie powstanie payload odpowiedzi, dzięki czemu awarie modelu/dostawcy zwiększają liczniki błędów i wyzwalają powiadomienia o awarii, zamiast oznaczać zadanie jako udane.
  * Gdy izolowane zadanie tury agenta osiągnie `timeoutSeconds`, cron przerywa bazowe uruchomienie agenta i daje mu krótkie okno na sprzątanie. Jeśli uruchomienie nie opróżni się, sprzątanie należące do Gateway wymusza wyczyszczenie własności sesji tego uruchomienia, zanim cron zapisze przekroczenie czasu, aby zakolejkowana praca czatu nie pozostała za nieaktualną sesją przetwarzania.
  * Jeśli izolowana tura agenta zawiesi się przed startem runnera albo przed pierwszym wywołaniem modelu, cron zapisuje przekroczenie czasu specyficzne dla fazy, takie jak `setup timed out before runner start` lub `stalled before first model call (last phase: context-engine)`. Te mechanizmy nadzoru obejmują osadzonych dostawców i dostawców opartych na CLI, zanim ich zewnętrzny proces CLI zostanie faktycznie uruchomiony, i są limitowane niezależnie od długich wartości `timeoutSeconds`, aby awarie zimnego startu/uwierzytelniania/kontekstu ujawniały się szybko, zamiast czekać przez cały budżet zadania.


## Typy harmonogramów

Rodzaj | Flaga CLI | Opis  
---|---|---  
`at` | `--at` | Jednorazowy znacznik czasu (ISO 8601 lub względny jak `20m`)  
`every` | `--every` | Stały interwał  
`cron` | `--cron` | 5-polowe lub 6-polowe wyrażenie cron z opcjonalnym `--tz`  
  
Znaczniki czasu bez strefy czasowej są traktowane jako UTC. Dodaj `--tz America/New_York`, aby planować według lokalnego czasu zegarowego.

Powtarzające się wyrażenia na początek godziny są automatycznie rozpraszane o maksymalnie 5 minut, aby ograniczyć skoki obciążenia. Użyj `--exact`, aby wymusić precyzyjny czas, albo `--stagger 30s`, aby podać jawne okno.

### Dzień miesiąca i dzień tygodnia używają logiki OR

Wyrażenia Cron są parsowane przez [croner](<https://github.com/Hexagon/croner>). Gdy zarówno pola dnia miesiąca, jak i dnia tygodnia nie są symbolami wieloznacznymi, croner dopasowuje, gdy pasuje **którekolwiek** pole — nie oba. To standardowe zachowanie Vixie cron.

CodeCopy code
[code]
    # Intended: "9 AM on the 15th, only if it's a Monday"# Actual:   "9 AM on every 15th, AND 9 AM on every Monday"0 9 15 * 1
[/code]

To uruchamia się około 5–6 razy w miesiącu zamiast 0–1 razy w miesiącu. OpenClaw używa tutaj domyślnego zachowania OR Cronera. Aby wymagać obu warunków, użyj modyfikatora dnia tygodnia `+` Cronera (`0 9 15 * +1`) albo zaplanuj według jednego pola i sprawdź drugie w prompcie lub poleceniu zadania.

## Style wykonania

Styl | Wartość `--session` | Uruchamiane w | Najlepsze do  
---|---|---|---  
Sesja główna | `main` | Następna tura Heartbeat | Przypomnienia, zdarzenia systemowe  
Izolowane | `isolated` | Dedykowane `cron:<jobId>` | Raporty, prace w tle  
Bieżąca sesja | `current` | Powiązana w chwili utworzenia | Praca cykliczna świadoma kontekstu  
Sesja niestandardowa | `session:custom-id` | Trwała nazwana sesja | Przepływy pracy budujące na historii  
  
Main session vs isolated vs custom

Zadania **sesji głównej** dodają zdarzenie systemowe do kolejki i opcjonalnie wybudzają Heartbeat (`--wake now` lub `--wake next-heartbeat`). Te zdarzenia systemowe nie przedłużają świeżości resetu dziennego/bezczynności dla sesji docelowej. Zadania **izolowane** uruchamiają dedykowaną turę agenta ze świeżą sesją. **Sesje niestandardowe** (`session:xxx`) utrwalają kontekst między uruchomieniami, umożliwiając przepływy pracy, takie jak codzienne statusy, które budują na poprzednich podsumowaniach.

What 'fresh session' means for isolated jobs

Dla zadań izolowanych „świeża sesja” oznacza nowy identyfikator transkryptu/sesji dla każdego uruchomienia. OpenClaw może przenieść bezpieczne preferencje, takie jak ustawienia myślenia/szybkości/szczegółowości, etykiety oraz jawnie wybrane przez użytkownika nadpisania modelu/uwierzytelniania, ale nie dziedziczy otaczającego kontekstu rozmowy ze starszego wiersza cron: routingu kanału/grupy, zasad wysyłania lub kolejkowania, podniesienia uprawnień, pochodzenia ani powiązania czasu działania ACP. Użyj `current` lub `session:<id>`, gdy zadanie cykliczne ma celowo budować na tym samym kontekście rozmowy.

Runtime cleanup

Dla zadań izolowanych demontaż czasu działania obejmuje teraz sprzątanie przeglądarki w trybie najlepszych starań dla tej sesji cron. Błędy sprzątania są ignorowane, więc rzeczywisty wynik cron nadal ma pierwszeństwo.

Izolowane uruchomienia cron usuwają też wszystkie dołączone instancje czasu działania MCP utworzone dla zadania przez współdzieloną ścieżkę sprzątania czasu działania. Jest to zgodne ze sposobem demontażu klientów MCP sesji głównej i sesji niestandardowej, dzięki czemu izolowane zadania cron nie wyciekają procesów potomnych stdio ani długotrwałych połączeń MCP między uruchomieniami.

Subagent and Discord delivery

Gdy izolowane uruchomienia cron orkiestrują subagentów, dostarczanie również preferuje finalne wyjście potomka zamiast nieaktualnego tymczasowego tekstu rodzica. Jeśli potomkowie nadal działają, OpenClaw wycisza tę częściową aktualizację rodzica zamiast ją ogłaszać.

Dla tekstowych celów ogłoszeń Discord OpenClaw wysyła kanoniczny finalny tekst asystenta raz, zamiast odtwarzać zarówno strumieniowane/pośrednie payloady tekstowe, jak i finalną odpowiedź. Media i ustrukturyzowane payloady Discord nadal są dostarczane jako osobne payloady, aby załączniki i komponenty nie zostały pominięte.

### Opcje payloadu dla zadań izolowanych

Tekst promptu (wymagany dla izolowanych).

Nadpisanie modelu; używa wybranego dozwolonego modelu dla zadania.

Nadpisanie poziomu myślenia.

Pomiń wstrzykiwanie pliku bootstrapu obszaru roboczego.

Ogranicz narzędzia, których zadanie może używać, na przykład `--tools exec,read`.

`--model` używa wybranego dozwolonego modelu jako modelu głównego tego zadania. Nie jest to to samo co nadpisanie `/model` sesji czatu: skonfigurowane łańcuchy awaryjne nadal obowiązują, gdy model główny zadania zawiedzie. Jeśli żądany model nie jest dozwolony lub nie można go rozwiązać, cron kończy uruchomienie niepowodzeniem z jawnym błędem walidacji, zamiast po cichu wracać do wyboru modelu agenta/domyślnego zadania.

Zadania Cron mogą też zawierać `fallbacks` na poziomie payloadu. Gdy ta lista jest obecna, zastępuje skonfigurowany łańcuch awaryjny dla zadania. Użyj `fallbacks: []` w payloadzie/API zadania, gdy chcesz ścisłego uruchomienia cron, które próbuje tylko wybranego modelu. Jeśli zadanie ma `--model`, ale nie ma ani payloadu, ani skonfigurowanych fallbacków, OpenClaw przekazuje jawne puste nadpisanie fallbacków, aby główny model agenta nie został dołączony jako ukryty dodatkowy cel ponowienia.

Priorytet wyboru modelu dla zadań izolowanych jest następujący:

  1. Nadpisanie modelu haka Gmail (gdy uruchomienie pochodzi z Gmail i to nadpisanie jest dozwolone)
  2. `model` payloadu per zadanie
  3. Wybrane przez użytkownika zapisane nadpisanie modelu sesji cron
  4. Wybór modelu agenta/domyślnego


Tryb szybki również podąża za rozwiązaną aktywną selekcją. Jeśli konfiguracja wybranego modelu ma `params.fastMode`, izolowany cron domyślnie jej używa. Zapisane nadpisanie `fastMode` sesji nadal ma pierwszeństwo przed konfiguracją w obu kierunkach.

Jeśli izolowane uruchomienie trafi na przekazanie przełączenia modelu na żywo, cron ponawia próbę z przełączonym dostawcą/modelem i utrwala tę aktywną selekcję dla bieżącego uruchomienia przed ponowieniem. Gdy przełączenie przenosi też nowy profil uwierzytelniania, cron utrwala również nadpisanie tego profilu uwierzytelniania dla bieżącego uruchomienia. Ponowienia są ograniczone: po pierwszej próbie plus 2 ponowieniach przełączenia cron przerywa zamiast zapętlać się bez końca.

Zanim izolowane uruchomienie Cron trafi do runnera agenta, OpenClaw sprawdza osiągalne lokalne endpointy dostawców dla skonfigurowanych dostawców `api: "ollama"` i `api: "openai-completions"`, których `baseUrl` jest adresem loopback, siecią prywatną albo `.local`. Jeśli ten endpoint nie działa, uruchomienie jest zapisywane jako `skipped` z czytelnym błędem dostawcy/modelu zamiast rozpoczynania wywołania modelu. Wynik endpointu jest buforowany przez 5 minut, więc wiele oczekujących zadań używających tego samego niedziałającego lokalnego serwera Ollama, vLLM, SGLang lub LM Studio współdzieli jedną małą próbę zamiast tworzyć burzę żądań. Pominięte uruchomienia wstępnej kontroli dostawcy nie zwiększają backoffu błędów wykonania; włącz `failureAlert.includeSkipped`, gdy chcesz otrzymywać powtarzane powiadomienia o pominięciach.

## Dostarczanie i wynik

Tryb | Co się dzieje  
---|---  
`announce` | Dostarcza końcowy tekst awaryjnie do celu, jeśli agent go nie wysłał  
`webhook` | Wysyła payload zdarzenia zakończenia metodą POST do URL  
`none` | Brak awaryjnego dostarczania przez runner  
  
Użyj `--announce --channel telegram --to "-1001234567890"` do dostarczania na kanał. Dla tematów forum Telegram użyj `-1001234567890:topic:123`; bezpośredni wywołujący RPC/konfiguracji mogą także przekazać `delivery.threadId` jako ciąg znaków lub liczbę. Cele Slack/Discord/Mattermost powinny używać jawnych prefiksów (`channel:<id>`, `user:<id>`). Identyfikatory pokoi Matrix rozróżniają wielkość liter; użyj dokładnego identyfikatora pokoju albo formy `room:!room:server` z Matrix.

Gdy dostarczanie announce używa `channel: "last"` albo pomija `channel`, cel z prefiksem dostawcy, taki jak `telegram:123`, może wybrać kanał, zanim Cron wróci do historii sesji albo pojedynczego skonfigurowanego kanału. Selektorami dostawcy są tylko prefiksy deklarowane przez załadowany Plugin. Jeśli `delivery.channel` jest jawny, prefiks celu musi wskazywać tego samego dostawcę; na przykład `channel: "whatsapp"` z `to: "telegram:123"` zostanie odrzucone zamiast pozwolić WhatsApp zinterpretować identyfikator Telegram jako numer telefonu. Prefiksy rodzaju celu i usługi, takie jak `channel:<id>`, `user:<id>`, `imessage:<handle>` oraz `sms:<number>`, pozostają składnią celu należącą do kanału, a nie selektorami dostawcy.

Dla izolowanych zadań dostarczanie czatu jest współdzielone. Jeśli trasa czatu jest dostępna, agent może użyć narzędzia `message`, nawet gdy zadanie używa `--no-deliver`. Jeśli agent wysyła do skonfigurowanego/bieżącego celu, OpenClaw pomija awaryjny announce. W przeciwnym razie `announce`, `webhook` i `none` kontrolują tylko to, co runner robi z końcową odpowiedzią po turze agenta.

Gdy agent tworzy izolowane przypomnienie z aktywnego czatu, OpenClaw zapisuje zachowany cel dostarczania na żywo dla awaryjnej trasy announce. Wewnętrzne klucze sesji mogą być pisane małymi literami; cele dostarczania dostawcy nie są rekonstruowane z tych kluczy, gdy dostępny jest bieżący kontekst czatu.

Niejawne dostarczanie announce używa skonfigurowanych list dozwolonych kanałów do walidacji i przekierowania nieaktualnych celów. Zatwierdzenia z magazynu par DM nie są odbiorcami automatyzacji awaryjnej; ustaw `delivery.to` albo skonfiguruj wpis `allowFrom` kanału, gdy zaplanowane zadanie ma proaktywnie wysłać wiadomość do DM.

Powiadomienia o błędach używają osobnej ścieżki miejsca docelowego:

  * `cron.failureDestination` ustawia globalną wartość domyślną dla powiadomień o błędach.
  * `job.delivery.failureDestination` zastępuje ją dla danego zadania.
  * Jeśli żadna z tych wartości nie jest ustawiona, a zadanie już dostarcza przez `announce`, powiadomienia o błędach wracają teraz do tego podstawowego celu announce.
  * `delivery.failureDestination` jest obsługiwane tylko w zadaniach `sessionTarget="isolated"`, chyba że podstawowym trybem dostarczania jest `webhook`.
  * `failureAlert.includeSkipped: true` włącza dla zadania albo globalnej polityki alertów Cron powtarzane alerty o pominiętych uruchomieniach. Pominięte uruchomienia utrzymują osobny licznik kolejnych pominięć, więc nie wpływają na backoff błędów wykonania.


## Przykłady CLI

### Jednorazowe przypomnienie

bashCopy code
[code]
    openclaw cron add \  --name "Calendar check" \  --at "20m" \  --session main \  --system-event "Next heartbeat: check calendar." \  --wake now
[/code]

### Cykliczne izolowane zadanie

bashCopy code
[code]
    openclaw cron add \  --name "Morning brief" \  --cron "0 7 * * *" \  --tz "America/Los_Angeles" \  --session isolated \  --message "Summarize overnight updates." \  --announce \  --channel slack \  --to "channel:C1234567890"
[/code]

### Nadpisanie modelu i myślenia

bashCopy code
[code]
    openclaw cron add \  --name "Deep analysis" \  --cron "0 6 * * 1" \  --tz "America/Los_Angeles" \  --session isolated \  --message "Weekly deep analysis of project progress." \  --model "opus" \  --thinking high \  --announce
[/code]

## Webhooki

Gateway może udostępniać endpointy HTTP Webhook dla zewnętrznych wyzwalaczy. Włącz w konfiguracji:

json5Copy code
[code]
    {  hooks: {    enabled: true,    token: "shared-secret",    path: "/hooks",  },}
[/code]

### Uwierzytelnianie

Każde żądanie musi zawierać token hooka w nagłówku:

  * `Authorization: Bearer <token>` (zalecane)
  * `x-openclaw-token: <token>`


Tokeny w query string są odrzucane.

POST /hooks/wake

Kolejkuje zdarzenie systemowe dla głównej sesji:

bashCopy code
[code]
    curl -X POST http://127.0.0.1:18789/hooks/wake \  -H 'Authorization: Bearer SECRET' \  -H 'Content-Type: application/json' \  -d '{"text":"New email received","mode":"now"}'
[/code]

Opis zdarzenia.

`now` albo `next-heartbeat`.

POST /hooks/agent

Uruchamia izolowaną turę agenta:

bashCopy code
[code]
    curl -X POST http://127.0.0.1:18789/hooks/agent \  -H 'Authorization: Bearer SECRET' \  -H 'Content-Type: application/json' \  -d '{"message":"Summarize inbox","name":"Email","model":"openai/gpt-5.4"}'
[/code]

Pola: `message` (wymagane), `name`, `agentId`, `wakeMode`, `deliver`, `channel`, `to`, `model`, `fallbacks`, `thinking`, `timeoutSeconds`.

OPENCLAW_DOCS_MARKER:accordionOpen:IHRpdGxlPSJNYXBvd2FuZSBob29raSAoUE9TVCAvaG9va3MvPG5hbWU )"> Niestandardowe nazwy hooków są rozwiązywane przez `hooks.mappings` w konfiguracji. Mapowania mogą przekształcać dowolne payloady w akcje `wake` lub `agent` za pomocą szablonów albo transformacji kodu.

## Integracja Gmail PubSub

Połącz wyzwalacze skrzynki odbiorczej Gmail z OpenClaw przez Google PubSub.

### Konfiguracja kreatorem (zalecane)

bashCopy code
[code]
    openclaw webhooks gmail setup --account openclaw@gmail.com
[/code]

To zapisuje konfigurację `hooks.gmail`, włącza preset Gmail i używa Tailscale Funnel dla endpointu push.

### Automatyczny start Gateway

Gdy `hooks.enabled=true` i ustawione jest `hooks.gmail.account`, Gateway uruchamia `gog gmail watch serve` przy starcie i automatycznie odnawia watch. Ustaw `OPENCLAW_SKIP_GMAIL_WATCHER=1`, aby zrezygnować.

### Ręczna jednorazowa konfiguracja

* ### Wybierz projekt GCP

Wybierz projekt GCP, do którego należy klient OAuth używany przez `gog`:

bashCopy code
[code]
    gcloud auth logingcloud config set project <project-id>gcloud services enable gmail.googleapis.com pubsub.googleapis.com
[/code]

* ### Utwórz temat i przyznaj Gmail dostęp push

bashCopy code
[code]
    gcloud pubsub topics create gog-gmail-watchgcloud pubsub topics add-iam-policy-binding gog-gmail-watch \  --member=serviceAccount:gmail-api-push@system.gserviceaccount.com \  --role=roles/pubsub.publisher
[/code]

* ### Uruchom watch

bashCopy code
[code]
    gog gmail watch start \  --account openclaw@gmail.com \  --label INBOX \  --topic projects/<project-id>/topics/gog-gmail-watch
[/code]

### Nadpisanie modelu Gmail

json5Copy code
[code]
    {  hooks: {    gmail: {      model: "openrouter/meta-llama/llama-3.3-70b-instruct:free",      thinking: "off",    },  },}
[/code]

## Zarządzanie zadaniami

bashCopy code
[code]
    # List all jobsopenclaw cron list # Get one stored job as JSONopenclaw cron get <jobId> # Show one job, including resolved delivery routeopenclaw cron show <jobId> # Edit a jobopenclaw cron edit <jobId> --message "Updated prompt" --model "opus" # Force run a job nowopenclaw cron run <jobId> # Run only if dueopenclaw cron run <jobId> --due # View run historyopenclaw cron runs --id <jobId> --limit 50 # Delete a jobopenclaw cron remove <jobId> # Agent selection (multi-agent setups)openclaw cron add --name "Ops sweep" --cron "0 6 * * *" --session isolated --message "Check ops queue" --agent opsopenclaw cron edit <jobId> --clear-agent
[/code]

## Konfiguracja

json5Copy code
[code]
    {  cron: {    enabled: true,    store: "~/.openclaw/cron/jobs.json",    maxConcurrentRuns: 1,    retry: {      maxAttempts: 3,      backoffMs: [60000, 120000, 300000],      retryOn: ["rate_limit", "overloaded", "network", "server_error"],    },    webhookToken: "replace-with-dedicated-webhook-token",    sessionRetention: "24h",    runLog: { maxBytes: "2mb", keepLines: 2000 },  },}
[/code]

`maxConcurrentRuns` ogranicza zarówno zaplanowane wysyłanie Cron, jak i wykonywanie izolowanych tur agenta. Izolowane tury agenta Cron używają wewnętrznie dedykowanej kolejki wykonania `cron-nested`, więc zwiększenie tej wartości pozwala niezależnym uruchomieniom LLM z Cron postępować równolegle zamiast uruchamiać tylko ich zewnętrzne wrappery Cron. Współdzielona kolejka `nested` spoza Cron nie jest rozszerzana przez to ustawienie.

Boczny plik stanu środowiska uruchomieniowego jest wyprowadzany z `cron.store`: magazyn `.json`, taki jak `~/clawd/cron/jobs.json`, używa `~/clawd/cron/jobs-state.json`, natomiast ścieżka magazynu bez sufiksu `.json` dodaje `-state.json`.

Jeśli ręcznie edytujesz `jobs.json`, nie dodawaj `jobs-state.json` do kontroli wersji. OpenClaw używa tego bocznego pliku do oczekujących slotów, aktywnych znaczników, metadanych ostatniego uruchomienia i tożsamości harmonogramu, która mówi schedulerowi, kiedy zewnętrznie edytowane zadanie potrzebuje świeżego `nextRunAtMs`.

Wyłącz Cron: `cron.enabled: false` albo `OPENCLAW_SKIP_CRON=1`.

Zachowanie ponownych prób

**Ponowna próba jednorazowa** : błędy przejściowe (limit szybkości, przeciążenie, sieć, błąd serwera) są ponawiane do 3 razy z wykładniczym backoffem. Błędy trwałe wyłączają natychmiast.

**Ponowna próba cykliczna** : wykładniczy backoff (od 30 s do 60 min) między ponownymi próbami. Backoff resetuje się po następnym udanym uruchomieniu.

Konserwacja

`cron.sessionRetention` (domyślnie `24h`) usuwa odizolowane wpisy sesji uruchomień. `cron.runLog.maxBytes` / `cron.runLog.keepLines` automatycznie przycinają pliki dziennika uruchomień.

## Rozwiązywanie problemów

### Drabinka poleceń

bashCopy code
[code]
    openclaw statusopenclaw gateway statusopenclaw cron statusopenclaw cron listopenclaw cron runs --id <jobId> --limit 20openclaw system heartbeat lastopenclaw logs --followopenclaw doctor
[/code]

Cron się nie uruchamia

  * Sprawdź `cron.enabled` i zmienną środowiskową `OPENCLAW_SKIP_CRON`.
  * Upewnij się, że Gateway działa nieprzerwanie.
  * W przypadku harmonogramów `cron` zweryfikuj strefę czasową (`--tz`) względem strefy czasowej hosta.
  * `reason: not-due` w wyniku uruchomienia oznacza, że ręczne uruchomienie zostało sprawdzone za pomocą `openclaw cron run <jobId> --due`, a zadanie nie było jeszcze wymagalne.

Cron się uruchomił, ale nic nie dostarczono

  * Tryb dostarczania `none` oznacza, że nie jest oczekiwane wysyłanie awaryjne przez runnera. Agent nadal może wysłać wiadomość bezpośrednio za pomocą narzędzia `message`, gdy dostępna jest trasa czatu.
  * Brakujący/nieprawidłowy cel dostarczania (`channel`/`to`) oznacza, że pominięto wysyłkę wychodzącą.
  * W przypadku Matrix skopiowane lub starsze zadania z identyfikatorami pokojów `delivery.to` zapisanymi małymi literami mogą się nie powieść, ponieważ identyfikatory pokojów Matrix rozróżniają wielkość liter. Edytuj zadanie, podając dokładną wartość `!room:server` lub `room:!room:server` z Matrix.
  * Błędy uwierzytelniania kanału (`unauthorized`, `Forbidden`) oznaczają, że dostarczanie zostało zablokowane przez poświadczenia.
  * Jeśli odizolowane uruchomienie zwraca tylko token ciszy (`NO_REPLY` / `no_reply`), OpenClaw wstrzymuje bezpośrednie dostarczanie wychodzące i wstrzymuje także awaryjną ścieżkę kolejkowanego podsumowania, więc nic nie zostaje opublikowane z powrotem na czacie.
  * Jeśli agent powinien sam wysłać wiadomość do użytkownika, sprawdź, czy zadanie ma użyteczną trasę (`channel: "last"` z poprzednim czatem albo jawny kanał/cel).

Cron lub Heartbeat wydaje się uniemożliwiać przełączenie w stylu /new

  * Świeżość dziennego i bezczynnego resetu nie opiera się na `updatedAt`; zobacz [Zarządzanie sesją](</pl/concepts/session#session-lifecycle>).
  * Wybudzenia Cron, uruchomienia Heartbeat, powiadomienia exec i księgowanie Gateway mogą aktualizować wiersz sesji na potrzeby routingu/statusu, ale nie wydłużają `sessionStartedAt` ani `lastInteractionAt`.
  * W przypadku starszych wierszy utworzonych przed istnieniem tych pól OpenClaw może odzyskać `sessionStartedAt` z nagłówka sesji transkryptu JSONL, gdy plik jest nadal dostępny. Starsze wiersze bezczynności bez `lastInteractionAt` używają tego odzyskanego czasu rozpoczęcia jako swojej bazowej wartości bezczynności.

Pułapki stref czasowych

  * Cron bez `--tz` używa strefy czasowej hosta Gateway.
  * Harmonogramy `at` bez strefy czasowej są traktowane jako UTC.
  * `activeHours` Heartbeat używa skonfigurowanego rozpoznawania strefy czasowej.


## Powiązane

  * [Automatyzacja](</pl/automation>) — wszystkie mechanizmy automatyzacji w skrócie
  * [Zadania w tle](</pl/automation/tasks>) — rejestr zadań dla wykonań Cron
  * [Heartbeat](</pl/gateway/heartbeat>) — okresowe tury sesji głównej
  * [Strefa czasowa](</pl/concepts/timezone>) — konfiguracja strefy czasowej


Was this useful?YesNo