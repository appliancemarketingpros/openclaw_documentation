---
title: Plugin personnel Zalo
source_url: https://docs.openclaw.ai/fr/plugins/zalouser
scraped_at: 2026-05-25
---

Prise en charge de Zalo Personal pour OpenClaw via un Plugin, en utilisant `zca-js` natif pour automatiser un compte utilisateur Zalo normal.

## Nommage

L’id du canal est `zalouser` afin d’indiquer explicitement que cela automatise un **compte utilisateur Zalo personnel** (non officiel). Nous réservons `zalo` à une éventuelle future intégration officielle de l’API Zalo.

## Où il s’exécute

Ce Plugin s’exécute **dans le processus Gateway**.

Si vous utilisez un Gateway distant, installez-le/configurez-le sur la **machine exécutant le Gateway** , puis redémarrez le Gateway.

Aucun binaire CLI externe `zca`/`openzca` n’est requis.

## Installation

### Option A : installer depuis npm

bashCopy code
[code]
    openclaw plugins install @openclaw/zalouser
[/code]

Utilisez le package nu pour suivre le tag de version officielle actuelle. Épinglez une version exacte uniquement lorsque vous avez besoin d’une installation reproductible.

Redémarrez ensuite le Gateway.

### Option B : installer depuis un dossier local (dev)

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/zalouser-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

Redémarrez ensuite le Gateway.

## Configuration

La configuration du canal se trouve sous `channels.zalouser` (et non `plugins.entries.*`) :

json5Copy code
[code]
    {  channels: {    zalouser: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

## CLI

bashCopy code
[code]
    openclaw channels login --channel zalouseropenclaw channels logout --channel zalouseropenclaw channels status --probeopenclaw message send --channel zalouser --target <threadId> --message "Hello from OpenClaw"openclaw directory peers list --channel zalouser --query "name"
[/code]

## Outil d’agent

Nom de l’outil : `zalouser`

Actions : `send`, `image`, `link`, `friends`, `groups`, `me`, `status`

Les actions de message de canal prennent également en charge `react` pour les réactions aux messages.

## Articles associés

  * [Créer des Plugins](</fr/plugins/building-plugins>)
  * [ClawHub](</fr/clawhub>)


Was this useful?YesNo