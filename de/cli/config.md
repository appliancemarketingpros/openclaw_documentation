---
title: Konfiguration
source_url: https://docs.openclaw.ai/de/cli/config
scraped_at: 2026-05-25
---

Konfigurationshilfen für nicht interaktive Bearbeitungen in `openclaw.json`: Werte per Pfad abrufen/festlegen/patchen/entfernen sowie Datei/Schema validieren und die aktive Konfigurationsdatei ausgeben. Ohne Unterbefehl ausführen, um den Konfigurationsassistenten zu öffnen (wie `openclaw configure`).

## Root-Optionen

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tc2VjdGlvbiA8c2VjdGlvbg " type="string"> Wiederholbarer Abschnittsfilter für die geführte Einrichtung, wenn Sie `openclaw config` ohne Unterbefehl ausführen.

Unterstützte geführte Abschnitte: `workspace`, `model`, `web`, `gateway`, `daemon`, `channels`, `plugins`, `skills`, `health`.

## Beispiele

bashCopy code
[code]
    openclaw config fileopenclaw config --section modelopenclaw config --section gateway --section daemonopenclaw config schemaopenclaw config get browser.executablePathopenclaw config set browser.executablePath "/usr/bin/google-chrome"openclaw config set browser.profiles.work.executablePath "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"openclaw config set agents.defaults.heartbeat.every "2h"openclaw config set agents.list[0].tools.exec.node "node-id-or-name"openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKENopenclaw config set secrets.providers.vaultfile --provider-source file --provider-path /etc/openclaw/secrets.json --provider-mode jsonopenclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config unset plugins.entries.brave.config.webSearch.apiKeyopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKEN --dry-runopenclaw config validateopenclaw config validate --json
[/code]

### `config schema`

Das generierte JSON-Schema für `openclaw.json` als JSON auf stdout ausgeben.

Enthaltene Elemente

  * Das aktuelle Root-Konfigurationsschema plus ein Root-Stringfeld `$schema` für Editor-Werkzeuge.
  * Dokumentationsmetadaten `title` und `description`, die von der Control UI verwendet werden.
  * Verschachtelte Objekt-, Wildcard- (`*`) und Array-Element-Knoten (`[]`) erben dieselben Metadaten `title` / `description`, wenn passende Felddokumentation vorhanden ist.
  * Zweige `anyOf` / `oneOf` / `allOf` erben ebenfalls dieselben Dokumentationsmetadaten, wenn passende Felddokumentation vorhanden ist.
  * Bestmögliche Live-Schemametadaten für Plugin + Kanal, wenn Runtime-Manifeste geladen werden können.
  * Ein bereinigtes Fallback-Schema, auch wenn die aktuelle Konfiguration ungültig ist.

Zugehöriges Runtime-RPC

`config.schema.lookup` gibt einen normalisierten Konfigurationspfad mit einem flachen Schemaknoten (`title`, `description`, `type`, `enum`, `const`, gemeinsame Grenzen), passenden UI-Hinweismetadaten und direkten Zusammenfassungen der untergeordneten Elemente zurück. Verwenden Sie es für pfadbezogenes Drill-down in der Control UI oder in benutzerdefinierten Clients.

bashCopy code
[code]
    openclaw config schema
[/code]

Leiten Sie es in eine Datei um, wenn Sie es mit anderen Werkzeugen prüfen oder validieren möchten:

bashCopy code
[code]
    openclaw config schema > openclaw.schema.json
[/code]

### Pfade

Pfade verwenden Punkt- oder Klammernotation:

bashCopy code
[code]
    openclaw config get agents.defaults.workspaceopenclaw config get agents.list[0].id
[/code]

Verwenden Sie den Index der Agent-Liste, um einen bestimmten Agent anzusprechen:

bashCopy code
[code]
    openclaw config get agents.listopenclaw config set agents.list[1].tools.exec.node "node-id-or-name"
[/code]

## Werte

Werte werden, wenn möglich, als JSON5 geparst; andernfalls werden sie als Strings behandelt. Verwenden Sie `--strict-json`, um JSON5-Parsing zu verlangen. `--json` wird weiterhin als Legacy-Alias unterstützt.

bashCopy code
[code]
    openclaw config set agents.defaults.heartbeat.every "0m"openclaw config set gateway.port 19001 --strict-jsonopenclaw config set channels.whatsapp.groups '["*"]' --strict-json
[/code]

`config get <path> --json` gibt den Rohwert als JSON statt als für das Terminal formatierten Text aus.

Verwenden Sie `--merge`, wenn Sie Einträge zu diesen Maps hinzufügen:

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set models.providers.ollama.models '[{"id":"llama3.2","name":"Llama 3.2"}]' --strict-json --merge
[/code]

