---
title: Genehmigungen
source_url: https://docs.openclaw.ai/de/cli/approvals
scraped_at: 2026-05-25
---

# `openclaw approvals`

Verwalten Sie Exec-Genehmigungen für den **lokalen Host** , den **Gateway-Host** oder einen **Node-Host**. Standardmäßig zielen Befehle auf die lokale Genehmigungsdatei auf dem Datenträger. Verwenden Sie `--gateway`, um das Gateway anzusprechen, oder `--node`, um eine bestimmte Node anzusprechen.

Alias: `openclaw exec-approvals`

Verwandt:

  * Exec-Genehmigungen: [Exec approvals](</de/tools/exec-approvals>)
  * Nodes: [Nodes](</de/nodes>)


## `openclaw exec-policy`

`openclaw exec-policy` ist der lokale Komfortbefehl, um die angeforderte Konfiguration `tools.exec.*` und die lokale Host-Genehmigungsdatei in einem Schritt synchron zu halten.

Verwenden Sie ihn, wenn Sie Folgendes möchten:

  * die lokal angeforderte Richtlinie, die Host-Genehmigungsdatei und die effektive Zusammenführung prüfen
  * ein lokales Preset wie YOLO oder deny-all anwenden
  * lokales `tools.exec.*` und lokales `~/.openclaw/exec-approvals.json` synchronisieren


Beispiele:

bashCopy code
[code]
    openclaw exec-policy showopenclaw exec-policy show --json openclaw exec-policy preset yoloopenclaw exec-policy preset cautious --json openclaw exec-policy set --host gateway --security full --ask off --ask-fallback full
[/code]

Ausgabemodi:

  * ohne `--json`: gibt die menschenlesbare Tabellenansicht aus
  * mit `--json`: gibt maschinenlesbare strukturierte Ausgabe aus


Aktueller Geltungsbereich:

  * `exec-policy` ist **nur lokal**
  * es aktualisiert die lokale Konfigurationsdatei und die lokale Genehmigungsdatei gemeinsam
  * es überträgt die Richtlinie **nicht** an den Gateway-Host oder einen Node-Host
  * `--host node` wird in diesem Befehl abgelehnt, weil Node-Exec-Genehmigungen zur Laufzeit von der Node abgerufen werden und stattdessen über nodegerichtete Genehmigungsbefehle verwaltet werden müssen
  * `openclaw exec-policy show` markiert Bereiche mit `host=node` zur Laufzeit als Node-verwaltet, statt eine effektive Richtlinie aus der lokalen Genehmigungsdatei abzuleiten


Wenn Sie Genehmigungen eines Remote-Hosts direkt bearbeiten müssen, verwenden Sie weiter `openclaw approvals set --gateway` oder `openclaw approvals set --node <id|name|ip>`.

## Häufige Befehle

bashCopy code
[code]
    openclaw approvals getopenclaw approvals get --node <id|name|ip>openclaw approvals get --gateway
[/code]

`openclaw approvals get` zeigt jetzt die effektive Exec-Richtlinie für lokale, Gateway- und Node-Ziele an:

  * angeforderte `tools.exec`-Richtlinie
  * Host-Richtlinie aus der Genehmigungsdatei
  * effektives Ergebnis nach Anwendung der Prioritätsregeln


Die Priorität ist beabsichtigt:

  * die Host-Genehmigungsdatei ist die durchsetzbare Quelle der Wahrheit
  * die angeforderte `tools.exec`-Richtlinie kann die Absicht einschränken oder erweitern, aber das effektive Ergebnis wird weiterhin aus den Host-Regeln abgeleitet
  * `--node` kombiniert die Node-Host-Genehmigungsdatei mit der Gateway-Richtlinie `tools.exec`, weil beides zur Laufzeit weiterhin gilt
  * wenn die Gateway-Konfiguration nicht verfügbar ist, greift die CLI auf den Snapshot der Node-Genehmigungen zurück und weist darauf hin, dass die endgültige Laufzeitrichtlinie nicht berechnet werden konnte


## Genehmigungen aus einer Datei ersetzen

