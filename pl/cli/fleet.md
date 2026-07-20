---
title: Flota
source_url: https://docs.openclaw.ai/pl/cli/fleet
scraped_at: 2026-07-20
---

ReferenceCLI commands

# `openclaw fleet`

`openclaw fleet` zarządza kompletnymi instancjami OpenClaw nazywanymi **komórkami**. Każda komórka ma własny Gateway, stan, poświadczenia, konta kanałów, kontener i port hosta dostępny tylko przez interfejs pętli zwrotnej. Należy używać jednej komórki dla każdej granicy zaufania dzierżawcy; nie należy używać jednego współdzielonego Gateway jako granicy w nieprzyjaznym środowisku wielodostępnym.

Fleet jest funkcją **eksperymentalną**. Nazwy poleceń, flagi, formaty danych wyjściowych i profil kontenera mogą zmieniać się między wydaniami bez okresu wycofywania.

Fleet obsługuje Docker i Podman. Domyślny obraz to `ghcr.io/openclaw/openclaw:latest`.

Fleet jest testowany na hostach z systemami Linux i macOS. Hosty z systemem Windows nie są obecnie przetestowane.

## Szybki start

bashCopy code
[code]
    openclaw fleet create acmeopenclaw fleet status acmeopenclaw fleet list
[/code]

`fleet create` jednorazowo wyświetla wygenerowany token Gateway wraz z adresem URL komórki. Token należy natychmiast zapisać, a następnie skonfigurować konta kanałów każdego dzierżawcy wewnątrz jego komórki.

## Identyfikatory dzierżawców

Identyfikatory dzierżawców muszą pasować do:

textCopy code
[code]
    ^[a-z0-9](?:[a-z0-9-]{0,38}[a-z0-9])?$
[/code]

Dozwolonych jest od 1 do 40 małych liter, cyfr i wewnętrznych łączników. Identyfikator musi zaczynać się i kończyć literą lub cyfrą. Wielkie litery, podkreślenia, ukośniki, kropki, białe znaki i ciągi służące do przechodzenia między katalogami, takie jak `../acme`, są odrzucane.

Identyfikator staje się częścią nazwy kontenera: `openclaw-cell-<tenant>`.

## `fleet create`

Utwórz komórkę i ją uruchom:

bashCopy code
[code]
    openclaw fleet create acme
[/code]

Utwórz komórkę Podman na stałym porcie bez jej uruchamiania:

bashCopy code
[code]
    openclaw fleet create acme \  --runtime podman \  --port 19125 \  --no-start
[/code]

Przekaż zmienne środowiskowe właściwe dla dzierżawcy, powtarzając `--env`:

bashCopy code
[code]
    openclaw fleet create acme \  --env TZ=America/Los_Angeles \  --env OPENCLAW_DISABLE_BONJOUR=1
[/code]

Klucze środowiskowe mogą zawierać litery, cyfry i podkreślenia oraz nie mogą zaczynać się cyfrą. Wartości muszą mieścić się w jednym wierszu, ponieważ Fleet przekazuje je przez chroniony plik środowiska uruchomieniowego. Fleet odrzuca próby zastąpienia zarządzanych zmiennych ścieżek kontenera i tokenu Gateway wymienionych w sekcji Układ pamięci masowej i kontenera.

### Opcje tworzenia

