---
title: Izolacja w piaskownicy
source_url: https://docs.openclaw.ai/pl/gateway/sandboxing
scraped_at: 2026-05-25
---

OpenClaw może uruchamiać **narzędzia wewnątrz backendów piaskownicy** , aby ograniczyć zakres skutków. Jest to **opcjonalne** i kontrolowane przez konfigurację (`agents.defaults.sandbox` lub `agents.list[].sandbox`). Jeśli uruchamianie w piaskownicy jest wyłączone, narzędzia działają na hoście. Gateway pozostaje na hoście; wykonywanie narzędzi odbywa się w izolowanej piaskownicy, gdy jest włączone.

## Co trafia do piaskownicy

  * Wykonywanie narzędzi (`exec`, `read`, `write`, `edit`, `apply_patch`, `process` itd.).
  * Opcjonalna przeglądarka w piaskownicy (`agents.defaults.sandbox.browser`).


Sandboxed browser details

  * Domyślnie przeglądarka w piaskownicy uruchamia się automatycznie (zapewnia dostępność CDP), gdy narzędzie przeglądarki jej potrzebuje. Skonfiguruj przez `agents.defaults.sandbox.browser.autoStart` i `agents.defaults.sandbox.browser.autoStartTimeoutMs`.
  * Domyślnie kontenery przeglądarki w piaskownicy używają dedykowanej sieci Docker (`openclaw-sandbox-browser`) zamiast globalnej sieci `bridge`. Skonfiguruj za pomocą `agents.defaults.sandbox.browser.network`.
  * Opcjonalne `agents.defaults.sandbox.browser.cdpSourceRange` ogranicza wejście CDP na krawędzi kontenera listą dozwolonych CIDR (na przykład `172.21.0.1/32`).
  * Dostęp obserwatora noVNC jest domyślnie chroniony hasłem; OpenClaw emituje krótkotrwały URL tokena, który serwuje lokalną stronę startową i otwiera noVNC z hasłem we fragmencie URL (nie w zapytaniu/logach nagłówków).
  * `agents.defaults.sandbox.browser.allowHostControl` pozwala sesjom w piaskownicy jawnie wskazywać przeglądarkę hosta.
  * Opcjonalne listy dozwolonych wartości bramkują `target: "custom"`: `allowedControlUrls`, `allowedControlHosts`, `allowedControlPorts`.


Nie trafia do piaskownicy:

  * Sam proces Gateway.
  * Każde narzędzie jawnie dopuszczone do działania poza piaskownicą (np. `tools.elevated`). 
    * **Podniesione`exec` omija piaskownicę i używa skonfigurowanej ścieżki ucieczki (`gateway` domyślnie albo `node`, gdy celem `exec` jest `node`).**
    * Jeśli uruchamianie w piaskownicy jest wyłączone, `tools.elevated` nie zmienia wykonywania (już odbywa się na hoście). Zobacz [Tryb podniesiony](</pl/tools/elevated>).


## Tryby

`agents.defaults.sandbox.mode` kontroluje, **kiedy** używana jest piaskownica:

### off

Brak uruchamiania w piaskownicy.

### non-main

Tylko sesje **inne niż główne** trafiają do piaskownicy (domyślne, jeśli chcesz, aby zwykłe czaty działały na hoście).

`"non-main"` opiera się na `session.mainKey` (domyślnie `"main"`), a nie na identyfikatorze agenta. Sesje grup/kanałów używają własnych kluczy, więc liczą się jako inne niż główne i trafią do piaskownicy.

### all

Każda sesja działa w piaskownicy.

## Zakres

`agents.defaults.sandbox.scope` kontroluje, **ile kontenerów** jest tworzonych:

  * `"agent"` (domyślnie): jeden kontener na agenta.
  * `"session"`: jeden kontener na sesję.
  * `"shared"`: jeden kontener współdzielony przez wszystkie sesje w piaskownicy.


## Backend

