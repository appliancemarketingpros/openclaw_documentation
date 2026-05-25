---
title: Aktualisieren
source_url: https://docs.openclaw.ai/de/cli/update
scraped_at: 2026-05-25
---

# `openclaw update`

OpenClaw sicher aktualisieren und zwischen Stable-/Beta-/Dev-Kanälen wechseln.

Wenn Sie über **npm/pnpm/bun** installiert haben (globale Installation, keine Git-Metadaten), erfolgen Aktualisierungen über den Package-Manager-Ablauf in [Aktualisieren](</de/install/updating>).

## Verwendung

bashCopy code
[code]
    openclaw updateopenclaw update statusopenclaw update wizardopenclaw update --channel betaopenclaw update --channel devopenclaw update --tag betaopenclaw update --tag mainopenclaw update --dry-runopenclaw update --no-restartopenclaw update --yesopenclaw update --jsonopenclaw --update
[/code]

## Optionen

  * `--no-restart`: überspringt den Neustart des Gateway-Dienstes nach einer erfolgreichen Aktualisierung. Package-Manager-Aktualisierungen, die den Gateway neu starten, prüfen, ob der neu gestartete Dienst die erwartete aktualisierte Version meldet, bevor der Befehl erfolgreich abgeschlossen wird.
  * `--channel <stable|beta|dev>`: legt den Update-Kanal fest (Git + npm; wird in der Konfiguration gespeichert).
  * `--tag <dist-tag|version|spec>`: überschreibt das Package-Ziel nur für diese Aktualisierung. Bei Package-Installationen wird `main` auf `github:openclaw/openclaw#main` abgebildet.
  * `--dry-run`: zeigt die geplanten Update-Aktionen (Kanal/Tag/Ziel/Neustart-Ablauf) an, ohne Konfiguration zu schreiben, zu installieren, Plugins zu synchronisieren oder neu zu starten.
  * `--json`: gibt maschinenlesbares `UpdateRunResult`-JSON aus, einschließlich `postUpdate.plugins.warnings`, wenn beschädigte oder nicht ladbare verwaltete Plugins nach erfolgreicher Kernaktualisierung repariert werden müssen, Details zum Plugin-Fallback im Beta-Kanal, wenn ein Plugin kein Beta-Release hat, und `postUpdate.plugins.integrityDrifts`, wenn während der Plugin-Synchronisierung nach der Aktualisierung eine Abweichung von npm-Plugin-Artefakten erkannt wird.
  * `--timeout <seconds>`: Timeout pro Schritt (Standard ist 1800s).
  * `--yes`: überspringt Bestätigungsaufforderungen (zum Beispiel die Bestätigung eines Downgrades).


`openclaw update` hat kein `--verbose`-Flag. Verwenden Sie `--dry-run`, um die geplanten Kanal-/Tag-/Installations-/Neustart-Aktionen vorab anzuzeigen, `--json` für maschinenlesbare Ergebnisse und `openclaw update status --json`, wenn Sie nur Kanal- und Verfügbarkeitsdetails benötigen. Wenn Sie Gateway-Protokolle rund um eine Aktualisierung debuggen, sind Konsolenausführlichkeit und Datei-Loglevel getrennt: Gateway `--verbose` wirkt sich auf Terminal-/WebSocket-Ausgaben aus, während Datei-Logs `logging.level: "debug"` oder `"trace"` in der Konfiguration erfordern. Siehe [Gateway-Logging](</de/gateway/logging>).

## `update status`

Zeigt den aktiven Update-Kanal + Git-Tag/Branch/SHA (für Quellcode-Checkouts) sowie die Update-Verfügbarkeit an.

bashCopy code
[code]
    openclaw update statusopenclaw update status --jsonopenclaw update status --timeout 10
[/code]

Optionen:

  * `--json`: gibt maschinenlesbares Status-JSON aus.
  * `--timeout <seconds>`: Timeout für Prüfungen (Standard ist 3s).


## `update wizard`

Interaktiver Ablauf zur Auswahl eines Update-Kanals und zur Bestätigung, ob der Gateway nach der Aktualisierung neu gestartet werden soll (Standard ist Neustart). Wenn Sie `dev` ohne Git-Checkout auswählen, wird angeboten, einen zu erstellen.

Optionen:

  * `--timeout <seconds>`: Timeout für jeden Update-Schritt (Standard `1800`)


## Funktionsweise

Wenn Sie Kanäle explizit wechseln (`--channel ...`), hält OpenClaw auch die Installationsmethode abgestimmt:

  * `dev` → stellt einen Git-Checkout sicher (Standard: `~/openclaw`, überschreibbar mit `OPENCLAW_GIT_DIR`), aktualisiert ihn und installiert die globale CLI aus diesem Checkout.
  * `stable` → installiert aus npm mit `latest`.
  * `beta` → bevorzugt den npm-Dist-Tag `beta`, fällt aber auf `latest` zurück, wenn Beta fehlt oder älter als das aktuelle Stable-Release ist.


Der automatische Updater des Gateway-Kerns (wenn über die Konfiguration aktiviert) startet den CLI-Update-Pfad außerhalb des laufenden Gateway-Request-Handlers. Package-Manager-Aktualisierungen über die Control-Plane `update.run` erzwingen nach dem Package-Austausch einen nicht verzögerten Neustart ohne Cooldown, weil der alte Gateway-Prozess möglicherweise noch In-Memory-Chunks hat, die auf Dateien verweisen, die durch das neue Package entfernt wurden.