Opcja | Wartość domyślna | Opis  
---|---|---  
`--image <ref>` | `ghcr.io/openclaw/openclaw:latest` | Obraz kontenera dla komórki.  
`--runtime <runtime>` | `docker` | CLI kontenera: `docker` lub `podman`.  
`--port <number>` | Przydzielany automatycznie od `19100` | Port hosta na interfejsie pętli zwrotnej. Jawnie wybrany port nie może należeć do innej zarejestrowanej komórki.  
`--memory <value>` | `2g` | Limit pamięci kontenera w składni Docker/Podman.  
`--cpus <value>` | `2` | Limit procesora kontenera.  
`--disk <size>` | Brak | Ogranicza zapisywalną warstwę kontenera, gdy backend pamięci masowej obsługuje limity przydziału.  
`--network <mode>` | `bridge` | Tryb sieci wychodzącej: `bridge` lub `internal`.  
`--pids-limit <number>` | `512` | Maksymalna liczba procesów w kontenerze.  
`--env &lt;KEY=VALUE&gt;` | Brak | Przekazuje zmienną środowiskową do komórki. Należy powtórzyć dla wielu wartości.  
`--gateway-token <value>` | Losowy 32-znakowy token szesnastkowy | Używa podanego tokenu Gateway zamiast generowania nowego. Zobacz Obsługa tokenów.  
`--no-start` | Komórka jest uruchamiana | Tworzy kontener bez jego uruchamiania.  
`--json` | Dane wyjściowe czytelne dla człowieka | Wyświetla dane wyjściowe w formacie przeznaczonym do odczytu maszynowego.  
  
Automatyczne przydzielanie wybiera pierwszy nieużywany port rejestru o numerze `19100` lub wyższym. Fleet odrzuca zduplikowane identyfikatory dzierżawców i jawnie wskazane porty, które są już przypisane do innej komórki.

Odwołania do obrazów są przekazywane jako jeden argument środowiska uruchomieniowego kontenerów. Puste odwołania i wartości zaczynające się od `-` są odrzucane, aby obraz nie mógł zostać zinterpretowany jako opcja Docker lub Podman.

Wybrany punkt końcowy Docker lub Podman musi być lokalny. Fleet odrzuca zdalne konteksty Docker, punkty końcowe `DOCKER_HOST` i zdalne usługi Podman przed zarezerwowaniem portu lub utworzeniem stanu lokalnego. Zdalne hosty komórek nie są obsługiwane.

Gdy Fleet uruchamia nową komórkę, polecenie tworzenia czeka około minuty, aż jej Gateway odpowie na `/healthz`. Jeśli komórka nie osiągnie prawidłowego stanu, Fleet pozostawia jej kontener i wiersz rejestru bez zmian na potrzeby `fleet status`, `fleet logs` lub jawnego usunięcia. `--no-start` pomija tę kontrolę stanu. Wygenerowany token Gateway nowej komórki o nieprawidłowym stanie nie zostaje utracony — pozostaje w środowisku kontenera (`docker|podman inspect`), a ponieważ komórka nie obsłużyła jeszcze żadnego ruchu, użycie `fleet rm --force` i następnie ponowne utworzenie komórki jest zawsze bezpieczną alternatywą.

### Przypinanie według skrótu

Polecenia tworzenia i aktualizacji akceptują odwołania do obrazów przypięte według skrótu, takie jak `--image ghcr.io/openclaw/openclaw@sha256:<digest>`. Fleet przekazuje odwołanie do obrazu bez żadnych zmian do Docker lub Podman, co pozwala operatorowi utrzymać komórkę na niezmiennych bajtach obrazu zamiast na zmiennym tagu.

Wynik tworzenia zawiera identyfikator dzierżawcy, nazwę kontenera, port hosta, token Gateway i lokalny adres URL. Nawet w danych wyjściowych JSON wynik należy traktować jako zawierający dane poufne, ponieważ obejmuje token.

### Limity dysku

`--disk` ogranicza tylko zapisywalną warstwę kontenera. Montowane przez dowiązanie katalogi stanu i uwierzytelniania poszczególnych dzierżawców pozostają pamięcią hosta; jeśli te katalogi również wymagają sztywnego limitu, należy użyć limitów przydziału projektów systemu plików hosta.

Środowisko uruchomieniowe/backend pamięci masowej | Obsługa `--disk`  
---|---  
Docker overlay2 na XFS | Wymaga opcji montowania XFS `pquota`.  
Docker btrfs lub zfs | Obsługiwane przez sterownik pamięci masowej.  
Podman overlay | Wymaga bazowej pamięci masowej XFS.  
Inne backendy | Tworzenie kontenera kończy się niepowodzeniem z błędem demona i wskazówkami Fleet dotyczącymi backendu.  
  