`agents.defaults.sandbox.backend` kontroluje, **które środowisko uruchomieniowe** zapewnia piaskownicę:

  * `"docker"` (domyślnie, gdy piaskownica jest włączona): lokalne środowisko piaskownicy oparte na Dockerze.
  * `"ssh"`: ogólne zdalne środowisko piaskownicy oparte na SSH.
  * `"openshell"`: środowisko piaskownicy oparte na OpenShell.


Konfiguracja specyficzna dla SSH znajduje się w `agents.defaults.sandbox.ssh`. Konfiguracja specyficzna dla OpenShell znajduje się w `plugins.entries.openshell.config`.

### Wybór backendu

| Docker | SSH | OpenShell  
---|---|---|---  
**Gdzie działa** | Lokalny kontener | Dowolny host dostępny przez SSH | Piaskownica zarządzana przez OpenShell  
**Konfiguracja** | `scripts/sandbox-setup.sh` | Klucz SSH + host docelowy | Włączony Plugin OpenShell  
**Model przestrzeni roboczej** | Montowanie bind albo kopia | Zdalnie kanoniczny (jednorazowe zasianie) | `mirror` lub `remote`  
**Kontrola sieci** | `docker.network` (domyślnie: brak) | Zależy od hosta zdalnego | Zależy od OpenShell  
**Piaskownica przeglądarki** | Obsługiwana | Nieobsługiwana | Jeszcze nieobsługiwana  
**Montowania bind** | `docker.binds` | N/D | N/D  
**Najlepsze do** | Lokalny rozwój, pełna izolacja | Odciążanie na zdalną maszynę | Zarządzane zdalne piaskownice z opcjonalną synchronizacją dwukierunkową  
  
### Backend Docker

Uruchamianie w piaskownicy jest domyślnie wyłączone. Jeśli włączysz piaskownicę i nie wybierzesz backendu, OpenClaw użyje backendu Docker. Wykonuje narzędzia i przeglądarki w piaskownicy lokalnie przez gniazdo demona Docker (`/var/run/docker.sock`). Izolacja kontenera piaskownicy jest określana przez przestrzenie nazw Docker.

Aby udostępnić GPU hosta piaskownicom Docker, ustaw `agents.defaults.sandbox.docker.gpus` albo nadpisanie per agent `agents.list[].sandbox.docker.gpus`. Wartość jest przekazywana do flagi Docker `--gpus` jako osobny argument, na przykład `"all"` albo `"device=GPU-uuid"`, i wymaga zgodnego środowiska uruchomieniowego hosta, takiego jak NVIDIA Container Toolkit.

### Backend SSH

