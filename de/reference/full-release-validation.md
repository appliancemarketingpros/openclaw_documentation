---
title: Vollständige Release-Validierung
source_url: https://docs.openclaw.ai/de/reference/full-release-validation
scraped_at: 2026-05-25
---

`Full Release Validation` ist der übergeordnete Release-Workflow. Er ist der einzige manuelle Einstiegspunkt für den Vorab-Release-Nachweis, die meiste Arbeit erfolgt jedoch in untergeordneten Workflows, sodass eine fehlgeschlagene Box erneut ausgeführt werden kann, ohne das gesamte Release neu zu starten.

Führen Sie ihn von einer vertrauenswürdigen Workflow-Referenz aus aus, normalerweise `main`, und übergeben Sie den Release-Branch, das Tag oder die vollständige Commit-SHA als `ref`:

bashCopy code
[code]
    gh workflow run full-release-validation.yml \  --ref main \  -f ref=release/YYYY.M.D \  -f provider=openai \  -f mode=both \  -f release_profile=stable
[/code]

Untergeordnete Workflows verwenden die vertrauenswürdige Workflow-Referenz für den Harness und die Eingabe `ref` für den zu testenden Kandidaten. Dadurch bleibt neue Validierungslogik verfügbar, wenn ein älterer Release-Branch oder ein älteres Tag validiert wird.

Standardmäßig führt `release_profile=stable` die release-blockierenden Lanes aus und überspringt den umfassenden Live-/Docker-Soak. Übergeben Sie `run_release_soak=true`, um die Soak-Lanes in einen stabilen Lauf einzubeziehen. `release_profile=full` aktiviert Soak-Lanes immer, sodass das breite Advisory-Profil niemals stillschweigend Abdeckung verliert.

Package Acceptance baut den Kandidaten-Tarball normalerweise aus dem aufgelösten `ref`, einschließlich vollständiger SHA-Läufe, die mit `pnpm ci:full-release` ausgelöst wurden. Nach einer Beta-Veröffentlichung übergeben Sie `release_package_spec=openclaw@YYYY.M.D-beta.N`, um das ausgelieferte npm-Paket über Release-Prüfungen, Package Acceptance, cross-OS, Release-Path-Docker und Package Telegram hinweg wiederzuverwenden. Verwenden Sie `package_acceptance_package_spec` nur, wenn Package Acceptance absichtlich ein anderes Paket nachweisen soll.

## Phasen der obersten Ebene