### Zasady ruchu wychodzącego

Tryb | Docker | Podman  
---|---|---  
`bridge` | Obsługiwany; wychodzący ruch sieciowy jest domyślnie nieograniczony. | Obsługiwany; wychodzący ruch sieciowy jest domyślnie nieograniczony.  
`internal` | Odrzucany, ponieważ Docker nie zachowuje opublikowanego portu Gateway na interfejsie pętli zwrotnej w sieci wewnętrznej. | Obsługiwany; Gateway na interfejsie pętli zwrotnej pozostaje opublikowany, a wychodzący ruch sieciowy jest blokowany.  
  
W przypadku Docker należy zachować tryb mostu i wymuszać zasady ruchu wychodzącego za pomocą reguł zapory hosta, takich jak łańcuch `DOCKER-USER`.

## `fleet list`

Wyświetl komórki w kolejności identyfikatorów dzierżawców:

bashCopy code
[code]
    openclaw fleet listopenclaw fleet lsopenclaw fleet list --json
[/code]

Tabela zawiera:

Kolumna | Znaczenie  
---|---  
`tenant` | Identyfikator dzierżawcy.  
`state` | Bieżący stan kontenera uzyskany przez inspekcję Docker lub Podman. `unknown` oznacza, że środowisko uruchomieniowe było niedostępne albo istnieje kontener o nazwie komórki, lecz jego etykiety własności Fleet nie odpowiadają rekordowi rejestru (sygnał kolizji lub manipulacji — przed podjęciem działania należy sprawdzić go ręcznie).  
`port` | Port hosta na interfejsie pętli zwrotnej mapowany na Gateway komórki.  
`image` | Zarejestrowany obraz kontenera.  
`created` | Czas utworzenia komórki.  
  
Wiersze rejestru pozostają widoczne, gdy Docker lub Podman jest niedostępny; tylko bieżący stan zmienia się na `unknown`.

## `fleet status`

Sprawdź jedną komórkę:

bashCopy code
[code]
    openclaw fleet status acmeopenclaw fleet status acme --json
[/code]

Stan łączy wiersz rejestru floty, bieżącą inspekcję kontenera i krótkie żądanie wykonywane w miarę możliwości do:

textCopy code
[code]
    http://127.0.0.1:<host-port>/healthz
[/code]

Wynik kontroli stanu to `ok`, `failed` lub `skipped`. `/healthz` potwierdza aktywność Gateway, a nie pełną gotowość każdego skonfigurowanego kanału lub pluginu. Sonda jest pomijana, gdy brak użytecznego lokalnego punktu końcowego do sprawdzenia.

## `fleet logs`

Przesyłaj strumieniowo logi kontenera komórki bezpośrednio do terminala:

bashCopy code
[code]
    openclaw fleet logs acmeopenclaw fleet logs acme --followopenclaw fleet logs acme --tail 200openclaw fleet logs acme --since 10m
[/code]

Fleet weryfikuje etykiety własności zarejestrowanego kontenera przed odczytaniem jakichkolwiek logów, dlatego odmawia dostępu do obcego kontenera używającego oczekiwanej nazwy komórki. Strumień jest przypięty do identyfikatora sprawdzonego kontenera, więc równoczesne zastąpienie nie może przekierować go do nowszej generacji. Naciśnij Ctrl-C, aby zakończyć `--follow` bez traktowania zatrzymania przez operatora jako niepowodzenia polecenia. Dane wyjściowe logów są przepuszczane przez filtr redagujący, który zastępuje bieżący token Gateway komórki ciągiem `<redacted>`, zanim cokolwiek dotrze do terminala.

`fleet logs` nie ma trybu `--json`, ponieważ logi kontenera są nieprzetworzonym strumieniem stdout/stderr. W skryptach należy ograniczyć dane wyjściowe za pomocą `--tail` i użyć zwykłego przekierowania powłoki lub potoków.

## `fleet start`, `fleet stop` i `fleet restart`

Sterowanie istniejącą komórką przy użyciu jej zarejestrowanego środowiska uruchomieniowego:

