---
title: Pluginy
source_url: https://docs.openclaw.ai/pl/cli/plugins
scraped_at: 2026-05-25
---

Zarządzaj pluginami Gateway, pakietami hooków i zgodnymi pakietami zbiorczymi.

[**System Plugin** Przewodnik dla użytkowników końcowych dotyczący instalowania, włączania i rozwiązywania problemów z pluginami. ](</pl/tools/plugin>) [**Zarządzanie pluginami** Szybkie przykłady instalowania, wyświetlania listy, aktualizowania, odinstalowywania i publikowania. ](</pl/plugins/manage-plugins>) [**Pakiety zbiorcze pluginów** Model zgodności pakietów zbiorczych. ](</pl/plugins/bundles>) [**Manifest Plugin** Pola manifestu i schemat konfiguracji. ](</pl/plugins/manifest>) [**Bezpieczeństwo** Wzmacnianie bezpieczeństwa instalacji pluginów. ](</pl/gateway/security>)

## Polecenia

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --jsonopenclaw plugins search <query>openclaw plugins search <query> --limit 20openclaw plugins search <query> --jsonopenclaw plugins install <path-or-spec>openclaw plugins inspect <id>openclaw plugins inspect <id> --runtimeopenclaw plugins inspect <id> --jsonopenclaw plugins inspect --allopenclaw plugins info <id>openclaw plugins enable <id>openclaw plugins disable <id>openclaw plugins registryopenclaw plugins registry --refreshopenclaw plugins uninstall <id>openclaw plugins doctoropenclaw plugins update <id-or-npm-spec>openclaw plugins update --allopenclaw plugins marketplace list <marketplace>openclaw plugins marketplace list <marketplace> --json
[/code]