bashCopy code
[code]
    openclaw approvals set --file ./exec-approvals.jsonopenclaw approvals set --stdin <<'EOF'{ version: 1, defaults: { security: "full", ask: "off" } }EOFopenclaw approvals set --node <id|name|ip> --file ./exec-approvals.jsonopenclaw approvals set --gateway --file ./exec-approvals.json
[/code]

`set` akzeptiert JSON5, nicht nur striktes JSON. Verwenden Sie entweder `--file` oder `--stdin`, nicht beides.

## Beispiel „Nie nachfragen“ / YOLO

Für einen Host, der bei Exec-Genehmigungen niemals anhalten soll, setzen Sie die Standardwerte der Host-Genehmigungen auf `full` \+ `off`:

bashCopy code
[code]
    openclaw approvals set --stdin <<'EOF'{  version: 1,  defaults: {    security: "full",    ask: "off",    askFallback: "full"  }}EOF
[/code]

Node-Variante:

bashCopy code
[code]
    openclaw approvals set --node <id|name|ip> --stdin <<'EOF'{  version: 1,  defaults: {    security: "full",    ask: "off",    askFallback: "full"  }}EOF
[/code]

Dies ändert nur die **Host-Genehmigungsdatei**. Um die angeforderte OpenClaw-Richtlinie synchron zu halten, setzen Sie zusätzlich:

bashCopy code
[code]
    openclaw config set tools.exec.host gatewayopenclaw config set tools.exec.security fullopenclaw config set tools.exec.ask off
[/code]

Warum `tools.exec.host=gateway` in diesem Beispiel:

  * `host=auto` bedeutet weiterhin „Sandbox, wenn verfügbar, sonst Gateway“.
  * Bei YOLO geht es um Genehmigungen, nicht um Routing.
  * Wenn Sie Host-Exec auch dann möchten, wenn eine Sandbox konfiguriert ist, machen Sie die Host-Auswahl mit `gateway` oder `/exec host=gateway` explizit.


Das entspricht dem aktuellen YOLO-Verhalten für Host-Standards. Verschärfen Sie es, wenn Sie Genehmigungen wünschen.

Lokale Abkürzung:

bashCopy code
[code]
    openclaw exec-policy preset yolo
[/code]

Diese lokale Abkürzung aktualisiert sowohl die angeforderte lokale Konfiguration `tools.exec.*` als auch die lokalen Standardgenehmigungen gemeinsam. Sie ist in ihrer Absicht gleichwertig mit der manuellen zweistufigen Einrichtung oben, aber nur für den lokalen Rechner.

## Allowlist-Helfer

bashCopy code
[code]
    openclaw approvals allowlist add "~/Projects/**/bin/rg"openclaw approvals allowlist add --agent main --node <id|name|ip> "/usr/bin/uptime"openclaw approvals allowlist add --agent "*" "/usr/bin/uname" openclaw approvals allowlist remove "~/Projects/**/bin/rg"
[/code]

## Häufige Optionen

`get`, `set` und `allowlist add|remove` unterstützen alle:

  * `--node <id|name|ip>`
  * `--gateway`
  * gemeinsame Node-RPC-Optionen: `--url`, `--token`, `--timeout`, `--json`


Hinweise zur Zielauswahl:

  * ohne Zielflags ist die lokale Genehmigungsdatei auf dem Datenträger gemeint
  * `--gateway` zielt auf die Genehmigungsdatei des Gateway-Hosts
  * `--node` zielt auf einen Node-Host, nachdem ID, Name, IP oder ID-Präfix aufgelöst wurde


`allowlist add|remove` unterstützt außerdem:

  * `--agent <id>` (Standard ist `*`)


## Hinweise

  * `--node` verwendet denselben Resolver wie `openclaw nodes` (ID, Name, IP oder ID-Präfix).
  * `--agent` hat standardmäßig den Wert `"*"`, was für alle Agenten gilt.
  * Der Node-Host muss `system.execApprovals.get/set` bereitstellen (macOS-App oder headless Node-Host).
  * Genehmigungsdateien werden pro Host unter `~/.openclaw/exec-approvals.json` gespeichert.


## Verwandt

  * [CLI-Referenz](</de/cli>)
  * [Exec-Genehmigungen](</de/tools/exec-approvals>)


Was this useful?YesNo