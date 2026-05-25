---
title: Konfiguracja
source_url: https://docs.openclaw.ai/pl/cli/config
scraped_at: 2026-05-25
---

Pomocnicze narzędzia konfiguracji do nieinteraktywnych edycji w `openclaw.json`: pobieranie/ustawianie/łatanie/usuwanie/plik/schemat/walidacja wartości według ścieżki oraz wypisywanie aktywnego pliku konfiguracji. Uruchom bez podkomendy, aby otworzyć kreator konfiguracji (tak samo jak `openclaw configure`).

## Opcje główne

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tc2VjdGlvbiA8c2VjdGlvbg " type="string"> Powtarzalny filtr sekcji konfiguracji prowadzonej, gdy uruchamiasz `openclaw config` bez podkomendy.

Obsługiwane sekcje konfiguracji prowadzonej: `workspace`, `model`, `web`, `gateway`, `daemon`, `channels`, `plugins`, `skills`, `health`.

## Przykłady

bashCopy code
[code]
    openclaw config fileopenclaw config --section modelopenclaw config --section gateway --section daemonopenclaw config schemaopenclaw config get browser.executablePathopenclaw config set browser.executablePath "/usr/bin/google-chrome"openclaw config set browser.profiles.work.executablePath "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"openclaw config set agents.defaults.heartbeat.every "2h"openclaw config set agents.list[0].tools.exec.node "node-id-or-name"openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKENopenclaw config set secrets.providers.vaultfile --provider-source file --provider-path /etc/openclaw/secrets.json --provider-mode jsonopenclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config unset plugins.entries.brave.config.webSearch.apiKeyopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKEN --dry-runopenclaw config validateopenclaw config validate --json
[/code]

### `config schema`

Wypisz wygenerowany schemat JSON dla `openclaw.json` na stdout jako JSON.

Co zawiera

  * Bieżący główny schemat konfiguracji oraz główne pole ciągu znaków `$schema` dla narzędzi edytora.
  * Metadane dokumentacji pól `title` i `description` używane przez Control UI.
  * Zagnieżdżone obiekty, wildcard (`*`) i węzły elementów tablicy (`[]`) dziedziczą te same metadane `title` / `description`, gdy istnieje pasująca dokumentacja pola.
  * Gałęzie `anyOf` / `oneOf` / `allOf` również dziedziczą te same metadane dokumentacji, gdy istnieje pasująca dokumentacja pola.
  * Metadane schematu Plugin + kanału w trybie best-effort na żywo, gdy można wczytać manifesty środowiska uruchomieniowego.
  * Czysty schemat awaryjny nawet wtedy, gdy bieżąca konfiguracja jest nieprawidłowa.

Powiązane RPC środowiska uruchomieniowego

`config.schema.lookup` zwraca jedną znormalizowaną ścieżkę konfiguracji z płytkim węzłem schematu (`title`, `description`, `type`, `enum`, `const`, typowe ograniczenia), dopasowanymi metadanymi wskazówek UI oraz podsumowaniami bezpośrednich elementów podrzędnych. Użyj go do zagłębiania się według ścieżki w Control UI lub klientach niestandardowych.

bashCopy code
[code]
    openclaw config schema
[/code]

Przekieruj wynik do pliku, gdy chcesz go sprawdzić lub zwalidować innymi narzędziami:

bashCopy code
[code]
    openclaw config schema > openclaw.schema.json
[/code]

### Ścieżki

Ścieżki używają notacji kropkowej lub nawiasowej:

bashCopy code
[code]
    openclaw config get agents.defaults.workspaceopenclaw config get agents.list[0].id
[/code]

Użyj indeksu listy agentów, aby wskazać konkretnego agenta:

bashCopy code
[code]
    openclaw config get agents.listopenclaw config set agents.list[1].tools.exec.node "node-id-or-name"
[/code]

## Wartości

Wartości są analizowane jako JSON5, gdy to możliwe; w przeciwnym razie są traktowane jako ciągi znaków. Użyj `--strict-json`, aby wymagać analizy JSON5. `--json` pozostaje obsługiwany jako starszy alias.

bashCopy code
[code]
    openclaw config set agents.defaults.heartbeat.every "0m"openclaw config set gateway.port 19001 --strict-jsonopenclaw config set channels.whatsapp.groups '["*"]' --strict-json
[/code]

`config get <path> --json` wypisuje surową wartość jako JSON zamiast tekstu formatowanego dla terminala.

