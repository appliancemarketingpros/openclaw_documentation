---
title: CLI piaskownicy
source_url: https://docs.openclaw.ai/pl/cli/sandbox
scraped_at: 2026-05-25
---

Zarządzaj środowiskami uruchomieniowymi sandbox na potrzeby izolowanego wykonywania agentów.

## Omówienie

OpenClaw może uruchamiać agentów w izolowanych środowiskach uruchomieniowych sandbox dla bezpieczeństwa. Polecenia `sandbox` pomagają sprawdzać i odtwarzać te środowiska po aktualizacjach lub zmianach konfiguracji.

Obecnie zwykle oznacza to:

  * Kontenery sandbox Docker
  * Środowiska uruchomieniowe sandbox SSH, gdy `agents.defaults.sandbox.backend = "ssh"`
  * Środowiska uruchomieniowe sandbox OpenShell, gdy `agents.defaults.sandbox.backend = "openshell"`


Dla `ssh` i OpenShell `remote` odtworzenie ma większe znaczenie niż w przypadku Docker:

  * zdalny obszar roboczy jest kanoniczny po początkowym zasianiu
  * `openclaw sandbox recreate` usuwa ten kanoniczny zdalny obszar roboczy dla wybranego zakresu
  * następne użycie ponownie zasiewa go z bieżącego lokalnego obszaru roboczego


## Polecenia

### `openclaw sandbox explain`

Sprawdź **efektywny** tryb/zakres/dostęp do obszaru roboczego sandbox, politykę narzędzi sandbox oraz bramki podniesionych uprawnień (ze ścieżkami kluczy konfiguracji do naprawy).

bashCopy code
[code]
    openclaw sandbox explainopenclaw sandbox explain --session agent:main:mainopenclaw sandbox explain --agent workopenclaw sandbox explain --json
[/code]

### `openclaw sandbox list`

Wyświetl wszystkie środowiska uruchomieniowe sandbox wraz z ich stanem i konfiguracją.

bashCopy code
[code]
    openclaw sandbox listopenclaw sandbox list --browser  # List only browser containersopenclaw sandbox list --json     # JSON output
[/code]

**Dane wyjściowe obejmują:**

  * Nazwę i stan środowiska uruchomieniowego
  * Backend (`docker`, `openshell` itd.)
  * Etykietę konfiguracji i informację, czy pasuje do bieżącej konfiguracji
  * Wiek (czas od utworzenia)
  * Czas bezczynności (czas od ostatniego użycia)
  * Powiązaną sesję/agenta


### `openclaw sandbox recreate`

Usuń środowiska uruchomieniowe sandbox, aby wymusić ich odtworzenie ze zaktualizowaną konfiguracją.

bashCopy code
[code]
    openclaw sandbox recreate --all                # Recreate all containersopenclaw sandbox recreate --session main       # Specific sessionopenclaw sandbox recreate --agent mybot        # Specific agentopenclaw sandbox recreate --browser            # Only browser containersopenclaw sandbox recreate --all --force        # Skip confirmation
[/code]

**Opcje:**

  * `--all`: Odtwórz wszystkie kontenery sandbox
  * `--session <key>`: Odtwórz kontener dla konkretnej sesji
  * `--agent <id>`: Odtwórz kontenery dla konkretnego agenta
  * `--browser`: Odtwórz tylko kontenery przeglądarki
  * `--force`: Pomiń monit o potwierdzenie


## Przypadki użycia

### Po aktualizacji obrazu Docker

bashCopy code
[code]
    # Pull new imagedocker pull openclaw-sandbox:latestdocker tag openclaw-sandbox:latest openclaw-sandbox:bookworm-slim # Update config to use new image# Edit config: agents.defaults.sandbox.docker.image (or agents.list[].sandbox.docker.image) # Recreate containersopenclaw sandbox recreate --all
[/code]

### Po zmianie konfiguracji sandbox

bashCopy code
[code]
    # Edit config: agents.defaults.sandbox.* (or agents.list[].sandbox.*) # Recreate to apply new configopenclaw sandbox recreate --all
