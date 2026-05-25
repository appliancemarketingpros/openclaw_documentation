---
title: Persoonlijke Zalo-Plugin
source_url: https://docs.openclaw.ai/nl/plugins/zalouser
scraped_at: 2026-05-25
---

Ondersteuning voor Zalo Personal in OpenClaw via een Plugin, waarbij native `zca-js` wordt gebruikt om een normaal Zalo-gebruikersaccount te automatiseren.

## Naamgeving

De kanaal-id is `zalouser` om expliciet te maken dat dit een **persoonlijk Zalo-gebruikersaccount** automatiseert (niet-officieel). We houden `zalo` gereserveerd voor een mogelijke toekomstige officiële Zalo API-integratie.

## Waar het draait

Deze Plugin draait **binnen het Gateway-proces**.

Als u een externe Gateway gebruikt, installeer/configureer deze dan op de **machine waarop de Gateway draait** en herstart daarna de Gateway.

Er is geen externe `zca`/`openzca` CLI-binary vereist.

## Installeren

### Optie A: installeren vanuit npm

bashCopy code
[code]
    openclaw plugins install @openclaw/zalouser
[/code]

Gebruik het kale pakket om de huidige officiële releasetag te volgen. Pin een exacte versie alleen wanneer u een reproduceerbare installatie nodig hebt.

Herstart daarna de Gateway.

### Optie B: installeren vanuit een lokale map (dev)

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/zalouser-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

Herstart daarna de Gateway.

## Configuratie

Kanaalconfiguratie staat onder `channels.zalouser` (niet `plugins.entries.*`):

json5Copy code
[code]
    {  channels: {    zalouser: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

## CLI

bashCopy code
[code]
    openclaw channels login --channel zalouseropenclaw channels logout --channel zalouseropenclaw channels status --probeopenclaw message send --channel zalouser --target <threadId> --message "Hello from OpenClaw"openclaw directory peers list --channel zalouser --query "name"
[/code]

## Agent-tool

Toolnaam: `zalouser`

Acties: `send`, `image`, `link`, `friends`, `groups`, `me`, `status`

Kanaalberichtacties ondersteunen ook `react` voor berichtreacties.

## Gerelateerd

  * [Plugins bouwen](</nl/plugins/building-plugins>)
  * [ClawHub](</nl/clawhub>)


Was this useful?YesNo