Bei Package-Manager-Installationen löst `openclaw update` die Ziel-Package-Version auf, bevor der Package Manager aufgerufen wird. Globale npm-Installationen verwenden eine gestufte Installation: OpenClaw installiert das neue Package in ein temporäres npm-Präfix, verifiziert dort das gepackte `dist`-Inventar und tauscht dann diesen sauberen Package-Baum in das echte globale Präfix ein. Wenn die Verifizierung fehlschlägt, werden Post-Update-Doctor, Plugin-Synchronisierung und Neustartarbeiten nicht aus dem verdächtigen Baum ausgeführt. Selbst wenn die installierte Version bereits dem Ziel entspricht, aktualisiert der Befehl die globale Package-Installation, führt anschließend die Plugin-Synchronisierung, eine Aktualisierung der Kernbefehls-Vervollständigung und Neustartarbeiten aus. Dadurch bleiben gepackte Sidecars und kanalverwaltete Plugin-Datensätze mit dem installierten OpenClaw-Build abgestimmt, während vollständige Neuaufbauten der Plugin-Befehlsvervollständigung expliziten `openclaw completion --write-state`-Ausführungen überlassen bleiben.

Wenn ein lokaler verwalteter Gateway-Dienst installiert und der Neustart aktiviert ist, stoppen Package-Manager-Aktualisierungen den laufenden Dienst, bevor der Package-Baum ersetzt wird, aktualisieren dann die Dienstmetadaten aus der aktualisierten Installation, starten den Dienst neu und prüfen, ob der neu gestartete Gateway die erwartete Version meldet, bevor Erfolg gemeldet wird. Unter macOS prüft die Post-Update-Prüfung außerdem, ob der LaunchAgent für das aktive Profil geladen/ausgeführt wird und der konfigurierte Loopback-Port funktionsfähig ist. Wenn die plist installiert ist, aber nicht von launchd überwacht wird, bootstrapt OpenClaw den LaunchAgent automatisch neu und führt anschließend die Health-/Versions-/Kanal-Bereitschaftsprüfungen erneut aus. Ein frischer Bootstrap lädt den RunAtLoad-Job direkt, sodass die Update-Wiederherstellung den neu gestarteten Gateway nicht sofort mit `kickstart -k` neu anstößt. Wenn der Gateway weiterhin nicht funktionsfähig wird, beendet sich der Befehl mit einem Nicht-Null-Code und gibt den Pfad zum Neustartprotokoll sowie explizite Anweisungen für Neustart, Neuinstallation und Package-Rollback aus. Mit `--no-restart` wird der Package-Austausch weiterhin ausgeführt, aber der verwaltete Dienst wird nicht gestoppt oder neu gestartet, sodass der laufende Gateway alten Code behalten kann, bis Sie ihn manuell neu starten.

## Git-Checkout-Ablauf

### Kanalauswahl

  * `stable`: den neuesten Nicht-Beta-Tag auschecken, dann Build und Doctor ausführen.
  * `beta`: den neuesten `-beta`-Tag bevorzugen, aber auf den neuesten Stable-Tag zurückfallen, wenn Beta fehlt oder älter ist.
  * `dev`: `main` auschecken, dann abrufen und rebasen.


### Update-Schritte

* ### Sauberen Worktree verifizieren

Erfordert keine uncommitteten Änderungen.

* ### Kanal wechseln

Wechselt zum ausgewählten Kanal (Tag oder Branch).

* ### Upstream abrufen

Nur Dev.

* ### Preflight-Build (nur Dev)

Führt den TypeScript-Build in einem temporären Worktree aus. Wenn die Spitze fehlschlägt, geht er bis zu 10 Commits zurück, um den neuesten baubaren Commit zu finden. Setzen Sie `OPENCLAW_UPDATE_PREFLIGHT_LINT=1`, um während dieses Preflights auch Lint auszuführen; Lint läuft im eingeschränkten seriellen Modus, weil Update-Hosts von Benutzern oft kleiner sind als CI-Runner.

* ### Rebase

Rebast auf den ausgewählten Commit (nur Dev).

* ### Abhängigkeiten installieren

Verwendet den Package Manager des Repos. Bei pnpm-Checkouts bootstrapt der Updater `pnpm` bei Bedarf (zuerst über `corepack`, dann mit einem temporären `npm install pnpm@11`-Fallback), statt `npm run build` innerhalb eines pnpm-Workspace auszuführen.

* ### Control UI bauen

Baut den Gateway und die Control UI.

* ### Doctor ausführen

`openclaw doctor` läuft als abschließende Safe-Update-Prüfung.

* ### Plugins synchronisieren

Synchronisiert Plugins mit dem aktiven Kanal. Dev verwendet gebündelte Plugins; Stable und Beta verwenden npm. Aktualisiert nachverfolgte Plugin-Installationen.

Im Beta-Update-Kanal versuchen nachverfolgte npm- und ClawHub-Plugin-Installationen, die der Default-/Latest-Linie folgen, zuerst ein Plugin-`@beta`-Release. Wenn das Plugin kein Beta-Release hat, fällt OpenClaw auf die aufgezeichnete Default-/Latest-Spezifikation zurück und meldet dies als Warnung. Bei npm-Plugins fällt OpenClaw außerdem zurück, wenn das Beta- Package existiert, aber die Installationsvalidierung fehlschlägt. Diese Plugin-Fallback-Warnungen führen nicht dazu, dass die Kernaktualisierung fehlschlägt. Exakte Versionen und explizite Tags werden nicht umgeschrieben.

## `--update`-Kurzform

`openclaw --update` wird zu `openclaw update` umgeschrieben (nützlich für Shells und Launcher-Skripte).

## Verwandt

  * `openclaw doctor` (bietet bei Git-Checkouts an, zuerst das Update auszuführen)
  * [Entwicklungskanäle](</de/install/development-channels>)
  * [Aktualisieren](</de/install/updating>)
  * [CLI-Referenz](</de/cli>)


Was this useful?YesNo