[/code]

### Po zmianie celu SSH lub materiałów uwierzytelniania SSH

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - agents.defaults.sandbox.ssh.target# - agents.defaults.sandbox.ssh.workspaceRoot# - agents.defaults.sandbox.ssh.identityFile / certificateFile / knownHostsFile# - agents.defaults.sandbox.ssh.identityData / certificateData / knownHostsData openclaw sandbox recreate --all
[/code]

Dla podstawowego backendu `ssh` odtworzenie usuwa zdalny katalog główny obszaru roboczego dla danego zakresu na celu SSH. Następne uruchomienie ponownie zasiewa go z lokalnego obszaru roboczego.

### Po zmianie źródła, polityki lub trybu OpenShell

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - plugins.entries.openshell.config.from# - plugins.entries.openshell.config.mode# - plugins.entries.openshell.config.policy openclaw sandbox recreate --all
[/code]

W trybie OpenShell `remote` odtworzenie usuwa kanoniczny zdalny obszar roboczy dla tego zakresu. Następne uruchomienie ponownie zasiewa go z lokalnego obszaru roboczego.

### Po zmianie setupCommand

bashCopy code
[code]
    openclaw sandbox recreate --all# or just one agent:openclaw sandbox recreate --agent family
[/code]

### Tylko dla konkretnego agenta

bashCopy code
[code]
    # Update only one agent's containersopenclaw sandbox recreate --agent alfred
[/code]

## Dlaczego jest to potrzebne

Gdy aktualizujesz konfigurację sandbox:

  * Istniejące środowiska uruchomieniowe nadal działają ze starymi ustawieniami.
  * Środowiska uruchomieniowe są usuwane dopiero po 24 godzinach bezczynności.
  * Regularnie używani agenci utrzymują stare środowiska uruchomieniowe aktywne bezterminowo.


Użyj `openclaw sandbox recreate`, aby wymusić usunięcie starych środowisk uruchomieniowych. Zostaną one automatycznie odtworzone z bieżącymi ustawieniami, gdy będą ponownie potrzebne.

## Migracja rejestru

OpenClaw przechowuje metadane środowiska uruchomieniowego sandbox jako jeden fragment JSON na wpis kontenera/przeglądarki w katalogu stanu sandbox. Starsze instalacje mogą nadal mieć monolityczne pliki starszego typu:

  * `~/.openclaw/sandbox/containers.json`
  * `~/.openclaw/sandbox/browsers.json`


Zwykłe odczyty środowisk uruchomieniowych sandbox nie przepisują tych plików. Uruchom `openclaw doctor --fix`, aby zmigrować prawidłowe starsze wpisy do katalogów rejestru podzielonego na fragmenty. Nieprawidłowe starsze pliki są poddawane kwarantannie, aby jeden wadliwy stary rejestr nie mógł ukryć bieżących wpisów środowisk uruchomieniowych.

## Konfiguracja

Ustawienia sandbox znajdują się w `~/.openclaw/openclaw.json` pod `agents.defaults.sandbox` (nadpisania dla poszczególnych agentów trafiają do `agents.list[].sandbox`):

jsoncCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "all", // off, non-main, all        "backend": "docker", // docker, ssh, openshell        "scope": "agent", // session, agent, shared        "docker": {          "image": "openclaw-sandbox:bookworm-slim",          "containerPrefix": "openclaw-sbx-",          // ... more Docker options        },        "prune": {          "idleHours": 24, // Auto-prune after 24h idle          "maxAgeDays": 7, // Auto-prune after 7 days        },      },    },  },}
[/code]

## Powiązane

  * [Dokumentacja CLI](</pl/cli>)
  * [Sandboxing](</pl/gateway/sandboxing>)
  * [Obszar roboczy agenta](</pl/concepts/agent-workspace>)
  * [Doctor](</pl/gateway/doctor>): sprawdza konfigurację sandbox.


Was this useful?YesNo