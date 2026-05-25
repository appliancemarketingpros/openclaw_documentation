---
title: Oracle Cloud
source_url: https://docs.openclaw.ai/it/install/oracle
scraped_at: 2026-05-25
---

Esegui un Gateway OpenClaw persistente sul livello ARM **Always Free** di Oracle Cloud (fino a 4 OCPU, 24 GB di RAM, 200 GB di archiviazione) senza costi.

## Prerequisiti

  * Account Oracle Cloud ([registrazione](<https://www.oracle.com/cloud/free/>)) -- consulta la [guida di registrazione della community](<https://gist.github.com/rssnyder/51e3cfedd730e7dd5f4a816143b25dbd>) se incontri problemi
  * Account Tailscale (gratuito su [tailscale.com](<https://tailscale.com>))
  * Una coppia di chiavi SSH
  * Circa 30 minuti


## Configurazione

* ### Crea un'istanza OCI

  1. Accedi alla [Oracle Cloud Console](<https://cloud.oracle.com/>).
  2. Vai a **Compute > Instances > Create Instance**.
  3. Configura: 
     * **Nome:** `openclaw`
     * **Immagine:** Ubuntu 24.04 (aarch64)
     * **Shape:** `VM.Standard.A1.Flex` (Ampere ARM)
     * **OCPU:** 2 (o fino a 4)
     * **Memoria:** 12 GB (o fino a 24 GB)
     * **Volume di avvio:** 50 GB (fino a 200 GB gratuiti)
     * **Chiave SSH:** aggiungi la tua chiave pubblica
  4. Fai clic su **Create** e prendi nota dell'indirizzo IP pubblico.


* ### Connettiti e aggiorna il sistema

bashCopy code
[code]
    ssh ubuntu@YOUR_PUBLIC_IP sudo apt update && sudo apt upgrade -ysudo apt install -y build-essential
[/code]

`build-essential` è necessario per la compilazione ARM di alcune dipendenze.

* ### Configura utente e hostname

bashCopy code
[code]
    sudo hostnamectl set-hostname openclawsudo passwd ubuntusudo loginctl enable-linger ubuntu
[/code]

Abilitare linger mantiene in esecuzione i servizi utente dopo il logout.

* ### Installa Tailscale

bashCopy code
[code]
    curl -fsSL https://tailscale.com/install.sh | shsudo tailscale up --ssh --hostname=openclaw
[/code]

D'ora in poi, connettiti tramite Tailscale: `ssh ubuntu@openclaw`.

* ### Installa OpenClaw

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bashsource ~/.bashrc
[/code]

Quando viene chiesto "How do you want to hatch your bot?", seleziona **Do this later**.

* ### Configura il Gateway

Usa l'autenticazione tramite token con Tailscale Serve per un accesso remoto sicuro.

bashCopy code
[code]
    openclaw config set gateway.bind loopbackopenclaw config set gateway.auth.mode tokenopenclaw doctor --generate-gateway-tokenopenclaw config set gateway.tailscale.mode serveopenclaw config set gateway.trustedProxies '["127.0.0.1"]' systemctl --user restart openclaw-gateway.service
[/code]

`gateway.trustedProxies=["127.0.0.1"]` qui serve solo per la gestione dell'IP inoltrato/client locale del proxy Tailscale Serve locale. **Non** è `gateway.auth.mode: "trusted-proxy"`. Le route del visualizzatore diff mantengono un comportamento fail-closed in questa configurazione: le richieste raw `127.0.0.1` al visualizzatore senza header proxy inoltrati possono restituire `Diff not found`. Usa `mode=file` / `mode=both` per gli allegati, oppure abilita intenzionalmente i visualizzatori remoti e imposta `plugins.entries.diffs.config.viewerBaseUrl` (o passa un proxy `baseUrl`) se hai bisogno di link del visualizzatore condivisibili.

* ### Blocca la sicurezza della VCN

Blocca tutto il traffico tranne Tailscale al perimetro di rete:

  1. Vai a **Networking > Virtual Cloud Networks** nella console OCI.
  2. Fai clic sulla tua VCN, poi su **Security Lists > Default Security List**.
  3. **Rimuovi** tutte le regole di ingresso tranne `0.0.0.0/0 UDP 41641` (Tailscale).
  4. Mantieni le regole di uscita predefinite (consenti tutto il traffico in uscita).


Questo blocca SSH sulla porta 22, HTTP, HTTPS e tutto il resto al perimetro di rete. Da questo momento puoi connetterti solo tramite Tailscale.

* ### Verifica

bashCopy code
[code]
    openclaw --versionsystemctl --user status openclaw-gateway.servicetailscale serve statuscurl http://localhost:18789
[/code]

Accedi alla Control UI da qualsiasi dispositivo sulla tua tailnet:

CodeCopy code
[code]
    https://openclaw.<tailnet-name>.ts.net/
[/code]

Sostituisci `<tailnet-name>` con il nome della tua tailnet (visibile in `tailscale status`).

## Verifica la postura di sicurezza

Con la VCN bloccata (solo UDP 41641 aperta) e il Gateway associato al loopback, il traffico pubblico è bloccato al perimetro di rete e l'accesso amministrativo è solo tramite tailnet. Questo elimina la necessità di diversi passaggi tradizionali di hardening dei VPS:

Passaggio tradizionale | Necessario? | Perché  
---|---|---  
Firewall UFW | No | La VCN blocca il traffico prima che raggiunga l'istanza.  
fail2ban | No | La porta 22 è bloccata nella VCN; non c'è superficie di attacco brute-force.  
Rafforzamento di sshd | No | Tailscale SSH non usa sshd.  
Disabilitare l'accesso root | No | Tailscale autentica tramite identità tailnet, non tramite utenti di sistema.  
Autenticazione solo con chiave SSH | No | Stesso motivo: l'identità tailnet sostituisce le chiavi SSH di sistema.  
Rafforzamento IPv6 | Di solito no | Dipende dalle impostazioni VCN/subnet; verifica cosa è effettivamente assegnato/esposto.  
  
Ancora consigliato:

  * `chmod 700 ~/.openclaw` per limitare i permessi dei file di credenziali.
  * `openclaw security audit` per un controllo della postura specifico di OpenClaw.
  * `sudo apt update && sudo apt upgrade` regolare per le patch del sistema operativo.
  * Controlla periodicamente i dispositivi nella [console di amministrazione Tailscale](<https://login.tailscale.com/admin>).


Comandi rapidi di verifica:

bashCopy code
[code]
    # Confirm no public ports are listeningsudo ss -tlnp | grep -v '127.0.0.1\|::1' # Verify Tailscale SSH is activetailscale status | grep -q 'offers: ssh' && echo "Tailscale SSH active" # Optional: disable sshd entirely once Tailscale SSH is confirmed workingsudo systemctl disable --now ssh
[/code]

## Note su ARM

Il livello Always Free è ARM (`aarch64`). La maggior parte delle funzionalità di OpenClaw funziona senza problemi; un piccolo numero di binari nativi richiede build ARM:

  * Node.js, Telegram, WhatsApp (Baileys): JavaScript puro, nessun problema.
  * La maggior parte dei pacchetti npm con codice nativo: artefatti precompilati `linux-arm64` disponibili.
  * Helper CLI opzionali (ad es. binari Go/Rust distribuiti dalle Skills): controlla che esista una release `aarch64` / `linux-arm64` prima dell'installazione.


Verifica l'architettura con `uname -m` (dovrebbe stampare `aarch64`). Per i binari senza build ARM, installa dai sorgenti o ignorali.

## Persistenza e backup

Lo stato di OpenClaw si trova in:

  * `~/.openclaw/` — `openclaw.json`, `auth-profiles.json` per agente, stato di canali/provider e dati di sessione.
  * `~/.openclaw/workspace/` — lo spazio di lavoro dell'agente ([SOUL.md](<http://SOUL.md>), memoria, artefatti).


Questi dati sopravvivono ai riavvii. Per creare uno snapshot portabile:

bashCopy code
[code]
    openclaw backup create
[/code]

## Fallback: tunnel SSH

Se Tailscale Serve non funziona, usa un tunnel SSH dalla tua macchina locale:

bashCopy code
[code]
    ssh -L 18789:127.0.0.1:18789 ubuntu@openclaw
[/code]

Poi apri `http://localhost:18789`.

## Risoluzione dei problemi

**La creazione dell'istanza fallisce ("Out of capacity")** \-- Le istanze ARM del livello gratuito sono molto richieste. Prova un dominio di disponibilità diverso o riprova durante le ore di minore traffico.

**Tailscale non si connette** \-- Esegui `sudo tailscale up --ssh --hostname=openclaw --reset` per riautenticarti.

**Il Gateway non si avvia** \-- Esegui `openclaw doctor --non-interactive` e controlla i log con `journalctl --user -u openclaw-gateway.service -n 50`.

**Problemi con binari ARM** \-- La maggior parte dei pacchetti npm funziona su ARM64. Per i binari nativi, cerca release `linux-arm64` o `aarch64`. Verifica l'architettura con `uname -m`.

## Prossimi passi

  * [Canali](</it/channels>) \-- collega Telegram, WhatsApp, Discord e altro
  * [Configurazione del Gateway](</it/gateway/configuration>) \-- tutte le opzioni di configurazione
  * [Aggiornamento](</it/install/updating>) \-- mantieni OpenClaw aggiornato


## Correlati

  * [Panoramica dell'installazione](</it/install>)
  * [GCP](</it/install/gcp>)
  * [Hosting VPS](</it/vps>)


Was this useful?YesNo