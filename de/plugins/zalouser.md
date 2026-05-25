---
title: Persönliches Zalo-Plugin
source_url: https://docs.openclaw.ai/de/plugins/zalouser
scraped_at: 2026-05-25
---

Unterstützung für Zalo Personal in OpenClaw über ein Plugin, wobei natives `zca-js` verwendet wird, um ein normales Zalo-Benutzerkonto zu automatisieren.

## Benennung

Die Channel-ID ist `zalouser`, um ausdrücklich klarzumachen, dass dies ein **persönliches Zalo-Benutzerkonto** automatisiert (inoffiziell). Wir halten `zalo` für eine mögliche zukünftige offizielle Integration der Zalo-API reserviert.

## Ausführungsort

Dieses Plugin läuft **innerhalb des Gateway-Prozesses**.

Wenn Sie einen Remote-Gateway verwenden, installieren/konfigurieren Sie es auf dem **Rechner, auf dem der Gateway läuft** , und starten Sie anschließend den Gateway neu.

Es ist keine externe `zca`/`openzca`-CLI-Binärdatei erforderlich.

## Installation

### Option A: Installation aus npm

bashCopy code
[code]
    openclaw plugins install @openclaw/zalouser
[/code]

Verwenden Sie das reine Paket, um dem aktuellen offiziellen Release-Tag zu folgen. Pinnen Sie eine exakte Version nur dann, wenn Sie eine reproduzierbare Installation benötigen.

Starten Sie den Gateway anschließend neu.

### Option B: Installation aus einem lokalen Ordner (Entwicklung)

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/zalouser-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

Starten Sie den Gateway anschließend neu.

## Konfiguration

Die Channel-Konfiguration befindet sich unter `channels.zalouser` (nicht `plugins.entries.*`):

json5Copy code
[code]
    {  channels: {    zalouser: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

## CLI

bashCopy code
[code]
    openclaw channels login --channel zalouseropenclaw channels logout --channel zalouseropenclaw channels status --probeopenclaw message send --channel zalouser --target <threadId> --message "Hello from OpenClaw"openclaw directory peers list --channel zalouser --query "name"
[/code]

## Agent-Tool

Tool-Name: `zalouser`

Aktionen: `send`, `image`, `link`, `friends`, `groups`, `me`, `status`

Channel-Nachrichtenaktionen unterstützen außerdem `react` für Nachrichtenreaktionen.

## Verwandte Themen

  * [Plugins erstellen](</de/plugins/building-plugins>)
  * [ClawHub](</de/clawhub>)


Was this useful?YesNo