bashCopy code
[code]
    openclaw fleet start acmeopenclaw fleet stop acmeopenclaw fleet restart acme
[/code]

Te polecenia działają na zarejestrowanej nazwie kontenera. Kończą się niepowodzeniem, jeśli dzierżawca jest nieznany lub zarejestrowane środowisko uruchomieniowe nie może wykonać operacji.

## `fleet upgrade`

Ponowne pobranie zarejestrowanego obrazu i zastąpienie kontenera komórki:

bashCopy code
[code]
    openclaw fleet upgrade acme
[/code]

Przeniesienie komórki do innego obrazu:

bashCopy code
[code]
    openclaw fleet upgrade acme --image ghcr.io/openclaw/openclaw:<version>
[/code]

Uaktualnienie pobiera obraz docelowy, sprawdza istniejący kontener i sieć poszczególnej komórki, zatrzymuje i usuwa kontener, a następnie tworzy go ponownie i uruchamia. Kontener zastępczy zachowuje ten sam port hosta, katalogi danych, sieć mostkową poszczególnej komórki, profil środowiska uruchomieniowego, limity zasobów, zasady ponownego uruchamiania, środowisko zarządzane przez Fleet oraz wartości pierwotnie podane za pomocą `--env`. Zamontowany stan pozostaje zachowany po zastąpieniu kontenera; domyślne środowisko obrazu może zmienić się wraz z obrazem docelowym.

Zastąpienie zostaje zatwierdzone dopiero po tym, jak jego Gateway odpowie na `/healthz` na porcie pętli zwrotnej komórki, zgodnie z kontraktem kontroli kondycji używanym przez oficjalny plik Compose. Kontener zastępczy, który zakończy działanie, wpadnie w pętlę awarii lub nie osiągnie prawidłowej kondycji w ciągu około minuty, zostanie usunięty, a poprzedni kontener przywrócony, dzięki czemu wadliwy obraz nie wyłączy działającej komórki.

Token Gateway celowo nie jest przechowywany w rejestrze Fleet. Przed usunięciem starego kontenera Fleet odczytuje jego środowisko i przenosi `OPENCLAW_GATEWAY_TOKEN` do kontenera zastępczego. Nie należy ręcznie usuwać starego kontenera przed uaktualnieniem, jeśli token nie istnieje w żadnym innym kontrolowanym miejscu.

## `fleet backup` i `fleet restore`

Tworzenie kopii zapasowej jednej zatrzymanej komórki:

bashCopy code
[code]
    openclaw fleet stop acmeopenclaw fleet backup acme --out ./acme.tgz
[/code]

Przywracanie tego archiwum do zarejestrowanej komórki:

bashCopy code
[code]
    openclaw fleet restore acme --from ./acme.tgz
[/code]

Są to polecenia wymagające uprawnień operatora hosta. Archiwa zawierają stan dzierżawcy i sekrety uwierzytelniania, są tworzone z trybem `0600` i muszą być przechowywane jak dane uwierzytelniające. Tworzenie kopii zapasowej odmawia działania dla uruchomionej komórki, aby stan SQLite został przechwycony spójnie. Przywracanie odmawia działania dla uruchomionej komórki, chyba że podano `--force`, zastępuje wyłącznie stan tego dzierżawcy, zmienia token Gateway i wyświetla nowy token jeden raz. Fleet tworzy kopię zapasową jednego dzierżawcy naraz; kopia zapasowa wszystkich dzierżawców jest oddzielną czynnością operatora.

Przywracanie wymaga istniejącego zatrzymanego kontenera, ponieważ sprawdzony profil jego środowiska uruchomieniowego dostarcza limity kontenera zastępczego, mapowanie użytkownika, pochodzenie środowiska oraz obraz. Jeśli zarejestrowany kontener został usunięty poza Fleet, należy najpierw uruchomić `fleet rm <tenant> --force` bez `--purge-data`, ponownie utworzyć komórkę z zamierzonym obrazem i `--no-start`, a następnie ponowić przywracanie. Pierwsze usunięcie pozostawia oba katalogi danych dzierżawcy bez zmian.

