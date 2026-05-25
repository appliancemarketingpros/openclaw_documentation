---
title: Browser
source_url: https://docs.openclaw.ai/de/cli/browser
scraped_at: 2026-05-25
---

# `openclaw browser`

Verwalten Sie die Browser-Steuerungsoberfläche von OpenClaw und führen Sie Browser-Aktionen aus (Lebenszyklus, Profile, Tabs, Snapshots, Screenshots, Navigation, Eingabe, Zustandsemulation und Debugging).

Verwandt:

  * Browser-Tool + API: [Browser-Tool](</de/tools/browser>)


## Häufige Flags

  * `--url <gatewayWsUrl>`: Gateway-WebSocket-URL (standardmäßig aus der Konfiguration).
  * `--token <token>`: Gateway-Token (falls erforderlich).
  * `--timeout <ms>`: Anforderungs-Timeout (ms).
  * `--expect-final`: auf eine finale Gateway-Antwort warten.
  * `--browser-profile <name>`: ein Browser-Profil auswählen (Standard aus der Konfiguration).
  * `--json`: maschinenlesbare Ausgabe (wo unterstützt).


## Schnellstart (lokal)

bashCopy code
[code]
    openclaw browser profilesopenclaw browser --browser-profile openclaw startopenclaw browser --browser-profile openclaw open https://example.comopenclaw browser --browser-profile openclaw snapshot
[/code]

Agenten können dieselbe Bereitschaftsprüfung mit `browser({ action: "doctor" })` ausführen.

## Schnelle Fehlerbehebung

Wenn `start` mit `not reachable after start` fehlschlägt, prüfen Sie zuerst die CDP-Bereitschaft. Wenn `start` und `tabs` erfolgreich sind, aber `open` oder `navigate` fehlschlägt, ist die Browser-Steuerungsebene intakt und der Fehler liegt üblicherweise an der Navigations-SSRF-Richtlinie.

Minimale Sequenz:

bashCopy code
[code]
    openclaw browser --browser-profile openclaw doctoropenclaw browser --browser-profile openclaw startopenclaw browser --browser-profile openclaw tabsopenclaw browser --browser-profile openclaw open https://example.com
[/code]