Użyj `--merge`, gdy dodajesz wpisy do tych map:

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set models.providers.ollama.models '[{"id":"llama3.2","name":"Llama 3.2"}]' --strict-json --merge
[/code]

Użyj `--replace` tylko wtedy, gdy celowo chcesz, aby podana wartość stała się pełną wartością docelową.

## Tryby `config set`

`openclaw config set` obsługuje cztery style przypisania:

### Tryb wartości

bashCopy code
[code]
    openclaw config set <path> <value>
[/code]

### Tryb konstruktora SecretRef

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN
[/code]

### Tryb konstruktora dostawcy

Tryb konstruktora dostawcy celuje wyłącznie w ścieżki `secrets.providers.<alias>`:

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-timeout-ms 5000
[/code]

### Tryb wsadowy

bashCopy code
[code]
    openclaw config set --batch-json '[  {    "path": "secrets.providers.default",    "provider": { "source": "env" }  },  {    "path": "channels.discord.token",    "ref": { "source": "env", "provider": "default", "id": "DISCORD_BOT_TOKEN" }  }]'
[/code]

bashCopy code
[code]
    openclaw config set --batch-file ./config-set.batch.json --dry-run
[/code]

Analiza wsadowa zawsze używa ładunku wsadowego (`--batch-json`/`--batch-file`) jako źródła prawdy. `--strict-json` / `--json` nie zmieniają zachowania analizy wsadowej.

## `config patch`

Użyj `config patch`, gdy chcesz wkleić lub przesłać potokiem łatkę w kształcie konfiguracji zamiast uruchamiać wiele poleceń `config set` opartych na ścieżkach. Wejście jest obiektem JSON5. Obiekty są scalane rekurencyjnie, tablice i wartości skalarne zastępują wartość docelową, a `null` usuwa ścieżkę docelową.

bashCopy code
[code]
    openclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config patch --file ./openclaw.patch.json5
[/code]

Możesz też przesłać łatkę potokiem przez stdin, co jest przydatne w zdalnych skryptach konfiguracji:

bashCopy code
[code]
    ssh openclaw-host 'openclaw config patch --stdin --dry-run' < ./openclaw.patch.json5ssh openclaw-host 'openclaw config patch --stdin' < ./openclaw.patch.json5
[/code]

Przykładowa łatka:

json5Copy code
[code]
    {  channels: {    slack: {      enabled: true,      mode: "socket",      botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },      appToken: { source: "env", provider: "default", id: "SLACK_APP_TOKEN" },      groupPolicy: "open",      requireMention: false,    },    discord: {      enabled: true,      token: { source: "env", provider: "default", id: "DISCORD_BOT_TOKEN" },      dmPolicy: "disabled",      dm: { enabled: false },      groupPolicy: "allowlist",    },  },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },      models: {        "openai/gpt-5.5": { params: { fastMode: true } },      },    },  },}
[/code]

Użyj `--replace-path <path>`, gdy jeden obiekt lub tablica musi stać się dokładnie podaną wartością zamiast być łatana rekurencyjnie:

bashCopy code
[code]
    openclaw config patch --file ./discord.patch.json5 --replace-path 'channels.discord.guilds["123"].channels'
[/code]

`--dry-run` uruchamia kontrole schematu i rozwiązywalności SecretRef bez zapisu. SecretRef oparte na exec są domyślnie pomijane podczas próby na sucho; dodaj `--allow-exec`, gdy celowo chcesz, aby próba na sucho wykonała polecenia dostawcy.

Tryb ścieżki/wartości JSON pozostaje obsługiwany zarówno dla SecretRef, jak i dostawców:

bashCopy code
[code]
    openclaw config set channels.discord.token \  '{"source":"env","provider":"default","id":"DISCORD_BOT_TOKEN"}' \  --strict-json openclaw config set secrets.providers.vaultfile \  '{"source":"file","path":"/etc/openclaw/secrets.json","mode":"json"}' \  --strict-json
[/code]

## Flagi konstruktora dostawcy

Cele konstruktora dostawcy muszą używać `secrets.providers.<alias>` jako ścieżki.

Typowe flagi

  * `--provider-source <env|file|exec>`
  * `--provider-timeout-ms <ms>` (`file`, `exec`)

Dostawca env (--provider-source env)

  * `--provider-allowlist &lt;ENV_VAR&gt;` (powtarzalne)

Dostawca plikowy (--provider-source file)

  * `--provider-path <path>` (wymagane)
  * `--provider-mode <singleValue|json>`
  * `--provider-max-bytes <bytes>`
  * `--provider-allow-insecure-path`