Oba polecenia przyjmują `--max-bytes <bytes>`, aby ograniczyć ilość archiwizowanych lub wyodrębnianych danych plików, i oba stosują ten sam stały budżet miliona segmentów ścieżek archiwum, dzięki czemu bomby archiwalne zawierające wyłącznie metadane nie mogą wyczerpać i-węzłów hosta, a każda zaakceptowana kopia zapasowa pozostaje możliwa do przywrócenia. Tworzenie kopii zapasowej przyjmuje `--out <path>`, a oba polecenia obsługują `--json`.

Archiwa zawierają wyłącznie zwykłe pliki i katalogi. Tworzenie kopii zapasowej nigdy nie podąża za dowiązaniami symbolicznymi ani nie przechowuje dowiązań symbolicznych, dowiązań twardych, gniazd czy węzłów urządzeń; liczba pominiętych elementów jest podawana w wyniku. Przywracanie odrzuca archiwa zawierające jakikolwiek inny typ wpisu. Odtwarzalne drzewa dowiązań symbolicznych, takie jak `node_modules` przestrzeni roboczej, muszą zostać ponownie zainstalowane wewnątrz komórki po przywróceniu.

## `fleet doctor`

Audyt wszystkich komórek lub jednego dzierżawcy bez zmiany stanu środowiska uruchomieniowego ani systemu plików:

bashCopy code
[code]
    openclaw fleet doctoropenclaw fleet doctor acme --json
[/code]

Doctor sprawdza lokalność środowiska uruchomieniowego, etykiety własności, kondycję, zabezpieczenia, limity zasobów, powiązanie portu pętli zwrotnej, obecność tokena, własność sieci i tryb ruchu wychodzącego oraz uprawnienia prywatnych katalogów stanu. Ostrzeżenia opisują zatrzymane komórki lub różnice własności; każde nieudane ustalenie powoduje ustawienie niezerowego kodu zakończenia procesu.

## `fleet rm`

Usunięcie zatrzymanej komórki ze środowiska uruchomieniowego i rejestru z zachowaniem danych dzierżawcy:

bashCopy code
[code]
    openclaw fleet rm acme
[/code]

Uruchomiony kontener wymaga `--force`:

bashCopy code
[code]
    openclaw fleet rm acme --force
[/code]

Trwałe usunięcie również danych komórki:

bashCopy code
[code]
    openclaw fleet rm acme --purge-data --force
[/code]

Fleet usuwa kontener komórki przed usunięciem jego dedykowanej sieci mostkowej. `--purge-data` wymaga `--force`. Przed rekurencyjnym usuwaniem Fleet rozpoznaje oba katalogi główne należące do Fleet oraz oba katalogi poszczególnych dzierżawców. Każdy cel musi być dokładnie oczekiwanym katalogiem końcowym dzierżawcy, znajdować się ściśle wewnątrz swojego katalogu głównego i nie może być dowiązaniem symbolicznym. Te kontrole zawierania zapobiegają przekierowaniu usuwania w inne miejsce przez uszkodzoną ścieżkę rejestru lub dowiązanie symboliczne między dzierżawcami.

Czyszczenie można ponowić, gdy dokładnie oczekiwany katalog dzierżawcy już nie istnieje. Pozwala to późniejszemu wywołaniu dokończyć czyszczenie po częściowej awarii systemu plików bez łagodzenia kontroli ścieżek dla katalogów, które nadal istnieją.

## Układ pamięci masowej i kontenerów

Stan komórki oraz klucze szyfrowania profilu uwierzytelniania używają oddzielnych ścieżek hosta dla poszczególnych dzierżawców w aktywnym katalogu stanu OpenClaw:

textCopy code
[code]
    <state-dir>/fleet/cells/<tenant>/<state-dir>/fleet/auth-profile-secrets/<tenant>/
[/code]

