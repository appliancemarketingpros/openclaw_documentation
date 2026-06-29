---
title: Upstash Box
source_url: https://docs.openclaw.ai/it/install/upstash
scraped_at: 2026-06-29
---

InstallHosting

Esegui un Gateway OpenClaw persistente su Upstash Box, un ambiente Linux gestito con supporto del ciclo di vita keep-alive.

Usa un tunnel SSH per l'accesso al dashboard. Non esporre direttamente la porta del Gateway a Internet pubblico.

## Prerequisiti

  * Account Upstash
  * Upstash Box keep-alive
  * Client SSH sulla tua macchina locale


## Creare un Box

Crea un Box keep-alive nella Console Upstash. Prendi nota dell'ID del Box, ad esempio `right-flamingo-14486`, e della chiave API del tuo Box.

Upstash mantiene la procedura dettagliata corrente per OpenClaw Box in [Configurazione di OpenClaw](<https://upstash.com/docs/box/guides/openclaw-setup>).

## Connettersi con un tunnel SSH

Inoltra la porta del dashboard OpenClaw alla tua macchina locale. Usa la chiave API del tuo Box come password SSH quando richiesto:

bashCopy code
[code]
    ssh -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

Le opzioni keepalive riducono le interruzioni del tunnel inattivo durante l'onboarding.

## Installare OpenClaw

All'interno del Box:

bashCopy code
[code]
    sudo npm install -g openclaw
[/code]

## Eseguire l'onboarding

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Segui le istruzioni. Copia l'URL del dashboard e il token al termine dell'onboarding.

## Avviare il Gateway

Configura il Gateway per la rete del Box e avvialo in background:

bashCopy code
[code]
    openclaw config set gateway.bind lannohup openclaw gateway > gateway.log 2>&1 &
[/code]

Con il tunnel SSH attivo, apri localmente l'URL del dashboard:

textCopy code
[code]
    http://127.0.0.1:18789/#token=<your-token>
[/code]

## Riavvio automatico

Imposta questo comando come script di inizializzazione del Box, in modo che il Gateway si riavvii quando il Box si avvia:

bashCopy code
[code]
    nohup openclaw gateway > gateway.log 2>&1 &
[/code]

## Risoluzione dei problemi

Se SSH si blocca durante l'onboarding, riconnettiti con una configurazione SSH pulita e keepalive:

bashCopy code
[code]
    ssh -F /dev/null -o ControlMaster=no -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

Questo evita impostazioni locali `~/.ssh/config` obsolete e mantiene attivo il tunnel durante periodi di inattività della rete.

## Correlati

  * [Accesso remoto](</it/gateway/remote>)
  * [Sicurezza del Gateway](</it/gateway/security>)
  * [Aggiornare OpenClaw](</it/install/updating>)


Was this useful?YesNo

Open issue