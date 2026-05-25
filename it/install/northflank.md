---
title: Northflank
source_url: https://docs.openclaw.ai/it/install/northflank
scraped_at: 2026-05-25
---

# Northflank

Distribuisci OpenClaw su Northflank con un template one-click e accedivi tramite la web Control UI. Questo è il percorso più semplice “senza terminale sul server”: Northflank esegue il Gateway al posto tuo.

## Come iniziare

  1. Fai clic su [Deploy OpenClaw](<https://northflank.com/stacks/deploy-openclaw>) per aprire il template.
  2. Crea un [account su Northflank](<https://app.northflank.com/signup>) se non ne hai già uno.
  3. Fai clic su **Deploy OpenClaw now**.
  4. Imposta la variabile d'ambiente richiesta: `OPENCLAW_GATEWAY_TOKEN` (usa un valore casuale forte).
  5. Fai clic su **Deploy stack** per compilare ed eseguire il template OpenClaw.
  6. Attendi il completamento del deployment, poi fai clic su **View resources**.
  7. Apri il servizio OpenClaw.
  8. Apri l'URL pubblico di OpenClaw su `/openclaw` e connettiti usando il secret condiviso configurato. Questo template usa `OPENCLAW_GATEWAY_TOKEN` per impostazione predefinita; se lo sostituisci con autenticazione tramite password, usa invece quella password.


## Cosa ottieni

  * Gateway OpenClaw ospitato + Control UI
  * Archiviazione persistente tramite Volume Northflank (`/data`) così `openclaw.json`, `auth-profiles.json` per agente, stato di canale/provider, sessioni e workspace sopravvivono ai redeploy


## Collegare un canale

Usa la Control UI su `/openclaw` oppure esegui `openclaw onboard` via SSH per le istruzioni di configurazione del canale:

  * [Telegram](</it/channels/telegram>) (il più rapido — basta un token bot)
  * [Discord](</it/channels/discord>)
  * [Tutti i canali](</it/channels>)


## Passi successivi

  * Configura i canali di messaggistica: [Canali](</it/channels>)
  * Configura il Gateway: [Configurazione del Gateway](</it/gateway/configuration>)
  * Mantieni OpenClaw aggiornato: [Aggiornamento](</it/install/updating>)


Was this useful?YesNo