Verwenden Sie `--replace` nur, wenn der angegebene Wert bewusst zum vollständigen Zielwert werden soll.

## `config set`-Modi

`openclaw config set` unterstützt vier Zuweisungsarten:

### Wertmodus

bashCopy code
[code]
    openclaw config set <path> <value>
[/code]

### SecretRef-Builder-Modus

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN
[/code]

### Provider-Builder-Modus

Der Provider-Builder-Modus zielt nur auf Pfade `secrets.providers.<alias>` ab:

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-timeout-ms 5000
[/code]

### Batch-Modus

bashCopy code
[code]
    openclaw config set --batch-json '[  {    "path": "secrets.providers.default",    "provider": { "source": "env" }  },  {    "path": "channels.discord.token",    "ref": { "source": "env", "provider": "default", "id": "DISCORD_BOT_TOKEN" }  }]'
[/code]

bashCopy code
[code]
    openclaw config set --batch-file ./config-set.batch.json --dry-run
[/code]

Batch-Parsing verwendet immer die Batch-Nutzlast (`--batch-json`/`--batch-file`) als Quelle der Wahrheit. `--strict-json` / `--json` ändern das Batch-Parsing-Verhalten nicht.

## `config patch`

Verwenden Sie `config patch`, wenn Sie einen konfigurationsförmigen Patch einfügen oder per Pipe übergeben möchten, statt viele pfadbasierte `config set`-Befehle auszuführen. Die Eingabe ist ein JSON5-Objekt. Objekte werden rekursiv zusammengeführt, Arrays und skalare Werte ersetzen den Zielwert, und `null` löscht den Zielpfad.

bashCopy code
[code]
    openclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config patch --file ./openclaw.patch.json5
[/code]

Sie können einen Patch auch über stdin per Pipe übergeben; das ist für Remote-Einrichtungsskripte nützlich:

bashCopy code
[code]
    ssh openclaw-host 'openclaw config patch --stdin --dry-run' < ./openclaw.patch.json5ssh openclaw-host 'openclaw config patch --stdin' < ./openclaw.patch.json5
[/code]

Beispiel-Patch:

json5Copy code
[code]
    {  channels: {    slack: {      enabled: true,      mode: "socket",      botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },      appToken: { source: "env", provider: "default", id: "SLACK_APP_TOKEN" },      groupPolicy: "open",      requireMention: false,    },    discord: {      enabled: true,      token: { source: "env", provider: "default", id: "DISCORD_BOT_TOKEN" },      dmPolicy: "disabled",      dm: { enabled: false },      groupPolicy: "allowlist",    },  },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },      models: {        "openai/gpt-5.5": { params: { fastMode: true } },      },    },  },}
[/code]

Verwenden Sie `--replace-path <path>`, wenn ein Objekt oder Array genau zum angegebenen Wert werden muss, statt rekursiv gepatcht zu werden:

bashCopy code
[code]
    openclaw config patch --file ./discord.patch.json5 --replace-path 'channels.discord.guilds["123"].channels'
[/code]

`--dry-run` führt Schema- und SecretRef-Auflösbarkeitsprüfungen aus, ohne zu schreiben. Exec-gestützte SecretRefs werden während des Probelaufs standardmäßig übersprungen; fügen Sie `--allow-exec` hinzu, wenn der Probelauf bewusst Provider-Befehle ausführen soll.

Der JSON-Pfad-/Wertmodus wird weiterhin sowohl für SecretRefs als auch für Provider unterstützt:

bashCopy code
[code]
    openclaw config set channels.discord.token \  '{"source":"env","provider":"default","id":"DISCORD_BOT_TOKEN"}' \  --strict-json openclaw config set secrets.providers.vaultfile \  '{"source":"file","path":"/etc/openclaw/secrets.json","mode":"json"}' \  --strict-json
[/code]

## Provider-Builder-Flags

Provider-Builder-Ziele müssen `secrets.providers.<alias>` als Pfad verwenden.

Gemeinsame Flags

  * `--provider-source <env|file|exec>`
  * `--provider-timeout-ms <ms>` (`file`, `exec`)

Env-Provider (--provider-source env)

  * `--provider-allowlist &lt;ENV_VAR&gt;` (wiederholbar)

Datei-Provider (--provider-source file)

  * `--provider-path <path>` (erforderlich)
  * `--provider-mode <singleValue|json>`
  * `--provider-max-bytes <bytes>`
  * `--provider-allow-insecure-path`