Użyj `backend: "ssh"`, gdy chcesz, aby OpenClaw uruchamiał w piaskownicy `exec`, narzędzia plikowe i odczyty multimediów na dowolnej maszynie dostępnej przez SSH.

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "all",        backend: "ssh",        scope: "session",        workspaceAccess: "rw",        ssh: {          target: "user@gateway-host:22",          workspaceRoot: "/tmp/openclaw-sandboxes",          strictHostKeyChecking: true,          updateHostKeys: true,          identityFile: "~/.ssh/id_ed25519",          certificateFile: "~/.ssh/id_ed25519-cert.pub",          knownHostsFile: "~/.ssh/known_hosts",          // Or use SecretRefs / inline contents instead of local files:          // identityData: { source: "env", provider: "default", id: "SSH_IDENTITY" },          // certificateData: { source: "env", provider: "default", id: "SSH_CERTIFICATE" },          // knownHostsData: { source: "env", provider: "default", id: "SSH_KNOWN_HOSTS" },        },      },    },  },}
[/code]

How it works

  * OpenClaw tworzy zdalny katalog główny dla danego zakresu pod `sandbox.ssh.workspaceRoot`.
  * Przy pierwszym użyciu po utworzeniu lub odtworzeniu OpenClaw jednorazowo zasiewa tę zdalną przestrzeń roboczą z lokalnej przestrzeni roboczej.
  * Następnie `exec`, `read`, `write`, `edit`, `apply_patch`, odczyty multimediów promptu oraz etapowanie multimediów przychodzących działają bezpośrednio na zdalnej przestrzeni roboczej przez SSH.
  * OpenClaw nie synchronizuje automatycznie zdalnych zmian z powrotem do lokalnej przestrzeni roboczej.

Authentication material

  * `identityFile`, `certificateFile`, `knownHostsFile`: użyj istniejących plików lokalnych i przekaż je przez konfigurację OpenSSH.
  * `identityData`, `certificateData`, `knownHostsData`: użyj ciągów inline lub SecretRefs. OpenClaw rozwiązuje je przez normalny zrzut środowiska uruchomieniowego sekretów, zapisuje do plików tymczasowych z `0600` i usuwa je po zakończeniu sesji SSH.
  * Jeśli dla tego samego elementu ustawiono zarówno `*File`, jak i `*Data`, `*Data` wygrywa dla tej sesji SSH.

Remote-canonical consequences

To model **zdalnie kanoniczny**. Zdalna przestrzeń robocza SSH staje się rzeczywistym stanem piaskownicy po początkowym zasianiu.

  * Lokalne edycje na hoście wykonane poza OpenClaw po kroku zasiania nie są widoczne zdalnie, dopóki nie odtworzysz piaskownicy.
  * `openclaw sandbox recreate` usuwa zdalny katalog główny dla danego zakresu i przy następnym użyciu ponownie zasiewa z lokalnego.
  * Piaskownica przeglądarki nie jest obsługiwana w backendzie SSH.
  * Ustawienia `sandbox.docker.*` nie mają zastosowania do backendu SSH.


### Backend OpenShell

Użyj `backend: "openshell"`, gdy chcesz, aby OpenClaw uruchamiał narzędzia w piaskownicy w zdalnym środowisku zarządzanym przez OpenShell. Pełny przewodnik konfiguracji, referencję konfiguracji i porównanie trybów przestrzeni roboczej znajdziesz na dedykowanej [stronie OpenShell](</pl/gateway/openshell>).

OpenShell ponownie wykorzystuje ten sam podstawowy transport SSH i mostek zdalnego systemu plików co ogólny backend SSH oraz dodaje cykl życia specyficzny dla OpenShell (`sandbox create/get/delete`, `sandbox ssh-config`) i opcjonalny tryb przestrzeni roboczej `mirror`.

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "all",        backend: "openshell",        scope: "session",        workspaceAccess: "rw",      },    },  },  plugins: {    entries: {      openshell: {        enabled: true,        config: {          from: "openclaw",          mode: "remote", // mirror | remote          remoteWorkspaceDir: "/sandbox",          remoteAgentWorkspaceDir: "/agent",        },      },    },  },}
[/code]

Tryby OpenShell:

  * `mirror` (domyślnie): lokalna przestrzeń robocza pozostaje kanoniczna. OpenClaw synchronizuje pliki lokalne do OpenShell przed `exec` i synchronizuje zdalną przestrzeń roboczą z powrotem po `exec`.
  * `remote`: przestrzeń robocza OpenShell jest kanoniczna po utworzeniu piaskownicy. OpenClaw jednorazowo zasiewa zdalną przestrzeń roboczą z lokalnej przestrzeni roboczej, a następnie narzędzia plikowe i `exec` działają bezpośrednio na zdalnej piaskownicy bez synchronizowania zmian z powrotem.


Remote transport details

  * OpenClaw prosi OpenShell o konfigurację SSH specyficzną dla piaskownicy przez `openshell sandbox ssh-config <name>`.
  * Core zapisuje tę konfigurację SSH do pliku tymczasowego, otwiera sesję SSH i ponownie wykorzystuje ten sam mostek zdalnego systemu plików używany przez `backend: "ssh"`.
  * W trybie `mirror` różni się tylko cykl życia: synchronizacja lokalnego do zdalnego przed `exec`, a potem synchronizacja z powrotem po `exec`.

Current OpenShell limitations

  * przeglądarka w piaskownicy nie jest jeszcze obsługiwana
  * `sandbox.docker.binds` nie jest obsługiwane w backendzie OpenShell
  * Pokrętła środowiska uruchomieniowego specyficzne dla Docker pod `sandbox.docker.*` nadal mają zastosowanie tylko do backendu Docker


#### Tryby przestrzeni roboczej

OpenShell ma dwa modele przestrzeni roboczej. To część, która w praktyce ma największe znaczenie.

### mirror (local canonical)

Użyj `plugins.entries.openshell.config.mode: "mirror"`, gdy chcesz, aby **lokalna przestrzeń robocza pozostała kanoniczna**.

Zachowanie:

  * Przed `exec` OpenClaw synchronizuje lokalny obszar roboczy do piaskownicy OpenShell.
  * Po `exec` OpenClaw synchronizuje zdalny obszar roboczy z powrotem do lokalnego obszaru roboczego.
  * Narzędzia plikowe nadal działają przez most piaskownicy, ale lokalny obszar roboczy pozostaje źródłem prawdy między turami.


Użyj tego, gdy:

  * edytujesz pliki lokalnie poza OpenClaw i chcesz, aby te zmiany automatycznie pojawiały się w piaskownicy
  * chcesz, aby piaskownica OpenShell zachowywała się możliwie podobnie do backendu Docker
  * chcesz, aby obszar roboczy hosta odzwierciedlał zapisy z piaskownicy po każdej turze exec


Kompromis: dodatkowy koszt synchronizacji przed i po exec.

### remote (OpenShell canonical)

Użyj `plugins.entries.openshell.config.mode: "remote"`, gdy chcesz, aby **obszar roboczy OpenShell stał się kanoniczny**.

Zachowanie:

  * Gdy piaskownica jest tworzona po raz pierwszy, OpenClaw jednorazowo inicjuje zdalny obszar roboczy z lokalnego obszaru roboczego.
  * Następnie `exec`, `read`, `write`, `edit` i `apply_patch` działają bezpośrednio na zdalnym obszarze roboczym OpenShell.
  * OpenClaw **nie** synchronizuje zdalnych zmian z powrotem do lokalnego obszaru roboczego po exec.
  * Odczyty multimediów w czasie promptu nadal działają, ponieważ narzędzia plikowe i multimedialne czytają przez most piaskownicy zamiast zakładać lokalną ścieżkę hosta.
  * Transport odbywa się przez SSH do piaskownicy OpenShell zwróconej przez `openshell sandbox ssh-config`.


Ważne konsekwencje:

  * Jeśli po kroku inicjowania edytujesz pliki na hoście poza OpenClaw, zdalna piaskownica **nie** zobaczy tych zmian automatycznie.
  * Jeśli piaskownica zostanie odtworzona, zdalny obszar roboczy zostanie ponownie zainicjowany z lokalnego obszaru roboczego.
  * Przy `scope: "agent"` lub `scope: "shared"` ten zdalny obszar roboczy jest współdzielony w tym samym zakresie.


Użyj tego, gdy:

  * piaskownica powinna działać głównie po zdalnej stronie OpenShell
  * chcesz zmniejszyć narzut synchronizacji na turę
  * nie chcesz, aby lokalne edycje hosta po cichu nadpisywały stan zdalnej piaskownicy


Wybierz `mirror`, jeśli traktujesz piaskownicę jako tymczasowe środowisko wykonawcze. Wybierz `remote`, jeśli traktujesz piaskownicę jako rzeczywisty obszar roboczy.

#### Cykl życia OpenShell

Piaskownice OpenShell są nadal zarządzane przez normalny cykl życia piaskownicy:

  * `openclaw sandbox list` pokazuje środowiska uruchomieniowe OpenShell oraz środowiska uruchomieniowe Docker
  * `openclaw sandbox recreate` usuwa bieżące środowisko uruchomieniowe i pozwala OpenClaw odtworzyć je przy następnym użyciu
  * logika czyszczenia również uwzględnia backend


Dla trybu `remote` odtworzenie jest szczególnie ważne:

  * odtworzenie usuwa kanoniczny zdalny obszar roboczy dla tego zakresu
  * następne użycie inicjuje świeży zdalny obszar roboczy z lokalnego obszaru roboczego


Dla trybu `mirror` odtworzenie głównie resetuje zdalne środowisko wykonawcze, ponieważ lokalny obszar roboczy i tak pozostaje kanoniczny.

## Dostęp do obszaru roboczego

`agents.defaults.sandbox.workspaceAccess` kontroluje, **co piaskownica może zobaczyć** :

### none (default)

Narzędzia widzą obszar roboczy piaskownicy pod `~/.openclaw/sandboxes`.

### ro

Montuje obszar roboczy agenta tylko do odczytu w `/agent` (wyłącza `write`/`edit`/`apply_patch`).

### rw

Montuje obszar roboczy agenta do odczytu/zapisu w `/workspace`.

Z backendem OpenShell:

  * tryb `mirror` nadal używa lokalnego obszaru roboczego jako kanonicznego źródła między turami exec
  * tryb `remote` używa zdalnego obszaru roboczego OpenShell jako kanonicznego źródła po początkowym zainicjowaniu
  * `workspaceAccess: "ro"` i `"none"` nadal ograniczają zachowanie zapisu w ten sam sposób


Przychodzące multimedia są kopiowane do aktywnego obszaru roboczego piaskownicy (`media/inbound/*`).

## Niestandardowe montowania bind

`agents.defaults.sandbox.docker.binds` montuje dodatkowe katalogi hosta w kontenerze. Format: `host:container:mode` (np. `"/home/user/source:/source:rw"`).

Globalne i per-agent bindy są **scalane** (nie zastępowane). Przy `scope: "shared"` bindy per-agent są ignorowane.

`agents.defaults.sandbox.browser.binds` montuje dodatkowe katalogi hosta tylko w kontenerze **przeglądarki piaskownicy**.

  * Gdy jest ustawione (w tym `[]`), zastępuje `agents.defaults.sandbox.docker.binds` dla kontenera przeglądarki.
  * Gdy jest pominięte, kontener przeglądarki używa awaryjnie `agents.defaults.sandbox.docker.binds` (zgodność wsteczna).


Przykład (źródło tylko do odczytu + dodatkowy katalog danych):

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        docker: {          binds: ["/home/user/source:/source:ro", "/var/data/myapp:/data:ro"],        },      },    },    list: [      {        id: "build",        sandbox: {          docker: {            binds: ["/mnt/cache:/cache:rw"],          },        },      },    ],  },}
[/code]

