---
title: App Linux
source_url: https://docs.openclaw.ai/it/platforms/linux
scraped_at: 2026-05-25
---

Gateway è completamente supportato su Linux. **Node è il runtime consigliato**. Bun non è consigliato per il Gateway (bug di WhatsApp/Telegram).

Sono previste app companion native per Linux. I contributi sono benvenuti se vuoi aiutare a realizzarne una.

## Percorso rapido per principianti (VPS)

  1. Installa Node 24 (consigliato; Node 22 LTS, attualmente `22.16+`, funziona ancora per compatibilità)
  2. `npm i -g openclaw@latest`
  3. `openclaw onboard --install-daemon`
  4. Dal tuo portatile: `ssh -N -L 18789:127.0.0.1:18789 <user>@<host>`
  5. Apri `http://127.0.0.1:18789/` e autenticati con il segreto condiviso configurato (token per impostazione predefinita; password se hai impostato `gateway.auth.mode: "password"`)


Guida completa al server Linux: [Server Linux](</it/vps>). Esempio VPS passo per passo: [exe.dev](</it/install/exe-dev>)

## Installazione

  * [Introduzione](</it/start/getting-started>)
  * [Installazione e aggiornamenti](</it/install/updating>)
  * Flussi opzionali: [Bun (sperimentale)](</it/install/bun>), [Nix](</it/install/nix>), [Docker](</it/install/docker>)


## Gateway

  * [Runbook del Gateway](</it/gateway>)
  * [Configurazione](</it/gateway/configuration>)


## Installazione del servizio Gateway (CLI)

Usa uno di questi:

CodeCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Oppure:

CodeCopy code
[code]
    openclaw gateway install
[/code]

Oppure:

CodeCopy code
[code]
    openclaw configure
[/code]

Seleziona **Servizio Gateway** quando richiesto.

Ripara/migra:

CodeCopy code
[code]
    openclaw doctor
[/code]

## Controllo di sistema (unità utente systemd)

OpenClaw installa per impostazione predefinita un servizio systemd **utente**. Usa un servizio **di sistema** per server condivisi o sempre attivi. `openclaw gateway install` e `openclaw onboard --install-daemon` generano già per te l'unità canonica corrente; scrivine una a mano solo quando hai bisogno di una configurazione personalizzata di sistema/gestore servizi. La guida completa al servizio si trova nel [runbook del Gateway](</it/gateway>).

Configurazione minima:

Crea `~/.config/systemd/user/openclaw-gateway[-<profile>].service`:

CodeCopy code
[code]
    [Unit]Description=OpenClaw Gateway (profile: <profile>, v<version>)After=network-online.targetWants=network-online.target [Service]ExecStart=/usr/local/bin/openclaw gateway --port 18789Restart=alwaysRestartSec=5TimeoutStopSec=30TimeoutStartSec=30SuccessExitStatus=0 143KillMode=control-group [Install]WantedBy=default.target
[/code]

Abilitalo:

CodeCopy code
[code]
    systemctl --user enable --now openclaw-gateway[-<profile>].service
[/code]

## Pressione sulla memoria e terminazioni OOM

Su Linux, il kernel sceglie una vittima OOM quando un cgroup di host, VM o container esaurisce la memoria. Il Gateway può essere una vittima sfavorevole perché gestisce sessioni e connessioni di canale di lunga durata. OpenClaw quindi indirizza, quando possibile, i processi figlio transitori a essere terminati prima del Gateway.

Per gli avvii di processi figlio Linux idonei, OpenClaw avvia il figlio tramite un breve wrapper `/bin/sh` che aumenta l'`oom_score_adj` del figlio stesso a `1000`, quindi esegue con `exec` il comando reale. Questa è un'operazione senza privilegi perché il figlio aumenta solo la propria probabilità di terminazione OOM.

Le superfici dei processi figlio coperte includono:

  * processi figlio di comandi gestiti dal supervisore,
  * processi figlio della shell PTY,
  * processi figlio di server stdio MCP,
  * processi browser/Chrome avviati da OpenClaw.


Il wrapper è disponibile solo su Linux e viene ignorato quando `/bin/sh` non è disponibile. Viene ignorato anche se l'ambiente del figlio imposta `OPENCLAW_CHILD_OOM_SCORE_ADJ=0`, `false`, `no` o `off`.

Per verificare un processo figlio:

bashCopy code
[code]
    cat /proc/<child-pid>/oom_score_adj
[/code]

Il valore previsto per i processi figlio coperti è `1000`. Il processo Gateway dovrebbe mantenere il suo punteggio normale, di solito `0`.

Questo non sostituisce la normale regolazione della memoria. Se un VPS o container termina ripetutamente i processi figlio, aumenta il limite di memoria, riduci la concorrenza o aggiungi controlli delle risorse più forti, come `MemoryMax=` di systemd o limiti di memoria a livello di container.

## Correlati

  * [Panoramica dell'installazione](</it/install>)
  * [Server Linux](</it/vps>)
  * [Raspberry Pi](</it/install/raspberry-pi>)


Was this useful?YesNo