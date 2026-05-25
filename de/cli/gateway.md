---
title: Gateway
source_url: https://docs.openclaw.ai/de/cli/gateway
scraped_at: 2026-05-25
---

The Gateway ist der WebSocket-Server von OpenClaw (Kanäle, Nodes, Sitzungen, Hooks). Unterbefehle auf dieser Seite befinden sich unter `openclaw gateway …`.

[**Bonjour discovery** Lokales mDNS + Wide-Area-DNS-SD-Setup. ](</de/gateway/bonjour>) [**Discovery overview** Wie OpenClaw Gateways ankündigt und findet. ](</de/gateway/discovery>) [**Configuration** Gateway-Konfigurationsschlüssel auf oberster Ebene. ](</de/gateway/configuration>)

## Gateway ausführen

Führen Sie einen lokalen Gateway-Prozess aus:

bashCopy code
[code]
    openclaw gateway
[/code]

Alias für die Ausführung im Vordergrund:

bashCopy code
[code]
    openclaw gateway run
[/code]

Startup behavior

  * Standardmäßig verweigert der Gateway den Start, sofern `gateway.mode=local` nicht in `~/.openclaw/openclaw.json` festgelegt ist. Verwenden Sie `--allow-unconfigured` für Ad-hoc-/Dev-Ausführungen.
  * `openclaw onboard --mode local` und `openclaw setup` sollen `gateway.mode=local` schreiben. Wenn die Datei existiert, aber `gateway.mode` fehlt, behandeln Sie dies als beschädigte oder überschriebene Konfiguration und reparieren Sie sie, statt den lokalen Modus implizit anzunehmen.
  * Wenn die Datei existiert und `gateway.mode` fehlt, behandelt der Gateway dies als verdächtigen Konfigurationsschaden und verweigert es, für Sie „local zu erraten“.
  * Binden über Loopback hinaus ohne Authentifizierung wird blockiert (Sicherheitsleitplanke).
  * `SIGUSR1` löst einen In-Process-Neustart aus, wenn dies autorisiert ist (`commands.restart` ist standardmäßig aktiviert; setzen Sie `commands.restart: false`, um manuelle Neustarts zu blockieren, während Anwenden/Aktualisieren per Gateway-Tool/Konfiguration weiterhin erlaubt bleibt).
  * `SIGINT`-/`SIGTERM`-Handler stoppen den Gateway-Prozess, stellen aber keinen benutzerdefinierten Terminalzustand wieder her. Wenn Sie die CLI mit einer TUI oder Raw-Mode-Eingabe umschließen, stellen Sie das Terminal vor dem Beenden wieder her.


### Optionen

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tcG9ydCA8cG9ydA " type="number"> WebSocket-Port (Standardwert stammt aus Konfiguration/Env; üblicherweise `18789`).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tdG9rZW4gPHRva2Vu " type="string"> Token-Überschreibung (setzt außerdem `OPENCLAW_GATEWAY_TOKEN` für den Prozess).

Tailscale-Serve-/Funnel-Konfiguration beim Herunterfahren zurücksetzen.

Gateway-Start ohne `gateway.mode=local` in der Konfiguration erlauben. Umgeht die Startschutzprüfung nur für Ad-hoc-/Dev-Bootstrap; schreibt oder repariert die Konfigurationsdatei nicht.