Dostawca exec (--provider-source exec)

  * `--provider-command <path>` (wymagane)
  * `--provider-arg <arg>` (powtarzalne)
  * `--provider-no-output-timeout-ms <ms>`
  * `--provider-max-output-bytes <bytes>`
  * `--provider-json-only`
  * `--provider-env &lt;KEY=VALUE&gt;` (powtarzalne)
  * `--provider-pass-env &lt;ENV_VAR&gt;` (powtarzalne)
  * `--provider-trusted-dir <path>` (powtarzalne)
  * `--provider-allow-insecure-path`
  * `--provider-allow-symlink-command`


Przykład wzmocnionego dostawcy exec:

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-json-only \  --provider-pass-env VAULT_TOKEN \  --provider-trusted-dir /usr/local/bin \  --provider-timeout-ms 5000
[/code]

## Próba na sucho

Użyj `--dry-run`, aby zwalidować zmiany bez zapisywania `openclaw.json`.

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run \  --json openclaw config set channels.discord.token \  --ref-provider vault \  --ref-source exec \  --ref-id discord/token \  --dry-run \  --allow-exec
[/code]

Zachowanie próby na sucho

  * Tryb konstruktora: uruchamia kontrole rozwiązywalności SecretRef dla zmienionych referencji/dostawców.
  * Tryb JSON (`--strict-json`, `--json` lub tryb wsadowy): uruchamia walidację schematu oraz kontrole rozwiązywalności SecretRef.
  * Walidacja zasad działa również dla znanych nieobsługiwanych powierzchni docelowych SecretRef.
  * Kontrole zasad oceniają pełną konfigurację po zmianie, więc zapisy obiektu nadrzędnego (na przykład ustawienie `hooks` jako obiektu) nie mogą ominąć walidacji nieobsługiwanej powierzchni.
  * Kontrole SecretRef typu exec są domyślnie pomijane podczas próby na sucho, aby uniknąć skutków ubocznych poleceń.
  * Użyj `--allow-exec` z `--dry-run`, aby włączyć kontrole SecretRef typu exec (może to wykonać polecenia dostawcy).
  * `--allow-exec` działa tylko przy próbie na sucho i zgłasza błąd, jeśli zostanie użyte bez `--dry-run`.

Pola --dry-run --json

`--dry-run --json` wypisuje raport czytelny maszynowo:

  * `ok`: czy dry-run zakończył się powodzeniem
  * `operations`: liczba ocenionych przypisań
  * `checks`: czy uruchomiono kontrole schematu/rozwiązywalności
  * `checks.resolvabilityComplete`: czy kontrole rozwiązywalności dobiegły końca (false, gdy odwołania exec są pomijane)
  * `refsChecked`: liczba odwołań faktycznie rozwiązanych podczas dry-run
  * `skippedExecRefs`: liczba odwołań exec pominiętych, ponieważ nie ustawiono `--allow-exec`
  * `errors`: ustrukturyzowane błędy schematu/rozwiązywalności, gdy `ok=false`


### Kształt danych wyjściowych JSON