Aby zbadać powolną instalację, inspekcję, odinstalowanie lub odświeżenie rejestru, uruchom polecenie z `OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1`. Ślad zapisuje czasy faz do stderr i zachowuje możliwość parsowania wyjścia JSON. Zobacz [Debugowanie](</pl/help/debugging#plugin-lifecycle-trace>).

### Instalacja

bashCopy code
[code]
    openclaw plugins search "calendar"                   # search ClawHub pluginsopenclaw plugins install <package>                      # npm by defaultopenclaw plugins install clawhub:<package>              # ClawHub onlyopenclaw plugins install npm:<package>                  # npm onlyopenclaw plugins install npm-pack:<path.tgz>            # local npm pack through npm install semanticsopenclaw plugins install git:github.com/<owner>/<repo>  # git repoopenclaw plugins install git:github.com/<owner>/<repo>@<ref>openclaw plugins install <package> --force              # overwrite existing installopenclaw plugins install <package> --pin                # pin versionopenclaw plugins install <package> --dangerously-force-unsafe-installopenclaw plugins install <path>                         # local pathopenclaw plugins install <plugin>@<marketplace>         # marketplaceopenclaw plugins install <plugin> --marketplace <name>  # marketplace (explicit)openclaw plugins install <plugin> --marketplace https://github.com/<owner>/<repo>
[/code]

Opiekunowie testujący instalacje wykonywane podczas konfiguracji mogą zastąpić automatyczne źródła instalacji pluginów za pomocą chronionych zmiennych środowiskowych. Zobacz [Zastąpienia instalacji pluginów](</pl/plugins/install-overrides>).

`plugins search` odpytuje ClawHub o możliwe do zainstalowania pakiety pluginów i wypisuje nazwy pakietów gotowe do instalacji. Przeszukuje pakiety code-plugin i bundle-plugin, a nie Skills. Użyj `openclaw skills search` dla Skills z ClawHub.

Dołączanie konfiguracji i naprawa nieprawidłowej konfiguracji

Jeśli sekcja `plugins` jest wspierana przez jednoplikowe `$include`, `plugins install/update/enable/disable/uninstall` zapisuje zmiany do tego dołączonego pliku i pozostawia `openclaw.json` bez zmian. Dołączenia główne, tablice dołączeń i dołączenia z równoległymi nadpisaniami kończą się bez zmian zamiast spłaszczać konfigurację. Zobacz [Dołączanie konfiguracji](</pl/gateway/configuration>), aby poznać obsługiwane kształty.

Jeśli konfiguracja jest nieprawidłowa podczas instalacji, `plugins install` zwykle kończy się bez zmian i informuje, aby najpierw uruchomić `openclaw doctor --fix`. Podczas uruchamiania Gateway i przeładowania na gorąco nieprawidłowa konfiguracja pluginów kończy się bez zmian jak każda inna nieprawidłowa konfiguracja; `openclaw doctor --fix` może poddać kwarantannie nieprawidłowy wpis pluginu. Jedynym udokumentowanym wyjątkiem podczas instalacji jest wąska ścieżka odzyskiwania dołączonego pluginu dla pluginów, które jawnie wybierają `openclaw.install.allowInvalidConfigRecovery`.

\--force oraz ponowna instalacja a aktualizacja

`--force` ponownie używa istniejącego celu instalacji i nadpisuje już zainstalowany plugin lub pakiet hooków w miejscu. Użyj tego, gdy celowo ponownie instalujesz ten sam identyfikator z nowej ścieżki lokalnej, archiwum, pakietu ClawHub lub artefaktu npm. Do rutynowych aktualizacji już śledzonego pluginu npm preferuj `openclaw plugins update <id-or-npm-spec>`.

Jeśli uruchomisz `plugins install` dla identyfikatora pluginu, który jest już zainstalowany, OpenClaw zatrzyma się i wskaże `plugins update <id-or-npm-spec>` dla zwykłej aktualizacji albo `plugins install <package> --force`, gdy rzeczywiście chcesz nadpisać bieżącą instalację z innego źródła.

Zakres --pin

`--pin` dotyczy tylko instalacji npm. Nie jest obsługiwane z instalacjami `git:`; użyj jawnego odwołania git, takiego jak `git:github.com/acme/plugin@v1.2.3`, gdy chcesz przypięte źródło. Nie jest obsługiwane z `--marketplace`, ponieważ instalacje z marketplace utrwalają metadane źródła marketplace zamiast specyfikacji npm.

\--dangerously-force-unsafe-install

`--dangerously-force-unsafe-install` to opcja awaryjna dla fałszywych alarmów w wbudowanym skanerze niebezpiecznego kodu. Pozwala kontynuować instalację nawet wtedy, gdy wbudowany skaner zgłasza ustalenia `critical`, ale **nie** omija blokad zasad hooka pluginu `before_install` i **nie** omija niepowodzeń skanowania.

Ta flaga CLI dotyczy przepływów instalacji/aktualizacji pluginów. Instalacje zależności Skills obsługiwane przez Gateway używają odpowiadającego jej nadpisania żądania `dangerouslyForceUnsafeInstall`, natomiast `openclaw skills install` pozostaje osobnym przepływem pobierania/instalacji Skills z ClawHub.

Jeśli plugin opublikowany przez Ciebie w ClawHub jest blokowany przez skan rejestru, użyj kroków dla wydawcy w [ClawHub](</pl/clawhub/security>).

Pakiety hooków i specyfikacje npm

`plugins install` jest także powierzchnią instalacji dla pakietów hooków, które udostępniają `openclaw.hooks` w `package.json`. Użyj `openclaw hooks` do filtrowanej widoczności hooków i włączania poszczególnych hooków, a nie do instalacji pakietów.

Specyfikacje npm są **tylko rejestrowe** (nazwa pakietu + opcjonalna **dokładna wersja** lub **dist-tag**). Specyfikacje Git/URL/file i zakresy semver są odrzucane. Instalacje zależności działają lokalnie dla projektu z `--ignore-scripts` ze względów bezpieczeństwa, nawet gdy powłoka ma globalne ustawienia instalacji npm. Zarządzane korzenie npm pluginów dziedziczą `overrides` npm na poziomie pakietu OpenClaw, więc piny bezpieczeństwa hosta dotyczą także wyniesionych zależności pluginów.

Użyj `npm:<package>`, gdy chcesz jawnie wskazać rozwiązywanie przez npm. Same specyfikacje pakietów również instalują bezpośrednio z npm podczas przejścia startowego.

Same specyfikacje i `@latest` pozostają na ścieżce stabilnej. Oznaczone datą wersje korekcyjne OpenClaw, takie jak `2026.5.3-1`, są stabilnymi wydaniami dla tego sprawdzenia. Jeśli npm rozwiąże którąkolwiek z nich do wydania wstępnego, OpenClaw zatrzyma się i poprosi o jawne wyrażenie zgody za pomocą tagu wydania wstępnego, takiego jak `@beta`/`@rc`, lub dokładnej wersji wydania wstępnego, takiej jak `@1.2.3-beta.4`.

Jeśli sama specyfikacja instalacji pasuje do oficjalnego identyfikatora pluginu (na przykład `diffs`), OpenClaw instaluje bezpośrednio wpis katalogu. Aby zainstalować pakiet npm o tej samej nazwie, użyj jawnej specyfikacji z zakresem (na przykład `@scope/diffs`).

Repozytoria Git

Użyj `git:<repo>`, aby instalować bezpośrednio z repozytorium git. Obsługiwane formy obejmują `git:github.com/owner/repo`, `git:owner/repo`, pełne adresy URL klonowania `https://`, `ssh://`, `git://`, `file://` oraz `git@host:owner/repo.git`. Dodaj `@<ref>` lub `#<ref>`, aby przed instalacją przełączyć się na gałąź, tag lub commit.

Instalacje Git klonują do katalogu tymczasowego, przełączają się na żądane odwołanie, gdy jest obecne, a następnie używają zwykłego instalatora katalogu pluginu. Oznacza to, że walidacja manifestu, skanowanie niebezpiecznego kodu, prace instalacyjne menedżera pakietów i rekordy instalacji zachowują się jak instalacje npm. Zarejestrowane instalacje Git obejmują źródłowy URL/ref oraz rozwiązany commit, aby `openclaw plugins update` mógł później ponownie rozwiązać źródło.

Po instalacji z git użyj `openclaw plugins inspect <id> --runtime --json`, aby zweryfikować rejestracje środowiska uruchomieniowego, takie jak metody gateway i polecenia CLI. Jeśli plugin zarejestrował korzeń CLI za pomocą `api.registerCli`, wykonaj to polecenie bezpośrednio przez główny CLI OpenClaw, na przykład `openclaw demo-plugin ping`.

Archiwa

Obsługiwane archiwa: `.zip`, `.tgz`, `.tar.gz`, `.tar`. Archiwa natywnych pluginów OpenClaw muszą zawierać prawidłowy `openclaw.plugin.json` w wyodrębnionym katalogu głównym pluginu; archiwa zawierające tylko `package.json` są odrzucane, zanim OpenClaw zapisze rekordy instalacji.

Użyj `npm-pack:<path.tgz>`, gdy plik jest tarballem npm-pack i chcesz przetestować tę samą zarządzaną ścieżkę instalacji korzenia npm, która jest używana przez instalacje z rejestru, w tym weryfikację `package-lock.json`, skanowanie wyniesionych zależności i rekordy instalacji npm. Zwykłe ścieżki archiwów nadal instalują się jako lokalne archiwa pod głównym katalogiem rozszerzeń pluginów.

Instalacje z marketplace Claude są również obsługiwane.

Instalacje ClawHub używają jawnego lokatora `clawhub:<package>`:

bashCopy code
[code]
    openclaw plugins install clawhub:openclaw-codex-app-serveropenclaw plugins install clawhub:openclaw-codex-app-server@1.2.3
[/code]

Same specyfikacje pluginów bezpieczne dla npm instalują z npm domyślnie podczas przejścia startowego:

bashCopy code
[code]
    openclaw plugins install openclaw-codex-app-server
[/code]

Użyj `npm:`, aby jawnie wskazać rozwiązywanie tylko przez npm:

bashCopy code
[code]
    openclaw plugins install npm:openclaw-codex-app-serveropenclaw plugins install npm:@scope/plugin-name@1.0.1
[/code]

OpenClaw sprawdza deklarowaną zgodność API pluginu / minimalną zgodność z Gateway przed instalacją. Gdy wybrana wersja ClawHub publikuje artefakt ClawPack, OpenClaw pobiera wersjonowany pakiet npm `.tgz`, weryfikuje nagłówek skrótu ClawHub oraz skrót artefaktu, a następnie instaluje go przez standardową ścieżkę archiwum. Starsze wersje ClawHub bez metadanych ClawPack nadal instalują się przez starszą ścieżkę weryfikacji archiwum pakietu. Zarejestrowane instalacje zachowują metadane źródła ClawHub, rodzaj artefaktu, integralność npm, sumę shasum npm, nazwę tarballa oraz fakty skrótu ClawPack na potrzeby późniejszych aktualizacji. Niewersjonowane instalacje ClawHub zachowują niewersjonowaną zarejestrowaną specyfikację, aby `openclaw plugins update` mogło śledzić nowsze wydania ClawHub; jawne selektory wersji lub tagów, takie jak `clawhub:pkg@1.2.3` i `clawhub:pkg@beta`, pozostają przypięte do tego selektora.

#### Skrót marketplace

Użyj skrótu `plugin@marketplace`, gdy nazwa marketplace istnieje w lokalnej pamięci podręcznej rejestru Claude pod `~/.claude/plugins/known_marketplaces.json`:

bashCopy code
[code]
    openclaw plugins marketplace list <marketplace-name>openclaw plugins install <plugin-name>@<marketplace-name>
[/code]

Użyj `--marketplace`, gdy chcesz jawnie przekazać źródło marketplace:

bashCopy code
[code]
    openclaw plugins install <plugin-name> --marketplace <marketplace-name>openclaw plugins install <plugin-name> --marketplace <owner/repo>openclaw plugins install <plugin-name> --marketplace https://github.com/<owner>/<repo>openclaw plugins install <plugin-name> --marketplace ./my-marketplace
[/code]

### Źródła marketplace

  * znana nazwa marketplace Claude z `~/.claude/plugins/known_marketplaces.json`
  * lokalny katalog główny marketplace lub ścieżka `marketplace.json`
  * skrót repozytorium GitHub, taki jak `owner/repo`
  * URL repozytorium GitHub, taki jak `https://github.com/owner/repo`
  * URL git


### Reguły zdalnego marketplace

W przypadku zdalnych marketplace ładowanych z GitHub lub git wpisy pluginów muszą pozostać wewnątrz sklonowanego repozytorium marketplace. OpenClaw akceptuje względne źródła ścieżek z tego repozytorium i odrzuca źródła pluginów HTTP(S), ścieżki bezwzględne, git, GitHub oraz inne źródła niebędące ścieżkami ze zdalnych manifestów.

Dla lokalnych ścieżek i archiwów OpenClaw automatycznie wykrywa:

  * natywne pluginy OpenClaw (`openclaw.plugin.json`)
  * pakiety zgodne z Codex (`.codex-plugin/plugin.json`)
  * pakiety zgodne z Claude (`.claude-plugin/plugin.json` lub domyślny układ komponentów Claude)
  * pakiety zgodne z Cursor (`.cursor-plugin/plugin.json`)


### Lista

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --jsonopenclaw plugins search <query>openclaw plugins search <query> --limit 20openclaw plugins search <query> --json
[/code]

Pokaż tylko włączone pluginy.

Przełącz z widoku tabeli na szczegółowe wiersze dla każdego pluginu z metadanymi źródła/pochodzenia/wersji/aktywacji.

Inwentarz czytelny maszynowo oraz diagnostyka rejestru i stan instalacji zależności pakietów.

`plugins search` to zdalne wyszukiwanie w katalogu ClawHub. Nie sprawdza lokalnego stanu, nie modyfikuje konfiguracji, nie instaluje pakietów ani nie ładuje kodu runtime pluginu. Wyniki wyszukiwania zawierają nazwę pakietu ClawHub, rodzinę, kanał, wersję, podsumowanie oraz wskazówkę instalacji, taką jak `openclaw plugins install clawhub:<package>`.

W przypadku pracy nad dołączonym pluginem wewnątrz spakowanego obrazu Docker zamontuj katalog źródłowy pluginu przez bind mount na odpowiadającą mu spakowaną ścieżkę źródłową, taką jak `/app/extensions/synology-chat`. OpenClaw odkryje tę zamontowaną nakładkę źródłową przed `/app/dist/extensions/synology-chat`; zwykły skopiowany katalog źródłowy pozostaje nieaktywny, więc standardowe instalacje pakietowe nadal używają skompilowanego dist.

Do debugowania hooków runtime:

  * `openclaw plugins inspect <id> --runtime --json` pokazuje zarejestrowane hooki i diagnostykę z przebiegu inspekcji po załadowaniu modułu. Inspekcja runtime nigdy nie instaluje zależności; użyj `openclaw doctor --fix`, aby wyczyścić starszy stan zależności lub odzyskać brakujące pluginy możliwe do pobrania, do których odwołuje się konfiguracja.
  * `openclaw gateway status --deep --require-rpc` potwierdza osiągalny Gateway, wskazówki dotyczące usługi/procesu, ścieżkę konfiguracji i stan RPC.
  * Niedołączone hooki konwersacji (`llm_input`, `llm_output`, `before_model_resolve`, `before_agent_reply`, `before_agent_run`, `before_agent_finalize`, `agent_end`) wymagają `plugins.entries.<id>.hooks.allowConversationAccess=true`.


Użyj `--link`, aby uniknąć kopiowania lokalnego katalogu (dodaje do `plugins.load.paths`):

bashCopy code
[code]
    openclaw plugins install -l ./my-plugin
[/code]

### Indeks pluginów

Metadane instalacji pluginu są stanem zarządzanym maszynowo, a nie konfiguracją użytkownika. Instalacje i aktualizacje zapisują je do `plugins/installs.json` w aktywnym katalogu stanu OpenClaw. Jego mapa najwyższego poziomu `installRecords` jest trwałym źródłem metadanych instalacji, w tym rekordów dla uszkodzonych lub brakujących manifestów pluginów. Tablica `plugins` jest pochodzącą z manifestów pamięcią podręczną zimnego rejestru. Plik zawiera ostrzeżenie, aby go nie edytować, i jest używany przez `openclaw plugins update`, odinstalowywanie, diagnostykę oraz zimny rejestr pluginów.

Gdy OpenClaw widzi dostarczone starsze rekordy `plugins.installs` w konfiguracji, odczyty runtime traktują je jako dane wejściowe zgodności bez przepisywania `openclaw.json`. Jawne zapisy pluginów i `openclaw doctor --fix` przenoszą te rekordy do indeksu pluginów i usuwają klucz konfiguracji, gdy zapisy konfiguracji są dozwolone; jeśli którykolwiek zapis się nie powiedzie, rekordy konfiguracji zostają zachowane, aby metadane instalacji nie zostały utracone.

### Odinstalowanie

bashCopy code
[code]
    openclaw plugins uninstall <id>openclaw plugins uninstall <id> --dry-runopenclaw plugins uninstall <id> --keep-files
[/code]

`uninstall` usuwa rekordy pluginu z `plugins.entries`, utrwalonego indeksu pluginów, wpisów list allow/deny pluginów oraz linkowanych wpisów `plugins.load.paths`, gdy ma to zastosowanie. O ile nie ustawiono `--keep-files`, odinstalowanie usuwa również śledzony zarządzany katalog instalacji, gdy znajduje się on wewnątrz katalogu głównego rozszerzeń pluginów OpenClaw. W przypadku pluginów Active Memory slot pamięci resetuje się do `memory-core`.

### Aktualizacja

bashCopy code
[code]
    openclaw plugins update <id-or-npm-spec>openclaw plugins update --allopenclaw plugins update <id-or-npm-spec> --dry-runopenclaw plugins update @openclaw/voice-callopenclaw plugins update openclaw-codex-app-server --dangerously-force-unsafe-install
[/code]

Aktualizacje dotyczą śledzonych instalacji pluginów w zarządzanym indeksie pluginów oraz śledzonych instalacji pakietów hooków w `hooks.internal.installs`.

Rozwiązywanie id pluginu kontra specyfikacja npm

Gdy przekazujesz id pluginu, OpenClaw ponownie używa zarejestrowanej specyfikacji instalacji dla tego pluginu. Oznacza to, że wcześniej zapisane dist-tags, takie jak `@beta`, oraz dokładnie przypięte wersje nadal są używane przy późniejszych uruchomieniach `update <id>`.

W przypadku instalacji npm możesz również przekazać jawną specyfikację pakietu npm z dist-tag lub dokładną wersją. OpenClaw rozwiązuje tę nazwę pakietu z powrotem do śledzonego rekordu pluginu, aktualizuje ten zainstalowany plugin i zapisuje nową specyfikację npm na potrzeby przyszłych aktualizacji opartych na id.

Przekazanie nazwy pakietu npm bez wersji lub tagu również rozwiązuje się z powrotem do śledzonego rekordu pluginu. Użyj tego, gdy plugin został przypięty do dokładnej wersji i chcesz przenieść go z powrotem na domyślną linię wydań rejestru.

Aktualizacje kanału beta

`openclaw plugins update` ponownie używa śledzonej specyfikacji pluginu, chyba że przekażesz nową specyfikację. `openclaw update` dodatkowo zna aktywny kanał aktualizacji OpenClaw: na kanale beta rekordy pluginów npm i ClawHub z domyślnej linii najpierw próbują `@beta`, a następnie wracają do zarejestrowanej specyfikacji default/latest, jeśli nie istnieje wydanie beta pluginu. Ten fallback jest raportowany jako ostrzeżenie i nie powoduje niepowodzenia aktualizacji core. Dokładne wersje i jawne tagi pozostają przypięte do tego selektora.

Sprawdzanie wersji i dryf integralności

Przed aktualizacją npm na żywo OpenClaw sprawdza zainstalowaną wersję pakietu względem metadanych rejestru npm. Jeśli zainstalowana wersja i zarejestrowana tożsamość artefaktu już pasują do rozwiązanego celu, aktualizacja jest pomijana bez pobierania, ponownej instalacji ani przepisywania `openclaw.json`.

Gdy istnieje zapisany skrót integralności, a skrót pobranego artefaktu się zmienia, OpenClaw traktuje to jako dryf artefaktu npm. Interaktywne polecenie `openclaw plugins update` wypisuje oczekiwane i rzeczywiste skróty oraz prosi o potwierdzenie przed kontynuowaniem. Nieinteraktywne helpery aktualizacji kończą się bezpiecznym niepowodzeniem, chyba że wywołujący dostarczy jawną zasadę kontynuacji.

\--dangerously-force-unsafe-install przy aktualizacji

`--dangerously-force-unsafe-install` jest również dostępne w `plugins update` jako awaryjne obejście dla fałszywych alarmów wbudowanego skanowania niebezpiecznego kodu podczas aktualizacji pluginów. Nadal nie omija blokad zasad pluginu `before_install` ani blokowania po niepowodzeniu skanowania i dotyczy tylko aktualizacji pluginów, a nie aktualizacji pakietów hooków.

### Inspekcja

bashCopy code
[code]
    openclaw plugins inspect <id>openclaw plugins inspect <id> --runtimeopenclaw plugins inspect <id> --json
[/code]

Inspekcja pokazuje tożsamość, stan ładowania, źródło, możliwości manifestu, flagi zasad, diagnostykę, metadane instalacji, możliwości pakietu oraz wszelkie wykryte wsparcie serwerów MCP lub LSP bez domyślnego importowania runtime pluginu. Dodaj `--runtime`, aby załadować moduł pluginu i uwzględnić zarejestrowane hooki, narzędzia, polecenia, usługi, metody Gateway oraz trasy HTTP. Inspekcja runtime raportuje brakujące zależności pluginu bezpośrednio; instalacje i naprawy pozostają w `openclaw plugins install`, `openclaw plugins update` i `openclaw doctor --fix`.

Polecenia CLI należące do pluginu są zwykle instalowane jako główne grupy poleceń `openclaw`, ale pluginy mogą też rejestrować zagnieżdżone polecenia pod nadrzędnym elementem core, takim jak `openclaw nodes`. Gdy `inspect --runtime` pokaże polecenie pod `cliCommands`, uruchom je pod wymienioną ścieżką; na przykład plugin rejestrujący `demo-git` można zweryfikować poleceniem `openclaw demo-git ping`.

Każdy plugin jest klasyfikowany według tego, co faktycznie rejestruje w runtime:

  * **plain-capability** — jeden typ capability (np. plugin tylko dla dostawcy)
  * **hybrid-capability** — wiele typów capability (np. tekst + mowa + obrazy)
  * **hook-only** — tylko hooki, bez capabilities ani powierzchni
  * **non-capability** — narzędzia/polecenia/usługi, ale bez capabilities


Więcej informacji o modelu capability znajdziesz w [kształtach Plugin](</pl/plugins/architecture#plugin-shapes>).

### Doctor

bashCopy code
[code]
    openclaw plugins doctor
[/code]

`doctor` raportuje błędy ładowania pluginów, diagnostykę manifestu/wykrywania oraz powiadomienia o zgodności. Gdy wszystko jest poprawne, wypisuje `No plugin issues detected.`

Jeśli skonfigurowany plugin jest obecny na dysku, ale zablokowany przez kontrole bezpieczeństwa ścieżek loadera, walidacja konfiguracji zachowuje wpis pluginu i zgłasza go jako `present but blocked`. Napraw poprzedzającą diagnostykę zablokowanego pluginu, taką jak własność ścieżki lub uprawnienia do zapisu dla wszystkich, zamiast usuwać konfigurację `plugins.entries.<id>` lub `plugins.allow`.

W przypadku błędów kształtu modułu, takich jak brakujące eksporty `register`/`activate`, uruchom ponownie z `OPENCLAW_PLUGIN_LOAD_DEBUG=1`, aby dołączyć zwięzłe podsumowanie kształtu eksportów w danych wyjściowych diagnostyki.

### Rejestr

bashCopy code
[code]
    openclaw plugins registryopenclaw plugins registry --refreshopenclaw plugins registry --json
[/code]

Lokalny rejestr pluginów to utrwalony model zimnego odczytu OpenClaw dla tożsamości zainstalowanych pluginów, ich włączenia, metadanych źródła i własności wkładów. Zwykłe uruchamianie, wyszukiwanie właściciela dostawcy, klasyfikacja konfiguracji kanału i inwentarz pluginów mogą go odczytywać bez importowania modułów runtime pluginów.

Użyj `plugins registry`, aby sprawdzić, czy utrwalony rejestr jest obecny, aktualny lub nieaktualny. Użyj `--refresh`, aby odbudować go z utrwalonego indeksu pluginów, zasad konfiguracji oraz metadanych manifestu/pakietu. To ścieżka naprawy, a nie ścieżka aktywacji runtime.

`openclaw doctor --fix` naprawia także zarządzane rozbieżności npm sąsiadujące z rejestrem: jeśli osierocony lub odzyskany pakiet `@openclaw/*` pod zarządzanym katalogiem głównym npm pluginów przesłania plugin dołączony do pakietu, doctor usuwa ten nieaktualny pakiet i odbudowuje rejestr, aby uruchamianie walidowało się względem dołączonego manifestu. Doctor ponownie łączy także pakiet hosta `openclaw` z zarządzanymi pluginami npm, które deklarują `peerDependencies.openclaw`, dzięki czemu lokalne importy runtime pakietu, takie jak `openclaw/plugin-sdk/*`, rozwiązują się po aktualizacjach lub naprawach npm.

### Marketplace

bashCopy code
[code]
    openclaw plugins marketplace list <source>openclaw plugins marketplace list <source> --json
[/code]

Lista Marketplace przyjmuje lokalną ścieżkę marketplace, ścieżkę `marketplace.json`, skrót GitHub w rodzaju `owner/repo`, URL repozytorium GitHub lub URL git. `--json` wypisuje rozpoznaną etykietę źródła oraz sparsowany manifest marketplace i wpisy pluginów.

## Powiązane

  * [Tworzenie pluginów](</pl/plugins/building-plugins>)
  * [Dokumentacja CLI](</pl/cli>)
  * [ClawHub](</pl/clawhub>)


Was this useful?YesNo