## Obrazy i konfiguracja

Domyślny obraz Docker: `openclaw-sandbox:bookworm-slim`

* ### Build the default image

Z checkoutu źródeł:

bashCopy code
[code]
    scripts/sandbox-setup.sh
[/code]

Z instalacji npm (checkout źródeł nie jest potrzebny):

bashCopy code
[code]
    docker build -t openclaw-sandbox:bookworm-slim - <<'DOCKERFILE'FROM debian:bookworm-slimENV DEBIAN_FRONTEND=noninteractiveRUN apt-get update && apt-get install -y --no-install-recommends \  bash ca-certificates curl git jq python3 ripgrep \  && rm -rf /var/lib/apt/lists/*RUN useradd --create-home --shell /bin/bash sandboxUSER sandboxWORKDIR /home/sandboxCMD ["sleep", "infinity"]DOCKERFILE
[/code]

Domyślny obraz **nie** zawiera Node. Jeśli skill potrzebuje Node (lub innych środowisk uruchomieniowych), wypiecz własny obraz albo zainstaluj przez `sandbox.docker.setupCommand` (wymaga wyjścia do sieci + zapisywalnego katalogu głównego + użytkownika root).

OpenClaw nie podstawia po cichu zwykłego `debian:bookworm-slim`, gdy brakuje `openclaw-sandbox:bookworm-slim`. Uruchomienia piaskownicy, które celują w domyślny obraz, szybko kończą się niepowodzeniem z instrukcją budowania, dopóki go nie zbudujesz, ponieważ dołączony obraz zawiera `python3` dla pomocników zapisu/edycji piaskownicy.

* ### Optional: build the common image

Dla bardziej funkcjonalnego obrazu piaskownicy z typowymi narzędziami (na przykład `curl`, `jq`, `nodejs`, `python3`, `git`):

Z checkoutu źródeł:

bashCopy code
[code]
    scripts/sandbox-common-setup.sh
[/code]

Z instalacji npm najpierw zbuduj domyślny obraz (zobacz wyżej), a następnie zbuduj obraz common na jego bazie, używając [`scripts/docker/sandbox/Dockerfile.common`](<https://github.com/openclaw/openclaw/blob/main/scripts/docker/sandbox/Dockerfile.common>) z repozytorium.

Następnie ustaw `agents.defaults.sandbox.docker.image` na `openclaw-sandbox-common:bookworm-slim`.

* ### Optional: build the sandbox browser image

Z checkoutu źródeł:

bashCopy code
[code]
    scripts/sandbox-browser-setup.sh
[/code]

Z instalacji npm zbuduj, używając [`scripts/docker/sandbox/Dockerfile.browser`](<https://github.com/openclaw/openclaw/blob/main/scripts/docker/sandbox/Dockerfile.browser>) z repozytorium.

Domyślnie kontenery piaskownicy Docker działają **bez sieci**. Nadpisz to przez `agents.defaults.sandbox.docker.network`.

Sandbox browser Chromium defaults

Dołączony obraz przeglądarki piaskownicy stosuje również konserwatywne domyślne ustawienia uruchamiania Chromium dla obciążeń kontenerowych. Bieżące ustawienia domyślne kontenera obejmują:

  * `--remote-debugging-address=127.0.0.1`
  * `--remote-debugging-port=<derived from OPENCLAW_BROWSER_CDP_PORT>`
  * `--user-data-dir=${HOME}/.chrome`
  * `--no-first-run`
  * `--no-default-browser-check`
  * `--disable-3d-apis`
  * `--disable-gpu`
  * `--disable-dev-shm-usage`
  * `--disable-background-networking`
  * `--disable-extensions`
  * `--disable-features=TranslateUI`
  * `--disable-breakpad`
  * `--disable-crash-reporter`
  * `--disable-software-rasterizer`
  * `--no-zygote`
  * `--metrics-recording-only`
  * `--renderer-process-limit=2`
  * `--no-sandbox` gdy `noSandbox` jest włączone.
  * Trzy flagi wzmacniające grafikę (`--disable-3d-apis`, `--disable-software-rasterizer`, `--disable-gpu`) są opcjonalne i przydatne, gdy kontenery nie mają obsługi GPU. Ustaw `OPENCLAW_BROWSER_DISABLE_GRAPHICS_FLAGS=0`, jeśli Twoje obciążenie wymaga WebGL lub innych funkcji 3D/przeglądarki.
  * `--disable-extensions` jest domyślnie włączone i można je wyłączyć za pomocą `OPENCLAW_BROWSER_DISABLE_EXTENSIONS=0` dla przepływów zależnych od rozszerzeń.
  * `--renderer-process-limit=2` jest kontrolowane przez `OPENCLAW_BROWSER_RENDERER_PROCESS_LIMIT=&lt;N&gt;`, gdzie `0` zachowuje domyślne ustawienie Chromium.


Jeśli potrzebujesz innego profilu środowiska uruchomieniowego, użyj własnego obrazu przeglądarki i zapewnij własny punkt wejścia. Dla lokalnych (niekontenerowych) profili Chromium użyj `browser.extraArgs`, aby dodać dodatkowe flagi uruchamiania.

Network security defaults

  * `network: "host"` jest blokowane.
  * `network: "container:<id>"` jest domyślnie blokowane (ryzyko obejścia przez dołączenie do przestrzeni nazw).
  * Awaryjne nadpisanie: `agents.defaults.sandbox.docker.dangerouslyAllowContainerNamespaceJoin: true`.


Instalacje Docker i konteneryzowany Gateway znajdują się tutaj: [Docker](</pl/install/docker>)

W przypadku wdrożeń Gateway Docker `scripts/docker/setup.sh` może zainicjować konfigurację piaskownicy. Ustaw `OPENCLAW_SANDBOX=1` (lub `true`/`yes`/`on`), aby włączyć tę ścieżkę. Lokalizację socketu możesz nadpisać za pomocą `OPENCLAW_DOCKER_SOCKET`. Pełna konfiguracja i opis zmiennych środowiskowych: [Docker](</pl/install/docker#agent-sandbox>).

## setupCommand (jednorazowa konfiguracja kontenera)

`setupCommand` uruchamia się **raz** po utworzeniu kontenera piaskownicy (nie przy każdym uruchomieniu). Wykonuje się wewnątrz kontenera przez `sh -lc`.

Ścieżki:

  * Globalnie: `agents.defaults.sandbox.docker.setupCommand`
  * Per-agent: `agents.list[].sandbox.docker.setupCommand`


Typowe pułapki

  * Domyślna wartość `docker.network` to `"none"` (brak ruchu wychodzącego), więc instalacje pakietów będą kończyć się niepowodzeniem.
  * `docker.network: "container:<id>"` wymaga `dangerouslyAllowContainerNamespaceJoin: true` i jest przeznaczone wyłącznie do użycia awaryjnego.
  * `readOnlyRoot: true` uniemożliwia zapisy; ustaw `readOnlyRoot: false` albo przygotuj własny obraz.
  * `user` musi być użytkownikiem root do instalowania pakietów (pomiń `user` albo ustaw `user: "0:0"`).
  * Wykonanie `exec` w piaskownicy **nie** dziedziczy `process.env` hosta. Użyj `agents.defaults.sandbox.docker.env` (albo własnego obrazu) dla kluczy API Skills.


## Zasady narzędzi i wyjścia awaryjne

Zasady zezwalania/odmawiania narzędzi nadal obowiązują przed regułami piaskownicy. Jeśli narzędzie jest zabronione globalnie albo dla danego agenta, piaskownica go nie przywraca.

`tools.elevated` to jawne wyjście awaryjne, które uruchamia `exec` poza piaskownicą (domyślnie `gateway`, albo `node`, gdy celem `exec` jest `node`). Dyrektywy `/exec` mają zastosowanie tylko do autoryzowanych nadawców i utrzymują się w ramach sesji; aby trwale wyłączyć `exec`, użyj odmowy w zasadach narzędzi (zobacz [Piaskownica kontra zasady narzędzi kontra podwyższone uprawnienia](</pl/gateway/sandbox-vs-tool-policy-vs-elevated>)).

Debugowanie:

  * Użyj `openclaw sandbox explain`, aby sprawdzić efektywny tryb piaskownicy, zasady narzędzi i klucze konfiguracji naprawczej.
  * Zobacz [Piaskownica kontra zasady narzędzi kontra podwyższone uprawnienia](</pl/gateway/sandbox-vs-tool-policy-vs-elevated>), aby poznać model myślowy „dlaczego to jest zablokowane?”.


Utrzymuj to w ścisłej izolacji.

## Nadpisania dla wielu agentów

Każdy agent może nadpisać piaskownicę i narzędzia: `agents.list[].sandbox` oraz `agents.list[].tools` (plus `agents.list[].tools.sandbox.tools` dla zasad narzędzi piaskownicy). Zobacz [Piaskownica i narzędzia wielu agentów](</pl/tools/multi-agent-sandbox-tools>), aby poznać kolejność pierwszeństwa.

## Minimalny przykład włączenia

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "non-main",        scope: "session",        workspaceAccess: "none",      },    },  },}
[/code]

## Powiązane

  * [Piaskownica i narzędzia wielu agentów](</pl/tools/multi-agent-sandbox-tools>) — nadpisania dla poszczególnych agentów i kolejność pierwszeństwa
  * [OpenShell](</pl/gateway/openshell>) — konfiguracja zarządzanego zaplecza piaskownicy, tryby przestrzeni roboczej i dokumentacja konfiguracji
  * [Konfiguracja piaskownicy](</pl/gateway/config-agents#agentsdefaultssandbox>)
  * [Piaskownica kontra zasady narzędzi kontra podwyższone uprawnienia](</pl/gateway/sandbox-vs-tool-policy-vs-elevated>) — debugowanie „dlaczego to jest zablokowane?”
  * [Bezpieczeństwo](</pl/gateway/security>)


Was this useful?YesNo