---
title: Railway
source_url: https://docs.openclaw.ai/it/install/railway
scraped_at: 2026-05-25
---

# Railway

Distribuisci OpenClaw su Railway con un template one-click e accedivi tramite la web Control UI. Questo è il percorso più semplice "senza terminale sul server": Railway esegue il Gateway al posto tuo.

## Checklist rapida (nuovi utenti)

  1. Fai clic su **Deploy on Railway** (sotto).
  2. Aggiungi un **Volume** montato in `/data`.
  3. Imposta le **Variables** richieste (almeno `OPENCLAW_GATEWAY_PORT` e `OPENCLAW_GATEWAY_TOKEN`).
  4. Abilita **HTTP Proxy** sulla porta `8080`.
  5. Apri `https://<your-railway-domain>/openclaw` e connettiti usando il secret condiviso configurato. Questo template usa `OPENCLAW_GATEWAY_TOKEN` per impostazione predefinita; se lo sostituisci con l’autenticazione tramite password, usa invece quella password.


## Deploy one-click

[ Deploy on Railway ](<https://railway.com/deploy/clawdbot-railway-template>)

Dopo il deploy, trova il tuo URL pubblico in **Railway → your service → Settings → Domains**.

Railway farà una delle seguenti cose:

  * ti assegnerà un dominio generato (spesso `https://<something>.up.railway.app`), oppure
  * userà il tuo dominio personalizzato se ne hai collegato uno.


Poi apri:

  * `https://<your-railway-domain>/openclaw` — Control UI


## Cosa ottieni

  * Gateway OpenClaw ospitato + Control UI
  * Archiviazione persistente tramite Railway Volume (`/data`) così `openclaw.json`, `auth-profiles.json` per agente, stato di canali/provider, sessioni e workspace sopravvivono ai redeploy


## Impostazioni Railway richieste

### Rete pubblica

Abilita **HTTP Proxy** per il servizio.

  * Porta: `8080`


### Volume (obbligatorio)

Collega un volume montato in:

  * `/data`


### Variabili

Imposta queste variabili sul servizio:

  * `OPENCLAW_GATEWAY_PORT=8080` (obbligatorio — deve corrispondere alla porta in Public Networking)
  * `OPENCLAW_GATEWAY_TOKEN` (obbligatorio; trattalo come un secret admin)
  * `OPENCLAW_STATE_DIR=/data/.openclaw` (consigliato)
  * `OPENCLAW_WORKSPACE_DIR=/data/workspace` (consigliato)


## Collega un canale

Usa la Control UI in `/openclaw` oppure esegui `openclaw onboard` tramite la shell di Railway per istruzioni sulla configurazione del canale:

  * [Telegram](</it/channels/telegram>) (il più rapido — serve solo un token bot)
  * [Discord](</it/channels/discord>)
  * [Tutti i canali](</it/channels>)


## Backup e migrazione

Esporta stato, configurazione, profili di autenticazione e workspace:

bashCopy code
[code]
    openclaw backup create
[/code]

Questo crea un archivio di backup portabile con lo stato di OpenClaw più qualsiasi workspace configurato. Vedi [Backup](</it/cli/backup>) per i dettagli.

## Passaggi successivi

  * Configura i canali di messaggistica: [Channels](</it/channels>)
  * Configura il Gateway: [Gateway configuration](</it/gateway/configuration>)
  * Mantieni OpenClaw aggiornato: [Updating](</it/install/updating>)


Was this useful?YesNo