Pierwszy katalog jest montowany w `/home/node/.openclaw`. Drugi jest montowany w `/home/node/.config/openclaw`, zgodnie z punktem montowania klucza szyfrowania w oficjalnej konfiguracji Docker. Dzięki temu klucz szyfrowania nie jest ujawniony w zwykłym punkcie montowania stanu ani uwzględniany, gdy kopia zapasowa lub udostępnienie obejmuje tylko katalog stanu komórki. Oba katalogi pozostają zachowane po zwykłym usunięciu i uaktualnieniu; `fleet rm --purge-data --force` usuwa oba po oddzielnych kontrolach zawierania.

Przed pierwszym uruchomieniem Fleet inicjuje konfigurację komórki za pomocą `gateway.mode=local`, uwierzytelniania tokenem, powiązania kontenera z siecią LAN oraz źródeł Control UI dla przydzielonego portu hosta. Wartość tokena nie jest zapisywana w tej konfiguracji; pozostaje w środowisku kontenera.

Fleet przypina ścieżki kontenera oficjalnego obrazu za pomocą następujących wartości środowiskowych:

Zmienna | Wartość w kontenerze  
---|---  
`HOME` | `/home/node`  
`OPENCLAW_HOME` | `/home/node`  
`OPENCLAW_STATE_DIR` | `/home/node/.openclaw`  
`OPENCLAW_CONFIG_PATH` | `/home/node/.openclaw/openclaw.json`  
`OPENCLAW_WORKSPACE_DIR` | `/home/node/.openclaw/workspace`  
`OPENCLAW_GATEWAY_TOKEN` | Wygenerowany lub podany token komórki  
  
Oficjalny obraz domyślnie używa użytkownika `node` bez uprawnień roota, z identyfikatorem UID 1000. Fleet zachowuje możliwość zapisu w prywatnych montowaniach bind `0700` bez udostępniania ich wszystkim użytkownikom. Docker działający w trybie rootful uruchamia komórkę z identyfikatorami UID i GID wywołującego użytkownika bez uprawnień roota; Docker działający w trybie rootless używa UID 0 kontenera, który w przestrzeni nazw użytkownika demona jest mapowany na wywołującego nieuprzywilejowanego użytkownika hosta. Podman używa `keep-id` z identyfikatorami UID i GID wywołującego użytkownika. Gdy sam Fleet działa jako root z rootful środowiskiem uruchomieniowym, zachowuje użytkownika obrazu i przypisuje początkowe pliki montowania do UID/GID 1000.

Na hostach z SELinux montowania Docker i Podman otrzymują prywatne ponowne etykietowanie `:Z`. W przypadku przywracania lub przenoszenia danych komórki ścieżki montowane za pomocą bind muszą pozostać zapisywalne dla efektywnego użytkownika kontenera. Profil jest przystosowany do trybu rootless, ale Docker lub Podman musi być już skonfigurowany do działania w tym trybie na hoście; Fleet nie przekształca demona rootful w demona rootless.

## Profil zabezpieczeń

Fleet stosuje następujący profil do każdej komórki:

Mechanizm | Zastosowany profil | Uzasadnienie  
---|---|---  
Możliwości systemu Linux | `--cap-drop=ALL` | Gateway jest procesem Node.js i nie wymaga żadnych dodatkowych możliwości systemu Linux.  
Eskalacja uprawnień | `--security-opt no-new-privileges` | Uniemożliwia procesom uzyskiwanie uprawnień za pośrednictwem plików binarnych setuid lub setgid.  
Proces init | `--init` | Zbiera procesy potomne i przekazuje sygnały cyklu życia kontenera.  
Limit procesów | Domyślnie `--pids-limit 512` | Ogranicza wyczerpanie zasobów przez rozwidlanie i procesy.  
Limit pamięci | Domyślnie `--memory 2g` | Ogranicza użycie pamięci przez komórkę.  
Limit CPU | Domyślnie `--cpus 2` | Ogranicza użycie CPU przez komórkę.  
Dysk warstwy zapisywalnej | Opcjonalnie `--disk` | Ogranicza warstwę kontenera, gdy backend pamięci masowej środowiska uruchomieniowego obsługuje limity.  
Zasady ponownego uruchamiania | `--restart unless-stopped` | Ponownie uruchamia uszkodzoną komórkę bez zastępowania celowego zatrzymania.  
Publikowanie na hoście | Tylko `127.0.0.1:<host-port>:18789` | Chroni Gateway przed udostępnieniem przez interfejsy hosta z symbolami wieloznacznymi.  
Sieć komórki | Jeden most lub wewnętrzna sieć Podman na komórkę | Oddziela ruch między adresami IP kontenerów i opcjonalnie blokuje ruch wychodzący Podman.  
Tożsamość kontenera | Mapowanie użytkownika zgodne z hostem | Zachowuje możliwość zapisu w prywatnych montowaniach bind bez przyznawania dostępu wszystkim użytkownikom.  
Stan trwały | Montowania poszczególnych komórek; brak współdzielonego montowania stanu | Przechowuje konfigurację, dane uwierzytelniające, sesje i przestrzenie robocze dzierżawcy w jego drzewie danych.  
Polecenie kontenera | `node dist/index.js gateway --bind lan --port 18789` | Nasłuchuje w sieci kontenera, aby mapowanie portu hosta wyłącznie na pętli zwrotnej mogło się z nim połączyć.  
  
Fleet nigdy nie montuje `/var/run/docker.sock`, nie używa `--privileged` ani sieci hosta i nie dodaje możliwości. Most poszczególnej komórki stanowi granicę separacji między komórkami, a nie zaporę ruchu wychodzącego: komórki zachowują dostęp do sieci wymagany przez dostawców i kanały. Port pętli zwrotnej należy udostępnić przez serwer proxy, tunel SSH lub konfigurację sieci Tailscale zgodną z wdrożeniem. `http://127.0.0.1:<port>` jest bezpośrednio osiągalny tylko z hosta Fleet.

Ten profil oddziela kontenery dzierżawców, ale nie chroni dzierżawców przed operatorem Fleet, administratorem środowiska uruchomieniowego kontenerów ani przejętym hostem. Pełny model zaufania i opcje silniejszej izolacji opisano w sekcji [Hosting wielodzierżawczy](</pl/gateway/multi-tenant-hosting>).

## Obsługa tokenów

Domyślnie `fleet create` generuje kryptograficznie losowy, 32-znakowy szesnastkowy token Gateway i wyświetla go jeden raz w wyniku tworzenia. Należy przechowywać go w zatwierdzonym menedżerze sekretów i unikać zapisywania wyniku tworzenia w dziennikach.

`--gateway-token` umieszcza niestandardowy token w argumentach lokalnego procesu, które mogą zostać zachowane w historii powłoki lub być widoczne na listach procesów. Preferowany jest wygenerowany token, chyba że istniejący przepływ zarządzania sekretami wymaga podania wartości.

Token oraz każda wartość przekazana za pomocą `--env` znajdują się w środowisku kontenera. Fleet zapisuje je w krótkotrwałym pliku środowiskowym z trybem `0600`, przekazuje do Docker lub Podman wyłącznie ścieżkę tego pliku i usuwa go po zakończeniu polecenia środowiska uruchomieniowego. Wartości wpisane bezpośrednio w `openclaw fleet create --gateway-token ...` lub `--env KEY=VALUE` mogą nadal być widoczne w argumentach zewnętrznego procesu `openclaw` i historii powłoki.

Wartości środowiska kontenera nie są ukryte przed zaufanym operatorem hosta: administratorzy Docker lub Podman mogą je odczytać przez inspekcję kontenera. Informacja Fleet „shown once” opisuje standardowe dane wyjściowe CLI, a nie zabezpieczenie przed administratorem hosta.

## Powiązane

  * [Hosting wielodostępny](</pl/gateway/multi-tenant-hosting>)
  * [Docker](</pl/install/docker>)
  * [Podman](</pl/install/podman>)
  * [Bezpieczeństwo Gateway](</pl/gateway/security>)


Was this useful?YesNo

Open issue