Ausführliche Anleitung: [Browser-Fehlerbehebung](</de/tools/browser#cdp-startup-failure-vs-navigation-ssrf-block>)

## Lebenszyklus

bashCopy code
[code]
    openclaw browser statusopenclaw browser doctoropenclaw browser doctor --deepopenclaw browser startopenclaw browser start --headlessopenclaw browser stopopenclaw browser --browser-profile openclaw reset-profile
[/code]

Hinweise:

  * `doctor --deep` fügt eine Live-Snapshot-Prüfung hinzu. Das ist nützlich, wenn die grundlegende CDP-Bereitschaft grün ist, Sie aber einen Nachweis möchten, dass der aktuelle Tab inspiziert werden kann.
  * Für `attachOnly`\- und Remote-CDP-Profile schließt `openclaw browser stop` die aktive Steuerungssitzung und löscht temporäre Emulationsüberschreibungen, selbst wenn OpenClaw den Browser-Prozess nicht selbst gestartet hat.
  * Bei lokal verwalteten Profilen stoppt `openclaw browser stop` den gestarteten Browser-Prozess.
  * `openclaw browser start --headless` gilt nur für diese Startanforderung und nur, wenn OpenClaw einen lokal verwalteten Browser startet. Es schreibt `browser.headless` oder die Profilkonfiguration nicht um und hat bei einem bereits laufenden Browser keine Wirkung.
  * Auf Linux-Hosts ohne `DISPLAY` oder `WAYLAND_DISPLAY` laufen lokal verwaltete Profile automatisch im Headless-Modus, es sei denn, `OPENCLAW_BROWSER_HEADLESS=0`, `browser.headless=false` oder `browser.profiles.<name>.headless=false` fordert ausdrücklich einen sichtbaren Browser an.


## Wenn der Befehl fehlt

Wenn `openclaw browser` ein unbekannter Befehl ist, prüfen Sie `plugins.allow` in `~/.openclaw/openclaw.json`.

Wenn `plugins.allow` vorhanden ist, führen Sie das gebündelte Browser-Plugin explizit auf, es sei denn, die Konfiguration hat bereits einen Root-`browser`-Block:

json5Copy code
[code]
    {  plugins: {    allow: ["telegram", "browser"],  },}
[/code]

Ein expliziter Root-`browser`-Block, zum Beispiel `browser.enabled=true` oder `browser.profiles.<name>`, aktiviert das gebündelte Browser-Plugin ebenfalls unter einer restriktiven Plugin-Allowlist.

Verwandt: [Browser-Tool](</de/tools/browser#missing-browser-command-or-tool>)

## Profile

Profile sind benannte Browser-Routing-Konfigurationen. In der Praxis:

  * `openclaw`: startet eine dedizierte von OpenClaw verwaltete Chrome-Instanz (isoliertes Benutzerdatenverzeichnis) oder hängt sich daran an.
  * `user`: steuert Ihre bestehende angemeldete Chrome-Sitzung über Chrome DevTools MCP.
  * benutzerdefinierte CDP-Profile: verweisen auf einen lokalen oder Remote-CDP-Endpunkt.

bashCopy code
[code]
    openclaw browser profilesopenclaw browser create-profile --name work --color "#FF5A36"openclaw browser create-profile --name chrome-live --driver existing-sessionopenclaw browser create-profile --name remote --cdp-url https://browser-host.example.comopenclaw browser delete-profile --name work
[/code]

Ein bestimmtes Profil verwenden:

bashCopy code
[code]
    openclaw browser --browser-profile work tabs
[/code]

## Tabs

bashCopy code
[code]
    openclaw browser tabsopenclaw browser tab new --label docsopenclaw browser tab label t1 docsopenclaw browser tab select 2openclaw browser tab close 2openclaw browser open https://docs.openclaw.ai --label docsopenclaw browser focus docsopenclaw browser close t1
[/code]

`tabs` gibt zuerst `suggestedTargetId` zurück, dann die stabile `tabId` wie `t1`, das optionale Label und die rohe `targetId`. Agenten sollten `suggestedTargetId` an `focus`, `close`, Snapshots und Aktionen zurückgeben. Sie können ein Label mit `open --label`, `tab new --label` oder `tab label` zuweisen; Labels, Tab-IDs, rohe Ziel-IDs und eindeutige Ziel-ID-Präfixe werden alle akzeptiert. Wenn Chromium das zugrunde liegende rohe Ziel während einer Navigation oder Formularübermittlung ersetzt, behält OpenClaw die stabile `tabId` bzw. das Label am Ersatztab, wenn die Zuordnung nachgewiesen werden kann. Rohe Ziel-IDs bleiben flüchtig; bevorzugen Sie `suggestedTargetId`.

## Snapshot / Screenshot / Aktionen

Snapshot:

bashCopy code
[code]
    openclaw browser snapshotopenclaw browser snapshot --urls
[/code]

Screenshot:

bashCopy code
[code]
    openclaw browser screenshotopenclaw browser screenshot --full-pageopenclaw browser screenshot --ref e12openclaw browser screenshot --labels
[/code]

Hinweise:

  * `--full-page` ist nur für Seitenerfassungen gedacht; es kann nicht mit `--ref` oder `--element` kombiniert werden.
  * `existing-session`-/`user`-Profile unterstützen Seiten-Screenshots und `--ref`-Screenshots aus Snapshot-Ausgaben, aber keine CSS-`--element`-Screenshots.
  * `--labels` blendet aktuelle Snapshot-Refs über dem Screenshot ein.
  * `snapshot --urls` hängt erkannte Linkziele an KI-Snapshots an, damit Agenten direkte Navigationsziele auswählen können, statt nur anhand des Linktexts zu raten.


Navigieren/Klicken/Tippen (ref-basierte UI-Automatisierung):

bashCopy code
[code]
    openclaw browser navigate https://example.comopenclaw browser click <ref>openclaw browser click-coords 120 340openclaw browser type <ref> "hello"openclaw browser press Enteropenclaw browser hover <ref>openclaw browser scrollintoview <ref>openclaw browser drag <startRef> <endRef>openclaw browser select <ref> OptionA OptionBopenclaw browser fill --fields '[{"ref":"1","value":"Ada"}]'openclaw browser wait --text "Done"openclaw browser evaluate --fn '(el) => el.textContent' --ref <ref>
[/code]

Aktionsantworten geben die aktuelle rohe `targetId` nach einem durch eine Aktion ausgelösten Seitenersatz zurück, wenn OpenClaw den Ersatztab nachweisen kann. Skripte sollten für langlebige Workflows weiterhin `suggestedTargetId`/Labels speichern und übergeben.

Datei- und Dialog-Helfer:

bashCopy code
[code]
    openclaw browser upload /tmp/openclaw/uploads/file.pdf --ref <ref>openclaw browser waitfordownloadopenclaw browser download <ref> report.pdfopenclaw browser dialog --accept
[/code]

Verwaltete Chrome-Profile speichern gewöhnliche per Klick ausgelöste Downloads im OpenClaw-Download-Verzeichnis (`/tmp/openclaw/downloads` standardmäßig oder im konfigurierten temporären Root). Verwenden Sie `waitfordownload` oder `download`, wenn der Agent auf eine bestimmte Datei warten und deren Pfad zurückgeben muss; diese expliziten Wartefunktionen besitzen den nächsten Download.

## Zustand und Speicher

Viewport + Emulation:

bashCopy code
[code]
    openclaw browser resize 1280 720openclaw browser set viewport 1280 720openclaw browser set offline onopenclaw browser set media darkopenclaw browser set timezone Europe/Londonopenclaw browser set locale en-GBopenclaw browser set geo 51.5074 -0.1278 --accuracy 25openclaw browser set device "iPhone 14"openclaw browser set headers '{"x-test":"1"}'openclaw browser set credentials myuser mypass
[/code]

Cookies + Speicher:

bashCopy code
[code]
    openclaw browser cookiesopenclaw browser cookies set session abc123 --url https://example.comopenclaw browser cookies clearopenclaw browser storage local getopenclaw browser storage local set token abc123openclaw browser storage session clear
[/code]

## Debugging

bashCopy code
[code]
    openclaw browser console --level erroropenclaw browser pdfopenclaw browser responsebody "**/api"openclaw browser highlight <ref>openclaw browser errors --clearopenclaw browser requests --filter apiopenclaw browser trace startopenclaw browser trace stop --out trace.zip
[/code]

## Bestehendes Chrome über MCP

Verwenden Sie das integrierte `user`-Profil oder erstellen Sie Ihr eigenes `existing-session`-Profil:

bashCopy code
[code]
    openclaw browser --browser-profile user tabsopenclaw browser create-profile --name chrome-live --driver existing-sessionopenclaw browser create-profile --name brave-live --driver existing-session --user-data-dir "~/Library/Application Support/BraveSoftware/Brave-Browser"openclaw browser --browser-profile chrome-live tabs
[/code]

Dieser Pfad ist nur für den Host vorgesehen. Für Docker, Headless-Server, Browserless oder andere Remote-Setups verwenden Sie stattdessen ein CDP-Profil.

Aktuelle Einschränkungen von existing-session:

  * Snapshot-gesteuerte Aktionen verwenden Refs, keine CSS-Selektoren
  * `browser.actionTimeoutMs` setzt unterstützte `act`-Anforderungen standardmäßig auf 60000 ms, wenn Aufrufer `timeoutMs` weglassen; `timeoutMs` pro Aufruf hat weiterhin Vorrang.
  * `click` ist nur Linksklick
  * `type` unterstützt `slowly=true` nicht
  * `press` unterstützt `delayMs` nicht
  * `hover`, `scrollintoview`, `drag`, `select`, `fill` und `evaluate` lehnen Timeout-Überschreibungen pro Aufruf ab
  * `select` unterstützt nur einen Wert
  * `wait --load networkidle` wird nicht unterstützt
  * Datei-Uploads erfordern `--ref` / `--input-ref`, unterstützen kein CSS-`--element` und unterstützen derzeit jeweils nur eine Datei
  * Dialog-Hooks unterstützen `--timeout` nicht
  * Screenshots unterstützen Seitenerfassungen und `--ref`, aber kein CSS-`--element`
  * `responsebody`, Download-Abfangung, PDF-Export und Batch-Aktionen erfordern weiterhin einen verwalteten Browser oder ein rohes CDP-Profil


## Remote-Browser-Steuerung (Node-Host-Proxy)

Wenn der Gateway auf einer anderen Maschine läuft als der Browser, führen Sie einen **Node-Host** auf der Maschine aus, die Chrome/Brave/Edge/Chromium hat. Der Gateway leitet Browser-Aktionen an diesen Node weiter (kein separater Browser-Steuerungsserver erforderlich).

Verwenden Sie `gateway.nodes.browser.mode`, um das automatische Routing zu steuern, und `gateway.nodes.browser.node`, um einen bestimmten Node festzulegen, wenn mehrere verbunden sind.

Sicherheit + Remote-Einrichtung: [Browser-Tool](</de/tools/browser>), [Remote-Zugriff](</de/gateway/remote>), [Tailscale](</de/gateway/tailscale>), [Sicherheit](</de/gateway/security>)

## Verwandt

  * [CLI-Referenz](</de/cli>)
  * [Browser](</de/tools/browser>)


Was this useful?YesNo