Exec-Provider (--provider-source exec)

  * `--provider-command <path>` (erforderlich)
  * `--provider-arg <arg>` (wiederholbar)
  * `--provider-no-output-timeout-ms <ms>`
  * `--provider-max-output-bytes <bytes>`
  * `--provider-json-only`
  * `--provider-env &lt;KEY=VALUE&gt;` (wiederholbar)
  * `--provider-pass-env &lt;ENV_VAR&gt;` (wiederholbar)
  * `--provider-trusted-dir <path>` (wiederholbar)
  * `--provider-allow-insecure-path`
  * `--provider-allow-symlink-command`


Beispiel für einen gehärteten Exec-Provider:

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-json-only \  --provider-pass-env VAULT_TOKEN \  --provider-trusted-dir /usr/local/bin \  --provider-timeout-ms 5000
[/code]

## Probelauf

Verwenden Sie `--dry-run`, um Änderungen zu validieren, ohne `openclaw.json` zu schreiben.

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run \  --json openclaw config set channels.discord.token \  --ref-provider vault \  --ref-source exec \  --ref-id discord/token \  --dry-run \  --allow-exec
[/code]

Probelauf-Verhalten

  * Builder-Modus: führt SecretRef-Auflösbarkeitsprüfungen für geänderte Refs/Provider aus.
  * JSON-Modus (`--strict-json`, `--json` oder Batch-Modus): führt Schemavalidierung plus SecretRef-Auflösbarkeitsprüfungen aus.
  * Richtlinienvalidierung wird auch für bekannte nicht unterstützte SecretRef-Zieloberflächen ausgeführt.
  * Richtlinienprüfungen werten die vollständige Konfiguration nach der Änderung aus, sodass Schreibvorgänge auf übergeordnete Objekte (zum Beispiel das Festlegen von `hooks` als Objekt) die Validierung nicht unterstützter Oberflächen nicht umgehen können.
  * Exec-SecretRef-Prüfungen werden während des Probelaufs standardmäßig übersprungen, um Nebenwirkungen von Befehlen zu vermeiden.
  * Verwenden Sie `--allow-exec` mit `--dry-run`, um Exec-SecretRef-Prüfungen explizit zu aktivieren (dies kann Provider-Befehle ausführen).
  * `--allow-exec` ist nur für den Probelauf vorgesehen und führt zu einem Fehler, wenn es ohne `--dry-run` verwendet wird.

Felder von --dry-run --json

`--dry-run --json` gibt einen maschinenlesbaren Bericht aus:

  * `ok`: ob der Testlauf bestanden wurde
  * `operations`: Anzahl der ausgewerteten Zuweisungen
  * `checks`: ob Schema-/Auflösbarkeitsprüfungen ausgeführt wurden
  * `checks.resolvabilityComplete`: ob Auflösbarkeitsprüfungen bis zum Abschluss ausgeführt wurden (false, wenn exec-Refs übersprungen werden)
  * `refsChecked`: Anzahl der während des Testlaufs tatsächlich aufgelösten Refs
  * `skippedExecRefs`: Anzahl der exec-Refs, die übersprungen wurden, weil `--allow-exec` nicht gesetzt war
  * `errors`: strukturierte Schema-/Auflösbarkeitsfehler, wenn `ok=false`


### Form der JSON-Ausgabe