Phase | Details  
---|---  
Zielauflösung | **Job:** `Resolve target ref`  
**Untergeordneter Workflow:** keiner |   
**Weist nach:** löst den Release-Branch, das Tag oder die vollständige Commit-SHA auf und zeichnet die ausgewählten Eingaben auf. |   
**Erneute Ausführung:** führen Sie den übergeordneten Workflow erneut aus, wenn dies fehlschlägt. |   
Vitest und normale CI | **Job:** `Run normal full CI`  
**Untergeordneter Workflow:** `CI` |   
**Weist nach:** manueller vollständiger CI-Graph gegen die Zielreferenz, einschließlich Linux-Node-Lanes, gebündelter Plugin-Shards, Channel-Verträgen, Node-22-Kompatibilität, `check`, `check-additional`, Build-Smoke, Dokumentationsprüfungen, Python-Skills, Windows, macOS, Control-UI-i18n und Android über den übergeordneten Workflow. |   
**Erneute Ausführung:** `rerun_group=ci`. |   
Plugin-Prerelease | **Job:** `Run plugin prerelease validation`  
**Untergeordneter Workflow:** `Plugin Prerelease` |   
**Weist nach:** release-spezifische statische Plugin-Prüfungen, agentische Plugin-Abdeckung, vollständige Erweiterungs-Batch-Shards, Plugin-Prerelease-Docker-Lanes und ein nicht blockierendes `plugin-inspector-advisory`-Artefakt für Kompatibilitätstriage. |   
**Erneute Ausführung:** `rerun_group=plugin-prerelease`. |   
Release-Prüfungen | **Job:** `Run release/live/Docker/QA validation`  
**Untergeordneter Workflow:** `OpenClaw Release Checks` |   
**Weist nach:** Installations-Smoke, cross-OS-Paketprüfungen, Package Acceptance, QA-Lab-Parität, Live-Matrix und Live-Telegram. Mit `run_release_soak=true` oder `release_profile=full` werden außerdem umfassende Live-/E2E-Suites und Docker-Release-Path-Chunks ausgeführt. |   
**Erneute Ausführung:** `rerun_group=release-checks` oder ein engerer Release-Checks-Handle. |   
Paketartefakt | **Job:** `Prepare release package artifact`  
**Untergeordneter Workflow:** keiner |   
**Weist nach:** erstellt den übergeordneten Tarball `release-package-under-test` früh genug für paketbezogene Prüfungen, die nicht auf `OpenClaw Release Checks` warten müssen. |   
**Erneute Ausführung:** führen Sie den übergeordneten Workflow erneut aus oder stellen Sie `release_package_spec` für erneute Läufe mit veröffentlichten Paketen bereit. |   
Package Telegram | **Job:** `Run package Telegram E2E`  
**Untergeordneter Workflow:** `NPM Telegram Beta E2E` |   
**Weist nach:** übergeordnetes artefaktgestütztes Telegram-Paket-Proof für `rerun_group=all` mit `release_profile=full` oder veröffentlichtes Paket-Telegram-Proof, wenn `release_package_spec` oder `npm_telegram_package_spec` gesetzt ist. |   
**Erneute Ausführung:** `rerun_group=npm-telegram` mit `release_package_spec` oder `npm_telegram_package_spec`. |   
Umbrella-Prüfer | **Job:** `Verify full validation`  
**Untergeordneter Workflow:** keiner |   
**Weist nach:** prüft aufgezeichnete Ergebnisse untergeordneter Läufe erneut und hängt Tabellen der langsamsten Jobs aus untergeordneten Workflows an. |   
**Erneute Ausführung:** führen Sie nur diesen Job erneut aus, nachdem ein fehlgeschlagener untergeordneter Workflow erneut bis Grün ausgeführt wurde. |   
  
Für `ref=main` und `rerun_group=all` ersetzt ein neuerer übergeordneter Workflow einen älteren. Wenn der übergeordnete Workflow abgebrochen wird, bricht sein Monitor alle untergeordneten Workflows ab, die er bereits ausgelöst hat. Release-Branch- und Tag-Validierungsläufe brechen sich standardmäßig nicht gegenseitig ab.

## Phasen der Release-Prüfungen

`OpenClaw Release Checks` ist der größte untergeordnete Workflow. Er löst das Ziel einmal auf und bereitet ein gemeinsames `release-package-under-test`-Artefakt vor, wenn paket- oder Docker-bezogene Phasen es benötigen.