Dev-Konfiguration + Workspace erstellen, falls sie fehlen (überspringt [BOOTSTRAP.md](<http://BOOTSTRAP.md>)).

Dev-Konfiguration + Anmeldedaten + Sitzungen + Workspace zurücksetzen (erfordert `--dev`).

Vor dem Start jeden vorhandenen Listener auf dem ausgewählten Port beenden.

Ausführliche Logs.

Nur CLI-Backend-Logs in der Konsole anzeigen (und stdout/stderr aktivieren).

Alias für `--ws-log compact`.

Rohe Modell-Stream-Ereignisse in jsonl protokollieren.

## Gateway neu starten

bashCopy code
[code]
    openclaw gateway restartopenclaw gateway restart --safeopenclaw gateway restart --safe --skip-deferralopenclaw gateway restart --force
[/code]

`openclaw gateway restart --safe` fordert den laufenden Gateway auf, aktive OpenClaw-Arbeit vor dem Neustart per Preflight zu prüfen. Wenn Vorgänge in der Warteschlange, Antwortzustellung, eingebettete Ausführungen oder Task-Ausführungen aktiv sind, meldet der Gateway die Blocker, fasst doppelte Safe-Restart-Anforderungen zusammen und startet neu, sobald die aktive Arbeit abgearbeitet ist. Ein einfaches `restart` behält aus Kompatibilitätsgründen das bestehende Service-Manager-Verhalten bei. Verwenden Sie `--force` nur, wenn Sie ausdrücklich den sofortigen Override-Pfad wünschen.

`openclaw gateway restart --safe --skip-deferral` führt denselben OpenClaw-bewussten koordinierten Neustart wie `--safe` aus, umgeht aber die Zurückstellungsprüfung für aktive Arbeit, sodass der Gateway den Neustart sofort ausgibt, auch wenn Blocker gemeldet werden. Verwenden Sie dies als operatorseitigen Notausstieg, wenn eine Zurückstellung durch eine hängengebliebene Task-Ausführung festhängt und `--safe` allein unbegrenzt warten würde. `--skip-deferral` erfordert `--safe`.

### Startprofiling

  * Setzen Sie `OPENCLAW_GATEWAY_STARTUP_TRACE=1`, um Phasen-Timings während des Gateway-Starts zu protokollieren, einschließlich `eventLoopMax`-Verzögerung pro Phase und Plugin-Lookup-Table-Timings für installed-index, Manifest-Registry, Startplanung und Owner-Map-Arbeit.
  * Setzen Sie `OPENCLAW_DIAGNOSTICS=timeline` mit `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=<path>`, um eine Best-Effort-JSONL-Startdiagnose-Timeline für externe QA-Harnesses zu schreiben. Sie können das Flag auch mit `diagnostics.flags: ["timeline"]` in der Konfiguration aktivieren; der Pfad wird weiterhin per Env bereitgestellt. Fügen Sie `OPENCLAW_DIAGNOSTICS_EVENT_LOOP=1` hinzu, um Event-Loop-Samples einzuschließen.
  * Führen Sie `pnpm test:startup:gateway -- --runs 5 --warmup 1` aus, um den Gateway-Start zu benchmarken. Der Benchmark zeichnet die erste Prozessausgabe, `/healthz`, `/readyz`, Start-Trace-Timings, Event-Loop-Verzögerung und Timingdetails der Plugin-Lookup-Table auf.


## Laufenden Gateway abfragen

Alle Abfragebefehle verwenden WebSocket-RPC.

### Output modes

  * Standard: menschenlesbar (in TTY farbig).
  * `--json`: maschinenlesbares JSON (ohne Styling/Spinner).
  * `--no-color` (oder `NO_COLOR=1`): ANSI deaktivieren, während das menschenlesbare Layout erhalten bleibt.


### Shared options

  * `--url <url>`: Gateway-WebSocket-URL.
  * `--token <token>`: Gateway-Token.
  * `--password <password>`: Gateway-Passwort.
  * `--timeout <ms>`: Timeout/Budget (variiert je nach Befehl).
  * `--expect-final`: auf eine „final“-Antwort warten (Agent-Aufrufe).


### `gateway health`

bashCopy code
[code]
    openclaw gateway health --url ws://127.0.0.1:18789
[/code]

Der HTTP-Endpunkt `/healthz` ist eine Liveness-Probe: Er antwortet, sobald der Server HTTP beantworten kann. Der HTTP-Endpunkt `/readyz` ist strenger und bleibt rot, während Start-Plugin-Sidecars, Kanäle oder konfigurierte Hooks noch stabilisieren. Lokale oder authentifizierte detaillierte Bereitschaftsantworten enthalten einen `eventLoop`-Diagnoseblock mit Event-Loop-Verzögerung, Event-Loop-Auslastung, CPU-Core-Verhältnis und einem `degraded`-Flag.

### `gateway usage-cost`

Nutzungs- und Kostenzusammenfassungen aus Sitzungslogs abrufen.

bashCopy code
[code]
    openclaw gateway usage-costopenclaw gateway usage-cost --days 7openclaw gateway usage-cost --json
[/code]

### `gateway stability`

Den aktuellen Diagnose-Stabilitätsrecorder von einem laufenden Gateway abrufen.

bashCopy code
[code]
    openclaw gateway stabilityopenclaw gateway stability --type payload.largeopenclaw gateway stability --bundle latestopenclaw gateway stability --bundle latest --exportopenclaw gateway stability --json
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tbGltaXQgPGxpbWl0 " type="number" default="25"> Maximale Anzahl einzuschließender aktueller Ereignisse (max. `1000`).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tdHlwZSA8dHlwZQ " type="string"> Nach Diagnoseereignistyp filtern, etwa `payload.large` oder `diagnostic.memory.pressure`.

Ein persistiertes Stabilitätsbundle lesen, statt den laufenden Gateway aufzurufen. Verwenden Sie `--bundle latest` (oder nur `--bundle`) für das neueste Bundle unter dem Zustandsverzeichnis, oder übergeben Sie direkt einen Bundle-JSON-Pfad.

Eine teilbare ZIP-Datei mit Supportdiagnosen schreiben, statt Stabilitätsdetails auszugeben.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tb3V0cHV0IDxwYXRo " type="string"> Ausgabepfad für `--export`.

Privacy and bundle behavior

  * Datensätze behalten operative Metadaten: Ereignisnamen, Zählwerte, Bytegrößen, Speicherwerte, Warteschlangen-/Sitzungszustand, Kanal-/Plugin-Namen und redigierte Sitzungszusammenfassungen. Sie behalten keinen Chattext, keine Webhook-Bodys, keine Tool-Ausgaben, keine rohen Anfrage- oder Antwortbodys, Tokens, Cookies, geheimen Werte, Hostnamen oder rohen Sitzungs-IDs. Setzen Sie `diagnostics.enabled: false`, um den Recorder vollständig zu deaktivieren.
  * Bei fatalen Gateway-Beendigungen, Shutdown-Timeouts und Startfehlern nach Neustarts schreibt OpenClaw denselben Diagnose-Snapshot nach `~/.openclaw/logs/stability/openclaw-stability-*.json`, wenn der Recorder Ereignisse hat. Prüfen Sie das neueste Bundle mit `openclaw gateway stability --bundle latest`; `--limit`, `--type` und `--since-seq` gelten ebenfalls für Bundle-Ausgaben.


### `gateway diagnostics export`

Eine lokale Diagnose-ZIP-Datei schreiben, die zum Anhängen an Fehlerberichte vorgesehen ist. Informationen zum Datenschutzmodell und zu Bundle-Inhalten finden Sie unter [Diagnostics Export](</de/gateway/diagnostics>).

bashCopy code
[code]
    openclaw gateway diagnostics exportopenclaw gateway diagnostics export --output openclaw-diagnostics.zipopenclaw gateway diagnostics export --json
[/code]

Suche nach persistiertem Stabilitätsbundle überspringen.

Den geschriebenen Pfad, die Größe und das Manifest als JSON ausgeben.

Der Export enthält ein Manifest, eine Markdown-Zusammenfassung, Konfigurationsstruktur, bereinigte Konfigurationsdetails, bereinigte Logzusammenfassungen, bereinigte Gateway-Status-/Health-Snapshots und, falls vorhanden, das neueste Stabilitätsbundle.

Er ist zum Teilen vorgesehen. Er behält operative Details, die beim Debugging helfen, etwa sichere OpenClaw-Logfelder, Subsystemnamen, Statuscodes, Dauern, konfigurierte Modi, Ports, Plugin-IDs, Provider-IDs, nicht geheime Feature-Einstellungen und redigierte operative Logmeldungen. Er lässt Chattext, Webhook-Bodys, Tool-Ausgaben, Anmeldedaten, Cookies, Konto-/Nachrichtenkennungen, Prompt-/Anweisungstext, Hostnamen und geheime Werte aus oder redigiert sie. Wenn eine LogTape-artige Nachricht wie Benutzer-/Chat-/Tool-Payload-Text aussieht, behält der Export nur bei, dass eine Nachricht ausgelassen wurde, plus ihre Byteanzahl.

### `gateway status`

`gateway status` zeigt den Gateway-Dienst (launchd/systemd/schtasks) sowie optional eine Probe der Konnektivitäts-/Authentifizierungsfähigkeit.

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway status --jsonopenclaw gateway status --require-rpc
[/code]

Überspringt die Konnektivitätsprüfung (nur Service-Ansicht).

Scannt auch systemweite Services.

Erweitert die standardmäßige Konnektivitätsprüfung zu einer Leseprüfung und beendet den Prozess mit einem Nicht-Null-Code, wenn diese Leseprüfung fehlschlägt. Kann nicht mit `--no-probe` kombiniert werden.

Statussemantik

  * `gateway status` bleibt für Diagnosen verfügbar, selbst wenn die lokale CLI-Konfiguration fehlt oder ungültig ist.
  * Das standardmäßige `gateway status` weist den Service-Zustand, die WebSocket-Verbindung und die zum Handshake-Zeitpunkt sichtbare Authentifizierungsfähigkeit nach. Es weist keine Lese-/Schreib-/Admin-Operationen nach.
  * Diagnoseprüfungen verändern bei der erstmaligen Geräteauthentifizierung nichts: Sie verwenden ein vorhandenes zwischengespeichertes Geräte-Token wieder, falls eines vorhanden ist, erstellen aber keine neue CLI-Geräteidentität oder schreibgeschützten Gerätekopplungsdatensatz nur zur Statusprüfung.
  * `gateway status` löst konfigurierte Authentifizierungs-SecretRefs für die Prüf-Authentifizierung auf, wenn möglich.
  * Wenn ein erforderlicher Authentifizierungs-SecretRef in diesem Befehlspfad nicht aufgelöst wird, meldet `gateway status --json` `rpc.authWarning`, wenn Prüfkonnektivität/Authentifizierung fehlschlägt; übergeben Sie `--token`/`--password` explizit oder lösen Sie zuerst die Secret-Quelle auf.
  * Wenn die Prüfung erfolgreich ist, werden Warnungen zu nicht aufgelösten Authentifizierungsreferenzen unterdrückt, um falsch positive Meldungen zu vermeiden.
  * Verwenden Sie `--require-rpc` in Skripten und Automatisierung, wenn ein lauschender Service nicht ausreicht und auch RPC-Aufrufe mit Leseumfang fehlerfrei sein müssen.
  * `--deep` fügt einen Best-Effort-Scan nach zusätzlichen launchd-/systemd-/schtasks-Installationen hinzu. Wenn mehrere Gateway-ähnliche Services erkannt werden, gibt die Ausgabe für Menschen Bereinigungshinweise aus und warnt, dass die meisten Setups ein Gateway pro Maschine ausführen sollten.
  * `--deep` meldet außerdem eine kürzliche Übergabe eines Gateway-Supervisor-Neustarts, wenn der Service-Prozess für einen externen Supervisor-Neustart sauber beendet wurde.
  * `--deep` führt die Konfigurationsvalidierung im Plugin-fähigen Modus (`pluginValidation: "full"`) aus und zeigt konfigurierte Plugin-Manifestwarnungen an (zum Beispiel fehlende Metadaten zur Kanalkonfiguration), damit Installations- und Update-Smoke-Checks sie erkennen. Das standardmäßige `gateway status` behält den schnellen schreibgeschützten Pfad bei, der die Plugin-Validierung überspringt.
  * Die Ausgabe für Menschen enthält den aufgelösten Dateilogpfad sowie eine Momentaufnahme der CLI-gegenüber-Service-Konfigurationspfade/-Gültigkeit, um Profil- oder Zustandsverzeichnisdrift zu diagnostizieren.

Linux-systemd-Prüfungen auf Authentifizierungsdrift

  * Bei Linux-systemd-Installationen lesen Prüfungen auf Service-Authentifizierungsdrift sowohl `Environment=`\- als auch `EnvironmentFile=`-Werte aus der Unit (einschließlich `%h`, zitierter Pfade, mehrerer Dateien und optionaler `-`-Dateien).
  * Driftprüfungen lösen `gateway.auth.token`-SecretRefs mit der zusammengeführten Laufzeitumgebung auf (zuerst Service-Befehlsumgebung, dann Prozessumgebung als Fallback).
  * Wenn Token-Authentifizierung nicht effektiv aktiv ist (expliziter `gateway.auth.mode` von `password`/`none`/`trusted-proxy` oder nicht gesetzter Modus, bei dem das Passwort gewinnen kann und kein Token-Kandidat gewinnen kann), überspringen Token-Driftprüfungen die Auflösung des Konfigurationstokens.


### `gateway probe`

`gateway probe` ist der Befehl zum „Alles debuggen“. Er prüft immer:

  * Ihr konfiguriertes Remote-Gateway (falls gesetzt) und
  * localhost (local loopback), **selbst wenn ein Remote-Ziel konfiguriert ist**.


Wenn Sie `--url` übergeben, wird dieses explizite Ziel vor beiden hinzugefügt. Die Ausgabe für Menschen kennzeichnet die Ziele als:

  * `URL (explicit)`
  * `Remote (configured)` oder `Remote (configured, inactive)`
  * `Local loopback`

bashCopy code
[code]
    openclaw gateway probeopenclaw gateway probe --json
[/code]

Interpretation

  * `Reachable: yes` bedeutet, dass mindestens ein Ziel eine WebSocket-Verbindung akzeptiert hat.
  * `Capability: read-only|write-capable|admin-capable|pairing-pending|connect-only` meldet, was die Prüfung über die Authentifizierung nachweisen konnte. Dies ist von der Erreichbarkeit getrennt.
  * `Read probe: ok` bedeutet, dass auch Detail-RPC-Aufrufe mit Leseumfang (`health`/`status`/`system-presence`/`config.get`) erfolgreich waren.
  * `Read probe: limited - missing scope: operator.read` bedeutet, dass die Verbindung erfolgreich war, RPC mit Leseumfang aber eingeschränkt ist. Dies wird als **eingeschränkte** Erreichbarkeit gemeldet, nicht als vollständiger Fehler.
  * `Read probe: failed` nach `Connect: ok` bedeutet, dass das Gateway die WebSocket-Verbindung akzeptiert hat, nachfolgende Lesediagnosen aber wegen Zeitüberschreitung oder Fehlern scheiterten. Auch dies ist **eingeschränkte** Erreichbarkeit, kein unerreichbares Gateway.
  * Wie `gateway status` verwendet probe vorhandene zwischengespeicherte Geräteauthentifizierung wieder, erstellt aber keine erstmalige Geräteidentität oder keinen Kopplungszustand.
  * Der Exit-Code ist nur dann ungleich null, wenn kein geprüftes Ziel erreichbar ist.

JSON-Ausgabe

Oberste Ebene:

  * `ok`: Mindestens ein Ziel ist erreichbar.
  * `degraded`: Mindestens ein Ziel hat eine Verbindung akzeptiert, aber die vollständige Detail-RPC-Diagnose nicht abgeschlossen.
  * `capability`: Beste Fähigkeit, die über erreichbare Ziele hinweg gesehen wurde (`read_only`, `write_capable`, `admin_capable`, `pairing_pending`, `connected_no_operator_scope` oder `unknown`).
  * `primaryTargetId`: Bestes Ziel, das in dieser Reihenfolge als aktiver Gewinner behandelt werden soll: explizite URL, SSH-Tunnel, konfiguriertes Remote-Ziel, dann local loopback.
  * `warnings[]`: Best-Effort-Warndatensätze mit `code`, `message` und optionalen `targetIds`.
  * `network`: Hinweise auf local loopback-/Tailnet-URLs, abgeleitet aus aktueller Konfiguration und Host-Netzwerk.
  * `discovery.timeoutMs` und `discovery.count`: Das tatsächlich für diesen Prüfdurchlauf verwendete Discovery-Budget bzw. die Ergebnisanzahl.


Pro Ziel (`targets[].connect`):

  * `ok`: Erreichbarkeit nach Verbindung + Einstufung als eingeschränkt.
  * `rpcOk`: Vollständiger Detail-RPC-Erfolg.
  * `scopeLimited`: Detail-RPC ist wegen fehlendem Operator-Umfang fehlgeschlagen.


Pro Ziel (`targets[].auth`):

  * `role`: In `hello-ok` gemeldete Authentifizierungsrolle, wenn verfügbar.
  * `scopes`: In `hello-ok` gemeldete gewährte Umfänge, wenn verfügbar.
  * `capability`: Die angezeigte Klassifizierung der Authentifizierungsfähigkeit für dieses Ziel.

Häufige Warncodes

  * `ssh_tunnel_failed`: Einrichtung des SSH-Tunnels fehlgeschlagen; der Befehl ist auf direkte Prüfungen zurückgefallen.
  * `multiple_gateways`: Mehr als ein Ziel war erreichbar; dies ist ungewöhnlich, sofern Sie nicht absichtlich isolierte Profile ausführen, etwa einen Rettungs-Bot.
  * `auth_secretref_unresolved`: Ein konfigurierter Authentifizierungs-SecretRef konnte für ein fehlgeschlagenes Ziel nicht aufgelöst werden.
  * `probe_scope_limited`: WebSocket-Verbindung erfolgreich, aber die Leseprüfung wurde durch fehlendes `operator.read` eingeschränkt.


#### Remote über SSH (Parität mit der Mac-App)

Der macOS-App-Modus „Remote over SSH“ verwendet eine lokale Portweiterleitung, sodass das Remote-Gateway (das möglicherweise nur an local loopback gebunden ist) unter `ws://127.0.0.1:<port>` erreichbar wird.

CLI-Entsprechung:

bashCopy code
[code]
    openclaw gateway probe --ssh user@gateway-host
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tc3NoIDx0YXJnZXQ " type="string"> `user@host` oder `user@host:port` (Port ist standardmäßig `22`).

Wählt den ersten erkannten Gateway-Host als SSH-Ziel aus dem aufgelösten Discovery-Endpunkt (`local.` plus konfigurierte Wide-Area-Domain, falls vorhanden). Nur-TXT-Hinweise werden ignoriert.

Konfiguration (optional, als Standardwerte verwendet):

  * `gateway.remote.sshTarget`
  * `gateway.remote.sshIdentity`


### `gateway call <method>`

Low-Level-RPC-Helfer.

bashCopy code
[code]
    openclaw gateway call statusopenclaw gateway call logs.tail --params '{"sinceMs": 60000}'
[/code]

Hauptsächlich für agentenartige RPCs, die Zwischenereignisse vor einer finalen Nutzlast streamen.

Maschinenlesbare JSON-Ausgabe.

## Gateway-Service verwalten

bashCopy code
[code]
    openclaw gateway installopenclaw gateway startopenclaw gateway stopopenclaw gateway restartopenclaw gateway uninstall
[/code]

### Mit einem Wrapper installieren

Verwenden Sie `--wrapper`, wenn der verwaltete Service über ein anderes ausführbares Programm gestartet werden muss, zum Beispiel ein Secrets-Manager-Shim oder ein Run-as-Helfer. Der Wrapper erhält die normalen Gateway-Argumente und ist dafür verantwortlich, schließlich `openclaw` oder Node mit diesen Argumenten per exec auszuführen.

bashCopy code
[code]
    cat > ~/.local/bin/openclaw-doppler <<'EOF'#!/usr/bin/env bashset -euo pipefailexec doppler run --project my-project --config production -- openclaw "$@"EOFchmod +x ~/.local/bin/openclaw-doppler openclaw gateway install --wrapper ~/.local/bin/openclaw-doppler --forceopenclaw gateway restart
[/code]

Sie können den Wrapper auch über die Umgebung setzen. `gateway install` validiert, dass der Pfad eine ausführbare Datei ist, schreibt den Wrapper in die Service-`ProgramArguments` und persistiert `OPENCLAW_WRAPPER` in der Service-Umgebung für spätere erzwungene Neuinstallationen, Updates und doctor- Reparaturen.

bashCopy code
[code]
    OPENCLAW_WRAPPER="$HOME/.local/bin/openclaw-doppler" openclaw gateway install --forceopenclaw doctor
[/code]

Um einen persistierten Wrapper zu entfernen, leeren Sie `OPENCLAW_WRAPPER` während der Neuinstallation:

bashCopy code
[code]
    OPENCLAW_WRAPPER= openclaw gateway install --forceopenclaw gateway restart
[/code]

Befehlsoptionen

  * `gateway status`: `--url`, `--token`, `--password`, `--timeout`, `--no-probe`, `--require-rpc`, `--deep`, `--json`
  * `gateway install`: `--port`, `--runtime <node|bun>`, `--token`, `--wrapper <path>`, `--force`, `--json`
  * `gateway restart`: `--safe`, `--skip-deferral`, `--force`, `--wait <duration>`, `--json`
  * `gateway uninstall|start`: `--json`
  * `gateway stop`: `--disable`, `--json`

Lifecycle-Verhalten

  * Verwenden Sie `gateway restart`, um einen verwalteten Dienst neu zu starten. Verketten Sie `gateway stop` und `gateway start` nicht als Ersatz für einen Neustart.
  * Unter macOS verwendet `gateway stop` standardmäßig `launchctl bootout`, wodurch der LaunchAgent aus der aktuellen Boot-Sitzung entfernt wird, ohne eine Deaktivierung dauerhaft zu speichern — die automatische KeepAlive-Wiederherstellung bleibt für zukünftige Abstürze aktiv und `gateway start` aktiviert sauber erneut, ohne ein manuelles `launchctl enable`. Übergeben Sie `--disable`, um KeepAlive und RunAtLoad dauerhaft zu unterdrücken, damit der Gateway bis zum nächsten expliziten `gateway start` nicht neu startet; verwenden Sie dies, wenn ein manueller Stopp Neustarts oder Systemneustarts überdauern soll.
  * `gateway restart --safe` weist den laufenden Gateway an, aktive OpenClaw-Arbeit vorab zu prüfen und den Neustart aufzuschieben, bis Antwortzustellung, eingebettete Runs und Task-Runs abgearbeitet sind. `--safe` kann nicht mit `--force` oder `--wait` kombiniert werden.
  * `gateway restart --wait 30s` überschreibt das konfigurierte Drain-Budget für diesen Neustart. Zahlen ohne Einheit sind Millisekunden; Einheiten wie `s`, `m` und `h` werden akzeptiert. `--wait 0` wartet unbegrenzt.
  * `gateway restart --safe --skip-deferral` führt den OpenClaw-bewussten sicheren Neustart aus, umgeht aber das Aufschub-Gate, sodass der Gateway den Neustart sofort auslöst, auch wenn Blocker gemeldet werden. Operator-Notausstieg für Aufschübe durch hängende Task-Runs; erfordert `--safe`.
  * `gateway restart --force` überspringt das Drain aktiver Arbeit und startet sofort neu. Verwenden Sie dies, wenn ein Operator die aufgeführten Task-Blocker bereits geprüft hat und den Gateway jetzt zurückhaben möchte.
  * Lifecycle-Befehle akzeptieren `--json` für Skripting.

Authentifizierung und SecretRefs zum Installationszeitpunkt

  * Wenn Token-Authentifizierung ein Token erfordert und `gateway.auth.token` von SecretRef verwaltet wird, validiert `gateway install`, dass die SecretRef auflösbar ist, speichert das aufgelöste Token jedoch nicht dauerhaft in Dienstumgebungs-Metadaten.
  * Wenn Token-Authentifizierung ein Token erfordert und die konfigurierte Token-SecretRef nicht aufgelöst ist, schlägt die Installation geschlossen fehl, statt Fallback-Klartext dauerhaft zu speichern.
  * Für Passwortauthentifizierung bei `gateway run` bevorzugen Sie `OPENCLAW_GATEWAY_PASSWORD`, `--password-file` oder ein SecretRef-gestütztes `gateway.auth.password` gegenüber inline `--password`.
  * Im abgeleiteten Authentifizierungsmodus lockert ein nur in der Shell gesetztes `OPENCLAW_GATEWAY_PASSWORD` die Token-Anforderungen für die Installation nicht; verwenden Sie dauerhafte Konfiguration (`gateway.auth.password` oder Konfiguration `env`), wenn Sie einen verwalteten Dienst installieren.
  * Wenn sowohl `gateway.auth.token` als auch `gateway.auth.password` konfiguriert sind und `gateway.auth.mode` nicht gesetzt ist, wird die Installation blockiert, bis der Modus explizit gesetzt ist.


## Gateways ermitteln (Bonjour)

`gateway discover` sucht nach Gateway-Beacons (`_openclaw-gw._tcp`).

  * Multicast DNS-SD: `local.`
  * Unicast DNS-SD (Wide-Area Bonjour): Wählen Sie eine Domain (Beispiel: `openclaw.internal.`) und richten Sie Split-DNS + einen DNS-Server ein; siehe [Bonjour](</de/gateway/bonjour>).


Nur Gateways mit aktivierter Bonjour-Ermittlung (Standard) kündigen den Beacon an.

Wide-Area-Ermittlungsdatensätze können diese TXT-Hinweise enthalten:

  * `role` (Hinweis zur Gateway-Rolle)
  * `transport` (Transporthinweis, z. B. `gateway`)
  * `gatewayPort` (WebSocket-Port, üblicherweise `18789`)
  * `sshPort` (nur vollständiger Ermittlungsmodus; Clients verwenden standardmäßig SSH-Ziele auf `22`, wenn er fehlt)
  * `tailnetDns` (MagicDNS-Hostname, wenn verfügbar)
  * `gatewayTls` / `gatewayTlsSha256` (TLS aktiviert + Zertifikat-Fingerabdruck)
  * `cliPath` (nur vollständiger Ermittlungsmodus)


### `gateway discover`

bashCopy code
[code]
    openclaw gateway discover
[/code]

Maschinenlesbare Ausgabe (deaktiviert auch Styling/Spinner).

Beispiele:

bashCopy code
[code]
    openclaw gateway discover --timeout 4000openclaw gateway discover --json | jq '.beacons[].wsUrl'
[/code]

## Verwandte Themen

  * [CLI-Referenz](</de/cli>)
  * [Gateway-Runbook](</de/gateway>)


Was this useful?YesNo