json5Copy code
[code]
    {  ok: boolean,  operations: number,  configPath: string,  inputModes: ["value" | "json" | "builder", ...],  checks: {    schema: boolean,    resolvability: boolean,    resolvabilityComplete: boolean,  },  refsChecked: number,  skippedExecRefs: number,  errors?: [    {      kind: "schema" | "resolvability",      message: string,      ref?: string, // present for resolvability errors    },  ],}
[/code]

### Erfolgsbeispiel

jsonCopy code
[code]
    {  "ok": true,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0}
[/code]

### Fehlerbeispiel

jsonCopy code
[code]
    {  "ok": false,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0,  "errors": [    {      "kind": "resolvability",      "message": "Error: Environment variable \"MISSING_TEST_SECRET\" is not set.",      "ref": "env:default:MISSING_TEST_SECRET"    }  ]}
[/code]

Wenn der Testlauf fehlschlägt

  * `config schema validation failed`: Ihre geänderte Config-Struktur ist ungültig; korrigieren Sie Pfad/Wert oder die Form des Provider-/Ref-Objekts.
  * `Config policy validation failed: unsupported SecretRef usage`: verschieben Sie diese Zugangsdaten zurück in Klartext-/String-Eingabe und verwenden Sie SecretRefs nur auf unterstützten Oberflächen.
  * `SecretRef assignment(s) could not be resolved`: referenzierter Provider/Ref kann derzeit nicht aufgelöst werden (fehlende Umgebungsvariable, ungültiger Dateizeiger, Fehler des exec-Providers oder Provider-/Quellenkonflikt).
  * `Dry run note: skipped <n> exec SecretRef resolvability check(s)`: Der Testlauf hat exec-Refs übersprungen; führen Sie ihn mit `--allow-exec` erneut aus, wenn Sie eine exec-Auflösbarkeitsprüfung benötigen.
  * Korrigieren Sie im Batch-Modus fehlschlagende Einträge und führen Sie `--dry-run` erneut aus, bevor Sie schreiben.


## Schreibsicherheit

`openclaw config set` und andere OpenClaw-eigene Config-Schreiber validieren die vollständige geänderte Config, bevor sie auf die Festplatte geschrieben wird. Wenn die neue Nutzlast die Schemavalidierung nicht besteht oder wie ein destruktives Überschreiben aussieht, bleibt die aktive Config unverändert und die abgelehnte Nutzlast wird daneben als `openclaw.json.rejected.*` gespeichert.

Bevorzugen Sie CLI-Schreibvorgänge für kleine Änderungen:

bashCopy code
[code]
    openclaw config set gateway.reload.mode hybrid --dry-runopenclaw config set gateway.reload.mode hybridopenclaw config validate
[/code]

Wenn ein Schreibvorgang abgelehnt wird, prüfen Sie die gespeicherte Nutzlast und korrigieren Sie die vollständige Config-Struktur:

bashCopy code
[code]
    CONFIG="$(openclaw config file)"ls -lt "$CONFIG".rejected.* 2>/dev/null | headopenclaw config validate
[/code]

Direkte Editor-Schreibvorgänge sind weiterhin erlaubt, aber das laufende Gateway behandelt sie als nicht vertrauenswürdig, bis sie validiert wurden. Ungültige direkte Änderungen lassen den Start fehlschlagen oder werden beim Hot Reload übersprungen; Gateway schreibt `openclaw.json` nicht neu. Führen Sie `openclaw doctor --fix` aus, um präfixierte/überschriebene Config zu reparieren oder die letzte als funktionierend bekannte Kopie wiederherzustellen. Siehe [Gateway-Fehlerbehebung](</de/gateway/troubleshooting#gateway-rejected-invalid-config>).

Die Wiederherstellung der gesamten Datei ist der Doctor-Reparatur vorbehalten. Plugin-Schemaänderungen oder `minHostVersion`-Abweichungen bleiben sichtbar, anstatt unabhängige Benutzereinstellungen wie Modelle, Provider, Auth-Profile, Kanäle, Gateway-Freigabe, Tools, Memory, Browser oder Cron-Config zurückzurollen.

## Unterbefehle

  * `config file`: Gibt den aktiven Config-Dateipfad aus (aufgelöst aus `OPENCLAW_CONFIG_PATH` oder dem Standardort). Der Pfad sollte eine reguläre Datei bezeichnen, keinen Symlink.


Starten Sie das Gateway nach Änderungen neu.

## Validieren

Validieren Sie die aktuelle Config gegen das aktive Schema, ohne das Gateway zu starten.

bashCopy code
[code]
    openclaw config validateopenclaw config validate --json
[/code]

Nachdem `openclaw config validate` erfolgreich ist, können Sie die lokale TUI verwenden, damit ein eingebetteter Agent die aktive Config mit der Dokumentation vergleicht, während Sie jede Änderung im selben Terminal validieren:

bashCopy code
[code]
    openclaw chat
[/code]

Dann innerhalb der TUI:

textCopy code
[code]
    !openclaw config file!openclaw docs gateway auth token secretref!openclaw config validate!openclaw doctor
[/code]

Typischer Reparaturablauf:

* ### Mit Dokumentation vergleichen

Bitten Sie den Agent, Ihre aktuelle Config mit der relevanten Dokumentationsseite zu vergleichen und die kleinste Korrektur vorzuschlagen.

* ### Gezielte Änderungen anwenden

Wenden Sie gezielte Änderungen mit `openclaw config set` oder `openclaw configure` an.

* ### Erneut validieren

Führen Sie `openclaw config validate` nach jeder Änderung erneut aus.

* ### Doctor für Laufzeitprobleme

Wenn die Validierung erfolgreich ist, die Laufzeit aber weiterhin fehlerhaft ist, führen Sie `openclaw doctor` oder `openclaw doctor --fix` aus, um Hilfe bei Migration und Reparatur zu erhalten.

## Siehe auch

  * [CLI-Referenz](</de/cli>)
  * [Konfiguration](</de/gateway/configuration>)


Was this useful?YesNo