Phase | Details  
---|---  
Release-Ziel | **Job:** `Resolve target ref`  
**Zugrunde liegender Workflow:** keiner |   
**Tests:** ausgewählte Referenz, optional erwartete SHA, Profil, Rerun-Gruppe und fokussierter Live-Suite-Filter. |   
**Rerun:** `rerun_group=release-checks`. |   
Paketartefakt | **Job:** `Prepare release package artifact`  
**Zugrunde liegender Workflow:** keiner |   
**Tests:** packt oder ermittelt einen Kandidaten-Tarball und lädt `release-package-under-test` für nachgelagerte paketbezogene Prüfungen hoch. |   
**Rerun:** das betroffene Paket, die Cross-OS- oder die Live/E2E-Gruppe. |   
Installations-Smoke | **Job:** `Run install smoke`  
**Zugrunde liegender Workflow:** `Install Smoke` |   
**Tests:** vollständiger Installationspfad mit Wiederverwendung des Root-Dockerfile-Smoke-Images, QR-Paketinstallation, Root- und Gateway-Docker-Smokes, Installer-Docker-Tests, Bun-Global-Install-Image-Provider-Smoke und schnellem gebündeltem Plugin-Installations-/Deinstallations-E2E. |   
**Rerun:** `rerun_group=install-smoke`. |   
Cross-OS | **Job:** `cross_os_release_checks`  
**Zugrunde liegender Workflow:** `OpenClaw Cross-OS Release Checks (Reusable)` |   
**Tests:** Fresh- und Upgrade-Lanes unter Linux, Windows und macOS für den ausgewählten Provider und Modus, mit dem Kandidaten-Tarball plus Baseline-Paket. |   
**Rerun:** `rerun_group=cross-os`. |   
Repo und Live-E2E | **Job:** `Run repo/live E2E validation`  
**Zugrunde liegender Workflow:** `OpenClaw Live And E2E Checks (Reusable)` |   
**Tests:** Repository-E2E, Live-Cache, OpenAI-Websocket-Streaming, nativer Live-Provider und Plugin-Shards sowie Docker-gestützte Live-Model-/Backend-/Gateway-Harnesses, ausgewählt durch `release_profile`. |   
**Läufe:** `run_release_soak=true`, `release_profile=full` oder fokussiertes `rerun_group=live-e2e`. |   
**Rerun:** `rerun_group=live-e2e`, optional mit `live_suite_filter`. |   
Docker-Release-Pfad | **Job:** `Run Docker release-path validation`  
**Zugrunde liegender Workflow:** `OpenClaw Live And E2E Checks (Reusable)` |   
**Tests:** Release-Pfad-Docker-Chunks gegen das gemeinsame Paketartefakt. |   
**Läufe:** `run_release_soak=true`, `release_profile=full` oder fokussiertes `rerun_group=live-e2e`. |   
**Rerun:** `rerun_group=live-e2e`. |   
Paketakzeptanz | **Job:** `Run package acceptance`  
**Zugrunde liegender Workflow:** `Package Acceptance` |   
**Tests:** Offline-Plugin-Paket-Fixtures, Plugin-Aktualisierung, mock-OpenAI-Telegram-Paketakzeptanz und Prüfungen für überlebende veröffentlichte Upgrades gegen denselben Tarball. Blockierende Release-Prüfungen verwenden die standardmäßig zuletzt veröffentlichte Baseline; Soak-Prüfungen werden auf jede stabile npm-Version ab `2026.4.23` sowie gemeldete Issue-Fixtures erweitert. |   
**Rerun:** `rerun_group=package`. |   
QA-Parität | **Job:** `Run QA Lab parity lane` und `Run QA Lab parity report`  
**Zugrunde liegender Workflow:** direkte Jobs |   
**Tests:** agentische Paritätspakete für Kandidat und Baseline, danach der Paritätsbericht. |   
**Rerun:** `rerun_group=qa-parity` oder `rerun_group=qa`. |   
QA-Live-Matrix | **Job:** `Run QA Lab live Matrix lane`  
**Zugrunde liegender Workflow:** direkter Job |   
**Tests:** schnelles Live-Matrix-QA-Profil in der Umgebung `qa-live-shared`. |   
**Rerun:** `rerun_group=qa-live` oder `rerun_group=qa`. |   
QA-Live-Telegram | **Job:** `Run QA Lab live Telegram lane`  
**Zugrunde liegender Workflow:** direkter Job |   
**Tests:** Live-Telegram-QA mit Convex-CI-Anmeldedaten-Leases. |   
**Rerun:** `rerun_group=qa-live` oder `rerun_group=qa`. |   
Release-Verifier | **Job:** `Verify release checks`  
**Zugrunde liegender Workflow:** keiner |   
**Tests:** erforderliche Release-Prüf-Jobs für die ausgewählte Rerun-Gruppe. |   
**Rerun:** erneut ausführen, nachdem fokussierte Child-Jobs bestanden haben. |   
  
## Docker-Release-Pfad-Chunks

Die Docker-Release-Pfad-Phase führt diese Chunks aus, wenn `live_suite_filter` leer ist:

Chunk | Abdeckung  
---|---  
`core` | Core-Docker-Release-Pfad-Smoke-Lanes.  
`package-update-openai` | OpenAI-Paketinstallations-/-aktualisierungsverhalten, Codex-On-Demand-Installation und Chat Completions-Tool-Aufrufe.  
`package-update-anthropic` | Anthropic-Paketinstallations- und Aktualisierungsverhalten.  
`package-update-core` | Provider-neutrales Paket- und Aktualisierungsverhalten.  
`plugins-runtime-plugins` | Plugin-Runtime-Lanes, die Plugin-Verhalten ausüben.  
`plugins-runtime-services` | Service-gestützte und Live-Plugin-Runtime-Lanes; enthält OpenWebUI, wenn angefordert.  
`plugins-runtime-install-a` through `plugins-runtime-install-h` | Plugin-Installations-/Runtime-Batches, aufgeteilt für parallele Release-Validierung.  
  
Verwenden Sie gezielt `docker_lanes=<lane[,lane]>` im wiederverwendbaren Live/E2E-Workflow, wenn nur eine Docker-Lane fehlgeschlagen ist. Die Release-Artefakte enthalten Rerun-Befehle pro Lane mit Eingaben für Paketartefakt- und Image-Wiederverwendung, wenn verfügbar.

## Release-Profile

`release_profile` steuert hauptsächlich die Live-/Provider-Breite innerhalb der Release-Prüfungen. Es entfernt nicht die normale vollständige CI, Plugin-Prerelease, Installations-Smoke, Paketakzeptanz oder QA Lab. Für `stable` sind erschöpfende Repo-/Live-E2E- und Docker- Release-Pfad-Chunks Soak-Abdeckung und laufen, wenn `run_release_soak=true`. `full` erzwingt die Soak-Abdeckung und sorgt außerdem dafür, dass der Umbrella-Lauf Paket-Telegram- E2E gegen das übergeordnete Release-Paketartefakt ausführt, wenn `rerun_group=all`, sodass ein vollständiger Pre-Publish-Kandidat diese Telegram-Paket-Lane nicht stillschweigend überspringt.

Profil | Vorgesehene Verwendung | Enthaltene Live-/Provider-Abdeckung  
---|---|---  
`minimum` | Schnellster releasekritischer Smoke. | OpenAI/Core-Live-Pfad, Docker-Live-Modelle für OpenAI, nativer Gateway-Core, natives OpenAI-Gateway-Profil, natives OpenAI-Plugin und Docker-Live-Gateway OpenAI.  
`stable` | Standardprofil für Release-Freigaben. | `minimum` plus Anthropic-Smoke, Google, MiniMax, Backend, natives Live-Test-Harness, Docker-Live-CLI-Backend, Docker-ACP-Bind, Docker-Codex-Harness und ein OpenCode Go-Smoke-Shard.  
`full` | Breiter beratender Sweep. | `stable` plus beratende Provider, Plugin-Live-Shards und Medien-Live-Shards.  
  
## Nur in Full enthaltene Ergänzungen

Diese Suites werden von `stable` übersprungen und von `full` eingeschlossen:

Bereich | Nur in Full enthaltene Abdeckung  
---|---  
Docker-Live-Modelle | OpenCode Go, OpenRouter, xAI, [Z.ai](<http://Z.ai>) und Fireworks.  
Docker-Live-Gateway | Beratende Provider, aufgeteilt in DeepSeek/Fireworks-, OpenCode Go/OpenRouter- und xAI/Z.ai-Shards.  
Native Gateway-Provider-Profile | Vollständige Anthropic Opus- und Sonnet/Haiku-Shards, Fireworks, DeepSeek, vollständige OpenCode Go-Modell-Shards, OpenRouter, xAI und [Z.ai](<http://Z.ai>).  
Native Plugin-Live-Shards | Plugins A-K, L-N, O-Z other, Moonshot und xAI.  
Native Medien-Live-Shards | Audio, Google-Musik, MiniMax-Musik und Videogruppen A-D.  
  
`stable` enthält `native-live-src-gateway-profiles-anthropic-smoke` und `native-live-src-gateway-profiles-opencode-go-smoke`; `full` verwendet stattdessen die breiteren Anthropic- und OpenCode Go-Modell-Shards. Fokussierte Reruns können weiterhin die aggregierten Handles `native-live-src-gateway-profiles-anthropic` oder `native-live-src-gateway-profiles-opencode-go` verwenden.

## Fokussierte Reruns

Verwenden Sie `rerun_group`, um zu vermeiden, dass nicht zusammenhängende Release-Boxen wiederholt werden:

Handle | Geltungsbereich  
---|---  
`all` | Alle Phasen der Full Release Validation.  
`ci` | Nur manueller vollständiger CI-Child.  
`plugin-prerelease` | Nur Plugin-Prerelease-Child.  
`release-checks` | Alle Phasen der OpenClaw Release Checks.  
`install-smoke` | Install Smoke über Release Checks.  
`cross-os` | Cross-OS-Release-Checks.  
`live-e2e` | Repo-/Live-E2E- und Docker-Validierung des Release-Pfads.  
`package` | Package Acceptance.  
`qa` | QA-Parität plus QA-Live-Lanes.  
`qa-parity` | Nur QA-Paritäts-Lanes und Bericht.  
`qa-live` | Nur QA-Live-Matrix und Telegram.  
`npm-telegram` | Telegram-E2E für veröffentlichtes Package; erfordert `release_package_spec` oder `npm_telegram_package_spec`.  
  
Verwenden Sie `live_suite_filter` mit `rerun_group=live-e2e`, wenn eine Live-Suite fehlgeschlagen ist. Gültige Filter-IDs sind im wiederverwendbaren Live-/E2E-Workflow definiert, einschließlich `docker-live-models`, `live-gateway-docker`, `live-gateway-anthropic-docker`, `live-gateway-google-docker`, `live-gateway-minimax-docker`, `live-gateway-advisory-docker`, `live-cli-backend-docker`, `live-acp-bind-docker` und `live-codex-harness-docker`.

Der Handle `live-gateway-advisory-docker` ist ein aggregierter Rerun-Handle für seine drei Provider-Shards, daher fächert er weiterhin auf alle Advisory-Docker-Gateway-Jobs auf.

Verwenden Sie `cross_os_suite_filter` mit `rerun_group=cross-os`, wenn eine Cross-OS-Lane fehlgeschlagen ist. Der Filter akzeptiert eine OS-ID, eine Suite-ID oder ein OS-/Suite-Paar, zum Beispiel `windows/packaged-upgrade`, `windows` oder `packaged-fresh`. Cross-OS- Zusammenfassungen enthalten Zeitmessungen pro Phase für Packaged-Upgrade-Lanes, und lang laufende Befehle geben Heartbeat-Zeilen aus, sodass ein festhängendes Windows-Update vor dem Job-Timeout sichtbar ist.

QA-Release-Check-Lanes sind advisory. Ein reiner QA-Fehler wird als Warnung gemeldet und blockiert den Release-Check-Verifier nicht; führen Sie `rerun_group=qa`, `qa-parity` oder `qa-live` erneut aus, wenn Sie frische QA-Nachweise benötigen.

## Aufzubewahrende Nachweise

Bewahren Sie die Zusammenfassung `Full Release Validation` als Index auf Release-Ebene auf. Sie verlinkt Child-Run-IDs und enthält Tabellen der langsamsten Jobs. Prüfen Sie bei Fehlern zuerst den Child- Workflow, und führen Sie dann den kleinsten passenden Handle oben erneut aus.

Nützliche Artefakte:

  * `release-package-under-test` aus dem Full-Release-Validation-Parent und `OpenClaw Release Checks`
  * Docker-Release-Pfad-Artefakte unter `.artifacts/docker-tests/`
  * Package-Acceptance-`package-under-test` und Docker-Acceptance-Artefakte
  * Cross-OS-Release-Check-Artefakte für jedes OS und jede Suite
  * QA-Paritäts-, Matrix- und Telegram-Artefakte


## Workflow-Dateien

  * `.github/workflows/full-release-validation.yml`
  * `.github/workflows/openclaw-release-checks.yml`
  * `.github/workflows/openclaw-live-and-e2e-checks-reusable.yml`
  * `.github/workflows/plugin-prerelease.yml`
  * `.github/workflows/install-smoke.yml`
  * `.github/workflows/openclaw-cross-os-release-checks-reusable.yml`
  * `.github/workflows/package-acceptance.yml`


Was this useful?YesNo