---
title: Plugin personale Zalo
source_url: https://docs.openclaw.ai/it/plugins/zalouser
scraped_at: 2026-05-25
---

Supporto a Zalo Personal per OpenClaw tramite un Plugin, usando `zca-js` nativo per automatizzare un normale account utente Zalo.

## Denominazione

L'id del canale è `zalouser` per rendere esplicito che automatizza un **account utente Zalo personale** (non ufficiale). Manteniamo `zalo` riservato per una potenziale futura integrazione ufficiale con l'API Zalo.

## Dove viene eseguito

Questo Plugin viene eseguito **all'interno del processo Gateway**.

Se usi un Gateway remoto, installalo/configuralo sulla **macchina che esegue il Gateway** , quindi riavvia il Gateway.

Non è richiesto alcun binario CLI esterno `zca`/`openzca`.

## Installazione

### Opzione A: installazione da npm

bashCopy code
[code]
    openclaw plugins install @openclaw/zalouser
[/code]

Usa il pacchetto senza versione per seguire il tag di rilascio ufficiale corrente. Fissa una versione esatta solo quando hai bisogno di un'installazione riproducibile.

Riavvia poi il Gateway.

### Opzione B: installazione da una cartella locale (dev)

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/zalouser-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

Riavvia poi il Gateway.

## Configurazione

La configurazione del canale si trova in `channels.zalouser` (non in `plugins.entries.*`):

json5Copy code
[code]
    {  channels: {    zalouser: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

## CLI

bashCopy code
[code]
    openclaw channels login --channel zalouseropenclaw channels logout --channel zalouseropenclaw channels status --probeopenclaw message send --channel zalouser --target <threadId> --message "Hello from OpenClaw"openclaw directory peers list --channel zalouser --query "name"
[/code]

## Strumento agente

Nome dello strumento: `zalouser`

Azioni: `send`, `image`, `link`, `friends`, `groups`, `me`, `status`

Le azioni sui messaggi del canale supportano anche `react` per le reazioni ai messaggi.

## Correlati

  * [Creazione di Plugin](</it/plugins/building-plugins>)
  * [ClawHub](</it/clawhub>)


Was this useful?YesNo