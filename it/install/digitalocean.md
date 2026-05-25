---
title: DigitalOcean
source_url: https://docs.openclaw.ai/it/install/digitalocean
scraped_at: 2026-05-25
---

Esegui un Gateway OpenClaw persistente su un Droplet DigitalOcean (~$6/mese per il piano Basic da 1 GB).

DigitalOcean è il percorso VPS a pagamento più semplice. Se preferisci opzioni più economiche o gratuite:

  * [Hetzner](</it/install/hetzner>) — €3,79/mese, più core/RAM per dollaro.
  * [Oracle Cloud](</it/install/oracle>) — ARM Always Free (fino a 4 OCPU, 24 GB RAM), ma la registrazione può essere macchinosa ed è solo ARM.


## Prerequisiti

  * Account DigitalOcean ([registrazione](<https://cloud.digitalocean.com/registrations/new>))
  * Coppia di chiavi SSH (o disponibilità a usare l'autenticazione con password)
  * Circa 20 minuti


## Configurazione

* ### Crea un Droplet

  1. Accedi a [DigitalOcean](<https://cloud.digitalocean.com/>).
  2. Fai clic su **Create > Droplets**.
  3. Scegli: 
     * **Regione:** quella più vicina a te
     * **Immagine:** Ubuntu 24.04 LTS
     * **Dimensione:** Basic, Regular, 1 vCPU / 1 GB RAM / 25 GB SSD
     * **Autenticazione:** chiave SSH (consigliata) o password
  4. Fai clic su **Create Droplet** e annota l'indirizzo IP.


* ### Connettiti e installa

bashCopy code
[code]
    ssh root@YOUR_DROPLET_IP apt update && apt upgrade -y # Install Node.js 24curl -fsSL https://deb.nodesource.com/setup_24.x | bash -apt install -y nodejs # Install OpenClawcurl -fsSL https://openclaw.ai/install.sh | bash # Create the non-root user that will own OpenClaw state and services.adduser openclawusermod -aG sudo openclawloginctl enable-linger openclaw su - openclawopenclaw --version
[/code]

Usa la shell root solo per il bootstrap del sistema. Esegui i comandi OpenClaw come utente non root `openclaw`, così lo stato risiede in `/home/openclaw/.openclaw/` e il Gateway viene installato come servizio systemd di quell'utente.

* ### Esegui l'onboarding

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

La procedura guidata ti accompagna attraverso l'autenticazione del modello, la configurazione del canale, la generazione del token del gateway e l'installazione del daemon (systemd).

* ### Aggiungi swap (consigliato per Droplet da 1 GB)

bashCopy code
[code]
    fallocate -l 2G /swapfilechmod 600 /swapfilemkswap /swapfileswapon /swapfileecho '/swapfile none swap sw 0 0' >> /etc/fstab
[/code]

* ### Verifica il gateway

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### Accedi alla UI di controllo

Il gateway si associa a loopback per impostazione predefinita. Scegli una di queste opzioni.

**Opzione A: tunnel SSH (la più semplice)**

bashCopy code
[code]
    # From your local machinessh -L 18789:localhost:18789 root@YOUR_DROPLET_IP
[/code]

Quindi apri `http://localhost:18789`.

**Opzione B: Tailscale Serve**

bashCopy code
[code]
    curl -fsSL https://tailscale.com/install.sh | sudo shsudo tailscale upopenclaw config set gateway.tailscale.mode serveopenclaw gateway restart
[/code]

Quindi apri `https://<magicdns>/` da qualsiasi dispositivo sulla tua tailnet.

Tailscale Serve autentica il traffico della UI di controllo e WebSocket tramite gli header di identità della tailnet, presupponendo che l'host del gateway stesso sia attendibile. Gli endpoint API HTTP seguono comunque la normale modalità di autenticazione del gateway (token/password). Per richiedere credenziali esplicite con segreto condiviso su Serve, imposta `gateway.auth.allowTailscale: false` e usa `gateway.auth.mode: "token"` o `"password"`.

**Opzione C: associazione tailnet (senza Serve)**

bashCopy code
[code]
    openclaw config set gateway.bind tailnetopenclaw gateway restart
[/code]

Quindi apri `http://<tailscale-ip>:18789` (token richiesto).

## Persistenza e backup

Lo stato di OpenClaw risiede in:

  * `~/.openclaw/` — `openclaw.json`, `auth-profiles.json` per agente, stato di canali/provider e dati di sessione.
  * `~/.openclaw/workspace/` — l'area di lavoro dell'agente ([SOUL.md](<http://SOUL.md>), memoria, artefatti).


Questi dati sopravvivono ai riavvii del Droplet. Per creare uno snapshot portabile:

bashCopy code
[code]
    openclaw backup create
[/code]

Gli snapshot DigitalOcean eseguono il backup dell'intero Droplet; `openclaw backup create` è portabile tra host.

## Suggerimenti per 1 GB di RAM

Il Droplet da $6 ha solo 1 GB di RAM. Per mantenere tutto fluido:

  * Assicurati che il passaggio di swap sopra sia in `/etc/fstab`, così sopravvive ai riavvii.
  * Preferisci modelli basati su API (Claude, GPT) rispetto a quelli locali — l'inferenza LLM locale non entra in 1 GB.
  * Imposta `agents.defaults.model.primary` su un modello più piccolo se riscontri OOM con prompt grandi.
  * Monitora con `free -h` e `htop`.


## Risoluzione dei problemi

**Il Gateway non si avvia** \-- Esegui `openclaw doctor --non-interactive` e controlla i log con `journalctl --user -u openclaw-gateway.service -n 50`.

**Porta già in uso** \-- Esegui `lsof -i :18789` per trovare il processo, quindi arrestalo.

**Memoria esaurita** \-- Verifica che lo swap sia attivo con `free -h`. Se riscontri ancora OOM, usa modelli basati su API (Claude, GPT) invece di modelli locali, oppure passa a un Droplet da 2 GB.

## Passaggi successivi

  * [Canali](</it/channels>) \-- collega Telegram, WhatsApp, Discord e altro
  * [Configurazione del Gateway](</it/gateway/configuration>) \-- tutte le opzioni di configurazione
  * [Aggiornamento](</it/install/updating>) \-- mantieni OpenClaw aggiornato


## Correlati

  * [Panoramica dell'installazione](</it/install>)
  * [Fly.io](</it/install/fly>)
  * [Hetzner](</it/install/hetzner>)
  * [Hosting VPS](</it/vps>)


Was this useful?YesNo