json5Copy code
[code]
    {  ok: boolean,  operations: number,  configPath: string,  inputModes: ["value" | "json" | "builder", ...],  checks: {    schema: boolean,    resolvability: boolean,    resolvabilityComplete: boolean,  },  refsChecked: number,  skippedExecRefs: number,  errors?: [    {      kind: "schema" | "resolvability",      message: string,      ref?: string, // present for resolvability errors    },  ],}
[/code]

### Przykład powodzenia

jsonCopy code
[code]
    {  "ok": true,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0}
[/code]

### Przykład niepowodzenia

jsonCopy code
[code]
    {  "ok": false,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0,  "errors": [    {      "kind": "resolvability",      "message": "Error: Environment variable \"MISSING_TEST_SECRET\" is not set.",      "ref": "env:default:MISSING_TEST_SECRET"    }  ]}
[/code]

Jeśli dry-run się nie powiedzie

  * `config schema validation failed`: kształt konfiguracji po zmianie jest nieprawidłowy; popraw ścieżkę/wartość albo kształt obiektu provider/ref.
  * `Config policy validation failed: unsupported SecretRef usage`: przenieś te dane uwierzytelniające z powrotem do wejścia zwykłym tekstem/ciągiem i pozostaw SecretRefs tylko na obsługiwanych powierzchniach.
  * `SecretRef assignment(s) could not be resolved`: wskazany provider/ref nie może obecnie zostać rozwiązany (brakująca zmienna środowiskowa, nieprawidłowy wskaźnik pliku, awaria providera exec albo niezgodność providera/źródła).
  * `Dry run note: skipped <n> exec SecretRef resolvability check(s)`: dry-run pominął odwołania exec; uruchom ponownie z `--allow-exec`, jeśli potrzebujesz walidacji rozwiązywalności exec.
  * W trybie wsadowym popraw błędne wpisy i uruchom ponownie `--dry-run` przed zapisem.


## Bezpieczeństwo zapisu

`openclaw config set` i inne narzędzia zapisujące konfigurację należące do OpenClaw walidują pełną konfigurację po zmianie przed zapisaniem jej na dysku. Jeśli nowy ładunek nie przejdzie walidacji schematu albo wygląda jak destrukcyjne nadpisanie, aktywna konfiguracja pozostaje bez zmian, a odrzucony ładunek zostaje zapisany obok niej jako `openclaw.json.rejected.*`.

Preferuj zapisy przez CLI przy małych zmianach:

bashCopy code
[code]
    openclaw config set gateway.reload.mode hybrid --dry-runopenclaw config set gateway.reload.mode hybridopenclaw config validate
[/code]

Jeśli zapis zostanie odrzucony, sprawdź zapisany ładunek i popraw pełny kształt konfiguracji:

bashCopy code
[code]
    CONFIG="$(openclaw config file)"ls -lt "$CONFIG".rejected.* 2>/dev/null | headopenclaw config validate
[/code]

Bezpośrednie zapisy w edytorze nadal są dozwolone, ale uruchomiony Gateway traktuje je jako niezaufane, dopóki nie przejdą walidacji. Nieprawidłowe bezpośrednie edycje powodują błąd uruchamiania albo są pomijane przez przeładowanie na gorąco; Gateway nie przepisuje `openclaw.json`. Uruchom `openclaw doctor --fix`, aby naprawić konfigurację z prefiksem/nadpisaną albo przywrócić ostatnią znaną dobrą kopię. Zobacz [rozwiązywanie problemów z Gateway](</pl/gateway/troubleshooting#gateway-rejected-invalid-config>).

Odzyskiwanie całego pliku jest zarezerwowane dla naprawy przez doctor. Zmiany schematu Plugin lub rozbieżność `minHostVersion` pozostają głośne zamiast wycofywać niepowiązane ustawienia użytkownika, takie jak modele, providerzy, profile uwierzytelniania, kanały, ekspozycja Gateway, narzędzia, pamięć, przeglądarka czy konfiguracja cron.

## Podkomendy

  * `config file`: Wypisuje ścieżkę aktywnego pliku konfiguracji (rozwiązaną z `OPENCLAW_CONFIG_PATH` albo domyślnej lokalizacji). Ścieżka powinna wskazywać zwykły plik, a nie dowiązanie symboliczne.


Uruchom ponownie gateway po zmianach.

## Walidacja

Zweryfikuj bieżącą konfigurację względem aktywnego schematu bez uruchamiania gateway.

bashCopy code
[code]
    openclaw config validateopenclaw config validate --json
[/code]

Gdy `openclaw config validate` przechodzi poprawnie, możesz użyć lokalnego TUI, aby osadzony agent porównał aktywną konfigurację z dokumentacją, podczas gdy walidujesz każdą zmianę z tego samego terminala:

bashCopy code
[code]
    openclaw chat
[/code]

Następnie wewnątrz TUI:

textCopy code
[code]
    !openclaw config file!openclaw docs gateway auth token secretref!openclaw config validate!openclaw doctor
[/code]

Typowa pętla naprawy:

* ### Porównaj z dokumentacją

Poproś agenta o porównanie bieżącej konfiguracji z odpowiednią stroną dokumentacji i zaproponowanie najmniejszej poprawki.

* ### Zastosuj ukierunkowane edycje

Zastosuj ukierunkowane edycje za pomocą `openclaw config set` albo `openclaw configure`.

* ### Zweryfikuj ponownie

Uruchom ponownie `openclaw config validate` po każdej zmianie.

* ### Doctor przy problemach w czasie działania

Jeśli walidacja przechodzi, ale środowisko wykonawcze nadal jest niezdrowe, uruchom `openclaw doctor` albo `openclaw doctor --fix`, aby uzyskać pomoc przy migracji i naprawie.

## Powiązane

  * [Dokumentacja CLI](</pl/cli>)
  * [Konfiguracja](</pl/gateway/configuration>)


Was this useful?YesNo